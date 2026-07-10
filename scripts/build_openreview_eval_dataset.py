#!/usr/bin/env python3
"""
Build an evaluation dataset from OpenReview papers, reviews, and rebuttals.

The output is intentionally compatible with eval/papers.json: a dictionary keyed
by paper id, where each value contains paper metadata and a reviews list with
strengths / weaknesses. This script adds extra fields such as rebuttal text and
OpenReview URLs.

Examples:
    python scripts/build_openreview_eval_dataset.py \
        --output eval/LetsTalk_papers_Qwen.json \
        --download-pdfs

    DASHSCOPE_API_KEY=... python scripts/build_openreview_eval_dataset.py \
        --use-llm-segmentation \
        --per-category 50 \
        --venues ICLR:2025 ICML:2025 NeurIPS:2025
"""

from __future__ import annotations

import argparse
import contextlib
import http.client
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Optional


OPENREVIEW_BASE_URL = "https://openreview.net"
OPENREVIEW_REQUEST_DELAY_SECONDS = 1.0
PDF_DOWNLOAD_ATTEMPTS = 3
DEFAULT_LLM_MODEL = "qwen3.6-plus"
_LAST_OPENREVIEW_REQUEST_AT = 0.0

DEFAULT_VENUES: dict[str, dict[int, str]] = {
    "ICLR": {
        2025: "ICLR.cc/2025/Conference",
        2024: "ICLR.cc/2024/Conference",
        2023: "ICLR.cc/2023/Conference",
    },
    "ICML": {
        2025: "ICML.cc/2025/Conference",
        2024: "ICML.cc/2024/Conference",
        2023: "ICML.cc/2023/Conference",
    },
    "NeurIPS": {
        2025: "NeurIPS.cc/2025/Conference",
        2024: "NeurIPS.cc/2024/Conference",
        2023: "NeurIPS.cc/2023/Conference",
    },
}


@dataclass(frozen=True)
class VenueSpec:
    conference: str
    year: int
    venue_id: str


def import_openreview() -> Any:
    try:
        import openreview  # type: ignore
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency: openreview-py. Install it with "
            "`pip install openreview-py` or `pip install -r requirements.txt`."
        ) from exc
    return openreview


def note_id(note: Any) -> str:
    return getattr(note, "id", None) or getattr(note, "forum", "")


def note_forum(note: Any) -> str:
    return getattr(note, "forum", None) or note_id(note)


def get_content(note: Any) -> dict[str, Any]:
    content = getattr(note, "content", None) or {}
    normalized = {}
    for key, value in content.items():
        if isinstance(value, dict) and "value" in value:
            normalized[key] = value["value"]
        else:
            normalized[key] = value
    return normalized


def as_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return "\n".join(as_text(item) for item in value if as_text(item))
    if isinstance(value, dict):
        if "value" in value:
            return as_text(value["value"])
        return json.dumps(value, ensure_ascii=False)
    return str(value).strip()


def as_float(value: Any) -> Optional[float]:
    text = as_text(value)
    if not text:
        return None
    match = re.search(r"-?\d+(?:\.\d+)?", text)
    return float(match.group(0)) if match else None


def slugify(text: str, fallback: str = "paper") -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return slug[:80] or fallback


def openreview_url(forum: str) -> str:
    return f"{OPENREVIEW_BASE_URL}/forum?id={forum}"


def parse_venue_specs(raw_specs: list[str]) -> list[VenueSpec]:
    specs = []
    for raw in raw_specs:
        parts = raw.split(":", 2)
        if len(parts) == 3:
            conference, year_text, venue_id = parts
        elif len(parts) == 2:
            conference, year_text = parts
            venue_id = DEFAULT_VENUES.get(conference, {}).get(int(year_text))
            if not venue_id:
                raise SystemExit(f"No default venue id for {raw}; pass CONF:YEAR:VENUE_ID.")
        else:
            raise SystemExit(f"Invalid venue spec {raw!r}; use CONF:YEAR or CONF:YEAR:VENUE_ID.")
        specs.append(VenueSpec(conference=conference, year=int(year_text), venue_id=venue_id))
    return specs


def get_client(openreview: Any) -> Any:
    username = os.getenv("OPENREVIEW_USERNAME")
    password = os.getenv("OPENREVIEW_PASSWORD")
    if username and password:
        return openreview.api.OpenReviewClient(
            baseurl="https://api2.openreview.net",
            username=username,
            password=password,
        )
    return openreview.api.OpenReviewClient(baseurl="https://api2.openreview.net")


def is_openreview_challenge_required_error(exc: Exception) -> bool:
    text = str(exc)
    return "ChallengeRequiredError" in text or "challengeUrl" in text


def openreview_challenge_message() -> str:
    return (
        "OpenReview API challenge required. Set OPENREVIEW_USERNAME and "
        "OPENREVIEW_PASSWORD, or complete OpenReview's challenge in an accepted session, "
        "then rerun the command."
    )


def get_all_notes(client: Any, **kwargs: Any) -> list[Any]:
    global _LAST_OPENREVIEW_REQUEST_AT
    for attempt in range(6):
        try:
            elapsed = time.monotonic() - _LAST_OPENREVIEW_REQUEST_AT
            if elapsed < OPENREVIEW_REQUEST_DELAY_SECONDS:
                time.sleep(OPENREVIEW_REQUEST_DELAY_SECONDS - elapsed)
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                if hasattr(client, "get_all_notes"):
                    notes = list(client.get_all_notes(**kwargs))
                else:
                    notes = list(client.get_notes(**kwargs))
            _LAST_OPENREVIEW_REQUEST_AT = time.monotonic()
            return notes
        except Exception as exc:
            _LAST_OPENREVIEW_REQUEST_AT = time.monotonic()
            message = str(exc)
            if "RateLimitError" not in message and "429" not in message and "Too many requests" not in message:
                raise
            match = re.search(r"try again in (\d+) seconds", message, re.IGNORECASE)
            wait_seconds = int(match.group(1)) + 5 if match else min(90, 15 * (attempt + 1))
            print(f"Rate limited by OpenReview; sleeping {wait_seconds}s before retrying...")
            time.sleep(wait_seconds)
    raise RuntimeError(f"OpenReview request failed after repeated rate-limit retries: {kwargs}")


def fetch_submissions(client: Any, venue: VenueSpec) -> list[Any]:
    attempts = [
        {"invitation": f"{venue.venue_id}/-/Submission"},
        {"content": {"venueid": venue.venue_id}},
    ]
    last_error = None
    for kwargs in attempts:
        try:
            notes = get_all_notes(client, **kwargs)
        except Exception as exc:  # OpenReview raises several custom types.
            last_error = exc
            continue
        if notes:
            return notes
    raise RuntimeError(f"Could not fetch submissions for {venue.venue_id}: {last_error}")


def dedupe_notes(*note_groups: Iterable[Any]) -> list[Any]:
    notes = []
    seen = set()
    for group in note_groups:
        for note in group:
            key = note_id(note) or id(note)
            if key in seen:
                continue
            seen.add(key)
            notes.append(note)
    return notes


def fetch_forum_notes(client: Any, forum: str) -> list[Any]:
    forum_notes = get_all_notes(client, forum=forum)
    try:
        reply_notes = get_all_notes(client, replyto=forum)
    except TypeError:
        reply_notes = []
    except Exception as exc:
        message = str(exc)
        if "unexpected keyword" not in message and "Invalid value for query parameter replyto" not in message:
            raise
        reply_notes = []
    return dedupe_notes(forum_notes, reply_notes)


def fetch_decision_notes(client: Any, venue: VenueSpec) -> dict[str, str]:
    decision_by_forum = {}
    invitations = [
        f"{venue.venue_id}/-/Decision",
        f"{venue.venue_id}/-/Paper_Decision",
        f"{venue.venue_id}/-/Acceptance_Decision",
        f"{venue.venue_id}/-/Final_Decision",
    ]
    for invitation in invitations:
        try:
            notes = get_all_notes(client, invitation=invitation)
        except Exception as exc:
            print(f"Decision-note lookup skipped for {invitation}: {exc}")
            continue
        for note in notes:
            forum = note_forum(note)
            text = decision_text(note)
            if forum and text:
                decision_by_forum[forum] = text
        if decision_by_forum:
            break
    return decision_by_forum


OFFICIAL_REVIEW_INVITATION_RE = r"(?:^|/)-/(?:official[_ -]?review|review)(?:\d+)?$"
FINAL_DECISION_INVITATION_RE = (
    r"(?:^|/)-/(?:decision|paper[_ -]?decision|acceptance[_ -]?decision|final[_ -]?decision)(?:$|/)"
)
NON_REVIEW_INVITATION_RE = (
    r"(?:^|/)-/[^/]*(?:comment|rebuttal|response|decision|recommendation|meta[_ -]?review)[^/]*(?:$|/)"
)
REVIEW_SIGNAL_KEYS = {
    "confidence",
    "numerical_score",
    "overall_assessment",
    "overall_recommendation",
    "quality",
    "rating",
    "recommendation",
    "reviewer_confidence",
    "score",
    "soundness",
}
REVIEW_BODY_KEYS = {
    "claims_and_evidence",
    "detailed_feedback",
    "detailed_feedback_to_authors",
    "experimental_designs_or_analyses",
    "main_review",
    "methods_and_evaluation_criteria",
    "paper_strengths",
    "paper_summary",
    "paper_weaknesses",
    "reasons_to_accept",
    "reasons_to_reject",
    "review",
    "strength_and_weaknesses",
    "strengths",
    "strengths_and_weaknesses",
    "summary",
    "summary_of_strengths",
    "summary_of_weaknesses",
    "theoretical_claims",
    "weaknesses",
}


def has_invitation(note: Any, pattern: str) -> bool:
    invitations = list(getattr(note, "invitations", None) or [])
    invitation = getattr(note, "invitation", None)
    if invitation:
        invitations.append(invitation)
    return any(re.search(pattern, inv, re.IGNORECASE) for inv in invitations)


def has_reviewer_signature_or_invitation(note: Any) -> bool:
    values = [*list(getattr(note, "signatures", None) or []), *list(getattr(note, "invitations", None) or [])]
    invitation = getattr(note, "invitation", None)
    if invitation:
        values.append(invitation)
    return bool(re.search(r"reviewer|anonreviewer", " ".join(values), re.IGNORECASE))


def has_author_signature(note: Any) -> bool:
    return bool(re.search(r"author", " ".join(getattr(note, "signatures", None) or []), re.IGNORECASE))


def is_official_review(note: Any) -> bool:
    if has_invitation(note, OFFICIAL_REVIEW_INVITATION_RE):
        return True
    if has_invitation(note, NON_REVIEW_INVITATION_RE) or has_author_signature(note):
        return False
    content = get_content(note)
    keys = {canonical_field_name(key) for key in content}
    has_review_body = bool(keys & REVIEW_BODY_KEYS)
    has_review_signal = bool(keys & REVIEW_SIGNAL_KEYS)
    if not has_review_body and not has_review_signal:
        return False
    if is_decision(note):
        return False
    if has_review_body and has_review_signal:
        return True
    return has_reviewer_signature_or_invitation(note) and has_review_body


def is_decision(note: Any) -> bool:
    if has_invitation(note, FINAL_DECISION_INVITATION_RE):
        return True
    if has_invitation(note, OFFICIAL_REVIEW_INVITATION_RE):
        return False
    content = get_content(note)
    keys = {canonical_field_name(key) for key in content}
    return bool(keys & {"decision", "final_decision"})


def is_author_rebuttal(note: Any) -> bool:
    invitations = getattr(note, "invitations", None) or []
    invitation = getattr(note, "invitation", None)
    if invitation:
        invitations = [*invitations, invitation]
    invitations = " ".join(invitations)
    if re.search(r"author|rebuttal|response|comment", invitations, re.IGNORECASE):
        signatures = " ".join(getattr(note, "signatures", None) or [])
        if re.search(r"author", signatures, re.IGNORECASE):
            return True
    signatures = " ".join(getattr(note, "signatures", None) or [])
    return bool(re.search(r"author", signatures, re.IGNORECASE) and not is_official_review(note))


def decision_text(note: Any) -> str:
    content = get_content(note)
    candidates = [
        content.get("decision"),
        content.get("Decision"),
        content.get("recommendation"),
        content.get("Recommendation"),
        content.get("final_decision"),
        content.get("Final Decision"),
        content.get("venue"),
    ]
    return " ".join(as_text(candidate) for candidate in candidates if as_text(candidate))


def paper_decision(submission: Any, forum_notes: list[Any]) -> str:
    content = get_content(submission)
    candidates = [content.get("decision"), content.get("Decision"), content.get("venue")]
    candidates.extend(decision_text(note) for note in forum_notes if is_decision(note))
    return " ".join(as_text(candidate) for candidate in candidates if as_text(candidate))


def submission_decision(submission: Any) -> str:
    content = get_content(submission)
    candidates = [
        content.get("decision"),
        content.get("Decision"),
        content.get("venue"),
        content.get("venueid"),
        content.get("Venue"),
    ]
    return " ".join(as_text(candidate) for candidate in candidates if as_text(candidate))


ORAL_ACCEPTANCE_MARKER_RE = re.compile(
    r"\boral\b",
    re.IGNORECASE,
)

ANY_ACCEPTANCE_MARKER_RE = re.compile(
    r"\b(?:accept(?:ed)?|oral|spotlight|poster|notable|award)\b",
    re.IGNORECASE,
)

REJECTION_MARKER_RE = re.compile(
    r"\b(?:reject(?:ed|ion)?|withdrawn|desk\s+reject(?:ed|ion)?)\b",
    re.IGNORECASE,
)


def classify_decision(text: str) -> Optional[str]:
    normalized = text.lower()
    if not normalized:
        return None
    if REJECTION_MARKER_RE.search(normalized):
        return "reject"
    if ORAL_ACCEPTANCE_MARKER_RE.search(normalized):
        return "accept_oral"
    return None


def classify_accept_reject_decision(text: str) -> Optional[str]:
    normalized = text.lower()
    if not normalized:
        return None
    if REJECTION_MARKER_RE.search(normalized):
        return "reject"
    if ANY_ACCEPTANCE_MARKER_RE.search(normalized):
        return "accept"
    return None


def collection_category_from_decision(text: str) -> Optional[str]:
    normalized = text.lower()
    if not normalized:
        return None
    if REJECTION_MARKER_RE.search(normalized):
        return "reject"
    if ORAL_ACCEPTANCE_MARKER_RE.search(normalized):
        return "accept_oral"
    if ANY_ACCEPTANCE_MARKER_RE.search(normalized):
        return "accept"
    return None


def likely_reject_from_submission_metadata(submission: Any, venue: VenueSpec) -> bool:
    content = get_content(submission)
    decision_text = submission_decision(submission)
    if classify_decision(decision_text):
        return False

    venueid = as_text(content.get("venueid") or content.get("venue_id") or content.get("Venue ID"))
    venue_text = as_text(content.get("venue") or content.get("Venue"))
    normalized_venue_text = venue_text.lower()
    if ANY_ACCEPTANCE_MARKER_RE.search(normalized_venue_text):
        return False
    if venueid == venue.venue_id:
        return True
    conference = venue.conference.lower()
    year = str(venue.year)
    return bool(
        conference in normalized_venue_text
        and ("submitted" in normalized_venue_text or year in normalized_venue_text)
    )


def get_title(submission: Any) -> str:
    content = get_content(submission)
    return as_text(content.get("title") or content.get("Title") or "Untitled")


def get_pdf_url(submission: Any) -> Optional[str]:
    content = get_content(submission)
    pdf_value = as_text(content.get("pdf") or content.get("PDF"))
    if pdf_value:
        if pdf_value.startswith("http"):
            return pdf_value
        if pdf_value.startswith("/"):
            return f"{OPENREVIEW_BASE_URL}{pdf_value}"
    forum = note_forum(submission)
    return f"{OPENREVIEW_BASE_URL}/pdf?id={forum}" if forum else None


def download_pdf(url: str, destination: Path, sleep_seconds: float = 0.0) -> bool:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and destination.stat().st_size > 0:
        return True

    last_error: Optional[Exception] = None
    for attempt in range(1, PDF_DOWNLOAD_ATTEMPTS + 1):
        try:
            with urllib.request.urlopen(url, timeout=60) as response:
                data = response.read()
            if not data:
                raise ValueError("empty PDF response")
            destination.write_bytes(data)
            if sleep_seconds:
                time.sleep(sleep_seconds)
            return True
        except (urllib.error.URLError, TimeoutError, OSError, http.client.HTTPException, ValueError) as exc:
            last_error = exc
            if attempt < PDF_DOWNLOAD_ATTEMPTS:
                time.sleep(min(10.0, 1.5 * attempt))

    print(
        f"Warning: failed to download PDF {url} after {PDF_DOWNLOAD_ATTEMPTS} attempts: {last_error}",
        file=sys.stderr,
    )
    return False


STRUCTURED_STRENGTH_KEYS = [
    "strengths",
    "Strengths",
    "paper_strengths",
    "Paper Strengths",
    "summary_of_strengths",
    "Summary Of Strengths",
    "Main Strengths",
    "Other Strengths",
]

STRUCTURED_WEAKNESS_KEYS = [
    "weaknesses",
    "Weaknesses",
    "paper_weaknesses",
    "Paper Weaknesses",
    "summary_of_weaknesses",
    "Summary Of Weaknesses",
    "Main Weaknesses",
    "Other Weaknesses",
]

COMBINED_STRENGTH_WEAKNESS_KEYS = [
    "strengths_and_weaknesses",
    "Strengths And Weaknesses",
    "Strengths and Weaknesses",
    "strength_and_weaknesses",
    "Strength And Weaknesses",
    "other_strengths_and_weaknesses",
    "Other Strengths And Weaknesses",
    "Other Strengths and Weaknesses",
]

SUBSTANTIVE_REVIEW_TEXT_KEYS = [
    "claims_and_evidence",
    "Claims And Evidence",
    "methods_and_evaluation_criteria",
    "Methods And Evaluation Criteria",
    "theoretical_claims",
    "Theoretical Claims",
    "experimental_designs_or_analyses",
    "Experimental Designs Or Analyses",
    "relation_to_broader_scientific_literature",
    "Relation To Broader Scientific Literature",
    "essential_references_not_discussed",
    "Essential References Not Discussed",
]

REVIEW_TEXT_KEYS = [
    "summary",
    "Summary",
    "main_review",
    "Main Review",
    "review",
    "Review",
    "comment",
    "Comment",
    "comments",
    "Comments",
    *STRUCTURED_STRENGTH_KEYS,
    *STRUCTURED_WEAKNESS_KEYS,
    *COMBINED_STRENGTH_WEAKNESS_KEYS,
    *SUBSTANTIVE_REVIEW_TEXT_KEYS,
]

SEGMENTATION_REVIEW_TEXT_KEYS = [
    "main_review",
    "Main Review",
    "review",
    "Review",
    "comment",
    "Comment",
    "comments",
    "Comments",
    *STRUCTURED_STRENGTH_KEYS,
    *STRUCTURED_WEAKNESS_KEYS,
    *COMBINED_STRENGTH_WEAKNESS_KEYS,
    "claims_and_evidence",
    "Claims And Evidence",
    "methods_and_evaluation_criteria",
    "Methods And Evaluation Criteria",
    "theoretical_claims",
    "Theoretical Claims",
    "experimental_designs_or_analyses",
    "Experimental Designs Or Analyses",
]

DIRECT_SEGMENTATION_TEXT_KEYS = [
    *STRUCTURED_STRENGTH_KEYS,
    *STRUCTURED_WEAKNESS_KEYS,
    *COMBINED_STRENGTH_WEAKNESS_KEYS,
]

SEGMENTATION_INCLUDE_KEYWORD_RE = re.compile(
    r"(?:"
    r"review|comment|feedback|critique|assessment|evaluation|justification|"
    r"strength|weakness|concern|limitation|drawback|shortcoming|"
    r"merit|positive|negative|pro|con|"
    r"reason(?:s)?_(?:to_)?(?:accept|reject)|accept(?:ance)?_reason|reject(?:ion)?_reason|"
    r"claim|evidence|method|experiment|analysis|theor|correct|valid|"
    r"sound|quality|clarity|significance|originality|novelty|contribution|"
    r"presentation|reproduc|empirical|technical|impact|"
    r"main|overall|summary_of_strength|summary_of_weakness"
    r")",
    re.IGNORECASE,
)

SEGMENTATION_EXCLUDE_KEYWORD_RE = re.compile(
    r"(?:"
    r"abstract|author_response|author_rebuttal|availability|bib(?:liography)?|citation|code_of_conduct|"
    r"compliance|conflict|consent|decision|ethic|"
    r"format|id$|identifier|license|metadata|paper_id|pdf|"
    r"question|rating|recommendation|reference|response|rebuttal|"
    r"reviewer_(?:confidence|expertise|id|identity|name|qualification)|"
    r"score|submission_checklist|supplement|title"
    r")",
    re.IGNORECASE,
)

REBUTTAL_TEXT_KEYS = [
    "rebuttal",
    "Rebuttal",
    "response",
    "Response",
    "author_response",
    "Author Response",
    "comment",
    "Comment",
    "comments",
    "Comments",
]

IGNORED_REVIEW_TEXT_KEYS = {
    "rating",
    "confidence",
    "recommendation",
    "decision",
    "reviewer",
    "reviewer_id",
    "review_id",
    "pdf",
    "questions",
    "questions_for_authors",
    "soundness",
    "presentation",
    "contribution",
    "quality",
    "clarity",
    "significance",
    "originality",
    "overall_recommendation",
    "overall_assessment",
    "other_comments_or_suggestions",
    "limitations",
    "flag_for_ethics_review",
    "ethical_concerns",
    "paper_formatting_concerns",
    "code_of_conduct",
    "code_of_conduct_acknowledgement",
    "responsible_reviewing_acknowledgement",
    "mandatory_acknowledgement",
    "final_justification",
}

PLACEHOLDER_SEGMENT_TEXTS = {
    "n/a",
    "na",
    "none",
    "not applicable",
    "nil",
    "see above",
    "see summary",
    "no comment",
    "no comments",
    "no further comment",
    "no further comments",
    "nothing else",
    "affirmed",
    "yes",
    "no",
}

NON_SUBSTANTIVE_SEGMENT_LABELS = {
    "ask",
    "asks",
    "cons",
    "details",
    "major",
    "minor",
    "pros",
    "ref",
    "reference",
    "references",
    "source",
    "sources",
    "strenght",
    "strenghts",
    "strength",
    "strengths",
    "typo",
    "typos",
    "weakness",
    "weaknesses",
}
REFERENCE_SEGMENT_LABELS = {
    "bibliography",
    "citation",
    "citations",
    "ref",
    "refs",
    "reference",
    "references",
    "related_work_references",
}
ALWAYS_IGNORED_SEGMENT_FIELD_LABELS = {
    "acknowledgement",
    "acknowledgements",
    "author_response",
    "availability",
    "checklist",
    "code_of_conduct",
    "code_of_conduct_acknowledgement",
    "comment_to_area_chair",
    "comment_to_program_committee",
    "compliance",
    "confidential_comment",
    "confidential_comments",
    "conflict_of_interest",
    "data_availability",
    "decision",
    "ethical_concerns",
    "ethics",
    "final_justification",
    "flag_for_ethics_review",
    "funding",
    "mandatory_acknowledgement",
    "metadata",
    "other_comments_or_suggestions",
    "paper_formatting_concerns",
    "questions",
    "questions_for_authors",
    "rating",
    "recommendation",
    "reviewer_confidence",
    "reviewer_expertise",
    "responsible_reviewing_acknowledgement",
    "response",
    "rebuttal",
    "reviewer",
    "reviewer_id",
    "review_id",
    "submission_checklist",
    "supplementary_material",
    *REFERENCE_SEGMENT_LABELS,
}
RUBRIC_SEGMENT_FIELD_LABELS = {
    "clarity",
    "confidence",
    "contribution",
    "limitations",
    "originality",
    "presentation",
    "quality",
    "significance",
    "soundness",
}
GENERIC_RUBRIC_VALUES = {
    "affirmed",
    "fair",
    "good",
    "high",
    "low",
    "medium",
    "moderate",
    "n/a",
    "na",
    "no",
    "none",
    "not applicable",
    "poor",
    "strong",
    "very good",
    "weak",
    "yes",
}
HTML_SPACER_SEGMENT_TEXTS = {"&nbsp;", "&nbsp", "&#160;", "<br>", "<br/>", "<br />"}
MARKUP_ONLY_SEGMENT_RE = re.compile(r"^[\s*_#>\.\-\u2013\u2014]+$")
URL_ONLY_SEGMENT_RE = re.compile(r"^https?://\S+$", re.IGNORECASE)
QUESTION_REFERENCE_ONLY_RE = re.compile(r"^(?:see\s+)?q(?:uestion)?\s*#?\d+[.)]?$", re.IGNORECASE)
TRAILING_QUESTION_REFERENCE_RE = re.compile(r"\s+(?:see\s+)?q(?:uestion)?\s*#?\d+[.)]?$", re.IGNORECASE)
SEGMENT_ENUMERATOR_RE = re.compile(r"^[SW]\d+\.?$", re.IGNORECASE)
STANDALONE_OUTLINE_LABEL_RE = re.compile(
    r"^(?:[*_`#\s>]*)?(?:\(?\d+\)?[.)]?|[A-Z][.)]|[SW]\d+\.?)(?:[*_`#\s>]*)$",
    re.IGNORECASE,
)
LEADING_SEGMENT_ENUMERATOR_PREFIX_RE = re.compile(
    r"^(?:\(?\d+\)?[.)]+|[A-Z][.)]|[SW]\d+[.)]+)\s*(?=[A-Z\"'])",
    re.IGNORECASE,
)
LEADING_BULLET_RE = re.compile(r"^\s*(?:[-*•]|\d+[.)]+)\s*(.+)$")
GENERIC_SEGMENT_HEADING_PREFIX_RE = re.compile(
    r"^(?:(?:minor|major|main|smaller)|"
    r"(?:(?:minor|major|main|smaller)\s+)?"
    r"(?:points?|comments?|concerns?|limitations?|remarks?|issues?|questions?|strengths?|weakness(?:es)?))"
    r"\s*:\s+",
    re.IGNORECASE,
)
SEGMENT_OUTLINE_HEADING_RE = re.compile(r"^(?:[*_`#\s>]*)(?:[SW]\d+)\.\s+\S.{0,80}$", re.IGNORECASE)
NON_SUBSTANTIVE_SECTION_HEADING_RE = re.compile(
    r"^(?:[*_`#\s>]*)?"
    r"(?:(?:minor|major|main|smaller)\s+)?"
    r"(?:points?|comments?|concerns?|limitations?|remarks?|issues?|questions?|"
    r"strengths?|weakness(?:es)?|figure\s*\d+(?:\s*\+\s*\d+)?|"
    r"implementation\s+details|experimental\s+validation|literature\s+positioning|"
    r"comparison\s+to\s+[A-Za-z0-9_-]+)"
    r"\s*:?(?:[*_`#\s>]*)$",
    re.IGNORECASE,
)
REFERENCE_CITATION_RE = re.compile(
    r"^\s*(?:\[\d+\]|\d+\.)\s+.{8,}(?:\b(?:19|20)\d{2}\b|arxiv|proceedings|conference|journal|doi)",
    re.IGNORECASE,
)
BIBLIOGRAPHY_FRAGMENT_RE = re.compile(
    r"(?:"
    r"^\s*\[[Rr]?\d+\]\s+[A-Z][A-Za-z]+,\s+[A-Z]\.?|"
    r"^\s*(?:PMLR(?:[.,]?\s*(?:19|20)\d{2}[.)]?)?|Springer|ISSN\s+\S+|Vol\.\s*\d+.*(?:19|20)\d{2})\.?$|"
    r"^\s*[A-Z][A-Za-z]+,\s+[A-Z]\.?(?:,.*)?$"
    r")",
    re.IGNORECASE,
)
ROMAN_SEGMENT_ENUMERATOR_RE = re.compile(
    r"^(?:i|ii|iii|iv|v|vi|vii|viii|ix|x)\.?$",
    re.IGNORECASE,
)

SECTION_HEADER_RE = re.compile(
    r"^\s*(?:#+\s*)?("
    r"strengths?|weakness(?:es)?|concerns?|"
    r"paper[_\s-]+strengths?|paper[_\s-]+weakness(?:es)?|"
    r"summary[_\s-]+of[_\s-]+strengths?|summary[_\s-]+of[_\s-]+weakness(?:es)?|"
    r"main[_\s-]+strengths?|main[_\s-]+weakness(?:es)?|"
    r"other[_\s-]+strengths?(?:[_\s-]+and[_\s-]+weakness(?:es)?)?|"
    r"strengths?[_\s-]+and[_\s-]+weakness(?:es)?|"
    r"claims[_\s-]+and[_\s-]+evidence|"
    r"methods[_\s-]+and[_\s-]+evaluation[_\s-]+criteria|"
    r"theoretical[_\s-]+claims|"
    r"experimental[_\s-]+designs?[_\s-]+or[_\s-]+analyses|"
    r"relation[_\s-]+to[_\s-]+broader[_\s-]+scientific[_\s-]+literature|"
    r"essential[_\s-]+references[_\s-]+not[_\s-]+discussed|"
    r"summary(?:\s+of\s+the\s+review)?|main\s+review|review|comments?|"
    r"references?|bibliography|citations?|related[_\s-]+work[_\s-]+references?|"
    r"questions?|soundness|presentation|contribution|quality|clarity|significance|originality|"
    r"checklists?|compliance|confidential[_\s-]+comments?|conflict[_\s-]+of[_\s-]+interest|"
    r"data[_\s-]+availability|ethical[_\s-]+concerns?|ethics|metadata|paper[_\s-]+formatting[_\s-]+concerns?|"
    r"reviewer[_\s-]+(?:confidence|expertise|qualification)|supplementary[_\s-]+material|"
    r"flag[_\s-]+for[_\s-]+ethics[_\s-]+review|"
    r"code[_\s-]+of[_\s-]+conduct(?:[_\s-]+acknowledgement)?|"
    r"(?:responsible[_\s-]+reviewing[_\s-]+)?acknowledgements?|mandatory[_\s-]+acknowledgement|"
    r"rating|confidence|recommendation|decision"
    r")\s*:?\s*$",
    re.IGNORECASE | re.MULTILINE,
)

WEAKNESS_CUE_RE = re.compile(
    r"(?:^|(?<=[.!?])\s+|\n+)"
    r"(?:(?:regarding|as\s+for|for)\s+(?:the\s+)?|the\s+)?"
    r"(?:(?:main|major|minor|potential)\s+)?"
    r"(?:weakness(?:es)?|limitation(?:s)?|concern(?:s)?|drawback(?:s)?|shortcoming(?:s)?)"
    r"(?:\s+(?:include|includes|are|is)\b|[:,;])\s*",
    re.IGNORECASE,
)
INLINE_STRENGTH_WEAKNESS_HEADER_RE = re.compile(
    r"(?:^|(?<=[.!?])\s+|\n+)\s*(?:#+\s*)?"
    r"(?P<label>strengths?|weakness(?:es)?|limitations?|concerns?|drawbacks?|shortcomings?)"
    r"\s*:\s*",
    re.IGNORECASE,
)


def canonical_field_name(key: str) -> str:
    return re.sub(r"[\s-]+", "_", key.strip().lower())


def is_section_header_label(text: str) -> bool:
    return "\n" not in text.strip() and bool(SECTION_HEADER_RE.match(text.strip()))


def split_leading_field_label(text: str) -> tuple[str, str] | None:
    first_line = str(text or "").strip().splitlines()[0] if str(text or "").strip() else ""
    first_line = standalone_segment_label(first_line)
    match = re.match(r"^([a-z0-9_ /\-]{2,80})\s*:\s*(.+)$", first_line, re.IGNORECASE)
    if not match:
        return None
    return canonical_field_name(match.group(1)), match.group(2).strip()


def is_generic_rubric_value(text: str) -> bool:
    normalized = re.sub(r"\s+", " ", str(text or "").strip().lower())
    normalized = normalized.strip(" .:;,-_")
    if normalized in GENERIC_RUBRIC_VALUES:
        return True
    if re.fullmatch(r"\d+(?:\.\d+)?(?:\s*/\s*\d+(?:\.\d+)?)?", normalized):
        return True
    return bool(re.fullmatch(r"\d+(?:\.\d+)?\s*:\s*\w+(?:\s+\w+)?", normalized))


def strip_segment_field_prefix(text: str) -> str:
    stripped = re.sub(r"\s+", " ", str(text or "").strip())
    for _ in range(3):
        label_and_body = split_leading_field_label(stripped)
        if not label_and_body:
            return stripped
        label, body = label_and_body
        if label in ALWAYS_IGNORED_SEGMENT_FIELD_LABELS:
            return ""
        if label in RUBRIC_SEGMENT_FIELD_LABELS:
            if is_generic_rubric_value(body):
                return ""
            stripped = body
            continue
        return stripped
    return stripped


def normalize_segment_text(text: str) -> str:
    stripped = re.sub(r"\s+", " ", str(text or "").strip())
    if not stripped:
        return ""
    if QUESTION_REFERENCE_ONLY_RE.fullmatch(stripped):
        return ""
    if stripped.startswith(">"):
        stripped = re.sub(r"(^|\s)>\s*", " ", stripped)
    stripped = stripped.replace("**", "").replace("__", "")
    stripped = re.sub(r"\s+", " ", stripped).strip()
    if QUESTION_REFERENCE_ONLY_RE.fullmatch(stripped):
        return ""
    for _ in range(3):
        previous = stripped
        stripped = LEADING_SEGMENT_ENUMERATOR_PREFIX_RE.sub("", stripped).strip()
        stripped = GENERIC_SEGMENT_HEADING_PREFIX_RE.sub("", stripped).strip()
        stripped = strip_segment_field_prefix(stripped).strip()
        stripped = TRAILING_QUESTION_REFERENCE_RE.sub("", stripped).strip()
        if stripped == previous:
            break
    return stripped


def is_placeholder_segment_text(text: str) -> bool:
    normalized = re.sub(r"\s+", " ", str(text or "").strip().lower())
    normalized = normalized.strip(" .:;,-_")
    return normalized in PLACEHOLDER_SEGMENT_TEXTS


def standalone_segment_label(text: str) -> str:
    label = str(text or "").strip()
    for _ in range(4):
        previous = label
        if len(label) >= 4 and label.startswith("**") and label.endswith("**"):
            label = label[2:-2].strip()
        if len(label) >= 4 and label.startswith("__") and label.endswith("__"):
            label = label[2:-2].strip()
        if len(label) >= 2 and label.startswith("*") and label.endswith("*"):
            label = label[1:-1].strip()
        if len(label) >= 2 and label.startswith("_") and label.endswith("_"):
            label = label[1:-1].strip()
        if label == previous:
            break
    label = re.sub(r"\s+", " ", label).strip()
    return label.rstrip(":\uFF1A").strip().lower()


def is_non_substantive_segment_text(text: str) -> bool:
    stripped = str(text or "").strip()
    if not stripped:
        return True
    label_and_body = split_leading_field_label(stripped)
    if label_and_body:
        label, body = label_and_body
        if label in ALWAYS_IGNORED_SEGMENT_FIELD_LABELS:
            return True
        if label in RUBRIC_SEGMENT_FIELD_LABELS and is_generic_rubric_value(body):
            return True
    if stripped.lower() in HTML_SPACER_SEGMENT_TEXTS:
        return True
    if URL_ONLY_SEGMENT_RE.fullmatch(stripped):
        return True
    if QUESTION_REFERENCE_ONLY_RE.fullmatch(stripped):
        return True
    if MARKUP_ONLY_SEGMENT_RE.fullmatch(stripped):
        return True
    if STANDALONE_OUTLINE_LABEL_RE.fullmatch(stripped):
        return True
    if NON_SUBSTANTIVE_SECTION_HEADING_RE.fullmatch(stripped):
        return True
    if is_section_header_label(stripped):
        return True
    if is_placeholder_segment_text(stripped):
        return True
    if REFERENCE_CITATION_RE.search(stripped):
        return True
    if BIBLIOGRAPHY_FRAGMENT_RE.search(stripped):
        return True
    if SEGMENT_OUTLINE_HEADING_RE.fullmatch(stripped) and len(stripped.split()) <= 6:
        return True
    if standalone_segment_label(stripped) in NON_SUBSTANTIVE_SEGMENT_LABELS:
        return True
    if SEGMENT_ENUMERATOR_RE.fullmatch(stripped):
        return True
    return bool(ROMAN_SEGMENT_ENUMERATOR_RE.fullmatch(stripped))


def split_bullets(text: str) -> list[str]:
    text = text.strip()
    if not text:
        return []
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    bullet_items = []
    current_bullet = []
    saw_bullet = False
    for line in lines:
        match = LEADING_BULLET_RE.match(line)
        if match:
            if current_bullet:
                cleaned = normalize_segment_text(" ".join(current_bullet))
                if cleaned and not is_non_substantive_segment_text(cleaned):
                    bullet_items.append(cleaned)
            saw_bullet = True
            current_bullet = [match.group(1).strip()]
        elif saw_bullet:
            current_bullet.append(line)
    if saw_bullet:
        if current_bullet:
            cleaned = normalize_segment_text(" ".join(current_bullet))
            if cleaned and not is_non_substantive_segment_text(cleaned):
                bullet_items.append(cleaned)
        return bullet_items
    chunks = re.split(r"\n{2,}|(?<=[.!?])\s+(?=[A-Z])", text)
    chunk_items = []
    for chunk in chunks:
        cleaned = normalize_segment_text(chunk)
        if cleaned and not is_non_substantive_segment_text(cleaned):
            chunk_items.append(cleaned)
    return chunk_items


def section_blocks(text: str) -> dict[str, str]:
    matches = list(SECTION_HEADER_RE.finditer(text))
    blocks: dict[str, str] = {}
    for idx, match in enumerate(matches):
        header = match.group(1).lower()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        blocks[header] = text[start:end].strip()
    return blocks


def is_strength_header(header: str) -> bool:
    canonical = canonical_field_name(header)
    return "strength" in canonical


def is_weakness_header(header: str) -> bool:
    canonical = canonical_field_name(header)
    return any(token in canonical for token in ("weakness", "limitation", "concern", "drawback", "shortcoming"))


def append_default_segment(
    strengths: list[str],
    weaknesses: list[str],
    text: str,
    default_section: str | None,
) -> None:
    if default_section == "strengths":
        strengths.extend(split_bullets(text))
    elif default_section == "weaknesses":
        weaknesses.extend(split_bullets(text))


def split_inline_strengths_weaknesses(
    text: str,
    default_section: str | None = None,
) -> tuple[list[str], list[str]]:
    matches = list(INLINE_STRENGTH_WEAKNESS_HEADER_RE.finditer(text))
    strengths: list[str] = []
    weaknesses: list[str] = []
    if not matches:
        if default_section == "strengths":
            match = WEAKNESS_CUE_RE.search(text)
            if match:
                strength_text = text[: match.start()].strip()
                weakness_text = WEAKNESS_CUE_RE.sub("", text[match.start() :], count=1).strip()
                return split_bullets(strength_text), split_bullets(weakness_text)
        append_default_segment(strengths, weaknesses, text, default_section)
        return dedupe_preserve_order(strengths), dedupe_preserve_order(weaknesses)

    append_default_segment(strengths, weaknesses, text[: matches[0].start()].strip(), default_section)
    for idx, match in enumerate(matches):
        header = match.group("label")
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        block = text[start:end].strip()
        if is_strength_header(header):
            strengths.extend(split_bullets(block))
        elif is_weakness_header(header):
            weaknesses.extend(split_bullets(block))
    return dedupe_preserve_order(strengths), dedupe_preserve_order(weaknesses)


def segment_overlap_key(text: str) -> str:
    normalized = normalize_segment_text(as_text(text))
    return re.sub(r"\s+", " ", normalized).strip().lower()


def dedupe_segment_sides(strengths: Iterable[str], weaknesses: Iterable[str]) -> tuple[list[str], list[str]]:
    deduped_strengths = dedupe_preserve_order(strengths)
    deduped_weaknesses = dedupe_preserve_order(weaknesses)
    weakness_keys = {key for item in deduped_weaknesses if (key := segment_overlap_key(item))}
    filtered_strengths = [item for item in deduped_strengths if segment_overlap_key(item) not in weakness_keys]
    return filtered_strengths, deduped_weaknesses


def split_combined_strengths_weaknesses(text: str) -> tuple[list[str], list[str]]:
    blocks = section_blocks(text)
    strengths = []
    weaknesses = []
    for header, block in blocks.items():
        if is_strength_header(header) and is_weakness_header(header):
            block_strengths, block_weaknesses = split_inline_strengths_weaknesses(block, default_section="strengths")
            strengths.extend(block_strengths)
            weaknesses.extend(block_weaknesses)
        elif is_strength_header(header):
            block_strengths, block_weaknesses = split_inline_strengths_weaknesses(block, default_section="strengths")
            strengths.extend(block_strengths)
            weaknesses.extend(block_weaknesses)
        elif is_weakness_header(header):
            block_strengths, block_weaknesses = split_inline_strengths_weaknesses(block, default_section="weaknesses")
            strengths.extend(block_strengths)
            weaknesses.extend(block_weaknesses)
    if strengths or weaknesses:
        return dedupe_segment_sides(strengths, weaknesses)

    strengths, weaknesses = split_inline_strengths_weaknesses(text, default_section="strengths")
    return dedupe_segment_sides(strengths, weaknesses)


def deterministic_segment(content: dict[str, Any], raw_review: str) -> tuple[list[str], list[str]]:
    strengths = []
    weaknesses = []
    for key in STRUCTURED_STRENGTH_KEYS:
        if key in content:
            field_strengths, field_weaknesses = split_inline_strengths_weaknesses(
                as_text(content[key]),
                default_section="strengths",
            )
            strengths.extend(field_strengths)
            weaknesses.extend(field_weaknesses)
    for key in STRUCTURED_WEAKNESS_KEYS:
        if key in content:
            field_strengths, field_weaknesses = split_inline_strengths_weaknesses(
                as_text(content[key]),
                default_section="weaknesses",
            )
            strengths.extend(field_strengths)
            weaknesses.extend(field_weaknesses)
    for key in COMBINED_STRENGTH_WEAKNESS_KEYS:
        if key in content:
            combined_strengths, combined_weaknesses = split_combined_strengths_weaknesses(as_text(content[key]))
            strengths.extend(combined_strengths)
            weaknesses.extend(combined_weaknesses)

    blocks = section_blocks(raw_review)
    for header, block in blocks.items():
        if is_strength_header(header) and is_weakness_header(header):
            block_strengths, block_weaknesses = split_inline_strengths_weaknesses(block, default_section="strengths")
            strengths.extend(block_strengths)
            weaknesses.extend(block_weaknesses)
        elif is_strength_header(header):
            block_strengths, block_weaknesses = split_inline_strengths_weaknesses(block, default_section="strengths")
            strengths.extend(block_strengths)
            weaknesses.extend(block_weaknesses)
        elif is_weakness_header(header):
            block_strengths, block_weaknesses = split_inline_strengths_weaknesses(block, default_section="weaknesses")
            strengths.extend(block_strengths)
            weaknesses.extend(block_weaknesses)

    return dedupe_segment_sides(strengths, weaknesses)


def is_ignored_segmentation_header(text: str) -> bool:
    ignored_keys = {canonical_field_name(key) for key in SUBSTANTIVE_REVIEW_TEXT_KEYS}
    ignored_keys.update(ALWAYS_IGNORED_SEGMENT_FIELD_LABELS)
    ignored_keys.update(REFERENCE_SEGMENT_LABELS)
    ignored_keys.update(
        canonical_field_name(key)
        for key in (
            "questions",
            "questions_for_authors",
            "soundness",
            "presentation",
            "contribution",
            "rating",
            "confidence",
            "recommendation",
            "decision",
        )
    )
    return canonical_field_name(text.rstrip(":")) in ignored_keys


def starts_ignored_review_section(line: str) -> bool:
    stripped = str(line or "").strip()
    if not stripped:
        return False
    if is_section_header_label(stripped) and is_ignored_segmentation_header(stripped):
        return True
    label_and_body = split_leading_field_label(stripped)
    if not label_and_body:
        return False
    label, _ = label_and_body
    return label in ALWAYS_IGNORED_SEGMENT_FIELD_LABELS or label in REFERENCE_SEGMENT_LABELS


def strip_ignored_review_sections(text: str) -> str:
    lines = str(text or "").splitlines()
    kept = []
    skipping = False
    for line in lines:
        stripped = line.strip()
        if starts_ignored_review_section(stripped):
            skipping = True
            continue
        if stripped and is_section_header_label(stripped):
            skipping = False
        if not skipping:
            kept.append(line)
    return "\n".join(kept).strip()


def previous_nonempty_line(source_text: str, index: int) -> str:
    for line in reversed(source_text[:index].splitlines()):
        if line.strip():
            return line.strip()
    return ""


def next_nonempty_line(source_text: str, index: int) -> str:
    for line in source_text[index:].splitlines():
        if line.strip():
            return line.strip()
    return ""


def previous_section_header(source_text: str, index: int) -> str:
    for line in reversed(source_text[:index].splitlines()):
        stripped = line.strip()
        if not stripped:
            continue
        if starts_ignored_review_section(stripped) or is_section_header_label(stripped):
            return stripped
    return ""


def source_has_clean_excerpt(text: str, source_text: str) -> bool:
    words = text.split()
    if not words:
        return False
    pattern = r"\s+".join(re.escape(word) for word in words)
    for match in re.finditer(pattern, source_text, re.IGNORECASE):
        if starts_ignored_review_section(previous_section_header(source_text, match.start())):
            continue
        previous_line = previous_nonempty_line(source_text, match.start())
        if starts_ignored_review_section(previous_line):
            continue
        header_boundary = is_section_header_label(previous_line)
        next_line = next_nonempty_line(source_text, match.end())
        prefix = source_text[: match.start()]
        suffix = source_text[match.end() :]
        stripped_prefix = prefix.rstrip()
        stripped_suffix = suffix.lstrip()
        previous = prefix[-1:] if prefix else ""
        previous_nonspace = stripped_prefix[-1:] if stripped_prefix else ""
        following = stripped_suffix[:1]
        raw_following = suffix[:1]
        text_has_terminal_boundary = text.rstrip().endswith((".", "!", "?", ":", ";"))
        previous_ok = (
            header_boundary
            or not previous_nonspace
            or previous in "\n\r"
            or previous_nonspace in "-–—*•([{`'\""
            or previous_nonspace in ".!?:;"
        )
        following_ok = (
            is_section_header_label(next_line)
            or not stripped_suffix
            or raw_following in "\n\r"
            or following in ")]}`'\""
            or (raw_following.isspace() and text_has_terminal_boundary)
            or following in ".!?:;"
        )
        if previous_ok and following_ok:
            return True
    return False


def source_supported_items(items: Iterable[str], source_text: str) -> list[str]:
    supported = []
    for item in items:
        for candidate in split_bullets(as_text(item)):
            raw_text = strip_segment_field_prefix(candidate)
            text = normalize_segment_text(raw_text)
            if (
                text
                and not is_non_substantive_segment_text(text)
                and (source_has_clean_excerpt(raw_text, source_text) or source_has_clean_excerpt(text, source_text))
            ):
                supported.append(text)
    return dedupe_preserve_order(supported)


def dedupe_preserve_order(items: Iterable[str]) -> list[str]:
    seen = set()
    out = []
    for item in items:
        normalized = re.sub(r"\s+", " ", item).strip()
        if normalized and normalized.lower() not in seen:
            seen.add(normalized.lower())
            out.append(normalized)
    return out


def content_text_parts(content: dict[str, Any], preferred: list[str], include_labels: bool) -> list[str]:
    parts = []
    seen = set()
    for preferred_key in preferred:
        canonical = canonical_field_name(preferred_key)
        if canonical in seen:
            continue
        for key, value in content.items():
            if canonical_field_name(key) != canonical:
                continue
            text = as_text(value)
            if text:
                parts.append(f"{key}\n{text}" if include_labels else text)
            seen.add(canonical)
            break
    return parts


def strip_leading_field_label(text: str, labels: Iterable[str]) -> str:
    label_set = {canonical_field_name(label) for label in labels}
    lines = text.strip().splitlines()
    while lines and canonical_field_name(lines[0].rstrip(":")) in label_set:
        lines = lines[1:]
        while lines and not lines[0].strip():
            lines = lines[1:]
    return "\n".join(lines).strip()


def build_raw_review(content: dict[str, Any]) -> str:
    return "\n\n".join(content_text_parts(content, REVIEW_TEXT_KEYS, include_labels=True)).strip()


def is_ignored_review_text_field(key: str) -> bool:
    canonical = canonical_field_name(key)
    ignored = {canonical_field_name(item) for item in IGNORED_REVIEW_TEXT_KEYS}
    ignored.update(ALWAYS_IGNORED_SEGMENT_FIELD_LABELS)
    ignored.update(REFERENCE_SEGMENT_LABELS)
    return canonical in ignored or bool(SEGMENTATION_EXCLUDE_KEYWORD_RE.search(canonical))


def has_substantive_segmentation_text(value: Any) -> bool:
    text = as_text(value)
    if not text:
        return False
    if "\n" not in text and is_non_substantive_segment_text(text):
        return False
    words = re.findall(r"[A-Za-z0-9]+", text)
    if len(words) >= 6:
        return True
    return "\n" in text or bool(re.search(r"[.!?].+[.!?]", text, re.DOTALL))


def is_likely_segmentation_content_field(key: str, value: Any) -> bool:
    if is_ignored_review_text_field(key):
        return False
    canonical = canonical_field_name(key)
    if any(canonical == canonical_field_name(item) for item in DIRECT_SEGMENTATION_TEXT_KEYS):
        text = as_text(value)
        return bool(text) and not is_non_substantive_segment_text(text)
    if not has_substantive_segmentation_text(value):
        return False
    if any(canonical == canonical_field_name(item) for item in SEGMENTATION_REVIEW_TEXT_KEYS):
        return True
    return bool(SEGMENTATION_INCLUDE_KEYWORD_RE.search(canonical))


def segmentation_content_text_parts(content: dict[str, Any], include_labels: bool) -> list[str]:
    parts = []
    seen = set()
    for preferred_key in SEGMENTATION_REVIEW_TEXT_KEYS:
        canonical = canonical_field_name(preferred_key)
        if canonical in seen:
            continue
        for key, value in content.items():
            if canonical_field_name(key) != canonical:
                continue
            if is_likely_segmentation_content_field(key, value):
                text = as_text(value)
                parts.append(f"{key}\n{text}" if include_labels else text)
            seen.add(canonical)
            break

    for key, value in content.items():
        canonical = canonical_field_name(key)
        if canonical in seen:
            continue
        if is_likely_segmentation_content_field(key, value):
            text = as_text(value)
            parts.append(f"{key}\n{text}" if include_labels else text)
            seen.add(canonical)

    if parts:
        return parts

    for key, value in content.items():
        canonical = canonical_field_name(key)
        if canonical in seen or is_ignored_review_text_field(key):
            continue
        if has_substantive_segmentation_text(value):
            text = as_text(value)
            parts.append(f"{key}\n{text}" if include_labels else text)
            seen.add(canonical)
    return parts


def build_segmentation_review_text(content: dict[str, Any]) -> str:
    parts = segmentation_content_text_parts(content, include_labels=True)
    cleaned_parts = [strip_ignored_review_sections(part) for part in parts]
    return "\n\n".join(part for part in cleaned_parts if part).strip()


def has_any_content_key(content: dict[str, Any], keys: Iterable[str]) -> bool:
    canonical_keys = {canonical_field_name(key) for key in keys}
    return any(canonical_field_name(key) in canonical_keys for key in content)


def needs_llm_segmentation(content: dict[str, Any], strengths: list[str], weaknesses: list[str]) -> bool:
    if not strengths or not weaknesses:
        return True
    if has_any_content_key(content, STRUCTURED_STRENGTH_KEYS) and has_any_content_key(
        content,
        STRUCTURED_WEAKNESS_KEYS,
    ):
        return False
    return has_any_content_key(content, COMBINED_STRENGTH_WEAKNESS_KEYS) or bool(strengths or weaknesses)


def build_rebuttal_text(content: dict[str, Any]) -> str:
    parts = [
        strip_leading_field_label(part, REBUTTAL_TEXT_KEYS)
        for part in content_text_parts(content, REBUTTAL_TEXT_KEYS, include_labels=False)
    ]
    if not parts:
        for key, value in content.items():
            if canonical_field_name(key) in IGNORED_REVIEW_TEXT_KEYS:
                continue
            text = strip_leading_field_label(as_text(value), REBUTTAL_TEXT_KEYS)
            if text:
                parts.append(text)
    return "\n\n".join(part for part in parts if part).strip()


def extract_json_object(text: str) -> dict[str, Any]:
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            return {"strengths": [], "weaknesses": []}
        try:
            data = json.loads(match.group(0))
        except json.JSONDecodeError:
            return {"strengths": [], "weaknesses": []}
    return data if isinstance(data, dict) else {"strengths": [], "weaknesses": []}


def llm_segment_review(
    raw_review: str,
    model: str,
    base_url: Optional[str],
    api_key_env: str,
) -> tuple[list[str], list[str]]:
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise RuntimeError("Missing openai package; install it or omit --use-llm-segmentation.") from exc

    api_key = os.getenv(api_key_env)
    if not api_key and api_key_env in {"DASHSCOPE_API_KEY", "QWEN_API_KEY"}:
        api_key = os.getenv("QWEN_API_KEY") or os.getenv("DASHSCOPE_API_KEY")
    if not api_key:
        raise RuntimeError(f"--use-llm-segmentation requires {api_key_env} in the environment.")

    client = OpenAI(api_key=api_key, base_url=base_url) if base_url else OpenAI(api_key=api_key)
    request = {
        "model": model,
        "temperature": 0,
        "response_format": {"type": "json_object"},
        "messages": [
            {
                "role": "system",
                "content": (
                    "You extract paper-specific strengths and weaknesses from peer-review text. "
                    "Field names vary by venue, so decide by meaning rather than by exact labels. "
                    "First identify which passages are actual reviewer judgments about the paper, "
                    "then return only strict JSON with keys strengths and weaknesses. Each value must "
                    "be an array of complete-sentence or complete-bullet verbatim excerpts copied "
                    "from the review text. Do not summarize, paraphrase, rewrite, infer, or invent. "
                    "Do not split a sentence at words like weakness or concern; keep the whole "
                    "sentence on the correct side. Put only substantive advantages of the paper "
                    "in strengths, such as novelty, correctness, soundness, clarity, significance, "
                    "empirical support, useful method design, or strong presentation when the reviewer "
                    "states them as positives. Put only substantive flaws, limitations, missing evidence, "
                    "unclear parts, invalid claims, weak experiments, missing comparisons, or other paper "
                    "concerns in weaknesses. Exclude anything that is not an evaluative claim about the "
                    "paper: summaries/background, reviewer questions, scores/ratings/recommendations/"
                    "confidence, checklists, administrative or compliance text, ethics/conduct statements, "
                    "conflicts of interest, reviewer identity/expertise, availability or formatting notes, "
                    "bibliographies/references/citations, author responses/rebuttals, and section headings. "
                    "For rubric fields, include text only when the field contains a substantive sentence "
                    "about the paper; omit bare scores or generic values such as 'good', 'high', 'yes', "
                    "or 'affirmed'. If a passage is not clearly a paper strength or weakness, omit it. "
                    "If the review does not explicitly state a strength or weakness, return an empty array "
                    "for that key."
                ),
            },
            {"role": "user", "content": raw_review},
        ],
    }
    try:
        response = client.chat.completions.create(**request)
    except Exception:
        request.pop("response_format", None)
        response = client.chat.completions.create(**request)
    payload = response.choices[0].message.content or "{}"
    data = extract_json_object(payload)
    return (
        source_supported_items((as_text(item) for item in data.get("strengths", [])), raw_review),
        source_supported_items((as_text(item) for item in data.get("weaknesses", [])), raw_review),
    )


def reviewer_id(note: Any, index: int) -> str:
    signatures = getattr(note, "signatures", None) or []
    signature = signatures[0] if signatures else f"Reviewer_{index + 1}"
    return signature.split("/")[-1].replace("AnonReviewer", "Reviewer")


def review_rating(content: dict[str, Any]) -> Optional[float]:
    for key in (
        "rating",
        "Rating",
        "recommendation",
        "Recommendation",
        "overall_recommendation",
        "Overall Recommendation",
        "overall_assessment",
        "Overall Assessment",
    ):
        value = as_float(content.get(key))
        if value is not None:
            return value
    return None


def review_confidence(content: dict[str, Any]) -> Optional[float]:
    for key in ("confidence", "Confidence"):
        value = as_float(content.get(key))
        if value is not None:
            return value
    return None


def collection_label_to_decision(label: str) -> str:
    return "accept" if label in {"accept_oral", "accept", "poster", "spotlight"} else "reject"


def decision_bucket_from_text(text: str) -> Optional[str]:
    category = collection_category_from_decision(text)
    if category is None:
        return None
    return collection_label_to_decision(category)


def reviewer_recommendation(content: dict[str, Any], rating: Optional[float], conference: str) -> Optional[str]:
    recommendation = " ".join(
        as_text(content.get(key))
        for key in (
            "recommendation",
            "Recommendation",
            "overall_recommendation",
            "Overall Recommendation",
            "decision",
            "Decision",
        )
        if as_text(content.get(key))
    ).lower()
    if "reject" in recommendation:
        return "reject"
    if "accept" in recommendation:
        return "accept"

    if rating is None:
        return None

    thresholds = {
        "ICLR": 6.0,
        "ICML": 3.0,
        "NeurIPS": 4.0,
    }
    return "accept" if rating >= thresholds.get(conference, rating + 1) else "reject"


POLICY_REJECTION_RE = re.compile(
    r"(?:"
    r"\bban(?:ned)?(?:\s+list)?\b|\bsanction(?:ed|s)?\b|\bembargo\b|\bofac\b|export\s+control|"
    r"restricted\s+(?:country|countries|affiliation|institution)|"
    r"ineligible\s+(?:country|countries|affiliation|institution|author)|"
    r"(?:country|nationality|affiliation|institution)\s+(?:ban|restriction|policy)\b|"
    r"(?:authors?|institution|affiliation).{0,80}\b(?:banned|sanctioned|restricted|ineligible)\b|"
    r"\b(?:banned|sanctioned|restricted|ineligible)\b.{0,80}(?:country|countries|authors?|institution|affiliation)"
    r")",
    re.IGNORECASE,
)


def forum_policy_text(submission: Any, forum_notes: list[Any]) -> str:
    parts = [paper_decision(submission, forum_notes)]
    for note in forum_notes:
        if is_decision(note):
            parts.append(build_raw_review(get_content(note)))
        elif is_author_rebuttal(note):
            parts.append(build_rebuttal_text(get_content(note)))
    return "\n\n".join(part for part in parts if part)


def reviewer_accept_fraction(forum_notes: list[Any], conference: str) -> tuple[int, int, float]:
    accept_count = 0
    total = 0
    for note in forum_notes:
        if not is_official_review(note):
            continue
        content = get_content(note)
        recommendation = reviewer_recommendation(content, review_rating(content), conference)
        if recommendation is None:
            continue
        total += 1
        if recommendation == "accept":
            accept_count += 1
    return accept_count, total, (accept_count / total if total else 0.0)


def dataset_decision_label(
    submission: Any,
    forum_notes: list[Any],
    conference: str,
    collection_label: str,
    respect_policy_overrides: bool = False,
) -> tuple[str, Optional[str]]:
    if collection_label != "reject":
        return collection_label_to_decision(collection_label), None
    if not respect_policy_overrides:
        return "reject", None

    accept_count, total, fraction = reviewer_accept_fraction(forum_notes, conference)
    if total and fraction > (2 / 3) and POLICY_REJECTION_RE.search(forum_policy_text(submission, forum_notes)):
        return (
            "accept",
            f"Rejected paper relabeled because {accept_count}/{total} reviewers recommended accept "
            "and the forum/decision text appears to cite country, sanctions, or affiliation policy.",
        )
    return "reject", None


def resolved_dataset_decision(
    submission: Any,
    forum_notes: list[Any],
    conference: str,
    fallback_label: str,
    respect_policy_overrides: bool = False,
) -> tuple[str, Optional[str]]:
    explicit_decision = classify_accept_reject_decision(paper_decision(submission, forum_notes))
    final_decision = explicit_decision or collection_label_to_decision(fallback_label)
    if final_decision == "reject" and respect_policy_overrides:
        return dataset_decision_label(
            submission=submission,
            forum_notes=forum_notes,
            conference=conference,
            collection_label="reject",
            respect_policy_overrides=True,
        )
    return final_decision, None


def rebuttals_for_review(review: Any, forum_notes: list[Any]) -> list[str]:
    review_id = note_id(review)
    direct_replies = []
    global_rebuttals = []
    for note in forum_notes:
        if note_id(note) == review_id or not is_author_rebuttal(note):
            continue
        content = get_content(note)
        text = build_rebuttal_text(content)
        if not text:
            continue
        replyto = getattr(note, "replyto", None)
        if replyto == review_id:
            direct_replies.append(text)
        elif getattr(note, "forum", None) == note_forum(review):
            global_rebuttals.append(text)
    return direct_replies or global_rebuttals


def collect_reviews(
    forum_notes: list[Any],
    use_llm_segmentation: bool,
    llm_model: str,
    llm_base_url: Optional[str],
    llm_api_key_env: str,
    max_reviews: int,
    dataset_decision: str,
) -> list[dict[str, Any]]:
    reviews = [note for note in forum_notes if is_official_review(note)]
    reviews.sort(key=lambda note: getattr(note, "cdate", 0) or getattr(note, "tcdate", 0) or 0)

    collected = []
    for idx, note in enumerate(reviews):
        content = get_content(note)
        raw_review = build_segmentation_review_text(content)
        strengths, weaknesses = deterministic_segment(content, raw_review)
        if use_llm_segmentation and raw_review and needs_llm_segmentation(content, strengths, weaknesses):
            llm_strengths, llm_weaknesses = llm_segment_review(
                raw_review=raw_review,
                model=llm_model,
                base_url=llm_base_url,
                api_key_env=llm_api_key_env,
            )
            if llm_strengths:
                strengths = llm_strengths
            if llm_weaknesses:
                weaknesses = llm_weaknesses
        strengths = source_supported_items(strengths, raw_review)
        weaknesses = source_supported_items(weaknesses, raw_review)
        strengths, weaknesses = dedupe_segment_sides(strengths, weaknesses)

        rating = review_rating(content)
        review_obj = {
            "reviewer_id": reviewer_id(note, idx),
            "strengths": strengths,
            "weaknesses": weaknesses,
            "rating": rating,
            "confidence": review_confidence(content),
            "decision": dataset_decision,
            "rebuttal": "\n\n".join(rebuttals_for_review(note, forum_notes)),
        }
        if strengths or weaknesses or raw_review:
            collected.append(review_obj)
        if len(collected) >= max_reviews:
            break
    return collected


def average_rating(reviews: list[dict[str, Any]]) -> Optional[float]:
    ratings = [review["rating"] for review in reviews if review.get("rating") is not None]
    return round(sum(ratings) / len(ratings), 4) if ratings else None


def select_papers(
    submissions: list[Any],
    client: Any,
    venue: VenueSpec,
    per_category: int,
    max_fallback_forum_checks: int,
) -> list[tuple[Any, str, Optional[list[Any]]]]:
    selected: dict[str, list[tuple[Any, str, Optional[list[Any]]]]] = {"accept": [], "reject": []}
    decision_by_forum = fetch_decision_notes(client, venue)
    if decision_by_forum:
        print(f"Found {len(decision_by_forum)} decision notes for {venue.conference} {venue.year}")

    for submission in submissions:
        if all(len(items) >= per_category for items in selected.values()):
            break
        forum = note_forum(submission)
        label = decision_bucket_from_text(" ".join([submission_decision(submission), decision_by_forum.get(forum, "")]))
        if label is None and likely_reject_from_submission_metadata(submission, venue):
            label = "reject"
        if label in selected and len(selected[label]) < per_category:
            selected[label].append((submission, label, None))
            print(
                f"  {venue.conference} {venue.year}: "
                f"{len(selected[label])}/{per_category} {label} - {get_title(submission)[:80]}"
            )

    if all(len(items) >= per_category for items in selected.values()):
        return selected["accept"] + selected["reject"]

    if max_fallback_forum_checks <= 0:
        print(
            f"Metadata decision labels were incomplete for {venue.conference} {venue.year}; "
            "skipping fallback forum scan to avoid OpenReview rate-limit retries."
        )
        return selected["accept_oral"] + selected["reject"]

    print(
        f"Metadata decision labels were incomplete for {venue.conference} {venue.year}; "
        f"checking up to {max_fallback_forum_checks} remaining forums."
    )
    selected_forums = {note_forum(submission) for items in selected.values() for submission, _, _ in items}
    fallback_checks = 0
    for submission in submissions:
        if all(len(items) >= per_category for items in selected.values()):
            break
        if fallback_checks >= max_fallback_forum_checks:
            print(
                f"Stopped fallback forum checks for {venue.conference} {venue.year} after "
                f"{fallback_checks} papers; selected {sum(len(items) for items in selected.values())} papers."
            )
            break
        forum = note_forum(submission)
        if forum in selected_forums:
            continue
        fallback_checks += 1
        forum_notes = fetch_forum_notes(client, forum)
        label = decision_bucket_from_text(paper_decision(submission, forum_notes))
        if label in selected and len(selected[label]) < per_category:
            selected[label].append((submission, label, forum_notes))
            selected_forums.add(forum)
            print(
                f"  {venue.conference} {venue.year}: "
                f"{len(selected[label])}/{per_category} {label} - {get_title(submission)[:80]}"
            )
    return selected["accept"] + selected["reject"]


def wait_for_next_paper(last_started_at: Optional[float], gap_seconds: float) -> float:
    if last_started_at is not None and gap_seconds > 0:
        elapsed = time.monotonic() - last_started_at
        if elapsed < gap_seconds:
            wait_seconds = gap_seconds - elapsed
            print(f"Waiting {wait_seconds:.1f}s to keep paper processing at <= 5 papers/minute...")
            time.sleep(wait_seconds)
    return time.monotonic()


def validate_dataset(
    dataset: dict[str, Any],
    venues: list[VenueSpec],
    expected_per_category: int,
    expected_reviews_per_paper: int,
) -> None:
    print("\nDataset summary:")
    for venue in venues:
        papers = [paper for paper in dataset.values() if paper.get("conference") == venue.conference]
        accept_count = sum(1 for paper in papers if paper.get("accept_or_not") == "accept")
        reject_count = sum(1 for paper in papers if paper.get("accept_or_not") == "reject")
        short_reviews = [
            paper.get("title", "Untitled")
            for paper in papers
            if len(paper.get("reviews", [])) != expected_reviews_per_paper
        ]
        print(
            f"  {venue.conference} {venue.year}: "
            f"{len(papers)} papers, accept={accept_count}, reject={reject_count}"
        )
        if accept_count < expected_per_category or reject_count < expected_per_category:
            print(
                f"    Warning: target is {expected_per_category} accept and "
                f"{expected_per_category} reject papers."
            )
        if short_reviews:
            print(
                f"    Warning: {len(short_reviews)} papers do not have "
                f"{expected_reviews_per_paper} reviews."
            )


def build_dataset(args: argparse.Namespace) -> dict[str, Any]:
    openreview = import_openreview()
    client = get_client(openreview)
    dataset = {}
    pdf_dir = Path(args.pdf_dir)
    output_path = Path(args.output)
    last_paper_started_at: Optional[float] = None
    venues = parse_venue_specs(args.venues)

    for venue in venues:
        print(f"Fetching submissions for {venue.conference} {venue.year} ({venue.venue_id})")
        submissions = fetch_submissions(client, venue)
        print(f"Found {len(submissions)} submissions; selecting target categories")
        effective_per_category = min(args.per_category, args.max_papers_per_conference // 2)
        if effective_per_category < args.per_category:
            print(
                f"Capping {venue.conference} {venue.year} to "
                f"{effective_per_category * 2} papers "
                f"({effective_per_category} accept + {effective_per_category} reject)."
            )
        selected = select_papers(
            submissions,
            client,
            venue,
            effective_per_category,
            args.max_fallback_forum_checks,
        )
        selected = selected[: args.max_papers_per_conference]
        print(f"Selected {len(selected)} papers for {venue.conference} {venue.year}")

        counters = {"accept": 0, "reject": 0}
        for submission, label, forum_notes in selected:
            last_paper_started_at = wait_for_next_paper(last_paper_started_at, args.paper_gap_seconds)
            title = get_title(submission)
            if forum_notes is None:
                forum_notes = fetch_forum_notes(client, note_forum(submission))
            final_decision, override_reason = resolved_dataset_decision(
                submission=submission,
                forum_notes=forum_notes,
                conference=venue.conference,
                fallback_label=label,
                respect_policy_overrides=args.respect_policy_overrides,
            )
            if counters[final_decision] >= effective_per_category:
                print(
                    f"Warning: skipping {title!r}; verified decision {final_decision!r} "
                    "would overfill that collection."
                )
                continue
            pdf_url = get_pdf_url(submission)

            reviews = collect_reviews(
                forum_notes=forum_notes,
                use_llm_segmentation=args.use_llm_segmentation,
                llm_model=args.llm_model,
                llm_base_url=args.llm_base_url,
                llm_api_key_env=args.llm_api_key_env,
                max_reviews=args.reviews_per_paper,
                dataset_decision=final_decision,
            )
            if len(reviews) < args.reviews_per_paper and not args.allow_incomplete:
                print(f"Warning: skipping {title!r}; only {len(reviews)} reviews found", file=sys.stderr)
                continue

            counters[final_decision] += 1
            key = (
                f"{venue.conference.lower()}_{final_decision}_"
                f"{venue.year}_{counters[final_decision]:03d}_{slugify(title)}"
            )

            paper_dir = ""
            if args.download_pdfs and pdf_url:
                pdf_path = pdf_dir / f"{key}.pdf"
                if download_pdf(pdf_url, pdf_path, sleep_seconds=args.sleep):
                    paper_dir = str(pdf_path)

            paper_record = {
                "title": title,
                "paper_dir": paper_dir,
                "paper_url": openreview_url(note_forum(submission)),
                "pdf_url": pdf_url,
                "conference": venue.conference,
                "year": venue.year,
                "topic": args.topic,
                "accept_or_not": final_decision,
                "collection_decision_category": final_decision,
                "score": average_rating(reviews),
                "reviews": reviews,
            }
            if override_reason:
                paper_record["decision_override_reason"] = override_reason
            dataset[key] = paper_record
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(json.dumps(dataset, indent=2, ensure_ascii=False), encoding="utf-8")

    validate_dataset(dataset, venues, min(args.per_category, args.max_papers_per_conference // 2), args.reviews_per_paper)
    return dataset


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--venues",
        nargs="+",
        default=["ICLR:2025", "ICML:2025", "NeurIPS:2025"],
        help="Venue specs as CONF:YEAR or CONF:YEAR:OPENREVIEW_VENUE_ID.",
    )
    parser.add_argument("--per-category", type=int, default=50)
    parser.add_argument(
        "--max-papers-per-conference",
        type=int,
        default=100,
        help="Maximum total papers to collect/download per conference.",
    )
    parser.add_argument("--reviews-per-paper", type=int, default=3)
    parser.add_argument("--output", default="eval/LetsTalk_papers_Qwen.json")
    parser.add_argument("--pdf-dir", default="data/openreview_pdf")
    parser.add_argument("--topic", default="Others")
    parser.add_argument("--download-pdfs", action="store_true")
    parser.add_argument("--allow-incomplete", action="store_true")
    parser.add_argument(
        "--respect-policy-overrides",
        action="store_true",
        help=(
            "Opt in to relabeling rejected papers as accept when reviewers strongly favored "
            "acceptance and policy-related rejection text is detected. Off by default so "
            "accept_or_not tracks the explicit OpenReview decision."
        ),
    )
    parser.add_argument(
        "--max-fallback-forum-checks",
        type=int,
        default=0,
        help=(
            "Maximum unselected forums to fetch when metadata cannot fill target categories. "
            "Default 0 avoids OpenReview rate-limit retry noise."
        ),
    )
    parser.add_argument("--use-llm-segmentation", action="store_true")
    parser.add_argument("--llm-model", default=DEFAULT_LLM_MODEL)
    parser.add_argument(
        "--llm-base-url",
        default="https://dashscope.aliyuncs.com/compatible-mode/v1",
        help="OpenAI-compatible API base URL. Use empty string for OpenAI's default endpoint.",
    )
    parser.add_argument(
        "--llm-api-key-env",
        default="DASHSCOPE_API_KEY",
        help="Environment variable containing the OpenAI-compatible API key.",
    )
    parser.add_argument("--sleep", type=float, default=0.2, help="Delay between network-heavy requests.")
    parser.add_argument(
        "--paper-gap-seconds",
        type=float,
        default=5.0,
        help="Minimum gap between selected paper processing starts; 5s means at most 12 papers/minute.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.llm_base_url == "":
        args.llm_base_url = None
    api_key_available = (
        os.getenv(args.llm_api_key_env)
        or os.getenv("QWEN_API_KEY")
        or os.getenv("DASHSCOPE_API_KEY")
    )
    if args.use_llm_segmentation and not api_key_available:
        raise SystemExit(f"--use-llm-segmentation requires {args.llm_api_key_env} in the environment.")

    try:
        dataset = build_dataset(args)
    except Exception as exc:
        if is_openreview_challenge_required_error(exc):
            print(openreview_challenge_message(), file=sys.stderr)
            raise SystemExit(1) from exc
        raise
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(dataset, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(dataset)} papers to {output}")


if __name__ == "__main__":
    main()

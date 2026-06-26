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


def fetch_forum_notes(client: Any, forum: str) -> list[Any]:
    return get_all_notes(client, forum=forum)


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


def has_invitation(note: Any, pattern: str) -> bool:
    invitations = getattr(note, "invitations", None) or []
    invitation = getattr(note, "invitation", None)
    if invitation:
        invitations.append(invitation)
    return any(re.search(pattern, inv, re.IGNORECASE) for inv in invitations)


def is_official_review(note: Any) -> bool:
    if has_invitation(note, r"official[_ -]?review|review$"):
        return True
    content = get_content(note)
    keys = {key.lower().replace(" ", "_") for key in content}
    reviewish = {"rating", "recommendation", "confidence", "summary", "soundness", "review"}
    return bool(keys & reviewish) and not is_decision(note)


def is_decision(note: Any) -> bool:
    return has_invitation(note, r"decision|recommendation$") or "decision" in get_content(note)


def is_author_rebuttal(note: Any) -> bool:
    invitations = " ".join((getattr(note, "invitations", None) or []) + [getattr(note, "invitation", "")])
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


ACCEPTANCE_MARKER_RE = re.compile(
    r"\b(?:accept(?:ed)?|oral|spotlight|poster|notable|award)\b",
    re.IGNORECASE,
)


def classify_decision(text: str) -> Optional[str]:
    normalized = text.lower()
    if not normalized:
        return None
    reject_tokens = ("reject", "withdrawn", "desk reject")
    if any(token in normalized for token in reject_tokens):
        return "reject"
    if ACCEPTANCE_MARKER_RE.search(normalized):
        return "accept_oral"
    return None


def likely_reject_from_submission_metadata(submission: Any, venue: VenueSpec) -> bool:
    content = get_content(submission)
    decision_text = submission_decision(submission)
    if classify_decision(decision_text):
        return False

    venueid = as_text(content.get("venueid") or content.get("venue_id") or content.get("Venue ID"))
    venue_text = as_text(content.get("venue") or content.get("Venue"))
    normalized_venue_text = venue_text.lower()
    if ACCEPTANCE_MARKER_RE.search(normalized_venue_text):
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
    try:
        with urllib.request.urlopen(url, timeout=60) as response:
            destination.write_bytes(response.read())
        if sleep_seconds:
            time.sleep(sleep_seconds)
        return True
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        print(f"Warning: failed to download PDF {url}: {exc}", file=sys.stderr)
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
    "Other Strengths And Weaknesses",
]

STRUCTURED_WEAKNESS_KEYS = [
    "weaknesses",
    "Weaknesses",
    "limitations",
    "Limitations",
    "paper_weaknesses",
    "Paper Weaknesses",
    "summary_of_weaknesses",
    "Summary Of Weaknesses",
    "Main Weaknesses",
    "Other Weaknesses",
    "Other Strengths And Weaknesses",
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
]

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
    "soundness",
    "presentation",
    "contribution",
    "flag_for_ethics_review",
    "code_of_conduct",
}

SECTION_HEADER_RE = re.compile(
    r"^\s*(?:#+\s*)?("
    r"strengths?|weakness(?:es)?|limitations?|concerns?|"
    r"summary(?:\s+of\s+the\s+review)?|main\s+review|review|comments?|"
    r"questions?|soundness|presentation|contribution|"
    r"flag[_\s-]+for[_\s-]+ethics[_\s-]+review|code[_\s-]+of[_\s-]+conduct|"
    r"rating|confidence|recommendation|decision"
    r")\s*:?\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def canonical_field_name(key: str) -> str:
    return re.sub(r"[\s-]+", "_", key.strip().lower())


def split_bullets(text: str) -> list[str]:
    text = text.strip()
    if not text:
        return []
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    bullet_lines = []
    saw_bullet = False
    for line in lines:
        cleaned, count = re.subn(r"^\s*(?:[-*•]|\d+[.)])\s+", "", line, count=1)
        saw_bullet = saw_bullet or count > 0
        cleaned = cleaned.strip()
        if cleaned:
            bullet_lines.append(cleaned)
    if saw_bullet:
        return bullet_lines
    chunks = re.split(r"\n{2,}|(?<=[.!?])\s+(?=[A-Z])", text)
    return [chunk.strip() for chunk in chunks if chunk.strip()]


def section_blocks(text: str) -> dict[str, str]:
    matches = list(SECTION_HEADER_RE.finditer(text))
    blocks: dict[str, str] = {}
    for idx, match in enumerate(matches):
        header = match.group(1).lower()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        blocks[header] = text[start:end].strip()
    return blocks


def deterministic_segment(content: dict[str, Any], raw_review: str) -> tuple[list[str], list[str]]:
    strengths = []
    weaknesses = []
    for key in STRUCTURED_STRENGTH_KEYS:
        if key in content and key != "Other Strengths And Weaknesses":
            strengths.extend(split_bullets(as_text(content[key])))
    for key in STRUCTURED_WEAKNESS_KEYS:
        if key in content and key != "Other Strengths And Weaknesses":
            weaknesses.extend(split_bullets(as_text(content[key])))

    blocks = section_blocks(raw_review)
    for header, block in blocks.items():
        if "strength" in header:
            strengths.extend(split_bullets(block))
        elif any(token in header for token in ("weakness", "limitation", "concern")):
            weaknesses.extend(split_bullets(block))

    return dedupe_preserve_order(strengths), dedupe_preserve_order(weaknesses)


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
                    "Segment peer review comments into strengths and weaknesses. "
                    "Return strict JSON with keys strengths and weaknesses, each an array "
                    "of concise faithful statements. Do not invent content."
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
        dedupe_preserve_order(as_text(item) for item in data.get("strengths", [])),
        dedupe_preserve_order(as_text(item) for item in data.get("weaknesses", [])),
    )


def reviewer_id(note: Any, index: int) -> str:
    signatures = getattr(note, "signatures", None) or []
    signature = signatures[0] if signatures else f"Reviewer_{index + 1}"
    return signature.split("/")[-1].replace("AnonReviewer", "Reviewer")


def review_rating(content: dict[str, Any]) -> Optional[float]:
    for key in ("rating", "Rating", "recommendation", "Recommendation", "overall_assessment"):
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
    return "accept" if label in {"accept_oral", "accept"} else "reject"


def reviewer_recommendation(content: dict[str, Any], rating: Optional[float], conference: str) -> Optional[str]:
    recommendation = " ".join(
        as_text(content.get(key))
        for key in ("recommendation", "Recommendation", "decision", "Decision")
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
    r"ban(?:ned)?(?:\s+list)?|sanction(?:ed|s)?|embargo|ofac|export\s+control|"
    r"restricted\s+(?:country|countries|affiliation|institution)|"
    r"ineligible\s+(?:country|countries|affiliation|institution|author)|"
    r"(?:country|nationality|affiliation|institution)\s+(?:ban|restriction|policy)|"
    r"(?:authors?|institution|affiliation).{0,80}(?:banned|sanctioned|restricted|ineligible)|"
    r"(?:banned|sanctioned|restricted|ineligible).{0,80}(?:country|countries|authors?|institution|affiliation)"
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
) -> tuple[str, Optional[str]]:
    if collection_label != "reject":
        return collection_label_to_decision(collection_label), None

    accept_count, total, fraction = reviewer_accept_fraction(forum_notes, conference)
    if total and fraction > (2 / 3) and POLICY_REJECTION_RE.search(forum_policy_text(submission, forum_notes)):
        return (
            "accept",
            f"Rejected paper relabeled because {accept_count}/{total} reviewers recommended accept "
            "and the forum/decision text appears to cite country, sanctions, or affiliation policy.",
        )
    return "reject", None


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
        raw_review = build_raw_review(content)
        strengths, weaknesses = deterministic_segment(content, raw_review)
        if use_llm_segmentation and raw_review and (not strengths or not weaknesses):
            strengths, weaknesses = llm_segment_review(
                raw_review=raw_review,
                model=llm_model,
                base_url=llm_base_url,
                api_key_env=llm_api_key_env,
            )

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
    selected: dict[str, list[tuple[Any, str, Optional[list[Any]]]]] = {"accept_oral": [], "reject": []}
    decision_by_forum = fetch_decision_notes(client, venue)
    if decision_by_forum:
        print(f"Found {len(decision_by_forum)} decision notes for {venue.conference} {venue.year}")

    for submission in submissions:
        if all(len(items) >= per_category for items in selected.values()):
            break
        forum = note_forum(submission)
        label = classify_decision(" ".join([submission_decision(submission), decision_by_forum.get(forum, "")]))
        if label is None and likely_reject_from_submission_metadata(submission, venue):
            label = "reject"
        if label in selected and len(selected[label]) < per_category:
            selected[label].append((submission, label, None))
            print(
                f"  {venue.conference} {venue.year}: "
                f"{len(selected[label])}/{per_category} {label} - {get_title(submission)[:80]}"
            )

    if all(len(items) >= per_category for items in selected.values()):
        return selected["accept_oral"] + selected["reject"]

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
        label = classify_decision(paper_decision(submission, forum_notes))
        if label in selected and len(selected[label]) < per_category:
            selected[label].append((submission, label, forum_notes))
            selected_forums.add(forum)
            print(
                f"  {venue.conference} {venue.year}: "
                f"{len(selected[label])}/{per_category} {label} - {get_title(submission)[:80]}"
            )
    return selected["accept_oral"] + selected["reject"]


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
                f"({effective_per_category} accept_oral + {effective_per_category} reject)."
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

        counters = {"accept_oral": 0, "reject": 0}
        for submission, label, forum_notes in selected:
            last_paper_started_at = wait_for_next_paper(last_paper_started_at, args.paper_gap_seconds)
            counters[label] += 1
            title = get_title(submission)
            category_name = "accept" if label == "accept_oral" else "reject"
            if forum_notes is None:
                forum_notes = fetch_forum_notes(client, note_forum(submission))
            final_decision, override_reason = dataset_decision_label(
                submission=submission,
                forum_notes=forum_notes,
                conference=venue.conference,
                collection_label=label,
            )
            key = (
                f"{venue.conference.lower()}_{category_name}_"
                f"{venue.year}_{counters[label]:03d}_{slugify(title)}"
            )
            pdf_url = get_pdf_url(submission)
            paper_dir = ""

            # Per-paper order: find correct paper -> download -> collect review/rebuttal -> Qwen segment -> add to dataset.
            if args.download_pdfs and pdf_url:
                pdf_path = pdf_dir / f"{key}.pdf"
                if download_pdf(pdf_url, pdf_path, sleep_seconds=args.sleep):
                    paper_dir = str(pdf_path)

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

            paper_record = {
                "title": title,
                "paper_dir": paper_dir,
                "paper_url": openreview_url(note_forum(submission)),
                "pdf_url": pdf_url,
                "conference": venue.conference,
                "year": venue.year,
                "topic": args.topic,
                "accept_or_not": final_decision,
                "collection_decision_category": label,
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
        "--max-fallback-forum-checks",
        type=int,
        default=0,
        help=(
            "Maximum unselected forums to fetch when metadata cannot fill target categories. "
            "Default 0 avoids OpenReview rate-limit retry noise."
        ),
    )
    parser.add_argument("--use-llm-segmentation", action="store_true")
    parser.add_argument("--llm-model", default="qwen3.7-plus")
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

    dataset = build_dataset(args)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(dataset, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(dataset)} papers to {output}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Offline quality audit for OpenReview evaluation JSON files.

The checks here deliberately avoid OpenReview or LLM calls. They are meant to be
run after build/repair jobs to catch silent drift before the dataset is used for
evaluation.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import scripts.build_openreview_eval_dataset as builder


DEFAULT_INPUT = "eval/openreview_2025_300_qwen.json"
DEFAULT_EXPECTED_YEAR = 2025
REQUIRED_RECORD_FIELDS = [
    "title",
    "paper_dir",
    "paper_url",
    "pdf_url",
    "conference",
    "year",
    "accept_or_not",
    "collection_decision_category",
    "score",
    "reviews",
]
REQUIRED_REVIEW_FIELDS = ["reviewer_id", "strengths", "weaknesses", "rating", "decision", "rebuttal"]
VALID_FINAL_LABELS = {"accept", "reject"}
VALID_COLLECTION_BUCKETS = {"accept", "reject"}
KEY_PATTERN = re.compile(
    r"^(?P<conference>[a-z0-9]+)_(?P<bucket>accept|reject)_(?P<year>\d{4})_"
    r"(?P<slot>\d{3})_(?P<slug>[a-z0-9_]*[a-z0-9][a-z0-9_]*)$"
)


@dataclass
class Audit:
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def load_dataset(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit(f"{path} must contain a JSON object keyed by paper id.")
    return data


def normalize_collection_bucket(label: Any) -> str:
    text = str(label or "").strip().lower()
    if text.startswith("accept"):
        return "accept"
    if text.startswith("reject"):
        return "reject"
    return text or "missing"


def bucket_from_key(key: str) -> str:
    match = KEY_PATTERN.match(key)
    if not match:
        return "unknown"
    return match.group("bucket")


def key_metadata_from_key(key: str) -> dict[str, str] | None:
    match = KEY_PATTERN.match(key)
    if not match:
        return None
    return match.groupdict()


def expected_year(args: argparse.Namespace) -> int | None:
    value = getattr(args, "expected_year", None)
    if value is None:
        return None
    value = int(value)
    if value < 0:
        return None
    return value


def average_rating(reviews: list[Any]) -> float | None:
    ratings = []
    for review in reviews:
        if not isinstance(review, dict):
            continue
        rating = review.get("rating")
        if is_finite_number(rating):
            ratings.append(float(rating))
    if not ratings:
        return None
    return round(sum(ratings) / len(ratings), 4)


def is_finite_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


def stripped_string(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return value.strip()


def normalized_segment_text(value: str) -> str:
    return " ".join(value.casefold().split())


def review_duplicate_signature(review: dict[str, Any]) -> str:
    payload = {
        "strengths": review.get("strengths"),
        "weaknesses": review.get("weaknesses"),
        "rating": review.get("rating"),
        "decision": review.get("decision"),
        "rebuttal": review.get("rebuttal"),
    }
    return json.dumps(payload, sort_keys=True, ensure_ascii=False)


def is_openreview_forum_url(url: str) -> bool:
    parsed = urlparse(str(url or ""))
    return (
        parsed.scheme in {"http", "https"}
        and parsed.netloc == "openreview.net"
        and parsed.path.rstrip("/") == "/forum"
        and bool(openreview_forum_id(url))
    )


def is_openreview_pdf_url(url: str) -> bool:
    parsed = urlparse(str(url or ""))
    if parsed.scheme not in {"http", "https"} or parsed.netloc != "openreview.net":
        return False
    if parsed.path.rstrip("/") == "/pdf":
        return bool(openreview_pdf_query_id(url))
    return bool(re.fullmatch(r"/pdf/[A-Za-z0-9]+\.pdf", parsed.path))


def local_pdf_error(path: Path) -> str | None:
    if not path.exists() or path.stat().st_size == 0:
        return f"missing local PDF {path}"
    try:
        with path.open("rb") as handle:
            header = handle.read(5)
    except OSError as exc:
        return f"cannot read local PDF {path}: {exc}"
    if not header.startswith(b"%PDF"):
        return f"local PDF {path} does not start with %PDF header"
    return None


def local_pdf_inventory_summary(data: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    pdf_dir = getattr(args, "pdf_dir", None)
    summary = {
        "pdf_dir": str(pdf_dir) if pdf_dir else None,
        "exists": bool(pdf_dir and pdf_dir.exists()),
        "total_pdf_files": 0,
        "referenced_pdf_files": 0,
        "missing_for_records": [],
        "orphan_pdf_files": [],
        "invalid_pdf_files": [],
    }
    if not pdf_dir or not pdf_dir.exists():
        return summary

    record_keys = {key for key, record in data.items() if isinstance(record, dict)}
    pdf_paths = sorted(pdf_dir.glob("*.pdf"))
    pdf_stems = {path.stem for path in pdf_paths}
    summary["total_pdf_files"] = len(pdf_paths)
    summary["referenced_pdf_files"] = len(record_keys & pdf_stems)
    summary["missing_for_records"] = sorted(record_keys - pdf_stems)
    summary["orphan_pdf_files"] = sorted(pdf_stems - record_keys)
    summary["invalid_pdf_files"] = [path.stem for path in pdf_paths if local_pdf_error(path)]
    return summary


def openreview_forum_id(url: str) -> str:
    parsed = urlparse(str(url or ""))
    if parsed.path.rstrip("/") != "/forum":
        return ""
    return (parse_qs(parsed.query).get("id") or [""])[0]


def openreview_pdf_query_id(url: str) -> str:
    parsed = urlparse(str(url or ""))
    if parsed.path.rstrip("/") != "/pdf":
        return ""
    return (parse_qs(parsed.query).get("id") or [""])[0]


def is_bad_segment_marker(text: str) -> bool:
    stripped = str(text or "").strip()
    if not stripped:
        return True
    if builder.is_non_substantive_segment_text(stripped):
        return True
    canonical = builder.canonical_field_name(stripped.rstrip(":"))
    ignored = {builder.canonical_field_name(key) for key in builder.IGNORED_REVIEW_TEXT_KEYS}
    ignored.update(builder.canonical_field_name(key) for key in builder.SUBSTANTIVE_REVIEW_TEXT_KEYS)
    return canonical in ignored


def add_distribution_checks(data: dict[str, Any], audit: Audit, args: argparse.Namespace) -> None:
    if args.expected_total is not None and args.expected_total >= 0 and len(data) != args.expected_total:
        audit.error(f"expected {args.expected_total} records, found {len(data)}")

    by_conference = Counter()
    by_collection = Counter()
    by_final_label = Counter()
    for record in data.values():
        if not isinstance(record, dict):
            continue
        conference = str(record.get("conference") or "missing")
        by_conference[conference] += 1
        by_collection[(conference, normalize_collection_bucket(record.get("collection_decision_category")))] += 1
        by_final_label[(conference, str(record.get("accept_or_not") or "missing").lower())] += 1

    for conference in args.expected_conference:
        if args.expected_per_conference is not None and args.expected_per_conference >= 0:
            found = by_conference.get(conference, 0)
            if found != args.expected_per_conference:
                audit.error(f"{conference}: expected {args.expected_per_conference} records, found {found}")
        if args.expected_per_collection_label is not None and args.expected_per_collection_label >= 0:
            for bucket in ("accept", "reject"):
                found = by_collection.get((conference, bucket), 0)
                if found != args.expected_per_collection_label:
                    audit.error(
                        f"{conference}: expected {args.expected_per_collection_label} collected {bucket} papers, "
                        f"found {found}"
                    )
        if args.expected_per_final_label is not None and args.expected_per_final_label >= 0:
            for label in ("accept", "reject"):
                found = by_final_label.get((conference, label), 0)
                if found != args.expected_per_final_label:
                    audit.error(
                        f"{conference}: expected {args.expected_per_final_label} final {label} papers, "
                        f"found {found}"
                    )

    audit.warn(f"conference counts: {dict(sorted(by_conference.items()))}")
    audit.warn(f"collection bucket counts: {dict(sorted(by_collection.items()))}")
    audit.warn(f"final label counts: {dict(sorted(by_final_label.items()))}")


def add_key_sequence_checks(data: dict[str, Any], audit: Audit, args: argparse.Namespace) -> None:
    if args.expected_per_collection_label is None or args.expected_per_collection_label < 1:
        return
    expected_slots = set(range(1, args.expected_per_collection_label + 1))
    for conference in args.expected_conference:
        conference_prefix = conference.lower()
        for bucket in ("accept", "reject"):
            slots = []
            pattern = re.compile(rf"^{re.escape(conference_prefix)}_{bucket}_(\d{{4}})_(\d{{3}})_")
            for key, record in data.items():
                if not isinstance(record, dict):
                    continue
                if str(record.get("conference") or "") != conference:
                    continue
                if normalize_collection_bucket(record.get("collection_decision_category")) != bucket:
                    continue
                match = pattern.match(key)
                if match:
                    slots.append(int(match.group(2)))
            if not slots:
                continue
            missing = sorted(expected_slots - set(slots))
            if missing:
                formatted = ", ".join(f"{slot:03d}" for slot in missing)
                audit.error(f"{conference}: missing collected {bucket} key slots: {formatted}")
            duplicates = sorted(slot for slot, count in Counter(slots).items() if count > 1)
            if duplicates:
                formatted = ", ".join(f"{slot:03d}" for slot in duplicates)
                audit.error(f"{conference}: duplicate collected {bucket} key slots: {formatted}")


def audit_record(
    key: str,
    record: Any,
    audit: Audit,
    args: argparse.Namespace,
    paper_urls: defaultdict[str, list[str]],
    pdf_urls: defaultdict[str, list[str]],
    paper_dirs: defaultdict[str, list[str]],
    titles: defaultdict[str, list[str]],
) -> None:
    if not isinstance(record, dict):
        audit.error(f"{key}: record is not an object")
        return

    for field_name in REQUIRED_RECORD_FIELDS:
        if field_name not in record:
            audit.error(f"{key}: missing record field {field_name}")

    raw_title = record.get("title")
    title = stripped_string(raw_title)
    if title:
        titles[title.lower()].append(key)
    elif not isinstance(raw_title, str):
        audit.error(f"{key}: title is not a non-empty string")
    else:
        audit.error(f"{key}: empty title")

    record_conference = stripped_string(record.get("conference"))
    expected_conferences = getattr(args, "expected_conference", None) or []
    if not isinstance(record.get("conference"), str) or not record_conference:
        audit.error(f"{key}: conference is not a non-empty string")
    elif expected_conferences and record_conference not in expected_conferences:
        audit.error(f"{key}: conference {record_conference!r} is not in expected conferences {expected_conferences!r}")

    record_year_value = record.get("year")
    record_year = str(record_year_value if record_year_value is not None else "").strip()
    target_year = expected_year(args)
    if not isinstance(record_year_value, int) or isinstance(record_year_value, bool):
        audit.error(f"{key}: year is not an integer")
    elif target_year is not None and record_year_value != target_year:
        audit.error(f"{key}: expected year {target_year}, found {record_year_value}")

    raw_paper_url = record.get("paper_url")
    paper_url = stripped_string(raw_paper_url)
    paper_forum_id = ""
    if paper_url:
        paper_urls[paper_url].append(key)
        if not is_openreview_forum_url(paper_url):
            audit.error(f"{key}: paper_url is not an OpenReview forum URL: {paper_url!r}")
        else:
            paper_forum_id = openreview_forum_id(paper_url)
    elif not isinstance(raw_paper_url, str):
        audit.error(f"{key}: paper_url is not a non-empty string")
    else:
        audit.error(f"{key}: empty paper_url")

    key_metadata = key_metadata_from_key(key)
    if key_metadata is None:
        audit.error(f"{key}: key does not match expected format '<conference>_<accept|reject>_<year>_<slot>_<slug>'")
    else:
        expected_slug = builder.slugify(title) if title else ""
        if expected_slug and key_metadata["slug"] != expected_slug:
            audit.error(f"{key}: key slug is {key_metadata['slug']!r}, but title slug is {expected_slug!r}")
        if record_conference.lower() != key_metadata["conference"]:
            audit.error(
                f"{key}: key conference is {key_metadata['conference']}, but conference is "
                f"{record.get('conference')!r}"
            )
        if record_year != key_metadata["year"]:
            audit.error(f"{key}: key year is {key_metadata['year']}, but year is {record.get('year')!r}")

    key_bucket = key_metadata["bucket"] if key_metadata else "unknown"
    collection_bucket = normalize_collection_bucket(record.get("collection_decision_category"))
    raw_collection_label = record.get("collection_decision_category")
    if not isinstance(raw_collection_label, str) or not stripped_string(raw_collection_label):
        audit.error(f"{key}: collection_decision_category is not a non-empty string")
    elif collection_bucket not in VALID_COLLECTION_BUCKETS:
        audit.error(
            f"{key}: collection_decision_category must normalize to accept/reject, found "
            f"{raw_collection_label!r}"
        )
    final_label = stripped_string(record.get("accept_or_not")).lower()
    if key_bucket != "unknown" and collection_bucket != key_bucket:
        audit.error(
            f"{key}: key bucket is {key_bucket}, but collection_decision_category is "
            f"{record.get('collection_decision_category')!r}"
        )
    if not isinstance(record.get("accept_or_not"), str):
        audit.error(f"{key}: accept_or_not must be a string accept/reject, found {record.get('accept_or_not')!r}")
    elif final_label not in VALID_FINAL_LABELS:
        audit.error(f"{key}: accept_or_not must be accept/reject, found {record.get('accept_or_not')!r}")
    elif key_bucket != "unknown" and final_label != key_bucket:
        if record.get("decision_override_reason"):
            audit.warn(f"{key}: final label differs from key bucket due to documented override")
        else:
            audit.error(f"{key}: key bucket is {key_bucket}, but accept_or_not is {final_label}")

    reviews = record.get("reviews")
    if not isinstance(reviews, list):
        audit.error(f"{key}: reviews is not a list")
        return
    if len(reviews) != args.reviews_per_paper:
        audit.error(f"{key}: expected {args.reviews_per_paper} reviews, found {len(reviews)}")

    expected_score = average_rating(reviews)
    score = record.get("score")
    if expected_score is not None:
        if not isinstance(score, (int, float)) or isinstance(score, bool):
            audit.error(f"{key}: score is not numeric")
        elif not is_finite_number(score):
            audit.error(f"{key}: score is not finite")
        elif abs(round(float(score), 4) - expected_score) > 0.0001:
            audit.error(f"{key}: score {score} does not match average rating {expected_score}")

    raw_pdf_url = record.get("pdf_url")
    pdf_url = stripped_string(raw_pdf_url)
    if not pdf_url:
        if not isinstance(raw_pdf_url, str):
            audit.error(f"{key}: pdf_url is not a non-empty string")
        else:
            audit.error(f"{key}: empty pdf_url")
    elif not is_openreview_pdf_url(pdf_url):
        audit.error(f"{key}: pdf_url is not an OpenReview PDF URL: {pdf_url!r}")
    else:
        pdf_urls[pdf_url].append(key)
        pdf_query_id = openreview_pdf_query_id(pdf_url)
        if paper_forum_id and pdf_query_id and paper_forum_id != pdf_query_id:
            audit.error(f"{key}: paper_url id {paper_forum_id!r} does not match pdf_url id {pdf_query_id!r}")
        if args.pdf_dir and args.pdf_dir.exists():
            pdf_path = args.pdf_dir / f"{key}.pdf"
            pdf_error = local_pdf_error(pdf_path)
            if pdf_error:
                audit.error(f"{key}: {pdf_error}")

    raw_paper_dir = record.get("paper_dir")
    paper_dir = stripped_string(raw_paper_dir)
    if not paper_dir:
        if not isinstance(raw_paper_dir, str):
            audit.error(f"{key}: paper_dir is not a non-empty string")
        else:
            audit.error(f"{key}: empty paper_dir")
    elif Path(paper_dir).suffix.lower() != ".pdf":
        audit.error(f"{key}: paper_dir is not a PDF path: {paper_dir!r}")
    else:
        paper_dirs[paper_dir].append(key)
        if args.pdf_dir and args.pdf_dir.exists():
            expected_pdf_path = args.pdf_dir / f"{key}.pdf"
            if Path(paper_dir) != expected_pdf_path:
                audit.error(f"{key}: paper_dir {paper_dir!r} does not match expected local PDF {str(expected_pdf_path)!r}")

    seen_reviewer_ids: dict[str, int] = {}
    seen_review_signatures: dict[str, int] = {}
    for index, review in enumerate(reviews):
        if isinstance(review, dict):
            reviewer_id = stripped_string(review.get("reviewer_id"))
            if reviewer_id:
                if reviewer_id in seen_reviewer_ids:
                    audit.error(
                        f"{key}: duplicate reviewer_id {reviewer_id!r} in reviews "
                        f"{seen_reviewer_ids[reviewer_id]} and {index}"
                    )
                seen_reviewer_ids[reviewer_id] = index

            signature = review_duplicate_signature(review)
            if signature in seen_review_signatures:
                audit.error(f"{key}: duplicate review payload in reviews {seen_review_signatures[signature]} and {index}")
            seen_review_signatures[signature] = index
        audit_review(key, index, review, final_label, audit)


def audit_review(key: str, index: int, review: Any, final_label: str, audit: Audit) -> None:
    prefix = f"{key} review[{index}]"
    if not isinstance(review, dict):
        audit.error(f"{prefix}: review is not an object")
        return

    for field_name in REQUIRED_REVIEW_FIELDS:
        if field_name not in review:
            audit.error(f"{prefix}: missing review field {field_name}")

    reviewer_id = review.get("reviewer_id")
    if not isinstance(reviewer_id, str) or not reviewer_id.strip():
        audit.error(f"{prefix}: reviewer_id is not a non-empty string")

    rating = review.get("rating")
    if not isinstance(rating, (int, float)) or isinstance(rating, bool):
        audit.error(f"{prefix}: rating is not numeric")
    elif not is_finite_number(rating):
        audit.error(f"{prefix}: rating is not finite")
    elif not (0 <= float(rating) <= 10):
        audit.error(f"{prefix}: rating {rating} outside expected 0..10 range")

    confidence = review.get("confidence")
    if confidence is None:
        audit.warn(f"{prefix}: confidence is null")
    elif not isinstance(confidence, (int, float)) or isinstance(confidence, bool):
        audit.error(f"{prefix}: confidence is not numeric/null")
    elif not is_finite_number(confidence):
        audit.error(f"{prefix}: confidence is not finite")
    elif not (0 <= float(confidence) <= 10):
        audit.error(f"{prefix}: confidence {confidence} outside expected 0..10 range")

    decision = review.get("decision")
    if not isinstance(decision, str) or stripped_string(decision).lower() not in VALID_FINAL_LABELS:
        audit.error(f"{prefix}: decision must be accept/reject, found {decision!r}")
    elif final_label in VALID_FINAL_LABELS and stripped_string(decision).lower() != final_label:
        audit.error(f"{prefix}: review decision {decision!r} does not match paper label {final_label}")

    rebuttal = review.get("rebuttal")
    if not isinstance(rebuttal, str):
        audit.error(f"{prefix}: rebuttal is not a string")

    strengths = review.get("strengths")
    weaknesses = review.get("weaknesses")
    if not isinstance(strengths, list) or not isinstance(weaknesses, list):
        audit.error(f"{prefix}: strengths and weaknesses must both be lists")
        return
    if not strengths and not weaknesses:
        audit.error(f"{prefix}: both strengths and weaknesses are empty")
    elif not strengths:
        audit.warn(f"{prefix}: strengths is empty")
    elif not weaknesses:
        audit.warn(f"{prefix}: weaknesses is empty")

    strength_segment_indexes = {
        key: index
        for index, item in enumerate(strengths)
        if isinstance(item, str) and (key := builder.segment_overlap_key(item))
    }
    weakness_segment_indexes = {
        key: index
        for index, item in enumerate(weaknesses)
        if isinstance(item, str) and (key := builder.segment_overlap_key(item))
    }
    for segment_key in sorted(strength_segment_indexes.keys() & weakness_segment_indexes.keys()):
        audit.error(
            f"{prefix}: segment appears in both strengths[{strength_segment_indexes[segment_key]}] "
            f"and weaknesses[{weakness_segment_indexes[segment_key]}]"
        )

    for side_name, items in (("strengths", strengths), ("weaknesses", weaknesses)):
        seen_segments: dict[str, int] = {}
        for item_index, item in enumerate(items):
            if not isinstance(item, str):
                audit.error(f"{prefix}: {side_name}[{item_index}] is not a string")
                continue
            normalized_item = normalized_segment_text(item)
            if normalized_item and normalized_item in seen_segments:
                audit.error(
                    f"{prefix}: duplicate {side_name} segment at indexes "
                    f"{seen_segments[normalized_item]} and {item_index}"
                )
            seen_segments[normalized_item] = item_index
            if builder.is_placeholder_segment_text(item):
                audit.error(f"{prefix}: {side_name}[{item_index}] is a placeholder segment: {item!r}")
                continue
            if is_bad_segment_marker(item):
                audit.error(f"{prefix}: {side_name}[{item_index}] is a section/rubric marker: {item!r}")


def audit_dataset(data: dict[str, Any], args: argparse.Namespace) -> Audit:
    audit = Audit()
    paper_urls: defaultdict[str, list[str]] = defaultdict(list)
    pdf_urls: defaultdict[str, list[str]] = defaultdict(list)
    paper_dirs: defaultdict[str, list[str]] = defaultdict(list)
    titles: defaultdict[str, list[str]] = defaultdict(list)

    add_distribution_checks(data, audit, args)
    add_key_sequence_checks(data, audit, args)
    add_quality_threshold_checks(data, audit, args)
    for key, record in data.items():
        audit_record(key, record, audit, args, paper_urls, pdf_urls, paper_dirs, titles)

    for url, keys in paper_urls.items():
        if len(keys) > 1:
            audit.error(f"duplicate paper_url {url}: {keys}")
    for url, keys in pdf_urls.items():
        if len(keys) > 1:
            audit.error(f"duplicate pdf_url {url}: {keys}")
    for path, keys in paper_dirs.items():
        if len(keys) > 1:
            audit.error(f"duplicate paper_dir {path}: {keys}")
    for title, keys in titles.items():
        if len(keys) > 1:
            audit.error(f"duplicate title {title!r}: {keys}")

    pdf_inventory = local_pdf_inventory_summary(data, args)
    if pdf_inventory["orphan_pdf_files"]:
        audit.warn(
            "local PDF directory has "
            f"{len(pdf_inventory['orphan_pdf_files'])} unreferenced PDF files: "
            f"{pdf_inventory['orphan_pdf_files'][:20]}"
        )
    if pdf_inventory["invalid_pdf_files"]:
        audit.warn(
            "local PDF directory has "
            f"{len(pdf_inventory['invalid_pdf_files'])} invalid PDF files: "
            f"{pdf_inventory['invalid_pdf_files'][:20]}"
        )

    return audit


def add_quality_threshold_checks(data: dict[str, Any], audit: Audit, args: argparse.Namespace) -> None:
    max_one_sided = getattr(args, "max_one_sided_segments", None)
    if max_one_sided is None or max_one_sided < 0:
        return
    segment_counts = review_segment_summary(data)["counts"]
    one_sided = int(segment_counts.get("one_sided", 0))
    if one_sided > max_one_sided:
        audit.error(f"expected at most {max_one_sided} one-sided segment reviews, found {one_sided}")


def nested_count(counter: Counter[tuple[str, str]]) -> dict[str, dict[str, int]]:
    result: dict[str, dict[str, int]] = {}
    for (outer, inner), count in sorted(counter.items()):
        result.setdefault(outer, {})[inner] = count
    return result


def distribution_summary(data: dict[str, Any]) -> dict[str, Any]:
    by_conference = Counter()
    by_collection = Counter()
    by_final_label = Counter()
    for record in data.values():
        if not isinstance(record, dict):
            continue
        conference = str(record.get("conference") or "missing")
        by_conference[conference] += 1
        by_collection[(conference, normalize_collection_bucket(record.get("collection_decision_category")))] += 1
        by_final_label[(conference, str(record.get("accept_or_not") or "missing").lower())] += 1
    return {
        "conference_counts": dict(sorted(by_conference.items())),
        "collection_bucket_counts": nested_count(by_collection),
        "final_label_counts": nested_count(by_final_label),
    }


def key_slot_summary(data: dict[str, Any], args: argparse.Namespace) -> list[dict[str, Any]]:
    if args.expected_per_collection_label is None or args.expected_per_collection_label < 1:
        return []

    expected_slots = set(range(1, args.expected_per_collection_label + 1))
    summary = []
    for conference in args.expected_conference:
        conference_prefix = conference.lower()
        for bucket in ("accept", "reject"):
            slots = []
            pattern = re.compile(rf"^{re.escape(conference_prefix)}_{bucket}_(\d{{4}})_(\d{{3}})_")
            for key, record in data.items():
                if not isinstance(record, dict):
                    continue
                if str(record.get("conference") or "") != conference:
                    continue
                if normalize_collection_bucket(record.get("collection_decision_category")) != bucket:
                    continue
                match = pattern.match(key)
                if match:
                    slots.append(int(match.group(2)))

            duplicates = sorted(slot for slot, count in Counter(slots).items() if count > 1)
            summary.append(
                {
                    "conference": conference,
                    "bucket": bucket,
                    "present_slots": [f"{slot:03d}" for slot in sorted(set(slots))],
                    "missing_slots": [f"{slot:03d}" for slot in sorted(expected_slots - set(slots))],
                    "duplicate_slots": [f"{slot:03d}" for slot in duplicates],
                }
            )
    return summary


def duplicate_summary(data: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    paper_urls: defaultdict[str, list[str]] = defaultdict(list)
    pdf_urls: defaultdict[str, list[str]] = defaultdict(list)
    paper_dirs: defaultdict[str, list[str]] = defaultdict(list)
    titles: defaultdict[str, list[str]] = defaultdict(list)
    for key, record in data.items():
        if not isinstance(record, dict):
            continue
        paper_url = str(record.get("paper_url") or "").strip()
        if paper_url:
            paper_urls[paper_url].append(key)
        pdf_url = str(record.get("pdf_url") or "").strip()
        if pdf_url:
            pdf_urls[pdf_url].append(key)
        paper_dir = str(record.get("paper_dir") or "").strip()
        if paper_dir:
            paper_dirs[paper_dir].append(key)
        title = str(record.get("title") or "").strip().lower()
        if title:
            titles[title].append(key)
    return {
        "paper_urls": [
            {"value": value, "keys": keys}
            for value, keys in sorted(paper_urls.items())
            if len(keys) > 1
        ],
        "pdf_urls": [
            {"value": value, "keys": keys}
            for value, keys in sorted(pdf_urls.items())
            if len(keys) > 1
        ],
        "paper_dirs": [
            {"value": value, "keys": keys}
            for value, keys in sorted(paper_dirs.items())
            if len(keys) > 1
        ],
        "titles": [
            {"value": value, "keys": keys}
            for value, keys in sorted(titles.items())
            if len(keys) > 1
        ],
    }


def review_segment_summary(data: dict[str, Any]) -> dict[str, Any]:
    counts = Counter()
    by_conference: defaultdict[str, Counter[str]] = defaultdict(Counter)
    problem_reviews = []
    for key, record in data.items():
        if not isinstance(record, dict):
            continue
        conference = str(record.get("conference") or "missing")
        reviews = record.get("reviews")
        if not isinstance(reviews, list):
            continue
        for index, review in enumerate(reviews):
            counts["total_reviews"] += 1
            by_conference[conference]["total_reviews"] += 1
            if not isinstance(review, dict):
                continue

            strengths_empty = not isinstance(review.get("strengths"), list) or not review.get("strengths")
            weaknesses_empty = not isinstance(review.get("weaknesses"), list) or not review.get("weaknesses")
            missing = []
            if strengths_empty:
                missing.append("strengths")
                counts["empty_strengths"] += 1
                by_conference[conference]["empty_strengths"] += 1
            if weaknesses_empty:
                missing.append("weaknesses")
                counts["empty_weaknesses"] += 1
                by_conference[conference]["empty_weaknesses"] += 1
            if strengths_empty and weaknesses_empty:
                counts["empty_both"] += 1
                by_conference[conference]["empty_both"] += 1
            elif strengths_empty or weaknesses_empty:
                counts["one_sided"] += 1
                by_conference[conference]["one_sided"] += 1

            if missing:
                problem_reviews.append(
                    {
                        "key": key,
                        "review_index": index,
                        "missing": missing,
                        "title": record.get("title"),
                        "conference": conference,
                        "paper_url": record.get("paper_url"),
                        "reviewer_id": review.get("reviewer_id"),
                        "rating": review.get("rating"),
                    }
                )

    return {
        "counts": dict(sorted(counts.items())),
        "by_conference": {key: dict(sorted(value.items())) for key, value in sorted(by_conference.items())},
        "problem_reviews": problem_reviews,
    }


def review_metadata_summary(data: dict[str, Any]) -> dict[str, Any]:
    counts = Counter()
    by_conference: defaultdict[str, Counter[str]] = defaultdict(Counter)
    for record in data.values():
        if not isinstance(record, dict):
            continue
        conference = str(record.get("conference") or "missing")
        reviews = record.get("reviews")
        if not isinstance(reviews, list):
            continue
        for review in reviews:
            counts["total_reviews"] += 1
            by_conference[conference]["total_reviews"] += 1
            if not isinstance(review, dict):
                counts["invalid_review_objects"] += 1
                by_conference[conference]["invalid_review_objects"] += 1
                continue

            rating = review.get("rating")
            if is_finite_number(rating):
                counts["finite_ratings"] += 1
                by_conference[conference]["finite_ratings"] += 1
            else:
                counts["invalid_ratings"] += 1
                by_conference[conference]["invalid_ratings"] += 1

            confidence = review.get("confidence")
            if confidence is None:
                counts["null_confidence"] += 1
                by_conference[conference]["null_confidence"] += 1
            elif is_finite_number(confidence):
                counts["finite_confidence"] += 1
                by_conference[conference]["finite_confidence"] += 1
            else:
                counts["invalid_confidence"] += 1
                by_conference[conference]["invalid_confidence"] += 1

    return {
        "counts": dict(sorted(counts.items())),
        "by_conference": {key: dict(sorted(value.items())) for key, value in sorted(by_conference.items())},
    }


def quality_summary(data: dict[str, Any], args: argparse.Namespace) -> dict[str, Any]:
    return {
        "distributions": distribution_summary(data),
        "key_slots": key_slot_summary(data, args),
        "duplicates": duplicate_summary(data),
        "local_pdfs": local_pdf_inventory_summary(data, args),
        "review_metadata": review_metadata_summary(data),
        "review_segments": review_segment_summary(data),
    }


def audit_criteria(args: argparse.Namespace) -> dict[str, Any]:
    return {
        "reviews_per_paper": args.reviews_per_paper,
        "expected_total": args.expected_total,
        "expected_year": expected_year(args),
        "expected_conference": args.expected_conference,
        "expected_per_conference": args.expected_per_conference,
        "expected_per_collection_label": args.expected_per_collection_label,
        "expected_per_final_label": args.expected_per_final_label,
        "max_one_sided_segments": getattr(args, "max_one_sided_segments", None),
        "pdf_dir": str(args.pdf_dir) if args.pdf_dir else None,
    }


def warning_category(message: str) -> str:
    if message.startswith("conference counts:") or message.startswith("collection bucket counts:") or message.startswith(
        "final label counts:"
    ):
        return "distribution"
    if "confidence is null" in message:
        return "confidence_null"
    if "strengths is empty" in message or "weaknesses is empty" in message:
        return "one_sided_segments"
    if message.startswith("local PDF directory has"):
        return "local_pdf_inventory"
    return "other"


def warning_breakdown(messages: list[str]) -> dict[str, int]:
    counts = Counter(warning_category(message) for message in messages)
    return dict(sorted(counts.items()))


def print_messages(label: str, messages: list[str], limit: int) -> None:
    print(f"{label}: {len(messages)}")
    for message in messages[:limit]:
        print(f"  - {message}")
    if len(messages) > limit:
        print(f"  ... {len(messages) - limit} more")


def audit_to_report(path: Path, data: dict[str, Any], audit: Audit, args: argparse.Namespace) -> dict[str, Any]:
    return {
        "input": str(path),
        "records": len(data),
        "passed": not audit.errors,
        "error_count": len(audit.errors),
        "warning_count": len(audit.warnings),
        "warning_breakdown": warning_breakdown(audit.warnings),
        "criteria": audit_criteria(args),
        "summary": quality_summary(data, args),
        "errors": audit.errors,
        "warnings": audit.warnings,
    }


def write_json_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--reviews-per-paper", type=int, default=3)
    parser.add_argument("--expected-total", type=int, default=300)
    parser.add_argument(
        "--expected-year",
        type=int,
        default=DEFAULT_EXPECTED_YEAR,
        help="Expected publication/review year for every record. Use -1 to skip this check.",
    )
    parser.add_argument("--expected-conference", nargs="+", default=["ICLR", "ICML", "NeurIPS"])
    parser.add_argument("--expected-per-conference", type=int, default=100)
    parser.add_argument("--expected-per-collection-label", type=int, default=50)
    parser.add_argument(
        "--expected-per-final-label",
        type=int,
        default=50,
        help="Expected final accept/reject count per conference. Use -1 to skip this balance check.",
    )
    parser.add_argument("--pdf-dir", type=Path, default=Path("data/openreview_pdf"))
    parser.add_argument(
        "--max-one-sided-segments",
        type=int,
        help=(
            "Optional stricter release gate: fail if more than this many reviews have only strengths "
            "or only weaknesses. Omit or pass -1 to skip."
        ),
    )
    parser.add_argument("--warn-only", action="store_true", help="Always exit 0, even when hard errors are found.")
    parser.add_argument("--max-messages", type=int, default=40)
    parser.add_argument("--json-output", type=Path, help="Optional path to write the complete audit report as JSON.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    path = Path(args.input)
    data = load_dataset(path)
    audit = audit_dataset(data, args)

    print(f"Dataset audit: {path}")
    print(f"Records: {len(data)}")
    print_messages("Errors", audit.errors, args.max_messages)
    print_messages("Warnings", audit.warnings, args.max_messages)
    if args.json_output:
        write_json_report(args.json_output, audit_to_report(path, data, audit, args))
        print(f"Wrote JSON audit report to {args.json_output}")
    if audit.errors and not args.warn_only:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Convert NLPeer ARR-22 reviews into a simple JSONL peer-review benchmark.

The converter intentionally uses only structured NLPeer review fields:
strength-like report fields, weakness-like report fields, and overall scores.
It does not infer, summarize, or heuristically split unstructured review text.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from collections.abc import Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional, Union


LABEL_NOTES = (
    "ARR-22 accept_or_not is constant and should not be used for "
    "accept/reject prediction."
)

LEADING_NUMBER_RE = re.compile(r"^\s*(-?(?:\d+(?:\.\d*)?|\.\d+))")


@dataclass
class ConversionStats:
    total_papers_seen: int = 0
    papers_exported: int = 0
    total_reviews_seen: int = 0
    reviews_exported: int = 0
    reviews_skipped_missing_strengths: int = 0
    reviews_skipped_missing_weaknesses: int = 0
    reviews_skipped_missing_score: int = 0
    score_distribution: Counter = field(default_factory=Counter)
    paper_score_distribution: Counter = field(default_factory=Counter)
    accept_or_not_distribution: Counter = field(default_factory=Counter)
    strength_field_distribution: Counter = field(default_factory=Counter)
    weakness_field_distribution: Counter = field(default_factory=Counter)
    score_field_distribution: Counter = field(default_factory=Counter)

    def to_json(self, dataset_request: str, dataset_key: str, version: int) -> dict[str, Any]:
        return {
            "dataset_request": dataset_request,
            "resolved_dataset_key": dataset_key,
            "version": version,
            "total_papers_seen": self.total_papers_seen,
            "papers_exported": self.papers_exported,
            "total_reviews_seen": self.total_reviews_seen,
            "reviews_exported": self.reviews_exported,
            "reviews_skipped_missing_strengths": self.reviews_skipped_missing_strengths,
            "reviews_skipped_missing_weaknesses": self.reviews_skipped_missing_weaknesses,
            "reviews_skipped_missing_score": self.reviews_skipped_missing_score,
            "score_distribution": dict(sorted(self.score_distribution.items())),
            "paper_score_distribution": dict(sorted(self.paper_score_distribution.items())),
            "accept_or_not_distribution": dict(sorted(self.accept_or_not_distribution.items())),
            "field_distributions": {
                "strength_fields": dict(sorted(self.strength_field_distribution.items())),
                "weakness_fields": dict(sorted(self.weakness_field_distribution.items())),
                "score_fields": dict(sorted(self.score_field_distribution.items())),
            },
            "warnings": [
                LABEL_NOTES,
                (
                    "Only reviews with structured strengths, structured weaknesses, "
                    "and parseable overall scores are exported."
                ),
            ],
        }


@dataclass(frozen=True)
class DatasetOption:
    key: str
    value: Any
    labels: tuple[str, ...]


@dataclass(frozen=True)
class ReviewExtraction:
    review: dict[str, Any]
    score: float
    strength_fields: tuple[str, ...]
    weakness_fields: tuple[str, ...]
    score_field: str


def import_nlpeer() -> tuple[Any, Any, Any]:
    try:
        from nlpeer import DATASETS, PAPERFORMATS, PaperReviewDataset
    except ImportError as exc:
        raise SystemExit(
            "Missing dependency: nlpeer. Install the official package with "
            "`pip install git+https://github.com/UKPLab/nlpeer`."
        ) from exc
    return DATASETS, PAPERFORMATS, PaperReviewDataset


def normalize_lookup(text: Any) -> str:
    return re.sub(r"[^a-z0-9]+", "", str(text).lower())


def normalize_field_name(name: Any) -> str:
    """Normalize NLPeer field names without inventing semantic aliases."""
    return re.sub(r"[\s_-]+", "", str(name).lower())


def iter_dataset_options(data_sets: Any) -> list[DatasetOption]:
    raw_items: list[tuple[str, Any]] = []
    if isinstance(data_sets, Mapping):
        raw_items = [(str(key), value) for key, value in data_sets.items()]
    elif hasattr(data_sets, "__members__"):
        raw_items = [(str(key), value) for key, value in data_sets.__members__.items()]
    else:
        for attr in dir(data_sets):
            if attr.startswith("_"):
                continue
            value = getattr(data_sets, attr)
            if callable(value):
                continue
            raw_items.append((attr, value))

    options = []
    seen = set()
    for key, value in raw_items:
        labels = [key, str(value)]
        for attr in ("name", "value"):
            label = getattr(value, attr, None)
            if label is not None:
                labels.append(str(label))
        unique_labels = tuple(dict.fromkeys(label for label in labels if label))
        identity = (key, repr(value))
        if identity in seen:
            continue
        seen.add(identity)
        options.append(DatasetOption(key=key, value=value, labels=unique_labels))
    return options


def resolve_dataset_option(data_sets: Any, requested: str) -> DatasetOption:
    options = iter_dataset_options(data_sets)
    requested_norm = normalize_lookup(requested)
    if not options:
        raise SystemExit("Could not inspect nlpeer.DATASETS; no dataset options were found.")

    def label_norms(option: DatasetOption) -> list[str]:
        return [normalize_lookup(label) for label in option.labels]

    for option in options:
        if requested_norm in label_norms(option):
            return option

    for option in options:
        norms = label_norms(option)
        if any(requested_norm in norm or norm in requested_norm for norm in norms):
            return option

    if requested_norm == "arr22":
        for option in options:
            norms = label_norms(option)
            if any("arr22" in norm or ("arr" in norm and "22" in norm) for norm in norms):
                return option

    available = ", ".join(option.key for option in options)
    raise SystemExit(f"Could not resolve dataset {requested!r} from nlpeer.DATASETS: {available}")


def is_arr22_option(option: DatasetOption) -> bool:
    norms = [normalize_lookup(label) for label in option.labels]
    return any(norm == "arr22" or ("arr" in norm and "22" in norm) for norm in norms)


def display_dataset_name(dataset_key: str) -> str:
    return "ARR-22" if normalize_lookup(dataset_key) == "arr22" else dataset_key


def paper_id_prefix(dataset_key: str) -> str:
    display = display_dataset_name(dataset_key)
    if normalize_lookup(display) == "arr22":
        return "arr22"
    return re.sub(r"[^a-z0-9]+", "_", display.lower()).strip("_")


def get_field(obj: Any, key: str, default: Any = None) -> Any:
    if isinstance(obj, Mapping):
        return obj.get(key, default)
    return getattr(obj, key, default)


def clean_text(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    return re.sub(r"\s+", " ", value).strip()


def extract_text_items(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        text = clean_text(value)
        return [text] if text else []
    if isinstance(value, Mapping):
        if "value" in value:
            return extract_text_items(value["value"])
        return []
    if isinstance(value, (list, tuple)):
        items = []
        for item in value:
            items.extend(extract_text_items(item))
        return items
    text = clean_text(str(value))
    return [text] if text else []


def dedupe_preserve_order(items: list[str]) -> list[str]:
    seen = set()
    deduped = []
    for item in items:
        normalized = item.lower()
        if normalized in seen:
            continue
        seen.add(normalized)
        deduped.append(item)
    return deduped


def extract_report_texts(report: Any, needle: str) -> tuple[list[str], tuple[str, ...]]:
    if not isinstance(report, Mapping):
        return [], ()

    texts = []
    fields = []
    for key, value in report.items():
        if needle not in normalize_field_name(key):
            continue
        field_texts = extract_text_items(value)
        if not field_texts:
            continue
        fields.append(str(key))
        texts.extend(field_texts)
    return dedupe_preserve_order(texts), tuple(fields)


def parse_numeric_score(value: Any) -> Optional[float]:
    if value is None or isinstance(value, bool):
        return None
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, Mapping):
        if "value" in value:
            return parse_numeric_score(value["value"])
        return None
    if isinstance(value, (list, tuple)) and len(value) == 1:
        return parse_numeric_score(value[0])
    if isinstance(value, str):
        match = LEADING_NUMBER_RE.match(value)
        return float(match.group(1)) if match else None
    return None


def extract_overall_score(scores: Any) -> tuple[Optional[float], Optional[str]]:
    if not isinstance(scores, Mapping):
        return None, None

    if "overall" in scores:
        return parse_numeric_score(scores["overall"]), "overall"

    for key, value in scores.items():
        if "overall" in normalize_field_name(key):
            return parse_numeric_score(value), str(key)
    return None, None


def reviewer_id(review: Any, paper_id: Any, review_index: int) -> str:
    rid = get_field(review, "rid")
    if rid is not None:
        rid_text = str(rid).strip()
        if rid_text:
            return rid_text
    digest = hashlib.sha1(f"{paper_id}:{review_index}".encode("utf-8")).hexdigest()[:12]
    return f"anonymous_{digest}"


def extract_structured_review(
    review: Any,
    paper_id: Any,
    review_index: int,
) -> tuple[Optional[ReviewExtraction], tuple[str, ...]]:
    report = get_field(review, "report", {})
    scores = get_field(review, "scores", {})

    strengths, strength_fields = extract_report_texts(report, "strength")
    weaknesses, weakness_fields = extract_report_texts(report, "weakness")
    score, score_field = extract_overall_score(scores)

    missing = []
    if not strengths:
        missing.append("missing_strengths")
    if not weaknesses:
        missing.append("missing_weaknesses")
    if score is None:
        missing.append("missing_score")

    if missing:
        return None, tuple(missing)

    extracted = ReviewExtraction(
        review={
            "reviewer_id": reviewer_id(review, paper_id, review_index),
            "strengths": strengths,
            "weaknesses": weaknesses,
        },
        score=score,
        strength_fields=strength_fields,
        weakness_fields=weakness_fields,
        score_field=score_field or "overall",
    )
    return extracted, ()


def json_number(value: float) -> Union[int, float]:
    rounded = round(float(value), 4)
    if rounded == 0:
        rounded = 0.0
    return int(rounded) if rounded.is_integer() else rounded


def score_key(value: float) -> str:
    number = json_number(value)
    return str(number)


def validate_record(record: dict[str, Any]) -> None:
    for key in ("paper_id", "accept_or_not", "score", "reviews"):
        assert key in record, f"missing required record key: {key}"
    assert isinstance(record["paper_id"], str) and record["paper_id"], "paper_id must be non-empty"
    assert record["accept_or_not"] == "accept", "ARR-22 accept_or_not must be accept"
    assert isinstance(record["score"], (int, float)) and not isinstance(record["score"], bool), (
        "score must be numeric"
    )
    assert isinstance(record["reviews"], list) and record["reviews"], "reviews must be a non-empty list"

    for review in record["reviews"]:
        for key in ("reviewer_id", "strengths", "weaknesses"):
            assert key in review, f"missing required review key: {key}"
        assert isinstance(review["reviewer_id"], str) and review["reviewer_id"], (
            "reviewer_id must be non-empty"
        )
        for key in ("strengths", "weaknesses"):
            values = review[key]
            assert isinstance(values, list) and values, f"{key} must be a non-empty list"
            assert all(isinstance(item, str) and item.strip() for item in values), (
                f"{key} must contain only non-empty strings"
            )


def load_paper_review_dataset(
    nlpeer_root: Path,
    dataset_value: Any,
    version: int,
    paper_formats: Any,
    paper_review_dataset_cls: Any,
) -> Any:
    paper_format = getattr(paper_formats, "ITG")
    try:
        return paper_review_dataset_cls(
            str(nlpeer_root),
            dataset_value,
            version=version,
            paper_format=paper_format,
        )
    except TypeError:
        return paper_review_dataset_cls(str(nlpeer_root), dataset_value, version, paper_format)


def convert_dataset(args: argparse.Namespace) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    data_sets, paper_formats, paper_review_dataset_cls = import_nlpeer()
    dataset_option = resolve_dataset_option(data_sets, args.dataset)
    if not is_arr22_option(dataset_option):
        raise SystemExit(
            f"This converter supports ARR-22 only, but {args.dataset!r} resolved to "
            f"{dataset_option.key!r}."
        )
    data = load_paper_review_dataset(
        nlpeer_root=Path(args.nlpeer_root),
        dataset_value=dataset_option.value,
        version=args.version,
        paper_formats=paper_formats,
        paper_review_dataset_cls=paper_review_dataset_cls,
    )

    stats = ConversionStats()
    records = []
    dataset_display = display_dataset_name(dataset_option.key)
    prefix = paper_id_prefix(dataset_option.key)

    for paper_id, meta, paper, reviews in data:
        del meta, paper
        stats.total_papers_seen += 1
        valid_reviews = []
        scores = []

        for review_index, review in enumerate(reviews or []):
            stats.total_reviews_seen += 1
            extracted, missing = extract_structured_review(review, paper_id, review_index)
            if "missing_strengths" in missing:
                stats.reviews_skipped_missing_strengths += 1
            if "missing_weaknesses" in missing:
                stats.reviews_skipped_missing_weaknesses += 1
            if "missing_score" in missing:
                stats.reviews_skipped_missing_score += 1
            if extracted is None:
                continue

            valid_reviews.append(extracted.review)
            scores.append(extracted.score)
            stats.reviews_exported += 1
            stats.score_distribution[score_key(extracted.score)] += 1
            stats.strength_field_distribution.update(extracted.strength_fields)
            stats.weakness_field_distribution.update(extracted.weakness_fields)
            stats.score_field_distribution[extracted.score_field] += 1

        if not valid_reviews:
            continue

        paper_score = json_number(sum(scores) / len(scores))
        record = {
            "paper_id": f"{prefix}_{paper_id}",
            "accept_or_not": "accept",
            "score": paper_score,
            "reviews": valid_reviews,
            "meta": {
                "source_dataset": dataset_display,
                "source_dataset_key": dataset_option.key,
                "source_version": args.version,
                "original_paper_id": str(paper_id),
                "num_reviews": len(valid_reviews),
                "score_source": "overall",
                "label_notes": LABEL_NOTES,
            },
        }
        validate_record(record)
        records.append(record)
        stats.papers_exported += 1
        stats.paper_score_distribution[score_key(float(paper_score))] += 1
        stats.accept_or_not_distribution["accept"] += 1

    stats_json = stats.to_json(
        dataset_request=args.dataset,
        dataset_key=dataset_option.key,
        version=args.version,
    )
    return records, stats_json


def write_jsonl(records: list[dict[str, Any]], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        for record in records:
            json.dump(record, handle, ensure_ascii=False, sort_keys=True)
            handle.write("\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--nlpeer-root", required=True, help="Path to the downloaded NLPeer root directory.")
    parser.add_argument("--out", required=True, help="Output JSONL path.")
    parser.add_argument("--stats-out", required=True, help="Output stats JSON path.")
    parser.add_argument(
        "--dataset",
        default="ARR22",
        help="Requested NLPeer dataset key; resolved against nlpeer.DATASETS. Default: ARR22.",
    )
    parser.add_argument("--version", type=int, default=1, help="NLPeer paper version to read. Default: 1.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    records, stats = convert_dataset(args)

    out_path = Path(args.out)
    stats_path = Path(args.stats_out)
    write_jsonl(records, out_path)
    stats_path.parent.mkdir(parents=True, exist_ok=True)
    stats_path.write_text(json.dumps(stats, indent=2, ensure_ascii=False, sort_keys=True), encoding="utf-8")

    print(
        f"Wrote {len(records)} papers and {stats['reviews_exported']} reviews to {out_path}; "
        f"stats written to {stats_path}."
    )
    if stats["accept_or_not_distribution"].get("accept"):
        print(f"Warning: {LABEL_NOTES}", file=sys.stderr)


if __name__ == "__main__":
    main()

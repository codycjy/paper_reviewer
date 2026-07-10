#!/usr/bin/env python3
"""
Offline cleanup for existing OpenReview evaluation JSON files.

This script does not call OpenReview or an LLM. It only fixes local artifacts
that can be corrected from the dataset itself:
  * stale collection_decision_category values that conflict with the paper key,
  * old policy override labels when the benchmark should track explicit decisions,
  * section/rubric markers leaked into strengths/weaknesses,
  * stale per-review decision labels and average paper scores.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import scripts.build_openreview_eval_dataset as builder
import scripts.repair_openreview_eval_dataset as repair


DEFAULT_INPUT = "eval/openreview_2025_300_qwen.json"


@dataclass
class CleanStats:
    records: int = 0
    changed_records: int = 0
    collection_recovered: int = 0
    policy_overrides_dropped: int = 0
    review_decisions_updated: int = 0
    scores_recomputed: int = 0
    segment_items_removed: int = 0
    empty_segment_reviews: int = 0


def load_dataset(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit(f"{path} must contain a JSON object keyed by paper id.")
    return data


def write_dataset(path: Path, dataset: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(dataset, indent=2, ensure_ascii=False), encoding="utf-8")


def count_segment_items(reviews: list[Any]) -> int:
    count = 0
    for review in reviews:
        if isinstance(review, dict):
            for key in ("strengths", "weaknesses"):
                value = review.get(key)
                if isinstance(value, list):
                    count += len(value)
    return count


def clean_record(key: str, record: Any, keep_policy_overrides: bool, stats: CleanStats) -> Any:
    if not isinstance(record, dict):
        return record

    original = json.dumps(record, sort_keys=True, ensure_ascii=False)
    cleaned = dict(record)
    collection_category, collection_warning = repair.resolve_collection_category(key, cleaned)
    if collection_warning:
        stats.collection_recovered += 1
    cleaned["collection_decision_category"] = collection_category

    final_label = str(cleaned.get("accept_or_not") or "").strip().lower()
    collection_bucket = repair.normalize_collection_bucket(collection_category)
    has_policy_override = bool(cleaned.get("decision_override_reason"))
    if has_policy_override and not keep_policy_overrides and collection_bucket == "reject":
        final_label = "reject"
        cleaned["accept_or_not"] = final_label
        cleaned.pop("decision_override_reason", None)
        stats.policy_overrides_dropped += 1
    elif final_label in {"accept", "reject"}:
        cleaned["accept_or_not"] = final_label

    reviews = cleaned.get("reviews")
    if isinstance(reviews, list):
        before_items = count_segment_items(reviews)
        reviews = repair.sanitize_reviews(reviews)
        after_items = count_segment_items(reviews)
        stats.segment_items_removed += max(0, before_items - after_items)

        for review in reviews:
            if not isinstance(review, dict):
                continue
            if final_label in {"accept", "reject"} and review.get("decision") != final_label:
                review["decision"] = final_label
                stats.review_decisions_updated += 1
            if not review.get("strengths") and not review.get("weaknesses"):
                stats.empty_segment_reviews += 1
        cleaned["reviews"] = reviews

        score = builder.average_rating(reviews)
        if cleaned.get("score") != score:
            cleaned["score"] = score
            stats.scores_recomputed += 1

    if json.dumps(cleaned, sort_keys=True, ensure_ascii=False) != original:
        stats.changed_records += 1
    return cleaned


def clean_dataset(dataset: dict[str, Any], keep_policy_overrides: bool) -> tuple[dict[str, Any], CleanStats]:
    stats = CleanStats(records=len(dataset))
    cleaned = {
        key: clean_record(key, record, keep_policy_overrides=keep_policy_overrides, stats=stats)
        for key, record in dataset.items()
    }
    return cleaned, stats


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--output", required=True)
    parser.add_argument(
        "--keep-policy-overrides",
        action="store_true",
        help="Keep legacy decision_override_reason labels instead of restoring explicit reject labels.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    dataset = load_dataset(Path(args.input))
    cleaned, stats = clean_dataset(dataset, keep_policy_overrides=args.keep_policy_overrides)
    write_dataset(Path(args.output), cleaned)
    print(f"Wrote {len(cleaned)} records to {args.output}")
    print(
        "Cleanup summary: "
        f"changed_records={stats.changed_records}, "
        f"collection_recovered={stats.collection_recovered}, "
        f"policy_overrides_dropped={stats.policy_overrides_dropped}, "
        f"review_decisions_updated={stats.review_decisions_updated}, "
        f"scores_recomputed={stats.scores_recomputed}, "
        f"segment_items_removed={stats.segment_items_removed}, "
        f"empty_segment_reviews={stats.empty_segment_reviews}"
    )


if __name__ == "__main__":
    main()

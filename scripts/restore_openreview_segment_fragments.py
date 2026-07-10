#!/usr/bin/env python3
"""
Restore fragmented review strength/weakness items from cleaner source datasets.

This is an offline repair helper for cases where a previous segmentation pass
split one numbered review point into several sentence fragments, or dropped the
leading sentence of a point. It does not call OpenReview or an LLM.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, urlparse


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import scripts.repair_openreview_eval_dataset as repair


def load_dataset(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit(f"{path} must contain a JSON object keyed by paper id.")
    return data


def write_dataset(path: Path, dataset: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(f"{path.name}.tmp")
    tmp_path.write_text(json.dumps(dataset, indent=2, ensure_ascii=False), encoding="utf-8")
    tmp_path.replace(path)


def forum_id(record: dict[str, Any]) -> str:
    for key in ("paper_url", "pdf_url"):
        value = str(record.get(key) or "")
        if not value:
            continue
        parsed = urlparse(value)
        query_id = parse_qs(parsed.query).get("id")
        if query_id and query_id[0]:
            return query_id[0]
    return ""


def normalized_title(record: dict[str, Any]) -> str:
    return re.sub(r"\s+", " ", str(record.get("title") or "").strip().lower())


def record_keys(record: dict[str, Any]) -> list[str]:
    keys = []
    forum = forum_id(record)
    if forum:
        keys.append(f"forum:{forum}")
    title = normalized_title(record)
    if title:
        keys.append(f"title:{title}")
    return keys


def review_key(review: dict[str, Any], index: int) -> str:
    reviewer_id = str(review.get("reviewer_id") or "").strip()
    if reviewer_id:
        return f"reviewer:{reviewer_id}"
    rating = review.get("rating")
    confidence = review.get("confidence")
    return f"index:{index}:rating:{rating}:confidence:{confidence}"


def compare_text(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(text or "").lower()).strip()


def text_contains(container: str, contained: str) -> bool:
    container_norm = compare_text(container)
    contained_norm = compare_text(contained)
    return bool(contained_norm) and contained_norm in container_norm


def sanitized_field(review: dict[str, Any], field: str) -> list[str]:
    items, _ = repair.trim_segment_items(review.get(field), field)
    return items


def field_restore_score(target_items: list[str], source_items: list[str]) -> int:
    if not target_items or not source_items or target_items == source_items:
        return 0
    target_chars = sum(len(item) for item in target_items)
    source_chars = sum(len(item) for item in source_items)
    if source_chars <= target_chars:
        return 0

    exact_matches = 0
    expanded_matches = 0
    for target in target_items:
        target_norm = compare_text(target)
        if not target_norm:
            continue
        for source in source_items:
            source_norm = compare_text(source)
            if target_norm == source_norm:
                exact_matches += 1
                break
            if target_norm in source_norm and len(source_norm) >= len(target_norm) + 20:
                expanded_matches += 1
                break

    source_covers_target = exact_matches + expanded_matches
    if expanded_matches >= 2:
        return 1000 + expanded_matches * 10 + source_covers_target
    if expanded_matches >= 1 and source_covers_target >= max(2, len(target_items) // 2):
        return 500 + expanded_matches * 10 + source_covers_target
    return 0


def add_dataset_to_source_index(
    index: dict[tuple[str, str], list[dict[str, Any]]],
    dataset: dict[str, Any],
) -> None:
    for record in dataset.values():
        if not isinstance(record, dict):
            continue
        keys = record_keys(record)
        if not keys:
            continue
        reviews = record.get("reviews")
        if not isinstance(reviews, list):
            continue
        for idx, review in enumerate(reviews):
            if not isinstance(review, dict):
                continue
            rkey = review_key(review, idx)
            for key in keys:
                index.setdefault((key, rkey), []).append(review)


def build_source_index_from_dataset_for_test(dataset: dict[str, Any]) -> dict[tuple[str, str], list[dict[str, Any]]]:
    index: dict[tuple[str, str], list[dict[str, Any]]] = {}
    add_dataset_to_source_index(index, dataset)
    return index


def build_source_index(source_paths: list[Path]) -> dict[tuple[str, str], list[dict[str, Any]]]:
    index: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for path in source_paths:
        dataset = load_dataset(path)
        add_dataset_to_source_index(index, dataset)
    return index


@dataclass
class RestoreStats:
    records: int = 0
    changed_records: int = 0
    changed_reviews: int = 0
    restored_fields: int = 0


def restore_dataset(dataset: dict[str, Any], source_index: dict[tuple[str, str], list[dict[str, Any]]]) -> tuple[dict[str, Any], RestoreStats]:
    stats = RestoreStats(records=len(dataset))
    restored: dict[str, Any] = {}
    for record_key, record in dataset.items():
        if not isinstance(record, dict):
            restored[record_key] = record
            continue
        cleaned_record = dict(record)
        reviews = record.get("reviews")
        if not isinstance(reviews, list):
            restored[record_key] = cleaned_record
            continue

        rec_keys = record_keys(record)
        cleaned_reviews = []
        record_changed = False
        for idx, review in enumerate(reviews):
            if not isinstance(review, dict):
                continue
            cleaned_review = dict(review)
            rkey = review_key(review, idx)
            source_reviews = []
            for key in rec_keys:
                source_reviews.extend(source_index.get((key, rkey), []))

            review_changed = False
            for field in ("strengths", "weaknesses"):
                target_items = sanitized_field(cleaned_review, field)
                best_items = target_items
                best_score = 0
                for source_review in source_reviews:
                    source_items = sanitized_field(source_review, field)
                    score = field_restore_score(target_items, source_items)
                    if score > best_score:
                        best_score = score
                        best_items = source_items
                if best_score:
                    cleaned_review[field] = best_items
                    review_changed = True
                    stats.restored_fields += 1
                else:
                    cleaned_review[field] = target_items

            cleaned_reviews.append(cleaned_review)
            if review_changed:
                stats.changed_reviews += 1
                record_changed = True

        cleaned_record["reviews"] = cleaned_reviews
        if record_changed:
            stats.changed_records += 1
        restored[record_key] = cleaned_record
    return restored, stats


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", required=True, help="Dataset JSON to repair.")
    parser.add_argument("--output", required=True, help="Output path. May be the same as --target.")
    parser.add_argument("--source", action="append", required=True, help="Source JSON with less fragmented review segments. Repeatable.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    target_path = Path(args.target)
    source_paths = [Path(path) for path in args.source]
    source_index = build_source_index(source_paths)
    dataset = load_dataset(target_path)
    restored, stats = restore_dataset(dataset, source_index)
    write_dataset(Path(args.output), restored)
    print(f"Wrote {len(restored)} records to {args.output}")
    print(
        "Restore summary: "
        f"changed_records={stats.changed_records}, "
        f"changed_reviews={stats.changed_reviews}, "
        f"restored_fields={stats.restored_fields}"
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Create a structured repair plan for an OpenReview evaluation dataset candidate.

The output is JSON so the last few quality issues can be tracked explicitly
while OpenReview/Qwen access is being fixed.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import scripts.audit_openreview_eval_dataset as audit


DEFAULT_INPUT = "eval/openreview_2025_300_qwen.cleaned.json"
DEFAULT_EXPECTED_YEAR = 2025


def load_dataset(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit(f"{path} must contain a JSON object keyed by paper id.")
    return data


def missing_slots(
    data: dict[str, Any],
    conferences: list[str],
    expected_per_collection_label: int,
) -> list[dict[str, Any]]:
    expected = set(range(1, expected_per_collection_label + 1))
    items = []
    for conference in conferences:
        conference_prefix = conference.lower()
        for bucket in ("accept", "reject"):
            pattern = re.compile(rf"^{re.escape(conference_prefix)}_{bucket}_(\d{{4}})_(\d{{3}})_")
            slots = []
            for key, record in data.items():
                if not isinstance(record, dict):
                    continue
                if str(record.get("conference") or "") != conference:
                    continue
                if audit.normalize_collection_bucket(record.get("collection_decision_category")) != bucket:
                    continue
                match = pattern.match(key)
                if match:
                    slots.append(int(match.group(2)))
            missing = sorted(expected - set(slots))
            duplicates = sorted(slot for slot, count in Counter(slots).items() if count > 1)
            if missing or duplicates:
                items.append(
                    {
                        "conference": conference,
                        "bucket": bucket,
                        "missing_slots": [f"{slot:03d}" for slot in missing],
                        "duplicate_slots": [f"{slot:03d}" for slot in duplicates],
                    }
                )
    return items


def empty_segment_reviews(data: dict[str, Any]) -> list[dict[str, Any]]:
    items = []
    for key, record in data.items():
        if not isinstance(record, dict):
            continue
        for index, review in enumerate(record.get("reviews") or []):
            if not isinstance(review, dict):
                continue
            if not review.get("strengths") and not review.get("weaknesses"):
                items.append(
                    {
                        "key": key,
                        "review_index": index,
                        "title": record.get("title"),
                        "conference": record.get("conference"),
                        "paper_url": record.get("paper_url"),
                        "rating": review.get("rating"),
                        "reviewer_id": review.get("reviewer_id"),
                    }
                )
    return items


def one_sided_segment_reviews(data: dict[str, Any]) -> list[dict[str, Any]]:
    items = []
    for key, record in data.items():
        if not isinstance(record, dict):
            continue
        for index, review in enumerate(record.get("reviews") or []):
            if not isinstance(review, dict):
                continue
            strengths_empty = not review.get("strengths")
            weaknesses_empty = not review.get("weaknesses")
            if strengths_empty == weaknesses_empty:
                continue
            missing_side = "strengths" if strengths_empty else "weaknesses"
            items.append(
                {
                    "key": key,
                    "review_index": index,
                    "missing_side": missing_side,
                    "title": record.get("title"),
                    "conference": record.get("conference"),
                    "paper_url": record.get("paper_url"),
                    "rating": review.get("rating"),
                    "reviewer_id": review.get("reviewer_id"),
                }
            )
    return items


def audit_report_path(dataset_path: Path) -> Path:
    if dataset_path.suffix == ".json":
        return dataset_path.with_name(f"{dataset_path.stem}.audit.json")
    return dataset_path.with_name(f"{dataset_path.name}.audit.json")


def missing_venue_specs(plan: dict[str, Any], expected_year: int) -> list[str]:
    seen = set()
    specs = []
    for item in plan.get("missing_slots", []):
        conference = str(item.get("conference") or "").strip()
        if not conference or conference in seen:
            continue
        seen.add(conference)
        specs.append(f"{conference}:{expected_year}")
    return specs


def refill_output_path(plan: dict[str, Any], expected_year: int) -> Path:
    venue_specs = missing_venue_specs(plan, expected_year)
    if len(venue_specs) == 1:
        conference = venue_specs[0].split(":", 1)[0].lower()
        return Path(f"eval/openreview_{expected_year}_{conference}_refill.json")
    return Path(f"eval/openreview_{expected_year}_refill.json")


def make_commands(input_path: Path, plan: dict[str, Any]) -> dict[str, str]:
    bad_review_keys = sorted({item["key"] for item in plan["empty_segment_reviews"]})
    segment_qa_keys = sorted(
        {item["key"] for item in plan.get("one_sided_segment_reviews", [])} - set(bad_review_keys)
    )
    expected_year = int(plan.get("expected_year") or DEFAULT_EXPECTED_YEAR)
    final_candidate_path = Path("eval/openreview_2025_300_qwen.final_candidate.json")
    refill_path = refill_output_path(plan, expected_year)
    commands = {
        "audit": (
            "/opt/miniconda3/envs/paper/bin/python scripts/audit_openreview_eval_dataset.py "
            f"--input {input_path} --expected-year {expected_year} --json-output {audit_report_path(input_path)}"
        ),
        "preflight_external_repairs": (
            "/opt/miniconda3/envs/paper/bin/python scripts/preflight_openreview_eval_repairs.py "
            f"--input {input_path} --expected-year {expected_year} "
            "--json-output eval/openreview_2025_300_qwen.preflight.json"
        )
    }
    if bad_review_keys:
        keys = " ".join(bad_review_keys)
        commands["repair_empty_reviews"] = (
            "/opt/miniconda3/envs/paper/bin/python scripts/repair_openreview_eval_dataset.py "
            f"--input {input_path} "
            "--output eval/openreview_2025_300_qwen.targeted_repair.json "
            f"--only-key {keys} "
            "--use-llm-segmentation --request-delay 5"
        )
    if segment_qa_keys:
        keys = " ".join(segment_qa_keys)
        commands["repair_one_sided_segments_optional"] = (
            "/opt/miniconda3/envs/paper/bin/python scripts/repair_openreview_eval_dataset.py "
            f"--input {input_path} "
            "--output eval/openreview_2025_300_qwen.segment_qa_repair.json "
            f"--only-key {keys} "
            "--use-llm-segmentation --request-delay 5"
        )
    if plan["missing_slots"]:
        venue_specs = " ".join(missing_venue_specs(plan, expected_year))
        commands["rebuild_missing_conference"] = (
            "/opt/miniconda3/envs/paper/bin/python scripts/build_openreview_eval_dataset.py "
            f"--venues {venue_specs} --per-category 50 --max-papers-per-conference 100 "
            f"--output {refill_path} "
            "--use-llm-segmentation --download-pdfs"
        )
    if bad_review_keys or plan["missing_slots"]:
        targeted_arg = (
            "--targeted-repair eval/openreview_2025_300_qwen.targeted_repair.json "
            if bad_review_keys
            else ""
        )
        refill_arg = f"--refill {refill_path} " if plan["missing_slots"] else ""
        commands["apply_repairs"] = (
            "/opt/miniconda3/envs/paper/bin/python scripts/apply_openreview_eval_dataset_repairs.py "
            f"--base {input_path} "
            "--plan eval/openreview_2025_300_qwen.repair_plan.json "
            f"{targeted_arg}"
            f"{refill_arg}"
            "--output eval/openreview_2025_300_qwen.final_candidate.json "
            f"--expected-year {expected_year} "
            "--audit-json-output eval/openreview_2025_300_qwen.final_candidate.audit.json"
        )
        if segment_qa_keys:
            commands["apply_repairs_with_segment_qa_optional"] = (
                commands["apply_repairs"]
                + " --segment-qa-repair eval/openreview_2025_300_qwen.segment_qa_repair.json"
            )
        commands["audit_final_candidate"] = (
            "/opt/miniconda3/envs/paper/bin/python scripts/audit_openreview_eval_dataset.py "
            f"--input {final_candidate_path} --expected-year {expected_year} "
            f"--json-output {audit_report_path(final_candidate_path)}"
        )
        commands["audit_final_candidate_strict_segments_optional"] = (
            commands["audit_final_candidate"] + " --max-one-sided-segments 0"
        )
        commands["promote_final_candidate"] = (
            "/opt/miniconda3/envs/paper/bin/python scripts/promote_openreview_eval_dataset.py "
            f"--candidate {final_candidate_path} "
            "--output eval/openreview_2025_300_qwen.json "
            f"--expected-year {expected_year} "
            "--audit-json-output eval/openreview_2025_300_qwen.audit.json "
            "--manifest-output eval/openreview_2025_300_qwen.manifest.json"
        )
        commands["promote_final_candidate_strict_segments_optional"] = (
            commands["promote_final_candidate"] + " --max-one-sided-segments 0"
        )
    return commands


def build_plan(args: argparse.Namespace) -> dict[str, Any]:
    input_path = Path(args.input)
    data = load_dataset(input_path)
    plan = {
        "input": str(input_path),
        "records": len(data),
        "expected_year": args.expected_year,
        "missing_slots": missing_slots(data, args.expected_conference, args.expected_per_collection_label),
        "empty_segment_reviews": empty_segment_reviews(data),
        "one_sided_segment_reviews": one_sided_segment_reviews(data),
    }
    plan["commands"] = make_commands(input_path, plan)
    return plan


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--expected-year", type=int, default=DEFAULT_EXPECTED_YEAR)
    parser.add_argument("--expected-conference", nargs="+", default=["ICLR", "ICML", "NeurIPS"])
    parser.add_argument("--expected-per-collection-label", type=int, default=50)
    parser.add_argument("--output", help="Optional path to write the JSON plan.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    plan = build_plan(args)
    text = json.dumps(plan, indent=2, ensure_ascii=False)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
        print(f"Wrote repair plan to {args.output}")
    else:
        print(text)


if __name__ == "__main__":
    main()

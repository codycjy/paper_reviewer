#!/usr/bin/env python3
"""
Summarize local readiness for OpenReview/Qwen-backed dataset repair commands.

This script does not call OpenReview or Qwen. It recomputes the repair targets
from the current dataset and reports whether the expected credential variables
are present before running the network-backed repair/refill commands.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import scripts.audit_openreview_eval_dataset as audit
import scripts.plan_openreview_eval_dataset_repairs as planner


DEFAULT_INPUT = "eval/openreview_2025_300_qwen.cleaned.json"
DEFAULT_EXPECTED_CONFERENCES = ["ICLR", "ICML", "NeurIPS"]
DEFAULT_EXPECTED_YEAR = 2025
DEFAULT_LLM_API_KEY_ENV = "DASHSCOPE_API_KEY"


def env_status(llm_api_key_env: str) -> dict[str, Any]:
    qwen_env_names = list(dict.fromkeys([llm_api_key_env, "QWEN_API_KEY", "DASHSCOPE_API_KEY"]))
    qwen_present = [name for name in qwen_env_names if os.getenv(name)]
    openreview_username = bool(os.getenv("OPENREVIEW_USERNAME"))
    openreview_password = bool(os.getenv("OPENREVIEW_PASSWORD"))
    return {
        "openreview_username": openreview_username,
        "openreview_password": openreview_password,
        "openreview_credentials_complete": openreview_username and openreview_password,
        "qwen_api_key_env": llm_api_key_env,
        "qwen_fallback_envs": qwen_env_names,
        "qwen_api_key_available": bool(qwen_present),
        "qwen_api_key_present_envs": qwen_present,
    }


def target_counts(plan: dict[str, Any]) -> dict[str, int]:
    missing_slots = sum(len(item.get("missing_slots") or []) for item in plan.get("missing_slots", []))
    return {
        "missing_slots": missing_slots,
        "missing_slot_groups": len(plan.get("missing_slots", [])),
        "empty_segment_reviews": len(plan.get("empty_segment_reviews", [])),
        "one_sided_segment_reviews": len(plan.get("one_sided_segment_reviews", [])),
    }


def audit_args_from_preflight(args: argparse.Namespace) -> argparse.Namespace:
    return argparse.Namespace(
        reviews_per_paper=args.reviews_per_paper,
        expected_total=args.expected_total,
        expected_year=args.expected_year,
        expected_conference=args.expected_conference,
        expected_per_conference=args.expected_per_conference,
        expected_per_collection_label=args.expected_per_collection_label,
        expected_per_final_label=args.expected_per_final_label,
        max_one_sided_segments=args.max_one_sided_segments,
        pdf_dir=Path(args.pdf_dir) if args.pdf_dir else None,
    )


def build_preflight(args: argparse.Namespace) -> dict[str, Any]:
    data = planner.load_dataset(Path(args.input))
    plan = planner.build_plan(
        argparse.Namespace(
            input=args.input,
            expected_year=args.expected_year,
            expected_conference=args.expected_conference,
            expected_per_collection_label=args.expected_per_collection_label,
            output=None,
        )
    )
    audit_args = audit_args_from_preflight(args)
    audit_result = audit.audit_dataset(data, audit_args)
    environment = env_status(args.llm_api_key_env)
    targets = target_counts(plan)
    required_external = targets["missing_slots"] + targets["empty_segment_reviews"]
    optional_external = targets["one_sided_segment_reviews"]

    notes = []
    if required_external:
        notes.append("Required repairs need OpenReview access and the plan's Qwen-backed commands.")
    if optional_external:
        notes.append("Optional one-sided segment QA also needs OpenReview access and Qwen quota.")
    if required_external and not environment["openreview_credentials_complete"]:
        notes.append(
            "OPENREVIEW_USERNAME/OPENREVIEW_PASSWORD are not both set; a browser challenge may still work, "
            "but this script cannot verify it offline."
        )
    if (required_external or optional_external) and not environment["qwen_api_key_available"]:
        notes.append("No Qwen/DashScope API key environment variable is set.")

    return {
        "input": args.input,
        "records": len(data),
        "audit": {
            "passed": not audit_result.errors,
            "error_count": len(audit_result.errors),
            "warning_count": len(audit_result.warnings),
            "warning_breakdown": audit.warning_breakdown(audit_result.warnings),
        },
        "repair_targets": targets,
        "environment": environment,
        "ready_for_required_external_repairs": (
            required_external == 0
            or (environment["openreview_credentials_complete"] and environment["qwen_api_key_available"])
        ),
        "notes": notes,
        "commands": plan.get("commands", {}),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--expected-year", type=int, default=DEFAULT_EXPECTED_YEAR)
    parser.add_argument("--expected-conference", nargs="+", default=DEFAULT_EXPECTED_CONFERENCES)
    parser.add_argument("--expected-total", type=int, default=300)
    parser.add_argument("--expected-per-conference", type=int, default=100)
    parser.add_argument("--expected-per-collection-label", type=int, default=50)
    parser.add_argument("--expected-per-final-label", type=int, default=50)
    parser.add_argument("--reviews-per-paper", type=int, default=3)
    parser.add_argument("--max-one-sided-segments", type=int)
    parser.add_argument("--pdf-dir", default="data/openreview_pdf")
    parser.add_argument("--llm-api-key-env", default=DEFAULT_LLM_API_KEY_ENV)
    parser.add_argument("--json-output", type=Path)
    parser.add_argument(
        "--strict-env",
        action="store_true",
        help="Exit nonzero when required external repairs remain but OpenReview/Qwen env vars are incomplete.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    report = build_preflight(args)
    text = json.dumps(report, indent=2, ensure_ascii=False)
    if args.json_output:
        args.json_output.parent.mkdir(parents=True, exist_ok=True)
        args.json_output.write_text(text + "\n", encoding="utf-8")
        print(f"Wrote preflight report to {args.json_output}")
    else:
        print(text)
    if args.strict_env and not report["ready_for_required_external_repairs"]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Promote a final OpenReview evaluation dataset candidate after a passing audit.

This is intentionally a narrow final step: it does not repair, fetch, or segment.
It only reruns the offline quality gate, writes the canonical dataset when the
gate passes, and records a manifest with hashes for reproducibility.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import scripts.audit_openreview_eval_dataset as audit


DEFAULT_CANDIDATE = "eval/openreview_2025_300_qwen.final_candidate.json"
DEFAULT_OUTPUT = "eval/openreview_2025_300_qwen.json"
DEFAULT_EXPECTED_CONFERENCES = ["ICLR", "ICML", "NeurIPS"]
DEFAULT_EXPECTED_YEAR = 2025


def load_dataset(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"candidate dataset not found: {path}")
    return audit.load_dataset(path)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def default_audit_report_path(output_path: Path) -> Path:
    if output_path.suffix == ".json":
        return output_path.with_name(f"{output_path.stem}.audit.json")
    return output_path.with_name(f"{output_path.name}.audit.json")


def default_manifest_path(output_path: Path) -> Path:
    if output_path.suffix == ".json":
        return output_path.with_name(f"{output_path.stem}.manifest.json")
    return output_path.with_name(f"{output_path.name}.manifest.json")


def audit_args_from_promote_args(args: argparse.Namespace) -> argparse.Namespace:
    return argparse.Namespace(
        reviews_per_paper=args.reviews_per_paper,
        expected_total=args.expected_total,
        expected_year=args.expected_year,
        expected_conference=args.expected_conference,
        expected_per_conference=args.expected_per_conference,
        expected_per_collection_label=args.expected_per_collection_label,
        expected_per_final_label=args.expected_per_final_label,
        max_one_sided_segments=args.max_one_sided_segments,
        pdf_dir=Path(args.pdf_dir),
    )


def build_manifest(
    args: argparse.Namespace,
    candidate_path: Path,
    output_path: Path,
    audit_report_path: Path,
    report: dict[str, Any],
) -> dict[str, Any]:
    return {
        "promoted_at_utc": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "candidate": str(candidate_path),
        "output": str(output_path),
        "audit_report": str(audit_report_path),
        "candidate_sha256": sha256_file(candidate_path),
        "output_sha256": sha256_file(output_path),
        "records": report["records"],
        "audit_passed": report["passed"],
        "audit_error_count": report["error_count"],
        "audit_warning_count": report["warning_count"],
        "expected": {
            "reviews_per_paper": args.reviews_per_paper,
            "expected_total": args.expected_total,
            "expected_year": args.expected_year,
            "expected_conference": args.expected_conference,
            "expected_per_conference": args.expected_per_conference,
            "expected_per_collection_label": args.expected_per_collection_label,
            "expected_per_final_label": args.expected_per_final_label,
            "max_one_sided_segments": args.max_one_sided_segments,
            "pdf_dir": str(args.pdf_dir),
        },
        "summary": report["summary"],
    }


def promote(args: argparse.Namespace) -> dict[str, Any]:
    candidate_path = Path(args.candidate)
    output_path = Path(args.output)
    audit_report_path = args.audit_json_output or default_audit_report_path(output_path)
    manifest_path = args.manifest_output or default_manifest_path(output_path)

    dataset = load_dataset(candidate_path)
    audit_args = audit_args_from_promote_args(args)
    audit_result = audit.audit_dataset(dataset, audit_args)
    report = audit.audit_to_report(candidate_path, dataset, audit_result, audit_args)
    audit.write_json_report(Path(audit_report_path), report)

    if audit_result.errors:
        for item in audit_result.errors:
            print(f"audit error: {item}", file=sys.stderr)
        raise SystemExit("promotion audit failed; canonical dataset was not replaced")

    write_json(output_path, dataset)
    manifest = build_manifest(args, candidate_path, output_path, Path(audit_report_path), report)
    write_json(Path(manifest_path), manifest)
    return {
        "output": str(output_path),
        "audit_report": str(audit_report_path),
        "manifest": str(manifest_path),
        "records": len(dataset),
        "warnings": len(audit_result.warnings),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", default=DEFAULT_CANDIDATE)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--audit-json-output",
        type=Path,
        help="Path for the promotion audit JSON. Defaults to OUTPUT with .audit.json suffix.",
    )
    parser.add_argument(
        "--manifest-output",
        type=Path,
        help="Path for the promotion manifest JSON. Defaults to OUTPUT with .manifest.json suffix.",
    )
    parser.add_argument("--reviews-per-paper", type=int, default=3)
    parser.add_argument("--expected-total", type=int, default=300)
    parser.add_argument(
        "--expected-year",
        type=int,
        default=DEFAULT_EXPECTED_YEAR,
        help="Expected publication/review year for every record. Use -1 to skip this check.",
    )
    parser.add_argument("--expected-conference", nargs="+", default=DEFAULT_EXPECTED_CONFERENCES)
    parser.add_argument("--expected-per-conference", type=int, default=100)
    parser.add_argument("--expected-per-collection-label", type=int, default=50)
    parser.add_argument(
        "--expected-per-final-label",
        type=int,
        default=50,
        help="Expected final accept/reject count per conference. Use -1 to skip this balance check.",
    )
    parser.add_argument(
        "--max-one-sided-segments",
        type=int,
        help=(
            "Optional stricter release gate: fail if more than this many reviews have only strengths "
            "or only weaknesses."
        ),
    )
    parser.add_argument("--pdf-dir", default="data/openreview_pdf")
    return parser.parse_args()


def main() -> None:
    result = promote(parse_args())
    print(
        "Promoted OpenReview dataset: "
        f"records={result['records']}, "
        f"warnings={result['warnings']}, "
        f"output={result['output']}, "
        f"audit_report={result['audit_report']}, "
        f"manifest={result['manifest']}"
    )


if __name__ == "__main__":
    main()

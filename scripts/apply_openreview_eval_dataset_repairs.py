#!/usr/bin/env python3
"""
Apply planned OpenReview dataset repairs from refill/targeted-repair outputs.

This is the final offline merge step after the network-backed commands in
openreview_2025_300_qwen.repair_plan.json have produced candidate records.
It refuses duplicate paper URLs/titles and rewrites refill keys into the exact
missing numbered slots recorded in the repair plan.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import scripts.audit_openreview_eval_dataset as audit
import scripts.clean_openreview_eval_dataset as cleaner


DEFAULT_BASE = "eval/openreview_2025_300_qwen.cleaned.json"
DEFAULT_PLAN = "eval/openreview_2025_300_qwen.repair_plan.json"
DEFAULT_OUTPUT = "eval/openreview_2025_300_qwen.final_candidate.json"
DEFAULT_EXPECTED_CONFERENCES = ["ICLR", "ICML", "NeurIPS"]
DEFAULT_EXPECTED_YEAR = 2025


@dataclass
class ApplyStats:
    targeted_records_replaced: int = 0
    segment_qa_records_replaced: int = 0
    segment_qa_records_skipped: int = 0
    missing_slots_filled: int = 0
    local_pdfs_copied: int = 0
    skipped_refill_candidates: list[str] = field(default_factory=list)
    unresolved: list[str] = field(default_factory=list)


def load_json_object(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise SystemExit(f"JSON input not found: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit(f"{path} must contain a JSON object.")
    return data


def write_dataset(path: Path, dataset: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(dataset, indent=2, ensure_ascii=False), encoding="utf-8")


def title_key(record: dict[str, Any]) -> str:
    return str(record.get("title") or "").strip().lower()


def paper_url(record: dict[str, Any]) -> str:
    return str(record.get("paper_url") or "").strip()


def has_empty_segments(record: dict[str, Any], review_index: int) -> bool:
    reviews = record.get("reviews") or []
    if review_index >= len(reviews) or not isinstance(reviews[review_index], dict):
        return True
    review = reviews[review_index]
    return not review.get("strengths") and not review.get("weaknesses")


def slot_key(source_key: str, slot: str) -> str:
    match = re.match(r"^(.+_\d{4})_\d{3}_(.+)$", source_key)
    if not match:
        raise ValueError(f"cannot rewrite key with numbered slot: {source_key}")
    return f"{match.group(1)}_{slot}_{match.group(2)}"


def normalize_record_for_key(key: str, record: dict[str, Any]) -> dict[str, Any]:
    cleaned = cleaner.clean_record(key, record, keep_policy_overrides=False, stats=cleaner.CleanStats())
    if not isinstance(cleaned, dict):
        raise ValueError(f"record for {key} did not clean to an object")
    return cleaned


def index_existing(dataset: dict[str, Any]) -> tuple[set[str], set[str]]:
    urls = set()
    titles = set()
    for record in dataset.values():
        if not isinstance(record, dict):
            continue
        url = paper_url(record)
        if url:
            urls.add(url)
        title = title_key(record)
        if title:
            titles.add(title)
    return urls, titles


def refill_quality_error(record: dict[str, Any], expected_reviews_per_paper: int | None) -> str | None:
    reviews = record.get("reviews")
    if not isinstance(reviews, list):
        return "reviews is not a list"
    if expected_reviews_per_paper is not None and len(reviews) != expected_reviews_per_paper:
        return f"expected {expected_reviews_per_paper} reviews, found {len(reviews)}"
    for index, review in enumerate(reviews):
        if not isinstance(review, dict):
            return f"review[{index}] is not an object"
        if not review.get("strengths") and not review.get("weaknesses"):
            return f"review[{index}] has empty strengths and weaknesses"
    return None


def refill_record_audit_errors(
    key: str,
    record: dict[str, Any],
    conference: str,
    expected_reviews_per_paper: int | None,
    expected_year: int | None,
) -> list[str]:
    args = argparse.Namespace(
        reviews_per_paper=expected_reviews_per_paper or len(record.get("reviews") or []),
        expected_year=expected_year,
        expected_conference=[conference] if conference else [],
        pdf_dir=None,
    )
    result = audit.Audit()
    audit.audit_record(
        key,
        record,
        result,
        args,
        defaultdict(list),
        defaultdict(list),
        defaultdict(list),
        defaultdict(list),
    )
    return result.errors


def record_audit_errors_for_existing_key(key: str, record: dict[str, Any], base_record: dict[str, Any]) -> list[str]:
    expected_year = record.get("year")
    if not isinstance(expected_year, int) or isinstance(expected_year, bool):
        expected_year = base_record.get("year")
    conference = str(record.get("conference") or base_record.get("conference") or "")
    return refill_record_audit_errors(
        key,
        record,
        conference,
        len(base_record.get("reviews") or []),
        expected_year if isinstance(expected_year, int) and not isinstance(expected_year, bool) else None,
    )


def candidate_url_error(key: str, base_record: dict[str, Any], replacement: dict[str, Any], repair_type: str) -> str | None:
    base_url = paper_url(base_record)
    replacement_url = paper_url(replacement)
    if base_url and replacement_url and base_url != replacement_url:
        return f"{repair_type} URL mismatch for {key}: {replacement_url} != {base_url}"
    return None


def cleaned_repair_candidates(
    key: str,
    base_record: dict[str, Any],
    repair_datasets: list[dict[str, Any]],
    repair_type: str,
) -> list[tuple[dict[str, Any], list[str]]]:
    candidates = []
    for repair_dataset in repair_datasets:
        replacement = repair_dataset.get(key)
        if not isinstance(replacement, dict):
            continue
        url_error = candidate_url_error(key, base_record, replacement, repair_type)
        if url_error:
            candidates.append((replacement, [url_error]))
            continue
        cleaned = normalize_record_for_key(key, replacement)
        candidates.append((cleaned, record_audit_errors_for_existing_key(key, cleaned, base_record)))
    return candidates


def apply_targeted_repairs(
    dataset: dict[str, Any],
    plan: dict[str, Any],
    repair_datasets: list[dict[str, Any]],
    stats: ApplyStats,
) -> None:
    for item in plan.get("empty_segment_reviews", []):
        key = item.get("key")
        review_index = int(item.get("review_index", -1))
        if not key or key not in dataset:
            stats.unresolved.append(f"targeted repair key missing from base: {key}")
            continue

        candidates = cleaned_repair_candidates(key, dataset[key], repair_datasets, "targeted repair")
        if not candidates:
            stats.unresolved.append(f"no targeted repair record supplied for {key}")
            continue

        unresolved_messages = []
        for cleaned, errors in candidates:
            if errors:
                unresolved_messages.append(f"targeted repair for {key} failed audit: {errors[0]}")
                continue
            if has_empty_segments(cleaned, review_index):
                unresolved_messages.append(f"targeted repair still has empty review[{review_index}] for {key}")
                continue
            dataset[key] = cleaned
            stats.targeted_records_replaced += 1
            break
        else:
            stats.unresolved.append(unresolved_messages[-1] if unresolved_messages else f"no usable targeted repair for {key}")


def grouped_one_sided_reviews(plan: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for item in plan.get("one_sided_segment_reviews", []):
        key = item.get("key")
        if key:
            grouped.setdefault(str(key), []).append(item)
    return grouped


def repairs_all_missing_sides(record: dict[str, Any], items: list[dict[str, Any]]) -> bool:
    reviews = record.get("reviews")
    if not isinstance(reviews, list):
        return False
    fixed_any = False
    for item in items:
        review_index = int(item.get("review_index", -1))
        missing_side = item.get("missing_side")
        if review_index < 0 or review_index >= len(reviews) or not isinstance(reviews[review_index], dict):
            return False
        if missing_side not in {"strengths", "weaknesses"}:
            return False
        if not reviews[review_index].get(missing_side):
            return False
        fixed_any = True
    return fixed_any


def apply_segment_qa_repairs(
    dataset: dict[str, Any],
    plan: dict[str, Any],
    repair_datasets: list[dict[str, Any]],
    stats: ApplyStats,
) -> None:
    grouped = grouped_one_sided_reviews(plan)
    for key, items in grouped.items():
        if key not in dataset:
            stats.segment_qa_records_skipped += 1
            continue
        candidates = cleaned_repair_candidates(key, dataset[key], repair_datasets, "segment QA repair")
        if not candidates:
            stats.segment_qa_records_skipped += 1
            continue

        for cleaned, errors in candidates:
            if errors:
                continue
            if repairs_all_missing_sides(cleaned, items):
                dataset[key] = cleaned
                stats.segment_qa_records_replaced += 1
                break
        else:
            stats.segment_qa_records_skipped += 1


def refill_candidates(
    refill_datasets: list[dict[str, Any]],
    conference: str,
    bucket: str,
    existing_urls: set[str],
    existing_titles: set[str],
    stats: ApplyStats,
    expected_reviews_per_paper: int | None = None,
    expected_year: int | None = None,
) -> list[tuple[str, dict[str, Any]]]:
    candidates = []
    seen_urls = set(existing_urls)
    seen_titles = set(existing_titles)
    for refill_dataset in refill_datasets:
        for key, record in refill_dataset.items():
            if not isinstance(record, dict):
                continue
            if str(record.get("conference") or "") != conference:
                continue
            if audit.normalize_collection_bucket(record.get("collection_decision_category")) != bucket:
                continue
            url = paper_url(record)
            title = title_key(record)
            if url and url in seen_urls:
                stats.skipped_refill_candidates.append(f"{key}: duplicate paper_url")
                continue
            if title and title in seen_titles:
                stats.skipped_refill_candidates.append(f"{key}: duplicate title")
                continue
            cleaned = normalize_record_for_key(key, record)
            quality_error = refill_quality_error(cleaned, expected_reviews_per_paper)
            if quality_error:
                stats.skipped_refill_candidates.append(f"{key}: {quality_error}")
                continue
            record_errors = refill_record_audit_errors(
                key,
                cleaned,
                conference,
                expected_reviews_per_paper,
                expected_year,
            )
            if record_errors:
                stats.skipped_refill_candidates.append(f"{key}: {record_errors[0]}")
                continue
            seen_urls.add(url)
            seen_titles.add(title)
            candidates.append((key, record))
    return sorted(candidates, key=lambda item: item[0])


def copy_local_pdf_if_available(
    source_key: str,
    dest_key: str,
    record: dict[str, Any],
    pdf_dir: Path,
    stats: ApplyStats,
) -> None:
    source = pdf_dir / f"{source_key}.pdf"
    dest = pdf_dir / f"{dest_key}.pdf"
    if source.exists() and source.stat().st_size > 0 and not dest.exists():
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, dest)
        stats.local_pdfs_copied += 1
    if dest.exists() and dest.stat().st_size > 0:
        record["paper_dir"] = str(dest)


def apply_refills(
    dataset: dict[str, Any],
    plan: dict[str, Any],
    refill_datasets: list[dict[str, Any]],
    pdf_dir: Path,
    stats: ApplyStats,
    expected_reviews_per_paper: int | None = None,
) -> None:
    existing_urls, existing_titles = index_existing(dataset)
    expected_year = int(plan.get("expected_year") or DEFAULT_EXPECTED_YEAR)
    for missing in plan.get("missing_slots", []):
        conference = str(missing.get("conference") or "")
        bucket = str(missing.get("bucket") or "")
        slots = list(missing.get("missing_slots") or [])
        candidates = refill_candidates(
            refill_datasets,
            conference,
            bucket,
            existing_urls,
            existing_titles,
            stats,
            expected_reviews_per_paper,
            expected_year,
        )
        if len(candidates) < len(slots):
            stats.unresolved.append(
                f"not enough refill candidates for {conference} {bucket}: need {len(slots)}, got {len(candidates)}"
            )
        for slot, (source_key, source_record) in zip(slots, candidates):
            dest_key = slot_key(source_key, str(slot))
            if dest_key in dataset:
                raise SystemExit(f"destination key already exists: {dest_key}")
            record = normalize_record_for_key(dest_key, source_record)
            copy_local_pdf_if_available(source_key, dest_key, record, pdf_dir, stats)
            dataset[dest_key] = record
            existing_urls.add(paper_url(record))
            existing_titles.add(title_key(record))
            stats.missing_slots_filled += 1


def apply_repairs(args: argparse.Namespace) -> tuple[dict[str, Any], ApplyStats]:
    dataset = load_json_object(Path(args.base))
    plan = load_json_object(Path(args.plan))
    repair_datasets = [load_json_object(Path(path)) for path in args.targeted_repair]
    segment_qa_datasets = [load_json_object(Path(path)) for path in args.segment_qa_repair]
    refill_datasets = [load_json_object(Path(path)) for path in args.refill]
    stats = ApplyStats()

    apply_targeted_repairs(dataset, plan, repair_datasets, stats)
    apply_segment_qa_repairs(dataset, plan, segment_qa_datasets, stats)
    apply_refills(dataset, plan, refill_datasets, Path(args.pdf_dir), stats, getattr(args, "reviews_per_paper", None))
    return dataset, stats


def default_audit_report_path(output_path: Path) -> Path:
    if output_path.suffix == ".json":
        return output_path.with_name(f"{output_path.stem}.audit.json")
    return output_path.with_name(f"{output_path.name}.audit.json")


def audit_args_from_apply_args(args: argparse.Namespace) -> argparse.Namespace:
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


def audit_candidate(dataset: dict[str, Any], output_path: Path, args: argparse.Namespace) -> audit.Audit:
    audit_args = audit_args_from_apply_args(args)
    result = audit.audit_dataset(dataset, audit_args)
    report_path = args.audit_json_output or default_audit_report_path(output_path)
    if report_path:
        audit.write_json_report(Path(report_path), audit.audit_to_report(output_path, dataset, result, audit_args))
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default=DEFAULT_BASE)
    parser.add_argument("--plan", default=DEFAULT_PLAN)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--targeted-repair", action="append", default=[])
    parser.add_argument(
        "--segment-qa-repair",
        action="append",
        default=[],
        help="Optional repair output for one-sided segment warnings; merged only when it fills a missing side.",
    )
    parser.add_argument("--refill", action="append", default=[])
    parser.add_argument("--pdf-dir", default="data/openreview_pdf")
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
    parser.add_argument(
        "--audit-json-output",
        type=Path,
        help="Path for the post-apply audit JSON. Defaults to OUTPUT with .audit.json suffix.",
    )
    parser.add_argument(
        "--allow-audit-errors",
        action="store_true",
        help="Write output even if the post-apply audit finds hard errors.",
    )
    parser.add_argument(
        "--allow-unresolved",
        action="store_true",
        help="Write output even if planned repairs were not fully supplied.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    dataset, stats = apply_repairs(args)
    if stats.unresolved and not args.allow_unresolved:
        for item in stats.unresolved:
            print(f"unresolved: {item}", file=sys.stderr)
        raise SystemExit("planned repairs are still unresolved; use --allow-unresolved to write a partial result")
    audit_result = audit_candidate(dataset, Path(args.output), args)
    if audit_result.errors and not args.allow_audit_errors:
        for item in audit_result.errors:
            print(f"audit error: {item}", file=sys.stderr)
        raise SystemExit("post-apply audit failed; use --allow-audit-errors only for a partial/debug output")
    write_dataset(Path(args.output), dataset)
    print(f"Wrote {len(dataset)} records to {args.output}")
    print(
        "Apply summary: "
        f"targeted_records_replaced={stats.targeted_records_replaced}, "
        f"segment_qa_records_replaced={stats.segment_qa_records_replaced}, "
        f"segment_qa_records_skipped={stats.segment_qa_records_skipped}, "
        f"missing_slots_filled={stats.missing_slots_filled}, "
        f"local_pdfs_copied={stats.local_pdfs_copied}, "
        f"skipped_refill_candidates={len(stats.skipped_refill_candidates)}, "
        f"unresolved={len(stats.unresolved)}, "
        f"audit_errors={len(audit_result.errors)}, "
        f"audit_warnings={len(audit_result.warnings)}"
    )


if __name__ == "__main__":
    main()

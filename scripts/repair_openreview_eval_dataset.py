#!/usr/bin/env python3
"""
Repair an existing OpenReview evaluation JSON file in place.

Unlike build_openreview_eval_dataset.py, this script never selects new papers.
It scans the current result file, refetches each existing paper forum from
OpenReview, and refreshes the fields that can drift or be parsed incorrectly:
final decision label, review ratings/confidence, strengths/weaknesses, rebuttals,
paper score, title, paper URL, and PDF URL.

Examples:
    python scripts/repair_openreview_eval_dataset.py \
        --input eval/openreview_2025_300_qwen.json

    OPENREVIEW_USERNAME=... OPENREVIEW_PASSWORD=... python scripts/repair_openreview_eval_dataset.py \
        --input eval/openreview_2025_300_qwen.json

    DASHSCOPE_API_KEY=... python scripts/repair_openreview_eval_dataset.py \
        --input eval/openreview_2025_300_qwen.json \
        --use-llm-segmentation
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional
from urllib.parse import parse_qs, urlparse


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import scripts.build_openreview_eval_dataset as builder


DEFAULT_INPUT = "eval/openreview_2025_300_qwen.json"
REPAIRED_FIELDS = [
    "title",
    "paper_url",
    "pdf_url",
    "accept_or_not",
    "collection_decision_category",
    "score",
    "reviews",
    "decision_override_reason",
]


def is_ignored_segment_marker(text: str) -> bool:
    canonical = builder.canonical_field_name(text.rstrip(":"))
    if canonical == "other_comments_or_suggestions" or canonical.startswith("other_comments_or_suggestions_"):
        return True
    for key in builder.SUBSTANTIVE_REVIEW_TEXT_KEYS:
        ignored = builder.canonical_field_name(key)
        if canonical == ignored or canonical.startswith(f"{ignored}_"):
            return True
    if canonical in builder.REFERENCE_SEGMENT_LABELS:
        return False
    if canonical.startswith("code_of_conduct") or canonical.endswith("_acknowledgement"):
        return False
    return builder.is_ignored_segmentation_header(text)


def append_clean_segment_items(target: list[str], items: Any) -> None:
    for item in items or []:
        text = builder.normalize_segment_text(builder.as_text(item))
        if builder.is_non_substantive_segment_text(text):
            continue
        if text:
            target.append(text)


def trim_segment_items(items: Any, field: str) -> tuple[list[str], list[str]]:
    kept = []
    opposite = []
    default_section = "strengths" if field == "strengths" else "weaknesses"
    for item in items or []:
        raw_text = builder.as_text(item)
        if is_ignored_segment_marker(raw_text):
            break
        strengths, weaknesses = builder.split_inline_strengths_weaknesses(raw_text, default_section=default_section)
        if field == "strengths":
            append_clean_segment_items(kept, strengths)
            append_clean_segment_items(opposite, weaknesses)
        else:
            append_clean_segment_items(opposite, strengths)
            append_clean_segment_items(kept, weaknesses)
    return builder.dedupe_preserve_order(kept), builder.dedupe_preserve_order(opposite)


def sanitize_reviews(reviews: list[Any]) -> list[dict[str, Any]]:
    sanitized = []
    for review in reviews:
        if not isinstance(review, dict):
            continue
        cleaned = dict(review)
        strengths, leaked_weaknesses = trim_segment_items(cleaned.get("strengths"), "strengths")
        weaknesses, leaked_strengths = trim_segment_items(cleaned.get("weaknesses"), "weaknesses")
        cleaned["strengths"], cleaned["weaknesses"] = builder.dedupe_segment_sides(
            [*strengths, *leaked_strengths],
            [*weaknesses, *leaked_weaknesses],
        )
        sanitized.append(cleaned)
    return sanitized


@dataclass
class RepairStats:
    seen: int = 0
    repaired: int = 0
    unchanged: int = 0
    failed: int = 0
    warnings: list[str] = field(default_factory=list)


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


def backup_file(path: Path) -> Path:
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    backup_path = path.with_name(f"{path.name}.bak.{timestamp}")
    shutil.copy2(path, backup_path)
    return backup_path


def forum_id_from_url(url: str) -> Optional[str]:
    if not url:
        return None
    parsed = urlparse(url)
    query_id = parse_qs(parsed.query).get("id")
    if query_id and query_id[0]:
        return query_id[0]
    return None


def forum_id_from_record(record: dict[str, Any]) -> Optional[str]:
    for key in ("paper_url", "pdf_url"):
        forum = forum_id_from_url(str(record.get(key) or ""))
        if forum:
            return forum
    return None


def find_submission_in_forum_notes(forum: str, forum_notes: list[Any]) -> Optional[Any]:
    for note in forum_notes:
        if builder.note_id(note) == forum:
            return note
    for note in forum_notes:
        content = builder.get_content(note)
        if builder.note_forum(note) == forum and (content.get("title") or content.get("Title")):
            return note
    return None


def fetch_submission_by_id(client: Any, forum: str) -> Any:
    if not hasattr(client, "get_note"):
        raise RuntimeError("OpenReview client does not support get_note; submission not found in forum notes.")
    try:
        return client.get_note(forum)
    except TypeError:
        return client.get_note(id=forum)
    except Exception as positional_error:
        try:
            return client.get_note(id=forum)
        except Exception:
            raise positional_error


def resolve_decision(
    key: str,
    record: dict[str, Any],
    submission: Any,
    forum_notes: list[Any],
    respect_policy_overrides: bool,
) -> tuple[str, str, Optional[str], Optional[str]]:
    decision_text = builder.paper_decision(submission, forum_notes)
    final_decision = builder.classify_accept_reject_decision(decision_text)
    warnings = []

    if final_decision is None:
        original = record.get("accept_or_not")
        final_decision = original if original in {"accept", "reject"} else "reject"
        warnings.append("could not infer explicit accept/reject decision; kept the existing label")

    collection_category = final_decision
    override_reason = None
    if (
        respect_policy_overrides
        and final_decision == "reject"
    ):
        final_decision, override_reason = builder.dataset_decision_label(
            submission=submission,
            forum_notes=forum_notes,
            conference=str(record.get("conference") or ""),
            collection_label="reject",
            respect_policy_overrides=True,
        )
        collection_category = final_decision

    key_bucket = collection_bucket_from_key(key)
    if key_bucket and final_decision != key_bucket and not override_reason:
        warnings.append(
            f"final decision {final_decision!r} differs from key bucket {key_bucket!r}; "
            "run rebalance_openreview_eval_dataset.py to rename/reindex this record"
        )

    return final_decision, collection_category, override_reason, "; ".join(warnings) if warnings else None


def normalize_collection_bucket(label: Any) -> str:
    text = str(label or "").strip().lower()
    if text.startswith("accept"):
        return "accept"
    if text.startswith("reject"):
        return "reject"
    return ""


def collection_bucket_from_key(key: str) -> Optional[str]:
    if "_accept_" in key:
        return "accept"
    if "_reject_" in key:
        return "reject"
    return None


def resolve_collection_category(key: str, record: dict[str, Any]) -> tuple[str, Optional[str]]:
    existing = str(record.get("collection_decision_category") or "").strip()
    final_label = str(record.get("accept_or_not") or "").strip().lower()
    if final_label in {"accept", "reject"}:
        existing_bucket = normalize_collection_bucket(existing)
        if existing and existing_bucket and existing_bucket != final_label:
            return final_label, (
                f"collection_decision_category {existing!r} conflicted with accept_or_not {final_label!r}; "
                "recovered the collection bucket from the verified decision label"
            )
        return final_label, None

    key_bucket = collection_bucket_from_key(key)
    if not key_bucket:
        return existing or str(record.get("accept_or_not") or "reject"), None

    existing_bucket = normalize_collection_bucket(existing)
    if existing and existing_bucket == key_bucket:
        return existing, None
    if existing and existing_bucket and existing_bucket != key_bucket:
        return key_bucket, (
            f"collection_decision_category {existing!r} conflicted with key bucket {key_bucket!r}; "
            "recovered the collection bucket from the paper key"
        )
    return key_bucket, None


def repair_record(
    key: str,
    record: dict[str, Any],
    client: Any,
    args: argparse.Namespace,
) -> tuple[dict[str, Any], list[str]]:
    warnings = []
    forum = forum_id_from_record(record)
    if not forum:
        raise RuntimeError("missing OpenReview forum id in paper_url/pdf_url")

    forum_notes = builder.fetch_forum_notes(client, forum)
    submission = find_submission_in_forum_notes(forum, forum_notes)
    if submission is None:
        submission = fetch_submission_by_id(client, forum)

    final_decision, collection_category, override_reason, decision_warning = resolve_decision(
        key=key,
        record=record,
        submission=submission,
        forum_notes=forum_notes,
        respect_policy_overrides=args.respect_policy_overrides,
    )
    if decision_warning:
        warnings.append(decision_warning)

    reviews = builder.collect_reviews(
        forum_notes=forum_notes,
        use_llm_segmentation=args.use_llm_segmentation,
        llm_model=args.llm_model,
        llm_base_url=args.llm_base_url,
        llm_api_key_env=args.llm_api_key_env,
        max_reviews=args.reviews_per_paper,
        dataset_decision=final_decision,
    )
    reviews = sanitize_reviews(reviews)
    if len(reviews) < args.reviews_per_paper:
        warnings.append(f"found {len(reviews)} official reviews; expected {args.reviews_per_paper}")
    if not reviews:
        reviews = sanitize_reviews(list(record.get("reviews") or []))
        warnings.append("kept existing reviews because refetch returned no official reviews")

    repaired = dict(record)
    repaired.update(
        {
            "title": builder.get_title(submission) or record.get("title", "Untitled"),
            "paper_url": builder.openreview_url(forum),
            "pdf_url": builder.get_pdf_url(submission) or record.get("pdf_url"),
            "accept_or_not": final_decision,
            "collection_decision_category": collection_category,
            "score": builder.average_rating(reviews),
            "reviews": reviews,
        }
    )

    if override_reason:
        repaired["decision_override_reason"] = override_reason
    else:
        repaired.pop("decision_override_reason", None)

    return repaired, warnings


def selected_items(dataset: dict[str, Any], args: argparse.Namespace) -> list[tuple[str, dict[str, Any]]]:
    items = [(key, value) for key, value in dataset.items() if isinstance(value, dict)]
    only_keys = normalize_only_keys(args.only_key)
    if only_keys:
        allowed_keys = set(only_keys)
        items = [(key, record) for key, record in items if key in allowed_keys]
    if args.only_conference:
        allowed = {conference.lower() for conference in args.only_conference}
        items = [
            (key, record)
            for key, record in items
            if str(record.get("conference") or "").lower() in allowed
        ]
    if args.start_after:
        keys = [key for key, _ in items]
        if args.start_after in keys:
            items = items[keys.index(args.start_after) + 1 :]
    if args.limit is not None:
        items = items[: args.limit]
    return items


def normalize_only_keys(values: Optional[list[str]]) -> Optional[list[str]]:
    if not values:
        return values
    keys: list[str] = []
    for value in values:
        keys.extend(part for part in str(value).split() if part)
    return keys


def changed_fields(original: dict[str, Any], repaired: dict[str, Any]) -> list[str]:
    return [field for field in REPAIRED_FIELDS if original.get(field) != repaired.get(field)]


def is_challenge_required_error(exc: Exception) -> bool:
    return builder.is_openreview_challenge_required_error(exc)


def print_audit(dataset: dict[str, Any], reviews_per_paper: int) -> None:
    print("\nCurrent audit:")
    conferences = sorted({str(record.get("conference") or "Unknown") for record in dataset.values()})
    for conference in conferences:
        papers = [record for record in dataset.values() if str(record.get("conference") or "Unknown") == conference]
        reviews = [review for record in papers for review in record.get("reviews", [])]
        print(
            f"  {conference}: papers={len(papers)}, "
            f"score_missing={sum(record.get('score') is None for record in papers)}, "
            f"short_review_papers={sum(len(record.get('reviews', [])) < reviews_per_paper for record in papers)}, "
            f"review_rating_missing={sum(review.get('rating') is None for review in reviews)}, "
            f"strengths_missing={sum(not review.get('strengths') for review in reviews)}, "
            f"weaknesses_missing={sum(not review.get('weaknesses') for review in reviews)}, "
            f"both_empty={sum(not review.get('strengths') and not review.get('weaknesses') for review in reviews)}"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default=DEFAULT_INPUT, help="Existing OpenReview eval JSON to repair.")
    parser.add_argument(
        "--output",
        default=None,
        help="Where to write the repaired JSON. Defaults to --input for in-place repair.",
    )
    parser.add_argument("--no-backup", action="store_true", help="Do not create a .bak timestamp backup.")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and report changes without writing JSON.")
    parser.add_argument("--only-key", nargs="+", help="Repair exact dataset keys only.")
    parser.add_argument("--only-conference", nargs="+", help="Restrict repair to conference names, e.g. ICML NeurIPS.")
    parser.add_argument("--start-after", help="Resume after this paper key.")
    parser.add_argument("--limit", type=int, help="Repair at most this many selected papers.")
    parser.add_argument("--reviews-per-paper", type=int, default=3)
    parser.add_argument("--respect-policy-overrides", action="store_true")
    parser.add_argument("--stop-on-error", action="store_true")
    parser.add_argument("--use-llm-segmentation", action="store_true")
    parser.add_argument("--llm-model", default=builder.DEFAULT_LLM_MODEL)
    parser.add_argument(
        "--llm-base-url",
        default="https://dashscope.aliyuncs.com/compatible-mode/v1",
        help="OpenAI-compatible API base URL. Use empty string for OpenAI's default endpoint.",
    )
    parser.add_argument("--llm-api-key-env", default="DASHSCOPE_API_KEY")
    parser.add_argument("--request-delay", type=float, default=1.0, help="Minimum delay between OpenReview requests.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.llm_base_url == "":
        args.llm_base_url = None
    if args.use_llm_segmentation:
        api_key_available = (
            builder.os.getenv(args.llm_api_key_env)
            or builder.os.getenv("QWEN_API_KEY")
            or builder.os.getenv("DASHSCOPE_API_KEY")
        )
        if not api_key_available:
            raise SystemExit(f"--use-llm-segmentation requires {args.llm_api_key_env} in the environment.")

    builder.OPENREVIEW_REQUEST_DELAY_SECONDS = args.request_delay
    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path
    dataset = load_dataset(input_path)
    items = selected_items(dataset, args)
    stats = RepairStats()
    backup_path: Optional[Path] = None
    wrote_any = False

    openreview = builder.import_openreview()
    client = builder.get_client(openreview)

    for index, (key, record) in enumerate(items, start=1):
        stats.seen += 1
        print(f"[{index}/{len(items)}] repairing {key}")
        try:
            repaired, warnings = repair_record(key, record, client, args)
        except Exception as exc:
            stats.failed += 1
            message = f"{key}: {exc}"
            stats.warnings.append(message)
            print(f"  ERROR: {exc}", file=sys.stderr)
            if is_challenge_required_error(exc):
                print(f"{builder.openreview_challenge_message()} Use --start-after if needed.", file=sys.stderr)
                break
            if args.stop_on_error:
                raise
            continue

        fields = changed_fields(record, repaired)
        if fields:
            stats.repaired += 1
            dataset[key] = repaired
            print(f"  updated: {', '.join(fields)}")
            if not args.dry_run:
                if output_path == input_path and not args.no_backup and backup_path is None:
                    backup_path = backup_file(input_path)
                    print(f"  backup written to {backup_path}")
                write_dataset(output_path, dataset)
                wrote_any = True
        else:
            stats.unchanged += 1
            print("  unchanged")
        for warning in warnings:
            stats.warnings.append(f"{key}: {warning}")
            print(f"  warning: {warning}")

    if not args.dry_run and wrote_any:
        write_dataset(output_path, dataset)
        print(f"\nWrote {len(dataset)} papers to {output_path}")
    elif not args.dry_run:
        print("\nNo JSON changes were written.")
    else:
        print("\nDry run only; no JSON written.")

    print(
        f"Repair summary: seen={stats.seen}, repaired={stats.repaired}, "
        f"unchanged={stats.unchanged}, failed={stats.failed}, warnings={len(stats.warnings)}"
    )
    if stats.warnings:
        print("First warnings:")
        for warning in stats.warnings[:20]:
            print(f"  - {warning}")
    print_audit(dataset, args.reviews_per_paper)


if __name__ == "__main__":
    main()

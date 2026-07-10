#!/usr/bin/env python3
"""
One-time rebalance for the current OpenReview evaluation dataset.

This script fixes records that were stored under the wrong accept/reject key,
renumbers keys after the move, keeps local PDF paths in sync with the new keys,
refetches missing official reviews, and tops up any conference/bucket with fewer
than the requested number of papers.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import time
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import scripts.build_openreview_eval_dataset as builder
import scripts.repair_openreview_eval_dataset as repair


DEFAULT_INPUT = "eval/openreview_2025_300_qwen.json"
DEFAULT_OUTPUT = "eval/openreview_2025_300_qwen.rebalanced.json"


@dataclass
class RebalanceStats:
    existing_seen: int = 0
    existing_kept: int = 0
    existing_rekeyed: int = 0
    existing_short_reviews: int = 0
    existing_dropped: int = 0
    topup_added: int = 0
    topup_checked: int = 0
    pdf_copied: int = 0
    pdf_moved: int = 0
    pdf_downloaded: int = 0
    pdf_missing: int = 0
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


def abs_or_repo_path(path: str | Path) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else REPO_ROOT / candidate


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def progress_bar(current: int, total: int, width: int = 24) -> str:
    if total <= 0:
        return "[........................] 0/0"
    current = min(max(current, 0), total)
    filled = int(width * current / total)
    return f"[{'#' * filled}{'.' * (width - filled)}] {current}/{total} ({current / total:.1%})"


def print_progress(phase: str, current: int, total: int, detail: str) -> None:
    print(f"{phase} {progress_bar(current, total)} {detail}", flush=True)


def key_parts(key: str) -> tuple[str, str, int, int, str] | None:
    parts = key.split("_", 4)
    if len(parts) != 5:
        return None
    conference, bucket, year_text, index_text, slug = parts
    if bucket not in {"accept", "reject"} or not year_text.isdigit() or not index_text.isdigit():
        return None
    return conference, bucket, int(year_text), int(index_text), slug


def old_index(key: str) -> int:
    parts = key_parts(key)
    return parts[3] if parts else 10**9


def bucket_from_record(record: dict[str, Any]) -> Optional[str]:
    decision = record.get("accept_or_not")
    if decision in {"accept", "reject"}:
        return str(decision)
    bucket = repair.normalize_collection_bucket(record.get("collection_decision_category"))
    return bucket or None


def make_key(conference: str, bucket: str, year: int, index: int, title: str) -> str:
    return f"{conference.lower()}_{bucket}_{year}_{index:03d}_{builder.slugify(title)}"


def pdf_candidates(old_key: str, record: dict[str, Any], pdf_dir: Path) -> list[Path]:
    candidates = []
    paper_dir = str(record.get("paper_dir") or "").strip()
    if paper_dir:
        candidates.append(abs_or_repo_path(paper_dir))
    candidates.append(abs_or_repo_path(pdf_dir / f"{old_key}.pdf"))
    return list(dict.fromkeys(candidates))


def first_existing_pdf(old_key: str, record: dict[str, Any], pdf_dir: Path) -> Optional[Path]:
    for candidate in pdf_candidates(old_key, record, pdf_dir):
        if candidate.exists() and candidate.stat().st_size > 0:
            return candidate
    return None


def pdf_urls_for_record(record: dict[str, Any]) -> list[str]:
    urls = []
    forum = repair.forum_id_from_record(record)
    if forum:
        urls.append(f"{builder.OPENREVIEW_BASE_URL}/pdf?id={forum}")
    pdf_url = str(record.get("pdf_url") or "").strip()
    if pdf_url:
        urls.append(pdf_url)
    return list(dict.fromkeys(urls))


def ensure_pdf_for_key(
    old_key: str,
    new_key: str,
    record: dict[str, Any],
    args: argparse.Namespace,
    stats: RebalanceStats,
) -> str:
    pdf_dir = Path(args.pdf_dir)
    target = abs_or_repo_path(pdf_dir / f"{new_key}.pdf")
    source = first_existing_pdf(old_key, record, pdf_dir)
    if target.exists() and target.stat().st_size > 0:
        return display_path(target)
    if source:
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.resolve() != target.resolve() and not args.dry_run:
            if args.move_pdfs:
                shutil.move(str(source), str(target))
                stats.pdf_moved += 1
            else:
                shutil.copy2(source, target)
                stats.pdf_copied += 1
        elif source.resolve() != target.resolve():
            stats.pdf_copied += 1
        return display_path(target)

    pdf_urls = pdf_urls_for_record(record)
    if args.download_pdfs and pdf_urls:
        if args.dry_run:
            stats.pdf_downloaded += 1
            return display_path(target)
        for pdf_url in pdf_urls:
            if builder.download_pdf(pdf_url, target, sleep_seconds=args.sleep):
                stats.pdf_downloaded += 1
                return display_path(target)

    stats.pdf_missing += 1
    return str(record.get("paper_dir") or "")


def merge_reviews(refetched: list[dict[str, Any]], existing: list[Any], min_reviews: int) -> list[dict[str, Any]]:
    merged = []
    seen = set()
    for review in [*refetched, *[item for item in existing if isinstance(item, dict)]]:
        reviewer_id = str(review.get("reviewer_id") or "")
        signature = (reviewer_id, review.get("rating"), review.get("confidence"))
        fallback = json.dumps(review, sort_keys=True, ensure_ascii=False)
        key = signature if reviewer_id else fallback
        if key in seen:
            continue
        seen.add(key)
        merged.append(dict(review))
        if len(merged) >= min_reviews:
            break
    return merged


def fetch_submission_and_notes(client: Any, forum: str) -> tuple[Any, list[Any]]:
    forum_notes = builder.fetch_forum_notes(client, forum)
    submission = repair.find_submission_in_forum_notes(forum, forum_notes)
    if submission is None:
        submission = repair.fetch_submission_by_id(client, forum)
    return submission, forum_notes


def collect_record_reviews(forum_notes: list[Any], decision: str, args: argparse.Namespace) -> list[dict[str, Any]]:
    reviews = builder.collect_reviews(
        forum_notes=forum_notes,
        use_llm_segmentation=args.use_llm_segmentation,
        llm_model=args.llm_model,
        llm_base_url=args.llm_base_url,
        llm_api_key_env=args.llm_api_key_env,
        max_reviews=args.reviews_per_paper,
        dataset_decision=decision,
    )
    return repair.sanitize_reviews(reviews)


def has_empty_segment_review(record_or_reviews: dict[str, Any] | list[Any]) -> bool:
    reviews = record_or_reviews if isinstance(record_or_reviews, list) else record_or_reviews.get("reviews", [])
    return any(
        isinstance(review, dict)
        and not review.get("strengths")
        and not review.get("weaknesses")
        for review in reviews or []
    )


def refresh_existing_record(
    old_key: str,
    record: dict[str, Any],
    client: Any,
    args: argparse.Namespace,
    stats: RebalanceStats,
) -> Optional[tuple[str, dict[str, Any]]]:
    stats.existing_seen += 1
    forum = repair.forum_id_from_record(record)
    if not forum:
        stats.warnings.append(f"{old_key}: missing OpenReview forum id")
        stats.existing_dropped += 1
        return None

    submission, forum_notes = fetch_submission_and_notes(client, forum)
    fallback = bucket_from_record(record) or repair.collection_bucket_from_key(old_key) or "reject"
    decision, override_reason = builder.resolved_dataset_decision(
        submission=submission,
        forum_notes=forum_notes,
        conference=str(record.get("conference") or ""),
        fallback_label=fallback,
        respect_policy_overrides=args.respect_policy_overrides,
    )
    reviews = collect_record_reviews(forum_notes, decision, args)
    reviews = merge_reviews(reviews, list(record.get("reviews") or []), args.reviews_per_paper)
    if len(reviews) < args.reviews_per_paper:
        stats.existing_short_reviews += 1
        stats.warnings.append(
            f"{old_key}: only {len(reviews)} usable official reviews after refetch; expected {args.reviews_per_paper}"
        )
        if args.drop_short_review_papers:
            stats.existing_dropped += 1
            return None
    if getattr(args, "drop_empty_segment_papers", False) and has_empty_segment_review(reviews):
        stats.existing_dropped += 1
        stats.warnings.append(f"{old_key}: at least one review has empty strengths and weaknesses")
        return None

    refreshed = dict(record)
    refreshed.update(
        {
            "title": builder.get_title(submission) or record.get("title", "Untitled"),
            "paper_url": builder.openreview_url(forum),
            "pdf_url": builder.get_pdf_url(submission) or record.get("pdf_url"),
            "accept_or_not": decision,
            "collection_decision_category": decision,
            "score": builder.average_rating(reviews),
            "reviews": reviews,
        }
    )
    if override_reason:
        refreshed["decision_override_reason"] = override_reason
    else:
        refreshed.pop("decision_override_reason", None)

    stats.existing_kept += 1
    return old_key, refreshed


def build_record_from_submission(
    submission: Any,
    forum_notes: list[Any],
    venue: builder.VenueSpec,
    decision: str,
    args: argparse.Namespace,
) -> Optional[dict[str, Any]]:
    reviews = collect_record_reviews(forum_notes, decision, args)
    if len(reviews) < args.reviews_per_paper:
        return None
    if getattr(args, "drop_empty_segment_papers", False) and has_empty_segment_review(reviews):
        return None
    pdf_url = builder.get_pdf_url(submission)
    return {
        "title": builder.get_title(submission),
        "paper_dir": "",
        "paper_url": builder.openreview_url(builder.note_forum(submission)),
        "pdf_url": pdf_url,
        "conference": venue.conference,
        "year": venue.year,
        "topic": args.topic,
        "accept_or_not": decision,
        "collection_decision_category": decision,
        "score": builder.average_rating(reviews),
        "reviews": reviews,
    }


def forum_from_submission(submission: Any) -> str:
    return builder.note_forum(submission) or builder.note_id(submission)


def top_up_bucket(
    groups: dict[tuple[str, str], list[tuple[str, dict[str, Any]]]],
    known_forums: set[str],
    known_urls: set[str],
    client: Any,
    venue: builder.VenueSpec,
    bucket: str,
    args: argparse.Namespace,
    stats: RebalanceStats,
) -> None:
    need = args.target_per_category - len(groups[(venue.conference, bucket)])
    if need <= 0:
        return
    print(f"Top-up needed for {venue.conference} {bucket}: {need}")
    print(f"Fetching submissions for {venue.conference} {venue.year}...", flush=True)
    submissions = builder.fetch_submissions(client, venue)
    print(f"Fetched {len(submissions)} submissions for {venue.conference} {venue.year}", flush=True)
    decision_by_forum = builder.fetch_decision_notes(client, venue)
    if decision_by_forum:
        print(f"Found {len(decision_by_forum)} decision notes for {venue.conference} {venue.year}", flush=True)
    checked_for_bucket = 0
    for submission in submissions:
        if len(groups[(venue.conference, bucket)]) >= args.target_per_category:
            break
        if checked_for_bucket >= args.max_topup_forum_checks:
            stats.warnings.append(
                f"{venue.conference} {bucket}: stopped after {checked_for_bucket} top-up forum checks"
            )
            break
        forum = forum_from_submission(submission)
        if not forum or forum in known_forums:
            continue

        candidate_decision = builder.decision_bucket_from_text(
            " ".join([builder.submission_decision(submission), decision_by_forum.get(forum, "")])
        )
        if candidate_decision is None and builder.likely_reject_from_submission_metadata(submission, venue):
            candidate_decision = "reject"
        if candidate_decision is not None and candidate_decision != bucket:
            continue

        checked_for_bucket += 1
        stats.topup_checked += 1
        remaining = args.target_per_category - len(groups[(venue.conference, bucket)])
        print_progress(
            f"Top-up {venue.conference} {bucket}",
            checked_for_bucket,
            args.max_topup_forum_checks,
            f"remaining={remaining} forum={forum}",
        )
        forum_notes = builder.fetch_forum_notes(client, forum)
        if candidate_decision is None:
            candidate_decision = builder.decision_bucket_from_text(builder.paper_decision(submission, forum_notes))
        decision, _ = builder.resolved_dataset_decision(
            submission=submission,
            forum_notes=forum_notes,
            conference=venue.conference,
            fallback_label=candidate_decision or bucket,
            respect_policy_overrides=args.respect_policy_overrides,
        )
        if decision != bucket:
            continue
        record = build_record_from_submission(submission, forum_notes, venue, decision, args)
        if record is None:
            stats.warnings.append(f"{venue.conference} {bucket}: skipped {forum}; fewer than 3 reviews")
            continue
        url = str(record.get("paper_url") or "")
        if url and url in known_urls:
            continue
        temp_key = f"topup_{forum}"
        groups[(venue.conference, bucket)].append((temp_key, record))
        known_forums.add(forum)
        if url:
            known_urls.add(url)
        stats.topup_added += 1
        print(f"  added {venue.conference} {bucket}: {record.get('title')}")


def venue_specs_for_dataset(dataset: dict[str, Any], args: argparse.Namespace) -> list[builder.VenueSpec]:
    if args.venues:
        return builder.parse_venue_specs(args.venues)
    seen: set[tuple[str, int]] = set()
    specs = []
    for record in dataset.values():
        if not isinstance(record, dict):
            continue
        conference = str(record.get("conference") or "").strip()
        year = record.get("year")
        if not conference or not isinstance(year, int) or isinstance(year, bool):
            continue
        if (conference, year) in seen:
            continue
        seen.add((conference, year))
        venue_id = builder.DEFAULT_VENUES.get(conference, {}).get(year)
        if venue_id:
            specs.append(builder.VenueSpec(conference, year, venue_id))
    return specs


def include_record(record: dict[str, Any], venues: list[builder.VenueSpec]) -> bool:
    allowed = {(venue.conference, venue.year) for venue in venues}
    return (str(record.get("conference") or ""), record.get("year")) in allowed


def sort_group_items(items: list[tuple[str, dict[str, Any]]]) -> list[tuple[str, dict[str, Any]]]:
    return sorted(
        items,
        key=lambda item: (
            1 if item[0].startswith("topup_") else 0,
            old_index(item[0]),
            str(item[1].get("title") or ""),
        ),
    )


def rekey_groups(
    groups: dict[tuple[str, str], list[tuple[str, dict[str, Any]]]],
    venues: list[builder.VenueSpec],
    args: argparse.Namespace,
    stats: RebalanceStats,
) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for venue in venues:
        for bucket in ("accept", "reject"):
            for index, (old_key, record) in enumerate(sort_group_items(groups[(venue.conference, bucket)]), start=1):
                new_key = make_key(
                    venue.conference,
                    bucket,
                    int(record.get("year") or venue.year),
                    index,
                    str(record.get("title") or "Untitled"),
                )
                if old_key != new_key and not old_key.startswith("topup_"):
                    stats.existing_rekeyed += 1
                updated = dict(record)
                updated["paper_dir"] = ensure_pdf_for_key(old_key, new_key, updated, args, stats)
                output[new_key] = updated
    return output


def append_topup_records(
    output: dict[str, Any],
    groups: dict[tuple[str, str], list[tuple[str, dict[str, Any]]]],
    venues: list[builder.VenueSpec],
    args: argparse.Namespace,
    stats: RebalanceStats,
) -> None:
    existing_keys = set(output)
    for venue in venues:
        for bucket in ("accept", "reject"):
            next_index = max(
                [old_index(key) for key, _ in groups[(venue.conference, bucket)] if not key.startswith("topup_")]
                or [0]
            )
            for old_key, record in sort_group_items(groups[(venue.conference, bucket)]):
                if not old_key.startswith("topup_"):
                    continue
                next_index += 1
                new_key = make_key(
                    venue.conference,
                    bucket,
                    int(record.get("year") or venue.year),
                    next_index,
                    str(record.get("title") or "Untitled"),
                )
                while new_key in existing_keys:
                    next_index += 1
                    new_key = make_key(
                        venue.conference,
                        bucket,
                        int(record.get("year") or venue.year),
                        next_index,
                        str(record.get("title") or "Untitled"),
                    )
                updated = dict(record)
                updated["paper_dir"] = ensure_pdf_for_key(old_key, new_key, updated, args, stats)
                output[new_key] = updated
                existing_keys.add(new_key)


def print_summary(dataset: dict[str, Any], venues: list[builder.VenueSpec], target: int) -> None:
    print("\nRebalanced summary:")
    for venue in venues:
        for bucket in ("accept", "reject"):
            records = [
                record
                for record in dataset.values()
                if isinstance(record, dict)
                and record.get("conference") == venue.conference
                and record.get("accept_or_not") == bucket
            ]
            short = sum(len(record.get("reviews") or []) < 3 for record in records)
            print(f"  {venue.conference} {bucket}: {len(records)} papers, short_review_papers={short}")
            if len(records) < target:
                print(f"    Warning: still below target {target}")


def rebalance_dataset(args: argparse.Namespace) -> tuple[dict[str, Any], RebalanceStats]:
    input_path = Path(args.input)
    dataset = load_dataset(input_path)
    venues = venue_specs_for_dataset(dataset, args)
    if not venues:
        raise SystemExit("No venue specs found. Pass --venues CONF:YEAR explicitly.")

    openreview = builder.import_openreview()
    client = builder.get_client(openreview)
    builder.OPENREVIEW_REQUEST_DELAY_SECONDS = args.request_delay

    stats = RebalanceStats()
    groups: dict[tuple[str, str], list[tuple[str, dict[str, Any]]]] = defaultdict(list)
    passthrough: dict[str, Any] = {}
    known_forums: set[str] = set()
    known_urls: set[str] = set()
    top_up_only = getattr(args, "top_up_only", False)
    dropped_existing_keys: set[str] = set()

    included_total = sum(
        1
        for record in dataset.values()
        if isinstance(record, dict) and include_record(record, venues)
    )
    included_index = 0
    for old_key, record in dataset.items():
        if not isinstance(record, dict):
            passthrough[old_key] = record
            continue
        forum = repair.forum_id_from_record(record)
        if forum:
            known_forums.add(forum)
        url = str(record.get("paper_url") or "")
        if url:
            known_urls.add(url)
        if not include_record(record, venues):
            passthrough[old_key] = record
            continue
        if top_up_only:
            stats.existing_seen += 1
            if getattr(args, "drop_empty_segment_papers", False) and has_empty_segment_review(record):
                stats.existing_dropped += 1
                dropped_existing_keys.add(old_key)
                stats.warnings.append(f"{old_key}: at least one review has empty strengths and weaknesses")
                print(f"  dropped: {old_key}; empty review segments", flush=True)
                continue
            bucket = bucket_from_record(record)
            if bucket in {"accept", "reject"}:
                groups[(str(record.get("conference")), bucket)].append((old_key, record))
            else:
                stats.warnings.append(f"{old_key}: could not assign accept/reject bucket")
            continue
        included_index += 1
        print_progress("Refresh existing", included_index, included_total, old_key)
        refreshed = refresh_existing_record(old_key, record, client, args, stats)
        if refreshed is None:
            print(f"  dropped: {old_key}", flush=True)
            continue
        refreshed_key, refreshed_record = refreshed
        forum = repair.forum_id_from_record(refreshed_record)
        if forum:
            known_forums.add(forum)
        url = str(refreshed_record.get("paper_url") or "")
        if url:
            known_urls.add(url)
        bucket = bucket_from_record(refreshed_record)
        if bucket not in {"accept", "reject"}:
            stats.warnings.append(f"{old_key}: could not assign accept/reject bucket")
            stats.existing_dropped += 1
            print(f"  dropped: {old_key}; could not assign accept/reject bucket", flush=True)
            continue
        groups[(str(refreshed_record.get("conference")), bucket)].append((refreshed_key, refreshed_record))
        print(
            f"  kept: {old_key} -> {bucket}, reviews={len(refreshed_record.get('reviews') or [])}",
            flush=True,
        )

    for venue in venues:
        for bucket in ("accept", "reject"):
            top_up_bucket(groups, known_forums, known_urls, client, venue, bucket, args, stats)

    if top_up_only:
        print("Appending top-up records and syncing PDFs...", flush=True)
        output = {key: value for key, value in dataset.items() if key not in dropped_existing_keys}
        append_topup_records(output, groups, venues, args, stats)
    else:
        print("Rekeying records and syncing PDFs...", flush=True)
        output = dict(passthrough)
        output.update(rekey_groups(groups, venues, args, stats))
    return output, stats


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--output", default=DEFAULT_OUTPUT)
    parser.add_argument("--venues", nargs="+", help="Venue specs as CONF:YEAR or CONF:YEAR:OPENREVIEW_VENUE_ID.")
    parser.add_argument("--target-per-category", type=int, default=50)
    parser.add_argument("--reviews-per-paper", type=int, default=3)
    parser.add_argument("--pdf-dir", default="data/openreview_pdf")
    parser.add_argument("--topic", default="Others")
    parser.add_argument("--request-delay", type=float, default=5.0)
    parser.add_argument("--max-topup-forum-checks", type=int, default=500)
    parser.add_argument("--sleep", type=float, default=0.2)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-backup", action="store_true")
    parser.add_argument(
        "--top-up-only",
        action="store_true",
        help="Keep existing records unchanged and only append papers needed to reach target counts.",
    )
    parser.add_argument(
        "--drop-empty-segment-papers",
        action="store_true",
        help="Drop selected papers that have any review with both strengths and weaknesses empty.",
    )
    parser.add_argument("--move-pdfs", action="store_true", help="Move old PDFs instead of copying them.")
    parser.add_argument("--no-download-pdfs", dest="download_pdfs", action="store_false")
    parser.set_defaults(download_pdfs=True)
    parser.add_argument(
        "--keep-short-review-papers",
        dest="drop_short_review_papers",
        action="store_false",
        help="Keep papers that still have fewer than --reviews-per-paper reviews after refetch.",
    )
    parser.set_defaults(drop_short_review_papers=True)
    parser.add_argument("--respect-policy-overrides", action="store_true")
    parser.add_argument("--use-llm-segmentation", action="store_true")
    parser.add_argument("--llm-model", default=builder.DEFAULT_LLM_MODEL)
    parser.add_argument(
        "--llm-base-url",
        default="https://dashscope.aliyuncs.com/compatible-mode/v1",
        help="OpenAI-compatible API base URL. Use empty string for OpenAI's default endpoint.",
    )
    parser.add_argument("--llm-api-key-env", default="DASHSCOPE_API_KEY")
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

    try:
        output, stats = rebalance_dataset(args)
    except Exception as exc:
        if builder.is_openreview_challenge_required_error(exc):
            print(builder.openreview_challenge_message(), file=sys.stderr)
            raise SystemExit(1) from exc
        raise

    output_path = Path(args.output)
    input_path = Path(args.input)
    if args.dry_run:
        print("\nDry run only; no JSON written.")
    else:
        if output_path == input_path and not args.no_backup:
            backup_path = backup_file(input_path)
            print(f"Backup written to {backup_path}")
        write_dataset(output_path, output)
        print(f"\nWrote {len(output)} papers to {output_path}")

    venues = venue_specs_for_dataset(output, args)
    print_summary(output, venues, args.target_per_category)
    print(
        "\nRebalance summary: "
        f"existing_seen={stats.existing_seen}, kept={stats.existing_kept}, "
        f"rekeyed={stats.existing_rekeyed}, short_reviews={stats.existing_short_reviews}, "
        f"dropped={stats.existing_dropped}, topup_checked={stats.topup_checked}, "
        f"topup_added={stats.topup_added}, pdf_copied={stats.pdf_copied}, "
        f"pdf_moved={stats.pdf_moved}, pdf_downloaded={stats.pdf_downloaded}, "
        f"pdf_missing={stats.pdf_missing}, warnings={len(stats.warnings)}"
    )
    if stats.warnings:
        print("First warnings:")
        for warning in stats.warnings[:20]:
            print(f"  - {warning}")


if __name__ == "__main__":
    main()

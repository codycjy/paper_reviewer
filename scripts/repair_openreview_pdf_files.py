#!/usr/bin/env python3
"""
Download missing OpenReview PDFs for an existing evaluation dataset.

This is intentionally PDF-only: it does not refetch reviews, decisions, or rekey
records. It fills paper_dir for records whose local PDF is missing by using the
OpenReview API client's authenticated get_pdf/get_attachment methods before
falling back to direct URL download.
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


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import scripts.build_openreview_eval_dataset as builder
import scripts.repair_openreview_eval_dataset as repair


DEFAULT_INPUT = "eval/openreview_2025_300_qwen.rebalanced.icml_topup.json"


@dataclass
class PdfRepairStats:
    seen: int = 0
    already_present: int = 0
    downloaded: int = 0
    failed: int = 0
    updated_records: int = 0
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


def local_pdf_path(key: str, args: argparse.Namespace) -> Path:
    return abs_or_repo_path(Path(args.pdf_dir) / f"{key}.pdf")


def existing_pdf_path(key: str, record: dict[str, Any], args: argparse.Namespace) -> Optional[Path]:
    candidates = []
    paper_dir = str(record.get("paper_dir") or "").strip()
    if paper_dir:
        candidates.append(abs_or_repo_path(paper_dir))
    candidates.append(local_pdf_path(key, args))
    for candidate in dict.fromkeys(candidates):
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


def download_via_client(client: Any, forum: str, destination: Path) -> bool:
    for getter in (
        lambda: client.get_pdf(forum),
        lambda: client.get_attachment("pdf", id=forum),
    ):
        try:
            data = getter()
        except Exception:
            continue
        if data:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
            return True
    return False


def download_pdf_for_record(
    key: str,
    record: dict[str, Any],
    client: Any,
    args: argparse.Namespace,
    stats: PdfRepairStats,
) -> Optional[str]:
    target = local_pdf_path(key, args)
    existing = existing_pdf_path(key, record, args)
    if existing:
        stats.already_present += 1
        return display_path(existing)

    if args.dry_run:
        stats.downloaded += 1
        return display_path(target)

    forum = repair.forum_id_from_record(record)
    if forum and download_via_client(client, forum, target):
        stats.downloaded += 1
        return display_path(target)

    for pdf_url in pdf_urls_for_record(record):
        if builder.download_pdf(pdf_url, target, sleep_seconds=args.sleep):
            stats.downloaded += 1
            return display_path(target)

    stats.failed += 1
    stats.warnings.append(f"{key}: failed to download PDF")
    return None


def should_process_record(key: str, record: dict[str, Any], args: argparse.Namespace) -> bool:
    if args.only_key and key not in args.only_key:
        return False
    if args.only_missing and existing_pdf_path(key, record, args):
        return False
    return True


def repair_pdfs(args: argparse.Namespace) -> tuple[dict[str, Any], PdfRepairStats]:
    dataset = load_dataset(Path(args.input))
    openreview = builder.import_openreview()
    client = builder.get_client(openreview)
    stats = PdfRepairStats()

    items = [(key, record) for key, record in dataset.items() if isinstance(record, dict)]
    selected = [(key, record) for key, record in items if should_process_record(key, record, args)]
    for index, (key, record) in enumerate(selected, start=1):
        stats.seen += 1
        print(f"[{index}/{len(selected)}] PDF {key}", flush=True)
        paper_dir = download_pdf_for_record(key, record, client, args, stats)
        if not paper_dir:
            print("  failed", flush=True)
            continue
        if record.get("paper_dir") != paper_dir:
            updated = dict(record)
            updated["paper_dir"] = paper_dir
            dataset[key] = updated
            stats.updated_records += 1
            print(f"  paper_dir -> {paper_dir}", flush=True)
        else:
            print("  already present", flush=True)
    return dataset, stats


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default=DEFAULT_INPUT)
    parser.add_argument("--output", help="Defaults to --input for in-place repair.")
    parser.add_argument("--pdf-dir", default="data/openreview_pdf")
    parser.add_argument("--only-missing", action="store_true", help="Skip records whose local PDF already exists.")
    parser.add_argument("--only-key", nargs="+", help="Repair exact dataset keys only.")
    parser.add_argument("--sleep", type=float, default=0.2)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--no-backup", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path
    dataset, stats = repair_pdfs(args)

    if args.dry_run:
        print("\nDry run only; no JSON written.")
    else:
        if output_path == input_path and not args.no_backup:
            backup_path = backup_file(input_path)
            print(f"Backup written to {backup_path}")
        write_dataset(output_path, dataset)
        print(f"\nWrote {len(dataset)} papers to {output_path}")

    print(
        "PDF repair summary: "
        f"seen={stats.seen}, already_present={stats.already_present}, "
        f"downloaded={stats.downloaded}, updated_records={stats.updated_records}, "
        f"failed={stats.failed}, warnings={len(stats.warnings)}"
    )
    if stats.warnings:
        print("First warnings:")
        for warning in stats.warnings[:20]:
            print(f"  - {warning}")


if __name__ == "__main__":
    main()

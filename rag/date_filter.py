from __future__ import annotations

from datetime import date

from .models import PaperMetadata


def _parse_date(value: str | None) -> date | None:
    if not value:
        return None
    try:
        return date.fromisoformat(value[:10])
    except ValueError:
        return None


def filter_by_cutoff(
    papers: list[PaperMetadata],
    cutoff_date: str,
    allow_undated: bool = False,
) -> tuple[list[PaperMetadata], dict]:
    cutoff = _parse_date(cutoff_date)
    if cutoff is None:
        raise ValueError(f"Invalid cutoff_date: {cutoff_date}")

    used: list[PaperMetadata] = []
    removed_post = 0
    removed_undated = 0
    for paper in papers:
        publication = _parse_date(paper.publication_date)
        if publication is None and paper.year:
            publication = _parse_date(f"{paper.year}-12-31")
        if publication is None:
            if allow_undated:
                used.append(paper)
            else:
                removed_undated += 1
            continue
        if publication > cutoff:
            removed_post += 1
            continue
        used.append(paper)

    return used, {
        "cutoff_date": cutoff_date,
        "allow_undated_evidence": allow_undated,
        "num_retrieved": len(papers),
        "num_removed_post_cutoff": removed_post,
        "num_removed_undated": removed_undated,
        "num_used": len(used),
    }

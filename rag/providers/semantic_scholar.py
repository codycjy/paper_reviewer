from __future__ import annotations

import os
from typing import Any

from rag.models import PaperMetadata, RelatedWorkQuery

from .base import (
    PaperSearchProvider,
    ProviderResult,
    encoded_query,
    is_forbidden_error,
    is_rate_limited_error,
    per_query_limit,
)


class SemanticScholarProvider(PaperSearchProvider):
    name = "Semantic Scholar"
    inter_query_delay_seconds = 3.0

    def search(self, queries: list[RelatedWorkQuery], limit: int = 10) -> ProviderResult:
        warnings: list[str] = []
        papers: list[PaperMetadata] = []
        seen: dict[str, PaperMetadata] = {}
        headers = {}
        if os.environ.get("SEMANTIC_SCHOLAR_API_KEY"):
            headers["x-api-key"] = os.environ["SEMANTIC_SCHOLAR_API_KEY"]
        fields = "title,authors,year,publicationDate,venue,abstract,url,citationCount,externalIds"
        query_limit = per_query_limit(limit, len(queries))
        for index, query in enumerate(queries):
            self._sleep_between_queries(index)
            if not encoded_query(query.query):
                warnings.append(f"Semantic Scholar query skipped for {query.group}: no search terms were available.")
                continue
            url = (
                "https://api.semanticscholar.org/graph/v1/paper/search"
                f"?query={encoded_query(query.query)}&limit={query_limit}&fields={fields}"
            )
            try:
                data = self._json_get(url, headers=headers)
            except Exception as exc:
                if is_rate_limited_error(exc):
                    warnings.append(
                        "Semantic Scholar rate-limited related-work search (HTTP 429); "
                        "skipped remaining Semantic Scholar queries. Configure SEMANTIC_SCHOLAR_API_KEY "
                        "or retry later."
                    )
                    break
                if is_forbidden_error(exc):
                    warnings.append(
                        "Semantic Scholar denied related-work search (HTTP 403); "
                        "skipped remaining Semantic Scholar queries."
                    )
                    break
                warnings.append(f"Semantic Scholar query failed for {query.group}: {exc}")
                continue
            for item in data.get("data", []):
                paper = self._parse_item(item, query.group)
                key = paper.doi or paper.arxiv_id or paper.source_ids.get("Semantic Scholar", "") or paper.title.lower()
                if key in seen:
                    seen[key].matched_query_groups = sorted(set(seen[key].matched_query_groups + [query.group]))
                    continue
                seen[key] = paper
                papers.append(paper)
        status = "used" if papers else "failed"
        if not papers and any("rate-limited" in warning for warning in warnings):
            status = "rate_limited"
        elif not papers and any("denied" in warning for warning in warnings):
            status = "forbidden"
        return ProviderResult(provider=self.name, papers=papers[:limit], warnings=warnings, status=status)

    def _parse_item(self, item: dict[str, Any], query_group: str) -> PaperMetadata:
        external = item.get("externalIds") or {}
        doi = (external.get("DOI") or "").lower()
        arxiv_id = external.get("ArXiv") or ""
        authors = [a.get("name", "") for a in item.get("authors", []) if a.get("name")]
        return PaperMetadata(
            paper_id="",
            title=item.get("title") or "",
            authors=authors,
            year=item.get("year"),
            publication_date=item.get("publicationDate"),
            venue=item.get("venue") or "",
            abstract=item.get("abstract") or "",
            url=item.get("url") or "",
            doi=doi,
            arxiv_id=arxiv_id,
            source_ids={"Semantic Scholar": item.get("paperId") or ""},
            sources=["Semantic Scholar"],
            matched_query_groups=[query_group],
            citation_count=item.get("citationCount"),
        )

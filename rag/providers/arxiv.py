from __future__ import annotations

import re
import xml.etree.ElementTree as ET

from rag.models import PaperMetadata, RelatedWorkQuery

from .base import PaperSearchProvider, ProviderResult, clean_search_query, encoded_query, per_query_limit


ATOM = "{http://www.w3.org/2005/Atom}"


def _text(parent: ET.Element, tag: str) -> str:
    found = parent.find(f"{ATOM}{tag}")
    return (found.text or "").strip() if found is not None else ""


class ArxivProvider(PaperSearchProvider):
    name = "arXiv"
    inter_query_delay_seconds = 3.0

    def search(self, queries: list[RelatedWorkQuery], limit: int = 10) -> ProviderResult:
        warnings: list[str] = []
        papers: list[PaperMetadata] = []
        seen: dict[str, PaperMetadata] = {}
        query_limit = per_query_limit(limit, len(queries))
        for index, query in enumerate(queries):
            self._sleep_between_queries(index)
            terms = " ".join(re.findall(r"[A-Za-z0-9][A-Za-z0-9_-]{2,}", clean_search_query(query.query))[:10])
            if not terms:
                warnings.append(f"arXiv query skipped for {query.group}: no search terms were available.")
                continue
            url = (
                "https://export.arxiv.org/api/query"
                f"?search_query=all:{encoded_query(terms)}"
                f"&start=0&max_results={query_limit}&sortBy=relevance&sortOrder=descending"
            )
            try:
                xml_text = self._text_get(url)
                root = ET.fromstring(xml_text)
            except Exception as exc:
                warnings.append(f"arXiv query failed for {query.group}: {exc}")
                continue
            for entry in root.findall(f"{ATOM}entry"):
                paper = self._parse_entry(entry, query.group)
                key = paper.arxiv_id or paper.title.lower()
                if key in seen:
                    seen[key].matched_query_groups = sorted(set(seen[key].matched_query_groups + [query.group]))
                    continue
                seen[key] = paper
                papers.append(paper)
        return ProviderResult(provider=self.name, papers=papers[:limit], warnings=warnings, status="used" if papers else "failed")

    def _parse_entry(self, entry: ET.Element, query_group: str) -> PaperMetadata:
        entry_id = _text(entry, "id")
        arxiv_id = entry_id.rstrip("/").split("/")[-1]
        authors = [
            _text(author, "name")
            for author in entry.findall(f"{ATOM}author")
            if _text(author, "name")
        ]
        published = _text(entry, "published")[:10] or None
        year = int(published[:4]) if published and published[:4].isdigit() else None
        return PaperMetadata(
            paper_id="",
            title=re.sub(r"\s+", " ", _text(entry, "title")),
            authors=authors,
            year=year,
            publication_date=published,
            venue="arXiv",
            abstract=re.sub(r"\s+", " ", _text(entry, "summary")),
            url=entry_id,
            arxiv_id=arxiv_id,
            source_ids={"arXiv": arxiv_id},
            sources=["arXiv"],
            matched_query_groups=[query_group],
        )

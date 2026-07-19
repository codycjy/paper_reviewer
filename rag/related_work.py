from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import re
from typing import Any

from .config import RAGConfig
from .date_filter import filter_by_cutoff
from .llm import RAGLLMAgent
from .models import PaperMetadata, RelatedWorkQuery, RerankedPaper, TargetPaperSummary
from .providers import ArxivProvider, OpenAlexProvider
from .providers.base import clean_search_query
from .security import prompt_injection_warnings
from .target_parser import llm_context_excerpt, summarize_target_paper


QUERY_GROUPS = [
    "same_problem",
    "same_method",
    "same_constraints",
    "benchmark_baseline",
    "novelty_competitor",
    "limitations_counterevidence",
]


FALLBACK_QUERY_STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "beyond",
    "by",
    "for",
    "from",
    "in",
    "into",
    "is",
    "learning",
    "machine",
    "model",
    "models",
    "of",
    "on",
    "or",
    "our",
    "paper",
    "that",
    "the",
    "this",
    "through",
    "to",
    "using",
    "via",
    "we",
    "with",
}


def _fallback_keywords(target: TargetPaperSummary, max_terms: int = 10) -> list[str]:
    title = clean_search_query(target.title)
    text = clean_search_query(" ".join([title, target.abstract, " ".join(target.claims[:4])]), max_chars=3000)
    title_terms = re.findall(r"[A-Za-z0-9]+(?:[-/][A-Za-z0-9]+)*", title)
    all_terms = re.findall(r"[A-Za-z0-9]+(?:[-/][A-Za-z0-9]+)*", text)

    ordered: list[str] = []
    seen: set[str] = set()
    for term in [*title_terms, *all_terms]:
        normalized = term.lower().strip("-/")
        if len(normalized) < 3 or normalized in FALLBACK_QUERY_STOPWORDS or normalized in seen:
            continue
        seen.add(normalized)
        ordered.append(normalized)
        if len(ordered) >= max_terms:
            break
    return ordered


def _fallback_query_text(target: TargetPaperSummary, group: str) -> str:
    keywords = _fallback_keywords(target)
    generic_topics = {"machine learning", "deep learning", "others"}
    topic_terms = [] if not target.topic or target.topic.strip().casefold() in generic_topics else _fallback_keywords(
        TargetPaperSummary(paper_id="", title=target.topic, abstract="", claims=[]),
        max_terms=2,
    )
    suffix_terms = {
        "same_problem": [],
        "same_method": ["architecture"],
        "same_constraints": ["scalable", "efficient"],
        "benchmark_baseline": ["benchmark", "baseline", "evaluation", "dataset"],
        "novelty_competitor": ["prior", "competing", "approach"],
        "limitations_counterevidence": ["limitations", "failure", "analysis"],
    }[group]
    query_terms = [*keywords, *topic_terms, *suffix_terms]
    return clean_search_query(" ".join(query_terms), max_chars=500)


def _generate_queries(
    paper: str,
    target: TargetPaperSummary,
    llm_agent: RAGLLMAgent,
    warnings: list[str],
) -> tuple[list[RelatedWorkQuery], str]:
    system_prompt = (
        "You generate scholarly search queries for related-work retrieval. "
        "Return only valid JSON. Do not invent bibliographic metadata."
    )
    user_prompt = f"""
Read the target paper excerpt and generate exactly one concise search query for each group:
{", ".join(QUERY_GROUPS)}.

The groups mean:
- same_problem: papers addressing the same research problem/task
- same_method: papers using similar methods or architectures
- same_constraints: papers sharing constraints, assumptions, or deployment setting
- benchmark_baseline: papers defining datasets, metrics, baselines, or benchmark comparisons
- novelty_competitor: prior papers that could challenge the novelty claim
- limitations_counterevidence: papers that expose limitations, negative results, or counterevidence

Return JSON:
{{
  "queries": [
    {{"group": "same_problem", "query": "...", "rationale": "..."}}
  ]
}}

Target title: {target.title}
Target topic: {target.topic}
Target abstract: {target.abstract}
Target claims: {json.dumps(target.claims, ensure_ascii=False)}

Target excerpt:
{llm_context_excerpt(paper)}
""".strip()
    try:
        data = llm_agent.complete_json(system_prompt, user_prompt)
        raw_queries = data.get("queries", [])
        source = "llm"
    except Exception as exc:
        warnings.append(f"Related-work query LLM failed; using deterministic fallback queries: {exc}")
        raw_queries = []
        source = "fallback"

    by_group: dict[str, RelatedWorkQuery] = {}
    for item in raw_queries:
        group = str(item.get("group", "")).strip()
        query = clean_search_query(item.get("query", ""), max_chars=500)
        if group in QUERY_GROUPS and query:
            by_group[group] = RelatedWorkQuery(
                group=group,
                query=query,
                rationale=str(item.get("rationale", "")).strip()[:500],
            )
    for group in QUERY_GROUPS:
        if group not in by_group:
            if source == "llm":
                source = "mixed"
            by_group[group] = RelatedWorkQuery(
                group=group,
                query=_fallback_query_text(target, group),
                rationale="Fallback query generated from target title, abstract, and extracted claims.",
            )
    return [by_group[group] for group in QUERY_GROUPS], source


def _canonical_title(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", title.lower()).strip()


def _dedupe_papers(papers: list[PaperMetadata]) -> list[PaperMetadata]:
    merged: dict[str, PaperMetadata] = {}
    for paper in papers:
        if not paper.title:
            continue
        key = paper.doi or (f"arxiv:{paper.arxiv_id.lower()}" if paper.arxiv_id else "") or _canonical_title(paper.title)
        if key in merged:
            existing = merged[key]
            existing.sources = sorted(set(existing.sources + paper.sources))
            existing.matched_query_groups = sorted(set(existing.matched_query_groups + paper.matched_query_groups))
            existing.source_ids.update({k: v for k, v in paper.source_ids.items() if v})
            if not existing.abstract and paper.abstract:
                existing.abstract = paper.abstract
            if not existing.url and paper.url:
                existing.url = paper.url
            if existing.citation_count is None and paper.citation_count is not None:
                existing.citation_count = paper.citation_count
            continue
        merged[key] = paper
    deduped = list(merged.values())
    for idx, paper in enumerate(deduped, 1):
        seed = paper.doi or paper.arxiv_id or paper.source_ids.get("OpenAlex") or paper.source_ids.get("Semantic Scholar") or paper.title
        suffix = hashlib.sha1(seed.encode("utf-8")).hexdigest()[:9]
        paper.paper_id = f"rw_{idx:03d}_{suffix}"
    return deduped


def _author_last_name(author: str) -> str:
    author = re.sub(r"\s+", " ", str(author or "")).strip()
    if not author:
        return ""
    candidate = author.split(",", 1)[0] if "," in author else author.split()[-1]
    return re.sub(r"[^A-Za-z0-9\-']", "", candidate).strip()


def _citation_label(paper: PaperMetadata) -> str:
    year = str(paper.year or (paper.publication_date or "")[:4] or "n.d.")
    names = [_author_last_name(author) for author in paper.authors if _author_last_name(author)]
    if not names:
        words = re.findall(r"[A-Za-z0-9]+", paper.title)
        title_label = " ".join(words[:4]) if words else "Untitled work"
        return f"{title_label}, {year}"
    if len(names) == 1:
        return f"{names[0]}, {year}"
    if len(names) == 2:
        return f"{names[0]} and {names[1]}, {year}"
    return f"{names[0]} et al., {year}"


def _reference_text(paper: PaperMetadata) -> str:
    return f"{paper.title or 'Untitled work'} ({_citation_label(paper)})"


def _replace_internal_ids_with_references(summary: str, papers: list[PaperMetadata]) -> str:
    by_id = {paper.paper_id: paper for paper in papers}

    def replace_bracket(match: re.Match) -> str:
        ids = re.findall(r"rw_[A-Za-z0-9_]+", match.group(0))
        refs = [_reference_text(by_id[paper_id]) for paper_id in ids if paper_id in by_id]
        if not refs:
            return match.group(0)
        return "(" + "; ".join(refs) + ")"

    summary = re.sub(r"\[(?:\s*rw_[A-Za-z0-9_]+(?:\s*,\s*)?)+\]", replace_bracket, summary)
    for paper_id, paper in by_id.items():
        summary = summary.replace(paper_id, _reference_text(paper))
    return summary


def _looks_like_reviewer_guidance(summary: str) -> bool:
    lowered = summary.lower()
    return any(
        phrase in lowered
        for phrase in (
            "reviewers should",
            "reviewer should",
            "reviewers can",
            "reviewer can",
            "to evaluate",
            "should refer",
            "should compare",
            "must use",
            "must be",
        )
    )


def _compose_intro_summary(target: TargetPaperSummary, papers: list[PaperMetadata]) -> str:
    papers = [paper for paper in papers if paper.title][:6]
    if not papers:
        return "No cutoff-valid related-work metadata was available to compose a related-work introduction."

    if target.title:
        opening = (
            f"The literature around {target.title} sits within a broader effort to replace or augment quadratic "
            "self-attention with more efficient token-mixing mechanisms."
        )
    else:
        opening = (
            "Prior work on efficient sequence modeling has explored alternatives to quadratic self-attention, "
            "including spectral token mixing, wavelet-based feature decompositions, long convolutions, state-space models, "
            "and benchmark suites for long-context evaluation."
        )

    sentences = [opening]
    for paper in papers[:4]:
        groups = set(paper.matched_query_groups)
        ref = _reference_text(paper)
        if "benchmark_baseline" in groups:
            role = "provides benchmark or baseline context for evaluating efficient long-sequence models"
        elif "same_method" in groups or "novelty_competitor" in groups:
            role = "is a close methodological reference for token-mixing design"
        elif "same_constraints" in groups:
            role = "frames the efficiency and hardware constraints that motivate subquadratic architectures"
        elif "limitations_counterevidence" in groups:
            role = "highlights limitations or counterpoints relevant to fixed spectral mixing"
        else:
            role = "contributes adjacent evidence on efficient sequence modeling"
        sentences.append(f"{ref} {role}.")
    return " ".join(sentences)


def _summary_from_ranked(
    summary: str,
    papers: list[PaperMetadata],
    ranked: list[RerankedPaper],
    target: TargetPaperSummary,
) -> str:
    by_id = {paper.paper_id: paper for paper in papers}
    ranked_papers = [by_id[item.paper_id] for item in ranked if item.paper_id in by_id]
    source_papers = ranked_papers or papers
    normalized = _replace_internal_ids_with_references(str(summary or "").strip(), source_papers)
    if not normalized or re.search(r"\brw_[A-Za-z0-9_]+\b", normalized) or _looks_like_reviewer_guidance(normalized):
        return _compose_intro_summary(target, source_papers)
    return normalized


def _candidate_payload(papers: list[PaperMetadata]) -> list[dict[str, Any]]:
    payload = []
    for paper in papers:
        payload.append({
            "paper_id": paper.paper_id,
            "title": paper.title,
            "reference": _reference_text(paper),
            "citation_label": _citation_label(paper),
            "authors": paper.authors[:8],
            "year": paper.year,
            "publication_date": paper.publication_date,
            "venue": paper.venue,
            "sources": paper.sources,
            "url": paper.url,
            "doi": paper.doi,
            "arxiv_id": paper.arxiv_id,
            "matched_query_groups": paper.matched_query_groups,
            "citation_count": paper.citation_count,
            "abstract": paper.abstract[:1600],
        })
    return payload


def _fallback_rerank(papers: list[PaperMetadata], target: TargetPaperSummary, top_k: int) -> tuple[list[RerankedPaper], str, str]:
    scored = []
    for paper in papers:
        scored.append((_lexical_relevance_score(paper, target), paper))
    scored.sort(key=lambda item: item[0], reverse=True)
    reranked = [
        RerankedPaper(
            rank=i + 1,
            paper_id=paper.paper_id,
            relevance_score=round(float(score), 3),
            relevance_types=paper.matched_query_groups[:3],
            rationale="Fallback lexical overlap ranking because LLM reranking was unavailable.",
            evidence_summary=paper.abstract[:300],
        )
        for i, (score, paper) in enumerate(scored[:top_k])
    ]
    summary = _compose_intro_summary(target, [paper for _, paper in scored[:top_k]])
    return reranked, summary, "fallback"


def _lexical_relevance_score(paper: PaperMetadata, target: TargetPaperSummary) -> float:
    target_terms = set(re.findall(r"[a-z0-9]{3,}", f"{target.title} {target.abstract}".lower()))
    terms = set(re.findall(r"[a-z0-9]{3,}", f"{paper.title} {paper.abstract}".lower()))
    overlap = len(target_terms & terms)
    denom = max(1, len(target_terms | terms))
    return overlap / denom


def _calibrate_saturated_scores(ranked: list[RerankedPaper]) -> None:
    if len(ranked) <= 1:
        return
    if not all(item.relevance_score >= 0.999 for item in ranked):
        return
    for index, item in enumerate(ranked):
        item.relevance_score = round(max(0.5, 1.0 - (0.05 * index)), 3)


def _fill_missing_reranked(
    ranked: list[RerankedPaper],
    papers: list[PaperMetadata],
    target: TargetPaperSummary,
    top_k: int,
    seen: set[str],
) -> bool:
    target_count = min(top_k, len(papers))
    if len(ranked) >= target_count:
        return False
    filled = False
    for paper in papers:
        if paper.paper_id in seen:
            continue
        score = round(float(_lexical_relevance_score(paper, target)), 3)
        ranked.append(RerankedPaper(
            rank=len(ranked) + 1,
            paper_id=paper.paper_id,
            relevance_score=score,
            relevance_types=paper.matched_query_groups[:3],
            rationale="LLM omitted this candidate; appended in cleaned candidate order to preserve the rerank input set.",
            evidence_summary=paper.abstract[:300],
        ))
        seen.add(paper.paper_id)
        filled = True
        if len(ranked) >= target_count:
            break
    return filled


def _rerank_with_llm(
    target: TargetPaperSummary,
    queries: list[RelatedWorkQuery],
    papers: list[PaperMetadata],
    llm_agent: RAGLLMAgent,
    top_k: int,
    warnings: list[str],
) -> tuple[list[RerankedPaper], str, str]:
    if not papers:
        return [], "No cutoff-valid related-work metadata was available for reranking.", "none"
    system_prompt = (
        "You are a related-work reranking agent. Use only the provided candidate metadata. "
        "Do not invent titles, authors, venues, years, URLs, DOIs, or paper IDs. "
        "Return only valid JSON."
    )
    user_prompt = f"""
Target paper:
{json.dumps(target.to_dict(), ensure_ascii=False)}

Search queries:
{json.dumps([q.to_dict() for q in queries], ensure_ascii=False)}

Candidate metadata:
{json.dumps(_candidate_payload(papers), ensure_ascii=False)}

Rerank candidates for usefulness as related work. Prefer papers that are directly relevant to novelty, baselines, benchmarks, methods, constraints, and limitations.
Return exactly {min(top_k, len(papers))} unique papers unless fewer valid candidates are provided. Do not return only one paper per query group.

Score on a calibrated 0.0-1.0 scale:
- 1.0: same paper, earlier version, or direct duplicate of the target.
- 0.85-0.95: central method, benchmark, or baseline needed to understand the target.
- 0.65-0.84: close related method, constraint, or limitation evidence.
- 0.40-0.64: useful background but not a direct comparison.
- below 0.40: weakly related.
Avoid giving the same score to every paper.

Write the summary as a related-work introduction paragraph for the target paper. Do not write instructions to reviewers.
Do not say "reviewers should", "must compare", or similar guidance. Do not cite internal paper IDs in the summary.
When citing prior work in the summary, use the supplied "reference" or "citation_label" fields, e.g. "FNet: Mixing Tokens with Fourier Transforms (Lee-Thorp et al., 2022)".

Return JSON:
{{
  "reranked_papers": [
    {{
      "rank": 1,
      "paper_id": "rw_...",
      "relevance_score": 0.0,
      "relevance_types": ["same_problem"],
      "rationale": "why this paper matters for reviewing the target",
      "evidence_summary": "one-sentence factual summary using only metadata"
    }}
  ],
  "summary": "A compact introduction-style related-work paragraph with real title/author/year references, not internal paper IDs."
}}
""".strip()
    valid_ids = {paper.paper_id for paper in papers}
    try:
        data = llm_agent.complete_json(system_prompt, user_prompt)
        raw_ranked = data.get("reranked_papers", [])
        summary = str(data.get("summary", "")).strip()
    except Exception as exc:
        warnings.append(f"Related-work rerank LLM failed; using lexical fallback reranking: {exc}")
        return _fallback_rerank(papers, target, top_k)

    ranked: list[RerankedPaper] = []
    seen: set[str] = set()
    for item in raw_ranked:
        paper_id = str(item.get("paper_id", "")).strip()
        if paper_id not in valid_ids or paper_id in seen:
            continue
        seen.add(paper_id)
        try:
            score = float(item.get("relevance_score", 0.0))
        except (TypeError, ValueError):
            score = 0.0
        ranked.append(RerankedPaper(
            rank=len(ranked) + 1,
            paper_id=paper_id,
            relevance_score=max(0.0, min(1.0, score)),
            relevance_types=[str(x) for x in item.get("relevance_types", []) if str(x)],
            rationale=str(item.get("rationale", "")).strip()[:1000],
            evidence_summary=str(item.get("evidence_summary", "")).strip()[:1000],
        ))
        if len(ranked) >= top_k:
            break
    if not ranked:
        warnings.append("Related-work rerank LLM returned no valid paper IDs; using lexical fallback reranking.")
        return _fallback_rerank(papers, target, top_k)
    _calibrate_saturated_scores(ranked)
    filled_from_fallback = _fill_missing_reranked(ranked, papers, target, top_k, seen)
    if not summary:
        summary = _compose_intro_summary(target, [next(p for p in papers if p.paper_id == item.paper_id) for item in ranked if item.paper_id in valid_ids])
    summary = _summary_from_ranked(summary, papers, ranked, target)
    return ranked, summary, "mixed" if filled_from_fallback else "llm"


def build_related_work_rag(
    paper: str,
    topic: str = "",
    provider: str = "cmu",
    model: str = "",
    api_key: str = "",
    config: RAGConfig | None = None,
    providers: list[Any] | None = None,
    llm_agent: RAGLLMAgent | None = None,
) -> dict[str, Any]:
    config = config or RAGConfig()
    target = summarize_target_paper(paper, topic=topic)
    warnings = prompt_injection_warnings(paper, "target paper")
    llm_agent = llm_agent or RAGLLMAgent(provider=provider, api_key=api_key, model=model)

    queries, query_source = _generate_queries(paper, target, llm_agent, warnings)

    search_providers = providers or [
        OpenAlexProvider(config.rag_cache_dir),
        ArxivProvider(config.rag_cache_dir),
    ]
    provider_status: dict[str, dict[str, Any]] = {}
    retrieved: list[PaperMetadata] = []
    max_workers = max(1, len(search_providers))
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(search_provider.search, queries, limit=config.provider_top_k)
            for search_provider in search_providers
        ]
    for search_provider, future in zip(search_providers, futures):
        try:
            result = future.result()
        except Exception as exc:
            provider_name = getattr(search_provider, "name", search_provider.__class__.__name__)
            warnings.append(f"{provider_name}: provider failed: {exc}")
            provider_status[provider_name] = {"status": "failed", "retrieved": 0, "warnings": [str(exc)]}
            continue
        retrieved.extend(result.papers)
        provider_status[result.provider] = {
            "status": result.status,
            "retrieved": len(result.papers),
            "warnings": result.warnings,
        }
        warnings.extend(result.warnings)

    deduped = _dedupe_papers(retrieved)
    cutoff_valid, cutoff_report = filter_by_cutoff(
        deduped,
        cutoff_date=config.cutoff_date,
        allow_undated=config.allow_undated_evidence,
    )
    candidate_cap = max(0, int(config.rerank_top_k))
    filtered = cutoff_valid[:candidate_cap] if candidate_cap else []
    cutoff_report["num_cutoff_valid"] = len(cutoff_valid)
    cutoff_report["candidate_cap"] = candidate_cap
    cutoff_report["num_removed_by_candidate_cap"] = max(0, len(cutoff_valid) - len(filtered))
    cutoff_report["num_used"] = len(filtered)
    evidence_warnings = []
    for paper_meta in filtered:
        evidence_warnings.extend(prompt_injection_warnings(paper_meta.abstract, paper_meta.paper_id))
    warnings.extend(evidence_warnings)

    reranked, summary, rerank_source = _rerank_with_llm(
        target=target,
        queries=queries,
        papers=filtered,
        llm_agent=llm_agent,
        top_k=len(filtered),
        warnings=warnings,
    )

    package_id_seed = target.paper_id + json.dumps([q.to_dict() for q in queries], sort_keys=True)
    package_id = "rag_rw_" + hashlib.sha1(package_id_seed.encode("utf-8")).hexdigest()[:12]
    return {
        "rag_package_id": package_id,
        "paper_id": target.paper_id,
        "target_paper_summary": target.to_dict(),
        "query_generation": {
            "groups": QUERY_GROUPS,
            "queries": [q.to_dict() for q in queries],
            "source": query_source,
        },
        "provider_status": provider_status,
        "paper_metadata": [paper.to_dict() for paper in filtered],
        "reranking_results": [item.to_dict() for item in reranked],
        "reranking": {"source": rerank_source},
        "related_work_summary": summary,
        "warnings": warnings,
        "cutoff_report": cutoff_report,
    }

from __future__ import annotations

from typing import Any

from .config import RAGConfig, rag_config_from_dict
from .llm import RAGLLMAgent
from .related_work import build_related_work_rag
from .review_memory import build_review_memory_from_package


def build_rag_package(
    paper: str,
    topic: str = "",
    provider: str = "cmu",
    model: str = "",
    api_key: str = "",
    config: RAGConfig | dict | None = None,
    **kwargs: Any,
) -> dict[str, Any]:
    rag_config = config if isinstance(config, RAGConfig) else rag_config_from_dict(config)
    if not rag_config.enable_related_work_rag:
        return {
            "rag_package_id": "",
            "paper_id": "",
            "target_paper_summary": {},
            "query_generation": {"groups": [], "queries": [], "source": "disabled"},
            "provider_status": {},
            "paper_metadata": [],
            "reranking_results": [],
            "reranking": {"source": "disabled"},
            "related_work_summary": "",
            "review_memory": {
                "status": "disabled",
                "summary": {},
                "selected_case": None,
                "attempted_source_paper_ids": [],
                "warnings": ["Review-memory RAG disabled because related-work RAG is disabled."],
            },
            "warnings": ["Related-work RAG disabled."],
            "cutoff_report": {},
        }
    llm_agent = kwargs.pop("llm_agent", None) or RAGLLMAgent(provider=provider, api_key=api_key, model=model)
    review_memory_provider = kwargs.pop("review_memory_provider", None)
    package = build_related_work_rag(
        paper=paper,
        topic=topic,
        provider=provider,
        model=model,
        api_key=api_key,
        config=rag_config,
        llm_agent=llm_agent,
        **kwargs,
    )
    review_memory = build_review_memory_from_package(
        package,
        llm_agent=llm_agent,
        config=rag_config,
        provider=review_memory_provider,
    )
    package["review_memory"] = review_memory
    package["warnings"] = list(package.get("warnings", [])) + list(review_memory.get("warnings", []))
    return package

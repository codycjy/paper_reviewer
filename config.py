from __future__ import annotations

VALID_TOPICS = [
    "Machine Learning",
    "Deep Learning",
    "Generative Models",
    "Transfer Learning",
    "Computer Vision",
    "NLP",
    "AI for Science",
    "Others",
]

DEFAULT_RAG_CONFIG = {
    "enable_rag": False,
    "enable_related_work_rag": True,
    "enable_review_memory_rag": False,
    "cutoff_date": "2024-12-31",
    "allow_undated_evidence": False,
    "rag_cache_dir": "data/rag_cache",
    "provider_top_k": 10,
    "rerank_top_k": 12,
    "review_memory_max_reviews": 4,
}

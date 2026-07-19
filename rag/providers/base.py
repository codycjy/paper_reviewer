from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from typing import Any

from rag.cache import JsonCache
from rag.models import PaperMetadata, RelatedWorkQuery


@dataclass
class ProviderResult:
    provider: str
    papers: list[PaperMetadata] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    status: str = "used"


class ProviderHTTPError(RuntimeError):
    def __init__(self, url: str, status_code: int, reason: str = ""):
        self.url = url
        self.status_code = int(status_code)
        self.reason = str(reason or "").strip()
        message = f"HTTP {self.status_code}"
        if self.reason:
            message = f"{message} {self.reason}"
        super().__init__(message)


def http_status_code(exc: BaseException) -> int | None:
    if isinstance(exc, ProviderHTTPError):
        return exc.status_code
    for attr in ("code", "status", "status_code"):
        value = getattr(exc, attr, None)
        if value is None:
            continue
        try:
            return int(value)
        except (TypeError, ValueError):
            continue
    return None


def is_rate_limited_error(exc: BaseException) -> bool:
    status = http_status_code(exc)
    return status == 429 or "429" in str(exc) or "RateLimitError" in str(exc)


def is_forbidden_error(exc: BaseException) -> bool:
    status = http_status_code(exc)
    return status == 403 or "403" in str(exc)


class PaperSearchProvider:
    name = "provider"
    default_headers = {"User-Agent": "paper-reviewer-rag/1.0"}
    inter_query_delay_seconds = 0.0

    def __init__(self, cache_dir: str = "data/rag_cache", timeout: int = 20):
        self.cache = JsonCache(cache_dir, self.name)
        self.timeout = timeout

    def _sleep_between_queries(self, query_index: int) -> None:
        if query_index > 0 and self.inter_query_delay_seconds > 0:
            time.sleep(self.inter_query_delay_seconds)

    def _json_get(self, url: str, headers: dict[str, str] | None = None) -> Any:
        cached = self.cache.get(url)
        if cached is not None:
            return cached
        request = urllib.request.Request(url, headers={**self.default_headers, **(headers or {})})
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                data = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            reason = getattr(exc, "reason", "") or getattr(exc, "msg", "")
            raise ProviderHTTPError(url, exc.code, reason) from exc
        self.cache.set(url, data)
        return data

    def _text_get(self, url: str, headers: dict[str, str] | None = None) -> str:
        cached = self.cache.get(url)
        if cached is not None:
            return cached
        request = urllib.request.Request(url, headers={**self.default_headers, **(headers or {})})
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                data = response.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as exc:
            reason = getattr(exc, "reason", "") or getattr(exc, "msg", "")
            raise ProviderHTTPError(url, exc.code, reason) from exc
        self.cache.set(url, data)
        return data

    def search(self, queries: list[RelatedWorkQuery], limit: int = 10) -> ProviderResult:
        raise NotImplementedError


def clean_search_query(query: str, max_chars: int = 260) -> str:
    text = str(query or "")
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\*\*\s*anonymous author\(s\)\s*\*\*", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"\banonymous author\(s\)\b", " ", text, flags=re.IGNORECASE)
    text = re.sub(r"[*_`#>\[\]{}|\\~^]+", " ", text)
    text = re.sub(r"[^\w\s\-+/:.,()]", " ", text, flags=re.UNICODE)
    text = re.sub(r"\s+", " ", text).strip(" .,;:-")
    return text[:max_chars].strip(" .,;:-")


def per_query_limit(total_limit: int, num_queries: int) -> int:
    num_queries = max(1, num_queries)
    total_limit = max(1, total_limit)
    return max(1, min(total_limit, (total_limit + num_queries - 1) // num_queries))


def encoded_query(query: str) -> str:
    return urllib.parse.quote_plus(clean_search_query(query))

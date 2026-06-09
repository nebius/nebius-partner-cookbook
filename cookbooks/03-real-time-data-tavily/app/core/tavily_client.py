"""Thin Tavily SDK client for fresh book context."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import requests
from tavily import TavilyClient as TavilySdkClient
from tavily.errors import TimeoutError as TavilyTimeoutError
from tavily.errors import UsageLimitExceededError
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from app.config import Settings


@dataclass
class TavilyResult:
    citation_id: int
    title: str
    url: str
    content: str
    score: float

    def to_public_dict(self) -> dict[str, object]:
        return {
            "citation": self.citation_id,
            "title": self.title,
            "url": self.url,
            "content": self.content,
            "score": self.score,
        }

    def to_context_line(self) -> str:
        return (
            f"[W{self.citation_id}] title={self.title}; url={self.url}; "
            f"score={self.score:.4f}; excerpt={self.content}"
        )


class TavilyClient:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.client = TavilySdkClient(api_key=settings.tavily_api_key)

    @retry(
        retry=retry_if_exception_type(
            (requests.HTTPError, requests.Timeout, TavilyTimeoutError, UsageLimitExceededError)
        ),
        wait=wait_exponential(multiplier=0.5, min=0.5, max=6.0),
        stop=stop_after_attempt(3),
        reraise=True,
    )
    def search(self, query: str) -> list[TavilyResult]:
        body = self.client.search(
            query=query,
            search_depth=self.settings.tavily_search_depth,
            max_results=self.settings.tavily_max_results,
            include_answer=False,
            include_raw_content=False,
            timeout=20.0,
        )
        return self._parse_results(body)

    def _parse_results(self, body: dict[str, Any]) -> list[TavilyResult]:
        parsed: list[TavilyResult] = []
        for index, item in enumerate(body.get("results", []), start=1):
            if not isinstance(item, dict):
                continue
            url = str(item.get("url") or "").strip()
            if not url:
                continue
            parsed.append(
                TavilyResult(
                    citation_id=index,
                    title=str(item.get("title") or url).strip(),
                    url=url,
                    content=str(item.get("content") or "").strip(),
                    score=float(item.get("score") or 0.0),
                )
            )
        return parsed

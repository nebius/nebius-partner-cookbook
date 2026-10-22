"""Thin Tavily SDK client for fresh book context."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, date, datetime, timedelta
from email.utils import parsedate_to_datetime
from typing import Any

import httpx
import requests
from tavily import TavilyClient as TavilySdkClient
from tavily.errors import TimeoutError as TavilyTimeoutError
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

from app.config import Settings

TAVILY_MAX_QUERY_CHARS = 400


@dataclass
class TavilyResult:
    citation_id: int
    title: str
    url: str
    content: str
    score: float
    published_date: str | None = None

    def to_public_dict(self) -> dict[str, object]:
        return {
            "citation": self.citation_id,
            "title": self.title,
            "url": self.url,
            "content": self.content,
            "score": self.score,
            "publishedDate": self.published_date,
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
            (
                httpx.HTTPError,
                requests.HTTPError,
                requests.Timeout,
                TavilyTimeoutError,
            )
        ),
        wait=wait_exponential(multiplier=0.5, min=0.5, max=6.0),
        stop=stop_after_attempt(3),
        reraise=True,
    )
    def search(self, query: str) -> list[TavilyResult]:
        today = datetime.now(UTC).date()
        earliest = today - timedelta(days=self.settings.tavily_max_age_days)
        latest = today + timedelta(days=1)
        body = self.client.search(
            query=query.strip()[:TAVILY_MAX_QUERY_CHARS],
            search_depth=self.settings.tavily_search_depth,
            topic=self.settings.tavily_topic,
            max_results=self.settings.tavily_max_results,
            start_date=earliest.isoformat(),
            end_date=latest.isoformat(),
            exclude_domains=self.settings.tavily_exclude_domains,
            include_answer=False,
            include_raw_content=False,
            timeout=20.0,
        )
        return self._parse_results(body, earliest=earliest, latest=latest)

    def _parse_results(
        self,
        body: dict[str, Any],
        *,
        earliest: date,
        latest: date,
    ) -> list[TavilyResult]:
        parsed: list[TavilyResult] = []
        for item in body.get("results", []):
            if not isinstance(item, dict):
                continue
            url = str(item.get("url") or "").strip()
            score = float(item.get("score") or 0.0)
            published = self._parse_published_date(item.get("published_date"))
            if not url or score < self.settings.tavily_min_score:
                continue
            if published is not None and not earliest <= published < latest:
                continue
            if (
                self.settings.tavily_topic == "news"
                and self.settings.tavily_strict_news_dates
                and published is None
            ):
                continue
            parsed.append(
                TavilyResult(
                    citation_id=len(parsed) + 1,
                    title=str(item.get("title") or url).strip(),
                    url=url,
                    content=str(item.get("content") or "").strip(),
                    score=score,
                    published_date=published.isoformat() if published else None,
                )
            )
        return parsed

    @staticmethod
    def _parse_published_date(value: object) -> date | None:
        raw = str(value or "").strip()
        if not raw:
            return None
        try:
            parsed = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        except ValueError:
            try:
                parsed = parsedate_to_datetime(raw)
            except (TypeError, ValueError):
                return None

        # Date-only and timezone-less sources are interpreted as UTC.
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=UTC)
        return parsed.astimezone(UTC).date()

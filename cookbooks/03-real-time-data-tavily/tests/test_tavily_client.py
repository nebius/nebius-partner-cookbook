"""Tavily quality controls remain deterministic and network-free."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Any

from app.config import Settings
from app.core.tavily_client import TavilyClient


class FakeTavilySdk:
    def __init__(self, response: dict[str, Any]) -> None:
        self.response = response
        self.kwargs: dict[str, object] = {}

    def search(self, **kwargs: object) -> dict[str, Any]:
        self.kwargs = kwargs
        return self.response


def _settings() -> Settings:
    return Settings(
        nebius_api_key="test-nebius",
        pinecone_api_key="test-pinecone",
        pinecone_index_name="test-index",
        tavily_api_key="test-tavily",
        nebius_enable_pricing_lookup=False,
    )


def test_search_passes_explicit_quality_and_date_controls() -> None:
    today = datetime.now(UTC).date()
    sdk = FakeTavilySdk(
        {
            "results": [
                {
                    "title": "Reliable recent review",
                    "url": "https://example.com/review",
                    "content": "A recent review.",
                    "score": 0.91,
                    "published_date": (today - timedelta(days=2)).isoformat(),
                }
            ]
        }
    )
    client = TavilyClient(_settings())
    client.client = sdk  # type: ignore[assignment]

    results = client.search("recent books")

    assert len(results) == 1
    assert results[0].published_date == (today - timedelta(days=2)).isoformat()
    assert sdk.kwargs["search_depth"] == "advanced"
    assert sdk.kwargs["topic"] == "news"
    assert sdk.kwargs["start_date"] == (today - timedelta(days=180)).isoformat()
    assert sdk.kwargs["end_date"] == (today + timedelta(days=1)).isoformat()
    assert sdk.kwargs["exclude_domains"] == ["facebook.com", "reddit.com", "linkedin.com"]


def test_search_rejects_social_stale_low_score_and_undated_results() -> None:
    today = datetime.now(UTC).date()
    sdk = FakeTavilySdk(
        {
            "results": [
                {
                    "title": "Social post",
                    "url": "https://www.reddit.com/r/books/example",
                    "content": "A post.",
                    "score": 0.99,
                    "published_date": today.isoformat(),
                },
                {
                    "title": "Stale article",
                    "url": "https://example.com/stale",
                    "content": "Old.",
                    "score": 0.99,
                    "published_date": (today - timedelta(days=181)).isoformat(),
                },
                {
                    "title": "Weak match",
                    "url": "https://example.com/weak",
                    "content": "Weak.",
                    "score": 0.69,
                    "published_date": today.isoformat(),
                },
                {
                    "title": "Undated article",
                    "url": "https://example.com/undated",
                    "content": "No date.",
                    "score": 0.99,
                },
            ]
        }
    )
    client = TavilyClient(_settings())
    client.client = sdk  # type: ignore[assignment]

    assert client.search("recent books") == []

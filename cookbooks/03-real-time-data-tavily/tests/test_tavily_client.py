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
        _env_file=None,
        tavily_search_depth="advanced",
        tavily_topic="news",
        tavily_max_results=5,
        tavily_max_age_days=180,
        tavily_min_score=0.7,
        tavily_strict_news_dates=True,
        tavily_exclude_domains=["facebook.com", "reddit.com", "linkedin.com"],
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


def test_search_rejects_stale_low_score_and_undated_results() -> None:
    today = datetime.now(UTC).date()
    sdk = FakeTavilySdk(
        {
            "results": [
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


def test_search_caps_every_query_at_the_sdk_boundary() -> None:
    sdk = FakeTavilySdk({"results": []})
    client = TavilyClient(_settings())
    client.client = sdk  # type: ignore[assignment]
    client.search("  " + "a" * 4000 + " books recommendations  ")
    assert sdk.kwargs["query"] == "a" * 400


def test_search_compares_dates_in_utc_with_an_exclusive_end(monkeypatch) -> None:
    class FrozenDatetime(datetime):
        @classmethod
        def now(cls, tz=None):
            return cls(2026, 9, 30, 22, 30, tzinfo=UTC)

    monkeypatch.setattr("app.core.tavily_client.datetime", FrozenDatetime)
    dates = [
        "2026-10-01T01:00:00+03:00",  # Still September 30 in UTC.
        "Wed, 30 Sep 2026 23:00:00 -0300",  # October 1 in UTC: outside the window.
        "2026-09-30",  # Date-only sources use UTC, regardless of local timezone.
    ]
    sdk = FakeTavilySdk(
        {
            "results": [
                {"url": f"https://example.com/{index}", "score": 0.9, "published_date": value}
                for index, value in enumerate(dates)
            ]
        }
    )
    client = TavilyClient(_settings())
    client.client = sdk  # type: ignore[assignment]
    results = client.search("recent books")
    assert [item.url for item in results] == ["https://example.com/0", "https://example.com/2"]
    assert all(item.published_date == "2026-09-30" for item in results)
    assert sdk.kwargs["end_date"] == "2026-10-01"


def test_quota_exhaustion_is_not_retried() -> None:
    from tavily.errors import UsageLimitExceededError

    calls = []

    class QuotaSdk:
        def search(self, **kwargs: object) -> dict[str, Any]:
            calls.append(kwargs)
            raise UsageLimitExceededError("quota exhausted")

    client = TavilyClient(_settings())
    client.client = QuotaSdk()  # type: ignore[assignment]
    import pytest

    with pytest.raises(UsageLimitExceededError):
        client.search("recent books")
    assert len(calls) == 1

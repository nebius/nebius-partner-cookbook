"""A failed web search must not be presented as successful filtering."""

from types import SimpleNamespace

import pytest
from fastapi.testclient import TestClient
from structlog.testing import capture_logs
from tavily.errors import InvalidAPIKeyError

from app.core.book_rag import BookRag, FreshSearchPlan
from app.core.nebius_pricing import TokenPrices
from app.main import app


@pytest.mark.parametrize("fails", [True, False])
def test_search_outcome_and_request_id(monkeypatch, fails: bool) -> None:
    class FakeTavily:
        def search(self, query: str) -> list:
            if fails:
                raise InvalidAPIKeyError("sensitive provider payload")
            return []

    class FakeRag:
        tavily = FakeTavily()
        search_fresh_context = BookRag.search_fresh_context
        pricing = SimpleNamespace(get_prices=lambda: TokenPrices(0, 0, 0))

        def __init__(self, settings) -> None:
            pass

        def narrate_progress(self, prompt: str) -> list[str]:
            return ["progress"] * 4

        def embed_query(self, prompt: str) -> tuple[list[float], int]:
            return [], 0

        def retrieve_books_from_vector(self, *args) -> list:
            return []

        def plan_fresh_search(self, *args) -> FreshSearchPlan:
            return FreshSearchPlan(query="recent books", rationale="freshness")

        def stream_synthesis(self, *args):
            return iter([])

    monkeypatch.setenv("ENV", "development")
    monkeypatch.setenv("NEBIUS_DEBUG_ERRORS", "true")
    monkeypatch.setattr("app.routes.agent.BookRag", FakeRag)
    with capture_logs() as logs, TestClient(app) as client:
        response = client.post("/agent/run", json={"prompt": "recent books"})
    request_id = response.headers["x-request-id"]
    assert request_id
    if fails:
        assert "event: error" in response.text
        assert "web_authentication_error" in response.text
        assert "web_sources_filtered" not in response.text
        assert "event: done" not in response.text
        assert request_id in response.text
        assert any(
            log.get("request_id") == request_id and log.get("error_type") == "InvalidAPIKeyError"
            for log in logs
        )
        assert "sensitive provider payload" not in response.text
        assert "sensitive provider payload" not in str(logs)
    else:
        assert "web_sources_filtered" in response.text
        assert "event: error" not in response.text
        assert "event: done" in response.text

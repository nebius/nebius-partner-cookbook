"""Agent route tests. Nebius and Pinecone are monkeypatched — no network."""

from __future__ import annotations

from fastapi.testclient import TestClient

from app.core.book_rag import RetrievedBook, SynthesisResult, UsageSummary
from app.core.nebius_pricing import TokenPrices
from app.main import app


def test_agent_run_streams_book_rag_events(monkeypatch) -> None:
    class FakeUsage:
        prompt_tokens = 123
        completion_tokens = 45

    class FakeDelta:
        def __init__(self, content: str | None) -> None:
            self.content = content

    class FakeChoice:
        def __init__(self, content: str | None) -> None:
            self.delta = FakeDelta(content)

    class FakeChunk:
        def __init__(self, content: str | None = None, usage: FakeUsage | None = None) -> None:
            self.choices = [FakeChoice(content)] if content is not None else []
            self.usage = usage

    class FakePricing:
        def get_prices(self) -> TokenPrices:
            return TokenPrices(
                input_per_million=0.13,
                output_per_million=0.4,
                embedding_per_million=0.01,
            )

    def fake_init(self, settings) -> None:
        self.settings = settings
        self.pricing = FakePricing()

    def fake_embed_query(self, prompt: str) -> tuple[list[float], int]:
        assert "Dune" in prompt
        return [0.1, 0.2, 0.3], 12

    def fake_narrate_progress(self, prompt: str) -> list[str]:
        assert "Dune" in prompt
        return [
            "I am mapping your reading taste into the book index.",
            "The vector is ready; Pinecone is returning nearby titles.",
            "I have the candidates and am shaping the recommendation.",
        ]

    def fake_retrieve_books_from_vector(
        self,
        query_vector: list[float],
        top_k: int,
        related_top_k: int,
        include_related: bool,
    ) -> list[RetrievedBook]:
        assert query_vector == [0.1, 0.2, 0.3]
        assert top_k == 10
        assert related_top_k == 4
        assert include_related is True
        return [
            RetrievedBook(
                citation_id=1,
                vector_id="book::1",
                score=0.91,
                retrieval_reason="direct semantic match",
                title="Dune",
                authors="Frank Herbert",
                genres=["science fiction"],
                average_rating="4.2",
                ratings_count="1000",
                publication_year="1965",
            )
        ]

    def fake_synthesize(self, prompt: str, books: list[RetrievedBook]) -> SynthesisResult:
        assert books[0].title == "Dune"
        return SynthesisResult(
            answer="Try Dune [1].",
            usage=UsageSummary(input_tokens=123, output_tokens=45, cost_usd=0.000034),
        )

    def fake_stream_synthesis(self, prompt: str, books: list[RetrievedBook]):
        assert books[0].title == "Dune"
        return iter(
            [
                FakeChunk("Try "),
                FakeChunk("Dune [1]."),
                FakeChunk(usage=FakeUsage()),
            ]
        )

    monkeypatch.setattr("app.routes.agent.BookRag.__init__", fake_init)
    monkeypatch.setattr("app.routes.agent.BookRag.narrate_progress", fake_narrate_progress)
    monkeypatch.setattr("app.routes.agent.BookRag.embed_query", fake_embed_query)
    monkeypatch.setattr(
        "app.routes.agent.BookRag.retrieve_books_from_vector",
        fake_retrieve_books_from_vector,
    )
    monkeypatch.setattr("app.routes.agent.BookRag.synthesize", fake_synthesize)
    monkeypatch.setattr("app.routes.agent.BookRag.stream_synthesis", fake_stream_synthesis)

    with TestClient(app) as client:
        with client.stream(
            "POST",
            "/agent/run",
            json={
                "prompt": "Recommend books after Dune",
                "top_k": 10,
                "related_top_k": 4,
                "include_related": True,
            },
        ) as response:
            assert response.status_code == 200
            body = b"".join(response.iter_bytes()).decode("utf-8")

    assert "event: status" in body
    assert "event: agent_message" in body
    assert "I am mapping your reading taste" in body
    assert "The vector is ready" in body
    assert "I have the candidates" in body
    assert "Requesting Pinecone Knowledge" in body
    assert "Synthesizing" in body
    assert "event: context" in body
    assert "Dune" in body
    assert "event: token" in body
    assert '"Try "' in body
    assert '"Dune [1]."' in body
    assert "Tokens:" in body
    assert "elapsedSeconds" in body
    assert "event: done" in body

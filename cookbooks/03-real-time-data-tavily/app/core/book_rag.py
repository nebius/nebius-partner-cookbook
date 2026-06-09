"""Simple Pinecone-backed book RAG over the Goodreads vectors."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from openai import OpenAI
from pinecone import Pinecone

from app.config import Settings
from app.core.nebius_pricing import NebiusPricing
from app.core.tavily_client import TavilyClient, TavilyResult

MAX_RAG_BOOKS = 10
DEFAULT_PROGRESS_MESSAGES = [
    "I am turning your request into a search vector for the book index.",
    "The query embedding is ready. I am checking Pinecone for matching books.",
    "I have book candidates. I am planning the Tavily freshness search.",
    "The fresh context is ready. I am asking Nebius to write the recommendations.",
]


@dataclass
class RetrievedBook:
    citation_id: int
    vector_id: str
    score: float
    retrieval_reason: str
    title: str
    authors: str
    genres: list[str]
    average_rating: str
    ratings_count: str
    publication_year: str

    def to_public_dict(self) -> dict[str, object]:
        return {
            "citation": self.citation_id,
            "id": self.vector_id,
            "score": self.score,
            "reason": self.retrieval_reason,
            "title": self.title,
            "authors": self.authors,
            "genres": self.genres,
            "averageRating": self.average_rating,
            "ratingsCount": self.ratings_count,
            "publicationYear": self.publication_year,
        }

    def to_context_line(self) -> str:
        details = [
            f"title={self.title}",
            f"authors={self.authors}",
            f"similarity={self.score:.4f}",
            f"retrieval_reason={self.retrieval_reason}",
        ]
        if self.genres:
            details.append(f"genres={', '.join(self.genres[:8])}")
        if self.average_rating:
            details.append(f"average_rating={self.average_rating}")
        if self.ratings_count:
            details.append(f"ratings_count={self.ratings_count}")
        if self.publication_year:
            details.append(f"publication_year={self.publication_year}")
        return f"[{self.citation_id}] " + "; ".join(details)


@dataclass
class UsageSummary:
    embedding_tokens: int = 0
    input_tokens: int = 0
    output_tokens: int = 0
    cost_usd: float = 0.0

    def to_public_dict(self) -> dict[str, object]:
        return {
            "embeddingTokens": self.embedding_tokens,
            "inputTokens": self.input_tokens,
            "outputTokens": self.output_tokens,
            "totalTokens": self.embedding_tokens + self.input_tokens + self.output_tokens,
            "costUsd": round(self.cost_usd, 6),
        }


@dataclass
class RetrievalResult:
    query_vector: list[float]
    books: list[RetrievedBook]
    usage: UsageSummary


@dataclass
class SynthesisResult:
    answer: str
    usage: UsageSummary


@dataclass
class CompletionRequest:
    messages: list[dict[str, str]]
    temperature: float
    max_tokens: int


@dataclass
class FreshSearchPlan:
    query: str
    rationale: str

    def to_public_dict(self) -> dict[str, str]:
        return {
            "query": self.query,
            "rationale": self.rationale,
        }


class BookRag:
    def __init__(self, settings: Settings) -> None:
        base_url = str(settings.nebius_base_url).rstrip("/")
        if not base_url.endswith("/v1"):
            base_url = f"{base_url}/v1"

        self.settings = settings
        self.nebius = OpenAI(api_key=settings.nebius_api_key, base_url=base_url)
        self.pinecone = Pinecone(api_key=settings.pinecone_api_key)
        self.index = self.pinecone.Index(settings.pinecone_index_name)
        self.tavily = TavilyClient(settings)
        self.pricing = NebiusPricing(settings)

    def retrieve(
        self,
        prompt: str,
        top_k: int,
        related_top_k: int,
        include_related: bool,
    ) -> RetrievalResult:
        query_vector, embedding_tokens = self.embed_query(prompt)
        books = self.retrieve_books_from_vector(query_vector, top_k, related_top_k, include_related)
        prices = self.pricing.get_prices()
        embedding_cost = embedding_tokens * prices.embedding_per_million / 1_000_000
        return RetrievalResult(
            query_vector=query_vector,
            books=books,
            usage=UsageSummary(embedding_tokens=embedding_tokens, cost_usd=embedding_cost),
        )

    def embed_query(self, prompt: str) -> tuple[list[float], int]:
        return self._embed_query(prompt)

    def retrieve_books_from_vector(
        self,
        query_vector: list[float],
        top_k: int,
        related_top_k: int,
        include_related: bool,
    ) -> list[RetrievedBook]:
        direct = self._query_books(query_vector, top_k, None, "direct semantic match")
        books = direct
        if include_related:
            books = self._merge_books(
                books,
                self._query_related_books(query_vector, related_top_k, direct),
            )
        return books[:MAX_RAG_BOOKS]

    def build_completion_request(
        self,
        prompt: str,
        books: list[RetrievedBook],
        fresh_sources: list[TavilyResult] | None = None,
    ) -> CompletionRequest:
        return CompletionRequest(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a precise book recommendation assistant. "
                        "Use Goodreads retrieval context as the curated book-memory layer. "
                        "Use Tavily web context as the live-grounding layer for recent books, "
                        "current editions, availability, pricing, and market context. "
                        "When the user's request depends on a date, launch timing, availability, "
                        "or other fresh facts that the Goodreads snapshot does not satisfy, "
                        "Tavily web sources may provide recommendation candidates directly. "
                        "Do not invent books, authors, ratings, sources, or citations."
                    ),
                },
                {
                    "role": "user",
                    "content": self._build_answer_prompt(prompt, books, fresh_sources or []),
                },
            ],
            temperature=self.settings.answer_temperature,
            max_tokens=self.settings.answer_max_tokens,
        )

    def synthesize(
        self,
        prompt: str,
        books: list[RetrievedBook],
        fresh_sources: list[TavilyResult] | None = None,
    ) -> SynthesisResult:
        request = self.build_completion_request(prompt, books, fresh_sources)
        response = self.nebius.chat.completions.create(
            model=self.settings.nebius_model,
            messages=request.messages,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
        )
        input_tokens = int(getattr(response.usage, "prompt_tokens", 0) or 0)
        output_tokens = int(getattr(response.usage, "completion_tokens", 0) or 0)
        prices = self.pricing.get_prices()
        cost = (
            input_tokens * prices.input_per_million / 1_000_000
            + output_tokens * prices.output_per_million / 1_000_000
        )
        return SynthesisResult(
            answer=response.choices[0].message.content or "",
            usage=UsageSummary(
                input_tokens=input_tokens, output_tokens=output_tokens, cost_usd=cost
            ),
        )

    def answer(
        self,
        prompt: str,
        top_k: int,
        related_top_k: int,
        include_related: bool,
    ) -> tuple[str, list[RetrievedBook]]:
        retrieval = self.retrieve(prompt, top_k, related_top_k, include_related)
        synthesis = self.synthesize(prompt, retrieval.books)
        return synthesis.answer, retrieval.books

    def narrate_progress(self, prompt: str) -> list[str]:
        try:
            response = self.nebius.chat.completions.create(
                model=self.settings.nebius_model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Write concise progress messages for a book recommendation RAG agent. "
                            'Return only JSON: {"messages":["...","...","...","..."]}. '
                            "Each message must be under 110 characters, natural, varied, "
                            "and in first person. "
                            "Use the user's book theme or reading context when it helps. "
                            "Do not mention hidden reasoning."
                        ),
                    },
                    {
                        "role": "user",
                        "content": (
                            "Create exactly four progress messages for these phases: "
                            "1) prepare a Nebius embedding, 2) query Pinecone knowledge, "
                            "3) plan and search Tavily for fresh book context, "
                            "4) synthesize book recommendations. "
                            "Make them specific to this request without pretending results "
                            "are known yet.\n"
                            f"User request / theme: {prompt}"
                        ),
                    },
                ],
                temperature=0.9,
                max_tokens=160,
            )
            content = response.choices[0].message.content or ""
            parsed = json.loads(content)
            messages = parsed.get("messages", [])
            if not isinstance(messages, list):
                return DEFAULT_PROGRESS_MESSAGES
            clean = [str(item).strip() for item in messages if str(item).strip()]
            if len(clean) != 4:
                return DEFAULT_PROGRESS_MESSAGES
            return [message[:160] for message in clean]
        except Exception:
            return DEFAULT_PROGRESS_MESSAGES

    def plan_fresh_search(self, prompt: str, books: list[RetrievedBook]) -> FreshSearchPlan:
        fallback_query = self._build_tavily_query(prompt, books)
        candidate_context = "\n".join(book.to_context_line() for book in books[:5])
        try:
            response = self.nebius.chat.completions.create(
                model=self.settings.nebius_model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Create a concise Tavily web search plan for a book recommendation "
                            "agent. Return only JSON with keys query and rationale. "
                            "The query must target freshness signals such as recent editions, "
                            "availability, pricing, newly released adjacent books, or current "
                            "market context. The rationale must be one short sentence and must "
                            "not reveal hidden chain-of-thought."
                        ),
                    },
                    {
                        "role": "user",
                        "content": (
                            f"User request:\n{prompt}\n\n"
                            f"Retrieved book candidates:\n{candidate_context}"
                        ),
                    },
                ],
                temperature=0.2,
                max_tokens=180,
            )
            content = response.choices[0].message.content or ""
            parsed = json.loads(content)
            query = str(parsed.get("query") or "").strip()
            rationale = str(parsed.get("rationale") or "").strip()
            if not query:
                return FreshSearchPlan(
                    query=fallback_query,
                    rationale="Use the retrieved candidates to look for current web context.",
                )
            return FreshSearchPlan(
                query=query[:500],
                rationale=(
                    rationale[:240]
                    or "Use current web context to qualify freshness-sensitive claims."
                ),
            )
        except Exception:
            return FreshSearchPlan(
                query=fallback_query,
                rationale="Use the retrieved candidates to look for current web context.",
            )

    def search_fresh_context(self, plan: FreshSearchPlan) -> list[TavilyResult]:
        try:
            return self.tavily.search(plan.query)
        except Exception:
            return []

    def stream_synthesis(
        self,
        prompt: str,
        books: list[RetrievedBook],
        fresh_sources: list[TavilyResult] | None = None,
    ):
        request = self.build_completion_request(prompt, books, fresh_sources)
        return self.nebius.chat.completions.create(
            model=self.settings.nebius_model,
            messages=request.messages,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
            stream=True,
            stream_options={"include_usage": True},
        )

    def _embed_query(self, prompt: str) -> tuple[list[float], int]:
        query_text = (
            "Instruct: Given a user's book preference or a book they liked, "
            "retrieve relevant Goodreads books.\n"
            f"Query: {prompt}"
        )
        response = self.nebius.embeddings.create(
            model=self.settings.nebius_embedding_model,
            input=[query_text],
            encoding_format="float",
        )
        embedding_tokens = int(getattr(response.usage, "prompt_tokens", 0) or 0)
        return response.data[0].embedding, embedding_tokens

    def _query_books(
        self,
        vector: list[float],
        top_k: int,
        extra_filter: dict[str, Any] | None,
        reason: str,
    ) -> list[RetrievedBook]:
        results = self.index.query(
            vector=vector,
            top_k=top_k,
            include_metadata=True,
            namespace=self.settings.pinecone_namespace,
            filter=self._combine_book_filter(extra_filter),
        )
        return self._matches_to_books(results.matches, reason)

    def _query_related_books(
        self,
        vector: list[float],
        top_k: int,
        seed_books: list[RetrievedBook],
    ) -> list[RetrievedBook]:
        authors, genres, years = self._filter_values(seed_books)
        related: list[RetrievedBook] = []

        for author in authors:
            related = self._merge_books(
                related,
                self._query_books(
                    vector, top_k, {"author_names": {"$in": [author]}}, "same author"
                ),
            )
        for genre in genres:
            related = self._merge_books(
                related,
                self._query_books(vector, top_k, {"genres": {"$in": [genre]}}, "same theme"),
            )
        for year in years:
            related = self._merge_books(
                related,
                self._query_books(
                    vector, top_k, {"publication_year": {"$eq": int(year)}}, "same year"
                ),
            )

        return related

    def _matches_to_books(self, matches: list[Any], reason: str) -> list[RetrievedBook]:
        books: list[RetrievedBook] = []
        for idx, match in enumerate(matches, start=1):
            metadata = dict(match.metadata or {})
            books.append(
                RetrievedBook(
                    citation_id=idx,
                    vector_id=str(match.id or ""),
                    score=max(0.0, float(match.score or 0.0)),
                    retrieval_reason=reason,
                    title=self._metadata_text(metadata, "title") or str(match.id or "(untitled)"),
                    authors=self._format_authors(metadata),
                    genres=self._metadata_list(metadata, "genres"),
                    average_rating=self._metadata_text(metadata, "average_rating"),
                    ratings_count=self._metadata_text(metadata, "ratings_count"),
                    publication_year=self._metadata_text(metadata, "publication_year"),
                )
            )
        return books

    def _build_answer_prompt(
        self,
        prompt: str,
        books: list[RetrievedBook],
        fresh_sources: list[TavilyResult],
    ) -> str:
        context = "\n".join(book.to_context_line() for book in books)
        web_context = "\n".join(source.to_context_line() for source in fresh_sources)
        return f"""User request:
{prompt}

Retrieved Goodreads book candidates:
{context}

Fresh Tavily web context:
{web_context or "(no fresh web sources returned)"}

Write a helpful book recommendation answer.
Use the Goodreads candidates when they satisfy the request.
Use Tavily web sources as recommendation evidence when the request asks for recent,
post-date, current, newly launched, available, or edition-specific books that are
missing from the Goodreads candidates.
Recommend at most 5 books across both source sets.
Recommend the strongest matches first, even when the strongest match comes from Tavily.
For each recommendation, explain briefly why it fits the request.
Do not say that no books match until you have checked both Goodreads and Tavily context.
If a Tavily result names a relevant book, edition, launch, list, article, or publisher page,
surface that result in the answer instead of treating it as background only.
When useful, mention whether a book was retrieved because it shares an author,
theme, or publication year with another strong candidate.
Include Goodreads citation markers like [1], [2], or [3] next to recommended titles.
Include web citation markers like [W1] or [W2] for Tavily-backed recommendations and
fresh web claims.
Clearly label Tavily-only recommendations as web-sourced when they do not appear in
the Goodreads candidates.
If the retrieved books are weak matches, say that clearly and suggest how to refine the query."""

    def _build_tavily_query(self, prompt: str, books: list[RetrievedBook]) -> str:
        titles = ", ".join(book.title for book in books[:5] if book.title)
        return (
            f"{prompt} books recommendations current availability recent editions pricing"
            f" newer books related to {titles}"
        ).strip()

    def _combine_book_filter(self, extra_filter: dict[str, Any] | None) -> dict[str, Any]:
        book_filter = {"record_type": {"$eq": "book"}}
        if extra_filter is None:
            return book_filter
        return {"$and": [book_filter, extra_filter]}

    def _merge_books(
        self,
        existing: list[RetrievedBook],
        additions: list[RetrievedBook],
    ) -> list[RetrievedBook]:
        seen = {book.vector_id for book in existing}
        merged = [*existing]
        for book in additions:
            if book.vector_id in seen:
                continue
            seen.add(book.vector_id)
            book.citation_id = len(merged) + 1
            merged.append(book)
        return merged

    def _filter_values(self, books: list[RetrievedBook]) -> tuple[list[str], list[str], list[str]]:
        authors: list[str] = []
        genres: list[str] = []
        years: list[str] = []

        for book in books[:5]:
            if book.authors and book.authors != "(unknown author)":
                for author in book.authors.split(","):
                    author = author.strip()
                    if author and author not in authors:
                        authors.append(author)
            for genre in book.genres[:5]:
                if genre not in genres:
                    genres.append(genre)
            if book.publication_year and book.publication_year not in years:
                years.append(book.publication_year)

        return authors[:5], genres[:8], years[:5]

    def _metadata_text(self, metadata: dict[str, Any], key: str) -> str:
        value = metadata.get(key)
        if value is None:
            return ""
        return str(value).strip()

    def _metadata_list(self, metadata: dict[str, Any], key: str) -> list[str]:
        value = metadata.get(key)
        if not isinstance(value, list):
            return []
        return [str(item).strip() for item in value if str(item).strip()]

    def _format_authors(self, metadata: dict[str, Any]) -> str:
        author_names = metadata.get("author_names")
        if isinstance(author_names, list):
            names = [str(item).strip() for item in author_names if str(item).strip()]
            if names:
                return ", ".join(names)
        return "(unknown author)"

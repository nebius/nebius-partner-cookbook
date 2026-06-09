#!/usr/bin/env python
"""Answer book questions with a simple Pinecone RAG loop.

The script embeds the user's request with Nebius, retrieves matching Goodreads
book vectors from Pinecone, then asks a Nebius chat model to recommend books
from the retrieved context.
"""

from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from openai import OpenAI
from pinecone import Pinecone

DEFAULT_EMBEDDING_MODEL = "Qwen/Qwen3-Embedding-8B"
DEFAULT_ANSWER_MODEL = "meta-llama/Llama-3.3-70B-Instruct"
DEFAULT_RETRIEVAL_INSTRUCTION = (
    "Given a user's book preference or a book they liked, retrieve relevant Goodreads books."
)
ANSI_RESET = "\033[0m"
ANSI_BOLD = "\033[1m"
ANSI_GREEN = "\033[32m"
ANSI_CYAN = "\033[36m"
ANSI_YELLOW = "\033[33m"


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


def load_dotenv_if_present() -> None:
    script_dir = Path(__file__).resolve().parent
    cookbook_dir = script_dir.parent

    for env_name in (".env.local", ".env"):
        env_path = cookbook_dir / env_name
        if not env_path.exists():
            continue

        with env_path.open("rt", encoding="utf-8") as handle:
            for raw_line in handle:
                line = raw_line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue

                key, value = line.split("=", 1)
                key = key.strip()
                value = value.strip()
                if not key:
                    continue
                if value and len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
                    value = value[1:-1]

                os.environ.setdefault(key, value)


def supports_color() -> bool:
    return (
        os.getenv("NO_COLOR") is None
        and hasattr(os.sys.stdout, "isatty")
        and os.sys.stdout.isatty()
    )


def colorize(text: str, *styles: str) -> str:
    if not supports_color():
        return text
    return f"{''.join(styles)}{text}{ANSI_RESET}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Recommend books with Nebius + Pinecone knowledge over Goodreads vectors."
    )
    parser.add_argument(
        "query",
        help=(
            "Natural-language book request, for example a topic to explore or "
            "a book you liked and want recommendations after."
        ),
    )
    parser.add_argument(
        "--instruction",
        default=DEFAULT_RETRIEVAL_INSTRUCTION,
        help="Retrieval instruction prepended to the query before embedding.",
    )
    parser.add_argument("--top-k", type=int, default=10, help="Number of matches to retrieve.")
    parser.add_argument(
        "--pinecone-index",
        default=None,
        help="Pinecone index name. Defaults to PINECONE_INDEX_NAME from the environment.",
    )
    parser.add_argument(
        "--pinecone-namespace",
        default=None,
        help="Pinecone namespace. Defaults to PINECONE_NAMESPACE from the environment if set.",
    )
    parser.add_argument(
        "--embedding-model",
        default=None,
        help="Nebius embedding model. Defaults to NEBIUS_EMBEDDING_MODEL or Qwen/Qwen3-Embedding-8B.",
    )
    parser.add_argument(
        "--answer-model",
        default=None,
        help="Nebius chat model. Defaults to NEBIUS_MODEL or meta-llama/Llama-3.3-70B-Instruct.",
    )
    parser.add_argument("--max-tokens", type=int, default=700)
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument(
        "--include-non-books",
        action="store_true",
        help="Disable the default Pinecone filter that keeps only book vectors.",
    )
    parser.add_argument(
        "--no-related",
        action="store_true",
        help="Disable follow-up retrieval for same author, same theme, and same year.",
    )
    parser.add_argument(
        "--related-top-k",
        type=int,
        default=4,
        help="Number of extra matches to fetch for each related retrieval pass.",
    )
    parser.add_argument(
        "--show-matches",
        action="store_true",
        help="Print Pinecone knowledge matches before the generated answer.",
    )
    parser.add_argument(
        "--no-answer",
        action="store_true",
        help="Only print retrieved matches, without calling the answer model.",
    )
    return parser.parse_args()


def require_env(name: str) -> str:
    value = os.environ.get(name)
    if value:
        return value
    raise SystemExit(f"Missing required environment variable: {name}")


def format_authors(metadata: dict[str, Any]) -> str:
    author_names = metadata.get("author_names")
    if isinstance(author_names, list):
        names = [str(item).strip() for item in author_names if str(item).strip()]
        if names:
            return ", ".join(names)

    author = metadata.get("author")
    if isinstance(author, str) and author.strip():
        return author.strip()

    return "(unknown author)"


def metadata_text(metadata: dict[str, Any], key: str) -> str:
    value = metadata.get(key)
    if value is None:
        return ""
    return str(value).strip()


def metadata_string_list(metadata: dict[str, Any], key: str) -> list[str]:
    value = metadata.get(key)
    if not isinstance(value, list):
        return []
    return [str(item).strip() for item in value if str(item).strip()]


def build_retrieved_books(matches: list[Any], reason: str) -> list[RetrievedBook]:
    books: list[RetrievedBook] = []
    for idx, match in enumerate(matches, start=1):
        metadata = dict(match.metadata or {})
        title = metadata_text(metadata, "title") or str(match.id or "(untitled)")
        books.append(
            RetrievedBook(
                citation_id=idx,
                vector_id=str(match.id or ""),
                score=max(0.0, float(match.score or 0.0)),
                retrieval_reason=reason,
                title=title,
                authors=format_authors(metadata),
                genres=metadata_string_list(metadata, "genres"),
                average_rating=metadata_text(metadata, "average_rating"),
                ratings_count=metadata_text(metadata, "ratings_count"),
                publication_year=metadata_text(metadata, "publication_year"),
            )
        )
    return books


def merge_books(
    existing: list[RetrievedBook], additions: list[RetrievedBook]
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


def first_filter_values(books: list[RetrievedBook]) -> tuple[list[str], list[str], list[str]]:
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


def book_filter() -> dict[str, Any]:
    return {"record_type": {"$eq": "book"}}


def combine_book_filter(
    extra_filter: dict[str, Any] | None, include_non_books: bool
) -> dict[str, Any] | None:
    if include_non_books:
        return extra_filter
    if extra_filter is None:
        return book_filter()
    return {"$and": [book_filter(), extra_filter]}


def query_related_books(
    index: Any,
    vector: list[float],
    namespace: str | None,
    include_non_books: bool,
    top_k: int,
    seed_books: list[RetrievedBook],
) -> list[RetrievedBook]:
    authors, genres, years = first_filter_values(seed_books)
    related: list[RetrievedBook] = []

    related_queries = []
    for author in authors:
        related_queries.append(("same author", {"author_names": {"$in": [author]}}))
    for genre in genres:
        related_queries.append(("same theme", {"genres": {"$in": [genre]}}))
    for year in years:
        related_queries.append(("same year", {"publication_year": {"$eq": int(year)}}))

    for reason, extra_filter in related_queries:
        results = index.query(
            vector=vector,
            top_k=top_k,
            include_metadata=True,
            namespace=namespace,
            filter=combine_book_filter(extra_filter, include_non_books),
        )
        related = merge_books(related, build_retrieved_books(results.matches, reason))

    return related


def print_matches(books: list[RetrievedBook]) -> None:
    for book in books:
        score_pct = f"{book.score * 100:.1f}%"
        print(
            f"{colorize(score_pct, ANSI_YELLOW)}  "
            f"[{book.citation_id}] "
            f"{colorize(book.title, ANSI_BOLD, ANSI_GREEN)}  "
            f"by {colorize(book.authors, ANSI_CYAN)}  "
            f"({book.retrieval_reason})"
        )


def build_answer_prompt(query: str, books: list[RetrievedBook]) -> str:
    context = "\n".join(book.to_context_line() for book in books)
    return f"""User request:
{query}

Retrieved Goodreads book candidates:
{context}

Write a helpful book recommendation answer.
Use only the retrieved candidates.
Recommend at most 5 books.
Recommend the strongest matches first.
For each recommendation, explain briefly why it fits the request.
When useful, mention whether a book was retrieved because it shares an author, theme, or publication year with another strong candidate.
Include citation markers like [1], [2], or [3] next to each recommended title.
If the retrieved books are weak matches, say that clearly and suggest how to refine the query."""


def main() -> None:
    load_dotenv_if_present()
    args = parse_args()

    if args.top_k < 1:
        raise SystemExit("--top-k must be greater than 0.")
    if args.related_top_k < 1:
        raise SystemExit("--related-top-k must be greater than 0.")
    if args.max_tokens < 1:
        raise SystemExit("--max-tokens must be greater than 0.")

    nebius_api_key = require_env("NEBIUS_API_KEY")
    pinecone_api_key = require_env("PINECONE_API_KEY")
    pinecone_index_name = args.pinecone_index or require_env("PINECONE_INDEX_NAME")
    pinecone_namespace = args.pinecone_namespace
    if pinecone_namespace is None:
        pinecone_namespace = os.environ.get("PINECONE_NAMESPACE")

    nebius_base_url = os.environ.get("NEBIUS_BASE_URL", "https://api.studio.nebius.ai").rstrip("/")
    if not nebius_base_url.endswith("/v1"):
        nebius_base_url = f"{nebius_base_url}/v1"

    embedding_model = (
        args.embedding_model or os.environ.get("NEBIUS_EMBEDDING_MODEL") or DEFAULT_EMBEDDING_MODEL
    )
    answer_model = args.answer_model or os.environ.get("NEBIUS_MODEL") or DEFAULT_ANSWER_MODEL
    query_text = f"Instruct: {args.instruction}\nQuery: {args.query}"

    nebius = OpenAI(api_key=nebius_api_key, base_url=nebius_base_url)
    embedding_response = nebius.embeddings.create(
        model=embedding_model,
        input=[query_text],
        encoding_format="float",
    )
    query_vector = embedding_response.data[0].embedding

    pinecone = Pinecone(api_key=pinecone_api_key)
    index = pinecone.Index(pinecone_index_name)
    results = index.query(
        vector=query_vector,
        top_k=args.top_k,
        include_metadata=True,
        namespace=pinecone_namespace,
        filter=combine_book_filter(None, args.include_non_books),
    )

    print(f"query={args.query}")
    print(f"index={pinecone_index_name}")
    print(f"namespace={pinecone_namespace or '(default)'}")
    print(f"embedding_model={embedding_model}")
    print(f"answer_model={answer_model if not args.no_answer else '(disabled)'}")
    print("")

    if not results.matches:
        print("No matches.")
        return

    books = build_retrieved_books(results.matches, "direct semantic match")
    if not args.no_related:
        related_books = query_related_books(
            index=index,
            vector=query_vector,
            namespace=pinecone_namespace,
            include_non_books=args.include_non_books,
            top_k=args.related_top_k,
            seed_books=books,
        )
        books = merge_books(books, related_books)

    if args.show_matches or args.no_answer:
        print_matches(books)
        print("")

    if args.no_answer:
        return

    completion = nebius.chat.completions.create(
        model=answer_model,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a precise book recommendation assistant. "
                    "Ground every recommendation in the supplied Goodreads retrieval context. "
                    "Do not invent books, authors, ratings, or citations."
                ),
            },
            {"role": "user", "content": build_answer_prompt(args.query, books)},
        ],
        temperature=args.temperature,
        max_tokens=args.max_tokens,
    )
    answer = completion.choices[0].message.content
    print(answer or "The answer model returned an empty response.")

    print("")
    print(colorize("Sources", ANSI_BOLD, ANSI_CYAN))
    print_matches(books)


if __name__ == "__main__":
    main()

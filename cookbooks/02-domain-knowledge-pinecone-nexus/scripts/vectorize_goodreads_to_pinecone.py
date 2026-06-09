#!/usr/bin/env python
"""Vectorize Goodreads dumps into Pinecone with Nebius embeddings.

Workflow:
1) Analyze each supported dataset and print basic stats.
2) Build enrichment maps from authors and genres.
3) Generate vector documents from books and selected supporting JSON files.
4) Batch upsert into Pinecone.
"""

from __future__ import annotations

import argparse
import gzip
import json
import os
import time
from collections import Counter
from concurrent.futures import ALL_COMPLETED, FIRST_COMPLETED, Future, ThreadPoolExecutor, wait
from dataclasses import dataclass, field
from pathlib import Path
from threading import Lock
from typing import Any, Dict, Iterable, List, Optional, Tuple

try:
    from openai import OpenAI

    OPENAI_AVAILABLE = True
except ImportError:
    OpenAI = None  # type: ignore[assignment]
    OPENAI_AVAILABLE = False

try:
    from pinecone import Pinecone

    PINECONE_AVAILABLE = True
except ImportError:
    Pinecone = None  # type: ignore[assignment]
    PINECONE_AVAILABLE = False


MAX_PREVIEW_KEYS = 12

ANSI_RESET = "\033[0m"
ANSI_BOLD = "\033[1m"
ANSI_DIM = "\033[2m"
ANSI_BLUE = "\033[34m"
ANSI_CYAN = "\033[36m"
ANSI_GREEN = "\033[32m"
ANSI_YELLOW = "\033[33m"
ANSI_RED = "\033[31m"


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


@dataclass
class DatasetStats:
    name: str
    path: Path
    total_lines: int = 0
    valid_records: int = 0
    invalid_lines: int = 0
    missing_id: int = 0
    seen_ids: int = 0
    duplicate_ids: int = 0
    empty_text: int = 0
    field_counts: Counter = field(default_factory=Counter)

    def as_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "path": str(self.path),
            "total_lines": self.total_lines,
            "valid_records": self.valid_records,
            "invalid_lines": self.invalid_lines,
            "missing_id": self.missing_id,
            "seen_ids": self.seen_ids,
            "duplicate_ids": self.duplicate_ids,
            "empty_text": self.empty_text,
            "top_fields": [k for k, _ in self.field_counts.most_common(MAX_PREVIEW_KEYS)],
        }

    def to_cli_lines(self) -> List[str]:
        top_fields = [k for k, _ in self.field_counts.most_common(MAX_PREVIEW_KEYS)]
        return [
            f"{colorize('[analyze]', ANSI_BLUE, ANSI_BOLD)} {colorize(self.name, ANSI_CYAN, ANSI_BOLD)}",
            f"  {colorize('path', ANSI_DIM)}: {self.path}",
            f"  {colorize('total lines', ANSI_DIM)}: {self.total_lines}",
            f"  {colorize('valid records', ANSI_DIM)}: {colorize(str(self.valid_records), ANSI_GREEN) if self.valid_records else self.valid_records}",
            f"  {colorize('invalid lines', ANSI_DIM)}: {colorize(str(self.invalid_lines), ANSI_YELLOW) if self.invalid_lines else self.invalid_lines}",
            f"  {colorize('missing id', ANSI_DIM)}: {colorize(str(self.missing_id), ANSI_YELLOW) if self.missing_id else self.missing_id}",
            f"  {colorize('seen ids', ANSI_DIM)}: {self.seen_ids}",
            f"  {colorize('duplicate ids', ANSI_DIM)}: {colorize(str(self.duplicate_ids), ANSI_YELLOW) if self.duplicate_ids else self.duplicate_ids}",
            f"  {colorize('empty text', ANSI_DIM)}: {colorize(str(self.empty_text), ANSI_YELLOW) if self.empty_text else self.empty_text}",
            f"  {colorize('top fields', ANSI_DIM)}: {', '.join(top_fields) if top_fields else '(none)'}",
        ]


Record = Dict[str, Any]


@dataclass
class VectorBatch:
    source: str
    ids: List[str]
    texts: List[str]
    metadata_rows: List[Dict[str, Any]]


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


def coerce_str(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _open_record_file(path: Path):
    if ".gz" in path.name:
        try:
            return gzip.open(path, "rt", encoding="utf-8")
        except (OSError, gzip.BadGzipFile):
            return open(path, "rt", encoding="utf-8")
    return open(path, "rt", encoding="utf-8")


def iterate_records(path: Path) -> Iterable[Record]:
    with _open_record_file(path) as handle:
        for idx, line in enumerate(handle, start=1):
            raw = line.strip()
            if not raw:
                continue
            try:
                yield idx, json.loads(raw)
            except json.JSONDecodeError:
                continue


def pick_dataset_file(data_dir: Path, base_name: str) -> Optional[Path]:
    candidates = [
        data_dir / f"{base_name}.json.gz.1",
        data_dir / f"{base_name}.json.gz.2",
        data_dir / f"{base_name}.json.gz",
        data_dir / f"{base_name}.json",
    ]
    for path in candidates:
        if path.exists():
            return path
    # Fallback to any file that starts with base_name and has accepted extensions.
    for path in data_dir.glob(f"{base_name}*"):
        if path.suffix in {".json", ".gz"} or ".json.gz." in path.name:
            return path
    return None


def analyze_dataset(path: Path, id_fields: Tuple[str, ...]) -> DatasetStats:
    name = path.name
    stats = DatasetStats(name=name, path=path)
    seen = set()

    for _line_no, record in iterate_records(path):
        stats.total_lines += 1
        if not isinstance(record, dict):
            stats.invalid_lines += 1
            continue
        stats.valid_records += 1
        stats.field_counts.update([coerce_str(k) for k in record.keys()])

        record_id = None
        for candidate in id_fields:
            if record.get(candidate):
                record_id = coerce_str(record.get(candidate))
                break
        if not record_id:
            stats.missing_id += 1
            continue

        if record_id in seen:
            stats.duplicate_ids += 1
        else:
            seen.add(record_id)
        stats.seen_ids += 1

    return stats


def build_author_index(path: Path) -> Dict[str, Record]:
    authors: Dict[str, Record] = {}
    for _line_no, record in iterate_records(path):
        if not isinstance(record, dict):
            continue
        author_id = coerce_str(record.get("author_id"))
        if not author_id:
            continue
        if author_id not in authors:
            authors[author_id] = record
    return authors


def build_genres_index(path: Path) -> Dict[str, List[str]]:
    genres: Dict[str, List[str]] = {}
    for _line_no, record in iterate_records(path):
        if not isinstance(record, dict):
            continue
        book_id = coerce_str(record.get("book_id"))
        if not book_id:
            continue
        raw = record.get("genres", {})
        if not isinstance(raw, dict):
            continue
        genres[book_id] = [
            g
            for g, count in sorted(raw.items(), key=lambda item: (-int(item[1]), item[0]))
            if str(count).isdigit() or isinstance(count, int)
        ]
    return genres


def resolve_book_authors(
    record: Record,
    authors: Dict[str, Record],
) -> List[Dict[str, str]]:
    linked: List[Dict[str, str]] = []
    raw_authors = record.get("authors")
    if not isinstance(raw_authors, list):
        return linked

    seen: set[str] = set()
    for item in raw_authors:
        if not isinstance(item, dict):
            continue
        author_id = coerce_str(item.get("author_id"))
        if not author_id:
            continue
        if author_id in seen:
            continue
        seen.add(author_id)
        author_record = authors.get(author_id, {})
        linked.append(
            {
                "id": author_id,
                "name": coerce_str(author_record.get("name") or item.get("name"))
                or coerce_str(item.get("name")),
            }
        )
    return linked


def build_works_index(path: Path) -> Dict[str, Record]:
    works: Dict[str, Record] = {}
    for _line_no, record in iterate_records(path):
        if not isinstance(record, dict):
            continue
        work_id = coerce_str(record.get("best_book_id") or record.get("work_id"))
        if not work_id:
            continue
        if work_id not in works:
            works[work_id] = record
    return works


def build_book_text(
    record: Record,
    genres: Dict[str, List[str]],
    linked_authors: List[Dict[str, str]],
) -> str:
    parts = [
        coerce_str(record.get("title")),
        coerce_str(record.get("title_without_series")),
        coerce_str(record.get("description")),
    ]

    pub_bits = []
    for key in ("publication_year", "publication_month", "publication_day"):
        value = coerce_str(record.get(key))
        if value:
            pub_bits.append(value)
    if pub_bits:
        parts.append(f"Published: {', '.join(pub_bits)}")

    book_id = coerce_str(record.get("book_id"))
    if book_id and genres.get(book_id):
        parts.append(f"Genres: {', '.join(genres[book_id])}")

    author_names = [author["name"] for author in linked_authors if author.get("name")]
    if author_names:
        parts.append("Authors: " + ", ".join(author_names))

    return "\n".join([p for p in parts if p])


def build_record_text(source: str, record: Record, extra: str = "") -> str:
    pieces = []
    if source == "authors":
        pieces.extend(
            [
                coerce_str(record.get("name")),
                f"Average rating: {coerce_str(record.get('average_rating'))}",
                f"Ratings count: {coerce_str(record.get('ratings_count'))}",
                f"Text reviews count: {coerce_str(record.get('text_reviews_count'))}",
                extra,
            ]
        )
    elif source == "genres":
        pieces.extend(
            [
                f"Book ID: {coerce_str(record.get('book_id'))}",
                extra,
            ]
        )
    elif source == "works":
        pieces.extend(
            [
                coerce_str(record.get("original_title")),
                coerce_str(record.get("best_book_id")),
                coerce_str(record.get("rating_dist")),
                coerce_str(record.get("description")),
                extra,
            ]
        )
    return "\n".join([p for p in pieces if p])


def safe_int(value: Any) -> Optional[int]:
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def sanitize_metadata_value(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, list):
        sanitized_items = [item for item in value if isinstance(item, str) and item]
        return sanitized_items
    return coerce_str(value)


def sanitize_metadata(metadata: Dict[str, Any]) -> Dict[str, Any]:
    sanitized: Dict[str, Any] = {}
    for key, value in metadata.items():
        normalized = sanitize_metadata_value(value)
        if normalized is None:
            continue
        sanitized[key] = normalized
    return sanitized


class GoodreadsVectorizer:
    def __init__(
        self,
        pinecone_index_name: str,
        pinecone_namespace: Optional[str],
        nebius_api_key: str,
        nebius_base_url: str,
        nebius_model: str,
        batch_size: int = 200,
        embed_batch: int = 64,
        embed_concurrency: int = 4,
        max_pending_embed_batches: Optional[int] = None,
        progress_interval: int = 500,
    ) -> None:
        self.batch_size = batch_size
        self.embed_batch = embed_batch
        self.embed_concurrency = max(1, embed_concurrency)
        self.max_pending_embed_batches = max_pending_embed_batches or (self.embed_concurrency * 2)
        self.namespace = pinecone_namespace
        self.progress_interval = max(1, progress_interval)

        if not OPENAI_AVAILABLE or not PINECONE_AVAILABLE:
            missing = []
            if not OPENAI_AVAILABLE:
                missing.append("openai")
            if not PINECONE_AVAILABLE:
                missing.append("pinecone")
            raise ImportError(
                "Missing optional dependencies for vectorization: "
                + ", ".join(sorted(set(missing)))
                + ". Install them with: pip install openai pinecone"
            )

        base_url = nebius_base_url.rstrip("/")
        if not base_url.endswith("/v1"):
            base_url = f"{base_url}/v1"
        self.embedding_client = OpenAI(api_key=nebius_api_key, base_url=base_url)
        self.embedding_model = nebius_model

        self.pinecone = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
        self.index = self.pinecone.Index(pinecone_index_name)
        self.total_vectors = 0
        self.start_time = time.time()
        self.embedding_calls = 0
        self.last_progress = 0
        self._stats_lock = Lock()

    def _embed_texts(self, texts: List[str]) -> List[List[float]]:
        with self._stats_lock:
            self.embedding_calls += 1
        response = self.embedding_client.embeddings.create(
            model=self.embedding_model,
            input=texts,
            encoding_format="float",
        )
        return [item.embedding for item in response.data]

    def _upsert(self, vectors: List[Dict[str, Any]], source: str) -> None:
        if not vectors:
            return
        self.index.upsert(vectors=vectors, namespace=self.namespace)
        with self._stats_lock:
            self.total_vectors += len(vectors)
            should_log = self.total_vectors - self.last_progress >= self.progress_interval
            if should_log:
                self.last_progress = self.total_vectors
                elapsed = time.time() - self.start_time
                rate = self.total_vectors / elapsed if elapsed > 0 else 0.0
                embedding_calls = self.embedding_calls
        # Emit progress in steady intervals to avoid log spam while still showing
        # live ingestion throughput on long runs.
        if should_log:
            print(
                f"[progress] upserted={self.total_vectors} source={source} "
                f"batch={len(vectors)} embeddings_calls={embedding_calls} "
                f"rate={rate:.2f} vectors/s",
                flush=True,
            )

    def _records_to_payload(
        self,
        source_records: Iterable[Tuple[str, List[float], Dict[str, Any]]],
    ) -> List[List[Dict[str, Any]]]:
        payload: List[Dict[str, Any]] = []
        batches: List[List[Dict[str, Any]]] = []
        for doc_id, embedding, metadata in source_records:
            payload.append(
                {
                    "id": doc_id,
                    "values": embedding,
                    "metadata": sanitize_metadata(metadata),
                }
            )
            if len(payload) >= self.batch_size:
                batches.append(payload)
                payload = []
        if payload:
            batches.append(payload)
        return batches

    def _embed_batch(self, batch: VectorBatch) -> Tuple[str, List[List[Dict[str, Any]]]]:
        embeddings = self._embed_texts(batch.texts)
        rows = [
            (doc_id, embedding, metadata)
            for doc_id, embedding, metadata in zip(batch.ids, embeddings, batch.metadata_rows)
        ]
        return batch.source, self._records_to_payload(rows)

    def _drain_completed_embeddings(
        self,
        pending_embeddings: Dict[Future[Tuple[str, List[List[Dict[str, Any]]]]], str],
        upsert_executor: ThreadPoolExecutor,
        pending_upserts: List[Future[None]],
        wait_for_all: bool = False,
    ) -> None:
        if not pending_embeddings:
            return

        done, _ = wait(
            pending_embeddings.keys(),
            return_when=ALL_COMPLETED if wait_for_all else FIRST_COMPLETED,
        )
        for future in done:
            source = pending_embeddings.pop(future)
            batch_source, payload_batches = future.result()
            for payload in payload_batches:
                pending_upserts.append(
                    upsert_executor.submit(self._upsert, payload, batch_source or source)
                )

    def _await_upserts(self, pending_upserts: List[Future[None]]) -> None:
        while pending_upserts:
            future = pending_upserts.pop(0)
            future.result()

    def _process_vector_batches(self, batches: Iterable[VectorBatch]) -> None:
        pending_embeddings: Dict[Future[Tuple[str, List[List[Dict[str, Any]]]]], str] = {}
        pending_upserts: List[Future[None]] = []

        with ThreadPoolExecutor(max_workers=self.embed_concurrency) as embed_executor:
            with ThreadPoolExecutor(max_workers=1) as upsert_executor:
                for batch in batches:
                    future = embed_executor.submit(self._embed_batch, batch)
                    pending_embeddings[future] = batch.source

                    while len(pending_embeddings) >= self.max_pending_embed_batches:
                        self._drain_completed_embeddings(
                            pending_embeddings,
                            upsert_executor,
                            pending_upserts,
                        )

                self._drain_completed_embeddings(
                    pending_embeddings,
                    upsert_executor,
                    pending_upserts,
                    wait_for_all=True,
                )
                self._await_upserts(pending_upserts)

    def upsert_books(
        self,
        books_path: Path,
        authors: Dict[str, Record],
        genres: Dict[str, List[str]],
        include_empty: bool,
        book_offset: int = 0,
    ) -> None:
        self._process_vector_batches(
            self._iter_book_batches(
                books_path,
                authors=authors,
                genres=genres,
                include_empty=include_empty,
                book_offset=book_offset,
            )
        )

    def _iter_book_batches(
        self,
        books_path: Path,
        authors: Dict[str, Record],
        genres: Dict[str, List[str]],
        include_empty: bool,
        book_offset: int = 0,
    ) -> Iterable[VectorBatch]:
        texts: List[str] = []
        metadata_rows: List[Dict[str, Any]] = []
        ids: List[str] = []
        seen_books = 0

        for _line_no, record in iterate_records(books_path):
            if not isinstance(record, dict):
                continue
            book_id = coerce_str(record.get("book_id"))
            if not book_id:
                continue
            if seen_books < book_offset:
                seen_books += 1
                continue
            seen_books += 1

            linked_authors = resolve_book_authors(record, authors)
            text = build_book_text(record, genres, linked_authors)
            if not text and not include_empty:
                continue
            book_genres = genres.get(book_id, [])

            meta = {
                "source": "goodreads_books",
                "record_type": "book",
                "book_id": book_id,
                "author_ids": [author["id"] for author in linked_authors if author.get("id")],
                "author_names": [author["name"] for author in linked_authors if author.get("name")],
                "author_count": len(linked_authors),
                "genres": book_genres[:15],
                "title": coerce_str(record.get("title")),
                "work_id": coerce_str(record.get("work_id")),
                "average_rating": coerce_str(record.get("average_rating")),
                "ratings_count": safe_int(record.get("ratings_count")),
                "text_reviews_count": safe_int(record.get("text_reviews_count")),
                "num_pages": safe_int(record.get("num_pages")),
                "publication_year": safe_int(record.get("publication_year")),
                "language_code": coerce_str(record.get("language_code")),
            }
            texts.append(text)
            metadata_rows.append(meta)
            ids.append(f"book::{book_id}")

            if len(texts) >= self.embed_batch:
                yield VectorBatch(
                    source="books",
                    ids=ids,
                    texts=texts,
                    metadata_rows=metadata_rows,
                )
                texts, metadata_rows, ids = [], [], []

        if texts:
            yield VectorBatch(
                source="books",
                ids=ids,
                texts=texts,
                metadata_rows=metadata_rows,
            )

    def upsert_other_records(
        self,
        source: str,
        path: Path,
    ) -> None:
        self._process_vector_batches(self._iter_other_record_batches(source, path))

    def _iter_other_record_batches(
        self,
        source: str,
        path: Path,
    ) -> Iterable[VectorBatch]:
        texts: List[str] = []
        metadata_rows: List[Dict[str, Any]] = []
        ids: List[str] = []

        id_fields = {
            "authors": ("author_id",),
            "genres": ("book_id",),
            "works": ("best_book_id", "work_id"),
        }[source]

        for _line_no, record in iterate_records(path):
            if not isinstance(record, dict):
                continue
            record_id = ""
            for field in id_fields:
                record_id = coerce_str(record.get(field))
                if record_id:
                    break
            if not record_id:
                continue

            extra = ""
            if source == "genres":
                raw_genres = record.get("genres", {})
                if isinstance(raw_genres, dict):
                    ordered = sorted(
                        raw_genres.items(),
                        key=lambda item: (
                            (-int(item[1]), item[0]) if str(item[1]).isdigit() else (-1, item[0])
                        ),
                    )
                    top = [name for name, _ in ordered[:15]]
                    extra = f"Top genres: {', '.join(top)}"

            text = build_record_text(source, record, extra=extra)
            if not text:
                continue

            meta = {
                "source": f"goodreads_{source}",
                "record_type": source[:-1] if source.endswith("s") else source,
                **{f"{source[:-1]}_id": record_id},
            }
            if source == "works":
                meta["best_book_id"] = coerce_str(record.get("best_book_id"))
            texts.append(text)
            metadata_rows.append(meta)
            ids.append(f"{source[:-1]}::{record_id}")

            if len(texts) >= self.embed_batch:
                yield VectorBatch(
                    source=source,
                    ids=ids,
                    texts=texts,
                    metadata_rows=metadata_rows,
                )
                texts, metadata_rows, ids = [], [], []

        if texts:
            yield VectorBatch(
                source=source,
                ids=ids,
                texts=texts,
                metadata_rows=metadata_rows,
            )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Vectorize Goodreads datasets into Pinecone.")
    parser.add_argument("--data-dir", default="data")
    parser.add_argument("--pinecone-index", default=None)
    parser.add_argument("--pinecone-namespace", default=None)
    parser.add_argument("--pinecone-batch-size", type=int, default=200, choices=[150, 200])
    parser.add_argument("--embed-batch-size", type=int, default=100)
    parser.add_argument(
        "--book-offset",
        type=int,
        default=0,
        help="Skip the first N valid book records before embedding books.",
    )
    parser.add_argument(
        "--embed-concurrency",
        type=int,
        default=6,
        help="Number of concurrent Nebius embedding requests to run.",
    )
    parser.add_argument(
        "--max-pending-embed-batches",
        type=int,
        default=None,
        help="Maximum number of embedding batches buffered in flight before backpressure kicks in.",
    )
    parser.add_argument(
        "--progress-interval",
        type=int,
        default=500,
        help="Print progress every N vectors upserted.",
    )
    parser.add_argument("--analyze-only", action="store_true")
    parser.add_argument("--skip-books", action="store_true")
    parser.add_argument("--skip-authors", action="store_true")
    parser.add_argument("--skip-genres", action="store_true")
    parser.add_argument("--include-empty-text", action="store_true")
    return parser.parse_args()


def validate_preflight(
    args: argparse.Namespace,
    data_dir: Path,
    datasets: Dict[str, Optional[Path]],
) -> None:
    errors: List[str] = []

    if not data_dir.exists():
        errors.append(f"Data directory not found: {data_dir}")
    elif not data_dir.is_dir():
        errors.append(f"Data directory is not a directory: {data_dir}")

    if args.embed_batch_size < 1:
        errors.append("--embed-batch-size must be greater than 0.")
    if args.book_offset < 0:
        errors.append("--book-offset must be greater than or equal to 0.")
    if args.embed_concurrency < 1:
        errors.append("--embed-concurrency must be greater than 0.")
    if args.max_pending_embed_batches is not None and args.max_pending_embed_batches < 1:
        errors.append("--max-pending-embed-batches must be greater than 0 when set.")
    if args.progress_interval < 1:
        errors.append("--progress-interval must be greater than 0.")

    requested_sources = {
        "books": not args.skip_books,
        "authors": not args.skip_authors,
        "genres": not args.skip_genres,
    }
    if not any(requested_sources.values()):
        errors.append("Nothing to do: all dataset families are skipped.")

    for source, enabled in requested_sources.items():
        if enabled and datasets.get(source) is None:
            errors.append(f"Missing required dataset for enabled source '{source}' in {data_dir}.")

    if not args.analyze_only:
        if not OPENAI_AVAILABLE:
            errors.append("Missing dependency 'openai'. Install vectorization dependencies first.")
        if not PINECONE_AVAILABLE:
            errors.append(
                "Missing dependency 'pinecone'. Install vectorization dependencies first."
            )
        if not os.environ.get("NEBIUS_API_KEY"):
            errors.append("Missing required environment variable: NEBIUS_API_KEY.")
        if not (args.pinecone_index or os.environ.get("PINECONE_INDEX_NAME")):
            errors.append("Missing Pinecone index. Set --pinecone-index or PINECONE_INDEX_NAME.")
        if not os.environ.get("PINECONE_API_KEY"):
            errors.append("Missing required environment variable: PINECONE_API_KEY.")

    if errors:
        lines = [
            "",
            colorize("Preflight validation failed.", ANSI_RED, ANSI_BOLD),
            "",
            colorize("Missing or invalid configuration:", ANSI_YELLOW, ANSI_BOLD),
            *[f"- {error}" for error in errors],
        ]

        if not args.analyze_only:
            lines.extend(
                [
                    "",
                    colorize(
                        "Expected configuration for a full vectorization run:", ANSI_CYAN, ANSI_BOLD
                    ),
                    "- Set `NEBIUS_API_KEY`.",
                    "- Set `PINECONE_API_KEY`.",
                    "- Set `PINECONE_INDEX_NAME` or pass `--pinecone-index <name>`.",
                    "",
                    colorize("Typical setup:", ANSI_CYAN, ANSI_BOLD),
                    "- `cd cookbooks/02-domain-knowledge-pinecone-nexus`",
                    "- `cp .env.vectorize.example .env.local`",
                    "- Fill the required values in `.env.local` or `.env`.",
                    "",
                    colorize("Example command:", ANSI_CYAN, ANSI_BOLD),
                    "- `uv run python scripts/vectorize_goodreads_to_pinecone.py --data-dir ../../data --embed-batch-size 100 --embed-concurrency 6 --pinecone-batch-size 200 --progress-interval 1000`",
                ]
            )

        raise SystemExit("\n".join(lines))


def main() -> None:
    load_dotenv_if_present()
    args = parse_args()
    data_dir = Path(args.data_dir)

    book_file = pick_dataset_file(data_dir, "goodreads_books")
    author_file = pick_dataset_file(data_dir, "goodreads_book_authors")
    genres_file = pick_dataset_file(data_dir, "goodreads_book_genres_initial")

    datasets = {
        "books": book_file,
        "authors": author_file,
        "genres": genres_file,
    }
    validate_preflight(args, data_dir, datasets)

    print("Analyzing datasets...")

    def print_stats(stats: DatasetStats) -> None:
        print("\n".join(stats.to_cli_lines()))

    if author_file:
        print_stats(analyze_dataset(author_file, ("author_id",)))
    if genres_file:
        print_stats(analyze_dataset(genres_file, ("book_id",)))
    print_stats(analyze_dataset(book_file, ("book_id",)))

    if args.analyze_only:
        return

    if args.embed_batch_size == 1:
        print(
            colorize(
                "[warn] --embed-batch-size 1 sends one embedding request per record. "
                "This is useful for debugging, but it is much slower than batched embedding. "
                "Use 100 for normal ingestion throughput.",
                ANSI_YELLOW,
                ANSI_BOLD,
            )
        )

    # Use credentials and defaults from the process environment (for example .env.local).
    nebius_api_key = os.environ["NEBIUS_API_KEY"]
    nebius_base_url = os.environ.get("NEBIUS_BASE_URL", "https://api.studio.nebius.ai")
    nebius_model = os.environ.get("NEBIUS_EMBEDDING_MODEL", "Qwen/Qwen3-Embedding-8B")
    pinecone_index = args.pinecone_index or os.environ.get("PINECONE_INDEX_NAME")
    if not pinecone_index:
        raise ValueError(
            "Missing Pinecone index. Set --pinecone-index or PINECONE_INDEX_NAME in env."
        )

    vectorizer = GoodreadsVectorizer(
        pinecone_index_name=pinecone_index,
        pinecone_namespace=args.pinecone_namespace,
        nebius_api_key=nebius_api_key,
        nebius_base_url=nebius_base_url,
        nebius_model=nebius_model,
        batch_size=args.pinecone_batch_size,
        embed_batch=args.embed_batch_size,
        embed_concurrency=args.embed_concurrency,
        max_pending_embed_batches=args.max_pending_embed_batches,
        progress_interval=args.progress_interval,
    )

    authors = build_author_index(author_file) if author_file and not args.skip_authors else {}
    # Keep a lightweight author lookup for book enrichment even when author vectors
    # are not being upserted. Book vectors should still be linked to authors.
    if not authors and author_file:
        authors = build_author_index(author_file)
    genres = build_genres_index(genres_file) if genres_file and not args.skip_genres else {}
    if not args.skip_books:
        print("Indexing books...")
        vectorizer.upsert_books(
            book_file,
            authors=authors,
            genres=genres,
            include_empty=args.include_empty_text,
            book_offset=args.book_offset,
        )
    if not args.skip_authors and author_file:
        print("Indexing authors...")
        vectorizer.upsert_other_records("authors", author_file)
    if not args.skip_genres and genres_file:
        print("Indexing genres...")
        vectorizer.upsert_other_records("genres", genres_file)

    print(f"Done. vectors upserted: {vectorizer.total_vectors}")


if __name__ == "__main__":
    main()

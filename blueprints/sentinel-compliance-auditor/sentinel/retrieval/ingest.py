"""Ingest SOP markdown files into Pinecone vector index."""
from __future__ import annotations

import random
import re
import threading
import time
import yaml
from pathlib import Path

from sentinel.config import (
    EMBEDDING_DIMENSION,
    EMBEDDING_MODEL,
    NEBIUS_API_KEY,
    NEBIUS_BASE_URL,
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME,
    SOPS_DIR,
)


def parse_sop(filepath: Path) -> dict:
    """Parse a markdown SOP file, extracting YAML frontmatter and sections."""
    text = filepath.read_text(encoding="utf-8")

    frontmatter = {}
    body = text
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            try:
                frontmatter = yaml.safe_load(parts[1]) or {}
            except yaml.YAMLError:
                pass
            body = parts[2]

    return {"frontmatter": frontmatter, "body": body, "path": str(filepath)}


def chunk_sections(
    text: str,
    *,
    split_pattern: str,
    extract_header,
    chunk_size: int,
    overlap: int,
    continuation_prefix: str,
    min_section_len: int = 0,
) -> list[tuple[str, str]]:
    """Split ``text`` into ``(chunk_text, section_header)`` pairs.

    The one section chunker shared by the SOP ingester and both regulation
    chunkers (.txt and .md): sections come from ``split_pattern``; a section
    longer than ``chunk_size`` is word-split (~5 chars/word) with ``overlap``
    chars carried over, each continuation re-titled
    ``{continuation_prefix}{header} (continued)``.
    """
    sections = re.split(split_pattern, text, flags=re.MULTILINE)
    pairs: list[tuple[str, str]] = []
    for section in sections:
        section = section.strip()
        if not section or len(section) < min_section_len:
            continue
        header = extract_header(section)
        if len(section) <= chunk_size:
            pairs.append((section, header))
            continue
        words = section.split()
        words_per_chunk = chunk_size // 5  # ~5 chars per word avg
        start = 0
        part = 0
        while start < len(words):
            end = start + words_per_chunk
            chunk_text = " ".join(words[start:end])
            if header and part > 0:
                chunk_text = f"{continuation_prefix}{header} (continued)\n\n{chunk_text}"
            pairs.append((chunk_text, header))
            part += 1
            start = end - overlap // 5
    return pairs


def md_header(prefix: str):
    """Header extractor for markdown sections split on `prefix` ('## ' for
    SOPs, '###' for regulation .md files). Lines at other heading levels —
    e.g. the H1 title block before the first section — yield no header."""
    def extract(section: str) -> str:
        first = section.split("\n", 1)[0]
        return first.lstrip("# ").strip() if first.startswith(prefix) else ""
    return extract


def chunk_sop(filepath: Path, chunk_size: int = 1500, overlap: int = 200) -> list[dict]:
    """Split a parsed SOP into chunks, preserving section headers."""
    parsed = parse_sop(filepath)
    fm = parsed["frontmatter"]
    body = parsed["body"]

    sop_id = fm.get("sop_id", filepath.stem)
    title = fm.get("title", filepath.stem)
    business_unit = fm.get("business_unit", filepath.parent.name)
    regulations = fm.get("regulations", [])

    pairs = chunk_sections(
        body,
        split_pattern=r"(?=^## )",
        extract_header=md_header("## "),
        chunk_size=chunk_size,
        overlap=overlap,
        continuation_prefix="## ",
    )
    return [
        {
            "id": f"{sop_id}::chunk-{chunk_idx:04d}",
            "text": chunk_text,
            "metadata": {
                "sop_id": sop_id,
                "title": title,
                "business_unit": business_unit,
                "section": section_header,
                "chunk_index": chunk_idx,
                "regulations": regulations,
                "source_path": str(filepath),
            },
        }
        for chunk_idx, (chunk_text, section_header) in enumerate(pairs)
    ]


def with_retries(fn, attempts: int = 3, base_delay: float = 2.0):
    """Call ``fn()``, retrying transient failures with exponential backoff.

    Used around Nebius embedding calls and Pinecone queries/upserts: a single
    5xx on one batch must not abort a 2,386-chunk ingestion, and a transient
    error must not fail a sub-agent's RAG tool call."""
    for attempt in range(1, attempts + 1):
        try:
            return fn()
        except Exception:
            if attempt == attempts:
                raise
            time.sleep(base_delay * 2 ** (attempt - 1) + random.uniform(0, base_delay))


_embedding_client = None
_embedding_client_lock = threading.Lock()


def _get_embedding_client():
    """Process-wide OpenAI client for embeddings, mirroring the shared httpx
    client in graph/tools.py: embed_texts is called thousands of times during a
    full audit (once per sub-agent RAG retrieval), so creating a fresh client
    per call wastes connections and DNS lookups."""
    global _embedding_client
    if _embedding_client is not None:
        return _embedding_client
    with _embedding_client_lock:
        if _embedding_client is None:
            from openai import OpenAI
            _embedding_client = OpenAI(base_url=NEBIUS_BASE_URL, api_key=NEBIUS_API_KEY)
    return _embedding_client


def embed_texts(texts: list[str], batch_size: int = 64) -> list[list[float]]:
    """Embed texts using Nebius-hosted BGE model."""
    client = _get_embedding_client()
    all_embeddings = []

    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        response = with_retries(lambda b=batch: client.embeddings.create(model=EMBEDDING_MODEL, input=b))
        all_embeddings.extend([d.embedding for d in response.data])

    return all_embeddings


def create_index():
    """Create Pinecone index if it doesn't exist."""
    from pinecone import Pinecone, ServerlessSpec
    pc = Pinecone(api_key=PINECONE_API_KEY)

    existing = [idx.name for idx in pc.list_indexes()]
    if PINECONE_INDEX_NAME not in existing:
        pc.create_index(
            name=PINECONE_INDEX_NAME,
            dimension=EMBEDDING_DIMENSION,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )

    return pc


def ingest_all_sops(business_units: list[str] | None = None):
    """Ingest all SOPs from the data directory into Pinecone."""
    pc = create_index()
    index = pc.Index(PINECONE_INDEX_NAME)

    sop_dirs = sorted(SOPS_DIR.iterdir()) if business_units is None else [
        SOPS_DIR / bu for bu in business_units
    ]

    total_chunks = 0
    for bu_dir in sop_dirs:
        if not bu_dir.is_dir():
            continue

        namespace = bu_dir.name
        sop_files = sorted(bu_dir.glob("*.md"))
        print(f"\nIngesting {namespace}: {len(sop_files)} SOPs")

        all_chunks = []
        for filepath in sop_files:
            chunks = chunk_sop(filepath)
            all_chunks.extend(chunks)

        if not all_chunks:
            continue

        texts = [c["text"] for c in all_chunks]
        embeddings = embed_texts(texts)

        vectors = []
        for chunk, embedding in zip(all_chunks, embeddings):
            meta = chunk["metadata"].copy()
            meta["text"] = chunk["text"][:4000]
            if isinstance(meta.get("regulations"), list):
                meta["regulations"] = ", ".join(meta["regulations"])
            vectors.append({
                "id": chunk["id"],
                "values": embedding,
                "metadata": meta,
            })

        # Clear the namespace first: re-ingesting after a file was edited to
        # produce fewer chunks (or renamed) must not leave orphaned vectors.
        try:
            index.delete(delete_all=True, namespace=namespace)
        except Exception:
            pass  # namespace may not exist yet

        batch_size = 100
        for i in range(0, len(vectors), batch_size):
            batch = vectors[i : i + batch_size]
            with_retries(lambda b=batch: index.upsert(vectors=b, namespace=namespace))

        total_chunks += len(vectors)
        print(f"  Upserted {len(vectors)} chunks into namespace '{namespace}'")

    print(f"\nTotal chunks ingested: {total_chunks}")
    return total_chunks


if __name__ == "__main__":
    ingest_all_sops()

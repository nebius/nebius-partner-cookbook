"""Retrieve regulation text from Pinecone for compliance grounding."""
from __future__ import annotations

from functools import lru_cache

from sentinel.config import PINECONE_API_KEY, PINECONE_INDEX_NAME
from sentinel.retrieval.ingest import embed_texts, with_retries


_pc = None
_index = None

NAMESPACE = "regulations"


def _get_index():
    global _pc, _index
    if _index is None:
        # Lazy import: pinecone may be absent in the LangGraph Cloud container
        # (see CLAUDE.md), and eval/naive_rag.py imports this module at its own
        # top level — a module-level import would break at import time there.
        from pinecone import Pinecone

        _pc = Pinecone(api_key=PINECONE_API_KEY)
        _index = _pc.Index(PINECONE_INDEX_NAME)
    return _index


def retrieve_regulation_text(
    query: str,
    regulations: list[str] | None = None,
    top_k: int = 20,
    editions: list[str] | None = None,
) -> list[dict]:
    """Retrieve regulation text chunks relevant to a query.

    Args:
        query: search query (e.g. SOP title + regulation names)
        regulations: optional filter — only return chunks from these regulations
        top_k: max chunks to return
        editions: optional filter — e.g. ``["current"]`` to exclude superseded
            historical editions (HIPAA 2017/2020/2024, EU AI Act 2021 proposal,
            NIST AI RMF 2022 drafts). ``None`` searches every edition.

    Returns:
        list of dicts with keys: text, section, regulation, edition, source, score
    """
    cached = _retrieve_cached(
        query.strip(),
        tuple(regulations) if regulations else None,
        top_k,
        tuple(editions) if editions else None,
    )
    # Shallow-copy each dict so one caller can't mutate the shared cache entry.
    return [dict(chunk) for chunk in cached]


@lru_cache(maxsize=512)
def _retrieve_cached(
    query: str,
    regulations: tuple[str, ...] | None,
    top_k: int,
    editions: tuple[str, ...] | None,
) -> tuple[dict, ...]:
    """Process-wide cache: a full audit runs 200 sub-agents that issue
    near-identical formulaic queries ("HIPAA access control requirements"
    across 152 HIPAA-tagged SOPs) — without this, every one re-embeds the
    query and round-trips Pinecone. lru_cache is thread-safe for ThreadPool
    workers; entries are treated as read-only by the caller above."""
    index = _get_index()
    embedding = embed_texts([query])[0]

    filter_dict: dict | None = {}
    if regulations:
        filter_dict["regulation"] = {"$in": list(regulations)}
    if editions:
        filter_dict["edition"] = {"$in": list(editions)}
    filter_dict = filter_dict or None

    results = with_retries(lambda: index.query(
        vector=embedding,
        top_k=top_k,
        namespace=NAMESPACE,
        include_metadata=True,
        filter=filter_dict,
    ))

    # Dedup identical texts: some historical editions are byte-identical to
    # each other (HIPAA 2017 vs 2020), so without this a top-k can spend
    # several slots on copies of the same section.
    chunks = []
    seen_texts: set[str] = set()
    for match in results.matches:
        meta = match.metadata or {}
        text = meta.get("text", "")
        if not text or text in seen_texts:
            continue
        seen_texts.add(text)
        chunks.append({
            "text": text,
            "section": meta.get("section", ""),
            "regulation": meta.get("regulation", ""),
            "edition": meta.get("edition", "current"),
            "source": meta.get("source", ""),
            "score": match.score,
        })

    return tuple(chunks)


def format_regulation_context(chunks: list[dict], max_chars: int = 12000) -> str:
    """Format retrieved regulation chunks into a text block for the LLM prompt.

    The budget fills in descending-score order (regulation groups ordered by
    their best chunk) — alphabetical grouping used to let a low-score group
    exhaust the budget before a high-score one. Duplicate texts are skipped,
    and non-current editions are labelled so the model can't silently quote
    superseded text as current law.
    """
    if not chunks:
        return ""

    ordered = sorted(chunks, key=lambda c: c.get("score", 0.0), reverse=True)
    by_regulation: dict[str, list[dict]] = {}
    for chunk in ordered:
        reg = chunk.get("regulation", "Unknown")
        by_regulation.setdefault(reg, []).append(chunk)
    # dict insertion order = order of each regulation's best-scoring chunk

    parts = []
    total = 0
    seen_texts: set[str] = set()
    for reg, reg_chunks in by_regulation.items():
        # Emit the regulation header lazily so budget exhaustion can't leave a
        # dangling empty "### {reg}", and count header chars toward max_chars.
        reg_header = f"\n### {reg}\n"
        header_emitted = False
        for chunk in reg_chunks:
            text = chunk.get("text", "")
            if not text or text in seen_texts:
                continue
            seen_texts.add(text)
            section = chunk.get("section", "")
            edition = chunk.get("edition", "current")
            label = section
            if edition and edition != "current":
                label = f"{section} [edition: {edition}]".strip()
            section_header = f"**{label}**\n" if label else ""
            piece = f"{section_header}{text}\n"
            needed = len(piece) + (0 if header_emitted else len(reg_header))
            if total + needed > max_chars:
                break
            if not header_emitted:
                parts.append(reg_header)
                total += len(reg_header)
                header_emitted = True
            parts.append(piece)
            total += len(piece)

    return "\n".join(parts)

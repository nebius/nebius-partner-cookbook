"""Retrieve regulation text from Pinecone for compliance grounding."""
from __future__ import annotations

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
) -> list[dict]:
    """Retrieve regulation text chunks relevant to a query.

    Args:
        query: search query (e.g. SOP title + regulation names)
        regulations: optional filter — only return chunks from these regulations
        top_k: max chunks to return

    Returns:
        list of dicts with keys: text, section, regulation, source, score
    """
    index = _get_index()
    embedding = embed_texts([query])[0]

    filter_dict = None
    if regulations:
        filter_dict = {"regulation": {"$in": regulations}}

    results = with_retries(lambda: index.query(
        vector=embedding,
        top_k=top_k,
        namespace=NAMESPACE,
        include_metadata=True,
        filter=filter_dict,
    ))

    chunks = []
    for match in results.matches:
        meta = match.metadata or {}
        chunks.append({
            "text": meta.get("text", ""),
            "section": meta.get("section", ""),
            "regulation": meta.get("regulation", ""),
            "source": meta.get("source", ""),
            "score": match.score,
        })

    return chunks


def format_regulation_context(chunks: list[dict], max_chars: int = 12000) -> str:
    """Format retrieved regulation chunks into a text block for the LLM prompt."""
    if not chunks:
        return ""

    by_regulation: dict[str, list[dict]] = {}
    for chunk in chunks:
        reg = chunk.get("regulation", "Unknown")
        by_regulation.setdefault(reg, []).append(chunk)

    parts = []
    total = 0
    for reg, reg_chunks in sorted(by_regulation.items()):
        # Emit the regulation header lazily so budget exhaustion can't leave a
        # dangling empty "### {reg}", and count header chars toward max_chars.
        reg_header = f"\n### {reg}\n"
        header_emitted = False
        for chunk in reg_chunks:
            section = chunk.get("section", "")
            text = chunk.get("text", "")
            section_header = f"**{section}**\n" if section else ""
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

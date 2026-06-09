"""Retrieve regulation text from Pinecone for compliance grounding."""
from __future__ import annotations

from pinecone import Pinecone

from sentinel.config import PINECONE_API_KEY, PINECONE_INDEX_NAME
from sentinel.retrieval.ingest import embed_texts


_pc: Pinecone | None = None
_index = None

NAMESPACE = "regulations"


def _get_index():
    global _pc, _index
    if _index is None:
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

    results = index.query(
        vector=embedding,
        top_k=top_k,
        namespace=NAMESPACE,
        include_metadata=True,
        filter=filter_dict,
    )

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
        parts.append(f"\n### {reg}\n")
        total += len(parts[-1])
        for chunk in reg_chunks:
            section = chunk.get("section", "")
            text = chunk.get("text", "")
            if total + len(text) > max_chars:
                break
            header = f"**{section}**\n" if section else ""
            parts.append(f"{header}{text}\n")
            total += len(text)

    return "\n".join(parts)

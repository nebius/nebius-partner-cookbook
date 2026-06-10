"""Ingest regulation text files into Pinecone for RAG-based compliance grounding."""
from __future__ import annotations

import re
from pathlib import Path

from sentinel.config import (
    EMBEDDING_DIMENSION,
    PINECONE_API_KEY,
    PINECONE_INDEX_NAME,
    REGULATIONS_DIR,
)
from sentinel.retrieval.ingest import chunk_sections, embed_texts, md_header, with_retries

REGULATION_MAP = {
    # Core 9 frameworks
    "hipaa_45cfr_part160": "HIPAA",
    "hipaa_45cfr_part162": "HIPAA",
    "hipaa_45cfr_part164": "HIPAA",
    "soc2": "SOC 2",
    "gdpr": "GDPR",
    "eu_ai_act": "EU AI Act",
    "nist_ai_rmf": "NIST AI RMF",
    "nist_ai_600": "NIST AI RMF",
    "california_sb53": "California SB 53",
    "california_sb942": "California SB 942",
    "california_ab853": "California AB 853",
    "sr_11_7": "SR 11-7",
    # Financial laws
    "bsa_31cfr": "BSA / 31 CFR",
    "ecoa_regulation_b": "ECOA / Reg B",
    "fcra": "FCRA",
    # EU directives & regulations
    "eu_amld4": "EU AMLD4",
    "eu_eprivacy": "EU ePrivacy",
    "eu_funds_transfer": "EU Funds Transfer Reg",
    "eu_mdr": "EU MDR",
    "eu_standard_contractual_clauses": "EU SCCs",
    # FDA / 21 CFR
    "fda_21cfr_part11": "FDA 21 CFR Part 11",
    "fda_21cfr_part807": "FDA 21 CFR Part 807",
    "fda_21cfr_part820": "FDA 21 CFR Part 820",
    "fda_ai_ml_samd": "FDA AI/ML SaMD",
    "fda_clinical_decision_support": "FDA CDS Guidance",
    # NIST publications
    "nist_csf": "NIST CSF 2.0",
    "nist_privacy_framework": "NIST Privacy Framework",
    "nist_sp_1270": "NIST SP 1270",
    "nist_sp_800_34": "NIST SP 800-34",
    "nist_sp_800_53": "NIST SP 800-53",
    "nist_sp_800_61": "NIST SP 800-61",
    "nist_sp_800_63b": "NIST SP 800-63B",
    "nist_sp_800_88": "NIST SP 800-88",
    "nist_sp_800_161": "NIST SP 800-161",
    "nist_sp_800_207": "NIST SP 800-207",
    "nist_sp_800_218": "NIST SP 800-218",
    # OWASP
    "owasp_api_security": "OWASP API Top 10",
    "owasp_top_10": "OWASP Top 10",
    "pci_dss": "PCI DSS",
}


EDITION_PATTERNS = {
    "_2017": "2017",
    "_2020": "2020",
    "_2024": "2024",
    "_draft1_2022": "2022-draft1",
    "_draft2_2022": "2022-draft2",
    "_2021_commission_proposal": "2021-proposal",
}


def _detect_regulation(filename: str) -> str:
    # Longest key first + startswith: unanchored substring matching with
    # insertion-order precedence could attribute a file to whichever shorter
    # key happened to occur first inside its name.
    for prefix in sorted(REGULATION_MAP, key=len, reverse=True):
        if filename.startswith(prefix):
            return REGULATION_MAP[prefix]
    return "Unknown"


def _detect_edition(filename: str) -> str:
    for pattern, edition in EDITION_PATTERNS.items():
        if pattern in filename:
            return edition
    return "current"


def _txt_header(section: str) -> str:
    """Header of a .txt regulation section: a '§ ...' line directly, or — when
    the section opens with a ===/--- ruler — the first non-ruler line below it
    (the title used to strip to '' and the section lost its name)."""
    lines = section.split("\n")
    first = lines[0].strip()
    if first.startswith("§"):
        return first.strip("= -§").strip()
    if first.startswith("=") or first.startswith("-"):
        title = first.strip("= -§").strip()
        if title:
            return title
        for line in lines[1:]:
            line = line.strip()
            if line and set(line) - {"=", "-", " "}:
                return line.strip("= -§").strip()
    return ""


def _chunk_regulation_file(
    filepath: Path,
    *,
    split_pattern: str,
    extract_header,
    continuation_prefix: str,
    # ~700 tokens per chunk. The previous 1200 chars (~300 tokens) was tiny for
    # a 4096-dim 32k-context embedder and split clauses across chunks.
    chunk_size: int = 2800,
    overlap: int = 200,
) -> list[dict]:
    text = filepath.read_text(encoding="utf-8")
    regulation = _detect_regulation(filepath.stem)
    edition = _detect_edition(filepath.stem)
    return [
        {
            "text": chunk_text,
            "section": header,
            "regulation": regulation,
            "edition": edition,
            "source": filepath.name,
        }
        for chunk_text, header in chunk_sections(
            text,
            split_pattern=split_pattern,
            extract_header=extract_header,
            chunk_size=chunk_size,
            overlap=overlap,
            continuation_prefix=continuation_prefix,
            min_section_len=20,
        )
    ]


def chunk_regulation(filepath: Path) -> list[dict]:
    if filepath.suffix == ".md":
        return _chunk_regulation_file(
            filepath, split_pattern=r"(?=^### )",
            extract_header=md_header("###"), continuation_prefix="### ",
        )
    # `^[ \t]*§ ` matches both eCFR-indented ("  § 164.312") and unindented
    # ("§ 1020.220", the BSA/31 CFR style) section headers — the old
    # two-space-indented pattern left 57% of the index (all of BSA) with no
    # section structure at all.
    return _chunk_regulation_file(
        filepath, split_pattern=r"(?=^[ \t]*§ |\n={40,}|\n-{40,})",
        extract_header=_txt_header, continuation_prefix="§ ",
    )


def ingest_regulations():
    """Ingest all regulation text files into Pinecone."""
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
    index = pc.Index(PINECONE_INDEX_NAME)

    files = sorted(REGULATIONS_DIR.glob("*.txt")) + sorted(REGULATIONS_DIR.glob("*.md"))
    files = [f for f in files if f.name != "README.md"]

    all_chunks = []
    for filepath in files:
        chunks = chunk_regulation(filepath)
        for i, chunk in enumerate(chunks):
            chunk["id"] = f"reg::{filepath.stem}::chunk-{i:04d}"
        all_chunks.extend(chunks)
        print(f"  {filepath.name}: {len(chunks)} chunks")

    if not all_chunks:
        print("No regulation chunks to ingest.")
        return 0

    print(f"\nEmbedding {len(all_chunks)} chunks...")
    texts = [c["text"] for c in all_chunks]
    embeddings = embed_texts(texts)

    vectors = []
    for chunk, embedding in zip(all_chunks, embeddings):
        vectors.append({
            "id": chunk["id"],
            "values": embedding,
            "metadata": {
                "text": chunk["text"][:4000],
                "section": chunk["section"],
                "regulation": chunk["regulation"],
                "edition": chunk.get("edition", "current"),
                "source": chunk["source"],
            },
        })

    namespace = "regulations"

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

    print(f"\nIngested {len(vectors)} regulation chunks into namespace '{namespace}'")
    return len(vectors)


if __name__ == "__main__":
    ingest_regulations()

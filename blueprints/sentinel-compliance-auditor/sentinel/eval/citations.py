"""Citation matching and verification against the regulation corpus.

Three consumers share this module:
- `scripts/eval_retrieval.py` — recall@k of expected citations in retrieved chunks
- `scripts/run_qa_eval.py` — retrieval recall inside the agentic Q&A path, and
  citation verification of answers (does the cited clause exist in the corpus?)
- tests

Verification is deterministic (existence in the source texts) — it catches
invented sections ("§164.999", "Article 999"), not subtly-wrong supporting
text. An LLM entailment check (does the clause say what the answer claims?)
would be the next level; see the docstring on `verify_citations`.
"""
from __future__ import annotations

import re
from functools import lru_cache

_ROMAN = r"[ivxlc]+"


# ── citation normalization + chunk matching (shared with eval_retrieval) ────

def normalize_citation(section: str) -> tuple[str, str]:
    """Return (clause_id, base_id) for tolerant matching.

    clause_id is the full normalized path (e.g. "164.308(a)(1)(ii)(a)"),
    base_id the coarse section (e.g. "164.308", "article 32", "cc6.1").
    """
    s = section.strip().lstrip("§").strip().lower()
    s = re.sub(r"\s+", " ", s)

    m = re.search(r"(\d{3}\.\d{3}(?:\([a-z0-9]+\))*)", s)
    if m:  # HIPAA / eCFR style: 164.308(a)(1)(ii)(A)
        clause = m.group(1)
        return clause, clause.split("(")[0]
    m = re.search(r"art(?:icle)?\.?\s*(\d+[a-z]?)", s)
    if m:  # GDPR / EU AI Act / directives
        return f"article {m.group(1)}", f"article {m.group(1)}"
    m = re.search(r"cc\s?(\d(?:\.\d)?)", s)
    if m:  # SOC 2 trust services criteria
        return f"cc{m.group(1)}", f"cc{m.group(1)}"
    m = re.search(r"(govern|map|measure|manage)\s*[-.]?\s*(\d(?:\.\d+)?)", s)
    if m:  # NIST AI RMF functions
        return f"{m.group(1)} {m.group(2)}", f"{m.group(1)} {m.group(2)}"
    m = re.search(rf"sections?\s+({_ROMAN})(?:\s*[-–]\s*({_ROMAN}))?\b", s)
    if m:  # SR 11-7 style roman-numeral sections, incl. ranges ("Sections II-IV")
        token = f"roman:{m.group(1)}" + (f"-{m.group(2)}" if m.group(2) else "")
        return token, token
    return s, s


def _haystack(chunk: dict) -> str:
    text = f"{chunk.get('section', '')}\n{chunk.get('text', '')}".lower()
    return re.sub(r"\s+", " ", text)


def citation_hit(citation: dict, chunks: list[dict]) -> tuple[bool, bool]:
    """(clause_hit, base_hit) — does any chunk contain the cited clause/section?

    Articles are matched as "article N" (word-bounded number); eCFR clauses by
    substring of the normalized path with progressively shorter prefixes
    counting only toward base_hit.
    """
    clause, base = normalize_citation(citation.get("section", ""))
    reg = (citation.get("regulation") or "").lower()
    clause_hit = base_hit = False

    def _reg_matches(chunk: dict) -> bool:
        chunk_reg = (chunk.get("regulation") or "").lower()
        return not (reg and chunk_reg) or reg in chunk_reg or chunk_reg in reg

    if base.startswith("roman:"):
        # SR 11-7 style: "Section IV" → a chunk whose text contains "IV." as a
        # heading (range citations accept any numeral in the range's file).
        numerals = base.split(":", 1)[1].split("-")
        pattern = "|".join(rf"\b{re.escape(n)}\." for n in numerals)
        for chunk in chunks:
            if _reg_matches(chunk) and re.search(pattern, _haystack(chunk)):
                return True, True
        return False, False

    for chunk in chunks:
        hay = _haystack(chunk)
        if base.startswith("article "):
            # "Article 32" exists in both GDPR and the EU AI Act — an article
            # number only counts when the chunk belongs to the cited regulation.
            num = base.split(" ", 1)[1]
            if not re.search(rf"art(?:icle)?\.?\s*{re.escape(num)}\b", hay):
                continue
            if not _reg_matches(chunk):
                continue
            clause_hit = base_hit = True
            break
        if clause in hay:
            clause_hit = base_hit = True
            break
        if base in hay:
            base_hit = True
    return clause_hit, base_hit


def parse_formatted_context(text: str) -> list[dict]:
    """Parse `format_regulation_context` output back into pseudo-chunks.

    The formatted context groups chunks under "### {regulation}" headers; the
    agentic Q&A path captures it as raw tool-output text, and citation_hit
    needs (regulation, text) pairs to disambiguate article numbers.
    """
    chunks: list[dict] = []
    current_reg = ""
    buf: list[str] = []

    def _flush():
        nonlocal buf
        body = "\n".join(buf).strip()
        if body:
            chunks.append({"regulation": current_reg, "section": "", "text": body})
        buf = []

    for line in text.splitlines():
        m = re.match(r"^### (.+)$", line.strip())
        if m:
            _flush()
            current_reg = m.group(1).strip()
            continue
        buf.append(line)
    _flush()
    return chunks


# ── citation extraction + corpus-backed verification ────────────────────────

# Regulation-name aliases for attributing bare "Article N" citations to the
# regulation mentioned nearest in the surrounding text.
_REG_ALIASES: dict[str, str] = {
    "gdpr": "GDPR",
    "general data protection": "GDPR",
    "eu ai act": "EU AI Act",
    "ai act": "EU AI Act",
    "mdr": "EU MDR",
    "medical device regulation": "EU MDR",
    "amld": "EU AMLD4",
    "eprivacy": "EU ePrivacy",
    "standard contractual clauses": "EU SCCs",
    "scc": "EU SCCs",
    "funds transfer": "EU Funds Transfer Reg",
}

# eCFR part → regulation, for bare numeric clause ids.
_ECFR_PARTS: dict[str, str] = {
    "160": "HIPAA", "162": "HIPAA", "164": "HIPAA",
    "1002": "ECOA / Reg B",
    "11": "FDA 21 CFR Part 11", "807": "FDA 21 CFR Part 807", "820": "FDA 21 CFR Part 820",
}
# 31 CFR chapter X (BSA) uses 4-digit parts 1000-1099.
_BSA_PART_RE = re.compile(r"^10\d{2}$")

_ARTICLE_BEARING = ("GDPR", "EU AI Act", "EU MDR", "EU AMLD4", "EU ePrivacy", "EU SCCs", "EU Funds Transfer Reg")

# Authoritative article counts. The local corpus texts are ABRIDGED (the GDPR
# file stops at Article 84 of 99; the AI Act file's sections end around 73 of
# 113), so corpus presence alone would falsely flag legitimate high-numbered
# articles as hallucinated. An article verifies if it appears in the corpus OR
# falls within the regulation's real bounds; numbers beyond every bound
# ("Article 291", "Article 999") are still caught.
_ARTICLE_MAX = {
    "GDPR": 99,
    "EU AI Act": 113,
    "EU MDR": 123,
    "EU AMLD4": 69,
    "EU ePrivacy": 21,
    "EU SCCs": 18,
    "EU Funds Transfer Reg": 27,
}


@lru_cache(maxsize=1)
def corpus_text_by_regulation() -> dict[str, str]:
    """Lowercased, whitespace-normalized source text per canonical regulation.

    ~10 MB in memory; built once per process from data/regulations/."""
    from sentinel.config import REGULATIONS_DIR
    from sentinel.retrieval.ingest_regulations import _detect_regulation

    texts: dict[str, list[str]] = {}
    files = sorted(REGULATIONS_DIR.glob("*.txt")) + sorted(REGULATIONS_DIR.glob("*.md"))
    for f in files:
        if f.name == "README.md":
            continue
        reg = _detect_regulation(f.stem)
        raw = f.read_text(encoding="utf-8", errors="ignore").lower()
        texts.setdefault(reg, []).append(re.sub(r"\s+", " ", raw))
    return {reg: "\n".join(parts) for reg, parts in texts.items()}


def extract_citations(answer: str) -> list[dict]:
    """Conservatively extract clause citations from an answer.

    Returns [{"raw", "regulation", "clause", "base"}]. The extractor favors
    precision: a missed citation costs nothing, a false extraction would flag
    a hallucination that isn't one.
    """
    if not answer:
        return []
    text = answer
    lowered = text.lower()
    citations: list[dict] = []
    seen: set[tuple[str, str]] = set()

    def _add(regulation: str, raw: str):
        clause, base = normalize_citation(raw)
        key = (regulation, clause)
        if key not in seen:
            seen.add(key)
            citations.append({"raw": raw.strip(), "regulation": regulation, "clause": clause, "base": base})

    # eCFR-style paths: "§ 164.312(a)(2)(iv)", "45 CFR 164.308", "1020.220".
    for m in re.finditer(r"(?:§\s*|\bcfr\s+(?:part\s+)?)?(\d{2,4})\.(\d{1,3})((?:\([a-z0-9]{1,4}\))*)", lowered):
        part = m.group(1)
        prefix = lowered[max(0, m.start() - 24):m.start()]
        anchored = "§" in prefix or "cfr" in prefix or "section" in prefix or m.group(0).lstrip().startswith("§")
        if part in _ECFR_PARTS:
            reg = _ECFR_PARTS[part]
        elif _BSA_PART_RE.match(part):
            reg = "BSA / 31 CFR"
        elif anchored:
            reg = ""  # unattributed eCFR — verified against the whole corpus
        else:
            continue  # bare number with no legal anchor — likely not a citation
        _add(reg, f"{part}.{m.group(2)}{m.group(3)}")

    # Articles: attribute to the nearest preceding regulation mention.
    reg_mentions = [
        (m.start(), canonical)
        for alias, canonical in _REG_ALIASES.items()
        for m in re.finditer(re.escape(alias), lowered)
    ]
    reg_mentions.sort()
    for m in re.finditer(r"\bart(?:icle)?s?\.?\s*(\d{1,3}[a-z]?)\b", lowered):
        preceding = [c for pos, c in reg_mentions if pos < m.start()]
        regulation = preceding[-1] if preceding else ""
        _add(regulation, f"article {m.group(1)}")

    # SOC 2 trust services criteria and NIST AI RMF functions.
    for m in re.finditer(r"\bcc\s?(\d\.\d)\b", lowered):
        _add("SOC 2", f"cc{m.group(1)}")
    for m in re.finditer(r"\b(govern|map|measure|manage)[ \-.]?(\d(?:\.\d+)?)\b", lowered):
        _add("NIST AI RMF", f"{m.group(1)} {m.group(2)}")

    return citations


def _exists_in_corpus(citation: dict) -> tuple[bool, bool]:
    """(base_exists, exact_exists) for one extracted citation."""
    corpus = corpus_text_by_regulation()
    regulation = citation["regulation"]
    clause = citation["clause"]
    base = citation["base"]

    if base.startswith("article "):
        num_str = base.split(" ", 1)[1].rstrip("abcdefghij")
        try:
            num = int(num_str)
        except ValueError:
            return False, False
        # Bounds, not corpus presence (the corpus is abridged). Attribution is
        # a nearest-mention heuristic, so per-regulation strictness would turn
        # attribution noise into false hallucination flags ("Article 49" near
        # an SCC mention is GDPR's Art. 49) — an article verifies if ANY
        # article-bearing regulation could contain it. "Article 291"/"999"
        # still fail every bound.
        hit = num <= max(_ARTICLE_MAX.values())
        return hit, hit

    targets = [regulation] if regulation in corpus else list(corpus)
    base_exists = any(base in corpus[r] for r in targets)
    # eCFR subsection paths rarely appear as one literal string in the source
    # ("164.312" then nested "(a)(2)(iv)") — exact is best-effort.
    exact_exists = base_exists and (clause == base or any(clause in corpus[r] for r in targets))
    return base_exists, exact_exists


def verify_citations(answer: str) -> dict:
    """Extract citations from an answer and verify each exists in the corpus.

    Returns {"n", "n_verified", "precision", "citations": [...]} where
    precision = base-level existence rate (None when nothing was extracted).
    Deterministic existence checking only — an entailment check (does the
    clause support the claim?) would need an LLM pass. An unverified citation
    means "not verifiable against the local corpus": usually a fabricated
    clause, occasionally a real citation to a document the KB doesn't carry.
    """
    citations = extract_citations(answer)
    results = []
    n_verified = 0
    for c in citations:
        base_exists, exact_exists = _exists_in_corpus(c)
        n_verified += int(base_exists)
        results.append({**c, "exists": base_exists, "exists_exact": exact_exists})
    return {
        "n": len(citations),
        "n_verified": n_verified,
        "precision": (n_verified / len(citations)) if citations else None,
        "citations": results,
    }

"""Weakness-recall scoring: did the audit actually FIND the planted defects?

The compliance matrix plants specific weaknesses in each gap/partial SOP
(e.g. "No post-market monitoring plan as required by Article 72"). Level
matching alone gives full credit for reaching the right verdict via entirely
wrong reasoning — and the worst-level aggregation means one spurious gap
finding can match a gap ground truth without ever touching the planted
defect. This module scores whether the run's finding texts for a (SOP,
regulation) pair mention each planted weakness.

Matching is deterministic: a clause-reference match (the weakness cites
"Article 72" and so does a finding) counts immediately; otherwise a
distinctive-term overlap threshold applies. An LLM matcher would be more
forgiving of paraphrase — this one is intentionally cheap, offline, and
reproducible.
"""
from __future__ import annotations

import re
from collections import defaultdict

# Generic audit/regulatory vocabulary that appears in almost every finding —
# matching on these would make everything "found".
_STOPWORDS = {
    "the", "a", "an", "and", "or", "for", "nor", "with", "without", "into",
    "this", "that", "these", "those", "are", "is", "was", "were", "been", "being",
    "not", "no", "none", "any", "all", "each", "per", "as", "by", "of", "to", "in",
    "on", "at", "from", "their", "its", "it", "be", "has", "have", "had", "but",
    "required", "requirements", "requirement", "requires", "require",
    "missing", "lacks", "lacking", "absent", "despite", "entirely", "only",
    "defined", "specified", "documented", "described", "established",
    "provisions", "provision", "procedures", "procedure", "process", "processes",
    "mechanisms", "mechanism", "controls", "control", "measures", "measure",
    "specific", "specifically", "explicit", "explicitly", "formal",
    "sop", "policy", "policies", "section", "article", "regulation",
}

_CLAUSE_REF_RE = re.compile(
    r"art(?:icle)?\.?\s*\d{1,3}[a-z]?\b"          # Article 72
    r"|\d{2,4}\.\d{1,3}(?:\([a-z0-9]{1,4}\))*"     # 164.308(a)(1)
    r"|\bcc\s?\d\.\d\b"                            # CC6.1
    r"|\b(?:govern|map|measure|manage)[ \-.]?\d(?:\.\d+)?\b",  # AI RMF
)


def _clause_refs(text: str) -> set[str]:
    return {re.sub(r"\s+", "", m.group(0)) for m in _CLAUSE_REF_RE.finditer(text.lower())}


def _distinctive_terms(text: str) -> set[str]:
    words = re.findall(r"[a-z][a-z\-]{3,}", text.lower())
    return {w.strip("-") for w in words if w.strip("-") not in _STOPWORDS}


def weakness_hit(weakness: str, findings_text: str, term_threshold: float = 0.5) -> bool:
    """Does the findings text mention this planted weakness?

    A shared clause reference counts immediately (the weakness names
    "Article 72" and a finding cites it). Otherwise at least
    ``term_threshold`` of the weakness's distinctive terms must appear.
    """
    if not findings_text:
        return False
    hay = findings_text.lower()

    weakness_refs = _clause_refs(weakness)
    if weakness_refs and weakness_refs & _clause_refs(findings_text):
        return True

    terms = _distinctive_terms(weakness)
    if not terms:
        return False
    present = sum(1 for t in terms if t in hay)
    return present / len(terms) >= term_threshold


def weakness_recall(matrix_entries: list[dict], pair_texts: dict) -> dict:
    """Score planted-weakness recall for an audit run.

    Args:
        matrix_entries: raw compliance-matrix entries (with ``weaknesses``).
        pair_texts: {(sop_id, regulation): finding text} parsed from the run.

    Returns overall recall (over ALL planted weaknesses — pairs the run never
    produced findings for count as missed), recall among scored pairs only,
    per-regulation breakdown, and per-weakness rows for drill-down.
    """
    rows = []
    by_regulation: dict[str, list[bool]] = defaultdict(list)
    scored_hits = scored_total = 0

    for entry in matrix_entries:
        weaknesses = entry.get("weaknesses") or []
        if not weaknesses:
            continue
        key = (entry["sop_id"], entry["regulation"])
        text = pair_texts.get(key, "")
        for weakness in weaknesses:
            hit = weakness_hit(weakness, text)
            rows.append({
                "sop_id": entry["sop_id"],
                "regulation": entry["regulation"],
                "weakness": weakness,
                "hit": hit,
                "pair_scored": bool(text),
            })
            by_regulation[entry["regulation"]].append(hit)
            if text:
                scored_total += 1
                scored_hits += int(hit)

    total = len(rows)
    hits = sum(1 for r in rows if r["hit"])
    return {
        "total_weaknesses": total,
        "hits": hits,
        "recall": (hits / total) if total else 0.0,
        "scored_total": scored_total,
        "scored_hits": scored_hits,
        "recall_scored": (scored_hits / scored_total) if scored_total else 0.0,
        "per_regulation": {
            reg: {"n": len(v), "recall": sum(v) / len(v)}
            for reg, v in sorted(by_regulation.items())
        },
        "rows": rows,
    }

#!/usr/bin/env python3
"""Retrieval-quality eval: recall@k of expected citations from the Q&A dataset.

End-to-end audit accuracy can't distinguish retrieval misses from reasoning
misses. This harness measures the retrieval layer alone: for each Q&A question
with `expected_citations`, run `retrieve_regulation_text` and check whether
the cited sections appear in the returned chunks.

Usage:
    python3 scripts/eval_retrieval.py                       # defaults: top_k=15, all editions
    python3 scripts/eval_retrieval.py --top-k 20 --editions current
    python3 scripts/eval_retrieval.py --filtered            # filter by regulations_involved
    python3 scripts/eval_retrieval.py --json                # machine-readable output
    python3 scripts/eval_retrieval.py --misses              # print every missed citation

Requires NEBIUS_API_KEY (query embedding) and PINECONE_API_KEY.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

DATASET_PATH = Path("data/eval/qa_dataset.jsonl")

# web_grounded answers live on the web, not in the KB — retrieval recall is
# not defined for them.
SKIP_CATEGORIES = {"web_grounded"}

# Copyrighted texts that are deliberately NOT ingested (see
# data/regulations/README.md) — their citations can never hit and would only
# deflate the metric. Override with --include-missing.
NOT_IN_KB = {"SOC 2", "PCI DSS"}

_ROMAN = r"[ivxlc]+"


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


def run_eval(top_k: int, editions: list[str] | None, filtered: bool, categories: set[str] | None,
             include_missing: bool = False):
    from dotenv import load_dotenv
    load_dotenv()
    from sentinel.retrieval.regulations import retrieve_regulation_text

    questions = [json.loads(line) for line in DATASET_PATH.read_text().splitlines() if line.strip()]
    rows = []
    for q in questions:
        if q.get("category") in SKIP_CATEGORIES:
            continue
        if categories and q.get("category") not in categories:
            continue
        citations = q.get("expected_citations") or []
        if not include_missing:
            citations = [c for c in citations if c.get("regulation") not in NOT_IN_KB]
        if not citations:
            continue

        regs = q.get("regulations_involved") if filtered else None
        chunks = retrieve_regulation_text(q["question"], regulations=regs, top_k=top_k, editions=editions)

        for citation in citations:
            clause_hit, base_hit = citation_hit(citation, chunks)
            rows.append({
                "question_id": q["id"],
                "category": q["category"],
                "regulation": citation.get("regulation", ""),
                "section": citation.get("section", ""),
                "clause_hit": clause_hit,
                "base_hit": base_hit,
            })
    return rows


def summarize(rows: list[dict]) -> dict:
    def recall(subset, key):
        return sum(1 for r in subset if r[key]) / len(subset) if subset else 0.0

    by_cat = defaultdict(list)
    by_reg = defaultdict(list)
    for r in rows:
        by_cat[r["category"]].append(r)
        by_reg[r["regulation"]].append(r)

    return {
        "n_citations": len(rows),
        "recall_clause": recall(rows, "clause_hit"),
        "recall_base": recall(rows, "base_hit"),
        "per_category": {
            cat: {"n": len(rs), "recall_clause": recall(rs, "clause_hit"), "recall_base": recall(rs, "base_hit")}
            for cat, rs in sorted(by_cat.items())
        },
        "per_regulation": {
            reg: {"n": len(rs), "recall_clause": recall(rs, "clause_hit"), "recall_base": recall(rs, "base_hit")}
            for reg, rs in sorted(by_reg.items())
        },
    }


def main():
    ap = argparse.ArgumentParser(description="Retrieval recall@k against expected citations")
    ap.add_argument("--top-k", type=int, default=15, help="chunks per query (sub-agents use 15)")
    ap.add_argument("--editions", default="all", help='"current", "all", or comma-separated list')
    ap.add_argument("--filtered", action="store_true", help="filter by the question's regulations_involved")
    ap.add_argument("--categories", default="", help="comma-separated category subset")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--misses", action="store_true", help="list every missed citation")
    ap.add_argument("--include-missing", action="store_true",
                    help=f"score citations for regulations not in the KB ({', '.join(sorted(NOT_IN_KB))})")
    args = ap.parse_args()

    editions = None if args.editions in ("all", "") else [e.strip() for e in args.editions.split(",")]
    categories = set(args.categories.split(",")) if args.categories else None

    rows = run_eval(args.top_k, editions, args.filtered, categories, include_missing=args.include_missing)
    summary = summarize(rows)
    summary["config"] = {"top_k": args.top_k, "editions": editions or "all", "filtered": args.filtered}

    if args.json:
        print(json.dumps({"summary": summary, "rows": rows}, indent=2))
        return

    cfg = summary["config"]
    print(f"\nRetrieval recall@{cfg['top_k']} (editions={cfg['editions']}, filtered={cfg['filtered']})")
    print(f"{'=' * 64}")
    print(f"  Citations scored:  {summary['n_citations']}")
    print(f"  Clause recall:     {summary['recall_clause']:.3f}   (full clause path found)")
    print(f"  Section recall:    {summary['recall_base']:.3f}   (base section found)")

    print(f"\n  {'Category':<22} {'n':>4} {'clause':>8} {'section':>9}")
    for cat, s in summary["per_category"].items():
        print(f"  {cat:<22} {s['n']:>4} {s['recall_clause']:>8.3f} {s['recall_base']:>9.3f}")

    print(f"\n  {'Regulation':<22} {'n':>4} {'clause':>8} {'section':>9}")
    for reg, s in summary["per_regulation"].items():
        print(f"  {reg:<22} {s['n']:>4} {s['recall_clause']:>8.3f} {s['recall_base']:>9.3f}")

    if args.misses:
        print("\nMissed citations (no base-section hit):")
        for r in rows:
            if not r["base_hit"]:
                print(f"  {r['question_id']} [{r['category']}] {r['regulation']} {r['section']}")


if __name__ == "__main__":
    main()

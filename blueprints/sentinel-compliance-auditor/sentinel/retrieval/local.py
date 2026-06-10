"""Local file-based SOP loading and lookup."""
from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

from sentinel.config import SOPS_DIR
from sentinel.models import SOPChunk
from sentinel.retrieval.ingest import parse_sop


@lru_cache(maxsize=1)
def _parsed_sops() -> tuple[dict, ...]:
    """Parse every SOP file once per process.

    Every sub-agent calls load_sop_by_id, so without this cache a full
    200-SOP audit re-parses the whole tree per call (~40,000 file parses).
    SOP files are static demo data; call _parsed_sops.cache_clear() after
    editing them in a live process.
    """
    from sentinel.config import SOP_BUSINESS_UNITS

    parsed_all = []
    for bu in SOP_BUSINESS_UNITS:
        bu_dir = SOPS_DIR / bu
        if not bu_dir.is_dir():
            continue
        for fp in sorted(bu_dir.glob("*.md")):
            parsed = parse_sop(fp)
            parsed["business_unit_dir"] = bu
            parsed_all.append(parsed)
    return tuple(parsed_all)


def load_sop_by_id(sop_id: str) -> dict | None:
    """Load a single SOP by its sop_id or title (fuzzy match) from any business unit."""
    query = sop_id.strip().lower()
    best_match = None
    best_score = 0

    for parsed in _parsed_sops():
        fm = parsed["frontmatter"]
        sid = fm.get("sop_id", "")
        title = fm.get("title", "")

        if sid == sop_id or sid.lower() == query:
            return parsed
        if title.lower() == query:
            return parsed

        if query in title.lower() or query in sid.lower():
            # Score against the field that actually matched (tightest match
            # wins) — scoring an ID match against the title length skewed
            # ranking toward SOPs with short titles.
            matched_lens = [len(f) for f in (title, sid) if query in f.lower()]
            score = len(query) / max(min(matched_lens), 1)
            if score > best_score:
                best_score = score
                best_match = parsed

    return best_match


def list_all_sops() -> list[dict]:
    """Return metadata for all SOPs across all business units."""
    results = []
    for parsed in _parsed_sops():
        fm = parsed["frontmatter"]
        stem = Path(parsed["path"]).stem
        results.append({
            "sop_id": fm.get("sop_id", stem),
            "title": fm.get("title", stem),
            "business_unit": fm.get("business_unit", parsed["business_unit_dir"]),
            "regulations": fm.get("regulations", []),
        })
    return results


def load_sop_chunks(sop: dict) -> list[SOPChunk]:
    """Convert a parsed SOP dict into SOPChunk objects (one per section)."""
    fm = sop["frontmatter"]
    body = sop["body"]
    sop_id = fm.get("sop_id", "UNKNOWN")
    title = fm.get("title", "")
    business_unit = fm.get("business_unit", "")

    sections = re.split(r"(?=^## )", body, flags=re.MULTILINE)
    chunks = []
    for section in sections:
        section = section.strip()
        if not section:
            continue
        header = ""
        lines = section.split("\n", 1)
        if lines[0].startswith("## "):
            header = lines[0].lstrip("# ").strip()
        chunks.append(SOPChunk(
            sop_id=sop_id,
            title=title,
            business_unit=business_unit,
            chunk_text=section,
            section=header,
        ))
    return chunks

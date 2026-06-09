#!/usr/bin/env python3
"""
Generate ~200 synthetic SOPs for Meridian Health Technologies using Nebius AI Studio (DeepSeek).

Usage:
    python3 scripts/generate_sops.py                    # Generate all SOPs
    python3 scripts/generate_sops.py --resume            # Skip already-generated files
    python3 scripts/generate_sops.py --concurrency 5     # Parallel API calls
    python3 scripts/generate_sops.py --dry-run           # Show what would be generated
    python3 scripts/generate_sops.py --sop SOP-AIML-001  # Generate a single SOP
"""

import argparse
import asyncio
import json
import os
import random
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from openai import AsyncOpenAI

from scripts.company_context import COMPANY_PROFILE
from scripts.sop_taxonomy import build_taxonomy

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
SOPS_DIR = DATA_DIR / "sops"

NEBIUS_BASE_URL = "https://api.tokenfactory.nebius.com/v1/"
MODEL = "deepseek-ai/DeepSeek-V4-Pro"
MAX_TOKENS = 16000

# Nebius pricing for DeepSeek-V3 (per 1M tokens)
INPUT_PRICE_PER_M = 0.30
OUTPUT_PRICE_PER_M = 0.60


def sop_filename(sop: dict) -> str:
    slug = sop["title"].lower()
    for ch in "/'&—–(),.":
        slug = slug.replace(ch, "")
    slug = slug.replace(" ", "_")
    slug = slug.replace("__", "_")
    return f"{sop['sop_id'].lower().replace('-', '_')}_{slug}.md"


def sop_filepath(sop: dict) -> Path:
    return SOPS_DIR / sop["dir"] / sop_filename(sop)


def build_version() -> str:
    major = random.choice([1, 2, 3, 4, 5])
    minor = random.randint(0, 9)
    return f"{major}.{minor}"


def build_dates() -> tuple[str, str, str]:
    year = random.choice([2024, 2025])
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    effective = f"{year}-{month:02d}-{day:02d}"

    review_year = 2025 if year == 2024 else 2026
    review_month = random.randint(1, 12)
    last_reviewed = f"{review_year}-{review_month:02d}-{random.randint(1, 28):02d}"

    next_month = review_month + 6
    next_year = review_year
    if next_month > 12:
        next_month -= 12
        next_year += 1
    next_review = f"{next_year}-{next_month:02d}-{random.randint(1, 28):02d}"

    return effective, last_reviewed, next_review


def build_prompt(sop: dict) -> str:
    effective, last_reviewed, next_review = build_dates()
    version = build_version()

    compliance_instructions = []
    for reg, level in sop["compliance_profile"].items():
        if level == "compliant":
            compliance_instructions.append(
                f"- {reg}: Write THOROUGH coverage. Reference specific articles/sections. "
                f"Include detailed controls, named roles, measurable metrics, and clear timelines."
            )
        elif level == "partial":
            weaknesses = sop["weaknesses"].get(reg, [])
            weakness_text = "; ".join(weaknesses)
            compliance_instructions.append(
                f"- {reg}: Write PARTIAL coverage. Address the topic but introduce these specific "
                f"weaknesses naturally (do NOT call them out as weaknesses — just write the "
                f"policy that way): {weakness_text}"
            )
        else:
            weaknesses = sop["weaknesses"].get(reg, [])
            weakness_text = "; ".join(weaknesses)
            compliance_instructions.append(
                f"- {reg}: Write with SIGNIFICANT GAPS. The policy should have notable omissions: "
                f"{weakness_text}. Do NOT mention these regulations or acknowledge the gaps — "
                f"simply omit the relevant content."
            )

    compliance_section = "\n".join(compliance_instructions)

    frontmatter = f"""---
sop_id: "{sop['sop_id']}"
title: "{sop['title']}"
business_unit: "{sop['business_unit']}"
version: "{version}"
effective_date: "{effective}"
last_reviewed: "{last_reviewed}"
next_review: "{next_review}"
owner: "{sop['owner']}"
approver: "{sop['approver']}"
classification: "Internal"
regulations:
{chr(10).join(f'  - "{r}"' for r in sop['regulations'])}
status: "Active"
---"""

    prompt = f"""You are a corporate policy writer for Meridian Health Technologies, Inc.
Write a detailed Standard Operating Procedure (SOP) document.

COMPANY CONTEXT:
{COMPANY_PROFILE}

DOCUMENT METADATA (include this exact YAML frontmatter at the top):
{frontmatter}

SOP DETAILS:
- Title: {sop['title']}
- Business Unit: {sop['business_unit']}
- Key Topics to Cover: {', '.join(sop['key_topics'])}
- Target Length: approximately {sop['target_pages']} pages (~{sop['target_pages'] * 500} words)

REGULATORY COVERAGE INSTRUCTIONS (CRITICAL — follow precisely):
{compliance_section}

DOCUMENT STRUCTURE:
Write the SOP with these sections (use ## for section headers):

1. **Purpose and Scope** — Why this SOP exists, what it covers, who it applies to
2. **Definitions and Acronyms** — Key terms used in the document
3. **Roles and Responsibilities** — RACI or similar responsibility matrix with specific named roles
4. **Policy Statements** — High-level policy commitments
5. **Detailed Procedures** — Step-by-step operational procedures (this should be the longest section, with sub-sections using ### headers)
6. **Controls and Safeguards** — Specific technical and administrative controls
7. **Monitoring, Metrics, and Reporting** — KPIs, dashboards, reporting cadence
8. **Exception Handling and Escalation** — How to handle deviations, who approves exceptions
9. **Training Requirements** — What training is needed, frequency, tracking
10. **Related Policies and References** — Cross-references to other Meridian SOPs and external standards
11. **Revision History** — Table of version history (include 3-5 plausible revisions)

STYLE GUIDELINES:
- Write in formal corporate policy language
- Use specific, actionable language (not vague aspirational statements) for compliant sections
- Include realistic procedure steps, forms, templates where appropriate
- Reference specific Meridian systems, tools, and organizational roles from the company context
- Use tables and bullet lists extensively
- Include specific SLAs, timelines, and quantitative thresholds where appropriate
- Reference other Meridian SOPs by their SOP-ID when mentioning related policies
- Make the document feel like a real enterprise policy that has been through several review cycles

Begin with the YAML frontmatter, then write the full SOP document."""

    return prompt


async def generate_single_sop(
    client: AsyncOpenAI,
    sop: dict,
    semaphore: asyncio.Semaphore,
    resume: bool = False,
) -> dict:
    filepath = sop_filepath(sop)

    if resume and filepath.exists() and filepath.stat().st_size > 1000:
        return {"sop_id": sop["sop_id"], "status": "skipped", "tokens": 0, "filepath": str(filepath)}

    async with semaphore:
        prompt = build_prompt(sop)
        start = time.time()

        try:
            response = await client.chat.completions.create(
                model=MODEL,
                max_tokens=MAX_TOKENS,
                messages=[{"role": "user", "content": prompt}],
            )

            content = response.choices[0].message.content
            elapsed = time.time() - start
            input_tokens = response.usage.prompt_tokens
            output_tokens = response.usage.completion_tokens

            filepath.parent.mkdir(parents=True, exist_ok=True)
            filepath.write_text(content, encoding="utf-8")

            return {
                "sop_id": sop["sop_id"],
                "status": "generated",
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "elapsed": round(elapsed, 1),
                "filepath": str(filepath),
                "words": len(content.split()),
            }

        except Exception as e:
            return {
                "sop_id": sop["sop_id"],
                "status": "error",
                "error": str(e),
                "filepath": str(filepath),
            }


def generate_compliance_matrix(taxonomy: list[dict]) -> None:
    matrix = []
    for sop in taxonomy:
        for reg, level in sop["compliance_profile"].items():
            entry = {
                "sop_id": sop["sop_id"],
                "title": sop["title"],
                "business_unit": sop["business_unit"],
                "regulation": reg,
                "compliance_level": level,
                "weaknesses": sop["weaknesses"].get(reg, []),
            }
            matrix.append(entry)

    output_path = DATA_DIR / "compliance_matrix.json"
    output_path.write_text(json.dumps(matrix, indent=2), encoding="utf-8")
    print(f"\nCompliance matrix written: {output_path}")
    print(f"  Total audit cells: {len(matrix)}")

    from collections import Counter
    levels = Counter(e["compliance_level"] for e in matrix)
    for level, count in sorted(levels.items()):
        print(f"  {level}: {count} ({100*count/len(matrix):.1f}%)")


async def main():
    parser = argparse.ArgumentParser(description="Generate synthetic SOPs for Sentinel Agent")
    parser.add_argument("--resume", action="store_true", help="Skip already-generated files")
    parser.add_argument("--concurrency", type=int, default=5, help="Max parallel API calls")
    parser.add_argument("--dry-run", action="store_true", help="Show plan without generating")
    parser.add_argument("--sop", type=str, help="Generate a single SOP by ID")
    parser.add_argument("--matrix-only", action="store_true", help="Only generate compliance matrix")
    args = parser.parse_args()

    taxonomy = build_taxonomy()

    if args.matrix_only:
        generate_compliance_matrix(taxonomy)
        return

    if args.sop:
        taxonomy = [s for s in taxonomy if s["sop_id"] == args.sop]
        if not taxonomy:
            print(f"SOP {args.sop} not found")
            sys.exit(1)

    if args.dry_run:
        print(f"Would generate {len(taxonomy)} SOPs:")
        for sop in taxonomy:
            fp = sop_filepath(sop)
            exists = fp.exists()
            skip = "(SKIP - exists)" if exists and args.resume else ""
            print(f"  {sop['sop_id']}: {sop['title']} -> {fp.name} {skip}")
        total_pages = sum(s["target_pages"] for s in taxonomy)
        print(f"\nTotal target pages: {total_pages}")
        est_input = len(taxonomy) * 3000
        est_output = len(taxonomy) * 15000
        est_cost = est_input * INPUT_PRICE_PER_M / 1e6 + est_output * OUTPUT_PRICE_PER_M / 1e6
        print(f"Estimated cost: ~${est_cost:.2f} (Nebius DeepSeek-V3)")
        return

    api_key = os.environ.get("NEBIUS_API_KEY")
    if not api_key:
        print("ERROR: Set NEBIUS_API_KEY environment variable")
        sys.exit(1)

    client = AsyncOpenAI(base_url=NEBIUS_BASE_URL, api_key=api_key)
    semaphore = asyncio.Semaphore(args.concurrency)

    print(f"Generating {len(taxonomy)} SOPs with concurrency={args.concurrency}")
    print(f"Model: {MODEL}")
    print(f"Endpoint: {NEBIUS_BASE_URL}")
    print(f"Output: {SOPS_DIR}")
    print()

    start_time = time.time()
    tasks = [generate_single_sop(client, sop, semaphore, args.resume) for sop in taxonomy]

    total_input = 0
    total_output = 0
    total_words = 0
    generated = 0
    skipped = 0
    errors = 0

    for coro in asyncio.as_completed(tasks):
        result = await coro
        sop_id = result["sop_id"]

        if result["status"] == "generated":
            generated += 1
            total_input += result.get("input_tokens", 0)
            total_output += result.get("output_tokens", 0)
            total_words += result.get("words", 0)
            print(
                f"  [{generated + skipped + errors}/{len(taxonomy)}] "
                f"{sop_id}: {result.get('words', 0)} words, "
                f"{result.get('elapsed', 0)}s"
            )
        elif result["status"] == "skipped":
            skipped += 1
            print(f"  [{generated + skipped + errors}/{len(taxonomy)}] {sop_id}: skipped (exists)")
        else:
            errors += 1
            print(f"  [{generated + skipped + errors}/{len(taxonomy)}] {sop_id}: ERROR - {result.get('error', 'unknown')}")

    elapsed = time.time() - start_time

    print(f"\n{'='*60}")
    print(f"Generation complete in {elapsed:.0f}s")
    print(f"  Generated: {generated}")
    print(f"  Skipped:   {skipped}")
    print(f"  Errors:    {errors}")
    print(f"  Total words: {total_words:,} (~{total_words // 500:,} pages)")
    print(f"  Input tokens:  {total_input:,}")
    print(f"  Output tokens: {total_output:,}")

    input_cost = total_input * INPUT_PRICE_PER_M / 1e6
    output_cost = total_output * OUTPUT_PRICE_PER_M / 1e6
    print(f"  Estimated cost: ${input_cost + output_cost:.2f} (input: ${input_cost:.2f}, output: ${output_cost:.2f})")

    generate_compliance_matrix(taxonomy)

    if errors > 0:
        print(f"\n{errors} SOPs failed. Re-run with --resume to retry only failed/missing SOPs.")


if __name__ == "__main__":
    asyncio.run(main())

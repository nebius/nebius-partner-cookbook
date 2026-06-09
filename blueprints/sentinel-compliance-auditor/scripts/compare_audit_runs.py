#!/usr/bin/env python3
"""Compare full audit runs from LangSmith by quality, cost, tokens, latency, and tool calls.

Usage:
    python scripts/compare_audit_runs.py <run_id1> <run_id2> ...
    python scripts/compare_audit_runs.py --json   # output as JSON

Example:
    python scripts/compare_audit_runs.py 019e7a83-... 019e7a42-... 019e73ea-...
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.validate_run import (
    PRICING,
    fetch_run_data,
    parse_run_stats,
    parse_full_findings,
    load_ground_truth,
    compute_metrics,
    macro_f1_for,
    worst_level,
)


def fetch_tool_calls(run_id: str) -> dict:
    """Count tool calls by name from the LangSmith trace."""
    from dotenv import load_dotenv
    load_dotenv()
    from langsmith import Client
    client = Client()

    tool_runs = list(client.list_runs(
        project_name="sentinel-agent",
        trace_id=run_id,
        run_type="tool",
    ))
    counts: dict[str, int] = {}
    for r in tool_runs:
        name = r.name or "unknown"
        counts[name] = counts.get(name, 0) + 1
    return counts


def analyze_run(run_id: str) -> dict:
    """Fetch and analyze a single audit run."""
    print(f"\n--- Fetching run {run_id[:12]}… ---")
    run_data = fetch_run_data(run_id)
    stats = parse_run_stats(run_data["content"], run_data)

    gt = load_ground_truth(revised=True)
    findings, total_parsed, failed_sops, error_sops = parse_full_findings(run_data["content"])
    predicted = {}
    for (sop, reg), levels in findings.items():
        predicted[(sop, reg)] = worst_level(levels)
    quality = compute_metrics(gt, predicted)
    f1 = macro_f1_for(quality["confusion"])

    print(f"  Fetching tool calls…")
    tool_calls = fetch_tool_calls(run_id)

    return {
        "run_id": run_id,
        "label": run_data["label"],
        "model": stats["model"],
        "input_tokens": stats["input_tokens"],
        "output_tokens": stats["output_tokens"],
        "total_tokens": stats["total_tokens"],
        "outer_tokens": stats.get("outer_tokens", 0),
        "sub_tokens": stats.get("sub_tokens", 0),
        "cost": stats["cost"],
        "latency_s": stats["latency"],
        "tool_calls": tool_calls,
        "total_tool_calls": sum(tool_calls.values()),
        "sops_audited": total_parsed,
        "failed_sops": len(failed_sops),
        "error_sops": len(error_sops),
        "quality": {
            "matched": quality["matched"],
            "total": quality["total"],
            "accuracy": quality["matched"] / quality["total"] if quality["total"] else 0,
            "false_positives": quality["false_positives"],
            "false_negatives": quality["false_negatives"],
            "macro_f1": f1,
            "missing": len(quality["missing_in_run"]),
            "extra": quality["extra_in_run"],
        },
    }


def print_comparison(runs: list[dict]):
    """Print a side-by-side comparison table."""
    col = 18

    def fmt(v, width=col):
        s = str(v)
        return s.rjust(width)

    labels = [r["model"].split("/")[-1][:16] for r in runs]
    header = "".ljust(24) + "".join(l.rjust(col) for l in labels)
    sep = "-" * len(header)

    print(f"\n{'=' * len(header)}")
    print("FULL AUDIT RUN COMPARISON")
    print(f"{'=' * len(header)}")
    print(header)
    print(sep)

    # Tokens
    print("TOKENS")
    print("  Input".ljust(24) + "".join(fmt(f"{r['input_tokens']:,}") for r in runs))
    print("  Output".ljust(24) + "".join(fmt(f"{r['output_tokens']:,}") for r in runs))
    print("  Total".ljust(24) + "".join(fmt(f"{r['total_tokens']:,}") for r in runs))
    print("  Outer agent".ljust(24) + "".join(fmt(f"{r['outer_tokens']:,}") for r in runs))
    print("  Sub-agents".ljust(24) + "".join(fmt(f"{r['sub_tokens']:,}") for r in runs))
    print(sep)

    # Cost
    print("COST")
    print("  Total".ljust(24) + "".join(fmt(f"${r['cost']:.2f}") for r in runs))
    prices = [PRICING.get(r["model"], {}) for r in runs]
    print("  $/1M in".ljust(24) + "".join(fmt(f"${p.get('input', 0):.2f}") for p in prices))
    print("  $/1M out".ljust(24) + "".join(fmt(f"${p.get('output', 0):.2f}") for p in prices))
    print(sep)

    # Latency
    print("LATENCY")
    print("  Wall time".ljust(24) + "".join(fmt(f"{r['latency_s']:.0f}s" if r['latency_s'] else "—") for r in runs))
    print("  Minutes".ljust(24) + "".join(fmt(f"{r['latency_s']/60:.1f}m" if r['latency_s'] else "—") for r in runs))
    print(sep)

    # Tool calls
    print("TOOL CALLS")
    print("  Total".ljust(24) + "".join(fmt(f"{r['total_tool_calls']:,}") for r in runs))
    all_tools = sorted(set().union(*(r["tool_calls"].keys() for r in runs)))
    for t in all_tools:
        print(f"  {t[:22]}".ljust(24) + "".join(fmt(str(r["tool_calls"].get(t, 0))) for r in runs))
    print(sep)

    # Quality
    print("QUALITY (vs revised compliance matrix)")
    q = [r["quality"] for r in runs]
    print("  Matched".ljust(24) + "".join(fmt(f"{x['matched']}/{x['total']}") for x in q))
    print("  Accuracy".ljust(24) + "".join(fmt(f"{x['accuracy']:.3f}") for x in q))
    print("  Macro F1".ljust(24) + "".join(fmt(f"{x['macro_f1']:.3f}") for x in q))
    print("  False pos (strict)".ljust(24) + "".join(fmt(str(x["false_positives"])) for x in q))
    print("  False neg (lenient)".ljust(24) + "".join(fmt(str(x["false_negatives"])) for x in q))
    print("  Missing (no finding)".ljust(24) + "".join(fmt(str(x["missing"])) for x in q))
    print("  Failed SOPs".ljust(24) + "".join(fmt(str(r["failed_sops"])) for r in runs))
    print("  Error SOPs".ljust(24) + "".join(fmt(str(r["error_sops"])) for r in runs))
    print(sep)

    # Summary ranking
    print("\nRANKING")
    by_f1 = sorted(runs, key=lambda r: r["quality"]["macro_f1"], reverse=True)
    by_cost = sorted(runs, key=lambda r: r["cost"])
    by_latency = sorted(runs, key=lambda r: r["latency_s"] or float("inf"))
    print(f"  Best quality:  {by_f1[0]['model'].split('/')[-1]} (F1={by_f1[0]['quality']['macro_f1']:.3f})")
    print(f"  Cheapest:      {by_cost[0]['model'].split('/')[-1]} (${by_cost[0]['cost']:.2f})")
    print(f"  Fastest:       {by_latency[0]['model'].split('/')[-1]} ({by_latency[0]['latency_s']:.0f}s)")


def main():
    ap = argparse.ArgumentParser(description="Compare full audit runs from LangSmith")
    ap.add_argument("run_ids", nargs="+", help="LangSmith run IDs")
    ap.add_argument("--json", action="store_true", help="Output as JSON")
    args = ap.parse_args()

    runs = []
    for rid in args.run_ids:
        rid = rid.strip().split("/r/")[-1].split("?")[0]
        runs.append(analyze_run(rid))

    if args.json:
        print(json.dumps(runs, indent=2, default=str))
    else:
        print_comparison(runs)


if __name__ == "__main__":
    main()

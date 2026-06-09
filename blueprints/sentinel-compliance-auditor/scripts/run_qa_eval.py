#!/usr/bin/env python3
"""Run the Q&A eval over `data/eval/qa_dataset.jsonl`.

Usage:
    python scripts/run_qa_eval.py --mode both                    # naive + optimized (Nebius DeepSeek)
    python scripts/run_qa_eval.py --mode all                     # all modes
    python scripts/run_qa_eval.py --mode naive --limit 5         # 5 questions, naive only
    python scripts/run_qa_eval.py --mode prototype               # GPT-5.5, no Tavily
    python scripts/run_qa_eval.py --mode grounded                # GPT-5.5 + Tavily
    python scripts/run_qa_eval.py --mode optimized               # DeepSeek-V4-Pro + Tavily
    python scripts/run_qa_eval.py --mode production              # Nemotron Ultra + Tavily
    python scripts/run_qa_eval.py --mode optimized --category sop_compliance
    python scripts/run_qa_eval.py --mode both --no-judge         # skip LLM-as-judge
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import sys
import threading
import traceback
from collections import defaultdict
from pathlib import Path

# Allow `python scripts/run_qa_eval.py` from repo root without `pip install -e .`.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from sentinel.eval.metrics import (
    binary_compliance_metrics,
    compute_metrics,
    estimate_cost,
    extract_compliance_level,
    macro_f1,
    normalize_level,
    to_binary_level,
)

DATASET_PATH = Path("data/eval/qa_dataset.jsonl")
RESULTS_DIR = Path("data/eval/results")

JUDGE_CATEGORIES = {
    "factual_single_hop",
    "multi_regulation",
    "edition_aware",
    "web_grounded",
    "negation_gap",
}
COMPLIANCE_CATEGORIES = {"sop_compliance"}


def load_dataset(path: Path) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    rows = []
    with path.open() as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line or line.startswith("//"):
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise ValueError(f"{path}:{i} invalid JSON — {e}") from e
    return rows


def filter_dataset(rows: list[dict], category: str | None, limit: int | None) -> list[dict]:
    if category:
        rows = [r for r in rows if r.get("category") == category]
    if limit is not None:
        rows = rows[:limit]
    return rows


def run_single(mode: str, question: dict) -> dict:
    """Dispatch one question through the requested baseline."""
    sop_id = question.get("sop_id") or None
    if mode == "naive":
        from sentinel.eval.naive_rag import naive_rag_answer
        return naive_rag_answer(question["question"], sop_id=sop_id)
    if mode == "prototype":
        from sentinel.eval.agentic_qa import agentic_qa_answer
        return agentic_qa_answer(question["question"], sop_id=sop_id, provider="openai", use_tavily=False)
    if mode == "grounded":
        from sentinel.eval.agentic_qa import agentic_qa_answer
        return agentic_qa_answer(question["question"], sop_id=sop_id, provider="openai", use_tavily=True)
    if mode == "optimized":
        from sentinel.eval.agentic_qa import agentic_qa_answer
        return agentic_qa_answer(question["question"], sop_id=sop_id, provider="nebius")
    if mode == "production":
        from sentinel.eval.agentic_qa import agentic_qa_answer
        from sentinel.config import NEBIUS_MODELS
        return agentic_qa_answer(question["question"], sop_id=sop_id, provider="nebius", model_name=NEBIUS_MODELS["nemotron"])
    raise ValueError(f"unknown mode: {mode}")


def score_row(question: dict, output: dict, run_judge: bool) -> dict:
    """Attach scores to a single answer."""
    category = question.get("category", "")
    scores: dict = {"category": category}

    if category in COMPLIANCE_CATEGORIES and question.get("expected_compliance_level"):
        predicted = extract_compliance_level(output.get("answer", ""))
        scores["expected_level"] = normalize_level(question["expected_compliance_level"])
        scores["predicted_level"] = predicted
        scores["level_match"] = predicted == scores["expected_level"] if predicted else False
        # Binary view (compliant vs non_compliant) is the headline metric.
        scores["expected_binary"] = to_binary_level(scores["expected_level"])
        scores["predicted_binary"] = to_binary_level(predicted) if predicted else None
        scores["binary_match"] = (
            scores["predicted_binary"] == scores["expected_binary"]
            if scores["predicted_binary"] else False
        )

    if run_judge and category in JUDGE_CATEGORIES:
        try:
            from sentinel.eval.judge import judge_answer
            j = judge_answer(
                question=question["question"],
                reference=question.get("expected_answer", ""),
                citations=question.get("expected_citations", []) or [],
                candidate=output.get("answer", ""),
            )
            scores["judge_correctness"] = j["correctness"]
            scores["judge_citations"] = j["citations"]
            scores["judge_rationale"] = j["rationale"]
            scores["judge_input_tokens"] = j["input_tokens"]
            scores["judge_output_tokens"] = j["output_tokens"]
        except Exception as e:
            scores["judge_error"] = f"{type(e).__name__}: {e}"

    return scores


def _process_one(mode: str, q: dict, run_judge: bool, print_lock: threading.Lock) -> dict:
    qid = q.get("id", "?")
    with print_lock:
        print(f"  [{mode}] {qid} ({q.get('category', '?')}) …", flush=True)
    try:
        output = run_single(mode, q)
        error = None
        if output.get("incomplete"):
            with print_lock:
                print(f"    INCOMPLETE [{qid}]: empty or truncated answer (finish_reason={output.get('finish_reason', '?')})", file=sys.stderr)
    except Exception as e:
        output = {"answer": "", "input_tokens": 0, "output_tokens": 0, "latency_s": 0.0, "model": "", "mode": mode}
        error = f"{type(e).__name__}: {e}\n{traceback.format_exc()}"
        with print_lock:
            print(f"    ERROR [{qid}]: {error.splitlines()[0]}", file=sys.stderr)

    scores = score_row(q, output, run_judge) if error is None else {"category": q.get("category", ""), "error": error}
    return {"question": q, "output": output, "scores": scores, "error": error}


def run_mode(mode: str, dataset: list[dict], run_judge: bool, workers: int = 1) -> dict:
    """Run all questions through one baseline and aggregate scoring.

    Each question is independent, so we thread-pool the question loop to
    keep wall time bounded.
    """
    print_lock = threading.Lock()
    if workers <= 1:
        rows = [_process_one(mode, q, run_judge, print_lock) for q in dataset]
    else:
        # Preserve dataset order in output for easy diffing across runs.
        results: list[dict | None] = [None] * len(dataset)
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {pool.submit(_process_one, mode, q, run_judge, print_lock): idx for idx, q in enumerate(dataset)}
            for fut in concurrent.futures.as_completed(futures):
                idx = futures[fut]
                results[idx] = fut.result()
        rows = [r for r in results if r is not None]

    return aggregate(mode, rows)


def aggregate(mode: str, rows: list[dict]) -> dict:
    """Roll up per-category accuracy, F1, tokens, cost, latency."""
    total = len(rows)
    failed = sum(1 for r in rows if r["error"])
    incomplete = sum(1 for r in rows if r["output"].get("incomplete"))
    in_tokens = sum(r["output"].get("input_tokens", 0) for r in rows)
    out_tokens = sum(r["output"].get("output_tokens", 0) for r in rows)
    judge_in = sum(r["scores"].get("judge_input_tokens", 0) for r in rows)
    judge_out = sum(r["scores"].get("judge_output_tokens", 0) for r in rows)
    latency_total = sum(r["output"].get("latency_s", 0.0) for r in rows)

    model = next((r["output"].get("model") for r in rows if r["output"].get("model")), "")
    answer_cost = estimate_cost(model, in_tokens, out_tokens)
    judge_cost = estimate_cost(model, judge_in, judge_out)

    # Compliance scoring for sop_compliance questions — both binary (primary) and 3-class (secondary).
    gt: dict = {}
    pred: dict = {}
    for r in rows:
        s = r["scores"]
        if "expected_level" in s and s.get("predicted_level"):
            key = r["question"].get("id", "")
            gt[key] = s["expected_level"]
            pred[key] = s["predicted_level"]
    m = compute_metrics(gt, pred) if gt else None
    f1 = macro_f1(m["confusion"]) if m else None
    binary_m = binary_compliance_metrics(gt, pred) if gt else None

    # Per-category aggregates.
    by_cat: dict = defaultdict(lambda: {
        "n": 0, "judge_correct_avg": [], "judge_cite_avg": [],
        "level_correct": 0, "level_total": 0,
        "binary_correct": 0, "binary_total": 0,
    })
    for r in rows:
        s = r["scores"]
        cat = s.get("category", "uncategorized")
        bucket = by_cat[cat]
        bucket["n"] += 1
        if s.get("judge_correctness", -1) >= 0:
            bucket["judge_correct_avg"].append(s["judge_correctness"])
            bucket["judge_cite_avg"].append(s["judge_citations"])
        if "expected_level" in s and s.get("predicted_level"):
            bucket["level_total"] += 1
            if s.get("level_match"):
                bucket["level_correct"] += 1
        if s.get("expected_binary") and s.get("predicted_binary"):
            bucket["binary_total"] += 1
            if s.get("binary_match"):
                bucket["binary_correct"] += 1

    per_category = {}
    for cat, b in by_cat.items():
        per_category[cat] = {
            "n": b["n"],
            "judge_correctness_avg": (sum(b["judge_correct_avg"]) / len(b["judge_correct_avg"])) if b["judge_correct_avg"] else None,
            "judge_citations_avg": (sum(b["judge_cite_avg"]) / len(b["judge_cite_avg"])) if b["judge_cite_avg"] else None,
            "binary_accuracy": (b["binary_correct"] / b["binary_total"]) if b["binary_total"] else None,
            "binary_total": b["binary_total"],
            "level_accuracy_3class": (b["level_correct"] / b["level_total"]) if b["level_total"] else None,
            "level_total": b["level_total"],
        }

    return {
        "mode": mode,
        "model": model,
        "total": total,
        "failed": failed,
        "incomplete": incomplete,
        "input_tokens": in_tokens,
        "output_tokens": out_tokens,
        "judge_input_tokens": judge_in,
        "judge_output_tokens": judge_out,
        "answer_cost_usd": round(answer_cost, 4),
        "judge_cost_usd": round(judge_cost, 4),
        "total_cost_usd": round(answer_cost + judge_cost, 4),
        "latency_total_s": round(latency_total, 1),
        "latency_avg_s": round(latency_total / total, 1) if total else 0,
        "compliance_binary": binary_m and {
            "n": binary_m["n"],
            "matched": binary_m["matched"],
            "accuracy": round(binary_m["accuracy"], 3),
            "recall_non_compliant": round(binary_m["recall_non_compliant"], 3),
            "precision_non_compliant": round(binary_m["precision_non_compliant"], 3),
            "f1_non_compliant": round(binary_m["f1_non_compliant"], 3),
            "recall_compliant": round(binary_m["recall_compliant"], 3),
            "precision_compliant": round(binary_m["precision_compliant"], 3),
            "f1_compliant": round(binary_m["f1_compliant"], 3),
            "macro_f1": round(binary_m["macro_f1"], 3),
            "tp_non_compliant": binary_m["tp_non_compliant"],
            "fp_non_compliant": binary_m["fp_non_compliant"],
            "tn_compliant": binary_m["tn_compliant"],
            "fn_non_compliant": binary_m["fn_non_compliant"],
            "mismatches": binary_m["mismatches"],
        },
        "compliance_3class": m and {
            "matched": m["matched"],
            "total": m["total"],
            "false_positives": m["false_positives"],
            "false_negatives": m["false_negatives"],
            "macro_f1": round(f1, 3) if f1 is not None else None,
            "mismatches": m["mismatches"],
        },
        "per_category": per_category,
        "rows": rows,
    }


def write_results(payload: dict, out_dir: Path, label: str, timestamp: str) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{label}_{timestamp}.json"
    with path.open("w") as f:
        json.dump(payload, f, indent=2, default=str)
    return path


def print_summary(payload: dict) -> None:
    mode = payload["mode"]
    print(f"\n=== {mode.upper()} ===")
    print(f"  Model:       {payload['model']}")
    print(f"  Total:       {payload['total']}   Failed: {payload['failed']}   Incomplete: {payload.get('incomplete', 0)}")
    print(f"  Tokens:      {payload['input_tokens']:,} in / {payload['output_tokens']:,} out")
    print(f"  Cost:        ${payload['total_cost_usd']:.3f} (answers: ${payload['answer_cost_usd']:.3f}, judge: ${payload['judge_cost_usd']:.3f})")
    print(f"  Latency:     {payload['latency_total_s']:.1f}s total, {payload['latency_avg_s']:.1f}s avg")
    cb = payload.get("compliance_binary")
    if cb:
        print(
            f"  Compliance (binary): {cb['matched']}/{cb['n']} matched   "
            f"acc {cb['accuracy']:.3f}   macro F1 {cb['macro_f1']:.3f}"
        )
        print(
            f"     non-compliant recall {cb['recall_non_compliant']:.3f} "
            f"(catches {cb['tp_non_compliant']} of {cb['tp_non_compliant']+cb['fn_non_compliant']} real issues)   "
            f"precision {cb['precision_non_compliant']:.3f}"
        )
    c3 = payload.get("compliance_3class")
    if c3:
        print(
            f"  Compliance (3-class): {c3['matched']}/{c3['total']} matched   "
            f"FP {c3['false_positives']} / FN {c3['false_negatives']}   macro F1 {c3['macro_f1']}"
        )
    print("  Per category:")
    for cat, c in sorted(payload["per_category"].items()):
        bits = [f"n={c['n']}"]
        if c["judge_correctness_avg"] is not None:
            bits.append(f"correct={c['judge_correctness_avg']:.2f}/2")
        if c["judge_citations_avg"] is not None:
            bits.append(f"cite={c['judge_citations_avg']:.2f}/2")
        if c.get("binary_accuracy") is not None:
            bits.append(f"binary_acc={c['binary_accuracy']:.2f} ({c['binary_total']})")
        if c.get("level_accuracy_3class") is not None:
            bits.append(f"3class_acc={c['level_accuracy_3class']:.2f}")
        print(f"    {cat:<22} {' | '.join(bits)}")


_MODE_LABEL = {
    "naive": "naive",
    "prototype": "proto",
    "grounded": "ground",
    "optimized": "optim",
    "production": "prod",
}
_COL = 13  # column width in the comparison table


def print_comparison(summaries: dict[str, dict]) -> None:
    """Print an N-mode comparison table — works for 2 or 3+ modes."""
    def fmt(d, k):
        v = d.get(k)
        return f"{v:.2f}" if isinstance(v, (int, float)) else "—"

    modes = list(summaries.keys())
    header = "=== " + " vs ".join(m.upper() for m in modes) + " ==="
    print(f"\n{header}")

    cats = sorted(set().union(*(s["per_category"].keys() for s in summaries.values())))
    abbr = [_MODE_LABEL.get(m, m[:7]) for m in modes]

    # Correctness row
    cols = "".join(f"{a + '_corr':>{_COL}}" for a in abbr)
    print(f"{'category':<22}{cols}")
    for cat in cats:
        row = f"{cat:<22}"
        for m in modes:
            row += f"{fmt(summaries[m]['per_category'].get(cat, {}), 'judge_correctness_avg'):>{_COL}}"
        print(row)

    # Citation row
    print()
    cols = "".join(f"{a + '_cite':>{_COL}}" for a in abbr)
    print(f"{'category':<22}{cols}")
    for cat in cats:
        row = f"{cat:<22}"
        for m in modes:
            row += f"{fmt(summaries[m]['per_category'].get(cat, {}), 'judge_citations_avg'):>{_COL}}"
        print(row)

    # Binary compliance row (only sop_compliance has it)
    has_compliance = any(s.get("compliance_binary") for s in summaries.values())
    if has_compliance:
        print(f"\n  Binary compliance metric (compliant vs non-compliant):")
        for m in modes:
            cb = summaries[m].get("compliance_binary") or {}
            if cb:
                print(f"    {m:<16} acc {cb['accuracy']:.3f}   non-comp recall {cb['recall_non_compliant']:.3f}   macro F1 {cb['macro_f1']:.3f}")

    # Cost / latency table
    print(f"\n  Cost / latency:")
    print(f"    {'mode':<18}{'cost':>10}{'wall (min)':>14}{'avg (s)':>10}")
    for m in modes:
        s = summaries[m]
        print(f"    {m:<18}${s['total_cost_usd']:>9.2f}{s['latency_total_s']/60:>14.1f}{s['latency_avg_s']:>10.1f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--mode",
        choices=["naive", "prototype", "grounded", "optimized", "production", "both", "all"],
        default="both",
        help="Single mode, or 'both' (naive+optimized) / 'all' (all five modes).",
    )
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--category", default=None)
    ap.add_argument("--dataset", default=str(DATASET_PATH))
    ap.add_argument("--results-dir", default=str(RESULTS_DIR))
    ap.add_argument("--no-judge", action="store_true", help="Skip LLM-as-judge scoring (faster, no judge cost).")
    ap.add_argument("--workers", type=int, default=5, help="Parallel workers per mode (default 5).")
    args = ap.parse_args()

    dataset_path = Path(args.dataset)
    results_dir = Path(args.results_dir)
    rows = filter_dataset(load_dataset(dataset_path), args.category, args.limit)
    if not rows:
        print(f"No rows after filtering ({args.dataset}, category={args.category}, limit={args.limit})", file=sys.stderr)
        sys.exit(1)
    print(f"Loaded {len(rows)} question(s) from {dataset_path}")

    timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    run_judge = not args.no_judge
    if args.mode == "both":
        modes = ["naive", "optimized"]
    elif args.mode == "all":
        modes = ["naive", "prototype", "grounded", "optimized", "production"]
    else:
        modes = [args.mode]

    summaries = {}
    for mode in modes:
        print(f"\n--- Running {mode} ({len(rows)} questions, {args.workers} worker(s)) ---")
        summary = run_mode(mode, rows, run_judge, workers=args.workers)
        # Sanitize mode-name into a filesystem-safe label (agentic-openai → agentic_openai).
        file_label = mode.replace("-", "_")
        path = write_results(summary, results_dir, file_label, timestamp)
        print(f"  Wrote {path}")
        print_summary(summary)
        summaries[mode] = summary

    if len(summaries) >= 2:
        comparison = {
            "timestamp": timestamp,
            "dataset": str(dataset_path),
            "limit": args.limit,
            "category_filter": args.category,
            "modes": list(summaries.keys()),
            **{mode: {k: v for k, v in s.items() if k != "rows"} for mode, s in summaries.items()},
        }
        cmp_path = write_results(comparison, results_dir, "comparison", timestamp)
        print(f"\n  Wrote {cmp_path}")
        print_comparison(summaries)


if __name__ == "__main__":
    main()

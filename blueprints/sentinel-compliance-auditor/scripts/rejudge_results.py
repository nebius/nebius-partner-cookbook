#!/usr/bin/env python3
"""Re-run the LLM judge over existing eval result files — without re-running
the agents. The answers are the expensive part (~$110 for a 4-agent eval-all);
when only the judge was broken (e.g. the Kimi max_tokens bug) or swapped,
re-scoring the stored answers salvages them.

Usage:
    python3 scripts/rejudge_results.py data/eval/results/optimized_*.json
    python3 scripts/rejudge_results.py --workers 8 <files...>

Writes a new `<mode>_rejudged_<timestamp>.json` next to each input; the
original files are untouched.
"""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import sys
import threading
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from scripts.run_qa_eval import JUDGE_CATEGORIES, _run_config, aggregate  # noqa: E402
from sentinel.eval.judge import judge_answer  # noqa: E402


def rejudge_row(row: dict) -> bool:
    """Re-judge one row in place. Returns True if it was re-scored."""
    scores = row["scores"]
    if scores.get("category") not in JUDGE_CATEGORIES or row.get("error"):
        return False
    question = row["question"]
    j = judge_answer(
        question=question["question"],
        reference=question.get("expected_answer", ""),
        citations=question.get("expected_citations", []) or [],
        candidate=row["output"].get("answer", ""),
    )
    scores.pop("judge_error", None)
    scores["judge_correctness"] = j["correctness"]
    scores["judge_citations"] = j["citations"]
    scores["judge_rationale"] = j["rationale"]
    scores["judge_input_tokens"] = j["input_tokens"]
    scores["judge_output_tokens"] = j["output_tokens"]
    return True


def rejudge_file(path: Path, workers: int) -> Path:
    payload = json.loads(path.read_text())
    mode = payload["mode"]
    rows = payload["rows"]

    print(f"\n--- {path.name} ({mode}, {len(rows)} rows) ---")
    lock = threading.Lock()
    done = {"n": 0}

    def _one(row: dict) -> bool:
        ok = rejudge_row(row)
        if ok:
            with lock:
                done["n"] += 1
                if done["n"] % 20 == 0:
                    print(f"  judged {done['n']}…")
        return ok

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        results = list(pool.map(_one, rows))
    print(f"  re-judged {sum(results)} rows")

    rebuilt = aggregate(mode, rows)
    rebuilt["config"] = {**payload.get("config", {}), **_run_config(Path("data/eval/qa_dataset.jsonl")), "rejudged_from": path.name}

    unparseable = sum(
        1 for r in rows
        if r["scores"].get("category") in JUDGE_CATEGORIES and r["scores"].get("judge_correctness") == -1
    )
    if unparseable:
        print(f"  WARNING: {unparseable} judge verdicts still unparseable")

    timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    out = path.parent / f"{mode}_rejudged_{timestamp}.json"
    out.write_text(json.dumps(rebuilt, indent=2, default=str))
    print(f"  wrote {out}")
    return out


def main():
    ap = argparse.ArgumentParser(description="Re-judge stored eval results")
    ap.add_argument("files", nargs="+", help="result JSON files")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    from dotenv import load_dotenv
    load_dotenv()

    for f in args.files:
        rejudge_file(Path(f), args.workers)


if __name__ == "__main__":
    main()

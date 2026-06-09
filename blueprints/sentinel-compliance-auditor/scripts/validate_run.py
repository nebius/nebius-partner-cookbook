#!/usr/bin/env python3
"""
Validate a LangSmith run's audit findings against compliance_matrix.json.
Fetches run data from LangSmith, parses the audit_all_sops output,
aggregates per (SOP, regulation), and computes accuracy metrics.

Usage:
    python scripts/validate_run.py <run_id>                    # Single run
    python scripts/validate_run.py <run_id1> <run_id2>         # Compare two runs
    python scripts/validate_run.py --original <run_id>         # Use original matrix
"""
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from sentinel.config import PRICING
from sentinel.models import normalize_level
from sentinel.token_accounting import AUDIT_TOOL_NAMES, sum_sub_agent_tokens

MATRIX_PATH = Path("data/compliance_matrix.json")
REVISED_MATRIX_PATH = Path("data/compliance_matrix_revised.json")

LEVEL_ORDER = {"compliant": 0, "partial": 1, "gap": 2}


def _get_langsmith_client():
    from dotenv import load_dotenv
    load_dotenv()
    from langsmith import Client
    return Client()


def _find_audit_text(obj):
    """Recursively search for the audit output string in a nested structure."""
    if isinstance(obj, str) and "Audit complete" in obj and len(obj) > 1000:
        return obj
    elif isinstance(obj, dict):
        for v in obj.values():
            r = _find_audit_text(v)
            if r:
                return r
    elif isinstance(obj, list):
        for item in obj:
            r = _find_audit_text(item)
            if r:
                return r
    return None


def fetch_run_data(run_id: str) -> dict:
    """Fetch run metadata and audit content from LangSmith.

    Returns dict with keys: label, model, content, start_time, end_time,
    total_tokens, prompt_tokens, completion_tokens, total_cost.
    """
    client = _get_langsmith_client()
    root = client.read_run(run_id)

    meta = root.extra.get("metadata", {}) if root.extra else {}
    request_id = meta.get("langgraph_request_id", run_id[:8])

    # Get model name and total token usage from all LLM runs in the trace
    model = None
    trace_input_tokens = 0
    trace_output_tokens = 0
    print(f"  Fetching LLM runs for token totals...")
    llm_runs = list(client.list_runs(
        project_name="sentinel-agent",
        trace_id=run_id,
        run_type="llm",
    ))
    trace_cache_read = 0
    trace_cache_creation = 0
    for r in llm_runs:
        trace_input_tokens += r.prompt_tokens or 0
        trace_output_tokens += r.completion_tokens or 0
        if r.extra:
            usage = r.extra.get("usage", {})
            if isinstance(usage, dict):
                trace_cache_read += usage.get("cache_read_input_tokens", 0) or 0
                trace_cache_creation += usage.get("cache_creation_input_tokens", 0) or 0
    if llm_runs:
        llm_meta = llm_runs[0].extra.get("metadata", {}) if llm_runs[0].extra else {}
        model = llm_meta.get("ls_model_name")
    cache_note = ""
    if trace_cache_read or trace_cache_creation:
        cache_note = f" (cache read: {trace_cache_read:,}, cache creation: {trace_cache_creation:,})"
    print(f"  Found {len(llm_runs)} LLM runs, {trace_input_tokens + trace_output_tokens:,} total tokens{cache_note}")

    # Determine label
    model_short = (model or "unknown").split("/")[-1]
    label = f"{model_short} ({request_id[:8]})"

    # Collect every audit tool output in the trace. A run may make several
    # audit calls (audit_single_sop / audit_sops / audit_all_sops); each carries
    # its own token lines, so all must be gathered (not just the first).
    audit_outputs: list[str] = []
    tool_runs = list(client.list_runs(
        project_name="sentinel-agent",
        trace_id=run_id,
        run_type="tool",
    ))
    for tr in tool_runs:
        if tr.name not in AUDIT_TOOL_NAMES or not tr.outputs:
            continue
        text = _find_audit_text(tr.outputs)
        if not text:
            out_str = str(tr.outputs.get("output", ""))
            if "Audit complete" in out_str or "Sub-agent tokens" in out_str:
                text = out_str
        if text:
            audit_outputs.append(text)

    content = "\n\n".join(audit_outputs) if audit_outputs else None

    # Fallback: search root run outputs
    if not content and root.outputs:
        content = _find_audit_text(root.outputs)
        if content:
            audit_outputs = [content]

    # Fallback: search Prompt chain runs (for pending root runs)
    if not content:
        chain_runs = list(client.list_runs(
            project_name="sentinel-agent",
            trace_id=run_id,
            run_type="chain",
            filter='eq(name, "Prompt")',
        ))
        for cr in sorted(chain_runs, key=lambda r: len(str(r.outputs)) if r.outputs else 0, reverse=True):
            if cr.outputs:
                content = _find_audit_text(cr.outputs)
                if content:
                    audit_outputs = [content]
                    break

    # Determine wall-clock latency: root start to last completed child end
    start_time = root.start_time
    end_time = root.end_time
    if not end_time:
        all_children = list(client.list_runs(
            project_name="sentinel-agent",
            trace_id=run_id,
        ))
        ended = [c.end_time for c in all_children if c.end_time]
        if ended:
            end_time = max(ended)

    return {
        "label": label,
        "model": model,
        "content": content,
        "audit_outputs": audit_outputs,
        "start_time": start_time,
        "end_time": end_time,
        "total_tokens": root.total_tokens or 0,
        "prompt_tokens": root.prompt_tokens or 0,
        "completion_tokens": root.completion_tokens or 0,
        "total_cost": root.total_cost,
        "trace_input_tokens": trace_input_tokens,
        "trace_output_tokens": trace_output_tokens,
        "trace_cache_read": trace_cache_read,
        "trace_cache_creation": trace_cache_creation,
    }


def parse_run_stats(content: str, run_data: dict) -> dict:
    """Compute cost from outer agent trace tokens + sub-agent tokens from audit output.

    The LangSmith trace only captures the outer Sentinel agent's LLM calls
    (sub-agents run in ThreadPoolExecutor and don't propagate trace context).
    Sub-agent tokens are summed across every audit tool output in the trace.
    Total cost = outer agent + sub-agent, both at the same model pricing.
    """
    # Outer agent tokens from LangSmith trace LLM runs
    outer_in = run_data.get("trace_input_tokens", 0)
    outer_out = run_data.get("trace_output_tokens", 0)

    # Sub-agent tokens summed across all audit tool outputs (falls back to the
    # combined content string when per-output texts weren't captured).
    audit_outputs = run_data.get("audit_outputs") or ([content] if content else [])
    sub_in, sub_out = sum_sub_agent_tokens(audit_outputs)

    input_tokens = outer_in + sub_in
    output_tokens = outer_out + sub_out
    total_tokens = input_tokens + output_tokens

    model = run_data.get("model", "")
    prices = PRICING.get(model, {"input": 0, "output": 0})
    cost = (input_tokens / 1_000_000) * prices["input"] + (output_tokens / 1_000_000) * prices["output"]

    latency = None
    start = run_data.get("start_time")
    end = run_data.get("end_time")
    if start and end:
        latency = (end - start).total_seconds()

    return {
        "total_tokens": total_tokens,
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "cost": cost,
        "latency": latency,
        "model": model or "unknown",
        "langsmith_cost": run_data.get("total_cost"),
        "outer_tokens": outer_in + outer_out,
        "sub_tokens": sub_in + sub_out,
        "cache_read": run_data.get("trace_cache_read", 0),
        "cache_creation": run_data.get("trace_cache_creation", 0),
    }


def classify_regulation(criterion):
    # type: (str) -> Optional[str]
    c = criterion.strip()
    if c.startswith("HIPAA"):
        return "HIPAA"
    if c.startswith("SOC2") or c.startswith("SOC 2") or c.startswith("SOC-2"):
        return "SOC 2"
    if c.startswith("GDPR"):
        return "GDPR"
    if c.startswith("EUAI") or c.startswith("EU-AI") or c.startswith("EUAIAct") or c.startswith("EU AI"):
        return "EU AI Act"
    if c.startswith("NIST"):
        return "NIST AI RMF"
    if c.startswith("SR11") or c.startswith("SR-11") or c.startswith("SR 11"):
        return "SR 11-7"
    if c.startswith("CA-") or c.startswith("California"):
        return None
    return None


def worst_level(levels):
    worst = "compliant"
    for l in levels:
        if LEVEL_ORDER.get(l, 0) > LEVEL_ORDER.get(worst, 0):
            worst = l
    return worst


def load_ground_truth(revised=True):
    path = REVISED_MATRIX_PATH if revised else MATRIX_PATH
    with open(path) as f:
        matrix = json.load(f)
    gt = {}
    for entry in matrix:
        key = (entry["sop_id"], entry["regulation"])
        gt[key] = normalize_level(entry["compliance_level"])
    return gt


def parse_full_findings(text):
    """Parse the complete audit_all_sops output text."""
    findings = defaultdict(list)
    current_sop = None
    total_parsed = 0
    sop_count = 0
    failed_sops = []
    error_sops = []

    for line in text.split("\n"):
        failed_match = re.match(r'^SOP (SOP-[A-Z]+-\d+): sub-agent did not produce', line)
        if failed_match:
            failed_sops.append(failed_match.group(1))
            continue

        error_match = re.match(r'^(SOP-[A-Z]+-\d+): FAILED', line)
        if error_match:
            error_sops.append(error_match.group(1))
            current_sop = None
            continue

        sop_match = re.match(r'^(SOP-[A-Z]+-\d+)\s+\(', line)
        if sop_match:
            current_sop = sop_match.group(1)
            sop_count += 1
            continue

        finding_match = re.match(r'^\s+(.+?):\s+(compliant|partial|gap)\s+\(', line)
        if finding_match and current_sop:
            criterion = finding_match.group(1)
            level = normalize_level(finding_match.group(2))
            reg = classify_regulation(criterion)
            if reg:
                findings[(current_sop, reg)].append(level)
                total_parsed += 1

    if sop_count > 0 and total_parsed == 0:
        print(f"  WARNING: Found {sop_count} SOP headers but 0 finding details — this run used a compact")
        print(f"  output format without per-finding lines. Re-run the audit with the latest code to get")
        print(f"  parseable output. Deploy first: make deploy")

    return findings, total_parsed, failed_sops, error_sops


def compute_metrics(gt, predicted):
    """Compute comparison metrics between ground truth and predictions."""
    matched = 0
    total = 0
    missing_in_run = []
    extra_in_run = 0
    mismatches = []
    confusion = defaultdict(int)
    false_positives = 0
    false_negatives = 0

    for key, gt_level in gt.items():
        if key in predicted:
            pred_level = predicted[key]
            total += 1
            confusion[(gt_level, pred_level)] += 1
            if gt_level == pred_level:
                matched += 1
            else:
                direction = LEVEL_ORDER[pred_level] - LEVEL_ORDER[gt_level]
                if direction > 0:
                    false_positives += 1
                else:
                    false_negatives += 1
                mismatches.append({
                    "sop_id": key[0],
                    "regulation": key[1],
                    "expected": gt_level,
                    "predicted": pred_level,
                })
        else:
            missing_in_run.append(key)

    for key in predicted:
        if key not in gt:
            extra_in_run += 1

    return {
        "matched": matched,
        "total": total,
        "false_positives": false_positives,
        "false_negatives": false_negatives,
        "mismatches": mismatches,
        "missing_in_run": missing_in_run,
        "extra_in_run": extra_in_run,
        "confusion": confusion,
    }


def macro_f1_for(confusion):
    levels = ["compliant", "partial", "gap"]
    f1s = []
    for cls in levels:
        tp = confusion.get((cls, cls), 0)
        fp = sum(confusion.get((g, cls), 0) for g in levels if g != cls)
        fn = sum(confusion.get((cls, p), 0) for p in levels if p != cls)
        prec = tp / (tp + fp) if (tp + fp) > 0 else 0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0
        f1s.append(f1)
    return sum(f1s) / len(f1s)


def print_stats(stats):
    """Print run stats block."""
    print(f"  Model:   {stats['model']}")
    print(f"  Tokens:  {stats['total_tokens']:,} ({stats['input_tokens']:,} in / {stats['output_tokens']:,} out)")
    outer = stats.get('outer_tokens', 0)
    sub = stats.get('sub_tokens', 0)
    if outer and sub:
        print(f"          (outer agent: {outer:,} + sub-agents: {sub:,})")
    cache_read = stats.get("cache_read", 0)
    cache_creation = stats.get("cache_creation", 0)
    if cache_read or cache_creation:
        print(f"          (cache read: {cache_read:,}, cache creation: {cache_creation:,})")
    print(f"  Cost:    ${stats['cost']:.2f}")
    if stats['latency']:
        print(f"  Latency: {stats['latency']:.0f}s ({stats['latency']/60:.1f}m)")


def print_full_report(gt, predicted, label=""):
    """Print the full validation report."""
    gt_regs = set(k[1] for k in gt)

    m = compute_metrics(gt, predicted)
    matched = m["matched"]
    mismatches = m["mismatches"]
    confusion = m["confusion"]

    gt_total = len(gt)
    failed = len(m["missing_in_run"])
    matched_pct = matched / gt_total * 100 if gt_total else 0
    fp_pct = m["false_positives"] / gt_total * 100 if gt_total else 0
    fn_pct = m["false_negatives"] / gt_total * 100 if gt_total else 0
    failed_pct = failed / gt_total * 100 if gt_total else 0

    if label:
        print(f"\n{'=' * 70}")
        print(label)
        print(f"{'=' * 70}")

    print(f"\n{'='*50}")
    print(f"  Matched:         {matched:>4}/{gt_total}  ({matched_pct:.1f}%)")
    print(f"  False positive:  {m['false_positives']:>4}/{gt_total}  ({fp_pct:.1f}%)  (too strict)")
    print(f"  False negative:  {m['false_negatives']:>4}/{gt_total}  ({fn_pct:.1f}%)  (too lenient)")
    print(f"  Failed:          {failed:>4}/{gt_total}  ({failed_pct:.1f}%)  (missing from run)")
    print(f"{'='*50}")

    # Confusion matrix
    levels = ["compliant", "partial", "gap"]
    hdr = "GT \\ Pred"
    print(f"\nConfusion Matrix:")
    print(f"{hdr:>12} {'compliant':>11} {'partial':>9} {'gap':>6} {'total':>7}")
    print("-" * 50)
    for gt_l in levels:
        row = [confusion.get((gt_l, p_l), 0) for p_l in levels]
        print(f"{gt_l:>12} {row[0]:>11} {row[1]:>9} {row[2]:>6} {sum(row):>7}")

    # Per-class F1
    for cls_name in levels:
        tp = confusion.get((cls_name, cls_name), 0)
        fp = sum(confusion.get((gt_l, cls_name), 0) for gt_l in levels if gt_l != cls_name)
        fn = sum(confusion.get((cls_name, p_l), 0) for p_l in levels if p_l != cls_name)
        prec = tp / (tp + fp) if (tp + fp) > 0 else 0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0
        print(f"\n{cls_name.title()} Detection:  TP={tp}  FP={fp}  FN={fn}")
        print(f"  Precision: {prec:.3f}  Recall: {rec:.3f}  F1: {f1:.3f}")

    print(f"\nMacro F1: {macro_f1_for(confusion):.3f}")

    # Per-regulation accuracy
    print(f"\nPer-Regulation Accuracy:")
    for reg in sorted(gt_regs):
        reg_keys = [k for k in gt if k[1] == reg and k in predicted]
        reg_match = sum(1 for k in reg_keys if gt[k] == predicted[k])
        reg_total = len(reg_keys)
        if reg_total > 0:
            print(f"  {reg:>15}: {reg_match}/{reg_total} ({reg_match/reg_total*100:.1f}%)")
        else:
            print(f"  {reg:>15}: no coverage")

    # Directional bias
    if mismatches:
        too_strict = sum(1 for m in mismatches if LEVEL_ORDER[m['predicted']] > LEVEL_ORDER[m['expected']])
        too_lenient = sum(1 for m in mismatches if LEVEL_ORDER[m['predicted']] < LEVEL_ORDER[m['expected']])
        within_one = sum(1 for m in mismatches if abs(LEVEL_ORDER[m['predicted']] - LEVEL_ORDER[m['expected']]) == 1)
        off_by_two = sum(1 for m in mismatches if abs(LEVEL_ORDER[m['predicted']] - LEVEL_ORDER[m['expected']]) == 2)
        print(f"\nDirectional Bias:")
        print(f"  Too strict (downgraded):  {too_strict} ({too_strict/len(mismatches)*100:.0f}% of mismatches)")
        print(f"  Too lenient (upgraded):   {too_lenient} ({too_lenient/len(mismatches)*100:.0f}% of mismatches)")
        print(f"  Adjacent-level mismatches: {within_one}")
        print(f"  Off-by-two (compliant<->gap): {off_by_two}")

    return m


def validate_single(run_id, gt):
    """Validate a single run and print full report."""
    print(f"Fetching run {run_id} from LangSmith...")
    run_data = fetch_run_data(run_id)

    content = run_data["content"]
    stats = parse_run_stats(content, run_data)

    print(f"\n{'=' * 70}")
    print(f"Run: {run_data['label']}")
    print(f"{'=' * 70}")
    print_stats(stats)

    if not content:
        print("\n  No audit content found — skipping quality evaluation.")
        return

    all_findings, total_parsed, failed_sops, error_sops = parse_full_findings(content)
    print(f"  Parsed {total_parsed} criterion-level findings")
    if failed_sops:
        print(f"  Failed SOPs (no structured findings): {len(failed_sops)}")
    if error_sops:
        print(f"  Error SOPs (504/timeout): {len(error_sops)}")

    predicted = {key: worst_level(levels) for key, levels in all_findings.items()}

    pred_sops = set(k[0] for k in predicted)
    pred_levels = Counter(predicted.values())

    print(f"\n  Aggregated: {len(predicted)} SOP-regulation pairs, {len(pred_sops)} SOPs")
    print(f"  compliant={pred_levels.get('compliant',0)}, partial={pred_levels.get('partial',0)}, gap={pred_levels.get('gap',0)}")

    print_full_report(gt, predicted)


def compare_runs(run_ids, gt):
    """Compare two runs side by side."""
    run_data_list = []
    for rid in run_ids:
        print(f"Fetching run {rid} from LangSmith...")
        run_data_list.append(fetch_run_data(rid))

    gt_total = len(gt)
    summaries = []

    for run_data in run_data_list:
        content = run_data["content"]
        stats = parse_run_stats(content, run_data)
        all_findings, total_parsed, failed_sops, error_sops = parse_full_findings(content)
        predicted = {key: worst_level(levels) for key, levels in all_findings.items()}
        m = compute_metrics(gt, predicted)

        print(f"\n{'=' * 70}")
        print(f"Run: {run_data['label']}")
        print(f"{'=' * 70}")
        print_stats(stats)
        print(f"  Parsed {total_parsed} findings, {len(predicted)} SOP-regulation pairs")
        if failed_sops:
            print(f"  Failed SOPs: {len(failed_sops)}")
        if error_sops:
            print(f"  Error SOPs: {len(error_sops)}")

        summaries.append((run_data["label"], m, stats))

    # Side-by-side summary
    r1_label, r1_m, r1_s = summaries[0]
    r2_label, r2_m, r2_s = summaries[1]

    print(f"\n\n{'=' * 70}")
    print("SIDE-BY-SIDE COMPARISON")
    print(f"{'=' * 70}")

    col1 = r1_label[:30]
    col2 = r2_label[:30]

    print(f"\n{'Metric':>20} {col1:>30} {col2:>30}")
    print("-" * 84)

    def row(label, v1, v2):
        p1 = v1 / gt_total * 100 if gt_total else 0
        p2 = v2 / gt_total * 100 if gt_total else 0
        print(f"  {label:>18} {v1:>4}/{gt_total} ({p1:>5.1f}%) {v2:>10}/{gt_total} ({p2:>5.1f}%)")

    row("Matched", r1_m["matched"], r2_m["matched"])
    row("False positive", r1_m["false_positives"], r2_m["false_positives"])
    row("False negative", r1_m["false_negatives"], r2_m["false_negatives"])
    row("Failed", len(r1_m["missing_in_run"]), len(r2_m["missing_in_run"]))

    mf1_1 = macro_f1_for(r1_m["confusion"])
    mf1_2 = macro_f1_for(r2_m["confusion"])
    print(f"  {'Macro F1':>18} {mf1_1:>18.3f}       {mf1_2:>18.3f}")

    print(f"\n{'':>20} {col1:>30} {col2:>30}")
    print("-" * 84)
    print(f"  {'Tokens':>18} {r1_s['total_tokens']:>27,} {r2_s['total_tokens']:>27,}")
    print(f"  {'Cost':>18} {'${:.2f}'.format(r1_s['cost']):>30} {'${:.2f}'.format(r2_s['cost']):>30}")
    lat1 = f"{r1_s['latency']:.0f}s" if r1_s['latency'] else "n/a"
    lat2 = f"{r2_s['latency']:.0f}s" if r2_s['latency'] else "n/a"
    print(f"  {'Latency':>18} {lat1:>30} {lat2:>30}")


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="Validate LangSmith audit runs against compliance matrix",
    )
    parser.add_argument("run_ids", nargs="*", help="LangSmith run ID(s)")
    parser.add_argument("--original", action="store_true", help="Use original compliance matrix instead of revised")
    args = parser.parse_args()

    if not args.run_ids:
        parser.print_help()
        sys.exit(0)

    use_revised = not args.original
    matrix_label = "ORIGINAL" if args.original else "REVISED"
    gt = load_ground_truth(revised=use_revised)
    gt_levels = Counter(gt.values())
    print(f"Ground truth ({matrix_label}): {len(gt)} pairs — compliant={gt_levels['compliant']}, partial={gt_levels['partial']}, gap={gt_levels['gap']}")

    if len(args.run_ids) == 1:
        validate_single(args.run_ids[0], gt)
    elif len(args.run_ids) == 2:
        compare_runs(args.run_ids, gt)
    else:
        print("Error: provide 1 or 2 run IDs", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Show all tool calls with arguments for a LangSmith run.

Fetches LLM runs from the trace and extracts tool_calls from each model
response, displaying them in chronological order with arguments, timing,
and token usage.

Usage:
    python scripts/inspect_tool_calls.py <run_id>
    python scripts/inspect_tool_calls.py <run_id> --show-output     # include tool output previews
    python scripts/inspect_tool_calls.py <run_id> --json            # machine-readable JSON
"""
import json
import sys
from datetime import datetime, timezone
from typing import Optional


def _get_langsmith_client():
    from dotenv import load_dotenv
    load_dotenv()
    from langsmith import Client
    return Client()


def _parse_time(t) -> Optional[datetime]:
    if t is None:
        return None
    if isinstance(t, datetime):
        return t
    return datetime.fromisoformat(str(t))


def _format_duration(start, end) -> str:
    if not start or not end:
        return "?"
    delta = _parse_time(end) - _parse_time(start)
    secs = delta.total_seconds()
    if secs < 1:
        return f"{secs*1000:.0f}ms"
    if secs < 60:
        return f"{secs:.1f}s"
    return f"{secs/60:.1f}m"


def _truncate(s: str, max_len: int = 200) -> str:
    if len(s) <= max_len:
        return s
    return s[:max_len] + "..."


def _count_tokens(text: str) -> int:
    import tiktoken
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))


def _extract_output_text(outputs) -> str:
    if not outputs:
        return ""
    if isinstance(outputs, dict):
        out_val = outputs.get("output", outputs)
        if isinstance(out_val, dict):
            return str(out_val.get("content", ""))
        return str(out_val)
    return str(outputs)


def _duration_seconds(start, end) -> Optional[float]:
    if not start or not end:
        return None
    delta = _parse_time(end) - _parse_time(start)
    return delta.total_seconds()


def _format_seconds(secs: float) -> str:
    if secs < 1:
        return f"{secs*1000:.0f}ms"
    if secs < 60:
        return f"{secs:.1f}s"
    return f"{secs/60:.1f}m"


def fetch_tool_calls(run_id: str, project_name: str = "sentinel-agent", log=None):
    if log is None:
        log = sys.stderr
    client = _get_langsmith_client()
    root = client.read_run(run_id)
    print(f"Run: {root.name or 'unnamed'}  status={root.status}  id={run_id}", file=log)
    print(f"Time: {root.start_time} → {root.end_time}  ({_format_duration(root.start_time, root.end_time)})", file=log)
    print(file=log)

    # Fetch all runs in the trace, sorted by start time
    all_runs = list(client.list_runs(
        project_name=project_name,
        trace_id=run_id,
    ))

    # Wall time: use root end_time, or fall back to the latest timestamp across all runs
    end_time = root.end_time
    if not end_time:
        for r in all_runs:
            for t in (r.end_time, r.start_time):
                if t and (not end_time or _parse_time(t) > _parse_time(end_time)):
                    end_time = t
    wall_seconds = _duration_seconds(root.start_time, end_time)

    # Index runs by ID for parent lookup
    runs_by_id = {str(r.id): r for r in all_runs}

    # Collect tool calls from LLM runs (the model deciding to call a tool)
    # and tool runs (the actual execution with inputs/outputs)
    llm_runs = sorted(
        [r for r in all_runs if r.run_type == "llm"],
        key=lambda r: r.start_time or datetime.min.replace(tzinfo=timezone.utc),
    )
    tool_runs = sorted(
        [r for r in all_runs if r.run_type == "tool"],
        key=lambda r: r.start_time or datetime.min.replace(tzinfo=timezone.utc),
    )

    # Index tool runs by (name, input args json) for matching to LLM tool_calls
    tool_runs_by_key = {}
    for tr in tool_runs:
        key = (tr.name, json.dumps(tr.inputs or {}, sort_keys=True))
        tool_runs_by_key.setdefault(key, []).append(tr)

    # Also index by parent for fallback
    tool_runs_by_parent = {}
    for tr in tool_runs:
        pid = str(tr.parent_run_id) if tr.parent_run_id else None
        if pid:
            tool_runs_by_parent.setdefault(pid, []).append(tr)

    entries = []
    step = 0

    for llm_run in llm_runs:
        if not llm_run.outputs:
            continue
        gens = llm_run.outputs.get("generations", [[]])
        if not gens or not gens[0]:
            continue
        msg = gens[0][0].get("message", {})
        kwargs = msg.get("kwargs", {})
        tool_calls = kwargs.get("tool_calls", [])
        if not tool_calls:
            continue

        # Find parent context (which agent/node this LLM call belongs to)
        parent_name = None
        if llm_run.parent_run_id:
            parent = runs_by_id.get(str(llm_run.parent_run_id))
            if parent:
                parent_name = parent.name

        for tc in tool_calls:
            step += 1
            tc_id = tc.get("id", "")
            tc_name = tc.get("name", "unknown")
            tc_args = tc.get("args", {})

            # Find matching tool execution by (name, args)
            matched_tool_run = None
            match_key = (tc_name, json.dumps(tc_args, sort_keys=True))
            candidates = tool_runs_by_key.get(match_key, [])
            used_ids = {e.get("tool_run_id") for e in entries}
            for c in candidates:
                if str(c.id) not in used_ids:
                    matched_tool_run = c
                    break
            # Fallback: match by name among siblings
            if not matched_tool_run:
                siblings = tool_runs_by_parent.get(str(llm_run.parent_run_id), [])
                for s in siblings:
                    if s.name == tc_name and str(s.id) not in used_ids:
                        matched_tool_run = s
                        break

            entry = {
                "step": step,
                "tool_name": tc_name,
                "tool_call_id": tc_id,
                "args": tc_args,
                "llm_run_id": str(llm_run.id),
                "llm_run_name": llm_run.name,
                "parent_name": parent_name,
                "llm_start": str(llm_run.start_time) if llm_run.start_time else None,
                "llm_tokens": llm_run.total_tokens,
            }

            if matched_tool_run:
                entry["tool_run_id"] = str(matched_tool_run.id)
                entry["tool_duration"] = _format_duration(
                    matched_tool_run.start_time, matched_tool_run.end_time
                )
                entry["tool_duration_secs"] = _duration_seconds(
                    matched_tool_run.start_time, matched_tool_run.end_time
                )
                entry["tool_status"] = matched_tool_run.status
                entry["tool_error"] = matched_tool_run.error
                output_text = _extract_output_text(matched_tool_run.outputs)
                if output_text:
                    entry["output_tokens"] = _count_tokens(output_text)
                    entry["output_preview"] = _truncate(output_text, 300)

            entries.append(entry)

    return entries, wall_seconds


def print_entries(entries, show_output: bool = False, wall_seconds: Optional[float] = None):
    if not entries:
        print("No tool calls found in this run.")
        return

    print(f"{'─' * 80}")
    print(f" {len(entries)} tool calls found")
    print(f"{'─' * 80}")
    print()

    current_parent = None
    for e in entries:
        parent = e.get("parent_name")
        if parent != current_parent:
            current_parent = parent
            if parent:
                print(f"┌─ Agent: {parent}")
                print(f"│")

        prefix = "│  " if current_parent else ""

        status_icon = "✓" if e.get("tool_status") == "success" else "✗" if e.get("tool_error") else "?"
        duration = e.get("tool_duration", "?")
        out_tok = e.get("output_tokens")
        tok_str = f"  {out_tok:,} tok" if out_tok is not None else ""

        print(f"{prefix}[{e['step']:>3}] {status_icon} {e['tool_name']}  ({duration}){tok_str}")

        args = e.get("args", {})
        if args:
            for k, v in args.items():
                v_str = str(v)
                if len(v_str) > 120:
                    v_str = v_str[:120] + "..."
                print(f"{prefix}      {k}: {v_str}")

        if e.get("tool_error"):
            print(f"{prefix}      ERROR: {_truncate(e['tool_error'], 200)}")

        if show_output and e.get("output_preview"):
            print(f"{prefix}      → {e['output_preview']}")

        print()

    # Summary
    tool_stats = {}
    for e in entries:
        name = e["tool_name"]
        if name not in tool_stats:
            tool_stats[name] = {"count": 0, "tokens": 0, "time": 0.0}
        tool_stats[name]["count"] += 1
        tool_stats[name]["tokens"] += e.get("output_tokens", 0)
        tool_stats[name]["time"] += e.get("tool_duration_secs") or 0.0
    total_tokens = sum(s["tokens"] for s in tool_stats.values())
    total_time = sum(s["time"] for s in tool_stats.values())
    print(f"{'─' * 80}")
    print(f"Summary ({total_tokens:,} output tokens total, {_format_seconds(total_time)} cumulative tool time):")
    for name, s in sorted(tool_stats.items(), key=lambda x: -x[1]["count"]):
        time_str = _format_seconds(s["time"]) if s["time"] > 0 else "?"
        print(f"  {name}: {s['count']} calls, {s['tokens']:,} tok, {time_str}")
    if wall_seconds is not None:
        print(f"\nWall time: {_format_seconds(wall_seconds)}")


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__.strip())
        sys.exit(0)

    run_id = args[0]
    show_output = "--show-output" in args
    as_json = "--json" in args

    log = sys.stderr if as_json else sys.stdout
    entries, wall_seconds = fetch_tool_calls(run_id, log=log)

    if as_json:
        print(json.dumps({"tool_calls": entries, "wall_seconds": wall_seconds}, indent=2, default=str))
    else:
        print_entries(entries, show_output=show_output, wall_seconds=wall_seconds)


if __name__ == "__main__":
    main()

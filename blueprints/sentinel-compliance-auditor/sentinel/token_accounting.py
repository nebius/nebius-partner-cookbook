"""Shared token-accounting format + parser for the audit pipeline.

`graph/tools.py` emits per-SOP and aggregate token lines as plain text; the UI
(`ui/server.py`) and the eval validator (`scripts/validate_run.py`) scrape them
back out. Centralizing the emit format, the regexes, and the audit tool-name set
here keeps producer and consumers in lockstep — a format change updates all
three at once (and `tests/test_token_accounting.py` round-trips emit→parse).

Only `re` is imported, so this stays safe to import in the LangGraph Cloud image.
"""
from __future__ import annotations

import re

# Tools whose results carry token lines. Consumers gate on these so a large
# audit result that gets offloaded and re-read via read_file isn't counted again.
AUDIT_TOOL_NAMES = frozenset({"audit_single_sop", "audit_sops", "audit_all_sops"})

# One format, two labels: per-SOP ("Sub-agent tokens") and batch aggregate
# ("Total tokens"). The matching regexes capture (input, output).
_TOKENS_FMT = "{label}: {total:,} ({inp:,} in / {out:,} out)"
_SUB_AGENT_LABEL = "Sub-agent tokens"
_TOTAL_LABEL = "Total tokens"


def _token_re(label: str) -> re.Pattern[str]:
    return re.compile(
        re.escape(label) + r":\s*[\d,]+\s*\(\s*([\d,]+)\s*in\s*/\s*([\d,]+)\s*out\)"
    )


SUB_AGENT_TOKENS_RE = _token_re(_SUB_AGENT_LABEL)
TOTAL_TOKENS_RE = _token_re(_TOTAL_LABEL)


def format_sub_agent_tokens(inp: int, out: int) -> str:
    """Per-SOP sub-agent token line (emitted by _audit_single_sop_impl)."""
    return _TOKENS_FMT.format(label=_SUB_AGENT_LABEL, total=inp + out, inp=inp, out=out)


def format_total_tokens(inp: int, out: int) -> str:
    """Aggregate token line for a batch audit summary (audit_sops/audit_all_sops)."""
    return _TOKENS_FMT.format(label=_TOTAL_LABEL, total=inp + out, inp=inp, out=out)


def _match(pattern: re.Pattern[str], text: str) -> tuple[int, int] | None:
    m = pattern.search(text)
    if not m:
        return None
    return int(m.group(1).replace(",", "")), int(m.group(2).replace(",", ""))


def parse_tokens_from_result(text: str) -> tuple[int, int] | None:
    """Parse one audit tool result's sub-agent tokens as (input, output).

    Within a single result the aggregate "Total tokens:" line supersedes the
    per-SOP "Sub-agent tokens:" lines (an audit_sops/audit_all_sops result has
    both; an individual audit_single_sop result has only the per-SOP line).
    Returns None when no token line is present.
    """
    if not text:
        return None
    return _match(TOTAL_TOKENS_RE, text) or _match(SUB_AGENT_TOKENS_RE, text)


def sum_sub_agent_tokens(audit_outputs) -> tuple[int, int]:
    """Sum (input, output) sub-agent tokens across several audit tool outputs.

    A run can make multiple audit calls, each reporting only its own sub-agents;
    summing per-output (each via `parse_tokens_from_result`) counts every call
    without double-counting the per-SOP lines inside an aggregate output.
    """
    sub_in = sub_out = 0
    for text in audit_outputs:
        parsed = parse_tokens_from_result(text)
        if parsed:
            sub_in += parsed[0]
            sub_out += parsed[1]
    return sub_in, sub_out

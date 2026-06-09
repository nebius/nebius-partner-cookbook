"""Tests for the shared token-accounting module (sentinel/token_accounting.py).

This is the single source of truth for the emit format, the parse regexes, and
the audit tool-name set used by tools.py (producer), ui/server.py and
scripts/validate_run.py (consumers). The round-trip test is the key guarantee:
if the emit format ever drifts, parsing must drift with it.
"""
from __future__ import annotations

from sentinel.token_accounting import (
    AUDIT_TOOL_NAMES,
    format_sub_agent_tokens,
    format_total_tokens,
    parse_tokens_from_result,
    sum_sub_agent_tokens,
)

# Realistic audit_sops output: one aggregate "Total tokens:" line (covers its
# sub-agents) plus per-SOP "Sub-agent tokens:" lines that must NOT be added on top.
AUDIT_SOPS_15 = (
    "Audit complete: 15 SOPs\n"
    f"  {format_total_tokens(18_796_249, 174_723)}\n"
    "  Failed: 0\n\n"
    "Per-SOP breakdown:\n"
    "SOP-CLIN-001 (Clinical Validation): 3 findings — 1C/1P/1G\n"
    f"{format_sub_agent_tokens(1_180_000, 20_000)}\n"
)
AUDIT_SOPS_5 = (
    "Audit complete: 5 SOPs\n"
    f"  {format_total_tokens(7_086_885, 63_560)}\n"
)
AUDIT_SINGLE = (
    "SOP-ISEC-008 (MFA): 5 findings — 2C/2P/1G\n"
    f"{format_sub_agent_tokens(450_000, 50_000)}"
)


def test_round_trip_total():
    """format_total_tokens output is parsed back to the same (in, out)."""
    assert parse_tokens_from_result(format_total_tokens(8_000_000, 1_000_000)) == (8_000_000, 1_000_000)


def test_round_trip_sub_agent():
    assert parse_tokens_from_result(format_sub_agent_tokens(123_456, 7_890)) == (123_456, 7_890)


def test_format_shape():
    assert format_total_tokens(1_000_000, 2_000) == "Total tokens: 1,002,000 (1,000,000 in / 2,000 out)"
    assert format_sub_agent_tokens(80_000, 20_000) == "Sub-agent tokens: 100,000 (80,000 in / 20,000 out)"


def test_total_supersedes_sub_agent_within_one_result():
    """An audit_sops output has both lines; the aggregate wins (no double-count)."""
    assert parse_tokens_from_result(AUDIT_SOPS_15) == (18_796_249, 174_723)


def test_individual_result_uses_sub_agent_line():
    assert parse_tokens_from_result(AUDIT_SINGLE) == (450_000, 50_000)


def test_parse_none_when_no_token_line():
    assert parse_tokens_from_result("list_sops returned 200 SOPs") is None
    assert parse_tokens_from_result("") is None
    assert parse_tokens_from_result(None) is None


def test_sum_multiple_audit_calls():
    """Several audit calls in one run are summed, not deduped to one."""
    assert sum_sub_agent_tokens([AUDIT_SOPS_15, AUDIT_SOPS_5]) == (
        18_796_249 + 7_086_885,
        174_723 + 63_560,
    )


def test_sum_mixed_calls():
    assert sum_sub_agent_tokens([AUDIT_SOPS_5, AUDIT_SINGLE]) == (
        7_086_885 + 450_000,
        63_560 + 50_000,
    )


def test_sum_empty():
    assert sum_sub_agent_tokens([]) == (0, 0)
    assert sum_sub_agent_tokens(["", "no token lines"]) == (0, 0)


def test_audit_tool_names():
    assert AUDIT_TOOL_NAMES == frozenset({"audit_single_sop", "audit_sops", "audit_all_sops"})
    assert "read_file" not in AUDIT_TOOL_NAMES  # the offloaded-reread guard

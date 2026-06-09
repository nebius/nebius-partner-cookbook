"""Integration: validate_run.parse_run_stats aggregates outer + all audit calls.

The pure token-summing logic is tested in test_token_accounting.py; here we
check parse_run_stats wires outer-trace tokens together with the per-call
sub-agent totals and prices them correctly.
"""
from __future__ import annotations

from scripts.validate_run import parse_run_stats

AUDIT_SOPS_15 = (
    "Audit complete: 15 SOPs\n"
    "  Total tokens: 18,970,972 (18,796,249 in / 174,723 out)\n"
)
AUDIT_SOPS_5 = (
    "Audit complete: 5 SOPs\n"
    "  Total tokens: 7,150,445 (7,086,885 in / 63,560 out)\n"
)
AUDIT_SINGLE = (
    "SOP-ISEC-008 (MFA): 5 findings — 2C/2P/1G\n"
    "Sub-agent tokens: 500,000 (450,000 in / 50,000 out)"
)


def test_parse_run_stats_sums_outer_and_all_audit_calls():
    """Mirrors the real run (019ea71b…): outer + audit #1 18.97M + audit #2 7.15M."""
    run_data = {
        "trace_input_tokens": 249_815,
        "trace_output_tokens": 10_107,
        "audit_outputs": [AUDIT_SOPS_15, AUDIT_SOPS_5],
        "model": "nvidia/Nemotron-3-Ultra-550b-a55b",
    }
    stats = parse_run_stats(None, run_data)

    assert stats["input_tokens"] == 249_815 + 18_796_249 + 7_086_885
    assert stats["output_tokens"] == 10_107 + 174_723 + 63_560
    assert stats["sub_tokens"] == (18_796_249 + 174_723) + (7_086_885 + 63_560)
    assert stats["outer_tokens"] == 249_815 + 10_107

    expected_cost = (stats["input_tokens"] / 1e6) * 1.00 + (stats["output_tokens"] / 1e6) * 3.00
    assert abs(stats["cost"] - expected_cost) < 1e-6


def test_parse_run_stats_falls_back_to_content():
    """When audit_outputs is absent, fall back to the combined content string."""
    run_data = {"trace_input_tokens": 0, "trace_output_tokens": 0, "model": "x"}
    stats = parse_run_stats(AUDIT_SINGLE, run_data)
    assert stats["input_tokens"] == 450_000
    assert stats["output_tokens"] == 50_000

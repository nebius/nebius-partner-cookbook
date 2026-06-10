"""Retry classification, token carry across attempts, and the audit fan-out.

Covers the regressions fixed in the structured-status refactor: retryability
must come from SopAuditResult.status, never from sniffing the summary text
(which embeds model-written prose), and the batch orchestrator must not stack
a second retry layer on top of the per-SOP one.
"""
from __future__ import annotations

from unittest.mock import patch


from sentinel.graph.tools import (
    MAX_RETRIES,
    RATE_LIMIT_BACKOFF,
    RETRY_BACKOFF,
    SopAuditResult,
    _audit_all_sops_impl,
    _audit_single_sop_with_retry,
    _is_rate_limited_error,
    _is_retryable,
    _retry_delay,
)


class TestIsRetryable:
    def test_ok_not_retryable(self):
        assert not _is_retryable(SopAuditResult("fine", [], status="ok"))

    def test_invalid_not_retryable(self):
        assert not _is_retryable(SopAuditResult("SOP not found: X", [], status="invalid"))

    def test_truncated_not_retryable(self):
        """Truncation would just truncate again."""
        assert not _is_retryable(SopAuditResult("truncated", [], status="truncated"))

    def test_failed_retryable(self):
        assert _is_retryable(SopAuditResult("FAILED: X — 504", [], status="failed"))

    def test_no_findings_retryable(self):
        assert _is_retryable(SopAuditResult("no structured findings", [], status="no_findings"))

    def test_failed_keyword_in_summary_text_is_ignored(self):
        """Regression: a gap_description like 'backup restore test FAILED'
        used to mark a successful audit retryable, discarding the good result
        and re-billing the whole sub-agent run."""
        summary = (
            "SOP-ITO-003 (Backup): 1 findings — 0C/0P/1G\n"
            "  SOC2-A1.2: gap (high) — backup restore test FAILED criteria undefined"
        )
        assert not _is_retryable(SopAuditResult(summary, [], status="ok"))


class TestRateLimitDetection:
    def test_429_detected(self):
        assert _is_rate_limited_error("Error code: 429 - too many requests")

    def test_quota_and_exceeded_detected(self):
        assert _is_rate_limited_error("Quota exhausted")
        assert _is_rate_limited_error("Rate limit exceeded")

    def test_plain_words_containing_rate_not_detected(self):
        """Regression: 'rate' used to match inside corporate/operate/accurate."""
        assert not _is_rate_limited_error("corporate governance must operate with accurate data")

    def test_generic_error_not_detected(self):
        assert not _is_rate_limited_error("504 Gateway Timeout")


class TestRetryDelay:
    def test_normal_backoff_range(self):
        d = _retry_delay(1, rate_limited=False)
        assert RETRY_BACKOFF <= d <= RETRY_BACKOFF * 1.5

    def test_rate_limited_backoff_is_longer(self):
        d = _retry_delay(1, rate_limited=True)
        assert RATE_LIMIT_BACKOFF <= d <= RATE_LIMIT_BACKOFF * 1.5

    def test_scales_with_attempt(self):
        assert _retry_delay(3, rate_limited=False) >= RETRY_BACKOFF * 3


def _ok(sop_id="SOP-X-001", tokens=(100, 10)):
    return SopAuditResult(f"{sop_id} (T): 1 findings — 1C/0P/0G", [], *tokens, status="ok")


def _failed(sop_id="SOP-X-001", tokens=(50, 5), rate_limited=False):
    return SopAuditResult(
        f"FAILED: {sop_id} — sub-agent error: boom", [], *tokens,
        status="failed", rate_limited=rate_limited,
    )


class TestSingleSopRetry:
    def test_success_first_try_no_retry(self):
        with patch("sentinel.graph.tools._audit_single_sop_impl", return_value=_ok()) as impl, \
             patch("sentinel.graph.tools.time.sleep") as sleep:
            result = _audit_single_sop_with_retry("SOP-X-001")
        assert impl.call_count == 1
        sleep.assert_not_called()
        assert result.status == "ok"

    def test_tokens_accumulate_across_attempts(self):
        """Failed attempts are still billed — their tokens must carry over."""
        with patch(
            "sentinel.graph.tools._audit_single_sop_impl",
            side_effect=[_failed(tokens=(50, 5)), _failed(tokens=(60, 6)), _ok(tokens=(100, 10))],
        ) as impl, patch("sentinel.graph.tools.time.sleep"):
            result = _audit_single_sop_with_retry("SOP-X-001")
        assert impl.call_count == 3
        assert result.status == "ok"
        assert result.input_tokens == 50 + 60 + 100
        assert result.output_tokens == 5 + 6 + 10

    def test_gives_up_after_max_retries(self):
        with patch(
            "sentinel.graph.tools._audit_single_sop_impl", return_value=_failed()
        ) as impl, patch("sentinel.graph.tools.time.sleep"):
            result = _audit_single_sop_with_retry("SOP-X-001")
        assert impl.call_count == 1 + MAX_RETRIES
        assert result.status == "failed"
        assert result.input_tokens == 50 * (1 + MAX_RETRIES)

    def test_truncated_result_not_retried(self):
        truncated = SopAuditResult("partial findings [truncated]", [], 80, 8, status="truncated")
        with patch(
            "sentinel.graph.tools._audit_single_sop_impl", return_value=truncated
        ) as impl, patch("sentinel.graph.tools.time.sleep"):
            result = _audit_single_sop_with_retry("SOP-X-001")
        assert impl.call_count == 1
        assert result.status == "truncated"


class TestAuditAllSopsFanout:
    SOPS = [
        {"sop_id": "SOP-A-001", "title": "A", "business_unit": "bu", "regulations": []},
        {"sop_id": "SOP-B-001", "title": "B", "business_unit": "bu", "regulations": []},
        {"sop_id": "SOP-C-001", "title": "C", "business_unit": "bu", "regulations": []},
    ]

    def _run(self, run_one):
        with patch("sentinel.retrieval.local.list_all_sops", return_value=self.SOPS):
            return _audit_all_sops_impl(run_one, max_workers=2)

    def test_run_one_called_exactly_once_per_sop(self):
        """Regression: the batch loop used to layer MAX_RETRIES more attempts
        on top of run_one's own retries — up to MAX_RETRIES² sub-agent runs."""
        calls = []

        def run_one(sop_id):
            calls.append(sop_id)
            return _failed(sop_id)  # still-retryable result must NOT re-run here

        summary = self._run(run_one)
        assert sorted(calls) == ["SOP-A-001", "SOP-B-001", "SOP-C-001"]
        assert "Failed after retries: 3" in summary

    def test_aggregates_findings_and_tokens(self, compliant_finding, gap_finding):
        results = {
            "SOP-A-001": SopAuditResult("SOP-A-001 (A): 1 findings — 1C/0P/0G", [compliant_finding], 100, 10, status="ok"),
            "SOP-B-001": SopAuditResult("SOP-B-001 (B): 1 findings — 0C/0P/1G", [gap_finding], 200, 20, status="ok"),
            "SOP-C-001": _failed("SOP-C-001", tokens=(30, 3)),
        }
        summary = self._run(lambda sid: results[sid])
        assert "Audit complete: 2 findings across 3 SOPs" in summary
        assert "Compliant: 1" in summary
        assert "Gap:       1" in summary
        assert "Failed after retries: 1" in summary
        # 330 in / 33 out, including the failed SOP's billed tokens
        assert "(330 in / 33 out)" in summary

    def test_run_one_exception_becomes_failed_result(self):
        def run_one(sop_id):
            if sop_id == "SOP-B-001":
                raise RuntimeError("connection reset")
            return _ok(sop_id)

        summary = self._run(run_one)
        assert "SOP-B-001: FAILED — connection reset" in summary
        assert "Failed after retries: 1" in summary

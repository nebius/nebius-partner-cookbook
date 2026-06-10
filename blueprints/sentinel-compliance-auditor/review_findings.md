# Codebase Review Findings — Sentinel Compliance Auditor

Review date: 2026-06-09. Four parallel reviews covering the agent core, retrieval/eval, UI, and scripts/tests/plumbing surfaced 36 findings (5 HIGH correctness, 1 HIGH invariant drift, 2 HIGH test coverage, 14 MEDIUM, 14 LOW).

**All 36 findings were fixed on 2026-06-10** across commits `df0d74b`…`4abfb88` (see git history for the per-finding commit messages; each names the findings it closes). The regression suite grew from 76 to 150 tests in the process, and the regulation index was re-ingested the same day (16,289 chunks from 43 source files), landing the improved section-header metadata in Pinecone.

The invariants the fixes introduced are documented in CLAUDE.md (structured-status retries, the atomic retrieval budget, the shared section chunker, the `/agents.js` agent registry, SSE disconnect cancellation, etc.) — that file, not this one, is the forward-looking reference.

## Where fixes deviated from the review's suggestions

- **Eval keyword regex (was finding 5):** the suggested pattern still let "not fully compliant" count as compliant (the engine skips the optional `fully` and matches at `compliant`); fixed-length lookbehinds including `(?<!not fully )` are anchored on `compliant` instead, and "not fully compliant" was added to the gap keywords.
- **Bare clause IDs (was finding 7):** bare `Art. N` identifiers remain unclassified — the per-finding lines carry no regulation context to disambiguate GDPR vs EU AI Act; `parse_full_findings` prints the unclassified count instead.
- **Nebius model reasoning (was finding 14):** reasoning stays off for Nemotron/Kimi/GLM (documented in code) — the `thinking`/`reasoning_effort` chat-template kwargs are DeepSeek-specific.

## Verified as fine (checked explicitly, no action needed)

- Message-type matching uses explicit set membership per the CLAUDE.md rule (`ui/server.py`).
- Token accounting: server gates on `AUDIT_TOOL_NAMES` and sums across multiple audit calls; values-mode usage overwrite is correct (full-state snapshots).
- Jira clients properly closed in `finally` blocks; ADF descriptions JSON-encoded (no injection path).
- `binary_compliance_metrics`/`macro_f1` math is correct; `GraphRecursionError` handled in `run_qa_eval.py`.
- All graph IDs referenced by the UI exist in `langgraph.json`.

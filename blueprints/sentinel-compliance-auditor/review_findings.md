# Codebase Review Findings — Sentinel Compliance Auditor

Review date: 2026-06-09. Four parallel reviews covering the agent core, retrieval/eval, UI, and scripts/tests/plumbing. Overall the codebase follows its documented invariants well (token accounting, message-type handling, Jira client cleanup); the items below are the exceptions, prioritized.

**Remediation status (2026-06-10):** all HIGH findings except 33/34 and all MEDIUM findings are fixed; each fixed finding is tagged with its commit below. Still open: test-coverage HIGHs (33, 34), the agent-pricing-registry and chunker bullets of 35, and the LOWs (12, 19, 23, 24, 27–32).

## Top issues — can corrupt results or multiply cost

### 1. Retry classification sniffs strings in LLM-generated text (HIGH) — ✅ fixed (df0d74b)
`sentinel/graph/tools.py:523-534` — `_is_retryable` checks `"FAILED" in result` against the full per-SOP summary, which embeds model-written `gap_description` text. A finding whose text contains "FAILED" (e.g. "backup restore test FAILED criteria undefined") marks a *successful* audit as retryable; the batch loop (`tools.py:604`) then discards the good result, re-runs, and double-bills. Similarly `_is_rate_limited` (`tools.py:538`) matches `"rate"` inside "corporate"/"operate"/"accurate". Also: the `"failed to parse sub-agent findings"` check at line 533 is dead — nothing emits that string anymore.

**Fix:** carry a structured status on `SopAuditResult` (e.g. `status: Literal["ok","failed","no_findings","truncated"]` plus `rate_limited: bool`) set at the failure sites; make `_is_retryable`/`_is_rate_limited` read the field, not the string.

### 2. Multiplicative retries: up to 25 sub-agent runs per SOP (HIGH) — ✅ fixed (df0d74b)
`sentinel/graph/tools.py:560-569` (`_audit_single_sop_with_retry`, up to 5 attempts) is the `run_one` passed into `_audit_all_sops_impl`, whose own retry loop (lines 603-620) re-invokes it up to `MAX_RETRIES` more times — 5×5 = 25 full sub-agent runs worst case per stubborn SOP, with compounding backoffs. The sibling `_audit_sops` (lines 887-923) has only single-layer retry, so the two batch tools behave inconsistently.

**Fix:** pick one retry layer — pass the non-retrying `_audit_single_sop_impl` into the batch orchestrator, or drop the batch-level retry loop.

### 3. Parallel tool calls silently dropped in the UI stream (HIGH) — ✅ fixed (e1b6138)
`ui/server.py:558-563` — `_normalize_event` forwards only `tool_calls[0]`; if the outer agent emits one AI message with N tool calls, N−1 never reach the client but N `tool_result` events do. The client matches results to "last toolCall without a result" LIFO (`audit.jsx:66-70`, `compare.jsx:96-99`), mis-attributing results for concurrent calls.

**Fix:** emit one `tool_call` event per entry including its `id`, include `tool_call_id` on `tool_result` events (present on the ToolMessage), and match by id in both JSX files.

### 4. Client disconnect never cancels LangGraph runs (HIGH) — ✅ fixed (e1b6138)
`ui/server.py:477-544, 587-605` — when the browser aborts, Starlette cancels `_drain_sse`, but the `_stream_one` producer threads keep consuming the runs to completion into an unbounded `queue.Queue`, each abandoned `run_in_executor(None, out_q.get)` parks a default-executor thread, and the runs keep burning tokens (×3 on `/api/race/stream`).

**Fix:** wrap the yield loop in `try/finally` (catch `asyncio.CancelledError`), set a `threading.Event` the producer checks, call `client.runs.cancel(thread_id, run_id)` (run_id already captured in `_on_run_created`), and use a bounded queue.

### 5. Eval keyword fallback counts "non-compliant" as "compliant" (HIGH) — ✅ fixed (4e7273a)
`sentinel/eval/metrics.py:51-57` — in `extract_compliance_level`, the regex `\b(?:fully\s+)?compliant\b` matches inside "non-compliant"/"not compliant" because the hyphen/space is a word boundary, so every negative mention also increments the `compliant` count. Gap keywords like `missing`/`fails to` also routinely appear in compliant answers ("no controls are missing"). Skews headline `sop_compliance` eval scores.

**Fix:** `r"(?<!non-)(?<!non )(?<!not )\b(?:fully\s+)?compliant\b"`, and consider dropping `missing` from the gap pattern.

## Benchmark pipeline accuracy (`scripts/validate_run.py`)

### 6. `classify_regulation` maps every NIST framework to "NIST AI RMF" (MEDIUM) — ✅ fixed (7476466)
`scripts/validate_run.py:226-227` — `c.startswith("NIST")` → "NIST AI RMF", but sub-agents cite NIST SP 800-53/63B/207/CSF; a gap against SP 800-53 folds into the (SOP, "NIST AI RMF") aggregation and can flip a compliant ground-truth pair to a false mismatch.

**Fix:** match only AI RMF prefixes (`NIST-AI`, `NIST AI`, `AI RMF`, `GOVERN/MAP/MEASURE/MANAGE`); return `None` for other NIST docs.

### 7. Bare clause IDs silently dropped by criterion prefix matching (MEDIUM) — ✅ fixed (7476466)
`scripts/validate_run.py:215-232` — sub-agents frequently emit `requirement_id` without a framework prefix (`CC6.1`, `164.312(a)(2)(iv)`, `Art. 13`); these classify to `None`, the finding is discarded, and the GT pair counts as "Failed (missing)" — deflating matched% model-dependently.

**Fix:** add pattern fallbacks (`^CC\d` → SOC 2, `^16[024]\.` / `^§\s*16[024]` → HIPAA, `^Art(icle)?\.?\s*\d+` with regulation context) and print a count of unclassified criteria.

### 8. Tokens lost when sub-agent raises after partial findings (MEDIUM) — ✅ fixed (df0d74b)
`sentinel/graph/tools.py:426-446` — on the exception path `result` is `None`, so `sub_in = sub_out = 0` even though tokens up to the crash were billed; summary emits `Sub-agent tokens: 0 (0 in / 0 out)`, undercounting in `ui/server.py` cost display and `validate_run.py`.

**Fix:** attach a `UsageMetadataCallbackHandler` to `subagent.invoke` so token counts survive exceptions; same for the no-findings FAILED return at line 430.

### 9. Error-SOP regex misses one of two FAILED formats (MEDIUM) — ✅ fixed (7476466)
`scripts/validate_run.py:269` matches `^(SOP-...): FAILED` (from `tools.py:592/903`) but not `FAILED: {sop_id} — sub-agent error: ...` (from `tools.py:430`); those SOPs are undercounted in the error diagnostic.

**Fix:** add a second pattern `^FAILED: (SOP-[A-Z]+-\d+)`.

### 10. Compare paths crash on runs with no audit content (MEDIUM) — ✅ fixed (7476466)
`scripts/validate_run.py:501-503` (`compare_runs`) and `scripts/compare_audit_runs.py:55-58` call `parse_full_findings(run_data["content"])` without the `if not content` guard that `validate_single` (line 468) has — `content=None` raises `AttributeError`.

**Fix:** guard and report "no audit content" per run.

## Documented invariants that have drifted

### 11. `pinecone` imported at module level, violating the lazy-import rule (HIGH per CLAUDE.md) — ✅ fixed (4cf4f4c)
`sentinel/retrieval/regulations.py:4` — top-level `from pinecone import Pinecone`, while CLAUDE.md explicitly says it must be lazy ("Do not move these to top-level imports"); `sentinel/eval/naive_rag.py:8` imports this module at its own top level, so any environment without pinecone breaks at import time.

**Fix:** move the import inside `_get_index()`; use `TYPE_CHECKING` for the annotation.

### 12. Sub-agent recursion limit doc drift (LOW) — ⬜ open
`sentinel/graph/tools.py:424` sets `recursion_limit: 120`; CLAUDE.md documents 80. Also: test count is 76, CLAUDE.md says 73. Sync whichever is intended.

### 13. `_build_deep_agent` registers harness profile under wrong key (MEDIUM) — ✅ fixed (efd4911)
`sentinel/graph/agent.py:52-57` — key hardcoded as `f"openai:{MODEL}"` (the Nebius default) even when the agent runs gpt-5.5/Nemotron/Kimi/GLM, so the `GeneralPurposeSubagentProfile(enabled=False)` override never applies to 6 of 7 agents. Also, only `ImportError` is caught at call sites — a duplicate-registration error of another type crashes the LangGraph Cloud build (all 7 graphs build in one process).

**Fix:** derive the key from the actual provider/model passed in; broaden the fallback or guard re-registration.

### 14. `_build_agent_nebius_model` diverges from `_build_model` (MEDIUM) — ✅ fixed (efd4911)
`sentinel/graph/agent.py:109-118` vs `36-44` — Nemotron/Kimi/GLM outer agents skip the pooled `httpx.Client` and `REASONING_EFFORT` plumbing; both functions hardcode `16_000` instead of `config.MODEL_MAX_TOKENS`.

**Fix:** route both through one helper using `MODEL_MAX_TOKENS`; document if reasoning is intentionally off for those models.

## Robustness & performance

### 15. Re-ingestion leaves stale vectors (MEDIUM) — ✅ fixed (4cf4f4c)
`sentinel/retrieval/ingest.py:196-199`, `ingest_regulations.py:246-250` — upserts by deterministic ID without clearing the namespace; editing a source file to produce fewer chunks (or renaming it) leaves orphaned vectors polluting retrieval.

**Fix:** delete by ID prefix per file (or `delete_all` per namespace) before upserting.

### 16. No retry on embedding/query calls (MEDIUM) — ✅ fixed (4cf4f4c)
`sentinel/retrieval/ingest.py:125-135` — a single Nebius 5xx on one batch aborts the entire 2,386-chunk ingestion; `retrieve_regulation_text` also fails sub-agent RAG tool calls on transient errors.

**Fix:** retry per-batch `embeddings.create` (3 attempts, exponential backoff); same for `index.query` in `regulations.py:46`.

### 17. `load_sop_by_id` re-parses all 200 SOP files per call (MEDIUM) — ✅ fixed (942a6f1)
`sentinel/retrieval/local.py:11-40` — called once per sub-agent (`tools.py:389`), so a full audit does ~40,000 file parses.

**Fix:** cache a parsed index via `functools.lru_cache`; `list_all_sops` benefits from the same cache.

### 18. `/api/findings` does ~200 directory walks per request (MEDIUM) — ✅ fixed (2b8f6ea)
`ui/server.py:406-460` — for each of up to 100 Jira issues, `_sop_title`/`_sop_unit` each `rglob` the whole SOP tree; re-fetched after every audit (`audit.jsx:96`).

**Fix:** build a module-level `{sop_id: (path, title, unit)}` index once.

### 19. `list_regulations` makes 36 sequential Pinecone queries (LOW) — ⬜ open
`sentinel/graph/tools.py:86-98` — one round trip per regulation just to harvest metadata; multi-second tool call.

**Fix:** parallelize with a small thread pool, or precompute the inventory at ingest time.

### 20. UI: O(n²) markdown re-parse on every token + 200ms tick re-renders (MEDIUM) — ✅ fixed (2b8f6ea)
`primitives.jsx:290-299` + `audit.jsx:60` / `compare.jsx:90` — each token event re-renders the screen and re-runs `marked.parse` + `DOMPurify.sanitize` over the full growing answer (×3 streams on Compare).

**Fix:** buffer tokens in a ref and flush on ~150ms interval; render plain text while running and parse markdown once on done.

### 21. Non-string tool results crash the Audit screen (MEDIUM) — ✅ fixed (2b8f6ea)
`audit.jsx:90-91, 254-255` — `tc.result.startsWith(...)`/`match(...)` assume strings, but `_normalize_event` (`ui/server.py:567`) passes ToolMessage `content` through unmodified; a content-block list throws and blanks the screen.

**Fix:** coerce in the server: `text = content if isinstance(content, str) else json.dumps(content)`.

### 22. Eval screen crashes entirely on a missing numeric field (MEDIUM) — ✅ fixed (2b8f6ea)
`eval.jsx:194` (`a.latencyAvg.toFixed(1)`), `eval.jsx:13-14, 51, 57` — `mapEvalResults` (`app-forge.jsx:64-71`) defaults cost fields but passes `latency_avg_s`/`input_tokens`/`total` through raw; with no error boundary, one bad eval JSON unmounts the whole React tree.

**Fix:** default remaining numeric fields to 0 in `mapEvalResults`, or add per-screen error boundaries.

### 23. No Stop button; AbortController is dead code (LOW) — ⬜ open
`audit.jsx:35, 43-44` — `streamRef.current = ctrl` is never used; a long `audit_all_sops` run can't be cancelled. Pairs with finding 4 for server-side cancellation.

### 24. Stale aborted-stream `onError` can mark a fresh race run failed (LOW) — ⬜ open
`compare.jsx:61-125` — effect cleanup calls `ctrl.abort()`; the old stream's `onError` fires asynchronously and can flip the *new* run's agents to error.

**Fix:** ignore `err.name === "AbortError"` or check `ctrlRef.current === ctrl` before applying handler effects.

### 25. `naive_agent._extract_user_message` crashes on block-list content (MEDIUM) — ✅ fixed (401903e)
`sentinel/graph/naive_agent.py:47-58, 68` — `msg.content` can be a list of content blocks; `question.strip()` raises `AttributeError`, failing the whole graph run.

**Fix:** flatten list content to concatenated text of `{"type": "text"}` blocks.

### 26. Jira error bodies discarded; newline summaries rejected (MEDIUM/LOW) — ✅ fixed (401903e)
`sentinel/actuation/jira_client.py:59, 78` — `raise_for_status()` drops Jira's field-level 400 diagnostics, making failures undebuggable by the agent. `jira_client.py:50` — `summary[:240]` doesn't strip newlines, which Jira rejects.

**Fix:** raise a custom error including truncated `resp.text`; `" ".join(summary.split())[:240]`.

### 27. `create_jira_tickets` assumes every array element is a dict (LOW) — ⬜ open
`sentinel/graph/tools.py:843-845` — a string element raises uncaught `AttributeError` (only `json.loads` is guarded).

**Fix:** validate `isinstance(f, dict)` per element; add failures to the `failed` list.

### 28. `record_finding` validation stricter than the JSON-fallback normalizers (LOW) — ⬜ open
`sentinel/graph/tools.py:218-225` rejects `"non-compliant"`/`"noncompliant"` that `normalize_compliance_level` (`models.py:24-48`) maps fine — same model output bounces off the tool, costing an extra turn.

**Fix:** run inputs through `COMPLIANCE_LEVEL_ALIASES`/`SEVERITY_ALIASES` first.

### 29. Retrieval-budget race + wasted budget on empty queries (LOW) — ⬜ open
`sentinel/graph/tools.py:242-244, 268-271` — check-then-increment race on `_retrieval_calls["count"]` under parallel tool calls; `_search_web_capped` burns a budget unit before `search_web` rejects an empty query.

**Fix:** validate the query before decrementing budget; lock or accept slight overrun.

### 30. `config.MODEL` silently falls back to DeepSeek on unknown `NEBIUS_MODEL` (LOW) — ⬜ open
`sentinel/config.py:21` — a typo or full model id quietly selects `deepseek-v4-pro`.

**Fix:** accept values already in `NEBIUS_MODELS.values()` as-is; warn or raise on unknown keys.

### 31. Retrieval/ingest misc (LOW) — ⬜ open
- `sentinel/retrieval/local.py:34-35` — fuzzy-match score computed against title length even when the match was on SOP ID; score against the field that matched.
- `sentinel/retrieval/ingest_regulations.py:74-78` — `_detect_regulation` unanchored substring matching with insertion-order precedence; sort keys longest-first and use `startswith`.
- `ingest_regulations.py:101-109` — `===`-ruler sections lose their titles (header strips to `""`); take the next non-empty line.
- `sentinel/retrieval/regulations.py:80-91` — `format_regulation_context` emits dangling empty `### {reg}` headers after budget exhaustion and doesn't count header lines toward `max_chars`.

### 32. Minor security notes (LOW) — ⬜ open
`ui/server.py:257-259` — `/api/health` is exempt from the API-key gate yet returns internal `LANGGRAPH_URL`; trim to `{"ok": true}`. `_trace_url` (`ui/server.py:92-97`) exposes workspace-scoped LangSmith tenant/project UUIDs to any keyed client. Posture otherwise solid: fail-closed key gate with `secrets.compare_digest`, DOMPurify on agent markdown, `StaticFiles` handles traversal.

## Tests & plumbing

### 33. `test_json_parsing.py` tests copies of the logic, not the real code (HIGH) — ⬜ open
`tests/test_json_parsing.py:8-17` defines its own `COMPLIANCE_LEVEL_MAP`/`SEVERITY_MAP` and replicates the extraction logic instead of importing `_parse_findings_json` from `tools.py` — real code can drift while 19 tests stay green.

**Fix:** import the real symbols; test `_parse_findings_json` against truncated/fenced inputs.

### 34. Zero coverage on highest-risk paths (HIGH) — ⬜ open
- Retry + fan-out in `tools.py:523-643` (`_is_retryable`, token carry across attempts, aggregation) — untested.
- `validate_run.py` parsing/classification pipeline (`parse_full_findings`, `classify_regulation`, `worst_level`, `compute_metrics`) — produces headline benchmark numbers, only token-stats tested.
- Jira path (`jira_client.py` + ticket builders in `tools.py:646-873`) — untested; the JSON-array parser handles LLM-supplied input.

**Fix:** mocked-`run_one` retry tests; round-trip test feeding an `_audit_all_sops_impl`-shaped summary through `parse_full_findings`; unit-test `_build_jira_issue_fields`/`_render_ticket_description`/`create_jira_tickets` with httpx mocked.

### 35. Duplication worth consolidating (MEDIUM) — ◐ partial (59fd637: metrics consolidated; pricing registry + chunkers open)
- `compute_metrics`/`macro_f1` duplicated in `scripts/validate_run.py:298-358` and `sentinel/eval/metrics.py:62-186`; `validate_run.compare_runs` duplicates `compare_audit_runs.py` for the 2-run case.
- Agent labels/pricing hardcoded in `audit.jsx:3-8`, `compare.jsx:3-12`, `ui/server.py:99-109`, `app-forge.jsx:49-54`, plus `config.py:PRICING` — a price change touches 5 places. Also duplicated `Th`/`Td`, `truncate`, `summarizeArgs`, trace-link markup across JSX files. Consider an `/api/agents` registry endpoint and shared primitives.
- Three near-identical chunkers: `_chunk_txt`/`_chunk_md` (`ingest_regulations.py:88-189`) and `chunk_sop` (`ingest.py:79-101`); extract one `_chunk_sections` helper.

### 36. Plumbing fixes (LOW/MEDIUM) — ✅ fixed (1380e39)
- `Makefile:5-8` — `make install` fails on fresh clone: nothing creates `.venv`. Add a `.venv:` target as prerequisite; add `ingest-regulations` to `.PHONY`.
- `.env.example` missing `MAX_AUDIT_WORKERS`, `NEBIUS_MODEL`, `JIRA_DEFAULT_ISSUE_TYPE`, `LANGGRAPH_URL`.
- Stray untracked `test-results/` at repo root — add to root `.gitignore`.
- LangSmith project name `"sentinel-agent"` hardcoded in `validate_run.py:70/101/126`, `compare_audit_runs.py:40`, `inspect_tool_calls.py:85` — use `os.environ.get("LANGCHAIN_PROJECT", "sentinel-agent")`.
- `data.js:103-158` — ~120 lines of dead mock data (`auditFindings`, `sopStatus`, `toolStream`, `costMeter`); stale `evalResults` mock silently renders as real data if `/api/eval-results` fails.
- `scripts/requirements.txt` is stale (just `openai>=1.30.0`); `tiktoken` used by `inspect_tool_calls.py` only available transitively.

## Verified as fine (checked explicitly, no action needed)

- Message-type matching uses explicit set membership per the CLAUDE.md rule (`ui/server.py:557,566`).
- Token accounting: server gates on `AUDIT_TOOL_NAMES` and sums across multiple audit calls; values-mode usage overwrite is correct (full-state snapshots).
- Jira clients properly closed in `finally` blocks; ADF descriptions JSON-encoded (no injection path).
- `binary_compliance_metrics`/`macro_f1` math is correct; `GraphRecursionError` handled in `run_qa_eval.py`.
- All graph IDs referenced by the UI exist in `langgraph.json`.

## Suggested fix order

1. ~~Findings 1–2 (retry misclassification + multiplicative retries)~~ — fixed.
2. ~~Findings 5–7 (eval regex, NIST classification, dropped clause IDs)~~ — fixed.
3. ~~Findings 3–4 (UI stream tool-call attribution + run cancellation)~~ — fixed.
4. ~~Finding 11 (lazy-import violation)~~ — fixed.
5. ~~Remaining MEDIUMs (13–18, 20–22, 25–26, 36, metrics bullet of 35)~~ — fixed.

## Remaining work

1. Findings 33–34 (HIGH) — test the real `_parse_findings_json`, retry/fan-out paths, `validate_run` parsing pipeline, and the Jira ticket builders.
2. Finding 35, open bullets — agent label/pricing registry endpoint (5 duplicated sites) and `_chunk_sections` chunker consolidation.
3. LOWs as time permits: 12 (doc drift — note `recursion_limit` is now 120 and the suite is 76 tests), 19, 23, 24, 27–32.

### Fix-note deviations

- Finding 5: the suggested regex still let "not fully compliant" count as compliant (the engine skips the optional `fully` and matches at `compliant`); fixed-length lookbehinds including `(?<!not fully )` are anchored on `compliant` instead, and "not fully compliant" was added to the gap keywords.
- Finding 7: bare `Art. N` IDs remain unclassified — the per-finding lines carry no regulation context to disambiguate GDPR vs EU AI Act; `parse_full_findings` now prints the unclassified count instead.
- Finding 14: reasoning stays off for Nemotron/Kimi/GLM (documented in code) — the `thinking`/`reasoning_effort` chat-template kwargs are DeepSeek-specific.

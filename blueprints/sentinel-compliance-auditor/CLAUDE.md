# CLAUDE.md — Sentinel Agent

## What this project is

Sentinel is a regulatory compliance auditor agent that audits 200 synthetic SOPs for a fictional healthcare fintech (Meridian Health Technologies) against 36 regulation frameworks (HIPAA, SOC 2, GDPR, EU AI Act, NIST AI RMF, SR 11-7, California SB 53/SB 942/AB 853, BSA, ECOA, FCRA, PCI DSS, OWASP, FDA, NIST SP 800-series, EU AMLD4/ePrivacy/MDR/SCCs). Regulation text is retrieved from Pinecone via agentic RAG. Built for the Nebius Blueprint for Agents demo (Nebius Inflection, June 9, 2026).

## Quick reference

```bash
make install              # Install into .venv (includes dev, deep, rag extras)
make ingest               # Ingest SOPs into Pinecone
make ingest-regulations   # Ingest regulation texts into Pinecone (namespace: regulations)
make test                 # Run regression tests (150 tests, no API keys needed)
make dev                  # LangGraph dev server on port 2024
make ui                   # UI (FastAPI + React) on port 8080
make deploy               # Deploy to LangGraph Cloud (remote Docker build)
```

## Architecture decisions

### Regulation knowledge base (not hardcoded clauses)
Regulation texts live in `data/regulations/` as `.txt` and `.md` files. Regulation texts are chunked, embedded (Qwen3-Embedding-8B on Nebius, 4096 dimensions), and stored in Pinecone namespace `regulations`. Sub-agents retrieve raw text chunks via semantic search with metadata filtering by regulation name. Multiple retrieval calls per regulation, per SOP.

Key modules:
- `sentinel/retrieval/regulations.py` — Pinecone regulation text retrieval: `retrieve_regulation_text()`, `format_regulation_context()`
- `sentinel/retrieval/ingest_regulations.py` — chunks .txt/.md files, embeds, upserts into Pinecone
- `scripts/extract_pdf_text.py` — extracts text from regulation PDFs (pypdf) for ingestion

Ingestion/retrieval invariants:
- One section chunker: `chunk_sections()` in `ingest.py` is shared by `chunk_sop` and both regulation chunkers (parameterized by split pattern, header extractor, continuation prefix) — don't fork per-format copies
- Re-ingestion clears the target namespace before upserting (stale vectors from shrunken/renamed files must not pollute retrieval)
- Nebius embedding calls, Pinecone upserts, and `retrieve_regulation_text` queries are wrapped in `with_retries()` (3 attempts, backoff + jitter) — one 5xx must not abort a 16k-chunk ingestion or fail a sub-agent tool call
- SOP files are parsed once per process behind `_parsed_sops()` (lru_cache) in `retrieval/local.py`; call `_parsed_sops.cache_clear()` after editing SOP files in a live process

### Sub-agent architecture (not single-shot LLM calls)
Each SOP is audited by a dedicated ReAct sub-agent (`audit_single_sop` in `tools.py`) built with `langchain.agents.create_agent`. The sub-agent has its own tool loop with access to a regulation knowledge base, Tavily (web search), the SOP text, and a `record_finding` tool. It determines which regulations apply based on the SOP's content and business unit, queries the knowledge base for each applicable regulation, and calls `record_finding` for each assessed requirement. `audit_all_sops` fans out 200 sub-agents through a `ThreadPoolExecutor` (configurable via `MAX_AUDIT_WORKERS`). Do not revert to single-shot LLM calls.

Sub-agent tools (built per-invocation in `_build_subagent_tools()`):
- `record_finding` — records a single audit finding into a closure-scoped list; called per requirement as the sub-agent assesses it, so partial progress survives truncation. Inputs are normalized through `COMPLIANCE_LEVEL_ALIASES`/`SEVERITY_ALIASES` first, so e.g. `"non-compliant"` records as `gap` instead of bouncing and costing an extra turn
- `retrieve_regulation_rag` — semantic search on Pinecone `regulations` namespace with optional regulation filter
- `search_web` — Tavily advanced search for latest guidance/enforcement
- `read_sop` — returns the full SOP text (closure over the loaded content)

`retrieve_regulation_rag` and `search_web` share a 30-call retrieval budget per sub-agent. Consumption is an atomic check-and-increment behind a lock (parallel tool calls must not race past the limit), and inputs are validated *before* consuming, so a rejected empty query doesn't burn a unit.

Finding extraction uses two phases: (1) tool-recorded findings from `record_finding` calls, (2) JSON parsing from the final message as a backwards-compatible fallback. Truncation is detected via `finish_reason=length` on the last AI message and surfaced explicitly. Each `_audit_single_sop_impl` call returns a `SopAuditResult(summary, findings, input_tokens, output_tokens, status, rate_limited)` — results are aggregated by value, not stored in shared module state, so repeated/concurrent audits in one process can't contaminate each other's totals. Token counts are accumulated in a `UsageMetadataCallbackHandler` attached to `subagent.invoke`, so they survive mid-run exceptions (tokens up to a crash were still billed).

Sub-agent invocations are wrapped in a try/except — transient errors (e.g. Nebius 504 timeouts) return a `SopAuditResult` with `status="failed"` (its summary still reads `"FAILED: ..."` for humans) so the per-SOP retry loop can re-attempt. Retry classification reads the structured `status`/`rate_limited` fields, never the summary text — model-written prose can legitimately contain words like "FAILED". If findings were already recorded via `record_finding` before the error, those findings are preserved.

Retries are per-SOP only: `_audit_single_sop_with_retry` makes up to `MAX_RETRIES` (4) re-attempts with backoff (longer when `rate_limited`), accumulating tokens across attempts. The batch orchestrators (`audit_sops`, `audit_all_sops`) call it once per SOP — do NOT re-add a batch-level retry layer on top; stacking the two multiplied to MAX_RETRIES² sub-agent runs per stubborn SOP. Statuses `truncated` (would truncate again) and `invalid` (bad input) are not retried.

### Multi-model support
- **Prototype** (`sentinel_prototype`): GPT-5.5 via OpenAI API — no Tavily
- **Grounded** (`sentinel_grounded`): GPT-5.5 via OpenAI API + Tavily web search
- **Optimized** (`sentinel_optimized`): DeepSeek-V4-Pro on Nebius (`https://api.tokenfactory.nebius.com/v1/`) + Tavily
- **Production** (`sentinel_nemotron`): Nemotron-3-Ultra-550b on Nebius + Tavily
- **Additional**: Kimi-K2.6 (`sentinel_kimi`), GLM-5.1 (`sentinel_glm`) via `_build_agent_nebius_model()`
- `model_name` is threaded through `build_tools()` → `_audit_single_sop_impl()` → `_build_subagent_model()` so sub-agents use the same model as the outer agent
- All models set `max_tokens` (`MODEL_MAX_TOKENS` = 16000) on the outer agent and sub-agents. Every Nebius model accepts it directly; for OpenAI reasoning models `ChatOpenAI` remaps it to `max_completion_tokens` (the raw OpenAI API rejects `max_tokens`)
- Provider switching is handled by `_build_model()` in `agent.py` — the single outer-model factory (pooled httpx client, `MODEL_MAX_TOKENS`, reasoning plumbing) used by all agents including the Nemotron/Kimi/GLM variants. Reasoning is intentionally off for those alternates: the `thinking`/`reasoning_effort` chat-template kwargs are DeepSeek-specific
- `_build_deep_agent` derives its harness-profile key from the model instance (`model.model_name`), not the config default — a hardcoded key silently skips the `GeneralPurposeSubagentProfile(enabled=False)` override for every other agent. Registration is guarded so re-registering (all 7 graphs build in one process) can't crash the LangGraph Cloud build
- An unknown `NEBIUS_MODEL` value raises at import (`config.py`) instead of silently falling back to DeepSeek; full model ids from `NEBIUS_MODELS.values()` are accepted as-is

### Recursion limits
- **Outer agent**: 25 graph nodes — set via `LANGGRAPH_DEFAULT_RECURSION_LIMIT` env var for cloud deployment. Typical runs use ~11 nodes.
- **Sub-agents**: 120 graph nodes — set in `_audit_single_sop_impl()` at `subagent.invoke()`. Typical sub-agents use 25–37 nodes (p95=37, max observed=65).

### deepagents optional dependency
`deepagents` is an optional dep (`[deep]` extra). It's lazy-imported in `agent.py` inside `_build_deep_agent()`. If the import fails, we fall back to `langchain.agents.create_agent`. This is required because deepagents pulls heavy transitive deps (grpcio, google-genai) that conflict with LangGraph Cloud's constraint file.

### Jira actuation
When an audit finding is a gap or partial at medium+ severity, the `create_jira_ticket` tool files a single ticket and `create_jira_tickets` files multiple tickets in batch (accepts a JSON array string; non-object elements land in the failed list, not an exception). Both are available to the outer Sentinel agent. The Jira client (`sentinel/actuation/jira_client.py`) uses the REST API v3 with basic auth (email + API token). API failures raise `JiraError` carrying the truncated response body so the agent sees Jira's field-level diagnostics; issue summaries collapse internal whitespace before the 240-char truncation (Jira rejects newlines). Ticket description is rendered in Atlassian Document Format (ADF). Labels include `sentinel`, `compliance-finding`, severity, regulation slug, and SOP slug. Configuration via `JIRA_BASE_URL`, `JIRA_EMAIL`, `JIRA_API_TOKEN`, `JIRA_PROJECT_KEY`, and optionally `JIRA_DEFAULT_ISSUE_TYPE` (default: Task).

### Lazy imports for cloud compatibility
`tavily` (in sub-agent tools in `tools.py`), `pinecone` (in `retrieval/ingest.py`, `retrieval/regulations.py`, `tools.py`), `openai` (in `retrieval/ingest.py`), and `httpx` (in `actuation/jira_client.py`) are imported lazily inside functions, not at module level. This prevents import failures in the LangGraph Cloud container where these packages may not be installed or configured. Do not move these to top-level imports.

## Key modules

| Module | Purpose |
|--------|---------|
| `sentinel/graph/agent.py` | Agent builders (`agent_prototype`, `agent_grounded`, `agent_optimized`, `agent_nemotron`) |
| `sentinel/graph/tools.py` | LangChain `@tool` definitions: `audit_single_sop` (sub-agent), `audit_sops`, `audit_all_sops`, `list_sops`, `list_regulations`, `retrieve_regulation_text_tool`, `create_jira_ticket`, `create_jira_tickets`; sub-agent builder `_build_subagent_tools()` with `record_finding` tool |
| `sentinel/chat_model.py` | `build_chat_model()` — single `ChatOpenAI` factory (provider/model/temperature/max_tokens/reasoning) used by the outer agent, sub-agents, and eval modules |
| `sentinel/token_accounting.py` | Single source of truth for the token-line emit format, parse regexes, and audit tool-name set; `tools.py` emits via `format_*`, `ui/server.py` + `scripts/validate_run.py` parse via `parse_tokens_from_result` / `sum_sub_agent_tokens` |
| `sentinel/models.py` | Pydantic models (`AuditFinding`, `SOPChunk`, `AuditMetrics`), enums (`ComplianceLevel`, `Severity`), shared alias maps (`COMPLIANCE_LEVEL_ALIASES`, `SEVERITY_ALIASES`) + normalizers |
| `sentinel/eval/metrics.py` | The single implementation of `compute_metrics`/`macro_f1`/`binary_compliance_metrics` + `extract_compliance_level`; `scripts/validate_run.py` wraps it — don't duplicate the confusion-matrix math |
| `sentinel/config.py` | API keys, model names, paths, pricing, business unit list |
| `sentinel/retrieval/local.py` | SOP loading: `list_all_sops()`, `load_sop_by_id()`, `load_sop_chunks()` |
| `sentinel/retrieval/regulations.py` | Pinecone regulation text retrieval: `retrieve_regulation_text()`, `format_regulation_context()` |
| `sentinel/retrieval/ingest_regulations.py` | Regulation text chunker + Pinecone ingestion (`REGULATION_MAP`, `EDITION_PATTERNS`, edition metadata) |
| `sentinel/retrieval/ingest.py` | SOP markdown parser (`parse_sop()`), chunker, Pinecone ingestion |
| `sentinel/actuation/jira_client.py` | Sync Jira Cloud REST client used by the `create_jira_ticket` tool |
| `ui/server.py` | FastAPI backend: serves static UI, the agent registry (`/agents.js`), SSE audit streaming (cancels LangGraph runs on client disconnect), eval results, Jira findings, KB stats |
| `ui/static/components-forge/audit.jsx` | Audit screen: composer, agent picker, live stream with Meter metrics, Jira findings register |
| `ui/static/components-forge/eval.jsx` | Evaluation screen: multi-agent benchmark dashboard (recall, cost, confusion matrices, per-category table) |
| `ui/static/components-forge/compare.jsx` | Compare screen: side-by-side agent race with parallel SSE streams |
| `scripts/validate_run.py` | Audit quality evaluation: compares LangSmith run output against compliance matrix |
| `scripts/compare_audit_runs.py` | Side-by-side comparison of N audit runs: quality, cost, tokens, latency, tool-call counts |
| `scripts/run_qa_eval.py` | Q&A eval runner: naive, prototype, grounded, optimized, production modes |
| `scripts/inspect_tool_calls.py` | LangSmith tool call inspector: shows all tool calls with args, timing, and output token counts for a run (`--show-output`, `--json`) |

## LangGraph Cloud deployment

- Config: `langgraph.json` — points to `sentinel/graph/agent.py:agent` as the graph entry
- Uses Python 3.12, Wolfi Linux image, reads `.env` for secrets
- Cloud URL: `https://sentinel-agent-c4dfa65772015432b388f980262380a8.us.langgraph.app`
- The `.dockerignore` excludes `scripts/`, `ui/`, `tests/` from the cloud image
- `setuptools` is configured with `include = ["sentinel*"]` in `pyproject.toml` to avoid packaging `scripts/` as a top-level package

## Data

### Quality evaluation
- `scripts/validate_run.py` fetches audit run data from LangSmith and compares against the compliance matrix
- Takes LangSmith run IDs as arguments — fetches run metadata (model, timing, tokens, cost) and audit content automatically
- Parses the `audit_all_sops` text output, classifies findings by regulation (criterion prefix matching + bare clause-ID fallbacks: `CC6.1` → SOC 2, `164.312…`/`§ 164…` → HIPAA; only the AI RMF maps to "NIST AI RMF" — other NIST docs return None), aggregates to worst compliance level per (SOP, regulation) pair
- The emit↔parse contract between the audit summary format (`tools.py`) and `parse_full_findings` is locked by a round-trip test (`tests/test_validate_run_pipeline.py`) — changing either side fails the suite
- LangSmith project name comes from `LANGCHAIN_PROJECT` (default `sentinel-agent`) in all three scripts
- Metrics: matched %, false positive % (too strict), false negative % (too lenient), failed % (missing), per-class F1, macro F1, per-regulation accuracy, directional bias, tokens, cost, latency
- Usage: `python3 scripts/validate_run.py <run_id>` (single run), `python3 scripts/validate_run.py <run_id1> <run_id2>` (side-by-side comparison), `--original` flag for original matrix
- Content extraction: tries `audit_all_sops` tool run output first, then root run outputs, then Prompt chain runs (for pending runs with null outputs)
- `data/compliance_matrix_revised.json` is a corrected copy with 16 SOC 2 level changes (15 gap→partial, 1 partial→compliant) based on manual SOP-vs-regulation review

### SOPs
- 200 SOPs across 10 business units in `data/sops/` (markdown with YAML frontmatter)
- SOP frontmatter `regulations` field is informational — the sub-agent determines applicable regulations dynamically
- 152 of 200 SOPs are tagged with SOC 2 or HIPAA (the rest cover EU AI Act, GDPR, etc.)
- Compliance matrix ground truth: `data/compliance_matrix.json`
- SOP generation scripts in `scripts/` (one-time use, not part of the agent)

### Regulations
- 36 regulation frameworks in `data/regulations/` as .txt, .md, .pdf, and .xml files
- 16,289 chunks ingested into Pinecone namespace `regulations` (from 43 .txt/.md source files, including PDF-extracted texts; re-ingested 2026-06-10 — the namespace is cleared on each re-ingest, so the index holds exactly the current files' chunks)
- Historical editions: HIPAA (2017, 2020, 2024, current), NIST AI RMF (2022 drafts, final), EU AI Act (2021 proposal, final)
- SOC 2 (AICPA) and PCI DSS (PCI SSC) texts are copyrighted: they live locally in `data/regulations/` and are ingested, but are **gitignored and must never be committed** — see `data/regulations/README.md` for download instructions if missing
- Each chunk carries `regulation`, `edition`, `section`, and `source` metadata for filtered retrieval
- PDFs are extracted to .txt via `scripts/extract_pdf_text.py` (pypdf) before ingestion
- See `data/regulations/README.md` for full file inventory and sources

## Integrations

### LangSmith MCP
Remote MCP server configured in `.mcp.json` (`https://api.smith.langchain.com/mcp`). Uses OAuth — authenticate via browser on first use. Provides access to LangSmith traces, runs, datasets, experiments, and prompt hub from Claude Code and Codex. Key tools: `fetch_runs` (inspect audit traces), `list_projects`, `list_datasets`, `run_experiment`, `get_billing_usage`.

### Jira Cloud
The `create_jira_ticket` (single) and `create_jira_tickets` (batch, accepts JSON array string) tools file compliance findings as tickets via the Jira Cloud REST API v3. Client: `sentinel/actuation/jira_client.py` (sync, basic auth). Ticket descriptions use Atlassian Document Format (ADF). Labels: `sentinel`, `compliance-finding`, severity, regulation slug, SOP slug. Priority mapped from severity (critical→Highest, high→High, medium→Medium, low→Low). Config: `JIRA_BASE_URL`, `JIRA_EMAIL`, `JIRA_API_TOKEN`, `JIRA_PROJECT_KEY`.

## Environment variables

Required: `NEBIUS_API_KEY` (and `UI_API_KEY` for the UI server, which refuses to start without it). Optional: `OPENAI_API_KEY` (Prototype/Grounded agents), `PINECONE_API_KEY` (Pinecone RAG), `TAVILY_API_KEY` (grounding), `LANGSMITH_API_KEY` (tracing + cloud auth), `JIRA_BASE_URL` / `JIRA_EMAIL` / `JIRA_API_TOKEN` / `JIRA_PROJECT_KEY` / `JIRA_DEFAULT_ISSUE_TYPE` (Jira actuation). Tuning: `NEBIUS_MODEL` (model key — unknown values raise at import), `MAX_AUDIT_WORKERS` (fan-out width, default 10), `LANGGRAPH_URL` (LangGraph server the UI talks to), `LANGCHAIN_PROJECT` (LangSmith project for the eval scripts). `LANGGRAPH_DEFAULT_RECURSION_LIMIT` sets the outer agent recursion limit for cloud deployment (default: 25). See `.env.example`.

## Patterns to follow

- The outer agent (Sentinel) uses `langchain_openai.ChatOpenAI` via `_build_model()` in `agent.py`
- Sub-agents (`audit_single_sop`) also use `ChatOpenAI` directly via `_build_subagent_model()`
- Tools in `sentinel/graph/tools.py` are decorated with `@tool` from `langchain_core.tools`
- Audit results are returned by value as `SopAuditResult` and aggregated per top-level audit call (no shared module-level accumulator); the fan-out orchestrators sum each run's own findings and tokens
- SOP lookup (`load_sop_by_id`) supports exact ID, exact title, and fuzzy substring matching
- The sub-agent determines which regulations apply — there is no predefined SOP-to-regulation mapping
- Regulation retrieval uses metadata filters (`regulation`, `edition`) on the Pinecone `regulations` namespace
- JSON parsing from sub-agent responses scans messages in reverse, strips markdown code fences, repairs truncated arrays, and maps unexpected enum values through `COMPLIANCE_LEVEL_ALIASES`/`SEVERITY_ALIASES` in `models.py` (the same maps `record_finding` and the eval scorers use — there is one set of aliases)
- All `ChatOpenAI` instances must set `stream_usage=True` — without it, custom `base_url` providers (Nebius, OpenAI) don't send `stream_options: {include_usage: true}` and `usage_metadata` is always `None` in thread state
- Token pricing is centralized in `PRICING` dict in `config.py`; the UI gets agent labels/graph ids/pricing from `/agents.js`, generated by `ui/server.py` from its agent registry + `PRICING` (read in the JSX as `window.SENTINEL_AGENTS`) — do not hardcode prices or labels in the JSX
- Sub-agent token usage is carried on `SopAuditResult` (accumulated across retry attempts) and included in tool result strings as `Sub-agent tokens: X (X in / X out)`. The emit format and the parser live together in `sentinel/token_accounting.py` — `tools.py` emits via `format_total_tokens`/`format_sub_agent_tokens`, and both consumers (`ui/server.py`, `scripts/validate_run.py`) parse via it, gated on `AUDIT_TOOL_NAMES` so a `read_file` re-read of offloaded audit output isn't double-counted. Consumers must sum across multiple audit calls in a run (each reports only its own sub-agents)
- Available Nebius models are in `NEBIUS_MODELS` dict in `config.py` — select via `NEBIUS_MODEL` env var (keys: `deepseek-v4-pro`, `nemotron`, `kimi-k2`, `glm-5`); unknown values raise at import rather than silently selecting DeepSeek
- The LangGraph SDK (via `messages-tuple` stream mode) serializes messages with short-form types: `"ai"` / `"AIMessageChunk"` for AI messages, `"tool"` for ToolMessages, `"human"` for user messages. Do not use substring matching (e.g. `"ToolMessage" in msg_type`) — use explicit set membership (`msg_type in ("tool", "ToolMessage", "ToolMessageChunk")`)
- SSE streaming: `_normalize_event` emits one `tool_call` event per entry (with its `id`); `tool_result` events carry `tool_call_id` and the JSX matches by id (LIFO fallback for id-less payloads). Non-string ToolMessage content is coerced to a JSON string server-side. On client disconnect (including the UI Stop button), `_drain_sse`'s `finally` sets a cancel event and producers call `runs.cancel` — abandoned streams must not keep burning tokens
- `message content` can be a string or a list of content blocks — flatten before calling string methods (see `naive_agent._content_to_text`)

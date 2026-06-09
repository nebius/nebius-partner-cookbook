# AGENTS.md — Sentinel Agent

## What this project is

Sentinel is a regulatory compliance auditor agent that audits 200 synthetic SOPs for a fictional healthcare fintech (Meridian Health Technologies) against 36 regulation frameworks. Regulation text is retrieved from Pinecone via agentic RAG. Built for the Nebius Blueprint for Agents demo (Nebius Inflection, June 9, 2026).

## Quick reference

```bash
make install              # Install into .venv (includes dev, deep, rag extras)
make ingest               # Ingest SOPs into Pinecone
make ingest-regulations   # Ingest regulation texts into Pinecone (namespace: regulations)
make test                 # Run regression tests (58 tests, no API keys needed)
make dev                  # LangGraph dev server on port 2024
make ui                   # UI (FastAPI + React) on port 8080
make deploy               # Deploy to LangGraph Cloud (remote Docker build)
```

## Architecture

### LangGraph agents (langgraph.json)

| Graph ID | Builder | Model | Description |
|----------|---------|-------|-------------|
| `sentinel_prototype` | `agent_prototype()` | GPT-5.5 | Baseline: OpenAI, no Tavily |
| `sentinel_grounded` | `agent_grounded()` | GPT-5.5 | OpenAI + Tavily web search |
| `sentinel_optimized` | `agent_optimized()` | DeepSeek-V4-Pro | Nebius + Tavily |
| `sentinel_nemotron` | `agent_nemotron()` | Nemotron-3-Ultra-550b | Nebius testing endpoint + Tavily |
| `sentinel_naive` | `agent_naive()` | DeepSeek-V4-Pro | Single retrieval + single LLM call, no tools |
| `sentinel_kimi` | `agent_kimi()` | Kimi-K2.6 | Nebius + Tavily |
| `sentinel_glm` | `agent_glm()` | GLM-5.1 | Nebius + Tavily |

### Sub-agent architecture
Each SOP is audited by a dedicated ReAct sub-agent with access to regulation retrieval, web search, the SOP text, and a `record_finding` tool. Sub-agents call `record_finding` per requirement as they go — partial progress survives truncation or errors. Retrieval calls are capped at 30 per SOP.

Sub-agent tools:
- `record_finding` — records a single finding into a closure-scoped list
- `retrieve_regulation_rag` — regulation knowledge base (Pinecone semantic search)
- `search_web` — Tavily web search (capped)
- `read_sop` — full SOP text

### Outer agent tools
- `list_sops` — search/discover SOPs (with synonym mapping for FDA, SaMD, AI/ML, etc.)
- `audit_single_sop` — audit one SOP via sub-agent
- `audit_sops` — audit a list of SOPs in parallel
- `audit_all_sops` — audit all 200 SOPs (expensive: $30–140, 15–90 min)
- `list_regulations` / `retrieve_regulation_text_tool` — regulation lookup
- `search_web` — Tavily web search
- `create_jira_ticket` — file a single Jira ticket
- `create_jira_tickets` — file multiple Jira tickets (JSON array string)

## Key modules

| Module | Purpose |
|--------|---------|
| `sentinel/graph/agent.py` | Agent builders |
| `sentinel/graph/tools.py` | All `@tool` definitions, sub-agent builder, prompts |
| `sentinel/graph/naive_agent.py` | Naive RAG baseline graph |
| `sentinel/models.py` | Pydantic models, enums |
| `sentinel/config.py` | API keys, model names, pricing |
| `sentinel/retrieval/local.py` | SOP loading and search |
| `sentinel/retrieval/regulations.py` | Pinecone regulation retrieval |
| `sentinel/retrieval/ingest.py` | SOP ingestion to Pinecone |
| `sentinel/retrieval/ingest_regulations.py` | Regulation text ingestion (36 frameworks) |
| `sentinel/actuation/jira_client.py` | Jira Cloud REST client |
| `sentinel/eval/agentic_qa.py` | Q&A eval agent |
| `sentinel/eval/judge.py` | LLM-as-judge (always uses DeepSeek) |
| `ui/server.py` | FastAPI backend: SSE streaming, eval results, Jira findings |
| `ui/static/components-forge/` | React UI: Audit, Compare, Evaluation screens |
| `scripts/validate_run.py` | Audit quality evaluation against compliance matrix |
| `scripts/run_qa_eval.py` | 120-question Q&A eval runner |
| `scripts/compare_audit_runs.py` | Side-by-side audit run comparison |

## Environment variables

Required: `NEBIUS_API_KEY`. Optional: `OPENAI_API_KEY`, `PINECONE_API_KEY`, `TAVILY_API_KEY`, `LANGSMITH_API_KEY`, `NEBIUS_TESTING_API_KEY` (Nemotron), `JIRA_BASE_URL` / `JIRA_EMAIL` / `JIRA_API_TOKEN` / `JIRA_PROJECT_KEY`. See `.env.example`.

## Patterns to follow

- All `ChatOpenAI` instances must set `stream_usage=True`
- Sub-agents use `record_finding` for incremental output — do not revert to final-message JSON
- Retrieval calls capped at 30 per SOP to prevent runaway loops
- Truncation is not retryable — only transient errors (429, 504) are retried with jitter
- Lazy imports for cloud compatibility: `tavily`, `pinecone`, `openai`, `httpx` inside functions
- Token pricing centralized in `PRICING` dict in `config.py`
- `model_name` threaded through `build_tools()` → sub-agents so alternate models work end-to-end
- All models set `max_tokens` (`MODEL_MAX_TOKENS` = 16000); every Nebius model accepts it, while `ChatOpenAI` remaps it to `max_completion_tokens` for OpenAI reasoning models (the raw OpenAI API rejects `max_tokens`)
- Judge always uses DeepSeek regardless of `NEBIUS_MODEL` env var

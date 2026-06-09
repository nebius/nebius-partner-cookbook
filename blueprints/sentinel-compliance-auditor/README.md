# Sentinel — Regulatory Compliance Auditor Agent

Sentinel is an AI-powered compliance auditor that assesses 200 enterprise SOPs against 36 regulation frameworks (HIPAA, SOC 2, GDPR, EU AI Act, NIST AI RMF, SR 11-7, California SB 53/SB 942/AB 853, BSA, ECOA, FCRA, PCI DSS, OWASP, FDA, NIST SP 800-series, EU AMLD4/ePrivacy/MDR/SCCs). Regulation text is retrieved from Pinecone via agentic RAG. Built for the [Nebius Blueprint for Agents](https://nebius.com/) demo (Nebius Inflection, June 9, 2026).

## Architecture

```
User Query (via UI or LangGraph API)
    |
    v
+-----------------------------------+
|  Sentinel Outer Agent             |  LangGraph ReAct (+ deepagents)
|  Prototype / Grounded / Optimized |  GPT-5.5 or DeepSeek-V4-Pro
|  / Production (Nemotron Ultra)    |  or Nemotron-3-Ultra-550b
+-----------------------------------+
    |
    +---> list_sops (search/discover SOPs, synonym mapping)
    |
    +---> audit_sops / audit_all_sops (ThreadPoolExecutor fan-out)
    |         |
    |         v  (per SOP, up to MAX_AUDIT_WORKERS in parallel)
    |    +----------------------------+
    |    |  Sub-Agent (sop_auditor)   |  LangGraph ReAct
    |    |  Same model as outer agent |  Retrieval capped at 30 calls
    |    +----------------------------+
    |         |
    |         +---> read_sop (full SOP text)
    |         +---> retrieve_regulation_rag (Pinecone semantic search)
    |         +---> search_web (Tavily, capped)
    |         +---> record_finding (per requirement, survives truncation)
    |         |
    |         v
    |    Returns SopAuditResult(findings, tokens) — aggregated by value per
    |    audit call (no shared global; concurrency-safe). Emits a token line
    |    parsed by the UI + validate_run via sentinel/token_accounting.py
    |
    +---> create_jira_ticket / create_jira_tickets (batch)
    |         |
    |         v
    |    Jira Cloud REST API → tickets on Kanban board
    |
    +---> search_web (outer agent, for ad-hoc questions)
    +---> list_regulations / retrieve_regulation_text_tool
```

**Models:** Nemotron-3-Ultra-550b (Production), DeepSeek-V4-Pro (Optimized), GPT-5.5 (Prototype/Grounded) on Nebius + OpenAI, all built via `build_chat_model` (`chat_model.py`)
**Orchestration:** LangGraph ReAct agent with per-SOP sub-agents, optional deepagents upgrade
**Retrieval:** Pinecone vector search (Qwen3-Embedding-8B, 4096 dims)
**Grounding:** Tavily live regulation search
**Observability:** LangSmith tracing with cost tracking; token-line emit/parse centralized in `sentinel/token_accounting.py` (summed per audit call by UI + `validate_run.py`)
**Actuation:** Jira Cloud REST API for filing compliance gap tickets
**Deployment:** LangGraph Cloud + UI (FastAPI + React)

## Quickstart

### Prerequisites

- Python 3.11+
- API keys: Nebius, OpenAI, Pinecone, Tavily (optional), LangSmith (optional)

### Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
make install
```

Copy `.env.example` to `.env` and fill in your API keys:

```bash
cp .env.example .env
```

### Ingest data

```bash
make ingest               # SOPs into Pinecone
make ingest-regulations   # Regulation texts into Pinecone (namespace: regulations)
```

### Run the demo

```bash
make dev     # LangGraph dev server on port 2024
make ui      # UI on port 8080 (connects to LangGraph)
```

`UI_API_KEY` is **required** — set it in `.env` first (e.g. `openssl rand -hex 32`);
the UI server refuses to start without it, even locally. Then open
http://localhost:8080: the UI prompts for the key on load and sends it as an
`X-API-Key` header on every request, and the server rejects any `/api/*` call
without it (so no agent run, Pinecone, or Jira call happens for an unauthenticated
caller).

### Test

```bash
make test    # Run all 73 regression tests
```

Tests cover JSON parsing/repair, SOP loading, metrics, and config validation. No API keys or external services required.

### Deploy

```bash
# Local development
make dev          # LangGraph dev server on port 2024
make ui           # UI on port 8080

# Cloud deployment
make deploy       # Deploy to LangGraph Cloud
```

**Exposing the UI publicly:** `make ui` binds `0.0.0.0:8080`. Before putting it on
a public address, set a strong `UI_API_KEY` (e.g. `openssl rand -hex 32`) to gate
the API, and front the server with a reverse proxy / load balancer that
terminates **TLS** and applies **rate limiting** — those are intentionally left to
the proxy layer rather than the app.

## Audit Approach

Sentinel fans out by SOP using a sub-agent architecture. Each SOP is audited by a dedicated LangGraph ReAct sub-agent that:

1. Reads the full SOP text
2. Determines which regulations apply based on content and business unit
3. Queries the regulation knowledge base via Pinecone vector search (multiple keyword queries per regulation)
4. Optionally searches the web for latest guidance
5. Calls `record_finding` for each assessed requirement — findings are captured incrementally so partial progress survives truncation or errors

`audit_all_sops` fans out sub-agents through a `ThreadPoolExecutor` (configurable via `MAX_AUDIT_WORKERS`).

Key tools:
- `audit_all_sops` — full audit across all 200 SOPs in parallel
- `audit_single_sop` — audit one SOP via a dedicated sub-agent
- `list_sops` — search and discover SOPs by title, ID, or business unit
- `list_regulations` — list all regulations in the knowledge base
- `retrieve_regulation_text_tool` — look up specific regulation requirements
- `create_jira_ticket` — file a Jira ticket for a compliance gap or partial finding

## Project Structure

```
sentinel_agent/
├── sentinel/                  # Core agent package
│   ├── config.py              # API keys, model config, pricing, paths
│   ├── models.py              # Pydantic models (AuditFinding, SOPChunk, AuditMetrics)
│   ├── chat_model.py          # build_chat_model() — single ChatOpenAI factory
│   ├── token_accounting.py    # Token-line emit format + parser (shared by tools/UI/eval)
│   ├── graph/
│   │   ├── agent.py           # ReAct agent (deepagents fallback to LangGraph)
│   │   └── tools.py           # LangChain tools: sub-agent auditing + retrieval
│   ├── retrieval/
│   │   ├── local.py           # SOP file loading and search
│   │   ├── regulations.py     # Pinecone regulation text retrieval
│   │   ├── ingest.py          # SOP -> Pinecone ingestion
│   │   └── ingest_regulations.py  # Regulation text -> Pinecone ingestion
│   ├── actuation/
│   │   └── jira_client.py     # Jira Cloud REST client
├── scripts/
│   ├── validate_run.py        # Audit quality evaluation against compliance matrix
│   ├── inspect_tool_calls.py  # LangSmith tool call inspector (args, timing, tokens)
│   ├── generate_sops.py       # SOP generation (one-time)
│   ├── extract_pdf_text.py    # PDF -> text extraction for regulations
│   └── sop_taxonomy.py        # SOP definitions + metadata
├── data/
│   ├── sops/                  # 200 generated SOPs (10 business units)
│   ├── regulations/           # 36 regulation frameworks (txt, md, pdf, xml)
│   ├── company_profile.md     # Meridian Health Technologies background
│   ├── compliance_matrix.json # Ground truth
│   └── compliance_matrix_revised.json # Revised ground truth (16 SOC 2 corrections)
├── langgraph.json             # LangGraph deployment config
├── pyproject.toml             # Dependencies
├── Makefile                   # Build/run targets
└── .env.example               # API key template
```

## Quality Evaluation

`scripts/validate_run.py` measures audit quality by comparing a LangSmith run's output against the compliance matrix ground truth.

```bash
# Validate a single run (uses revised matrix by default)
python3 scripts/validate_run.py <langsmith-run-id>

# Compare two runs side by side
python3 scripts/validate_run.py <run-id-1> <run-id-2>

# Use original (uncorrected) matrix
python3 scripts/validate_run.py --original <run-id>
```

The script fetches run data from LangSmith (model, timing, tokens, cost, audit content), parses the `audit_all_sops` output, classifies each finding by regulation, aggregates to worst compliance level per (SOP, regulation) pair, and reports:

- **Matched %** — exact agreement with ground truth
- **False positive %** — agent predicted stricter than ground truth (e.g. gap when matrix says partial)
- **False negative %** — agent predicted more lenient than ground truth
- **Per-class F1** — precision/recall/F1 for compliant, partial, and gap detection
- **Failed %** — SOP-regulation pairs missing from run output (504 errors, no structured findings)
- **Per-regulation accuracy** — breakdown across HIPAA, SOC 2, GDPR, etc.
- **Cost, tokens, latency** — from LangSmith run metadata and parsed sub-agent token counts

`data/compliance_matrix_revised.json` contains 16 SOC 2 corrections (15 gap→partial, 1 partial→compliant) based on manual review of SOP content against the SOC 2 Trust Services Criteria.

## Company Profile

**Meridian Health Technologies** is a fictional AI-powered healthcare fintech that:
- Provides AI-driven clinical decision support and diagnostic tools
- Operates healthcare payment processing, lending, and fraud detection
- Manages patient data across EU and US jurisdictions
- Deploys ML models for credit scoring and risk assessment

## Regulation Coverage

9 core regulation frameworks with full text in the Pinecone index:

- **HIPAA Security Rule** — Administrative (164.308), Physical (164.310), Technical (164.312) safeguards
- **SOC 2 Trust Services Criteria** — CC1 through CC9
- **GDPR** — Data protection, privacy rights, cross-border transfers
- **EU AI Act** — High-risk AI system requirements, conformity assessments
- **NIST AI RMF** — AI risk management framework
- **SR 11-7** — Model risk management (banking/fintech)
- **California AI Laws** — SB 53, SB 942, AB 853

Historical editions are included for temporal analysis (e.g., HIPAA 2017/2020/2024, EU AI Act proposal vs. final).

27 additional external standards referenced by SOPs are also available in `data/regulations/`: 11 NIST special publications (SP 800-53, 800-88, 800-61, CSF 2.0, 800-63B, 800-207, 800-34, 1270, Privacy Framework, 800-161, 800-218), 5 FDA/eCFR titles (21 CFR Parts 820, 11, 807 + AI/ML SaMD + CDS guidance), 5 EU directives (MDR, SCCs, ePrivacy, AMLD4, Funds Transfer), 2 OWASP guides (Top 10, API Security), and 4 financial laws (BSA, ECOA/Reg B, FCRA, PCI DSS). See `data/regulations/README.md` for full inventory.

## Data

### SOPs

Located in `data/sops/`, organized by business unit subdirectory (e.g. `data/sops/01_ai_ml_engineering/sop_aiml_001_*.md`). Each SOP is a Markdown file with YAML frontmatter containing `sop_id`, `title`, `business_unit`, and `regulations` fields.

200 SOPs across 10 business units (AI/ML Engineering, Clinical AI Products, Customer Operations, Data Governance & Privacy, Financial Services, Human Resources, IT Operations, Information Security, Legal & Compliance, Product & Engineering), 20 SOPs each.

To regenerate SOPs (requires `NEBIUS_API_KEY`):

```bash
python3 scripts/generate_sops.py                    # Generate all SOPs
python3 scripts/generate_sops.py --resume            # Skip already-generated files
python3 scripts/generate_sops.py --concurrency 5     # Parallel API calls
python3 scripts/generate_sops.py --sop SOP-AIML-001  # Generate a single SOP
```

SOP definitions and metadata are in `scripts/sop_taxonomy.py`. The company profile used for generation is in `data/company_profile.md`.

### Regulations

Located in `data/regulations/` as `.txt`, `.md`, `.pdf`, and `.xml` files. See `data/regulations/README.md` for the full inventory and sources. PDFs are extracted to `.txt` via `scripts/extract_pdf_text.py` (pypdf) before ingestion.

To ingest into Pinecone:

```bash
make ingest-regulations   # Chunks, embeds, upserts into Pinecone namespace "regulations"
```

### Compliance matrix

420 ground-truth (SOP, regulation) pairs in `data/compliance_matrix_revised.json` across 6 regulations:

| Regulation | SOPs | Description |
|------------|------|-------------|
| SOC 2 | 121 | Trust Services Criteria CC1–CC9 |
| HIPAA | 94 | Security Rule administrative, physical, technical safeguards |
| GDPR | 76 | Data protection and privacy |
| EU AI Act | 63 | High-risk AI system requirements |
| NIST AI RMF | 37 | AI risk management framework |
| SR 11-7 | 29 | Model risk management |

Compliance level distribution: 170 compliant (40%), 161 partial (38%), 89 gap (21%). SOPs are deliberately varied — compliant SOPs cite regulation articles and have specific controls, partial SOPs use vague language, gap SOPs are missing key requirements.

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `NEBIUS_API_KEY` | Yes | Nebius AI Studio API key |
| `OPENAI_API_KEY` | Optional | OpenAI API key (for Prototype agent) |
| `PINECONE_API_KEY` | Yes | Pinecone vector DB key (agentic RAG) |
| `TAVILY_API_KEY` | Optional | Live regulation grounding |
| `LANGSMITH_API_KEY` | Optional | LangSmith tracing + cloud auth |
| `JIRA_BASE_URL` | For Jira | Atlassian site URL (e.g. `https://your-org.atlassian.net`) |
| `JIRA_EMAIL` | For Jira | Atlassian account email tied to the API token |
| `JIRA_API_TOKEN` | For Jira | API token from id.atlassian.com |
| `JIRA_PROJECT_KEY` | For Jira | Target Jira project key (e.g. `SENT`) |
| `LANGGRAPH_URL` | Optional | Override UI backend URL |
| `UI_API_KEY` | Yes (UI) | Shared secret that gates the UI's `/api/*` endpoints. The UI **refuses to start** without it (even locally); every API call must supply a matching `X-API-Key`. Generate with `openssl rand -hex 32`. |

## Cost

| Operation | Model | Tokens | Cost | Latency |
|-----------|-------|--------|------|---------|
| Full audit (Production) | Nemotron-3-Ultra-550b (\$1.00/\$3.00 per M tokens) | ~12M | ~$12 | ~23m |
| Full audit (Optimized) | DeepSeek-V4-Pro (\$1.75/\$3.50 per M tokens) | ~36M | ~$64 | ~53m |
| Full audit (Prototype) | GPT-5.5 (\$5.00/\$30.00 per M tokens) | ~18M | ~$140 | ~13m |
| SOP ingestion | Qwen3-Embedding-8B | ~2M | ~$0.02 | ~5m |

Each SOP audit fans out a dedicated sub-agent with multiple tool calls (regulation retrieval, web search), so token counts are dominated by sub-agent usage across 200 SOPs. Token usage and cost are displayed live in the UI. Use `scripts/validate_run.py` to get exact cost/token/latency breakdowns for any LangSmith run.

## Integrations

### Jira Cloud

The `create_jira_ticket` tool files compliance findings as tickets on a Jira Kanban board via the [Jira Cloud REST API v3](https://developer.atlassian.com/cloud/jira/platform/rest/v3/). Tickets are created for gap or partial findings at medium+ severity.

- **Client:** `sentinel/actuation/jira_client.py` — sync REST client with basic auth (email + API token)
- **Description format:** Atlassian Document Format (ADF)
- **Labels:** `sentinel`, `compliance-finding`, severity, regulation slug, SOP slug
- **Priority mapping:** critical → Highest, high → High, medium → Medium, low → Low

Setup: create an API token at [id.atlassian.com](https://id.atlassian.com), then set in `.env`:

```bash
JIRA_BASE_URL=https://your-org.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your-api-token
JIRA_PROJECT_KEY=SENT
```

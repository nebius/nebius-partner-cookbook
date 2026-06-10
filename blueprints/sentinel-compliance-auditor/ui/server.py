"""FastAPI backend for the UI.

Serves the static HTML/CSS/JSX from ui/static/ and exposes a small JSON+SSE
API that the React app uses to:
- read 120-question eval results (Eval screen)
- list dataset questions for the random-draw (Compare screen)
- count SOPs / regulations in the Pinecone-ingested corpus (Audit hero stats)
- fetch findings from Jira (Audit findings table)
- stream a single LangGraph audit (Audit composer)
- stream 3 parallel agents on the same question (Compare race)
"""
from __future__ import annotations

import asyncio
import functools
import json
import os
import queue
import re
import secrets
import threading
import time
from pathlib import Path
from typing import Any

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import Response, StreamingResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from langgraph_sdk import get_sync_client

from sentinel.config import (
    JIRA_API_TOKEN,
    JIRA_BASE_URL,
    JIRA_DEFAULT_ISSUE_TYPE,
    JIRA_EMAIL,
    JIRA_PROJECT_KEY,
    MODEL,
    NEBIUS_MODELS,
    OPENAI_MODEL,
    PRICING,
    SOP_BUSINESS_UNITS,
)
from sentinel.token_accounting import AUDIT_TOOL_NAMES, parse_tokens_from_result

STATIC_DIR = Path(__file__).resolve().parent / "static"
EVAL_RESULTS_DIR = PROJECT_ROOT / "data" / "eval" / "results"
EVAL_AGENTS = {
    "optimized":   EVAL_RESULTS_DIR / "optimized_rejudged_20260610_163109.json",
    "prototype":   EVAL_RESULTS_DIR / "prototype_rejudged_20260610_163010.json",
    "grounded":    EVAL_RESULTS_DIR / "grounded_rejudged_20260610_163040.json",
    "nemotron":    EVAL_RESULTS_DIR / "production_rejudged_20260610_163135.json",
}
DATASET_PATH = PROJECT_ROOT / "data" / "eval" / "qa_dataset.jsonl"
SOPS_DIR = PROJECT_ROOT / "data" / "sops"
REGULATIONS_DIR = PROJECT_ROOT / "data" / "regulations"

# Shared-secret gate for the JSON+SSE API. When set, every /api/* request
# (except /api/health for LB probes) must send a matching X-API-Key header.
# Leave empty for local dev to disable the gate. TLS + rate limiting are
# expected to be handled by the reverse proxy / load balancer in front.
UI_API_KEY = os.environ.get("UI_API_KEY", "")

LANGGRAPH_URL = os.environ.get("LANGGRAPH_URL", "http://localhost:2024")
LANGSMITH_API_KEY = os.environ.get("LANGSMITH_API_KEY", "")
LANGSMITH_PROJECT = os.environ.get("LANGCHAIN_PROJECT", "sentinel-agent")

# LangSmith URLs need the workspace + project UUIDs, not names. Looked up once
# via the SDK and cached for the lifetime of the process.
_LS_IDS: dict[str, str | None] = {"tenant": None, "project": None, "resolved": False}


def _get_ls_ids() -> tuple[str | None, str | None]:
    if _LS_IDS["resolved"]:
        return _LS_IDS["tenant"], _LS_IDS["project"]
    _LS_IDS["resolved"] = True
    if not LANGSMITH_API_KEY:
        return None, None
    try:
        from langsmith import Client
        c = Client(api_key=LANGSMITH_API_KEY)
        _LS_IDS["tenant"]  = c._get_tenant_id()
        _LS_IDS["project"] = str(c.read_project(project_name=LANGSMITH_PROJECT).id)
    except Exception as exc:
        print(f"[forge] could not resolve LangSmith workspace/project for {LANGSMITH_PROJECT!r}: {exc}")
    return _LS_IDS["tenant"], _LS_IDS["project"]


def _trace_url(run_id: str) -> str | None:
    """Direct LangSmith trace URL. Returns None if LangSmith is not reachable."""
    tenant, project = _get_ls_ids()
    if not tenant or not project:
        return None
    return f"https://smith.langchain.com/o/{tenant}/projects/p/{project}/r/{run_id}?poll=true"

# ── Agent registry ───────────────────────────────────────────────────────────
# The single source for agent labels, graph ids, models, and (via
# config.PRICING) prices. Served to the React app as /agents.js — the JSX
# screens and app-forge.jsx read window.SENTINEL_AGENTS instead of carrying
# their own copies, so a price or label change happens in one place.

_NEMOTRON_MODEL = NEBIUS_MODELS["nemotron"]

PARALLEL_AGENTS = [
    {"key": "naive",  "label": "Naive RAG",        "sublabel": "DeepSeek-V4-Pro",
     "tagline": "1 retrieval + 1 LLM call · no tools",
     "graph_id": "sentinel_naive", "model": MODEL},
    {"key": "openai", "label": "Grounded agent", "sublabel": "GPT-5.5 + Tavily",
     "tagline": "ReAct · Pinecone + web · sub-agent fan-out",
     "graph_id": "sentinel_grounded", "model": OPENAI_MODEL},
    {"key": "nemotron", "label": "Production agent", "sublabel": "Nemotron-Ultra + Tavily + LangSmith + Snowglobe",
     "tagline": "ReAct · Pinecone + web · sub-agent fan-out",
     "graph_id": "sentinel_nemotron", "model": _NEMOTRON_MODEL},
]

AUDIT_AGENTS = [
    {"key": "sentinel_prototype",      "graph_id": "sentinel_prototype", "label": "Prototype",
     "sublabel": "GPT-5.5", "model": OPENAI_MODEL},
    {"key": "sentinel_prototype_plus", "graph_id": "sentinel_grounded",  "label": "Grounded",
     "sublabel": "GPT-5.5 + Tavily", "model": OPENAI_MODEL},
    {"key": "sentinel_production",     "graph_id": "sentinel_optimized", "label": "Optimized",
     "sublabel": "DeepSeek-V4-Pro + Tavily", "model": MODEL},
    {"key": "sentinel_nemotron",       "graph_id": "sentinel_nemotron",  "label": "Production",
     "sublabel": "Nemotron-Ultra + Tavily + LangSmith + Snowglobe", "model": _NEMOTRON_MODEL},
]

EVAL_AGENT_META = {
    "prototype": {"label": "Prototype agent",  "sublabel": "GPT-5.5 + Pinecone"},
    "grounded":  {"label": "Grounded agent",   "sublabel": "GPT-5.5 + Pinecone + Tavily"},
    "optimized": {"label": "Optimized agent",  "sublabel": "DeepSeek-V4-Pro + Pinecone + Tavily"},
    "nemotron":  {"label": "Production agent", "sublabel": "Nemotron-Ultra + Tavily + LangSmith + Snowglobe"},
}


def _agent_registry() -> dict:
    return {
        "pricing": PRICING,
        "audit": [{**a, "pricing": PRICING.get(a["model"], {"input": 0, "output": 0})} for a in AUDIT_AGENTS],
        "race": PARALLEL_AGENTS,
        "evalMeta": EVAL_AGENT_META,
    }

app = FastAPI(title="Sentinel UI", version="0.1.0")

if not UI_API_KEY:
    # Fail closed: the UI must never run without a key, even locally. Refusing to
    # start (rather than warning) removes the "forgot to set it in prod" footgun.
    import sys

    print(
        "[sentinel-ui] FATAL: UI_API_KEY is not set. The UI refuses to start "
        "without it. Set UI_API_KEY in .env (e.g. `openssl rand -hex 32`). TLS + "
        "rate limiting are expected at your reverse proxy / load balancer.",
        file=sys.stderr,
        flush=True,
    )
    raise SystemExit(1)


@app.middleware("http")
async def _require_api_key(request: Request, call_next):
    """Gate every /api/* call behind the shared X-API-Key, except the LB health probe.

    UI_API_KEY is guaranteed set (the process exits at import otherwise), so the
    gate always enforces. The check runs before any route handler, so no agent
    run / LangGraph thread is started for an unauthorized caller. Constant-time
    comparison avoids a timing side-channel.
    """
    path = request.url.path
    if path.startswith("/api/") and path != "/api/health":
        provided = request.headers.get("x-api-key", "")
        if not secrets.compare_digest(provided, UI_API_KEY):
            return JSONResponse({"detail": "invalid or missing API key"}, status_code=401)
    return await call_next(request)


@app.get("/api/auth-check")
def auth_check():
    """Lightweight endpoint for the UI to validate an API key without triggering Pinecone."""
    return {"ok": True}


# ── helpers ──────────────────────────────────────────────────────────────────

def _langgraph_client():
    kwargs: dict[str, Any] = {"url": LANGGRAPH_URL}
    if LANGSMITH_API_KEY and "localhost" not in LANGGRAPH_URL:
        kwargs["api_key"] = LANGSMITH_API_KEY
    return get_sync_client(**kwargs)


def _jira_client():
    if not (JIRA_BASE_URL and JIRA_EMAIL and JIRA_API_TOKEN):
        return None
    from sentinel.actuation.jira_client import JiraClient
    return JiraClient(
        base_url=JIRA_BASE_URL,
        email=JIRA_EMAIL,
        api_token=JIRA_API_TOKEN,
        project_key=JIRA_PROJECT_KEY or "SENT",
        issue_type=JIRA_DEFAULT_ISSUE_TYPE,
    )


# Parse the `[SEV] CLAUSE: Title (SOP-XYZ-NNN)` summary that create_jira_ticket emits.
_SUMMARY_RE = re.compile(r"^\[(\w+)\]\s+([^:]+):\s+(.+?)\s+\((SOP-[A-Z]+-\d+)\)\s*$")
# Map BU directory prefix to human-readable name.
_BU_LABELS = {
    "01": "AI/ML Engineering",
    "02": "Clinical AI Products",
    "03": "Data Governance",
    "04": "Financial Services",
    "05": "Information Security",
    "06": "IT Operations",
    "07": "Human Resources",
    "08": "Legal & Compliance",
    "09": "Product Engineering",
    "10": "Customer Operations",
}
# Regulation slug → display name (matches _slug in tools.py).
_REG_LABEL = {
    "hipaa": "HIPAA",
    "soc-2": "SOC 2",
    "soc2": "SOC 2",
    "gdpr": "GDPR",
    "eu-ai-act": "EU AI Act",
    "nist-ai-rmf": "NIST AI RMF",
    "sr-11-7": "SR 11-7",
    "sb-53": "SB 53",
    "sb-942": "SB 942",
    "ab-853": "AB 853",
}


_SOP_ID_RE = re.compile(r"^SOP-([A-Z]+)-(\d+)$")
_SOP_FILE_RE = re.compile(r"^sop_([a-z]+)_(\d+)_.*\.md$")


@functools.lru_cache(maxsize=1)
def _sop_path_index() -> dict[str, Path]:
    """{'SOP-ISEC-008' → path} from one walk of the SOP tree.

    /api/findings resolves title + unit for up to 100 Jira issues per request;
    without the index each resolution rglob'd the whole tree (~200 walks)."""
    index: dict[str, Path] = {}
    if not SOPS_DIR.exists():
        return index
    for path in SOPS_DIR.rglob("sop_*.md"):
        m = _SOP_FILE_RE.match(path.name)
        if m:
            index[f"SOP-{m.group(1).upper()}-{m.group(2)}"] = path
    return index


def _find_sop_path(sop_id: str) -> Path | None:
    m = _SOP_ID_RE.match(sop_id.strip())
    if not m:
        return None
    return _sop_path_index().get(f"SOP-{m.group(1)}-{m.group(2).zfill(3)}")


@functools.lru_cache(maxsize=512)
def _sop_unit(sop_id: str) -> str:
    """Resolve SOP-XYZ-NNN → business unit display label (e.g. 'Information Security')."""
    path = _find_sop_path(sop_id)
    if path is None:
        return ""
    try:
        bu_dir = path.relative_to(SOPS_DIR).parts[0]
    except (ValueError, IndexError):
        return ""
    return _BU_LABELS.get(bu_dir[:2], bu_dir.replace("_", " ").title())


@functools.lru_cache(maxsize=512)
def _sop_title(sop_id: str) -> str:
    """Read the `title:` frontmatter of a SOP. Returns '' if not found."""
    path = _find_sop_path(sop_id)
    if path is None:
        return ""
    try:
        text = path.read_text()
    except OSError:
        return ""
    match = re.search(r"^title:\s*['\"]?(.+?)['\"]?$", text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return ""


# ── basic + GET endpoints ────────────────────────────────────────────────────

@app.get("/api/health")
def health():
    # Exempt from the API-key gate (LB probes) — return nothing internal.
    return {"ok": True}


@app.get("/agents.js")
def agents_js():
    """Agent registry as a synchronous script (loaded by index.html before the
    app bundles), so labels/pricing render on first paint without a fetch."""
    payload = json.dumps(_agent_registry(), indent=2)
    return Response(
        f"window.SENTINEL_AGENTS = {payload};\n",
        media_type="application/javascript",
    )


@app.get("/api/eval-results")
def eval_results():
    out = {}
    for key, path in EVAL_AGENTS.items():
        if path.exists():
            out[key] = json.loads(path.read_text())
    if not out:
        raise HTTPException(status_code=404, detail="No eval result files found")
    return out


@app.get("/api/dataset")
def dataset():
    if not DATASET_PATH.exists():
        raise HTTPException(status_code=404, detail="qa_dataset.jsonl not found")
    rows = [json.loads(line) for line in DATASET_PATH.read_text().splitlines() if line.strip()]
    return {"count": len(rows), "questions": rows}


_kb_stats_cache: dict[str, Any] = {"data": None, "fetched_at": 0.0}
_KB_STATS_TTL_S = 300.0


def _compute_kb_stats() -> dict[str, Any]:
    """Pull live counts straight from Pinecone.

    - SOPs: list IDs in each business-unit namespace, dedupe by `SOP-XYZ-NNN`
      prefix (vectors are filed as `<sop_id>::chunk-NNNN`).
    - Regulations: list IDs in the `regulations` namespace, parse filename stem
      between `reg::` and `::chunk-`, map to framework via REGULATION_MAP.
    """
    from sentinel.retrieval.regulations import _get_index
    from sentinel.retrieval.ingest_regulations import _detect_regulation

    index = _get_index()
    stats = index.describe_index_stats()
    namespaces = stats.get("namespaces", {}) or {}

    def _iter_ids(ns: str):
        """Pinecone v3 SDK: index.list() yields ListResponse pages, each with .vectors[]."""
        for page in index.list(namespace=ns):
            vectors = getattr(page, "vectors", None) or page.get("vectors", [])
            for v in vectors:
                vid = getattr(v, "id", None) or (v.get("id") if hasattr(v, "get") else None)
                if vid:
                    yield vid

    sop_ids: set[str] = set()
    populated_bus: list[str] = []
    for ns in namespaces:
        if ns == "regulations" or ns == "":
            continue
        populated_bus.append(ns)
        try:
            for vid in _iter_ids(ns):
                head = vid.split("::", 1)[0]
                if head:
                    sop_ids.add(head)
        except Exception:
            pass

    regulation_files: set[str] = set()
    try:
        for vid in _iter_ids("regulations"):
            parts = vid.split("::", 2)
            if len(parts) >= 2 and parts[0] == "reg":
                regulation_files.add(parts[1])
    except Exception:
        pass

    frameworks: set[str] = set()
    for stem in regulation_files:
        framework = _detect_regulation(stem)
        if framework:
            frameworks.add(framework)

    return {
        "source": "pinecone",
        "index": os.environ.get("PINECONE_INDEX_NAME", "sentinel-sops"),
        "sop_count": len(sop_ids),
        "regulation_count": len(frameworks),
        "regulations": sorted(frameworks),
        "namespaces_populated": sorted(populated_bus),
        "regulations_namespace_vectors": namespaces.get("regulations", {}).get("vector_count", 0),
        "total_vectors": stats.get("total_vector_count", 0),
        "business_units": SOP_BUSINESS_UNITS,
    }


def _disk_kb_stats() -> dict[str, Any]:
    """Fallback when Pinecone is unreachable — count on-disk corpus."""
    from sentinel.retrieval.ingest_regulations import REGULATION_MAP
    sop_count = sum(1 for _ in SOPS_DIR.rglob("sop_*.md")) if SOPS_DIR.exists() else 0
    regulations = sorted(set(REGULATION_MAP.values()))
    return {
        "source": "disk",
        "sop_count": sop_count,
        "regulation_count": len(regulations),
        "regulations": regulations,
        "business_units": SOP_BUSINESS_UNITS,
    }


@app.get("/api/kb-stats")
def kb_stats(refresh: bool = False):
    """Live SOP + framework counts from Pinecone, cached for 5 minutes."""
    now = time.time()
    if not refresh and _kb_stats_cache["data"] and (now - _kb_stats_cache["fetched_at"] < _KB_STATS_TTL_S):
        return _kb_stats_cache["data"]
    try:
        data = _compute_kb_stats()
    except Exception as exc:
        data = _disk_kb_stats()
        data["error"] = f"pinecone unavailable: {exc}"
    _kb_stats_cache["data"] = data
    _kb_stats_cache["fetched_at"] = now
    return data


@app.get("/api/findings")
def findings():
    """Reads Jira issues with `labels = sentinel` and renders rows for the findings table.

    Returns {issues: [...], jira_configured: bool, error?: str}. Gracefully
    degrades to an empty list when Jira isn't configured.
    """
    if not (JIRA_BASE_URL and JIRA_EMAIL and JIRA_API_TOKEN):
        return {"issues": [], "jira_configured": False, "error": "Jira not configured"}

    client = _jira_client()
    if client is None:
        return {"issues": [], "jira_configured": False, "error": "Jira client unavailable"}

    try:
        issues = client.list_issues(
            jql="labels = sentinel ORDER BY created DESC",
            fields=["summary", "labels", "priority", "status", "created"],
            max_results=100,
        )
    except Exception as exc:
        return {"issues": [], "jira_configured": True, "error": str(exc)}
    finally:
        client.close()

    rows: list[dict[str, Any]] = []
    for issue in issues:
        f = issue.get("fields", {})
        summary = f.get("summary", "")
        labels = f.get("labels", [])
        priority = (f.get("priority") or {}).get("name", "").lower()
        status = (f.get("status") or {}).get("name", "")

        # Parse summary: "[HIGH] HIPAA-164.312: Access Control (SOP-ISEC-008)"
        m = _SUMMARY_RE.match(summary)
        sop = clause_id = title = severity_in_summary = ""
        if m:
            severity_in_summary = m.group(1).lower()
            clause_id = m.group(2).strip()
            title = m.group(3).strip()
            sop = m.group(4).strip()

        # Regulation from labels (skip housekeeping labels).
        reserved = {"sentinel", "compliance-finding"}
        reg = ""
        for lbl in labels:
            low = lbl.lower()
            if low in reserved or low.startswith("sev-") or low.startswith("sop-"):
                continue
            if low in _REG_LABEL:
                reg = _REG_LABEL[low]
                break
            reg = lbl.replace("-", " ").title()
            break

        # Severity: prefer Jira priority field, fall back to summary tag.
        sev_norm = priority or severity_in_summary or "medium"
        if sev_norm in ("highest", "critical"):
            severity = "high"
        elif sev_norm in ("high",):
            severity = "high"
        elif sev_norm in ("medium",):
            severity = "med"
        else:
            severity = "low"
        # Compliance level heuristic: high/critical → gap, medium → partial.
        level = "gap" if severity == "high" else "partial"

        rows.append({
            "key": issue.get("key", ""),
            "url": f"{JIRA_BASE_URL.rstrip('/')}/browse/{issue.get('key', '')}",
            "sop": sop,
            "title": _sop_title(sop) or title,
            "unit": _sop_unit(sop),
            "reg": (clause_id and f"{reg} {clause_id}") if reg else clause_id,
            "level": level,
            "evidence": title,
            "severity": severity,
            "status": status,
        })

    from urllib.parse import quote
    register_url = (
        f"{JIRA_BASE_URL.rstrip('/')}/issues/?jql="
        + quote('labels = "sentinel" ORDER BY created DESC')
    )
    return {"issues": rows, "jira_configured": True, "register_url": register_url}


# ── SSE: single audit stream ─────────────────────────────────────────────────

class AuditRequest(BaseModel):
    message: str
    graph_id: str = "sentinel_optimized"


def _stream_one(
    thread_id: str,
    message: str,
    graph_id: str,
    out_q: "queue.Queue[str | None]",
    prefix: str = "",
    cancel_event: "threading.Event | None" = None,
):
    """Push SSE-formatted lines into out_q. Producer for a single LangGraph stream.

    `prefix` is prepended to each event's payload so the multiplexed race
    endpoint can attribute events to the right agent column.

    `cancel_event` is set by the consumer when the client disconnects: the
    producer stops streaming and cancels the LangGraph run instead of letting
    it burn tokens to completion into a queue nobody reads.
    """
    if cancel_event is None:
        cancel_event = threading.Event()

    def _put(payload: str) -> bool:
        """Bounded-queue put that gives up once the client has disconnected."""
        while not cancel_event.is_set():
            try:
                out_q.put(payload, timeout=1.0)
                return True
            except queue.Full:
                continue
        return False

    run_info = {"run_id": None}

    def _on_run_created(meta):
        rid = getattr(meta, "run_id", None) or (meta.get("run_id") if hasattr(meta, "get") else None)
        if not rid:
            return
        run_info["run_id"] = rid
        _put(json.dumps({
            "type": "run_started",
            "agent": prefix,
            "run_id": rid,
            "trace_url": _trace_url(rid),
        }))

    outer_tokens = {"input": 0, "output": 0}
    sub_tokens = {"input": 0, "output": 0}

    def _emit_usage():
        _put(json.dumps({
            "type": "usage", "agent": prefix,
            "input_tokens": outer_tokens["input"] + sub_tokens["input"],
            "output_tokens": outer_tokens["output"] + sub_tokens["output"],
        }))

    client = None
    try:
        client = _langgraph_client()
        for event in client.runs.stream(
            thread_id=thread_id,
            assistant_id=graph_id,
            input={"messages": [{"role": "user", "content": message}]},
            stream_mode=["messages-tuple", "values"],
            on_run_created=_on_run_created,
        ):
            if cancel_event.is_set():
                break
            for payload in _normalize_event(event, prefix):
                parsed = json.loads(payload)
                if parsed.get("type") == "usage":
                    outer_tokens["input"] = parsed["input_tokens"]
                    outer_tokens["output"] = parsed["output_tokens"]
                    _emit_usage()
                elif parsed.get("type") == "tool_result":
                    _put(payload)
                    text = parsed.get("text", "")
                    # Accumulate across audit tool calls: a run may make several
                    # audit_sops / audit_single_sop calls, each reporting only its
                    # own sub-agents' tokens. Gate on the tool name so a read_file
                    # that re-reads offloaded audit output isn't counted again.
                    if parsed.get("name") in AUDIT_TOOL_NAMES and isinstance(text, str):
                        toks = parse_tokens_from_result(text)
                        if toks:
                            sub_tokens["input"] += toks[0]
                            sub_tokens["output"] += toks[1]
                            _emit_usage()
                else:
                    _put(payload)
    except Exception as exc:
        _put(json.dumps({"type": "error", "agent": prefix, "error": str(exc)}))
    finally:
        if cancel_event.is_set() and client is not None and run_info["run_id"]:
            try:
                client.runs.cancel(thread_id, run_info["run_id"])
            except Exception:
                pass
        done_payload = json.dumps({"type": "done", "agent": prefix})
        if cancel_event.is_set():
            # Consumer is gone — never block on a full queue.
            try:
                out_q.put_nowait(done_payload)
            except queue.Full:
                pass
        else:
            out_q.put(done_payload)


def _normalize_event(event, agent: str = "") -> list[str]:
    """LangGraph SDK event → JSON payloads understood by the React client.

    Returns a list because one AI message can carry several parallel tool
    calls — each gets its own event (with its `id`, so the client can match
    `tool_result` events by `tool_call_id` instead of guessing LIFO).
    """
    if event.event == "messages" and event.data:
        msg = event.data[0] if isinstance(event.data, list) else event.data
        if not isinstance(msg, dict):
            return []
        msg_type = msg.get("type", "")
        content = msg.get("content", "")
        tool_calls = msg.get("tool_calls", [])

        if msg_type in ("AIMessageChunk", "AIMessage", "ai"):
            payloads = [
                json.dumps({
                    "type": "tool_call", "agent": agent,
                    "id": tc.get("id", ""),
                    "name": tc.get("name", ""), "args": tc.get("args", {}),
                })
                for tc in tool_calls
                if tc.get("name")
            ]
            if payloads:
                return payloads
            if isinstance(content, str) and content:
                return [json.dumps({"type": "token", "agent": agent, "text": content})]
        elif msg_type in ("tool", "ToolMessage", "ToolMessageChunk") and content:
            # ToolMessage content can be a list of content blocks; the client
            # calls string methods on it (startsWith/match), so coerce here.
            text = content if isinstance(content, str) else json.dumps(content, default=str)
            return [json.dumps({
                "type": "tool_result", "agent": agent,
                "name": msg.get("name", ""),
                "tool_call_id": msg.get("tool_call_id", ""),
                "text": text,
            })]

    elif event.event == "values" and isinstance(event.data, dict):
        usage: list[dict[str, int]] = []
        for msg in event.data.get("messages", []):
            if not isinstance(msg, dict):
                continue
            u = msg.get("usage_metadata")
            if u and (u.get("input_tokens") or u.get("output_tokens")):
                usage.append(u)
        if usage:
            in_tok = sum(u.get("input_tokens", 0) for u in usage)
            out_tok = sum(u.get("output_tokens", 0) for u in usage)
            return [json.dumps({
                "type": "usage", "agent": agent,
                "input_tokens": in_tok, "output_tokens": out_tok,
            })]
    return []


async def _drain_sse(
    out_q: "queue.Queue[str | None]",
    n_producers: int,
    cancel_event: "threading.Event | None" = None,
):
    """Yield SSE-formatted events from the queue until N producers have signalled done."""
    loop = asyncio.get_event_loop()
    done = 0
    try:
        while done < n_producers:
            payload = await loop.run_in_executor(None, out_q.get)
            if payload is None:
                done += 1
                continue
            try:
                obj = json.loads(payload)
            except json.JSONDecodeError:
                continue
            if obj.get("type") == "done":
                done += 1
                yield f"data: {payload}\n\n"
                continue
            yield f"data: {payload}\n\n"
        yield "data: {\"type\":\"all_done\"}\n\n"
    finally:
        # Reached on client disconnect (Starlette closes the generator) as
        # well as on normal completion: tell producers to stop streaming and
        # cancel their LangGraph runs.
        if cancel_event is not None:
            cancel_event.set()


@app.post("/api/audit/stream")
async def audit_stream(req: AuditRequest):
    """Single-agent SSE stream. Used by the Audit screen composer."""
    client = _langgraph_client()
    thread = client.threads.create()
    tid = thread["thread_id"]

    out_q: queue.Queue[str | None] = queue.Queue(maxsize=2000)
    cancel_event = threading.Event()
    threading.Thread(
        target=_stream_one,
        args=(tid, req.message, req.graph_id, out_q, "", cancel_event),
        daemon=True,
    ).start()
    return StreamingResponse(
        _drain_sse(out_q, n_producers=1, cancel_event=cancel_event),
        media_type="text/event-stream",
    )


# ── SSE: 3-way race stream ───────────────────────────────────────────────────

class RaceRequest(BaseModel):
    message: str
    question_id: str | None = None  # purely metadata for the client to echo


@app.post("/api/race/stream")
async def race_stream(req: RaceRequest):
    """3 agents in parallel against the same question. Events are tagged with `agent`."""
    client = _langgraph_client()
    # Spin up 3 fresh LangGraph threads in parallel.
    import concurrent.futures
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(PARALLEL_AGENTS)) as ex:
        futures = [ex.submit(client.threads.create) for _ in PARALLEL_AGENTS]
        try:
            thread_ids = [f.result()["thread_id"] for f in futures]
        except Exception as exc:
            raise HTTPException(status_code=502, detail=f"LangGraph thread create failed: {exc}")

    out_q: queue.Queue[str | None] = queue.Queue(maxsize=2000)
    cancel_event = threading.Event()
    for tid, agent in zip(thread_ids, PARALLEL_AGENTS):
        threading.Thread(
            target=_stream_one,
            args=(tid, req.message, agent["graph_id"], out_q, agent["key"], cancel_event),
            daemon=True,
        ).start()
    return StreamingResponse(
        _drain_sse(out_q, n_producers=len(PARALLEL_AGENTS), cancel_event=cancel_event),
        media_type="text/event-stream",
    )


# ── static files ────────────────────────────────────────────────────────────

# Must be mounted LAST so /api/* routes win over the static fallback.
app.mount("/", StaticFiles(directory=str(STATIC_DIR), html=True), name="static")

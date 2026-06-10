"""LangChain tools wrapping Sentinel's retrieval and auditing functions."""
from __future__ import annotations

import json
import logging
import re
import threading
import time
from typing import NamedTuple

from langchain_core.tools import tool

logger = logging.getLogger(__name__)

MAX_RETRIES = 4
RETRY_BACKOFF = 5
RATE_LIMIT_BACKOFF = 30

from sentinel.config import PINECONE_API_KEY, TAVILY_API_KEY
from sentinel.models import (
    COMPLIANCE_LEVEL_ALIASES,
    SEVERITY_ALIASES,
    AuditFinding,
    ComplianceLevel,
    normalize_compliance_level,
    normalize_severity,
)
from sentinel.token_accounting import format_sub_agent_tokens, format_total_tokens

class SopAuditResult(NamedTuple):
    """Per-SOP audit outcome, returned by value rather than accumulated in a
    module-level dict. Returning results means concurrent sub-agent workers and
    repeated/parallel top-level audits in one process can't contaminate each
    other's findings or token totals — each audit aggregates only its own.

    ``status`` is the structured outcome set at each failure site so retry
    logic never has to sniff the summary text (which embeds model-written
    prose that can contain words like "FAILED" or "rate"):
      - "ok"          successful audit with findings
      - "invalid"     bad input (unknown SOP, empty SOP) — not retryable
      - "failed"      transient sub-agent error — retryable
      - "no_findings" finished without structured findings — retryable
      - "truncated"   hit a length limit — NOT retryable (would truncate again)
    """
    summary: str
    findings: list  # list[AuditFinding]
    input_tokens: int = 0
    output_tokens: int = 0
    status: str = "ok"
    rate_limited: bool = False

_shared_http_client = None
_http_client_lock = threading.Lock()


def _get_shared_http_client():
    """Return a process-wide httpx.Client with connection pooling.

    httpx.Client is thread-safe, so all ThreadPoolExecutor workers share one
    pool.  DNS is resolved once per hostname and TCP connections are reused
    across SOP audits, eliminating the DNS-exhaustion failures seen under high
    concurrency.
    """
    global _shared_http_client
    if _shared_http_client is not None:
        return _shared_http_client
    with _http_client_lock:
        if _shared_http_client is None:
            import httpx

            _shared_http_client = httpx.Client(
                limits=httpx.Limits(
                    max_connections=200,
                    max_keepalive_connections=100,
                    keepalive_expiry=120,
                ),
                timeout=httpx.Timeout(600.0, connect=30.0),
            )
    return _shared_http_client


@tool
def list_regulations() -> str:
    """List all regulations available in the knowledge base. Returns regulation names and document sources."""
    if not PINECONE_API_KEY:
        return _list_regulations_local()
    try:
        import concurrent.futures

        from sentinel.config import PINECONE_INDEX_NAME
        from sentinel.retrieval.ingest import embed_texts
        from sentinel.retrieval.ingest_regulations import REGULATION_MAP
        from pinecone import Pinecone

        pc = Pinecone(api_key=PINECONE_API_KEY)
        index = pc.Index(PINECONE_INDEX_NAME)

        known_regs = sorted(set(REGULATION_MAP.values()))
        query_text = "regulatory compliance requirements"
        embedding = embed_texts([query_text])[0]

        def _sources_for(reg_name: str) -> set[str]:
            results = index.query(
                vector=embedding,
                top_k=5,
                namespace="regulations",
                include_metadata=True,
                filter={"regulation": {"$eq": reg_name}},
            )
            return {
                f"{match.metadata.get('source', '')} ({match.metadata.get('edition', 'current')})"
                for match in results.matches
            }

        # One round trip per regulation just to harvest metadata — run them in
        # parallel or this tool call takes multiple seconds.
        regs: dict[str, set[str]] = {}
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            futures = {executor.submit(_sources_for, r): r for r in known_regs}
            for future in concurrent.futures.as_completed(futures):
                sources = future.result()
                if sources:
                    regs[futures[future]] = sources

        lines = []
        for reg in sorted(regs.keys()):
            sources = ", ".join(sorted(regs[reg]))
            lines.append(f"- {reg}: {sources}")
        return f"{len(regs)} regulations in knowledge base:\n" + "\n".join(lines)
    except Exception:
        return _list_regulations_local()


def _list_regulations_local() -> str:
    from sentinel.config import DATA_DIR
    reg_dir = DATA_DIR / "regulations"
    files = sorted(reg_dir.glob("*.txt")) + sorted(reg_dir.glob("*.md"))
    files = [f for f in files if f.name != "README.md"]
    lines = [f"- {f.stem}" for f in files]
    return f"{len(files)} regulation files available:\n" + "\n".join(lines)


_LIST_SOPS_SYNONYMS = {
    "fda": "clinical ai products",
    "samd": "clinical ai products",
    "medical device": "clinical ai products",
    "ai/ml": "ai/ml engineering",
    "ai ml": "ai/ml engineering",
    "machine learning": "ai/ml engineering",
    "algorithm": "ai/ml engineering",
}


@tool
def list_sops(query: str = "") -> str:
    """List all available SOPs. Pass an empty query (the default) to return ALL SOPs in a single call — use this for broad discovery questions instead of guessing keywords. Optionally filter by a search query (matches title, SOP ID, or business unit substring). Available business units: 'AI/ML Engineering' (SOP-AIML-*), 'Clinical AI Products' (SOP-CLIN-*), 'Customer Operations' (SOP-COPS-*), 'Data Governance & Privacy' (SOP-DGP-*), 'Financial Services' (SOP-FIN-*), 'Human Resources' (SOP-HR-*), 'Information Security' (SOP-ISEC-*), 'IT Operations & Infrastructure' (SOP-ITOP-*), 'Legal & Compliance' (SOP-LEGC-*), 'Product & Engineering' (SOP-PENG-*)."""
    from sentinel.retrieval.local import list_all_sops

    all_sops = list_all_sops()
    if query:
        q = query.lower()
        expanded = _LIST_SOPS_SYNONYMS.get(q, q)
        all_sops = [
            s for s in all_sops
            if q in s["title"].lower()
            or q in s["sop_id"].lower()
            or q in s.get("business_unit", "").lower()
            or expanded in s.get("business_unit", "").lower()
        ]

    if not all_sops:
        return f"No SOPs found matching '{query}'"

    lines = [f"- {s['sop_id']}: {s['title']} ({s.get('business_unit', '')})" for s in all_sops]
    return f"{len(all_sops)} SOPs:\n" + "\n".join(lines)


def _editions_filter(edition: str) -> list[str] | None:
    """Map the tool-level `edition` arg to the retrieval filter. Default is
    current-only — superseded editions (HIPAA 2017/2020, EU AI Act 2021
    proposal) must be requested explicitly, not retrieved by accident."""
    edition = (edition or "").strip().lower()
    if edition in ("", "all", "any"):
        return None
    return [edition]


@tool
def retrieve_regulation_text_tool(query: str, regulation: str = "", edition: str = "current") -> str:
    """Retrieve regulation text from the knowledge base for a given query. Optionally filter by regulation name (e.g. 'HIPAA', 'SOC 2', 'GDPR'). `edition` defaults to 'current'; pass a historical edition (e.g. '2017', '2021-proposal') or 'all' to search every edition."""
    if not PINECONE_API_KEY:
        return "Pinecone not configured. Use local retrieval mode."
    try:
        from sentinel.retrieval.regulations import retrieve_regulation_text, format_regulation_context
        regs = [regulation] if regulation else None
        chunks = retrieve_regulation_text(query, regulations=regs, top_k=15, editions=_editions_filter(edition))
        if not chunks:
            return f"No regulation text found for: {query}"
        context = format_regulation_context(chunks)
        return f"Retrieved {len(chunks)} regulation sections:\n{context}"
    except Exception as e:
        return f"Regulation retrieval failed: {e}"


@tool
def search_web(query: str = "") -> str:
    """Search the web via Tavily for latest regulatory guidance, enforcement actions, or interpretation. Use for questions the static knowledge base can't answer — e.g. recent HHS OCR enforcement, FDA AI/ML device guidance, EU AI Office codes of practice, EDPB decisions, OCC bulletins. The `query` argument is required and must be a non-empty search phrase."""
    if not isinstance(query, str) or not query.strip():
        return "Missing or empty 'query' argument — please re-issue with a specific search phrase"
    if not TAVILY_API_KEY:
        return "Tavily not configured — web search unavailable."
    try:
        from tavily import TavilyClient
        client = TavilyClient(api_key=TAVILY_API_KEY)
        response = client.search(
            query=query,
            search_depth="advanced",
            max_results=3,
            include_answer=True,
        )
        parts = []
        if response.get("answer"):
            parts.append(f"Summary: {response['answer']}")
        for result in response.get("results", [])[:3]:
            parts.append(f"Source: {result.get('title', '')}\nURL: {result.get('url', '')}\n{result.get('content', '')[:500]}")
        return "\n\n".join(parts) if parts else "No results found."
    except Exception as e:
        return f"Web search failed: {e}"


def _build_subagent_tools(sop_text: str, sop_id: str, sop_title: str, use_tavily: bool = True):
    """Build the tool set for the audit sub-agent.

    Returns (tools, recorded_findings) where recorded_findings is a mutable
    list populated by the record_finding tool during execution.
    """
    recorded_findings: list[dict] = []
    _retrieval_calls = {"count": 0, "limit": 30}
    _budget_lock = threading.Lock()

    def _consume_retrieval_budget() -> bool:
        """Atomic check-and-increment — parallel tool calls must not race past
        the limit. Callers validate their inputs BEFORE consuming, so a
        rejected empty query doesn't burn a budget unit."""
        with _budget_lock:
            if _retrieval_calls["count"] >= _retrieval_calls["limit"]:
                return False
            _retrieval_calls["count"] += 1
            return True

    _budget_exhausted_msg = (
        f"Retrieval limit reached ({_retrieval_calls['limit']} calls). "
        "Record your findings now with record_finding and finish the audit."
    )

    @tool
    def record_finding(
        requirement_id: str,
        requirement_title: str,
        regulation: str,
        compliance_level: str,
        severity: str,
        reasoning: str,
        evidence_quote: str = "",
        gap_description: str = "",
        remediation: str = "",
    ) -> str:
        """Record a single audit finding. Call this IMMEDIATELY after assessing each requirement — do NOT wait until the end. Each call saves one finding."""
        valid_levels = {"compliant", "partial", "gap"}
        valid_sevs = {"critical", "high", "medium", "low", "info"}
        # Normalize through the shared alias maps first: the JSON-fallback
        # path accepts "non-compliant"/"noncompliant" etc., so the tool must
        # too — bouncing the same output costs the sub-agent an extra turn.
        cl = COMPLIANCE_LEVEL_ALIASES.get(compliance_level.lower().strip(), "")
        sev = SEVERITY_ALIASES.get(severity.lower().strip(), "")
        if cl not in valid_levels:
            return f"Invalid compliance_level '{compliance_level}'. Must be one of: {', '.join(sorted(valid_levels))}"
        if sev not in valid_sevs:
            return f"Invalid severity '{severity}'. Must be one of: {', '.join(sorted(valid_sevs))}"
        recorded_findings.append({
            "requirement_id": requirement_id,
            "requirement_title": requirement_title,
            "regulation": regulation,
            "compliance_level": cl,
            "severity": sev,
            "evidence_quote": evidence_quote or "",
            "gap_description": gap_description or "",
            "remediation": remediation or "",
            "reasoning": reasoning,
        })
        return f"Recorded finding #{len(recorded_findings)}: {requirement_id} ({regulation}) — {cl}/{sev}"

    @tool
    def retrieve_regulation_rag(query: str = "", regulation: str = "", edition: str = "current") -> str:
        """Search the Pinecone vector store for regulation text chunks via semantic similarity. Use targeted queries like 'HIPAA access control requirements' or 'SOC 2 CC6 logical access'. Optionally filter by regulation name. `edition` defaults to 'current'; pass a historical edition (e.g. '2017', '2021-proposal') or 'all' only when comparing editions. The `query` argument is required and must be a non-empty search phrase."""
        if not isinstance(query, str) or not query.strip():
            return "Missing or empty 'query' argument — please re-issue with a specific search phrase"
        if not PINECONE_API_KEY:
            return "Pinecone not configured."
        if not _consume_retrieval_budget():
            return _budget_exhausted_msg
        try:
            from sentinel.retrieval.regulations import retrieve_regulation_text, format_regulation_context
            regs = [regulation] if regulation else None
            chunks = retrieve_regulation_text(query, regulations=regs, top_k=15, editions=_editions_filter(edition))
            if not chunks:
                return f"No regulation text found for: {query}"
            context = format_regulation_context(chunks)
            return f"Retrieved {len(chunks)} sections:\n{context}"
        except Exception as e:
            return f"RAG retrieval failed: {e}"

    @tool
    def read_sop() -> str:
        """Read the full SOP text being audited. Call this to review the SOP content before or during your assessment."""
        return f"SOP: {sop_id} — {sop_title}\n\n{sop_text}"

    @tool
    def _search_web_capped(query: str = "") -> str:
        """Search the web for current regulatory guidance, enforcement actions, or recent developments. Use when you need information beyond the static knowledge base."""
        if not isinstance(query, str) or not query.strip():
            return "Missing or empty 'query' argument — please re-issue with a specific search phrase"
        if not _consume_retrieval_budget():
            return _budget_exhausted_msg
        return search_web.invoke({"query": query})
    _search_web_capped.name = "search_web"

    tools = [read_sop, record_finding]
    if PINECONE_API_KEY:
        tools.insert(0, retrieve_regulation_rag)
    if use_tavily:
        tools.append(_search_web_capped)
    return tools, recorded_findings


_AUDIT_SUBAGENT_PROMPT_RAG = """You are an expert regulatory compliance auditor assessing a single SOP for Meridian Health Technologies, an AI-powered healthcare fintech company.

## Your Task
Audit the SOP against ALL applicable regulations. You must determine which regulations are relevant based on the SOP's content and business unit.

## Process
1. First, call `read_sop` to review the SOP content
2. Work through regulations ONE AT A TIME. For each applicable regulation:
   a. Retrieve the relevant sections from the knowledge base (2–4 targeted queries)
   b. Assess the SOP against each requirement you found
   c. Call `record_finding` for EACH requirement IMMEDIATELY after assessing it — before moving to the next regulation
3. If you need clarification on a regulation's current interpretation, use `search_web`
4. After all requirements are assessed, output a single short sentence summarizing counts (e.g. "Done — 12 findings recorded."). Do NOT repeat findings in your final message.

IMPORTANT: Retrieve, assess, and record findings for each regulation before moving to the next. This ensures partial progress is saved if the audit is interrupted.

## Rules
- Every `retrieve_regulation_rag` and `search_web` call MUST include a non-empty `query` argument. Never emit a tool call with empty `{}` args — if you have nothing specific to search for, don't call the tool. When issuing parallel tool calls, double-check that each call's argument dict contains a concrete `query` string.
- Be thorough: check EVERY regulation that could apply
- Be specific: cite exact regulatory sections
- Be efficient: you have a budget of ~30 retrieval calls total. Use 2–4 targeted queries per regulation, not dozens. Once you have enough context for a regulation, record your findings and move on.
- Do NOT downgrade severity for aspirational language
- Skip regulations clearly irrelevant to this SOP's scope
- If a retrieval tool call fails (returns an error), do NOT cite that regulation's requirements from memory. Only record findings based on text you successfully retrieved. State that retrieval failed in your summary.

## CRITICAL: Output Method
For EACH requirement you assess, IMMEDIATELY call `record_finding` with these fields:
- requirement_id: short identifier (e.g. "HIPAA-164.312(a)", "CC6.1", "GDPR-Art.32")
- requirement_title: brief title
- regulation: which regulation (e.g. "HIPAA", "SOC 2", "GDPR")
- compliance_level: "compliant" | "partial" | "gap"
- severity: "critical" | "high" | "medium" | "low" | "info"
- evidence_quote: exact quote from the SOP (empty string if none)
- gap_description: what is missing (empty string if compliant)
- remediation: specific recommendation (empty string if compliant)
- reasoning: 2-3 sentences citing the specific regulation section

Call `record_finding` ONCE PER REQUIREMENT as you go. Do NOT accumulate findings for a batch output.
After calling `record_finding` for every requirement, your FINAL message should be a single short sentence (e.g. "Done — 12 findings recorded."). Do NOT list findings in your final message — the harness reads them from record_finding calls."""

def _build_subagent_model(provider: str = "nebius", model_name: str | None = None):
    """Build the ChatOpenAI model for audit sub-agents.

    All instances share a single httpx.Client via ``_get_shared_http_client()``
    so that ThreadPoolExecutor workers reuse one connection pool instead of each
    creating their own (which caused DNS-exhaustion failures at 50 workers).
    """
    from sentinel.chat_model import build_chat_model
    from sentinel.config import MODEL_MAX_TOKENS
    return build_chat_model(
        provider,
        model=model_name,
        max_tokens=MODEL_MAX_TOKENS,
        http_client=_get_shared_http_client(),
        reasoning=True,
    )


def _parse_findings_json(messages) -> str | None:
    """Extract a JSON findings array from sub-agent messages (backwards compat fallback)."""
    for msg in reversed(messages):
        content = msg.content if hasattr(msg, "content") else str(msg)
        if not isinstance(content, str) or "[" not in content:
            continue

        if "```" in content:
            fence_start = content.find("```")
            lang_end = content.find("\n", fence_start)
            inner_start = lang_end + 1 if lang_end > fence_start else fence_start + 3
            fence_end = content.find("```", inner_start)
            if fence_end > inner_start:
                content = content[inner_start:fence_end].strip()

        start_idx = content.find("[")
        if start_idx < 0:
            continue

        candidate = content[start_idx:]
        end_idx = candidate.rfind("]")
        if end_idx > 0:
            candidate = candidate[: end_idx + 1]

        try:
            parsed = json.loads(candidate)
            if isinstance(parsed, list) and parsed and isinstance(parsed[0], dict):
                return candidate
        except json.JSONDecodeError:
            repaired = candidate.rstrip().rstrip(",")
            if not repaired.endswith("}"):
                last_brace = repaired.rfind("}")
                if last_brace > 0:
                    repaired = repaired[: last_brace + 1]
            repaired += "]"
            try:
                parsed = json.loads(repaired)
                if isinstance(parsed, list) and parsed and isinstance(parsed[0], dict):
                    return repaired
            except json.JSONDecodeError:
                continue
    return None


def _audit_single_sop_impl(sop_id: str, provider: str = "nebius", use_tavily: bool = True, model_name: str | None = None) -> SopAuditResult:
    """Core implementation for auditing a single SOP."""
    from langchain.agents import create_agent
    from sentinel.retrieval.local import load_sop_by_id, load_sop_chunks

    sop = load_sop_by_id(sop_id)
    if sop is None:
        return SopAuditResult(f"SOP not found: {sop_id}", [], status="invalid")

    fm = sop["frontmatter"]
    chunks = load_sop_chunks(sop)
    if not chunks:
        return SopAuditResult(f"SOP {sop_id} has no content", [], status="invalid")

    actual_id = fm.get("sop_id", sop_id)
    title = fm.get("title", "")
    business_unit = fm.get("business_unit", "")
    sop_text = "\n\n---\n\n".join(f"[{c.section}]\n{c.chunk_text}" for c in chunks)

    subagent_tools, recorded_findings = _build_subagent_tools(sop_text, actual_id, title, use_tavily=use_tavily)
    model = _build_subagent_model(provider, model_name=model_name)

    subagent = create_agent(
        model=model,
        tools=subagent_tools,
        system_prompt=_AUDIT_SUBAGENT_PROMPT_RAG,
        name="sop_auditor",
    )

    from langchain_core.callbacks import UsageMetadataCallbackHandler

    # Token usage is accumulated in a callback so counts survive exceptions
    # mid-run — tokens burned up to a crash were still billed.
    usage_cb = UsageMetadataCallbackHandler()

    start = time.time()
    result = None
    truncated = False
    try:
        result = subagent.invoke(
            {
                "messages": [{
                    "role": "user",
                    "content": f"Audit SOP {actual_id}: {title} (Business Unit: {business_unit})",
                }],
            },
            config={"recursion_limit": 120, "callbacks": [usage_cb]},
        )
    except Exception as e:
        elapsed = time.time() - start
        logger.error("Sub-agent for %s failed after %.1fs: %s", actual_id, elapsed, e)
        if not recorded_findings:
            sub_in, sub_out = _usage_from_callback(usage_cb)
            return SopAuditResult(
                f"FAILED: {actual_id} — sub-agent error: {e}", [], sub_in, sub_out,
                status="failed", rate_limited=_is_rate_limited_error(str(e)),
            )
        logger.info("%s: sub-agent errored but %d findings were recorded via tool — surfacing partial results", actual_id, len(recorded_findings))
        truncated = True
    else:
        elapsed = time.time() - start

    messages = result.get("messages", []) if result else []
    sub_in, sub_out = _usage_from_callback(usage_cb)
    if sub_in == 0 and sub_out == 0:
        # Fall back to message-attached usage if the callback saw nothing.
        sub_in = sum(
            usage.get("input_tokens", 0)
            for msg in messages
            if (usage := getattr(msg, "usage_metadata", None))
        )
        sub_out = sum(
            usage.get("output_tokens", 0)
            for msg in messages
            if (usage := getattr(msg, "usage_metadata", None))
        )

    # Detect truncation from the last AI message. Don't reset `truncated` here:
    # an exception with partial recorded findings already set it True above
    # (and `messages` is empty on that path, so the loop won't re-detect it).
    for msg in reversed(messages):
        if getattr(msg, "type", "") == "ai":
            rm = getattr(msg, "response_metadata", None) or {}
            if isinstance(rm, dict) and rm.get("finish_reason") == "length":
                truncated = True
                logger.warning("Sub-agent for %s was truncated (finish_reason=length)", actual_id)
            content = getattr(msg, "content", None)
            if not truncated and (content is None or content == ""):
                truncated = True
                logger.warning("Sub-agent for %s produced empty final message (likely truncated)", actual_id)
            break

    # Phase 1: Use tool-recorded findings if available
    items = []
    findings_source = "none"

    if recorded_findings:
        items = list(recorded_findings)
        findings_source = "tool"
        logger.info("%s: %d findings recorded via record_finding tool", actual_id, len(items))

    # Phase 2: Fall back to JSON parsing from messages (backwards compat)
    if not items:
        findings_json = _parse_findings_json(messages)
        if findings_json:
            try:
                parsed = json.loads(findings_json)
                if isinstance(parsed, list):
                    items = parsed
                else:
                    items = [parsed]
                findings_source = "json"
            except json.JSONDecodeError:
                pass

    if not items:
        suffix = " (response was truncated)" if truncated else ""
        return SopAuditResult(
            f"SOP {actual_id}: sub-agent did not produce structured findings{suffix}",
            [], sub_in, sub_out,
            status="truncated" if truncated else "no_findings",
        )

    findings = []
    for data in items:
        rid = data.get("requirement_id", data.get("clause_id", ""))
        try:
            findings.append(AuditFinding(
                clause_id=rid,
                clause_title=data.get("requirement_title", data.get("clause_title", "")),
                regulation=data.get("regulation", ""),
                sop_id=actual_id,
                sop_title=title,
                business_unit=business_unit,
                compliance_level=normalize_compliance_level(data.get("compliance_level", "gap")),
                severity=normalize_severity(data.get("severity", "high")),
                evidence_quote=data.get("evidence_quote", ""),
                gap_description=data.get("gap_description", ""),
                remediation=data.get("remediation", ""),
                reasoning=data.get("reasoning", ""),
            ))
        except (ValueError, KeyError):
            continue

    compliant = sum(1 for f in findings if f.compliance_level == ComplianceLevel.COMPLIANT)
    partial = sum(1 for f in findings if f.compliance_level == ComplianceLevel.PARTIAL)
    gap = sum(1 for f in findings if f.compliance_level == ComplianceLevel.GAP)

    partial_tag = " [PARTIAL — sub-agent hit limit]" if (truncated and findings_source == "tool") else (" [truncated]" if truncated else "")
    lines = [f"{actual_id} ({title}): {len(findings)} findings — {compliant}C/{partial}P/{gap}G{partial_tag}"]
    for f in findings:
        lines.append(f"  {f.clause_id}: {f.compliance_level.value} ({f.severity.value}) — {f.gap_description or 'Compliant'}")
    lines.append(format_sub_agent_tokens(sub_in, sub_out))
    return SopAuditResult(
        "\n".join(lines), findings, sub_in, sub_out,
        status="truncated" if truncated else "ok",
    )


def _usage_from_callback(usage_cb) -> tuple[int, int]:
    """Sum (input_tokens, output_tokens) across all models seen by a
    UsageMetadataCallbackHandler."""
    totals = usage_cb.usage_metadata.values()
    return (
        sum(u.get("input_tokens", 0) for u in totals),
        sum(u.get("output_tokens", 0) for u in totals),
    )


def _is_rate_limited_error(error_text: str) -> bool:
    """Sniff an exception/transport message (never LLM-generated text) for
    rate-limit markers."""
    lowered = error_text.lower()
    return "429" in error_text or "rate limit" in lowered or "quota" in lowered or "exceeded" in lowered


def _is_retryable(result: SopAuditResult) -> bool:
    """Check if a single-SOP audit result indicates a retryable failure.

    Reads the structured status, never the summary text — summaries embed
    model-written gap descriptions that can legitimately contain "FAILED".
    Truncation is NOT retryable — it will just truncate again.
    """
    return result.status in ("failed", "no_findings")


def _retry_delay(attempt: int, rate_limited: bool) -> float:
    """Compute retry delay with jitter. Longer for rate limits."""
    import random
    base = RATE_LIMIT_BACKOFF if rate_limited else RETRY_BACKOFF
    delay = base * attempt
    return delay + random.uniform(0, delay * 0.5)


def _audit_single_sop_with_retry(
    sop_id: str,
    provider: str = "nebius",
    use_tavily: bool = True,
    model_name: str | None = None,
) -> SopAuditResult:
    """Audit one SOP, retrying transient failures. Tokens accumulate across every
    attempt (failed attempts are still billed); the returned findings are the
    final attempt's."""
    result = _audit_single_sop_impl(sop_id, provider=provider, use_tavily=use_tavily, model_name=model_name)
    tok_in, tok_out = result.input_tokens, result.output_tokens
    for attempt in range(1, MAX_RETRIES + 1):
        if not _is_retryable(result):
            break
        delay = _retry_delay(attempt, result.rate_limited)
        logger.info("Retry attempt %d/%d for %s (waiting %.0fs)", attempt, MAX_RETRIES, sop_id, delay)
        time.sleep(delay)
        result = _audit_single_sop_impl(sop_id, provider=provider, use_tavily=use_tavily, model_name=model_name)
        tok_in += result.input_tokens
        tok_out += result.output_tokens
    return result._replace(input_tokens=tok_in, output_tokens=tok_out)


def _audit_all_sops_impl(run_one, max_workers: int | None = None) -> str:
    """Core implementation for auditing all SOPs.

    ``run_one`` is a callable ``(sop_id) -> SopAuditResult``. Results are
    aggregated from the returned values (no shared module state), so a process
    can run repeated or concurrent audits without contaminating totals.

    Retries happen inside ``run_one`` (per-SOP, up to MAX_RETRIES attempts);
    there is deliberately no second batch-level retry layer here — stacking
    the two multiplied to MAX_RETRIES² sub-agent runs per stubborn SOP.
    """
    import concurrent.futures
    from sentinel.config import MAX_AUDIT_WORKERS
    from sentinel.retrieval.local import list_all_sops

    workers = max_workers or MAX_AUDIT_WORKERS
    all_sops = list_all_sops()

    def _audit_one(sop_meta: dict) -> SopAuditResult:
        sid = sop_meta["sop_id"]
        try:
            return run_one(sid)
        except Exception as e:
            return SopAuditResult(
                f"{sid}: FAILED — {e}", [],
                status="failed", rate_limited=_is_rate_limited_error(str(e)),
            )

    results_by_id: dict[str, SopAuditResult] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(_audit_one, s): s["sop_id"] for s in all_sops}
        for future in concurrent.futures.as_completed(futures):
            sid = futures[future]
            results_by_id[sid] = future.result()

    results = list(results_by_id.values())
    still_failed = sum(1 for r in results if _is_retryable(r))

    findings = [f for r in results for f in r.findings]
    total = len(findings)
    compliant = sum(1 for f in findings if f.compliance_level == ComplianceLevel.COMPLIANT)
    partial = sum(1 for f in findings if f.compliance_level == ComplianceLevel.PARTIAL)
    gap = sum(1 for f in findings if f.compliance_level == ComplianceLevel.GAP)

    # Per-SOP retry already accumulates tokens across attempts into each result.
    tok_in = sum(r.input_tokens for r in results)
    tok_out = sum(r.output_tokens for r in results)

    summary = (
        f"Audit complete: {total} findings across {len(all_sops)} SOPs\n"
        f"  Compliant: {compliant} ({100*compliant//max(total,1)}%)\n"
        f"  Partial:   {partial} ({100*partial//max(total,1)}%)\n"
        f"  Gap:       {gap} ({100*gap//max(total,1)}%)\n"
        f"  {format_total_tokens(tok_in, tok_out)}\n"
        f"  Failed after retries: {still_failed}\n\n"
        "Per-SOP breakdown:\n" + "\n".join(sorted(r.summary for r in results))
    )
    return summary


def _slug(text: str) -> str:
    """Lowercase, alphanumeric-and-dashes slug for Jira labels."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def _render_ticket_description(
    *,
    sop_id: str,
    clause_id: str,
    clause_title: str,
    regulation: str,
    severity: str,
    gap_description: str,
    remediation: str,
    evidence_quote: str,
    reasoning: str,
) -> str:
    """Render a plain-text Jira description with section headers. ADF wrapping happens in the client."""
    parts: list[str] = []
    parts.append(f"SOP: {sop_id}")
    parts.append(f"Regulation: {regulation}")
    parts.append(f"Clause: {clause_id} — {clause_title}")
    parts.append(f"Severity: {severity}")
    if evidence_quote:
        parts.append(f"Evidence:\n  \"{evidence_quote.strip()}\"")
    parts.append(f"Gap:\n  {gap_description}")
    if remediation:
        parts.append(f"Recommended remediation:\n  {remediation}")
    if reasoning:
        parts.append(f"Reasoning:\n  {reasoning}")
    parts.append("Filed automatically by the Sentinel compliance agent.")
    return "\n\n".join(parts)


def _jira_config() -> tuple[dict, list[str]]:
    """Return (Jira config kwargs, list of missing required env-var names)."""
    from sentinel.config import (
        JIRA_API_TOKEN,
        JIRA_BASE_URL,
        JIRA_DEFAULT_ISSUE_TYPE,
        JIRA_EMAIL,
        JIRA_PROJECT_KEY,
    )
    cfg = {
        "base_url": JIRA_BASE_URL,
        "email": JIRA_EMAIL,
        "api_token": JIRA_API_TOKEN,
        "project_key": JIRA_PROJECT_KEY,
        "issue_type": JIRA_DEFAULT_ISSUE_TYPE,
    }
    required = ["JIRA_BASE_URL", "JIRA_EMAIL", "JIRA_API_TOKEN", "JIRA_PROJECT_KEY"]
    keys = ["base_url", "email", "api_token", "project_key"]
    missing = [name for name, key in zip(required, keys) if not cfg[key]]
    return cfg, missing


def _make_jira_client(cfg: dict):
    from sentinel.actuation.jira_client import JiraClient
    return JiraClient(
        base_url=cfg["base_url"],
        email=cfg["email"],
        api_token=cfg["api_token"],
        project_key=cfg["project_key"],
        issue_type=cfg["issue_type"],
    )


def _build_jira_issue_fields(
    *,
    sop_id: str,
    clause_id: str,
    clause_title: str,
    regulation: str,
    severity: str,
    gap_description: str,
    remediation: str = "",
    evidence_quote: str = "",
    reasoning: str = "",
) -> tuple[str, list[str], str, str]:
    """Build the (summary, labels, description, priority) for one finding's ticket."""
    from sentinel.actuation.jira_client import SEVERITY_TO_PRIORITY
    sev = (severity or "").strip().lower()
    if sev not in SEVERITY_TO_PRIORITY:
        sev = "medium"

    summary = f"[{sev.upper()}] {clause_id}: {clause_title} ({sop_id})"
    labels = sorted({
        "sentinel",
        "compliance-finding",
        f"sev-{sev}",
        _slug(regulation) or "regulation",
        _slug(sop_id) or "sop",
    })
    description = _render_ticket_description(
        sop_id=sop_id,
        clause_id=clause_id,
        clause_title=clause_title,
        regulation=regulation,
        severity=sev,
        gap_description=gap_description,
        remediation=remediation,
        evidence_quote=evidence_quote,
        reasoning=reasoning,
    )
    return summary, labels, description, SEVERITY_TO_PRIORITY[sev]


@tool
def create_jira_ticket(
    sop_id: str,
    clause_id: str,
    clause_title: str,
    regulation: str,
    severity: str,
    gap_description: str,
    remediation: str = "",
    evidence_quote: str = "",
    reasoning: str = "",
) -> str:
    """Create a Jira ticket for a confirmed compliance gap in the project configured via JIRA_PROJECT_KEY.

    Call this when an audit finding has compliance_level 'gap' or 'partial' AND severity is medium or higher,
    so a human assignee can act on it. One call creates one ticket. Returns the issue key and URL on success.

    Args:
        sop_id: SOP identifier (e.g. 'SOP-ISEC-002')
        clause_id: regulatory clause identifier (e.g. 'HIPAA-164.312(a)', 'CC6.1')
        clause_title: short title of the clause (e.g. 'Access Control')
        regulation: regulation name (e.g. 'HIPAA', 'SOC 2', 'GDPR')
        severity: one of 'critical', 'high', 'medium', 'low', 'info'
        gap_description: what is missing or insufficient in the SOP
        remediation: recommended remediation (optional)
        evidence_quote: exact quote from the SOP (optional)
        reasoning: 2-3 sentence rationale citing the regulation (optional)
    """
    cfg, missing = _jira_config()
    if missing:
        return f"Jira not configured — set {', '.join(missing)} in the environment"

    summary, labels, description, priority = _build_jira_issue_fields(
        sop_id=sop_id,
        clause_id=clause_id,
        clause_title=clause_title,
        regulation=regulation,
        severity=severity,
        gap_description=gap_description,
        remediation=remediation,
        evidence_quote=evidence_quote,
        reasoning=reasoning,
    )

    try:
        client = _make_jira_client(cfg)
        try:
            issue = client.create_issue(
                summary=summary,
                description=description,
                labels=labels,
                priority=priority,
            )
        finally:
            client.close()
        return f"Filed Jira ticket {issue['key']} at {issue['url']}"
    except Exception as e:
        logger.exception("create_jira_ticket failed")
        return f"Jira ticket creation failed: {e}"


@tool
def create_jira_tickets(findings_json: str) -> str:
    """Create multiple Jira tickets at once for confirmed compliance gaps.

    Use this instead of calling create_jira_ticket repeatedly.
    Pass a JSON array string where each object has: sop_id, clause_id, clause_title, regulation, severity, gap_description.
    Optional fields: remediation, evidence_quote, reasoning.

    Example: '[{"sop_id":"SOP-ISEC-008","clause_id":"HIPAA-164.312(a)","clause_title":"Access Control","regulation":"HIPAA","severity":"high","gap_description":"Missing MFA requirement"}]'

    Returns a summary of created tickets and any failures.
    """
    try:
        findings = json.loads(findings_json)
    except (json.JSONDecodeError, TypeError):
        return "Invalid JSON. Pass a JSON array string of finding objects."
    if not isinstance(findings, list):
        return "Expected a JSON array of findings."

    cfg, missing = _jira_config()
    if missing:
        return f"Jira not configured — set {', '.join(missing)} in the environment"
    if not findings:
        return "No findings provided."

    client = _make_jira_client(cfg)
    created = []
    failed = []
    try:
        for i, f in enumerate(findings):
            if not isinstance(f, dict):
                failed.append(f"item {i}: expected an object, got {type(f).__name__}")
                continue
            sop_id = f.get("sop_id", "")
            clause_id = f.get("clause_id", f.get("requirement_id", ""))
            summary, labels, description, priority = _build_jira_issue_fields(
                sop_id=sop_id,
                clause_id=clause_id,
                clause_title=f.get("clause_title", f.get("requirement_title", "")),
                regulation=f.get("regulation", ""),
                severity=f.get("severity", "medium"),
                gap_description=f.get("gap_description", ""),
                remediation=f.get("remediation", ""),
                evidence_quote=f.get("evidence_quote", ""),
                reasoning=f.get("reasoning", ""),
            )
            try:
                issue = client.create_issue(
                    summary=summary, description=description,
                    labels=labels, priority=priority,
                )
                created.append(f"{issue['key']} — {clause_id} ({sop_id})")
            except Exception as e:
                failed.append(f"{clause_id} ({sop_id}): {e}")
    finally:
        client.close()

    lines = [f"Created {len(created)} Jira ticket(s), {len(failed)} failed."]
    for t in created:
        lines.append(f"  ✓ {t}")
    for f in failed:
        lines.append(f"  ✗ {f}")
    return "\n".join(lines)


def build_tools(provider: str = "nebius", use_tavily: bool = True, model_name: str | None = None) -> list:
    """Build the complete tool list for the agent, parameterized by provider, Tavily, and optional model_name override."""

    def _run_one(sop_id: str) -> SopAuditResult:
        return _audit_single_sop_with_retry(sop_id, provider=provider, use_tavily=use_tavily, model_name=model_name)

    @tool
    def _audit_single_sop(sop_id: str) -> str:
        """Audit one SOP against all relevant regulations using a sub-agent with access to the regulation knowledge base. Accepts an SOP ID (e.g. 'SOP-AIML-009') or title (e.g. 'Algorithmic Bias Detection'). The sub-agent determines which regulations apply and iteratively retrieves regulatory text."""
        return _run_one(sop_id).summary

    @tool
    def _audit_sops(sop_ids: list[str]) -> str:
        """Audit a specific list of SOPs in parallel using sub-agents. Accepts a list of SOP IDs (e.g. ['SOP-AIML-009', 'SOP-ISEC-008']) or titles. Use this when the user asks to audit a subset of SOPs — by business unit, regulation, or explicit list. For ALL SOPs, use audit_all_sops instead."""
        import concurrent.futures
        from sentinel.config import MAX_AUDIT_WORKERS

        if not sop_ids:
            return "No SOP IDs provided."

        workers = min(len(sop_ids), MAX_AUDIT_WORKERS)
        results_by_id: dict[str, SopAuditResult] = {}

        def _audit_one(sid: str) -> SopAuditResult:
            try:
                return _run_one(sid)
            except Exception as e:
                return SopAuditResult(
                    f"{sid}: FAILED — {e}", [],
                    status="failed", rate_limited=_is_rate_limited_error(str(e)),
                )

        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            futures = {executor.submit(_audit_one, sid): sid for sid in sop_ids}
            for future in concurrent.futures.as_completed(futures):
                sid = futures[future]
                results_by_id[sid] = future.result()

        results = list(results_by_id.values())
        still_failed = sum(1 for r in results if _is_retryable(r))

        tok_in = sum(r.input_tokens for r in results)
        tok_out = sum(r.output_tokens for r in results)

        summary = (
            f"Audit complete: {len(sop_ids)} SOPs\n"
            f"  Failed: {still_failed}\n"
            f"  {format_total_tokens(tok_in, tok_out)}\n\n"
            "Per-SOP breakdown:\n" + "\n".join(sorted(r.summary for r in results))
        )
        return summary

    @tool
    def _audit_all_sops() -> str:
        """Run the full audit across ALL 200 SOPs using sub-agents. Each SOP gets its own auditor sub-agent with access to the regulation knowledge base. Fans out with configurable parallelism (MAX_AUDIT_WORKERS)."""
        return _audit_all_sops_impl(_run_one)

    _audit_single_sop.name = "audit_single_sop"
    _audit_sops.name = "audit_sops"
    _audit_all_sops.name = "audit_all_sops"

    tools = [
        list_sops,
        list_regulations,
        retrieve_regulation_text_tool,
        _audit_single_sop,
        _audit_sops,
        _audit_all_sops,
        create_jira_ticket,
        create_jira_tickets,
    ]
    if use_tavily:
        tools.insert(3, search_web)
    return tools

// Forge-styled Audit screen — composer + Jira-sourced findings register

const AUDIT_AGENTS = [
  { key: "sentinel_prototype",      graph_id: "sentinel_prototype",     label: "Prototype",   sublabel: "GPT-5.5",                                       pricing: { input: 5.00, output: 30.00 } },
  { key: "sentinel_prototype_plus", graph_id: "sentinel_grounded", label: "Grounded",    sublabel: "GPT-5.5 + Tavily",                              pricing: { input: 5.00, output: 30.00 } },
  { key: "sentinel_production",     graph_id: "sentinel_optimized",          label: "Optimized",   sublabel: "DeepSeek-V4-Pro + Tavily",                      pricing: { input: 1.75, output: 3.50 } },
  { key: "sentinel_nemotron",       graph_id: "sentinel_nemotron", label: "Production",  sublabel: "Nemotron-Ultra + Tavily + LangSmith + Snowglobe", pricing: { input: 1.00, output: 3.00 } },
];


const AuditScreen = ({ loadStatus }) => {
  const _ls = loadStatus || {};
  const kbLoading       = _ls.kb       === "loading";
  const data = window.SENTINEL_DATA || {};
  const kb = data.kbStats || { sop_count: 200, regulation_count: 36, regulations: [] };
  const [findingsVersion, setFindingsVersion] = React.useState(0);
  const findingsLoading = _ls.findings === "loading" && findingsVersion === 0;
  const findingsResp = data.findings || { issues: [], jira_configured: false };
  const findings = findingsResp.issues || [];

  // composer state
  const [draft, setDraft] = React.useState("");
  const [selectedAgent, setSelectedAgent] = React.useState("sentinel_nemotron");
  const [audit, setAudit] = React.useState({
    status: "idle",        // idle | running | done | error
    tokens: [],            // streamed text chunks
    toolCalls: [],         // {name, args, result?, t}
    inputTokens: 0,
    outputTokens: 0,
    error: null,
    startedAt: null,
    endedAt: null,
    traceUrl: null,
  });
  const streamRef = React.useRef(null);

  const sopCount = kb.sop_count ?? 200;
  const regCount = kb.regulation_count ?? 36;
  const regList  = (kb.regulations || []).join(", ") || "HIPAA, SOC 2, GDPR, EU AI Act, NIST AI RMF, SR 11-7, California SB 53/942, AB 853, BSA, ECOA, FCRA, PCI DSS, OWASP, FDA, NIST SP 800-series, EU AMLD4/ePrivacy/MDR/SCCs";

  const sendAudit = (text) => {
    if (!text || audit.status === "running") return;
    const ctrl = new AbortController();
    streamRef.current = ctrl;
    setAudit({
      status: "running", tokens: [], toolCalls: [],
      inputTokens: 0, outputTokens: 0, error: null,
      startedAt: Date.now(), endedAt: null,
      traceUrl: null,
    });
    const graphId = (AUDIT_AGENTS.find(a => a.key === selectedAgent) || {}).graph_id || selectedAgent;
    window.ForgeAPI.streamAudit(text, graphId, {
      signal: ctrl.signal,
      onEvent: (ev) => {
        setAudit(prev => {
          if (ev.type === "run_started") {
            return { ...prev, traceUrl: ev.trace_url };
          }
          if (ev.type === "token") {
            return { ...prev, tokens: [...prev.tokens, ev.text] };
          }
          if (ev.type === "tool_call") {
            return { ...prev, toolCalls: [...prev.toolCalls, { name: ev.name, args: ev.args, t: Date.now() }] };
          }
          if (ev.type === "tool_result") {
            const tc = [...prev.toolCalls];
            for (let i = tc.length - 1; i >= 0; i--) {
              if (!tc[i].result) { tc[i] = { ...tc[i], result: ev.text }; break; }
            }
            return { ...prev, toolCalls: tc };
          }
          if (ev.type === "usage") {
            return { ...prev, inputTokens: ev.input_tokens, outputTokens: ev.output_tokens };
          }
          if (ev.type === "error") {
            return { ...prev, error: ev.error, status: "error" };
          }
          return prev;
        });
      },
      onDone:  () => setAudit(prev => ({ ...prev, status: prev.status === "error" ? "error" : "done", endedAt: Date.now() })),
      onError: (err) => setAudit(prev => ({ ...prev, error: err.message, status: "error", endedAt: Date.now() })),
    });
  };

  // Re-fetch Jira findings when an audit run completes with ticket creations
  React.useEffect(() => {
    if (audit.status !== "done") return;
    const hasTickets = audit.toolCalls.some(tc =>
      (tc.name === "create_jira_ticket" && tc.result && !tc.result.startsWith("Jira ticket creation failed")) ||
      (tc.name === "create_jira_tickets" && tc.result && tc.result.includes("Created"))
    );
    if (!hasTickets) return;
    const API = window.ForgeAPI;
    if (!API) return;
    API.getFindings().then(d => {
      window.SENTINEL_DATA.findings = d;
      setFindingsVersion(v => v + 1);
    }).catch(() => {});
  }, [audit.status]);

  // Keep the elapsed counter ticking even when no SSE event has arrived
  // (slow tool call, model warm-up). Cleared as soon as status leaves "running".
  const [, setTick] = React.useState(0);
  React.useEffect(() => {
    if (audit.status !== "running") return;
    const id = setInterval(() => setTick(t => t + 1), 200);
    return () => clearInterval(id);
  }, [audit.status]);

  const elapsedSec = audit.startedAt
    ? ((audit.endedAt || Date.now()) - audit.startedAt) / 1000
    : 0;
  const responseText = audit.tokens.join("");

  const totalIn = audit.inputTokens;
  const totalOut = audit.outputTokens;

  return (
    <div style={{ padding: "28px 32px", display: "flex", flexDirection: "column", gap: 28 }}>

      {/* ─── HERO SLAB ─── */}
      <Slab padding={36}>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1.05fr", gap: 40, alignItems: "center" }}>
          {/* Left: kicker + title + body */}
          <div>
            <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 28 }}>
              <span className="f-kicker" style={{ color: "var(--forge-on-dark-mute)" }}>Live audit</span>
            </div>
            <h1 style={{
              margin: 0, font: "700 64px/1.02 var(--forge-font)",
              letterSpacing: "-0.025em", color: "var(--forge-on-dark-strong)"
            }}>Sentinel<br />Audit Engine</h1>
            <p style={{
              margin: "22px 0 0", font: "400 16px/24px var(--forge-font)",
              color: "var(--forge-on-dark-mute)", maxWidth: 480
            }}>
              Auditing <strong style={{ color: "var(--forge-on-dark)" }}>{sopCount} SOPs</strong> from{" "}
              <strong style={{ color: "var(--forge-on-dark)" }}>Meridian Health Tech</strong> against {regCount} regulations.
              ReAct sub-agent fan-out, region-pinned on Nebius GPUs, retrieval grounded in Pinecone.
            </p>
          </div>

          {/* Right: 1×2 stat grid */}
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 14, position: "relative" }}>
            <StatCard
              kicker={<span style={{ display: "inline-flex", alignItems: "center", gap: 6 }}>
                SOPs in scope{kbLoading && <Spinner size={9} color="var(--forge-lime)"/>}
              </span>}
              value={sopCount}
              body="Across 10 business units of Meridian Health Tech." />
            <StatCard
              kicker={<span style={{ display: "inline-flex", alignItems: "center", gap: 6 }}>
                Policies in scope{kbLoading && <Spinner size={9} color="var(--forge-lime)"/>}
              </span>}
              value={regCount}
              body={regList} />
          </div>
        </div>
      </Slab>

      {/* ─── COMPOSER + LIVE STREAM ─── */}
      <Slab padding={28}>
        <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 8 }}>
          <span className="f-kicker">ReAct stream</span>
          {audit.status === "running" && <StatusChip tone="running"><Spinner size={9} color="var(--forge-lime)" /> Running</StatusChip>}
          {audit.status === "done"    && <StatusChip tone="warm"><Icon name="check" size={9} color="var(--forge-mint-warm)" stroke={3}/> Done</StatusChip>}
          {audit.status === "error"   && <StatusChip tone="danger">Error</StatusChip>}
          {audit.status === "idle"    && <StatusChip tone="cold">Idle</StatusChip>}
        </div>
        <h2 style={{ margin: "0 0 24px", font: "700 28px/1.1 var(--forge-font)", letterSpacing: "-0.015em", color: "var(--forge-on-dark-strong)" }}>Ask the audit agent</h2>

        {/* Composer */}
        <div style={{
          marginBottom: 18,
          border: "1px solid var(--forge-border-dark)",
          borderRadius: 14,
          background: "var(--forge-ink-2)",
          overflow: "hidden"
        }}>
          <div style={{ padding: "20px 22px", display: "flex", alignItems: "flex-start", gap: 14 }}>
            <div style={{ width: 28, height: 28, borderRadius: 8, background: "rgba(212,250,80,0.12)", display: "grid", placeItems: "center", flexShrink: 0, marginTop: 2 }}>
              <Icon name="search" size={13} color="var(--forge-lime)" />
            </div>
            <textarea
              rows={3}
              value={draft}
              onChange={(e) => setDraft(e.target.value)}
              onKeyDown={(e) => { if (e.key === "Enter" && !e.shiftKey && draft.trim()) { e.preventDefault(); sendAudit(draft.trim()); } }}
              placeholder="Ask the auditor — e.g. ‘Audit SOP-ISEC-008 against HIPAA §164.312’"
              disabled={audit.status === "running"}
              style={{
                flex: 1, minWidth: 0, border: 0, outline: "none",
                background: "transparent",
                font: "400 15px/22px var(--forge-font)",
                color: "var(--forge-on-dark)",
                letterSpacing: "-0.005em",
                opacity: audit.status === "running" ? 0.6 : 1,
                resize: "vertical",
                minHeight: 66,
              }} />
            <Btn
              variant="lime"
              size="m"
              onClick={() => sendAudit(draft.trim())}
              disabled={!draft.trim() || audit.status === "running"}
              icon={<Icon name="send" size={12} color="var(--forge-ink)" stroke={2.5} />}
              style={{ marginTop: 2, flexShrink: 0 }}>
              Send
            </Btn>
          </div>

          {/* Agent picker */}
          <div style={{
            padding: "12px 18px",
            borderTop: "1px solid var(--forge-border-dark)",
            background: "rgba(0,0,0,0.08)",
            display: "flex", alignItems: "center", gap: 10, flexWrap: "wrap"
          }}>
            <span className="f-kicker" style={{ color: "var(--forge-on-dark-faint)" }}>Agent</span>
            {AUDIT_AGENTS.map(a => (
              <TemplateChip
                key={a.key}
                selected={selectedAgent === a.key}
                disabled={a.disabled}
                onClick={() => !a.disabled && audit.status !== "running" && setSelectedAgent(a.key)}>
                {a.label}
                {a.sublabel && <span style={{ fontWeight: 400, opacity: 0.7 }}>{a.sublabel}</span>}
              </TemplateChip>
            ))}
          </div>

        </div>

        {/* Live stream output */}
        {audit.status !== "idle" && (
          <div style={{
            border: "1px solid var(--forge-border-dark)",
            borderRadius: 12,
            background: "var(--forge-ink-2)",
            overflow: "hidden",
          }}>
            {/* Meter row — matches Compare section style */}
            <div style={{
              display: "flex", alignItems: "center", gap: 12,
              padding: "16px 24px", borderBottom: "1px solid var(--forge-border-dark)",
              background: "rgba(255,255,255,0.02)",
            }}>
              <div style={{ flex: 1 }}><Meter label="elapsed" value={`${elapsedSec.toFixed(1)}s`} live={audit.status === "running"}/></div>
              <div style={{ flex: 1 }}><Meter label="tokens in" value={`${(totalIn / 1000).toFixed(1)}k`}/></div>
              <div style={{ flex: 1 }}><Meter label="tokens out" value={`${(totalOut / 1000).toFixed(1)}k`}/></div>
              <div style={{ flex: 1 }}><Meter label="tools" value={audit.toolCalls.length}/></div>
              <div style={{ flex: 1 }}><Meter label="jira tickets" value={audit.toolCalls.reduce((n, tc) => {
                if (tc.name === "create_jira_ticket" && tc.result && !tc.result.startsWith("Jira ticket creation failed")) return n + 1;
                if (tc.name === "create_jira_tickets" && tc.result) { const m = tc.result.match(/Created (\d+)/); if (m) return n + parseInt(m[1], 10); }
                return n;
              }, 0)}/></div>
              {(() => {
                const ag = AUDIT_AGENTS.find(a => a.key === selectedAgent);
                if (!ag || !ag.pricing) return null;
                const cost = (totalIn * ag.pricing.input + totalOut * ag.pricing.output) / 1_000_000;
                return <div style={{ flex: 1 }}><Meter label="cost" value={`$${cost < 0.01 ? cost.toFixed(4) : cost.toFixed(2)}`} accent/></div>;
              })()}
              <div style={{ flex: 1 }}/>
              {audit.traceUrl && (
                <a href={audit.traceUrl} target="_blank" rel="noopener noreferrer"
                   style={{
                     display: "inline-flex", alignItems: "center", gap: 6,
                     padding: "5px 11px", borderRadius: 999,
                     border: "1px solid var(--forge-cyan-deep)",
                     color: "var(--forge-cyan)",
                     font: "700 10px/1 var(--forge-font)",
                     letterSpacing: "0.10em", textTransform: "uppercase",
                     textDecoration: "none", whiteSpace: "nowrap",
                   }}>
                  <Icon name="arrowUR" size={10} color="var(--forge-cyan)"/>
                  Trace
                </a>
              )}
            </div>

            <StreamPane status={audit.status} maxHeight={520} padding="16px 20px">
              {audit.toolCalls.map((tc, i) => (
                <ToolCard key={i} done={Boolean(tc.result)} name={tc.name} arg={summarizeArgs(tc.args)} result={tc.result ? truncate(tc.result, 240) : null} />
              ))}

              {responseText && (
                <div style={{
                  marginTop: 14, padding: "14px 16px", borderRadius: 12,
                  background: audit.status === "done" ? "rgba(212,250,80,0.05)" : "rgba(255,255,255,0.03)",
                  border: audit.status === "done"
                    ? "1px solid rgba(212,250,80,0.18)"
                    : "1px solid var(--forge-border-dark)",
                }}>
                  <Markdown text={responseText} />
                </div>
              )}

              {audit.error && (
                <div style={{ marginTop: 14, color: "var(--forge-red)", font: "500 12px/18px var(--forge-mono)" }}>
                  {audit.error}
                </div>
              )}
            </StreamPane>
          </div>
        )}
      </Slab>

      {/* ─── FINDINGS TABLE — Jira-sourced ─── */}
      <div style={{ paddingTop: 16 }}>
        <SectionTitle kicker={
          findingsLoading
            ? <span style={{ display: "inline-flex", alignItems: "center", gap: 8 }}>
                <Spinner size={9} color="var(--forge-ink)"/>
                Loading findings from Jira…
              </span>
            : findingsResp.jira_configured
              ? `Jira · ${findings.length} ticket${findings.length === 1 ? "" : "s"} with label "sentinel"`
              : "Jira not configured — set JIRA_BASE_URL / JIRA_EMAIL / JIRA_API_TOKEN"
        }
        action={
          findingsResp.register_url && (
            <Btn
              variant="ink"
              size="m"
              onClick={() => window.open(findingsResp.register_url, "_blank", "noopener,noreferrer")}
              iconRight={<Icon name="arrowUR" size={13} color="#fff" />}>
              Open full register
            </Btn>
          )
        }>
          Findings register
        </SectionTitle>

        <PaperCard>
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr style={{ background: "rgba(7,26,48,0.03)" }}>
                <Th>SOP</Th>
                <Th>Business unit</Th>
                <Th>Regulation</Th>
                <Th>Level</Th>
                <Th>Evidence</Th>
                <Th align="right">Severity</Th>
              </tr>
            </thead>
            <tbody>
              {findings.length === 0 && (
                <tr><Td muted style={{ textAlign: "center", padding: "32px 18px" }} colSpan={6}>
                  {findingsLoading
                    ? <span style={{ display: "inline-flex", alignItems: "center", gap: 8 }}>
                        <Spinner size={9} color="var(--forge-on-light-mute)"/>
                        Loading findings from Jira…
                      </span>
                    : findingsResp.jira_configured
                      ? "No tickets yet. Run an audit and the agent will file gaps as Jira tickets."
                      : "Configure Jira to populate this table."}
                </Td></tr>
              )}
              {findings.map((f, i) => <FindingRow key={f.key || i} f={f}/>)}
            </tbody>
          </table>
        </PaperCard>
      </div>
    </div>);

};

const FindingRow = ({ f }) => {
  const [hover, setHover] = React.useState(false);
  const clickable = Boolean(f.url);
  const open = (e) => {
    if (!clickable) return;
    // Cmd/Ctrl/middle-click → new tab; plain click → also new tab to keep the demo running.
    window.open(f.url, "_blank", "noopener,noreferrer");
  };
  return (
    <tr
      onClick={open}
      onMouseEnter={() => setHover(true)}
      onMouseLeave={() => setHover(false)}
      title={clickable ? `Open ${f.key} in Jira` : ""}
      style={{
        borderTop: "1px solid rgba(7,26,48,0.08)",
        background: hover && clickable ? "rgba(212,250,80,0.10)" : "transparent",
        cursor: clickable ? "pointer" : "default",
        transition: "background 90ms ease",
      }}>
      <Td>
        <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
          <span style={{ font: "600 12.5px/1.3 var(--forge-mono)", color: "var(--forge-on-light)" }}>{f.sop || "—"}</span>
          {clickable && (
            <span style={{
              font: "600 9px/1 var(--forge-mono)",
              color: hover ? "var(--forge-on-light)" : "var(--forge-on-light-mute)",
              padding: "2px 6px", borderRadius: 4,
              border: "1px solid rgba(7,26,48,0.15)",
              background: "rgba(7,26,48,0.04)",
              letterSpacing: "0.04em",
            }}>{f.key}</span>
          )}
          <span style={{ opacity: clickable ? (hover ? 1 : 0.35) : 0, transition: "opacity 90ms" }}>
            <Icon name="arrowUR" size={11} color="var(--forge-on-light-mute)" />
          </span>
        </div>
        <div style={{ font: "400 11.5px/15px var(--forge-font)", color: "var(--forge-on-light-mute)", marginTop: 2 }}>{f.title}</div>
      </Td>
      <Td muted>{f.unit || "—"}</Td>
      <Td><span style={{ font: "500 12px/16px var(--forge-mono)", color: "var(--forge-on-light)" }}>{f.reg}</span></Td>
      <Td><LevelChip level={f.level} /></Td>
      <Td muted style={{ maxWidth: 360 }}>{f.evidence}</Td>
      <Td align="right">
        {f.severity === "high" && <SeverityChip tone="danger">High</SeverityChip>}
        {f.severity === "med"  && <SeverityChip tone="partial">Medium</SeverityChip>}
        {f.severity === "low"  && <SeverityChip tone="partial">Low</SeverityChip>}
      </Td>
    </tr>
  );
};

const summarizeArgs = (args) => {
  if (!args || typeof args !== "object") return "";
  const entries = Object.entries(args);
  if (entries.length === 0) return "{}";
  return entries.map(([k, v]) => `${k}: ${truncate(JSON.stringify(v), 60)}`).join(", ");
};
const truncate = (s, n) => (s.length > n ? s.slice(0, n) + "…" : s);

// ──── helpers ────

const TemplateChip = ({ children, selected, disabled, onClick }) =>
<button onClick={disabled ? undefined : onClick} style={{
  display: "inline-flex", alignItems: "center", gap: 6,
  padding: "6px 12px", borderRadius: 999,
  background: selected ? "var(--forge-lime)" : "transparent",
  color: disabled ? "var(--forge-on-dark-faint)" : selected ? "var(--forge-ink)" : "var(--forge-cyan)",
  border: `1px solid ${disabled ? "rgba(255,255,255,0.10)" : selected ? "var(--forge-lime)" : "var(--forge-cyan-deep)"}`,
  font: "600 11px/1 var(--forge-font)",
  letterSpacing: "0.06em",
  cursor: disabled ? "not-allowed" : "pointer", whiteSpace: "nowrap",
  opacity: disabled ? 0.5 : 1,
}}>{children}</button>;


const ToolCard = ({ done, name, arg, duration, result }) =>
<Panel padding={18} style={{ marginTop: 14 }}>
    <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
      {done ?
    <Icon name="check" size={14} color="var(--forge-mint-warm)" stroke={2.5} /> :
    <Spinner size={12} />}
      <span style={{ font: "700 13px/1 var(--forge-mono)", color: "var(--forge-on-dark-strong)" }}>{name}</span>
      <span style={{ font: "400 12px/1 var(--forge-mono)", color: "var(--forge-on-dark-mute)" }}>{arg}</span>
      <div style={{ flex: 1 }} />
      <span style={{ font: "500 11px/1 var(--forge-mono)", color: "var(--forge-on-dark-faint)" }}>{duration}</span>
    </div>
    {result &&
  <div style={{ marginTop: 10, paddingLeft: 24, font: "400 12px/18px var(--forge-mono)", color: "var(--forge-on-dark-mute)" }}>
        → {result}
      </div>
  }
  </Panel>;


const Th = ({ children, align }) =>
<th style={{
  font: "600 11px/1 var(--forge-font)", letterSpacing: "0.12em", textTransform: "uppercase",
  color: "var(--forge-on-light-mute)", padding: "14px 18px",
  textAlign: align || "left", whiteSpace: "nowrap"
}}>{children}</th>;

const Td = ({ children, muted, align, style }) =>
<td style={{
  padding: "14px 18px",
  font: "400 13px/19px var(--forge-font)",
  color: muted ? "var(--forge-on-light-mute)" : "var(--forge-on-light)",
  textAlign: align || "left",
  verticalAlign: "top", ...style
}}>{children}</td>;


const LevelChip = ({ level }) => {
  const styles = {
    compliant: { color: "rgb(0,100,40)", bg: "var(--forge-mint-bg)", border: "rgba(0,140,70,0.30)", label: "Compliant" },
    partial: { color: "rgb(132,85,0)", bg: "var(--forge-amber-bg)", border: "rgba(180,130,0,0.30)", label: "Partial" },
    gap: { color: "rgb(160,0,40)", bg: "var(--forge-rose-bg)", border: "rgba(207,0,43,0.30)", label: "Gap" }
  }[level];
  return (
    <span style={{
      display: "inline-flex", alignItems: "center", gap: 6,
      padding: "4px 10px", borderRadius: 999,
      background: styles.bg, color: styles.color,
      border: `1px solid ${styles.border}`,
      font: "600 11px/16px var(--forge-font)", letterSpacing: "0.04em",
      whiteSpace: "nowrap"
    }}>
      <span style={{ width: 6, height: 6, borderRadius: 2, background: styles.color, opacity: 0.85 }} />
      {styles.label}
    </span>);

};

const SeverityChip = ({ tone, children }) => {
  const styles = {
    danger: { color: "rgb(160,0,40)", border: "rgba(207,0,43,0.40)" },
    partial: { color: "rgb(132,85,0)", border: "rgba(180,130,0,0.40)" }
  }[tone];
  return (
    <span style={{
      display: "inline-flex", padding: "3px 10px", borderRadius: 999,
      border: `1px solid ${styles.border}`, color: styles.color,
      font: "700 10px/16px var(--forge-font)", letterSpacing: "0.10em",
      textTransform: "uppercase", whiteSpace: "nowrap"
    }}>{children}</span>);

};

Object.assign(window, { AuditScreen });
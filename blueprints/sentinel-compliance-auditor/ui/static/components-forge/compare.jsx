// Forge-styled Compare screen — 3-way race on a single random question.

const AGENT_PRICING = {
  "deepseek-ai/DeepSeek-V4-Pro":       { input: 1.75, output: 3.50 },
  "gpt-5.5":                            { input: 5.00, output: 30.00 },
  "nvidia/Nemotron-3-Ultra-550b-a55b":  { input: 1.00, output: 3.00 },
};
const AGENT_CONFIG = {
  naive:    { label: "Naive RAG",         sublabel: "DeepSeek-V4-Pro",                                    tagline: "1 retrieval + 1 LLM call · no tools",        model: "deepseek-ai/DeepSeek-V4-Pro" },
  openai:   { label: "Grounded agent",    sublabel: "GPT-5.5 + Tavily",                                  tagline: "ReAct · Pinecone + web · sub-agent fan-out", model: "gpt-5.5" },
  nemotron: { label: "Production agent",  sublabel: "Nemotron-Ultra + Tavily + LangSmith + Snowglobe",   tagline: "ReAct · Pinecone + web · sub-agent fan-out", model: "nvidia/Nemotron-3-Ultra-550b-a55b" },
};

const blankAgentState = (key) => ({
  ...AGENT_CONFIG[key], key,
  status: "pending",  // pending | running | done | error
  startedAt: null, endedAt: null,
  tokens: { in: 0, out: 0 },
  toolCalls: [],
  answer: "",
  error: null,
  traceUrl: null,
});

const pickQuestion = (dataset) => {
  if (!dataset || dataset.length === 0) return null;
  return dataset[Math.floor(Math.random() * dataset.length)];
};

const CompareScreen = () => {
  const dataset = (window.SENTINEL_DATA && window.SENTINEL_DATA.dataset) || [];
  const fallbackQ = (window.SENTINEL_DATA && window.SENTINEL_DATA.raceQuestion) || null;

  const [question, setQuestion] = React.useState(null);
  const [agents, setAgents] = React.useState(() => ({
    naive:  blankAgentState("naive"),
    nemotron: blankAgentState("nemotron"),
    openai: blankAgentState("openai"),
  }));
  // Increment to start a new race. Race is *not* auto-triggered on question
  // selection — user must click Start.
  const [runToken, setRunToken] = React.useState(0);
  const ctrlRef = React.useRef(null);

  // Pick a question once the dataset is loaded; re-pick if the dataset arrives
  // after we already fell back to the static raceQuestion.
  const usedFallback = React.useRef(false);
  React.useEffect(() => {
    if (dataset.length > 0) {
      if (!question || usedFallback.current) {
        usedFallback.current = false;
        setQuestion(pickQuestion(dataset));
      }
    } else if (!question && fallbackQ) {
      usedFallback.current = true;
      setQuestion(fallbackQ);
    }
  }, [dataset.length]);

  // Run the race only when the user presses Start (runToken increment).
  React.useEffect(() => {
    if (runToken === 0 || !question) return;
    if (ctrlRef.current) ctrlRef.current.abort();
    const ctrl = new AbortController();
    ctrlRef.current = ctrl;

    const now = Date.now();
    setAgents({
      naive:  { ...blankAgentState("naive"),  status: "running", startedAt: now },
      nemotron: { ...blankAgentState("nemotron"), status: "running", startedAt: now },
      openai: { ...blankAgentState("openai"), status: "running", startedAt: now },
    });

    const qText = question.question || question.text || "";
    const message = question.sop_id
      ? `For ${question.sop_id}: ${qText}`
      : qText;
    window.ForgeAPI.streamRace(message, question.id, {
      signal: ctrl.signal,
      onEvent: (ev) => {
        const key = ev.agent;
        if (!key || !AGENT_CONFIG[key]) return;
        setAgents(prev => {
          const a = prev[key];
          if (!a) return prev;
          if (ev.type === "run_started") {
            return { ...prev, [key]: { ...a, traceUrl: ev.trace_url } };
          }
          if (ev.type === "token") {
            return { ...prev, [key]: { ...a, answer: a.answer + ev.text } };
          }
          if (ev.type === "tool_call") {
            return { ...prev, [key]: { ...a, toolCalls: [...a.toolCalls, { name: ev.name, args: ev.args, t: Date.now() }] } };
          }
          if (ev.type === "tool_result") {
            const tc = [...a.toolCalls];
            for (let i = tc.length - 1; i >= 0; i--) {
              if (!tc[i].result) { tc[i] = { ...tc[i], result: ev.text }; break; }
            }
            return { ...prev, [key]: { ...a, toolCalls: tc } };
          }
          if (ev.type === "usage") {
            return { ...prev, [key]: { ...a, tokens: { in: ev.input_tokens, out: ev.output_tokens } } };
          }
          if (ev.type === "done") {
            return { ...prev, [key]: { ...a, status: a.status === "error" ? "error" : "done", endedAt: Date.now() } };
          }
          if (ev.type === "error") {
            return { ...prev, [key]: { ...a, status: "error", error: ev.error, endedAt: Date.now() } };
          }
          return prev;
        });
      },
      onError: (err) => {
        console.warn("[forge] race stream error:", err);
        setAgents(prev => Object.fromEntries(
          Object.entries(prev).map(([k, a]) => [k, a.status === "running"
            ? { ...a, status: "error", error: String(err), endedAt: Date.now() }
            : a]),
        ));
      },
    });

    return () => ctrl.abort();
  }, [runToken]);

  const anyRunning = ["naive", "openai", "nemotron"].some(k => agents[k].status === "running");

  // Force a re-render every 200ms while any agent is running so the elapsed
  // counters keep ticking even when no SSE event has arrived in a while
  // (e.g. during a slow tool call or LLM warm-up).
  const [, setTick] = React.useState(0);
  React.useEffect(() => {
    if (!anyRunning) return;
    const id = setInterval(() => setTick(t => t + 1), 200);
    return () => clearInterval(id);
  }, [anyRunning]);
  const handleDrawNext = () => {
    if (ctrlRef.current) ctrlRef.current.abort();
    const q2 = pickQuestion(dataset);
    if (!q2) return;
    setQuestion(q2);
    setAgents({
      naive:  blankAgentState("naive"),
      nemotron: blankAgentState("nemotron"),
      openai: blankAgentState("openai"),
    });
  };
  const handleStart = () => {
    if (!question || anyRunning) return;
    setRunToken(t => t + 1);
  };

  // Build the agent objects in the shape AgentSlab expects.
  const expectedLevel = question?.expected_compliance_level || null;
  const renderAgents = ["naive", "openai", "nemotron"].map(key => {
    const a = agents[key];
    const elapsed = a.startedAt ? ((a.endedAt || Date.now()) - a.startedAt) / 1000 : 0;
    const px = AGENT_PRICING[a.model] || { input: 0, output: 0 };
    const cost = (a.tokens.in * px.input + a.tokens.out * px.output) / 1e6;
    // Only compute a verdict when the question carries a ground-truth label.
    // Otherwise the level claim is just noise (e.g. for factual_single_hop
    // questions where compliance doesn't apply).
    const verdictLevel = (a.status === "done" && expectedLevel) ? extractCompliance(a.answer) : null;
    const verdict = verdictLevel ? { level: verdictLevel, note: noteForVerdict(a, verdictLevel) } : null;
    const gtMatch = (a.status === "done" && expectedLevel && verdictLevel)
      ? sameClass(verdictLevel, expectedLevel)
      : null;
    return {
      key, label: a.label, sublabel: a.sublabel, tagline: a.tagline,
      status: a.status,                              // pending | running | done | error
      elapsed,
      tokens: a.tokens, cost,
      stream: [
        ...a.toolCalls.map(tc => ({ kind: "tool", name: tc.name, arg: shortArgs(tc.args), result: tc.result ? truncateC(tc.result, 220) : undefined, status: tc.result ? undefined : "running" })),
        ...(a.answer ? [{ kind: "answer", text: a.answer }] : []),
      ],
      verdict,
      gtMatch,
      hasGT: Boolean(expectedLevel),
      error: a.error,
      traceUrl: a.traceUrl,
    };
  });

  const gtLabel = question?.expected_compliance_level === "compliant" ? "Compliant" : "Non-compliant";

  return (
    <div style={{ padding: "28px 32px", display: "flex", flexDirection: "column", gap: 28 }}>

      {/* ─── HERO SLAB ─── */}
      <Slab padding={36}>
        <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 22 }}>
          <span className="f-kicker">Compare</span>
          <OutlinePill size="s">Single question · 3 agents in parallel</OutlinePill>
          <div style={{ flex: 1 }}/>
          <Btn
            variant="ghostDark"
            size="m"
            onClick={handleDrawNext}
            disabled={dataset.length === 0 || anyRunning}
            icon={<Icon name="arrow" size={13}/>}>
            Draw next question
          </Btn>
          <Btn
            variant="lime"
            size="m"
            onClick={handleStart}
            disabled={!question || anyRunning}
            icon={<Icon name="play" size={13} color="var(--forge-ink)" stroke={2.5}/>}>
            {anyRunning ? "Running…" : (runToken > 0 ? "Run again" : "Start")}
          </Btn>
        </div>

        {question ? (
          <div style={{ display: "grid", gridTemplateColumns: "1.5fr 1fr", gap: 40 }}>
            <div>
              <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 18, flexWrap: "wrap" }}>
                <span style={{ font: "600 12px/1 var(--forge-mono)", color: "var(--forge-lime)", padding: "5px 10px", border: "1px solid rgba(212,250,80,0.45)", borderRadius: 999, letterSpacing: "0.08em", whiteSpace: "nowrap" }}>
                  {(question.id || "").toUpperCase()}
                </span>
                <OutlinePill size="s">{(question.category || "").replace(/_/g, " ")}</OutlinePill>
                <OutlinePill size="s" tone="muteDark">{question.difficulty || "?"}</OutlinePill>
                <span style={{ font: "500 12px/1 var(--forge-mono)", color: "var(--forge-on-dark-faint)" }}>
                  random draw · {dataset.length || 0} questions in pool
                </span>
              </div>
              <h1 style={{
                margin: 0, font: "700 34px/1.15 var(--forge-font)",
                letterSpacing: "-0.02em", color: "var(--forge-on-dark-strong)",
              }}>{question.question || question.text}</h1>
            </div>

            <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
              {question.sop_id && (
                <MetaPanel kicker="Target SOP" value={question.sop_id} />
              )}
              {(question.regulations_involved || question.regulations) && (
                <MetaPanel kicker="Regulations" value={(question.regulations_involved || question.regulations || []).join(" · ")}/>
              )}
              {question.expected_compliance_level && (
                <MetaPanel
                  kicker="Ground truth"
                  value={gtLabel}
                  sub={`Expected: ${question.expected_compliance_level}`}
                  valueColor={question.expected_compliance_level === "compliant" ? "var(--forge-mint-warm)" : "var(--forge-amber)"}/>
              )}
              {question.edition && (
                <MetaPanel kicker="Edition" value={question.edition}/>
              )}
            </div>
          </div>
        ) : (
          <div style={{ font: "500 14px/22px var(--forge-font)", color: "var(--forge-on-dark-mute)" }}>
            Loading dataset…
          </div>
        )}
      </Slab>

      {/* ─── 3-WAY RACE ─── */}
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 20 }}>
        {renderAgents.map(a => <AgentSlab key={a.key} agent={a}/>)}
      </div>

      {/* ─── RACE SUMMARY ─── */}
      <Slab padding={28}>
        <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 20 }}>
          <span className="f-kicker">Race summary</span>
          <OutlinePill size="s">Same retrieval index · 3 configs</OutlinePill>
        </div>

        <div style={{
          display: "grid",
          gridTemplateColumns: "1.4fr 1fr 1fr 1fr 1fr",
          rowGap: 14, columnGap: 18, alignItems: "center",
        }}>
          <SumHeader>Configuration</SumHeader>
          <SumHeader>Verdict</SumHeader>
          <SumHeader>Tokens</SumHeader>
          <SumHeader>Cost</SumHeader>
          <SumHeader>Latency</SumHeader>

          {renderAgents.map(a => (
            <React.Fragment key={a.key}>
              <div>
                <div style={{ font: "700 15px/20px var(--forge-font)", color: "var(--forge-on-dark-strong)" }}>{a.label}</div>
                <div style={{ font: "400 12px/16px var(--forge-font)", color: "var(--forge-on-dark-mute)" }}>{a.sublabel}</div>
              </div>
              <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                {a.status === "done"    && <StatusChip tone="warm">Done</StatusChip>}
                {a.status === "running" && <StatusChip tone="running">Streaming</StatusChip>}
                {a.status === "error"   && <StatusChip tone="danger">Error</StatusChip>}
                {a.status === "pending" && <StatusChip tone="cold">Not started</StatusChip>}
              </div>
              <SumNum>{((a.tokens.in + a.tokens.out) / 1000).toFixed(1)}k</SumNum>
              <SumNum accent>${a.cost.toFixed(4)}</SumNum>
              <SumNum>{a.elapsed.toFixed(1)}s</SumNum>
            </React.Fragment>
          ))}
        </div>
      </Slab>
    </div>
  );
};

// Heuristic compliance-level extraction from a freeform answer.
// Mirrors sentinel/eval/metrics.py extract_compliance_level — first explicit
// label wins; "compliant" only counts when not negated by "non-".
const extractCompliance = (text) => {
  if (!text) return null;
  const t = text.toLowerCase();
  // Look at the bolded verdict prefix first (the demo's models tend to emit
  // "**Partial.**" or "**Gap.**" as the first sentence).
  const head = t.slice(0, 240);
  if (/\bgap\b/.test(head))     return "gap";
  if (/\bpartial\b/.test(head)) return "partial";
  if (/\bnon[- ]compliant\b/.test(head)) return "gap";
  if (/(^|[^a-z-])compliant\b/.test(head)) return "compliant";
  // Fallback to whole text.
  if (/\bgap\b/.test(t))     return "gap";
  if (/\bpartial\b/.test(t)) return "partial";
  if (/\bnon[- ]compliant\b/.test(t)) return "gap";
  if (/(^|[^a-z-])compliant\b/.test(t)) return "compliant";
  return null;
};

const sameClass = (predicted, expected) => {
  if (!predicted || !expected) return null;
  // Binary collapse: compliant vs non_compliant (partial+gap).
  const binarize = (lvl) => (lvl === "compliant" ? "compliant" : "non_compliant");
  return binarize(predicted) === binarize(expected);
};

const noteForVerdict = (a, level) => {
  if (level === "gap")       return "Flagged a gap";
  if (level === "partial")   return "Flagged partial — controls missing or vague";
  if (level === "compliant") return "Cleared as compliant";
  return "";
};

const shortArgs = (args) => {
  if (!args || typeof args !== "object") return "";
  const entries = Object.entries(args);
  if (entries.length === 0) return "{}";
  return entries.map(([k, v]) => `${k}: ${truncateC(JSON.stringify(v), 60)}`).join(", ");
};
const truncateC = (s, n) => (s && s.length > n ? s.slice(0, n) + "…" : s || "");

// ─── AgentSlab — one column of the race ───
const AgentSlab = ({ agent: a }) => {
  return (
    <Slab padding={0} style={{ display: "flex", flexDirection: "column" }}>
      {/* Header */}
      <div style={{ padding: "22px 24px", borderBottom: "1px solid var(--forge-border-dark)" }}>
        <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 10 }}>
          <div style={{ font: "700 18px/1.1 var(--forge-font)", color: "var(--forge-on-dark-strong)", letterSpacing: "-0.01em" }}>
            {a.label}
          </div>
          {a.status === "done"    && <StatusChip tone="warm"><Icon name="check" size={9} color="var(--forge-mint-warm)" stroke={3}/> Done</StatusChip>}
          {a.status === "running" && <StatusChip tone="running"><Spinner size={8} color="var(--forge-lime)"/> Running</StatusChip>}
          {a.status === "error"   && <StatusChip tone="danger">Error</StatusChip>}
          {a.status === "pending" && <StatusChip tone="cold">Ready</StatusChip>}
        </div>
        <div style={{ font: "500 12px/16px var(--forge-font)", color: "var(--forge-on-dark-mute)", marginBottom: 4 }}>{a.sublabel}</div>
        <div style={{ font: "400 12px/16px var(--forge-mono)", color: "var(--forge-on-dark-faint)" }}>{a.tagline}</div>
      </div>

      {/* Meter row */}
      <div style={{
        display: "flex", alignItems: "center", gap: 12,
        padding: "16px 24px", borderBottom: "1px solid var(--forge-border-dark)",
        background: "rgba(255,255,255,0.02)",
      }}>
        <div style={{ flex: 1 }}><Meter label="elapsed" value={`${a.elapsed.toFixed(1)}s`} live={a.status === "running"}/></div>
        <div style={{ flex: 1 }}><Meter label="tokens"  value={`${((a.tokens.in + a.tokens.out) / 1000).toFixed(1)}k`}/></div>
        <div style={{ flex: 1 }}><Meter label="cost"    value={`$${a.cost.toFixed(4)}`} accent/></div>
        {a.traceUrl && a.key === "nemotron" && (
          <a href={a.traceUrl} target="_blank" rel="noopener noreferrer"
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

      {/* Stream — capped height + scroll so the slab doesn't grow as tokens arrive. */}
      <StreamPane status={a.status}>
        {a.stream.map((item, i) => {
          if (item.kind === "thought") {
            return (
              <div key={i} style={{ display: "flex", gap: 10 }}>
                <Icon name="shield" size={14} color="var(--forge-lime)"/>
                <div style={{ font: "400 13px/19px var(--forge-font)", fontStyle: "italic", color: "var(--forge-on-dark-mute)" }}>{item.text}</div>
              </div>
            );
          }
          if (item.kind === "tool") {
            const running = item.status === "running";
            return (
              <div key={i} style={{
                border: "1px solid var(--forge-border-dark)",
                borderRadius: 10, padding: "10px 12px",
                background: running ? "rgba(212,250,80,0.05)" : "rgba(255,255,255,0.02)",
              }}>
                <div style={{ display: "flex", alignItems: "center", gap: 8 }}>
                  {running ? <Spinner size={10}/> : <Icon name="check" size={12} color="var(--forge-mint-warm)" stroke={2.5}/>}
                  <span style={{ font: "700 12px/1 var(--forge-mono)", color: "var(--forge-on-dark-strong)" }}>{item.name}</span>
                  <div style={{ flex: 1 }}/>
                  {!running && <span style={{ font: "500 10px/1 var(--forge-mono)", color: "var(--forge-on-dark-faint)" }}>{item.ms}ms</span>}
                </div>
                <div style={{ marginTop: 6, paddingLeft: 20, font: "400 11px/16px var(--forge-mono)", color: "var(--forge-on-dark-mute)" }}>
                  arg: {item.arg}
                  {!running && <div style={{ marginTop: 4, color: "var(--forge-on-dark)" }}>→ {item.result}</div>}
                </div>
              </div>
            );
          }
          if (item.kind === "answer") {
            const isFinal = a.status === "done";
            return (
              <div key={i} style={{
                marginTop: 4, padding: "14px 16px", borderRadius: 12,
                background: isFinal ? "rgba(212,250,80,0.05)" : "rgba(255,255,255,0.03)",
                border: isFinal ? "1px solid rgba(212,250,80,0.18)" : "1px solid var(--forge-border-dark)",
              }}>
                <div className="f-kicker" style={{
                  color: isFinal ? "var(--forge-lime)" : "var(--forge-on-dark-mute)",
                  marginBottom: 8, display: "inline-flex", alignItems: "center", gap: 6,
                }}>
                  {!isFinal && <Spinner size={8} color="var(--forge-lime)"/>}
                  {isFinal ? "Final answer" : "Streaming response"}
                </div>
                <Markdown text={item.text} />
              </div>
            );
          }
          return null;
        })}
        {a.status === "running" && (
          <div style={{ display: "flex", alignItems: "center", gap: 8, padding: "8px 12px", borderRadius: 8, background: "rgba(212,250,80,0.06)" }}>
            <Spinner size={10}/>
            <span style={{ font: "500 11px/1 var(--forge-font)", color: "var(--forge-on-dark-mute)" }}>Synthesizing answer…</span>
            <span style={{ display: "inline-block", width: 7, height: 12, background: "var(--forge-lime)" }}/>
          </div>
        )}
      </StreamPane>

      {/* Verdict footer */}
      <div style={{ padding: "16px 24px", borderTop: "1px solid var(--forge-border-dark)" }}>
        {a.verdict ? (
          <>
            <div style={{ display: "flex", alignItems: "center", gap: 8, marginBottom: 8, flexWrap: "wrap" }}>
              <span className="f-kicker">Verdict</span>
              <LevelDarkChip level={a.verdict.level}/>
              {a.gtMatch === true  && <MatchChip ok/>}
              {a.gtMatch === false && <MatchChip ok={false}/>}
            </div>
            <div style={{ font: "400 12px/17px var(--forge-font)", color: "var(--forge-on-dark-mute)" }}>{a.verdict.note}</div>
          </>
        ) : a.status === "done" ? (
          a.hasGT ? (
            <div style={{ display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
              <span className="f-kicker">Verdict</span>
              <span style={{ font: "500 12px/16px var(--forge-font)", color: "var(--forge-on-dark-mute)" }}>
                No explicit level in the answer
              </span>
            </div>
          ) : (
            <div style={{ display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
              <span className="f-kicker">Done</span>
              <span style={{ font: "500 12px/16px var(--forge-mono)", color: "var(--forge-on-dark-mute)" }}>
                {a.elapsed.toFixed(1)}s · ${a.cost.toFixed(4)} · {((a.tokens.in + a.tokens.out) / 1000).toFixed(1)}k tokens
              </span>
            </div>
          )
        ) : a.status === "error" ? (
          <div style={{ display: "flex", alignItems: "center", gap: 8, flexWrap: "wrap" }}>
            <span className="f-kicker" style={{ color: "var(--forge-red)" }}>Error</span>
            <span style={{ font: "500 12px/16px var(--forge-font)", color: "var(--forge-on-dark-mute)" }}>
              {a.error || "stream failed"}
            </span>
          </div>
        ) : a.status === "running" ? (
          <div style={{ display: "flex", alignItems: "center", gap: 8, font: "500 12px/1 var(--forge-font)", color: "var(--forge-on-dark-faint)" }}>
            <Spinner size={9}/> Verdict pending…
          </div>
        ) : (
          <div style={{ font: "500 12px/1 var(--forge-font)", color: "var(--forge-on-dark-faint)" }}>
            Press Start to run the race.
          </div>
        )}
      </div>
    </Slab>
  );
};

// helpers

const MetaPanel = ({ kicker, value, sub, valueColor }) => (
  <div style={{
    padding: "16px 18px",
    border: "1px solid var(--forge-border-dark)",
    borderRadius: 14,
    background: "rgba(255,255,255,0.02)",
  }}>
    <div className="f-kicker" style={{ color: "var(--forge-on-dark-mute)", marginBottom: 6 }}>{kicker}</div>
    <div style={{ font: "700 18px/22px var(--forge-font)", color: valueColor || "var(--forge-on-dark-strong)", letterSpacing: "-0.005em" }}>
      {value}
    </div>
    {sub && <div style={{ font: "400 12px/16px var(--forge-font)", color: "var(--forge-on-dark-mute)", marginTop: 4 }}>{sub}</div>}
  </div>
);

const LevelDarkChip = ({ level }) => {
  const styles = {
    compliant: { color: "var(--forge-mint-warm)", bg: "rgba(120,220,140,0.10)", border: "rgba(120,220,140,0.40)", label: "Compliant" },
    partial:   { color: "var(--forge-amber)",     bg: "rgba(255,190,92,0.10)",  border: "rgba(255,190,92,0.45)",  label: "Partial" },
    gap:       { color: "var(--forge-red)",       bg: "rgba(247,100,110,0.10)", border: "rgba(247,100,110,0.45)", label: "Gap" },
  }[level];
  return (
    <span style={{
      display: "inline-flex", alignItems: "center", gap: 6,
      padding: "4px 11px", borderRadius: 999,
      background: styles.bg, color: styles.color,
      border: `1px solid ${styles.border}`,
      font: "700 11px/16px var(--forge-font)", letterSpacing: "0.04em",
      whiteSpace: "nowrap",
    }}>
      <span style={{ width: 6, height: 6, borderRadius: 2, background: styles.color }}/>
      {styles.label}
    </span>
  );
};

const MatchChip = ({ ok }) => (
  <span style={{
    display: "inline-flex", alignItems: "center", gap: 5,
    padding: "4px 10px", borderRadius: 999,
    border: ok ? "1px solid rgba(120,220,140,0.45)" : "1px solid rgba(247,100,110,0.45)",
    color: ok ? "var(--forge-mint-warm)" : "var(--forge-red)",
    font: "600 10px/1 var(--forge-font)", letterSpacing: "0.12em",
    textTransform: "uppercase", whiteSpace: "nowrap",
  }}>
    <Icon name={ok ? "check" : "x"} size={10} color={ok ? "var(--forge-mint-warm)" : "var(--forge-red)"} stroke={3}/>
    {ok ? "Matches GT" : "Misses GT"}
  </span>
);

const SumHeader = ({ children }) => (
  <div className="f-kicker" style={{ color: "var(--forge-on-dark-mute)", letterSpacing: "0.12em" }}>{children}</div>
);
const SumNum = ({ children, accent }) => (
  <div style={{
    font: "700 17px/1 var(--forge-mono)",
    color: accent ? "var(--forge-lime)" : "var(--forge-on-dark-strong)",
  }}>{children}</div>
);

Object.assign(window, { CompareScreen });

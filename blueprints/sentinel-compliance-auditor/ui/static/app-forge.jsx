// Forge app — single-page nav between Audit / Compare / Eval.
// Hydrates window.SENTINEL_DATA from the backend on mount.

const TWEAK_DEFAULTS = /*EDITMODE-BEGIN*/{
  "focus": "balanced"
}/*EDITMODE-END*/;

function useForgeData() {
  // version increments after each successful load → triggers re-render of screens
  // that read directly from window.SENTINEL_DATA.
  const [version, setVersion] = React.useState(0);
  const [status, setStatus] = React.useState({ kb: "loading", eval: "loading", dataset: "loading", findings: "loading" });

  React.useEffect(() => {
    let cancelled = false;
    const API = window.ForgeAPI;
    if (!API) return;

    // Fire all four endpoints in parallel. Each one updates its own slice of
    // window.SENTINEL_DATA + status the moment it returns, so a slow query
    // (e.g. cold Pinecone /api/kb-stats taking ~10s) no longer blocks the
    // others. The screen re-renders after each individual completion.
    const tasks = [
      ["kb",       API.getKbStats,     (d) => { window.SENTINEL_DATA.kbStats = d; }],
      ["eval",     API.getEvalResults, (d) => { window.SENTINEL_DATA.evalResults = mapEvalResults(d); }],
      ["dataset",  API.getDataset,     (d) => { window.SENTINEL_DATA.dataset = d.questions || []; }],
      ["findings", API.getFindings,    (d) => { window.SENTINEL_DATA.findings = d; }],
    ];
    tasks.forEach(([key, fetcher, assign]) => {
      fetcher()
        .then((data) => {
          if (cancelled) return;
          assign(data);
          setStatus(s => ({ ...s, [key]: "ok" }));
          setVersion(v => v + 1);
        })
        .catch((err) => {
          console.warn(`[forge] failed to load /api/${key}:`, err);
          if (!cancelled) setStatus(s => ({ ...s, [key]: "error" }));
        });
    });

    return () => { cancelled = true; };
  }, []);

  return { version, status };
}

const EVAL_AGENT_META = {
  prototype:  { label: "Prototype agent",   sublabel: "GPT-5.5 + Pinecone" },
  grounded:     { label: "Grounded agent",    sublabel: "GPT-5.5 + Pinecone + Tavily" },
  optimized:  { label: "Optimized agent",   sublabel: "DeepSeek-V4-Pro + Pinecone + Tavily" },
  nemotron:   { label: "Production agent",  sublabel: "Nemotron-Ultra + Tavily + LangSmith + Snowglobe" },
};

function mapEvalResults(api) {
  const mapMode = (m, key) => {
    if (!m) return null;
    const meta = EVAL_AGENT_META[key] || {};
    return {
      key,
      label: meta.label || key,
      sublabel: meta.sublabel || "",
      model: m.model,
      // Default every numeric field: one eval JSON missing a field must not
      // unmount the Eval screen on a .toFixed() of undefined.
      total: m.total ?? 0,
      totalCost: m.total_cost_usd ?? 0,
      answerCost: m.answer_cost_usd ?? m.total_cost_usd ?? 0,
      latencyAvg: m.latency_avg_s ?? 0,
      latencyTotal: m.latency_total_s ?? 0,
      inputTokens: m.input_tokens ?? 0,
      outputTokens: m.output_tokens ?? 0,
      binary: {
        accuracy: m.compliance_binary?.accuracy ?? 0,
        recallNonCompliant: m.compliance_binary?.recall_non_compliant ?? 0,
        precisionNonCompliant: m.compliance_binary?.precision_non_compliant ?? 0,
        f1NonCompliant: m.compliance_binary?.f1_non_compliant ?? 0,
        macroF1: m.compliance_binary?.macro_f1 ?? 0,
        tp: m.compliance_binary?.tp_non_compliant ?? 0,
        fp: m.compliance_binary?.fp_non_compliant ?? 0,
        tn: m.compliance_binary?.tn_compliant ?? 0,
        fn: m.compliance_binary?.fn_non_compliant ?? 0,
      },
      perCategory: Object.fromEntries(Object.entries(m.per_category || {}).map(([k, v]) => [k, {
        n: v.n,
        correctness: v.judge_correctness_avg,
        citations:   v.judge_citations_avg,
        binaryAcc:   v.binary_accuracy,
      }])),
    };
  };
  const agents = {};
  for (const key of Object.keys(EVAL_AGENT_META)) {
    const mapped = mapMode(api[key], key);
    if (mapped) agents[key] = mapped;
  }
  return agents;
}


function App() {
  const [scene, setScene] = React.useState("audit");
  const [t, setTweak] = useTweaks(TWEAK_DEFAULTS);
  const { version, status } = useForgeData();

  return (
    <div data-screen-label={
      scene === "audit"   ? "01 Audit" :
      scene === "compare" ? "02 Compare" :
                            "03 Evaluation"
    }>
      <SpinnerStyle/>
      <Topbar scene={scene} nav={setScene}/>
      <main style={{ maxWidth: 1480, margin: "0 auto" }}>
        {/* All three screens stay mounted so in-flight streams + composer state
            survive tab switches. Inactive screens are display:none, which keeps
            React state + SSE readers alive but skips layout. */}
        <div style={{ display: scene === "audit"   ? "block" : "none" }}><AuditScreen   dataVersion={version} loadStatus={status}/></div>
        <div style={{ display: scene === "compare" ? "block" : "none" }}><CompareScreen dataVersion={version} loadStatus={status}/></div>
        <div style={{ display: scene === "eval"    ? "block" : "none" }}><EvalScreen    dataVersion={version} loadStatus={status}/></div>
      </main>

      <TweaksPanel>
        <TweakSection label="Screen">
          <TweakRadio
            label="Active screen"
            value={scene}
            onChange={v => setScene(v)}
            options={[
              { value: "audit",   label: "Audit"   },
              { value: "compare", label: "Compare" },
              { value: "eval",    label: "Eval"    },
            ]}
          />
        </TweakSection>
        <TweakSection label="Demo focus">
          <TweakSelect
            label="Story"
            value={t.focus}
            onChange={v => setTweak("focus", v)}
            options={[
              { value: "balanced", label: "Balanced — all three equal" },
              { value: "recall",   label: "100% recall vs 12% miss" },
              { value: "cost",     label: "Nebius 3.4× cheaper" },
              { value: "category", label: "Where agents matter most" },
            ]}/>
        </TweakSection>
        <TweakSection label="Data status">
          <div style={{ font: "500 11px/16px var(--forge-font)", color: "rgba(255,255,255,0.7)" }}>
            kb: {status.kb} · eval: {status.eval} · dataset: {status.dataset} · findings: {status.findings}
          </div>
        </TweakSection>
      </TweaksPanel>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App/>);

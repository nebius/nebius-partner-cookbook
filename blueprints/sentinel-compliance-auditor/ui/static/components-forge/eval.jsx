// Forge-styled Eval screen — multi-agent benchmark dashboard

// ── CI rendering ─────────────────────────────────────────────────────────────
// Resolve the displayed value + interval for a binary metric: prefer MEASURED
// run-to-run stats (mean ± 95% CI over N repeated runs), else the per-question
// bootstrap CI, else the bare point estimate.
const metricView = (a, repeatKey, bootstrapKey, point) => {
  const rs = a.repeatStats?.metrics?.[repeatKey];
  if (rs && rs.ci95) return { value: rs.mean, ci: rs.ci95, method: `${a.repeatStats.repeats} runs` };
  const ci = a.ci?.[bootstrapKey];
  return { value: point, ci: ci || null, method: ci ? "bootstrap" : null };
};

const CiBracket = ({ ci, fmt }) => {
  if (!ci) return null;
  const f = fmt || (v => v.toFixed(2));
  return (
    <span style={{ font: "500 10px/1 var(--forge-mono)", color: "var(--forge-on-dark-faint)", marginLeft: 6 }}>
      [{f(ci[0])}–{f(ci[1])}]
    </span>
  );
};

// Bar with the CI range drawn as a lighter band behind the point value.
const CiBar = ({ value, ci, color }) => (
  <div style={{ position: "relative", height: 10, borderRadius: 999, background: "rgba(255,255,255,0.05)", overflow: "hidden" }}>
    {ci && (
      <div style={{
        position: "absolute", top: 0, height: "100%",
        left: (ci[0] * 100) + "%", width: (Math.max(ci[1] - ci[0], 0.005) * 100) + "%",
        background: "rgba(255,255,255,0.10)",
      }}/>
    )}
    <div style={{ position: "absolute", top: 0, height: "100%", width: (value * 100) + "%", background: color, borderRadius: 999 }}/>
  </div>
);

const CiFootnote = ({ agents }) => {
  const hasRepeats = agents.some(a => a.repeatStats);
  const hasBootstrap = agents.some(a => a.ci);
  if (!hasRepeats && !hasBootstrap) return null;
  const n = agents.find(a => a.repeatStats)?.repeatStats?.repeats;
  return (
    <div style={{ marginTop: 4, font: "400 10px/14px var(--forge-font)", color: "var(--forge-on-dark-faint)" }}>
      Brackets: 95% CI — {hasRepeats ? `measured across ${n} repeated runs where available, else ` : ""}
      bootstrap over scored questions (n≈{agents.find(a => a.ci)?.ci?.n ?? 35}).
      Overlapping intervals → ranking not significant.
    </div>
  );
};

const EvalScreen = () => {
  const r = (window.SENTINEL_DATA && window.SENTINEL_DATA.evalResults) || null;
  if (!r || Object.keys(r).length === 0) {
    return (
      <div style={{ padding: "60px 32px", textAlign: "center" }}>
        <span className="f-kicker-light">Loading evaluation results…</span>
      </div>
    );
  }
  const agents = Object.values(r);
  const bestCost = Math.min(...agents.map(a => a.totalCost));
  const bestRecall = Math.max(...agents.map(a => a.binary.recallNonCompliant));

  return (
    <div style={{ padding: "28px 32px", display: "flex", flexDirection: "column", gap: 28 }}>

      {/* ─── HERO SLAB ─── */}
      <Slab padding={36}>
        <div style={{ display: "grid", gridTemplateColumns: "1fr 1.05fr", gap: 40 }}>
          <div>
            <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 28 }}>
              <span className="f-kicker">120-question evaluation</span>
            </div>
            <h1 style={{ margin: 0, font: "700 60px/1.02 var(--forge-font)", letterSpacing: "-0.025em", color: "var(--forge-on-dark-strong)" }}>
              Agent<br/>Comparison
            </h1>
            <p style={{
              margin: "22px 0 0", font: "400 16px/24px var(--forge-font)",
              color: "var(--forge-on-dark-mute)", maxWidth: 480,
            }}>
              Same dataset, same prompts, same Pinecone index. {agents.length} agent configurations
              compared across compliance accuracy, cost, and latency.
            </p>
          </div>

          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 14 }}>
            <StatCard
              kicker="Questions"
              value={agents[0].total}
              body="Curated test set: 6 categories spanning factual retrieval, synthesis, edition-aware, web-grounded and gap detection."
            />
            <StatCard
              kicker="Agents compared"
              value={agents.length}
              body={agents.map(a => a.label).join(", ")}
            />
            {(() => {
              const views = agents.map(a => metricView(a, "binary_recall_non_compliant", "recall_non_compliant", a.binary.recallNonCompliant));
              const best = views.reduce((acc, mv) => (mv.value > acc.value ? mv : acc), views[0]);
              return (
                <StatCard
                  kicker="Best recall"
                  value={best.value.toFixed(2)}
                  valueColor="var(--forge-lime)"
                  body={best.ci
                    ? `Non-compliant recall — catching every real compliance issue. 95% CI [${best.ci[0].toFixed(2)}–${best.ci[1].toFixed(2)}]${best.method === "bootstrap" ? "" : ` over ${best.method}`}.`
                    : "Non-compliant recall — catching every real compliance issue."}
                />
              );
            })()}
            <StatCard
              kicker="Lowest cost"
              value={`$${bestCost.toFixed(2)}`}
              valueColor="var(--forge-lime)"
              body={(() => {
                const cheapest = agents.reduce((acc, a) => (a.totalCost < acc.totalCost ? a : acc), agents[0]);
                const ci = cheapest?.repeatStats?.metrics?.total_cost_usd?.ci95;
                return ci
                  ? `Total spend for the full 120-question run. 95% CI [$${ci[0].toFixed(2)}–$${ci[1].toFixed(2)}] over ${cheapest.repeatStats.repeats} runs.`
                  : "Total spend for the full 120-question run.";
              })()}
            />
          </div>
        </div>
      </Slab>

      {/* ─── RECALL + PRECISION + COST BARS ─── */}
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: 20 }}>
        <Slab padding={28}>
          <div className="f-kicker" style={{ color: "var(--forge-mint-warm)", marginBottom: 14 }}>Audit safety</div>
          <div style={{ font: "700 22px/1.25 var(--forge-font)", letterSpacing: "-0.01em", color: "var(--forge-on-dark-strong)", marginBottom: 20 }}>
            Non-compliant recall
          </div>
          {(() => {
            const views = agents.map(a => ({ a, mv: metricView(a, "binary_recall_non_compliant", "recall_non_compliant", a.binary.recallNonCompliant) }));
            const best = Math.max(...views.map(x => x.mv.value));
            return views.map(({ a, mv }) => {
              const isBest = mv.value >= best;
              return (
                <div key={a.key} style={{ marginBottom: 14 }}>
                  <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", marginBottom: 6 }}>
                    <span style={{ font: "500 12px/1 var(--forge-font)", color: "var(--forge-on-dark-mute)" }}>{a.label}</span>
                    <span>
                      <span style={{ font: "700 12px/1 var(--forge-mono)", color: isBest ? "var(--forge-mint-warm)" : "var(--forge-on-dark)" }}>{mv.value.toFixed(2)}</span>
                      <CiBracket ci={mv.ci}/>
                    </span>
                  </div>
                  <CiBar value={mv.value} ci={mv.ci} color={isBest ? "var(--forge-mint-warm)" : "rgba(255,255,255,0.20)"}/>
                </div>
              );
            });
          })()}
          <CiFootnote agents={agents}/>
        </Slab>

        {(() => {
          const bestPrec = Math.max(...agents.map(a => a.binary.precisionNonCompliant));
          return (
            <Slab padding={28}>
              <div className="f-kicker" style={{ color: "var(--forge-amber)", marginBottom: 14 }}>False alarm rate</div>
              <div style={{ font: "700 22px/1.25 var(--forge-font)", letterSpacing: "-0.01em", color: "var(--forge-on-dark-strong)", marginBottom: 20 }}>
                Non-compliant precision
              </div>
              {(() => {
                const views = agents.map(a => ({ a, mv: metricView(a, "binary_precision_non_compliant", "precision_non_compliant", a.binary.precisionNonCompliant) }));
                const best = Math.max(...views.map(x => x.mv.value));
                return views.map(({ a, mv }) => {
                  const isBest = mv.value >= best;
                  return (
                    <div key={a.key} style={{ marginBottom: 14 }}>
                      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", marginBottom: 6 }}>
                        <span style={{ font: "500 12px/1 var(--forge-font)", color: "var(--forge-on-dark-mute)" }}>{a.label}</span>
                        <span>
                          <span style={{ font: "700 12px/1 var(--forge-mono)", color: isBest ? "var(--forge-amber)" : "var(--forge-on-dark)" }}>{mv.value.toFixed(2)}</span>
                          <CiBracket ci={mv.ci}/>
                        </span>
                      </div>
                      <CiBar value={mv.value} ci={mv.ci} color={isBest ? "var(--forge-amber)" : "rgba(255,255,255,0.20)"}/>
                    </div>
                  );
                });
              })()}
              <CiFootnote agents={agents}/>
            </Slab>
          );
        })()}

        <Slab padding={28}>
          <div className="f-kicker" style={{ color: "var(--forge-lime)", marginBottom: 14 }}>Cost · quality</div>
          <div style={{ font: "700 22px/1.25 var(--forge-font)", letterSpacing: "-0.01em", color: "var(--forge-on-dark-strong)", marginBottom: 20 }}>
            Total cost per 120-question run
          </div>
          {(() => {
            const dollars = v => "$" + v.toFixed(2);
            const views = agents.map(a => ({ a, mv: metricView(a, "total_cost_usd", null, a.totalCost) }));
            const cheapestCost = Math.min(...views.map(x => x.mv.value));
            const maxCost = Math.max(...views.map(x => x.mv.ci ? x.mv.ci[1] : x.mv.value));
            return views.map(({ a, mv }) => {
              const cheapest = mv.value <= cheapestCost;
              // CiBar works in a 0..1 domain — scale dollars by the axis max.
              const scaledCi = mv.ci ? [mv.ci[0] / maxCost, mv.ci[1] / maxCost] : null;
              return (
                <div key={a.key} style={{ marginBottom: 14 }}>
                  <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", marginBottom: 6 }}>
                    <span style={{ font: "500 12px/1 var(--forge-font)", color: "var(--forge-on-dark-mute)" }}>{a.label}</span>
                    <span>
                      <span style={{ font: "700 12px/1 var(--forge-mono)", color: cheapest ? "var(--forge-lime)" : "var(--forge-on-dark)" }}>{dollars(mv.value)}</span>
                      <CiBracket ci={mv.ci} fmt={dollars}/>
                    </span>
                  </div>
                  <CiBar value={mv.value / maxCost} ci={scaledCi} color={cheapest ? "var(--forge-lime)" : "rgba(255,255,255,0.25)"}/>
                </div>
              );
            });
          })()}
          <CiFootnote agents={agents}/>
        </Slab>
      </div>

      {/* ─── CONFUSION MATRICES ─── */}
      <div>
        <SectionTitle
          kicker="SOP compliance · binary classification"
          action={<OutlinePill tone="muteLight">{agents[0].binary.tp + agents[0].binary.fn + agents[0].binary.fp + agents[0].binary.tn} SOPs scored</OutlinePill>}>
          Did the agent catch the gap?
        </SectionTitle>
        <div style={{ display: "grid", gridTemplateColumns: `repeat(${Math.min(agents.length, 4)}, 1fr)`, gap: 16 }}>
          {agents.map(a => <ConfusionSlab key={a.key} mode={a}/>)}
        </div>
      </div>

      {/* ─── COST / LATENCY TABLE ─── */}
      <div>
        <SectionTitle kicker="Per 120-question run · includes grader calls">
          Cost · latency · tokens
        </SectionTitle>
        <PaperCard>
          <table style={{ width: "100%", borderCollapse: "collapse" }}>
            <thead>
              <tr>
                <Th>Configuration</Th>
                <Th>Model</Th>
                <Th align="right">Cost</Th>
                <Th align="right">Tokens in</Th>
                <Th align="right">Tokens out</Th>
                <Th align="right">Avg latency</Th>
              </tr>
            </thead>
            <tbody>
              {agents.map(a => {
                const cheapest = a.totalCost <= bestCost;
                return (
                  <tr key={a.key} style={{ borderTop: "1px solid rgba(7,26,48,0.08)" }}>
                    <Td>
                      <div style={{ font: "600 14px/19px var(--forge-font)", color: "var(--forge-on-light)" }}>{a.label}</div>
                      <div style={{ font: "400 11.5px/14px var(--forge-font)", color: "var(--forge-on-light-mute)" }}>{a.sublabel}</div>
                    </Td>
                    <Td muted style={{ font: "500 12px/16px var(--forge-mono)" }}>{a.model}</Td>
                    <Td align="right">
                      <span style={{ font: "700 16px/1 var(--forge-mono)", color: cheapest ? "rgb(60,140,40)" : "var(--forge-on-light)" }}>${a.totalCost.toFixed(2)}</span>
                    </Td>
                    <Td align="right">
                      <span style={{ font: "600 14px/1 var(--forge-mono)" }}>{(a.inputTokens / 1e6).toFixed(2)}M</span>
                    </Td>
                    <Td align="right">
                      <span style={{ font: "600 14px/1 var(--forge-mono)" }}>{(a.outputTokens / 1e6).toFixed(2)}M</span>
                    </Td>
                    <Td align="right">
                      <span style={{ font: "600 14px/1 var(--forge-mono)" }}>{a.latencyAvg.toFixed(1)}s</span>
                    </Td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </PaperCard>
      </div>

      {/* ─── PER-CATEGORY TABLE ─── */}
      <div style={{ paddingTop: 12 }}>
        <SectionTitle
          kicker="LLM-as-judge correctness · 0–2 · shared grader"
          action={<OutlinePill tone="muteLight">Freeform categories</OutlinePill>}>
          Where the gap shows up
        </SectionTitle>
        <PaperCard>
          <CategoryTable agents={agents}/>
        </PaperCard>
      </div>
    </div>
  );
};

// ─── Category table ───
const CategoryTable = ({ agents }) => {
  const cats = [
    { key: "factual_single_hop", label: "Factual · single hop", expl: "Direct retrieval of one clause" },
    { key: "multi_regulation",   label: "Multi-regulation",     expl: "Synthesis across 2+ frameworks" },
    { key: "edition_aware",      label: "Edition-aware",        expl: "Distinguishing historical versions" },
    { key: "negation_gap",       label: "Negation · gap",       expl: "Identifying what's missing" },
    { key: "web_grounded",       label: "Web-grounded",         expl: "Needs live web grounding" },
  ];
  return (
    <table style={{ width: "100%", borderCollapse: "collapse" }}>
      <thead>
        <tr>
          <Th>Category</Th>
          <Th align="center">n</Th>
          {agents.map(a => <Th key={a.key} align="center">{a.label}</Th>)}
        </tr>
      </thead>
      <tbody>
        {cats.map(c => {
          const scores = agents.map(a => a.perCategory[c.key]?.correctness);
          const validScores = scores.filter(v => v != null);
          const best = validScores.length ? Math.max(...validScores) : 0;
          return (
            <tr key={c.key} style={{ borderTop: "1px solid rgba(7,26,48,0.08)" }}>
              <Td>
                <div style={{ font: "600 14px/19px var(--forge-font)" }}>{c.label}</div>
                <div style={{ font: "400 11.5px/15px var(--forge-font)", color: "var(--forge-on-light-mute)" }}>{c.expl}</div>
              </Td>
              <Td align="center" muted><span style={{ font: "500 12px/1 var(--forge-mono)" }}>{agents[0].perCategory[c.key]?.n ?? "—"}</span></Td>
              {agents.map((a, i) => <ScoreCell key={a.key} value={scores[i]} highlight={scores[i] != null && scores[i] >= best && best > 0}/>)}
            </tr>
          );
        })}
      </tbody>
    </table>
  );
};

const ScoreCell = ({ value, highlight }) => {
  if (value == null) {
    return <td style={{ padding: "14px 18px", textAlign: "center", font: "500 13px/1 var(--forge-mono)", color: "var(--forge-on-light-mute)" }}>—</td>;
  }
  const tone = value >= 1.7 ? "rgb(60,140,40)" : value >= 1.0 ? "rgb(170,115,0)" : "rgb(180,0,40)";
  return (
    <td style={{ padding: "14px 18px", textAlign: "center" }}>
      <span style={{
        display: "inline-flex", alignItems: "center", gap: 6,
        padding: "5px 11px", borderRadius: 999,
        background: highlight ? "rgba(212,250,80,0.25)" : "transparent",
        border: highlight ? "1px solid rgba(120,160,0,0.45)" : "1px solid transparent",
      }}>
        <span style={{ width: 6, height: 6, borderRadius: 999, background: tone }}/>
        <span style={{ font: "700 13px/1 var(--forge-mono)" }}>{value.toFixed(2)}</span>
      </span>
    </td>
  );
};

// ─── Confusion matrix as Slab ───
const ConfusionSlab = ({ mode }) => {
  const b = mode.binary;
  const perfect = b.recallNonCompliant >= 1.0;
  return (
    <Slab padding={24}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-start", marginBottom: 18 }}>
        <div>
          <div className="f-kicker">{mode.label}</div>
          <div style={{ font: "500 12px/16px var(--forge-font)", color: "var(--forge-on-dark-mute)", marginTop: 6 }}>{mode.sublabel}</div>
        </div>
        <span style={{
          display: "inline-flex", alignItems: "center", gap: 6,
          padding: "4px 11px", borderRadius: 999,
          color: perfect ? "var(--forge-mint-warm)" : "var(--forge-on-dark)",
          border: perfect ? "1px solid var(--forge-mint-warm)" : "1px solid rgba(255,255,255,0.20)",
          font: "700 11px/1 var(--forge-mono)",
          whiteSpace: "nowrap",
        }}>recall {b.recallNonCompliant.toFixed(2)}</span>
      </div>

      <div style={{ display: "grid", gridTemplateColumns: "auto 1fr 1fr", gap: 5 }}>
        <div/>
        <CornerLabel>pred non-comp.</CornerLabel>
        <CornerLabel>pred compliant</CornerLabel>

        <RowLabel>actual non-comp.</RowLabel>
        <ConfCell value={b.tp} tone="success" label="TP"/>
        <ConfCell value={b.fn} tone={b.fn === 0 ? "successDim" : "danger"} label="FN"/>

        <RowLabel>actual compliant</RowLabel>
        <ConfCell value={b.fp} tone="warn" label="FP"/>
        <ConfCell value={b.tn} tone="successDim" label="TN"/>
      </div>

      <div style={{ display: "flex", gap: 18, marginTop: 16, font: "500 11px/14px var(--forge-font)", color: "var(--forge-on-dark-mute)" }}>
        <span>F1 <span style={{ font: "700 11px/1 var(--forge-mono)", color: "var(--forge-on-dark-strong)" }}>{b.f1NonCompliant.toFixed(2)}</span></span>
        <span>Prec <span style={{ font: "700 11px/1 var(--forge-mono)", color: "var(--forge-on-dark-strong)" }}>{b.precisionNonCompliant.toFixed(2)}</span></span>
        <span>Acc <span style={{ font: "700 11px/1 var(--forge-mono)", color: "var(--forge-on-dark-strong)" }}>{b.accuracy.toFixed(2)}</span></span>
      </div>
    </Slab>
  );
};

const ConfCell = ({ value, tone, label }) => {
  const styles = {
    success:    { bg: "rgba(120,220,140,0.18)", fg: "var(--forge-mint-warm)", border: "rgba(120,220,140,0.35)" },
    successDim: { bg: "rgba(120,220,140,0.06)", fg: "rgba(120,220,140,0.80)", border: "rgba(120,220,140,0.20)" },
    warn:       { bg: "rgba(255,190,92,0.14)",  fg: "var(--forge-amber)",     border: "rgba(255,190,92,0.35)" },
    danger:     { bg: "rgba(247,100,110,0.16)", fg: "var(--forge-red)",       border: "rgba(247,100,110,0.40)" },
  }[tone];
  return (
    <div style={{
      padding: "12px 8px", borderRadius: 8,
      background: styles.bg, color: styles.fg,
      border: `1px solid ${styles.border}`,
      display: "flex", flexDirection: "column", alignItems: "center", gap: 2,
    }}>
      <span style={{ font: "800 22px/1 var(--forge-font)" }}>{value}</span>
      <span style={{ font: "600 9px/1 var(--forge-font)", letterSpacing: "0.12em", opacity: 0.85 }}>{label}</span>
    </div>
  );
};

const CornerLabel = ({ children }) => (
  <div style={{
    font: "600 10px/14px var(--forge-font)", letterSpacing: "0.10em",
    color: "var(--forge-on-dark-faint)", textAlign: "center",
    textTransform: "uppercase", padding: "6px 0",
  }}>{children}</div>
);
const RowLabel = ({ children }) => (
  <div style={{
    font: "600 10px/1 var(--forge-font)", letterSpacing: "0.10em",
    color: "var(--forge-on-dark-faint)", textTransform: "uppercase",
    display: "flex", alignItems: "center", paddingRight: 8,
  }}>{children}</div>
);

// Th / Td come from primitives.jsx

Object.assign(window, { EvalScreen });

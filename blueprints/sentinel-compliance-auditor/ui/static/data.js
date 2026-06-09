// Real data from sentinel-agent repo (comparison_3way_20260521.json) + SOPs
window.SENTINEL_DATA = {
  evalResults: {
    naive: {
      label: "Naive RAG",
      sublabel: "DeepSeek-V4-Pro",
      tagline: "1 retrieval + 1 LLM call · no tools",
      model: "deepseek-ai/DeepSeek-V4-Pro",
      total: 120,
      totalCost: 1.48,
      latencyAvg: 14.3,
      latencyTotal: 1715.2,
      inputTokens: 698170,
      outputTokens: 43663,
      binary: {
        accuracy: 0.781,
        recallNonCompliant: 0.864,
        precisionNonCompliant: 0.826,
        f1NonCompliant: 0.844,
        macroF1: 0.738,
        tp: 19, fp: 4, tn: 6, fn: 3,
      },
      perCategory: {
        factual_single_hop: { n: 22, correctness: 1.05, citations: 1.05 },
        multi_regulation:   { n: 22, correctness: 0.73, citations: 0.73 },
        edition_aware:      { n: 14, correctness: 0.36, citations: 0.29 },
        sop_compliance:     { n: 35, binaryAcc: 0.78 },
        web_grounded:       { n: 10, correctness: 0.50, citations: 0.20 },
        negation_gap:       { n: 17, correctness: 0.88, citations: 0.65 },
      },
    },
    agentic: {
      label: "Agentic (Nebius)",
      sublabel: "DeepSeek-V4-Pro + Pinecone + Tavily",
      tagline: "ReAct · Pinecone + web · sub-agent fan-out",
      model: "deepseek-ai/DeepSeek-V4-Pro",
      total: 120,
      totalCost: 12.92,
      latencyAvg: 91.1,
      latencyTotal: 10936.6,
      inputTokens: 6520751,
      outputTokens: 332211,
      binary: {
        accuracy: 0.771,
        recallNonCompliant: 1.0,
        precisionNonCompliant: 0.758,
        f1NonCompliant: 0.862,
        macroF1: 0.598,
        tp: 25, fp: 8, tn: 2, fn: 0,
      },
      perCategory: {
        factual_single_hop: { n: 22, correctness: 1.91, citations: 1.73 },
        multi_regulation:   { n: 22, correctness: 2.00, citations: 1.64 },
        edition_aware:      { n: 14, correctness: 1.71, citations: 1.14 },
        sop_compliance:     { n: 35, binaryAcc: 0.77 },
        web_grounded:       { n: 10, correctness: 1.70, citations: 1.20 },
        negation_gap:       { n: 17, correctness: 1.88, citations: 1.47 },
      },
    },
    openai: {
      label: "Agentic (OpenAI)",
      sublabel: "GPT-5.5 + Pinecone + Tavily",
      tagline: "ReAct · Pinecone + web · sub-agent fan-out",
      model: "gpt-5.5",
      total: 120,
      totalCost: 44.11,
      latencyAvg: 64.9,
      latencyTotal: 7786.5,
      inputTokens: 6339895,
      outputTokens: 384064,
      binary: {
        accuracy: 0.771,
        recallNonCompliant: 1.0,
        precisionNonCompliant: 0.758,
        f1NonCompliant: 0.862,
        macroF1: 0.598,
        tp: 25, fp: 8, tn: 2, fn: 0,
      },
      perCategory: {
        factual_single_hop: { n: 22, correctness: 1.95, citations: 1.86 },
        multi_regulation:   { n: 22, correctness: 2.00, citations: 1.77 },
        edition_aware:      { n: 14, correctness: 1.50, citations: 1.64 },
        sop_compliance:     { n: 35, binaryAcc: 0.77 },
        web_grounded:       { n: 10, correctness: 1.40, citations: 1.30 },
        negation_gap:       { n: 17, correctness: 1.88, citations: 1.76 },
      },
    },
  },

  // The question being raced in the Compare tab — drawn from negation_gap
  raceQuestion: {
    id: "q-042",
    category: "negation_gap",
    difficulty: "hard",
    sop_id: "SOP-ISEC-008",
    sopTitle: "Cryptographic Controls and Key Management",
    regulations_involved: ["HIPAA Security Rule", "SOC 2 CC6.1"],
    expected_compliance_level: "non_compliant",
    question: "Review SOP-ISEC-008 (Cryptographic Controls and Key Management). Does it satisfy 45 CFR 164.312(a)(2)(iv) — encryption and decryption of ePHI — and SOC 2 CC6.1 logical access controls? Identify any specific safeguards that are missing or vague.",
  },

  // Findings table for the audit screen
  auditFindings: [
    { sop: "SOP-AIML-004", title: "Model Validation Framework",          unit: "AI/ML Engineering",       reg: "EU AI Act", level: "compliant", evidence: "Section 4.2 cites Article 9 risk-mgmt requirements verbatim", severity: "—" },
    { sop: "SOP-AIML-007", title: "Model Monitoring & Drift Detection",  unit: "AI/ML Engineering",       reg: "NIST AI RMF", level: "partial",  evidence: "Drift thresholds defined; lacks Govern-1.6 incident escalation",  severity: "med" },
    { sop: "SOP-CAI-002",  title: "Clinical AI Deployment Protocol",     unit: "Clinical AI Products",    reg: "HIPAA §164.312", level: "compliant", evidence: "AES-256 at rest, TLS 1.3 in transit, audit logging on PHI access", severity: "—" },
    { sop: "SOP-DGP-004",  title: "PHI Access Control Procedure",        unit: "Data Governance",         reg: "HIPAA §164.308(a)(4)", level: "gap", evidence: "No documented periodic access review cadence (§164.308(a)(4)(ii)(C))", severity: "high" },
    { sop: "SOP-DGP-008",  title: "Data Subject Rights Handling",        unit: "Data Governance",         reg: "GDPR Art. 15-22", level: "compliant", evidence: "30-day SLA, identity verification flow documented", severity: "—" },
    { sop: "SOP-FIN-003",  title: "Model Risk Documentation",            unit: "Financial Services",     reg: "SR 11-7", level: "partial",  evidence: "Effective challenge process referenced but no quantitative thresholds", severity: "med" },
    { sop: "SOP-ISEC-002", title: "Access Control & Identity Mgmt",      unit: "Information Security",   reg: "SOC 2 CC6.1", level: "compliant", evidence: "MFA enforced org-wide; quarterly access reviews", severity: "—" },
    { sop: "SOP-ISEC-006", title: "Security Incident Response",          unit: "Information Security",   reg: "HIPAA §164.308(a)(6)", level: "compliant", evidence: "72-hour breach notification, IR team named, evidence preservation", severity: "—" },
    { sop: "SOP-ISEC-008", title: "Cryptographic Controls",              unit: "Information Security",   reg: "HIPAA §164.312(a)(2)(iv)", level: "gap", evidence: "Key rotation cadence not specified; HSM use 'recommended', not required", severity: "high" },
    { sop: "SOP-ISEC-012", title: "Security Logging & Monitoring",       unit: "Information Security",   reg: "SOC 2 CC7.2", level: "partial",  evidence: "SIEM coverage gaps in dev environments; log retention < 1 year", severity: "med" },
    { sop: "SOP-ITO-005",  title: "Change Management",                   unit: "IT Operations",          reg: "SOC 2 CC8.1", level: "compliant", evidence: "CAB approval, rollback plans, change windows documented", severity: "—" },
    { sop: "SOP-LEG-002",  title: "Cross-Border Data Transfer",          unit: "Legal & Compliance",     reg: "GDPR Ch. V", level: "partial",  evidence: "SCCs in place; TIA missing for 3 sub-processors", severity: "med" },
  ],

  // 200-SOP grid status — for the heatmap chip strip
  sopStatus: (() => {
    // Stable distribution that matches the narrative: 8 running, 89 compliant, 74 partial, 29 gap.
    const order = [];
    for (let i = 0; i < 8;  i++) order.push("running");
    for (let i = 0; i < 89; i++) order.push("compliant");
    for (let i = 0; i < 74; i++) order.push("partial");
    for (let i = 0; i < 29; i++) order.push("gap");
    // Shuffle deterministically (Fisher-Yates with stable seed) to mix the heatmap.
    let s = 7;
    const rng = () => { s = (s * 1103515245 + 12345) & 0x7fffffff; return s / 0x7fffffff; };
    for (let i = order.length - 1; i > 0; i--) {
      const j = Math.floor(rng() * (i + 1));
      [order[i], order[j]] = [order[j], order[i]];
    }
    return order;
  })(),

  // Tool-call stream for the audit chat
  toolStream: [
    { kind: "user", text: "Audit all SOPs against their tagged regulations. Focus on HIPAA Security Rule and SOC 2." },
    { kind: "thought", text: "I'll fan out to 200 SOPs in parallel using audit_all_sops. Each sub-agent will pull regulation text from Pinecone, then assess compliance level." },
    { kind: "tool", name: "list_regulations", args: {}, result: "9 frameworks in knowledge base: HIPAA, SOC 2, GDPR, EU AI Act, NIST AI RMF, SR 11-7, SB 53, SB 942, AB 853", durationMs: 412 },
    { kind: "tool", name: "audit_all_sops", args: { workers: 10 }, result: "Spawning 200 sub-agents (10-wide pool). 192/200 complete · 8 in-flight.", durationMs: 0, running: true },
    { kind: "subagents", items: [
      { sop: "SOP-ISEC-008", reg: "HIPAA §164.312", level: "gap", note: "Key rotation cadence not specified" },
      { sop: "SOP-DGP-004",  reg: "HIPAA §164.308", level: "gap", note: "No periodic access review cadence" },
      { sop: "SOP-ITO-005",  reg: "SOC 2 CC8.1",    level: "compliant", note: "CAB + rollback documented" },
      { sop: "SOP-AIML-007", reg: "NIST AI RMF",    level: "partial",  note: "Drift defined; incident escalation missing" },
    ]},
  ],

  // session-level cost meter
  costMeter: {
    inputTokens: 5_843_212,
    outputTokens: 297_044,
    costUsd: 11.26,
    elapsedSec: 9_417,
    sopsComplete: 192,
    sopsTotal: 200,
  },
};

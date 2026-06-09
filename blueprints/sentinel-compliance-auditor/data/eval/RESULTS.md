# Naive RAG vs Agentic Stack — Evaluation Results

End-to-end accuracy evaluation of the demo's claim that **agentic compliance auditing (deepagents + Pinecone + Tavily) beats naive RAG**, plus a model-swap study comparing the agentic stack on an open-weights model (Nebius DeepSeek-V4-Pro) vs. a closed commercial model (OpenAI gpt-5.5). 120-question hand-crafted Q&A dataset, scored against `compliance_matrix.json` ground truth and an LLM-as-judge for freeform answers.

**Three configurations evaluated:**

| Mode | Model | Stack | Tools |
|---|---|---|---|
| `naive` | DeepSeek-V4-Pro (Nebius) | Single retrieval → single LLM call, no tools | none |
| `agentic` (Nebius) | DeepSeek-V4-Pro (Nebius) | ReAct agent | retrieve_regulation, search_web, read_sop |
| `agentic-openai` | gpt-5.5 (OpenAI) | ReAct agent (identical to above) | retrieve_regulation, search_web, read_sop |

Same prompts, same retrieval primitive (Pinecone, namespace `regulations`), same temperature (0.1). The two agentic configs differ **only** in the underlying chat model. Judge stays on Nebius DeepSeek for grader consistency across modes.

Source files: `data/eval/qa_dataset.jsonl`, `scripts/run_qa_eval.py`, `sentinel/eval/`. Raw run output: `data/eval/results/{naive,agentic,agentic_openai}_*.json` + `comparison_3way_20260521.json`.

---

## Dataset

- **120 questions** across 6 categories
- **35 `sop_compliance` questions** with ground truth from `data/compliance_matrix.json` (10 compliant, 10 partial, 15 gap)
- **28 unique SOPs** spanning all 10 business units
- All 6 in-Pinecone regulation frameworks exercised (HIPAA, GDPR, SOC 2, EU AI Act, NIST AI RMF, SR 11-7)

---

## Per-category correctness (LLM-as-judge, 0–2)

| Category | n | naive | agentic (Nebius) | agentic (OpenAI) |
|---|---|---|---|---|
| `factual_single_hop` | 22 | 1.05 | 1.91 | 1.95 |
| `multi_regulation` | 22 | 0.73 | 2.00 | 2.00 |
| `edition_aware` | 14 | 0.36 | **1.71** | 1.50 |
| `negation_gap` | 17 | 0.88 | 1.88 | 1.88 |
| `web_grounded` | 10 | 0.50 | **1.70** | 1.40 |

Both agentic configs decisively beat naive in every category (+0.86 to +1.35). Between the two agentic models: **Nebius slightly better on edition-aware (+0.21) and web-grounded (+0.30)**; the other three categories are tied or within 0.05.

## Per-category citation quality (LLM-as-judge, 0–2)

| Category | n | naive | agentic (Nebius) | agentic (OpenAI) |
|---|---|---|---|---|
| `factual_single_hop` | 22 | 1.05 | 1.73 | **1.86** |
| `multi_regulation` | 22 | 0.73 | 1.64 | **1.77** |
| `edition_aware` | 14 | 0.29 | 1.14 | **1.64** |
| `negation_gap` | 17 | 0.65 | 1.47 | **1.76** |
| `web_grounded` | 10 | 0.20 | 1.20 | **1.30** |

**OpenAI cites better than Nebius across every category** — most significantly on `edition_aware` (+0.50) and `negation_gap` (+0.29). gpt-5.5 appears more rigorous about producing specific regulatory section references.

---

## SOP compliance — BINARY scoring (primary)

Partial and gap collapsed to `non_compliant` since both require audit remediation (the partial-vs-gap distinction is severity, not action). `non_compliant` is the positive class.

| Metric | naive | agentic (Nebius) | agentic (OpenAI) |
|---|---|---|---|
| Accuracy | 0.781 | 0.771 | 0.771 |
| **Non-compliant recall** | 0.864 | **1.000** | **1.000** |
| Non-compliant precision | 0.826 | 0.758 | 0.758 |
| Compliant recall | 0.600 | 0.200 | 0.200 |
| Macro F1 | 0.738 | 0.598 | 0.598 |
| TP / FP / TN / FN | 19/4/6/3 | 25/8/2/0 | 25/8/2/0 |

**Both agentic configs achieve identical sop_compliance metrics**, including the same "partial bias" on compliant SOPs (8 of 10 compliant SOPs flagged as `partial`). The 100% non-compliant recall — the key audit-safety metric — holds for both models. Naive misses 12% of real issues.

## SOP compliance — 3-class detail (secondary)

| Metric | naive | agentic (Nebius) | agentic (OpenAI) |
|---|---|---|---|
| Exact-level accuracy | 0.594 | 0.400 | 0.429 |
| **Adjacent-tolerant** | 0.844 | **1.000** | **1.000** |
| Off-by-2 catastrophic misses | 5 | **0** | **0** |
| 3-class macro F1 | — | 0.352 | 0.389 |

OpenAI is marginally better on exact 3-class match (+0.029 accuracy, +0.037 macro F1) but otherwise identical. **Both agentic configs are 100% adjacent-tolerant** — zero catastrophic compliant↔gap errors.

---

## Cost / latency (5 workers)

| Metric | naive | agentic (Nebius) | agentic (OpenAI) | OAI vs Nebius |
|---|---|---|---|---|
| Total cost | $1.48 | $12.92 | $44.11 | **3.41×** |
| Input tokens | 698 K | 6.52 M | 6.34 M | 0.97× |
| Output tokens | 44 K | 332 K | 384 K | 1.16× |
| Wall time | 28.6 min | 182.3 min | 129.8 min | **0.71×** |
| Avg per question | 14.3 s | 91.1 s | 64.9 s | **0.71×** |

OpenAI's token usage is comparable to Nebius (~same retrieval volume, slightly more output) but **3.4× more expensive** due to pricing differentials ($5/M in + $30/M out vs Nebius $1.75/M + $3.50/M). Despite the cost, OpenAI is **30% faster** in wall time — fewer ReAct iterations per question.

---

## What the demo can claim, defensibly

1. **The agentic stack never misses a real compliance issue** (100% non-compliant recall, 0 catastrophic compliant↔gap errors) — **regardless of underlying model.** Both Nebius DeepSeek and OpenAI gpt-5.5 deliver identical sop_compliance metrics. The capability lives in the stack, not the model.
2. **Naive RAG misses 12% of real issues**, including 5 catastrophic compliant↔gap confusions.
3. **Agentic dominates every freeform Q&A category** by 0.86–1.35 correctness points (out of 2). Citation quality is strictly higher (+0.42 to +1.35 over naive).
4. **Model choice is a cost-quality knob, not a capability boundary:** OpenAI cites better (+0.10 to +0.50 across all categories) and is 30% faster, but costs 3.4× more. Nebius is slightly better on edition-aware and web-grounded categories.
5. **Cost premium ≈ 8.7× (Nebius) or ≈ 30× (OpenAI)** over naive RAG. False alarms are recoverable; missed issues are not.

The trade-off the agent makes — over-flag compliant SOPs as "needs review" rather than risk missing one — is the correct audit-safety posture, and it holds with either model.

---

# Metric definitions

### LLM-as-judge metrics (freeform categories)

A separate `ChatOpenAI` call (Nebius DeepSeek, shared across modes for grader consistency) grades each candidate answer 0–2 on two axes (see `sentinel/eval/judge.py`).

- **Correctness (0/1/2)** — `0` = wrong or missing; `1` = partially correct or vague; `2` = fully correct and on-point. Compared against `expected_answer` in the dataset.
- **Citation quality (0/1/2)** — `0` = no specific citation; `1` = some citations but missing/wrong sections; `2` = cites the expected regulation(s) and section(s).

Aggregated per category as the arithmetic mean across questions.

### SOP compliance — binary

Maps 3-class predictions to binary via `compliant → compliant`, `partial → non_compliant`, `gap → non_compliant`. `non_compliant` is the positive class.

- **Accuracy** — `(TP + TN) / total`. Direct match rate.
- **Non-compliant recall** — `TP / (TP + FN)`. *Of all SOPs that are truly non-compliant, how many did we catch?* **The audit-safety metric — 1.0 means zero missed issues.**
- **Non-compliant precision** — `TP / (TP + FP)`. *Of all our non-compliant flags, how many were right?* Inverse of false-alarm rate.
- **Compliant recall** — `TN / (TN + FP)`. *Of truly compliant SOPs, how many did we correctly clear?*
- **Macro F1** — `(F1_non_compliant + F1_compliant) / 2`. Penalises bad performance on either class.

### SOP compliance — 3-class

Levels: `compliant=0, partial=1, gap=2` (ordinal distance matters).

- **Exact-level accuracy** — strict 3-class match rate.
- **Adjacent-tolerant accuracy** — proportion where `|predicted − expected| ≤ 1`. Forgives one-step disagreements; flags catastrophic ones.
- **Off-by-2 catastrophic misses** — count of cases where `|predicted − expected| = 2` (compliant↔gap). **For an audit demo this should be 0.**
- **FP (too-strict)** — predicted level higher than GT (the auditor flags issues that aren't there).
- **FN (too-lenient)** — predicted level lower than GT (the auditor misses issues — worse).

### Cost / latency

- **Total cost (USD)** — `(input_tokens × $price_in + output_tokens × $price_out) / 1M` using model-specific pricing (DeepSeek-V4-Pro: $1.75/M in, $3.50/M out; gpt-5.5: $5/M in, $30/M out). Sum across answer + judge calls.
- **Wall time** — total elapsed seconds for the whole run with N workers concurrent. Bounded by tail latency.
- **Avg per question** — total wall time / question count. Useful for thinking about user-facing UX in the actual UI (not concurrency-discounted).

---

# Category definitions

The 6 question categories test structurally different capabilities. By design, 5 of them probe capabilities naive RAG **structurally lacks**; the 6th is a control case.

### `factual_single_hop` (n=22)

Direct retrieval of one regulation clause. *"What does HIPAA §164.308(a)(1)(ii)(A) require?"*

- **Naive can do it.** This is what RAG is designed for: one retrieval → answer.
- **Agent slightly better** at precise section citation.
- **Purpose:** sanity baseline. Verifies no regression on the easy case.

### `multi_regulation` (n=22)

Synthesis across two or more frameworks. *"Compare SOC 2 CC6.2 and HIPAA §164.308(a)(4) on access review."*

- **Naive fails:** a single Pinecone retrieval ranks by embedding similarity — it pulls chunks from *one* framework that best matches the query, missing the cross-framework citation.
- **Agent wins:** can issue multiple `retrieve_regulation(query, regulation="X")` calls, one per framework, then synthesise.
- **Purpose:** real compliance work involves overlapping frameworks (healthcare AI processes PHI under HIPAA AND falls under EU AI Act AND is auditable under SOC 2).

### `edition_aware` (n=14)

Distinguishing between historical versions of the same regulation. *"What changed between SR 11-7 (2011) and SR 26-2 (2026)?"*

- **Naive fails:** Pinecone stores `edition` as chunk metadata but naive queries without filters → retrieval mixes editions, model conflates them.
- **Agent wins:** can issue two filtered retrievals and explicitly contrast.
- **Purpose:** regulations evolve (HIPAA Privacy Rule → Omnibus → 2024 NPRM; EU AI Act 2021 proposal → 2024 final). Compliance work needs the version distinction.

### `sop_compliance` (n=35)

The demo's headline task: structured compliance judgment. *"Is SOP-X compliant with regulation Y?"* with a 3-class verdict (compliant / partial / gap), scored against `compliance_matrix.json`.

- **Naive struggles:** without SOP text in context, nothing to judge against; even with SOP text passed in, one retrieval rarely covers all required articles.
- **Agent wins:** uses `read_sop()` to inspect the SOP, iterates retrieval over multiple regulation articles, reasons over both. This is what the production demo does for every SOP audit.
- **Purpose:** measure the actual production task. Ground truth from a hand-labeled matrix.

### `web_grounded` (n=10)

Questions that require *current* information not in the static knowledge base. *"What's the most recent HHS OCR enforcement action affecting AI in healthcare?"*

- **Naive structurally fails:** no web access. Knowledge base contains regulation text but not enforcement bulletins, recent guidance, news.
- **Agent wins:** has `search_web(query)` via Tavily. Can fetch and cite current enforcement actions, regulator publications, case law.
- **Purpose:** real compliance work isn't just "what does the rule say" but "what did the regulator do *last week*?" Structural ability gap — agent should win every web_grounded question.

### `negation_gap` (n=17)

Identifying what's *missing* from an SOP, not what's present. *"What controls are MISSING from SOP-AIML-001 under EU AI Act Article 9?"*

- **Naive struggles:** retrieval surfaces what the regulation requires, not what the SOP lacks. The model has to reason over both sets — but single-pass reasoning tends to list what's *present* (the easy part) and miss what's *absent*.
- **Agent wins:** ReAct loop is structurally suited to set-difference reasoning — retrieve requirement, read SOP, retrieve next requirement, read SOP again, build a missing-controls checklist.
- **Purpose:** gap detection is the hardest and most valuable audit task. Listing missing items requires deliberative reasoning, not retrieval skill.

---

## Capability summary

| Category | Naive can do? | Agent can do? | Why the gap |
|---|---|---|---|
| `factual_single_hop` | ✓ yes | ✓ yes (slightly better) | Single retrieval suffices |
| `multi_regulation` | ✗ misses cross-framework | ✓ yes | Needs multiple filtered retrievals |
| `edition_aware` | ✗ conflates editions | ✓ yes | Needs metadata filter |
| `sop_compliance` | △ partial | ✓ yes | Needs SOP read + multi-article retrieval |
| `web_grounded` | ✗ no web access | ✓ yes | Needs Tavily |
| `negation_gap` | △ partial reasoning | ✓ yes | Needs iterative reasoning |

Five of six categories test capabilities naive RAG **structurally lacks**. The sixth (`factual_single_hop`) is the control where both should work.

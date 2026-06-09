---
sop_id: "SOP-AIML-019"
title: "A/B Testing and Canary Releases for Models"
business_unit: "AI/ML Engineering"
version: "5.2"
effective_date: "2025-08-25"
last_reviewed: "2026-06-05"
next_review: "2026-12-05"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: A/B Testing and Canary Releases for Models

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the unified framework for conducting A/B tests, multivariate tests, and canary deployments across all model types within Meridian Health Technologies' AI/ML portfolio. The procedures defined herein ensure that all model changes—from minor hyperparameter adjustments to full architectural replacements—are validated in real-world production contexts with appropriate statistical rigor, safety guardrails, and regulatory compliance before full-scale rollout.

This SOP operationalizes Meridian's commitment to evidence-based model evolution, patient safety, and financial integrity. By mandating structured experimentation and graduated exposure, the organization mitigates the risk of deploying underperforming, biased, or unsafe models into clinical, financial, and analytical workflows. The framework also serves as a critical control mechanism to satisfy Meridian's obligations under the EU AI Act for high-risk AI systems, NIST AI RMF governance principles, SR 11-7 model risk management expectations, and SOC 2 change management requirements.

### 1.2 Scope

**In-Scope Activities and Assets:**

This SOP applies to all A/B testing, multivariate testing, and canary release activities involving the following model categories deployed to or intended for deployment to Production, Pre-Production Staging, or Customer-Facing Sandbox environments:

| Model Category | Business Unit(s) Affected | Example Systems |
|----------------|--------------------------|-----------------|
| Clinical Decision Support Models | Clinical AI, Product | Radiology Triage Engine, Sepsis Early Warning System, Drug Interaction Predictor |
| Patient-Facing Diagnostic Models | Clinical AI, Regulatory Affairs | Dermatology Image Classifier (CE-marked), Arrhythmia Detection Pipeline |
| Clinical Workflow Optimization Models | Clinical Operations, AI/ML Engineering | ED Patient Flow Predictor, OR Scheduling Optimizer |
| Financial Risk and Fraud Models | Financial Intelligence, Revenue Cycle | Claims Denial Predictor, Anomaly Detection System v4, Payment Integrity Engine |
| Patient Experience and Personalization Models | Patient Engagement, Marketing | Care Gap Prioritization Engine, Appointment Adherence Predictor |
| Core NLP/NLU and Generative Models | AI/ML Engineering, All Business Units | Meridian Clinical Language Model (MCLM), Automated Chart Abstraction Pipeline |
| Infrastructure and MLOps Tooling | AI/ML Engineering, Platform Engineering | Model Serving Router, Feature Store Query Optimizer |

**Out-of-Scope Activities:**

- Standard unit, integration, and regression tests executed within CI/CD pipelines prior to deployment (governed by SOP-AIML-008).
- Shadow deployments where a candidate model receives production traffic but returns no responses to downstream systems (governed by SOP-AIML-014).
- Post-deployment model monitoring for already fully rolled-out models (governed by SOP-AIML-022).

### 1.3 Applicability

This SOP is binding upon all personnel, contractors, and third-party vendors involved in the design, approval, execution, and observation of model experiments within Meridian Health Technologies. Compliance is mandatory for all releases meeting the scope criteria defined above. Violations of this procedure shall be managed in accordance with the *Employee Corrective Action Policy* (HR-POL-042) and the *Vendor Contract Breach Management Procedure* (PROC-VEND-017).

---

## 2. Definitions and Acronyms

For the purposes of this document, the following definitions and acronyms apply. Terms not defined here shall carry their standard meaning as documented in the *Meridian Corporate Glossary* (REF-DOC-001).

| Term / Acronym | Definition |
|----------------|------------|
| **A/B Test (Controlled Experiment)** | A randomized experiment comparing two variants—Control (A) and Treatment (B)—against a single, pre-registered Primary Success Metric over a fixed observation period. |
| **Multivariate Test (MVT)** | A randomized experiment comparing three or more variants simultaneously, typically testing multiple independent model changes, against a pre-registered set of metrics. Requires enhanced statistical correction (e.g., Bonferroni adjustment). |
| **Canary Release** | A graduated deployment strategy where a new model version (Canary) initially serves a minimal, tightly-controlled percentage of production traffic. Traffic is increased stepwise based on automated metric checks and manual Stage-Gate approvals. |
| **Shadow Deployment** | A candidate model mirrors live production traffic and records predictions without returning results to downstream systems. Governed by SOP-AIML-014. Not a substitute for A/B or Canary testing as defined here. |
| **Variant** | A distinct branch within an experiment. Includes Control (current production model) and one or more Treatments (candidate models). |
| **Control Variant** | The currently deployed, fully-validated production model serving as the benchmark in any experiment. |
| **Treatment Variant (Candidate)** | A new, updated, or alternative model whose performance is being evaluated against the Control. |
| **Randomization Unit** | The atomic entity on which traffic is randomly split. Must be a stable, unique identifier. For clinical models, this is the `patient_id`. For financial models, this is the `claim_id`. For NLP models, this is the `document_hash`. |
| **Primary Success Metric (PSM)** | The single, pre-registered metric that determines experiment success. Must be directly tied to business value or clinical safety. Examples: diagnostic sensitivity, denial overturn rate, patient wait time reduction. |
| **Guardrail Metrics** | Pre-defined, non-primary metrics that must not degrade by a statistically significant margin during an experiment. These act as safety, fairness, and business health checks. If any guardrail is violated, the experiment may be paused or terminated, regardless of PSM status. |
| **Minimum Detectable Effect (MDE)** | The smallest meaningful improvement over the Control that the experiment is statistically powered to detect. Set based on clinical, operational, or financial materiality. |
| **Statistical Power** | The probability that an experiment correctly rejects the null hypothesis (no difference between variants) when a true effect of at least the MDE exists. Minimum threshold for all Meridian experiments: 80%. |
| **Practical Significance** | A finding that, while statistically significant, represents an effect size large enough to justify the cost and operational disruption of a full rollout. All rollouts require a documented Practical Significance assessment. |
| **Stage-Gate** | A mandatory review checkpoint within a Canary release where the Release Manager and Designated Approver must explicitly approve progression before the canary traffic percentage is increased. |
| **Automatic Rollback** | An immediate, system-executed rollback (via the MLOps Router—see Section 6) triggered without human intervention when a Pre-Defined Catastrophic Threshold is breached. |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix (RACI)

The following matrix delineates responsibilities for the lifecycle of an A/B test or Canary release:

| Activity / Deliverable | Experiment Owner (EO) | Release Manager (RM) | Data Science Review Board (DSRB) | AI/ML Engineering (Platform) | Clinical Safety Officer (CSO) | Chief AI Officer (CAIO) |
|---|---|---|---|---|---|---|
| **Experiment Design Document (EDD) Authoring** | **R, A** | C | C | C | C | I |
| **Statistical Design Approval** | C | C | **R, A** | I | I | I |
| **Clinical / Financial Safety Review** | C | C | I | I | **R, A** | I |
| **Traffic Routing Configuration** | I | **R** | I | **A** | I | I |
| **Stage-Gate Review** | **R** | **A** | C | I | C | I |
| **Rollback Decision (Standard)** | C | **R** | C | **A** | C | I |
| **Rollback Decision (Catastrophic)** | I | I | I | **A (System)** | I | I |
| **Final Results & Rollout Approval** | **R** | C | **R** | C | **R** | **A** |
| **Artifact Archiving** | **R** | C | I | **A** | I | I |

### 3.2 Named Role Definitions

**Experiment Owner (EO):** A senior Data Scientist or ML Engineer from the originating business unit. This individual authors the EDD, monitors the experiment's health daily, and presents final results to the DSRB. The EO must have completed the mandatory training `TRAIN-AIML-019-2` ("Advanced Statistical Experimental Design for Safety-Critical Systems").

**Release Manager (RM):** A designated DevOps or MLOps engineer from the AI/ML Engineering Platform team. The RM is the sole executor of traffic routing changes in the Meridian MLOps Router (`mlops-router.internal.meridian.com`). All routing changes must be performed via audited Terraform Enterprise runs.

**Data Science Review Board (DSRB):** A standing committee chaired by the VP of Biostatistics. Members include at least two Principal Statisticians and one rotating Principal Engineer. The DSRB validates all EDD statistical designs, reviews final results, and adjudicates disputes over statistical methodology. Meets weekly on Wednesdays at 14:00 ET.

**Clinical Safety Officer (CSO):** Dr. Anya Sharma (Chief Medical Informatics Officer). The CSO holds veto power over any clinical model experiment. The CSO must sign off on the *Safety Assessment Checklist* (Appendix A) for all experiments affecting patient-facing models.

**Chief AI Officer (CAIO):** Dr. Marcus Rivera. The CAIO holds ultimate authority over all AI/ML artifacts, including authority to mandate the termination of any experiment deemed to pose a regulatory, reputational, or ethical risk.

---

## 4. Policy Statements

The following policies govern all A/B tests and Canary releases. Deviation must be authorized through the formal exception process defined in Section 8.

- **POL-019-01: Mandatory Pre-Registration.** All A/B tests and Canary releases, including all variants, metrics, sizing parameters, and success criteria, must be pre-registered in an approved Experiment Design Document (EDD) and logged in the Meridian Experiment Tracker ("Guild Tracker") *before* a single byte of experimental production traffic is routed.

- **POL-019-02: Single Primary Success Metric.** Every experiment must have exactly one, unambiguous, pre-registered Primary Success Metric (PSM) directly tied to a business or clinical Key Performance Indicator (KPI). Cherry-picking positive secondary metrics post-hoc to justify a rollout is strictly prohibited.

- **POL-019-03: Mandatory Guardrails for High-Risk Models.** For EU AI Act High-Risk models (see SOP-RISK-001), Guardrail Metrics must be explicitly defined. At minimum, guardrails must monitor for fairness degradation (by protected attributes), stability, and critical safety outcomes. Breach of any guardrail triggers an automatic experiment pause and mandatory CSO review.

- **POL-019-04: Mandatory Observation Period.** No A/B test may be concluded before the expiration of the pre-registered minimum observation period. This period must account for one full business cycle (minimum 1 week) and the cycle of any external effects (e.g., month-end financial close). The absolute minimum observation period for any high-risk model is 14 calendar days.

- **POL-019-05: Canary Graduation Gates.** A Canary release may not progress to the next traffic percentage increment (e.g., 1% to 5%) until all pre-defined health checks on the current increment have been met for the Minimum Soak Time, and the formal Stage-Gate review has been documented by the RM.

- **POL-019-06: Audit Trail Immutability.** All experiment configuration changes, traffic shifts, Stage-Gate approvals, and rollback events must generate immutable, timestamped audit log entries in Splunk. Logs must be retained for the period defined in SOP-DATA-011 (currently 7 years for clinical data).

---

## 5. Detailed Procedures

This section constitutes the operational workflow. All steps are mandatory unless explicitly marked as conditional.

### 5.1 Phase 1: Experiment Design and Approval

This phase is the sole responsibility of the Experiment Owner (EO) and must be completed before an RM ticket is opened.

#### 5.1.1 Step 1: Draft the Experiment Design Document (EDD)

The EO must complete the official template `FRM-AIML-019-1` (Experiment Design Document). The EDD is a controlled document and must include the following sections at minimum:

1.  **Experiment Hypothesis:** A clear, falsifiable business hypothesis (e.g., "Deploying the new Gradient Boosting model (v3) will reduce false-positive cardiac alerts by at least a relative 10% compared to the current LSTM model (v2), without any statistically significant increase in false-negative alerts.").
2.  **Variant Definitions:**
    - **Control:** Precise identification (Model Registry URI, container tag, etc.).
    - **Treatment(s):** Precise identification for each candidate. For Canary releases, the Treatment is the new model version.
3.  **Randomization Strategy:**
    - **Unit of Randomization:** Must be specified (e.g., `patient_id`).
    - **Salt & Hashing Procedure:** Procedure for salting and hashing the randomization unit to assign traffic. Standard procedure uses the `meridian-experiments` Python library, which applies a consistent SHA-256 hash using a per-project global salt.
4.  **Metrics Framework:**
    - **Primary Success Metric (PSM):** Exhaustive definition including source table/stream, aggregation logic, unit of measurement, and direction of good (e.g., "higher is better").
    - **Secondary Metrics:** Informational metrics to understand side effects.
    - **Guardrail Metrics:** Each must have a defined "no-worse-than" bound using a non-inferiority margin or a strict degradation threshold.
5.  **Sizing and Duration:**
    - **Minimum Detectable Effect (MDE):** Justified based on materiality.
    - **Desired Statistical Power:** Must be >= 0.80.
    - **Significance Level (Alpha):** Standard = 0.05.
    - **Required Sample Size:** Calculated using a standard power analysis (the `meridian-ml.experiments.power` package is the approved tool).
    - **Minimum Observation Period (Calendar Days):** Justified per POL-019-04.
6.  **Safety and Ethical Assessment:** A checklist confirming review of potential biases, downstream patient impact, data privacy implications, and, for generative models, hallucination risk.
7.  **Rollback Criteria:** Pre-defined thresholds requiring a Standard Rollback (Section 5.4).

#### 5.1.2 Step 2: Statistical Design Review (DSRB)

The EO submits the completed EDD to the Data Science Review Board via the ServiceNow workflow `DSRB Review Request`. The DSRB review focuses on:

- Appropriateness of the PSM for the hypothesis.
- Correctness of the Randomization Unit.
- Validity of the statistical sizing and power analysis. The DSRB statistician will independently re-run the power analysis.
- Correctness of the multiple comparison correction strategy (e.g., Bonferroni, Benjamini-Hochberg) if a Multivariate Test is proposed.
- Guardrail metric selection and thresholds.

The DSRB records its decision (Approved / Revisions Requested / Rejected) in Guild Tracker. A rejection is final; a new EDD must be submitted.

#### 5.1.3 Step 3: Clinical/Fiscal Safety Review

- **High-Risk Clinical Models:** The approved EDD is routed to the CSO for a Safety Review. The CSO reviews the "Safety and Ethical Assessment" section of the EDD and may impose additional, experiment-specific guardrail metrics. The CSO signature is mandatory.
- **Financial Models impacting Revenue Cycle (above $1M annual ARR):** The approved EDD is routed to the VP of Financial Intelligence, who serves as the Financial Safety Reviewer, analogous to the CSO.

### 5.2 Phase 2: Technical Implementation and Setup

Performed jointly by the EO and the Release Manager (RM), after Phase 1 approval.

#### 5.2.1 Step 4: RM Opens Infrastructure Ticket

The RM creates a Change Request in ServiceNow (`CHG` type), linking the approved EDD Guild Tracker ID. The ticket details the infrastructure-as-code changes required.

#### 5.2.2 Step 5: Model Registration and Containerization

The EO ensures all treatment models are registered in the **Meridian Model Registry** (`model-registry.ml.meridian.com`). Each variant is tagged with the Guild Tracker Experiment ID. Models must be packaged as standard Meridian Inference Service (MIS) containers. The RM verifies all containers pass a vulnerability scan in Prisma Cloud.

#### 5.2.3 Step 6: Experiment Routing Configuration (RM & EO)

The RM and EO co-author the Terraform configuration for the MLOps Router (`meridian-mlops/providers/router`). This configuration defines:

- **Traffic Split Rules:** Initial split percentages for an A/B test (e.g., 50/50) or a Canary (e.g., 1% new / 99% current).
- **Allocation Hashing Logic:** Terraform module that codifies the randomization unit and hashing procedure from the EDD.
- **Shadow Traffic Rules (Optional):** If, for a Canary, the treatment model also receives shadow traffic of all requests as a diagnostic aid, this is declared here.

This configuration is peer-reviewed by a second MLOps engineer, then merged into the `production` branch of the `mlops-infra` GitLab repository, triggering a Terraform Enterprise plan and apply.

### 5.3 Phase 3: Execution and Monitoring

This is the live phase of the experiment, from activation to conclusion.

#### 5.3.1 Step 7: Experiment Activation

Upon Terraform apply success, the RM, following a strict change window (e.g., Tuesday 04:00-06:00 ET), runs the `publish-experiment-config` CLI command. The system confirms routing to all variants. The RM updates the ServiceNow CHG ticket to "Active" and declares the experiment start time (`T0`).

#### 5.3.2 Step 8: Continuous Metric Monitoring

From `T0`, the EO performs continuous (daily) health checks using the custom Meridian Experiment Dashboard in Grafana (`grafana.ml.meridian.com/d/aiml019`).

**Daily Checks (EO Responsibility):**
1.  **Sample Ratio Mismatch (SRM) Check:** A chi-squared test comparing the observed traffic ratio against the configured split. A p-value < 0.001 for SRM triggers an immediate investigation. No experiment-related decision can be made until SRM is resolved.
2.  **Guardrail Metric Status:** Each guardrail must be checked against its "no-worse-than" bound.
3.  **Data Quality & Latency:** Monitor for upstream data drift and model serving latency spikes.

**Weekly Status Report:** The EO posts a brief status update in the Slack channel `#ml-experiments-active`.

**Procedure for Guardrail Breach:**
If any guardrail metric crosses its pre-defined breach threshold, the following occurs:
1.  **Automated Pause:** The monitoring system (Grafana alert hook) automatically triggers a "safe-routing" event in the MLOps Router, setting the Treatment variant traffic to 0% (a full stop). An alert is fired to `#ml-experiments-active` and the RM on-call pager.
2.  **CSO Notification (High-Risk Models):** For high-risk models, the CSO is immediately notified.
3.  **Root Cause Analysis (RCA):** The EO and RM have 48 business hours to perform an RCA and present findings in a Guardrail Breach Report (`FRM-AIML-019-3`). The experiment may not resume without DSRB and CSO/Financial Safety Reviewer approval of the report.

#### 5.3.3 Step 9: Canary Stage-Gate Process

This process replaces Step 8 for a graduated Canary release. Only after the Minimum Soak Time for the current traffic step (e.g., 24 hours for a 1% step) has elapsed and all health checks are "green":

1.  **EO Calls the Gate:** The EO prepares a brief Stage-Gate Report in Guild Tracker, showing the current step's PSM, Guardrails, and latency/error rate comparisons.
2.  **RM & CSO Approve:** The RM and, for high-risk models, the CSO, provide explicit digital sign-off in Guild Tracker.
3.  **RM Executes Next Step:** The RM executes the Terraform configuration change for the next traffic percentage (e.g., 1% -> 5%). The Minimum Soak Time resets for the new step.

**Standard Canary Traffic Steps**: 1% -> 5% -> 25% -> 50% -> 100%.

#### 5.3.4 Step 10: Final Statistical Analysis

At the end of the pre-registered observation period, the EO stops data collection via the Guild Tracker "End Analysis Period" function. The EO performs the final analysis using the `meridian-ml.experiments.evaluate` function, which produces the official Experiment Results Report (`FRM-AIML-019-4`). The report explicitly states whether the PSM achieved statistical significance, and if Guardrails were maintained.

### 5.4 Phase 4: Closure and Rollout Decision

#### 5.4.1 Step 11: Final Review Meeting

The EO presents the official Experiment Results Report to the DSRB. The meeting is conducted from the *DSRB Review* Jira project; all materials must be linked. The DSRB reviews and validates:

- Statistical validity of results.
- Absence of SRM issues.
- Adequacy of observation period.
- A **Practical Significance Assessment**, documented by the EO, which weighs the statistical effect against the operational cost of a full rollout.

The DSRB votes on a recommendation: **"Roll Out"**, **"Do Not Roll Out"**, or **"Gather More Data"**.

#### 5.4.2 Step 12: Go/No-Go Authorization

The DSRB recommendation, the EDD, and the final report are forwarded to the CAIO (Dr. Rivera) for the final Go/No-Go decision. For clinical models, the CSO must co-sign the authorization. The CAIO decision is final and is recorded in Guild Tracker.

#### 5.4.3 Step 13: Full Rollout or Rollback (RM)

Upon "Go" authorization, the RM executes the traffic routing change to 100% for the winning Treatment via a standard Change Request. This transition terminates the experiment phase, and the model becomes the new standard production version, subject to SOP-AIML-022 (Monitoring). If "No-Go" or "Rollback" is the decision, the RM executes the traffic shift returning the Control to 100%.

---

## 6. Controls and Safeguards

This section details technical and administrative controls that enforce policy.

### 6.1 Technical Safeguards

**1. MLOps Router Traffic Control Gate:**
The Meridian MLOps Router (`mlops-router`) is the sole point of ingress for inference requests to A/B or Canary models. Its control plane enforces all traffic splits. Features include:
- **Atomic Assignment:** User/Patient assignment to a variant is based on a hash of the unit (e.g., `patient_id`) and a per-experiment salt. Assignment is consistent for the life of the experiment (no "carry-over" effect for users).
- **"Zero-Traffic Kill Switch":** A single, 2FA-protected API endpoint (`POST /router/experiment/{id}/pause`) that the RM, CAIO, or CSO can invoke to immediately set all non-control traffic to 0%. This bypasses normal CI/CD and has a guaranteed execution time of < 15 seconds.
- **Latency Circuit Breaker:** If the p99 latency for a Treatment model exceeds the Control model by a factor of 3x for a rolling 5-minute window, the router automatically isolates the Treatment, serving 100% traffic from Control. This triggers an immediate incident ticket.

**2. Automated Sample Ratio Mismatch (SRM) Detection:**
A continuous drift-detection job runs hourly in the Databricks monitoring workspace, comparing the actual ratio of assigned units to the configured ratio. An alert is fired to the `#ml-experiments-active` Slack channel on warning (p < 0.01) and critical (p < 0.001).

**3. Immutable Audit Ledger:**
All configuration changes to the MLOps Router are managed by Terraform Enterprise. All Terraform run logs, along with structured application logs that capture every routing decision (Assignment ID, Hash, Variant Selected, Timestamp), are streamed to a write-once-read-many (WORM) audit index in Splunk.

**4. Guardrail-Backed Feature Flag:**
The experiment infrastructure is wrapped in a feature flag service (LaunchDarkly). The Canary Stage-Gate process is programmatically gated: the `rollout_percentage` flag cannot be increased if the "guardrail_breach" metric flag is in a `true` state.

### 6.2 Administrative Safeguards

- **Pre-Registration Mandate:** Guild Tracker will reject any manual traffic split configuration via Terraform Enterprise if a valid `experiment_id` from Guild Tracker is not provided in the plan. This is enforced via an Open Policy Agent (OPA) policy on the Terraform plan.
- **Segregation of Duties:** The Experiment Owner (EO) may *define* the EDD. The Data Science Review Board (DSRB) *validates* the design. The Release Manager (RM) *executes* the technical deployment. No single individual can design and deploy without independent review.
- **Required Review Cadence:** An open experiment that has not had a documented health check from the EO in 7 calendar days triggers an automatic Stage-Gate hold, pausing the experiment until a health check is completed.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Core Metrics Framework (KPIs)

| KPI | Description | Measurement Method | Target / Threshold |
|-----|-------------|--------------------|--------------------|
| **Experiment Velocity** | Median calendar days from EDD first draft to Final Rollout Decision. | Guild Tracker lifecycle analytics. | < 30 days for non-clinical, < 60 days for clinical. |
| **False Discovery Rate (FDR)** | Proportion of "successful" experiments (PSM met) that later exhibit degraded long-term metrics post-rollout (measured 30 days post-rollout vs. experiment period). | Difference-in-differences analysis of PSM & long-term KPI. | < 10%. Trigger for a full methodological review by DSRB. |
| **Guardrail Breach Rate** | Percentage of experiments terminated early due to a Guardrail Metric violation. | Monthly summary from Guild Tracker. | Monitored as a process health indicator; no specific threshold set. |
| **Rollback Duration** | Time from rollback decision (manual or automatic) to 100% traffic back on Control. | Splunk audit logs of router config changes and CLI commands. | < 60 seconds for automated, < 5 minutes for manual (during business hours). |

### 7.2 Dashboards and Observability

The following dashboards are mandatory sources of truth during any live experiment:

1.  **AIML-019 Experiment Live Dashboard (Grafana):**
    - **Folder:** `AI-Experiments`
    - **Primary Panels:** Real-time PSM progression, Guardrail metric charts with breach threshold lines, Variant Request Volume & Error Rate, p-value and Confidence Interval evolution, SRM p-value over time.
2.  **MLOps Router Service Dashboard (Datadog):**
    - Monitors the health of the serving infrastructure itself: router CPU/memory, model container resource usage, serving latency (p50, p95, p99), gRPC/HTTP error codes.
3.  **Guild Tracker Portfolio View:**
    - Management-level view showing all experiments by status (Design, Active, Closed), business unit, and risk classification.

### 7.3 Reporting Cadence

- **Weekly (Automated):** Guild Tracker sends a "Weekly Experiment Digest" email to the AI/ML Engineering team and key stakeholders, listing all newly activated, newly paused, and newly concluded experiments.
- **Monthly (Manual):** The AI/ML Platform team (RM lead) publishes a "Model Experimentation Health Report," analyzing the core KPIs and highlighting any policy violations or near-misses. This report is reviewed in the CAIO's monthly business review.
- **Quarterly (Manual):** A "Model Governance Quarterly Review" is presented to the Clinical Safety and Compliance Committee, summarizing all A/B and Canary activities on high-risk clinical models, including all safety-related guardrail breaches and their RCAs.

---

## 8. Exception Handling and Escalation

This section defines the process for granting an exception to any non-negotiable control in this SOP. An exception is defined as a temporary, documented deviation from a policy statement or mandatory procedure step.

### 8.1 Exception Request Process

1.  **Initiator:** The Experiment Owner files an *Experiment Exception Request* using the form `FRM-AIML-019-5` in ServiceNow. The form requires:
    - Reference to the specific SOP policy/procedure step to be excepted.
    - Business justification for why the exception is required.
    - Risk assessment of the deviation, including proposed compensating controls.
    - Expiration date for the exception (must not exceed 90 days).
2.  **Technical Review:** The RM reviews the technical and operational risk of the proposed compensating controls.
3.  **Business/Clinical Approval:**
    - **Standard ML Exception:** Approved by the CAIO.
    - **High-Risk Clinical ML Exception:** Co-approved by the CAIO and CSO.
    - **Financial Model Exception (>$1M ARR):** Co-approved by the CAIO and Chief Financial Officer (CFO).

### 8.2 Emergency Rollback Escalation

In the event that an automatic rollback fails or a rollback decision cannot be executed via normal tools:
1.  The **RM** invokes the "network isolation" runbook (`RUNBOOK-MLOPS-004`), which revokes network-level ingress permissions to the Treatment model's serving pods.
2.  The RM immediately declares a **SEV1 incident** in PagerDuty, which pages the VP of Engineering (David Park) and the CAIO.
3.  The SEV1 is then managed per the standard *Incident Management Procedure* (PROC-IT-101).

---

## 9. Training Requirements

Compliance with this SOP requires verifiable training. The role-based training matrix is as follows:

| Role(s) | Required Training | Frequency | Owner |
|---------|-------------------|-----------|-------|
| Experiment Owner (EO) | `TRAIN-AIML-019-1`: SOP Awareness & Guild Tracker Usage | Once, with annual refresher. | AI/ML Engineering L&D |
| Experiment Owner (EO) | **`TRAIN-AIML-019-2`: Advanced Statistical Experimental Design** | Once, with bi-annual recertification. | DSRB (VP of Biostatistics) |
| Release Manager (RM) | `TRAIN-AIML-019-3`: MLOps Router Operations & Terraform for Experiments | Once, with annual hands-on simulation. | AI/ML Platform Team Lead |
| DSRB Reviewer, CSO | `TRAIN-AIML-019-4`: Regulated Model Review & Safety Assessment | Once, with annual regulatory update briefing. | Legal & Compliance |

Training completion is tracked in the Workday Learning Management System (LMS). An experiment cannot be transitioned to "Active" if the EO and RM have expired certifications for their respective mandatory trainings. This gating is enforced programmatically via the Guild Tracker API.

---

## 10. Related Policies and References

### 10.1 Internal Policies and SOPs

| Identifier | Title |
|------------|-------|
| SOP-AIML-008 | Model CI/CD, Validation, and Pre-Deployment Testing |
| SOP-AIML-014 | Shadow Deployment and Latent Model Scoring |
| SOP-AIML-022 | Production Model Monitoring and Alerting |
| SOP-AIML-030 | Data and Model Versioning |
| SOP-RISK-001 | AI Risk Classification and EU AI Act Compliance Framework |
| SOP-DATA-011 | Data Retention and Archiving Policy |
| SOP-PRIV-005 | Patient Data De-identification and Pseudonymization |
| PROC-IT-101 | Major Incident Management Procedure |
| HR-POL-042 | Employee Corrective Action Policy |
| PROC-VEND-017 | Vendor Contract Breach Management Procedure |

### 10.2 External References

| Identifier | Title/Description |
|------------|-------------------|
| **EU AI Act, Reg 2024/1689** | Title III, Chapter 2 (Requirements for high-risk AI systems); Title IV (Transparency). |
| **NIST AI RMF 1.0** | NIST AI 100-1, especially Map, Measure, and Manage functions. |
| **ISO/IEC 42001:2023** | Artificial Intelligence — Management System. |
| **AICPA TSC 2022** | SOC 2 categories CC8.1 (Changes to infrastructure, data, and software), PI1.1 (Processing Integrity). |

---

## 11. Revision History

| Version | Date | Author | Summary of Changes |
|---|---|---|---|
| 1.0 | 2023-01-19 | J. Park (AI Eng) | Initial version. Focused on A/B testing for non-clinical models only. |
| 2.0 | 2023-09-15 | M. Rivera (CAIO) | Expanded scope to include clinical models and added CSO role. Introduced mandatory guardrails. |
| 3.0 | 2024-02-28 | L. Chen (MLOps) | Introduced Canary Release procedures and MLOps Router technical controls. Added ServiceNow integration. |
| 4.0 | 2024-06-10 | K. O'Malley (Legal) | Major revision to align with newly approved EU AI Act requirements. Added pre-registration mandate and enhanced audit trail requirements. |
| 4.1 | 2024-11-05 | A. Davis (DSRB) | Refined statistical procedures, added explicit SRM checks, mandated `meridian-ml.experiments` standard library. |
| 5.0 | 2025-05-12 | R. Evans (Platform) | Integrated Canary and A/B workflows into single, unified control plane. Switched to Guild Tracker as source of truth. |
| 5.1 | 2025-08-01 | A. Davis (DSRB) | Post-audit revision: clarified statistical power analysis requirements and MDE justification. |
| **5.2** | **2026-06-05** | **M. Rivera (CAIO)** | **Biennial full review. Updated to align with NIST AI RMF 1.0 MAP, MEASURE, and MANAGE functions. Clarified stakeholder feedback mechanisms.** |
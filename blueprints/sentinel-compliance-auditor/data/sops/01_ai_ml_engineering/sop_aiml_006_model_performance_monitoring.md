---
sop_id: "SOP-AIML-006"
title: "Model Performance Monitoring"
business_unit: "AI/ML Engineering"
version: "4.4"
effective_date: "2024-12-18"
last_reviewed: "2025-09-09"
next_review: "2026-03-13"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "SR 11-7"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: Model Performance Monitoring

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for the continuous monitoring of machine learning (ML) and artificial intelligence (AI) model performance across all business units at Meridian Health Technologies, Inc. The purpose of this framework is to ensure that all models deployed in production operate within their designated performance envelopes, maintain alignment with intended clinical and financial outcomes, and do not introduce undue risk to patients, customers, or the organization.

Post-deployment model behavior can diverge from expected benchmarks due to data drift, concept drift, adversarial inputs, system latency, or upstream data pipeline failures. A structured monitoring program is essential to detect these anomalies early, trigger appropriate remediation, and maintain compliance with internal governance standards and external regulatory obligations pertaining to high-risk AI systems and automated decision-making.

### 1.2 Scope

This SOP applies to the full lifecycle of the following model categories:

| Model Category | Business Unit | Regulatory Classification | Deployment Environment |
|---|---|---|---|
| Clinical AI/ML (Diagnostic Imaging, Risk Stratification) | Clinical AI (Office of the Chief Medical Officer) | High-Risk AI System; FDA 510(k) Cleared; CE Marked under EU MDR | Clinical Decision Support Platform (AWS eu-west-1, us-east-1) |
| Financial Risk Models (Credit scoring, claims propensity) | MedFin Solutions (Office of the CFO) | Automated Individual Decision-Making | Private Cloud (Azure, US East 2) |
| Operational AI (Triage bots, readmission predictors) | AI/ML Engineering | High-Risk AI System | Hybrid Cloud (GCP us-central1, on-premises) |
| Generative AI (Clinical summarization, member support copilots) | Emerging Tech & Innovation | General Purpose AI with High-Risk Application | GCP Vertex AI |
| Third-Party/Procured Models (e.g., NLP for document classification) | AI/ML Engineering, Vendor Management | High-Risk (subject to Meridian's quality system) | Vendor-hosted SaaS, or Meridian-managed container |

This SOP is binding on all FTEs, contractors, seconded consultants, and third-party vendors who design, develop, deploy, or maintain models on behalf of Meridian Health Technologies. It applies to models in Shadow Production, A/B Testing, and Full Production environments.

### 1.3 Out of Scope

- Pre-deployment model validation and acceptance testing (Refer to **SOP-AIML-003: Model Validation and Acceptance Testing**).
- Data quality monitoring in the feature store (Refer to **SOP-DE-008: Feature and Source Data Quality Monitoring**), unless data errors simulate model drift.
- Security monitoring for adversarial attacks on model endpoints (Refer to **SOP-SEC-017: AI Endpoint Security and Threat Modelling**), though performance degradation resulting from an attack is in scope.

---

## 2. Definitions and Acronyms

For the purposes of this document, the following definitions apply:

| Term / Acronym | Definition |
|---|---|
| **AUC-ROC** | Area Under the Receiver Operating Characteristic Curve. A metric measuring binary classifier separability. |
| **Data Drift** | A change in the statistical properties of the input features compared to the training or validation baseline. Measured via Population Stability Index (PSI) or Kullback-Leibler Divergence. |
| **Concept Drift** | A change in the statistical relationship between the model inputs and the target variable. The definition of a "correct" prediction shifts. |
| **Prediction Drift** | A change in the distribution of the model's output scores over time. |
| **F1 Score** | The harmonic mean of precision and recall. A primary metric for classification models with imbalanced classes. |
| **RMSE** | Root Mean Square Error. A primary metric for regression models. |
| **PSI** | Population Stability Index. A statistical measure of divergence between two distributions. Used for data and prediction drift. PSI < 0.10 indicates no shift; 0.10 <= PSI < 0.25 indicates moderate shift; PSI >= 0.25 indicates significant shift. |
| **MTTR** | Mean Time to Resolve. Time from alert trigger to operational closure. |
| **MTTD** | Mean Time to Detect. Time from a performance degradation event to the generation of an automated alert. |
| **Ground Truth Latency** | The time delay between serving a prediction and receiving the actual confirmed outcome (the "label"). |
| **Shadow Mode** | A model running in parallel with a production Champion model; its predictions are logged but not actioned. |
| **Champion-Challenger** | An operational paradigm in which a "Champion" model serves traffic, while one or more "Challenger" models are assessed on a percentage of live traffic or Shadow Mode logs. (This paradigm is used for A/B testing new model versions, but a formal Challenger Model governance policy for high-impact decisions is not currently in scope of this SOP.) |

---

## 5. Detailed Procedures

### 5.1 Model Onboarding and Baseline Registration

Before any model can be deployed as a production service or in shadow mode, it must be formally onboarded onto the Meridian Model Performance Monitor (MPM), which is implemented via the **Arize Observe** platform. No model shall be considered deployable without completing this onboarding.

1.  **Model Registry Entry:** The Model Owner must ensure the model is registered in the Meridian Model Registry (MLflow). The registry entry must include:
    *   Model ID, version, description, and business purpose.
    *   Owner (individual, not a team alias).
    *   Training dataset snapshot reference (Hashed S3 URI).
    *   Framework and dependencies (Docker image SHA).
2.  **Baseline Metric Capture:** The Model Owner must upload a JSON file containing the performance metrics obtained during the final Acceptance Test phase to the MPM.
3.  **Baseline Data Distribution:** The Model Owner must upload a reference schema and statistical profile of the training/reference data. This includes, for each feature:
    *   Data type.
    *   Mean, median, standard deviation (numerical).
    *   Cardinality, mode, frequency distribution (categorical).
    *   PSI binning strategy.
4.  **SLA Definition:** The Model Owner must define and propose Service Level Agreements (SLAs) for the model, including target latency (p99 in ms), and availability (99.99% for Clinical AI, 99.9% for others). These SLAs are subject to review by the VP of Engineering.
5.  **Dashboard Configuration:** The ML Operations (MLOps) team will create a dedicated model monitoring dashboard in Arize. The dashboard will contain panels for:
    *   Data Drift (features and predictions).
    *   Performance Metrics (compared to baseline and SLA thresholds).
    *   Traffic and latency.

### 5.2 Performance Metric Calculation

Model performance shall be evaluated on a configurable sliding time window. The standard windows are 1 hour, 24 hours, and 7 days. The MLOps team is responsible for ensuring the metric calculation pipeline is operational.

#### 5.2.1 Metrics by Model Type

The following metrics are mandatory and must be calculated where ground truth is available:

| Model Type | Primary Metrics | Secondary Metrics | Monitoring Type |
|---|---|---|---|
| Binary Classification (Clinical) | AUROC, Sensitivity (Recall), Specificity, Positive Predictive Value (Precision) | F1 Score, Brier Score (Calibration) | Ground-truth linked via Patient ID in the data warehouse. |
| Binary Classification (Financial) | AUROC, Precision-Recall AUC | Lift at 10%, Gain Chart | Ground-truth linked via Claim ID. |
| Multi-class Classification | Macro-Averaged F1 Score, Weighted F1 Score | Confusion Matrix Mosaic, Per-Class Recall | Ground-truth linked. |
| Regression | RMSE, Mean Absolute Error (MAE), R-squared | Prediction Error Distribution (histogram), error quantiles | Ground-truth linked. |
| NLP / Summarization | ROUGE-L (Summarization), BLEU/COMET (Translation), Token Error Rate | Semantic Similarity Score (via Ada-003 embeddings), Hallucination Rate | Ground-truth sourced from human review sampling (5% of traffic). |
| Ranking (RecSys) | Precision@k, Recall@k, Mean Reciprocal Rank (MRR) | Normalized Discounted Cumulative Gain (NDCG) | Ground-truth from click/interaction logs. |

#### 5.2.2 Handling Ground Truth Latency

For models where ground truth latency exceeds the standard 1-hour monitoring window (e.g., clinical outcomes taking 30-90 days), the model shall be monitored via Prediction Drift and Data Drift metrics in real-time. The MLOps team shall maintain a delayed-label pipeline that retroactively calculates performance metrics when labels are available. The MPM dashboard must display a "Label Status" gauge showing the date of the most recent complete label set.

### 5.3 Drift Detection Procedures

Drift is the primary indicator of silent model failure and is monitored continuously.

#### 5.3.1 Data Drift Monitoring

Data drift is calculated by comparing the distribution of input features in a current monitoring window (default: 24 hours) against the baseline training distribution.
*   **Algorithm:** Population Stability Index (PSI) is the primary algorithm. Jensen-Shannon Divergence (JSD) may be used for high-dimensional or textual embeddings.
*   **Feature Coverage:** The top 20 features by Shapley (SHAP) importance score, plus any features specifically mandated by the Model Owner during onboarding, must be monitored.
*   **Pipeline:** The Meridian Feature Store (Feast) triggers a Pub/Sub event for every new prediction request, including the final feature vector. The MLOps drift pipeline consumes this vector and updates the Arize dashboard.

#### 5.3.2 Prediction Drift Monitoring

Prediction drift is monitored by comparing the distribution of model output scores over the monitoring window against the baseline. PSI >= 0.2 triggers an alert. This is the primary monitoring methodology for models with long ground truth latency.

### 5.4 Alerting Thresholds and Configuration

Alerting is managed through PagerDuty, integrated using Arize webhooks. All thresholds are configured as code in the `meridian-ml/alerting-config` repository.

#### 5.4.1 Standard Threshold Matrix

| Alert Type | Severity Level | Threshold | Window | Action |
|---|---|---|---|---|
| Performance Drop | Critical | AUROC drops >0.05 absolute, or F1 drops >0.07 absolute | 24 hours | PagerDuty Page to MLOps On-Call and Model Owner |
| Performance Drop | Warning | AUROC drops >0.03 absolute, or F1 drops >0.04 absolute | 24 hours | ServiceNow Ticket (Priority P2), Slack alert to #ml-model-support |
| Significant Data Drift | Critical | PSI >= 0.25 for any top-5 SHAP feature | 1 hour | PagerDuty Page, automatic rollout freeze |
| Significant Data Drift | Warning | PSI >= 0.18 for any top-5 SHAP feature | 24 hours | ServiceNow Ticket (Priority P3), Slack alert |
| Prediction Drift | Critical | PSI >= 0.30 on prediction distribution | 1 hour | PagerDuty Page |
| Traffic Zero | Critical | 0 predictions in a 5-minute rolling window for an active model | 5 minutes | PagerDuty Page to SRE (primary), MLOps (secondary) |
| Latency SLA Breach | Warning | p99 latency exceeds SLA benchmark for >10% of requests in 1 hour | 1 hour | ServiceNow Ticket (Priority P3), Slack alert |
| Feature Missing Rate | Critical | A top-5 feature has >20% null/coerced default values | 24 hours | PagerDuty Page |

### 5.5 Degradation Response Playbook

When a Critical severity alert is triggered, the following incident response procedure is initiated. All steps must be logged in the Incident Channel (#incident-model-performance) on Slack and the resulting post-mortem document.

1.  **Triage (0-15 minutes):** The primary MLOps Engineer acknowledges the PagerDuty alert. They log into the Arize dashboard and verify the alert is not a false positive caused by a telemetry pipeline error. They identify the failing model and metric.
2.  **Communication (15-20 minutes):** If the alert is valid, the engineer declares a "Model Performance Incident" via the `/incident declare` OpsGenie command. This broadcasts a notification to the Model Owner, the AI/ML Engineering Director, and the product manager.
3.  **Mitigation (20-60 minutes):** The Model Owner, in consultation with the MLOps engineer, implements an immediate mitigation:
    *   **Rollback:** If the degradation correlates with a recent deployment, the model version is rolled back to the previous stable version using the standard CI/CD pipeline.
    *   **Traffic Shunt:** If rollback is not feasible, a traffic rule is deployed to shunt a portion of traffic to a heuristic or rule-based fallback system. For clinical models, this may involve a "Model Non-Predictive" workflow fallback, directing the user to seek alternative clinical decision support.
    *   **Feature Off:** The MLOps engineer can toggle the model off via the LaunchDarkly feature flag `[model-id]-active`, reverting the system to its non-automated baseline.
4.  **Root Cause Analysis, RCA (60 minutes - 48 hours):** The Model Owner leads a deep dive. This includes analyzing upstream data pipeline failures (checking DataDog logs for Kafka lag or feature store errors), evaluating incoming data for semantic anomalies, and testing the existing model endpoint against a holdout validation set.
5.  **Closure and Post-Mortem (72 hours):** A blameless post-mortem is drafted in Confluence using the `Model Incident Post-Mortem Template` and shared with all stakeholders.

---

## 6. Controls and Safeguards

### 6.1 Automated Rollback Gates

The CI/CD pipeline (Jenkins X) that deploys a new model version or updates model artifacts is gated by a 60-minute "bake" period under shadow traffic. If, during this bake period, an automated monitor detects a Critical performance drop or significant prediction drift compared to the stable production version, the pipeline automatically halts and triggers an alert. Promotion to the full production serving environment requires a manual approval step by the Model Owner and an MLOps engineer.

### 6.2 Ground Truth Validation Pipelines

For all high-risk classification models, a dedicated Airflow DAG (`gt_validator_[model_id]`) runs daily. This pipeline independently re-materializes the serving feature set from the raw data lake and calculates performance metrics. The results are cross-referenced with the Arize-reported metrics. A discrepancy of >2% in any primary metric triggers a Warning alert to diagnose a potential calculation discrepancy in the monitoring platform.

### 6.3 Infrastructure and Compute Monitoring

The MLOps team maintains a supplementary Grafana dashboard (not a replacement for Arize) for infrastructure health. Controls include:
- **GPU Utilization:** Models requiring accelerators shall not exceed 80% sustained utilization without an automated capacity adjustment ticket being filed.
- **Endpoint Response:** Health check probes on the Triton Inference Server endpoint are executed at 15-second intervals. Three consecutive failed probes trigger a force restart of the container orchestration (Kubernetes Operator).

### 6.4 Access Control

Access to individual model dashboards in Arize is granted according to the principle of least privilege. Model Owners have read-only access to dashboards of other teams' models unless explicit cross-functional permissions are granted via the Okta integration. Write access to alerting thresholds is restricted to the MLOps Core team and the Director of AI/ML Engineering.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs) for the Monitoring Program

The health of the Model Performance Monitoring program itself is measured against a set of operational KPIs. The AI/ML Engineering Director reviews these metrics monthly.

| KPI Category | KPI Name | Measurement Methodology | Target |
|---|---|---|---|
| Detection Responsiveness | Mean Time to Detect (MTTD) | Average time from when a metric crosses a Critical threshold to a PagerDuty alert being generated. Calculated daily. | < 5 minutes |
| Response Responsiveness | Mean Time to Resolve (MTTR) | Average time from PagerDuty alert to service restoration (rollback, fallback, or fix). Calculated per incident. | < 45 minutes |
| Alert Hygiene | Alert-to-Signal Ratio | The ratio of valid, actionable alerts to total alerts. Includes false positive events from telemetry glitches. | > 80% (1 false positive per 5 real) |
| Coverage | Model Monitoring Coverage | Percentage of production models (by traffic volume) with complete Arize dashboards and active alerts. | 100% for Clinical/Financial, 99% for Operational |
| Post-Incident Follow-Through | RCA Timeliness | Percentage of Critical incidents with a published post-mortem document within 72 hours of incident closure. | 97% |

### 7.2 Reporting Cadence

A formal Model Health Report is produced by the MLOps Lead, comprising aggregated statistics from Arize and manual summaries of Critical incidents and post-mortem findings.

| Report Level | Recipients | Cadence | Content |
|---|---|---|---|
| Operational Snapshot | MLOps Engineers, Model Owners | Weekly (automated email) | Top 10 models by drift, open ServiceNow tickets, alert volume summary. |
| Program Health Review | Director of AI/ML, VP of Engineering, Product VPs | Monthly (presentation) | KPI trend analysis, MTTR/MTTD review, significant drift events, model sunsetting candidates. |
| Executive Summary | Chief AI Officer, Chief Medical Officer, CFO | Quarterly (formal document) | Aggregate program health, key risks and remediation efforts, regulatory posture summary, key transparency artifacts related to AI operations for external stakeholder review. |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Requests

Situations may arise where a model's performance is intentionally allowed to drift, or monitoring thresholds must be temporarily adjusted. These are not normal operational events and require a formal, documented exception. A Model Owner must submit an exception request via the ServiceNow `Model Monitoring Exception` catalog item, providing a compelling justification and a risk analysis.

**Standard Exception Categories:**
- **Periodic Drift (Seasonality):** A model exhibiting known, periodic drift (e.g., respiratory illness prediction models spiking in winter). The exception must define the time-bound period and the adjusted thresholds. The VP of Engineering must approve.
- **Data Source Migration:** During a planned, time-bound migration of an upstream data system, a model may exhibit elevated data drift. A temporary "watch-only" (alert suppression) period, not exceeding 72 hours, can be granted by the Director of AI/ML.
- **Ground Truth Corruption:** If the ground truth data pipeline is confirmed to be corrupted, performance metric alerting may be suppressed for the duration of the fix. This requires approval from the VP of Engineering and the VP of Data Platform.

### 8.2 Escalation for Unresolved Degradation

If a model's primary Critical performance metric remains consistently below the baseline threshold for a period exceeding 7 days, and no viable remediation (retraining, rollback, etc.) has been successful, the issue is escalated from the Model Owner to the VP of Engineering. A formal "Model Remediation or Sunset Review" meeting is triggered with the product manager. The outcome must be a binding decision to:
1.  Allocate new engineering resources for a redesign.
2.  Replace the model with a heuristic.
3.  Formally sunset the model functionality.

---

## 9. Training Requirements

All personnel associated with the AI/ML lifecycle are required to complete role-specific training on Model Performance Monitoring principles and tooling. Training records are tracked in the Workday Learning Management System.

| Role | Required Training Module(s) | Frequency | Assessment |
|---|---|---|---|
| Model Owner (Data Scientist/ML Engineer) | `MPM-101: Model Monitoring Theory & Drift`, `MPM-102: Arize Dashboard and Alerting for Owners` | Annually | Passing grade (80%) on MPM-102 quiz |
| MLOps Engineer | `MPM-201: Advanced Alerting Configuration`, `MPM-202: Degradation Response Playbook Drill`, `MPM-210: Monitoring Infrastructure` | Bi-annually | Practical Simulation Exercise (passed/failed) |
| AI/ML SRE | Same as MLOps Engineer, plus `SRE-301: Incident Command for AI Services` | Annually | 3-hour live-fire tabletop exercise |
| Medical/Financial Auditor | `MPM-101` (abridged, non-technical) | Annually | Attestation of completion |
| Product Manager | `MPM-001: AI Model Lifecycle for Product Managers` | Annually | None |

### 9.1 Playbook Drill Requirements

The MLOps team will conduct a failure injection drill once per quarter in the staging environment. The drill shall simulate a realistic model degradation scenario (e.g., extreme drift, endpoint latency spike). All on-call engineers must respond according to Section 5.5 of this SOP. A drill report is published and reviewed by the Director of AI/ML.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP-ID | Document Title | Relevance |
|---|---|---|
| **SOP-AIML-001** | AI/ML Model Lifecycle Management | Overarching governance for model stages (Develop, Validate, Deploy, Monitor, Retire). |
| **SOP-AIML-003** | Model Validation and Acceptance Testing | Pre-deployment performance criteria and baseline derivation. |
| **SOP-AIML-005** | Model Explainability and Transparency | Requirements for generating SHAP values and user-facing explanations, which inform drift analysis. |
| **SOP-DE-008** | Feature and Source Data Quality Monitoring | Procedures for monitoring data quality upstream of model inference, which is a primary trigger for data drift. |
| **SOP-SEC-017** | AI Endpoint Security and Threat Modelling | Procedures for hardening model endpoints, detecting adversarial input patterns, and managing security-related performance impacts. |
| **SOP-DP-004** | Data Retention and Archival | Policy governing the retention period of model prediction and ground truth logs (currently 7 years). |
| **SOP-QA-009** | Corrective and Preventive Action (CAPA) | Procedure for managing systemic issues identified during a monitoring root cause analysis, triggering process-wide changes. |

### 10.2 External Standards and Regulatory References

- **ISO/IEC 42001:2023** — Information technology — Artificial intelligence — Management system. Used as the reference framework for our AI Management System.
- **NIST AI 100-1** — Artificial Intelligence Risk Management Framework (AI RMF 1.0). Guiding document for risk-based performance governance.
- **21 CFR Part 820** — Quality System Regulation (for FDA-cleared clinical models).

---

## 11. Revision History

| Version | Date | Author | Approver | Description of Change |
|---|---|---|---|---|
| 1.0 | 2021-06-14 | J. Park | M. Kapoor | Initial Draft. Separated performance monitoring from model validation. Basic alerting structure. |
| 2.0 | 2022-11-08 | L. Chen | D. Park | Major revision. Introduced Arize platform. Formalized PSI thresholds, added Ground Truth Latency handling, and detailed playbook. |
| 3.1 | 2023-08-22 | L. Chen | D. Park | Posture update for EU MDR deployment. Added SLA targets for clinical models, new hallucination metric for NLP. |
| 3.4 | 2024-02-29 | R. Singh | M. Rivera | Expanded scope to include Shadow Mode monitoring, introduced Automated Rollback Gates in Section 6.1. Updated on-call rotation schema. |
| 4.1 | 2024-09-20 | M. O'Connor | D. Park | Complete rewrite of Section 5 (Procedures) to reflect CI/CD migration. Added Champion-Challenger references. Updated all alerting thresholds. |
| 4.4 | 2024-12-18 | M. O'Connor | D. Park | Quarterly Review. Refined KPIs in Section 7.1, added formalized exception request process in ServiceNow. Clarified RACI for new Emerging Tech models. |
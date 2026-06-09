---
sop_id: "SOP-AIML-007"
title: "Model Retraining and Continuous Learning"
business_unit: "AI/ML Engineering"
version: "3.8"
effective_date: "2024-05-17"
last_reviewed: "2025-10-09"
next_review: "2026-04-01"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "SR 11-7"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: Model Retraining and Continuous Learning

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for managing the lifecycle of machine learning models subsequent to their initial deployment at Meridian Health Technologies, Inc. The purpose is to ensure that all AI/ML models operating in production environments maintain their predictive performance, safety profile, fairness characteristics, and regulatory compliance posture over time through structured retraining, continuous learning protocols, and rigorous validation gates.

This SOP defines the triggers that initiate retraining activities, the data freshness requirements for training datasets, the validation and approval chain required before a retrained model can be promoted to production, and the rollback procedures to revert to a prior stable state in the event of performance degradation or operational failure.

### 1.2 Scope
This SOP applies to all machine learning models, deep neural networks, natural language processing systems, and statistical algorithms developed or procured by Meridian Health Technologies that are deployed in production environments supporting any of the four business lines:

| Business Line | In-Scope Models | Risk Classification |
|---|---|---|
| Clinical AI Platform | Diagnostic imaging models, patient risk scoring, adverse event prediction, clinical decision support algorithms | High-Risk AI (EU AI Act Annex III) |
| HealthPay Financial Services | Credit scoring, fraud detection, claims adjudication, medical lending underwriting, payment anomaly detection | Model Risk (SR 11-7) |
| MedInsight Analytics | Care gap identification, population risk stratification, outcomes prediction, readmission forecasting | PHI-Handling Systems |
| Meridian SaaS Platform | Infrastructure-level auto-scaling prediction, anomaly detection, intelligent routing, resource optimization | Operational Models |

**In-Scope Activities:**
- Scheduled periodic retraining on refreshed datasets
- Trigger-based retraining in response to detected drift or degradation
- Continuous learning through online parameter updates
- Shadow deployment and A/B testing of retrained models
- Model validation and approval gates
- Production promotion and rollback procedures

**Out of Scope:**
- Initial model development and first deployment (see SOP-AIML-002)
- Model decommissioning and archival (see SOP-AIML-011)
- Third-party vendor model management (see SOP-VEND-005)
- Infrastructure model retraining for the SaaS platform (see SOP-ITOPS-014)

### 1.3 Target Audience
- AI/ML Engineering teams
- MLOps and Platform Engineering
- Clinical AI Product teams
- Financial Services quantitative analytics teams
- Model Validation personnel
- Data Governance stewards
- Quality Assurance engineers
- Compliance and Regulatory Affairs

---

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
|---|---|
| **AUC-ROC** | Area Under the Receiver Operating Characteristic curve; primary binary classification performance metric |
| **Concept Drift** | Change in the statistical relationship between model inputs and target outputs over time |
| **Continuous Learning** | Automated, incremental parameter updates to a deployed model without full retraining |
| **DAG** | Directed Acyclic Graph; workflow orchestration structure used in Kubeflow pipelines |
| **Data Drift** | Change in the statistical distribution of input features over time relative to the training baseline |
| **Data Freshness Window** | Maximum permissible age of training data relative to the retraining execution date |
| **Drift Detection** | Automated statistical testing to identify data drift and concept drift against established baselines |
| **Feature Store** | Centralized repository (Feast on AWS RDS) for curated and documented feature definitions |
| **KPI** | Key Performance Indicator |
| **Label Drift** | Shift in the distribution of ground-truth labels over time |
| **MRE** | Model Risk Evaluation; quantitative assessment protocol defined in SOP-AIML-004 |
| **MTTD** | Mean Time to Detect; average time from drift onset to automated alert generation |
| **MTTR** | Mean Time to Respond; average time from drift alert to resolution (rollback or new model promotion) |
| **PR-AUC** | Precision-Recall Area Under the Curve; primary metric for imbalanced classification problems |
| **Retraining Pipeline** | Automated Kubeflow DAG that executes data extraction, feature engineering, training, and evaluation |
| **Shadow Deployment** | Parallel deployment of a candidate model receiving production traffic without affecting outcomes |
| **Staleness Threshold** | Maximum permissible time since last retraining before a model is flagged for mandatory review |

---

## 3. Roles and Responsibilities

The following RACI matrix assigns accountability for each phase of the model retraining lifecycle:

| Activity | AI/ML Engineering | MLOps Team | Model Validation | Business Unit Owner | Data Governance | Compliance | CISO |
|---|---|---|---|---|---|---|---|
| Drift monitoring configuration | R | A | C | I | I | I | I |
| Retraining trigger approval | C | C | I | A | I | I | I |
| Training data certification | I | I | I | C | A, R | I | I |
| Retraining pipeline execution | R | A | I | I | I | I | I |
| Validation testing execution | R | C | A | I | I | I | I |
| Fairness assessment | R | I | A | C | I | C | I |
| Production promotion approval | I | C | A | R | I | C | I |
| Rollback execution | I | A, R | I | C | I | I | I |
| Incident response coordination | C | R | I | A | I | R | I |

**Specific Role Assignments:**

| Role | Named Individual / Team |
|---|---|
| Chief AI Officer (SOP Owner) | Dr. Marcus Rivera |
| VP of Engineering (Approver) | David Park |
| Head of MLOps | Sarah Chen |
| Lead Model Validation | Dr. James Okonkwo |
| Director of Data Governance | Maria Fernandez |
| Clinical AI Safety Officer | Dr. Priya Nair |
| Financial Model Risk Officer | Jonathan Weiss |
| Compliance Officer – AI Systems | Rebecca Thornton |

---

## 4. Policy Statements

### 4.1 General Principles
**PS-001:** All production AI/ML models shall be subject to continuous monitoring and shall be retrained when predefined performance thresholds are breached or when data staleness exceeds established limits.

**PS-002:** No retrained model shall be promoted to production without successfully passing the Model Validation Gate as defined in Section 5.6.

**PS-003:** A rollback plan and a stable prior model version shall be maintained and kept deployable for every production model at all times.

**PS-004:** All retraining and continuous learning activities shall be auditable, with complete traceability from training data through to production deployment.

**PS-005:** Retraining frequency shall be risk-calibrated: high-risk models (Clinical AI Platform, HealthPay credit models) shall be subject to more stringent data freshness requirements and mandatory periodic retraining.

### 4.2 Data Governance
**PS-006:** All data used for retraining shall be certified by the Data Governance team as compliant with data lineage, consent management, and data quality requirements per SOP-DATA-003.

**PS-007:** Training datasets shall not contain production inference data logged more recently than the Data Freshness Window defined in Section 5.3.

### 4.3 Regulatory Compliance
**PS-008:** Retraining activities for Clinical AI Platform models shall generate documentation addressing EU AI Act requirements for ongoing conformity.

**PS-009:** Retraining activities for HealthPay models shall follow model risk management practices per SR 11-7, with model documentation maintained to support independent review.

**PS-010:** All retraining processes shall align with NIST AI RMF 1.0 practices as detailed in the Controls and Safeguards section of this SOP.

### 4.4 Continuous Learning Governance
**PS-011:** Continuous learning (online parameter updates) is permitted only for non-high-risk models and requires prior written approval from the Model Validation team.

**PS-012:** Any model undergoing continuous learning shall be subject to guardrail constraints that limit the magnitude of parameter updates per batch and per 24-hour period.

---

## 5. Detailed Procedures

### 5.1 Retraining Triggers

Retraining can be initiated through any of the following trigger mechanisms. All triggers generate an automated ticket in Jira Service Management with the `model-retraining` issue type and are routed to the owning AI/ML Engineering squad.

#### 5.1.1 Scheduled Periodic Retraining

| Model Tier | Maximum Retraining Interval | Data Freshness Window | Applicable Models |
|---|---|---|---|
| Tier 1 (Critical) | 30 calendar days | 14 days | Clinical diagnostic, Credit scoring |
| Tier 2 (High) | 60 calendar days | 30 days | Risk prediction, Fraud detection |
| Tier 3 (Standard) | 90 calendar days | 45 days | Readmission prediction, Care gap |
| Tier 4 (Operational) | 180 calendar days | 90 days | Infrastructure auto-scaling |

The MLOps platform (Meridian Model Registry, built on MLflow) automatically calculates the Staleness Threshold based on the last successful retraining completion timestamp and the Maximum Retraining Interval. When a model's staleness exceeds 80% of the Maximum Retraining Interval, an early-warning notification is dispatched to the model owner. At 95%, an escalation notification is sent to the Business Unit Owner.

#### 5.1.2 Drift-Based Triggers

Drift detection runs continuously on production inference logs using the Meridian Drift Monitor (Evidently AI deployed on AWS EKS). The following thresholds shall trigger automatic retraining ticket generation:

| Drift Metric | Trigger Threshold | Measurement Window |
|---|---|---|
| Data Drift (Population Stability Index) | PSI > 0.25 | 7-day rolling window |
| Data Drift (Kolmogorov-Smirnov p-value) | p < 0.01 on any top-10 feature | 7-day rolling window |
| Concept Drift (Proxy: AUC-ROC degradation) | ΔAUC < -0.05 from baseline | 14-day rolling window |
| Concept Drift (Proxy: PR-AUC degradation) | ΔPR-AUC < -0.05 from baseline | 14-day rolling window |
| Label Drift (Chi-squared p-value) | p < 0.01 | 30-day rolling window |
| Prediction Distribution Shift | KL Divergence > 0.15 | 7-day rolling window |

When a drift-based trigger fires, the Jira ticket is automatically assigned a priority level:

- **P1 (Critical):** Any Tier 1 model drift + performance degradation exceeding 10%
- **P2 (High):** Tier 1 or Tier 2 model drift with any performance degradation
- **P3 (Medium):** Tier 3 model drift with any performance degradation
- **P4 (Low):** Drift detected but no measured performance degradation

**P1 tickets require acknowledgment within 2 hours and resolution within 24 hours.**
**P2 tickets require acknowledgment within 4 hours and resolution within 5 business days.**

#### 5.1.3 Performance-Based Triggers

Automated performance evaluation against holdout datasets (maintained per Section 5.3.2) runs weekly. If any of the following conditions are met, a retraining ticket is generated:

| Model Type | Metric | Degradation Threshold | Holdout Dataset |
|---|---|---|---|
| Binary Classification | AUC-ROC | < 0.80 (absolute) or -0.10 from baseline | Temporal holdout, most recent 30 days |
| Binary Classification (imbalanced) | PR-AUC | < 0.60 (absolute) or -0.15 from baseline | Temporal holdout, most recent 30 days |
| Regression | Root Mean Square Error (RMSE) | +20% from baseline | Temporal holdout, most recent 30 days |
| Multi-class Classification | Weighted F1 Score | -0.10 from baseline | Temporal holdout, most recent 30 days |
| Ranking | Normalized Discounted Cumulative Gain (NDCG@10) | -0.08 from baseline | Temporal holdout, most recent 30 days |

#### 5.1.4 Manual Trigger

Model owners, Business Unit Owners, or Model Validation may initiate retraining by submitting a `model-retraining-manual` Jira request. Manual retraining must include a written justification citing one or more of the following approved reasons:
- Upstream data schema change
- New feature availability with demonstrated predictive value
- Regulatory or policy change affecting model use context
- Security vulnerability in dependencies of the current model artifact
- Results from an adverse event investigation or audit finding

Manual triggers for Tier 1 and Tier 2 models require VP-level approval from the relevant business unit.

#### 5.1.5 Continuous Learning Triggers

For models approved for continuous learning (non-high-risk Tier 3 or Tier 4 only, with written Model Validation approval), online updates are triggered under the following conditions:

| Parameter | Permitted Range |
|---|---|
| Minimum samples accumulated before update | 10,000 inference records |
| Maximum update frequency | Once per 24 hours |
| Maximum parameter delta norm (L2) | 0.05 |
| Minimum batch accuracy vs. current model | ≥ 98% of current model |

Continuous learning updates are logged in the Model Registry as minor version increments (e.g., v2.3 → v2.4) with full traceability to the batch of samples used.

### 5.2 Retraining Data Pipeline

#### 5.2.1 Data Source Configuration

All retraining data sources must be registered in the Meridian Feature Store (Feast on AWS RDS) and in the Data Catalog (Alation). The following data source types are permitted for retraining:

| Source Type | Certification Required | Retention for Audit |
|---|---|---|
| Production Feature Store (online) | Automated lineage check | 7 years |
| Offline Feature Store (batch) | Data Governance certification within last 90 days | 7 years |
| Ground Truth / Labeling Pipeline | Human-in-the-loop QA audit (SOP-DATA-005) | 7 years |
| Clinical Data Warehouse (Epic Clarity) | IRB-approved data use agreement + DPO review | 10 years |
| Claims Data Lake (Snowflake) | Data Governance certification + access review | 10 years |
| Transaction Log (HealthPay) | Financial data quality check (SOP-FIN-004) | 7 years |

#### 5.2.2 Dataset Assembly

The Retraining Pipeline DAG (Kubeflow, defined in `kfp/retraining/pipeline_v3.yaml`) executes the following steps:

1. **Data Extraction:** Query the Feature Store for the registered feature set of the target model, limited to the Data Freshness Window period plus a 30-day buffer to ensure temporal coverage. Extraction queries are immutable and logged.
2. **Data Quality Screening (Great Expectations Suite):**
   - Null rate per feature must not exceed 5% (Tier 1: 2%)
   - Feature distributions must pass Kolmogorov-Smirnov test against baseline at p > 0.05 for Tier 1 models
   - Outlier detection via Isolation Forest with manual review for Tier 1 models
   - Completeness: At least 95% of expected records present
3. **Label Validation:** Ground-truth labels are validated against source systems. For clinical models, labels must reconcile with Epic Clarity within a 30-day reconciliation window. For financial models, labels must reconcile with the General Ledger within 7 days.
4. **Train/Validation/Test Split Configuration:**
   - **Training set:** 70% of eligible data
   - **Validation set:** 15% of eligible data, stratified to preserve class balance
   - **Test set:** 15% of eligible data, temporally posterior to training and validation data
5. **Feature Engineering:** All transformations executed identically to the production pipeline, validated via hash comparison on 1,000 randomly sampled records.
6. **Bias and Fairness Pre-Screening:** Execute the Meridian Fairness Toolkit (Aequitas integration) on assembled features against protected attributes per SOP-FAIR-001. Flag any demographic parity violation exceeding 15% for review.

#### 5.2.3 Data Freshness Compliance

The Data Freshness Window is enforced programmatically in the data extraction step. Records with `event_timestamp` or equivalent outside the window are excluded. The pipeline logs the number and percentage of records excluded for freshness violations. If the remaining dataset size is below the minimum sample threshold (defined per model in the Model Registry), the pipeline halts with a `FRESHNESS_FAIL` status and notifies the Data Governance team and Model Owner.

| Tier | Minimum Retraining Samples |
|---|---|
| Tier 1 | 500,000 |
| Tier 2 | 200,000 |
| Tier 3 | 50,000 |
| Tier 4 | 10,000 |

### 5.3 Model Training Execution

#### 5.3.1 Training Environment

All retraining shall be executed on the Meridian AI Platform (AWS SageMaker on GovCloud for Clinical models; AWS SageMaker on standard commercial cloud for all other models) in a dedicated training environment that is logically isolated from production inference environments. Training jobs are logged with the following metadata tags:

- `sop_id: SOP-AIML-007`
- `model_id`: (from Model Registry)
- `version`: (candidate version, e.g., `v3.9-candidate`)
- `trigger_type`: (`scheduled`, `drift`, `performance`, `manual`, `continuous_learning`)
- `parent_version`: (the current production version being superseded)
- `training_data_hash`: SHA-256 of the combined training dataset
- `pipeline_run_id`: unique execution identifier

#### 5.3.2 Training Configuration

Retraining shall, unless otherwise documented in a Model Retraining Exception Request (MRER, Form AIML-007-MRER-01), use the identical model architecture, hyperparameter ranges, and training methodology as the current production model. Any modification to architecture or hyperparameters constitutes a Model Change Request and requires separate approval under SOP-AIML-004.

**Hyperparameter Tuning Restriction:** Automated hyperparameter search (grid, random, Bayesian) is permitted during retraining only for Tier 3 and Tier 4 models. For Tier 1 and Tier 2 models, hyperparameters are locked to the production configuration unless a Model Change Request is approved.

#### 5.3.3 Training Logging

The following training metadata shall be captured and stored in the Model Registry:

| Metadata Attribute | Description | Required Tier |
|---|---|---|
| Training completion timestamp | UTC timestamp | All |
| Training dataset hash | SHA-256 | All |
| Feature list and versions | From Feature Store | All |
| Hyperparameter set | Complete JSON | All |
| Training hardware configuration | Instance type, GPU count | All |
| Package dependency manifest | `requirements.txt` or Conda environment YAML, fully pinned | All |
| Convergence metrics | Loss curves per epoch | Tier 1, Tier 2 |
| Gradient norm statistics | Per-layer, training final epoch | Tier 1 |
| Carbon footprint estimate | Using CodeCarbon; reported in kg CO2e | All |

### 5.4 Validation Testing After Retraining

This section defines the comprehensive suite of tests that a retrained candidate model must pass before it can proceed to the Model Validation Gate.

#### 5.4.1 Performance Validation

The candidate model's performance metrics must meet the following criteria against the temporal holdout test set:

| Metric | Threshold | Comparison |
|---|---|---|
| AUC-ROC / PR-AUC / RMSE | Must meet or exceed the current production model's performance | Side-by-side on identical test set |
| Statistical significance (DeLong test for AUC; paired t-test for RMSE) | p < 0.05 for any claimed improvement; non-inferiority margin test for equivalence (Δ < 0.02) | Candidate vs. Production |
| Subgroup performance | Maximum 5% degradation on any demographic subgroup vs. production model | Stratified evaluation per SOP-FAIR-001 |
| Calibration (Expected Calibration Error, ECE) | ECE ≤ 0.08 for classification models | Brier score decomposition |

#### 5.4.2 Robustness Testing

| Test | Description | Passing Criteria |
|---|---|---|
| Gaussian noise injection | Add ε ~ N(0, σ²) to 10% of features, where σ = 0.1 × feature std dev | Performance degradation ≤ 2% |
| Missing feature simulation | For top-5 features by importance, set 5% of records to NULL | Prediction distribution shift ≤ 5% (KL) |
| Adversarial perturbation (Tier 1 only) | Fast Gradient Sign Method (FGSM) attack with ε = 0.01 | AUC-ROC ≥ 0.75 after perturbation |
| Edge case performance | Evaluate on subset with feature values in the 1st and 99th percentile | No catastrophic prediction failures (defined as > 5 × mean absolute residual) |

#### 5.4.3 Fairness and Bias Assessment

All candidate models must pass the Meridian Fairness Assessment Protocol:

| Fairness Metric | Threshold | Reference |
|---|---|---|
| Demographic parity difference | ≤ 0.10 | Between protected and reference groups |
| Equalized odds difference | ≤ 0.08 | Between protected and reference groups |
| Disparate impact ratio | ≥ 0.80 | Per EEOC Uniform Guidelines threshold |
| Counterfactual fairness (Tier 1) | ≤ 5% prediction change when protected attribute is flipped | Causal model variant |

Results are recorded in the Fairness Assessment Report (Form AIML-007-FAIR-01) and stored in the Model Registry as an artifact linked to the candidate model version.

#### 5.4.4 Shadow Deployment Evaluation

For Tier 1 and Tier 2 candidate models, a shadow deployment phase is mandatory:

| Parameter | Requirement |
|---|---|
| Shadow duration | Minimum 14 calendar days |
| Traffic shadowed | 100% of production inference volume |
| Logging | All shadow predictions logged to `s3://meridian-model-shadow/` bucket |
| Comparison | Daily automated comparison of shadow predictions vs. production predictions; alert if prediction discrepancy > 8% for any single feature subgroup |

Shadow deployment is executed by the MLOps team using the Meridian Shadow Router (API Gateway with traffic mirroring rules). The shadow environment is provisioned with identical compute resources as the production inference endpoint.

### 5.5 Model Validation Gate

The Model Validation Gate is the structured review checkpoint through which all retrained models must pass prior to production promotion. The gate is documented using the Model Validation Report (MVR, Template AIML-007-MVR-01).

#### 5.5.1 Gate Components

| Gate Component | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|---|---|---|---|---|
| Performance validation review | Required | Required | Required | Required |
| Robustness testing review | Required | Required | Optional | N/A |
| Fairness assessment review | Required, with Legal sign-off | Required | Required | N/A |
| Shadow deployment results review | Required | Required | Recommended | N/A |
| Clinical safety review (Clinical AI only) | Required, with Clinical AI Safety Officer sign-off | Required | N/A | N/A |
| Financial soundness review (HealthPay only) | Required, with Financial Model Risk Officer sign-off | Required | N/A | N/A |
| Data lineage attestation | Required | Required | Required | Required |
| Dependency vulnerability scan | Required | Required | Required | Required |
| Documentation completeness check | Required | Required | Recommended | N/A |

#### 5.5.2 Approval Authorities

| Model Tier | Required Approvals |
|---|---|
| Tier 1 (Critical) | (1) Lead Model Validation, (2) Business Unit Owner, (3) Clinical AI Safety Officer or Financial Model Risk Officer (as applicable), (4) Chief AI Officer or designee |
| Tier 2 (High) | (1) Lead Model Validation, (2) Business Unit Owner |
| Tier 3 (Standard) | (1) Model Validation team member (senior or above), (2) Model Owner |
| Tier 4 (Operational) | (1) Model Owner |

All approvals are recorded in the Model Registry as immutable approval events linked to the candidate model version.

### 5.6 Production Promotion

Upon successful completion of the Model Validation Gate, the following promotion steps are executed:

| Step | Responsible | Timeline |
|---|---|---|
| 1. Candidate model registry status set to `validated` | Model Validation | Within 24 hours of final approval |
| 2. Production deployment canary (10% traffic, 4-hour bake) | MLOps | Scheduled within next maintenance window (Wed 02:00-06:00 UTC) |
| 3. Canary health check: Error rate < 0.1%, latency p99 < 200% of production baseline, prediction distribution within KL divergence < 0.05 of shadow | MLOps | Monitored for 4 hours |
| 4. Full traffic cutover (blue/green deployment) | MLOps | Upon canary health check pass |
| 5. Production model version tag set to `production` in Model Registry; prior version tagged `production-rollback-target` | MLOps | Immediately after cutover |
| 6. Notification to model stakeholders (Slack channel #model-deployments, email to model-owners@meridian.com) | MLOps | Within 1 hour of promotion |
| 7. 72-hour post-deployment monitoring intensification | MLOps, AI/ML Engineering | 72 continuous hours |

### 5.7 Rollback Procedures

#### 5.7.1 Rollback Triggers

A rollback to the prior stable model version shall be initiated when any of the following conditions is met following a promotion:

| Condition | Threshold | Detection Mechanism |
|---|---|---|
| Inference error rate | > 1.0% (Tier 1: > 0.1%) | Datadog APM monitors |
| Prediction distribution shift | KL divergence > 0.30 from pre-promotion baseline | Automated daily comparison |
| Latency violation | p99 latency > 1000ms (Tier 1: > 500ms) | AWS CloudWatch alarms |
| Adverse clinical event flag (Clinical AI) | Any flag raised by Clinical AI Safety Officer | Manual escalation |
| Model performance degradation detected in production | AUC-ROC < 0.80 monitored on labeled holdout | Weekly automated evaluation |
| Security vulnerability (Critical severity) | Any CVE with CVSS ≥ 9.0 in model dependencies | Snyk continuous scanning |

#### 5.7.2 Rollback Execution

| Step | Responsible | Timeline |
|---|---|---|
| 1. Rollback decision logged in Model Registry with rationale | Model Owner or Incident Commander | Within 15 minutes of trigger confirmation |
| 2. Traffic cutover to `production-rollback-target` version (100% instant cutover, no canary) | MLOps (automated via rollback pipeline) | Within 10 minutes of logged decision |
| 3. Rollback health check (identical to promotion canary criteria) | MLOps | Monitored 2 hours |
| 4. Incident ticket (P1) created with root cause analysis assignment | MLOps | Within 30 minutes |
| 5. Root cause analysis (RCA) completed and documented | AI/ML Engineering | Within 5 business days |
| 6. RCA review meeting with Model Validation | Model Owner + Model Validation | Within 10 business days |

#### 5.7.3 Post-Rollback State

The rolled-back model resumes production status. The failed model version is tagged `rollback-reverted` in the Model Registry and is quarantined: it may not be promoted again without a full retraining cycle and a new Model Validation Gate.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

**6.1.1 Pipeline Integrity Controls**
- All retraining pipeline DAG definitions are stored in version-controlled Git repositories (`meridian-ml/kfp-pipelines`) with branch protection requiring at least one approving review prior to merge to `main`.
- Pipeline execution is fully containerized and runs on dedicated AWS EKS node groups with no shared tenancy.
- Pipeline artifacts (datasets, models, reports) are stored in the Meridian Model Registry with SHA-256 integrity hashes that are verified on read.
- Immutable logging: All pipeline step outputs are logged to CloudWatch Logs with write-once, append-only retention for 7 years.

**6.1.2 Access Controls**
- Production model endpoints and Model Registry write operations are protected by AWS IAM roles governed by Attribute-Based Access Control (ABAC).
- Direct modification of production model weights outside the retraining pipeline is prohibited and would trigger a `PRODUCTION_TAMPER` alert in AWS GuardDuty.

**6.1.3 Canary and Guardrail Controls (NIST AI RMF MAP-2.1)**
- All Tier 1 and Tier 2 models shall have numeric output guardrails: predictions outside [P1, P99] of the training label distribution are flagged for review and not directly actioned.
- The Meridian Inference Gateway enforces rate limits, input schema validation, and payload size limits for all production model endpoints.

### 6.2 Administrative Controls (NIST AI RMF GOVERN-1.2, GOVERN-2.1)

**6.2.1 Documentation Requirements**
The following documentation shall be maintained current for each production model and reviewed at each retraining cycle:
- Model Fact Sheet (Template AIML-007-MFS-01): summary of intended use, training data provenance, performance benchmarks, fairness metrics, known limitations, and ethical considerations. This documentation is maintained to support ongoing conformity and aligns with EU AI Act technical documentation expectations.
- Training Run Report (auto-generated from pipeline logs)
- Validation Report (MVR per Section 5.5)
- Fairness Assessment Report (Form AIML-007-FAIR-01)

**6.2.2 Quality Management System Integration**
Model retraining activities are governed by the Meridian AI Quality Management System (AI-QMS), documented in the Quality Manual (QM-AI-001). The AI-QMS defines:
- Quality objectives for model retraining (performance non-regression, fairness non-regression, latency stability)
- Documented procedures for non-conformance handling (Section 8)
- Management review of retraining quality metrics at quarterly AI Governance Committee meetings

**6.2.3 Independent Review Requirements (NIST AI RMF MAP-3.3, MEASURE-2.3)**
The Model Validation function, as described in this SOP, performs validation testing on retrained models. Model Validation personnel operate with independence from the development teams, reporting through a separate management chain to the Chief Risk Officer (for financial models) and the Chief Medical Informatics Officer (for clinical models).

### 6.3 Data Protection Controls (NIST AI RMF GOVERN-5.1, MANAGE-4.1)

| Control | Implementation |
|---|---|
| Training data encryption | AES-256 at rest (AWS KMS managed keys); TLS 1.3 in transit |
| PHI de-identification | Mandatory Safe Harbor de-identification (18 HIPAA identifiers removed) before inclusion in any Feature Store dataset accessible to AI/ML Engineering; validated by automated PHI scanner (AWS Comprehend Medical) |
| Data minimization | Training datasets shall include only features with documented predictive relevance (SHAP importance ≥ 0.005 or equivalent) |
| Right-to-be-forgotten compliance | Individual data subject deletion requests processed within 30 days; affected training datasets flagged for incremental retraining with that data excluded |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators

| KPI ID | KPI Description | Target | Measurement Cadence | Responsible |
|---|---|---|---|---|
| KPI-001 | Mean Time to Detect (MTTD) drift for Tier 1 models | ≤ 48 hours | Monthly | MLOps |
| KPI-002 | Mean Time to Respond (MTTR) for drift-triggered retraining to model promotion | ≤ 21 calendar days | Monthly | AI/ML Engineering |
| KPI-003 | Percentage of Tier 1 models within Data Freshness Window | ≥ 98% | Weekly | MLOps |
| KPI-004 | Model retraining success rate (candidate model completes all validation gates) | ≥ 95% | Monthly | AI/ML Engineering |
| KPI-005 | Rollback rate post-promotion | ≤ 2% | Quarterly | Model Validation |
| KPI-006 | Shadow deployment pass rate | ≥ 90% | Quarterly | MLOps |
| KPI-007 | Fairness metric compliance rate (all protected groups within threshold) | 100% | Per retraining | AI/ML Engineering |
| KPI-008 | Documentation completeness at Model Validation Gate | ≥ 100% of checklist items | Per retraining | Model Validation |

### 7.2 Dashboards

The MLOps team maintains the following operational dashboards, accessible at `https://monitoring.meridian.internal`:

| Dashboard Name | Content | Refresh Interval | Primary Audience |
|---|---|---|---|
| Model Health Overview | All production models: staleness status, drift status, error rates, latency, prediction distribution | 5 minutes | MLOps, AI/ML Engineering |
| Retraining Pipeline Status | All recent and active pipeline runs: status, duration, stage completion | 1 minute | MLOps |
| Fairness Monitor | Per-model fairness metric trends over time, subgroup performance | Daily | Model Validation, Compliance |
| Model Validation Queue | Candidate models awaiting validation, validation status, approval status | Real-time | Model Validation, Model Owners |
| Regulatory Compliance Dashboard | Per-model: documentation status, retraining interval compliance, audit readiness | Daily | Compliance, Legal |

### 7.3 Reporting Cadence

| Report | Frequency | Audience | Content |
|---|---|---|---|
| Retraining Operations Summary | Weekly | AI/ML Engineering, MLOps, VP of Engineering | All retraining activities, pipeline health, incidents, MTTR |
| Model Risk Dashboard | Monthly | Model Validation, Business Unit Owners, CRO | Drift events, performance trends, rollbacks, RCA status |
| AI Governance Report | Quarterly | AI Governance Committee, Chief AI Officer, CISO, DPO | KPIs, fairness trends, audit findings, regulatory compliance status, NIST AI RMF alignment review |
| EU AI Act Compliance Report | Semi-annually | Compliance, DPO, Legal, Clinical AI Safety Officer | Technical documentation status for Annex IV models, QMS effectiveness, adverse event summary |
| Annual Model Inventory and Risk Assessment | Annually | Board of Directors (via AI Governance Committee), C-Suite | Comprehensive model inventory with risk classifications, major incidents, regulatory posture |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types

| Exception Type | Description | Requested When |
|---|---|---|
| RETRAIN-DEFER | Defer scheduled retraining beyond Maximum Retraining Interval | Legitimate operational constraint prevents retraining (e.g., data pipeline outage, compute capacity freeze) |
| VALIDATE-WAIVE | Waive one or more validation gate components | Specific validation test is demonstrably inapplicable (e.g., fairness metric for single-demographic use case) |
| ROLLBACK-HOLD | Delay rollback execution beyond standard timeline | Rollback would cause greater harm than continued operation (requires extraordinary evidence) |

### 8.2 Exception Request Process

1. **Initiation:** Model Owner submits Exception Request via Jira form `model-retraining-exception`, providing:
   - Model ID and current version
   - Exception type
   - Detailed justification
   - Impact assessment (what is the risk of NOT granting the exception?)
   - Proposed mitigation plan
   - Proposed duration (maximum for RETRAIN-DEFER: 30 calendar days)

2. **Risk Assessment:** Model Validation team evaluates the exception within:
   - Tier 1 models: 24 hours
   - Tier 2 models: 3 business days
   - Tier 3 and Tier 4 models: 5 business days

3. **Approval Authority:**

| Model Tier | Exception Approver |
|---|---|
| Tier 1 | Chief AI Officer + CISO + Business Unit VP |
| Tier 2 | Chief AI Officer + Business Unit Owner |
| Tier 3 | Director of AI/ML Engineering + Model Validation Lead |
| Tier 4 | Model Owner + MLOps Lead |

4. **Documentation:** All approved exceptions are logged in the Model Registry, linked to the affected model version, and reported in the next quarterly AI Governance Report.

### 8.3 Escalation Path

| Escalation Level | Trigger | Escalation Contact | Timeline |
|---|---|---|---|
| Level 1 | Model Owner unable to resolve retraining issue within 3 business days | Director of AI/ML Engineering | Immediate |
| Level 2 | Drift-triggered P1 ticket unacknowledged for > 4 hours | VP of Engineering (David Park) + CISO | Hour 4 |
| Level 3 | Tier 1 model exceeds Maximum Retraining Interval by > 7 days without approved RETRAIN-DEFER | Chief AI Officer (Dr. Marcus Rivera) | Day 7 |
| Level 4 | Any Clinical AI Platform model involved in a patient safety event attributable to model performance | Chief AI Officer + Chief Medical Officer + Legal | Immediate |

---

## 9. Training Requirements

### 9.1 Required Training

| Training Module | Code | Audience | Frequency | Duration |
|---|---|---|---|---|
| Model Retraining and Continuous Learning SOP Training | TRN-AIML-007-A | All personnel listed in Section 3 RACI matrix | Annually (refresher) + upon SOP version change | 4 hours |
| MLOps Pipeline Operations | TRN-MLOPS-003 | MLOps team, AI/ML Engineering | Annually | 8 hours (including hands-on lab) |
| Fairness Assessment Protocol Training | TRN-FAIR-001 | AI/ML Engineering, Model Validation, Data Governance | Annually | 6 hours |
| Model Validation for Retrained Models | TRN-VAL-002 | Model Validation team members | Annually | 8 hours |
| EU AI Act Compliance for AI Personnel | TRN-REG-EUAI-001 | All AI/ML personnel working on Clinical AI or deploying in EU region | Bi-annually | 4 hours |
| NIST AI RMF Practitioner Training | TRN-RMF-001 | AI/ML Engineering leads, MLOps leads, Model Validation | Bi-annually | 6 hours |

### 9.2 Training Tracking

All training completions are logged in the Meridian Learning Management System (Workday Learning). Compliance is monitored by the AI/ML Engineering Operations Manager. Personnel who are out of compliance with required training shall have their Model Registry write access suspended until completion is verified.

### 9.3 New Hire Onboarding

New hires in roles subject to this SOP must complete the following within 30 calendar days of their start date:
- TRN-AIML-007-A (Model Retraining SOP Training)
- TRN-ETH-001 (AI Ethics at Meridian)
- Role-specific training from the list in Section 9.1
- Shadow a complete retraining cycle with an experienced team member (logged as OJT-AIML-007)

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|---|---|---|
| SOP-AIML-001 | AI/ML Model Lifecycle Management | Parent SOP; governance framework for all ML activities |
| SOP-AIML-002 | Model Development and Initial Deployment | Covers the pre-production phases not addressed here |
| SOP-AIML-004 | Model Risk Evaluation and Validation | Deep validation protocols; MRE methodology referenced in Section 5.5 |
| SOP-AIML-005 | Model Registry and Version Control | Defines the Model Registry schema and versioning semantics |
| SOP-AIML-011 | Model Decommissioning and Archival | End-of-life procedures |
| SOP-DATA-003 | Data Lineage and Certification for AI | Data Governance certification requirements referenced in Section 5.2 |
| SOP-DATA-005 | Ground Truth and Labeling Quality Assurance | Label validation protocols |
| SOP-FAIR-001 | Algorithmic Fairness Assessment Protocol | Fairness metrics and thresholds referenced in Section 5.4.3 |
| SOP-BCP-002 | Business Continuity Planning for AI Systems | DR and recovery procedures linked to rollback |
| SOP-SEC-009 | AI Model Security and Adversarial Defense | Robustness testing standards |
| SOP-VEND-005 | Third-Party Model Governance | Out-of-scope boundary |
| SOP-ITOPS-014 | Infrastructure Model Management | Operational model governance for SaaS platform |

### 10.2 External Standards and Regulations

| Reference | Description | Applicability |
|---|---|---|
| NIST AI 100-1 | Artificial Intelligence Risk Management Framework (AI RMF 1.0) | Enterprise-wide, detailed alignment in Controls and Safeguards section |
| EU AI Act (Regulation 2024/1689) | Harmonized rules on artificial intelligence | Clinical AI Platform models (High-Risk AI systems) |
| SR 11-7 / OCC 2011-12 | Supervisory Guidance on Model Risk Management | HealthPay Financial Services models |
| FDA AI/ML-Based Software as a Medical Device (SaMD) Action Plan | Regulatory framework for adaptive AI in medical devices | Clinical diagnostic models |
| ISO/IEC 42001:2023 | Artificial Intelligence Management System | Referenced in quality management system design |
| HIPAA Security Rule | ePHI protections | MedInsight Analytics models handling PHI |

---

## 11. Revision History

| Version | Effective Date | Author | Description of Changes |
|---|---|---|---|
| 3.8 | 2024-05-17 | Dr. Marcus Rivera (CAIO) | Current version. Expanded NIST AI RMF alignment controls (Section 6); added shadow deployment requirements for Tier 2 models; refined drift detection thresholds based on 12-month production telemetry review; added carbon footprint logging requirement. |
| 3.7 | 2024-02-01 | Dr. Marcus Rivera (CAIO) | Incorporated EU AI Act technical documentation requirements (Section 6.2.1); updated roles to include Clinical AI Safety Officer; refined rollback trigger metrics based on incident postmortems from Q4 2023. |
| 3.6 | 2023-10-15 | Sarah Chen (MLOps) | Replaced manual drift analysis with automated Evidently AI integration; introduced Kubeflow DAG versioning controls; updated Data Freshness Window for Tier 3 models from 60 to 45 days; added Continuous Learning governance constraints. |
| 3.5 | 2023-07-22 | Dr. Marcus Rivera (CAIO) | Post-acquisition harmonization: unified Meridian model registry references; updated role names to reflect current organizational structure; expanded Fairness Assessment section per consent decree requirements. |
| 3.4 | 2023-04-10 | Former CTO (name redacted) | Transition from SageMaker Studio notebooks to standardized Kubeflow pipelines; introduced Model Validation Gate; removed legacy model retraining scripts. |
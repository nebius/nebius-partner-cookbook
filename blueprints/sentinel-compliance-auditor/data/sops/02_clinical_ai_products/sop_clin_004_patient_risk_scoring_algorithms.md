---
sop_id: "SOP-CLIN-004"
title: "Patient Risk Scoring Algorithms"
business_unit: "Clinical AI Products"
version: "3.9"
effective_date: "2025-08-19"
last_reviewed: "2026-12-23"
next_review: "2027-06-22"
owner: "Dr. Aisha Okafor, VP of Clinical AI Products"
approver: "Dr. Priya Patel, Chief Medical Officer"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "HIPAA"
  - "SR 11-7"
  - "NIST AI RMF"
status: "Active"
---

# SOP-CLIN-004: Patient Risk Scoring Algorithms

## 1. Purpose and Scope

This Standard Operating Procedure (SOP) establishes the governance framework, lifecycle management, and operational controls for all artificial intelligence/machine learning (AI/ML) algorithms designed, developed, procured, or deployed by Meridian Health that generate patient risk scores. The purpose of this document is to ensure that patient risk scoring is performed in a reliable, transparent, fair, and clinically safe manner, consistent with Meridian’s mission to leverage data-driven insights while safeguarding patient welfare and data integrity.

**Scope.** This SOP applies to:

- All Clinical AI Products under the remit of the VP of Clinical AI Products, Dr. Aisha Okafor.
- All algorithmic systems that ingest Protected Health Information (PHI) from Meridian’s Data Lake, electronic health record (EHR) feeds, or patient-reported outcome instruments and output a quantitative score, classification, or probability intended to inform clinical decision support, resource triage, or population health stratification.
- Model development, validation, deployment, monitoring, and retirement activities conducted by internal Data Science, Machine Learning Engineering (MLE), and Clinical Informatics teams, as well as third-party vendors contracted through the Meridian Vendor Risk Management process (per SOP-PROC-012).
- Governance committees exercising oversight of algorithmic performance, including the Algorithmic Bias Review Board (ABRB) and the Clinical Decision Support Safety Committee (CDSSC).

**Out of Scope.** Research models that have not received Institutional Review Board (IRB) authorization for clinical use and are operated in a sandboxed environment without access to production data stores are exempt, provided they are never introduced into a clinical workflow without full review under this SOP.

**Applicability.** All employees, contractors, credentialed clinicians, data scientists, and quality improvement personnel who design, train, validate, deploy, or retire patient risk scoring algorithms must adhere to this policy. Business owners at the VP level are accountable for compliance within their units.

---

## 2. Definitions and Acronyms

| Term | Definition |
|---|---|
| **Algorithm** | The complete computational procedure—data preprocessing, feature engineering, model core, and post-processing logic—that converts input feature vectors into a patient risk score. |
| **Area Under the Receiver Operating Characteristic Curve (AUROC)** | A summary metric of binary classifier discrimination across all possible thresholds. AUROC = 1.0 indicates perfect separation; 0.5 indicates no better than random chance. |
| **Calibration-in-the-Large (CITL)** | The difference between the mean observed outcome rate and the mean predicted risk in a validation cohort. Values near zero indicate good aggregate calibration. |
| **Calibration Slope** | The coefficient of the linear predictor in a recalibration regression (observed outcome ~ log-odds predicted risk). A slope of 1.0 indicates perfect calibration; <1.0 indicates overfitting to the training signal. |
| **Clinical Decision Support Safety Committee (CDSSC)** | Meridian’s cross-functional governance body chaired by the Chief Medical Information Officer (CMIO) responsible for reviewing all in-production risk models at least semi-annually. |
| **Fairness-Aware Threshold Tuning (FATT)** | The process of selecting decision thresholds for distinct demographic subpopulations to equalize prespecified fairness criteria (e.g., equalized odds) while maintaining clinically acceptable sensitivity and specificity. |
| **MAPE (Macro-Averaged Prediction Error)** | The absolute difference between predicted and observed risk, averaged across strata defined by age, sex, Elixhauser comorbidity count, and payer type. Used to detect systematic under- or over-estimation within protected groups. |
| **Model Risk Tier** | A classification of algorithm criticality: *Tier 1*—directly triggers a clinical intervention (e.g., automated sepsis alert activates a rapid response team); *Tier 2*—informs clinician judgment but does not automate downstream actions (e.g., readmission risk displayed on a dashboard); *Tier 3*—aggregate population analytics only, no patient-level visible output. |
| **Net Reclassification Improvement (NRI)** | The proportion of patients correctly reclassified by the new model relative to a baseline comparator (e.g., a logistic regression of age plus sex) across clinically meaningful risk strata. |
| **Patient Risk Score** | A numeric value, typically expressed as a probability (0.0–1.0) or scaled integer (e.g., 1–100), representing the predicted likelihood of a specific adverse clinical event within a defined time horizon. |
| **Protected Group** | Any subpopulation defined by race, ethnicity, primary language, sex, gender identity, payer status, or age ≥65 years, per Meridian’s Health Equity Policy (see SOP-CO-019). |
| **Shadow Deployment** | The operation of a model in a production environment with live clinical data flowing through the inference pipeline, where model outputs are stored and monitored but not displayed to clinicians or used for decision-making. |
| **Threshold** | The numeric cutpoint applied to a continuous risk score that defines the boundary between a positive and negative classification for clinical action triggers. |

---

## 3. Roles and Responsibilities

| Role | Responsibility | RACI Designation |
|---|---|---|
| **VP of Clinical AI Products (Dr. Aisha Okafor)** | Ultimate accountability for all patient risk scoring algorithms. Owns model lifecycle documentation. Approves model promotion to production. | Approve (A) for deployment; Informed (I) for Tier 3 models. |
| **Chief Medical Officer (Dr. Priya Patel)** | Approves clinical validity thresholds, risk model tiers, and override protocols. Chairs escalation review for models with sustained calibration drift >0.10. | Approve (A) for clinical validity; Consult (C) for Tier 2/3 thresholds. |
| **Chief Medical Information Officer (CMIO)** | Chairs the CDSSC. Ensures EHR integration complies with clinical workflow standards. Approves UX design for clinical-facing risk displays. | Approve (A) for clinical integration; Consult (C) for EHR workflow design. |
| **Vice President of Data Science** | Manages the model development team. Ensures technical documentation (model architecture, training data provenance, feature engineering code) is version-controlled in Meridian’s Model Repository. | Responsible (R) for model development and Shadow Deployment. |
| **Chief Health Equity Officer** | Reviews fairness metrics, sets MAPE thresholds per protected group, and convenes the ABRB when disparity metrics exceed prespecified bounds. | Approve (A) for fairness thresholds; Consult (C) for protected group definitions. |
| **Chief Information Security Officer (CISO)** | Ensures PHI used in model training and inference complies with access controls defined in SOP-SEC-031. | Consult (C) for data pipeline security. |
| **Clinical Informatics Lead** | Maps model inputs to structured EHR data fields. Maintains the Feature Dictionary. Coordinates prospective clinical validation studies. | Responsible (R) for clinical data mapping and validation study execution. |
| **Machine Learning Engineering (MLE) Team** | Builds, monitors, and maintains the inference pipeline. Implements logging infrastructure. Responds to model performance alerts. | Responsible (R) for inference pipeline uptime, latency, and monitoring dashboards. |
| **Quality Improvement (QI) Directors** | Operational owners of care pathways activated by Tier 1 risk models. Provide feedback on alert fatigue, workflow friction, and unintended consequences. | Consult (C); Responsible (R) for care pathway adherence metrics. |

---

## 4. Policy Statements

Meridian Health commits to the following principles governing patient risk scoring algorithms:

1. **Clinical Benefit and Non-Maleficence.** Every algorithm deployed to production must demonstrate, via a prospective or historically-controlled clinical validation study, a net expected benefit to patients—defined as an improvement in either a clinically relevant outcome metric (e.g., reduced inpatient mortality, reduced 30-day readmission rate, earlier identification of sepsis) or a significant reduction in measurement-to-intervention latency without increasing false-positive harm rates beyond the acceptable threshold defined by the CDSSC.

2. **Performance Transparency.** Model performance characteristics—including AUROC, CITL, calibration slope, sensitivity, specificity, and positive predictive value (PPV)—must be made available to end-users via a standardized Model Fact Sheet accessible from within the EHR clinical decision support interface.

3. **Fairness Monitoring.** All risk scores must be continuously monitored for differential performance across Protected Groups as defined in Section 2. A macro-averaged prediction error (MAPE) disparity greater than ±0.05 between any two protected groups triggers a mandatory Algorithmic Bias Review Board (ABRB) case review within 30 calendar days.

4. **Shadow Deployment Mandate.** No Tier 1 or Tier 2 model shall be activated for clinical use without first completing a minimum 90-day Shadow Deployment period during which real-time inference is performed but outputs are not visible to clinical end-users. The Shadow Deployment Report must confirm: (a) inference pipeline uptime ≥99.5%; (b) end-to-end latency p95 ≤200ms; (c) data drift (Population Stability Index) ≤0.25; and (d) output distribution clinically plausible as adjudicated by the Clinical Informatics Lead.

5. **Threshold Governance.** Classification thresholds for Tier 1 models (automated clinical actions) must be established jointly by the Clinical Informatics Lead and the owning QI Director, documented in the Model Configuration Registry, and approved by the CDSSC. Thresholds for Tier 2 models (clinical decision support with human override) may be set to a default of 0.5 (for binary classifiers) but must be adjustable by individual clinical business units with all adjustments logged for audit.

6. **Human Override Audit Trail.** Every instance in which a clinician overrides or dismisses a risk score recommendation must be captured in the EHR audit log and linked to a specific encounter ID for downstream analysis by the Clinical Informatics team.

7. **Lifecycle Review.** Every algorithm shall undergo a formal lifecycle review at intervals not exceeding 12 months, or immediately upon detection of performance degradation exceeding predefined control limits (see Section 6). The review must consider model retirement, recalibration, retraining on more recent data, or redesign.

---

## 5. Detailed Procedures

### 5.1 Algorithm Conception and Risk Tier Classification

1. **Proposal Submission.** Any Meridian employee or affiliate seeking to develop a new patient risk scoring algorithm must submit a completed Algorithm Proposal Form (APF) to the VP of Clinical AI Products via the Clinical AI Intake Portal (ServiceNow Catalog Item: "Clinical AI – New Algorithm Proposal").
2. **APF Contents.** The APF must include:
   - Proposed clinical use case, target outcome, and time horizon.
   - Anticipated data sources (specify Meridian Data Lake tables, EHR flowsheets, or external datasets).
   - Proposed Model Risk Tier (per Section 2 definitions) with justification.
   - Named business sponsor (VP-level or above).
   - Preliminary fairness considerations (list of Protected Groups anticipated to be relevant).
3. **Triage Review (≤10 business days).** The VP of Clinical AI Products, in consultation with the CMIO and Chief Health Equity Officer, shall:
   - Assign a final Model Risk Tier.
   - Approve or reject the proposal.
   - If approved, designate a **Model Lead** (typically a Senior Data Scientist) and a **Clinical Sponsor**.
   - Log the decision in the Model Inventory (SharePoint List "Clinical AI Model Registry"), assigning a unique Model ID (format: `MDL-YYYY-NNN`).

### 5.2 Training Data Curation and Feature Engineering

1. **Cohort Definition.** The Model Lead, in collaboration with the Clinical Sponsor and Clinical Informatics Lead, shall author a formal Cohort Definition Document (CDD) specifying:
   - Inclusion criteria (e.g., all adult inpatient encounters with length of stay ≥24 hours, January 1, 2022 – December 31, 2024).
   - Exclusion criteria (e.g., elective admissions, patients leaving against medical advice, encounters with missing primary diagnosis).
   - Outcome labeling logic (e.g., "30-day unplanned readmission" defined as inpatient readmission within 30 days of discharge, excluding planned procedures per CMS Planned Readmission Algorithm v9.0).
   - Censoring rules and lookback windows.
2. **Data Extraction.** The MLE team executes the CDD against the Meridian Data Lake using SQL-based extraction scripts version-controlled in the Git repository `meridian-clinical-ai/cohort-definitions`. A Data Quality Report (DQR) must be generated automatically upon extraction and reviewed by the Model Lead. The DQR must report:
   - Row count per inclusion/exclusion step.
   - Proportion of missingness for each candidate feature.
   - Distribution of outcome prevalence across Protected Groups.
3. **Train/Validation/Test Split.** Data must be partitioned chronologically (not random) to prevent temporal data leakage:
   - **Training set:** Earliest 60% of the time window.
   - **Validation (calibration) set:** Next 20% of the time window.
   - **Test (holdout) set:** Most recent 20% of the time window.
   - A holdout "prospective simulation" set consisting of the 90 days immediately following the test set cutoff may be reserved for Shadow Deployment comparison.

### 5.3 Model Development and Calibration

1. **Baseline Model.** Every project must train a simple logistic regression comparator model using no more than 10 hand-selected features (documented in the CDD). This serves as a sanity check for more complex architectures.
2. **Candidate Architectures.** The Model Lead may explore gradient boosted trees (LightGBM/XGBoost), deep neural networks, or other architectures. All experiments must be logged in MLflow Tracking Server (`mlflow.meridian.internal`) with hyperparameters, feature sets, and performance metrics recorded per run.
3. **Calibration.** All models that output a probability must undergo isotonic regression or Platt scaling on the validation set. Post-calibration calibration error (Expected Calibration Error, ECE) computed on the test set must be ≤0.08 for Tier 1 models and ≤0.12 for Tier 2 models.
4. **Feature Importance.** SHAP (SHapley Additive exPlanations) values must be computed for the final model on the test set and aggregated to global feature importance rankings. The top 20 features must be reviewed by the Clinical Informatics Lead for clinical plausibility. Any clinically implausible feature exhibiting high importance must be investigated for potential label leakage or confounding and documented.

### 5.4 Clinical Validation Protocol

1. **Study Design.** The Clinical Informatics Lead, in conjunction with the QI Director for the target clinical area, shall author a Clinical Validation Protocol (CVP). The CVP can be:
   - *Historically-controlled silent prospective:* Run the model on historical data with simulated clinical actions based on retrospective chart review to estimate counterfactual outcomes.
   - *Prospective silent observation:* Deploy the model in Shadow Deployment concurrent with existing clinical workflows, but do not display scores. Compare model-triggered events against actual clinical events captured in the EHR.
2. **Performance Endpoints.** The CVP must define, at minimum:
   - Sensitivity at the proposed operational threshold.
   - Specificity at the proposed operational threshold.
   - PPV and Negative Predictive Value (NPV) given outcome prevalence.
   - Alert rate (expected proportion of encounters triggering an alert per day/week) to quantify anticipated workflow burden.
3. **Fairness Evaluation.** Compute the following metrics stratified by each Protected Group and append to the CVP:
   - AUROC per group.
   - CITL per group.
   - False-positive rate and false-negative rate at the proposed threshold.
   - A Fairness Report Card must be generated using the Meridian internal tool "EquiScore" and attached to the CVP.
4. **CVP Approval.** The CDSSC must review and approve the CVP and Fairness Report Card prior to the start of the Shadow Deployment. Approval is documented in the Model Configuration Registry.

### 5.5 Shadow Deployment and Monitoring (Minimum 90 Days)

1. **Pipeline Configuration.** MLE deploys the model container (Docker image) to the Meridian Model Serving Platform (Kubernetes cluster `merid-ml-infer-prod`) with the `shadow` flag enabled in the Model Configuration Registry, ensuring inference outputs are written to the Shadow Log (`s3://meridian-shadow-log/`) but the EHR integration endpoint is disabled.
2. **Data Validation.** During the first 14 days of Shadow Deployment, the MLE team performs a data validation audit every business day, comparing the distribution, mean, and variance of each input feature against the test set distribution via Population Stability Index (PSI). Any feature with PSI >0.25 triggers a Data Drift Alert (PagerDuty service `clinical-ai-data-drift`), and the Clinical Informatics Lead must determine whether the drift is attributable to secular clinical trends (acceptable) or a data pipeline defect (must be remediated before clinical activation).
3. **Shadow Performance Report.** At the conclusion of the 90-day minimum Shadow Deployment, the Model Lead generates a Shadow Performance Report (SPR) containing:
   - Aggregate performance metrics vs. the test set baseline.
   - Drift metrics (PSI, outcome prevalence shift).
   - Latency percentiles (p50, p95, p99).
   - Anomalous inference counts (scores outside the [0, 1] probability range or manifestly nonsensical values).
4. **Shadow Exit Gate.** The CDSSC reviews the SPR. Exit criteria for Shadow Deployment:
   - PSI for all features ≤0.30 (or drift explained and accepted).
   - Outcome prevalence within ±20% of the validation set prevalence.
   - Latency p95 ≤500ms.
   - No critical anomalies (scores out of range) in more than 0.01% of inferences.
   - Fairness metrics (MAPE per Protected Group) within prespecified bounds set by the Chief Health Equity Officer.
   - Clinical Sponsor sign-off.

### 5.6 Clinical Activation and Threshold Setting

1. **Threshold Workshop.** Prior to clinical activation, the Clinical Informatics Lead convenes a Threshold Workshop with the QI Director, Clinical Sponsor, and a representative from the CDSSC. The workshop reviews the sensitivity/specificity trade-off curve, expected alert volume, and operational capacity of the target care team.
2. **Threshold Decision.** For Tier 1 models, a single operational threshold must be selected and documented in the Model Configuration Registry and the EHR CDS module configuration. For Tier 2 models, a default threshold is set, and individual clinical business units may request threshold adjustments via a Change Request (CR) submitted to the CDSSC.
3. **Go-Live Communication.** At least 14 calendar days before clinical activation, the Clinical Informatics Lead must distribute a Go-Live Notification to all affected clinical stakeholders, including:
   - Model ID and clinical purpose.
   - Operational threshold and alert logic.
   - Expected alert volume (per shift/per clinician).
   - Instructions for providing feedback and for the human override mechanism.
   - Contact for the 24/7 on-call Clinical AI support rotation (PagerDuty escalation policy `clinical-ai-support`).
4. **Activation.** MLE flips the `shadow` flag to `production` in the Model Configuration Registry. The EHR integration endpoint is activated. Model inference now flows to the EHR CDS module via the HL7 FHIR `RiskAssessment` resource.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control ID | Control Description | Implementation Mechanism | Applicable Tier |
|---|---|---|---|
| TEC-001 | All inference requests must be authenticated via OAuth2 client credentials grant. | Kong API Gateway plugin `oauth2-cc` on `/inference` routes. | All |
| TEC-002 | PHI used in inference must be encrypted in transit (TLS 1.3) and at rest (AES-256-GCM). | Istio mTLS mesh + AWS KMS-managed keys on S3 data stores. | All |
| TEC-003 | Model weights and serialized artifacts must be stored in an immutable artifact registry with write-once-read-many (WORM) policy. | AWS ECR with immutable tags enabled; model binaries hashed (SHA-256) and logged at registration. | All |
| TEC-004 | Every inference event must generate a structured audit log record containing: model ID, version, input feature vector hash, output score, timestamp, and session ID. | Fluentd sidecar in inference pod → structured JSON → Elasticsearch index `clinical-inference-audit-{YYYY-MM}`. Index retention period: 7 years. | All |

### 6.2 Administrative Controls

| Control ID | Control Description | Frequency | Owner |
|---|---|---|---|
| ADM-001 | Model Inventory Review: Validate accuracy of Model Configuration Registry entries, retirement status, and Shadow/Production flags. | Quarterly | VP of Clinical AI Products |
| ADM-002 | CDSSC Lifecycle Review: Full performance review of every active Tier 1 and Tier 2 model against current clinical data. | Semi-annual (or per Section 4, Policy 7 if drift triggers breached). | CMIO |
| ADM-003 | Algorithmic Bias Review Board (ABRB) Case Review: Review of any model exceeding MAPE disparity bound of ±0.05 between protected groups. | Within 30 calendar days of trigger. | Chief Health Equity Officer |
| ADM-004 | Clinician Feedback Survey: Structured survey sent to all active clinical users of Tier 1 alerts, measuring perceived clinical utility, alert fatigue (e.g., "I override this alert without reading it"), and patient safety concerns. | Quarterly | Clinical Informatics Lead |

### 6.3 Quality Management System

Meridian maintains a Quality Management System (QMS) for clinical AI products covering design controls, risk management, document and record control, and corrective and preventive actions (CAPA). The Clinical AI QMS aligns with the general principles of software as a medical device lifecycle management. Product-specific quality plans are developed during the Algorithm Conception phase. Training records, audit logs, and performance reviews are maintained as quality records.

### 6.4 Risk Classification Framework

All patient risk scoring algorithms are evaluated through a structured risk assessment process, considering the severity of the target clinical condition, the immediacy of the clinical intervention triggered, and the reversibility of any potential adverse outcome resulting from an incorrect score. The Model Risk Tier assigned during proposal triage (Section 5.1) serves as the operational risk classification. Algorithms that directly trigger irreversible or high-acuity clinical actions undergo an enhanced review by the CDSSC, which includes review of failure mode and effects analysis (FMEA) documentation prepared by the Clinical Informatics Lead.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Real-Time Monitoring Dashboards

The MLE team maintains a Grafana dashboard (`Clinical AI – Inference Health`) displaying:

- **Request rate** (inferences per second, per model).
- **Latency** (p50, p95, p99 per model over 5-minute rolling windows).
- **Error rate** (HTTP 5xx or prediction failures as a proportion of total requests).
- **Score distribution histogram** (last 60 minutes) overlaid with the expected distribution band from the SPR.

Alerting thresholds:
- **Page:** (PagerDuty `clinical-ai-critical`): Error rate >1% sustained for 5 minutes; latency p95 >2000ms for Tier 1 models; any inference returning a non-numeric or out-of-bounds score.
- **Warning:** (Slack channel `#clinical-ai-alerts`): Error rate >0.1%; latency p95 >500ms for Tier 1 models; PSI >0.25 detected in any feature in the last 24 hours based on the data drift detection pipeline.

### 7.2 Clinical Performance Metrics (Reported Monthly)

A monthly **Clinical AI Performance Report (CAPR)** is published to the Clinical AI Sharepoint site and reviewed by the CDSSC. Each active model must report:

| Metric | Definition | Acceptable Range | Escalation Trigger |
|---|---|---|---|
| Observed Outcome Rate | Actual event rate in the population receiving scores over the reporting month. | Within ±15% of expected prevalence from CVP. | Deviation >±25% triggers an Ad Hoc Lifecycle Review. |
| Alert Override Rate | Proportion of Tier 1 alerts dismissed or acknowledged without resulting in the intended clinical action. | ≤60% override rate. | >60% override rate triggers a QI Workflow Review per SOP-QI-007. |
| MAPE Disparity | Difference in MAPE between the highest-disparity and lowest-disparity Protected Groups. | ≤0.05. | >0.05 triggers ABRB Case Review within 30 days per ADM-003. |
| Calibration Slope (Quarterly) | Recalibration regression slope on a rolling 12-month window of inference data. | 0.85–1.15 for Tier 1; 0.75–1.25 for Tier 2. | Slope outside range triggers model recalibration procedure. |

### 7.3 Longitudinal Fairness Reporting

The Chief Health Equity Officer receives an automated **Fairness Dashboard** (built on Tableau, sourcing from the inference audit log joined with patient demographic tables) updated weekly. The dashboard displays trend lines of MAPE per Protected Group for each active Tier 1 and Tier 2 model. Any sustained divergence for >4 consecutive weeks triggers a mandatory ABRB Case Review even if the MAPE disparity bound has not yet been breached—this is a leading-indicator review per the NIST AI RMF Act function.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types and Approval Authority

| Exception Type | Definition | Approval Authority | Maximum Duration |
|---|---|---|---|
| Shadow Deployment Duration Reduction | Request to reduce the 90-day Shadow Deployment for a Tier 2 model to no less than 45 days. | CDSSC Chair (CMIO) | Single instance; must be reapproved at 45-day mark if extension needed. |
| Calibration Threshold Waiver | Request to deploy a Tier 2 model with ECE up to 0.15 (exceeding the 0.12 standard). | VP of Clinical AI Products | 6 months; must be accompanied by a remediation plan with milestones. |
| Fairness Bound Exception | Request to operate a model with MAPE disparity between 0.05 and 0.08 for a defined period due to clinical necessity (e.g., no available alternative model for a rare disease). | Chief Health Equity Officer + Chief Medical Officer jointly | 4 months; ABRB must review monthly. |
| Tier Classification Downgrade | Request to classify a model as Tier 2 when its clinical impact characteristics meet Tier 1 definitions per Section 2. | Chief Medical Officer (sole authority) | Permanent (if approved); documented rationale required. |
| Production Emergency Rollback | Immediate deactivation of a model due to a patient safety concern or critical technical failure. | On-call MLE Lead (any tier) | Immediate; post-hoc notification to CDSSC within 24 hours. |

### 8.2 Escalation Pathway for Algorithmic Harm Events

1. **Identification.** Any clinician, data scientist, or QI staff member who identifies a potential patient harm event related to an incorrect risk score must immediately file a Safety Event Report via the Meridian RL Solutions incident reporting system, selecting the category "Clinical AI/Algorithmic."
2. **Initial Triage (within 4 hours of filing).** The Patient Safety Officer and the on-call Clinical Informatics Lead jointly triage the event:
   - **Severity 1 (Critical):** Actual patient harm or high probability of imminent harm. Model is immediately placed into **Emergency Suspension** status via the Model Configuration Registry, ceasing all clinical-facing inference. The CMO, CMIO, and VP of Clinical AI Products are notified via PagerDuty `clinical-ai-sev1`.
   - **Severity 2 (Elevated):** Significant potential for harm or systematic error identified, but no confirmed harm. Model remains active but the CDSSC is convened within 72 hours for a Risk-Benefit Assessment.
   - **Severity 3 (Routine):** Isolated incident, no systemic concern. Logged for trending analysis.
3. **Root Cause Analysis (RCA).** For Severity 1 events, a formal RCA must be initiated within 5 business days, led by the VP of Clinical AI Products or designee, with participation from MLE, Clinical Informatics, and the involved clinical unit. The RCA report is reviewed by the CDSSC.
4. **Model Reactivation.** A suspended model may only be reactivated upon CDSSC approval of a remediation plan that addresses the root cause with verified corrective actions, and upon completion of a re-validation study (which may be expedited but not waived).

---

## 9. Training Requirements

### 9.1 Required Training Matrix

| Role | Training Module | Frequency | Delivery Method | Tracking |
|---|---|---|---|---|
| All Data Scientists (internal) | "Responsible AI in Healthcare: Managing Bias and Fairness in Clinical Risk Models" | Annually | LMS e-learning (Cornerstone course ID: CLIN-AI-RES-101) | Cornerstone auto-enrollment; completion tracked by VP of Clinical AI Products dashboard. |
| MLE Team | "Inference Pipeline Security and PHI Handling" | Annually | LMS e-learning + live workshop | Cornerstone; live attendance tracked via QR check-in. |
| Clinical Informatics Leads | "Clinical Validation Study Design" + "Threshold Governance and CDS Configuration" | Every 2 years | Live bootcamp (2 days, Meridian Simulation Lab) | Cornerstone event registration; CME credits awarded. |
| All Clinical End-Users (Tier 1 alert recipients) | "Interpreting the Patient Risk Score: Meridian Clinical AI" | At initial deployment and upon any substantive model update (v2.0+). Also available on demand. | EHR-embedded Microlearning (≤5 minutes, HealthStream pop-up). Refresher triggered annually. | EHR access log; completion status linked to clinical license profile. |
| CDSSC Members | "AI Model Lifecycle Governance and Post-Market Surveillance" | Biannually | In-person seminar with external expert faculty | Signature log. |

### 9.2 Competency Assessment

- Data Scientists must pass a post-course assessment (≥80% score) for "Responsible AI in Healthcare," including a case study requiring analysis of a simulated fairness report and recommendation of a FATT strategy.
- MLE team members must complete a hands-on practical exam involving the simulated rollback of a compromised inference pipeline within a sandbox environment, graded pass/fail by the VP of Data Science.
- Competency records are maintained in each employee’s personnel file and reviewed during annual performance appraisals for compliance.

---

## 10. Related Policies and References

### 10.1 Internal Policies

| SOP ID | Title | Relationship |
|---|---|---|
| SOP-DATA-002 | Clinical Data Lake Access and Governance | Defines data access permissions for training data extraction. |
| SOP-CLIN-001 | Clinical Decision Support Lifecycle Governance | Overarching CDS lifecycle; this SOP is subservient for risk-scoring-specific algorithms. |
| SOP-CLIN-005 | EHR Integration and CDS Alert Configuration | Specifies technical configuration of CDS hooks in Epic. |
| SOP-CO-019 | Health Equity and Algorithmic Fairness Policy | Defines Protected Groups, fairness standards, and ABRB charter. |
| SOP-QI-007 | Clinical Workflow Redesign Triggered by Alert Fatigue | Procedures for addressing high override rates. |
| SOP-SEC-031 | Protected Health Information Security Controls | Specifies encryption standards, access logging, and audit requirements. |
| SOP-PROC-012 | Vendor Risk Management for Procured Clinical Algorithms | Applies to third-party risk models integrated into Meridian systems. |
| SOP-CLIN-003 | Clinical Validation Study Standards | Defines acceptable study designs, endpoints, and statistical analysis plans. |

### 10.2 External Standards and Frameworks

- **NIST AI RMF 1.0** (AI Risk Management Framework), NIST AI 100-1, January 2023. This SOP operationalizes the Govern, Map, Measure, and Manage functions as detailed throughout Sections 5 (Map/Measure), 6 (Govern), and 7 (Manage). Specifically:
  - **Govern (GOV-1 to GOV-6):** Sections 4 (Policy Statements), 6.2 (Administrative Controls), and 8 (Exception Handling) address policies, accountability structures, and organizational risk tolerance.
  - **Map (MAP-1 to MAP-5):** Sections 5.1 (Algorithm Conception) and 5.2 (Training Data Curation) establish context, categorize the AI system, and document the intended use case.
  - **Measure (MEASURE-1 to MEASURE-4):** Sections 5.3 (Calibration), 5.4 (Clinical Validation), and 7 (Metrics) define quantitative and qualitative metrics for trustworthiness, fairness, and clinical efficacy.
  - **Manage (MANAGE-1 to MANAGE-4):** Sections 8.2 (Escalation), 5.6 (Activation), and the Lifecycle Review (Policy 7) define risk treatment, response, and post-deployment monitoring procedures. The ABRB embodies the NIST AI RMF recommendation for interdisciplinary teams in risk management (Playbook §3.2).
- **HIPAA Privacy Rule (45 CFR Part 164, Subpart E).** This SOP governs the use of PHI for algorithm development under the healthcare operations provision. Minimum necessary data elements must be specified in the Cohort Definition Document.
- **EU Medical Device Regulation (EU MDR) 2017/745.** Applies to Meridian’s CE-marked Clinical AI products (SOP-RA-008, Clinical AI Regulatory Dossier). This SOP implements post-market surveillance (PMS) and vigilance obligations.
- **ISO 13485:2016** (Medical Devices – Quality Management Systems). Meridian’s QMS (Section 6.3) is certified under ISO 13485; this SOP documents risk management and design control procedures within that QMS scope.
- **NIST SP 800-53 Rev. 5**, Security and Privacy Controls for Information Systems. Controls in Section 6.1 map to AC (Access Control), AU (Audit and Accountability), and SC (System and Communications Protection) control families.

---

## 11. Revision History

| Version | Date | Author/Editor | Summary of Changes |
|---|---|---|---|
| 1.0 | 2021-03-15 | Dr. Aisha Okafor | Initial publication. Established basic risk score governance, Tier classification, and validation requirements. |
| 2.0 | 2022-07-22 | Dr. Aisha Okafor / CMIO Office | Major revision: introduced Shadow Deployment mandate, ABRB definition, and threshold governance. Added Fairness Report Card requirement. |
| 2.5 | 2023-02-01 | Clinical Informatics Lead (Dr. S. Chen) | Interim update: Added MAPE definition and disparity thresholds per new Health Equity policy (SOP-CO-019). Refined calibration metrics. |
| 3.0 | 2023-11-10 | VP of Clinical AI Products / CISO Office | Added detailed technical controls (TEC-001 through TEC-004). Integrated NIST AI RMF references throughout. Expanded training requirements. Updated for MDR CE-marking requirements post-2023 audit finding. |
| 3.5 | 2024-09-30 | MLE Team Lead (J. Ortiz) | Revision: Updated inference pipeline technology stack references (Kubernetes, Grafana). Refined Shadow Deployment exit criteria with quantitative bounds. Clarified escalation Severity definitions per RCA feedback from incident MER-2024-081 (readmission model alert fatigue). |
| 3.9 | 2025-08-19 | Dr. Aisha Okafor | Current version: Integrated FATT terminology into threshold procedure, added Tier classification downgrade exception, updated PagerDuty routing for Clinical AI alerts, expanded fairness monitoring to include weekly leading-indicator dashboard per ABRB recommendation. Clarified end-to-end latency SLA for Tier 1 inference. Updated regulatory references for EU AI Act transition. |

---

**Document Classification: Internal.** This document contains proprietary information about Meridian Health’s clinical algorithmic infrastructure, validation procedures, and security controls. Distribution is limited to Meridian employees, credentialed affiliates, and authorized contractors under NDA. Do not reproduce or distribute externally without written permission from the VP of Clinical AI Products.

**End of SOP-CLIN-004.**
---
sop_id: "SOP-FIN-018"
title: "Credit Risk Model Back-Testing"
business_unit: "Financial Services"
version: "3.3"
effective_date: "2025-06-18"
last_reviewed: "2026-02-13"
next_review: "2026-08-06"
owner: "Robert Liu, VP of Financial Services"
approver: "James Thornton, Chief Financial Officer"
classification: "Internal"
regulations:
  - "SR 11-7"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: Credit Risk Model Back-Testing

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the mandatory framework for conducting rigorous, independent back-testing of all credit risk models within the HealthPay Financial Services business unit at Meridian Health Technologies, Inc. The objective is to ensure that models used for credit origination, medical lending, patient financing, and claims-based credit assessments continue to perform as expected, remain conceptually sound, and do not introduce unmanaged risk to the organization or its stakeholders. This SOP operationalizes the model validation and ongoing monitoring requirements prescribed by the Federal Reserve's Supervisory Guidance on Model Risk Management (SR 11-7) and integrates selected risk management practices from the NIST Artificial Intelligence Risk Management Framework (AI RMF 1.0).

Back-testing, as defined herein, is the quantitative ex-post comparison of a model’s predicted credit risk outcomes (probability of default, loss given default, credit score bands, delinquency status) against realized, observed outcomes over defined performance windows. This process is a critical control for identifying model drift, calibration decay, and discriminatory outcomes, thereby triggering timely remediation, recalibration, or retirement of models.

### 1.2 Scope

This SOP applies to all models within the HealthPay Financial Services division classified as "Credit Risk Models" in the Meridian Model Inventory System (MMIS), regardless of the underlying technology (e.g., logistic regression, gradient-boosted trees, or neural networks). The scope includes:

- **Origination Models:** Models that assign a Meridian HealthPay Score (MHPS) to healthcare providers and patients seeking medical loans.
- **Behavioral Scoring Models:** Models that predict the probability of delinquency (30, 60, 90+ days past due) on existing patient financing plans.
- **Collections Models:** Models that prioritize collection activities based on predicted recovery rates.
- **Claims-Based Credit Assessment Models:** AI/ML models that leverage historical medical claims data (with appropriate consent and de-identification per SOP-PRIV-042) to assess creditworthiness for unbanked or underbanked patients.
- **Fraud Detection Models:** Models predicting the likelihood of fraudulent credit applications within the healthcare financing context.
- **Adverse Event Prediction for Lending:** Models predicting patient-specific financial toxicity risk based on upcoming scheduled procedures, integrated to adjust credit limits dynamically.

This SOP applies to all phases of the model lifecycle post-implementation: ongoing monitoring, outcomes analysis, and model change management. It does not cover initial model development or pre-implementation independent validation, which are governed by SOP-FIN-012 (Model Development and Validation). All personnel involved in the development, implementation, validation, monitoring, and governance of these models, including full-time employees, contractors, and third-party vendors, are bound by this SOP.

### 1.3 Applicability

This SOP is binding for all Meridian Health Technologies, Inc. global offices, including Boston (HQ), London, Berlin, Singapore, and Toronto, for models deployed in the respective regions, provided they do not conflict with binding local regulations. Where a local standard is more stringent, the more stringent standard applies.

---

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
| :--- | :--- |
| **Back-Testing** | The systematic process of comparing a model’s predicted risk metrics against realized outcomes during a specific observation period. |
| **SR 11-7** | Federal Reserve Supervisory Guidance (SR Letter 11-7) on Model Risk Management. |
| **NIST AI RMF** | National Institute of Standards and Technology Artificial Intelligence Risk Management Framework 1.0. |
| **Model Risk Tier** | A classification (Tier 1, 2, 3) assigned in the MMIS based on a model's complexity, business materiality, and regulatory criticality. Tier 1 is the highest risk. |
| **Performance Window (PW)** | A fixed, retrospective time period (e.g., 12 months) over which model outcomes are realized and analyzed. |
| **Outflow Period** | The time required for a prediction made at a point in time to fully materialize into a realized outcome (e.g., 18 months for a 12-month loan to fully mature to "default" or "paid in full"). |
| **Observation Point (OP)** | The specific date on which a set of model predictions is extracted for back-testing. |
| **Probability of Default (PD)** | The likelihood that a borrower will fail to make a required payment within a defined period. |
| **Loss Given Default (LGD)** | The estimated economic loss incurred if a default event occurs, expressed as a percentage of the Exposure at Default (EAD). |
| **Exposure at Default (EAD)** | The total outstanding principal balance expected to be owed at the time of default. |
| **Rank Ordering Power (Kendall's Tau)** | A statistical metric measuring the model’s ability to correctly rank-order obligors from riskiest to safest. |
| **Population Stability Index (PSI)** | A metric measuring the shift in the distribution of model input features or scores between the development sample and the current production population. |
| **Characteristic Stability Index (CSI)** | A granular version of PSI, measuring distributional shift for individual model input features. |
| **Recalibration Trigger** | A predefined quantitative threshold or qualitative finding that, when breached, mandates a formal model recalibration or redevelopment activity. |
| **MMIS** | Meridian Model Inventory System, the centralized system of record for all AI and non-AI models at Meridian, managed by the Chief AI Officer's team. |
| **HP-AMS** | HealthPay Analytics & Monitoring Suite, the primary dashboard for real-time and batch model performance monitoring. |
| **MRG** | Model Risk Governance committee, a sub-committee of the Board-level AI Governance Committee. |
| **MAD** | Mean Absolute Difference, a measure of calibration error between predicted and observed default rates. |
| **Adverse Impact Ratio (AIR)** | A fairness metric measuring the ratio of adverse outcomes (e.g., credit denial) for a protected group relative to a control group. An AIR below 0.80 is a mandatory investigation trigger. |

---

## 3. Roles and Responsibilities

The following responsibility matrix formalizes the segregation of duties mandatory for effective model risk management. The matrix follows a RACI model (Responsible, Accountable, Consulted, Informed).

| Role | Responsibility | RACI |
| :--- | :--- | :--- |
| **VP of Financial Services (Robert Liu)** | Ultimate ownership of all HealthPay models, their business performance, and risk appetite. Approves exceptions to recalibration timelines for Tier 3 models. | A (Tier 3), I (Tier 1-2) |
| **Chief Financial Officer (James Thornton)** | Approver for all Tier 1 model changes, recalibration plans, and material exception requests. Chairs the MRG. | A (Tier 1) |
| **Head of Model Risk Management (Reporting to CRO)** | Independent authority responsible for defining back-testing methodology, validating findings, and recommending model actions. Is not involved in model development. | R, A (Validation) |
| **Lead Model Developer, Financial Services** | Executes the scheduled back-testing procedures according to this SOP, produces the Back-Testing Analysis Package (BTAP), and implements recalibration activities. | R (Execution) |
| **Chief AI Officer (Dr. Marcus Rivera)** | Accountable for the governance, risk tiering, and lifecycle status of all models in the MMIS. Ensures NIST AI RMF principles are mapped to risk controls. | A (Governance) |
| **Chief Information Security Officer (Rachel Kim)** | Ensures the security and integrity of data pipelines (Kafka, Snowflake) used for back-testing data extraction. | C |
| **Chief Privacy Officer/DPO (Dr. Klaus Weber)** | Ensures that the use of data for back-testing, particularly claims-based models, complies with HIPAA, GDPR, and data usage consent agreements. | C |
| **Data Engineering Lead (Platform Team)** | Responsible for maintaining the integrity of the "Single Source of Truth" data tables in Snowflake (`FIN.MODEL_LOG` and `FIN.OUTCOMES_FACT`) used for all back-testing. | R (Data) |
| **VP of IT Operations (Samantha Torres)** | Ensures compute resources (AWS SageMaker, MLflow) are provisioned and available for scheduled back-testing jobs. | R (Infrastructure) |
| **Internal Audit** | Conducts periodic, independent audits of the adherence to this SOP and the effectiveness of the back-testing control environment. | I |

---

## 4. Policy Statements

The following policy statements represent the non-discretionary commitments governing credit risk model back-testing at Meridian Health Technologies.

1.  **Mandatory Cadence:** All Tier 1 credit risk models shall undergo a full, independent back-test no less than **annually**. Tier 2 models shall undergo back-testing **semi-annually**. Tier 3 models shall undergo back-testing **semi-annually**, with a reduced-scope Quarterly Performance Review (QPR) at the end of each intervening quarter.

2.  **Independent Execution:** Back-testing activities for Tier 1 and Tier 2 models must be executed or independently replicated by the Model Risk Management (MRM) team, separate from the model development team. The MRM team must provide a written challenge opinion on all Tier 1 back-tests. For Tier 3 models, the development team may execute the back-test, but the MRM team must independently review and approve the final Back-Testing Analysis Package (BTAP).

3.  **Representative Data:** Back-testing must be conducted on an "out-of-time" sample—a period not used in the model’s development or its most recent recalibration. The sample must be representative of the current portfolio and macroeconomic conditions.

4.  **Comprehensive Outcomes Analysis:** The back-test must assess both **discriminatory power** (is the model effective at separating good and bad outcomes?) and **calibration accuracy** (do predicted event rates match observed event rates?).

5.  **Fair Lending Assessment:** Every back-test must include a quantitative fair lending analysis, reporting Adverse Impact Ratios (AIR) across age, race, gender, and geography (where legally permissible to collect and analyze such data, and in strict accordance with SOP-PRIV-028). Any statistically significant disparity is a mandatory recalibration trigger, irrespective of overall model accuracy.

6.  **Transparent Reporting:** The results of every back-test, including all key metrics and the MRM challenge opinion, must be documented in a standardized BTAP and presented to the Model Risk Governance (MRG) committee.

7.  **Remediation Override:** The Chief Financial Officer, in consultation with the Chief AI Officer and General Counsel, holds the authority to mandate the immediate suspension ("kill switch") of any model deemed to be causing consumer harm, financial loss, or material reputational risk, overriding scheduled remediation timelines specified in this SOP.

---

## 5. Detailed Procedures

This section outlines the step-by-step operational procedures for executing a credit risk model back-test. The process maps to the "Map," "Measure," and "Manage" functions of the NIST AI RMF, incorporating risk identification (MAP), quantitative analysis (MEASURE), and response triggers (MANAGE).

### 5.1 Initiation and Data Extraction

This stage is triggered automatically via a Jira ticket generated by the HealthPay Analytics & Monitoring Suite (HP-AMS) 30 business days before the scheduled back-test date for a given model, as recorded in the MMIS.

#### 5.1.1 Scope Definition in MMIS
The Lead Model Developer, in consultation with the MRM Lead, confirms the back-test scope in the MMIS Back-Testing Module:
- **Model ID & Version:** (e.g., `FIN-ML-005 v2.1`)
- **Observation Point (OP):** The "as-of" date for extracting model predictions (e.g., `2025-06-30`).
- **Prediction Window (PW):** The outcome realization window (e.g., `12M` for a 12-month PD model).
- **Outflow Window:** The total time allowed for outcomes to materialize (e.g., `OP - 18M`). Only predictions made on or before this date can be included to ensure the full outcome window has elapsed.
- **Sample Selection Criteria:** Filters for portfolio, product type, and geography.

#### 5.1.2 Data Extraction Technical Protocol
The Data Engineering Lead executes the following validated Snowflake SQL template to extract data into the secured `FIN.BACKTEST_SANDBOX` schema:

```sql
-- SOP-FIN-018 Standard Extraction Query
-- Date: {RUN_DATE}
-- Model: {MODEL_ID_Version}

SELECT
    m.transaction_id,
    m.application_date,
    m.prediction_date,
    m.model_score,
    m.predicted_pd,
    m.predicted_lgd,
    m.predicted_ead,
    m.decision_code, -- 'APPROVE', 'DECLINE', etc.
    o.realized_outcome, -- 'DEFAULT', 'PIF', 'PD-90', 'PIF-EARLY'
    o.outcome_date,
    o.actual_loss_amount,
    o.exposure_at_default
FROM
    FIN.MODEL_LOG m
LEFT JOIN
    FIN.OUTCOMES_FACT o
ON
    m.transaction_id = o.transaction_id
WHERE
    m.model_id = '{MODEL_ID}'
    AND m.model_version = '{VERSION}'
    AND m.prediction_date <= DATEADD(month, -{OUTFLOW_MONTHS}, '{OP_DATE}')
    AND m.prediction_date > DATEADD(month, -{OUTFLOW_MONTHS + PW_MONTHS}, '{OP_DATE}')
    AND m.environment = 'PRODUCTION'
    AND m.application_date BETWEEN '{SAMPLE_START}' AND '{SAMPLE_END}';
```

#### 5.1.3 Data Integrity and Exclusions
Before any analysis, the following integrity checks must be performed and documented in the BTAP:
- **Completeness Check:** Verify that the `realized_outcome` field is populated for >98% of records drawn from the outflow period. If not, the back-test is placed on hold and the cause of missing data (e.g., loan sold to a third party, data pipeline error) is investigated per SOP-FIN-009 (Data Quality Incident Management).
- **Outlier Analysis:** Identify and review accounts where `actual_loss_amount` exceeds 10x the predicted EAD. These must be individually reviewed but never automatically excluded unless proven to be a data entry error.
- **Exclusion Documentation:** All excluded records, with justification, must be detailed in an appendix to the BTAP. No records may be excluded for the sole reason of being an adverse model outcome (e.g., a high-value default).

### 5.2 Quantitative Analysis: Discriminatory Power

This analysis must be performed on the entire sample and segmented by critical subgroups (age, geography, credit score band).

#### 5.2.1 Rank Ordering Metrics
- **Kendall's Tau-b:** Calculate the rank correlation between the predicted PD and the binary realized default outcome.
    - *Tier 1 Target: > 0.40*
    - *Tier 2/3 Target: > 0.30*
- **Gini Coefficient / AUROC:** Calculate the Area Under the Receiver Operating Characteristic curve.
    - *Tier 1 Target: > 0.75*
    - *Tier 2/3 Target: > 0.70*
- **Procedure:** Calculate these metrics for each performance window. Plot the AUROC trajectory over time. A monotonic declining AUROC over three consecutive back-tests (e.g., annual tests for 3 years) is a qualitative recalibration trigger, even if the absolute metric remains above the threshold.

### 5.3 Quantitative Analysis: Calibration and Accuracy

This analysis compares predicted event rates to realized event rates across the probability distribution.

#### 5.3.1 Binned Probability Analysis
1.  Bin all predictions into deciles (10 equal groups) based on predicted PD.
2.  For each decile, calculate the mean predicted PD and the realized default rate.
3.  Plot these points: X-axis is mean predicted PD, Y-axis is realized default rate. A well-calibrated model will have these points near the 45-degree line.
4.  **Calibration Metric (MAD):** Calculate the Mean Absolute Difference between predicted and realized rates across deciles.
    - *Tier 1/2 Target: MAD < 0.015*
    - *Tier 3 Target: MAD < 0.025*

#### 5.3.2 Hosmer-Lemeshow (H-L) Goodness-of-Fit Test
- For PD models, calculate the H-L statistic across deciles.
- **Procedure:** A p-value < 0.05 on the H-L test indicates poor calibration and is a **mandatory recalibration trigger** for all model tiers, regardless of MAD performance.

### 5.4 Quantitative Analysis: Stability and Drift

This analysis measures the similarity between the development/validation data and the current production environment.

#### 5.4.1 Population Stability Index (PSI)
1.  Use the development sample’s score distribution as the "expected" baseline.
2.  Use the current back-test sample’s score distribution as the "actual" distribution.
3.  Calculate PSI:
    - *PSI < 0.10:* Insignificant shift. No action.
    - *0.10 <= PSI < 0.25:* Moderate shift. Mandates enhanced monitoring (monthly) and a qualitative root-cause analysis.
    - *PSI >= 0.25:* Significant shift. **Mandatory recalibration trigger.**

#### 5.4.2 Characteristic Stability Index (CSI)
- For the top 10 features by information value (IV) in the model, calculate the CSI using the same thresholds as PSI.
- Provide a heatmap of CSI values in the BTAP. Any single feature with CSI > 0.25 requires an investigation into the root cause (e.g., change in underwriting policy, new product launch, macroeconomic shock).

### 5.5 Fair Lending and Bias Analysis

This procedure addresses the MAP function of the NIST AI RMF by analyzing risk for different demographic segments. It is governed by strict data handling protocols as prescribed by our Privacy Office (SOP-PRIV-028). All analysis must be performed on a secure, access-restricted Snowflake environment with query-level audit logging.

**Procedure:**
1.  **Proxy Matching (Where Applicable):** Where direct demographic data is not legally collected (e.g., credit applications in the US), the analysis must use Bayesian Improved Surname and Geocoding (BISG) proxy methodology to assign proxy probabilities for race and ethnicity. This proxy data is used exclusively for bias testing and is not stored outside the designated analytics sandbox.
2.  **Adverse Impact Ratio (AIR) Calculation:** Define the control group as the "most favored" demographic segment by approval rate. Calculate the AIR for each other protected group.
    - AIR = (Approval Rate for Target Group) / (Approval Rate for Control Group).
3.  **Thresholds and Triggers:**
    - **AIR <= 0.80:** **Mandatory Recalibration Trigger.** The MRM team must immediately open a high-priority finding.
    - **0.80 < AIR < 0.90:** Mandates an "explainability deep-dive." A SHAP (SHapley Additive exPlanations) analysis must be conducted to identify the top contributing features driving the disparity and assess their business necessity.
4.  **Documentation:** All fairness results, including proxy methodology and SHAP analysis, must be documented in a "Fairness Addendum" to the BTAP, reviewed by the General Counsel and CPO before submission to the MRG.

### 5.6 Back-Testing Analysis Package (BTAP) Completion and Review

The BTAP is the formal, auditable record of the back-test. The Lead Model Developer completes the BTAP template in the MMIS.

#### 5.6.1 Mandatory BTAP Contents
1.  **Executive Summary:** A brief (1-page) narrative summarizing model health, key findings, and recommended actions.
2.  **Procedure Log:** Timestamps, executor names, and script run-IDs for execution of all procedures in Sections 5.1-5.5.
3.  **Dashboard Graphics:** Direct, traceable exports from Datadog and LangSmith showing the metrics described:
    - AUROC trajectory chart (Datadog RUM dashboard).
    - Calibration plot (Binned PD vs. Realized).
    - PSI/CSI gauge charts with amber/red threshold indicators.
4.  **Metric Sign-Off Table:**
| Metric | Target | Actual | Status | Comment |
| :--- | :--- | :--- | :--- | :--- |
| Kendall's Tau | >0.40 | 0.43 | PASS | |
| AUROC | >0.75 | 0.78 | PASS | |
| MAD | <0.015 | 0.018 | FAIL | Underestimation of risk in high-score deciles. |
| H-L p-value | >0.05 | 0.11 | PASS | |
| PSI | <0.25 | 0.15 | WARN | Shift driven by new 'Medical Residency Refinance' product. |
| AIR (Proxy) | >0.80 | 0.75 | FAIL | Impact identified in BISG-proxy for Black applicants. |
5.  **Findings Register:** A numbered list of all findings (failures, warnings, and observations), mapped to a recommended remediation plan with clear timelines.
6.  **MRM Challenge Opinion:** For Tier 1 and Tier 2, a formal written opinion from the Head of Model Risk Management, either concurring with the findings or providing a dissenting view with a separate risk assessment.

#### 5.6.2 Formal Review and Approval Flow
The completed BTAP must be routed via ServiceNow for approval:
1.  **Submitter:** Lead Model Developer.
2.  **Independent Review:** Head of Model Risk Management (for Tier 1 & 2: mandatory 10 business day review SLA; for Tier 3: 5 business day SLA).
3.  **Business Approver:** Robert Liu, VP of Financial Services.
4.  **Final Approver:** James Thornton, CFO (for Tier 1; for Tier 2/3, approval authority rests with the VP of Financial Services). The Model Risk Governance (MRG) committee receives the approved BTAP at its next scheduled meeting.

---

## 6. Controls and Safeguards

The integrity of the back-testing process is protected by a multi-layered set of administrative and technical controls, directly mapped to the requirements of SR 11-7, sections "Model Validation" and "Ongoing Monitoring."

### 6.1 Administrative Controls

| Control ID | Control Description | SR 11-7 Alignment | Implementation |
| :--- | :--- | :--- | :--- |
| **ADM-01** | Segregation of Duties | Validation Standards | Enforced by system permissions. The MMIS prevents the same user account that confirms the "Final Back-Test Execution" from performing the "Independent Review Approval." |
| **ADM-02** | Inventory and Risk Tiering | Model Oversight | All models in scope are registered in MMIS. The CAIO's office annually reviews and signs off on the risk tier (Tier 1, 2, 3) of each model based on a standardized rubric in SOP-FIN-005 (Model Risk Tiering). |
| **ADM-03** | Board-Level Reporting | Board Reporting | A summarized model health dashboard, aggregating findings from this SOP, is presented to the Board-level AI Governance Committee semiannually by the CFO. |
| **ADM-04** | Change Management | Model Change Protocol | Any code modification to a production model requires a change request in ServiceNow pre-attached with a "mini" back-test comparing the proposed model against the champion model on a static dataset. |

### 6.2 Technical Controls

| Control ID | Control Description | Implementation Detail |
| :--- | :--- | :--- |
| **TEC-01** | Immutable Audit Trail | The `FIN.MODEL_LOG` table in Snowflake is append-only. No DELETE or UPDATE transactions are permitted on the `predicted_pd`, `decision_code`, and related fields. All changes to model code in production require a new version, leaving the old version's predictions untouched. |
| **TEC-02** | Automated Metric Logging | Every model prediction event is instrumented using a custom LangChain/TorchServe callback that fires a metric event to Datadog. The "HealthPay Model Health" dashboard in Datadog visualizes real-time PSI and drift against the development baseline. Alerts are configured at the thresholds defined in Section 5.4. |
| **TEC-03** | Model Risk Tier Mapping | The NIST AI RMF MAP function is partially operationalized through an automated system in the MMIS. Every new model requires a registration form (FM-MOD-001) that captures its complexity, training data, and business use case. However, the mapping of all AI models to their specific AI risk categories (e.g., toxicity, misinformation) is not yet a fully automated, enforced workflow. The categorization is currently a manual, non-blocking field in the MMIS for non-credit models, meaning not all legacy MedInsight models have an assigned NIST AI risk profile in the database. |
| **TEC-04** | Data Leakage Prevention | A static "cutoff" checkpoint for all feature creation scripts is enforced in the MLflow tracking server. Back-tests run in a separate AWS account (`fin-model-validation`) with `ReadOnlyAccess` to the production Snowflake views, as enforced by IAM policies. This prevents accidental training on future data. |
| **TEC-05** | Container Image Signing | All model serving images (Docker) used in production EKS clusters are signed using AWS Signer. A Kubernetes Admission Controller (OPA/Gatekeeper) blocks unsigned images. SBOMs for these container images are generated at build time via the `syft` tool and stored in an OCI-compliant registry (Harbor). |

---

## 7. Monitoring, Metrics, and Reporting

Continuous monitoring is essential for the early detection of performance degradation between scheduled back-tests. This section details the ongoing monitoring controls, the quantitative SLAs, and the reporting and governance cadences required by SR 11-7's pillars on ongoing monitoring and board reporting.

### 7.1 Continuous Performance Monitoring (HP-AMS)

The HealthPay Analytics & Monitoring Suite (HP-AMS) is the central nervous system for model health. Data flows from production inference services (via LangChain callback integration) into a Snowflake stream, and finally into Datadog for real-time visualization.

**Tier 1 & Tier 2 Model Dashboard (Real-Time):**
- **Drift Monitor:** Real-time PSI for the top 5 model features, using the development/validation sample as the baseline. A drift severity score (1-5) is displayed.
- **Score Distribution:** Live histogram of the Meridian HealthPay Score (MHPS) with overlaid statistical process control (SPC) bands set at ±2 standard deviations from the historical mean.
- **System Health SLA:** Model inference latency (p95 < 200ms) and success rate (> 99.95%). A breach on latency triggers an alert to the MLOps team (L2).

**Tier 3 Model Dashboard (Batch, refreshed daily):**
- **Stability Metrics:** A daily batch job calculates PSI and a simplified MAD (Mean Absolute Difference) on a static, recent 1-month rolling window.
- **Volume Spike Detector:** An alert is generated if the daily application volume processed by a single model fluctuates by > 50% above the trailing 30-day average, triggering an investigation into the cause of the anomaly (e.g., new marketing campaign, product launch).

### 7.2 Key Performance Indicators (KPIs) and Service Level Agreements (SLAs)

The following SLAs are non-negotiable performance targets.

| KPI / SLA | Category | Measurement Period | Target / Threshold | Consequence of Breach |
| :--- | :--- | :--- | :--- | :--- |
| **BTAP Completion Timeliness** | Process Adherence | Per Scheduled Back-Test | 100% completed by MRG meeting date | Automatic "High" severity governance finding, escalation to CAIO. |
| **Model Kill-Switch Activation Time** | Risk Mitigation | Per Incident | Time to confirm suspension < 1 business hour from officer decision. | Post-incident RCA required; infrastructure review mandated. |
| **Recalibration Cycle Time** | Remediation Efficacy | Per Recalibration Trigger | Tier 1: 90 days. Tier 2: 60 days. Tier 3: 45 days. | Weekly status reporting to MRG; risk-acceptance extension required from CFO. |
| **Fair Lending AIR Threshold** | Fairness | Per Back-Test | AIR > 0.80 for all protected groups. Stat p-value > 0.05 for disparity. | Immediate suspension of a discriminatory model path if a targeted fix is not live within 15 business days. |
| **Data Completeness Rate** | Data Quality | Daily Snapshot | Outcome field populated for >98% of matured predictions. | Back-testing for the affected cohort is "On Hold" and highlighted in the next MRG deck. |

### 7.3 Reporting Cadence

| Report Type | Audience | Frequency | Responsibility | Key Content |
| :--- | :--- | :--- | :--- | :--- |
| **Back-Testing Analysis Package (BTAP)** | MRG Committee | Per Model Schedule (Annually/Semi-Annually) | Lead Model Developer, MRM Lead | Full quantitative analysis, findings, MRM challenge opinion, remediation plan. |
| **Quarterly Performance Review (QPR)** | VP of Financial Services | Quarterly (for Tier 3 models not in a full back-test cycle) | Lead Model Developer | Abbreviated scorecard: PSI, CSI for top 3 features, volume, MAD on a trailing 3-month window. |
| **Model Health Summary** | Board AI Governance Committee | Semi-Annually | Chief AI Officer, CFO | Tier 1 model status summary, aggregate drift metrics across portfolio, top material findings, remediation status heatmap. |
| **Incident Flash Report** | CISO, CFO, General Counsel | Ad-Hoc (within 24 hours of a critical finding) | Head of MRM | A standardized one-pager detailing a critical model finding, its business impact, and immediate containment actions. |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Request Process

A formal exception is required for any deviation from the mandatory procedures, timelines, or control requirements specified in this SOP. Common exception scenarios include:
- Inability to meet a recalibration deadline (e.g., Tier 1 model requiring >90 days).
- An incomplete back-test due to unresolvable data gaps (<98% completeness).
- A request by the VP of Financial Services to continue using a model that has breached a "Warning" threshold but not a "Mandatory Recalibration" trigger, without invoking the full recalibration process.

**Procedure:**
1.  **Initiation:** The Lead Model Developer documents the justification for the exception in an "SOP-FIN-018 Exception Request" (Form ID: FIN-018-EXC) within ServiceNow.
2.  **Risk Assessment:** The MRM Lead must append an independent risk assessment to the ticket, quantifying the incremental model risk (e.g., "Estimated additional Expected Loss over the 30-day exception period: $75,000").
3.  **Approval Workflow:**
    - **Tier 3:** Approval by VP of Financial Services (Robert Liu).
    - **Tier 2:** Approval by VP of Financial Services and Chief AI Officer (Robert Liu & Dr. Marcus Rivera).
    - **Tier 1:** Approval by Chief Financial Officer (James Thornton). Any Tier 1 exception must be reviewed by the next MRG committee meeting.
4.  **Sunsetting:** All approved exceptions must have a hard expiration date, not exceeding 90 days (or one more back-test cycle), upon which the exception is automatically closed and the standard policy applies.

### 8.2 Escalation Path

If the independent MRM challenge opinion documents a significant risk that the model development team and VP of Financial Services plan to accept without remediation, the Head of Model Risk Management is empowered and obligated to escalate the matter directly to the Chief Risk Officer and the Audit Committee Chair. This follows the formal "Risk Escalation & Acceptance" policy as defined in SOP-RISK-001.

---

## 9. Training Requirements

All personnel with assigned responsibilities in Section 3 must complete specialized, role-based training to maintain their authorization for access to model development and validation tools.

| Training Module | Mandatory Audience | Frequency | Provider / System |
| :--- | :--- | :--- | :--- |
| **SR 11-7 & Model Risk Governance** | ALL roles (R, A, C, I) from Section 3. | Annually | Meridian LMS (Workday Learning) |
| **SOP-FIN-018 Deep Dive & Practical Lab** | Lead Model Developers, Data Engineering Lead, MRM Analysts. | Annually | Instructor-led; includes a lab on executing a mock back-test in the `FIN.BACKTEST_SANDBOX` environment. |
| **Fair Lending & Proxying Methodologies** | MRM Analysts, Model Developers working on Tier 1 models, CPO delegates. | Semi-Annually | Instructor-led by Privacy Office; covers legal frameworks, BISG methodology, and AIR calculation. |
| **NIST AI RMF in Practice** | Chief AI Officer, MRM Analysts, Model Developers. | Annually | Asynchronous course covering the MAP, MEASURE, and MANAGE functions and their mapping to internal tools like MMIS. |

**Tracking:** Training completion is tracked via the Workday Learning platform. Access to the Meridian Model Inventory System (MMIS) and the Snowflake `FIN.BACKTEST_SANDBOX` is contingent upon the status of assigned training being "Complete." System access is automatically revoked 30 days past the training due date.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
| :--- | :--- | :--- |
| **SOP-FIN-005** | Model Risk Tiering Methodology | Defines the rubric for determining if a model is Tier 1, 2, or 3. |
| **SOP-FIN-012** | Model Development and Independent Validation | Governs the lifecycle prior to this SOP's ongoing monitoring phase. |
| **SOP-FIN-009** | Data Quality Incident Management | Procedure to follow when data completeness checks in Section 5.1.3 fail. |
| **SOP-PRIV-028** | Use of Sensitive Data for Bias Testing | Governs the strict data handling, proxy methodology, and access controls for the Fair Lending Analysis (Section 5.5). |
| **SOP-AI-022** | AI Model Registry Standards | Defines technical requirements for registering a model in the MMIS, including model cards and metadata. |
| **SOP-TECH-110** | CI/CD Pipeline Security & Promotion | Procedure for promoting a recalibrated model artifact from the staging environment to production. |
| **SOP-RISK-001** | Enterprise Risk Escalation and Acceptance | The formal policy invoked during the Head of MRM's escalation (Section 8.2). |

### 10.2 External Regulatory and Standards References

- **Board of Governors of the Federal Reserve System. (2011). SR Letter 11-7: Supervisory Guidance on Model Risk Management.**
- **National Institute of Standards and Technology. (2023). Artificial Intelligence Risk Management Framework (AI RMF 1.0). NIST AI 100-1.** *Specifically, the MAP, MEASURE, and MANAGE functions serve as foundational pillars for our procedural organization.*
- **European Union. (2024). Regulation (EU) 2024/1689 (Artificial Intelligence Act).** *Applicable to models processing data of EU residents from our Berlin office.*
- **Interagency Guidelines Establishing Standards for Safety and Soundness.** *Appendix A, Operational and Managerial Standards.*

---

## 11. Revision History

| Version | Date | Author/Owner | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2021-03-15 | Sarah Jenkins (former Head of Fin. Eng.) | Initial creation. Covered origination models only. Annual back-testing. |
| 2.0 | 2022-11-01 | Robert Liu, VP of Fin. Services | Major rewrite. Expanded scope to all credit models per SR 11-7. Introduced Tiered model risk framework and semi-annual cadence. Added Section 8 (Exceptions). |
| 2.5 | 2023-08-22 | Robert Liu, VP of Fin. Services | Interim update. Added Fair Lending (AIR) analysis requirement after an internal audit finding. Added Section 5.5. Upgraded PSI threshold logic. |
| 3.0 | 2024-04-10 | Robert Liu, VP of Fin. Services | Annual review. Integrated NIST AI RMF principles (MAP, MEASURE, MANAGE). Migrated data extraction to new Snowflake `FIN.MODEL_LOG`. Added automated controls. |
| 3.1 | 2024-11-15 | Robert Liu, VP of Fin. Services | Post-regulatory exam update. Enhanced segregation of duties controls (ADM-01). Formalized MRM Challenge Opinion requirement for Tier 1/2. |
| 3.2 | 2025-02-05 | Robert Liu, VP of Fin. Services | Minor revision. Updated all role holders and committee names to align with 2025 organizational structure. Clarified container image signing (TEC-05). |
| 3.3 | 2025-06-18 | Robert Liu, VP of Fin. Services | Major revision. Extended scope to new Claims-Based Credit Assessment Models. Added new definitions for Outflow Period. Updated recalibration SLAs in Section 7. Formalized the Fairness Addendum. |
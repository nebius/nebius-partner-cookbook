---
sop_id: "SOP-CLIN-005"
title: "Diagnostic AI Accuracy and Calibration"
business_unit: "Clinical AI Products"
version: "4.6"
effective_date: "2024-06-26"
last_reviewed: "2025-11-09"
next_review: "2026-05-05"
owner: "Dr. Aisha Okafor, VP of Clinical AI Products"
approver: "Dr. Priya Patel, Chief Medical Officer"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: Diagnostic AI Accuracy and Calibration
## SOP-CLIN-005 | Version 4.6

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework and mandatory processes for ensuring, measuring, and maintaining the accuracy and statistical calibration of all diagnostic and clinical decision support Artificial Intelligence (AI) models developed, deployed, or maintained by the Clinical AI Products business unit of Meridian Health Technologies, Inc. ("Meridian"). The purpose is to guarantee that model outputs are statistically reliable, clinically safe, and interpretable by qualified clinicians, thereby mitigating risks of misdiagnosis, delayed treatment, or inappropriate clinical pathway selection.

### 1.2 Scope

This SOP applies to:

- **All personnel** within the Clinical AI Products division, including data scientists, machine learning (ML) engineers, clinical validators, product managers, and quality assurance specialists.
- **All AI systems** classified as Class II or Class III medical devices under FDA regulations, high-risk AI systems under the EU AI Act (Annex III), or any system whose output directly informs a clinical decision, including but not limited to:
    - Diagnostic imaging analysis models (radiology, pathology, ophthalmology).
    - Patient risk scoring algorithms (sepsis prediction, readmission risk, mortality risk).
    - Adverse event prediction systems.
    - Clinical deterioration early warning systems.
- **All phases of the AI model lifecycle**, from initial development and pre-clinical validation through deployment, post-market surveillance, and decommissioning.
- **All deployment environments**, including cloud-based inference endpoints on the Meridian SaaS Platform (AWS us-east-1, eu-west-1) and on-premise containerized deployments at client sites.

This SOP is subsidiary to the overarching AI Governance Framework and operates in conjunction with SOP-SOFT-002 (Medical Device Software Lifecycle) and SOP-DATA-001 (Clinical Data Integrity and Management).

---

## 2. Definitions and Acronyms

| Term | Definition |
| :--- | :--- |
| **Accuracy** | The proportion of correct predictions (both true positives and true negatives) among the total number of cases examined. |
| **Adverse Event** | Any untoward medical occurrence in a patient or clinical trial subject administered a diagnostic test, which does not necessarily have a causal relationship with the test itself. |
| **AUC-ROC** | Area Under the Receiver Operating Characteristic Curve; a performance metric measuring a model's ability to distinguish between classes across all thresholds. |
| **Calibration** | The agreement between observed outcomes and model-predicted probabilities. A perfectly calibrated model that predicts a 20% risk will see the event occur in exactly 20% of similar cases. |
| **Calibration Curve (Reliability Diagram)** | A graphical plot of observed event frequency versus predicted probability, used to visually assess calibration. |
| **Calibration-in-the-Large (CITL)** | A calibration metric assessing whether predicted probabilities are systematically too high or too low. |
| **Clinical Decision Support (CDS)** | A system that provides clinicians, staff, patients, or other individuals with knowledge and person-specific information, intelligently filtered or presented at appropriate times, to enhance health and health care. |
| **Confidence Interval (CI)** | A range of values that is likely to contain the true value of an unknown population parameter (e.g., 95% CI for AUC). |
| **Data Drift** | A change in the statistical properties of the model's input features over time. |
| **Concept Drift** | A change in the statistical relationship between the model's input features and the target outcome over time. |
| **Expected Calibration Error (ECE)** | A primary metric summarizing calibration performance by computing the weighted average of the absolute difference between accuracy and confidence across prediction bins. |
| **Ground Truth** | The definitive, verified clinical outcome, as determined through chart review by a qualified clinical panel, adjudicated diagnosis, or confirmed biomarker, against which model predictions are compared. |
| **Human Oversight** | The mechanisms by which a qualified human clinician reviews, interprets, and can act upon AI model outputs. |
| **Negative Predictive Value (NPV)** | The probability that a subject with a negative screening test truly does not have the disease. |
| **Positive Predictive Value (PPV)** | The probability that a subject with a positive screening test truly has the disease. |
| **Sensitivity (Recall)** | The proportion of actual positives that are correctly identified by the model. |
| **Specificity** | The proportion of actual negatives that are correctly identified by the model. |
| **Subgroup** | A subset of the patient population, defined by protected or clinically significant attributes (e.g., age decile, biological sex, ethnicity, comorbidity status, insurance type). |

---

## 3. Roles and Responsibilities

The following RACI matrix defines the roles and responsibilities for the lifecycle of a diagnostic AI model. No single individual may hold contradictory roles (e.g., Developer and Independent Validator) for the same model.

| Activity / Task | VP Clinical AI (Dr. Aisha Okafor) | Lead Data Scientist | Clinical Validation Lead | Quality Assurance (QA) | Chief Medical Officer (Dr. Priya Patel) | Medical Advisory Board |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Protocol Development** | A | R | C | I | I | I |
| **Model Training** | I | R | C | I | I | I |
| **Pre-Clinical Accuracy Testing** | I | R | C | I | I | I |
| **Independent Clinical Validation** | I | I | R | A | C | C |
| **Calibration Assessment** | I | C | R | A | I | I |
| **Equity & Fairness Assessment** | A | R | R | I | I | C |
| **Risk Classification per EU AI Act** | A | C | C | I | I | I |
| **Approval for Clinical Use** | A | I | C | I | R | C |
| **Post-Market Monitoring Review** | A | C | C | R | I | I |
| **Exception Approval** | R | I | I | I | A | I |

**Key:**
- **R** = Responsible (The Doer)
- **A** = Accountable (The Approver)
- **C** = Consulted (Two-way communication)
- **I** = Informed (One-way communication)

### 3.1 Key Role Descriptions

- **VP of Clinical AI Products:** Holds ultimate accountability for the business unit's compliance with this SOP. Approves all model release candidates and exception requests.
- **Lead Data Scientist:** Responsible for the technical execution of model development, including adherence to training protocols, data splitting, and code review.
- **Clinical Validation Lead:** An independent function, separate from the Core Development Team, responsible for designing and executing the prospective or retrospective clinical validation study against ground truth. Must hold a relevant clinical license (e.g., M.D., Pharm.D.).
- **Medical Advisory Board:** An external panel of three to five practicing clinicians from diverse geographic and clinical settings, which serves as the final arbiter of clinical safety and advises on post-market adverse events.

---

## 4. Policy Statements

Meridian Health Technologies adheres to the following mandatory policies for all diagnostic AI systems:

- **4.1 Pre-Clinical Hold:** No AI model or updated model version shall be deployed to a clinical environment, even for silent or shadow mode evaluation, without formal release authorization from the Chief Medical Officer and the VP of Clinical AI Products upon successful completion of independent clinical validation.
- **4.2 Performance Thresholding:** Every diagnostic AI model must be designed and validated against pre-specified, clinically justified minimum performance thresholds for sensitivity, specificity, and PPV/NPV, established in the Clinical Performance Protocol (see Section 5.1).
- **4.3 Calibration as a Gate:** No model shall be released if the Expected Calibration Error (ECE) exceeds 0.05 (5%) on the held-out test set and independent validation cohort. Calibration curves must be reviewed visually and approved as a primary release criterion.
- **4.4 Subgroup Reporting Mandate:** A Subgroup Analysis Report is a mandatory component of the full validation package for every model release (see Section 5.8).
- **4.5 Transparency and Interpretability:** All outputs presented to a clinician must include confidence scores presented in natural language or intuitive visual formats (e.g., "Based on a cohort of N similar patients..."), not raw logarithmic probabilities.
- **4.6 Continuous Monitoring:** Every deployed AI model is subject to continuous, automated technical monitoring for data drift and periodic (monthly) clinical monitoring against ground truth, as detailed in Section 7.
- **4.7 Human Control:** AI-generated diagnostic outputs are advisory. The licensed healthcare professional at the point of care remains wholly and solely responsible for all clinical interpretations and decisions.

---

## 5. Detailed Procedures

This section outlines the end-to-end procedure, from protocol definition through deployment and monitoring.

### 5.1 Clinical Performance Protocol (Template: FRM-CLIN-005-01)

Before any model training or data analysis begins, the Lead Data Scientist and Clinical Validation Lead must co-author a Clinical Performance Protocol. This protocol is a locked, version-controlled document in Meridian’s Quality Management System (Greenlight QMS). The template `FRM-CLIN-005-01` must include the following sections:

1.  **Clinical Statement:** A narrative description of the intended clinical use, patient population, and clinical workflow.
2.  **Ground Truth Definition:** A precise, reproducible definition of the gold standard for diagnosis. For example: "Pneumonia is defined by Board-Certified Radiologist chest x-ray interpretation AND positive sputum culture."
3.  **Minimum Performance Thresholds:** A table of statistically derived, clinically justified minimum values, including:
    - Lower bound of the 95% CI for Sensitivity must be > 0.85.
    - Lower bound of the 95% CI for Specificity must be > 0.80.
    - Expected Calibration Error (ECE) < 0.05.
4.  **Adjudication Strategy:** How conflicting data points will be resolved by the Ground Truth Adjudication Panel.
5.  **Subgroup Definitions:** A pre-specified list of subgroups for analysis (see Section 5.8).

### 5.2 Data Split and Management

1.  The Core Development Data Set must be partitioned into three, strictly walled-off segments using a deterministic, cryptographic, patient-level hashing function to prevent data leakage:
    - **Training Set:** Used for model weight optimization (~60% of data).
    - **Tuning/Calibration Set:** Used for hyperparameter tuning and threshold calibration (~15% of data).
    - **Internal Hold-Out Test Set:** Sequestered data, not used in any training or tuning activity (~25% of data).
2.  The Snowflake Data Governance team (Data Platform unit) is responsible for executing and certifying this split. The hash key is stored in HashiCorp Vault and is not accessible to the Core Development Team.
3.  An **Independent Validation Data Set**, external to the Core Development Data Set and ideally sourced from a different clinical site or geographically distinct patient records, must be acquired. This is the gold standard for the independent validation in Section 5.4.

### 5.3 Pre-Clinical Accuracy and Calibration Assessment

Upon completion of model training on the Training and Tuning sets, the Lead Data Scientist will unlock the Internal Hold-Out Test Set. The following process is mandatory:

1.  **Inference Execution:** Run inference on the full Internal Hold-Out Test Set.
2.  **Metric Calculation:** Compute the following using the Meridian Clinical ML Observability Platform (currently based on a customized MLflow and LangSmith stack):
    - Sensitivity, Specificity, PPV, NPV, AUC-ROC.
    - All metrics must be reported with 95% confidence intervals (CIs), calculated via bootstrapping with 2,000 resamples.
    - ECE and Maximum Calibration Error (MCE).
3.  **Calibration Curve Generation:** Generate and save the calibration curve (reliability diagram) with 95% CIs per bin.
4.  **Technical Gate Review:** The Lead Data Scientist and a peer reviewer conduct a Technical Gate Review, logging results in the `Technical Validation Report`. If ECE > 0.05, the model immediately fails and must be re-calibrated. Accepted techniques include Platt Scaling or Isotonic Regression, which must be performed on the *Tuning/Calibration Set* only.

### 5.4 Independent Clinical Validation

After a model passes the Technical Gate Review, the Clinical Validation Lead, acting independently from the Core Development Team, executes the pre-registered Clinical Validation Study.

1.  **Study Execution:** Run inference on the Independent Validation Data Set.
2.  **Ground Truthing:** For a statistically representative sample of the predictions (stratified by predicted probability decile and score strata), the Clinical Validation Lead will blind-chart-review against the Ground Truth Definition via the Adjudication Panel.
3.  **Statistical Analysis:** Calculate final clinical sensitivity, specificity, PPV, and NPV with 95% CIs.
4.  **Calibration-in-the-Large (CITL) and Calibration Slope** must be checked.
5.  A paired statistical test will formally compare the performance on the Internal Test Set and the Independent Validation Set. A significant degradation (p<0.05) triggers an automatic failure review.
6.  The **Validation Report** (`FRM-CLIN-005-02`) is authored by the Clinical Validation Lead and reviewed by QA, and forms the basis of the release decision.

### 5.5 Human Factors and Oversight Integration

Every Diagnostic AI product must undergo a Human Factors and Oversight Integration evaluation before release. This evaluation, managed by the Product Management and UX Research teams in partnership with the Clinical Validation Lead, will:
1.  Define the specific UI presentation of model outputs, including confidence intervals and clinically actionable phrasing.
2.  Define the intended decision-making workflow. For example: "Clinician views image -> Clinician forms preliminary impression -> Clinician activates AI Assist -> Model output is overlaid -> Clinician documents final interpretation, including a required field for 'AI Concordance (Agree/Disagree with clinically meaningful difference)'."
3.  Validate the "time-to-decision" and "cognitive error rate" in a simulated clinical environment.

### 5.6 Release Authorization

The final release package is a version-controlled bundle in Greenlight QMS, containing:
1.  Approved Clinical Performance Protocol (`FRM-CLIN-005-01`).
2.  Technical Validation Report.
3.  Independent Clinical Validation Report (`FRM-CLIN-005-02`).
4.  Subgroup Analysis Report (`FRM-CLIN-005-03`).
5.  A signed Release Authorization form, bearing the digital signatures of the VP of Clinical AI Products (Accountable) and the Chief Medical Officer (Approver).

### 5.7 Silent Mode and Phased Rollout

All new models must undergo a mandatory **14-day Silent Mode** deployment at initial client sites. During this phase, the model performs inference in the background but its outputs are not displayed to the clinician. The primary goal is to validate:
- Real-world model latency and stability.
- Real-world feature distribution against the training data (Data Drift analysis).
- Silent Mode monitoring data is reviewed daily by the MLOps team, and a summary report is generated at the end of the 14-day period. Any critical drift event pauses the rollout.

### 5.8 Subgroup Analysis (Equity and Fairness Reporting)

A formal Subgroup Analysis Report (`FRM-CLIN-005-03`) is a required component of the validation package.

1.  **Methodology:** For each pre-specified subgroup (defined in Section 5.1), model performance metrics (AUC-ROC, Sensitivity, Specificity, ECE) must be calculated alongside their 95% confidence intervals.
2.  **Analysis:** Subgroups with meaningfully lower performance (defined as a statistically significant difference from the overall population mean at p<0.05, or a clinically significant absolute difference of >5% in sensitivity/specificity) must be flagged.
3.  **Content of Report:**
    - A detailed table of performance metrics per subgroup.
    - Flagged subgroups and an investigational root-cause analysis (e.g., small sample size, pathophysiological variance).
    - An actionable mitigation plan if the flag is sustained upon investigation. This may include mandatory label clarification in the product UI stating the limitations for that sub-cohort, restricting use, or an immediate re-training initiative.

---

## 6. Controls and Safeguards

The following technical and administrative controls are mandatory for all production clinical AI systems.

### 6.1 Technical Controls

| Control ID | Control Name | Description |
| :--- | :--- | :--- |
| **TC-01** | **Input Integrity Guard** | All input features to the model are validated against the training data schema. Invalid input (e.g., an incorrect imaging series type, out-of-range lab value) is rejected; the model explicitly returns an `INPUT_VALIDATION_ERROR` status instead of an erroneous prediction. |
| **TC-02** | **Confidence Thresholding** | Models are configured with a low-confidence threshold. Any prediction where the class probability does not exceed the threshold (e.g., >0.65) is suppressed and a `LOW_CONFIDENCE` status is returned, along with a message: "Analysis indeterminate. Insufficient confidence to provide a specific assessment. Rely on standard clinical examination." |
| **TC-03** | **Data Drift Sentinel** | An automated sentinel process continuously compares the statistical distribution of incoming inference features against the baseline established by the training set. Uses the Two-Sample Kolmogorov-Smirnov test for continuous features and Chi-squared test for categorical features. Drift is declared at p<0.001. |
| **TC-04** | **Adversarial Input Filter** | An input preprocessing step screens for anomalous pixel patterns or metadata that could indicate a corrupted or adversarially crafted input designed to fool the model. |
| **TC-05** | **Immutable Audit Log** | Every single model inference generates an immutable audit log entry stored in a HIPAA-compliant log on the Meridian SaaS Platform. The entry contains: a unique inference ID, a hashed patient ID, model ID and version, input feature hash, predicted probabilities, final rendered output string, and timestamp. |

### 6.2 Administrative Safeguards

- **Peer Review of Code:** No model training or evaluation code shall be committed to the `main` branch without a mandatory peer review by another qualified ML engineer. The peer review must specifically verify adherence to data splitting procedures and independent test set usage.
- **Scheduled Calibration Audits:** On a monthly basis, QA will pull a statistically random sample of a minimum of 200 recent inferences, cross-referencing model output with ultimate clinical outcomes (ground truth) as part of the routine Post-Market Surveillance process.
- **Access Control:** Access to production model weights and the model registry is restricted exclusively to the MLOps Deployment Team. Data Scientists and Developers have no access privileges to production artifacts.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Real-Time Technical Monitoring

The Meridian MLOps Dashboard tracks the following KPIs for all in-service models on a 15-minute rolling basis:

| Metric | Alert Threshold | Critical Alert Threshold |
| :--- | :--- | :--- |
| Response Latency (p99) | > 500ms | > 1200ms for > 5 minutes |
| Error Rate (HTTP 5xx) | > 0.1% of requests | > 1% of requests |
| Low Confidence Rate | > 15% of inferences | > 30% of inferences |
| Data Drift Severity Score | Score change > 0.5 | Score change > 1.0 |

A Critical Alert triggers an immediate incident (per standard ITIL Incident Management process) and pages the Senior Director of MLOps.

### 7.2 Periodic Clinical Monitoring (Post-Market Surveillance)

On a **monthly** basis, for every deployed model, the Clinical Validation Lead will oversee the following:

1.  **Retrospective Review:** QA pulls an automated sample of 200 completed patient encounters where the AI provided a clinical output. Cases are stratified by AI concordance (Agree/Disagree field).
2.  **Ground Truth Determination:** For cases where the clinician disagreed with the AI, the Clinical Validation Lead (an M.D.) performs a chart review to determine a final adjudicated Ground Truth.
3.  **Metric Trending:** Roll up adjudicated data to compute *in-vivo* Sensitivity, Specificity, and the current Production Calibration Curve. Plot these metrics against the baseline from the initial Independent Clinical Validation.

### 7.3 Quarterly Business Review (QBR)

By the 15th calendar day following the end of each fiscal quarter, the VP of Clinical AI Products will present a Clinical AI Quality Dashboard to the Chief Medical Officer and Chief Technology Officer. The report must include:
- A summary of all in-vivo model performance trends versus baseline.
- Top 3 models by Data Drift Severity Score.
- An aggregated summary of all Subgroup Analysis findings from post-market surveillance, including any newly emerging disparities.
- Summary of all adverse events, exceptions, and deviations.

---

## 9. Training Requirements

All personnel involved in the lifecycle of diagnostic AI must complete the following training program. Training records are maintained in Workday Learning.

| Training Module | Target Audience | Frequency | Content |
| :--- | :--- | :--- | :--- |
| **TR-CLIN-005.1: SOP Overview** | All Clinical AI personnel | Annually & on new hire | Detailed walkthrough of this SOP-CLIN-005, roles and responsibilities. |
| **TR-CLIN-005.2: Calibration Masterclass** | Data Scientists, ML Engineers | Bi-annually | Hands-on workshop on modern calibration techniques (Platt scaling, isotonic regression, temperature scaling), interpreting calibration curves, and debugging miscalibration. |
| **TR-CLIN-005.3: Human Factors for AI** | Product Managers, UX Researchers, Clinical Validation Leads | Annually | Principles for safe UI design for AI outputs, clinician cognitive load awareness, and designing for appropriate skepticism. |
| **TR-CLIN-005.4: Clinical Ground Truthing** | Clinical Validation Leads, QA Team | Annually | Standardized methodology for chart review, protocol adjudication, and inter-rater reliability calculation. |

All roles must achieve a pass rate of 100% on the associated knowledge check quiz before being granted access to production clinical AI tooling (e.g., model registry, inference deployment console).

---

## 10. Exception Handling and Escalation

### 10.1 Exception Types

Any proposed deviation from the mandatory policies in Section 4 or procedures in Section 5 constitutes an Exception. Common examples include:
- Releasing a model with an ECE exceeding 0.05 due to a novel, compelling clinical justification.
- Deploying a model without a full 14-day Silent Mode due to a declared internal clinical emergency.
- Using a non-standard calibration technique.

### 10.2 Exception Process

1.  **Request:** The Lead Data Scientist formally documents the exception request using template `FRM-QUAL-010` in Greenlight QMS. The request must contain a detailed technical and clinical rationale, a risk assessment of the proposed deviation, a specific compensatory control, and an expiration date for the exception.
2.  **Risk Review:** The QA team assesses the risk and categorizes it (Minor, Major, Critical).
3.  **Approval Matrix:**
    - **Minor Risk:** Approved jointly by VP of Clinical AI and the Quality Director.
    - **Major Risk:** Approved jointly by VP of Clinical AI and Chief Medical Officer.
    - **Critical Risk:** Approved jointly by Chief Medical Officer, VP of Clinical AI, and Chief Technology Officer.
4.  **Tracking:** All active exceptions are logged in an "Exception and Deviation Register" and are reviewed by the Quality Director monthly. No permanent exceptions are permitted; all must have a defined remediation plan and expiry.

---

## 11. Related Policies and References

### 11.1 Internal Meridian SOPs

| Document ID | Document Title |
| :--- | :--- |
| SOP-CLIN-002 | Clinical Performance Validation Protocol |
| SOP-CLIN-008 | Post-Market Clinical Surveillance |
| SOP-DATA-001 | Clinical Data Integrity and Management |
| SOP-SOFT-002 | Medical Device Software Lifecycle |
| SOP-MLOPS-001 | Model Deployment and Rollback |
| SOP-QUAL-001 | Nonconformance and CAPA Management |
| SOP-QUAL-003 | Adverse Event Reporting for Software as a Medical Device |
| SOP-RA-005 | EU AI Act High-Risk System Technical Documentation |

### 11.2 External Standards and References

- ISO 13485:2016 - Medical devices — Quality management systems.
- ISO 14971:2019 - Medical devices — Application of risk management to medical devices.
- IEC 62304:2006+AMD1:2015 - Medical device software — Software life cycle processes.
- Good Machine Learning Practice (GMLP) for Medical Device Development (FDA, Health Canada, MHRA).
- CONSORT-AI extension for clinical trials.

---

## 12. Revision History

| Version | Effective Date | Author(s) | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2021-03-15 | Dr. A. Okafor, S. Chen | Initial Release. Established core accuracy and calibration framework. |
| 2.1 | 2022-01-10 | Dr. A. Okafor, J. Patel | Added Section 5.7 (Silent Mode). Updated calibration ECE threshold from 0.08 to 0.06. |
| 3.0 | 2022-11-01 | J. Patel, Dr. M. Williams | Major revision adding Section 5.8 (Subgroup Analysis) and Section 9 (Training). |
| 4.2 | 2023-08-18 | Dr. A. Okafor, K. Nguyen | Updated Roles and Responsibilities to reflect new Clinical Validation Lead function. Updated metric names for drift. |
| 4.6 | 2024-06-26 | Dr. A. Okafor, L. Kim | Refined scope to specifically enumerate high-risk and pediatric models. Updated ECE gate to 0.05. Enhanced controls against data leakage and clarified CI reporting methods. Formalized Human Factors review. |
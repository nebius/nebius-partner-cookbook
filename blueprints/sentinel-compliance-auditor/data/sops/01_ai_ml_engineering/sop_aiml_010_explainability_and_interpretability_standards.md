---
sop_id: "SOP-AIML-010"
title: "Explainability and Interpretability Standards"
business_unit: "AI/ML Engineering"
version: "5.5"
effective_date: "2024-11-22"
last_reviewed: "2025-01-20"
next_review: "2025-07-18"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "NIST AI RMF"
  - "SR 11-7"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Explainability and Interpretability Standards

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the minimum requirements, standard methodologies, and governance framework for ensuring the explainability and interpretability of Artificial Intelligence (AI) and Machine Learning (ML) models developed, procured, or deployed by Meridian Health Technologies, Inc. The objective is to provide stakeholders—including clinicians, patients, regulators, model validators, and internal developers—with sufficient understanding of model behavior to foster appropriate trust, enable effective challenge, and support safe operational decision-making.

### 1.2 Scope
This SOP applies to all employees, contractors, and third-party partners involved in the AI/ML lifecycle across all Meridian business units. The mandated controls vary by model risk tier, which is defined by business unit context and regulatory exposure.

The scope explicitly includes:
- **Clinical AI Platform:** All models deployed in clinical decision support, diagnostic imaging analysis, patient risk scoring, and adverse event prediction.
- **HealthPay Financial Services:** All models used for credit scoring, medical lending underwriting, fraud detection, and claims processing.
- **MedInsight Analytics:** Population health models, care gap identification algorithms, and outcomes prediction engines that influence care pathways or reimbursement.
- **Meridian SaaS Platform:** Foundational AI services, including natural language processing (NLP) modules and feature stores that serve feature-engineering logic to downstream models.

This SOP covers the entire model lifecycle: design, data preparation, development, validation, deployment, monitoring, and decommissioning.

### 1.3 Regulatory Applicability Matrix

| Regulation/Standard | Applicable Business Unit(s) | Model Tier Impact | Coverage Level |
|---|---|---|---|
| NIST AI RMF 1.0 | Enterprise-wide | All Tiers | Thorough |
| SR 11-7 | HealthPay Financial Services | Tier 1 & 2 | Thorough |
| EU AI Act | Clinical AI Platform | Tier 1 | As Required |
| GDPR | MedInsight & Clinical AI Platform (EU data subjects) | Tier 1 & 2 | As Required |
| FDA 510(k) / EU MDR | Clinical AI (SaMD components) | Tier 1 | As Required |

---

## 2. Definitions and Acronyms

| Term | Definition |
|---|---|
| **AI/ML** | Artificial Intelligence / Machine Learning. |
| **Black-Box Model** | A model whose internal logic is not readily accessible or decipherable by a human operator (e.g., deep neural networks, complex gradient-boosted trees). |
| **Counterfactual Explanation** | An explanation that describes how a change in an input variable would alter the output of a prediction (e.g., "If your income was $5k higher, the credit offer would have been accepted"). |
| **Data Subject** | An identified or identifiable natural person about whom data is processed. Includes patients, loan applicants, and end-users. |
| **Explainable AI (XAI)** | A suite of techniques, methods, and processes that allow human users to comprehend and trust the results and output created by machine learning algorithms. |
| **Global Explanation** | An explanation that describes the overall behavior of a machine learning model, abstracting from individual predictions. Techniques include feature importance, partial dependence plots, and global surrogate models. |
| **Ground Truth** | The actual, verified, or observed value of a target variable. |
| **Grounding (NIST AI RMF)** | The process of aligning AI system operations with the expectations of affected individuals and communities (also referred to as "Contestation"). Meridian implements grounding primarily through the Appeals Process. |
| **Interpretability** | The degree to which a human can consistently predict a model’s output. Often used interchangeably with explainability, but in this SOP, "interpretability" refers to an intrinsic property of a transparent model (e.g., linear regression coefficients). |
| **LIME (Local Interpretable Model-agnostic Explanations)** | A model-agnostic technique that explains individual predictions by perturbing the input data locally and fitting a simple interpretable model. |
| **Local Explanation** | An explanation that justifies a single, specific prediction made by a model for a given data subject. |
| **Model Card** | A standardized, structured documentation artifact summarizing a model's intended use, architecture, performance metrics, evaluation results, ethical considerations, and explainability methods. |
| **Permutation Feature Importance** | A global technique that measures the drop in a model's performance score when a single feature's values are randomly shuffled, breaking the relationship between the feature and the true outcome. |
| **Robustness** | The ability of an AI system to maintain its level of performance under a variety of circumstances, including adversarial inputs or data perturbations. |
| **SHAP (SHapley Additive exPlanations)** | A game-theoretic approach to explain the output of any machine learning model. It connects optimal credit allocation with local explanations using the classic Shapley values from cooperative game theory and their related extensions. |
| **Tier 1 Model** | A model with high business impact where a material failure could cause significant financial loss, regulatory non-compliance, or life-threatening clinical risk. All Clinical AI Platform models are Tier 1. |
| **Tier 2 Model** | A model with moderate business impact, such as a pre-screening tool, or a model used to optimize administrative workflows. |
| **Transparent Model (White-Box)** | A model whose decision-making logic is inherently understandable to a human expert, such as linear/logistic regression, single decision trees, or simple rule-based systems. |

---

## 3. Roles and Responsibilities

The following RACI (Responsible, Accountable, Consulted, Informed) matrix delineates the core functions involved in the explainability lifecycle.

| Role | Responsibility | Accountable for... | Consulted on... | Informed on... |
|---|---|---|---|---|
| **Model Developer (AI/ML Engineering)** | Building models, implementing XAI libraries (SHAP/LIME), generating Model Cards. | Technical accuracy of explanations and code. | Feasibility of XAI requirements. | Tier 1 model deployment approval status. |
| **Model Validator (AI Risk, under Chief Risk Officer)** | Independent validation of model logic, XAI output, and conceptual soundness. | Objective challenge of model interpretability and robustness of explanations. | N/A (Independent Review). | N/A |
| **Product Manager (Applicable BU)** | Translating user needs into XAI requirements. Designing user-facing explanation interfaces. | Ensuring explanations are usable and meaningful for the end-user (e.g., clinician, loan officer). | Technical limitation of XAI methods. | Model development timelines and XAI bugs. |
| **Data Subject Advocate (Customer Operations)** | Managing the appeals and explanation-request workflow for external end-users and patients. | Data subject satisfaction and timely response to human review requests (Grounding). | Wording of user-facing explanations. | All Tier 1 model decisions. |
| **Compliance Officer (Legal & Compliance)** | Interpreting regulatory mandates (SR 11-7, GDPR). | Regulatory alignment of the policy documentation. | Specific explanation requirements for high-risk use cases. | Breach incidents related to automated processing. |
| **Chief AI Officer (CAIO, Dr. Marcus Rivera)** | Owner of this SOP. Defines the overall strategy for explainability. | Enterprise-wide adherence to this standard. | All XAI strategy and tooling decisions. | All exception approvals for Tier 1 models. |
| **VP of Engineering (David Park)** | Approver of this SOP. Ensures technical infrastructure supports the explainability pipeline. | System stability and data integrity for the XAI logging infrastructure. | Architecture for real-time XAI generation. | Major incidents involving the XAI service. |

---

## 4. Policy Statements

### 4.1 Core Principles
Meridian establishes the following core principles for AI/ML systems:

1.  **Right to Explanation:** Every end-user subject to an automated decision made by a Tier 1 or Tier 2 model has the right to request a plain-language, meaningful explanation of the logic involved.
2.  **Proportionality:** The rigor and complexity of explainability methods must be proportional to the model's risk tier, the decision's impact, and the technical context.
3.  **Accuracy-Fidelity Trade-off:** The explanation must be a high-fidelity reconstruction of the model's actual decision logic. Misleading post-hoc rationalizations are strictly prohibited.
4.  **Contestability (Grounding):** Users must have a clearly defined mechanism to contest a model-generated output and request human review.

### 4.2 Tier-Specific Interpretability Mandates

| Requirement | Tier 1 (High Risk: Clinical AI, Credit Underwriting) | Tier 2 (Moderate Risk: Population Health Analytics) | Tier 3 (Low Risk: Internal workflow NLP) |
|---|---|---|---|
| **Global Explanation** | Mandatory (Permutation Feature Importance + Global Surrogate or Partial Dependence Plots) | Mandatory (Permutation Feature Importance) | Recommended |
| **Local Explanation** | Mandatory (Counterfactual + SHAP/LIME at inference) | Mandatory (SHAP/LIME at inference) | Optional |
| **Intrinsic Interpretability** | Required unless benchmark proves >15% performance uplift over White-Box. Deep Neural Networks require explicit VP approval. | Recommended. Black-box models allowed with justification. | Allowed without justification. |
| **Model Cards** | Mandatory, auto-generated via CI/CD pipeline. | Mandatory. | Optional. |
| **Contestability** | Immediate escalation to human-in-the-loop. | Batch escalation (24-hour SLA). | Not required. |

### 4.3 Privacy and Data Protection
Meridian processes training data to provide these explanations. Data subjects receive a general notice acknowledging the categories of personal data being processed, consistent with transparency obligations. The lawful basis for processing personal data for XAI generation is "Legitimate Interest," grounded in the need to ensure model safety, fairness, and contestability. Data used in explanation generation is pseudonymized wherever technically feasible.

---

## 5. Detailed Procedures

### 5.1 Model Development and XAI Instrumentation

This procedure is executed by the Model Developer during the model-building phase.

**Step 1.1: Select XAI Library**
Based on the technical environment, developers must select the approved XAI library.
- For Python-based models (Meridian standard): Use **SHAP** (version 0.41.0+) for global and local explanations.
- For Tabular Neural Networks: Pair SHAP with **LIME** (version 0.2.0.1+) for locally faithful surrogate modeling.
- For Tree-based Ensemble Models (XGBoost, LightGBM): Use the `TreeExplainer` module of SHAP for computationally efficient exact calculation.

**Step 1.2: Global Feature Importance Generation**
After model training and cross-validation is complete, the developer must run the following script via the MLOps pipeline (`Meridian-Pipeline v2.1.3`):
```python
# Pseudocode for pipeline execution
explainer = shap.Explainer(model, background_data)
shap_values = explainer(X_test)
global_plot = shap.summary_plot(shap_values, X_test, show=False)
log_artifact("global_importance.png", global_plot)
```
*Output Artifact:* `global_importance.png` must be attached to the Model Registry record in the Meridian ML Platform (MLflow instance).

**Step 1.3: Local Explanation Endpoint**
For models requiring real-time inference (REST APIs), the developer must implement a `/v2/explain` endpoint that returns a structured JSON payload alongside the prediction. The endpoint must calculate SHAP values for the single prediction request within a 500ms latency budget.

**Step 1.4: Counterfactual Logic**
For Tier 1 models, developers must implement counterfactual logic within the `/v2/explain` endpoint. The system must run a local perturbation algorithm to identify the minimum change in the top-3 input features required to flip the model's binary classification (e.g., from "High Risk" to "Low Risk").

### 5.2 Tier 1 Intrinsic Interpretability Waiver Process

If a developer believes a black-box model is required for a Tier 1 use case:

1.  **Benchmarking Report:** The developer prepares a detailed report (Template: `FRM-XAI-T1-WAIVER`) comparing the performance of a transparent linear model versus the proposed black-box architecture. Performance must be measured by the **Area Under the Receiver Operating Characteristic (AUROC)** on a hold-out test set.
2.  **Threshold Justification:** The report must demonstrate a performance uplift of at least 15% absolute AUROC for the black-box model.
3.  **Review Chain:** The report is reviewed by the Lead Model Validator, who challenges the test design and metrics. Following internal validation, the CAIO (Dr. Rivera) reviews the risk trade-off.
4.  **Final Approval (VP Engineering):** If the clinical or financial need is validated, the waiver must be counter-signed by the VP of Engineering (David Park). No High-Impact Clinical Black-Box model may be deployed without this physical signature.

### 5.3 SR 11-7 Model Documentation (Financial Context)

For all HealthPay models subject to SR 11-7 governance, the following specific documentation steps must be followed *before* model validation testing begins.

**Step 3.1: Conceptual Soundness**
The Model Developer must document the theoretical foundation of the model. This includes a detailed mapping of input variables to the output logic. If SHAP values reveal a counter-intuitive variable importance, this must be specifically justified and reconciled with business logic. The documentation must answer: *Why does this variable matter, and does the direction of its impact align with the expected business logic?*

**Step 3.2: Local Explanation for Adverse Actions**
When a credit-decision model (Model ID: `HP-CS-v3`) results in an adverse action (denial of credit or higher interest rate), a "Principal Adverse Reasons" report must be generated immediately. This report is structured as follows:
- **Generation Engine:** Custom script consuming the SHAP `Explanation` object.
- **Format:** A ranked list of the top four (4) specific features that negatively impacted the applicant's score.
- **Template:** The Customer Operations system (`CRM-Salesforce-HealthPay`) automatically generates a letter using the `ADVERSE_REASON_01` template, populating the fields `REASON_1`, `REASON_2`, etc., with statements like: *"Your application was denied primarily due to [Feature Name], such as [Instance Value], compared to the average of [Demographic Average]."*
- **Prohibited Disclosures:** The system must strip internal SHAP magnitude values. Explanations must be in plain English.

**Step 3.3: Model Validator Challenge**
Per SR 11-7 Section III(D) (Independent Validation), the Model Validator must attempt to "break" the explanation using adversarial perturbations. The validator receives a copy of the model, introduces designed noise, and records whether the SHAP KernelExplainer converges correctly and whether the feature logic remains consistent.

### 5.4 NIST AI RMF 1.0 Alignment Procedures

Meridian aligns its operational procedures with the Playbook recommendations for NIST AI RMF 1.0. The following specific actions are triggered during the Model Card creation process (`SOP-AIML-005`):

**Procedure 4.1: MAP Function Alignment**
During the "Map" stage (Govern 1), the Product Manager confirms that the model's context is mapped to the specific taxonomy of [NIST AI RMF Playbook, Play 2 (Stakeholder Impact Mapping)]. The "Impacted Stakeholders" matrix must specifically define "Clinicians" and "Patients" as distinct cohorts with different explanation requirements.

**Procedure 4.2: MEASURE Function Alignment (Measure 2)**
The Model Card must contain a dedicated "Explainability & Grounding" section, directly addressing [Measure 2.11: Human-AI Configuration]. For Tier 1 Clinical AI models, the model card must explicitly document the "Human-in-the-Loop" configuration, specifying the latency threshold (e.g., *"Clinician override must be accepted within 2 seconds of alert to prevent auto-escalation"*).

**Procedure 4.3: MANAGE Function Alignment (Manage 4)**
During deployment, the MLOps pipeline checks for adherence to [Manage 4.3: Response, Appeal, and Override]. A "Contestation API" must be registered in the API Gateway (`Kong-v3`). This endpoint registers a complaint or override request, automatically linking it to the specific prediction UUID. If the override rate for a specific clinical model exceeds 5% of its daily inference volume, an automatic incident ticket is generated in ServiceNow and assigned to the Tier 3 Clinical Informatics Support Queue.

### 5.5 Model Validation and Approval

| Control Step | Tier 1 Criteria | Tier 2 Criteria |
|---|---|---|
| **Code Review** | Peer review required. XAI logic manually inspected by Model Validator. | Automated pipeline check for SHAP library presence (v0.41+). |
| **Conceptual Soundness** | Detailed memo required. | Section within Model Card required. |
| **Stress Test (Adversarial)** | Validator executes 100+ adversarial perturbations. | Developer executes 10 random perturbations, logged. |
| **Documentation Quality** | 100% fields in Model Card. | 95% fields in Model Card. |
| **User Acceptance (UI)** | Product Manager signs off on user-facing explanation text. | Standard template used. |

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

1.  **XAI Logging Pipeline:** All Tier 1 model predictions and their corresponding SHAP/LIME explanations must be logged atomically to the `xai_logs` data lake partition (`s3://meridian-logs/explainability/prod/`). No prediction transaction succeeds without the XAI artifact logging succeeding.
2.  **Data Versioning:** The training dataset and background dataset used for SHAP calculations must be versioned using Data Version Control (`DVC v2.0.3`). Discrepancy between training distribution and explanation background distribution triggers an automated alert in the `#aiml-monitoring` Slack channel.
3.  **Baseline Drift Monitoring:** Permutation Feature Importance (Global) is recalculated nightly on live inference traffic. If the Euclidean distance between the current Global Importance vector and the baseline (approved) vector exceeds a threshold of 0.35, an automatic model freeze is placed on the specific deployment endpoint pending manual review by the MLOps team.

### 6.2 Administrative Controls

1.  **Annual Explainability Audit:** The Internal Audit department shall perform an annual review of a random sample of 50 Tier 1 and Tier 2 models, checking for valid Model Cards, valid XAI artifact logs, and non-stale explanations. The audit focuses on the fidelity of the explanations to the model internals.
2.  **Segregation of Duties:** The Model Developer cannot approve their own explanation logic. The "Approval" role in the ML Registry (MLflow) is strictly assigned to the Model Validator group.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The following KPIs are tracked via the central Model Operations (`ModelOps`) Dashboard built on Grafana 8:

| Metric Name | Definition | Target | Measurement Interval |
|---|---|---|---|
| **XAI Availability (XAI-A)** | % of Tier 1 predictions successfully logged with SHAP values. | 99.99% (Log level SLA) | Real-time (last 5 min) |
| **Explanation Latency (XAI-L)** | 99th percentile (P99) response time for `/v2/explain` endpoint. | < 450ms | Hourly Aggregation |
| **Counterfactual Plausibility (CF-P)** | % of counterfactuals generated that fail plausibility checks (e.g., suggesting "Age: -5"). | < 0.1% | Daily Batch |
| **Model Override Rate (Grounding)** | % of Adverse Credit decisions overridden by human officers per SR 11-7 Section III. | 2.0% - 6.0% (Threshold) | Weekly Aggregation |
| **Missing Artifact Score (MAS)** | % of active Tier 1 models missing Global Importance attachments in ML Registry. | 0.0% | Weekly Audit |

### 7.2 Reporting

- **Real-Time:** A Grafana panel ("XAI Health Pulse") displays current XAI-A and XAI-L for the Clinical AI Platform and HealthPay.
- **Monthly:** The CAIO (Dr. Rivera) receives a "Model Interpretability Scorecard" containing aggregate Override Rates, Drift Metrics, and exception counts.
- **Quarterly:** A model-specific XAI report is pushed to Compliance for SR 11-7 audit preparation, detailing all adverse action reason codes and their associated feature distributions.

---

## 8. Exception Handling and Escalation

### 8.1 Standard Exception Process

Any deviation from the XAI techniques and logging mandates described in this SOP requires a formal Exception Request.

1.  **Request Submission:** The Model Developer submits the `FRM-XAI-EXC-01` form in the Meridian Governance Portal (MetricStream). The request must detail:
    - Affected Model ID.
    - Specific procedure for which exception is sought.
    - Technical justification (e.g., SHAP not compatible with a proprietary scoring engine).
    - Proposed compensating control (e.g., manual human review of all outputs).
    - Duration of exception (max 90 days).
2.  **Technical Review:** The Lead Model Validator reviews the compensating control.
3.  **Approval Matrix:**
    - **Tier 1 Exception:** Requires CAIO (Dr. Rivera) approval.
    - **Tier 2 Exception:** Requires VP of AI/ML Engineering approval.
    - **SR 11-7 Adverse Action Exception:** Cannot be approved. If the system fails to provide Principal Adverse Reasons, the automated decision pipeline must halt, and all applications must be sent to manual underwriting.

### 8.2 Incident Escalation (Grounding Failure)

If a Data Subject Advocate (CustomerOps) identifies a consistent pattern of "explanation defects" (e.g., nonsensical variable importance), they initiate a `SEV-2` incident.
1.  The Model Developer has **4 hours** to verify if the explanation is true to the model logic.
2.  If the explanation is technically correct but contextually misleading, the Product Manager must initiate an emergency UI update (hotfix) within **24 hours**.

---

## 9. Training Requirements

All personnel governed by this SOP must complete the following training:

1.  **Module: "AI & ML Interpretability Fundamentals" (LMS Code: AIML-010-T1)**
    - **Target Audience:** Model Developers, Validators, Product Managers.
    - **Frequency:** Annually.
    - **Content:** SHAP mathematics overview, LIME limitations, counterfactual generation, recognizing adversarial noise.
2.  **Module: "Ethics and Controllership in Automated Lending" (LMS Code: COMP-HP-02)**
    - **Target Audience:** HealthPay Customer Experience & Underwriting teams.
    - **Frequency:** Semi-annually.
    - **Content:** Specific instructions on reading the "Principal Adverse Reasons" report and explaining them to data subjects without violating Fair Lending laws. Focuses on SR 11-7 compliance.
3.  **Training Compliance Tracking:**
    - Completion of these modules is tracked via the Workday Learning Management System (LMS). Access to Tier 1 model production logs is automatically suspended for accounts with expired critical training credentials.

---

## 10. Related Policies and References

| Document ID | Title |
|---|---|
| **SOP-AIML-001** | AI/ML Model Lifecycle and Risk Management |
| **SOP-AIML-005** | Model Cards and Algorithmic Documentation Standards |
| **SOP-SEC-200** | Data Classification and Handling Policy |
| **SOP-COMP-110** | Fair Lending and Adverse Action Compliance |
| **SOP-QA-500** | Clinical Decision Support Systems Performance Monitoring |
| **NIST AI RMF 1.0** | NIST Artificial Intelligence Risk Management Framework (January 2023) |
| **FRB SR 11-7** | Federal Reserve Board Supervision and Regulation Letter 11-7 (Guidance on Model Risk Management) |

---

## 11. Revision History

| Date | Version | Author | Summary of Changes |
|---|---|---|---|
| 2022-06-15 | 1.0 | Dr. M. Rivera | Initial Draft. Established core SHAP requirements for Clinical AI. |
| 2023-01-10 | 2.1 | J. Chen (Legal) | Added SR 11-7 adverse action documentation requirements for HealthPay. |
| 2023-08-04 | 3.3 | P. Gupta (ML Eng) | Integrated NIST AI RMF mapping procedures (Measure 2.11, Manage 4.3). Defined Model Card linkage. |
| 2024-03-20 | 4.0 | Dr. M. Rivera | Introduced Counterfactual logic mandatory for all Tier 1 models. Updated versioning requirements for background datasets. |
| 2024-11-22 | 5.5 | Dr. M. Rivera | Refined Intrinsic Interpretability Waiver Process (15% AUROC threshold). Clarified roles for Model Validator adversarial testing. Added MLOps model-freeze control for drift detection. |
---
sop_id: "SOP-AIML-009"
title: "Algorithmic Bias Detection and Mitigation"
business_unit: "AI/ML Engineering"
version: "4.8"
effective_date: "2024-01-09"
last_reviewed: "2025-07-01"
next_review: "2026-01-12"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "NIST AI RMF"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Algorithmic Bias Detection and Mitigation

## 1. Purpose and Scope

### 1.1 Purpose

The purpose of this Standard Operating Procedure (SOP) is to establish a standardized, enterprise-wide framework for the detection, measurement, and mitigation of algorithmic bias within all artificial intelligence and machine learning (AI/ML) systems developed, procured, or deployed by Meridian Health Technologies, Inc. This SOP defines the mandatory processes, tools, and governance structures designed to ensure that our algorithmic systems produce equitable outcomes across all demographic groups, uphold our ethical commitments, and comply with our regulatory obligations concerning non-discrimination and data protection.

### 1.2 Scope

This SOP applies to all Meridian Health Technologies business units, departments, and personnel involved in the AI/ML lifecycle, including but not limited to research, development, data science, machine learning engineering, product management, quality assurance, and operational deployment.

The scope of this SOP explicitly covers:

| In-Scope Systems | Out-of-Scope Systems |
| :--- | :--- |
| Clinical AI Platform (risk scoring, diagnostic imaging, adverse event prediction) | Simple rule-based engines with no learning component (e.g., basic `if-this-then-that` claims routing) |
| HealthPay Financial Services (credit scoring, fraud detection, lending models) | Spreadsheets or manual statistical analyses not used for automated decision-making |
| MedInsight Analytics (care gap identification, population health outcomes) | Legacy third-party tools where Meridian cannot influence the model’s retraining or design, as documented by the VP of Engineering |
| All Generative AI features deployed to production (chatbots, summarization) | |
| Any internally developed or externally procured model that informs consequential decisions about individuals | |

This SOP applies to all stages of the model lifecycle: problem formulation, data acquisition, feature engineering, model training, validation, deployment, monitoring, and retirement. Compliance with this SOP is mandatory for all full-time employees and contingent workers (contractors, consultants) at all Meridian locations globally (Boston HQ, London, Berlin, Singapore, Toronto).

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **Algorithmic Bias** | Systematic and repeatable errors in a model’s outputs that create unfair outcomes, privileging one arbitrary group over another. |
| **Protected Attribute** | A characteristic of an individual that is legally protected from discrimination. For the purposes of this SOP, protected attributes include: race, color, ethnicity, national origin, religion, sex, gender identity, sexual orientation, age, disability, genetic information, and family status. |
| **Fairness Metric** | A quantitative measure used to assess the presence and magnitude of bias. Examples include Statistical Parity Difference (SPD), Equal Opportunity Difference (EOD), and Average Odds Difference (AOD). |
| **Disparate Impact** | A legal theory of discrimination that examines whether a facially neutral policy or practice disproportionately harms members of a protected group. Operationalized in this SOP as the 80% Rule (see Section 4.2). |
| **Model Risk Tier** | A classification (Critical, High, Standard, Low) assigned to each model based on the potential severity of harm from biased or erroneous outputs, as defined in the Model Risk Management procedure. |
| **Ground Truth** | The objectively correct label or outcome for a given data point, as determined by clinical or operational consensus. |
| **PII** | Personally Identifiable Information. |
| **PHI** | Protected Health Information. |
| **Model Card** | A structured, short document providing key information about a trained model, including intended use, performance metrics across sub-groups, and known limitations. |
| **AI/ML CoE** | AI/Machine Learning Center of Excellence, led by the Chief AI Officer. |
| **EU DPO** | European Union Data Protection Officer, Dr. Klaus Weber. |
| **IRB** | Internal Review Board, an internal, cross-functional body that reviews high-risk AI use cases. |

---

## 3. Roles and Responsibilities

The following matrix defines the accountability and responsibility for the execution of this SOP. Roles are structured according to the RACI model (Responsible, Accountable, Consulted, Informed).

| Role / Title | Responsibility (RACI) | Key Duties |
| :--- | :--- | :--- |
| **Chief AI Officer (CAIO)** — Dr. Marcus Rivera | **Accountable** | Holds ultimate authority over the AI/ML governance framework. Signs off on all Critical and High-risk model deployments and bias mitigation exceptions. |
| **VP of Engineering** — David Park | **Accountable** | Accountable for the technical implementation of bias testing tooling and infrastructure across all engineering pipelines. Holds engineering teams responsible for executing this SOP. |
| **Product Managers (Clinical, HealthPay, MedInsight)** | **Consulted / Informed** | Responsible for defining fairness requirements in Product Requirements Documents (PRDs) for their respective products. Consulted during bias remediation for impacts to feature timelines. |
| **Data Scientists & ML Engineers** | **Responsible** | Execute all technical procedures defined in Section 5. Must author and maintain Model Cards. Must implement and test bias mitigation strategies. |
| **Data Owners (Clinical, Financial, etc.)** | **Responsible / Consulted** | Responsible for ensuring that training data is sourced, labeled, and documented in compliance with data governance policies. Must approve the use of new data sources for model training. |
| **Chief Compliance Officer** — Thomas Anderson | **Consulted** | Provides regulatory interpretation. Reviews and approves all Disparate Impact Reports for lending models under HealthPay before deployment. |
| **Chief Privacy Officer / EU DPO** — Dr. Klaus Weber | **Consulted** | Must be consulted on any data collection or processing activity involving PII from EU data subjects for bias detection, to ensure alignment with data minimization and purpose limitation principles. Reviews Data Protection Impact Assessments (DPIAs) where algorithmic bias creates a high risk to individuals. |
| **VP of IT Operations** — Samantha Torres | **Responsible / Informed** | Responsible for deploying and maintaining the infrastructure for the automated bias monitoring pipeline (Kafka, Snowflake) in the production environment. |
| **General Counsel** — Maria Gonzalez | **Consulted** | Provides legal review of fairness criteria and disparate impact thresholds. Approves the legal sufficiency of non-discrimination policies embedded in algorithms. |
| **Internal Review Board (IRB)** | **Responsible** | Reviews and adjudicates complex bias versus accuracy trade-off decisions for Critical and High-risk models. The IRB comprises the CAIO, VP of Engineering, Chief Compliance Officer, and a rotating Product lead. |

---

## 4. Policy Statements

### 4.1 Fairness by Design

Meridian Health Technologies is committed to the principle of “Fairness by Design.” Algorithmic fairness is not a post-hoc remediation step but a foundational requirement integrated from the earliest stages of the ML lifecycle. All AI/ML projects must commence with a mandatory bias scoping exercise, which identifies potential protected attributes, defines the fairness criteria in partnership with the product team, and documents these in the project’s Bias Testing Plan.

### 4.2 The 80% Rule (Disparate Impact)

In addition to formal fairness metrics, Meridian adopts the “80% Rule” as a practical standard for assessing disparate impact in high-stakes classification models (e.g., lending, clinical risk scoring). A model exhibits potential disparate impact if the selection or favorable outcome rate for a protected group is less than 80% of the rate for the group with the highest selection rate.

- **Formula:** `Disparate Impact Ratio = (Positive Outcome Rate for Protected Group) / (Positive Outcome Rate for Reference Group)`
- **Threshold:** A ratio below 0.80 requires mandatory investigation and documented justification or remediation, as outlined in Section 6.2.

### 4.3 Human-in-the-Loop for High-Risk Decisions

No AI/ML model classified as Critical or High risk shall make a fully automated, consequential decision about an individual without meaningful human oversight. The human reviewer must have the authority and competence to override the algorithmic recommendation and must have access to the salient factors (explainability dashboard) that contributed to the model’s output. This is mandatory for the Clinical AI Platform and patient financing decisions in HealthPay.

### 4.4 Privacy and Data Minimization in Bias Testing

All bias testing activities that involve PII or PHI must be conducted in a manner consistent with data minimization principles. Data Scientists must use de-identified or pseudonymized datasets for bias analysis whenever possible. The explicit approval of the Data Owner and a consultation with the Chief Privacy Officer are prerequisites for using directly identifiable PII/PHI for bias detection when no alternative exists.

### 4.5 Transparency and Model Cards

Every model deployed to production must be accompanied by a completed Model Card. The Model Card is a live document in the MLflow model registry and must be updated with each significant model version change. The Model Card must be reviewed and approved by the model owner before a new model version can be deployed to production.

---

## 5. Detailed Procedures

This section outlines the step-by-step operational procedures for the Algorithmic Bias Detection and Mitigation lifecycle.

### 5.1 Phase 1: Pre-Development — Bias Scoping and Planning

This phase is the responsibility of the Product Manager and Lead Data Scientist, executed through the project’s `Bias Testing Plan` document in Confluence.

**Procedure Steps:**
1.  **Identify the Decision Context:**
    - The Product Manager defines the model’s primary objective, the population it will serve, and the nature of the decision it will inform or automate.
    - Document this in the Product Requirements Document (PRD).
2.  **Identify Potential Protected Attributes:**
    - The Lead Data Scientist conducts an initial scan to list all attributes relevant to the modeling task that could serve as proxies for protected classes, even if not explicitly present in the data (e.g., zip code as a proxy for race, medical diagnosis codes as a proxy for disability).
    - This list is documented in the Bias Testing Plan.
3.  **Define Relevant Fairness Metrics:**
    - The Data Scientist, in consultation with the Product Manager and Chief Compliance Officer (for HealthPay), selects the appropriate fairness metrics from the taxonomy defined in Section 6.1.
    - The choice must be justified in the Bias Testing Plan. For example: "For the patient readmission risk model, we will prioritize the Equal Opportunity Difference because the cost of a false negative (missing a high-risk patient) is asymmetrically high."
4.  **Set Fairness Thresholds:**
    - Pre-define the acceptable bounds for each selected fairness metric. The default global threshold is ±0.10 for all difference-based metrics, but this can be tightened by the Product Manager for specific sensitive contexts.
5.  **Consult Privacy Officer:**
    - If the bias detection plan involves PII/PHI, the Lead Data Scientist must open a `Privacy Consultation Ticket` in ServiceNow (Category: `Bias-Testing-DPIA`) to consult with Dr. Weber’s office. The consultation must confirm the lawful basis for processing, data minimization techniques used, and retention period.

### 5.2 Phase 2: Data Preparation and Pre-processing

**Procedure Steps:**
1.  **Data Discovery and Classification:**
    - The Data Scientist uses the Meridian Data Catalog (powered by Alation) to locate and request access to approved datasets. All datasets must have a completed Data Quality and Lineage score.
2.  **Proxy Detection and Mitigation:**
    - Run the internal `meridian-fairness` Python library’s `proxy_detector` module on the assembled feature set. This module performs statistical tests (e.g., Pearson correlation) to flag variables with a high correlation to known protected attributes.
    - **Action:** Any flagged variable with a correlation coefficient ≥ 0.6 must be either (a) removed from the training feature set, or (b) documented with a compelling business justification accepted by the IRB.
3.  **Class Imbalance Check:**
    - Execute the `fairness_checks.class_balance()` function to generate a demographic breakdown of the sample population across the identified protected attributes.
    - **Action:** If any demographic group represents less than 5% of the training dataset, the Data Scientist must implement one of the following re-sampling strategies and document the rationale:
        - **Up-sampling:** SMOTE (Synthetic Minority Over-sampling Technique) for the minority group.
        - **Down-sampling:** Random undersampling of the majority group.
        - **Data Augmentation:** Synthesize new data points for the minority group using approved generative methods.
4.  **Train/Test/Validation Split:**
    - All splits must be stratified across the key protected attributes identified in the Bias Testing Plan. This ensures consistent representation in each data partition. The `stratified_split` function in the `meridian-mlops` library must be used.

### 5.3 Phase 3: Model Training and Validation — Bias Detection

**Procedure Steps:**
1.  **Train Candidate Models and Baseline:**
    - Train all candidate models and a simple baseline model (e.g., logistic regression). Track all experiments using the `mlflow` experimentation tracking server at `https://mlflow.meridian.internal`.
    - **Mandatory Tag:** Every experiment run must be tagged with the Confluence page ID of the associated Bias Testing Plan.
2.  **Generate Sub-Group Performance Metrics:**
    - Using the held-out Validation dataset, run the `fairness_metrics.evaluate()` function from the `meridian-fairness` library for every candidate model. This function automatically slices the dataset across all pre-identified protected attributes and computes the full suite of fairness metrics.
    - The output is a `FairnessAssessment` JSON object, which must be serialized and logged as an artifact to the parent MLflow run.
3.  **Fairness Threshold Validation:**
    - Compare the computed metrics against the thresholds defined in Phase 1.
    - **If all metrics are within defined thresholds:** Proceed to Section 5.4 for deployment.
    - **If any metric fails the threshold (e.g., EOD is 0.15, exceeding the 0.10 limit):** This triggers a mandatory bias remediation process per Section 5.5. The model cannot proceed to deployment.

### 5.4 Phase 4: Pre-Deployment Approval and Documentation

Before a model can be promoted to the Staging or Production registry in MLflow, the following controls must be satisfied.

**Procedure Steps:**
1.  **Complete the Model Card:**
    - The Lead Data Scientist is responsible for completing every required field in the Model Card, including detailed sections on performance across sub-groups and known biases.
    - The Model Card is an MLflow `model-card.md` file located in the model's versioned repository.
2.  **Generate the `BiasComplianceCheck` Report:**
    - Execute the final automated compliance check script: `run_bias_compliance_check(model_uri)`. This script verifies:
        - A `Bias Testing Plan` ID is linked.
        - The `FairnessAssessment` object is present and all values are compliant.
        - All data lineage tags are present.
        - The Model Card is 100% filled out.
        - The Privacy Consultation Ticket (if required) is in `Approved` status.
    - A passing check changes the model's `bias_governance` tag to `PASSED`. A failing check returns a detailed list of remediation items.
3.  **Model Approval:**
    - A `Pre-Deployment Model Review` request must be submitted through the Meridian Model Registry UI. This request automatically notifies the Accountable roles:
        - **Standard/Low Risk Models:** VP of Engineering reviews the `BiasComplianceCheck` PASSED status and approves.
        - **High Risk Models:** CAIO must review and approve.
        - **Critical Risk Models:** CAIO and the full IRB must review the complete fairness assessment package and unanimously approve deployment.
    - No model can be deployed to production without the `bias_governance: PASSED` tag and the requisite human approvals.

### 5.5 Phase 5: Bias Remediation (If Detection Fails)

If a model fails the fairness threshold validation in Section 5.3, the following strict hierarchy of mitigation strategies must be explored and documented.

**Remediation Hierarchy:**
1.  **Pre-processing Interventions (Data-first):**
    - Re-balance the training dataset using more aggressive data augmentation in collaboration with the Data Owner.
    - Re-label data where label bias is suspected. Implement the `Label_Bias_Debugger` tool (internal, based on confidence score variance).
2.  **In-processing Interventions (Model-first):**
    - Implement a fairness-constrained optimization algorithm available in `meridian-fairness`. The Lead Data Scientist shall test adversarial debiasing and prejudice remover methods.
    - The choice of mitigation must be documented with an explanation of the bias-accuracy trade-off. For Critical and High-risk models, this trade-off must be presented to the IRB.
3.  **Post-processing Interventions (Output-first):**
    - Apply threshold adjustment based on protected group membership (e.g., using a different classification threshold for a disadvantaged group to equalize opportunity). This is the method of last resort and is only permissible with explicit IRB approval, as it introduces a different form of group-based treatment that must be legally vetted by General Counsel.

If all three tiers are exhausted and the model still cannot meet the fairness thresholds, the model shall not be deployed in its current form. The project must be rescoped, or the use case for automated decision-making must be abandoned.

### 5.6 Phase 6: Continuous Production Monitoring and Retraining

Fairness is not a static property; models drift.

**Procedure Steps:**
1.  **Automated Metric Logging:**
    - The `meridian-monitoring` Kafka cluster consumes logs from all production model services. For every 10,000th prediction, the system calculates the current Disparate Impact Ratio and Statistical Parity Difference using the latest available ground-truth feedback, grouped by protected attribute proxies. These metrics are written to the `fairness_metrics_production` InfluxDB database.
2.  **Drift Alerting:**
    - A model is flagged for bias drift if its production fairness metrics deviate by more than 20% from its baseline validation metrics recorded at deployment. This triggers a `P0` ServiceNow incident automatically assigned to the owning MLOps squad and the CAIO.
3.  **Scheduled Re-validation:**
    - For all deployed models, a full, offline re-assessment of bias must be conducted every **180 days** for Standard risk models and every **30 days** for High and Critical risk models. This re-assessment uses the same code as Section 5.3 but on a more recent (last 60 days) production sampling dataset.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control ID | Control Name | Description |
| :--- | :--- | :--- |
| **T-01** | `meridian-fairness` Library | A centralized, approved Python library for bias detection and mitigation. All Data Science teams are mandated to use it. No unapproved, self-coded bias testing scripts are permitted in production pipelines. |
| **T-02** | MLflow Model Registry Tags | Model registry gates prevent promotion to `Production` stage unless the model’s MLflow tags include `bias_governance: PASSED` and a valid Confluence ID for the `bias_testing_plan`. |
| **T-03** | Proxy Detector Module | An automated script that scans all incoming features for potential proxies to protected attributes, providing a risk score (0.0-1.0). Variables with a score > 0.85 are automatically blocked until manually overridden by the CAIO. |
| **T-04** | Kafka Monitoring Stream | A dedicated, hardened Kafka topic (`bias-prod-metrics`) that receives fairness metrics from production inference services. This stream is write-only for application services. |
| **T-05** | Differential Privacy | For High and Critical risk models, the training process must incorporate differential privacy techniques to minimize the risk of model inversion, thereby indirectly protecting group and individual data.

### 6.2 Administrative Controls

| Control ID | Control Name | Description |
| :--- | :--- | :--- |
| **A-01** | Disparate Impact Review | Every HealthPay lending model and any other model using the 80% Rule must have a formal `Disparate Impact Report` filed and approved by the Chief Compliance Officer prior to each deployment and after each annual monitoring event. |
| **A-02** | Mandatory Ethical Review | Every new AI/ML project with a Critical risk classification must pass a review by the Internal Review Board (IRB). The IRB specifically adjudicates fairness vs. accuracy trade-offs that the model team cannot resolve. |
| **A-03** | Vendor Model Assessment | Any procured third-party model or API (e.g., generative AI services) must undergo a vendor fairness certification process. The vendor must attest to the methods used for bias testing their solution. |
| **A-04** | Data Governance Audit | Quarterly audits by the Data Governance team to ensure training data sources used in active models have valid, documented lineage and that proxy detection was performed. |
| **A-05** | Consequence Management | A deliberate failure to comply with this SOP (e.g., bypassing the `meridian-fairness` library, or deploying a Critical model without IRB approval) is a violation of the Employee Code of Conduct and will result in disciplinary action, up to and including termination of employment. |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The AI/ML Center of Excellence (CoE) will track the following KPIs through a Grafana dashboard (`AI Governance — Bias KPIs`):

| KPI | Target | Measurement Method |
| :--- | :--- | :--- |
| **Bias Testing Compliance Rate** | 100% of production models | Automatic check: model `bias_governance` tag == `PASSED` |
| **Mean Time to Mitigate (MTTM)** | < 14 days for P0 Bias Incidents | ServiceNow `MTTM` KPI for incidents with category `Bias-Drift` |
| **High-Risk Model Monitoring Lag** | < 7 days | Difference between current date and the last successful run of the 30-day re-validation job |
| **Remediation Tier Distribution** | Track pre/post/in-processing usage | Manual logging in the remediation procedure; aggregated quarterly |
| **Synthetic Data Usage** | Increase by 15% YoY | Count of models tagged with `training_data: augmented` in MLflow |

### 7.2 Reporting Cadence

- **Monthly:** An automated report from the CAIO’s office will be sent to the VP of Engineering and all Data Science Team Leads (DSTLs), detailing the compliance status of all models in the `Staging` and `Production` registries, highlighting active non-compliance incidents.
- **Quarterly:** The CAIO will present the “State of AI Fairness at Meridian” report to the Executive Leadership Team. This report will summarize KPI trends, detail all P0 and P1 bias incidents over the prior quarter, and highlight decisions made by the Internal Review Board.
- **Annually:** A comprehensive review of this SOP-AIML-009 policy and its associated KPIs will be conducted by the AI/ML CoE, the Chief Compliance Officer, and the General Counsel.

---

## 8. Exception Handling and Escalation

### 8.1 General Exception Policy

Exceptions to any provision of this SOP must be exceptional, temporary, and granted through a formal, documented process. A verbal or email-based “waiver” is not valid. Exceptions exist primarily to handle unanticipated conflicts between fairness and model utility where no standard mitigation is viable.

### 8.2 Exception Handling Procedure

1.  **Request Initiation:**
    - The Lead Data Scientist opens a `Policy Exception Request` in ServiceNow, linked to the specific model (MLflow `run_id`) and citing the specific clause of this SOP from which deviation is sought (e.g., "Exception requested for Section 5.3.3, EOD threshold of 0.10, for model X. Current EOD is 0.13.").
2.  **Technical Justification and Risk Assessment:**
    - The request must include a detailed technical justification explaining why standard remediations (per the hierarchy in Section 5.5) are infeasible or would render the model scientifically useless.
    - This must be accompanied by a risk assessment quantifying the potential harm of the biased outcomes.
3.  **Review and Approval Workflow:**
    - **Standard/Low Risk Model:** Request is routed to the AI/ML CoE Operations Lead.
    - **High Risk Model:** Request is routed to the CAIO (Dr. Marcus Rivera).
    - **Critical Risk Model:** Request is routed to the full Internal Review Board. Approval requires a majority vote, with the Chief Compliance Officer holding veto power.
4.  **Remediation Plan and Expiry:**
    - Every granted exception must include a clear, time-bound remediation plan and an expiry date (maximum 90 days). The exception is not renewable without escalating to the VP of Engineering and General Counsel.
    - The model in production will be tagged with `policy_exception: true` and linked to the ServiceNow ticket, visible on the primary governance dashboard.

### 8.3 Escalation Paths

| Escalation Trigger | Escalation Path |
| :--- | :--- |
| P0 Bias Drift incident unresolved for 7 days | Incident auto-escalates from MLOps Squad -> CAIO -> Chief Compliance Officer -> General Counsel. |
| Disagreement between a Team Lead and a Product Manager on fairness metric selection | Escalate jointly to the CAIO and the relevant business unit VP. A final binding decision will be issued within 5 business days. |
| A vendor refuses to provide necessary data for a bias audit | Escalate from the Vendor Manager to the VP of Engineering and the General Counsel for a contractual breach review. |

---

## 9. Training Requirements

### 9.1 Training Catalog

| Training Module Code | Title | Audience | Frequency | Method |
| :--- | :--- | :--- | :--- | :--- |
| **AMLX-101** | Algorithmic Bias & Fairness — Foundations | All technical staff (Data Scientists, MLOps Engineers, QA Analysts) | Onboarding and Annually | LMS (Workday Learning) + Live Workshop |
| **AMLX-201** | Advanced Fairness Metrics and Remediation Toolkit | Senior Data Scientists, ML Engineers | Annually | Hands-on Lab using `meridian-fairness` library |
| **AMLX-PRD** | Defining Fairness in PRDs | Product Managers, Product Directors | Annually | LMS (Workday Learning) |
| **AMLX-LEG** | Legal Aspects of Algorithmic Discrimination | Chief Compliance Officer, General Counsel, CAIO, IRB Members, EU DPO | Annually | Seminar led by external legal counsel |

### 9.2 Training Tracking and Compliance

- All training modules are assigned and tracked through **Workday Learning**.
- Completion of role-required training is a key compliance metric. Non-completion within 30 days of the assignment triggers an automated notification to the individual and their direct manager.
- Continued non-compliance (beyond 60 days) results in the revocation of access rights to the Meridian SageMaker Studio and MLOps deployment pipeline (i.e., the user cannot push models to production). The CAIO receives a monthly report on training non-compliance.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies (SOPs)

| SOP ID | Document Title |
| :--- | :--- |
| **SOP-DAT-004** | Data Classification, Handling, and Labeling |
| **SOP-SEC-012** | Identity and Access Management for MLOps Infrastructure |
| **SOP-PRI-008** | Conducting a Data Protection Impact Assessment (DPIA) |
| **SOP-AIML-001** | AI/ML Model Risk Management |
| **SOP-AIML-005** | Model Lifecycle Management from Experimentation to Production |
| **SOP-AIML-014** | Generative AI Development and Use Policy |
| **SOP-AIML-022** | Human-in-the-Loop Mandate for Critical Systems |
| **SOP-COMP-021** | Regulatory Complaints and Non-Conformity Management |

### 10.2 External References

- **NIST Special Publication 1270:** Towards a Standard for Identifying and Managing Bias in Artificial Intelligence (Guidance referenced for taxonomy and metrics).
- **ISO/IEC 42001:2023:** Information Technology — Artificial Intelligence — Management System.
- **GDPR Article 5:** Principles relating to processing of personal data (specifically, data minimization and purpose limitation as applied to bias detection procedures). See SOP-PRI-008.
- **Meridian Employee Data Protection and Privacy Notice [Internal Link]:** This notice outlines, for Meridian employees, how their personal data is processed by Meridian for internal compliance purposes, including algorithmic fairness testing.

---

## 11. Revision History

| Version | Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2022-05-15 | Dr. Sarah Chen (Prev. CAIO) | Initial Draft. Established foundational Fairness by Design principle and basic disparate impact threshold. |
| 2.2 | 2023-01-20 | David Park | Major revision: Introduced formal Model Card mandate and integrated `meridian-fairness` library v1.0 as a technical control. Expanded Remediation Hierarchy. |
| 3.5 | 2023-09-12 | Dr. Marcus Rivera | Revised Roles and Responsibilities to include EU DPO consultation triggered by PII/PHI use in bias testing. Added Privacy consultation ticket step in Phase 1. Updated regulatory references. |
| 4.0 | 2024-01-09 | Dr. Marcus Rivera | Comprehensive restructuring. Introduced IRB role for Critical trade-off decisions. Mandated stratified splitting and proxy detection in Phase 2. Updated Continuous Monitoring to include automated drift alerting and ServiceNow integration. |
| 4.8 | 2025-07-01 | Dr. Marcus Rivera | Updated Vendor Assessment control (A-03) for third-party generative APIs. Refined training module codes for the '24-'25 cycle. No changes to detection thresholds or remediation hierarchy. Next review Jan 2026. |
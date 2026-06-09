---
sop_id: "SOP-FIN-001"
title: "Credit Scoring Model Governance"
business_unit: "Financial Services"
version: "3.6"
effective_date: "2025-09-03"
last_reviewed: "2026-12-01"
next_review: "2027-06-10"
owner: "Robert Liu, VP of Financial Services"
approver: "James Thornton, Chief Financial Officer"
classification: "Internal"
regulations:
  - "SR 11-7"
  - "EU AI Act"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: Credit Scoring Model Governance

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for the governance, development, validation, deployment, and decommissioning of credit scoring models utilized by the HealthPay Financial Services business unit of Meridian Health Technologies, Inc. The purpose is to ensure the safety, soundness, fairness, and regulatory compliance of all automated lending decisions, aligning with the Board’s risk appetite and the company’s commitment to ethical AI.

### 1.2 Scope
This SOP applies to all models classified within the Credit Scoring Model Inventory, including but not limited to:
- **Origination Models:** Patient financing eligibility and term assignment models.
- **Collection Models:** Early-stage delinquency prediction and optimal contact strategy models.
- **Fraud Models:** Application fraud and synthetic identity detection models.

This SOP applies to all employees, contractors, and third-party vendors who design, develop, implement, validate, use, or oversee these models across all Meridian Health Technologies global offices. All models are subject to this governance framework regardless of development origin (in-house, vendor-supplied, or open-source derived).

### 1.3 Regulatory Alignment
This SOP is designed to align with the following regulatory and industry standards:
- **SR 11-7:** Federal Reserve Supervisory Guidance on Model Risk Management.
- **EU AI Act:** Regulation (EU) 2024/1689, specifically for high-risk AI systems per Annex III, point 5(b) related to creditworthiness assessment.
- **NIST AI RMF 1.0:** AI Risk Management Framework.
- **Regulation (EU) 2025/XXXX:** The EU Artificial Intelligence Act (final text).
- **SOC 2 Type II:** Trust Services Criteria for Security, Availability, and Processing Integrity.

---

## 2. Definitions and Acronyms

| Term | Definition |
| :--- | :--- |
| **AI System** | A machine-based system designed to operate with varying levels of autonomy, that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments (per OECD/EU AI Act). |
| **Credit Scoring Model** | Any quantitative method, system, or approach that is used to assign a credit score, estimate a probability of default, or inform a credit decision. This includes both traditional statistical models and AI/ML systems. |
| **Deployer** | Any natural or legal person, public authority, agency, or other body using an AI system under its authority, except where the AI system is used in the course of a personal non-professional activity (per EU AI Act Art. 3(4)). Meridian Health Technologies is the Deployer for all models in scope. |
| **Model Developer** | The internal team or external vendor responsible for the initial design, coding, and documentation of the model. |
| **Model Inventory** | The centralized, authoritative record of all models in scope, maintained in the Meridian Model Risk Management System (MRMS). |
| **Model Owner** | The senior business leader accountable for the end-to-end lifecycle of a specific model, including its performance, use, and decommissioning. |
| **Model Validator** | A qualified independent party performing an objective review of a model's conceptual soundness, performance, and compliance with this SOP. |
| **Model Risk Tier** | A classification (A, B, or C) assigned to each model reflecting its materiality and complexity, which dictates the stringency of governance controls. |
| **PHI** | Protected Health Information, as defined by HIPAA. |
| **SME** | Subject Matter Expert. |

| Acronym | Expansion |
| :--- | :--- |
| AI RMF | Artificial Intelligence Risk Management Framework |
| AUROC | Area Under the Receiver Operating Characteristic Curve |
| DPO | Data Protection Officer |
| FPR | False Positive Rate |
| FRB | Federal Reserve Board |
| GDPR | General Data Protection Regulation |
| MRE | Model Risk Exception |
| MRMS | Model Risk Management System (Salesforce-based internal tool) |
| NIST | National Institute of Standards and Technology |

---

## 3. Roles and Responsibilities

### 3.1 Governance RACI Matrix

| Role | Model Lifecycle | Ongoing Monitoring | Validation | Exception Approval | External Audit |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Model Owner** | A | R | C | I | C |
| **Model Developer** | R | C | I | I | C |
| **Independent Model Validator** | I | I | R | C | C |
| **VP of Financial Services (Robert Liu)** | A | A | C | A | R |
| **Chief AI Officer (Dr. Marcus Rivera)** | C | C | R | A | C |
| **Chief Compliance Officer (Thomas Anderson)** | C | C | C | I | R |
| **Data Protection Officer (Dr. Klaus Weber)** | C | I | I | C | C |
| **Internal Audit** | I | I | I | I | A |
*Key: R=Responsible, A=Accountable, C=Consulted, I=Informed*

### 3.2 Role Details

- **Model Owner:** Typically a Director or VP within the Financial Services business unit. Accountable for the business outcome of the model, ensuring model documentation is complete and accurate, funding the validation process, and implementing required corrective actions. The Model Owner initiates the model lifecycle and is the primary point of contact for all model-related questions.
- **Independent Model Validator:** This function reports administratively to the VP of Financial Services but has an independent reporting line to the Chief AI Officer for technical findings and the Chief Compliance Officer for compliance-related findings. The Chief AI Officer is ultimately responsible for ensuring the validator’s independence. No member of the model development team may serve as the Independent Model Validator for a model they built. The roles of model owner and validator, while separate, both provide critical oversight.
- **Chief Privacy Officer / DPO (Dr. Klaus Weber):** Must be consulted for any model that processes personal data of EU residents, per GDPR Art. 35, to conduct or advise on a Data Protection Impact Assessment (DPIA). Responsible for ensuring the processing of special category data for bias detection meets the requirements of GDPR Art. 9.

---

## 4. Policy Statements

4.1 **All models are subject to independent validation prior to production deployment.** No model will be deployed without a formal, documented, and approved validation report on file in the MRMS.

4.2 **Fair and ethical lending is a foundational requirement.** Models must not discriminate against any protected class. Meridian adheres to a "fairness by design" principle. All credit scoring models must be assessed for adverse impact using both quantitative (statistical parity, equal opportunity difference) and qualitative (expert clinical review) methods.

4.3 **Explainability must be proportionate to model materiality.** All models, including AI/ML systems, must produce a clear, intelligible explanation of how key input features influence the credit score output, suitable for consumer-facing disclosure requirements under the EU AI Act Art. 86 and adverse action notices under the Fair Credit Reporting Act (FCRA).

4.4 **Model Risk Tiers.** Each model will be assigned a risk tier by the VP of Financial Services and the Chief AI Officer based on a standard risk assessment.
- **Tier A (High Risk):** Models that autonomously deny credit, set interest rates, or impact > 10,000 applicants annually. Material financial, legal, or reputational risk.
- **Tier B (Moderate Risk):** Models that inform but do not finalize credit decisions, such as collection prioritization models. Moderate financial or operational risk.
- **Tier C (Low Risk):** Support models with no direct customer impact (e.g., operational forecasting).

4.5 **Human Oversight Requirement.** Per the EU AI Act Art. 14, all high-risk AI systems (Tier A) must have effective human oversight built into the system and the operational workflow. The human-in-the-loop must have the authority, competence, and capacity to override the model's recommendation. The system architecture will prompt a mandatory manual review on every Tier A application identified as an "Adverse Decision."

---

## 5. Detailed Procedures

### 5.1 Model Lifecycle Management

The model lifecycle follows a strict, phased approach managed through the MRMS.

#### 5.1.1 Phase I: Initiation & Scoping (Lead: Model Owner)
1.  **Business Case Submission:** The Model Owner submits a formal business case through the MRMS, detailing the problem statement, proposed modeling approach, data sources, and proposed risk tier.
2.  **Data Privacy Review:** If the proposed data includes PHI or EU personal data, the DPO (Dr. Weber) is automatically notified to initiate a DPIA.
3.  **Tier Assignment & Approval:** The VP of Financial Services (Robert Liu) and Chief AI Officer (Dr. Marcus Rivera) jointly approve the risk tier within 10 business days. Their approval authorizes entry into the development phase.

#### 5.1.2 Phase II: Development & Documentation (Lead: Model Developer)
1.  **Development Workspace:** Development occurs within the secure Meridian AI Sandbox (AWS Sagemaker environment), isolated from production data systems.
2.  **Baseline Model Training:** Developers train candidate models using an approved baseline dataset.
3.  **Model Narrative Documentation:** The developer must produce a comprehensive "Model Narrative" document (see Section 5.3 for template) and upload it to the MRMS.
4.  **Performance Assessment:** The developer performs an initial performance assessment on out-of-sample, out-of-time test data. Target performance metrics must meet the thresholds defined in Table 5-A below. If performance metrics do not meet defined expectations, the Model Owner and Chief AI Officer must be notified with a remediation plan.

**Table 5-A: Minimum Performance Thresholds for Progression to Validation**

| Metric | Tier A | Tier B | Tier C | Measurement Method |
| :--- | :---: | :---: | :---: | :--- |
| AUROC | ≥ 0.72 | ≥ 0.68 | N/A | 10-fold stratified cross-validation |
| False Positive Rate (FPR) @ 10% Target | < 25% | < 30% | N/A | Confusion matrix analysis |
| Adverse Impact Ratio (AIR) | > 0.85 | > 0.80 | > 0.75 | Compared against the control group (most advantaged demographic) |

#### 5.1.3 Phase III: Independent Validation (Lead: Independent Model Validator)
This phase is the core of the model risk management framework and cannot begin until Phase II documentation is complete.
1.  **Validation Kick-off:** Model Owner formally requests validation in the MRMS, attaching the Model Narrative and model artifacts (code, weights, training logs).
2.  **Completeness Check:** Validator has 5 business days to perform a documentation completeness check.
3.  **Three-Lines-of-Defense Validation:** The validator conducts a thorough review covering:
    - **Conceptual Soundness:** Assessment of the theoretical basis, modeling technique selection, and variable transformations.
    - **Data Quality & Integrity:** Verification of data lineage, completeness, and appropriateness. Includes a review of how missing values and outliers were handled.
    - **Outcomes Analysis:** Replication of developer performance testing using a hold-out "gold set" unknown to the developer. Includes back-testing and sensitivity analysis.
    - **Fairness & Bias Audit:** Using the AI Trust and Bias (ATB) toolkit, the validator generates a detailed bias audit report, looking at slices of protected demographics. For models processing EU data, this is performed in conjunction with the DPO.
    - **Explainability Assessment:** For Tier A models, the validator must certify that the provided explanations (e.g., SHAP values) are consistent, stable, and intelligible by a non-data-scientist loan officer.
4.  **Validation Report:** The validator documents findings in a standard Validation Report. Findings are classified as:
    - **Material (High):** Critical flaw that makes the model unfit for its intended purpose. Deployment is blocked.
    - **Significant (Medium):** A weakness requiring a documented remediation plan and a follow-up re-validation within a specified timeframe.
    - **Advisory (Low):** A recommendation for improvement that does not impact the model's fundamental validity.
5.  **Sign-off:** The completed Validation Report, regardless of findings, is sent for sign-off to the Model Owner, VP of Financial Services, and Chief AI Officer.

#### 5.1.4 Phase IV: Deployment & Production Readiness (Lead: VP of IT Operations)
Deployment cannot proceed without a Validation Report showing no open Material (High) findings and an approved deployment request.
1.  **Deployment Request:** Model Owner submits a "Request for Production Deployment" form with the final, signed Validation Report.
2.  **Infrastructure Scrutiny:** VP of IT Operations (or delegate) confirms the production environment meets the Non-Functional Requirements (see Table 5-B below).

**Table 5-B: Non-Functional Requirements for Model Deployment**

| Requirement | Specification | Tooling |
| :--- | :--- | :--- |
| **Latency** | P99 response time for scoring API < 150ms | Datadog APM |
| **Throughput** | System must handle peak concurrent requests of 500/sec | JMeter load test report |
| **Drift Monitoring** | Input and Output data drift monitors must be active and connected to Datadog | Datadog, Evidently AI |
| **Explainability** | SHAP/LIME explanations must be stored in audit trail alongside the score | In-house Explainability Service (IES) |
| **Access Control** | Model API endpoint restricted to authorized service accounts only | Okta & AWS IAM |

3.  **Canary Deployment:** The model is deployed to a 5% traffic canary for a 72-hour observation period. During this time, the Developer and Validator monitor performance against stability metrics. A successful canary deployment clears the way for full rollout.

#### 5.1.5 Phase V: Decommissioning (Lead: Model Owner)
1.  **Trigger:** When a model's performance degrades beyond acceptable thresholds and cannot be remediated, or when the business use case ceases.
2.  **Decommissioning Plan:** The Model Owner creates a plan detailing how active decisions will be handled, data archives will be maintained, and all model artifacts will be securely removed from production. The plan is approved by the Chief AI Officer.
3.  **Final Audit:** The model files are securely archived in a read-only, immutable S3 bucket for a period of 7 years, and the model status in MRMS is changed to "Decommissioned."

### 5.2 Model Inventory Management
The MRMS is the system of record. It is the Model Owner's responsibility to ensure their models' records are continuously updated.
- **Minimum Data Model:** The MRMS must capture, at minimum: Model ID, Owner, Developer, Validation Status, Current Risk Tier, Data Sources, Data Sensitivity Level, and a complete audit log of all status changes.
- **Annual Attestation:** On December 1st of each year, every Model Owner must perform a formal attestation of completeness and accuracy for all models they own in the MRMS.

### 5.3 Key Process Templates
- **Form M-200: Model Narrative Document** — This is a mandatory template for Tier A models and highly recommended for Tier B. The document must contain:
    - Section 1: Executive Summary & Intended Use.
    - Section 2: Development Data (source, quality assessment, excluded populations).
    - Section 3: Model Theory & Architecture (algorithm selection rationale, feature engineering, hyperparameter tuning).
    - Section 4: Performance Evaluation (in-sample, out-of-sample, fairness/bias metrics).
    - Section 5: Implementation Guide (input variables, expected output format, known failure modes).
    - Section 6: Explanation Methodology (for explainable AI compliance).
- **Form M-102: Model Risk Exception (MRE) Request** — Used for any deviation from this SOP, per Section 8.
- **Form M-401: Production Deployment & Rollback Authorization** — The operational approval document.

---

## 6. Controls and Safeguards

### 6.1 Data Privacy Controls
- **Pseudonymization:** All PHI and personal identifiers (per GDPR Art. 4(5)) used for model training must be pseudonymized at the point of extraction from the production HealthPay database. The encryption key shall be stored separately in the centralized HashiCorp Vault.
- **Special Category Data:** Processing of data revealing racial or ethnic origin for the purpose of bias monitoring is only permitted under the strict control of the DPO, with a documented Article 9(2)(g) substantial public interest justification, logged and audited.

### 6.2 AI System Safeguards (EU AI Act Alignment)
- **Art. 10 Data Governance:** Before model training, the training, validation, and testing datasets must be assessed for relevance, representativeness, freedom from errors, and completeness. This assessment is a prerequisite checklist item in the Phase I Initiation.
- **Art. 12 Record-Keeping:** For all Tier A models, the system shall automatically generate logs comprising the events listed in Annex IV of the AI Act. This includes recording the date, time, originator, and result of every credit decision, with a retention period of no less than 10 years in an immutable, timestamped audit trail (Meridian's "Secure Ledger" service).
- **Art. 15 Accuracy, Robustness, and Cybersecurity:** The production deployment checklist (Section 5.1.4) must include a penetration test and adversarial robustness assessment report completed by the Meridian Product Security (ProdSec) team, renewed annually.

### 6.3 Model Access Control
All model artifacts (code, model weights, training data schemas) are stored in the Meridian Models Repository (AWS CodeCommit). Access is governed by a Role-Based Access Control (RBAC) matrix maintained by IT. No individual shall have both developer write access and production read access.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Ongoing Monitoring Program
All deployed Tier A and B models are subject to an automated ongoing monitoring program, running on a daily basis, to detect performance degradation and concept drift. The monitoring framework, powered by the Evidently AI and Datadog platforms, generates a weekly "Model Health Report" for each model.

### 7.2 Key Performance Indicators (KPIs)
The following KPIs are tracked on a real-time dashboard and are subject to quarterly formal reviews:

| KPI | Calculation | Target Threshold | Alert Severity |
| :--- | :--- | :--- | :--- |
| **Population Stability Index (PSI)** | `∑(Actual% - Expected%) * ln(Actual%/Expected%)` | PSI < 0.15 | P1 - Critical for PSI > 0.25 |
| **Characteristic Drift Rate** | % of top 20 input features with JS Divergence > 0.1 | < 20% of features | P2 - High for > 40% |
| **Default Rate by Score Band** | `(Defaults in Band / Total in Band)` | Monitored for inversion | P2 - High deviation from baseline |
| **Adverse Action Rate** | `(Denials / Total Applications)` | Monitored vs. historical baseline | P3 - Moderate for ±15% shift |
| **Human Override Rate** | `(Manual Overrides / System Decisions)` | Monitored for trend; target < 2% | P2 - High for P99 override time > 5s |

### 7.3 Annual Review
No later than the anniversary of the last review, each Tier A model undergoes a full re-validation, following the same standards as the initial Phase III (Section 5.1.3). Tier B models are subject to a streamlined, risk-based annual review focusing on outcomes analysis and PSI review. The performance of all models is reported quarterly to the Board Risk Committee.

---

## 8. Exception Handling and Escalation

### 8.1 Model Risk Exception (MRE)
Any deviation from this SOP, including the deployment of a model before material validation findings are closed, requires a formal MRE.
1.  **Submission:** The Model Owner submits Form M-102, detailing the nature of the exception, the compensating controls in place, and the permanent remediation plan with a firm deadline.
2.  **Approval Authority:**
    - **Tier C & Advisory Findings (Low):** VP of Financial Services (Robert Liu).
    - **Tier B & Significant Findings (Medium):** VP of Financial Services and Chief AI Officer (Dr. Marcus Rivera) jointly.
    - **Tier A & Material Findings (High):** Cannot be approved. Any MRE for Tier A material findings requires a formal appeal to the Chief Risk Officer, who will brief the Board Risk Committee Chair.

### 8.2 Escalation
- **Performance Degradation:** If a KPI alert (Table 7-A) is not resolved within 48 hours, it is automatically escalated from the Model Owner to the VP of Financial Services. If it persists for 5 business days, it is escalated to the Chief AI Officer and the Chief Financial Officer.
- **Bias Incident:** Any substantiated finding of discriminatory bias is escalated immediately to the Chief AI Officer, the DPO, and the Chief Compliance Officer, triggering the Meridian Incident Response Protocol (SOP-SEC-003).

---

## 9. Training Requirements

All personnel involved in the credit scoring model lifecycle must complete mandatory training, tracked via the Workday Learning Management System.

| Training Module | Audience | Frequency | Provider |
| :--- | :--- | :--- | :--- |
| **FIN-101: Credit Model Governance Fundamentals** | All Model Owners, Developers, Validators | Annually | Internal LMS (compliance team) |
| **FIN-201: SR 11-7 & MRM Regulatory Landscape** | Model Owners, Validators, Internal Audit | Annually | External Consultant (e.g., Oliver Wyman) |
| **AI-301: Fairness and Bias in AI Lending Systems** | All Model Owners, Developers, Validators | Semi-Annually | Chief AI Officer's office, DPO |
| **FIN-202: EU AI Act & Deployer Obligations** | All staff involved with Tier A models | Annually | External Legal Counsel |
| **SEC-101: Secure Development & Deployment** | Model Developers | On Assignment, then Annually | Meridian Product Security Team |

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs
- **SOP-MRM-001:** Enterprise Model Risk Management Framework
- **SOP-FIN-002:** Adverse Action and Credit Denial Notices
- **SOP-DP-005:** Data Protection Impact Assessment (DPIA) Procedure
- **SOP-AI-001:** AI Ethics and Fairness Policy
- **SOP-SEC-003:** Information Security Incident Response Plan
- **SOP-RDE-008:** Secure Product Development Lifecycle

### 10.2 External Standards and Regulatory References
- **SR Letter 11-7:** Supervisory Guidance on Model Risk Management, Board of Governors of the Federal Reserve System, April 4, 2011.
- **Regulation (EU) 2024/1689 (AI Act):** Laying down harmonized rules on artificial intelligence.
- **NIST AI 100-1:** Artificial Intelligence Risk Management Framework (AI RMF 1.0), January 26, 2023.
- **Fair Credit Reporting Act (FCRA):** 15 U.S.C. § 1681 et seq.
- **Equal Credit Opportunity Act (ECOA):** 15 U.S.C. § 1691 et seq.

---

## 11. Revision History

| Version | Date | Author | Revision Description | Approver |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 2021-03-15 | Sarah Jenkins, Dir. of Compliance | Initial creation of model risk governance framework. | David Chen, VP Fin. Svcs. |
| 2.1 | 2022-07-22 | Mark Williams, Sr. Validator | Major update to incorporate independent validation phase and three-lines-of-defense model. | David Chen, VP Fin. Svcs. |
| 2.5 | 2023-11-05 | Robert Liu, VP Fin. Svcs. | Added risk tiering definitions, refined scope for vendor models, added annual attestation. | James Thornton, CFO |
| 3.0 | 2024-06-14 | Anya Sharma, Chief AI Council | Comprehensive update to align with NIST AI RMF 1.0; introduce AI risk categories (GOVERN, MAP); update fairness/bias testing requirements. | James Thornton, CFO |
| 3.3 | 2025-04-10 | Dr. Marcus Rivera, CAIO | Incorporated preliminary EU AI Act requirements; defined deployer role; added templates for model narrative and MRE. | James Thornton, CFO |
| 3.6 | 2025-09-03 | Robert Liu, VP Fin. Svcs. | Full EU AI Act Art. 10, 12, 14, 15, 25, 86 alignment review; added specific quantitative thresholds for performance; revised training curricula; updated all roles to current state. | James Thornton, CFO |
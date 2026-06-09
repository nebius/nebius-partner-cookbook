---
sop_id: "SOP-FIN-020"
title: "Fair Lending Compliance"
business_unit: "Financial Services"
version: "3.2"
effective_date: "2025-07-28"
last_reviewed: "2026-12-23"
next_review: "2027-06-24"
owner: "Robert Liu, VP of Financial Services"
approver: "James Thornton, Chief Financial Officer"
classification: "Internal"
regulations:
  - "SR 11-7"
  - "EU AI Act"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Fair Lending Compliance

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, governance, and operational controls for ensuring fair lending compliance across all Meridian Health Technologies, Inc. (“Meridian”) HealthPay Financial Services products, including patient financing, medical lending, and automated credit decisioning models. This document formalizes the company’s commitment to preventing discriminatory outcomes in credit transactions, ensuring equitable access to healthcare financing for all protected classes, and maintaining strict adherence to applicable regulatory standards.

The purpose of this SOP is to:

- Define the end-to-end lifecycle management of fair lending risk, from model development through ongoing monitoring and remediation.
- Establish rigorous testing protocols for disparate impact, disparate treatment, and proxy discrimination using advanced statistical methodologies.
- Ensure compliance with the Equal Credit Opportunity Act (ECOA), Fair Credit Reporting Act (FCRA), SR 11-7 guidance, the EU AI Act (Regulation 2024/1689), and the General Data Protection Regulation (GDPR).
- Operationalize the governance framework under the NIST AI Risk Management Framework (AI RMF 1.0) and align with Meridian’s existing SOC 2 Type II and HITRUST CSF control environments.

### 1.2 Scope

This SOP applies to all business activities, personnel, and third-party relationships within the HealthPay Financial Services business unit, including:

- **Products:** Patient financing loans (MedCredit, CarePay), revolving medical credit lines (HealthLine), and provider-integrated pre-qualification engines.
- **Models:** All proprietary, third-party, and hybrid statistical models, machine learning (ML) algorithms, and rules-based engines that influence credit adjudication, risk-based pricing, credit limit assignment, or adverse action determinations. This includes models developed using PyTorch, TensorFlow, and models served via AWS SageMaker endpoints.
- **Data:** All structured and unstructured data used for model training, validation, and inference, including alternative data sources (e.g., propensity-to-pay scores derived from provider billing histories), stored in Snowflake, PostgreSQL, and AWS S3 data lakes.
- **Personnel:** All full-time employees, contractors, and consultants within the Financial Services business unit, Data Science department, Risk Management, Legal, and Compliance teams who develop, deploy, validate, or audit credit models.
- **Third Parties:** Any external vendor providing credit decisioning services, alternative data, or analytic tools, including but not limited to credit bureau integrators, alternative data aggregators, and SaaS providers with model hosting capabilities.
- **Jurisdictions:** Operations in the United States, Canada, and the European Union (specifically member states where HealthPay is offered). This SOP is effective for all locations as of **2025-07-28** and remains in force until superseded.

### 1.3 Out of Scope

The following items are explicitly outside the scope of this SOP and are governed by separate policies:

- General anti-fraud controls not directly related to protected class bias (See SOP-SEC-045: Fraud Detection and Prevention).
- Data privacy and subject access rights unrelated to credit decisions (See SOP-PRI-012: Data Subject Access Request Handling).
- Clinical AI model management, even if leveraged for risk segmentation (See SOP-CAI-105: Clinical AI Model Lifecycle Management).

## 2. Definitions and Acronyms

| Term | Definition |
| :--- | :--- |
| **Adverse Action** | A denial or revocation of credit, a change in the terms of an existing credit arrangement, or a refusal to grant credit in substantially the amount or on substantially the terms requested, as defined by ECOA and FCRA. |
| **Adverse Impact Ratio (AIR)** | A quantitative metric calculated by dividing the approval rate for a specific protected class group by the approval rate for a control group (typically the most favored group). An AIR below 0.80 (80% rule) triggers mandatory remediation review. |
| **Alternative Data** | Non-traditional credit data used in underwriting models, including medical payment history, provider billing analytics, and demographic data proxies. |
| **BISG Proxy** | Bayesian Improved Surname Geocoding, a statistical method used to impute race and ethnicity when self-reported data is unavailable, used strictly for bias testing and not for credit decisioning. |
| **Consequence Management** | The formal process of risk assessment, mitigation, and model recalibration triggered by a breach of pre-defined fair lending thresholds. |
| **Disparate Impact** | A facially neutral policy or practice that disproportionately excludes or burdens members of a protected class, even without intentional discrimination. |
| **Disparate Treatment** | Overt and intentional discrimination against a protected class applicant. |
| **ECOA** | Equal Credit Opportunity Act (U.S. Code Title 15, Chapter 41). |
| **EU AI Act** | Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence. |
| **Fair Lending Risk Tier** | A classification assigned to each model (Tier 1 - Critical, Tier 2 - High, Tier 3 - Moderate) based on volume, complexity, and EU AI Act classification. |
| **FCRA** | Fair Credit Reporting Act (U.S. Code Title 15, Section 1681). |
| **Model Risk Tier** | Classification aligning with SR 11-7 and EU AI Act risk levels, determining the cadence and intensity of validation and monitoring. |
| **Proxy Discrimination** | A form of disparate impact where a facially neutral variable serves as a close proxy for a protected class characteristic (e.g., ZIP code as a proxy for race). |
| **Protected Class** | A group of persons protected by law from discrimination. Under ECOA: race, color, religion, national origin, sex, marital status, age, receipt of public assistance, and good faith exercise of rights under the Consumer Credit Protection Act. Under EU AI Act: any group protected by EU non-discrimination law (Article 21, EU Charter of Fundamental Rights). |
| **Regulatory Action Trigger (RAT)** | A pre-defined metric threshold which, if breached, mandates immediate notification to the Chief Compliance Officer and a halt to model inference for net-new originations. |
| **Shapley Additive Explanations (SHAP)** | A game-theoretic approach to explain the output of machine learning models, used to generate applicant-level adverse action reasons and feature importance analysis. |

## 3. Roles and Responsibilities

A Responsibility Assignment Matrix (RACI) is defined below. “R” denotes Responsible (doer), “A” denotes Accountable (approver), “C” denotes Consulted, and “I” denotes Informed.

| Activity / Decision | Model Developer | Model Owner | Independent Validator | Fair Lending Officer | Chief Compliance Officer | AI Governance Committee |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Model Development & Feature Selection** | R | A | C | C | I | I |
| **Disparate Impact Testing (Initial)** | R | C | A | R | I | I |
| **Alternative Data Governance Approval** | C | R | C | A | I | A |
| **EU AI Act Conformity Assessment (Art. 16)** | R | A | R | C | C | A |
| **Ongoing Monitoring Report Generation** | I | R | A | R | I | C |
| **Breach of Adverse Impact Ratio < 0.80** | I | I | R | A | C | A |
| **Adverse Action Reason Code Validation** | R | A | C | C | I | I |
| **GDPR Automated Decision-Making Review (Art. 22)** | I | R | C | A | A | I |

### 3.1 Named Roles and Specific Duties

- **Robert Liu, VP of Financial Services (Executive Sponsor & SOP Owner):** Serves as the ultimate accountable officer for fair lending compliance within the business unit. Approves annual fair lending budget, sanctions remediation plans over $250,000, and chairs the quarterly Fair Lending Governance Forum.
- **Dr. Anya Sharma, Director of Fair Lending Analytics (Independent Validator):** Leads a functionally independent team, walled off from model development profit-and-loss pressure, responsible for all quantitative testing. Reports administratively to the Chief Risk Officer but has a dotted-line reporting obligation to the Chair of the Audit Committee.
- **Fair Lending Officer (Compliance):** A dedicated role within the Compliance department responsible for regulatory horizon scanning, adverse action template review, and fielding consumer complaints related to potential discrimination.
- **Model Owner:** The business-line VP or Director who owns the profit-and-loss for a specific credit product and serves as the primary accountable party for the model's overall performance and risk governance.

## 4. Policy Statements

The following high-level policy commitments govern all fair lending activities at Meridian.

1.  **Zero Tolerance for Disparate Treatment:** Meridian expressly prohibits any intentional discrimination in any aspect of a credit transaction. The deliberate use of a protected class characteristic (e.g., race, gender, age) or a known, direct proxy as a predictive variable or decisioning factor is strictly forbidden.
2.  **Mandatory Disparate Impact Testing:** All credit decisioning models, prior to production deployment and annually thereafter (semi-annually for Tier 1 models), must undergo rigorous statistical testing for disparate impact. Testing must be conducted by the Independent Validator using the BISG proxy methodology on all applicable ECOA and EU non-discrimination protected classes where direct data is missing.
3.  **Explainability and Reason Codes:** Every automated credit decision must be accompanied by a set of principal reason codes, generated via SHAP values or equivalent model-agnostic explainer tools. These reason codes must be intelligible, accurate, and provided to the applicant or counterparty in compliance with ECOA adverse action notices and GDPR Articles 13, 14, and 22.
4.  **Alternative Data Stewardship:** Any non-traditional data source (e.g., provider billing history, geolocation data) must be approved by the Fair Lending Officer and AI Governance Committee before use in model development. A Proxy Discrimination Risk Assessment (PDRA) must be filed and approved for every alternative data feature.
5.  **Right to Human Review (EU AI Act Compliance):** For all credit decisions processed by high-risk AI systems within the European Union, Meridian guarantees the right to obtain human intervention on the part of the controller, to express his or her point of view, and to contest the decision, as mandated by Article 14(5) and Article 86 of the EU AI Act.

## 5. Detailed Procedures

This section outlines the complete fair lending lifecycle. Each procedure is mandatory unless a formal exception is documented and approved per Section 8.

### 5.1 Model Risk Tiering and Initial Classification

Before a new model or a major retrain of an existing model enters development, it must be risk-tiered.

1.  **Initiator:** The Model Developer completes Form FL-101: Model Risk Classification Request.
2.  **Tiering Criteria:**
    - **Tier 1 (Critical):**
        - Annual origination volume > 50,000 loans.
        - Model constitutes a "high-risk AI system" under EU AI Act Annex III, Clause 5(b).
        - Model leverages complex neural architectures (e.g., Transformer-based models) or > 500 input features.
    - **Tier 2 (High):**
        - Annual origination volume between 5,000 and 50,000 loans.
        - Model is a gradient-boosted tree or ensemble model using traditional bureau and Meridian proprietary data.
    - **Tier 3 (Moderate):**
        - Model is a rules-based engine or simple logistic regression.
        - Annual originations < 5,000.
3.  **Review:** The AI Governance Committee reviews the FL-101 form within 10 business days. The VP of Financial Services has final veto authority over tier assignments.

### 5.2 Pre-Deployment Fair Lending Testing

The Independent Validator must complete this testing and produce the "Final Fair Lending Assessment Report (FL-200)" before the model can be deployed to a Production (prod) AWS SageMaker endpoint or equivalent operational environment.

1.  **Data Acquisition:** The Validator extracts the development sample (Snowflake schema `FIN_DL_MODELING`) and the holdout/out-of-time validation sample.
2.  **BISG Imputation:** Race and ethnicity probabilities are imputed using the BISG method via Meridian’s secure analytics environment (Databricks, `bias_audit` cluster), strictly locked from production model pipelines.
3.  **Threshold Analysis:**
    - For each protected class group (e.g., Black, Hispanic, Female, Age > 62), the Validator calculates the Adverse Impact Ratio (AIR).
    - The threshold for a mandatory remediation review is set at an AIR of **< 0.85** for Tier 1 models and **< 0.80** for Tier 2 and Tier 3 models.
4.  **Proxy Discrimination Scan:** The Validator utilizes a proprietary "Feature-Proteus" script to scan all active model features. Any feature exhibiting > 0.6 Spearman correlation to a BISG-imputed protected class is flagged as a High-Risk Proxy. Model Developers must provide an overriding business necessity justification for retaining a High-Risk Proxy, subject to approval by the Fair Lending Officer.
5.  **Outcome Deterministic Test:** The Validator re-runs the entire validation sample through the model, substituting protected class proxy features with a neutral default. The variance in approval rate constitutes the "Marginal Disparate Impact." A variance > 5% requires remediation before production launch.
6.  **Sign-Off:** The Independent Validator signs the FL-200 report. The Model Owner and Fair Lending Officer counter-sign, acknowledging the risk profile.

### 5.3 SR 11-7 Alignment – Model Development and Validation

All credit models must adhere to Meridian’s Model Risk Management framework, which aligns with SR 11-7 principles of effective challenge and governance.

1.  **Development Standards:** Model Developers must document all steps of the model development process, including theory, design, data selection, feature engineering, and training logic, within a Model Development Document (MDD) stored in the Meridian internal repository (Confluence).
2.  **Independent Review:** An "Independent Review" of the model is conducted by the Fair Lending Analytics team. This review challenges the model's conceptual soundness and methodology but does not constitute an independent validation in the strictest sense of a separate, ring-fenced quantitative audit.
3.  **Ongoing Monitoring:** Upon deployment, the model must undergo ongoing monitoring. This monitoring confirms stability and predictive power. The specific performance thresholds for this monitoring, including the boundary limits for concept drift and feature stability indexes, are detailed in the model's MDD. The governance structure outlines that a designated Model Owner is responsible for the business application, and a review of effectiveness is overseen by the risk function.

### 5.4 EU AI Act Compliance Protocol (Specific Procedure)

Given that Meridian’s HealthPay lending model constitutes a “high-risk AI system” under Annex III, the following rigorous procedure is mandatory for all EU (and UK voluntary compliance) deployments.

**Reference: Article 16 (Obligations of Providers), Article 17 (Quality Management System), Article 20 (Automatically Generated Logs), Article 86 (Right to Explanation).**

1.  **Conformity Assessment (Art. 16, Art. 43):** Before placing a model on the EU market, the Data Science team, led by the EU Compliance Lead, must conduct a conformity assessment against the requirements of Title III, Chapter 2 of the EU AI Act. The assessment package includes:
    - FL-EU-101: EU AI Act Conformity Checklist.
    - A detailed description of the model’s intended purpose and foreseeable misuse.
    - Model Card, version 2.1 or higher, published to the internal EU AI Registry.
    - The assessment must be completed and approved by the AI Governance Committee within **30 calendar days** before the planned EU go-live date.
2.  **Quality Management System (Art. 17):** The provider (Meridian) maintains a proportionate and effective QMS, documented in Confluence space "QMS-EU-AI." This QMS documents:
    - The fair lending strategy and regulatory interpretation.
    - Design, design verification, and quality control procedures.
    - Technical documentation including specifications of training, testing, and validation data (art. 18).
    - The system is audited internally every 180 days by the Internal Audit team.
3.  **Human Oversight (Art. 14, Art. 5(1)(e)):** The specific human-oversight interface is the "CareTeam Dispute Console." If an applicant is denied via the automated system, they are instructed to contact CareTeam. During a dispute review, the CareTeam Agent is presented with the full application and a SHAP-based feature importance waterfall chart. The Agent, who has received mandatory EU AI Act training, has the override authority to approve the loan. Every override decision (overturned or upheld) is logged with the Agent’s unique identifier and a mandatory narrative justification.
4.  **Transparency and Explanations (Art. 86, Art. 13):** The Adverse Action Notice (AAN) provided to the applicant must include:
    - "This decision was produced by an automated high-risk AI system."
    - The top 3 SHAP-derived principal reason codes in plain, intelligible language.
    - Clear and accessible contact details for the CareTeam Dispute Console, with an explicit notification of the right to human intervention and contestability. A standardized template `T-EU-AAN-01` is maintained by the Fair Lending Officer.

### 5.5 GDPR Automated Decision-Making Compliance (Specific Procedure)

**Reference: Article 22 (Automated individual decision-making), Article 35 (Data Protection Impact Assessment).**

1.  **Data Protection Impact Assessment (DPIA):** A comprehensive DPIA (Template `T-PRI-DPIA-03`) must be completed for every Tier 1 and Tier 2 model before processing any personal data of EU residents. This DPIA explicitly evaluates the necessity and proportionality of automated processing and the risks to the rights and freedoms of data subjects. The DPIA is reviewed and approved by the Data Protection Officer (DPO) and entered into the central DPIA Register within **15 business days**.
2.  **Article 22(3) Safeguards:** Meridian relies on the "necessary for entering into, or performance of, a contract" lawful basis (Art. 22(2)(a) / Art. 6(1)(b)). To satisfy Article 22(3), the following safeguards are programmatically enforced:
    - **Right to Human Intervention:** Defined and operationalized in Section 5.4.4 above, the Dispute Console is the legally mandated safeguard.
    - **Measurable Metrics:** The CareTeam's performance on EU disputes is tracked monthly. Key metrics include:
        - Time-to-first-human-response (SLA: < 4 hours during business hours).
        - Decision override rate.
        - Override sustain rate (post-hoc review of overrides to ensure they were not discriminatory).
3.  **Data Minimization and Bias Monitoring (Art. 5(1)(c) & Art. 35(7)(b)):** The DPIA must include a technical appendix showing that model features are adequate, relevant, and limited. The ongoing monitoring regime (Section 7) acts as the periodic review of bias risk.

### 5.6 Remediation and Consequence Management

When a RAT is breached or a significant bias concern is identified, the following remediation procedure is initiated.

1.  **Immediate Containment (T 0 hours):** The Responsible ML Engineer, upon alert from the Fairness Monitor Dashboard (Grafana), evaluates the severity. If the alert is classified as 'P1 - Critical' (e.g., Tier 1 AIR < 0.70), they initiate the Feature Flag Kill Switch (`meridian.exp.global_kill`) for the offending model version, immediately halting new originations under that model. Existing pending applications are queued for manual adjudication.
2.  **Root Cause Analysis (T + 48 hours):** The Model Developer and Independent Validator form a "War Room" to conduct a forensic root cause analysis. This analysis identifies the specific feature interactions, data drift, or coding errors causing the bias.
3.  **Model Recalibration:** The Model Developer develops a remediated model version. This version undergoes the full Pre-Deployment Fair Lending Testing procedure (Section 5.2) as a "new" model.
4.  **Retrospective Review and Remediation of Past Harm:** The Fair Lending Officer leads a review of the affected population (all applications scored by the biased model during the period of peak bias). If a pattern of potential economic harm is identified (e.g., a protected class group was systematically over-denied), Meridian will proactively contact affected individuals, re-evaluate their applications under the new model, and offer credit if qualified, along with a remediation letter acknowledging the re-evaluation.

## 7. Monitoring, Metrics, and Reporting

Ongoing monitoring is critical to validate that models operate as approved and to detect emergent bias.

### 7.1 Key Performance Indicators (KPIs) and Metrics

The Fair Lending Analytics dashboard, hosted in Grafana ("Fair Lending Command Center"), displays near-real-time metrics on all active credit models.

| Metric | Definition | Regulatory Threshold (Tier 1) | Regulatory Action Trigger (RAT) |
| :--- | :--- | :--- | :--- |
| **AIR – Race/Ethnicity** | Approval rate ratio for BISG-imputed groups vs. Non-Hispanic White. | < 0.85 | < 0.75 |
| **AIR – Gender** | Approval rate ratio for Female applicants vs. Male applicants. | < 0.90 | < 0.80 |
| **AIR – Age (>62)** | Approval rate ratio for applicants over 62 vs. applicants under 62. | < 0.80 | < 0.70 |
| **Proxy Risk Index (PRI)** | A composite score (0-100) measuring the aggregate proxy risk of all features, weighted by SHAP importance. | > 25 | > 45 |
| **Adverse Action Reason Code Stability Index (CSI)** | Jensen-Shannon divergence comparing daily distribution of top-5 reason codes to a 90-day baseline. | JS Divergence > 0.15 | JS Divergence > 0.30 |
| **EU Override Rate** | Number of CareTeam overrides divided by total EU automated denials. | N/A (Monitoring) | Statistically anomalous shift ( > 3 Standard Deviations from 6-month mean) |

### 7.2 Reporting Cadence and Recipients

| Report Name | Frequency | Author | Audience |
| :--- | :--- | :--- | :--- |
| **Fair Lending Weekly Flash Report** | Weekly (Monday 10:00 AM ET) | Fair Lending Analytics | VP of Financial Services, Head of Underwriting |
| **Model Health & Bias Monitoring Dashboard** | Real-time | Data (Automated) | ML Engineering, Model Owner |
| **Quarterly Fair Lending Governance Forum (QFGF) Pack** | Quarterly | Fair Lending Officer | AI Governance Committee, CRO, CFO |
| **Annual ECOA/FCRA Board of Directors Report** | Annually | Chief Compliance Officer | Board of Directors, Audit Committee Chair |

### 7.3 EU AI Act Post-Market Monitoring (Article 61)

For EU models, the quarterly QFGF pack includes a specific “EU AI Act Post-Market Monitoring Report.” This report documents any instances of the model performing in an unexpected manner that could present a risk to fundamental rights and non-discrimination. The report is filed into the Technical Documentation (Annex IV) and retained for 10 years.

## 8. Exception Handling and Escalation

### 8.1 Exception Handling

A formal exception must be requested if a business unit needs to temporarily deviate from a policy statement or procedure (e.g., deploying a model with an AIR of 0.82 on a Tier 1 model due to an urgent business need).

1.  **Request:** Model Owner submits Form FL-EX-001, detailing the specific procedure element deviated from, the business justification, the compensating controls, and a proposed exit plan date.
2.  **Risk Assessment:** The Independent Validator appends a quantitative assessment of the added risk (e.g., "This exception increases marginal disparate impact risk by 2%").
3.  **Approval Authority:**
    - Tier 3 exceptions: Approved by the Fair Lending Officer.
    - Tier 2 exceptions: Approved by the Fair Lending Officer and the Chief Compliance Officer.
    - Tier 1 exceptions (including any deviation from EU AI Act conformity): Approved by the AI Governance Committee and the Chief Risk Officer. No exceptions are granted for the mandatory human oversight requirements under Article 14 of the EU AI Act.

All approved exceptions are logged in the central Risk and Compliance Register (ServiceNow GRC) and are reviewed quarterly. No exception may exceed a duration of 180 days without a formal re-approval.

### 8.2 Escalation Path for Suspected Discrimination

If any employee, contractor, or agent suspects a violation of this SOP or unlawful discrimination, they must follow the prescribed escalation path:

1.  **Immediate Manager:** Employee reports concern to their direct manager.
2.  **Fair Lending Officer:** If the concern is not resolved, or if the manager is implicated, the employee escalates directly to the Fair Lending Officer (dedicated Slack channel `#ask-fair-lending` or confidential email).
3.  **Speak Up Hotline:** As an alternative or anonymous channel, employees may use the third-party "Meridian Integrity Line," managed by Navex Global. All reports are handled per SOP-HR-081 (Whistleblower Protections and Investigations). Retaliation against good-faith reporters is strictly prohibited.

## 9. Training Requirements

| Audience | Course Title | Content | Frequency | Tool / Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **All Financial Services Staff** | `FL-100: Foundations of Fair Lending` | ECOA, FCRA, identification of redlining and steering risks, Meridian's commitment to equity. | Annually | Workday Learning (Completion tracked; 90% pass rate on final quiz) |
| **Model Developers (ML Engineers, Data Scientists)** | `FL-201: Algorithmic Fairness & Bias Detection` | Hands-on workshop covering BISG, SHAP for bias, disparate impact vs. disparate treatment, EU AI Act data requirements. | Semi-annually | Workday Learning + JupyterHub Lab practical. Lab must be completed with a score of 100%. |
| **Independent Validators / Fair Lending Analytics** | `FL-301: Advanced Fair Lending Testing` | Advanced statistical tests, Margin of error calculations, EU AI Act Art. 20 log interrogation. Certified by an external vendor (e.g., FICO or Fair Isaac). | On hiring, then Annually | External Cert (LinkedIn Learning) + Meridian Internal Assessment |
| **CareTeam (Dispute Console Staff)** | `FL-EU-102: EU AI Human Oversight & GDPR` | Procedures for contesting an AI decision, documenting overrides without introducing bias, handling sensitive data during a manual review, and the legal consequences of an override under the EU AI Act. | Quarterly | Workday Learning. Failure requires immediate re-training and suspension of override authority until passed. |

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

- **SOP-FIN-018:** Model Risk Management (SR 11-7 Framework)
- **SOP-PRI-012:** Data Subject Access Request (DSAR) Handling (GDPR)
- **SOP-PRI-015:** Data Protection Impact Assessment (DPIA) Procedure
- **SOP-SEC-045:** Fraud Detection and Prevention in Digital Channels
- **SOP-CAI-105:** Clinical AI Model Lifecycle Management
- **SOP-HR-081:** Code of Conduct, Whistleblower Protection, and Investigations

### 10.2 External Regulatory and Standards References

- **Regulation B (12 CFR Part 1002):** Equal Credit Opportunity Act (ECOA).
- **Fair Credit Reporting Act (FCRA), 15 U.S.C. § 1681.**
- **Regulation (EU) 2024/1689:** The EU Artificial Intelligence Act.
- **Regulation (EU) 2016/679:** General Data Protection Regulation (GDPR).
- **Federal Reserve SR Letter 11-7:** Guidance on Model Risk Management.
- **NIST AI RMF 1.0:** AI Risk Management Framework.

## 11. Revision History

| Version | Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2023-04-12 | Sarah Jenkins, VP of FS (prev.) | Initial creation of SOP. Established base ECOA testing procedures. |
| 2.0 | 2024-08-22 | Robert Liu | Major revision: incorporated EU AI Act and GDPR requirements post-market expansion launch. Added roles and responsibilities matrix. |
| 3.0 | 2025-06-15 | Anya Sharma, Ph.D. | Rewritten Section 5.2 to adopt BISG methodology and revised AIR thresholds from 0.90 to 0.85 for Tier 1 systems. Added Proxy Risk Index metric. |
| 3.1 | 2025-11-08 | Robert Liu | Revised to align with NIST AI RMF 1.0 publication. Added Section 6 controls table and enhanced Section 7 KPI definitions. |
| 3.2 | 2026-12-20 | Robert Liu | Annual review. Updated roles/responsibilities to reflect new org structure. Clarified SR 11-7 alignment in Section 5.3. Updated EU AI Act references post-draft amendments. No material changes to testing procedures. |
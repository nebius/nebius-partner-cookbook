---
sop_id: "SOP-CLIN-011"
title: "Drug Interaction Checking System"
business_unit: "Clinical AI Products"
version: "3.0"
effective_date: "2025-05-20"
last_reviewed: "2026-08-27"
next_review: "2027-02-21"
owner: "Dr. Aisha Okafor, VP of Clinical AI Products"
approver: "Dr. Priya Patel, Chief Medical Officer"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Drug Interaction Checking System

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the governance, operational, and technical framework for the Meridian Health Technologies Drug Interaction Checking System (DICS). The DICS is a Class III clinical decision support module integrated within the Clinical AI Platform. Its primary clinical function is to analyze patient-specific medication profiles against a curated knowledge base of drug-drug, drug-allergy, drug-food, and drug-laboratory interactions to generate real-time, context-aware alerts for healthcare providers.

The purpose of this SOP is to ensure that:
1.  The DICS operates in a safe, effective, and compliant manner across all deployments in North America and the European Union.
2.  The system adheres to the stringent requirements for High-Risk AI Systems under the **EU AI Act (Regulation 2024/1689)**, including but not limited to accuracy, robustness, transparency, and human oversight.
3.  The system and its operators maintain the privacy and security of Protected Health Information (PHI) in full compliance with **HIPAA (45 CFR Parts 160, 162, and 164)** .
4.  A consistent, auditable, and clinically validated process governs the lifecycle of alert logic, from knowledge base updates to end-user overrides.

### 1.2 Scope

This SOP applies to all components, personnel, and processes involved in the DICS lifecycle:

- **Personnel:** All Meridian employees, contractors, subcontractors, and third-party vendors who design, develop, deploy, test, validate, monitor, or support the DICS. This includes, but is not limited to, the Clinical AI Products, Engineering, Data Science, Compliance, Legal, Clinical Informatics, Customer Operations, and IT Operations teams.
- **Technical Components:**
    - The DICS inference engine (hosted on the Meridian SaaS Platform, AWS us-east-1 and eu-west-1).
    - The Meridian Curated Interaction Knowledge Base (MCI-KB).
    - The Alert Logic Engine, including all clinical decision support rules.
    - The Override Documentation Module within the electronic health record (EHR) integration layer.
    - Data pipelines ingesting, normalizing, and processing medication, allergy, and laboratory data.
    - All related monitoring, logging, and observability tools.
- **Deployments:** The DICS deployed in over 340 hospitals and clinics across North America and the EU.
- **Data:** Any patient data, including PHI, processed by the system.
- **External Systems:** Interfaces and APIs connecting Meridian’s SaaS Platform to customer EHR systems (e.g., Epic, Cerner, Meditech), pharmacy systems, and laboratory information systems.

This SOP is a subordinate document to the corporate AI Governance Policy (SOP-GOV-003) and operates in conjunction with the Clinical AI Lifecycle Management SOP (SOP-CLIN-010).

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **Adverse Drug Event (ADE)** | An injury resulting from the use of a drug, including harm caused by a drug interaction. |
| **Alert Fatigue** | A state of desensitization in a clinician caused by exposure to an excessive number of non-contextual or low-value alerts, leading to potential overriding of critical warnings. |
| **Alert Logic** | The set of deterministic and probabilistic rules, including machine learning models, that evaluate patient-specific data against the MCI-KB to determine if an alert should be fired and at what severity level. |
| **CDS** | Clinical Decision Support. |
| **Clinical AI Product Council** | A cross-functional governance body chaired by the VP of Clinical AI Products and including the Chief Medical Officer, Chief AI Officer, and VP of Engineering, responsible for reviewing and approving all high-risk CDS rules and significant changes to the DICS. |
| **Confidence Score** | A quantitative metric (0.0 to 1.0) produced by the ML-based interaction prediction model, reflecting the calculated probability and severity of a predicted interaction. |
| **Contraindication** | A specific situation in which a drug, procedure, or surgery should not be used because it may be harmful to the person. DICS handles absolute and relative contraindications. |
| **DICS** | Drug Interaction Checking System. This Meridian-specific system. |
| **EHR** | Electronic Health Record. |
| **EU AI Act** | Regulation (EU) 2024/1689 of the European Parliament and of the Council laying down harmonised rules on artificial intelligence. |
| **Explanatory Statement** | A plain-language, human-readable justification generated by the DICS for each alert, detailing the interacting substances, potential clinical outcome, and the evidence source. Mandated by EU AI Act Art. 13. |
| **Ground Truth** | Clinically validated reference data used to train and evaluate the accuracy of the ML-based interaction prediction model. |
| **High-Risk AI System** | As defined in Annex III of the EU AI Act, a system intended to be used for diagnosis, treatment decision-making, or managing patient care that poses a significant risk to health and safety. The DICS is classified as such. |
| **Human-in-the-Loop (HITL)** | A governance mechanism ensuring that a qualified clinician reviews and retains the authority to accept or override the DICS’s alert recommendation. |
| **MCI-KB** | Meridian Curated Interaction Knowledge Base. The proprietary, structured database of interaction evidence. |
| **Override** | An action by a qualified clinician to dismiss or disregard a DICS alert without changing the triggering medication order. |
| **Override Documentation** | A mandatory, structured, and timestamped record of the clinical rationale provided by a clinician when overriding an alert. |
| **Pharmacovigilance (PhV)** | The science and activities relating to the detection, assessment, understanding, and prevention of adverse effects or any other drug-related problem. |
| **PHI** | Protected Health Information, as defined by HIPAA. |
| **QMS** | Quality Management System, aligned with ISO 13485 and the Meridian AI Quality Management Framework (SOP-QMS-001). |
| **Severity Level** | A classification of the potential clinical harm of an interaction: `CRITICAL` (Contraindicated, high risk of life-threatening ADE), `MAJOR` (Clinically significant, requires intervention), `MODERATE` (Monitor closely), `MINOR` (Clinically insignificant). |

---

## 3. Roles and Responsibilities

The following RACI matrix defines the roles and responsibilities for the lifecycle of the DICS.

| Activity / Decision | Clinical AI VP (Dr. Okafor) | Medical Informatics Team | AI/ML Engineering Team | Platform Engineering Team | Chief Medical Officer (Dr. Patel) | Compliance Officer (T. Anderson) | Customer Support | Clinical End-User (Provider) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. MCI-KB Content Update & Clinical Validation** | A | R | C | I | A | I | I | I |
| **2. Alert Logic Rule Authoring & Tuning** | A | R | C | I | C | I | I | I |
| **3. Model Retraining & Ground Truth Validation** | C | R | R | I | C | I | I | I |
| **4. System Deployment & Rollback** | C | C | R | R | I | I | I | I |
| **5. SOC 2 & HIPAA Infrastructure Controls** | C | I | I | R | I | A | I | I |
| **6. EU AI Act Conformity Assessment** | R | R | R | R | A | R | I | I |
| **7. Clinical Alert Override & Documentation** | I | I | I | I | I | I | I | **R** |
| **8. System Safety & Pharmacovigilance Monitoring** | A | R | C | I | R | I | I | I |
| **9. 21 CFR Part 11 Audit Trail Review** | C | I | I | I | I | R | I | I |
| **10. End-User Training Delivery** | C | R | I | I | I | I | R | I |

**Key to RACI:**
- **R** (Responsible): The person(s) who do the work to complete the task.
- **A** (Accountable): The person ultimately answerable for the correct and complete finish of the task. This person signs off on the work.
- **C** (Consulted): A subject matter expert whose opinion is sought before a decision or action is taken. Two-way communication.
- **I** (Informed): A stakeholder who is kept up-to-date on progress, often one-way communication.

**Named Role Details:**
- **Dr. Aisha Okafor (VP, Clinical AI Products):** Ultimate owner of the product, accountable for product safety and commercial availability.
- **Dr. Priya Patel (Chief Medical Officer):** The highest clinical authority. Approves all Critical and Major severity alert logic and any override analytics report signaling a potential safety issue.
- **Clinical Informatics Team:** A team of PharmD and MD-credentialed individuals responsible for content curation, rule authoring, and clinical validation of the MCI-KB.
- **AI/ML Engineering Team:** Responsible for the development, retraining, and technical validation of the ML-based interaction prediction model.
- **Platform Engineering Team:** Responsible for the secure, scalable, and HIPAA-compliant infrastructure of the SaaS platform (AWS environments).
- **Deployment Engineering Team:** Executes the blue/green deployment to production environments, following the CI/CD playbook.
- **Clinical End-User (Provider):** A licensed healthcare professional (MD, DO, PharmD, NP, PA) authorized to prescribe medications and who has the final legal and clinical authority to accept or override the DICS alert.

---

## 4. Policy Statements

1.  **Safety First:** Meridian Health Technologies is committed to patient safety as its paramount priority. The DICS shall be designed, deployed, and maintained to maximize the detection of clinically significant drug interactions while minimizing false positives and alert fatigue. The system shall err on the side of safety for interactions classified as `CRITICAL` and `MAJOR`.
2.  **Human-in-the-Loop (HITL):** The DICS is a Clinical Decision Support (CDS) tool. It does not replace the clinical judgment of a qualified healthcare provider. The system’s output is an alert notification, not a clinical order. The authority and responsibility for all prescribing decisions rests solely with the attending clinician. This principle is fundamental to compliance with **EU AI Act Article 14 (Human Oversight)** .
3.  **Transparency and Explainability:** For every alert fired, the system shall generate an Explanatory Statement. This statement shall be clear, concise, and provide sufficient clinical context for the provider to make an informed decision, in compliance with **EU AI Act Article 13 (Transparency and provision of information to deployers)** .
4.  **Data Minimization and Privacy:** The DICS shall process only the minimum necessary PHI required to execute the interaction check. All PHI at rest and in transit shall be encrypted according to Meridian’s Data Classification and Protection Policy (SOP-SEC-005), meeting the standards of the **HIPAA Security Rule (45 CFR Part 164, Subpart C)** .
5.  **Structured Override Documentation:** Every override of a `CRITICAL` or `MAJOR` alert shall be accompanied by a mandatory, structured clinical justification. This creates a continuous Pharmacovigilance (PhV) feedback loop. An override without a documented rationale is a non-conformity.
6.  **Bias Mitigation:** The ML-based interaction prediction model shall be evaluated not just for overall accuracy but for performance across demographic subgroups (age, sex, race) to identify and mitigate potential bias, supporting compliance with the **EU AI Act Article 10 (Data and data governance)** .
7.  **Continuous Quality Improvement:** The Clinical Informatics Team shall use aggregated and anonymized override data, alert statistics, and real-world evidence to continuously tune the alert logic and MCI-KB to improve clinical utility and reduce alert fatigue.

---

## 5. Detailed Procedures

This section details the operational procedures for the DICS lifecycle.

### 5.1 MCI-KB Update and Curation Procedure

The MCI-KB is updated on a scheduled basis and through an emergency process.

**A. Scheduled Monthly Update Cycle**
- **Week 1 (Curation):** The Clinical Informatics Team, led by a PharmD, ingests new evidence from the following authoritative sources:
    - Primary Literature: PubMed alerts for key drug-interaction journals (e.g., *Drug Safety*, *Clinical Pharmacology & Therapeutics*).
    - Regulatory: FDA Drug Safety Communications, EMA PRAC recommendations.
    - Compendia: Micromedex, Lexicomp, DailyMed updates.
    - Proprietary Sources: Licensed clinical content vendors.
    - Meridian Pharmacovigilance (PhV) Data: Analysis of aggregate override trends (see Section 5.6).
- **Week 2 (Evidence Grading):** Each proposed interaction entry or modification is graded using a standardized taxonomy:
    - **Evidence Level A:** Meta-analyses, Randomized Controlled Trials (RCTs) powered for the interaction endpoint.
    - **Evidence Level B:** Well-designed cohort or case-control studies.
    - **Evidence Level C:** Case series, significant pharmacovigilance signal (FDA AERS/FAERS, EMA EudraVigilance), or mechanistic plausibility confirmed by a clinical consensus panel.
    - **Evidence Level D:** Theoretical interaction based on *in vitro* data or known metabolic pathways (CYP450, P-gp) without clinical confirmation. These are typically classified as `MINOR` or `MODERATE`.
- **Week 3 (Staging):** The updated Knowledge Base (vX.Y.n) is staged in the `nonprod-dics` environment.
- **Week 4 (Validation & Go-Live):** A scripted clinical validation suite is executed against the staged KB. Upon approval by the Clinical AI Product Council, the new KB is scheduled for production deployment via the standard CD pipeline.

**B. Emergency (Breakthrough) Update Cycle**
- **Trigger:** A new "Black Box" warning, FDA/EMA safety communication mandating immediate action, or a high-signal internal PhV alert.
- **Procedure:**
    1.  The on-call Clinical Informatics Lead creates a `CRITICAL` Jira ticket (`DICS-EMERG-####`).
    2.  The new interaction data is manually curated and peer-reviewed by a second clinical team member within **4 hours**. The review must document the source, clinical rationale, and suggested severity.
    3.  The update is prepared as a configuration-only "hotfix" to bypass the standard code release pipeline.
    4.  The Chief Medical Officer (or designated backup) must approve the emergency entry via an emergency Change Advisory Board (e-CAB) ticket in ServiceNow. Approval threshold: Unanimous.
    5.  Deployment is executed immediately upon approval. Post-deployment testing begins within **1 hour** of the first successful check. An Incident Post-Mortem is created within 5 business days. This emergency process aligns with the Pharmacovigilance Agreement obligations in **SOP-REG-008**.

### 5.2 Alert Logic and Inference Engine Operation

The Alert Logic is a composite system:
1.  **Deterministic Rules Engine:** A first-pass filter based on the explicit relational data in the MCI-KB (e.g., `DRUG_A + DRUG_B = CONTRAINDICATED`). If a deterministic `CRITICAL` rule fires, the process stops immediately and generates an alert.
2.  **Machine Learning (ML) Inference Model:** Where no deterministic rule exists or for combinations of 3+ substances, the patient's context vectors (medications, allergies, labs, demographics) are passed to a Gradient-Boosted Tree ensemble. This model outputs a Predicted Interaction Severity Score (`P_ISS`) and a Confidence Score.
    - `P_ISS >= 0.90` → `CRITICAL` candidate
    - `P_ISS >= 0.70 and < 0.90` → `MAJOR` candidate
    - `P_ISS >= 0.40 and < 0.70` → `MODERATE` candidate
    - `P_ISS < 0.40` → `MINOR` or no alert based on configuration.

**Algorithmic Fairness Check:** During the ML candidate classification in the EU environment only, a "Fairness Gate" wrapper is applied. The model's P_ISS is re-evaluated against protected demographic proxies (age, sex). If the standard deviation of P_ISS for any group exceeds a threshold of 0.15 for `MAJOR` or `CRITICAL` candidates, the alert is automatically downgraded to `MODERATE` and flagged for manual audit. This procedure is a direct control for the bias mitigation requirements of **EU AI Act Article 10(2)(f)** .

### 5.3 Alert Firing and User Interface Procedure

Once a Severity Level is determined, the alert is fired to the user interface.

| Severity Level | Visual Indicator | Workflow Action | Override Documentation Required |
| :--- | :--- | :--- | :--- |
| **CRITICAL** | Red modal, full-screen interruption. Audible alarm (if configured). | "**Cancel Order**" (default) or "**Override & Document**". | **Mandatory, Structured.** Free-text rationale AND selection from a structured, clinical pre-text list (e.g., "Specialist consultant confirmed benefit outweighs risk"). |
| **MAJOR** | Yellow pop-up panel, workflow suspension. | "**Cancel Order**", "**Modify Order**", or "**Override & Acknowledge**". | **Mandatory.** Free-text rationale OR selection from structured list. |
| **MODERATE** | Amber contextual banner, no workflow suspension. | "**Acknowledge**" (alert dismissed, order proceeds) or "**Modify Order**". | **Optional.** Acknowledge action is logged, but a clinical rationale is not forced. |
| **MINOR** | Informational text only, displayed within the order entry screen. | No action required. | None. |

The alert pop-up must contain:
1.  A clear, non-technical "Plain Language Summary" of the interaction (e.g., "Taking Drug X with Drug Y can significantly increase the risk of sudden cardiac arrest.") → **(EU AI Act Art. 13 compliance)** .
2.  The Severity Level classification.
3.  The Explanatory Statement (mandatory for CRITICAL/MAJOR).
4.  The `Source(s)` of evidence.
5.  A direct link to a detailed "Clinical Insight Card" for more information.

### 5.4 Override Documentation and Pharmacovigilance (PhV) Procedure

This procedure is the Human-in-the-Loop control mechanism mandated by **EU AI Act Article 14(3)** and is critical to the continuous safety monitoring required by our QMS.

1.  **Override Initiation:** Clinician initiates an override on a `CRITICAL` or `MAJOR` alert.
2.  **Structured Data Capture (`dics_override_log`):** The following data is immutably logged with an auditable hash chain in a segregated, high-security audit log:
    - `override_id`: (UUID v4)
    - `alert_id`: The unique ID of the fired alert.
    - `timestamp`: ISO 8601 format in UTC.
    - `user_id`: EHR/Meridian-verified user ID (NPI number where available).
    - `user_role`: MD, PharmD, etc.
    - `patient_case_id`: De-identified hash of the patient case.
    - `severity_level`: The level of the alert being overridden.
    - `rationale_structured`: The selected structured reason (if chosen from list).
    - `rationale_free_text`: The clinician's typed rationale (minimum 10 characters for CRITICAL overrides).
3.  **Real-Time Safety Monitoring:** A separate rules engine monitors the `dics_override_log` stream in real-time. An automated "High-Stakes Override" notification is sent to the hospital’s Chief Medical Informatics Officer (CMIO) and Meridian’s on-call Safety Officer if **any** of the following conditions are met:
    - **Override of a `CRITICAL` alert.**
    - Three or more `MAJOR` overrides within a single order session.
    - Override free-text rationale contains keywords from a curated "Pharmacovigilance Watch List" (e.g., "I disagree with this interaction," "this combination is safe," "no risk").

### 5.5 Model Retraining and Validation Gate Procedure

This procedure ensures the ML component remains current and robust.

1.  **Retraining Cadence:** The ML model is scheduled for full retraining on a **quarterly basis**.
2.  **Expanded Dataset:**
    - **Ground Truth:** Updated MCI-KB with new and modified entries manually validated by clinical informaticists.
    - **Adverse Safety Data:** Anonymized, aggregated override data where a `CRITICAL` or `MAJOR` override was followed by an ADE report within 7 days is designated as a "Hard Negative" and given high weight during retraining.
3.  **Validation Gate:**
    - **Data Split:** Dataset is split chronologically: 70% (Training), 15% (Validation-Tuning), 15% (Holdout Test).
    - **Primary Metric (Safety Recall):** Recall for `CRITICAL` and `MAJOR` interactions must be ** >= 0.99** on the Holdout Test set. A value below this threshold **halts the release**.
    - **Secondary Metric (Alert Fatigue Precision):** Precision for `MODERATE` and `MINOR` alerts must demonstrate a positive trend or remain above **0.85**. This ensures we are reducing noise.
    - **Fairness Metric:** The 95% Confidence Interval of the Safety Recall metric must overlap across subgroups of sex and age category. A statistically significant difference automatically halts the release and triggers a Bias Review.
4.  **A/B Deployment Strategy:**
    - A "Shadow" instance of the new Candidate Model is deployed in the production environment.
    - The Shadow Model receives 100% of live traffic but its alerts are recorded to the audit log only, not shown to the user.
    - For a **1-week** bake period, the clinical performance of the Candidate Model is compared against the Champion Model by the Medical Informatics team. The primary comparison metric is Clinical Utility (Alert Rate x Positive Predictive Value).
5.  **Promotion:** Upon successful completion of the bake period and approval by the VP of Clinical AI Products, the Candidate Model is promoted to Champion via a feature-flag activation.

### 5.6 Alert Tuning Procedure (Mitigating Alert Fatigue)

A continuous process overseen by the Clinical AI Product Council.

1.  **Data Aggregation:** Weekly, the analytics pipeline (AWS QuickSight dashboards) aggregates:
    - Alert Rate per 100 orders per facility/region.
    - Severity distribution of fired alerts.
    - Override rate, stratified by Severity Level and specific Alert Rule ID.
2.  **Tuning Targets:** The Clinical AI Product Council reviews the data monthly and sets quantitative targets for the next quarter. The default targets are:
    - Overall Override Rate for `MODERATE` alerts: `> 70%` (indicating the need to demote to MINOR or switch to informational display).
    - Overall Override Rate for `MAJOR` alerts: `> 30%` (triggers a human review of the rule's language and clinical context).
    - Override Rate for a single `CRITICAL` rule: `> 5%` (triggers an immediate clinical safety review).
3.  **Tuning Actions:**
    - **Demotion:** Moving a noisy rule to a lower severity.
    - **Contextualization:** Adding logic to suppress an alert if specific patient-context conditions are met (e.g., "Do not fire interaction alert between Warfarin and Statin if INR is monitored Q 4 weeks and is within therapeutic range").
    - **Reframing:** Rewriting the language of the alert to better guide action.
    - **Deprecation:** Removing a clinically obsolete rule from the MCI-KB.

### 5.7 EU Environment-Specific Data Sovereignty Procedure

To comply with EU data protection laws and the EU AI Act, the following controls are enforced for the EU SaaS environment (`eu-west-1`):

1.  **Data Residency:** All PHI and the dics_override_log data remain within the EU AWS region. No raw patient data is transferred outside this boundary.
2.  **Pseudonymized Model Retraining:** European data is not used in the global ML model retraining. Instead, a **Federated Learning** approach is used. A local "Worker Model" is trained on the aggregated, pseudonymized EU dataset. The global "Master Model’s" architecture and parameters are adjusted by ingesting only the anonymized *gradients* from the Worker Model, never the raw or pseudonymized data itself. This is orchestrated through a secure aggregator service.
3.  **Conformity Assessment:** The EU Authorized Representative (as defined in SOP-REG-025) maintains on file the EU Declaration of Conformity for the DICS as a standalone High-Risk AI System, meeting the requirements of **EU AI Act Art. 16 and Annex V**.

---

## 6. Controls and Safeguards

| Control ID | Category | Domain | Control Detail | Regulation Mapping |
| :--- | :--- | :--- | :--- | :--- |
| **DICS-C1** | Administrative | QMS/CAPA | Every override of a `CRITICAL` alert is automatically logged as a "Use Error" event in the Meridian QMS system (ETQ Reliance). The Clinical Safety Officer (CSO) reviews all events weekly and may initiate a Corrective and Preventive Action (CAPA) if a trend is identified. | EU AI Act Art. 72 |
| **DICS-C2** | Technical | Accuracy/Robustness | The "Safety Recall" metric (as defined in 5.5) is implemented as a hard block in the CI/CD pipeline (Jenkins). A failed test returns a non-zero exit code, preventing the building of the new model artifact. | EU AI Act Art. 8, 9 |
| **DICS-C3** | Technical | Record Keeping | The `dics_override_log` is stored in an immutable, encrypted, and write-once-read-many (WORM) compliant audit log using AWS QLDB. Log entries are cryptographically chained, ensuring no record can be deleted or altered retroactively. This log is part of the legally-mandated audit trail. | EU AI Act Art. 12; HIPAA 164.312(b) |
| **DICS-C4** | Administrative | Human Oversight | The structured, mandatory nature of the `CRITICAL` and `MAJOR` override documentation ensures a record of human oversight, confirming the deployer (clinician) understands the AI’s output and has the capability to disregard it. | EU AI Act Art. 14(3) & 14(4)(a) |
| **DICS-C5** | Administrative | Data Governance | "Data Access by Design" principle applied. A Data Use Agreement (DUA) with each customer explicitly prohibits the re-identification of any de-identified patient data used for model training and validation. | EU AI Act Art. 10(5) |
| **DICS-C6** | Technical | HIPAA Security | All DICS service-to-service communication (e.g., DICS engine to EHR FHIR APIs) is authenticated via mutual TLS (mTLS) and encrypted using AES-256-GCM. All audit logs are encrypted at rest using AWS KMS keys with annual key rotation. | HIPAA 164.312(a)(1) & (e)(2) |
| **DICS-C7** | Technical | HIPAA Privacy | The DICS implements "Strict Opt-In Access Control." A clinician can be denied access to DICS functionality for a specific patient case via a "Break-the-Glass" feature, and a full audit trail of this access control override is captured. | HIPAA 164.312(a)(1) |
| **DICS-C8** | Administrative | Security | Quarterly access reviews are conducted by the IAM team. The Clinical AI VP signs off on all permissions assigned to roles that can alter `CRITICAL` or `MAJOR` alert logic or configuration (e.g., "prod-dics-admin-role"). | HIPAA 164.308(a)(3)(i) |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| Metric (KPI) | Calculation | Target | Owner |
| :--- | :--- | :--- | :--- |
| **DICS System Uptime** | `(Total Minutes in Period - Unplanned Downtime Minutes) / Total Minutes` | `≥ 99.95%` | Platform Engineering Team |
| **Alert Logic Execution Time (p95)** | `p95(engine_response_ms)` | `< 200ms` | AI/ML Engineering Team |
| **Safety Recall Rate (CRITICAL/MAJOR)** | `True_Positives / (True_Positives + False_Negatives)` on Holdout Set | `≥ 99.5%` | AI/ML Engineering Team |
| **Critical Alert Override Rate** | `(Number of Overridden CRITICAL Alerts / Total Fired CRITICAL Alerts) * 100` | `< 2%` (Monitor for change) | VP Clinical AI |
| **Mandatory Documentation Compliance** | `(Number of CRITICAL/MAJOR Overrides with complete documentation / Total CRITICAL/MAJOR Overrides) * 100` | `= 100%` (Zero is critical) | Compliance Officer |
| **Alert Fatigue Index (AFI)** | `(Override Rate for ALL alerts) * (Avg. Alerts per 100 Orders)` | Quarterly target set by Council | Clinical Informatics Team |

### 7.2 Dashboards and Reporting Cadence

- **Real-Time Operations Dashboard:** (Datadog) Displays system health, latency, error rates, and alert volume. Monitored 24/7 by the NOC.
- **Clinical Performance Weekly Report:** (AWS QuickSight) Auto-generated every Monday for the VP of Clinical AI Products. Focuses on alert and override rates by alert ID, severity, and customer.
- **Monthly Quality and Safety Report:** (Manual) Prepared by the Clinical Informatics Team and presented to the Clinical AI Product Council. Includes deep-dive analyses on top overridden rules, fairness metric trends, and a summary of all CAPAs initiated. This report is a core input to the Post-Market Surveillance (PMS) process (**EU AI Act Art. 61**).
- **Quarterly Management Review:** (Slide Deck) A summary for executive leadership and the Board, covering major risks, major releases, and regulatory compliance posture. The CEO is accountable for reviewing and acting on these findings.

---

## 8. Exception Handling and Escalation

### 8.1 Standard Exception Process

Any deviation from the procedures defined in this SOP must follow the formal exception management process. Exceptions include, but are not limited to: skipping a validation gate, using unapproved data for retraining, or deploying an MCI-KB update without full review.

1.  An Exception Request must be submitted via the ServiceNow "Policy Exception" form. The request must define the scope, technical and clinical justification, risk assessment, and a proposed compensatory control.
2.  **Approval Matrix:**
    - **Risk Level 1 (Minor deviation, e.g., documentation format error):** Approval from the Clinical AI VP (Dr. Okafor).
    - **Risk Level 2 (Moderate deviation, e.g., using a smaller testing dataset for a minor rule update):** Approval from Clinical AI VP and Compliance Officer.
    - **Risk Level 3 (Major deviation, e.g., skipping a fairness validation gate):** Approval from Chief Medical Officer (Dr. Patel), Chief AI Officer, and Chief Compliance Officer. This level requires an entry in the Risk Register (see SOP-GOV-003).
3.  All exceptions are time-bound with a mandatory expiration date (max 90 days). A permanent change to this SOP must be initiated via the document change control process before the exception expires.

### 8.2 Clinical Safety Escalation Pathway

If an end-user (provider) has a good-faith belief that the DICS system is producing unsafe, inaccurate, or misleading alerts that could lead to patient harm, the following immediate escalation pathway is activated:

1.  **Step 1: Immediate Circumvention.** The clinician is empowered and instructed to use their professional judgment to bypass the DICS for that specific order and manage the patient independently. The system's output is a warning, not a clinical order.
2.  **Step 2: Report Incident.** The clinician must report the incident immediately via the designated hospital IT/Safety hotline, which is directly connected to Meridian’s P1 Incident Management System (PagerDuty).
3.  **Step 3: Meridian Triaging.** The Meridian NOC receives the P1 ticket. The on-call engineer identifies the specific alert rule or model logic. The on-call Clinical Informatics Lead is paged within **15 minutes**.
4.  **Step 4: Immediate Containment.** If the Clinical Informatics Lead and on-call engineer agree there is a plausible safety risk, they have the authority to temporarily disable (kill-switch) the specific alert rule or, in an extreme case, switch the system to a "safety mode" where only deterministic `CRITICAL` alerts are shown. This kill-switch is logged immutably.
5.  **Step 5: Review and Remediation.** A full review by the Clinical AI Product Council is held within one business day. The Chief Medical Officer (Dr. Patel) is the final decider on restoring the disabled rule and is accountable for the safety sign-off.

---

## 9. Training Requirements

| Role | Training Module | Frequency | Delivery Method | Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **Clinical End-User (Provider)** | `DICS-101`: Clinical Application and Override Governance | Annually, and upon any major UX change to the alerting interface. | On-demand e-learning module via customer's LMS, integrated into Meridian Clinical Academy. | Completion certificate logged to Meridian's training system (Docebo) via API. |
| **Clinical Informatics Team** | `DICS-201`: Advanced MCI-KB Curation, Rule Authoring, and PhV | Initially at hire, then annually. | 3-day in-person workshop at Meridian HQ. | Pass/Fail practical exam on a staging system. Recorded in Workday HRMS. |
| **Customer Support (L1/L2)** | `DICS-100`: DICS Fundamentals, Common Issues, and Escalation Path | Initially, then semi-annually. | On-demand video + knowledge base article review. | Quarterly quiz in Docebo; support ticket quality audit. |
| **Compliance & Legal Staff** | `DICS-REG-301`: EU AI Act & HIPAA Regulatory Deep Dive for DICS | Annually, with updates when regulations change. | Instructor-led session by external counsel. | Attendance recorded in Workday. |

Training is tracked and enforced by the Learning & Development department. An employee is not granted access to the DICS production systems until their compliance training is 100% complete. Non-compliance with training triggers an automatic de-provisioning of access by the IAM system.

---

## 10. Related Policies and References

- **SOP-GOV-003:** Enterprise AI Governance Policy
- **SOP-CLIN-010:** Clinical AI Lifecycle Management
- **SOP-REG-008:** Pharmacovigilance and Post-Market Surveillance Procedure
- **SOP-REG-025:** EU Authorized Representative and Conformity Assessment Procedure
- **SOP-QMS-001:** AI Quality Management Framework (ISO 13485 aligned)
- **SOP-SEC-005:** Data Classification and Protection Policy (HIPAA Security Rule)
- **SOP-FED-001:** Federated Machine Learning Data Standards
- **External Standard:** Regulation (EU) 2024/1689 (Artificial Intelligence Act), Articles 8-14, 16, 61, 72, Annex III, Annex IV, Annex V
- **External Standard:** Health Insurance Portability and Accountability Act (HIPAA) of 1996, 45 CFR Parts 160, 162, and 164
- **External Standard:** ISO 14971: Application of risk management to medical devices
- **External Standard:** ISO 13485: Medical devices - Quality management systems

---

## 11. Revision History

| Version | Date | Author | Approver | Summary of Changes |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 2022-11-15 | J. Smith (former VP) | Dr. P. Patel | Initial version. Focused on US market and deterministic rules. |
| 2.0 | 2024-03-01 | K. Jones (CIS) | Dr. P. Patel | Major revision. Introduced ML inference engine, revised alert severity levels, added formal model validation and shadow deployment procedures. |
| 2.1 | 2024-06-10 | M. Davis (Compliance) | Dr. P. Patel | Minor revision. Added preliminary EU AI Act references and expanded the override documentation data schema for future PhV needs. |
| 3.0 | 2025-05-20 | Dr. A. Okafor | Dr. P. Patel | Major revision. Full integration of EU AI Act compliance controls for High-Risk AI systems, including HITL governance, fairness metrics, conformity assessment, and mandatory QMS linkage. Expanded roles to include the Clinical AI Product Council. Restructured document completely. |
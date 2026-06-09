---
sop_id: "SOP-CLIN-013"
title: "Patient Safety Monitoring"
business_unit: "Clinical AI Products"
version: "1.8"
effective_date: "2025-06-08"
last_reviewed: "2026-12-16"
next_review: "2027-06-15"
owner: "Dr. Aisha Okafor, VP of Clinical AI Products"
approver: "Dr. Priya Patel, Chief Medical Officer"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Patient Safety Monitoring

## SOP-CLIN-013

**Version:** 1.8
**Effective Date:** 2025-06-08
**Owner:** Dr. Aisha Okafor, VP of Clinical AI Products
**Approver:** Dr. Priya Patel, Chief Medical Officer

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, governance, operational procedures, and technical controls for the continuous monitoring of patient safety across all Clinical AI Platform products deployed by Meridian Health Technologies, Inc. This document serves as a core component of Meridian's risk management system as required under the EU AI Act for high-risk AI systems and aligns with the organization's adoption of the NIST AI Risk Management Framework. The primary objectives of this SOP are to:

1.  Define the systematic detection, triage, investigation, and resolution of potential and actual patient safety signals originating from Clinical AI systems.
2.  Establish the Patient Safety Review Board (PSRB) as the authoritative governance body for AI-related safety events.
3.  Detail the real-time technical monitoring infrastructure, including dashboards, automated alerts, and logging requirements.
4.  Codify mandatory incident escalation pathways with specific service level agreements (SLAs) based on severity classification.
5.  Ensure compliance with the transparency, human oversight, and post-market monitoring obligations detailed in Articles 61 and 72 of the EU AI Act for high-risk AI systems.

### 1.2 Scope

This SOP applies globally to all Meridian Health Technologies employees, contractors, subsidiaries, and business units involved in the design, development, deployment, monitoring, and maintenance of the following product lines, classified as high-risk AI systems under Annex III of the EU AI Act:

- **Clinical AI Platform:** AI-driven clinical decision support (CDS) tools, diagnostic imaging analysis modules (including FDA 510(k)-cleared and CE-marked algorithms), patient risk scoring models, and adverse event prediction systems deployed in over 340 hospitals and clinics.
- **MedInsight Analytics:** Components of the platform that generate prospective care gap alerts or outcomes predictions that are surfaced directly to clinical users.
- **HealthPay Financial Services:** Models subject to SR 11-7 where adverse model behavior could indirectly impact patient care through denial or delay of financing for critical procedures (monitored under SOP-FIN-042, with safety signals escalated to this SOP).

**Out of Scope:** This SOP does not cover cybersecurity incident response (see SOP-SEC-007), general IT infrastructure monitoring (see SOP-IT-015), or financial model risk management (see SOP-FIN-042), except where such incidents trigger a patient safety event as defined herein.

### 1.3 Applicability

All personnel with responsibilities defined in Section 3 must comply with this SOP. Adherence is mandatory and subject to audit by the Internal Audit team and the Chief Compliance Officer.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **AE** | Adverse Event: An actual event where the use of a Clinical AI product is reasonably suspected to have contributed to patient harm, including delayed diagnosis, incorrect treatment recommendation, or psychological distress. |
| **AI Safety Signal** | Any data point, pattern, or alert that suggests a potential or actual degradation in the safety performance of an AI model, including but not limited to concept drift, data drift, model output anomalies, and reports from clinical users. |
| **CDS** | Clinical Decision Support: AI-driven tools providing diagnostic or therapeutic suggestions. |
| **CISO** | Chief Information Security Officer |
| **CMO** | Chief Medical Officer |
| **DQA** | Data Quality Audit |
| **DR** | Disaster Recovery |
| **EU AI Act** | Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence. |
| **FPIR** | Formal Patient Incident Report |
| **GDPR** | General Data Protection Regulation (Regulation (EU) 2016/679) |
| **HIPAA** | Health Insurance Portability and Accountability Act of 1996 |
| **KPI** | Key Performance Indicator |
| **MLOps** | Machine Learning Operations |
| **NIST AI RMF** | National Institute of Standards and Technology AI Risk Management Framework 1.0 |
| **PHI** | Protected Health Information |
| **PSRB** | Patient Safety Review Board |
| **QMS** | Quality Management System |
| **RCA** | Root Cause Analysis |
| **SaaS** | Software as a Service |
| **SAE** | Serious Adverse Event: A patient safety event resulting in death, life-threatening illness, prolonged hospitalization, or permanent impairment, where the AI system is a suspected contributory cause. |
| **SLA** | Service Level Agreement |
| **SME** | Subject Matter Expert |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix (RACI)

The following matrix delineates roles for the key operational threads of this SOP. A role assignment signifies ultimate accountability for the function.

| Activity/Task | Chief AI Officer (Dr. Marcus Rivera) | Chief Medical Officer (Dr. Priya Patel) | VP, Clinical AI Products (Dr. Aisha Okafor) | Patient Safety Review Board (PSRB) | MLOps Lead | Clinical Safety Lead | Customer Success Manager |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Policy Governance & Resourcing** | A | C | R | I | I | C | I |
| **Continuous Monitoring Architecture** | A | I | R | C | R | C | I |
| **Dashboard & Alert Configuration** | I | I | A | C | R | R | I |
| **Initial Signal Triage (Level 1-2)** | I | I | I | I | C | A/R | I |
| **PSRB Convening & Facilitation** | I | A | R | - | I | R | I |
| **SAE Investigation & RCA** | C | A | I | R | C | R | I |
| **External Regulatory Reporting** | C | A/R | R | C | I | I | I |
| **Customer-Facing Communication** | I | C | A | I | I | I | R |

**Key:** R = Responsible (executes), A = Accountable (approver), C = Consulted, I = Informed.

### 3.2 Named Roles and Responsibilities

- **Dr. Priya Patel, Chief Medical Officer (CMO):** Serves as the ultimate accountable executive for all patient safety matters. Approves all severity classifications for SAEs. Serves as the Chair of the Patient Safety Review Board (PSRB). Authorizes external notifications to competent authorities under Article 73 of the EU AI Act.
- **Dr. Aisha Okafor, VP of Clinical AI Products:** Acts as the Process Owner for this SOP. Responsible for maintaining the SOP, overseeing the operational execution of safety monitoring, and directing resources for all signal investigations. Acts as the primary liaison between the PSRB and the Product Management team for remediation prioritization.
- **Clinical Safety Lead:** A dedicated role within the Clinical AI Quality team. Performs Level 2 triage on all incoming safety signals. Manages the PSRB agenda and evidence pack. Maintains the central safety signal log in the QMS.
- **MLOps Lead:** Responsible for the technical implementation of monitoring scripts, data drift detection algorithms, and dashboard availability. Ensures all model inference logs are shipped to the central security information and event management (SIEM) and data lake for analysis.
- **Privacy Officer:** Consulted on any safety event involving a data breach or potential unauthorized disclosure of PHI. Ensures Data Protection Impact Assessments (DPIAs) are updated following an investigation that reveals systemic data governance issues.
- **Customer Success Managers (CSMs):** Serve as the initial verbal intake point for clinical customer complaints. Responsible for creating an initial ticket within 15 minutes of a verbal report. Escalate any written complaint received from a Chief Medical Informatics Officer (CMIO) or equivalent title directly to the Clinical Safety Lead and VP of Clinical AI Products immediately.

---

## 4. Policy Statements

### 4.1 Commitment to a Safety-First Culture
Meridian Health Technologies is unequivocally committed to a safety-first operating model. No commercial metric, including renewal rate or annual recurring revenue (ARR), shall take precedence over the timely investigation and containment of a confirmed patient safety signal. Retaliation against any Personnel who reports a safety concern in good faith is strictly prohibited.

### 4.2 Proactive Safety Monitoring
Meridian does not rely solely on customer-reported events. All Clinical AI models in production shall be subject to a continuous, automated monitoring regime. The technical infrastructure shall track input data statistical properties, output distribution, inference latency, and silent model failure modes using a comprehensive suite of drift detection algorithms. This proactive surveillance is the cornerstone of our compliance with Article 72 of the EU AI Act.

### 4.3 Transparency and Reporting
Meridian shall operate transparently with its clinical customers. Any confirmed SAE, or any AI Safety Signal with a Severity Level of 1 or 2 (see Section 8), shall be communicated to the affected customer's designated point of contact within the SLA timelines defined in Section 8. Meridian shall also maintain a publicly available summary of serious incidents filed with competent authorities, as required by Article 71.

### 4.4 Mandatory Incident Escalation and Logging
All Personnel are required to log any complaint, technical alert, or clinical observation that could constitute an AI Safety Signal immediately upon discovery. No triage shall occur prior to logging. The QMS shall serve as the single, immutable system of record for all safety signals, investigations, and resulting design changes, ensuring an unbroken chain of custody and evidence traceability.

---

## 5. Detailed Procedures

### 5.1 Phase 1: Signal Intake and Logging
This phase captures the initial moment a potential safety signal enters the Meridian operational ecosystem.

1.  **Source Identification:** Signals may originate from one of four primary sources:
    - **Customer Verbal/Written Report:** Received by a CSM, Support Engineer, or any other Personnel.
    - **Automated Technical Alert:** Triggered by Datadog monitors, the MLOps platform (e.g., Evidently AI), or anomaly detection scripts. These alerts are routed to the `#cls-ai-patient-safety-alerts` Slack channel and a PagerDuty escalation.
    - **Proactive Data Drift Detection:** Weekly statistical analysis of inference logs against baseline data distributions, as described in Section 7.
    - **Social Media/Publication Scan:** The Corporate Communications team monitors public forums and medical literature for reports of harm related to Meridian products.
2.  **Immediate Triage Ticket Creation (15-Minute SLA):** The individual who first receives or discovers the signal MUST immediately create a ticket in the QMS (Jira Service Management). The ticket type MUST be `"Patient Safety Signal"`. The ticket must, at a minimum, capture:
    - Signal Source (Customer, Auto-Alert, etc.)
    - Date/Time of Discovery
    - A concise, factual description of the signal (no speculation).
    - Any immediate artifacts (e.g., screenshot of a faulty recommendation, Datadog alert ID, customer email subject line).
3.  **Signal Log Entry:** The automated Jira workflow populates the **PSRB Central Safety Signal Log (CSSL)**, assigning a unique identifier `SAF-YYYY-XXXX`.

### 5.2 Phase 2: Initial Triage and Confirmation (Level 1 & 2)
This phase filters non-material technical noise from genuine patient safety signals requiring investigation.

1.  **Level 1 Triage (Performed by MLOps On-Call Engineer - 1 Hour SLA):**
    - Validate the technical alert. Rule out false positives resulting from deployment artifacts, known maintenance windows, or non-safety related latency spikes.
    - If the alert is technical and false, annotate the ticket `"False Alarm - Technical"`, document the root cause of the false positive (e.g., misconfigured monitor threshold), and close the ticket.
    - If the alert **cannot** be immediately dismissed, or if the source was a customer report, immediately escalate to Level 2 Triage by pinging the Clinical Safety Lead.
2.  **Level 2 Triage (Performed by Clinical Safety Lead - 2 Hour SLA from Level 1 Escalation):**
    - Review the signal against the current model risk profiles established in the pre-deployment risk assessments.
    - Conduct an initial clinical plausibility assessment. For example, if the alert is for a patient deterioration model showing a spike in risk scores for a single hospital, determine if it correlates with a real-world event (e.g., a mass casualty incident in the hospital's catchment area) versus plausible model drift.
    - Make a preliminary Severity Classification (S0-S4, as defined in Section 8.1).
    - **Decision:** "Close - Not a Clinical Signal" or "Escalate to PSRB Event."
    - Document the rationale and decision in the QMS ticket.

### 5.3 Phase 3: PSRB Activation and Investigation
This phase constitutes the formal investigation governed by the Patient Safety Review Board.

1.  **Activation Criteria:** The Clinical Safety Lead must activate the PSRB for all signals classified as Potential Severity S0, S1, or S2, or any signal where clinical harm cannot be immediately ruled out.
2.  **PSRB Notice:** Within 4 hours of the Level 2 decision to escalate, the Clinical Safety Lead issues a PSRB convening notice via email and Slack to the standing members (CMO, VP of Clinical AI, Chief Architect, Privacy Officer, Legal Counsel). The notice includes the `SAF-ID` and the initial severity classification.
3.  **Evidence Pack Assembly:** The MLOps Lead and Clinical Safety Lead jointly assemble the PSRB Evidence Pack, which includes:
    - The initial QMS ticket.
    - All relevant inference input payloads, model outputs, and user session logs from the affected time window.
    - A 72-hour input data quality report showing data completeness and statistical distributions.
    - The current model card and approved risk profile.
    - Relevant clinical context (e.g., patient cohort characteristics).
4.  **PSRB Meeting (Convened within 24 Hours for S0/S1; 5 Business Days for S2):**
    - **Chair:** Dr. Priya Patel (CMO). In her absence, Dr. Marcus Rivera (Chief AI Officer).
    - **Quorum:** A voting quorum consists of the CMO (or designee), VP of Clinical AI Products, and one member from Legal or Compliance.
    - **Agenda:** (1) Review of the Signal; (2) Review of the Evidence Pack; (3) Root Cause Analysis (RCA) hypothesis generation; (4) Decision on Final Severity Classification; (5) Immediate containment actions.
    - **Decision Log:** All decisions, dissenting opinions, and assigned action items are documented in the QMS ticket. An action is a committed deliverable with a named owner and a due date.

### 5.4 Phase 4: Root Cause Analysis and Remediation
Following the PSRB meeting, a formal RCA is conducted.

1.  **RCA Team:** Formed by the VP of Clinical AI Products. Includes MLOps Lead, Model Developers, Clinical SMEs, and a Quality Assurance representative.
2.  **Methodology:** The team shall use the "5 Whys" methodology and a Fishbone (Ishikawa) Diagram to trace the root cause. Potential causal categories include:
    - **Model Defect:** Algorithmic bias, model staleness, fragility to outlier inputs.
    - **Data Defect:** Training-data pollution, input-data schema mismatch, upstream ETL failure, data drift.
    - **Infrastructure Defect:** Latency timeout causing fallback to a less accurate model, misconfiguration in deployment pipeline, failure of a fallback rule.
    - **Human Factors:** Insufficient user training leading to off-label use ("automation misuse"), alert fatigue leading to overrides.
3.  **Corrective and Preventive Action (CAPA):** The RCA results in a CAPA plan documented in the QMS. The product manager for the affected model is responsible for creating user stories in Jira Product Board to implement the CAPA. Security fixes follow SOP-SEC-007.

### 6.5 Post-Market Monitoring Compliance (EU AI Act, Article 72)
This procedure fulfills Meridian's Article 72 obligations for a post-market monitoring system proportionate to the risks.
1.  **Documented Plan:** This SOP serves as the documented Post-Market Monitoring (PMM) plan for each high-risk AI system the Clinical AI Products team deploys.
2.  **Data Collection and Analysis:** The MLOps team shall continuously collect and, at a minimum, weekly analyze the data logs specified in Section 7.2 to detect trends.
3.  **Reporting to Notified Body:** Any SAE (S0) or a statistically significant increase in near-misses (S1) that points to a systemic design flaw shall be immediately reported via the QMS to our notified body (TÜV SÜD) as per their technical documentation submission requirements, which satisfies the Article 72(3) obligation.

### 6.2 Administrative Controls
- **GxP Validation:** All dashboards and automated monitors used for safety signal detection are classified as GxP-adjacent systems and are subject to a change control and validation review with each version update, as overseen by the Quality Assurance team.
- **Segregation of Duties:** No single individual can both perform the initial Level 2 triage and have the sole authority to close a PSRB-eligible case. The PSRB vote serves as the gate for closure.

### 6.3 Human Oversight Controls (EU AI Act, Article 14)
Meridian implements the following human oversight measures, operationalized through this SOP, to prevent or minimize risks to patient safety:
1.  **"Human-in-the-Loop" User Interface Design:** All Clinical AI CDS tools display a confidence score and a mandatory link to the model evidence card. Recommendation output fields are never pre-populated into an electronic health record (EHR) order entry field; the clinician must actively review and select the recommendation.
2.  **Operator Override Monitoring:** A KPI tracked on the Patient Safety Dashboard is the "Model Override Rate" per clinical site. A sudden spike or a sustained decline in override rate for a specific model triggers a Level 1 PSRB review, as it may indicate either alert fatigue or unsafe automation bias by the clinicians, a core concern of Article 14(4)(b).

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Patient Safety Dashboard
The Clinical Safety Lead, in partnership with MLOps and Data Engineering, maintains a real-time Patient Safety Dashboard in Datadog and PowerBI. This dashboard is the "single pane of glass" for operational oversight and is prominently displayed in the Clinical AI Operations Center.

**Dashboard Key Performance Indicators (KPIs):**
| Metric (KPI) | Definition | Target | Escalation Threshold |
| :--- | :--- | :--- | :--- |
| **New Safety Signals Per Week** | Count of new `SAF-YYYY-XXXX` IDs logged. | Informational | > 10% increase week-over-week for two consecutive weeks triggers an alert to the CMO. |
| **Mean Time to Triage (MTTT)** | Time from Signal Intake (Ticket Created) to Level 2 Triage Decision. | < 3 Hours | P95 > 4 hours for a calendar month triggers a CAPA. |
| **Mean Time to Resolution (MTTR)** | Time from PSRB Activation to CAPA Implementation for Severity S1/S2 events. | < 30 Days | Exceeding target triggers a red status for the accountable Product Manager. |
| **Open PSRB Investigations** | Count of investigations in Phase 3 or Phase 4. | - | No aging investigation > 45 Days without CMO-approved exception. |
| **Data Drift Severity Score** | Automated metric quantifying the distance between real-world inference data distribution and the baseline training data distribution, using Population Stability Index (PSI > 0.2). | PSI < 0.15 | PSI > 0.25 auto-generates a `SAF` ticket. |

### 7.2 Proactive Technical Monitoring (Automated Drift Detection)
The MLOps platform runs the following scans on inference payloads stored in the S3 data lake `meridian-clinical-ai-{region}-inferencelog`:

1.  **Data Completeness:** Scans for unexpected `NULL` values in critical input features. Threshold: > 2% `NULL` rate triggers an alert.
2.  **Feature Drift:** Kullback-Leibler divergence calculation for top-30 SHAP features. Threshold: Divergence > 0.3 generates a technical warning.
3.  **Prediction Drift:** Monitors the distribution of model outputs. Threshold: > 5% shift in mean prediction value, or > 10% shift in standard deviation over a 24-hour rolling window, triggers a `SAF` ticket.
4.  **Silent Model Failure:** Detection of a 0.0 confidence score output or a generic "error fallback" recommendation rate exceeding 1% of all inferences for a model version.

### 7.3 Quarterly Safety Summary Report
The Clinical Safety Lead will compile and publish a Quarterly Safety Summary Report covering:
- Summary of all signals received (source, model affected, initial severity).
- Findings and CAPA status for all closed PSRB investigations.
- Aggregate statistical data from the dashboard (MTTT, MTTR, Drift Scores).
- Assessment of model performance at each clinical site, including override rate analysis.

This report is distributed to the CMO, Chief AI Officer, Chief Compliance Officer, and the Board of Directors' Patient Safety Committee.

---

## 8. Exception Handling and Escalation

### 8.1 Severity Classification and Escalation SLAs
All AI Safety Signals are classified according to the following schema. The severity dictates the mandatory escalation timeline and communication protocol.

| Severity | Definition | Example | Triage SLA (Phase 1) | PSRB Convening SLA | External Notification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **S0 - Critical SAE** | Confirmed or strongly suspected AI-contributed event resulting in death or life-threatening deterioration. | An AI diagnostic tool systematically but silently misses an acute stroke finding on imaging, resulting in a discharge and a subsequent fatal outcome for a cohort of patients. | Immediate (within 1 Hour) | Immediately (within 4 Hours) | CMO notifies Competent Authority (FDA, Notified Body, Competent National Authority under Art. 73) within 24 hours of confirmation. |
| **S1 - Major Near Miss** | A demonstrable, reproducible flaw in the AI model that, if a clinician had not fortuitously overridden it, would have likely led to a Serious Adverse Event (SAE). | An AI-based chemotherapy dosing calculator consistently recommends a supratherapeutic dose for patients with a specific, uncommon renal function profile, caught only by an alert pharmacist. | 2 Hours | 8 Business Hours | CMO notifies Competent Authority and affected clinical sites within 3 calendar days, or as defined by the relevant national competent authority. |
| **S2 - Minor Incident** | A model error that caused a transient clinical confusion or a minor, non-harmful workflow disruption, but with no potential for serious harm. | A patient deterioration model experiences a latency spike, causing an ICU nurse to receive a risk score on a 15-minute delay, during which the patient's status was manually assessed with no change. | 4 Hours | 5 Business Days | CMO notifies the affected clinical site's CMIO within 7 calendar days. No competent authority notification is required unless a trend is identified. |
| **S3 - Non-Safety Anomaly** | A technical fault with no clinical relevance or a UI/UX bug that causes user frustration but does not alter the clinical recommendation. | The color of a risk score widget on the dashboard changes from "yellow" to "white" due to a CSS version mis-match, but the score itself remains correct. | Standard Support | N/A | Standard support ticket communication. |
| **S4 - Clinical Inquiry** | A question from a clinician about a model's output or functionality where no fault or harm is alleged. | "Can you explain the factors this model used to arrive at this specific risk score for my patient?" This is a requested explanation, not a complaint. | Standard Support | N/A | Handled by Clinical Education or CSM; logged for trend analysis. |

### 8.2 Exception Handling
Any deviation from the SLAs or procedures defined in this SOP requires a formal Exception Request, which must be submitted in the QMS. The Exception Request must detail:
1.  The procedure being deviated from.
2.  The rationale for the deviation (must be a justifiable operational conflict, not convenience).
3.  A compensatory mitigation plan to ensure patient safety is maintained during the deviation period.

Exceptions are approved by the VP of Clinical AI Products and the Chief Medical Officer. All approved exceptions are recorded in the QMS and referenced in the relevant SAF ticket. A standing exception report is reviewed quarterly by the PSRB.

---

## 9. Training Requirements

### 9.1 Role-Based Training Curriculum
All Personnel with roles defined in Section 3 must complete the required training modules before being granted access to Clinical AI systems or the QMS Safety Signal project.

| Training Module ID | Module Name | Target Audience | Frequency | Assessment |
| :--- | :--- | :--- | :--- | :--- |
| **T-CLIN-009** | Patient Safety Fundamentals & Safety Culture | All Personnel (Scope of 1.2) | Annually | Mandatory Quiz (Pass >= 85%) |
| **T-CLIN-013** | SOP-CLIN-013 Procedure Walkthrough | All Personnel (Scope of 1.2) | On Assignment, then Annually | Attestation of Understanding |
| **T-CLIN-015** | Jira Service Management for Safety Events | Clinical Safety Lead, MLOps, CSMs | Initial Role-Based | Hands-on Simulation |
| **T-CLIN-020** | Advanced RCA & CAPA Methodology | PSRB Members, MLOps Lead | Annually | Peer Review of a Mock RCA |

### 9.2 Training Records
The Quality Assurance department, using the corporate Learning Management System (LMS) `SuccessFactors`, maintains training records for all assigned curricula. Personnel without current, passing records for the applicable modules shall have their access to the QMS and relevant production systems automatically suspended until the record is complete. Training non-compliance is reported monthly to the VP of Clinical AI Products and the Chief Compliance Officer.

---

## 10. Related Policies and References

| Reference ID | Document Title | Relationship |
| :--- | :--- | :--- |
| **SOP-SEC-007** | Information Security Incident Response | Incident response procedure invoked if a safety signal investigation reveals a root cause of a cybersecurity breach. |
| **SOP-QA-004** | Corrective and Preventive Action (CAPA) | The overarching QMS procedure for CAPA management, which this SOP follows for all Phase 4 remediations. |
| **SOP-IT-015** | SaaS Infrastructure Monitoring and Alerting | Governs the standard uptime, latency, and error rate monitoring for the Meridian SaaS Platform, which feeds into Phase 1 of this SOP. |
| **SOP-FIN-042** | Algorithmic Model Risk Management for Financial Products | Governs the SR 11-7-compliant monitoring of HealthPay models; an escalation path is defined here if model behavior could indirectly harm a patient. |
| **POL-DG-101** | Corporate Data Governance Policy | Defines data ownership, classification, and quality standards for all data, including the model inference logs used for patient safety monitoring. |
| **POL-REG-045** | EU AI Act High-Risk System Compliance Policy | Foundational policy setting out the organization's strategy for conformity assessments, CE marking, and post-market obligations. |
| **NIST AI RMF 1.0** | NIST AI Risk Management Framework | The voluntary framework used by Meridian to structure its governance and risk assessment for AI safety. |
| **ISO 13485:2016** | Medical Devices - Quality Management Systems | The international standard upon which Meridian’s QMS for Clinical AI products is based. |

---

## 11. Revision History

| Version | Date | Author/Editor | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2023-10-15 | Dr. Aisha Okafor | Initial draft of the SOP, establishing PSRB and core monitoring loops. |
| 1.3 | 2024-03-20 | Dr. Aisha Okafor | Major revision post-beta to incorporate formal Severity Classification S0-S4 and explicit SLAs. Added RACI matrix. |
| 1.5 | 2024-09-01 | Dr. Aisha Okafor / Dr. Priya Patel | Updated to incorporate post-market monitoring obligations under newly passed EU AI Act (Articles 61, 72). Added Section 6.5. Expanded training requirements. |
| 1.7 | 2025-03-05 | Clinical Safety Lead | Procedural updates to QMS workflows. Replaced "Signal Review Committee" with final "Patient Safety Review Board" title. Added detailed technical monitoring metrics from MLOps platform. |
| 1.8 | 2025-06-08 | Dr. Aisha Okafor | Annual review cycle. Updated Section 3 to reflect new MLOps Lead title. Strengthened EU AI Act Art. 14 human oversight controls in Section 6.3. Updated related docs to reference CE marking under EU MDR. |
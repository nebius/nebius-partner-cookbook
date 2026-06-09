---
sop_id: "SOP-CLIN-017"
title: "Post-Market Surveillance for AI Products"
business_unit: "Clinical AI Products"
version: "3.4"
effective_date: "2024-10-26"
last_reviewed: "2025-06-04"
next_review: "2025-12-16"
owner: "Dr. Aisha Okafor, VP of Clinical AI Products"
approver: "Dr. Priya Patel, Chief Medical Officer"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Post-Market Surveillance for AI Products

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the framework and requirements for the continuous, systematic post-market surveillance (PMS) of all Artificial Intelligence (AI) and Machine Learning (ML) based products developed and deployed by the Clinical AI Products business unit of Meridian Health Technologies, Inc. The purpose of this PMS system is to proactively collect, monitor, analyze, and act upon real-world data to ensure the continued safety, effectiveness, performance, and regulatory compliance of our AI products throughout their entire lifecycle.

This SOP is designed to ensure that Meridian Health Technologies meets its obligations to maintain a proactive and systematic process for monitoring the performance of AI products after they have been released to the market. It establishes the mechanisms for the early detection of performance drift, emergent bias, safety signals, and other issues that may require corrective action, including field safety corrective actions (FSCA).

### 1.2 Scope
This SOP applies to all software products, modules, and features classified under the Clinical AI Platform business line, including but not limited to:

- Clinical decision support tools (e.g., MeridianSepsisPredict, MeridianDx-Radiology)
- Diagnostic imaging analysis systems (e.g., MeridianMammoAI, MeridianLungCT)
- Patient risk scoring models (e.g., MeridianReadmitScore, MeridianFallRisk)
- Adverse event prediction systems (e.g., MeridianAKIPredict, MeridianDVT-Screen)
- Any AI/ML component integrated into a clinical workflow, regardless of whether the algorithm is static or continuously learning.

This SOP applies to all versions of the above products that have received regulatory clearance or approval (including FDA 510(k), CE marking under EU MDR, and UKCA marking) and are actively deployed at customer sites. It is **not** applicable to products in the pre-market clinical investigation phase, which are governed by SOP-CLIN-009 (Clinical Investigation Management).

This SOP applies to all Meridian employees, contractors, and third-party partners involved in the following activities: product development, quality assurance, regulatory affairs, clinical affairs, customer support, sales engineering, and field service operations. Adherence to this SOP is mandatory for all personnel in scope.

---

## 2. Definitions and Acronyms

For the purposes of this document, the following definitions and acronyms apply:

| Term / Acronym | Definition |
| :--- | :--- |
| **AE** | Adverse Event. Any untoward medical occurrence in a patient, user, or other person, whether or not considered related to the Meridian AI product. |
| **AIMgmt** | Meridian's enterprise AI lifecycle and monitoring platform used for tracking model drift, data quality, and performance KPIs. |
| **CAPA** | Corrective and Preventive Action. A systematic process for investigating and correcting non-conformities and preventing their recurrence. |
| **CS** | Customer Support. The Meridian team responsible for frontline interaction with end-users and administrative customers, reachable via the ServiceNow ticketing system. |
| **FSCA** | Field Safety Corrective Action. An action taken by Meridian to reduce a risk of death or serious deterioration in the state of health associated with the use of a marketed product. |
| **ISMS** | Information Security Management System. Meridian's framework of policies (SOP-ISMS-001 et seq.) for managing sensitive company and customer information. |
| **KPI** | Key Performance Indicator. A measurable value that demonstrates how effectively a product is achieving key business objectives. |
| **MLOps** | Machine Learning Operations. The set of practices that aims to deploy and maintain ML models in production reliably and efficiently. |
| **PMS** | Post-Market Surveillance. The proactive, systematic process of collecting and analyzing data on a product's real-world performance. |
| **PSP** | Post-Market Surveillance Plan. The product-specific artifact that details the surveillance strategy for a given AI product. |
| **PSUR** | Periodic Safety Update Report. A comprehensive summary report that analyzes PMS data for a given product over a defined reporting period. |
| **QMS** | Quality Management System. The organizational structure, procedures, processes, and resources needed to implement quality management, governed by Meridian's Quality Manual. |
| **SAE** | Serious Adverse Event. An AE that results in death, life-threatening illness or injury, inpatient hospitalization or prolongation of existing hospitalization, persistent or significant disability/incapacity, or is a congenital anomaly/birth defect. |
| **SOP** | Standard Operating Procedure. A Meridian-controlled document detailing specific procedures. |

---

## 3. Roles and Responsibilities

The following RACI matrix defines the key roles for post-market surveillance activities (R=Responsible, A=Accountable, C=Consulted, I=Informed).

| Activity / Task | VP Clinical AI Products (Dr. Okafor) | Chief Medical Officer (Dr. Patel) | Director of QA/Risk | PMS Manager | MLOps Engineer | Clinical Data Analyst | Customer Support Lead |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **PMS Plan Ownership** | A | C | R | C | C | C | I |
| **Real-World Data Pipeline Management** | I | I | C | C | R | C | I |
| **Signal Detection & Triage** | C | I | C | R | I | R | C |
| **Complaint Investigation** | I | I | R | R | I | C | I |
| **CAPA Initiation & Oversight** | A | I | R | C | C | C | I |
| **FSCA Decision-Making** | R | A | C | C | I | I | I |
| **PSUR Authoring & Approval** | A | C | R | R | I | C | I |

### Detailed Responsibilities:

- **VP of Clinical AI Products (Dr. Aisha Okafor):** Acts as the key decision-maker regarding product lifecycle and market status. Accountable for the PMS budget and resources. Has final sign-off on the overall PMS strategy and FSCA communications.
- **Chief Medical Officer (Dr. Priya Patel):** Provides independent medical and clinical oversight. Accountable for the final clinical risk assessment in all SAE investigations and FSCA decisions. Serves as the ultimate approver for all PSURs.
- **PMS Manager (Vacant, currently covered by Director of QA/Risk):** Responsible for the day-to-day operationalization of this SOP. Manages the PMS inbox in ServiceNow, triages incoming signals, coordinates investigations, and owns the PSUR documentation. This role is the hub of all surveillance activities.
- **MLOps Engineer:** Responsible for the technical implementation of automated surveillance pipelines in AIMgmt. Configures drift monitors, data quality checks, and automated alerts. Acts as the technical SME during investigations into model performance degradation.
- **Clinical Data Analyst:** Responsible for conducting deep-dive ad-hoc analyses on surveillance data, creating dashboards, performing root cause analyses on performance drifts, and generating statistical reports for PSURs.

---

## 4. Policy Statements

Meridian Health Technologies is committed to ensuring the safety, quality, and continuous high performance of its Clinical AI products throughout their entire lifecycle. To uphold this commitment, the following high-level policies are established:

1.  **Proactive and Systematic Surveillance:** Post-Market Surveillance shall not be a passive process. Meridian will proactively design, implement, and maintain a systematic PMS process for every AI product, as detailed in a product-specific Post-Market Surveillance Plan (PSP). This process begins the moment a product receives its first regulatory clearance and continues until the final product decommissioning.

2.  **Real-World Performance Analysis:** Continuous monitoring of real-world performance is mandatory for all AI products. Meridian will collect and analyze input data, model predictions, and clinical outcomes to proactively detect model drift, bias, and degradation against the locked-down performance benchmarks established in the product's technical file.

3.  **Complaint-Driven Surveillance:** All feedback, queries, and reports of potential issues received through our multi-channel complaint handling system (via Meridian ServiceNow Portal, direct customer calls, field service reports, and internal escalations) constitute vital PMS data and must be captured, triaged, and formally investigated under the Meridian QMS.

4.  **Aggressive Reporting Culture:** Meridian fosters a culture of safety that encourages all personnel, contractors, and partners to immediately escalate any perceived performance issue, adverse event, or safety concern without delay or fear of reprisal. Early intervention is critical to patient safety.

5.  **Risk-Driven Corrective Action:** Findings from PMS activities will be assessed using our risk management framework. Any identified risk that is deemed unacceptable will result in a corrective or preventive action (CAPA) or a Field Safety Corrective Action (FSCA), executed as a controlled change through our change management board.

6.  **Information Security:** All data collected, stored, and analyzed for PMS purposes shall be handled in strict accordance with ISMS policies. All patient data used for retrospective analysis will be de-identified per Meridian's Data De-identification Protocol.

7.  **Breach Notification:** In the event of a breach of unsecured PHI related to PMS data stores, Meridian will trigger its Breach Notification and Response Plan (SOP-ISMS-012) immediately upon discovery. Affected individuals, relevant regulatory bodies, and customers will be notified without unreasonable delay and in accordance with legal requirements.

8.  **PHI Handling for Surveillance:** All PHI used in PMS investigation, trend analysis, or complaint investigation must adhere to the principle of least privilege access. PHI may only be used in its fully identifiable form during a specific complaint investigation where it is necessary to correlate a clinical outcome with a specific prediction; for all other PMS activities, including PSUR compilation and trend analysis, only de-identified data sets are permitted. All workforce members with access to PMS data must undergo annual HIPAA and data privacy training.

---

## 5. Detailed Procedures

### 5.1 Post-Market Surveillance Plan (PSP)

For every released Clinical AI product, the PMS Manager shall author and maintain a product-specific Post-Market Surveillance Plan (PSP). The PSP is a living document that defines the "how" and "what" of surveillance for that product.

**PSP Template (MUST be completed for every product):**

| Section | Content Requirement |
| :--- | :--- |
| **Product Identification** | Product Name(s), Version(s), Unique Device Identifier (UDI), regulatory status. |
| **Surveillance Objectives** | A clear statement of what the PMS activities aim to achieve (e.g., detect recall bias in readmission model, monitor concept drift in sepsis detector). |
| **Data Sources** | A detailed list of all data sources, including automated pipeline data (AIMgmt), Help Desk tickets (ServiceNow), complaints, literature reviews, and registry data. |
| **Proactive KPIs & Thresholds** | Specific, quantitative measures of performance (e.g., AUC-ROC, sensitivity, specificity, PPV) and their acceptable drift thresholds. (See Section 7). |
| **Reactive Data Gathering** | Procedure detailing how complaint data, service tickets, and social media listening will be captured and fed into the PMS process. |
| **Scheduled Analysis & Reporting** | A calendar defining the frequency of all PMS activities: daily automated checks (AIMgmt), weekly CS ticket review, bi-annual PSUR generation. |

The PSP must be approved by the VP of Clinical AI Products and the Chief Medical Officer before a product's market release. It shall be reviewed at least annually against this SOP.

### 5.2 Real-World Performance Monitoring (Proactive)

This procedure describes the continuous, automated monitoring of AI product performance via our AIMgmt MLOps platform.

**Step 1: Data Ingestion and Quality Check**
The MLOps Engineer shall configure the AIMgmt platform to continuously ingest a stream of de-identified inference data from customer sites. This process is automated. For every inference event, the pipeline must capture: a unique prediction ID, the input features (de-identified), the model’s prediction/score, and the timestamp.
- **Data Quality Monitor:** An automated rule checks that incoming data conforms to the expected schema and value ranges. If a Data Quality (DQ) KPI breaches its threshold (e.g., >10% of a feature's values are NULL for a 5-minute window), an AIMgmt "Data Quality" alert is generated and sent to the `#mlops-pms-critical` Slack channel and the PMS Manager's ServiceNow queue.

**Step 2: Performance Metric Drift Detection**
AIMgmt calculates daily performance KPIs against available ground truth data. Two monitors are active:
1.  **Baseline Monitor:** Compares the daily metric against the locked-down baseline in the technical file. A breach is a >10% relative change in a non-safety-critical metric (e.g., specificity) or a >5% relative change in a safety-critical metric (e.g., sensitivity for MeridianSepsisPredict).
2.  **Prediction Distribution Drift (Data Drift):** Compares the distribution of input features for the current day vs. the training data baseline using a Population Stability Index (PSI). A PSI > 0.2 on any key feature triggers a "Data Drift" alert.

**Step 3: Alert Triage (The 60-Minute Rule)**
Upon receiving an AIMgmt alert, the on-call MLOps Engineer has a 60-minute window to perform initial triage. The triage steps are:
1.  **Acknowledge & Verify:** Acknowledge the alert in AIMgmt. Pull up the product's live dashboard and manually verify the spike/drop is not an ingestion pipeline failure.
2.  **Impact Analysis:** Determine the affected product, version, and customer sites.
3.  **Containment (If Necessary):** If the issue appears to be causing real-world harm, the engineer (in consultation with the PMS Manager) has the authority to initiate a remote feature-flag kill switch, turning off the AI component for the affected sites while the clinical workflow continues on a non-AI fallback, as per the approved contingency plan. This is considered an emergency change and follows the Emergency Change Management Procedure (SOP-RND-035).

All triage actions, findings, and the decision rationale must be fully documented in a ServiceNow Incident record within two hours.

### 5.3 Complaint Handling and Reactive Surveillance

This procedure details the handling of all performance and safety-related complaints received from customers or internal sources.

**Step 1: Logging the Complaint**
Any Meridian employee who receives a communication, verbal or written, that alleges a deficiency in the performance, safety, or quality of a Clinical AI product MUST log the complaint into ServiceNow (`Product Safety > Complaint`) within 1 business day. The record must capture:
- Date of Awareness: The date Meridian became aware of the issue.
- Source: Customer name, contact details, and site.
- Product: Name and version of the AI product.
- Incident Description: A verbatim account of the customer's report. Do not interpret or censor the description.
- Classification: The reporter's preliminary assessment (`Non-Serious AE`, `Serious AE`, `Performance Issue`, `Usability Issue`).

**Step 2: Initial Screening and Triage (24-Hour SLA)**
The PMS Manager reviews all new complaint records within 24 hours of submission.
- **Is it reportable?** If the complaint describes an event that led to a patient's death or serious injury, it is classified as a potential SAE and is immediately escalated to the CMO and VP of Clinical AI Products for a mandatory FSCA evaluation under Section 5.4. The clock starts immediately.
- **What is the priority?** The PMS Manager assigns a priority level (P1-Critical to P4-Cosmetic) based on the potential patient safety impact and business disruption.

**Step 3: Investigation (15-Day SLA for P1/P2)**
For any complaint classified as P1 or P2, a formal investigation is conducted and documented as a CAPA report. The PMS Manager assigns an Investigation Team, which must include a Clinical Data Analyst and a technical SME (e.g., the product's AI Architect).
The investigation MUST:
1.  **Replicate the Data:** Gain access to the specific patient case's de-identified input feature vector. Determine the model's prediction and confidence score for that case.
2.  **Cohort Analysis:** Analyze the model's performance in a broader cohort of similar patients from the AIMgmt database. Determine if the case was an isolated anomaly or part of a systemic drift.
3.  **Root Cause Analysis:** Employ a structured methodology (e.g., “5 Whys”) to determine the root cause: Was it a data quality problem? A model limitation? An edge case of the clinical workflow? A user error?
4.  **Risk Assessment:** Document the clinical impact and the potential for recurrence.

**Step 4: Closing the Complaint**
The complaint is closed in ServiceNow only when the root cause is identified, the risk is assessed, and a CAPA plan (if any) has been initiated and linked to the complaint record. The customer must be communicated to regarding the outcome of the review.

### 5.4 Field Safety Corrective Action (FSCA)

An FSCA is the most critical PMS output. This procedure is invoked when a product issue presents a significant risk to patient health or safety.

**Step 1: FSCA Evaluation Conference**
When a P1 complaint or an AIMgmt critical alert is confirmed, the CMO must convene an FSCA Evaluation Conference. This mandatory high-priority meeting must occur within 48 hours of verification and includes the CMO, VP of Clinical AI Products, Director of QA/Risk, and the relevant Investigation Team lead.

The conference answers three questions:
1.  **Is the product non-conforming?** (Yes/No)
2.  **Is there a causal link between the non-conformity and a serious patient incident?** (Yes/No/Unclear)
3.  **Is a risk to public health ongoing?** This determines the urgency of the FSCA.

**Step 2: Decision and Strategy**
If the answer to Question 1 and Question 3 is "Yes," an FSCA is mandatory. The VP of Clinical AI Products, in consultation with the group, determines the action strategy. There are three primary strategies:
1.  **Product Recall:** The permanent removal of a product from all customer sites. This is reserved for issues where a software fix is infeasible in a relevant timeframe.
2.  **Field Safety Notice (FSN):** An FSN is an urgent customer communication that mandates a specific user action to mitigate risk while a permanent fix is developed.
3.  **Field Safety Correction:** An immediate intervention, such as deploying a feature-flag kill switch, pushing an emergency over-the-air patch, or performing a mandatory field upgrade, after which the product may remain in use or be returned to use.

**Step 3: FSN Communication (24-Hour Turnaround)**
If an FSN is the chosen strategy, the VP of Clinical AI Products, Clinical Product Manager, and Chief of Corporate Communications must draft a Field Safety Notice. The notice must be approved by the CMO and transmitted to all affected customers via email, in-product notification, and a posted notice on the Meridian ServiceNow Portal within 24 hours of the decision.

### 5.5 Periodic Safety Update Report (PSUR)

A PSUR is a comprehensive product-specific report that serves as the record of all PMS activities over a defined period.

**Frequency:** PSURs are generated bi-annually for products with CE marking, or annually for products with a PMS maturity score of “Low” or if performance is stable with no P1/P2 incidents in the review period.

**Mandatory PSUR Contents (Template `FRM-PMS-101`):**
1.  **Product Identification & Report Scope:** Product name, version(s), UDI, and the reporting period covered.
2.  **Conclusion of the Benefit-Risk Determination:** A clear, evidence-based statement confirming that the benefits of using the product continue to outweigh the identified risks.
3.  **Sales & Usage Data:** Total deployed instances, active unique users, and the total number of inferences performed in the reporting period.
4.  **Proactive Trend Analysis:** Graphical presentations of all monitored KPIs (see Section 7), drift metrics, and a written narrative of all AIMgmt alerts and their root causes.
5.  **Reactive Complaint Summary:** A rolled-up, aggregated, and de-identified analysis of all complaints, categorized by type, root cause, and criticality.
6.  **FSCA Summary:** A detailed log of all FSCAs, CAPAs, and software patches released during the period.

The PSUR is authored by the PMS Manager, reviewed by the Director of QA/Risk, and approved by the Chief Medical Officer. Completed, approved PSURs are stored as Quality Records in the `QMS-PMS` controlled document library.

---

## 6. Controls and Safeguards

The following technical and administrative controls are in place to ensure the integrity and security of the PMS process.

| Control Category | Control ID | Control Description |
| :--- | :--- | :--- |
| **Access Control** | IAM-PMS-001 | Access to the AIMgmt dashboard, ServiceNow PMS queues, and the `QMS-PMS` document library is granted via Role-Based Access Control (RBAC). |
| **Data Integrity** | DQ-PMS-001 | Automated data quality monitors at the point of ingestion into the AIMgmt PMS data lake. Any data pipeline failure stops the clock for KPI monitoring until the issue is resolved. |
| **Audit Trail** | AUD-PMS-001 | Every action taken on a complaint record in ServiceNow, every field deployed in an FSCA, and every CAPA record change is logged in an immutable audit log with user ID and timestamp. |
| **Segregation of Duties** | SOD-PMS-001 | The person performing a PMS investigation cannot be the sole QA approver for the resulting CAPA. |
| **Privacy by Design** | PRV-PMS-001 | All data pipelines for proactive monitoring are designed to automatically strip and de-identify patient-identifiable information (PII/PHI) before it reaches the AIMgmt analytics layer, in accordance with the Data De-identification Protocol. Only personnel with a specific, documented "break-glass" role (the PMS Manager and CMO) can access the raw, identified log for an active, high-priority investigation. |
| **Encryption** | ENC-PMS-001 | All PMS data, including identified complaint logs and de-identified data sets, is encrypted at rest (AES-256) and in transit (TLS 1.3) within the Meridian corporate network. |

### 6.1 PHI Handling for Post-Market Surveillance

Personnel handling PHI as part of complaint investigations or field safety actions must follow established Meridian data handling procedures at all times. PHI may only be accessed for the specific, documented purpose of investigating a reported incident.

- **Data Minimization:** Only the minimum necessary PHI to carry out a complaint investigation shall be accessed.
- **Data Storage:** Identified PHI related to a complaint shall be stored as part of the secured, restricted-access complaint record in ServiceNow. It MUST NOT be stored in unsecured locations, local hard drives, or third-party non-compliant cloud tools.
- **Data Sharing:** No PHI related to a PMS activity may be shared outside of the documented investigation team without the explicit approval of the Data Protection Officer.
- **Workforce Training:** All personnel with access to PMS data must complete the mandatory annual Meridian HIPAA & Data Privacy Training (SOP-CORP-109). Completion is tracked in the Meridian LMS.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 PMS Process KPIs (Quality & Compliance Health)

These KPIs measure the health and compliance of the PMS process itself. They are reviewed monthly by the VP of Clinical AI Products.

| KPI | Target | Measurement Method |
| :--- | :---: | :--- |
| **% of PSPs Reviewed On-Time** | 100% | AIMgmt Compliance Calendar |
| **Mean Time to Complaint Triage** | < 16 business hours | ServiceNow Report `RPT-CS-010` |
| **% of P1/P2 Investigations Closed within 15-day SLA** | > 90% | ServiceNow Dashboard `DB-QA-002` |
| **% of FSCA Decisions Made within 48-hr Window** | 100% | Manual QMS Audit Log |

### 7.2 Product Performance KPIs (Safety and Effectiveness)

These are product-specific and defined in the PSP. They are monitored by the MLOps team and reported in the PSUR. Examples include:

- **For a Classification Model (e.g., sepsis prediction):**
    - Sensitivity (Recall)
    - Positive Predictive Value (Precision)
    - Area Under the Receiver Operating Characteristic curve (AUC-ROC)
    - Net Reclassification Improvement (NRI) vs. baseline
- **For a Risk Score Model (e.g., fall risk):**
    - Observed vs. Expected (O/E) ratio by risk decile
    - Mean Brier Score (measure of calibration)

### 7.3 PMS Dashboards

The following ServiceNow dashboards are the source of truth for PMS status:
- **`DB-VP-001: Clinical AI PMS Executive View`:** Provides a real-time summary of all in-flight investigations, PSP compliance, and key alert statistics.
- **`DB-QA-002: PMS Complaint & CAPA Status`:** A detailed operational dashboard used by the PMS Manager to manage the queue of open complaints and CAPAs.

---

## 8. Exception Handling and Escalation

### 8.1 General Exceptions
Any request for a deviation from the mandatory procedures defined in this SOP (e.g., extending a 15-day investigation SLA) must be formally requested via a ServiceNow "SOP Deviation" request. The request MUST include:
- A detailed justification for the exception.
- A risk assessment of the impact of the exception.
- A proposed compensatory control.

**Approval Authority:**
- Deviations to operational SLAs (e.g., investigation timeline extension): **VP of Clinical AI Products**.
- Deviations to mandatory PSP content or reporting frequency: **Chief Medical Officer**.

### 8.2 Escalation Path for Unresolved Disputes
If a consensus cannot be reached within the Investigation Team (e.g., a Clinical Data Analyst and an AI Architect disagree on the root cause), the issue follows a strict hierarchical escalation path:

1.  **Escalation Level 1:** The PMS Manager, acting as a neutral facilitator, mediates the dispute and documents the differing positions. (Resolution target: 2 business days).
2.  **Escalation Level 2:** If not resolved, the matter is escalated to the Director of QA/Risk, who will review the evidence and make a binding decision based on patient safety risk. (Resolution target: 5 business days from Level 1).
3.  **Escalation Level 3:** The final arbiter is the Chief Medical Officer. No CAPA or FSCA decision can be blocked by an internal technical dispute; the CMO will make a risk-based decision that resolves the deadlock.

---

## 9. Training Requirements

All personnel performing roles identified in Section 3 must undergo training on this SOP to ensure a consistent, high-quality approach to post-market surveillance.

| Training Module | Target Audience | Frequency | Method |
| :--- | :--- | :---: | :--- |
| **SOP-CLIN-017: PMS Awareness & Principles** | All Clinical AI Product business unit employees, all Customer Support Tier 2/3 staff. | Once (within 30 days of hire) annually thereafter. | Computer-Based Training (CBT) in LMS, followed by a 10-question quiz (pass mark: 80%). |
| **AIMgmt PMS & Drift Detection Workshop** | MLOps Engineers, Clinical Data Analysts. | Annually. | Instructor-led hands-on workshop focusing on drift interpretation, alert triage, and the emergency kill-switch procedure. |
| **Complaint Handling & FSCA Decision Workshop** | PMS Manager, VP Clinical AI Products, CMO, QA/Risk Director. | Bi-annually. | A 4-hour tabletop simulation facilitated by an external regulatory affairs consultant, covering a realistic FSCA scenario from complaint receipt to FSN issuance. |

All training records are tracked automatically in the Meridian Corporate LMS. The VP of Clinical AI Products reviews department-wide training compliance quarterly. An employee who is out of compliance is prohibited from contributing to any PMS activity until training is completed.

---

## 10. Related Policies and References

| Document ID | Document Title |
| :--- | :--- |
| `SOP-CLIN-009` | Clinical Investigation and Pre-Market Evaluation Management |
| `SOP-QA-002` | Corrective and Preventive Action (CAPA) Management |
| `SOP-CORP-109` | HIPAA & Data Privacy Annual Training |
| `SOP-ISMS-012` | Breach Notification and Response Plan |
| `SOP-RND-035` | Emergency Change and Feature-Flag Management |
| `SOP-CLIN-024` | AI Model Performance Monitoring & Drift Detection |
| `FRM-PMS-101` | PSUR Report Template |
| `PLN-CLIN-SEPS-V2` | Post-Market Surveillance Plan for MeridianSepsisPredict V2 |
| `NIST AI 100-1` | Artificial Intelligence Risk Management Framework (AI RMF 1.0) |
| `21 CFR Part 822` | Post-Market Surveillance (US FDA) |

---

## 11. Revision History

| Version | Date | Author | Revision Description |
| :--- | :--- | :--- | :--- |
| 1.0 | 2019-11-08 | J. Miller (Former VP, Clin) | Initial SOP creation. Focused on reactive, complaint-based PMS for first-generation fixed-algorithm products. |
| 2.1 | 2021-02-15 | A. Okafor | Major revision. Added proactive real-world monitoring procedure using new AIMgmt platform. Introduced concept of PSP and PSUR. Expanded roles to include MLOps Engineer. |
| 3.0 | 2022-09-01 | K. Chen (QA Manager) | Major revision. Integrated CAPA and FSCA procedures from retired SOP-QA-015. Harmonized with ISO 13485 and new EU MDR requirements. Added controls section. Increased training frequency. |
| 3.2 | 2023-04-10 | A. Okafor | Minor revision. Updated RACI matrix to reflect new PMS Manager role. Changed complaint logging SLA from 3 business days to 1 business day. |
| 3.3 | 2024-01-18 | P. Gupta (Reg Affairs) | Minor revision. Updated references to comply with 2024 FDA guidance on MLMD FSCAs. Clarified data retention requirements in Section 6. |
| 3.4 | 2024-10-26 | A. Okafor | Major revision. Full restructuring to align with SOP-CLIN-024 and new regulatory standards. Updated all roles, KPIs, and thresholds based on learnings from three years of AIMgmt operational data. Revised PHI handling language. This version supersedes all prior. |
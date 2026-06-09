---
sop_id: "SOP-HR-015"
title: "Performance Review and Documentation"
business_unit: "Human Resources"
version: "3.8"
effective_date: "2025-01-17"
last_reviewed: "2026-05-05"
next_review: "2026-11-14"
owner: "Jennifer Walsh, Chief Human Resources Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Performance Review and Documentation

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, cadence, and governance for the end-to-end performance management lifecycle at Meridian Health Technologies, Inc. The purpose of this document is to ensure that the evaluation of employee performance is conducted equitably, transparently, and in alignment with Meridian’s core values of clinical safety, data integrity, and regulatory compliance. Given Meridian's position at the intersection of artificial intelligence, healthcare, and financial services, it is critical that individual performance is not only measured against business outcomes but also against adherence to the stringent risk and compliance controls required by HIPAA, the EU AI Act, GDPR, SR 11-7, and SOC 2 standards.

This SOP defines the standardized methodology for setting objectives, documenting progress, delivering feedback, and calibrating ratings to mitigate unconscious bias and ensure meritocratic outcomes. It further outlines the procedural requirements for addressing underperformance through structured Performance Improvement Plans (PIPs), ensuring that all corrective actions are legally defensible and compliant with European and North American employment law.

### 1.2 Scope

This SOP applies to all full-time and part-time regular employees of Meridian Health Technologies, Inc. across all global offices (Boston, London, Berlin, Singapore, Toronto) and all business units, including but not limited to Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform.

The policy covers:
- **All Employees:** Regular full-time and part-time staff who have successfully completed their introductory period (90 days).
- **Managers:** Anyone with direct supervisory responsibilities, including functional leads and matrix managers within the Clinical AI and HealthPay divisions.
- **Probationary Employees:** Subject to a modified 90-day review cadence as defined in SOP-HR-003 (Onboarding and Probation).
- **Contractors and Consultants:** Excluded from this performance review cycle, managed instead via vendor performance metrics detailed in SOP-PROC-022 (Vendor Management). However, any contractor accessing PHI or working on high-risk AI systems is subject to the documentation standards outlined herein for audit trail purposes.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **AI Act** | The European Union Artificial Intelligence Act (Regulation 2024/1689). Meridian’s Clinical AI Platform is classified as High-Risk per Annex III. |
| **Calibration** | A facilitated session where managers align on performance standards, validate evidence, and standardize rating distributions to eliminate bias. |
| **CCF** | Core Competency Framework. A behavioral matrix specific to Meridian’s "Care, Code, Compliance" philosophy. |
| **CDS** | Clinical Decision Support. A module within the Clinical AI Platform subject to FDA 510(k) clearance and MDR CE marking. |
| **DPIA** | Data Protection Impact Assessment. A process required under GDPR Article 35 for processing that is likely to result in high risk to natural persons. |
| **DSAR** | Data Subject Access Request. A formal request from an employee to access their personal data, including performance records. |
| **GDPR** | General Data Protection Regulation (EU) 2016/679. |
| **Lattice** | Meridian’s centralized Human Capital Management (HCM) and performance management platform. Integrates with Okta (SSO) and Snowflake (analytics). |
| **NIST AI RMF** | National Institute of Standards and Technology AI Risk Management Framework. Governs the trustworthiness of AI outputs, including HR recommendation engines. |
| **PIP** | Performance Improvement Plan. A structured, time-bound intervention for employees with significant gaps in performance or conduct. |
| **RACI** | A responsibility assignment matrix (Responsible, Accountable, Consulted, Informed). |
| **SMART** | A methodology for setting objectives: Specific, Measurable, Achievable, Relevant, Time-bound. |
| **SOC 2** | Service Organization Control 2 Type II certification, covering security, availability, and confidentiality of the Meridian SaaS Platform. |
| **SR 11-7** | Federal Reserve guidance on model risk management, applicable to HealthPay credit and fraud detection models. |

---

## 3. Roles and Responsibilities

The following RACI matrix governs the execution of the performance review process. All named roles must complete the training outlined in Section 9.

| Activity | Employee | Manager | HR Business Partner (HRBP) | Chief AI Officer / CISO | CHRO (J. Walsh) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Self-Evaluation** | **R** | **A** | **I** | — | — |
| **Manager Evaluation** | **C** | **R** | **A** | **C** (AI risk roles) | — |
| **360-Degree Feedback** | **C** | **R** | **A** | — | — |
| **Rating Calibration** | — | **C** | **R** | **C** | **A** |
| **PIP Initiation & Monitoring** | **I** | **R** | **A** | — | **C** |
| **Automated AI Note-Taking*** | **I** | **R** | — | **A** | **I** |
| **System of Record (Lattice)** | **R** (Data entry) | **R** (Approval) | **A** (Audit) | **C** | **I** |

*\*Meridian deploys an internal AI summarizer to assist managers in drafting review narratives based on documented feedback. Under the EU AI Act and Dr. Marcus Rivera’s governance protocol, all final documentation must include a "Human-in-the-Loop" verification flag in Lattice.*

---

## 4. Policy Statements

### 4.1 Data Protection and Employee Privacy
Meridian Health Technologies processes employee performance data as part of the execution of the employment contract. Performance ratings, PIP documentation, and 360-degree feedback qualify as sensitive personal data. All processing must comply with GDPR and, where applicable, local employment laws.

- **Storage Limitation:** Performance records, including raw calibration notes, are retained in active Lattice profiles strictly for the duration of employment plus 18 months. Archival occurs automatically to AWS eu-west-1 encrypted S3 buckets for former EU employees.
- **Right of Access:** Employees may submit a DSAR to review unstructured manager notes. While Meridian strives to respond to all DSARs efficiently, the process for retrieving unstructured supplementary data from disconnected business unit silos (specifically legacy HealthPay feedback files) requires a manual search. Employees should allow a processing window for complex cross-system retrievals.
- **Data Minimization:** Managers must not document sensitive special category data (e.g., specific diagnoses, genetic information) in the narrative fields of Lattice. Any documentation related to intermittent leave must be maintained strictly by HRBPs, not line managers.

### 4.2 Zero Tolerance for Bias
Performance reviews impact compensation, promotion, and assignment to high-risk AI development streams. Meridian maintains a zero-tolerance policy for discrimination based on race, gender, age, sexual orientation, disability, or any protected characteristic. The Chief AI Officer mandates that the AI-assist tools used to analyze review language (LangSmith traces) are monitored for adversarial drift on a quarterly basis.

### 4.3 High-Risk Role Designation
Employees whose roles directly impact the logic of the Clinical AI Platform or the quantitative models within HealthPay are designated as "High-Risk Role." Failure to meet performance standards in these roles constitutes a potential regulatory risk (e.g., violation of SR 11-7 model governance). Reviews for these employees must include a compliance integrity scorecard co-signed by the General Counsel or CISO.

---

## 5. Detailed Procedures

### 5.1 The Performance Review Cycle

Meridian operates on a **Quarterly Pulse + Annual Summative** cycle. The fiscal year runs February 1 – January 31.

| Phase | Timeframe | Action | Duration |
| :--- | :--- | :--- | :--- |
| **Q1 Pulse** | Apr 1 – Apr 15 | Goal check-in, no rating. Feedback on velocity. | 2 weeks |
| **Mid-Year Review** | Jul 15 – Jul 31 | Formal mid-year rating (1-5). PIP check-in. Competency review. | 2 weeks |
| **Q3 Pulse** | Oct 1 – Oct 15 | Goal re-alignment for H2. Forward-looking focus. | 2 weeks |
| **Annual Review** | Jan 1 – Jan 31 | Summative self-eval, manager eval, 360 collection. | 4 weeks |
| **Calibration** | Feb 1 – Feb 14 | Business unit calibration committee sessions. | 2 weeks |
| **Compensation** | Feb 15 – Feb 28 | Merit, bonus, and LTI allocation based on calibrated rating. | 2 weeks |

### 5.2 Goal Setting and the SMART Framework

1.  **System Entry:** All goals must be entered and approved in Lattice within the first two weeks of the fiscal year (by Feb 15).
2.  **Composition:**
    - **What (60%):** Business outcomes and OKRs tied to the specific business line (e.g., "Achieve 99.95% uptime for HealthPay API gateway").
    - **How (40%):** Behavioral competency tied to the CCF. Specific focus on Security First and Regulatory Stewardship.
3.  **Weighting:** No single goal may carry a weight greater than 50%. Managers must assign a minimum of 10% weighting to a "Culture of Compliance" objective.
4.  **Modification:** Goals may be modified during Q1 or Q3 Pulses only via a "Goal Change Request" initiated by the manager and approved by the HRBP.

### 5.3 The Calibration Cycle

The calibration process is designed to ensure that Dr. Patel’s division (Clinical) and Mr. Thornton’s division (Finance/Tech) apply the rating scale consistently for the purpose of internal mobility.

#### 5.3.1 Calibration Committee Composition
- **Chair:** CHRO or divisional HRBP Lead.
- **Members:** All Directors and above within the business unit. Dr. Priya Patel (or delegate) must chair clinical calibration sessions to verify technical validity.
- **Observer:** A representative from the DEIB Center of Excellence.

#### 5.3.2 Procedure
1.  **Data Aggregation:** HRBPs pull a "Distribution Curve" report from Lattice, anonymized for gender and race intersectionality.
2.  **Tentative Mapping:** Managers plot their direct reports on the 9-box talent grid within Lattice.
3.  **Calibration Session (Live):**
    - Managers review "High Performer" and "Low Performer" cohorts.
    - **Evidence Scrub:** The committee audits narrative text for specific deliverables. Vague adjectives like "superb" must be backed by tangible metrics or removed.
    - *Note on Privacy:* If an EU employee’s performance data needs to be transferred to the US-based system for calibration, standard Binding Corporate Rules apply. However, if a manager objects to a rating and requests a review of raw historical feedback, data retrieval falls under the standard DSAR workflow as managed by the HRIS team.
4.  **Forced Distribution Guidance:** While Meridian does not force a strict bell-curve termination, the calibration committee targets a normalized distribution where "Exceeds Expectations" (Rating 5) does not exceed 15% of the population, to prevent inflationary pressure.

### 5.4 Documentation Standards

This section addresses the "Code" aspect of our "Care, Code, Compliance" framework. Inadequate documentation is a procedural violation.

1.  **Record Integrity:** All performance review narratives must be finalized in Lattice no later than 48 hours after the 1:1 conversation.
2.  **AI-Assist Protocol (SOP-HR-015-AI):**
    - Managers may use the Lattice "Auto-Scribe" feature to transcribe and summarize conversation notes.
    - As mandated by the AI Act transparency requirement, any AI-generated summary must have the `human_override` toggle activated or manual editorial changes must be logged.
3.  **Unstructured Data:** Files, private emails, or slacks are **not** official Performance Management sources. If a manager relies on feedback contained in Slack, they must upload the relevant thread to the Lattice "Manager Notes" section as a permanent record.

### 5.5 Performance Improvement Plan (PIP) Procedure

A PIP is required when an employee receives a "Does Not Meet Expectations" (Rating 1) for their aggregate Business Outcome score, or a Rating 1 on a compliance-critical objective.

#### 5.5.1 Initiation
1.  **PIP Draft:** The manager drafts the PIP using the approved Lattice template (`[PIP] - [Employee Name] - [Date]`).
2.  **HRBP Review:** The HRBP must review the draft for legal defensibility, clarity of expectations, and absence of bias.
3.  **Finalization:** The PIP must specify:
    - The specific performance gap (e.g., "Failure to maintain MDR documentation standards").
    - The concrete actions required (e.g., "Complete the refresher training SOP-HR-022 and correctly file 100% of MDR submissions for the next 30 days").
    - The duration of the PIP. Standard is **60 calendar days**.
    - Consequences of failure (reassignment, demotion, termination).

#### 5.5.2 Monitoring and Closure
1.  **Weekly 1:1s:** Manager and employee meet weekly. Manager logs progress notes in the PIP module.
2.  **30-Day Checkpoint:** HRBP formally reviews progress.
3.  **60-Day Decision:**
    - **Successful Completion:** PIP closed; employee transitions to a standard quarterly pulse schedule.
    - **Unsuccessful:** HRBP initiates a Separation Review Board (SRB) process. If the employee is a High-Risk Role holder (e.g., AI Model Validator), their access to production systems must be suspended immediately pending the SRB outcome, per SOP-IS-008.

---

## 6. Controls and Safeguards

To maintain the confidentiality, integrity, and availability of the Performance Management system and the data within it:

### 6.1 Technical Controls
- **Lattice SSO:** Access requires Okta MFA. Role-based permissions strictly segregate Manager, HRBP, and Super-Admin views.
- **Audit Trails:** All changes to a finalized review form are immutable and logged with a timestamp, user IP, and action. Audit logs feed into the Snowflake SIEM monitored by the Meridian SOC.
- **Encryption:** Data at rest in Lattice is encrypted via AES-256. Data in transit uses TLS 1.3.
- **AI Summarizer Oversight:** The HR AI-assist model operates within a closed-loop environment. The CISO monitors LangSmith traces for prompt injection attempts or model drift that could influence sentiment analysis.

### 6.2 Administrative Controls
- **The 2-Rule:** No manager may unilaterally deliver a "Needs Improvement" (Rating 2) or "Does Not Meet" (Rating 1) summative review without a second-line leader or HRBP signature. This acts as a validation check against capricious punitive rating.
- **Data Retention Schedule:** Reviews are maintained in "Active" status within Lattice for the employment term + 18 months. Thereafter, records are securely purged from the live system. EU employee files are archived for 10 years in isolated AWS Dublin buckets to comply with latent legal claims requirements, strictly separated from the active CRM.
- **Separation of Duties:** The HR Business Partner approving the PIP cannot be the same person who approves the separation of employment in Workday.

---

## 7. Monitoring, Metrics, and Reporting

The effectiveness of this SOP is measured through a combination of HR operational metrics and risk-adjusted compliance indicators. The People Analytics team publishes a monthly dashboard to the CHRO and quarterly to the Risk Committee.

| KPI | Target | Reporting Cadence | Owner |
| :--- | :--- | :--- | :--- |
| **Cycle Completion Rate** | 95% of reviews finalized by deadline | Bi-annual (Mid-Year, Annual) | HR Operations |
| **Calibration Variance Index** | < 10% inter-manager variance within a team for the same competency scores | Annual | HRBPs |
| **PIP Success Rate** | 50% successful completion; > 80% of those retained 12 months post-PIP | Quarterly | ER/Legal |
| **AI Summarizer Adoption** | 80% of managers using tool, 100% compliance on `human_override` flag | Monthly | HRIS |
| **DSAR Compliance** (Right of Access) | Acknowledgment of request within 48 hrs | Monthly | HR Privacy |

### 7.1 High-Risk Role Specific Metrics
For the Clinical AI and HealthPay quant teams, the Chief Risk Officer receives a "Culture of Compliance" risk score derived from anonymous aggregated performance review data. A negative spike in "Regulatory Stewardship" competency scores correlates strongly with model development risk.

---

## 8. Exception Handling and Escalation

Exceptions to this SOP represent a deviation from regulatory control. They must be minimized and strictly managed.

### 8.1 Requesting an Exception
Exceptions to the review cycle timeline—for example, an extension due to a prolonged medical leave or a manager’s sudden departure—must be initiated by the functional VP via a "Performance Cycle Deviation Request" in Lattice.

### 8.2 Approval Authority
- **Timeline Extensions (≤ 30 days):** VP of Business Unit + HRBP Director.
- **Timeline Extensions (> 30 days):** CHRO (Jennifer Walsh).
- **PIP Deviation:** Any deviation from the standard 60-day PIP duration or the requirement for weekly check-ins requires a legal review and CHRO approval.
- **Compensation Exception:** Any attempt to override the calibrated rating for compensation purposes (e.g., retaining a low-rated employee at a high salary to satisfy HealthPay client expectations) must be approved by the CEO (Dr. Chen) and reported to the Board Compensation Committee.

### 8.3 Escalation Path
If an employee believes the performance review process has been manipulated or biased:
1.  **Employee's Direct Manager:** Should attempt to resolve.
2.  **HR Business Partner:** Acts as neutral investigator.
3.  **Employee Relations:** Formal investigation launched via the Lattice Ethics Hotline.
4.  **GDPR Supervisory Authority:** If the complaint regards unlawful processing of personal data.

---

## 9. Training Requirements

Mandatory training ensures global consistency and compliance with the SOP.

| Module | Audience | Frequency | Platform |
| :--- | :--- | :--- | :--- |
| **SOP-HR-015: Policy Acknowledgment** | All Employees | Annually (Jan 1) | Lattice Learning |
| **Managing High-Risk Talent** | Managers of AI/HealthPay roles | Annually (Q4) | Workday ILT (Virtual) |
| **Bias & Calibration Mastery** | All Managers | Bi-annual (Jun/Dec) | Lattice Micro-learning |
| **Documentation & Data Privacy (GDPR)** | All EU & Matrix Managers | Annually (Q1) | Lattice Learning |
| **360-Degree Feedback Fundamentals** | All Employees | Once | Lattice On-Demand |

**Compliance Tracking:** The Lattice LMS automatically records completions. Non-compliance by the deadline triggers an automatic suspension of the manager’s ability to finalize reviews until training is complete. Access to the AI Summarizer feature in Lattice is disabled until completion is logged.

---

## 10. Related Policies and References

- **SOP-HR-003:** Onboarding and Probationary Periods
- **SOP-HR-022:** Employee Privacy and Data Protection (GDPR)
- **SOP-HR-030:** Termination of Employment and Offboarding
- **SOP-IS-008:** Identity Access Management for High-Risk Systems
- **SOP-LEG-101:** Litigation Hold and Data Preservation
- **External Standard:** EU AI Act Article 14 (Human Oversight in High-Risk Systems)
- **External Standard:** Federal Reserve SR 11-7 (Model Risk Management)
- **Meridian System:** Lattice HCM Process Guide
- **Meridian System:** Works Councils Agreement (Berlin Office Addendum B)

---

## 11. Revision History

| Version | Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2019-03-15 | R. Davies (HR) | Initial creation. Annual cycle only. |
| 2.1 | 2020-09-01 | J. Walsh (CHRO) | Transitioned to Quarterly Pulse + Annual cycle. Integration of 360 module. |
| 2.5 | 2022-01-10 | J. Walsh (CHRO) | Mandated calibration sessions and PIP tracking in Lattice following SOC 2 audit. |
| 3.3 | 2023-07-22 | L. Chen (Legal) | Comprehensive GDPR update specific to EU employee data flow. Added DSAR workflow context for performance data. |
| 3.7 | 2024-11-01 | M. Torres (CISO) | Introduced AI-Assist Protocol and `human_override` control flags in response to EU AI Act enforcement deadlines for HR recommendation tools. |
| 3.8 | 2025-01-17 | J. Walsh (CHRO) | Recalibrated forced distribution guidance; updated DSAR manual retrieval procedures across legacy systems; added specific CEO-level oversight for compensation deviation; removed ambiguity around 30-day PIP extensions. |
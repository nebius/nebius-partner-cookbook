---
sop_id: "SOP-LEGC-003"
title: "Internal Audit Program"
business_unit: "Legal & Compliance"
version: "4.3"
effective_date: "2025-12-28"
last_reviewed: "2026-10-07"
next_review: "2027-04-18"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
  - "GDPR"
  - "SR 11-7"
status: "Active"
---

# Standard Operating Procedure: Internal Audit Program

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework for Meridian Health Technologies, Inc.’s (“Meridian” or the “Company”) Internal Audit Program. The program is designed to provide independent, objective assurance and consulting activity designed to add value and improve Meridian’s operations. It helps the organization accomplish its objectives by bringing a systematic, disciplined approach to evaluate and improve the effectiveness of governance, risk management, and control processes. This SOP ensures that the internal audit function operates as a cornerstone of Meridian’s compliance posture, specifically addressing the rigorous demands of healthcare data protection and financial model governance, while providing assurance to the Board of Directors and executive leadership.

### 1.2 Scope

This SOP applies to all business lines, departments, geographies, and processes within Meridian Health Technologies, Inc., including but not limited to:

- **Clinical AI Platform:** Algorithm development lifecycle, training data quality, model deployment, clinical validation, adverse event reporting, and human-in-the-loop protocols.
- **HealthPay Financial Services:** Transaction processing, loan origination and underwriting models, fraud detection systems, claims adjudication algorithms, and custody of funds.
- **MedInsight Analytics:** Protected Health Information (PHI) data aggregation pipelines, de-identification and anonymization processes, care gap logic, and outcomes prediction model outputs.
- **Enterprise Technology & IT Operations:** Cloud infrastructure (AWS, Azure), Identity and Access Management (Okta), endpoint security (CrowdStrike), secrets management (HashiCorp Vault), encryption key management (AWS KMS), and observability platforms (Datadog, PagerDuty).
- **Corporate Functions:** Human Resources, Finance, Legal, and Compliance processes, including those directly governed by this SOP.
- **Third-Party and Vendor Risk:** Controls governing due diligence, ongoing monitoring, and offboarding of vendors that process Meridian data, especially Business Associates under the Health Insurance Portability and Accountability Act (HIPAA) and Processors under the General Data Protection Regulation (GDPR).

The scope covers all Meridian entities, including subsidiaries, and applies to all Meridian systems, data centers (on-premises or cloud), and SaaS applications that process, store, or transmit Meridian data. The program covers financial, operational, regulatory compliance, and information technology general controls (ITGCs) audits.

## 2. Definitions and Acronyms

The following definitions apply to this SOP and all Meridian internal audit activities:

| Term / Acronym | Definition |
| :--- | :--- |
| **Audit Universe** | A comprehensive catalog of all auditable units within Meridian, including business processes, legal entities, applications, infrastructure components, and compliance frameworks. The Audit Universe is the foundation for risk-based planning. |
| **AWARF** | Audit Workpaper Archival and Retention Form. The standardized form used to catalogue, reference, and archive all audit evidence according to the record retention schedule. |
| **BCP/DR** | Business Continuity Plan / Disaster Recovery. |
| **Business Associate Agreement (BAA)** | A legal contract between a HIPAA-covered entity and a business associate that establishes the permitted uses and disclosures of PHI by the business associate. |
| **CAT** | Control Assessment Template. The standardized working paper used to document the walkthrough, test of design, and test of operating effectiveness for a single control. |
| **CCO** | Chief Compliance Officer. The owner of this SOP, responsible for overseeing the independence and performance of the internal audit function. |
| **CISO** | Chief Information Security Officer. |
| **Conformity Assessment Body (CAB)** | An external organization accredited to perform certification audits, such as ISO 27001 or SOC 2. The Meridian Internal Audit Program audits the organization’s readiness for, and adherence to, standards set by CABs. |
| **Data Controller (GDPR)** | The natural or legal person, public authority, agency, or other body which, alone or jointly with others, determines the purposes and means of the processing of personal data. Meridian is the Data Controller for its HR and clinical trial data. |
| **Data Processor (GDPR)** | A natural or legal person, public authority, agency, or other body which processes personal data on behalf of the controller. Meridian’s cloud hosting providers and SaaS vendors are typically data processors. |
| **DPIA** | Data Protection Impact Assessment, as required by **GDPR Article 35** for processing, using new technologies, that is likely to result in a high risk to the rights and freedoms of natural persons. |
| **ePHI** | Electronic Protected Health Information, as defined by the HIPAA Security Rule (45 CFR Parts 160 and 164). |
| **Finding** | A formal output of an audit engagement identifying a control deficiency. Findings are rated by severity. |
| **GC** | General Counsel. The approver of this SOP and head of the legal department. |
| **GDPR** | General Data Protection Regulation (EU) 2016/679. |
| **HIPAA** | Health Insurance Portability and Accountability Act of 1996 and its implementing regulations, including the Privacy Rule, Security Rule, and Breach Notification Rule. |
| **IIA** | The Institute of Internal Auditors. Meridian’s internal audit methodology adheres to the International Standards for the Professional Practice of Internal Auditing (the IIA Standards). |
| **IPPF** | International Professional Practices Framework, promulgated by the IIA. |
| **ISMS** | Information Security Management System. |
| **LOIS** | Loan Origination and Information System. Meridian’s core banking platform for HealthPay Financial Services. |
| **PRAC** | Policy Review and Approval Committee. The governance body responsible for approving all Meridian policies. |
| **RACI** | A responsibility assignment matrix (Responsible, Accountable, Consulted, Informed). |
| **RCM** | Risk and Control Matrix. The primary planning document for a specific audit engagement, linking risks to controls and defining the testing strategy. |
| **SAR** | Subject Access Request, as defined by **GDPR Article 15** (Right of access by the data subject). |
| **SR 11-7** | Federal Reserve Supervision and Regulation Letter 11-7, "Guidance on Model Risk Management." |
| **UBW** | Ultimate Beneficial Owner. |

## 3. Roles and Responsibilities

The following RACI matrix defines the roles and responsibilities for the lifecycle of the Internal Audit Program:

| Activity / Task | Chief Compliance Officer (CCO) | VP, Internal Audit | Audit Engagement Lead | Process Owner (Auditee) | Executive Leadership Team | GC / CISO | Audit Committee |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Audit Charter & Plan Approval** | A | R | C | I | C | C | R, A |
| **Risk-Based Audit Planning** | C | A, R | R | C | I | C | C |
| **Audit Engagement Kickoff** | I | A | R | C | I | I | I |
| **Control Walkthrough & Design Assessment** | I | A | R | C, R | I | I | I |
| **Execution of Testing Procedures** | I | A, C | R | I | - | I | - |
| **Drafting Finding and Report** | C | A, R | R | I | - | I | - |
| **Management Action Plan (MAP) Development** | I | A, C | C | R | I | I | I |
| **MAP Implementation and Closure** | I | A | R | I | I | C | I |
| **Approval of Critical (Level 1) Exceptions** | C | R | - | I | A | C | R |
| **Quarterly Audit Status Reporting** | A, R | C, R | R | I | I | I | I, A |

**Specific Named Roles:**

- **Thomas Anderson, Chief Compliance Officer (CCO):** The Owner of this SOP. Responsible for the administrative oversight of the program, ensuring the independence of the internal audit function, reviewing and approving the annual risk assessment methodology, and acting as the primary executive liaison for regulatory examiners.
- **VP, Internal Audit:** Reports functionally to the Audit Committee of the Board of Directors and administratively to the CCO. Responsible for managing the day-to-day operations of the Internal Audit Program, including developing the audit universe, executing the risk-based audit plan, maintaining quality assurance and improvement program (QAIP) conformance, and supervising all audit staff.
- **Audit Engagement Lead:** An internal audit staff member assigned to lead a specific engagement. Responsible for all phases of the engagement, from detailed risk and control matrix creation through report issuance and finding follow-up.
- **Process Owner (Auditee):** The Meridian senior manager or director directly responsible for the auditable unit. For example, the VP of Engineering is the Process Owner for the Clinical AI Platform’s model development lifecycle. Process Owners are responsible for providing evidence, developing Management Action Plans (MAPs), and implementing corrective actions.
- **Maria Gonzalez, General Counsel (GC):** The Approver of this SOP. Acts as the highest escalation point for legal issues identified during audits, particularly those involving regulatory non-compliance (e.g., GDPR data subject rights violations, HIPAA breach notification concerns).

## 4. Policy Statements

1.  **Independence and Objectivity:** The Internal Audit function shall maintain organizational independence and individual objectivity. The VP, Internal Audit, reports functionally to the Audit Committee of the Board of Directors to ensure such independence. Internal auditors shall not have direct operational responsibility or authority over any of the activities they audit.
2.  **Standards Conformance:** The Internal Audit Program shall be designed and operated in general conformance with the mandatory elements of the Institute of Internal Auditors (IIA) International Professional Practices Framework (IPPF), including the Core Principles for the Professional Practice of Internal Auditing, the Definition of Internal Auditing, the Code of Ethics, and the International Standards for the Professional Practice of Internal Auditing.
3.  **Risk-Based Approach:** Audit resources shall be allocated using a formal, documented risk-based planning methodology that assesses inherent risk across the entire Meridian Audit Universe, considering strategic, operational, financial, and compliance risk dimensions. The annual audit plan shall be presented to the Audit Committee for review and approval by December 15th of the preceding fiscal year.
4.  **Continuous Risk Assessment:** The Audit Universe shall be a living document, reviewed and updated quarterly by the VP, Internal Audit, to reflect changes in Meridian’s business profile, emerging threats, new regulatory requirements, and results of recent audit and risk assessments.
5.  **Data Protection Compliance (GDPR & HIPAA):** Every engagement plan shall explicitly include objectives and tests designed to verify compliance with:
    - **HIPAA Privacy Rule (45 CFR Part 164, Subpart E):** Controls related to PHI use and disclosure, verification requirements (§164.514(h)), Minimum Necessary Standard, and rights of individuals (e.g., Right to Access PHI at §164.524).
    - **HIPAA Security Rule (45 CFR Part 164, Subpart C):** Administrative, physical, and technical safeguards for ePHI. This includes, but is not limited to, Risk Analysis (§164.308(a)(1)(ii)(A)), Risk Management (§164.308(a)(1)(ii)(B)), Access Controls (§164.312(a)(1)), Audit Controls (§164.312(b)), Integrity Controls (§164.312(c)(1)), and Transmission Security (§164.312(e)(1)).
    - **HIPAA Breach Notification Rule (45 CFR Part 164, Subpart D):** The detection, investigation, and notification procedures for a Breach of Unsecured PHI.
    - **GDPR Core Principles (Article 5):** The processing of personal data shall be lawful, fair, and transparent during the audit.
    - **GDPR Data Subject Rights (Articles 15-22):** The operational procedures and technical mechanisms supporting a data subject's right to access, rectification, erasure ("Right to be Forgotten"), restriction of processing, data portability, and objection.
    - **GDPR Controller and Processor Obligations (Articles 24-28):** Verifying adherence to data protection-by-design and default, and the presence of appropriate technical and organizational measures at any third-party data processor.
6.  **Audit Evidence and Workpapers:** All findings and conclusions must be supported by sufficient, reliable, relevant, and useful evidence. Standard audit workpapers shall be completed for every stage of the engagement, including Engagement Planning Memo, Risk and Control Matrix (RCM), Control Assessment Template (CAT), and a Finding Summary Sheet. All workpapers must be reviewed and approved by the VP, Internal Audit, or their designee, independent of the engagement lead, within 10 business days of the evidence collection date.
7.  **Confidentiality and Data Minimization:** Audit personnel shall collect and process the minimum necessary personal data to achieve a specific audit objective. All audit data extracted from production systems shall be stored in a dedicated, encrypted audit repository on the Meridian SharePoint platform with access granted on a strict "need-to-know" basis managed by IAM role `GRP-INTL-AUD-RO`.

## 5. Detailed Procedures

### 5.1 Maintaining the Audit Universe and Conducting the Risk Assessment

This procedure formalizes the annual and quarterly updates to the Audit Universe to drive the risk-based audit plan.

1.  **Catalog Auditable Entities:** The VP, Internal Audit, maintains the master "Meridian Audit Universe Register" (Template: `FRM-LEGC-003-AU`) in the GRC platform (Vanta). Entities are identified through:
    - Organizational charts (all VPs and above).
    - Financial Statements (significant account balances).
    - IT Asset Inventory and CMDB (applications, databases, OS, networks).
    - Regulatory Compliance Register maintained by Legal & Compliance.
    - Centralized Risk Register (See SOP-RISK-001).
2.  **Define Risk Factors and Weightings:** The VP, Internal Audit, and CCO annually review and propose to the Audit Committee a set of standardized risk scoring factors. These shall include:
    - **Strategic Impact (Weight: 25%):** Alignment with Meridian’s top 3 strategic initiatives.
    - **Operational Criticality (Weight: 20%):** Business process tier (Tier 1-4) from BCP/DR classification.
    - **Financial Materiality (Weight: 20%):** Revenue flow, asset value, or expense base.
    - **Regulatory & Legal Exposure (Weight: 25%):** The maximum potential fine or sanction from non-compliance (e.g., GDPR fine risk up to 4% annual global turnover, HIPAA civil money penalties).
    - **Information Sensitivity (Weight: 10%):** Concentration of regulated data (e.g., ePHI records, GDPR-covered data element counts).
3.  **Annual Entity Scoring:** Between October 1st and November 15th, the Audit Engagement Leads, under the direction of the VP, Internal Audit, shall score each auditable entity in the register using the approved risk factors. Each factor is scored on a 1-5 scale (1=Low, 5=Critical). The total risk score is the weighted sum of individual factor scores.
4.  **Formulate Draft Plan:** Entities are ranked by their total risk score. The draft annual audit plan must schedule engagements based on a clear threshold:
    - **High-Risk Entities (Score > 4.0):** Must be audited at least once per fiscal year.
    - **Medium-Risk Entities (Score 2.5 - 4.0):** Must be audited at least once every 24 months.
    - **Low-Risk Entities (Score < 2.5):** May be audited on a rotational basis, not to exceed a 36-month cycle, or assessed via continuous monitoring.
5.  **Plan Approval:** The VP, Internal Audit, presents the risk-scored register, draft plan, and resource budget to the Audit Committee for review and approval by December 15th.

### 5.2 The Audit Engagement Lifecycle

Every audit engagement, from planning to follow-up, follows this standard lifecycle.

#### 5.2.1 Planning and Kickoff

1.  **Risk and Control Matrix (RCM):** The Audit Engagement Lead creates an RCM (`FRM-LEGC-003-RCM`) specific to the auditable entity. The RCM identifies process-level risks and maps them to relevant controls from Meridian’s central control framework (see SOP-ISMS-002) and external regulations.
2.  **Engagement-Specific Data Scoping Memo (GDPR Articles 5, 6, 14 & HIPAA Minimum Necessary):** A mandatory memo must be drafted and approved by the Office of the Data Protection Officer (DPO) and Associate General Counsel (Privacy) before any data extraction.
    - It must list the precise data categories required from production systems.
    - It must articulate the lawful basis for processing this data for the audit engagement, categorized as processing necessary for compliance with a legal obligation under **GDPR Article 6(1)(c)**.
    - It must document the justification for access to any ePHI, explicitly stating why a de-identified or limited data set cannot fulfill the audit objective, in compliance with the HIPAA Minimum Necessary Standard at §164.514(d)(3)(iii). Access to the full dataset, including Direct Identifiers, requires justification signed off by the CCO.
3.  **Entrance Meeting:** The Audit Engagement Lead conducts a formal entrance meeting with the Process Owner and key stakeholders. Agenda includes: scope, objectives, timelines, required resources, key control owners, and communication protocol.

#### 5.2.2 Fieldwork and Testing

1.  **Control Walkthrough and Test of Design (ToD):** The auditor performs a walkthrough for each control listed in the RCM by tracing a single transaction from initiation through processing to recording. The Control Assessment Template (CAT) is used to document: the control objective, control description, frequency (Real-time, Daily, Weekly, Monthly, Annual), the responsible role, and the system/tool used. The Lead Auditor assesses if the control, as designed, would prevent or detect a material error or regulatory non-compliance risk.
2.  **Test of Operating Effectiveness (ToE):** Upon satisfactory completion of the ToD, the auditor executes the test plan detailed in the CAT. This involves:
    - **Sampling:** Using structured, non-statistical or statistical sampling methods. Sample sizes are based on control frequency (e.g., for weekly controls, >=5 items; for monthly, >=3 items) and must be justified in the CAT.
    - **Inquiry and Observation:** Supplemental evidence gathering.
    - **Re-performance:** The strongest form of evidence, where the auditor independently replicates the control activity.
3.  **Fieldwork Status Tracking:** All audit findings must be logged in the "Audit Findings Module" of Vanta within 24 hours of identification. Daily stand-ups are held with the audit team to track progress.

#### 5.2.3 Reporting

1.  **Draft Report and Findings Discussion:** A findings list is prepared and presented to the Process Owner before the exit meeting. Findings are classified per Section 5.4.
2.  **Exit Meeting:** The auditor presents the overall assessment, each finding, its rating, and requests Management Action Plans (MAPs) from the Process Owner. Any factual disagreement is resolved at this stage.
3.  **Final Report Issuance:** The final report is issued within 10 business days of the exit meeting. It includes the overall rating and an Appendix with the full findings log and agreed MAPs.

#### 5.2.4 Management Action Plan (MAP) Follow-Up

1.  **MAP Commitment:** Process Owners must document a MAP in Vanta for each finding. The MAP includes: a detailed corrective action, a named Responsible Officer, and a committed closure date.
2.  **Closure Verification:** On or before the committed closure date, the Process Owner submits evidence of completion (e.g., new policy, updated system configuration screenshots, training records). The original Audit Engagement Lead reviews the evidence and, if sufficient, re-tests the remediated control. A finding is formally "Closed" in Vanta only after successful re-testing or validation.
3.  **Overdue MAP Escalation:** Any finding with a MAP overdue by more than 30 days is automatically escalated to the CCO and the relevant Executive Leadership Team member. Overdue by 60 days is escalated to the Chair of the Audit Committee.

### 5.3 Specific High-Risk Procedure: Joint-Audit of a Business Associate (HIPAA & GDPR)

This procedure applies when Meridian must audit a third-party vendor that acts as both a HIPAA Business Associate (BA) and a GDPR Data Processor.

1.  **Trigger:** A joint-audit is triggered when a vendor processes both designated "high-risk" ePHI data sets and GDPR-covered personal data for a primary EU-facing Meridian service.
2.  **Pre-Audit Review:** The auditor reviews the vendor's HIPAA Business Associate Agreement (BAA) and GDPR Data Processing Agreement (DPA) (See **GDPR Article 28(3)**), specifically mapping required technical and organizational measures (TOMs) from the DPA to the audit program.
3.  **Hybrid Testing Program:** The audit program must integrate:
    - **HIPAA Security Rule:** Validation of BAA-required ePHI safeguards, including encryption at rest/transit, access controls, and audit log integrity.
    - **GDPR Article 28 Processor Obligations:** Verification that the processor (a) acts only on documented instructions from Meridian; (b) ensures staff confidentiality; (c) implements appropriate security per **Article 32**; and (d) adheres to sub-processor rules per **Article 28(2) and (4)**.
4.  **Data Transfer Mechanism Validation:** For any data flows involving a transfer of personal data from the EEA to a third country (e.g., US-based vendor), the auditor validates the existence and effectiveness of the specific transfer mechanism referenced in the DPA. For a vendor relying on Standard Contractual Clauses (SCCs), the auditor verifies the vendor’s documented technical measures to uphold the "essentially equivalent" data protection standard, particularly regarding US government access requests.
5.  **Reporting:** A single report with a joint findings section is produced. A finding of non-compliance with **GDPR Article 28(3)** (failure to adhere to the DPA) is automatically categorized as a Critical Finding for the owning Meridian business unit.

### 5.4 Finding Severity Ratings and Required Response Times

All control exceptions are classified into the following standardized taxonomy. The Process Owner is held to the stated response time for the initial MAP.

| Severity | Rating ID | Criteria | Example | Initial MAP Response Time |
| :--- | :--- | :--- | :--- | :--- |
| **Critical / Level 1** | FIND-1 | A systemic control failure that has resulted in, or has a high probability of resulting in, significant financial loss, major regulatory action (e.g., GDPR fine, HIPAA violation), or severe reputational damage. Indicative of pervasive root cause. | Unencrypted ePHI found on a publicly accessible S3 bucket due to systemic security group misconfiguration; evidence that Data Protection-by-Design under GDPR Art. 25 was never considered. | 5 Business Days |
| **Major / Level 2** | FIND-2 | An internal control weakness that could lead to a material misstatement in financials or a reportable non-compliance event if not corrected. A breakdown in a process-level, but not systemic, control. | A single instance where the HIPAA 60-day Breach Notification deadline was missed by 5 days due to a flawed, but now-corrected, runbook. | 15 Business Days |
| **Minor / Level 3** | FIND-3 | A control is designed and operating effectively but is not fully documented, or a low-risk deviation from policy was observed. No immediate risk of material misstatement or non-compliance. | A data processing activity found operating without a current official Data Protection Impact Assessment (DPIA) record on file, though all technical controls are in place (relates to GDPR Art. 35 record-keeping). | 30 Business Days |
| **Observation / Level 4** | FIND-4 | A non-mandatory suggestion for process improvement or efficiency enhancement. No control deficiency exists. | A recommendation to automate a manual, but fully-compliant, data subject access request (DSAR) tracking spreadsheet for GDPR Art. 15. | Next Fiscal Year's Plan |

## 6. Controls and Safeguards

### 6.1 Administrative Controls

| Control ID | Control Description | Control Purpose / Risk Mitigated |
| :--- | :--- | :--- |
| **ADM-LEGC-003-01** | The Audit Committee Charter formally defines Independence and Authority. An annual self-assessment of independence is filed by the VP, Internal Audit. | Mitigates the risk that audit function independence is compromised by executive pressure or conflicts of interest. (IIA Standard 1100) |
| **ADM-LEGC-003-02** | A formal Quality Assurance and Improvement Program (QAIP) exists, requiring an internal review of at least 1 engagement per quarter against IIA Standard checklists. An external quality assessment must be performed at least once every five years. | Ensures consistency and adherence to professional standards across all engagements. (IIA Standard 1300) |
| **ADM-LEGC-003-03** | All audit staff and consultants must sign a Confidentiality Agreement addendum specific to the audit function, binding them to the highest level of data privacy, acknowledging the criminal penalties for unauthorized ePHI access and GDPR violations. | Deters unauthorized disclosure of sensitive corporate and personal data obtained during audits. |
| **ADM-LEGC-003-04** | Mandatory annual joint-design and operating effectiveness assessment for controls related to **GDPR Art. 32 (Security of Processing)** and **HIPAA §164.312 (Technical Safeguards)**. | Provides a holistic, integrated assurance over the foundational security controls that protect both HIPAA and GDPR-regulated data. |

### 6.2 Technical Controls for the Audit Environment

| Control ID | Control Description | Relevant System/Tool |
| :--- | :--- | :--- |
| **TECH-LEGC-003-01** | The centralized audit evidence repository (`GRC-SharePoint-Audit-R0`) enforces role-based access controls (RBAC) using IAM group `GRP-INTL-AUD-RO`. Data is encrypted at rest with Microsoft-managed keys. Access is logged and reviewed quarterly. | Meridian SharePoint Online, Okta, Microsoft Purview |
| **TECH-LEGC-003-02** | Any extraction of data from production systems (e.g., MedInsight data warehouse, LOIS core banking) for audit ETL must be performed via a dedicated, read-only API key or service account, with the password rotated immediately upon extraction completion. Bulk manual SQL queries on production are prohibited. | AWS Secrets Manager, Informatica, Custom ETL scripts |
| **TECH-LEGC-003-03** | To uphold the **GDPR Art. 32** and **HIPAA** standard of pseudonymization, auditors must always first use Meridian’s in-house De-Identification Service (`de-id.internal.meridian.tech`) before manual analysis. The re-identification key must be stored separately by the DPO. | Meridian HDM De-identification Pipeline |
| **TECH-LEGC-003-04** | An immutable audit log of all access, queries, and data extractions by audit personnel is created and mirrored to a central SIEM (Sumo Logic). The CISO's office has read-only access to this log for independent oversight. | Sumo Logic, AWS CloudTrail |

## 7. Monitoring, Metrics, and Reporting

### 7.1 Program Key Performance Indicators (KPIs)

The effectiveness of the Internal Audit Program is measured and reported quarterly to the Audit Committee and the CCO.

| Metric (KPI) | Calculation | Target / SLA | Reporting Tool |
| :--- | :--- | :--- | :--- |
| **Plan Completion Rate** | (# of Engagements Completed per SOP vs. Final Audit Plan) / (Total # of Planned Engagements) | >= 90% per fiscal year | Vanta GRC |
| **On-Time Report Issuance** | (Reports Issued Within 10 Business Days of Exit Meeting) / (Total Reports Issued) | >= 95% | Jira (Audit Project) |
| **MAP Closure Timeliness — Level 1 Findings** | (Level 1 Findings Closed by Committed Date) / (Total Level 1 Findings Closed) | 100% on time | Vanta Findings Module |
| **MAP Closure Timeliness — Level 2 & 3 Findings** | (Level 2 & 3 Findings Closed by Committed Date) / (Total Closed in Period) | >= 90% on time | Vanta Findings Module |
| **Overdue Remediation Escalation Efficiency** | (Overdue MAPs Escalated to CCO within 3 Bus. Days of Breach) / (Total Overdue MAPs) | 100% met | Vanta, Jira |
| **QAIP Conformance Score** | Quarterly internal review of 1 closed engagement against IIA Standard Checklist. Score out of 100. | Average Score >= 85 | QAIP Review Tool |

### 7.2 Reporting Cadence

- **Monthly (VP, Internal Audit):** A one-page "Audit Flash Report" is sent to the CCO and GC. It includes: status of all open MAPs, any overdue items, and a critical issues watch list.
- **Quarterly (CCO to Audit Committee and Board):** A formal "Quarterly Internal Audit Status and Performance Report" is presented. It includes:
    - A dashboard of the KPIs in section 7.1.
    - A "Top 10 Risks" heat map based on current audit findings.
    - Detailed status of all Critical (FIND-1) findings and their MAPs.
    - Updates to the Audit Universe risk assessment.
- **Annual (Audit Committee):** A comprehensive "Annual Report on the State of Internal Controls," summarizing all engagements, trends in findings, and the final risk ranking of the Audit Universe to support the upcoming year's planning cycle.

## 8. Exception Handling and Escalation

### 8.1 Policy Exception Requests

Any deviation from the specific procedures detailed in this SOP (e.g., a Process Owner refusing to provide a dataset scoped in the approved DPA, a request to delay an entrance meeting by more than two weeks) requires a formal Exception Request.

1.  **Initiation:** The Process Owner submits a request via the "Policy Exception" workflow in ServiceNow, referencing `SOP-LEGC-003`. The request must articulate the specific section, the exact business justification for the deviation, compensating controls, and a timeframe.
2.  **Impact Assessment:** The Audit Engagement Lead prepares an impact assessment ("Risk of Foregoing Control/Procedure") within 5 business days.
3.  **Approval Authority:**
    - **Minor Exceptions (Low risk, < 30 days):** VP, Internal Audit.
    - **Moderate Exceptions (Med risk, 30-90 days):** VP, Internal Audit and CCO.
    - **Critical Exceptions (High risk or > 90 days):** Must be approved by the GC, with notation to the Audit Committee.

### 8.2 Escalation for Unresolved Disagreements

If a Process Owner disputes a Finding Severity or a MAP deadline commitment, and the issue is not resolved at the VP, Internal Audit level within 5 business days:

1.  The matter is formally documented in a "Dispute Resolution Memo," stating facts and positions, authored by the VP, Internal Audit.
2.  The Memo is presented to the CCO and the Process Owner’s Executive Leader.
3.  If unresolved, the final arbiter is the Chair of the Audit Committee. For disputes involving an interpretation of GDPR or HIPAA statutory mandates, the CCO temporarily pauses the escalation and the GC solicits an independent legal opinion that shall be binding.

## 9. Training Requirements

All personnel with assigned roles in the RACI (Section 3) must complete mandatory, role-based training.

| Training Module Title | Delivery Platform | Audience | Frequency | Completion Tracking |
| :--- | :--- | :--- | :--- | :--- |
| **Internal Auditor IIA Standards and Ethics** | Meridian LMS (Workday) | VP, Internal Audit; Audit Engagement Leads; Staff Auditors | Annually | LMS with 100% required pass rate on post-assessment |
| **Data Protection for Auditors: HIPAA & GDPR Practical Application** | Instructor-Led by DPO & Privacy Counsel | All Internal Audit personnel | Annually | Instructor sign-off sheet; attendance recorded in Workday |
| **Vanta GRC for Audit Management** | Meridian Tech University (Workday) | VP, Internal Audit; Audit Engagement Leads | Upon Role Change or System Update | LMS Completion Status |
| **Fraud Awareness & Professional Skepticism** | Meridian LMS (Workday) | All Internal Audit personnel | Annually | LMS Completion Status |
| **GDPR Art. 15, 17, 18 Procedure for Auditees** | Meridian LMS (Workday) | All People Managers and above | Upon hire, annually | LMS Completion Status. *Purpose: Ensure Process Owners understand data rights when auditors request data from their systems.* |

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

- **SOP-RISK-001:** Enterprise Risk Management Framework
- **SOP-ISMS-002:** Information Security Management System (ISMS) — Core Controls
- **SOP-PRIV-001:** Global Data Protection and Privacy Policy
- **SOP-PRIV-005:** HIPAA Privacy Rule Compliance — Use and Disclosure of PHI
- **SOP-PRIV-007:** General Data Protection Regulation (GDPR) — Procedure for Data Subject Requests
- **SOP-PRIV-010:** Third-Party Risk Management (TPRM)
- **SOP-ENG-CLIN-004:** Clinical AI Model Development and Validation Lifecycle
- **SOP-HR-002:** Code of Conduct and Whistleblower Policy

### 10.2 External Standards and Regulatory References

- Institute of Internal Auditors (IIA): International Standards for the Professional Practice of Internal Auditing
- General Data Protection Regulation (EU) 2016/679, specifically Article 5 (Principles), Art. 25 (Data Protection by Design), Art. 28 (Processor), Art. 32 (Security), and Art. 35 (DPIA).
- Health Insurance Portability and Accountability Act (HIPAA) of 1996, specifically Security Rule (45 CFR §164.308, §164.310, §164.312), Privacy Rule (45 CFR §164.502, §164.514), and Breach Notification Rule (45 CFR §164.400-414).

## 11. Revision History

| Version | Date | Author | Approved By | Summary of Changes |
| :--- | :--- | :--- | :--- | :--- |
| 4.0 | 2025-05-12 | T. Anderson, CCO | M. Gonzalez, GC | Major revision: Added joint-audit procedure for HIPAA/GDPR (Section 5.3); moved audit reporting cadence from SOP-EXEC-001; incorporated changes from 2025 IIA Standards update. |
| 4.1 | 2025-09-08 | J. Reeves, VP Internal Audit | T. Anderson, CCO | Refined Finding Severity taxonomy (Section 5.4) to align with Vanta module config; added precise timeline for overdue MAP escalation; introduced Technical Controls section (6.2) for audit environment. |
| 4.2 | 2026-04-22 | T. Anderson, CCO | M. Gonzalez, GC | Updated RACI to reflect new VP, IT role; added clarification on Minimum Necessary standard per guidance from DPO on 2026-03-17; minor formatting updates. |
| 4.3 | 2026-07-19 | J. Reeves, VP Internal Audit | T. Anderson, CCO | Updated Training Requirements (Section 9) to mandate annual data protection training; clarified the definition of "Critical" findings to include systemic GDPR Art. 28 processor failures; updated related policy cross-references. |
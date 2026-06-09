---
sop_id: "SOP-FIN-016"
title: "Financial Reporting and Disclosure"
business_unit: "Financial Services"
version: "4.0"
effective_date: "2025-01-23"
last_reviewed: "2026-10-01"
next_review: "2027-04-21"
owner: "Robert Liu, VP of Financial Services"
approver: "James Thornton, Chief Financial Officer"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Financial Reporting and Disclosure

## 1. Purpose and Scope

### 1.1 Purpose

The purpose of this Standard Operating Procedure (SOP) is to establish a formal, controlled, and auditable framework for the preparation, review, approval, disclosure, and retention of financial reports within Meridian Health Technologies, Inc. ("Meridian" or the "Company"). This SOP is designed to ensure the accuracy, completeness, timeliness, and integrity of all financial reporting, thereby supporting the Company's commitment to transparency, regulatory compliance, and operational excellence. Specifically, this SOP operationalizes Meridian's obligations under the Trust Services Criteria (TSC) for SOC 2, particularly the criteria related to the accuracy, completeness, and timeliness of system outputs (P1.1, P1.2, P1.3).

### 1.2 Scope

This SOP applies to all financial reports generated, processed, or disseminated by the **Financial Services** business unit, encompassing the **HealthPay Financial Services** platform and related operational financial functions. The scope includes, but is not limited to:

- **Internal Financial Reports:** Operational dashboards, transaction volume reports, revenue leakage analyses, model risk performance scorecards, and management review packages.
- **External Financial Reports:** Client-facing settlement reports, billing statements, 1099-K tax form generation, partner bank reconciliation statements, and data submissions for annual SOC 2 Type II audits.
- **Regulatory and Compliance Reports:** Reports required under SR 11-7 model risk management, state money transmitter licensing requirements, and specific disclosures to the Board-level AI Governance Committee regarding financial model performance.
- **Systems:** All data originating from the HealthPay platform, AWS (us-east-1, eu-west-1) S3 data lakes, Snowflake financial data warehouse, and any downstream analytics tools used for report generation.

### 1.3 Applicability

This SOP is binding on all Meridian employees, contractors, and third-party service providers who are involved in the lifecycle of financial data, including its capture, aggregation, analysis, report creation, approval, distribution, and archival. Adherence is mandatory, and non-compliance is subject to disciplinary action as outlined in the Meridian Employee Handbook.

## 2. Definitions and Acronyms

| Term | Definition |
| :--- | :--- |
| **ACH** | Automated Clearing House, an electronic network for financial transactions in the U.S. |
| **BAS** | Business Activity Summary, a daily aggregated report of financial transactions. |
| **CFO** | Chief Financial Officer |
| **CISO** | Chief Information Security Officer |
| **Control Owner** | The individual designated as accountable for the design and operating effectiveness of a specific control activity. |
| **DDP** | Daily Discrepancy Percentage, a KPI measuring daily unreconciled transactions. |
| **Disclosure Committee** | A cross-functional committee responsible for reviewing and approving external financial disclosures. |
| **EFT** | Electronic Funds Transfer. |
| **EOD** | End of Day, typically defined as 23:59 UTC for global operations. |
| **FTP** | File Transfer Protocol; Meridian exclusively uses SFTP (Secure FTP). |
| **GAAP** | Generally Accepted Accounting Principles (U.S.). |
| **KRI** | Key Risk Indicator. |
| **KPI** | Key Performance Indicator. |
| **PCI DSS** | Payment Card Industry Data Security Standard. |
| **PHI/PII** | Protected Health Information / Personally Identifiable Information. |
| **RACM** | Risk and Control Matrix. |
| **Reconciliation** | The process of comparing two sets of records to ensure figures are accurate and in agreement. |
| **SOC 2** | Service Organization Control 2, an auditing standard focused on security, availability, processing integrity, confidentiality, and privacy. |
| **SR 11-7** | Federal Reserve guidance on Model Risk Management. |
| **TSC** | Trust Services Criteria, the control criteria used in a SOC 2 examination. |
| **WIP** | Work In Progress, a preliminary version of a report undergoing drafting and review. |

## 3. Roles and Responsibilities

The following responsibility assignment matrix (RACI) defines the roles and duties for the financial reporting lifecycle. (R=Responsible, A=Accountable, C=Consulted, I=Informed).

| Activity / Task | VP, Fin. Services (Robert Liu) | CFO (James Thornton) | Finance Operations Manager | Data Engineering Lead | CISO (Rachel Kim) | Compliance Officer (Thomas Anderson) | External Auditors |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Financial Reporting Process Design** | A | C | R | C | C | C | I |
| **Internal Report Generation** | I | I | R | C | I | I | I |
| **External Report Generation** | A | I | R | C | C | C | I |
| **Control Performance & Evidence** | I | I | R | R | C | C | I |
| **SOC 2 P1.2 (Completeness)** | I | A | R | C | I | I | I |
| **SOC 2 P1.3 (Timeliness)** | A | I | R | R | I | I | I |
| **Report Accuracy Review** | R | A | R | R | I | I | I |
| **System Access Reviews** | I | I | I | R | A | I | I |
| **Exception Approval** | R | A | I | I | I | R | I |
| **Model Risk Reporting (SR 11-7)** | R | A | I | C | I | I | I |
| **Disclosure Committee Approval** | R | A | C | I | I | R | I |

### 3.1 Key Responsibilities Defined

- **VP of Financial Services (Robert Liu):** Ultimate process owner. Accountable for the design, implementation, and continuous improvement of this SOP. Responsible for approving exceptions and signing off on all external financial reports before submission.
- **Chief Financial Officer (James Thornton):** Final approver for all external financial disclosures and audit reports. Chairs the Disclosure Committee. Accountable for the integrity of financial information at the entity level.
- **Finance Operations Manager:** Responsible for the day-to-day execution of report generation, initial quality assurance review, control execution, and evidence preservation.
- **Data Engineering Lead:** Responsible for ensuring the technical infrastructure for data extraction, transformation, and loading (ETL) processes is operational, accurate, and properly configured. Consults on the remediation of data quality issues.
- **Chief Information Security Officer (Rachel Kim):** Accountable for the logical and physical security controls over financial data, including access management, encryption, and network security, as it relates to report generation and distribution.
- **Chief Compliance Officer (Thomas Anderson):** Consults on regulatory requirements and provides independent oversight of the control environment. Reviews all external reports for regulatory compliance prior to Disclosure Committee submission.
- **External Auditors:** Provide an independent and objective assessment of the design and operating effectiveness of the controls described in this SOP as part of the annual SOC 2 Type II audit.

## 4. Policy Statements

Meridian Health Technologies, Inc. is committed to the highest standards of financial integrity and transparency. The following policy statements govern all financial reporting activities:

1.  **Accuracy and Completeness:** All financial reports shall be a true, accurate, and complete representation of the underlying transactions and events, prepared in accordance with U.S. GAAP and internal management reporting standards. Controls must be in place to prevent material omissions or errors, directly addressing SOC 2 TSC **P1.1** and **P1.2**.

2.  **Timeliness:** Financial reports shall be produced and delivered within predefined, published timelines to satisfy internal management needs, contractual client obligations, and regulatory deadlines, fulfilling SOC 2 TSC **P1.3**.

3.  **Standardization:** All reports will follow standardized templates, data definitions, and calculation methodologies as defined in the Meridian Financial Data Dictionary (maintained on the company Confluence instance) to ensure consistency and comparability over time.

4.  **Data Security and Confidentiality:** The creation, storage, and transmission of financial reports containing sensitive, confidential, or PII/PHI data shall adhere to all applicable security policies, including SOP-IS-030 (Data Classification and Handling). Such reports must be encrypted at rest (using AWS KMS-managed keys) and in transit (TLS 1.2 or higher).

5.  **Segregation of Duties (SoD):** No single individual shall have the ability to unilaterally create, approve, and distribute a material external financial report. The roles of Report Preparation, Report Review, and Report Approval must be performed by separate qualified individuals.

6.  **Retention and Disposal:** Financial reports and all supporting documentation shall be retained for a minimum of seven (7) years, or as dictated by the longest applicable regulatory or contractual requirement. Reports will be securely disposed of thereafter via an approved data destruction method as per SOP-IS-022 (Data Retention and Destruction).

7.  **Non-Retaliation:** Any employee who, in good faith, reports a suspected error, irregularity, or violation of this policy is protected under the Meridian Whistleblower Policy (SOP-LG-005).

## 5. Detailed Procedures

This section details the step-by-step operational procedures for the financial reporting lifecycle.

### 5.1 General Report Generation Workflow

The following workflow applies to all standard financial reports, both internal and external. Reports are classified as "Standard" if they are on a defined schedule.
Sub-section 5.2 details additional steps for External Reports only.

**Step 1: Data Extraction and Ingestion (Operated by: Data Engineering Team — Automated)**
1.1. The orchestration system (Apache Airflow) triggers the ETL pipelines for the HealthPay Financial Services data.
1.2. Transactional data is extracted from source databases (PostgreSQL on AWS RDS) and streamed in near real-time via Apache Kafka.
1.3. Data is landed in the raw zone of the Snowflake data warehouse (`FIN_RAW` database). An automated row count hash and checksum is generated to ensure ingestion fidelity.

**Step 2: Data Transformation and Aggregation (Operated by: Data Engineering Team — Automated)**
2.1. Scheduled `dbt` models execute against the raw data to perform cleaning, normalization, and business logic application (e.g., fee calculations, currency conversion using 4 PM London time spot rates for non-USD transactions).
2.2. Transformed data is written to the `FIN_ANALYTICS` schema in Snowflake.
2.3. The `dbt` run results, including test pass/fail statuses for data quality checks (uniqueness, not null, referential integrity), are logged and surfaced in a central Data Quality Dashboard in Datadog.

**Step 3: Report Generation (Operated by: Finance Operations Analyst)**
3.1. On the scheduled date and time, the Finance Operations Analyst accesses the Meridian Financial Reporting Portal (internal micro-frontend application).
3.2. The analyst selects the required report (e.g., Monthly Client Revenue Summary, Daily Settlement File) and confirms the target parameters (e.g., Client ID, Date Range, Partner Bank).
3.3. The application queries the `FIN_ANALYTICS` schema and renders the report in its pre-defined template.
3.4. A system-generated "Report Meta-Footer" is automatically appended to every page and includes:
    - Report ID (GUID)
    - Generation Timestamp (UTC)
    - Data As-of Timestamp (UTC)
    - Generating User ID
    - Source Schema Version

### 5.2 External Financial Report Workflow (Supplemental Steps)

For reports designated as "External" (i.e., destined for a client, partner bank, or regulator), Steps 4 through 9 below replace Step 4 from the general workflow.

**Step 4: First-Line Quality Assurance Review (Operated by: Finance Operations Manager)**
4.1. The Finance Operations Manager accesses the "WIP Reports" queue in the Reporting Portal.
4.2. The Manager performs a substantive analytical review, which includes:
    - Comparing key metrics (total volume, average transaction size, fee totals) against the prior reporting period (MoM and YoY variance analysis). Any variance > ±5% on a material metric must be annotated and explained.
    - Re-performing a manual calculation for a 5% random sample of transaction line items to verify fee accuracy.
    - Verifying the source data filter parameters are accurate for the intended recipient.
4.3. If the review passes, the Manager electronically signs the report in the system, which changes its status from "WIP" to "Peer Reviewed." If it fails, the Manager rejects the report, specifying reasons in a mandatory comment field, routing it back to the originating Analyst for correction.

**Step 5: Technical Integrity and Controls Verification (Operated by: Data Engineering Lead)**
5.1. For any external report with a materiality threshold defined by the CFO (currently set at a report representing >$500,000 in client funds flow), the Data Engineering Lead must provide a secondary confirmation.
5.2. The Lead validates that all `dbt` tests for the underlying data models passed with a 100% success rate. Any warnings or failures require documented remediation and sign-off by the Lead and VP before the report can proceed.
5.3. The Lead runs a row-by-row reconciliation script against a read-replica of the source transactional database, confirming the report balance matches the transactional total to a tolerance of <0.01%. A system "Integrity Verified" token is affixed to the report metadata.

**Step 6: Compliance Review (Operated by: Chief Compliance Officer)**
*(Applicable to all reports required for licensing, regulatory filing, or where directed by VP)*
6.1. The Chief Compliance Officer (or their delegate) is notified via ServiceNow to review the report. The notification includes a direct, read-only link to the report and its review trail.
6.2. The review focuses on adherence to regulatory (e.g., 31 CFR Chapter X for BSA/AML data formats if applicable) and contractual disclosure standards. The officer adds the "Compliance Approved" flag in the system, or rejects with a detailed non-conformance note.

**Step 7: Executive Approvals (Operated by: VP of Fin. Services / CFO)**
7.1. The system enforces a mandatory approval hierarchy:
    - Reports valued up to $1M or of "Internal Use" classification require approval by the **VP of Financial Services (Robert Liu)** .
    - All other external reports, SOC 2 audit packages, and SR 11-7 model performance disclosures require the approval of the **CFO (James Thornton)** .
7.2. The approver performs a final, holistic review of the report's narrative, the review trail, and any annotated variances. Approval is executed via single sign-on (SSO)-secured digital signature. Rejection forces the report back to "Draft" status.

**Step 8: Secure Distribution (Operated by: Finance Operations Manager)**
8.1. Upon final approval, Finance Operations initiates distribution via one of two secure channels, determined by the External Recipient Data Handling Matrix published by the CISO's office:
    - **Channel A (SFTP Push):** For high-volume settlement files (.csv, .txt) sent to partner banks and large payment clients. Files are PGP-encrypted with the recipient's public key before push to a dedicated, IP-restricted Meridian SFTP server.
    - **Channel B (Secure Portal):** For clients without SFTP capability. The report is published to the client's dedicated, read-only, authenticated portal view. An automated email notification is generated, which **must never contain the report or PHI/PII data**, informing the client's designated contact that a statement is available for download.

**Step 9: Archival (Automated)**
9.1. Upon successful distribution, a final, immutable copy of the report, along with its complete digital signature and review trail, is automatically archived by the system into the Meridian Records Management System (RMS) under a predefined retention policy code. The source WIP files are permanently purged after 90 days.

### 5.3 Manual Ad-Hoc Reporting Procedure

For any non-standard, ad-hoc report request, a formal ServiceNow Change Request (CRQ) must be logged. The workflow described in 5.1 and the controls in 5.2 apply proportionally. Before generation, the CRQ must be formally approved by the Finance Operations Manager, who will determine the appropriate review controls based on a tiered risk assessment of the data's intended use and audience.

## 6. Controls and Safeguards

This section details the specific technical and administrative controls mapped to the SOC 2 Trust Services Criteria. These controls are documented in the formal Risk and Control Matrix (RACM) maintained in ServiceNow GRC.

| Control ID | Control Description | SOC 2 TSC Mapping | Control Activity | Control Owner | Frequency | Evidence |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **FIN-P1.1-C01** | Automated data completeness checks prevent processing of incomplete transactions into the reporting warehouse. | P1.1, P1.2 | Ingestion pipeline validates row counts and checksums against source system logs. Pipeline halts on mismatch. | Data Engineering Lead | Per ETL run (Continuous) | Datadog log showing "Raw_Ingest_Check" status: PASS. |
| **FIN-P1.2-C02** | All manual adjusting journal entries to the `FIN_ANALYTICS` schema are subject to peer review. | P1.2 | A ServiceNow Task is auto-created for any direct SQL `UPDATE` on `FIN_ANALYTICS`. Task requires approval from Finance Operations Manager before execution. | VP of Financial Services | Auto-generated ServiceNow approval record linked to the SQL script execution. |
| **FIN-P1.1-C03** | Quarterly reconciliation of all HealthPay bank accounts against internal partner records. | P1.1 | Finance Operations Manager obtains bank statements directly from partner bank portals. A three-way match is performed (Bank Statement vs. Internal Ledger vs. Partner Settlement File). Discrepancies >$100 are documented and resolved. | Finance Operations Manager | Quarterly | Signed Reconciliation Summary document (QMR-{YYYY}-{Q#}), stored in RMS. |
| **FIN-P1.2-C04** | Standardized report templates include mandatory fields for completeness. | P1.2 | The Meridian Financial Reporting Portal enforces "Required" fields in each template schema. A report cannot be generated and routed for approval unless all fields are populated. | VP of Financial Services | Continuous | Report Generation Template Specification v4.0 (Confluence). |
| **FIN-P1.3-C05** | Timeliness of client settlement reports is tracked and measured. | P1.3 | A script monitors the SFTP/Portal distribution status against the contractual deadline (typically T+1 business day by 8:00 AM local recipient time). A live SLA dashboard tracks on-time delivery percentage. | Finance Operations Manager | Continuous / Daily | SLA Compliance Dashboard (Tableau). |
| **FIN-P1.3-C06** | 1099-K forms are processed and handed to the designated postal service provider. | P1.3 | An automated job confirms data hand-off to certified third-party processor (CFO agreed-upon) by Jan 15th annually. VP of Financial Services receives an automated confirmation email. | VP of Financial Services | Annual | Confirmation email from third-party processor. |
| **CC7.1-C07** | User access reviews for financial systems are performed. | CC6.1, CC6.3 | Data Engineering Lead runs an access review list for all privileged and user accounts on Snowflake `FIN_ANALYTICS` and the Reporting Portal. Finance Operations Manager certifies the access is appropriate. | CISO (Rachel Kim) | Quarterly | Signed User Access Review report. |
| **A1.2-C08** | Use of a Disclosure Committee for external financial communications. | A1.2, A1.3, C1.1 | The committee pre-reviews all significant external disclosures (e.g., material SOC 2 system description narratives, audited financial statements of the carve-out). Committee meetings are minuted. | CFO (James Thornton) | Per Disclosure Committee Charter |

### 6.1 Security Safeguards

- **Access Control:** Role-Based Access Control (RBAC) is enforced in Snowflake and the Reporting Portal via Okta SSO. Only members of the `FIN_OPS_ANALYST`, `FIN_OPS_MGR`, and `FIN_ENG` AD groups have access to the WIP environment. The distribution systems are segregated.
- **Encryption:** All data within the Snowflake `FIN_ANALYTICS` schema utilizes Transparent Data Encryption (TDE) with AWS KMS keys. Reports at rest on the SFTP server and in the RMS are encrypted. All data in transit is encrypted via TLS 1.2+.
- **Audit Trails:** All activities within the Reporting Portal and Snowflake are logged immutably. The complete digital signature chain (generation, review, approvals) forms a complete, non-repudiable audit trail for each external report.

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

These metrics are monitored continuously and formally reviewed at the monthly Finance Operations Review meeting chaired by Robert Liu.

| KPI | Definition | Target | Owner | Dashboard |
| :--- | :--- | :--- | :--- | :--- |
| **External Report On-Time Delivery (OTD)** | % of reports distributed on or before the contractual or SLA time. | **99.95%** | Finance Operations Manager | SLA Compliance Dashboard (Tableau) |
| **Daily Discrepancy Percentage (DDP)** | The number of unreconciled transactions / total daily transactions. | **< 0.01%** | Finance Operations Manager | HealthPay Reconciliation Dashboard (Grafana) |
| **First-Pass Yield (FPY)** | % of reports that pass the First-Line QA review (Step 4) without needing rework. | **> 95.0%** | Finance Operations Manager | Reporting Portal Analytics |
| **dbt Test Coverage** | % of all data models in `FIN_ANALYTICS` with documented and automated data quality tests. | **100%** | Data Engineering Lead | Data Quality Dashboard (Datadog) |
| **SOC 2 Control Failure Remediation Time** | Mean time from identifying a control deficiency to implementing a permanent remediating action. | **< 30 Days** | VP of Financial Services | ServiceNow GRC Dashboard |

### 7.2 Key Risk Indicators (KRIs)

These thresholds trigger proactive risk management actions.

| KRI | Amber Threshold (>24h) | Red Threshold (>1h) | Escalation |
| :--- | :--- | :--- | :--- |
| **EOD Batch Processing Delay** | Delay > 2 Hours past EOD. | Delay > 4 Hours past EOD. | Red triggers PagerDuty alert for Data Engineering Lead & VP. |
| **Single Report Variance (Material)** | An unexplained variance for a single client report > 3% but < 5% MoM. | An unexplained variance for a single client report > 5% MoM. | Red requires immediate halt of distribution, root cause analysis, and CFO notification. |
| **Stale System Access** | A privileged user account dormant for > 30 days but < 60 days. | A privileged user account dormant for > 60 days. | Red triggers immediate, forced deactivation of the account and a User Access Review cycle. |

### 7.3 Reporting Cadence

- **Daily:** The Finance Operations Manager reviews the SLA Dashboard and DDP metrics each morning.
- **Weekly:** A WIP financial control report is circulated to the VP of Financial Services.
- **Monthly:** The full KPI and KRI scorecard is compiled by the Finance Operations Manager and presented by the VP of Financial Services to the CFO. This is the primary forum for reviewing this SOP's effectiveness.
- **Quarterly:** A summary of the quarterly SOC 2 control testing (self-assessment) is presented by the VP of Financial Services to the CISO and Compliance Officer.
- **Annually:** A comprehensive process review and SOC 2 control attestation is completed for the external auditors.

## 8. Exception Handling and Escalation

### 8.1 General Exception Process

Deviations from the standard procedures outlined in Section 5 shall only be permitted on a temporary basis due to an exceptional business or technical event. A standing deviation is not permitted under this SOP.

1.  **Identification:** The need for an exception is identified by any team member.
2.  **Documentation:** A formal Exception Request must be logged in ServiceNow (`GRC > Policy Exception`), linked to SOP-FIN-016. The request must detail:
    - Nature of the deviation.
    - Specific steps being waived or modified.
    - Business justification and risk assessment.
    - Compensating control(s) implemented for the duration of the exception.
    - Duration of the requested exception (not to exceed 90 days).
3.  **Escalation and Approval:**
    - **Technical & Minor Procedural Exceptions** (e.g., skipping a secondary review on a low-value, non-material ad-hoc report due to urgent, time-sensitive need) require approval from the **VP of Financial Services (Robert Liu)** .
    - **Material & Control Deviations** (e.g., any exception impacting an SOC 2-tested control, a financial reporting system outage >2 hours, or a workaround for a core control) require joint approval from the **VP of Financial Services (Robert Liu)** and the **Chief Compliance Officer (Thomas Anderson)** . The **CFO (James Thornton)** must be informed.
4.  **Remediation:** All approved exceptions must have a linked remediation ServiceNow Task, with a clear owner and deadline to return to the standard procedure. Overdue remediation tasks are automatically escalated to the approver.

### 8.2 Incidents and Urgent Escalation

If a critical error is discovered in a report after distribution, this constitutes a severity 1 (SEV1) incident for the Financial Services BU.
1.  **Immediate Action:** The discoverer must immediately alert the Finance Operations Manager and the Data Engineering Lead through the dedicated #fin-sev1 Slack channel and by phone.
2.  **Containment:** The first responder will halt all further dependent report distributions and revoke erroneous digital files from SFTP or client portals if technically feasible.
3.  **Communication:** The VP of Financial Services (Robert Liu) will coordinate client communication within 1 business hour of verification, in consultation with the Meridian Account Management and Legal teams.
4.  **Post-Incident Review:** A post-mortem analysis and Corrective and Preventive Action (CAPA) plan must be documented in ServiceNow within 5 business days of resolution, presented to the CFO for review.

## 9. Training Requirements

All personnel identified in the RACI matrix (Section 3) must complete mandatory training on this SOP to ensure their designated role is fully understood.

| Training Module | Target Audience | Frequency | Content | Tracking Method |
| :--- | :--- | :--- | :--- | :--- |
| **FIN-016-101: Financial Reporting Lifecycle** | All Finance & Data Eng. staff. | Annually & on SOP revision. | Covers SOP procedures, key changes in latest version, and practical run-through of the reporting portal. | Workday Learning LMS — Auto-assignment based on AD group membership. |
| **FIN-016-201: Control Owner Certification** | Finance Ops Manager, VP of Fin. Services, Data Eng. Lead. | Semi-Annually & on Control change. | Deep-dive into the specific SOC 2 controls in the RACM (Section 6), evidence gathering standards, and internal audit facilitation. | Workday Learning LMS — Assigned by Compliance Officer. Requires passing a knowledge check quiz (80% pass mark). |
| **FIN-016-EXC: Exception Handling** | All staff identified in the escalation path. | Once, upon role assignment. | Covers the ServiceNow Exception process and SEV1 incident response protocols. | Manager sign-off in Workday attestation. |

**Training Compliance:** The VP of Financial Services is responsible for ensuring 100% training compliance for their BU. A monthly "Training Compliance" report is generated from Workday and reviewed. Non-compliance beyond 30 days from the assignment date is flagged to the individual's manager and the HR Business Partner.

## 10. Related Policies and References

This SOP does not exist in isolation and must be read in conjunction with the following internal policies and external standards:

### 10.1 Internal Meridian Policies

| SOP ID | Policy Title | Relationship |
| :--- | :--- | :--- |
| **SOP-IS-030** | Data Classification and Handling Policy | Defines data sensitivity levels that guide report distribution security. |
| **SOP-IS-022** | Data Retention and Destruction Policy | Governs the archival and ultimate disposal timeline for all financial reports. |
| **SOP-IS-008** | Access Control Policy | Defines RBAC fundamentals, user provisioning, and de-provisioning, enforced for financial systems. |
| **SOP-GRC-002** | Enterprise Risk Management Framework | Establishes the overall methodology for defining risk appetite and KRIs. |
| **SOP-AI-014** | Model Risk Management (SR 11-7) | Governs the lifecycle of financial models, whose performance is monitored and reported in this SOP. |
| **SOP-SEC-011** | Incident Response Plan | Provides the overarching framework for SEV1 incident response, including reporting-specific scenarios. |
| **SOP-LG-005** | Whistleblower and Non-Retaliation Policy | Protects employees reporting concerns about financial reporting integrity. |

### 10.2 External Standards and Regulations

- **SOC 2 Trust Services Criteria:** _TSP Section 100: 2017 Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy_ (AICPA Guide). This SOP is a key artifact for the Processing Integrity (P1) principle, specifically P1.1, P1.2, P1.3, and the supporting Common Criteria (CC6, CC7, A1).
- **SSAE 18 (Statement on Standards for Attestation Engagements No. 18):** Governs the audit of the controls described herein.
- **Internal Revenue Code Section 6050W:** Mandates the reporting requirements handled by this SOP for client 1099-K generation.

## 11. Revision History

| Version | Date | Author(s) | Summary of Changes |
| :--- | :--- | :--- | :--- |
| **4.0** | 2024-04-08 | Sarah Jenkins (Compliance), Alex Chen (Fin. Ops. Mgr.) | **Major Update:** Full restructure for SOC 2 readiness. Added Sections 6 (Controls and Safeguards with TSC mapping) and 7 (KPIs and KRIs with new dashboards). Defined formalized roles in Section 3 RACI. Updated exception process from email to ServiceNow workflow. |
| **3.4** | 2025-10-07 | Robert Liu (VP, Fin. Services) | **Process Update:** Added Section 5.3 for Ad-Hoc Reporting. Revised Section 5.2 Step 5 to formalize Data Engineering Lead's role in technical verification. Updated KPI targets in Section 7.1. |
| **3.3** | 2023-09-01 | Maria Diaz (Data Eng.) | **Technical Update:** Migrated all data extraction procedures from legacy Informatica to dbt/Apache Airflow stack. Updated technical references in Sections 5.1 and 6. |
| **3.1** | 2022-11-15 | Robert Liu (VP, Fin. Services) | **Compliance:** Enhanced distribution security (Section 5.2, Step 8) to mandate PGP encryption for all partner SFTP transfers in response to CISO audit finding. |
| **3.0** | 2022-02-10 | James Thornton (CFO) | **Governance:** Introduced Disclosure Committee and CFO Approval chain for external reports (Section 5.2, Step 7). Established this SOP as a foundational, auditable document. |
| **2.0** | 2021-06-01 | Robert Liu (VP, Fin. Services) | Initial formalization of manual processes into a controlled SOP. Added roles, definitions, and first version of the RACI. |
| **1.0** | 2020-01-15 | IT Operations | Initial operational draft. |
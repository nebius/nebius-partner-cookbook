---
sop_id: "SOP-COPS-001"
title: "Customer Data Handling"
business_unit: "Customer Operations"
version: "5.2"
effective_date: "2025-07-23"
last_reviewed: "2026-05-10"
next_review: "2026-11-24"
owner: "Michael Chang, VP of Customer Operations"
approver: "Robert Liu, VP of Financial Services"
classification: "Internal"
regulations:
  - "GDPR"
  - "HIPAA"
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Customer Data Handling

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP-COPS-001) establishes the framework, controls, and procedural requirements for the handling, storage, transmission, and disposal of Customer Data within Meridian Health Technologies, Inc. The purpose of this document is to ensure the confidentiality, integrity, and availability (CIA) of all customer information assets in accordance with contractual obligations, industry standards, and applicable regulatory mandates, specifically including the Health Insurance Portability and Accountability Act (HIPAA). This SOP operationalizes the principles defined in the Meridian Information Security Policy (SOP-IS-002) and the Data Governance Framework (SOP-DG-005).

### 1.2 Scope
This SOP applies to all full-time employees, contractors, temporary staff, interns, and third-party vendors (collectively "Personnel") who access, process, transmit, or dispose of Meridian Customer Data across all business units, including Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform. The scope encompasses all environments—production, staging, development, and disaster recovery—hosted on Amazon Web Services (AWS us-east-1, eu-west-1) and Azure (DR). This document governs data in all states: at rest, in transit, and in use.

### 1.3 Applicability by Data Classification
The controls in this SOP apply based on the Meridian Data Classification Schema:
- **Public:** No restrictions.
- **Internal:** Standard access controls apply.
- **Confidential:** Strict access controls, encryption, and audit logging.
- **Restricted:** Maximum security controls, including PHI, payment card data, and authentication secrets. This SOP focuses primarily on Confidential and Restricted classifications.

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
| :--- | :--- |
| **Business Associate (BA)** | As defined under 45 CFR § 160.103, an entity that performs functions or activities on behalf of, or provides services to, a Covered Entity that involve the use or disclosure of Protected Health Information (PHI). Meridian acts as a BA for its HealthPay and MedInsight products. |
| **Covered Entity (CE)** | A health plan, health care clearinghouse, or health care provider that transmits any health information in electronic form. |
| **Customer Data** | Any information provided by, generated for, or related to a customer or their end-users, including but not limited to PHI, Personally Identifiable Information (PII), financial data, clinical data, and metadata. |
| **Data Custodian** | The individual or team responsible for implementing and managing security controls over the data, as directed by the Data Owner. |
| **Data Lake** | The centralized repository (Snowflake/AWS S3) storing raw, unstructured, and structured data. |
| **Data Owner** | The senior leader (VP or above) ultimately accountable for the classification, use, and lifecycle of a specific data domain. |
| **Data Steward** | The operational role responsible for data quality, metadata management, and enforcing access policies on behalf of the Data Owner. |
| **ePHI** | Electronic Protected Health Information, as defined by HIPAA. |
| **HIPAA** | Health Insurance Portability and Accountability Act of 1996, as amended by the HITECH Act and the Omnibus Rule of 2013. |
| **PHI** | Protected Health Information. Individually identifiable health information held or transmitted in any form. |
| **Secure Communication** | Transmission channels encrypted using TLS 1.2 or higher. |
| **ServiceNow** | Meridian's IT Service Management (ITSM) and ticketing system used for access requests and incident reporting. |
| **SOC 2** | Service Organization Control 2 report framework. |
| **TSB** | Technical Security Baseline, the minimum security configuration standards defined by CISO Rachel Kim. |

## 3. Roles and Responsibilities

The following RACI (Responsible, Accountable, Consulted, Informed) matrix dictates the authority and duty of each role in the lifecycle of Customer Data.

| Activity | Data Owner (VP) | Data Steward | Data Custodian (IT/Eng) | CISO Rachel Kim | Chief Privacy Officer (Dr. Weber) | VP Customer Ops (M. Chang) | Personnel |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Data Classification** | A | R | C | C | C | I | I |
| **Access Authorization** | A | C | R | I | I | I | I |
| **Physical Media Encryption** | I | I | R / A | C | I | I | - |
| **HIPAA Breach Notification** | A | R | C | C | C | I | C |
| **Secure Transmission Setup** | I | I | R / A | C | I | I | - |
| **Data Retention & Disposal** | A | R | C | I | I | C | I |
| **Policy Compliance Acknowledgment** | A | I | I | I | I | R | R |

### 3.1 Data Owners (VP-Level)
- **VP of Clinical AI Products (Dr. Aisha Okafor):** Owner of all clinical model input/output data.
- **VP of Financial Services (Robert Liu):** Owner of HealthPay transactional and credit scoring data.
- **VP of Customer Operations (Michael Chang):** Owner of customer service records, support tickets, and call recordings.
- Data Owners must review and approve access control lists (ACLs) for their domains quarterly.

### 3.2 Data Stewards
Designated by Data Owners via a formal Data Stewardship Nomination Form (Appendix A). Responsible for running the quarterly "Stale Access Review" reports in Okta and Snowflake and flagging discrepancies within 5 business days.

### 3.3 Customer Operations Specialists (Levels I-III)
The primary executors of this SOP. Level III Specialists have elevated privileges to run de-identification scripts; Level I and II are restricted to viewing data via the Meridian SaaS Platform UI only.

## 4. Policy Statements

Meridian Health Technologies adheres to the following mandatory policy commitments regarding the handling of Customer Data:

- **P-01: Minimum Necessary.** Personnel shall only access the minimum necessary Customer Data required to perform a specific, authorized job function. This is enforced via Role-Based Access Control (RBAC) in Okta and attribute-based controls in Snowflake (see HIPAA § 164.502(b), § 164.514(d)).
- **P-02: Encryption Mandate.** All Customer Data classified as Restricted must be encrypted at rest using AES-256 and in transit using TLS 1.2 or higher. No Customer Data containing PHI shall be transmitted over email without a Meridian-approved encryption gateway (Mimecast Secure Messaging).
- **P-03: Secure Disposal.** Physical media (hard drives, USB tokens) that have ever stored Customer Data must be securely erased per NIST 800-88 standards or physically destroyed by Meridian's certified vendor (Shred-It Corp, Contract #V-2024-1122).
- **P-04: Clear Desk and Screen.** Personnel must lock their workstation (Windows+L) whenever leaving it unattended. Physical documents containing Restricted data must be locked in a classified-asset cabinet (Securitall Model S-700) overnight.
- **P-05: Prohibition of Public Cloud Storage.** Use of unauthorized consumer cloud storage services (e.g., Dropbox, personal Google Drive) for Customer Data is strictly prohibited. The only authorized storage locations are Meridian’s AWS S3 buckets (prefix: `meridian-restricted-*`) and the local encrypted SSD of company-issued MacBooks/ThinkBooks.

## 5. Detailed Procedures

This section outlines the step-by-step operational workflows required to manage Customer Data within the scope of SOP-COPS-001.

### 5.1 Data Access Request and Provisioning
This procedure applies whenever Personnel require access to a system beyond the default "Standard User" RBAC group.

1.  **Request Submission:** The Personnel (Requestor) navigates to the Meridian ServiceNow Portal, selects "Access Request – Data," and completes the "HIPAA-Aware Data Access Form." The form requires:
    - `Requestor ID` (auto-populated from Okta).
    - `Data Domain` (e.g., MedInsight Claims, HealthPay Transactions).
    - `Justification` (Business justification specific to ticket/incident).
    - `Duration` (up to 90 days; permanent access requires VP approval).
2.  **Manager Review:** The Requestor’s direct manager receives an automated ServiceNow notification. The manager must verify the business justification and approve/reject within 2 business days.
3.  **Data Owner Approval:** If the request involves Confidential/Restricted data, ServiceNow routes the ticket to the relevant Data Owner (e.g., Robert Liu for transactional data). Data Owners have a 5-day SLA for approval.
4.  **Provisioning (Data Custodian):** Upon dual approval (Manager + Owner), the IT Provisioning team creates the appropriate Okta group assignment and Snowflake Role. Provisioning is executed within 1 business day of final approval.
5.  **Verification:** The Requestor must log in and verify access within 24 hours. Failure to verify triggers an automatic auto-revoke script executed via AWS Lambda (`AutoDeprovision-StaleAccess`).

### 5.2 Secure Handling in Customer Operations (Day-to-Day)
This is the core workflow for Customer Operations Specialists (Level I-III).

#### 5.2.1 Identity Verification Before Data Disclosure
Before disclosing ANY data, even internally classified as Internal, the Specialist must:
1.  Request **three** verification attributes from the caller, per the Meridian Customer Verification Matrix (Appendix B).
2.  Attributes must belong exclusively to the authenticated user profile in Zendesk, which syncs via SSO with Okta.
3.  **For PHI disclosures:** The caller must provide the unique "Meridian Privacy PIN" (a 6-digit alphanumeric code set during account creation).
4.  **Failed Verification:** If verification fails twice, the request MUST be escalated to a Level III Specialist (Team Lead) via Zendesk escalation trigger `ES-PHI-VERIFY-FAIL`. No data is disclosed.

#### 5.2.2 Secure Screen Sharing
When screen sharing is required for troubleshooting:
1.  Close all non-relevant tabs and applications, including internal Slack/Teams channels containing non-public data.
2.  Activate "Watermark Mode" on macOS/Windows, which overlays the viewer's name and timestamp, deterring photography.
3.  Initiate sharing via the Meridian-licensed Zoom instance, ensuring "End-to-End Encryption" is enabled in the session settings.
4.  Never share a local terminal window; use the browser-based Meridian Internal Tool Console (MITC), which masks API keys and connection strings.

#### 5.2.3 Data Extraction for Reporting
Level II Specialists may generate reports that aggregate de-identified data.
1.  **Query Execution:** Log into the *Data Lake Read-Only Interface* (AWS QuickSight). Do NOT use SnowSQL shell for routine queries.
2.  **De-identification:** Before export, apply the `fn_deidentify_phi()` function. This function, maintained by the Data Lake team, strips direct identifiers (name, MRN, SSN) and truncates dates to "Year" precision per 45 CFR § 164.514(a) Safe Harbor method.
3.  **Export Destination:** Export the report *only* to the `meridian-internal-exports` S3 bucket. Exporting to the local workstation download folder is blocked by endpoint DLP agents.
4.  **Validation:** A random 5% sample of exported reports is audited weekly by the Data Steward to ensure the de-identification function was applied correctly.

### 5.3 Data Transmission Procedures
Personnel must use the following methods when transmitting Customer Data.

1.  **Internal Transmission (AWS VPC):** Data transmitted between AWS EC2 instances and S3/RDS/Redshift within the same VPC is encrypted via AWS native TLS mechanisms. No user action required.
2.  **External Transmission to Customers (e.g., Claims data):**
    - **SFTP (Primary):** Meridian Standard SFTP (`sftp.meridian.com`, port 22). Files must be PGP-encrypted with the customer's specific public key. Personnel must first upload the file to the SFTP Staging Bucket (`sftp-staging`), where an automated job (`pgp-encrypt-dispatcher`) encrypts and moves the file to the outbound queue.
    - **Mimecast Secure Messaging (Secondary):** For ad-hoc transmission of a single PHI record. Use the "Send Secure" button in the Outlook Web Add-in. This portal-based method is the *only* HIPAA-compliant method for email-based transmittal of PHI (per the 2013 HIPAA Omnibus Rule emphasis on covered entity transmissions).
3.  **Prohibited Transmissions:** FTP (unencrypted), HTTP (unencrypted), standard SMTP (email) for Restricted data. Personnel found violating this rule are subject to immediate disciplinary action as defined in the Sanctions Policy (SOP-HR-009).

### 5.4 Physical Data Handling and Clean Desk
Given the hybrid workforce, physical security remains a priority.

1.  **Printing Restricted Data:** Prohibited by default. If an exception is granted for regulatory filing, printing must occur on a Meridian Secure Print Release station. The print job is released only upon the user's badging in at the printer.
2.  **Clean Desk Enforcement:** The Senior Operations Manager performs a physical walkthrough of the Boston and Chicago offices daily at 6:00 PM local time. Any unattended document is scanned, logged in ServiceNow incident `CT-DESK-*`, and securely shredded. A weekly "Clean Desk Compliance" metric is reported to the VP of Customer Operations.

### 5.5 Data Disposal and Media Sanitization
Customer Data must be securely disposed of in accordance with the Meridian Retention Schedule (Appendix C).

1.  **Electronic Disposal (AWS):** When an EC2 instance is decommissioned, the automated termination script runs a `shred` (Linux) or a compliant wipe utility. The S3 buckets enforce a lifecycle policy that deletes objects after the contractual period + 90 days.
2.  **Physical Media (Laptops/USB):** All faulty or decommissioned laptops must be surrendered to IT Operations (Boston, Room 104). The IT Hardware Steward logs the device serial number into the "Destruction Logbook" and performs a DoD 5220.22-M 7-pass secure erase. Upon completion, the device is physically shredded in the Meridian hard drive crusher. **Under no circumstances is a laptop containing PHI to be disposed of without IT wiping.**

## 6. Controls and Safeguards

### 6.1 Administrative Controls
- **HIPAA Business Associate Agreements (BAAs):** Vendor Management maintains a master repository of executed BAAs in the ContractWorks system (Link: `cw.meridian.com`). No vendor with access to PHI is onboarded without an executed BAA (HIPAA § 164.504(e)).
- **Sanction Policy:** The HR department maintains a formal Sanction Policy for HIPAA violations. Penalties range from mandatory retraining to immediate termination.
- **Non-Disclosure Agreement (NDA):** All Personnel sign an NDA containing specific clauses regarding HIPAA and data confidentiality on the first day. A digital renewal is required annually on the employment anniversary.

### 6.2 Technical Controls
- **Access Control (Okta & Snowflake):**
    - Multi-Factor Authentication (MFA) enforced for all Okta users via Duo Security push notification.
    - Snowflake Row-Level Security (RLS) policies dynamically filter rows based on the user's Okta group membership (e.g., a Specialist can only see the `hospital_id` matching their assigned facility).
- **DLP (Endpoint and Network):**
    - **Netskope Cloud Access Security Broker (CASB):** Monitors all traffic to unmanaged SaaS applications. A "Restricted Data Classification" label triggers an automatic block and audit log.
    - **Microsoft Purview DLP (Endpoint):** Monitors clipboard operations. Copying PHI from the Meridian SaaS Platform into a Notepad.exe triggers a visual pop-up warning and a low-severity incident log in Splunk.
- **Encryption Key Management:** AWS Key Management Service (KMS) rotates Customer Master Keys (CMKs) annually. The CISO's office holds the root key material; Engineering holds sub-keys for daily operations.

### 6.3 Physical Controls
- **Server Rooms:** Access to the Meridian data cage in the Equinix DC1 facility requires biometric (palm vein) scan and a paired key-card. Access logs are reviewed bi-weekly by the Physical Security Officer.

## 7. Monitoring, Metrics, and Reporting

The effectiveness of the Customer Data Handling program is tracked via a dashboard (Splunk Dashboard ID: `HIPAA-Compliance-DB`) and monthly reporting.

### 7.1 Key Performance Indicators (KPIs)

| Metric | Target | Measurement Tool/Method | Reporting Cadence |
| :--- | :--- | :--- | :--- |
| **Stale Access Remediation** | > 95% revoked within 48 hours | Okta "Last Login" report vs. Active Directory | Monthly to Data Owners |
| **PHI Transmission Violations** | 0 incidents | Netskope block events for unauthorized data flows | Instant Alert to CISO |
| **Clean Desk Adherence** | < 2 violations per week | SOC-Physical walk-through log | Weekly to VP Cust. Ops |
| **Data Access Request SLA** | > 90% processed within 5 business days | ServiceNow Dashboard | Monthly |
| **Unencrypted DB Connections** | Zero active connections per quarter | AWS Trusted Advisor / Nmap internal scan | Monthly to Engineering |

### 7.2 HIPAA Log Review
The Security Operations Team reviews the following specific HIPAA logs weekly in the `meridian-log-prod` S3 bucket:
- **PHI Read Events:** Snowflake `QUERY_HISTORY` filtered on objects containing ePHI. Any bulk export event (> 1000 rows in 5 minutes) triggers an incident response playbook (SOP-IR-004).
- **Access Elevation:** Any Okta event where a user is added to the `Domain-Admin` or `Restricted-Data-Custodian` roles must have a corresponding, closed-access request ticket.

## 8. Exception Handling and Escalation

### 8.1 Exception Request Process
Compliance with this SOP is mandatory. Deviations require a formal exception.

1.  **Form Submission:** The Requestor submits SOP Exception Request Form (Appendix D) in ServiceNow, detailing:
    - Specific section of SOP for which exception is sought.
    - Business justification and compensating controls to be used.
    - Duration of the exception (maximum 90 days, renewable).
2.  **Risk Assessment:** CISO (or delegate) performs a risk assessment of the proposed compensating controls. Findings are documented on the ServiceNow ticket.
3.  **Approval Matrix:**
    - **Low-risk exceptions** (e.g., disabling watermark mode for 1 hour due to a UI rendering bug): Approvable by the VP of Customer Operations (Michael Chang) alone.
    - **Medium-to-High-risk exceptions** (e.g., transmitting PHI via a temporary, non-standard Mimecast alternative during an outage): Require joint approval from CISO (Rachel Kim) and the relevant Data Owner.
4.  **Expiration:** No exception is permanent. On the expiration date, the compensating control MUST be revoked, and ServiceNow automatically notifies the approver to manually validate the revocation.

### 8.2 Escalation Path for Customer Data Breaches
- **Immediate Action:** Any Personnel who suspects a breach (e.g., unauthorized disclosure, ransomware affecting ePHI) must IMMEDIATELY stop handling data and contact `security-hotline@meridian.com` (SOC-2 direct line).
- **Breach Response:** The Meridian Computer Incident Response Team (CIRT), led by Rachel Kim, activates SOP-IR-002 (HIPAA Breach Response). Under no circumstances should the discoverer attempt to remediate the breach on their own, which could compromise forensic evidence.
- **Notification:** The Chief Legal Officer and Chief Privacy Officer (Dr. Weber) are immediately engaged to evaluate the threshold under 45 CFR § 164.404 (Notification to Individuals) and § 164.408 (Notification to the Secretary).

## 9. Training Requirements

All Personnel with access to Customer Data must complete the following mandatory training tracks, managed via the Workday Learning Management System (LMS).

| Training Module | Target Audience | Frequency | Provider |
| :--- | :--- | :--- | :--- |
| **HIPAA Fundamentals for BAs** | All Personnel | Annual (Initial within 30 days of hire) | MedTrain Learning |
| **Meridian Data Classification & Handling (SOP-COPS-001)** | Customer Ops, Engineering, IT | Annual, plus upon SOP revision > v4.x | Internal (Dr. Weber / M. Chang) |
| **Secure Coding Practices** | Engineering, DevOps | Annual | SANS SEC540 |
| **Phishing and Social Engineering** | All Personnel | Quarterly simulated campaign | KnowBe4 |
| **Incident Reporting Drill** | All Personnel | Bi-Annual tabletop exercise | Internal (CISO Team) |

**Tracking and Escalation:** Training completion is tracked weekly. Personnel failing to complete assigned training within 15 days of the deadline have their access to Production systems automatically suspended until completion is verified.

## 10. Related Policies and References

| Identifier | Document Name | Relationship |
| :--- | :--- | :--- |
| **SOP-IS-002** | Information Security Policy | Parent policy defining overall security responsibilities. |
| **SOP-DG-005** | Data Governance Framework | Establishes the classification schema and Data Owner responsibilities. |
| **SOP-IR-002** | HIPAA Breach Incident Response | Step-by-step forensic investigation and notification process for breaches involving PHI. |
| **SOP-IR-004** | Bulk Data Anomaly Response Playbook | Technical procedure for responding to anomalous bulk ePHI reads. |
| **SOP-HR-009** | Sanctions Policy | Describes disciplinary process for policy violations. |
| **SOP-VEND-003** | Third Party Vendor Risk Management | Defines due diligence and BA agreement requirements for vendors. |
| **45 CFR Part 164** | HIPAA Security and Privacy Rules | Federal regulation (External Reference). |
| **NIST 800-88 Rev 1** | Guidelines for Media Sanitization | Standard used for data destruction. |

## 11. Revision History

| Version | Date | Author(s) | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2022-01-15 | J. Smith (Cust Ops), A. Chen (Legal) | Initial Draft. Defined core data classifications and basic procedures. |
| 2.0 | 2022-08-10 | M. Chang | Major revision: Added detailed Identity Verification process (Section 5.2.1) and integrated Zoom E2EE mandate. |
| 3.1 | 2023-03-04 | R. Kim (CISO) | Updated Controls (Section 6) to mandate Netskope CASB and Microsoft Purview DLP rollout. Updated encryption specifics. |
| 4.0 | 2024-06-12 | B. Davis (Cust Ops Lead) | Simplified the Customer Operations workflow (Section 5.2), removed deprecated FTP procedure, added Clean Desk walkthrough KPI. |
| 5.0 | 2025-02-17 | M. Chang, R. Kim | Full re-write to align with new AWS Multi-Account architecture. Migrated access requests to ServiceNow from legacy Remedy. |
| 5.1 | 2025-04-03 | R. Kim | Clarified Key rotation schedule (Section 6.2) from Manual to KMS Automated; updated Netskope block event rules. |
| 5.2 | 2025-07-23 | M. Chang | Added Section 5.5.1 on physical laptop disposal logbook. Updated the RACI matrix to reflect new Data Steward role. Updated Appendix A form link. |
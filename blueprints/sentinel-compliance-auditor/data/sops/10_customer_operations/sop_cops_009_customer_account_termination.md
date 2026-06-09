---
sop_id: "SOP-COPS-009"
title: "Customer Account Termination"
business_unit: "Customer Operations"
version: "3.2"
effective_date: "2025-03-27"
last_reviewed: "2026-05-21"
next_review: "2026-11-04"
owner: "Michael Chang, VP of Customer Operations"
approver: "Robert Liu, VP of Financial Services"
classification: "Internal"
regulations:
  - "GDPR"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Customer Account Termination

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the unified, enterprise-wide framework for the termination of customer accounts across all Meridian Health Technologies, Inc. business lines. The purpose of this document is to define the end-to-end process for executing account terminations—whether initiated by the customer, by Meridian, or by regulatory mandate—in a manner that ensures operational consistency, financial integrity, data security, and rigorous regulatory compliance, particularly with the Health Insurance Portability and Accountability Act (HIPAA).

This SOP serves as the single authoritative source for the procedural, technical, and administrative controls required to deprovision access, settle financial obligations, manage the retention and ultimate destruction of Protected Health Information (PHI), and document the complete termination lifecycle. Given Meridian’s role as a business associate and covered entity handling PHI for approximately 12 million patients, the integrity of the termination process is paramount to preventing unauthorized data exposure and ensuring compliance with contractual obligations.

### 1.2 Scope

This SOP applies to all customer accounts managed by Meridian Health Technologies, encompassing the following business lines and their associated data domains:

| Business Line | Account Types in Scope | Data Classification |
|---|---|---|
| Clinical AI Platform | Hospital, clinic, and imaging center accounts | PHI, Clinical Decision Support Data, Diagnostic Outputs |
| HealthPay Financial Services | Provider billing accounts, payer accounts, lending partners | PHI, Financial Data, Personally Identifiable Information (PII) |
| MedInsight Analytics | Health system and insurer analytics accounts | PHI, Population Health Data, Risk Scores |

The procedures herein govern the full account termination lifecycle, including:

- Termination request intake and validation
- Multi-departmental coordination for operational, financial, and technical offboarding
- Data retention scheduling and secure data deletion in accordance with HIPAA
- Final invoicing, payment reconciliation, and refund processing
- Access deprovisioning and encryption key management
- Legal hold preservation for accounts subject to litigation or investigation

This SOP applies to all Meridian employees, contractors, and third-party service providers who have a role in the termination lifecycle, including but not limited to personnel within Customer Operations, Finance, Legal, Information Security, Platform Engineering, and Data Governance.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| Account Termination | The permanent deactivation of a customer's access to Meridian systems and the initiation of post-termination data management procedures. |
| Termination for Convenience | A customer-initiated termination without cause, subject to contractual notice periods. |
| Termination for Cause | A Meridian-initiated termination due to a material breach of contract by the customer, including non-payment, violation of acceptable use policies, or regulatory non-compliance. |
| Data Retention Period | The defined duration, post-termination, during which Meridian retains customer data as specified in the Business Associate Agreement (BAA) and this SOP before secure destruction. |
| Secure Data Destruction | The irreversible rendering of PHI and other sensitive data such that it cannot be reconstructed, using NIST SP 800-88-compliant methods. |
| Final Reconciliation | The financial close-out process, including the calculation of all outstanding charges, credits, and the issuance of the final invoice. |
| Legal Hold | A directive issued by the Legal Department suspending normal data destruction procedures for an account involved in pending or anticipated litigation, investigation, or audit. |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| BAA | Business Associate Agreement |
| BAU | Business as Usual |
| CR | Change Request |
| CRM | Customer Relationship Management (Salesforce) |
| CSM | Customer Success Manager |
| DLM | Data Lifecycle Management |
| DRE | Data Retention Engine |
| EPHI | Electronic Protected Health Information |
| FTP | File Transfer Protocol (Secure, SFTP) |
| HIPAA | Health Insurance Portability and Accountability Act of 1996 |
| IAM | Identity and Access Management (Okta) |
| IDM | Intelligent Data Management (Rubrik) |
| IT | Information Technology |
| KPI | Key Performance Indicator |
| SLA | Service Level Agreement |
| SOC | Security Operations Center |

---

## 3. Roles and Responsibilities

The following matrix defines the roles and responsibilities for the execution of this SOP. All named roles are accountable for the actions described herein.

| Role | Responsibility | Accountable / Responsible / Consulted / Informed |
|---|---|---|
| **VP, Customer Operations** (Michael Chang) | Ultimate process owner. Approves all exceptions. | Accountable |
| **CSM** (Assigned per account) | Primary point of contact for the customer. Initiates termination workflow in CRM. | Responsible |
| **Billing Specialist** (Finance Dept) | Performs final invoice calculation, reconciliation, and payment processing. | Responsible |
| **Collections Specialist** (Finance Dept) | Manages recovery of outstanding balances prior to termination finalization. | Responsible |
| **Platform Engineering Lead** (Assigned per business line) | Executes technical deprovisioning, data export, and secure deletion tasks. | Responsible |
| **Data Governance Officer** (Sarah Chen) | Approves data retention schedules, ensures compliance with HIPAA data management requirements. | Consulted |
| **Legal Counsel, Commercial** (David Miller) | Reviews termination for cause, approves legal holds. | Consulted |
| **Chief Information Security Officer (CISO)** (Dr. Anya Sharma) | Approves data destruction certificates for terminated account environments. | Consulted |
| **VP, Financial Services** (Robert Liu) | Final approver for all financial waivers related to termination. | Approver (Financial) |

---

## 4. Policy Statements

Meridian Health Technologies is committed to a transparent, secure, and compliant account termination process. The following high-level policies govern all termination activities:

1.  **Security-First Offboarding:** The deprovisioning of logical access controls shall be the first technical action executed upon final termination confirmation, in accordance with the principle of least privilege. No data deletion shall commence until access revocation is verified.
2.  **Financial Finality:** No customer account termination shall be considered complete until a final invoice has been generated, presented, and all outstanding financial obligations are fully settled or written off in accordance with SOP-FIN-101 ("Revenue Recognition and Collections"). Accounts with outstanding balances exceeding 90 days past due will be escalated for Termination for Cause review.
3.  **Mandated Data Lifecycle:** All PHI shall be managed according to a strict lifecycle defined by the Meridian Data Retention Policy (SOP-DG-004). Post-termination, data shall be transitioned to an "Archived" state for the prescribed retention period, followed by "Certified Destruction." Exceptions to the standard retention period require approval from the VP of Legal and the Data Governance Officer.
4.  **Non-Retaliation for Regulatory Exit:** In cases where a customer terminates their agreement due to a regulatory directive, Meridian shall execute the termination with full cooperation and without undue delay or punitive action, ensuring a smooth transfer of custodial data as required by law.
5.  **Zero-Data Residual:** Upon completion of the retention period, all customer data, including backups, replicas, and logs containing PHI, must be destroyed and a certificate of destruction must be generated and stored as evidence, per the detailed controls in Section 6.

---

## 5. Detailed Procedures

This section outlines the step-by-step operational workflows for the two primary termination scenarios: Customer-Initiated and Meridian-Initiated. Each workflow is managed via a designated "Termination Case" in the Salesforce CRM.

### 5.1 Phase 1: Initiation and Validation

#### 5.1.1 Procedure: Customer-Initiated Termination (CIT)

1.  **Receipt of Request:** The CSM receives a written notice of termination from the customer's authorized signatory. Acceptable channels are email to the CSM or a ticket submitted through the Meridian Support Portal.
2.  **Case Creation (CSM):** Within 2 business hours of receipt, the CSM creates a new Case in Salesforce with the following record type: "Account Termination – CIT."
    - Record is populated with: Account ID, Termination Reason (picklist: Cost, Product Gap, M&A, Regulatory, Other), Requested Effective Date.
    - The CSM attaches the customer's original written notice to the Case record.
3.  **Contractual Review (CSM & Legal):**
    - The CSM cross-references the contract (stored in Agiloft Contract Management System) to validate: (a) The notice period is being met; (b) Any early termination fees or outstanding committed spend clauses are identified.
    - If a contractual breach (e.g., insufficient notice) is detected, the CSM consults the Legal Counsel, Commercial. They jointly craft a response to the customer within 24 hours, acknowledging the termination but clarifying contractual obligations.
4.  **Case Approval (Manager, Customer Success):** Upon validation, the CSM’s direct manager approves the Case, which transitions it to Phase 2: Financial Reconciliation. The approval SLA is 24 hours from Case creation.

#### 5.1.2 Procedure: Meridian-Initiated Termination (MIT) for Cause

1.  **Material Breach Identification:** Any Meridian leader (typically CSM, VP of Sales, CISO, or Legal Counsel) who identifies a material breach triggers this process. Grounds include: consistent non-payment (escalated per SOP-FIN-105), violation of the Acceptable Use Policy (SOP-IS-001), or actions jeopardizing the security or integrity of the Meridian Clinical AI Platform.
2.  **Executive Review Board (ERB) Convening:** The identifying party convenes an ad-hoc ERB. Standing members are the VP of Customer Operations, VP of Financial Services (Robert Liu), and the VP of Legal. The CISO serves as a permanent member for security-related breaches.
3.  **Case Creation (VP, Customer Operations):** The VP creates a "Termination for Cause – MIT" Case in Salesforce, populating it with a detailed "Breach Rationale" document and all supporting evidence.
4.  **ERB Deliberation and Vote:** The ERB reviews the evidence within 3 business days. Termination requires a two-thirds majority vote. The official "Record of Decision" is attached to the Salesforce Case.
5.  **Customer Notification:** Upon a successful vote, Legal Counsel drafts and sends a "Notice of Termination for Cause" via certified mail and email, citing the breach and effective date (typically immediate or as specified in the contract's cure period clauses). The Case proceeds to Phase 2.

### 5.2 Phase 2: Financial Reconciliation and Final Billing

This phase is executed by a designated Billing Specialist upon Case advancement from Phase 1.

1.  **Invoicing Hold:** The Billing Specialist places a "Termination in Progress" hold on the account in NetSuite, preventing the generation of the next regular billing cycle invoice.
2.  **Financial Reconciliation Packet (FRP):** The Billing Specialist compiles the FRP from the ERP (NetSuite), which details:
    - All open and unbilled charges (e.g., usage overages from data ingestion pipelines).
    - All unapplied credits and pre-paid balances.
    - Current aging balance, including disputed amounts.
    - Any contractual early termination fees (from Step 3 in Section 5.1.1).
    - Post-termination charges, including data retention hosting and final data export support, in accordance with the current rate card.
3.  **Draft Final Invoice:** Billing Specialist drafts the "Final Settlement Invoice" in NetSuite, applying all credits and calculating a net payment due (or refund due) to the customer. For HealthPay accounts, this includes a full merchant settlement reconciliation.
4.  **Financial Approval:**
    - For amounts **<$50,000**: The Finance Manager, Customer Operations, approves the draft invoice.
    - For amounts **≥$50,000**: The VP, Financial Services (Robert Liu) approves the draft invoice.
5.  **Customer Presentation:** The CSM presents the approved Final Settlement Invoice to the customer via secure email (Mimecast encrypted) with a read receipt. The cover letter includes instructions for final payment and data export options.
6.  **Payment and Closure:**
    - The Billing Specialist tracks payment against the Final Invoice. Net terms are 15 days from presentation, unless contractually superseded.
    - Upon payment, the Case status is updated to "Financials Concluded."
    - **Collections Escalation:** If payment is not received within the 15-day net term, the Case is automatically routed to the Collections queue per SOP-FIN-105. The legal hold process (Section 5.4) may be triggered.

### 5.3 Phase 3: Data Management and Technical Deprovisioning

Execution of this phase is critically dependent on the Data Governance Officer's approval of the Data Retention Schedule (DRS). This process strictly adheres to HIPAA §164.310(d)(2)(iii) and §164.310(d)(2)(iv) for the proper disposal and reuse of hardware and electronic media.

#### 5.3.1 Step A: Access Revocation (Day 0)

Upon Case status transition to "Ready for Offboarding," the Platform Engineering Lead executes an automated playbook via Okta and AWS IAM.

1.  **Human User Accounts:** All human user accounts (SSO, VPN, Support Portal) associated with the customer's account are **disabled**. No user accounts are deleted at this stage to preserve audit trails.
2.  **Machine/API Credentials:** All API keys, OAuth tokens, and service accounts used by the customer for programmatic access (e.g., to the Clinical AI inference API) are **revoked and deleted**.
3.  **Verification:** An output report from Okta is validated against the customer’s authorized user roster. Discrepancies are resolved within 4 hours.

#### 5.3.2 Step B: Data Retention Schedule (DRS) Drafting (Day 0-2)

The Data Governance Officer, in consultation with the Platform Engineering Lead and the CSM, drafts a DRS. This form specifies:

- The active data stores for the account (e.g., Clinical AI S3 bucket, HealthPay MongoDB cluster, MedInsight Snowflake schema).
- The assigned retention period for PHI, based on contractual, regulatory (HIPAA §164.316(b)(2)), and business needs. The standard minimum retention is 6 years, or as specified by state law or the BAA.
- An explicit, dated "Destruction Date."

#### 5.3.3 Step C: Data Export (Optional, by Customer Request) (Day 2-5)

If requested in writing and at the customer’s expense, the Platform Engineering Lead initiates a PHI export.

1.  **Export Job:** A job is created using the Meridian Data Egress Utility (DEU) to extract all PHI associated with the customer's tenant ID into an encrypted, compressed archive.
2.  **Integrity Check:** A SHA-256 hash of the archive is generated and provided to the customer through an out-of-band channel.
3.  **Secure Transfer:** The encrypted archive is made available via a time-limited, encrypted S3 pre-signed URL with multi-factor authentication required for download. The file is automatically purged after 72 hours.

#### 5.3.4 Step D: Secure Data Destruction (Post-Retention)

On the scheduled Destruction Date, the following procedures are executed by Platform Engineering:

1.  **Primary Storage:** Data is crypto-shredded. All encryption keys managed by AWS Key Management Service (KMS) specific to the customer's tenant are securely destroyed.
2.  **Secondary Storage and Backups:** Deduplicated backup catalogs in Rubrik are purged. Snapshot-based backups are made irreversibly non-recoverable using Rubrik's "Secure Erasure" feature, with a tamper-evident log.
3.  **Log Data:** Application logs, security telemetry, and audit logs containing PHI (e.g., URLs with patient IDs) are processed through a retention-aware purging pipeline in Splunk, retaining only the records that are legally or operationally required without the PHI.
4.  **Certificate of Destruction:** A "Certificate of PHI Destruction" is generated, signed by the executing Platform Engineering Lead and the Data Governance Officer. It attests to the destruction methodology, date, and scope of data. This certificate is attached to the Salesforce Case.

### 5.4 Phase 4: Case Closure and Quality Assurance

1.  **Gate Check:** A manual "Termination Checklist" in Salesforce must have all items checked:
    - [ ] All access revoked and verified.
    - [ ] Final invoice paid or collection plan active.
    - [ ] Data export completed (or waived by customer).
    - [ ] DRS activated in Data Retention Engine.
    - [ ] No active Legal Holds on the account.
2.  **QA Review:** A designated Customer Operations QA Analyst reviews the completed checklist and all attached evidence. Any discrepancy requires re-execution of the relevant step. SLA for QA review is 2 business days.
3.  **Closure:** Upon successful QA review, the VP of Customer Operations (Michael Chang) is the final sign-off authority for the Case. The account status in Salesforce is set to "Terminated," and all monitoring dashboards are updated.

---

## 6. Controls and Safeguards

The following controls are implemented to ensure the integrity, confidentiality, and availability of customer data during and after the termination process, in alignment with HIPAA Security Rule (45 CFR Part 164, Subpart C) requirements.

### 6.1 Administrative Controls

| Control ID | Control Description | HIPAA Reference |
|---|---|---|
| ADMIN-01 | Formal, documented termination procedure (this SOP) reviewed annually. | §164.316(b)(1) (Policies and procedures) |
| ADMIN-02 | A Designated Account Termination Officer (DATO) is appointed within Customer Operations (currently Director, Customer Operations, reporting to Michael Chang) to oversee all terminations. | §164.308(a)(2) (Assigned security responsibility) |
| ADMIN-03 | All termination Cases must have a formally approved Data Retention Schedule (DRS) prior to any data destruction activity. | §164.308(a)(7)(ii)(A) (Data retention and disposal) |
| ADMIN-04 | A Business Associate Agreement (BAA) Addendum on Termination is executed as part of offboarding, reaffirming obligations regarding the retention, use, and disclosure of PHI by the former customer during the retention period. | §164.504(e) (Business associate contracts) |

### 6.2 Technical Controls

| Control ID | Control Description | HIPAA Reference |
|---|---|---|
| TECH-01 | **Automated Deprovisioning Playbook:** Ansible playbooks, triggered automatically by the CRM-to-IAM webhook, execute the disabling of user accounts and revocation of API keys to prevent manual error. | §164.312(a)(1) (Access Control – Unique User Identification) |
| TECH-02 | **Crypto-Shredding:** Customer-specific data at rest is encrypted with dedicated AWS KMS keys. Deletion of the key renders all encrypted data permanently and irreversibly inaccessible. | §164.312(e)(1) (Transmission Security); Addressable implementation for data at rest deletion. |
| TECH-03 | **Immutable Audit Logs:** All termination actions (financial, access, data) are logged to a write-once, read-many (WORM), immutable log stream in Splunk Cloud. | §164.312(b) (Audit Controls) |
| TECH-04 | **Person or Entity Authentication:** Two-factor authentication is required for all personnel accessing the Data Retention Engine (DRE) to modify or approve a DRS. | §164.312(d) (Person or Entity Authentication) |
| TECH-05 | **PHI De-Identification for Reporting:** Operational metrics and dashboards for tracking terminations are generated using de-identified data, stripping all 18 HIPAA Safe Harbor identifiers before aggregation. | §164.514(a) |

### 6.3 Physical Safeguards

While the primary data centers are cloud-based (AWS), Meridian maintains controls for physical termination access to corporate offices.

| Control ID | Control Description | HIPAA Reference |
|---|---|---|
| PHYS-01 | Workstation Access: The CSM is responsible for ensuring that any shared Meridian device previously accessible to the terminated customer for remote management is factory-reset before reuse. | §164.310(b) (Workstation Use) |
| PHYS-02 | Media Re-Use: All physical media (USB drives, HDDs) retrieved from a terminated customer site relationship must be securely destroyed (NIST SP 800-88 Level 3) and documented. | §164.310(d)(2)(iii) (Media Re-Use) |

---

## 7. Monitoring, Metrics, and Reporting

The effectiveness of this SOP is continuously monitored through a set of defined Key Performance Indicators (KPIs), which are visualized on a live operational dashboard maintained by the Customer Operations Excellence team.

### 7.1 Key Performance Indicators (KPIs)

| KPI | Target | Description | Owner |
|---|---|---|---|
| **Mean Time to Complete Termination (MTCT)** | <45 Days | The average calendar days from Case creation to final closure, for complex enterprise accounts. | VP, Customer Operations |
| **Access Revocation SLA Adherence** | 100% | Percentage of terminations where user access revocation (Phase 3, Step A) is completed within 4 hours of Phase 3 activation. | CISO / Director, IAM |
| **Financial Reconciliation Accuracy** | 99.5% | Percentage of Final Settlement Invoices with $0 in post-closure corrections. | VP, Financial Services |
| **Certificate of Destruction Generation Rate** | 100% | Percentage of terminated accounts that have a Certificate of Destruction generated and filed. Threshold is absolute. | Data Governance Officer |
| **Termination Case QA Pass Rate** | >98% | Percentage of closed Cases that pass the QA gate without requiring rework. | Director, Customer Operations |

### 7.2 Reporting Cadence

- **Weekly Operational Review:** The Customer Operations team reviews a "Termination Queue" dashboard showing all active Cases by phase, highlighting any Case exceeding the SLA for its current phase.
- **Monthly Business Review (MBR):** The VP of Customer Operations and VP of Financial Services review the aggregated KPIs, including MTCT and Financial Reconciliation Accuracy, to identify process bottlenecks.
- **Quarterly HIPAA Compliance Review:** The Data Governance Officer and CISO present a "PHI Destruction and Retention Report" to the Privacy and Security Committee, based solely on the HIPAA-compliant metrics from this SOP. This report details all Certificates of Destruction issued and any incidents or escalations related to unauthorized data retention.

---

## 8. Exception Handling and Escalation

Deviations from the standard procedure are to be minimized but are required for exceptional circumstances. The following process must be followed for any exception.

### 8.1 Exception Request Process

1.  **Formal Request:** Any team member identifying a need for an exception (e.g., customer requests early data destruction before the standard retention period, or a waiver of early termination fees) must document the request using the "SOP-COPS-009 Exception Request" form within the Meridian Compliance Portal (ServiceNow GRC module). The request must detail:
    - The specific step or control from which a deviation is sought.
    - The business and/or technical justification.
    - A risk assessment of the proposed deviation.
    - The proposed alternative control.

2.  **Risk Scoring:** The Director of Customer Operations performs an initial risk scoring based on data sensitivity (PHI exposure) and financial impact.

### 8.2 Escalation and Approval Matrix

| Exception Type | Risk Level | Approval Authority | Max Validity |
|---|---|---|---|
| **Financial Waiver** (Fee < $5,000) | Low | Director, Customer Operations | One-time |
| **Financial Waiver** (Fee ≥ $5,000) | High | **VP, Financial Services (Robert Liu)** & VP, Customer Operations | One-time |
| **Data Retention Alteration** (Any) | Critical | **VP, Legal** & Data Governance Officer | Case-specific |
| **Access Revocation Delay** (Any) | High | CISO (Dr. Anya Sharma) | 5 business days |

All approved exceptions are filed with the Case and reviewed during the quarterly compliance review. An expired exception that has not been resolved must be escalated immediately to the VP of Customer Operations.

---

## 9. Training Requirements

All personnel with roles defined in Section 3 are required to undergo role-specific training on this SOP to ensure consistent and compliant execution of all termination procedures.

### 9.1 Training Curriculum

| Module Code | Target Audience | Content | Frequency |
|---|---|---|---|
| T-COPS-009-01 | All roles | **Fundamentals:** An overview of the account termination lifecycle, emphasizing the "why" behind the policy, focusing on the security-first and data lifecycle principles. | Annual |
| T-COPS-009-02 | CSMs, Billing Specialists, QA Analysts | **Operational:** A hands-on workshop navigating the Salesforce Termination Case. Includes scenario-based simulations for CIT and MIT initiation, and Phase 2 financial reconciliation. | Bi-Annual |
| T-COPS-009-03 | Platform Engineering, Data Governance, Legal | **Technical and Legal:** Deep-dive into Phase 3: Data Retention and Destruction. Covers crypto-shredding, Rubrik secure erasure, legal hold implementation, and Certificate of Destruction generation. Addresses HIPAA §164.310(d) specifically. | Annual |

### 9.2 Tracking and Compliance

All training is managed and tracked through the Meridian Learning Management System (LMS), Workday Learning. Role-based training curricula are automatically assigned. Completion is mandatory before any employee is granted permissions in the Salesforce Termination Case workflow or the AWS/Rubrik destruction tools.

- **Compliance Metric:** "Critical SOP Training Compliance" dashboard tracks completion rates.
- **Threshold:** 95% on-time completion rate for all assigned audiences.
- **Escalation:** Employees past due on mandatory training by 15 days are reported to their VP and have their access to the CRM Terminations module suspended until compliance is achieved.

---

## 10. Related Policies and References

This SOP must be read and executed in conjunction with the following Meridian policies and external standards.

### 10.1 Internal Meridian SOPs

| SOP ID | Policy Title | Relationship |
|---|---|---|
| SOP-FIN-101 | Revenue Recognition and Collections | Governs how final invoices are managed and disputes resolved. |
| SOP-FIN-105 | Escalation and Write-Offs for Non-Payment | Procedure triggered if a terminating customer fails to pay the Final Invoice. |
| SOP-DG-004 | Enterprise Data Retention and Disposal | The master data retention policy defining standard PHI retention periods. |
| SOP-IS-001 | Identity and Access Management | Defines standard procedures for account creation and revocation that are modified during termination. |
| SOP-IS-015 | Incident Response | Governs any breach incident discovered during the termination data export or audit processes. |
| SOP-LEG-011 | Litigation Hold and Legal Preservation | Procedure for placing a legal hold on a customer account that supersedes the standard destruction timeline. |
| SOP-VEN-003 | Third-Party Risk Management | Procedure for offboarding any subprocessors engaged specifically for the terminated customer. |

### 10.2 External Standards and Regulations

- **Health Insurance Portability and Accountability Act (HIPAA) of 1996**, specifically the Privacy Rule (45 CFR Part 164, Subparts E) and Security Rule (45 CFR Part 160 and Part 164, Subparts A and C).
- **Health Information Technology for Economic and Clinical Health (HITECH) Act**.
- NIST Special Publication 800-88, Revision 1, "Guidelines for Media Sanitization."

---

## 11. Revision History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 1.0 | 2019-10-01 | Sarah Jenkins (VP, Cust Ops) | Initial creation of combined termination SOP for newly integrated business units. |
| 2.0 | 2021-05-20 | Michael Chang | Major revision to integrate new MedInsight Analytics platform and automate Phase 3 procedures via Ansible. Shifted to Risk-Approval Matrix for exceptions. |
| 2.5 | 2023-01-17 | David Miller (Legal) | Updated termination for cause clause to align with revised standard Customer Terms of Service (v4.3). Added explicit Certificate of Destruction requirement. |
| 3.0 | 2024-09-12 | Michael Chang | Full document restructure into phases (1-4). Defined KPIs and formal QA gate. Added Crypto-shredding tech controls. |
| 3.1 | 2025-01-18 | Dr. Anya Sharma (CISO) | Reviewed and augmented technical controls (TECH-01 through TECH-05). Specified HIPAA § references in Section 6 Controls. |
| 3.2 | 2025-03-27 | Michael Chang | Formalized ERB voting for MIT. Updated approval authority in exception matrix to reflect new VP of Financial Services. Added WORM log specification. |
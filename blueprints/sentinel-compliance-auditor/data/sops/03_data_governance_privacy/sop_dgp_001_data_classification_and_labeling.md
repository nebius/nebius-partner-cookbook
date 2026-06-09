---
sop_id: "SOP-DGP-001"
title: "Data Classification and Labeling"
business_unit: "Data Governance & Privacy"
version: "3.3"
effective_date: "2024-07-23"
last_reviewed: "2025-12-01"
next_review: "2026-06-03"
owner: "Dr. Klaus Weber, Chief Privacy Officer / DPO"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
  - "HIPAA"
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Data Classification and Labeling

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework and operational directives for classifying, labeling, and handling all data assets throughout their lifecycle at Meridian Health Technologies, Inc. ("Meridian"). The fundamental purpose of this document is to ensure that all data—whether at rest, in transit, or in use—receives a commensurate and verifiable level of protection based on its sensitivity, criticality, and regulatory obligations. This framework is designed to translate abstract legal and contractual mandates into concrete, executable technical and administrative controls that are auditable by internal assurance teams and external assessors.

### 1.2 Scope

This SOP applies universally to all Meridian business units, departments, and geographical locations, including the headquarters in Boston and the global offices in London, Berlin, Singapore, and Toronto. It governs all data created, collected, stored, processed, transmitted, or disposed of by Meridian’s workforce, contractors, consultants, and third-party vendors operating on behalf of Meridian.

The scope encompasses all product platforms and supporting corporate systems:
- **Clinical AI Platform:** Patient health information, diagnostic images, risk scores, and model inference logs.
- **HealthPay Financial Services:** Non-public personal information (NPI), credit reports, payment card data, and transaction records.
- **MedInsight Analytics:** Protected Health Information (PHI) for ~12M patients, aggregated population health data, and care gap analyses.
- **Meridian SaaS Platform:** System configurations, identity and access management logs, and all underlying tenant data hosted on AWS.
- **Corporate Systems:** Human resources records, intellectual property, financial ledgers, and internal communications.

### 1.3 Scope Exclusions

This SOP does not cover the classification of national security classified information, as Meridian does not function as a government contractor requiring such designations. Data that is purely personal and non-business-related, stored incidentally on Meridian-managed personal devices under a Bring Your Own Device (BYOD) policy, is excluded provided that such data is stored exclusively within a secured, isolated container managed by the Mobile Device Management (MDM) solution.

## 2. Definitions and Acronyms

To ensure unambiguous interpretation of this SOP, the following terminology is established:

| Term | Definition |
| :--- | :--- |
| **Data Asset** | A discrete body of information, defined and managed as a single unit so that it can be understood, shared, protected, and exploited effectively. Data assets include databases, data lakes, files, data dictionaries, and structured message payloads. |
| **Protected Health Information (PHI)** | Individually identifiable health information held or transmitted by a covered entity or its business associate, in any form or medium, as defined under the HIPAA Privacy Rule (45 CFR § 160.103). |
| **Electronic Protected Health Information (ePHI)** | PHI that is created, stored, transmitted, or received electronically. |
| **Non-Public Personal Information (NPI)** | Personally identifiable financial information that is not publicly available, as defined under the Gramm-Leach-Bliley Act (GLBA). |
| **Personal Data** | Any information relating to an identified or identifiable natural person (‘data subject’) as defined under Article 4(1) of the GDPR. |
| **Data Classification** | The process of organizing data into categories that represent the risk level and impact severity in the event of unauthorized disclosure, alteration, or destruction. |
| **Data Label** | A security attribute applied to a data asset (file header, metadata tag, watermark) that indicates its classification tier and applicable handling caveats. |
| **Data Steward** | A senior departmental leader designated to oversee the lifecycle of a specific data domain, who makes decisions on classification and remediation. |
| **Data Custodian** | The technical role responsible for implementing and maintaining the security controls on data assets as directed by the Data Steward. This includes database administrators, cloud architects, and storage engineers. |
| **DS4P** | Data Segmentation for Privacy, a framework adopted from HL7 standards for tagging sensitive data at the attribute or segment level. |
| **AWS KMS** | AWS Key Management Service, the primary cryptographic key lifecycle management system used by Meridian. |
| **SR 11-7** | Federal Reserve and OCC Supervisory Guidance on Model Risk Management applicable to HealthPay’s credit scoring and lending models. |

## 3. Roles and Responsibilities

A RACI model is instituted to ensure unambiguous accountability. The following matrix delineates the division of duties for the lifecycle of data classification.

### 3.1 RACI Matrix

| Activity | Chief Privacy Officer / DPO | Data Stewards | Data Custodians | CISO | General Counsel | Chief Compliance Officer | VP of IT Ops |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Defining Classification Tiers | **A** | R | C | R | C | R | I |
| Conducting Initial Data Inventory & Classification | I | **A/R** | R | I | I | C | C |
| Applying Technical Metadata Labels | I | C | **R** | A | I | I | I |
| Approving Reclassification Requests | C | R | I | C | **A** | R | I |
| Auditing Label Efficacy | C | I | I | R | I | **A** | R |
| Handling Data Breach Escalations | R | I | I | **A/R** | C | R | I |

**Key:** R=Responsible, A=Accountable, C=Consulted, I=Informed

### 3.2 Named Roles and Responsibilities

**Dr. Klaus Weber, Chief Privacy Officer / DPO (Owner of SOP-DGP-001)**
- Provides authoritative interpretation of GDPR, HIPAA, and other privacy regulations as they pertain to classification.
- Maintains the Data Classification and Labeling Register.
- Reports on classification gaps to the AI Governance Committee quarterly.

**Data Stewards (Appointed per business unit)**
- **VP of Clinical AI Products (Dr. Aisha Okafor):** Steward for all clinical model inputs, training datasets, and patient risk scores. Responsible for ensuring PHI is classified as "Restricted" at the point of ingestion.
- **VP of Financial Services (Robert Liu):** Steward for NPI, credit models (subject to SR 11-7), and payment tokens.
- **VP of Engineering (David Park):** Steward for technical telemetry, source code, and infrastructure-as-code.

**Data Custodians (Centralized IT Operations)**
- **VP of IT Operations (Samantha Torres):** Oversees the technical implementation of access controls aligned with labels across AWS and Azure.
- The team manages the automated tagging scripts and AWS KMS key policies.

**Chief Information Security Officer (Rachel Kim)**
- Ensures that all security controls (encryption, access, DLP) align with the classification tier policies defined herein.

**General Counsel (Maria Gonzalez)**
- Grants final approval on legal-hold reclassifications and discovery-related handling caveats.

## 4. Policy Statements

### 4.1 Foundational Policy

All digital assets owned or managed by Meridian Health Technologies shall be categorized into one of four mutually exclusive tiers based on the potential impact of a security breach on individuals' privacy, corporate financial standing, and regulatory standing. No data asset shall be stored, processed, or transmitted without a valid, machine-readable label corresponding to its classification tier.

### 4.2 Policy on Data Minimization

Meridian observes the principle of data minimization by design. Classification processes shall be executed prior to data ingestion where feasible, preventing over-collection of unclassified data. Redundant, obsolete, or trivial (ROT) data that falls outside defined business purposes and retention schedules has a default classification of "Candidate for Disposal" and shall not be labeled.

### 4.3 Policy on Standardized Metadata

Meridian mandates the use of a standardized JSON schema for data labels stored in AWS Glue Catalog, Snowflake object tags, and embedded file metadata. This schema ensures consistent parsing by automated security tools such as CrowdStrike DLP and our SIEM.

### 4.4 Privacy Notices and Lawful Basis

Data classification shall inform the specific privacy notices provided to data subjects. While Meridian provides summary privacy notices at point of data collection, the correlation of specific data elements to their detailed legal bases is reflected in the classification schema, enabling technical enforcement of purpose limitation for each business unit's processing activities. The classification engine is configured to flag any processing activity that lacks a documented lawful basis in the metadata registry.

## 5. Detailed Procedures

This section provides the prescriptive, step-by-step procedures required for compliance with SOP-DGP-001.

### 5.1 Initial Data Inventory and Classification (IDIC) Procedure

This procedure applies when onboarding a new data asset (database, S3 bucket, third-party feed, or model training set).

**Step 1: Data Asset Registration**
1.  The Data Steward, or their designee, shall create a new entry in the Meridian Configuration Management Database (CMDB) using ServiceNow form **F-CLASS-001**.
2.  Required fields: Asset Name, System of Origin, Data Domain (e.g., Clinical, Financial, HR), Data Volume (GB/TB), and Tentative Retention Period.

**Step 2: Preliminary Classification Tier Assignment**
1.  The Data Steward shall use the Meridian Data Classification Decision Tree (Appendix A) to assign a preliminary tier based on the most sensitive element within the asset. The classification decision tree uses the following logic:
    - **Decision Node 1:** Does the data asset contain elements defined by 45 CFR § 160.103 as PHI? If YES → **Restricted**.
    - **Decision Node 2:** Does it contain non-public financial information, including credit scores or income data used for SR 11-7 models? If YES → **Restricted**.
    - **Decision Node 3:** Does it contain Personal Data of an EU data subject as per GDPR Article 4(1), without direct identifiers but with a high re-identification risk? If YES → **Confidential**.
2.  The Steward documents the assigned tier in F-CLASS-001.

**Step 3: Regulatory Overlay Analysis**
1.  The Chief Privacy Office (CPO) team performs an automated regulatory overlay scan using the classification "heat map" tool embedded in Snowflake.
2.  The scan maps data elements to specific regulatory articles (e.g., "Data Set tagged as HIPAA §164.502 + EU AI Act Annex III").
3.  If the scan identifies a conflict between the preliminary tier and regulatory requirements (e.g., marking high-risk AI input data merely as "Internal"), the CPO issues a mandatory override.
4.  The asset is updated in ServiceNow.

**Step 4: Automated Labeling**
1.  Upon final CMDB classification, Data Custodians configure the Meridian Labeling Engine (MLE) via a Terraform-managed pipeline (`meridian-labeling/v2.1`).
2.  The MLE pushes metadata tags to the asset's native environment:
    - **AWS S3:** Custom metadata header `x-meridian-classification` and IAM policy condition keys.
    - **Snowflake:** SET TAG `MERIDIAN_DG.TIER = 'RESTRICTED'` on the relevant schema or table.
    - **PostgreSQL:** COMMENT ON TABLE command with a structured text prefix `MDC:RESTRICTED`.

### 5.2 Classification Tiers and Handling Procedures

Meridian defines four classification tiers. The associated handling procedures are mandatory.

#### 5.2.1 Tier 1: Restricted (Red)

**Definition:** Data whose unauthorized disclosure, alteration, or destruction would pose a critical and material risk to the organization, subject us to mandatory breach reporting obligations under federal/state law, and cause severe reputational damage.

**Data Examples:**
- Electronic Protected Health Information (ePHI) governed by the HIPAA Privacy and Security Rules (45 CFR Parts 160, 162, and 164).
- Diagnostic images with identifiable patient markers processed by the Clinical AI Platform.
- NPI, including full consumer credit reports, Social Security Numbers, and payment card primary account numbers (PAN).
- Output of high-risk AI systems as classified under Annex III of the EU AI Act.
- Cryptographic private keys and hardware security module (HSM) material.

**Handling Requirements:**
1.  **Encryption at Rest:** Must use AES-256 encryption with keys managed exclusively by a FIPS 140-2 Level 3 certified HSM (AWS KMS). Key rotation is mandated every 90 days.
2.  **Encryption in Transit:** TLS 1.3 is mandatory for all network transport. mTLS must be implemented for intra-service communication within the Kubernetes clusters hosting the SaaS platform.
3.  **Access Control:** Zero Trust architecture is enforced. Per-session authentication via Okta is required. Access must be authorized through a valid ticket in the Privileged Access Management (PAM) system (HashiCorp Vault). No standing privileged access is permitted.
4.  **PHI De-identification:** For secondary use (e.g., MedInsight analytics), PHI must be de-identified using the HIPAA Safe Harbor method (45 CFR § 164.514(b)) or Expert Determination, producing a derivative dataset verified by the Chief Medical Officer.
5.  **Audit Logging:** All access queries must generate an immutable log event transmitted to the central SIEM (Splunk Cloud) with a unique correlation ID. Logs are retained for a minimum of 7 years in accordance with HIPAA audit requirements.
6.  **Storage Locality:** ePHI and EU Personal Data classified as Restricted must reside within designated geo-fenced data environments (AWS us-east-1 for US data, eu-west-1 for EU data).

#### 5.2.2 Tier 2: Confidential (Yellow)

**Definition:** Data whose unauthorized disclosure could cause significant harm to Meridian’s competitive position, constitutes a violation of contractual data processing agreements (DPAs), or represents sensitive corporate information whose disclosure is restricted under GDPR Articles 13-14 obligations but lacks direct public identifiers.

**Data Examples:**
- Pseudonymized patient datasets where the master key to re-identification exists under Meridian’s control.
- Source code for proprietary AI models in the Clinical AI Platform (excluding the compiled inference containers).
- Detailed internal financial reports, merger and acquisition strategy documents, and board meeting minutes.
- Internal vulnerability scan reports and penetration test raw results.
- HR records containing performance reviews and salary data.

**Handling Requirements:**
1.  **Access Control:** Role-based, with group membership reviewed on an annual basis. Access log collection is continuous but review for anomalies occurs on an automated, event-triggered basis.
2.  **Encryption:** AES-256 at rest, with monthly key rotation. TLS 1.2+ in transit.
3.  **Sharing:** Sharing with third parties requires a DPA to be executed by General Counsel. Internal sharing across business units requires written approval from the relevant Data Steward.
4.  **Data Segmentation:** DS4P tags must be applied at the attribute level if the dataset is used in cross-functional analytics, ensuring that Confidential attributes are masked for users without correct authorization in visualization tools like Tableau.

#### 5.2.3 Tier 3: Internal (Green)

**Definition:** Information intended for active use within Meridian, but whose external disclosure would cause only limited, manageable damage to operations.

**Data Examples:**
- Standard operating procedures, policies, and training materials.
- Non-sensitive project schedules, meeting minutes (non-privileged), and product launch checklists.
- Employee directory (phone numbers, email addresses, office locations).
- Anonymized, aggregated data with zero re-identification risk, verified by the CPO.

**Handling Requirements:**
1.  **Distribution:** Requires TLS for email transmission. Files shared via Google Workspace must have link-sharing disabled by default.
2.  **Disposal:** Approved methods include any commercial-grade deletion tool that removes file pointers, but does not require NIST 800-88 cryptographic purge.

#### 5.2.4 Tier 4: Public (White)

**Definition:** Information explicitly produced and authorized for unrestricted dissemination to the public.

**Data Examples:**
- Marketing materials, public press releases, and verified success stories.
- Publicly posted regulatory filings.
- User manuals for the SaaS platform (excluding system admin guides).

**Handling Requirements:**
1.  **Approval:** Requires documented publication approval from the Corporate Communications team or the SEC legal counsel for investor-related materials.
2.  **Integrity:** While confidentiality is not required, integrity controls must be implemented to prevent website defacement. All public-facing documents must be hosted on the CMS with WAF protection provided by AWS WAF.

### 5.3 Data Labeling Standard

All data shall be programmatically labeled with the Meridian Standard Label (MSL).

**5.3.1 Label Structure**
The MSL is a structured JSON object compatible with AWS Resource Tags, Snowflake Object Tags, and custom file metadata.
```json
{
  "sop_dgp_001": {
    "tier": "Restricted",
    "regulatory_regime": ["HIPAA", "EU_AI_ACT_ANNEX_III"],
    "data_domain": "Clinical_Imaging",
    "ph_indicator": true,
    "pci_indicator": false,
    "expiration_date": "2028-03-15"
  }
}
```

**5.3.2 Mandated Labeling Tools**
- **AWS:** AWS Tags propagated via CloudFormation StackSets are mandatory. Untaggable resources cannot be launched without an exception (see Section 8).
- **Snowflake:** All database objects must use Snowflake's native Tag-Based Masking Policies linked to the `MERIDIAN_DG` schema tags.
- **Legacy PostgreSQL:** A database trigger implemented by VP of IT Operations enforces the presence of the `MDC` comment before `INSERT` privileges are granted.

### 5.4 Reclassification Procedure

Data classification is not static. A formal reclassification process must be initiated by a Data Steward when:
- A data asset's legal retention period expires, transitioning from "Active" to "Archival."
- A de-identification project is completed, moving data from "Restricted" to "Confidential" after Expert Determination certification.
- A vulnerability that was previously unknown is discovered, requiring immediate reclassification.

**Procedure:**
1.  **Request Submission:** Steward submits a reclassification ticket via ServiceNow using template template **F-RECLASS-003**, providing a detailed justification, the asset ID, and the proposed tier.
2.  **Impact Analysis:** The CPO and CISO jointly perform a 14-day analysis on the downstream impact. This includes the effect on existing access controls, DLP profiles, and backup encryption schemas.
3.  **Custodian Execution:** Upon approval, a change request (CR) is opened by the Custodian. The new labels are applied via the CD pipeline.
4.  **Verification:** A two-person integrity check is required. The Data Custodian who applied the label and the requesting Data Steward must jointly verify the new label visibility and correct access policy enforcement before the CR can be closed. This verification must be recorded in the ServiceNow ticket.

## 6. Controls and Safeguards

### 6.1 Technical Controls

**6.1.1 Cloud Access Controls (AWS & Azure)**
Access to data objects is programmatically enforced through IAM Policies and Service Control Policies (SCPs). An SCP is applied organization-wide to deny any `s3:PutObject` operation that does not include a valid `x-amz-object-locking-staging` header if the bucket enforces a classification policy. For data classified as Restricted, the SCP enforces an "encryption required" condition using the `s3:x-amz-server-side-encryption` condition key. Logical access is governed by group memberships synced from Okta; access to Confidential data requires assignment to a specific Security Group in Active Directory.

**6.1.2 Data Loss Prevention (DLP)**
CrowdStrike Falcon DLP sensors are deployed on all endpoints. A dedicated DLP policy, `DLP-RESTRICTED-PHI`, uses the Meridian Standard Label (MSL) regex pattern to detect attempts to copy Restricted data to removable media or unapproved cloud sync services. The default action is "Block" with an immediate alert to the SOC.

**6.1.3 Database Monitoring**
AWS GuardDuty and Snowflake’s anomalous query detection are active. Any SQL command that attempts to `UNSET` or `DROP` a classification tag triggers a P1-level security incident, as this action is a direct violation of the integrity policy.

### 6.2 Administrative Controls

**6.2.1 Annual Data Lifecycle Review**
Data Stewards are responsible for conducting an annual review of their data assets in the CMDB. This review validates that data assets are still accurately classified. The review completion rate is tracked by the Chief Compliance Officer and must reach a threshold of 95% by the end of each fiscal year. Stewards failing to meet this target are subject to an internal audit finding memo.

**6.2.2 Incident Response**
In the event of a confirmed data breach involving Restricted or Confidential data, Meridian will activate the Breach Response Plan documented in SOP-SEC-005. The incident response lifecycle consists of Triage, Containment, Eradication, and Recovery, executed by the CIRT. An immediate containment action for a "Restricted" data spill is the forced rotation of all impacted AWS KMS customer-managed keys and the invalidation of active user sessions on the affected system.

## 7. Monitoring, Metrics, and Reporting

### 7.1 Compliance Monitoring

The effectiveness of data classification controls is continuously audited through automated tooling and manual governance. The Data Governance Committee's objective is to achieve a state where all data assets are fully classified and correctly labeled.

### 7.2 Key Performance Indicators (KPIs)

| Metric | Target | Monitoring System | Reporting Owner |
| :--- | :--- | :--- | :--- |
| **Classification Coverage** | 98% of CMDB-registered data assets must have a verified classification. | ServiceNow Dashboard | Chief Privacy Officer |
| **Labeling Fidelity** | <1% tag deviation rate (a deviation is an object not tagged per its CMDB record). | AWS Config / Snowflake Tag Views | Data Custodian |
| **Restricted Data Encryption** | 100% of Restricted data in S3 must be encrypted with a customer-managed KMS key. | AWS Config Rule `ENCRYPTED-VOLUMES` | CISO |
| **Reclassification Cycle Time** | Average time from reclassification request to label application: < 14 days. | ServiceNow Report | VP of IT Operations |
| **Unauthorized Activity Detection** | Mean time to detection (MTTD) for DLP alerts on Restricted data: < 5 minutes. | CrowdStrike Falcon | SOC Manager |

### 7.3 Reporting Cadence

- **Monthly:** The Data Governance & Privacy business unit will generate an automated "Classification Compliance Scorecard" in Looker, pulling tag data from AWS via the Steampipe plugin and Snowflake ACCOUNT_USAGE views. This scorecard is distributed to all Data Stewards detailing their unlabeled assets.
- **Quarterly:** A formal report is presented by Dr. Klaus Weber to the AI Governance Committee, highlighting risks arising from unclassified data, shadow IT datasets, and the efficacy of privacy-enhancing technologies in maintaining classification.

## 8. Exception Handling and Escalation

### 8.1 Exception Requests

A temporary exception to the automated labeling or tier-specific handling requirements may be granted when compliance would demonstrably block a critical business function or when a legacy system is incompatible with automated tagging.

**8.1.1 Exception Request Procedure:**
1.  **Documentation:** The requesting party completes the "Data Classification Exception Request" form (F-CLASS-EXC-004) in ServiceNow. The form requires the specific control to be waived, the technical rationale, the business justification, and a compensatory safeguarding control proposal (e.g., "Instead of automated tag, asset will be in a dedicated secured AWS Account with manual access review").
2.  **Risk Scoring:** The CISO's Governance, Risk, and Compliance (GRC) team scores the exception on a 1-10 risk scale. Exceptions scoring above a 7 require a compensating control approved by the CISO.
3.  **Approval Authority:**
    - **Tier-Restricted Exception:** Requires joint written approval from the CISO (Rachel Kim) and General Counsel (Maria Gonzalez). These are valid for a maximum of 90 days.
    - **Tier-Confidential Exception:** Requires approval from the CISO and the relevant Data Steward. Valid for 180 days.
    - **Tier-Internal/Public:** Approved by the Data Steward alone.

### 8.2 Escalation for Non-Compliance

If a business unit or individual is found to be willfully circumventing data labeling requirements (e.g., by stripping metadata before export), the violation will be escalated through the following path:
1.  **Immediate Technical Containment:** The CISO will order the temporary suspension of the offending system's network connectivity.
2.  **Mandatory Disclosure:** The Chief Compliance Officer must be notified within 24 hours for determination of any regulatory reporting obligations.
3.  **Corrective Action:** The individual responsible and their direct manager will be enrolled in a mandatory "Data Governance and Security" refresher training assigned by HR within one week of the containment. Repeated violations will result in disciplinary action as per the Employee Code of Conduct.

## 9. Training Requirements

### 9.1 Mandatory Training Curriculum

Effective execution of this SOP relies on a trained workforce. Meridian mandates the following training tracks, delivered through the Workday Learning Management System (LMS).

### 9.2 Role-Specific Requirements

- **Meridian Data Classification Foundation (Course: MD-FND-101):**
    - **Audience:** All employees with access to Meridian corporate systems.
    - **Content:** The four classification tiers, identification of PHI/NPI, and the prohibition of public cloud sharing for Internal data.
    - **Frequency:** Annually.

- **Data Steward Governance Workshop (Course: MD-STEW-201):**
    - **Audience:** All formally designated Data Stewards.
    - **Content:** Use of the ServiceNow (F-CLASS-001, F-RECLASS-003) forms, mastering the regulatory overlay heat map tool, and advanced DS4P application logic.
    - **Frequency:** Semi-annually. Led by the VP of Data Governance.

- **Engineering Labeling & Custodian Pipelines (Course: MD-CUST-301):**
    - **Audience:** Data Custodians, Cloud Architects, DevOps Pipeline Engineers.
    - **Content:** CI/CD integration of the Meridian Labeling Engine (MLE), Terraform module specifications, AWS Config remediation rules, and SIEM log source integration.
    - **Frequency:** Quarterly, as part of the "Tech Talks" program, to address updates in API versions and new technical controls.

### 9.3 Non-Compliance Tracking

Training completion is tracked and reported monthly by the HR Transformation team. System access to Restricted data repositories is automatically gated behind the completion status of Course MD-FND-101. An Active Directory dynamic group (`DENY-UNTRAINED-USERS`) automatically revokes Okta push access for any user more than 30 days past their training due date.

## 10. Related Policies and References

- **SOP-DGP-002:** Data Retention and Destruction Schedule.
- **SOP-SEC-005:** Breach Response Plan and Incident Lifecycle.
- **SOP-AI-001:** AI Model Risk Management and Input Provenance (relating to SR 11-7 and EU AI Act compliance).
- **SOP-ENG-008:** Infrastructure-as-Code (Terraform) Management Standards.
- **External Standards:**
    - NIST Special Publication 800-53, Rev. 5: Security and Privacy Controls for Information Systems and Organizations.
    - NIST Special Publication 800-88, Rev. 1: Guidelines for Media Sanitization.
    - Federal Reserve SR Letter 11-7: Supervisory Guidance on Model Risk Management.
    - GDPR, Articles 4, 5, 13, 14, 30, 32, 35.
    - HIPAA Security Rule (45 CFR Part 164, Subparts C & D) and Breach Notification Rule (45 CFR § 164.400-414).
    - HL7 Data Segmentation for Privacy (DS4P) Implementation Guide, Release 2.

## 11. Revision History

| Version | Date | Author(s) | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2021-01-28 | K. Weber, P. Lin | Initial publication of Data Classification Policy. Defined three original tiers (Sensitive, Internal, Public). |
| 2.0 | 2022-08-15 | K. Weber, S. Torres | Major revision. Introduced "Restricted" as a new top tier to align with stricter DPA requirements from clients. Added the JSON-based Meridian Standard Label (MSL) schema in Section 5.3. Introduced AWS S3 tag enforcement architecture. |
| 3.0 | 2024-01-05 | K. Weber, A. Okafor | Update to incorporate HL7 DS4P attribute-level segmentation for MedInsight analytics. Added Section 5.2.1.5, mandating 7-year immutable audit logs for Restricted ePHI datasets. |
| 3.1 | 2024-04-30 | R. Kim | Altered Section 6.1.1 to include new CrowdStrike DLP policy templates and updated the SCP for TLS 1.3 enforcement. Reclassified container orchestration secrets under the technical custodian's scope. |
| 3.2 | 2024-07-23 | K. Weber, M. Gonzalez | Incorporation of EU AI Act Annex III compliance overlay. Added "High-Risk AI Output" as an explicit example of Tier 1 - Restricted. Updated Section 8.1 Exception Handling to require Legal approval for all Restricted tier exceptions. |
| 3.3 | 2025-12-01 | K. Weber | Annual review. Expanded Section 5.1 to include explicit decision tree nodes for HIPAA and SR 11-7. Updated Data Steward assignments. Added `sop_id` metadata to policy header. Minor formatting updates for consistency. |
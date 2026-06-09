---
sop_id: "SOP-DGP-016"
title: "Data Minimization Standards"
business_unit: "Data Governance & Privacy"
version: "2.3"
effective_date: "2025-11-05"
last_reviewed: "2026-12-25"
next_review: "2027-06-19"
owner: "Dr. Klaus Weber, Chief Privacy Officer / DPO"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Data Minimization Standards

**SOP-DGP-016 | Version 2.3**
**Owner:** Dr. Klaus Weber, Chief Privacy Officer / DPO
**Effective Date:** 2025-11-05

---

## 1. Purpose and Scope

### 1.1 Purpose

Meridian Health Technologies, Inc. (“Meridian”) processes vast quantities of sensitive data across its Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and Meridian SaaS Platform. This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for data minimization — the principle that Meridian shall collect, process, and retain only the minimum amount of personal data necessary to achieve a specified, legitimate purpose.

This SOP operationalizes the privacy-by-design and privacy-by-default principles embedded in our regulatory obligations and serves as the procedural backbone for ensuring that personal data, whether belonging to patients, providers, employees, or research subjects, does not proliferate unchecked across our systems.

### 1.2 Scope

This SOP applies to:

- **All Business Units**: Clinical AI, HealthPay Financial Services, MedInsight Analytics, IT Operations, Customer Operations, Human Resources, and any department that collects or processes personal data.
- **All Data Subjects**: Patients (including EU data subjects), healthcare providers, clinical trial participants, Meridian employees, contractors, and website visitors.
- **All Systems and Platforms**: Including but not limited to Snowflake data warehouses, PostgreSQL transactional databases, Apache Kafka event streams, Pinecone vector databases, SageMaker model training pipelines, Redis caching layers, and all downstream analytics environments.
- **All Processing Activities**: Collection, recording, storage, retrieval, consultation, use, disclosure by transmission, dissemination, alignment, combination, restriction, erasure, or destruction of personal data.
- **All Geographies**: All Meridian offices, including the United States (Austin headquarters), European Union (Berlin office), and any third-party processing locations where Meridian acts as data controller or data processor.

### 1.3 Out of Scope

This SOP does not override legally mandated retention periods, such as those required by FDA 21 CFR Part 11 for clinical trial data or IRS requirements for financial records. Where a legal obligation conflicts with minimization, the legal obligation prevails, and the conflict must be documented as a Standard Exception per Section 8.1.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|---|---|
| **Personal Data** | Any information relating to an identified or identifiable natural person. Includes direct identifiers (name, SSN, email) and indirect identifiers (IP address, device fingerprints, pseudonymous tokens where re-identification is possible). |
| **Protected Health Information (PHI)** | Individually identifiable health information held or transmitted by Meridian in its capacity as a Covered Entity or Business Associate under HIPAA. |
| **Data Minimization** | The principle that Meridian limits the collection, use, and retention of personal data to that which is adequate, relevant, and limited to what is necessary in relation to the purposes for which it is processed. |
| **Purpose Limitation** | The constraint that personal data collected for one purpose shall not be repurposed for an incompatible secondary purpose without explicit re-consent or a documented legal basis. |
| **Storage Limitation** | The requirement that personal data be retained only for as long as necessary to fulfill the original processing purpose, after which it must be securely anonymized, deleted, or archived with restricted access. |
| **Data Lifecycle** | The end-to-end journey of a data element from collection, through active processing and analytics, into restricted archival storage, and culminating in certified destruction. |
| **Privacy Impact Assessment (PIA)** | A mandatory, structured risk assessment conducted for any new project, system, or feature that involves personal data before development begins. Documented in the PIA Registry. |
| **DSAR** | Data Subject Access Request — a formal request from an individual exercising rights under GDPR or HIPAA. |
| **ARO** | Annual Review Obligation — the mandatory yearly audit of a data store’s minimization compliance. |
| **PIM** | Meridian’s internal Privacy Information Management System, built on a Snowflake backend with a Tableau frontend. |
| **K-Anonymity** | A statistical measure applied to de-identified datasets where any individual record is indistinguishable from at least K-1 other records. Meridian requires K ≥ 5 for released research datasets. |

---

## 3. Roles and Responsibilities

| Role | Responsibility | Accountable Party |
|---|---|---|
| **Data Subject** | The individual to whom the personal data relates. Meridian employees are Data Subjects in the HR context. | N/A |
| **Data Steward** | Assigned per data domain (Clinical, Financial, HR). Responsible for executing data minimization on their domain’s assets per the procedures in Section 5. A named individual per domain. | Chief Data Officer (CDO) |
| **Privacy Analyst** | Embedded within the Data Governance team. Conducts PIAs, reviews collection forms for minimization adherence, and maintains the Data Inventory. | Chief Privacy Officer (CPO) via Dr. Klaus Weber |
| **Engineering Lead** | Ensures technical implementation of minimization controls in code, pipelines, and infrastructure. Responsible for enforcing field-level collection limits. | VP of Engineering |
| **Chief Privacy Officer (CPO) / DPO** | Dr. Klaus Weber. Ultimate authority on interpretation of this SOP. Approves all Standard Exceptions related to GDPR and HIPAA minimization. Escalates non-compliance to General Counsel. | General Counsel |
| **General Counsel** | Maria Gonzalez. Approves all Policy Exceptions (extraordinary deviations) and adjudicates conflicts between legal retention mandates and minimization. | Board of Directors |
| **Internal Audit** | Independent team conducting semi-annual audits of minimization adherence. Reports findings to the Audit Committee. | Audit Committee Chair |

**RACI Matrix for Core Minimization Activities:**
- *P* = Performer, *A* = Accountable, *C* = Consulted, *I* = Informed

| Activity | Data Steward | Privacy Analyst | Engineering Lead | CPO / DPO | General Counsel |
|---|---|---|---|---|---|
| New Collection Request Review | C | P | C | A | I |
| Annual Data Review (ARO) | P | C | I | A | I |
| Deletion Execution | C | I | P | A | I |
| Exception Approval (Standard) | I | C | I | A | I |
| Exception Approval (Policy) | I | C | I | C | A |

---

## 4. Policy Statements

### 4.1 Collection Limitation

Meridian collects personal data only where it is directly necessary for the explicit, specified, and legitimate purpose communicated to the data subject. All collection forms — whether web-based enrollment in HealthPay, patient intake for a clinical AI study, or employee onboarding in Workday — must be reviewed and approved by a Privacy Analyst prior to deployment. The reviewer will challenge every field that is not demonstrably essential.

### 4.2 Purpose Specification and Binding

No dataset, data lake table, or analytics stream may be created without a registered, documented purpose in the Meridian Data Catalog. Repurposing data from a clinical context for financial modeling, or vice versa, is prohibited without a full PIA and, where required, re-notification to the Data Subject.

### 4.3 Proportionate and Adequate Processing

Once collected, personal data shall not be processed in a manner that is excessive relative to the stated purpose. For example, an analytics model predicting hospital readmission risk may use age and diagnostic codes but shall not ingest full free-text clinical notes unless the model’s accuracy is provably inadequate without them and a PIA approves the inclusion.

### 4.4 Storage Limitation with Automated Enforcement

Meridian assigns a maximum retention period to every data asset. At the end of that period, the PIM system (Section 6.2) triggers an automated retention review. No personal data may be retained beyond its assigned period without a documented, approved exception. Data for which the retention period has expired and no exception is approved must be irreversibly deleted or rendered fully anonymous (K-anonymity ≥ 5) within 30 calendar days of expiration.

### 4.5 Periodic Review

All active data stores containing personal data are subject to an Annual Review Obligation (ARO), conducted by the respective Data Steward. The ARO must re-justify the necessity of retention for each data category in the store. Failure to complete an ARO within 90 days of its scheduled date results in automatic, enforced deletion or archival, at the discretion of the CPO.

---

## 5. Detailed Procedures

### 5.1 Procedure: New Data Collection Request (NDCR)

This procedure is triggered whenever any Meridian team plans to collect personal data through a new or modified form, API endpoint, application, clinical device, or research instrument.

1.  **Requester Initiates NDCR in ServiceNow**: The Business Unit Lead or Product Manager navigates to the “Privacy—New Data Collection” request in ServiceNow and completes the NDCR form. The form requires:
    -   Proposed Collection Title
    -   Specific, enumerated list of *every* proposed data element/field
    -   Justification for *each* element, linking it to a legitimate purpose
    -   Data Subject category (Patient, Provider, Employee, etc.)
    -   Proposed Retention Period (from collection to destruction)
2.  **Privacy Analyst Review**: Within 5 business days, the assigned Privacy Analyst reviews the NDCR. The Analyst applies the principle of strict necessity:
    -   **Is each field essential to the purpose?** The Analyst cross-references the justification against the product requirements.
    -   **Could the purpose be achieved with less granular data?** E.g., “Age” or “Age Range” instead of “Date of Birth”; “Zip Code” instead of “Full Address.”
    -   **Any Indirect Identifiers?** IP addresses, device IDs, or cookies logged by default must be justified if they relate to an identifiable individual.
3.  **Challenge and Re-Specification**: The Analyst provides a formal written response in the ServiceNow ticket, flagging any fields that fail the necessity test. The Requester may either:
    -   **Accept Removal**: Update the NDCR and remove the field.
    -   **Provide Override Justification**: Provide a detailed, written argument for why the field is functionally essential and no less-granular alternative exists.
4.  **CPO Decision**: The Analyst and CPO (Dr. Klaus Weber) review the Override Justification and issue a final determination within 5 business days. CPO decision is final.
5.  **Engineering Implementation**: Once approved, the final, approved list of fields becomes a locked specification for the Engineering Lead to implement. The Engineering team must not collect any field not on the approved list.
6.  **Post-Deployment Audit**: 30 days after deployment, Internal Audit selects a random sample of collections to verify that the live system is collecting only approved fields.

### 5.2 Procedure: Annual Review Obligation (ARO)

The ARO procedure is the primary mechanism for enforcing storage limitation. It applies to every data store in the Data Inventory (e.g., Snowflake schemas, S3 buckets, application databases).

1.  **Scheduling**: On the 1st of each month, PIM generates a report of all AROs due, based on the data store’s `last_aro_date` field. The ARO is due exactly 365 days from the last completion date. Data Stores with a null `last_aro_date` are considered immediately due.
2.  **Data Steward Preparation**: The assigned Data Steward receives an automated ServiceNow task 60 days before the due date. The Steward must prepare a report containing:
    -   Current list of all data categories/tables in the store.
    -   Current volume (record count and size in GB) for each.
    -   Original collection purpose from the Data Catalog.
    -   An audit log of *all* internal accesses to the data store in the preceding 12 months, pulled from AWS CloudTrail and Snowflake Access History.
3.  **The “Necessity Re-Test” Meeting**: The Data Steward convenes a 30-minute meeting with:
    -   The assigned Privacy Analyst
    -   The relevant Business Unit Lead
    -   Agenda: For each data category, answer three questions:
        1.  **Purpose Continuation**: Is the original purpose still active and relevant?
        2.  **Access Validation**: Has the data been accessed for that purpose in the past 12 months? Data that has not been accessed for its stated purpose is presumed unnecessary.
        3.  **Retention Justification**: Is the current retention period still justifiable, or can it be shortened?
4.  **Disposition Determination**: For each category, the Steward and Privacy Analyst determine one of the following:
    -   **Retain as Is**: Purpose is active, access is validated, retention period is minimal. Record the justification.
    -   **Reduce Retention**: The current retention period is excessive for the active purpose. Set a new, shorter retention date. PIM records this new date.
    -   **Migrate to Cold Archive**: The purpose is complete, but a legal or audit obligation requires retaining the data in a non-accessible state for X months. Data must be moved to a restricted-access `archive` bucket with no direct query access.
    -   **Flag for Deletion**: Purpose is complete and no valid legal hold exists. Data is flagged for immediate disposal per Procedure SOP-DGP-017 (Data Retention and Deletion Procedures).
5.  **Sign-Off and Logging**: The Data Steward and Privacy Analyst sign off on the ARO in ServiceNow. The ARO form, dispositions, and justifications are digitally signed and stored immutably as a compliance artifact for six (6) years from the date of signing.

### 5.3 Procedure: De-Identification Process for Research

When clinical data from MedInsight Analytics is requested for an AI/ML research project that does not require direct identifiers, the following minimization-through-de-identification procedure is mandatory.

**Step 3.1 (Safe Harbor Method - HIPAA §164.514(b)(2))** : A Data Steward from the Clinical domain and a Privacy Analyst jointly run a script against the proposed dataset to verify the removal of all 18 HIPAA identifiers. This includes names, all geographic subdivisions smaller than a State (except the initial three digits of a zip code if certain population thresholds are met), all date elements (except year) directly related to an individual, telephone numbers, fax numbers, email addresses, Social Security numbers, medical record numbers, health plan beneficiary numbers, account numbers, certificate/license numbers, vehicle identifiers and serial numbers including license plates, device identifiers and serial numbers, URLs, IP addresses, biometric identifiers including finger and voice prints, full-face photographs and any comparable images, and any other unique identifying characteristic or code, except as permitted for re-identification.

**Step 3.2 (Expert Determination - HIPAA §164.514(b)(1))** : For complex, high-dimensional data (like multi-omic profiles or free-text notes used for NLP training), a qualified external statistician, approved by the CPO, applies generally accepted statistical and scientific principles to determine that the risk is very small that the information could be used, alone or in combination with other reasonably available information, to identify an individual. The methodology and results of this analysis are documented in a formal Expert Determination report.

**Step 3.3 (GDPR Re-Identification Risk Assessment)** : For datasets containing EU resident data, the Privacy Analyst performs an additional, specific re-identification risk assessment considering the “means likely reasonably to be used” by a motivated intruder. The dataset is approved for research use only if the risk is deemed “Low.”

**Step 3.4 (Controlled Release)** : The approved de-identified dataset is released not as a direct database export, but via a controlled, audit-logged Snowflake secure view or a pre-signed, time-limited S3 URL. The receiving researcher must acknowledge a Data Use Agreement (DUA) that legally prohibits re-identification attempts.

### 5.4 Procedure: Privacy Notice Content Generation

This procedure is invoked by the Privacy Operations team when a new or materially modified processing activity requires updates to public-facing notices.

1.  **Activity Mapping**: The Privacy Analyst maps the approved data elements and purposes from the NDCR (or ARO) into the Meridian Data Processing Inventory, a structured YAML repository.
2.  **Notice Template Update**: The Analyst translates the inventory entries into plain-language updates for the applicable notice template. For each processing activity, the notice must state the specific categories of personal data and the specific purpose.
3.  **Review and Publication**: The updated notice draft is reviewed by the CPO for legal accuracy and by the Product Manager for readability. The final notice is published to the relevant Meridian platform (e.g., the HealthPay patient portal, the MedInsight researcher dashboard) and the version hash is logged.
4.  **Record of Notice**: A timestamped PDF copy of the specific notice version presented to users is archived in PIM for a period of seven (7) years, indexed against the corresponding ServiceNow NDCR ticket.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls: Collection

| Control ID | Control Description | Implementation Tool |
|---|---|---|
| **TCL-DM-01** | **Strict Field Validation**: API endpoints for all user-facing applications (HealthPay, MedInsight portal) use strict, allow-listed JSON schemas. Any field sent by the client not in the approved schema is silently discarded server-side, and an alert is written to an `excess_data` security log. | AWS API Gateway Request Validation, integrated with Meridian’s WAF. |
| **TCL-DM-02** | **Default Minimum Logging**: All application-level logs (CloudWatch, ELK stack) are configured, by default, to hash or truncate potential Personal Data fields (e.g., query strings containing email addresses). Full logging for debugging requires an approved, 48-hour, auto-expiring exception ticket. | Fluent Bit filter plugins with a central rules file. |
| **TCL-DM-03** | **Sensor Data Minimization**: Medical devices (under CE marking and MDR) that stream data send only validated, clinically-necessary sensor readings, as configured by the Clinical AI Platform engineering team. Raw diagnostic telemetry containing device serial numbers is segregated at the edge. | AWS IoT Core Rule Engine and AWS Greengrass edge processing. |

### 6.2 Technical Controls: Storage and Processing

| Control ID | Control Description | Implementation Tool |
|---|---|---|
| **TCL-DM-04** | **Automated Retention Lock**: Every S3 bucket and Snowflake table containing personal data is tagged with an `expiration_date` metadata tag. The PIM system uses a nightly AWS Lambda function to scan for any object where `current_date > expiration_date`. Non-compliant objects are immediately moved to a `quarantine` bucket with zero user permissions, pending an incident review. | AWS Lambda, S3 Object Tagging, Snowflake Table Comments. |
| **TCL-DM-05** | **Tokenization**: Primary identifiers (e.g., `member_id` in HealthPay) are isolated in a single, hardened `identity_vault` PostgreSQL database. All downstream analytics systems use a system-generated, irreversible `derived_id` token for linking records, eliminating direct identifiers from the analytics environment. | Proprietary vault service, managed by IT Operations under SOP-IDM-004. |
| **TCL-DM-06** | **Differential Privacy Budget**: For internal aggregate analytics dashboards that expose population statistics to Business Users (e.g., average readmission rate), a differential privacy library adds calibrated noise (ε = 1.0). The CPO manages the privacy budget, and a dashboard displays the current ε remaining for the fiscal year. | Open-source DP library integrated into Tableau via a Hyper API extension. |

### 6.3 Administrative Controls

- **Data Processing Inventory (DPI)**: The Privacy team maintains a comprehensive, living inventory of all personal data processing activities, which is the authoritative source for this SOP’s enforcement. It maps Purposes to Data Categories to Retention Periods to Assets.
- **PIAs are Mandatory Pre-Checkpoints**: No architecture review board (ARB) meeting can approve a new system or major feature without a completed and approved PIA-ID. The PIA must include a specific section on how the design achieves data minimization.
- **Third-Party Risk Assessments**: Before any personal data is shared with a vendor or research partner, the Vendor Risk Management team conducts a review that specifically scrutinizes the partner's own data minimization practices and their alignment with Meridian's standards.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The effectiveness of this SOP is measured against the following KPIs, tracked monthly in the Privacy & Security Dashboard:

| KPI Name | Metric Definition | Target |
|---|---|---|
| **COLL-01: Collection Necessity Rate** | % of new NDCRs where >90% of initially proposed fields are approved without challenge and re-specification. (Higher is better). | ≥ 95% |
| **STOR-01: ARO Overdue Rate** | % of data stores with a scheduled ARO that is >30 days past due. | 0% |
| **STOR-02: Excess Retention Rate** | % of personal data objects in a `quarantine` bucket due to exceeding their retention lock, relative to total objects tracked. | < 0.1% |
| **STOR-03: Stale Data Index** | % of active data stores with >80% of their records unaccessed for >365 days, identified during AROs. | < 5% of all active data stores |
| **PROC-01: PIA-to-Live Cycle Time** | Median days from NDCR approval to PIA final approval and code deployment. | ≤ 30 business days |
| **DSAR-01: Search Complexity** | Average number of distinct data stores that must be searched to fulfill a single DSAR. A lower number indicates better minimization and less data sprawl. | ≤ 5 data stores per DSAR |

### 7.2 Reporting Cadence

- **Monthly Operational Report**: A Privacy Analyst generates an automated Tableau report from PIM data, focusing on KPIs COLL-01, STOR-01, and STOR-02. Reviewed by the CPO.
- **Quarterly Governance Review**: The CPO presents the full KPI dashboard, including trends and analysis of stale data indices, to the Data Governance Steering Committee, co-chaired by the Chief Data Officer and the Chief Information Security Officer (CISO).
- **Semi-Annual Audit Report**: Internal Audit conducts a detailed audit of a random sample of AROs, NDCRs, and exception tickets. Their findings, particularly on ARO sign-off integrity and DSAR search complexity, are reported directly to the Audit Committee of the Board.

---

## 8. Exception Handling and Escalation

### 8.1 Standard Exceptions

Standard exceptions are deviations from procedure where the policy principle (minimization) is not violated, but a conflicting obligation exists.

**Common Scenarios**:
- A mandatory legal hold (from General Counsel) requires freezing deletion of specific data relevant to active litigation.
- FDA’s 21 CFR Part 11 requires retention of full clinical trial master files for a period exceeding the default analytics retention period.
- A Data Subject explicitly requests, via a verified DSAR, that their data be retained for a period longer than the standard for a specific, stated purpose (e.g., ongoing patient portal access).

**Process**:
1.  Data Steward files a “Standard Exception—Legal/Regulatory Hold” request in ServiceNow, attaching the legal hold notice or regulatory citation.
2.  The CPO reviews and approves within 3 business days.
3.  The approved exception sets a new, documented `legal_hold_expiration` date on the affected data objects, overriding the standard `expiration_date`. All automated deletion jobs for these objects are suspended until that date.
4.  Standard exceptions are reviewed quarterly by the General Counsel’s office to ensure they remain valid.

### 8.2 Policy Exceptions

Policy exceptions are requests to explicitly violate the minimization principle, for example, collecting a non-essential data field because a product manager believes it will be useful for an unspecified future purpose (“data hoarding”).

**Approval Authority**: Policy exceptions require the joint, documented approval of the Chief Privacy Officer (Dr. Klaus Weber) and the General Counsel (Maria Gonzalez). No VP or Product Manager has authority to grant a Policy Exception.

**Escalation Path for Unapproved Deviations**: Any Privacy Analyst, Data Steward, or Engineer who discovers an unapproved deviation — such as a shadow IT system collecting unauthorized data — is obligated to follow this escalation path immediately:
1.  **Immediate Report**: Notify direct manager and the CPO’s office via a “Privacy Incident—Unauthorized Collection” ticket within 24 hours of discovery.
2.  **CPO Triage**: The CPO or delegate triages the incident within 48 hours. Immediate technical measures, such as shutting down a collection endpoint, may be mandated.
3.  **General Counsel Involvement**: If the unauthorized collection is significant in volume or sensitivity, or appears willful, General Counsel is engaged immediately to assess regulatory reporting obligations and legal exposure.
4.  **Remediation Plan**: Within 5 business days, the responsible Business Unit must produce a remediation plan, approved by the CPO, to either retroactively justify the collection with a PIA (unlikely) or irreversibly delete the data.

---

## 9. Training Requirements

All training is tracked through the Meridian Learning Management System (LMS), `Compass`.

| Training Module | Target Audience | Frequency | Module ID |
|---|---|---|---|
| **Privacy at Meridian: Core Principles** | All employees, contractors, and interns on day 1, then annually. Covers the fundamentals of GDPR and HIPAA, including the policy of data minimization. | Annual | PRIV-100 |
| **SOP-DGP-016: Minimization in Practice** | All members of the Engineering, Product, Clinical AI, and Data Governance teams. Practical exercises on writing compliant NDCRs and conducting AROs. | Biennially | PRIV-201 |
| **De-Identification Workshop** | Data Stewards (Clinical & Research), Privacy Analysts, and AI/ML Researchers. A hands-on lab using the Safe Harbor script and the Expert Determination framework against synthetic Meridian datasets. | Biennially | PRIV-301 |
| **“Privacy Trap” Series: The Unnecessary Field** | Product Managers and UX Designers. A short, 15-minute micro-learning module simulating a feature design meeting where unnecessary data fields are proposed. Completion required before gaining access to the NDCR form in ServiceNow. | Once, with annual refresher | PRIV-102 |

**Training Effectiveness Measurement**: Following each annual training, the Privacy team will analyze a correlation metric: **“Training Completion Status vs. Number of Challenges Received on NDCR Submissions.”** A persistent high-challenge rate from a fully-trained team may trigger targeted, in-person coaching.

---

## 10. Related Policies and References

**Internal Meridian Policies**:

| SOP ID | Policy Name | Relationship |
|---|---|---|
| SOP-DGP-001 | Data Governance Charter | Establishes overarching governance bodies. |
| SOP-DGP-005 | Privacy Impact Assessment Standards | Mandatory procedure for PIA, referenced herein. |
| SOP-DGP-017 | Data Retention and Deletion Procedures | Specifies secure deletion methods and logging. |
| SOP-SEC-022 | Access Control Policy | Defines “least privilege” access to minimized data. |
| SOP-DGP-025 | Data Subject Access Request Handling | Process fulfilled more efficiently due to minimization. |
| SOP-IDM-004 | Identity Vault Management | Controls for the secure tokenization vault. |

**External References**:
-   Regulation (EU) 2016/679 (General Data Protection Regulation)
-   Health Insurance Portability and Accountability Act of 1996 (HIPAA) Privacy and Security Rules (45 CFR Parts 160, 162, and 164)
-   FDA 21 CFR Part 11 (Electronic Records; Electronic Signatures)
-   MDCG 2019-11: Guidance on Qualification and Classification of Software in Regulation (EU) 2017/745 (MDR)

---

## 11. Revision History

| Version | Effective Date | Author(s) | Summary of Changes |
|---|---|---|---|
| 2.3 | 2025-11-05 | Dr. Klaus Weber, CPO | Major update: Incorporated ARO Procedural changes per 2025 Internal Audit finding. Added `STOR-03: Stale Data Index` KPI. Updated De-identification procedure to formalize Expert Determination workflow for NLP. Updated related policies list. |
| 2.2 | 2025-06-15 | Dr. Klaus Weber, L. Chen (Privacy Analyst) | Minor revision: Modified KPI `COLL-01` target from 98% to 95%. Updated ServiceNow NDCR form layout reference. Added AWS IoT Core to sensor controls TCL-DM-03 following MDR product launch. |
| 2.1 | 2024-11-01 | Dr. Klaus Weber, J. Singh (Data Governance) | Updated role of “Data Steward” from functional to named role. Clarified PIA integration for MDR compliance. Added Section 8 Exception Handling specificity for FDA 21 CFR Part 11 holds. |
| 2.0 | 2024-04-19 | Dr. Klaus Weber, M. Gonzalez (Legal) | Major overhaul: Moved from a descriptive policy to a procedural standard with measurable KPIs. Introduced NDCR and ARO formal procedures. Aligned controls with the MedInsight and HealthPay platform separation. Integrated Snowflake and AWS S3-based automated enforcement. |
| 1.2 | 2023-08-22 | M. Gonzalez, Legal | Introduced initial definitions for de-identification. Added references to then-draft GDPR Article 25 principles. |
| 1.0 | 2023-03-01 | M. Gonzalez, Legal | Initial document creation. |
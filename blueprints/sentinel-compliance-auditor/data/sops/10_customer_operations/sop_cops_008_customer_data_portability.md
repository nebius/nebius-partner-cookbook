---
sop_id: "SOP-COPS-008"
title: "Customer Data Portability"
business_unit: "Customer Operations"
version: "3.5"
effective_date: "2025-07-13"
last_reviewed: "2026-07-09"
next_review: "2027-01-02"
owner: "Michael Chang, VP of Customer Operations"
approver: "Robert Liu, VP of Financial Services"
classification: "Internal"
regulations:
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Customer Data Portability

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, responsibilities, and operational workflows for fulfilling customer data portability requests across Meridian Health Technologies, Inc. products and business lines. The purpose of this SOP is to:

1.  Ensure Meridian's compliance with data portability obligations under the General Data Protection Regulation (GDPR) and other applicable data protection frameworks in jurisdictions where Meridian operates.
2.  Define a standardized, auditable, and efficient process for responding to verified data subject access and portability requests (DSARs) originating from individual end-users, patient guarantors, and authorized representatives of covered entities.
3.  Establish technical specifications for portable data formats, transmission mechanisms, and quality assurance to ensure that exported data is structured, commonly used, and machine-readable.
4.  Delineate clear roles, accountability, and escalation paths between Customer Operations, Engineering, Privacy, and Information Security teams to facilitate seamless request fulfillment.

### 1.2 Scope

This SOP applies to all employees, contractors, and third-party service providers of Meridian Health Technologies, Inc. who are involved in the ingestion, processing, or fulfillment of data portability requests. The scope encompasses:

- **In-Scope Data Subjects:**
    - Identified or identifiable natural persons whose personal data has been provided to Meridian and is undergoing processing by automated means.
    - Specific emphasis is placed on EU data subjects under GDPR jurisdiction, as identified by residency, citizenship, or location data captured during service delivery.
    - Patients, healthcare provider staff users, and individual borrowers/guarantors within the HealthPay Financial Services ecosystem.

- **In-Scope Systems and Products:**
    - **MedInsight Analytics:** All patient-level, structured data elements contributed by the data subject or the covered entity on their behalf.
    - **HealthPay Financial Services:** Transactional history, payment instrument metadata, lending application data, and consumer credit profile data provided by the data subject.
    - **Clinical AI Platform:** Input data directly provided by a clinician user about a patient, where the patient is the data subject. This excludes derived model weights, proprietary inference logic, and de-identified aggregated datasets which constitute Meridian Intellectual Property (IP).
    - **Meridian SaaS Platform:** User profile metadata, access control lists, and configuration settings stored in the identity and access management (IAM) layer.

- **Out of Scope:**
    - Data that has been fully anonymized and is no longer reasonably attributable to an identifiable individual, verified by statistical analysis approved by Dr. Klaus Weber, Chief Privacy Officer / DPO.
    - Internal corporate records, unless they contain personal data undergoing processing by automated means and provided by the data subject.
    - Trade secrets and intellectual property as rigorously defined by Maria Gonzalez, General Counsel, in the IP Classification Register (refer to SOP-SEC-015).
    - Data portability requests from corporate entities (B2B) that do not contain personal data of individuals.

### 1.3 Applicability

This SOP is binding for Meridian operations in North America (United States, Canada) and the European Union (specifically operations out of London and Berlin offices, and cloud infrastructure hosted in eu-west-1). Any conflict between this SOP and local statutory requirements must be escalated immediately to the Chief Compliance Officer, Thomas Anderson, and the Global Privacy Office.

---

## 2. Definitions and Acronyms

| Term | Definition |
| :--- | :--- |
| **Data Subject** | An identified or identifiable natural person to whom personal data pertains. |
| **Data Portability** | The right of a data subject to receive their provided personal data in a structured, commonly used, and machine-readable format, and to transmit that data to another controller. |
| **DSAR** | Data Subject Access and Portability Request. A formal request invoking rights under GDPR Chapter 3. |
| **Machine-Readable Format** | A file format structured so that software applications can easily identify, recognize, and extract specific data, including individual facts and their internal structure (e.g., CSV, JSON, XML, Parquet). |
| **Verification Credential** | A set of attributes used to confirm the identity of the requestor, including government-issued photo ID, biometric verification via Okta Verify, or knowledge-based authentication (KBA) questions derived from HealthPay financial history. |
| **PHI** | Protected Health Information, as defined by HIPAA. |
| **IP** | Intellectual Property, specifically Meridian’s proprietary algorithms, model weights, risk scores, and inference logic. |
| **DPO** | Data Protection Officer (Dr. Klaus Weber). |
| **SLA** | Service Level Agreement. |
| **JSON** | JavaScript Object Notation. |
| **CSV** | Comma-Separated Values. |
| **NDJSON** | Newline Delimited JSON. |

---

## 3. Roles and Responsibilities

The following RACI matrix delineates the responsibilities for the Data Portability process.

| Role / Title | Responsibility Description | RACI (R, A, C, I) |
| :--- | :--- | :--- |
| **Data Subject** | Submits the verified request. Provides necessary identity credentials. | R |
| **VP of Customer Operations (Michael Chang)** | Ultimate process owner. Approves SLA exceptions and major process design changes. | A |
| **Customer Operations Specialist (Tier 1)** | Intake, initial verification, and logging of DSARs in ServiceNow. Communication of timelines. | R |
| **Chief Privacy Officer / DPO (Dr. Klaus Weber)** | Regulatory interpretation, complex case review, Data Protection Impact Assessment (DPIA) advisory, and final approval on data scope for ambiguous requests. | C, A |
| **VP of Engineering (David Park)** | Responsible for the technical execution of data extraction scripts and maintaining the Data Export API. | C |
| **Data Engineering Team (Export Squad)** | Executes secure data extraction from Snowflake, PostgreSQL, and MongoDB. Validates data completeness against source schemas. | R |
| **CISO (Rachel Kim)** | Approves the secure transmission mechanism. Ensures encryption standards compliance (AES-256, TLS 1.3). | I, C |
| **General Counsel (Maria Gonzalez)** | Determines boundaries of trade secrets and IP. Adjudicates redaction of commercially sensitive information. | C |
| **VP of Financial Services (Robert Liu)** | Approver of this SOP. Ensures SR 11-7 implications for credit data portability are addressed. | A, I |

---

## 4. Policy Statements

Meridian Health Technologies is committed to empowering data subjects with control over their personal data. The following policy statements govern all data portability activities:

1.  **Right to Portability:** Meridian acknowledges the right of data subjects to receive their personal data, which they have provided to a controller, in a structured, commonly used, and machine-readable format.

2.  **Scope of Exportable Data:** The export package will include data actively and knowingly provided by the data subject (e.g., patient intake forms, payment transaction history, chat logs with Meridian virtual agents, and observations generated by the user during use of the Clinical AI Platform). It excludes derived data, enriched data, and Meridian proprietary risk scores, unless such derived data constitutes personal data inextricably linked to the provided data and not protected by trade secret law, as determined by General Counsel.

3.  **Format Standardization:** The primary export format is JSON or NDJSON for nested data structures (e.g., patient history) and CSV for tabular transaction logs. Metadata schemas, explaining the structure of the export, will be provided in a companion `README.md` file.

4.  **Charge Policy:** Generally, data portability requests will be fulfilled free of charge. However, under Article 12(5) of the GDPR, Meridian reserves the right to charge a reasonable administrative fee or refuse to act on manifestly unfounded or excessive requests, particularly repetitive requests within a rolling 12-month period. Any decision to charge a fee must be authorized by the DPO.

5.  **Direct Transmission:** Where technically feasible and requested by the data subject, Meridian will transmit the personal data directly to another controller. The receiving endpoint must pass a security assessment conducted by the CISO's office to prevent data proliferation to unauthorized third parties.

6.  **Data Completeness:** Meridian commits to providing all in-scope data points existing within the identified Production systems (Snowflake, Kafka event store, MongoDB) at the time of request processing. The extraction process does not guarantee the re-formatting or re-creation of data fields that were not captured during the original data collection event.

---

## 5. Detailed Procedures

This section outlines the step-by-step operational workflow, from intake to closure.

### 5.1 Intake and Identity Verification

1.  **Channel Identification:**
    - All DSARs must be directed to the centralized intake point: `privacyportal.meridian.tech` (managed via DataGrail) or via encrypted email to `dsar@meridian.tech`.
    - Requests received via unauthorized channels (e.g., direct DMs to support staff via LinkedIn) must be redirected to the official channel. Staff must not process requests received outside the official ticketing system.

2.  **Ticket Generation:**
    - Upon receipt, the DataGrail platform automatically generates a ServiceNow ticket under the category `[DSAR-PORTABILITY]`.
    - The requester receives an automated acknowledgment via their provided email address within 4 business hours.

3.  **Identity Verification (Tier 1):**
    - Customer Operations Specialist verifies the requestor’s identity against the master data profile.
    - **High Confidence Match:** If the email matches a verified user account in Okta, a push notification to Okta Verify is sent for biometric/passcode confirmation.
    - **Low Confidence Match:** If the requester is not an active platform user (e.g., former patient), a manual identity verification process is triggered.
        - Requestor must upload a government-issued ID and a utility bill through the portal.
        - Specialist conducts a visual comparison and KBA challenge derived from the HealthPay transaction history (e.g., "Confirm the amount of your last payment to Meridian HealthPay for March 2026").
    - If verification fails twice, the request is put on hold and escalated to the Privacy Team for validation.

### 5.2 Data Scope Definition and Cataloging

Once identity is verified, the Data Engineering Export Squad initiates the data scoping phase using the Meridian Data Catalog (powered by Atlan).

1.  **Profile Linkage:**
    - The Data Engineer queries the Golden Record Linkage Service (GRLS) using the verified Global Unique Identifier (GUID) to discover all data nodes linked to the subject across MedInsight, HealthPay, and Clinical AI.
2.  **Scope Determination:**
    - **HealthPay Data:** Includes `transaction_history`, `payment_method_tokens`, `loan_application_submissions`, and `authorization_consents`. Derived risk scores are automatically filtered out by a tag-based exclusion policy in the extraction script.
    - **Clinical AI Data:** Includes input prompt text, uploaded clinical image metadata (not the proprietary diagnostic overlay), and adverse event reporting forms submitted by the clinician.
    - **MedInsight Data:** Includes patient demographics, patient-generated outcome measures, and care history logs.
3.  **Conflict Resolution:**
    - If a data object is flagged as "Mixed IP/Derived," the script quarantines the object. General Counsel (Maria Gonzalez) and the DPO receive an automated Slack notification in `#legal-dsar-review` to adjudicate within 3 business days.

### 5.3 Extraction and Formatting

The extraction is automated via a Parametrized Kubeflow Pipeline (`dsar-export-v3.5`).

1.  **Pipeline Execution:**
    - The Export Squad triggers the pipeline via the Meridian MLOps console, passing the GUID and the authorized data scope manifest.
    - The pipeline executes federated queries against Snowflake (`PROD_SNOWFLAKE.ANALYTICS`), PostgreSQL (`PROD_PAYMENTS`), and MongoDB (`CLINICAL_DOCS`).

2.  **Formatting Standards:**
    - **Tabular Data (CSV):** Transaction ledgers and claims history are exported in UTF-8 encoded CSV with header rows. Commas within data fields are escaped with standard string quoting.
    - **Structured Data (JSON):** Patient profiles, assessment data, and interaction logs are exported as a single NDJSON file per data source, enabling streamability.
    - **Metadata:** A `SCHEMA_MANIFEST.json` file is auto-generated describing field types, null values, and relationship keys for each export file.

3.  **Data Completeness Check:**
    - A checksum script compares the row count and column hash of the extracted CSV flat files against the source tables.
    - If the deviation is >0%, the pipeline halts and a manual investigation is triggered by PagerDuty alert (`#dsar-alerts`).

### 5.4 Data Package Assembly and Encryption

1.  **Package Assembly:**
    - All exported files are compressed into a single `.tar.gz` archive using standard gzip compression. The archive is named `[YYYY-MM-DD]_[GUID]_DataExport.tar.gz`.
2.  **Encryption Protocol:**
    - The archive is encrypted using AES-256-GCM.
    - The encryption key is generated per-request via HashiCorp Vault Transit Engine.
    - The encrypted package is stored in a temporary, dedicated AWS S3 bucket (`meridian-dsar-temp-eu-west-1`) with a lifecycle policy for automatic deletion after 14 days.

### 5.5 Delivery and Post-Delivery

1.  **Direct Download (Primary Method):**
    - A time-limited, pre-signed S3 URL is generated (validity: 72 hours).
    - The link is delivered to the verified requestor via the DataGrail Secure Link portal.

2.  **Direct Transmission (Secondary Method):**
    - If the data subject requests direct transmission to a third-party controller, the third party must provide an API endpoint or SFTP server details.
    - The CISO team conducts a "Trusted Endpoint Assessment" (TEA).
    - **Pre-Requisites for Third-Party Reception:** The receiving third party must demonstrate SOC 2 Type II certification or equivalent, have a published privacy policy, and sign a "Data Receiver Acknowledgement" agreement which disclaims Meridian liability for data integrity post-transfer.

3.  **Closure:**
    - Upon successful delivery confirmation (portal download log or HTTP 200 response from third-party endpoint), the ServiceNow ticket is closed.
    - The S3 object retention timer begins; data is cryptographically shredded after 14 days.

### 5.6 Response Timelines

- **Standard Fulfillment Target:** Meridian aims to fulfill all verified portability requests within **45 calendar days** from the date of successful identity verification.
- **Complexity Extension:** For complex requests involving multiple business lines and mixed IP/data adjudication, the response timeline may extend to **60 calendar days**.
- **Communication Protocol:** If the 45-day timeline cannot be met, Customer Operations must notify the data subject before the 30th day, explaining the reasons for the delay.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

- **Segregation of Duties:** The identity verification role (Customer Operations) is logically separated from the data extraction role (Data Engineering) in ServiceNow and AWS IAM.
- **Legal Advisory Trigger:** If a data subject threatens litigation regarding the scope of exported data, all technical work must pause, and the case must be frozen pending General Counsel review.
- **Manual Override Logging:** Any manual execution of a script, or ad-hoc SQL query used to supplement the automated pipeline, must be logged in the `dsar_manual_intervention` Snowflake table with a justification narrative.

### 6.2 Technical Controls

- **Data Minimization in Transit:** The extraction pipeline applies column-based masking policies defined in AWS KMS before compression, ensuring that data categories tagged as `INTERNAL_MERCHANT_SECRETS` are never exported.
- **Endpoint Validation:** The Trusted Endpoint Assessment (TEA) script validates the receiving server’s SSL certificate chain against the Meridian internal CA before initiating a POST request in the direct transmission flow.
- **Malware Scanning:** The final `.tar.gz` export package is scanned by CrowdStrike Falcon Sandbox before the download link is activated for the data subject.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| Metric | Target | Calculation | Monitoring Tool |
| :--- | :--- | :--- | :--- |
| **Request Volume** | Monitor only | Total DSAR intakes per quarter | ServiceNow Dashboard |
| **Verification Rate** | ≥ 95% | % of requests successfully verified against received | DataGrail Analytics |
| **Timeline Compliance (45-C Day)** | ≥ 90% | % of requests completed within 45 calendar days of verification | ServiceNow SLAs |
| **Data Completeness Accuracy** | 100% | % of requests with 0% checksum deviation | Datadog Custom Metric |
| **Customer Satisfaction (CSAT)** | ≥ 4.5 / 5.0 | Post-closure survey rating of "Clarity of Data Provided" | Medallia Survey |

### 7.2 Reporting Cadence

- **Monthly Operations Report:** VP of Customer Operations reviews open and overdue DSARs in the monthly QBR.
- **Quarterly Audit Report:** The Compliance team (Thomas Anderson) presents a report to the Board AI Governance Committee, detailing volume trends, systemic root causes for delays, and regulatory horizon scanning.

---

## 8. Exception Handling and Escalation

### 8.1 Exceptions to Standard Process

Any deviation from the standard process (e.g., bypassing the DataGrail portal, using a mobile storage device for highly restricted network environments) is prohibited unless a formal Exception Request is approved.

- **Exception Request Form:** Requester must submit a ticket in ServiceNow using the `[DSAR-EXCEPTION]` template, specifying the technical constraint, the proposed alternative, and compensating controls.
- **Approval Matrix:**
    - **Technical Exceptions (e.g., format change):** Requires approval from VP of Engineering (David Park).
    - **Policy Exceptions (e.g., fee waiver for excessive request):** Requires joint approval from CFO (James Thornton) and DPO (Klaus Weber).

### 8.2 Escalation Path

| Trigger | Escalation Level | Action Owner |
| :--- | :--- | :--- |
| Failed identity verification twice | Level 1 | Privacy Compliance Analyst |
| Legal "Cease & Hold" order received | Level 2 | General Counsel (Maria Gonzalez) |
| Pipeline checksum failure (data loss) | Level 1 | Data Engineering Lead |
| Breach of 60-day deadline imminent | Level 3 | VP of Customer Operations & DPO |
| Security incident during transmission | Level 3 | CISO (Rachel Kim) |

---

## 9. Training Requirements

All personnel with assigned roles in the RACI matrix must complete the following training curriculum managed via the Workday Learning Platform:

- **Course: `SOP-COPS-008 Data Portability Fundamentals`**
    - **Audience:** All Customer Operations, Engineering, and Legal staff.
    - **Content:** GDPR Chapter 3 overview, Meridian's scope limitations (IP vs. Personal Data), portal walkthrough.
    - **Frequency:** Annually, or upon material SOP revision.

- **Course: `Secure Data Transfer and Encryption Protocols`**
    - **Audience:** Data Engineering Export Squad.
    - **Content:** Hands-on lab for executing the Kubeflow pipeline, Vault encryption key management, and verification of S3 bucket policies.
    - **Frequency:** Bi-annually.

- **Compliance & Ethics Refresh:**
    - **Audience:** All Staff.
    - **Content:** Consequences of unauthorized data disclosure and the criticality of identity verification.
    - **Frequency:** Quarterly updates via the internal "Privacy Pulse" newsletter.

---

## 10. Related Policies and References

| Reference ID | Document Title |
| :--- | :--- |
| SOP-SEC-015 | Intellectual Property Classification and Trade Secret Protection |
| SOP-LEG-022 | Data Subject Access Request (DSAR) Adjudication Guidelines |
| SOP-CMP-009 | Data Retention and Destruction Policy |
| SOP-SEC-010 | Cryptographic Key Management Standard |
| SOP-ENG-030 | Data Integration and Quality Assurance |
| EXT-REG-GDPR | EU General Data Protection Regulation 2016/679 |
| EXT-REG-HIPAA | Health Insurance Portability and Accountability Act |

---

## 11. Revision History

| Version | Date | Author | Description of Change |
| :--- | :--- | :--- | :--- |
| 1.0 | 2023-02-15 | Michael Chang | Initial draft. Established manual DSAR process via email. |
| 2.1 | 2024-05-20 | Samantha Torres | Integrated DataGrail portal for automated intake. Reduced manual identity verification. |
| 3.0 | 2025-01-10 | David Park | Automatted extraction via Kubeflow pipeline. Migrated from CSV-only to JSON/CSV dual format. |
| 3.2 | 2026-01-22 | Thomas Anderson | Added Direct Transmission controls (TEA Process) and explicit SR 11-7 carve-outs for credit scores. |
| 3.5 | 2026-07-09 | Michael Chang | Updated timelines clarification; added Clinical AI Platform input data handling; extended maximum response time to 60 days; removed rigid DPIA trigger logic for operational efficiency. |
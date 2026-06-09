---
sop_id: "SOP-LEGC-008"
title: "Litigation Hold and E-Discovery"
business_unit: "Legal & Compliance"
version: "2.9"
effective_date: "2024-06-25"
last_reviewed: "2025-11-24"
next_review: "2026-05-11"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Litigation Hold and E-Discovery

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for the identification, preservation, collection, processing, review, and production of electronically stored information (ESI) in response to actual, pending, or reasonably anticipated litigation, regulatory investigations, and government audits. The purpose of this SOP is to ensure that Meridian Health Technologies, Inc. (hereinafter "Meridian") conducts e-discovery and litigation holds in a legally defensible, consistent, repeatable, and auditable manner, while maintaining strict compliance with applicable data protection and privacy laws, notably the General Data Protection Regulation (GDPR) and the Health Insurance Portability and Accountability Act (HIPAA).

### 1.2 Scope
This SOP applies to all business units, subsidiaries, and global offices (Boston, London, Berlin, Singapore, Toronto) of Meridian, and covers all current and former full-time employees, part-time employees, contractors, consultants, temporary staff, and third-party service providers with access to Meridian’s systems or data (collectively "Personnel"). The scope encompasses all Electronically Stored Information (ESI), regardless of format, created, stored, or transmitted on any Meridian-owned, leased, or personally owned device (under BYOD policy) used for Meridian business. This includes, but is not limited to, data within the Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform.

This SOP covers the end-to-end e-discovery lifecycle, from the triggering event to the final release of a legal hold and the disposition of collected data, ensuring alignment with the regulatory obligations of GDPR, HIPAA, and the NIST AI Risk Management Framework (AI RMF) as voluntarily adopted by Meridian, particularly concerning high-risk AI systems under the EU AI Act.

---

## 2. Definitions and Acronyms

| Term | Definition |
| :--- | :--- |
| **Business Continuity Plan (BCP)** | A documented set of procedures and information to maintain critical operations during a disruption. |
| **Custodian** | An individual or entity that has possession, custody, or control of potentially relevant documents and ESI. |
| **Data Processor** | A natural or legal person, public authority, agency, or other body which processes personal data on behalf of the controller (as defined by GDPR Art. 4(8)). |
| **Data Protection Officer (DPO)** | Dr. Klaus Weber, the designated DPO for Meridian, responsible for overseeing GDPR compliance. |
| **Data Subject Access Request (DSAR)** | A request made by an individual to access their personal data, as defined under GDPR Art. 15. |
| **Defensibility** | The ability to demonstrate, through documented policies, procedures, and audit trails, that the e-discovery process is reasonable, consistent, and good-faith. |
| **E-Discovery Liaison** | A designated individual within each business unit who serves as the primary point of contact for the Legal & Compliance team during an e-discovery matter. |
| **Electronically Stored Information (ESI)** | All information created, manipulated, communicated, stored, and best utilized in digital form, requiring the use of computer hardware and software. This includes AI/ML models, training data, weights, and prompts. |
| **General Data Protection Regulation (GDPR)** | Regulation (EU) 2016/679 of the European Parliament and of the Council on the protection of natural persons with regard to the processing of personal data and on the free movement of such data. |
| **HIPAA** | The Health Insurance Portability and Accountability Act of 1996 and its implementing regulations, including the Privacy Rule, Security Rule, and Breach Notification Rule. |
| **Legal Hold (or Litigation Hold)** | A communication issued by the Legal & Compliance department that suspends routine data destruction policies and instructs custodians to preserve all potentially relevant documents and ESI. |
| **Legal Hold Release** | A formal notification issued by the Legal & Compliance department that lifts the preservation obligation for a specific matter. |
| **Personal Data** | Any information relating to an identified or identifiable natural person (‘data subject’), as defined by GDPR Art. 4(1). |
| **Protected Health Information (PHI)** | Individually identifiable health information held or transmitted by a covered entity or its business associate, in any form or medium, as defined by 45 CFR § 160.103. |
| **Triggering Event** | An event, such as receipt of a complaint, a demand letter, a regulatory inquiry, or a credible threat of litigation, that gives rise to a duty to preserve. |

---

## 3. Roles and Responsibilities

| Role | Responsibility | RACI (Trigger -> Release) |
| :--- | :--- | :--- |
| **Chief Compliance Officer (CCO)** | Ultimate authority and oversight for the Litigation Hold and E-Discovery process. Approves all exception requests. | Accountable (A) |
| **General Counsel (GC)** | Provides legal direction on scope of holds, relevance, and privilege. Approves all legal hold communications and productions. | Responsible (R) for Legal Strategy |
| **VP of IT Operations (Samantha Torres)** | Ensures technical capability and execution of ESI preservation and collection across Meridian’s infrastructure (AWS, Azure, Snowflake). | Responsible (R) for Technical Execution |
| **Chief Information Security Officer (Rachel Kim)** | Ensures all preservation, collection, and transfer activities comply with security policies and do not introduce undue risk. | Consulted (C) |
| **Chief Privacy Officer / DPO (Dr. Klaus Weber)** | Authorizes any cross-border data transfer in compliance with GDPR Chapter V. Reviews all collections for privacy impacts. | Consulted (C) for EU Data, Responsible (R) for GDPR compliance. |
| **E-Discovery Manager (Legal Ops)** | Day-to-day management of the full e-discovery lifecycle, manages external vendors, coordinates with external counsel. | Responsible (R) for Process Management |
| **Business Unit E-Discovery Liaisons** | Identifies key custodians and data sources within their unit. Assists in executing and confirming compliance with legal holds. | Consulted (C) |
| **Personnel (All Employees/Custodians)** | On receipt of a Legal Hold Notice, must immediately comply with preservation instructions and confirm compliance within 48 hours. | Informed (I), Responsible (R) for own data preservation |

---

## 4. Policy Statements

1.  **Duty to Preserve:** Meridian has a duty to preserve all potentially relevant ESI when litigation, a regulatory investigation, or an audit is reasonably anticipated. This duty supersedes any conflicting data retention or destruction policy, including data lifecycle management in Snowflake and log rotation in AWS CloudWatch.
2.  **Defensibility Principle:** Every action taken from issuance of a legal hold to the final production of ESI must be documented, repeatable, and auditable to withstand judicial scrutiny. Meridian adopts the EDRM (Electronic Discovery Reference Model) as its process framework.
3.  **Privacy by Design in E-Discovery:** Meridian will execute its e-discovery obligations in a manner that, by default, minimizes the processing of Personal Data and PHI, in accordance with GDPR Art. 25 and HIPAA’s Minimum Necessary Standard (45 CFR § 164.502(b)).
4.  **Transparency:** A record of processing activities (ROPA) for e-discovery, as required by GDPR Art. 30, shall be maintained by the Legal & Compliance department, detailing the purpose, categories of data, and retention periods for all data processed in a litigation matter.
5.  **Cross-Border Data Transfer Control:** No ESI containing EU Personal Data shall be transferred from an EU location (e.g., AWS eu-west-1) to the United States (AWS us-east-1) for processing without prior written authorization from the DPO using an approved transfer mechanism (Standard Contractual Clauses or Binding Corporate Rules) as mandated by GDPR Chapter V.
6.  **Sanctions for Non-Compliance:** Failure to comply with a Legal Hold Notice or accidental spoliation of evidence will be subject to disciplinary action, up to and including termination of employment, in accordance with the Meridian Employee Handbook.

---

## 5. Detailed Procedures

### 5.1 Issue Identification and Triggering Event
The e-discovery process is initiated by a Triggering Event reported to the Legal & Compliance team.
1.  **Reporting Channels:** Any employee receiving a subpoena, summons, complaint, attorney demand letter, notice of a government audit (e.g., OCR HIPAA audit, EU DPA inquiry), or a formal DSAR that relates to potential litigation must forward it to `legal-notices@meridianhealthtech.com` within **2 hours** of receipt.
2.  **Case Intake Assessment:** The E-Discovery Manager creates a new matter intake form in the Meridian Matter Management System (Salesforce Litify) within **4 business hours** of notification. The General Counsel (GC) will assess the Triggering Event and, within **1 business day**, make a preliminary determination on whether a duty to preserve has been triggered.
3.  **Custodian & Data Source Scoping:** Upon a positive trigger determination, the E-Discovery Manager will convene a scoping meeting within **2 business days**. This meeting must include the GC, the relevant Business Unit E-Discovery Liaison, the CISO, and (if EU data may be involved) the DPO. The meeting’s output is a formal **Custodian & Data Source Map**, identifying:
    - **Key Custodians:** Named individuals likely to have relevant information.
    - **Data Repositories:** Specific data sources (e.g., AWS S3 buckets: `meridian-clinical-ai-prod`, Snowflake `MEDINSIGHT_ANALYTICS_RAW`, Gmail/Drive for specific users, Slack channels).
    - **AI System Considerations:** For any matter involving the Clinical AI Platform, the map must specifically identify relevant AI models (versions), training datasets, and inference logs, in consultation with the VP of Clinical AI Products or their designate.

### 5.2 Issuance of Legal Hold Notice
1.  **Drafting the Notice:** The E-Discovery Manager drafts the Legal Hold Notice using the approved template (`TEMP-LEG-001`). The notice must be written in plain language and include:
    - A clear, non-technical description of the matter.
    - Specific categories of documents and ESI to be preserved.
    - An explicit instruction to cease any automatic deletion or alteration of data, including AI model retraining pipelines.
    - A link to the Acknowledgement Form.
    - Contact information for the E-Discovery Manager.
2.  **Legal Review and Approval:** The GC must review and approve the Legal Hold Notice and the custodian list for legal accuracy and scope before distribution. This approval is recorded in the matter’s log.
3.  **Distribution:** The E-Discovery Manager issues the Legal Hold Notice via the enterprise legal hold management system (Onna). Notices are sent to all identified custodians’ `@meridianhealthtech.com` email addresses.
4.  **Custodian Acknowledgment Deadline:** All custodians must acknowledge receipt and understanding of the Legal Hold Notice within **48 hours**. The Onna system will send automatic reminders every 24 hours for non-responders. At 72 hours of non-response, the E-Discovery Manager will escalate to the custodian’s direct manager and the VP of the business unit.

### 5.3 Data Preservation
1.  **Automated In-Place Preservation:** On receipt of a signed Custodian & Data Source Map, the VP of IT Operations will execute technical preservation measures within **3 business days**.
    - **O365 (Email & OneDrive):** Place targeted mailboxes and OneDrive accounts on In-Place Hold via Microsoft Purview. Ensure the hold reason is documented with the matter ID.
    - **Slack (Enterprise Grid):** Apply a legal hold to all channels and direct messages associated with identified custodians via the Slack Discovery API.
    - **Cloud Infrastructure (AWS & Azure):** Apply S3 Object Lock in governance mode to specified buckets (e.g., `meridian-medinsight-logs`). Apply WORM (Write Once, Read Many) policy on relevant Azure Blob Storage containers. Create snapshots of specific EC2 instances and RDS databases, tagging them with `PURPOSE: Legal Hold` and `MATTER_ID`.
2.  **AI/ML System Preservation (Clinical AI & HealthPay):**
    - **Model Freezing:** For matters involving Clinical AI or HealthPay credit models, a complete snapshot of the production model binary, associated weights, and training hyperparameters in MLflow must be taken, and the `model_version` tagged as `LEGAL_HOLD_[MATTER_ID]`. No retraining or fine-tuning of a frozen model is permitted without approval from the GC, CCO, and a written exception per Section 7.
    - **Inference Log Preservation:** All LangSmith traces and CloudWatch logs for inferences from the frozen model during the relevant period must be streamed and locked in a separate, immutable S3 bucket.
3.  **Custodian Self-Preservation Guidance:** The Legal Hold Notice instructs custodians to personally preserve relevant non-centrally managed files, such as local downloads, browser bookmarks, and paper documents. The notice specifically prohibits manual deletion of any email, Slack message, or file related to the matter’s subject.

### 5.4 Collection
1.  **Collection Planning Meeting:** Once the scope of discovery requests is clarified, the GC, E-Discovery Manager, and DPO (for EU data) meet to define a collection plan that strictly adheres to the principle of minimization (GDPR Art. 5(1)(c)) and the HIPAA Minimum Necessary Standard.
2.  **Targeted Collection Execution:** The VP of IT Operations executes the defensible collection from the preserved data repositories using Forensically Sound Collection Tools (Microsoft Purview eDiscovery Premium, AWS DataSync).
    - **De-Duplication and Filtering:** A critical step is performed *after* collection using RelativityOne, applying near-native deduplication (on MD5 hash) across the entire collection set. Date-range and keyword filters are applied to cull data before review.
    - **PHI/PII Culling Log:** A detailed log of all culling criteria applied (keywords, date ranges, domains) must be maintained and approved by the GC to defend against challenges of over-collection.
3.  **Chain of Custody:** An unbroken chain of custody form (`FORM-LEG-002`) must be maintained for all data collections. This form tracks the data from its source location (e.g., AWS eu-west-1), through collection, to its secure storage in the review platform. It must log the date, time, name of handler, action taken, and transfer mechanism. For EU data, the DPO co-signs the chain of custody to confirm the authorized transfer mechanism used.

### 5.5 Processing and Review
1.  **Data Ingestion into Review Platform:** Collected ESI is ingested into RelativityOne. For EU Personal Data, the processing must occur on an instance hosted in the EU (eu-west-1) or in a US instance governed by a DPO-approved Data Processing Agreement incorporating the EU SCCs.
2.  **Technology-Assisted Review (TAR) Protocol:** For any matter with over 50,000 documents, the use of Continuous Active Learning (CAL) is mandatory to ensure proportional and efficient review. The TAR protocol must be documented in detail, including the seed set, stability criteria (e.g., F1 score of >80% and a recall of >75% for the rich set), and control set validation. This protocol must be defensible and approved by external counsel and the GC.
3.  **Privilege Review:** A second-level review for Attorney-Client Privilege and Work Product Doctrine must be conducted by the Meridian GC’s office or designated external counsel. Privileged documents must be logged on a privileged log and redacted or withheld.

### 5.6 Production
1.  **Pre-Production Quality Control (QC):** A 5% random sample of the production set must be statically sampled and manually QC’d by a second reviewer for privilege, redaction failures, and responsiveness. The production cannot proceed if the error rate exceeds 2%.
2.  **Production Format:** Documents are produced in a flat file format (TIFF/PDF with extracted text and native files) with a standard load file (Concordance `.dat` or CSV), unless a different format is agreed upon with the requesting party.
3.  **Final Sign-Off:** The GC and CCO provide a final written sign-off via DocuSign on the production manifest before the production is released to the requesting party.

### 5.7 Release and Disposition
1.  **Legal Hold Release:** Upon written confirmation of matter resolution (final, non-appealable judgment or settlement agreement), the E-Discovery Manager issues a Legal Hold Release Notice within **5 business days**.
2.  **Data Disposition:** The VP of IT Operations will remove all technical holds and delete legal hold snapshots within **30 days** of the release notice. Data collected and housed in RelativityOne will be purged in accordance with the project’s data retention policy, which must be confirmed by the DPO to ensure timely de-provisioning of access and deletion of Personal Data in accordance with GDPR Art. 17.

---

## 6. Controls and Safeguards

| Control ID | Control Category | Control Description | Regulatory Alignment |
| :--- | :--- | :--- | :--- |
| **CTRL-LEG-001** | Administrative | Formal legal hold policy reviewed and approved annually by the AI Governance Committee and the Board. | NIST AI RMF Govern 1.1; GDPR Art. 5(2) |
| **CTRL-LEG-002** | Technical | Immutable WORM storage for all collected and preserved ESI before processing. S3 Object Lock must be enabled with a retention period of `min(statute_of_limitations, 10 years)`. | SR 11-7; SOC 2 CC6.1 |
| **CTRL-LEG-003** | Administrative | All e-discovery vendors (e.g., Relativity, Onna) undergo a third-party security and privacy risk assessment and must hold SOC 2 Type II and ISO 27001 certifications. | SOC 2 CC9.2; GDPR Art. 28 |
| **CTRL-LEG-004** | Technical | Automated logging of all user and administrative actions within the e-discovery platform to CloudTrail and Datadog, with immutable log storage. | SOC 2 CC7.2; GDPR Art. 30 |
| **CTRL-LEG-005** | Privacy | Pseudonymization of PHI and EU Personal Data within the review platform where full identifiers are not strictly necessary for the review. This is executed by automated scripts before data load. Key must be stored separately in HashiCorp Vault. | HIPAA 45 CFR § 164.514(a); GDPR Art. 25 |
| **CTRL-LEG-006** | Technical | Role-Based Access Control (RBAC) enforced in RelativityOne via Okta SSO with MFA. Access must be reviewed and re-certified by the E-Discovery Manager every 30 days during an active matter. | SOC 2 CC6.1; HIPAA § 164.312(a)(1) |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)
| Metric | Target | Measurement Frequency | Owner |
| :--- | :--- | :--- | :--- |
| Custodian Acknowledgement Rate (48 hrs) | 100% | Per Legal Hold | E-Discovery Manager |
| Time from Trigger to Hold Issuance | < 5 business days | Quarterly | CCO |
| Preservation Technical Execution Time | < 3 business days from map approval | Per Matter | VP of IT Operations |
| PHI Breach Incidents related to E-Discovery | 0 | Continuous | CISO |
| GDPR Data Transfer Compliance | 100% DPO authorization before transfer | Per Matter | DPO |
| Production QC Defect Rate | < 2% | Per Production | GC |

### 7.2 Reporting Cadence
- **Monthly:** The E-Discovery Manager prepares a "Matters on Hold" report for the CCO detailing the number of active holds, custodian count, and the number of matters approaching disposition review.
- **Quarterly:** The CCO presents a "Legal Hold Defensibility Report" to the Board-level AI Governance Committee, summarizing KPI metrics, exception logs, and any audit findings against this SOP.
- **Annually:** This SOP undergoes an annual review by the General Counsel, CCO, CISO, and DPO. The review incorporates lessons learned from closed matters, changes in law, and technological advancements. The SOC 2 Type II audit will test the operational effectiveness of this SOP’s controls.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Request Process
Any deviation from the prescribed timelines or procedures in this SOP requires a formal, written exception request.
1.  **Submission:** The requestor must complete the `FORM-LEG-003` ("Litigation Hold Exception Request") and submit it to `compliance@meridianhealthtech.com`.
2.  **Contents:** The form must detail the specific procedure for which an exception is sought, a compelling business justification, the scope of data affected, the duration of the exception, and a mitigation plan to minimize risk.
3.  **Approval Authority:**
    - Exceptions related to legal strategy must be approved by the **General Counsel**.
    - Exceptions related to technical preservation must be approved by the **VP of IT Operations** and the **CISO**.
    - **All exceptions** require final sign-off by the **Chief Compliance Officer**.
    - Any exception involving EU Personal Data requires mandatory authorization from the **DPO**.

### 8.2 Escalation Matrix
In the event of suspected data spoliation, an unauthorized disclosure of PHI/PII during transfer, or willful non-compliance by a custodian:
1.  Immediate notification to the **Chief Compliance Officer (CCO)**.
2.  If the incident involves PHI, the **CISO** must be notified within 1 hour, and the HIPAA Breach Notification protocol (`SOP-ISMS-005`) must be initiated, with a risk assessment completed within 24 hours.
3.  If the incident involves EU Personal Data, the **DPO** must be notified without undue delay, and a data breach notification to the relevant Supervisory Authority under GDPR Art. 33 must be evaluated within 72 hours.

---

## 9. Training Requirements

1.  **Role-Based Training:**
    - **All Personnel:** Annual training on the Duty to Preserve and the Litigation Hold process, delivered via the Workday Learning module `MOD-LEG-001`. A quiz score of 90% is required to pass.
    - **Data Custodians (upon hold placement):** An immediate, 5-minute micro-training video is automatically pushed via Onna with the hold notice, which must be viewed before the acknowledgment form can be submitted.
    - **E-Discovery Team (Legal, IT, Privacy):** Biennial, in-depth training on advanced e-discovery topics, including cross-border data transfers, TAR protocols, and AI system preservation. Led by external counsel and the DPO.
2.  **Tracking and Enforcement:** Training completion is tracked in Workday. Managers receive a monthly non-compliance report. Personnel who fail to complete required training within 30 days will have their Okta credentials suspended until training is completed, per `SOP-HR-012`.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs
- `SOP-ISMS-001`: Information Security Management System Policy
- `SOP-ISMS-005`: Incident Response and Breach Notification
- `SOP-DPO-001`: Data Protection Governance and GDPR Compliance
- `SOP-HR-012`: Employee Disciplinary Policy
- `SOP-MRM-001`: Model Risk Management (for HealthPay AI models)
- `SOP-CAI-003`: Clinical AI Platform Lifecycle Management
- `SOP-PRM-002`: Third-Party Risk Management

### 10.2 External References
- Electronic Discovery Reference Model (EDRM)
- NIST Special Publication 800-53, Revision 5
- Federal Rule of Civil Procedure 37(e)
- GDPR, Articles 5, 6, 15, 17, 25, 28, 33, 44-49
- HIPAA, 45 CFR Parts 160, 164 (Privacy, Security, Breach Notification Rules)

---

## 11. Revision History

| Version | Date | Author(s) | Description of Changes |
| :--- | :--- | :--- | :--- |
| 2.9 | 2025-11-24 | Thomas Anderson, Dr. Klaus Weber | Updated Section 5.5.1 to mandate EU-based RelativityOne instance for EU data processing. Clarified DPO co-signature requirements in chain of custody (Section 5.4.3). Enhanced AI system preservation steps (Section 5.3.2) to include LangSmith traces. |
| 2.8 | 2025-01-15 | Thomas Anderson, Samantha Torres | Revised Section 5.3.1 to incorporate new Azure WORM storage capabilities for DR targets. Updated technical controls (CTRL-LEG-002) to reflect the 10-year statutory hold period. |
| 2.7 | 2024-06-25 | Thomas Anderson, Maria Gonzalez | Added explicit reference to NIST AI RMF and high-risk AI systems (Section 1.2, 5.1.3). Added AI model preservation (Freezing) sub-procedure. Clarified TAR protocol metrics in Section 5.5.2. |
| 2.6 | 2023-11-10 | Thomas Anderson | Initial comprehensive rewrite. Merged separate e-discovery and litigation hold policies into one SOP. Introduced RACI matrix and formal KPI metrics. Aligned with updated GDPR Art. 30 ROPA requirements. |

**End of Document: SOP-LEGC-008**
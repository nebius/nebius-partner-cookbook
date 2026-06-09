---
sop_id: "SOP-DGP-012"
title: "Data Sharing Agreements"
business_unit: "Data Governance & Privacy"
version: "2.1"
effective_date: "2025-07-20"
last_reviewed: "2026-04-05"
next_review: "2026-10-28"
owner: "Dr. Klaus Weber, Chief Privacy Officer / DPO"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Data Sharing Agreements

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide framework governing the initiation, review, approval, execution, and ongoing monitoring of all Data Sharing Agreements (DSAs) at Meridian Health Technologies, Inc. ("Meridian"). The purpose of this SOP is to ensure that all sharing of Meridian-controlled data with external parties—including protected health information (PHI), personal data of European Union data subjects, AI model training data, financial transaction data, and de-identified analytics data—is conducted in strict compliance with applicable legal and regulatory obligations, contractual commitments, and ethical principles. This SOP operationalizes the data minimization, purpose limitation, and accountability principles set forth in Regulation (EU) 2016/679 (General Data Protection Regulation, "GDPR") and the Health Insurance Portability and Accountability Act of 1996 ("HIPAA") Privacy and Security Rules, as amended.

### 1.2 Scope

This SOP applies to all Meridian employees, contractors, consultants, and third-party partners ("Personnel") involved in the disclosure, transmission, or making available of Meridian data to any External Recipient. An External Recipient is defined as any entity, organization, or individual that is not a Meridian employee acting within the scope of their employment. This includes, but is not limited to, academic research institutions, pharmaceutical partners, health system customers, health information exchanges (HIEs), business associates (as defined under HIPAA), data processors and sub-processors (as defined under GDPR), cloud service providers, and independent software vendors.

The data types covered by this SOP encompass:
- **PHI:** Individually identifiable health information subject to HIPAA.
- **GDPR Personal Data:** Any information relating to an identified or identifiable natural person located in the European Economic Area (EEA), including but not limited to, clinical trial data, patient-reported outcomes, and biometric data processed via Meridian’s CE-marked medical devices under EU MDR.
- **Confidential Business Information (CBI):** Proprietary algorithms, source code, product roadmaps, and financial terms.
- **AI/ML Model Training Data:** Any dataset used to train, validate, or test a Meridian AI/ML model, regardless of its de-identification status, subject to the controls of SOP-AIF-015 (AI Model Lifecycle Governance).
- **De-Identified/Aggregated Data:** Data that has been rendered non-identifiable in accordance with the expert determination or safe harbor methods defined in HIPAA and recital 26 of GDPR, where the recipient's ability to re-identify is contractually restricted.

This SOP does not apply to (a) sharing data with Meridian employees for internal business purposes governed by SOP-IS-005 (Information Security Policy), or (b) public disclosures approved by Corporate Communications under SOP-COR-003 (External Communications Policy).

## 2. Definitions and Acronyms

| Term | Definition |
| :--- | :--- |
| **Agreement Data Set (ADS)** | The precisely defined data elements, source systems, and data formats authorized for sharing under a specific DSA. |
| **Business Associate Agreement (BAA)** | A legally binding contract mandated by 45 CFR 164.502(e) and 164.504(e) between a HIPAA-covered entity and a Business Associate, establishing permitted uses and disclosures of PHI. |
| **Controller-to-Controller SCCs** | Standard Contractual Clauses adopted by the European Commission for the transfer of personal data between two independent data controllers. |
| **Controller-to-Processor SCCs** | Standard Contractual Clauses adopted by the European Commission (most recently, Commission Implementing Decision (EU) 2021/914) for the transfer of personal data to a processor in a third country. |
| **Data Privacy Impact Assessment (DPIA)** | A mandated risk assessment under GDPR Article 35 for processing operations, particularly using new technologies, that are likely to result in a high risk to the rights and freedoms of natural persons. |
| **Data Sharing Agreement (DSA)** | The Meridian-authored master agreement template that integrates HIPAA, GDPR, and commercial requirements, governing the overarching relationship for a specific data-sharing initiative. |
| **Data Use Agreement (DUA)** | A specific agreement required by HIPAA for the sharing of a Limited Data Set, as defined at 45 CFR 164.514(e). |
| **External Recipient** | The counterparty to a DSA, acting as a Controller, Joint Controller, or Processor. |
| **Joint Controller Agreement (JCA)** | A legally binding contract mandated by GDPR Article 26 where two or more controllers jointly determine the purposes and means of processing. |
| **Limited Data Set (LDS)** | PHI that excludes the following 16 direct identifiers of the individual or of relatives, employers, or household members of the individual: names, postal address information (other than town or city, state, and zip code), telephone/ fax numbers, electronic mail addresses, social security numbers, medical record numbers, health plan beneficiary numbers, account numbers, certificate/license numbers, vehicle identifiers and serial numbers (including license plate numbers), device identifiers and serial numbers, Web URLs, Internet Protocol (IP) address numbers, biometric identifiers (including finger and voice prints), and full face photographic images. |
| **Privacy Shield Framework** | Although the EU-U.S. Privacy Shield was invalidated by the Court of Justice of the European Union (CJEU) in *Schrems II*, Meridian maintains self-certification to the Swiss-U.S. Privacy Shield for non-EU data, alongside mandatory SCCs and Transfer Impact Assessments. |
| **Sensitive Information** | A subset of personal data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, genetic data, biometric data processed for the purpose of uniquely identifying a natural person, data concerning health, or data concerning a natural person's sex life or sexual orientation (GDPR Article 9). |
| **Transfer Impact Assessment (TIA)** | A documented assessment, required following the Court of Justice of the European Union ruling in *Data Protection Commissioner v. Facebook Ireland Ltd & Maximillian Schrems* (C-311/18), evaluating the legislation of the third country of destination and the technical and organizational measures in place to ensure compliance with GDPR Article 46. |

## 3. Roles and Responsibilities

A RACI (Responsible, Accountable, Consulted, Informed) matrix has been established to define clear ownership for all activities within this SOP.

| Activity | Data Governance & Privacy (Owner: Dr. Klaus Weber) | Office of the General Counsel (Approver: Maria Gonzalez) | Meridian Information Security (InfoSec) | Data Steward (Business Owner) | External Relations / Alliances |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Initial DSA Request** | I | I | N/A | R | C |
| **DPIA & TIA Execution** | R | C | C | C | N/A |
| **Negotiation & Legal Drafting** | C | R/A | C | C | R |
| **Technical Control Validation** | C | I | R/A | C | I |
| **Annual Compliance Audit** | R/A | C | C | I | I |
| **Data Subject Rights Fulfillment** | R/A | C | N/A | C | N/A |
| **Termination & Data Destruction** | R | C | N/A | R/A | I |
| **Business Case Approval** | N/A | N/A | N/A | R/A | C |

**Specifically, the following named roles hold the following responsibilities:**

- **Dr. Klaus Weber, Chief Privacy Officer / DPO:** The ultimate process owner for this SOP. Dr. Weber holds the final authority to halt any data-sharing activity deemed non-compliant with GDPR or HIPAA. He serves as the single point of contact for Supervisory Authorities (e.g., Berlin DPA) and data subjects.
- **Maria Gonzalez, General Counsel:** Holds the authority to bind Meridian legally. She is the sole approver of all contract modifications to the standard DSA template, including but not limited to indemnification, limitation of liability, and choice of law/venue clauses.
- **Data Steward (VP or Director Level):** Each business unit (Clinical AI, Commercial, Med Affairs) assigns a Data Steward. The Data Steward must certify the business necessity, accuracy, and minimum necessary nature of the Agreement Data Set (ADS) before any data pull. The Data Steward is the "data owner" for access control purposes.

## 4. Policy Statements

Meridian Health Technologies is committed to responsible data stewardship. The following policy statements form the non-negotiable foundation of this SOP:

1.  **Prohibition of Sale:** Meridian unequivocally prohibits the sale of PHI as defined under 45 CFR 164.502(a)(5)(ii). Any release of PHI will be structured as a service, research collaboration, or public health activity governed by HIPAA’s permitted disclosures at 164.502(a)(1).
2.  **Purpose Limitation:** Data shared under any DSA will be strictly limited to the defined, explicit, and legitimate business purpose stated in the agreement. Secondary processing of the same ADS for a new purpose requires a new DSA and, where applicable, a new notice to data subjects under GDPR Articles 13 and 14.
3.  **Data Minimization:** All DSAs must reflect our organizational commitment to provide the "Minimum Necessary" information (HIPAA 45 CFR 164.502(b)) and "adequate, relevant and limited to what is necessary" (GDPR Article 5(1)(c)). The Data Steward must technically validate that a query extracts only the approved ADS.
4.  **No Waiver of Rights:** No contract clause may compel Meridian to waive the rights of its data subjects, including the right to erasure (GDPR Article 17) or the right to an accounting of disclosures (HIPAA 45 CFR 164.528).
5.  **Transparency:** The existence of a DSA involving personal data will be noted in Meridian’s central Record of Processing Activities (ROPA) maintained by the DPO, as mandated by GDPR Article 30.

## 5. Detailed Procedures

### 5.1 Initiating a Data Sharing Request

The business owner (requestor) who identifies a business need for external data sharing must initiate the process through the Meridian Data Governance Portal (MDGP) on the intranet (http://mdgp.internal.meridian.tech). This is the sole entry point, superseding prior email-based requests.

1.  The requestor logs into MDGP using single sign-on (SSO) and selects "Initiate DSA."
2.  Form DSA-101 "Data Sharing Purpose and Need" must be completed. This form requires:
    - **Title of Initiative:** A concise, descriptive project name.
    - **Primary Business Justification:** A 250-word narrative, selecting from pre-defined categories: Clinical Research, Market Access, HIE Interoperability, AI Model Validation, Public Health (mandatory reporting), or Payment/Healthcare Operations.
    - **Identification of Counterparty:** Full legal entity name, jurisdiction of incorporation, and primary contact.
    - **Anticipated Regulatory Crosswalk:** Selection of GDPR Art. 6/9, HIPAA 45 CFR 164.506 (Treatment, Payment, Operations), 164.508 (Authorization), or 164.512 (Uses and Disclosures without Authorization).
    - **Agreement Data Set (ADS) Definition:** Detailed description of data fields, patient cohorts, timeframes, and source systems (e.g., AWS Redshift Clinical Data Warehouse, Salesforce Health Cloud).
3.  Upon submission, the MDGP generates a unique DSA Pre-ID (e.g., `PRE-DSA-2026-089`). This ID will persist through to final execution.

### 5.2 Legal & Privacy Intake and Risk Triage

Upon submission, the MDGP routes the `PRE-DSA` notification simultaneously to the Office of General Counsel (OGC) and the Office of the Chief Privacy Officer (OCPO).

1.  **Triaging Paralegal (OGC):** Within two (2) business days, the designated OGC paralegal acknowledges the request and performs a Conflict Check and Sanctions Verification (against OFAC, EU Consolidated List) of the External Recipient.
2.  **Privacy Analyst (OCPO):** Concurrently, an OCPO analyst reviews the "Anticipated Regulatory Crosswalk" and the ADS.
    - If personal data is confirmed, the analyst creates a record in the central GDPR Article 30 ROPA system (SaaS: OneTrust) and assigns a ROPA ID.
    - The analyst determines if a formal **Data Privacy Impact Assessment (DPIA)** is required per GDPR Article 35. A DPIA is mandatory for any DSA involving: (a) systematic and extensive profiling; (b) large-scale processing of special categories of *genetic or biometric data*; or (c) large-scale processing of data concerning criminal convictions.
    - If cross-border data transfer out of the EEA is detected, a **Transfer Impact Assessment (TIA)** is immediately triggered.

### 5.3 Agreement Template Selection and Drafting

The OGC, in collaboration with OCPO, selects the appropriate Meridian DSA template from the OGC Clause Library, based on the counterparty's role.

| Counterparty Role | Primary Template | Mandatory Appendices |
| :--- | :--- | :--- |
| **Business Associate (HIPAA)** | `MHT-BAA-v4.2` | Exhibit A: Permitted Services; Exhibit B: Security Contact; Exhibit C: Minimum Necessary Protocol |
| **Data Processor (GDPR)** | `MHT-DPA-v3.0` | Annex I(A) Parties, I(B) Subject Matter/Duration/Nature Purpose; Annex II: Sub-processor Authorization Model Clauses |
| **Independent Controller (Two-way data exchange)** | `MHT-Controller-DSA-v2.5` | Schedule 1: ADS; Schedule 2: Joint Controller Addendum (if applicable); Module 1 SCCs |
| **Academic Research Partner (De-Identified/LDS)** | `MHT-RESEARCH-DUA-v1.8` | Article 28 GDPR provisions (if EU data); 45 CFR 164.514(e) DUA provisions; Prohibition of Re-identification Rider |
| **Vendor for Payment/Operations (No PHI)** | `MHT-MSA-SOW-v5.0` | Addendum X: Non-PII Data Security Rider |

**Template Customization Process:**
No modification to the "Limitation of Liability," "Indemnification," "Governing Law," or "Data Use Limitations" sections is permitted without explicit sign-off from Maria Gonzalez.

### 5.4 The Transfer Impact Assessment (TIA) Procedure

For any DSA involving the transfer of personal data from the EEA to a third country (including the USA), a TIA must be completed and approved before the DSA is countersigned. This is a critical post-*Schrems II* requirement.

1.  **Step 1: Mapping the Transfer.** The CPO’s analyst documents:
    - Controller identity: `Meridian Health Technologies GmbH` (Frankfurt Office).
    - Exporter identity: Same.
    - Importer identity: External Recipient legal entity.
    - Transfer Mechanism: SCCs (EU 2021/914), Binding Corporate Rules, or an adequacy decision.
2.  **Step 2: Third Country Law Assessment.** The OGC, aided by external local counsel, prepares a memorandum assessing the Recipient Country's surveillance laws. Key consideration: Can public authorities access the data without adequate safeguards?
3.  **Step 3: Technical Controls Assessment.** InfoSec must document the state of encryption in transit and at rest.
    - *Standard:* All EEA transfers *must* use Meridian's Data Transfer Endpoint Encryption Standard (`INFOSEC-ENC-009`), requiring AES-256 encryption at rest and TLS 1.3 with Perfect Forward Secrecy in transit.
    - *Supplementary Measure:* If the TIA identifies a high risk of government access, a *Bring Your Own Key (BYOK)* model with a pseudonymization gate must be deployed at the Meridian edge network before export. The key management system must reside solely within the EEA (`eu-west-2` AWS region).
4.  **Step 4: TIA Finalization.** Dr. Klaus Weber reviews and signs the final TIA, making a documented finding of "Effective Protection" or "Suspension." A "Suspension" finding immediately halts the DSA execution.

### 5.5 Detailed Review and Approval Workflow (SLAs)

The following Service Level Agreements (SLAs) govern the processing pipeline, measured from the time of the initial request submission to MDGP.

| Step | Process | SLA Target (Business Days) | Responsible Party | Escalation Trigger (Overdue) |
| :--- | :--- | :--- | :--- | :--- |
| 1 | Intake & Triaging | Day 0-2 | OGC Paralegal | Day 3 |
| 2 | DPIA/TIA Trigger Assessment | Day 2-5 | OCPO Privacy Analyst | Day 6 |
| 3 | DPIA Draft & Review | Day 5-25 | OCPO (with InfoSec) | Day 30 |
| 4 | TIA Draft & Review | Day 5-30 | OGC + External Counsel | Day 35 |
| 5 | DSA Drafting & First Pass | Day 5-15 | OGC Legal Counsel | Day 16 |
| 6 | Internal Business Review | Day 15-20 | Data Steward (Requestor) | Day 21 |
| 7 | External Counterparty Negotiation | Day 20-60 | External Alliances (with OGC) | Day 65 |
| 8 | Final Compliance Audit & Sign-off | Day 60-65 | Dr. Klaus Weber | Day 66 |
| 9 | Final Legal Counter-Signature | Day 65-70 | Maria Gonzalez | Day 71 |

### 5.6 Execution and Data Provisioning

Upon full execution by Maria Gonzalez, the OGC uploads the fully signed DSA PDF to the MDGP repository and updates the status to "Active."

1.  **Infosec Onboarding:** The External Recipient must pass Meridian's third-party risk management (TPRM) assessment (`SOP-IS-TPRM-001`).
2.  **Credential Exchange:** Meridian InfoSec issues a one-time-use, encrypted data transfer credential. No user accounts are created for External Recipients on Meridian's primary production network.
3.  **Secure Transfer:** The Data Steward, or an Automated Data Processing (ADP) job approved by the Data Steward, extracts the ADS precisely as defined in Schedule 1 of the DSA. The data file is encrypted using the External Recipient's PGP key (pre-approved public key fingerprint) and transferred via the Secure Managed File Transfer (SMFT) platform (Product: Axway MFT). Transfer must be a "push" from Meridian to the Recipient's designated secure endpoint.
4.  **Verification:** A Meridian Data Engineer verifies a cryptographic hash (SHA-256) of the transferred file against the source to ensure no corruption. The External Recipient confirms receipt and validates the hash.

### 5.7 Ongoing Monitoring and Amendment

An Active DSA is not a static document.
1.  **Annual Review:** On the anniversary of the execution date, the assigned Privacy Analyst contacts the External Recipient’s Privacy/Compliance office to request revalidation of their security posture (e.g., a summary of any changes to their SOC 2 Type II or ISO 27001 certifications).
2.  **Scope Change:** Any request from the Business Owner to expand the ADS (adding new data elements or use purposes) requires a DSA Amendment Form (Form DSA-AMEND-001), which re-enters the triage workflow at Step 5.1. Informal "mission creep" is strictly prohibited.

### 5.8 Termination Procedures

Termination of a DSA may occur for cause (breach), convenience (end of project), or contract expiration.

1.  **Notice:** The OGC or CPO drafts a formal termination notice specifying the effective date and applicable clause (e.g., "Termination for Convenience per Section 12.1 of the Agreement").
2.  **Data Destruction Protocol:**
    - Within thirty (30) calendar days of termination, the External Recipient’s Chief Privacy Officer (or equivalent) must certify the permanent destruction of all copies of the ADS, including backups, using a NIST SP 800-88-compliant method.
    - Where lawfulness of processing is based solely on consent (GDPR Art. 7), the Recipient must also cascade this instruction to any sub-processors.
    - Exceptions for record-keeping are allowed solely for a single archived copy required by applicable law, stored offline and not used for any new processing.
3.  **Final Reporting:** The Meridian CPO records the "Final Effective Date" in the ROPA, and the MDGP status is set to "Terminated." The ADS access credentials are revoked by InfoSec within twenty-four (24) hours.

## 6. Controls and Safeguards

Meridian has implemented the following technical, administrative, and physical controls to enforce this SOP.

| Control ID | Control Category | Description | Reference Standard |
| :--- | :--- | :--- | :--- |
| **CTL-DGP-012-01** | Administrative | **Required DSA Content.** No DSA will be signed unless it explicitly includes: (i) Permitted Use/Purpose; (ii) Prohibition of Re-identification (if applicable); (iii) Audit Rights for Meridian; (iv) Obligation to notify Meridian of any legal demand by a government agency for the data; (v) Breach Notification timelines (24 hours for GDPR, 48 hours for HIPAA). | GDPR Art. 28; 45 CFR 164.504(e)(2) |
| **CTL-DGP-012-02** | Technical | **Automated Data Redaction (ADR).** Before any ADS leaves the SMFT, Meridian’s Data Loss Prevention (DLP) module (Forcepoint) validates the file against the approved ADS schema. Any field not explicitly approved in the DSA is automatically redacted or flagged for manual review by the Data Steward. | Internal `INFOSEC-DLP-004` |
| **CTL-DGP-012-03** | Administrative | **Right to Audit.** All BAA and DPA templates include a clause granting Meridian the right to audit the Recipient’s compliance with contractual privacy obligations at least annually. A "Virtual Audit Protocol" using a standardized ISO 27001 controls questionnaire is the default method unless a breach triggers an on-site right. | SOP-DGP-012-A01 |
| **CTL-DGP-012-04** | Cryptographic | **Data Sovereignty Tagging.** All files containing EEA-sourced personal data are tagged with custom AWS S3 Object Lock metadata (Key: `data-residency`, Value: `EEA-only`). This attribute is validated by Policy-as-Code (AWS SCPs) before any cross-region replication. | GDPR Art. 44 |
| **CTL-DGP-012-05** | Administrative | **Sub-Processor Allowed List.** A Data Processor may only engage a Sub-Processor from Meridian’s pre-approved list (Appendix A to the DPA). Any new sub-processor requires a 14-day prior notification and a right to object for the Controller. | GDPR Art. 28(2) |

## 7. Monitoring, Metrics, and Reporting

The effectiveness of this SOP is measured through a series of quantitative KPIs reported to the Data Governance Council quarterly.

| Metric ID | KPI | Target | Measurement Methodology | Reporting Tool |
| :--- | :--- | :--- | :--- | :--- |
| **KPI-DSA-01** | **Time-to-Execution (Median)** | < 65 Business Days | MDGP workflow status timestamps, from `Initiate` to `Active`. | Tableau KPI Dashboard |
| **KPI-DSA-02** | **Percentage of DSAs with Expired Reviews** | 0% | Count of active DSAs where `Last Review Date` > 365 days from `current date` / Total Active DSAs. | OneTrust, Power BI |
| **KPI-DSA-03** | **TIA Compliance Rate** | 100% | Count of active cross-border DSAs without an approved TIA on file. Target is zero. | Manual CPO Audit |
| **KPI-DSA-04** | **Unauthorized Data Sharing Incidents** | 0 | Incidents logged in ServiceNow "Privacy Incident" queue classified as "Unauthorized 3rd Party Disclosure." | ServiceNow |
| **KPI-DSA-05** | **Data Subject Request (DSR) – DSA Responsiveness** | < 28 Days | Time from receiving a DSR that implicates a DSA Recipient to notification of Recipient and closure of request. | OneTrust DSR Module |

The CPO will present a "Data Sharing Governance Scorecard" at each quarterly Data Governance Council meeting. The scorecard will use a Red-Amber-Green (RAG) status for each KPI. Any KPI in Red status requires a formal remediation plan with an assigned owner and due date within two weeks of the meeting.

## 8. Exception Handling and Escalation

### 8.1 Standard Exception Process

A recognized need to deviate from the standard DSA template terms or procedure requires a formal exception. The requestor must submit a "Data Sharing Exception Request" (Form DSA-EXC-001) via MDGP. The form must detail:
- The specific controls or clauses from which deviation is requested.
- The compelling business justification (e.g., critical clinical trial milestone, irreplaceable dataset).
- A proposed compensating control (e.g., additional audit log access, increased cyber insurance coverage) to reduce risk to an acceptable level.

### 8.2 Approval Authority for Exceptions

| Risk Severity | Definition | Approval Authority |
| :--- | :--- | :--- |
| **Low** | Non-material administrative errors (e.g., extension of notice period by 10 business days). | CPO (Dr. Klaus Weber) and Data Steward. |
| **Medium** | Modification of a non-core data security control, sharing a Limited Data Set without a formal DUA counter-signature for < 30 days. | CPO and General Counsel (Maria Gonzalez) jointly. |
| **High / Critical** | Any waiver of GDPR Article 28 processor terms, waiver of international transfer safeguards, or sharing of full PHI without a BAA. | **CEO + CPO + General Counsel** unanimous approval; non-delegable. |

### 8.3 Emergency Access Protocol

In a situation involving an active, verifiable threat to life or health (e.g., a medical device vulnerability requiring immediate third-party forensics), the CPO may authorize a temporary, time-limited (48-hour) data sharing via verbal approval, documented and ratified within 72 hours. This does not exempt the sharing from Breach Notification laws if PHI is compromised.

## 9. Training Requirements

All Personnel identified in the RACI matrix (Section 3) must complete mandatory, role-based training on this SOP.

| Role | Training Module | Duration | Frequency | Delivery Method | Tracking |
| :--- | :--- | :--- | :---: | :--- | :--- |
| **All Staff** | "Data Sharing at Meridian: An Overview" (MDG-100) | 15 minutes | Annual | Digital Learning (Workday) | 100% Completion by Q1 |
| **Data Stewards** | "Defining and Classifying the ADS for Sharing" (MDG-200) | 45 minutes | Annual | Instructor-Led Webinar (Dr. Weber) | Workday+ Quiz (>80%) |
| **OGC / OCPO** | "Advanced DSA Negotiation: GDPR & HIPAA Interplay" (MDG-300) | 4 hours | Annual | Offsite Workshop | Workday, Certificate |
| **CEO / C-Suite** | "Executive Briefing: Data Sharing Risk Liability" (MDG-EXEC) | 30 minutes | Bi-Annual | In-Person Briefing | Acknowledgment Form |

Failure to complete required training within the calendar quarter triggers an automated notification to the employee's manager and a temporary revocation of access to the MDGP portal, preventing initiation of new DSAs.

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

- `SOP-IS-005`: Information Security Policy
- `SOP-IS-TPRM-001`: Third-Party Risk Management Standard
- `SOP-DGP-003`: Data Subject Access Request (DSAR) Handling Procedure
- `SOP-AIF-015`: AI Model Lifecycle Governance (Fairness, Explainability, and Transparency)
- `SOP-IG-002`: Records Retention and Destruction Schedule
- `INFOSEC-ENC-009`: Data Transfer Endpoint Encryption Standard
- Form DSA-101: Data Sharing Purpose and Need (MDGP)
- Form DSA-EXC-001: Exception Request (MDGP)

### 10.2 External Regulations and Standards

- **HIPAA:** 45 CFR Parts 160 and 164, Subpart A (General Provisions), Subpart C (Security Standards), Subpart D (Breach Notification), Subpart E (Privacy of Individually Identifiable Health Information).
- **GDPR:** Regulation (EU) 2016/679 of the European Parliament and of the Council, particularly Articles 5 (Principles), 6 (Lawfulness), 9 (Special Categories), 13-14 (Transparency), 17 (Right to Erasure), 26 (Joint Controllers), 28 (Processor), 30 (Records of Processing), 35 (DPIA), 44-49 (International Transfers).
- **Data Protection Act 2018 (UK GDPR):** Applicable to any Meridian business with UK data subjects, ensuring adequacy decisions and the UK Addendum to the SCCs.
- **NIST SP 800-88:** Guidelines for Media Sanitization (for Data Destruction protocols).
- **EU MDR 2017/745:** Annex I, Chapter II, Section 17 (Information Governance for Clinical Devices).

## 11. Revision History

| Version | Date | Author | Sections Revised | Description of Change |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 2024-02-01 | D. Weber (CPO) | All | Initial Release. Replaced prior ad-hoc DUA process. |
| 1.1 | 2024-09-12 | M. Chen (OCPO) | 5.4, 6, 9 | Added formal TIA procedure post-*Schrems II* ruling. Updated control CTL-DGP-012-04. Added Data Steward advanced training (MDG-200). |
| 2.0 | 2025-07-20 | D. Weber, M. Gonzalez | 1, 3, 5.2, 5.5, 8.2 | Major revision. Expanded scope to cover Confidential Business Information and AI Training Data. Streamlined triage SLA from 5 to 2 days. Updated Approval Matrix to address High-severity exceptions. |
| 2.1 | 2026-04-05 | J. Patel (OCPO Analyst) | 2, 5.4, 10.2, Cover | Routine annual review. Updated Definitions of SCCs to cite Implementing Decision (EU) 2021/914. Added BYOK pseudonymization gate requirement. Added UK GDPR cross-ref. Version bumped to 2.1. |
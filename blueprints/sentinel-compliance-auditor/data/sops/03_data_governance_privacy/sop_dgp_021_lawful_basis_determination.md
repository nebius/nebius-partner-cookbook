---
sop_id: "SOP-DGP-021"
title: "Lawful Basis Determination"
business_unit: "Data Governance & Privacy"
version: "5.4"
effective_date: "2024-12-26"
last_reviewed: "2025-09-11"
next_review: "2026-03-26"
owner: "Dr. Klaus Weber, Chief Privacy Officer / DPO"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Lawful Basis Determination

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the mandatory framework for identifying, documenting, and validating the lawful basis for all personal data processing activities conducted by Meridian Health Technologies, Inc. and its wholly-owned subsidiaries. The purpose of this SOP is to ensure that no personal data processing activity commences or continues without a properly identified, documented, and approved lawful basis as required under the General Data Protection Regulation (GDPR). This document provides the operational methodology by which Meridian demonstrates accountability for its processing activities through a defensible, auditable trail of lawful basis determinations.

### 1.2 Scope

This SOP applies to:

**In-Scope Entities:**
- Meridian Health Technologies, Inc. (Boston headquarters)
- Meridian Health Technologies GmbH (Berlin office)
- Meridian Health Technologies UK Ltd. (London office)
- Meridian Health Technologies Asia-Pacific Pte. Ltd. (Singapore office)
- Meridian Health Technologies Canada Inc. (Toronto office)
- All subsidiaries, joint ventures, and acquired entities where Meridian exercises operational control

**In-Scope Data Processing Activities:**
- Collection, recording, organization, structuring, storage, adaptation, retrieval, consultation, use, disclosure by transmission, dissemination, alignment, combination, restriction, erasure, or destruction of personal data
- Processing of personal data relating to: patients (via the Clinical AI Platform), healthcare provider employees (via HealthPay Financial Services), insured individuals (via MedInsight Analytics), website visitors, clinical trial participants, employees, contractors, job applicants, and business contacts
- Processing conducted wholly or partly by automated means, including AI/ML model training, inference, and scoring operations
- Processing conducted through third-party data processors and sub-processors engaged by Meridian
- Cross-border data transfers originating from the European Economic Area (EEA) and the United Kingdom

**Out-of-Scope Activities (explicit exclusions):**
- Processing of data pertaining exclusively to legal entities (corporations, partnerships) where no natural person is identifiable
- Processing of truly anonymized data where re-identification is impossible per Meridian's Anonymization Standard (SOP-DGP-019)
- Personal data processing conducted by employees for purely personal or household purposes on Meridian-owned devices (prohibited by Acceptable Use Policy SOP-INFOSEC-003)

### 1.3 Applicability

Compliance with this SOP is mandatory for all Meridian personnel, contractors, consultants, temporary workers, and third-party service providers who design, develop, test, deploy, operate, or procure systems that process personal data. Product Managers, Engineering Directors, and Data Stewards bear primary responsibility for initiating lawful basis determinations prior to the commencement of any new processing activity. Non-compliance with this SOP may result in disciplinary action up to and including termination of employment or contract, and may expose Meridian to regulatory fines and reputational damage.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Consent** | Any freely given, specific, informed, and unambiguous indication of the data subject's wishes by which he or she, by a statement or by a clear affirmative action, signifies agreement to the processing of personal data relating to him or her. |
| **Controller** | The natural or legal person which, alone or jointly with others, determines the purposes and means of the processing of personal data. For purposes of this SOP, Meridian acts as Controller for all processing activities except where a contractual arrangement designates Meridian as Processor. |
| **Data Subject** | An identified or identifiable natural person about whom Meridian processes personal data. |
| **Lawful Basis Determination (LBD)** | The formal, documented process by which a specific lawful basis for processing is selected, justified, and approved. |
| **Legitimate Interests Assessment (LIA)** | A three-part, documented assessment that (1) identifies the legitimate interest pursued by Meridian or a third party; (2) demonstrates the necessity of the processing to achieve that interest; and (3) balances Meridian's interests against the rights and freedoms of the data subjects concerned, concluding whether the legitimate interest provides a valid lawful basis. |
| **Personal Data** | Any information relating to an identified or identifiable natural person ('data subject'); an identifiable natural person is one who can be identified, directly or indirectly, in particular by reference to an identifier such as a name, identification number, location data, online identifier, or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural, or social identity of that natural person. |
| **Processing** | Any operation or set of operations which is performed on personal data or sets of personal data, whether or not by automated means. |
| **Special Categories of Personal Data** | Personal data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, or trade union membership; genetic data; biometric data processed for the purpose of uniquely identifying a natural person; data concerning health; data concerning a natural person's sex life or sexual orientation. |

### 2.2 Acronyms

| Acronym | Expansion |
|---|---|
| **DPO** | Data Protection Officer |
| **DPR** | Data Processing Register (Meridian's centralized record of processing activities, maintained in OneTrust) |
| **GC** | General Counsel |
| **LIA** | Legitimate Interests Assessment |
| **LBD** | Lawful Basis Determination |
| **ROPA** | Record of Processing Activities |
| **TIA** | Transfer Impact Assessment |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix

The following RACI matrix defines the roles and responsibilities for the Lawful Basis Determination process:

| Activity / Deliverable | Product Manager | Data Steward | Engineering Lead | Privacy Counsel | DPO | General Counsel | Chief Data Officer |
|---|---|---|---|---|---|---|---|
| Initiate LBD for new processing | **A** | **R** | C | C | I | I | I |
| Draft Legitimate Interests Assessment (LIA) | C | **R** | C | **A** | C | I | I |
| Draft Consent Mechanism | **R** | C | C | **A** | I | I | I |
| Approve LBD (Standard Risk) | C | C | C | **A/R** | C | I | I |
| Approve LBD (High Risk, including Special Categories) | C | C | C | C | **R** | **A** | I |
| Maintain Data Processing Register Entry | I | **R** | I | C | C | I | **A** |
| Annual LBD Recertification | **R** | C | C | **A** | I | I | I |

**R = Responsible** (performs the work); **A = Accountable** (approves, sign-off); **C = Consulted** (provides input); **I = Informed** (receives notification)

### 3.2 Named Role Responsibilities

**Dr. Klaus Weber, Chief Privacy Officer / DPO**
- Maintains authority and independence to exercise DPO functions as required.
- Provides advisory oversight on all LBDs involving Special Categories of data.
- Performs annual audits of the LBD control framework.
- Reports LBD compliance metrics to the Data Governance Council quarterly.

**Maria Gonzalez, General Counsel**
- Approves all LBDs classified as High Risk.
- Escalates unresolvable conflicts between Meridian's legitimate interests and data subject rights to the Executive Risk Committee.
- Authorizes the approval of exceptions to this SOP (see Section 8).

**Product Managers (per product line)**
- Initiate the LBD workflow within OneTrust within 5 business days of concept approval for any new processing activity.
- Serve as the primary point of contact for LIA evidence gathering.
- Implement technical controls mandated by the approved LBD (e.g., consent management modules, opt-out mechanisms).

**Data Stewards (Data Governance & Privacy Unit)**
- Conduct the operational work of drafting LBDs and LIAs.
- Maintain the accuracy and completeness of entries within Meridian's Data Processing Register.
- Flag overdue LBD recertifications to Product Managers monthly.

**Privacy Counsel**
- Review and approve LBDs classified as Standard Risk.
- Provide legal analysis for the balancing test phase of Legitimate Interests Assessments.
- Deliver the annual "Lawful Basis and You" training module.

---

## 4. Policy Statements

Meridian Health Technologies, Inc. commits to the following high-level policy statements regarding the determination of lawful bases for processing personal data:

- **PS-01: No Processing Without Lawful Basis.** Every instance of personal data processing conducted by or on behalf of Meridian must be mapped to a specific, identified lawful basis before the processing activity commences. Processing activities lacking a documented lawful basis are prohibited and must be immediately suspended upon discovery.

- **PS-02: Basis Must Be Recorded and Communicated.** The specific lawful basis relied upon for each processing purpose must be recorded in the record of processing activity and communicated to the data subject at the point of data collection via the applicable privacy notice (Customer Privacy Notice v.4.2; Employee Privacy Notice v.2.1).

- **PS-03: Lawful Basis Must Be Stable and Predictable.** Meridian will not arbitrarily switch between lawful bases for the same processing purpose. If a change in lawful basis becomes necessary due to a change in the purpose or means of processing, a new LBD must be completed and approved prior to implementing the change.

- **PS-04: Legitimate Interests Must Be Balanced.** For any processing activity where Meridian relies upon "Legitimate Interests" as its lawful basis (Article 6(1)(f)), a Legitimate Interests Assessment (LIA) must be completed, documenting the specific legitimate interest pursued, the necessity of the processing, and the conclusion that Meridian's interests do not override the fundamental rights and freedoms of the affected data subjects.

- **PS-05: Special Categories Require Enhanced Scrutiny.** Processing of Special Categories of Personal Data (Article 9) requires identification of a specific exemption condition under Article 9(2), documented in conjunction with the Lawful Basis Determination, and approved by the General Counsel. The standard of "explicit consent" for Special Categories requires a separate, granular, and verifiable affirmative opt-in.

- **PS-06: Consent Must Be Demonstrable, Granular, and Withdrawable.** Where Meridian relies upon consent as its lawful basis, the mechanism for obtaining such consent must include: a clear affirmative action, granular options (consent cannot be bundled), a record of the consent event, and an easily accessible mechanism for withdrawal of consent.

---

## 5. Detailed Procedures

This section details the operational steps required to complete a Lawful Basis Determination. All workflows are executed within the OneTrust Data Mapping module (Production Instance: `onetrust.meridian.health`), which serves as the system of record.

### 5.1 Procedure: Initiating a Lawful Basis Determination

This procedure is initiated when a Product Manager proposes a new processing activity, or when an existing activity changes purpose.

**Step 1: Identify Processing Trigger.** The Product Manager identifies that a new product feature, marketing initiative, or operational change will involve the collection or use of personal data. Triggers include, but are not limited to: Product Requirements Document (PRD) approval; Marketing campaign design; New vendor onboarding involving personal data; API endpoint creation exposing personal data.

**Step 2: Initiate LBD Ticket.** The Product Manager creates a new "Lawful Basis Determination" ticket within the OneTrust platform. The ticket must contain:
- Proposed processing activity name (must match the activity name in the Data Processing Register).
- Detailed description of the processing purpose (minimum 150 characters; vague descriptions like "analytics" are rejected).
- Categories of data subjects (e.g., patients, employees, HCPs, website visitors).
- Categories of personal data (e.g., contact details, health data, financial data, IP address).
- Identification of whether the processing involves Special Categories of data (Yes/No).
- Identification of data recipients (including third-party processors).

**Step 3: Ticket Triage.** The OneTrust workflow engine assigns the ticket to the designated Data Steward for the relevant business unit. The Data Steward has 3 business days to acknowledge the ticket and begin the LBD analysis. If Special Categories data is flagged, the ticket is automatically escalated to the DPO queue and assigned a "High Risk" classification.

### 5.2 Procedure: Selecting the Appropriate Lawful Basis

The Data Steward, in consultation with Privacy Counsel, analyzes the processing purpose against the six lawful bases defined in Article 6(1). The selection follows the decision hierarchy defined by the Data Governance Council.

**The Six Lawful Bases under Article 6(1):**
1.  **Consent (Article 6(1)(a)):** The data subject has given consent for one or more specific purposes.
2.  **Contractual Necessity (Article 6(1)(b)):** Processing is necessary for the performance of a contract to which the data subject is party, or in order to take steps at the request of the data subject prior to entering into a contract.
3.  **Legal Obligation (Article 6(1)(c)):** Processing is necessary for compliance with a legal obligation to which Meridian is subject.
4.  **Vital Interests (Article 6(1)(d)):** Processing is necessary in order to protect the vital interests of the data subject or of another natural person.
5.  **Public Task (Article 6(1)(e)):** Processing is necessary for the performance of a task carried out in the public interest, or in the exercise of official authority vested in Meridian.
6.  **Legitimate Interests (Article 6(1)(f)):** Processing is necessary for the purposes of the legitimate interests pursued by Meridian or by a third party, except where such interests are overridden by the interests or fundamental rights and freedoms of the data subject.

**Selection Decision Tree:**
The Data Steward must apply the following decision tree, documented within the OneTrust LBD module:

1.  **Check Legal Obligation (6(1)(c)) First.** Is the processing required by a specific, identified law or regulation (beyond general corporate record-keeping)? If yes, select **Legal Obligation**. Document the specific statutory or regulatory provision. (Note: Meridian's obligations under FDA 21 CFR Part 11 for Clinical AI Platform audit trails exemplify this basis.)

2.  **Check Contractual Necessity (6(1)(b)).** Is the processing genuinely necessary to deliver the core service requested by the data subject under a contract? This basis is narrow and strictly interpreted. It does not include processing for business improvement, marketing, or broad fraud prevention unrelated to the specific contract. Example: Processing an employee's bank details for payroll. If yes, select **Contractual Necessity**.

3.  **Check Vital Interests (6(1)(d)).** Is the processing necessary to protect someone's life? This basis is exceptionally rare in Meridian's operations. Document the life-threatening scenario. If yes, select **Vital Interests**.

4.  **Check Public Task (6(1)(e)).** Is Meridian exercising official authority or performing a specific task in the public interest (as mandated by law)? This basis is generally inapplicable to Meridian as a private, for-profit entity, with the potential exception of clinical trials mandated by public health authorities. If yes, select **Public Task** and document the legal mandate.

5.  **Evaluate Suitability of Consent (6(1)(a)).** Before considering Legitimate Interests, the Data Steward must ask: Would consent be effective and appropriate? Consent is the *required* starting point for marketing communications, certain cookie uses, and any Special Categories processing not falling under another Article 9 exemption. If the processing gives the data subject genuine, ongoing choice and control, select **Consent** and proceed to design the consent mechanism (per Section 5.5).

6.  **Consider Legitimate Interests (6(1)(f)).** If none of the above bases apply, the Data Steward must consider Legitimate Interests. **This basis cannot be selected as a default.** The Data Steward must complete the Legitimate Interests Assessment detailed in Section 5.3.

**Documenting the Basis:**
The Data Steward populates the "Lawful Basis" field in the OneTrust processing record and drafts a justification statement (minimum 300 characters) explaining why the selected basis is applicable and why other bases were ruled out. This justification is reviewed and approved per the risk classification workflow.

### 5.3 Procedure: Conducting the Legitimate Interests Assessment (LIA)

Where Legitimate Interests is identified as the proposed lawful basis, the Data Steward must complete the **Meridian Legitimate Interests Assessment (Form LIA-001)** . This procedure must not be circumvented.

**Step 1: Identify the Legitimate Interest.** The Data Steward documents the specific interest pursued. It must be:
- **Lawful:** The interest itself must be lawful.
- **Real and Present:** Not speculative or hypothetical. Examples include: network and information security (legitimate), preventing fraud against Meridian (legitimate), direct marketing of similar products to existing customers (legitimate, subject to opt-out), improving core platform functionality through pseudonymized usage analytics (legitimate, subject to controls).
- **Sufficiently Specific:** Vague references to "business purposes" are rejected.

**Step 2: Necessity Test.** The Data Steward must determine if the processing is *necessary* to achieve the stated purpose. The question is: "Is there another, less intrusive way to achieve the same result?" If a reasonable, less privacy-intrusive alternative exists, the processing is not "necessary," and the Legitimate Interests basis fails. Document the consideration and rejection of less intrusive alternatives.

**Step 3: Balancing Test.** The Data Steward must balance Meridian's legitimate interest against the interests, fundamental rights, and freedoms of the data subjects. This assessment must specifically consider:
- **The Nature of the Interest:** Is it compelling or trivial?
- **The Impact on Data Subjects:** What is the nature of the processing? What is the reasonable expectation of the data subject? How intrusive is the processing? Consider the volume of data, sensitivity, and impact on vulnerable individuals (e.g., patients). Meridian's scale of processing in AI and analytics inherently increases the potential impact.
- **The Mitigating Controls:** What safeguards are in place to minimize impact (e.g., pseudonymization, data minimization, strong access controls, opt-out mechanisms)?

**Step 4: Conclusion and Approval.** The Data Steward records the conclusion of the balancing test: either Meridian's interests override the data subject's interests (basis valid), or they do not (basis invalid, must revert to Consent or redesign processing). The completed LIA Form LIA-001 is attached to the OneTrust record.

| Assessment Component | Guiding Questions for Data Steward |
|---|---|
| Purpose Identification | Is the interest lawful, specific, and clearly articulated? |
| Necessity Assessment | Could the purpose be reasonably achieved by alternative, less intrusive means? |
| Balancing Test — Data Subject Expectations | Would a reasonable data subject expect this processing in the given context? |
| Balancing Test — Impact Severity | What is the potential severity of impact on the individual (minor annoyance to significant harm)? |
| Balancing Test — Vulnerable Individuals | Are the data subjects children, patients, or otherwise vulnerable persons? |
| Balancing Test — Mitigating Safeguards | Can pseudonymization, data minimization, or an easily accessible opt-out reduce the impact? |

### 5.4 Procedure: Processing Special Categories of Data

When the LBD Ticket flags Special Categories of Data, this procedure applies in addition to the Article 6 basis selection.

**Step 1: Article 9 Exemption Identification.** The Data Steward must, in collaboration with the DPO, identify both an Article 6 lawful basis AND a specific Article 9(2) exemption condition. The most common applicable exemptions for Meridian are:
- **Article 9(2)(a) — Explicit Consent:** The data subject has given explicit consent for one or more specified purposes. This requires a distinct, granular consent mechanism.
- **Article 9(2)(h) — Health or Social Care:** Processing is necessary for the purposes of preventive or occupational medicine, medical diagnosis, the provision of health or social care or treatment, or the management of health or social care systems and services. This is frequently relevant for the Clinical AI Platform.
- **Article 9(2)(j) — Scientific Research:** Processing is necessary for archiving purposes in the public interest, scientific or historical research purposes or statistical purposes. This is relevant for MedInsight Analytics de-identification protocols.

**Step 2: Enhanced Documentation.** The justification statement in OneTrust must explicitly reference the selected Article 9(2) exemption and explain its applicability. For explicit consent, the specific consent language displayed to the data subject must be attached to the record.

### 5.5 Procedure: Designing a Consent Mechanism

Where Consent is selected as the lawful basis, the Product Manager and UX Design Lead must collaborate with the Data Steward to design the consent collection mechanism according to the following technical requirements:

1.  **Granularity:** Consent requests must be presented separately for each distinct processing purpose. Consent may not be bundled, e.g., "I agree to receive marketing emails AND have my data shared with partners" must be two separate checkboxes.
2.  **Affirmative Action:** Pre-ticked boxes or implied consent from inaction are prohibited. The mechanism requires a clear, un-ticked checkbox, toggle, or similar active user interface element.
3.  **Informed:** The consent request must include, in plain language: the identity of the controller (Meridian), the purpose of each processing operation, and the types of data to be processed.
4.  **Conditionality (Prohibition on Bundling):** Consent for non-essential processing cannot be made a condition of service. Access to the Clinical AI Platform for clinicians cannot be made conditional on consent to receive marketing newsletters.
5.  **Record-Keeping:** The Meridian Identity and Consent Service (MICS, `mics.meridian.health`) must log each consent event with a timestamp, the specific consent language version shown, the data subject's identity, and the mechanism used. These logs are immutable and retained for the duration of processing plus 6 years.
6.  **Withdrawal:** Withdrawing consent must be as easy as giving it. A consent management dashboard accessible via the Meridian Privacy Center allows data subjects to view and withdraw consent for each purpose in real time.

#### 6.2 Technical Controls (MAP)

| **Control ID** | **Control Description** | **Implementation Mechanism** |
|---|---|---|
| **CTL-DGP-022-07** | Purpose Limitation Enforcement. Data tagged for a specific processing purpose cannot be repurposed without a new LBD. | Meridian Data Catalog (Alation) enforces purpose-based access tags. A dataset tagged "Purpose: Payroll Processing" cannot be accessed by the Marketing Analytics cluster. |
| **CTL-DGP-022-08** | Storage Limitation Tracking. Personal data processed under a specific lawful basis must have a defined retention period mapped to that basis. | Retention rules in MICS and OneTrust are linked to the LBD record. Automated data deletion jobs execute based on these rules (per SOP-DGP-018, Data Retention and Disposal). |
| **CTL-DGP-022-09** | LBD Status Monitoring. An automated script (`lbd_monitor.py`) queries the OneTrust API daily to identify any processing activities lacking an active, approved LBD, and generates an alert to the Data Governance & Privacy Operations team. |

### 5.6 Procedure: Documenting and Communicating the Basis

**Step 1: Register of Processing Activities (ROPA).** All lawful basis determinations are centrally recorded in the Meridian Record of Processing Activities maintained in OneTrust. Each processing activity record must link directly to the approved LBD.

**Step 2: Privacy Notice Mapping.** Within 30 calendar days of LBD approval, the Product Manager must ensure that the applicable external or internal privacy notice accurately reflects the purposes and lawful bases of processing. The Meridian Privacy Notice Management Console tracks versioning and links notice clauses directly to OneTrust processing records.

---

## 6. Controls and Safeguards

Meridian implements the following technical and administrative controls to ensure the integrity of the lawful basis determination framework:

### 6.1 Administrative Controls

| Control ID | Control Description | Control Owner | Frequency |
|---|---|---|---|
| **AC-LBD-01** | Mandatory review of all active LBDs by the Data Steward and Product Manager. Recertification that the original basis remains valid and that the processing purpose has not shifted. | Data Steward | Annual, or upon material change |
| **AC-LBD-02** | The DPO conducts a random sampling of 20% of all approved LBDs per quarter for quality assurance, checking adherence to the decision hierarchy and adequacy of the LIA. | DPO | Quarterly |
| **AC-LBD-03** | All new LBDs for High Risk processing are reviewed by the General Counsel prior to implementation. | Privacy Counsel / DPO | Per Event |
| **AC-LBD-04** | Data Processor Agreement (DPA) reviews must confirm that the processor's documented lawful basis is consistent with Meridian's instructions. | Vendor Management / Privacy Counsel | Onboarding and Annual Renewal |

### 6.2 Technical Controls

| Control ID | System / Platform | Control Description |
|---|---|---|
| **TC-LBD-05** | OneTrust | Workflow engine prevents a processing activity record from moving from "Design" to "Production" status without an approved LBD attached. |
| **TC-LBD-06** | OneTrust | Automated alerts to Data Stewards at 90, 60, and 30 days prior to LBD recertification due date. |
| **TC-LBD-07** | Immutable Audit Log (Splunk) | All LBD approvals, rejections, and modifications are logged with user ID, timestamp, and change detail. |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The Data Governance & Privacy Unit tracks the following metrics in the monthly Data Governance Dashboard (Tableau):

| Metric | Target | Measurement Method |
|---|---|---|
| **LBD Coverage Rate** | 100% | (Number of Production processing records with an Approved LBD) / (Total Number of Production processing records) * 100. |
| **LBD Recertification Timeliness** | ≥ 95% on-time | Percentage of LBDs recertified on or before the annual due date. |
| **Mean Time to Approve (MTTA) — Standard Risk** | ≤ 10 business days | Average elapsed time from LBD ticket creation to Privacy Counsel approval for Standard Risk tickets. |
| **Mean Time to Approve (MTTA) — High Risk** | ≤ 20 business days | Average elapsed time from ticket creation to GC/DPO approval. |
| **Legitimate Interests Basis Usage** | Trend monitoring | The absolute number and proportion of processing activities relying on Legitimate Interests versus Consent or other bases. An increasing trend triggers a review by the DPO. |

### 7.2 Reporting Cadence

- **Monthly:** Operational MTTA and recertification metrics reported to the Chief Data Officer and relevant Product Directors.
- **Quarterly:** Aggregate KPI report, LIA quality audit results, and basis-usage trends reported to the Data Governance Council, chaired by the Chief Data Officer and including the DPO and General Counsel.
- **Annually:** Comprehensive review of the LBD framework presented to the Audit Committee of the Board of Directors.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Requests

Situations may arise where strict adherence to this SOP's timeline or procedural steps is impracticable. Such deviations require a formal exception request. Examples include: an urgent product patch requiring immediate personal data processing to rectify a patient safety issue where MTTA cannot be met; an acquisition integration where processing activities must commence before full LBDs are cataloged.

### 8.2 Exception Procedure

1.  **Documentation:** The requesting Product Manager must complete the "SOP Exception Request" form within the OneTrust Policy Management module. The form requires a detailed description of the deviation, the compelling business or technical justification, the impacted scope (data subjects, data categories), a proposed compensating control, and a defined remediation date.
2.  **Review:** The DPO reviews the exception for privacy risk. The Chief Information Security Officer (CISO) reviews for security risk.
3.  **Approval Authority:**
    - Exceptions extending timelines by ≤ 15 business days for Standard Risk processing are approved by the DPO.
    - All exceptions involving Special Categories of data or High Risk processing require the joint written approval of the DPO, the CISO, and the General Counsel.
4.  **Tracking:** All approved exceptions are logged in a central register, and the remediation date is tracked by the DPO. Expired, unremediated exceptions are immediately escalated to the General Counsel for potential service suspension.

---

## 9. Training Requirements

### 9.1 Mandatory Training Assignments

All personnel assigned a role in the RACI matrix (Section 3.1) must complete the following training:

| Training Module | Course ID | Required For | Frequency | Platform |
|---|---|---|---|---|
| Lawful Basis and You | PRIV-LBD-101 | All Product Managers, Data Stewards, Marketing Managers, UX Designers | Annually | Workday Learning |
| Advanced Legitimate Interests Assessment | PRIV-LBD-201 | Privacy Counsel, Data Stewards, DPO | Annually | Workday Learning |
| OneTrust Data Mapping & LBD Workflow | OT-WF-040 | Data Stewards, Privacy Counsel | On Role Assignment + Annually | OneTrust University |

### 9.2 Training Compliance Tracking

Training completion is tracked within the Workday Learning Management System (LMS). On the first day of each month, an automated report identifies any in-role personnel with overdue training assignments. This report is sent to the individual's direct manager and the DPO. Access to OneTrust data mapping modules may be suspended for personnel with training compliance gaps exceeding 60 days.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| Document ID | Document Title | Relationship |
|---|---|---|
| SOP-DGP-001 | Data Governance Framework Charter | Defines the overarching governance structure. |
| SOP-DGP-022 | Record of Processing Activities (ROPA) Management | Defines the procedure for maintaining the central ROPA into which LBDs are recorded. |
| SOP-DGP-018 | Data Retention and Disposal Standard | Defines retention rules linked to lawful basis. |
| SOP-INFOSEC-012 | Access Control Standard | Details authentication and authorization controls protecting personal data. |
| SOP-RMC-005 | Third-Party Vendor Risk Management | Covers due diligence for data processors, including validating their lawful basis. |
| SOP-DEV-030 | Secure SDLC Policy | Mandates LBD initiation at the design phase of software development. |

### 10.2 External References

- Regulation (EU) 2016/679 (General Data Protection Regulation)
- UK General Data Protection Regulation, as amended
- ICO Guidance: Lawful basis for processing
- EDPB Guidelines 2/2019 on the processing of personal data under Article 6(1)(b) GDPR in the context of the provision of online services to data subjects

---

## 11. Revision History

| Version | Date | Author | Description of Change |
|---|---|---|---|
| 1.0 | 2018-05-15 | Anna Petrova, Privacy Manager | Initial version created in preparation for GDPR enforcement. |
| 2.0 | 2019-08-20 | Anna Petrova, Privacy Manager | Added detailed Legitimate Interests Assessment procedure and Form LIA-001. |
| 3.0 | 2020-11-01 | Dr. Klaus Weber, DPO | Incorporation of UK GDPR post-Brexit transition period; added OneTrust integration points. |
| 4.0 | 2022-02-18 | Dr. Klaus Weber, DPO | Major revision: introduced formal RACI matrix, Consent Mechanism Design Procedure (Section 5.5), and recertification KPIs. |
| 5.0 | 2023-01-15 | Maria Gonzalez, GC / Dr. Klaus Weber, DPO | Revised exception handling for High Risk processing per Executive Risk Committee directive; updated MTTA targets. |
| 5.1 | 2023-06-10 | Dr. Klaus Weber, DPO | Clarified exclusion of anonymized data scope; updated cross-references for new Data Retention SOP. |
| 5.2 | 2023-11-05 | Dr. Klaus Weber, DPO | Annual review cycle update; minor text corrections to Article 9 exemption guidance. |
| 5.3 | 2024-06-22 | Dr. Klaus Weber, DPO | Incorporated CE marking obligations as a "Legal Obligation" lawful basis example. Approved by M. Gonzalez. |
| 5.4 | 2024-12-26 | Dr. Klaus Weber, DPO | Updated recertification process to include automated OneTrust alerts; revised Section 7 KPIs for MTTA targets. This version supersedes all prior versions. |
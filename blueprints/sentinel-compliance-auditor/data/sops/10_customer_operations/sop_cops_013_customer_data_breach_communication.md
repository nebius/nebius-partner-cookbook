---
sop_id: "SOP-COPS-013"
title: "Customer Data Breach Communication"
business_unit: "Customer Operations"
version: "4.0"
effective_date: "2025-09-04"
last_reviewed: "2026-02-12"
next_review: "2026-08-07"
owner: "Michael Chang, VP of Customer Operations"
approver: "Robert Liu, VP of Financial Services"
classification: "Internal"
regulations:
  - "GDPR"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Customer Data Breach Communication

## SOP-COPS-013

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the mandatory framework, operational responsibilities, protocols, timelines, and communication templates governing Meridian Health Technologies, Inc.’s response to confirmed or reasonably suspected breaches of customer data. The procedure is designed to ensure that all external and internal communications are executed with precision, legal accuracy, regulatory compliance, and operational consistency, while maintaining the trust of our customers, partners, patients, and the public.

This SOP operationalizes Meridian’s commitment to transparency, accountability, and the protection of personal data as prescribed by applicable data protection laws, contractual obligations, and our internal policies. It provides the single source of truth for the Customer Operations team and all stakeholders involved in breach communication lifecycle management.

### 1.2 Scope

This SOP applies to all business units, departments, subsidiaries, and geographies of Meridian Health Technologies, Inc., including but not limited to:

- **Customer Operations** (primary executing unit)
- **Information Security** (CISO)
- **Privacy Office / Data Protection Officer (DPO)**
- **Legal and Compliance**
- **Clinical AI Platform**
- **HealthPay Financial Services**
- **MedInsight Analytics**
- **Meridian SaaS Platform**
- **Engineering and IT Operations**
- **Marketing and Corporate Communications**
- **Human Resources**

**In-Scope Data Incidents:**

This SOP governs communications for any security incident involving the actual or suspected:

1.  **Confidentiality Breach:** Unauthorized access, disclosure, or acquisition of Customer Data.
2.  **Integrity Breach:** Unauthorized alteration, corruption, or destruction of Customer Data.
3.  **Availability Breach:** Unauthorized or accidental loss of access to, or destruction of, Customer Data, where such loss has a significant impact on customer operations (as defined in customer Service Level Agreements).

**In-Scope Data Types:**

- **Customer Operational Data:** Configuration data, system logs, metadata, administrative credentials, and API keys related to customer environments on the Meridian SaaS Platform.
- **Personal Data (as defined by GDPR Article 4(1)):** Any information relating to an identified or identifiable natural person processed on behalf of our customers, including patients, healthcare providers, and employees.
- **Special Categories of Personal Data (GDPR Article 9):** Data revealing racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic data, biometric data for the purpose of uniquely identifying a natural person, data concerning health, or data concerning a natural person's sex life or sexual orientation. This is highly prevalent in MedInsight Analytics and Clinical AI Platform data sets.
- **Financial Data:** Payment card information, bank account details, credit history, and loan information processed by HealthPay Financial Services.
- **Account Credentials:** Usernames, passwords, multi-factor authentication tokens, and Single Sign-On (SSO) assertions.

**Out of Scope:**

- Internal HR data breaches not impacting customer data are governed by SOP-HR-007: Employee Data Breach Response.
- Physical security breaches of Meridian office space not involving digital customer data are governed by SOP-SEC-014: Physical Incident Response.
- Breaches of Meridian's own corporate financial data are governed by SOP-FIN-022.

### 1.3 Applicability

This SOP applies to all Meridian employees, contractors, consultants, interns, and third-party vendors who have access to Meridian systems or data, or who are involved in the incident response and communication lifecycle. Compliance with this SOP is a condition of employment and contractual engagement. Failure to adhere to the procedures defined herein may result in disciplinary action, up to and including termination of employment or contract, and potential civil or criminal liability.

---

## 2. Definitions and Acronyms

For the purposes of this SOP, the following definitions apply. Terms are aligned with GDPR Article 4 definitions where applicable.

| Term | Definition |
| :--- | :--- |
| **Breach (Confirmed)** | A security incident that has been verified by the Security Incident Response Team (SIRT) and the Privacy Office to have resulted in the accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to, Customer Data. |
| **Breach (Suspected)** | A security incident that, based on initial indicators and an active investigation, is reasonably believed to have resulted in a breach, but for which a formal confirmation has not yet been made. |
| **Business Continuity Plan (BCP)** | The documented collection of procedures and information that is developed, compiled, and maintained in readiness for use in an incident to enable Meridian to continue to deliver its critical products and services at an acceptable predefined level. |
| **Communication Lead** | The single designated individual from Customer Operations responsible for drafting, coordinating approvals, and disseminating all breach-related communications to the affected customer. |
| **Controller** | The natural or legal person, public authority, agency, or other body which, alone or jointly with others, determines the purposes and means of the processing of personal data (GDPR Article 4(7)). Our customers are the Controllers for the data we process. |
| **Customer Data** | All data, including Personal Data, provided, generated, or processed by or on behalf of Meridian’s customers through the use of Meridian’s products and services. |
| **Data Protection Officer (DPO)** | Dr. Klaus Weber, Meridian's statutorily appointed Data Protection Officer per GDPR Article 37, based in Berlin, responsible for overseeing data protection strategy and compliance and serving as the primary contact for supervisory authorities. |
| **Data Subject** | An identified or identifiable natural person to whom Personal Data relates (GDPR Article 4(1)). |
| **Incident Commander** | The individual from the Security Incident Response Team (SIRT) with overall authority and responsibility for managing the technical and operational response to a security incident. |
| **Personal Data Breach** | A breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to, personal data transmitted, stored, or otherwise processed (GDPR Article 4(12)). |
| **Processor** | A natural or legal person, public authority, agency, or other body which processes personal data on behalf of the controller (GDPR Article 4(8)). Meridian acts as a Data Processor for our customers. |
| **Security Incident** | An event or series of events involving the Meridian technology stack that has the potential to compromise the confidentiality, integrity, or availability of Customer Data. An incident is a precursor to a potential breach. |
| **Security Incident Response Team (SIRT)** | The cross-functional team led by the CISO's office, responsible for the technical investigation, containment, eradication, and recovery from security incidents. |
| **Supervisory Authority (SA)** | An independent public authority established by an EU Member State responsible for monitoring the application of the GDPR. The Lead Supervisory Authority for Meridian is the Berliner Beauftragte für Datenschutz und Informationsfreiheit (Berlin DPA). |

### Acronyms

| Acronym | Full Name |
| :--- | :--- |
| **BCP** | Business Continuity Plan |
| **CISO** | Chief Information Security Officer |
| **DPA** | Data Protection Authority (interchangeable with Supervisory Authority) |
| **DPO** | Data Protection Officer |
| **DPIA** | Data Protection Impact Assessment |
| **EDR** | Endpoint Detection and Response |
| **KB** | Knowledge Base |
| **MTTD** | Mean Time to Detect |
| **MTTR** | Mean Time to Resolve |
| **NIST** | National Institute of Standards and Technology |
| **PII** | Personally Identifiable Information |
| **PHI** | Protected Health Information |
| **RACI** | Responsible, Accountable, Consulted, Informed |
| **SA** | Supervisory Authority |
| **SIEM** | Security Information and Event Management |
| **SIRT** | Security Incident Response Team |
| **SLA** | Service Level Agreement |
| **SSO** | Single Sign-On |
| **TPS** | Transactions Per Second |

---

## 3. Roles and Responsibilities

The following RACI matrix delineates the specific responsibilities of named roles and functional groups during a breach communication event. This matrix assumes a "Confirmed Breach" scenario requiring immediate and comprehensive action.

| Activity / Decision | VP Customer Ops (M. Chang) | DPO (Dr. K. Weber) | CISO (SIRT Lead) | General Counsel | Incident Commander | Communication Lead | Customer Success Manager (CSM) | Corp. Comms |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Breach Declaration** — Formal confirmation of a notifiable breach | A | R | C | C | I | I | I | I |
| **2. Severity & Impact Assessment** — Determination of regulatory and contractual impact scope | C | R | R | A | C | I | C | I |
| **3. Notification Strategy** — Selection of communication tiers, channels, and timing | A | C | C | C | I | R | C | I |
| **4. Draft Initial Notification** — Creation of customer-facing breach notification | I | C | C | R | I | A | C | I |
| **5. Legal & Regulatory Review** — Approval of notification language for legal accuracy | I | C | I | A | I | R | I | I |
| **6. Customer Communication Delivery** — Execution of outbound communication via selected channels | A | I | I | I | I | R | R | I |
| **7. Notify SA (GDPR Art. 33)** — Submission of notification to Berlin DPA within 72 hours | I | R | C | A | C | I | I | I |
| **8. Public Relations Statement** — Issuance of public-facing statements, if required | C | C | I | A | I | I | I | R |

**Responsibility Key:**
- **R:** Responsible (Performs the task)
- **A:** Accountable (Ultimate ownership — the "buck stops here")
- **C:** Consulted (SME input required before action)
- **I:** Informed (Notified after decision/action)

### 3.3 Detailed Role Descriptions

**3.3.1 VP of Customer Operations (Michael Chang):**
As the Owner of this SOP, Mr. Chang is the Accountable executive for the entire breach communication lifecycle. He authorizes all customer-facing notifications before dissemination, resolves resource conflicts within the Customer Operations team, and serves as the executive escalation point for customer grievances related to breach communications.

**3.3.2 Data Protection Officer (Dr. Klaus Weber):**
Dr. Weber has the independent authority and responsibility, as mandated by GDPR Article 39, to advise on and monitor Meridian’s compliance with data protection law. For breach communications, his role is to:
- Make the formal Responsible determination of whether a breach is "likely to result in a risk to the rights and freedoms of natural persons" (GDPR Article 33).
- Lead the Responsible drafting and submission of the supervisory authority notification within 72 hours.
- Advise on the specific content and data subject-facing language of customer breach notifications when high-risk processing is involved.
- Serve as the primary point of contact for the Berlin DPA and all other EU supervisory authorities.

**3.3.3 General Counsel:**
The General Counsel is Accountable for the final legal review and approval of all external breach notification language to manage corporate liability, contractual obligations, and litigation risk. This includes the approval of any public-facing statements coordinated by Corporate Communications.

**3.3.4 Customer Success Manager (CSM):**
The assigned CSM is the human face of Meridian for the affected customer. They are Responsible for delivering the notification via approved, secure channels such as a scheduled video call. They are also responsible for post-communication relationship management, including coordinating technical briefings and managing follow-up questions documented in Salesforce.

---

## 4. Policy Statements

The following statements constitute the high-level policy commitments of Meridian Health Technologies, Inc., regarding data breach communication. These statements are mandatory and non-discretionary.

**PS-001: Commitment to Transparency**
Meridian will, in good faith, communicate confirmed breaches of Customer Data to affected customers with clarity, accuracy, and without undue delay. Transparency is the foundational principle upon which customer trust is maintained. We will not misrepresent, delay beyond regulatory or contractual timelines without explicit approval per Section 8, or obfuscate the facts of a breach.

**PS-002: Regulatory Compliance Primacy**
All breach communication activities will be conducted in strict adherence to applicable data protection laws, with primacy given to the General Data Protection Regulation (GDPR). Where regulatory obligations conflict with commercial interests, regulatory obligations shall prevail. The DPO has the authority to override standard communication timelines to meet statutory deadlines.

**PS-003: Precision and Accuracy**
All communications, from initial notification to final forensic report summary, must be factually precise, verified by the SIRT, and approved by Legal. No speculation, blame attribution, or unverified information shall be included in any customer-facing communication. All statements must be demonstrably true at the time of communication.

**PS-004: Designated Communication Channels**
Breach notifications must be delivered exclusively through approved, secure channels as defined in Section 5.6. No breach-related communication shall be conducted via unofficial channels, personal devices, or unapproved messaging platforms.

**PS-005: Single Point of Contact**
Each affected customer will be assigned a Communication Lead and a CSM as their dedicated, named points of contact throughout the breach response lifecycle. This team is responsible for delivering a unified, consistent, and cohesive message to the customer, preventing information asymmetry and confusion.

**PS-006: Confidentiality of Investigations**
Details of an ongoing internal investigation, including raw forensic data, internal incident tickets, and unconfirmed root cause hypotheses, are classified "Meridian Internal: SIRT" and are strictly privileged. Only the final, approved Root Cause Analysis (RCA) summary may be shared externally, and only after Legal and the DPO have approved its release.

**PS-007: Continuous Improvement**
Every confirmed breach event shall undergo a formal "Black-Box Review" within 30 days of closure. A summary of communication lessons learned, metric deviations, and proposed improvements to this SOP and related templates will be submitted to the VP of Customer Operations for review and approval.

---

## 5. Detailed Procedures

This section defines the mandatory operational procedures for executing a Customer Data Breach Communication event. These procedures are sequential and time-bound unless otherwise explicitly extended via the Exception Handling process in Section 8.

### 5.1 Phase 1: Incident Verification and Severity Assessment

This phase begins immediately upon the creation of a Severity 1 (Sev1) incident ticket in ServiceNow by the SIRT.

**Step 1.1: Trigger Event**
The Incident Commander raises a Sev1 incident in ServiceNow (`INC-SIRT`) indicating confirmed or highly-suspected unauthorized access, exfiltration, encryption, or destruction of Customer Data.

**Step 1.2: Immediate Stakeholder Paging**
The Incident Commander on-call page triggers an automated paging workflow (PagerDuty `Meridian_SIRT_OnCall` service) which simultaneously alerts:
- VP of Customer Operations (Michael Chang) or delegate
- DPO (Dr. Klaus Weber) or delegate
- General Counsel office (via `Legal-Breach-Hotline` distribution list)
- CISO or delegate

A secure, emergency-response Slack channel (`#incident-<INC-ID>-command`) is automatically created and all paged members are forcefully joined.

**Step 1.3: 60-Minute Triage Window**
Within 60 minutes of the Sev1 ticket creation, a "Triage Call" must be convened and chaired by the Incident Commander. The mandatory agenda is:
1.  **Facts Summary:** SIRT presents a concise, factual summary of the incident (time of detection, initial vector, systems/data affected, containment actions taken). No speculation.
2.  **Data Affected Confirmation:** SIRT confirms the specific data repositories, S3 buckets, or database tables involved. The DPO maps this to the record of processing activities (ROPA) to identify Controllers, Data Subjects, and data categories.
3.  **Breach Determination Vote:** The DPO makes a formal, recorded determination: (a) Confirmed Breach of Personal Data, (b) Confirmed Breach of Non-Personal Data, or (c) Incident, Investigation Pending. For option (a), the 72-hour notification clock under GDPR Article 33 formally begins.
4.  **Customer Impact Scoping:** The CSM Lead for the affected product identifies the specific customer accounts, tenants, and configurations involved. A preliminary list is presented.
5.  **Communication Lead Nomination:** The VP of Customer Operations nominates and confirms the Communication Lead for this incident.

**Deliverable:** ServiceNow ticket `INC-SIRT` is updated with "Triage Decision" and "Affected Customers (Preliminary)." The 72-hour SA notification clock timestamp is logged for option (a) events.

### 5.2 Phase 2: Notification Preparation and Approval Workflow

This phase is executed concurrently with the SIRT's ongoing containment and investigation.

**Step 2.1: Template Selection and Assembly**
The Communication Lead, in consultation with the DPO and Legal, selects the appropriate initial notification template from the Meridian Legal and Comms Template Library (Google Drive: `Legal_Templates/Breach_Notifications/v4.0/`). The primary templates are:

| Template ID | Template Name | Use Case | Regulatory Trigger |
| :--- | :--- | :--- | :--- |
| **T-GDPR-33-A** | SA Notification — GDPR Art. 33 | Formal notification to the Berlin DPA | GDPR Art. 33 (all breaches) |
| **T-GDPR-34-A** | Data Subject Notification — GDPR Art. 34 | Direct communication to individuals | GDPR Art. 34 (high risk) |
| **T-CUST-01** | Initial Customer Breach Notification — Controller | First formal notice to our direct customer/Controller | Contractual & GDPR Art. 33(3) |
| **T-CUST-02** | Follow-up Breach Notification — Controller | Update to customer on findings, remediation | Best practice, contractual |
| **T-CUST-03** | Final Breach RCA Summary — Controller | Final report to customer post-investigation | Best practice |

**Step 2.2: Draft Initial Customer Notification (T-CUST-01)**
The Communication Lead populates `T-CUST-01` within 4 hours of the Triage Decision. This draft is created in a secure, access-controlled Google Doc (`breach-comms-<INC-ID>-draft`) shared only with the approval chain. The draft must contain, at a minimum, the following mandatory fields:

- **Incident Summary:** A plain-language, non-technical description of the incident (e.g., "On [DATE], Meridian detected unauthorized access to a database supporting the MedInsight Analytics platform. The accessed data included reports generated by your organization.")
- **Nature of the Breach:** A factual statement, e.g., "A vulnerability in a third-party software library was exploited to gain unauthorized access."
- **Categories of Personal Data Concerned:** (e.g., Name, Health Insurance Number, Diagnosis Codes (ICD-10), Bank Account Details). The DPO provides this precise list from the ROPA.
- **Approximate Number of Data Subjects Concerned:** (e.g., "Approximately 14,900 individuals whose data was processed in the affected reports.")
- **Likely Consequences:** A brief, factual assessment of risk (e.g., "The likely consequences include a risk of identity theft, potential for medical identity fraud, and risk of financial loss.")
- **Measures Taken or Proposed:** What Meridian has done (e.g., "The vulnerable service was immediately isolated, the vulnerability was patched, and the compromised credentials were revoked. Mandiant has been engaged for a forensic investigation.")
- **Customer Action Required:** Clear, actionable directives for the customer (Controller) e.g., "As the Data Controller, you are legally obligated to assess your duty to notify the affected Data Subjects under GDPR Article 34. We recommend you contact your legal counsel to prepare a notification. Meridian will provide a detailed FAQ document to support your communications within 24 hours."
- **Designated Meridian Contacts:** Name, title, direct line, and secure email of the Communication Lead and CSM.

**Step 2.3: Approval Workflow Execution**
The Communication Lead initiates the electronic approval workflow via DocuSign CLM with a strict 48-hour maximum completion window. The approval order and criteria are:

1.  **DPO (Dr. Weber) — Compliance Approval:** Reviews the notification against GDPR Articles 33 and 34. Verifies the accuracy and completeness of the regulatory content. *Decision Criteria: The notification fully and accurately satisfies the processor's obligations to inform the controller without undue delay.*
2.  **General Counsel — Legal/Commercial Approval:** Reviews the notification for legal liability, contractual compliance, adherence to confidentially clauses in our DPA, and litigation risk. *Decision Criteria: The language protects Meridian’s legal and commercial interests without breaching our transparency commitment.*
3.  **VP of Customer Operations (M. Chang) — Final Approval:** Confirms the operational readiness to deliver the communication via the channels defined. Ensures the CSM team is fully briefed and the FAQ support document is prepared. *Decision Criteria: All operational prerequisites for a successful, empathetic, and controlled customer delivery are met.*

### 5.3 Phase 3: Supervisory Authority Notification (GDPR-Focused)

This is a legally distinct and critically time-sensitive procedure executed by the DPO's office.

**Step 3.1: Strict 72-Hour Timeline Adherence**
Per GDPR Article 33(1), in the case of a personal data breach, Meridian as Processor shall notify the Controller (our customer) without undue delay. To ensure our customers as Controllers can meet their 72-hour deadline to the SA, Meridian commits to delivering `T-CUST-01` with a complete SA-ready facts package to the customer within **24 hours** of the Breach Confirmation (Triage Decision). This is Meridian's primary regulatory communication SLA.

**Step 3.2: Direct SA Notification Protocol (Contingency)**
Pursuant to GDPR Article 28(3)(f), if a Meridian customer (Controller) is demonstrably unable or unwilling to notify the SA, and the DPO advises that a notification must be made to mitigate immediate risk of harm, Meridian will, acting on the documented instructions of the Controller, notify the Berlin DPA (or relevant Lead SA). This is executed using Template `T-GDPR-33-A`.

The `T-GDPR-33-A` content follows GDPR Article 33 requirements strictly and must include:
- Nature of the breach: categories, approximate numbers of data subjects and data records.
- DPO contact details: Dr. Klaus Weber, direct office line (+49 30 1663 4827), dpo@meridian-healthtech.de.
- Likely consequences of the breach.
- Measures taken or proposed to be taken by the processor.

**Step 3.3: Communication to Data Subjects (Art. 34)**
When a breach is likely to result in a *high risk* to the rights and freedoms of natural persons, our customer (Controller) is obligated to communicate the breach to the Data Subject without undue delay (GDPR Art. 34). As the Processor, Meridian's role is to provide the Controller, within the `T-CUST-01` package, with a complete, clear, and plain-language communication pack (`T-GDPR-34-A` template pre-populated) that the Controller can, at its discretion, deploy. This pack includes Meridian's recommendation that notification occur via direct, prominent channels (e.g., email, SMS, in-app notification).

### 5.4 Phase 4: Customer Communication Delivery

**Step 4.1: Channel Selection Mandate**
Communication must be tiered based on incident severity and regulatory urgency. The VP of Customer Operations selects the tier.

**Tier 1 — Sev1 Breach: Highly Urgent & Regulatory-Driven**
*   **Channel 1 (Mandatory — Within 1 hr of final T-CUST-01 approval):** A mandatory, out-of-band secure communication to the customer's named executive and security contacts. This is delivered via PGP-encrypted email to pre-registered emergency contacts stored in the Customer Contact Registry in Salesforce. The email subject line will follow the format: `[URGENT - ACTION REQUIRED] Meridian Security Incident Notification - Case #<INC-ID>`.
*   **Channel 2 (Mandatory — Within 1 hr of email):** The assigned CSM initiates a direct, secure video call (using Zoom E2EE) with the customer's executive team. During this call, the CSM verbally walks through the `T-CUST-01` document, answers initial questions, and coordinates the flow of subsequent information. The call is logged in Salesforce with the outcome.
*   **Channel 3 (As Directed):** A formal, registered letter is dispatched to the customer's legal department if so directed by Meridian's General Counsel (typically for breaches involving large volumes of financial or health data).

**Step 4.2: Communication Delivery Confirmation**
The Communication Lead is responsible for logging a detailed delivery confirmation in the ServiceNow incident record (`INC-SIRT`) for each affected customer, including:
- Timestamp of encrypted email delivery and read receipt (if obtained).
- Timestamp, duration, and attendees of the secure video call.
- Timestamp of any out-of-band phone call.
- Explicit confirmation that the communication was received by a named individual at the customer.

### 5.5 Phase 5: Follow-Up and Final Closure

**Step 5.1: Daily Status Updates**
The Communication Lead provides a written daily status update (via PGP-encrypted email) to all affected customers for the duration of the incident, at a consistent time of 09:00 and 17:00 local time for the customer's primary contact. The update will include: current investigation status, confirmed root cause (if validated), progress on data restoration, and a forecast for the Final RCA Summary (`T-CUST-03`).

**Step 5.2: Final Root Cause Analysis (RCA) Summary**
Within 10 business days of incident closure and confirmation from SIRT that root cause is fully identified and remediated, the Communication Lead assembles and delivers the final `T-CUST-03` package. This package contains three sections:
1.  **Executive Summary:** A non-technical summary of the RCA, impact assessment, and Meridian's remediation plan, approved by the VP of Customer Operations and Legal.
2.  **Technical RCA:** (Optional, by customer request) A detailed technical report from SIRT, sanitized to remove Meridian's internal architecture specifics. The CISO must approve distribution.
3.  **Audited Evidence of Remediation:** A summary of the corrective actions applied, e.g., "WAF Rule `WAF-4472` deployed globally to block SQL injection vector," with a statement of verification.

**Step 5.3: Formal Incident Closure**
The incident is formally closed in ServiceNow when `T-CUST-03` delivery is confirmed for all affected customers, and the VP of Customer Operations moves the incident state to "Closed - Comms Complete." This triggers the automated Black-Box Review scheduling per CS-007.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

| Control ID | Control Description | Control Mechanism | Owner |
| :--- | :--- | :--- | :--- |
| **ADM-001** | **Annual Breach Communication Drill** | Mandatory, company-wide, multi-product simulated breach exercise ("Project Nightlight"). Must test the full activation of the incident command structure, template selection, and delivery of a simulated notification to mock customer executives within the defined SLAs. | VP Customer Ops & CISO |
| **ADM-002** | **Semi-Annual Template Review** | All communication templates (T-CUST-01 through 03, SA, and Data Subject) are reviewed for legal and regulatory accuracy by Legal and the DPO. Version updates are approved and published in the Google Drive repository. | DPO / General Counsel |
| **ADM-003** | **Customer Contact Registry Integrity** | The Salesforce Customer Contact Registry, containing Tier 1 emergency contacts, must be verified by the CSM team on a quarterly basis. A mandatory field completeness check is enforced on key accounts. | VP Customer Ops |
| **ADM-004** | **Segregation of Duties** | The individual who writes a breach notification cannot be the same individual who performs the final approval of the same notification. The DocuSign workflow enforces this through role-based routing. | VP Customer Ops |

### 6.2 Technical Controls

| Control ID | Control Description | Technical Mechanism | System/Tool |
| :--- | :--- | :--- | :--- |
| **TEC-001** | **PGP Encryption Enforcement** | All Tier 1 outbound email notifications are programmatically encrypted via a server-side policy. The ServiceNow-Jira integration fetches the customer's public PGP key from the Registry. Emails to unregistered contacts are blocked by Secure Email Gateway (SEG). | Mimecast SEG, Salesforce API |
| **TEC-002** | **Secure Drafting Environment** | All draft communications are created, shared, and approved exclusively within Meridian's Google Workspace environment, governed by data loss prevention (DLP) rules. Forwarding or downloading of `breach-comms-*` documents is blocked by a context-aware access policy. | Google Workspace, GSuite DLP |
| **TEC-003** | **Non-Repudiation of Approval** | The DocuSign approval workflow records a tamper-proof audit trail with a cryptographic signature for each approval step, ensuring non-repudiation. | DocuSign CLM |
| **TEC-004** | **Zoom E2EE Requirement** | All Tier 1, Channel 2 video calls with customers must be conducted using Zoom's End-to-End Encrypted (E2EE) meeting configuration, preventing Meridian's own Zoom infrastructure from having access to decryption keys. | Zoom Admin Console |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The performance and effectiveness of this SOP are measured against the following Key Performance Indicators. Target SLAs are absolute thresholds.

| KPI ID | Metric Description | Target (SLA) | Measurement Tool | Reporting Cadence |
| :--- | :--- | :--- | :--- | :--- |
| **KPI-01** | **Mean Time to First Customer Notification (MTTCN)** — Time elapsed from Sev1 ticket creation to confirmed delivery of T-CUST-01 via Channel 1 to the first affected customer. | **≤ 4 hours** | ServiceNow | Real-time dashboard, Monthly CSM Review |
| **KPI-02** | **Mean Time to All-Customer Notification (MTTACN)** — Time elapsed from Sev1 ticket creation to confirmed delivery for the last affected customer. | **≤ 8 hours** | ServiceNow | Monthly CSM Review |
| **KPI-03** | **Supervisory Authority Notification SLA Compliance** — Percentage of incidents where `T-CUST-01` (with SA-ready pack) was delivered to the customer/Controller enabling their ≤72-hour SA deadline. Meridian's internal sub-SLA is ≤24 hours. | **100%** | ServiceNow, DPO Quarterly Report | Quarterly Executive Review |
| **KPI-04** | **Customer Communication Accuracy Rate** — Percentage of closed incidents where no post-closure errata or correction was required for the customer-facing T-CUST-01 notification. | **≥ 99.5%** | ServiceNow Post-Incident Review | Quarterly Executive Review |
| **KPI-05** | **Drill Performance Score** — Score achieved during the annual "Project Nightlight" drill, measured against a pre-published scorecard. | **≥ 85%** | Drill After-Action Report | Annual |

### 7.2 Dashboards and Reporting

1.  **Real-Time Breach Communication Dashboard:** A dedicated, read-only dashboard in Grafana, fed by ServiceNow data, showing the status of all active breach communication events. Displayed on a large wall monitor in the SIRT war room and available digitally to named roles. Displays MTTCN, MTTACN, and approval workflow status.
2.  **VP Customer Ops Monthly CSM Review:** A monthly meeting where KPI-01 and KPI-02 are reviewed, deviations are analyzed, and process adjustments are discussed.
3.  **Quarterly Executive Privacy and Security Review:** Chaired by the CISO and DPO, this meeting includes a review of KPI-03 and KPI-04, presenting a scorecard on overall breach communication regulatory compliance posture to the C-Suite.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Handling

Any deviation from the mandatory timelines, channel selection, or approval workflow defined in Section 5 constitutes an Exception. Exceptions must be formally approved *before* the deviation occurs, except in circumstances where immediate action to contain a greater harm is required (e.g., notifying law enforcement before a customer as directed by a court order).

**Exception Procedure:**

1.  **Request Initiation:** The individual seeking the exception (typically the Communication Lead or DPO) creates an Exception Request ticket in ServiceNow (`INC-SIRT` related service request), detailing:
    - **SOP Reference:** The specific step or KPI being deviated from.
    - **Reason for Exception:** A clear, fact-based justification. "Resource constraints" is not a valid justification.
    - **Impact of Deviation:** An assessment of the increased risk or impact of not following the standard procedure.
    - **Mitigation Plan:** The alternative actions being proposed to minimize the increased risk.
2.  **Exception Approval:** The Exception must be approved by two parties simultaneously: **VP of Customer Operations (Michael Chang)** AND **General Counsel**. In the case of a regulatory-trigger exception, the **DPO (Dr. Weber)** serves as a third required approver. A tie is resolved in favor of the most privacy-conservative option.
3.  **Logging:** All approved exceptions are formally logged in the `INC-SIRT` record and aggregated in a quarterly Exception Report reviewed by Internal Audit.

### 8.2 Escalation Matrix

If the Communication Lead encounters an unresolvable blocker at any stage of the procedure, the following escalation path is mandatory. Each step must be given a maximum of 15 minutes to respond before the next level is engaged.

| Escalation Level | Role | Name | Contact Method | Trigger Condition |
| :--- | :--- | :--- | :--- | :--- |
| **Level 1** | Incident Commander | (SIRT On-Call) | PagerDuty, #incident-command Slack | Standard collaboration. |
| **Level 2** | VP of Customer Operations | Michael Chang | PagerDuty `mgmt-oncall`, direct mobile | Resolver delay > 30 mins; critical customer rejection of comms. |
| **Level 3** | Chief Legal Officer / DPO | Legal-OC / Dr. Klaus Weber | `Legal-Breach-Hotline` phone bridge, DPO direct mobile | Legal approval standstill; regulatory dispute; risk of non-compliance with Art. 33 timelines. |
| **Level 4** | Chief Executive Officer | Boardroom Line | Secure call via CISO | Corporate existential threat; instruction from Level 3 executives to escalate. |

---

## 9. Training Requirements

### 9.1 Role-Based Training Curriculum

Compliance with this SOP requires rigorous, role-specific training that is tracked and verified.

| Training Module ID | Module Name | Target Audience | Frequency | Delivery Method | Proficiency Verification |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T-COPS-013-A** | Breach Communication Standard Operating Procedure: Foundation | All in-scope personnel (per Section 1.2) | **Annual** | Mandatory e-Learning course (Litmos) | 100% score on final quiz with 3 attempts. |
| **T-COPS-013-B** | Breach Communication Command and Control Drill | SIRT, DPO, Legal, Comms Lead, CSMs | **Annual** (aligned with "Project Nightlight") | "Project Nightlight" tabletop/physical simulation | Performance score from drill assessor. Score below 70% triggers mandatory retraining. |
| **T-COPS-013-C** | Advanced Breach Communications for Executives | VP Customer Ops, DPO, General Counsel, CISO | **Biennial** | Expert-led, closed-door seminar by external counsel on the latest precedents. | Facilitator sign-off on participation. |
| **T-COPS-013-D** | Breach Template Workshop for CS Ops | Communication Lead Pool, Tier 2 Support Engineers | **Semi-Annual** | Hands-on instructor-led workshop reviewing recent template changes and common errors. | Submission and instructor approval of a practice notification based on a fictitious scenario. |

### 9.2 Training Tracking and Enforcement

All training records are maintained in Litmos and tied to employee HR files. Non-completion of mandatory training (T-COPS-013-A, T-COPS-013-B) by the annual deadline will result in:
1.  Automated notification to the employee and their manager 30 days, 14 days, and 3 days before the deadline.
2.  Immediate revocation of access to the `breach-comms-*` templates and related ServiceNow workflows 1 day past the deadline.
3.  A formal Performance Improvement Plan (PIP) entry, documented by the employee's manager, following a grace period of 7 days post-deadline.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | SOP Title | Relationship |
| :--- | :--- | :--- |
| **SOP-IS-009** | Information Security Incident Response Plan | Parent procedure for all security incidents. This Comms SOP is a downstream execution branch. |
| **SOP-PRIV-002** | Record of Processing Activities (ROPA) and DPIA Management | Source of truth for mapping data types, systems, and Controllers used in Phase 1.3 triage. |
| **SOP-LEG-005** | Third-Party Vendor Breach Response | Procedure for incidents originating at a sub-processor (e.g., AWS, Mandiant). |
| **SOP-BCP-011** | Business Continuity and Disaster Recovery Plan | Provides the operational framework for restoring services while communication procedures occur in parallel. |
| **SOP-COPS-016** | Secure Customer Contact Registry Management | Procedure for maintaining the veracity and security of the emergency contacts used in Tier 1 notifications. |
| **SOP-HR-007** | Employee Data Breach Response | Governing SOP for breaches of internal HR data, which are explicitly out of scope here. |

### 10.2 External References

| Reference ID | External Standard/Regulation | Relevant Section |
| :--- | :--- | :--- |
| **GDPR** | General Data Protection Regulation (Regulation (EU) 2016/679) | Articles 4, 9, 28, 33, 34, 37-39 |
| **NIST SP 800-61 Rev. 2** | Computer Security Incident Handling Guide | Incident Response Lifecycle Alignment |
| **ISO/IEC 27035-2:2016** | Information security incident management — Part 2: Guidelines to plan and prepare for incident response | Framework for incident categories and response planning |

---

## 11. Revision History

| Version | Date | Author(s) | Summary of Changes |
| :--- | :--- | :--- | :--- |
| **1.0** | 2020-03-15 | S. Johansson, Legal | Initial draft, pre-CSAT implementation. Basic email templates only. |
| **2.0** | 2021-11-09 | A. Gupta, Customer Ops | Major revision. Added Phase 1 triage procedure, formal RACI matrix, and Tier 1/Tier 2 communication channels. Integrated with PagerDuty for paging. |
| **2.1** | 2022-07-22 | Dr. K. Weber, DPO | Minor revision. Aligned all templates and timelines with new EU Standard Contractual Clauses and refined the SA notification procedure. |
| **3.0** | 2023-05-04 | M. Chang & M. Rivera | Major revision post-MedInsight launch. Expanded scope to include health data (GDPR Art. 9). Introduced T-GDPR-34-A template and mandatory secure video call tier. Defined the "Black-Box Review" mandate. |
| **4.0** | 2025-09-04 | M. Chang & Office of General Counsel | Full rewrite. Migrated entire approval workflow to DocuSign CLM. Replaced Slackbridge with native PagerDuty paging. Codified the 24-hour SA pack SLA as a core regulatory KPI. Updated all templates to `v4.0` to cover HealthPay and Clinical AI product-specific use cases. Formalized the "Exception Handling" section. |
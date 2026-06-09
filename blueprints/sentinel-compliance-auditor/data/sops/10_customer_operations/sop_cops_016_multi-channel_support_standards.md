---
sop_id: "SOP-COPS-016"
title: "Multi-Channel Support Standards"
business_unit: "Customer Operations"
version: "3.2"
effective_date: "2024-07-20"
last_reviewed: "2025-09-09"
next_review: "2026-03-03"
owner: "Michael Chang, VP of Customer Operations"
approver: "Robert Liu, VP of Financial Services"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Multi-Channel Support Standards

## 1. Purpose and Scope

This Standard Operating Procedure (SOP) establishes the uniform standards, protocols, and governance framework for delivering customer support across all communication channels at Meridian Health Technologies, Inc. The purpose of this document is to ensure that every customer interaction—regardless of the entry point—is handled with equivalent rigor, security, and quality, thereby maintaining the integrity of our SOC 2 Type II controls, HIPAA compliance obligations, and contractual commitments to the 340+ hospitals, clinics, and payer organizations relying on Meridian’s AI-powered healthcare fintech platforms.

**Scope:** This SOP applies to all Customer Operations personnel, including Tier 1, Tier 2, and Tier 3 support analysts, Customer Success Managers (CSMs), and any Meridian employee or contractor who interacts with external customers through official support channels. The covered channels include the Meridian Support Portal (web-based ticketing), email, live chat, phone, and integrated in-app messaging within the Meridian SaaS Platform and Clinical AI Platform. This SOP also governs the handoff protocols between Customer Operations and the following internal groups: Clinical AI Engineering, HealthPay Financial Services Operations, MedInsight Analytics Support, IT Operations, and the Security Operations Center (SOC). All procedures herein apply to interactions involving Protected Health Information (PHI), personally identifiable information (PII), and sensitive financial data processed by the HealthPay platform subject to SR 11-7 model risk management oversight.

**Applicability:** This SOP is binding on all full-time, part-time, and contract personnel within the Customer Operations business unit. It also applies to third-party vendors providing outsourced Tier 1 support services, as explicitly referenced in the Meridian Vendor Management Policy (SOP-SEC-011) and the Business Associate Agreement (BAA) framework managed by the General Counsel’s office. Non-compliance with these procedures shall be subject to corrective action per SOP-HR-004 (Employee Disciplinary Procedures).

---

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
|--------------|------------|
| **AHT** | Average Handle Time. Mean duration of a customer interaction from initiation to closure, inclusive of post-interaction documentation. |
| **BAA** | Business Associate Agreement. Legal contract governing PHI handling between Meridian and its customers or vendors. |
| **CJIS** | Criminal Justice Information Services. Security framework referenced for certain government-contracted modules, though not primary for this SOP. |
| **CSAT** | Customer Satisfaction Score. Post-interaction survey metric measured on a 1-5 Likert scale. |
| **FCR** | First Contact Resolution. Percentage of issues resolved during the initial interaction without escalation or callback. |
| **HIPAA** | Health Insurance Portability and Accountability Act of 1996. U.S. federal law governing PHI privacy and security. |
| **MFA** | Multi-Factor Authentication. An authentication method requiring two or more verification factors, enforced via Okta for all support tools. |
| **PHI** | Protected Health Information. Individually identifiable health information held or transmitted by Meridian or its business associates. |
| **PII** | Personally Identifiable Information. Information that can distinguish or trace an individual’s identity. |
| **SLA** | Service Level Agreement. Contractual commitment between Meridian and its customers regarding support responsiveness and resolution timelines. |
| **SOC 2** | Service Organization Control 2. Auditing standard for service providers storing customer data in the cloud, focusing on Trust Services Criteria (Security, Availability, Confidentiality, Processing Integrity, Privacy). |
| **SR 11-7** | Federal Reserve / OCC guidance on Model Risk Management applicable to HealthPay Financial Services models. |
| **SSO** | Single Sign-On. Authentication scheme allowing users to log in with a single ID to any of several related systems, implemented via Okta. |
| **Tier 1** | Frontline customer support handling initial intake, triage, and resolution of known issues. Staffed internally and via approved external BPO partner. |
| **Tier 2** | Technical support specialists handling complex troubleshooting, configuration changes, and detailed data analysis. Internal Meridian employees only. |
| **Tier 3** | Engineering and specialized support. Comprises dedicated pods from Clinical AI, HealthPay, MedInsight, and Platform Engineering. |
| **TSM** | Ticket Status Management. Central ticketing platform (Jira Service Management Cloud) used for all channel intake. |
| **VOC** | Voice of the Customer. Aggregate qualitative feedback and quantitative CSAT/VOC survey data. |

---

## 3. Roles and Responsibilities

This section establishes the responsibility assignment matrix for multi-channel support operations. The matrix clarifies accountability for each critical function, ensuring alignment with SOC 2 Trust Services Criteria pertaining to Security and Availability.

### 3.1 RACI Matrix

| Activity / Decision | CAIO (Chair) | CHRO (Owner) | CMO | DPO | VP, Cust Ops | Tier 2 Lead | BPO Manager |
|---------------------|--------------|--------------|-----|-----|--------------|-------------|-------------|
| **Channel Configuration & SSO Enforcement** | A | C | I | R | R | C | I |
| **PHI Disclosure Review (per ticket)** | I | I | A | R | C | C | C |
| **Severity 1 Outbreak Detection & Escalation** | R | I | C | I | A | R | I |
| **SOC 2 Quarterly Access Review (Support Tools)** | A | C | I | R | R | C | C |
| **Quarterly Metric Review & SLA Adjustment** | A | R | C | C | R | C | C |
| **Annual BAA Training for BPO Agents** | I | I | I | A | C | I | R |

**R=Responsible, A=Accountable, C=Consulted, I=Informed**

### 3.2 Defined Roles

- **VP of Customer Operations (Michael Chang):** Accountable for operational performance across all channels. Owners of Tier 1 and Tier 2 resourcing, including the third-party BPO contract for Tier 1 overflow support. Ensures adherence to SOC 2 Control Activities for staffing and training.
- **VP of Financial Services (Robert Liu):** Approver of this SOP due to the direct impact of support interactions on HealthPay model users. Ensures that support processes do not introduce unvalidated workarounds into SR 11-7 governed model outputs.
- **Clinical Risk Escalation Liaison:** A designated Tier 3 nurse-clinician responsible for immediate clinical triage if a support ticket suggests a potential adverse clinical event resulting from AI model output.
- **BPO Tier 1 Manager:** External partner lead. Responsible for adherence to Meridian’s SSO, MFA, and clean desk policy. Operates strictly within a zero-PHI-storage environment; agent screens are blocked from local caching.

---

## 4. Policy Statements

Meridian Health Technologies is committed to delivering support services that meet the Availability, Confidentiality, and Processing Integrity criteria of our SOC 2 certification. The following high-level policy commitments govern all multi-channel support operations:

1. **Universal Intake & Uniformity:** Any communication intended as a request for support received via email, portal form, chat, phone, or in-app messenger will be ingested into the TSM platform (Jira Service Management) as a formal, auditable ticket. No out-of-band support for covered systems is permitted. Support provided via unrecorded instant message or personal device is a direct violation of this policy.
2. **Identity Verification:** Before discussing any account-specific information, PII, or PHI across any channel, the agent must authenticate the contacting party via Okta SSO challenge or Meridian-established out-of-band verification. Support shall only be provided to named contacts registered in the customer’s active directory record.
3. **Channel-Neutral SLA Adherence:** Response and resolution targets are governed by the customer’s contractual SLA tier, not by the channel of intake. A patient safety issue reported via phone carries the same severity weighting and response clock as one submitted via the portal. (See Section 5.1).
4. **Prohibition of Uncontrolled Electronic Transmission of PHI:** Agents will not send unstructured PHI via standard email. All PHI-containing responses must be delivered through the secure TSM portal or encrypted within an Okta-authenticated session. This is a technical enforcement point, not merely procedural guidance, enforced by Data Loss Prevention (DLP) rules on the Jira and email platforms.
5. **Data Integrity & Audit Trail:** All modifications to ticket data, including severity reclassification, reassignment, and resolution status changes, are logged immutably in the TSM audit log. This meets the SOC 2 Processing Integrity requirement for complete, accurate, and timely data processing.
6. **Breach Notification:** In the event of a confirmed breach originating from or discovered through a support channel interaction (e.g., misrouted PHI, unauthorized access), the DPO must be notified within 15 minutes of discovery. The DPO will convene the Breach Response Team. The organization will notify affected customers and individuals without unreasonable delay, recognizing that the specific 60-day timeline to report an impermissible disclosure of PHI affecting 500 or more individuals to HHS and media is a distinct, legally defined requirement managed under SOP-LEG-001. Any unauthorized disclosure of PHI affecting any number of individuals is escalated and logged as a formal incident.

---

## 5. Detailed Procedures

### 5.1 Channel-Specific Procedures & Intake

All channels converge into Jira Service Management (TSM). Agents are required to work from TSM, even if the initial customer contact was via a synchronous channel.

| Channel | Intake Method | Identity Verification Requirement | Permissible Content | Special Constraints |
|---------|---------------|----------------------------------|---------------------|---------------------|
| **Meridian Support Portal** | Self-service web form (Okta SSO-enforced) | Automatic via MFA-secured login session. Additional verification for high-risk financial transactions. | All support requests, including those containing PHI if masked via auto-redaction rules in the form parser. | Primary intake channel for Clinical AI and HealthPay support. PHI upload requires explicit session-bound encryption key. |
| **Email** | Monitored inbox (support@meridianhealthtech.com). Automated forwarding rule creates TSM ticket; sender receives auto-acknowledgment. | Agent must verify sender identity via Okta verification link if PHI is present or before executing any account changes. Outbound PHI via email is blocked by DLP; agents redirected to TSM secure reply. | Non-urgent technical inquiries, pre-sales, documentation requests. PHI in free-text email body triggers automatic DLP hold. | SOC 2 Control: Emails with attachments classified as PHI are quarantined; agent manually releases them to TSM after DPO audit approval. |
| **Live Chat (Web & In-App)** | Intercom chat widget, integrated with Okta for session token. Transcript auto-saved into TSM upon close. | Pre-authenticated via Okta SSO for in-app; web chat requires validation of email vs. authorized contact DB before PHI discussion. | Quick configuration guidance, “how-to” inquiries. PHI strictly prohibited in web chat. In-app chat allows PHI only within the authenticated clinical workspace session. | Full transcript stored in TSM for 7 years per HIPAA and SOC 2 retention requirements. |
| **Phone** | Toll-free line. All calls recorded (IVR warning). Agent manually creates TSM ticket during/after call; call recording linked to ticket. | Agent verifies caller’s identity using the Meridian Directory and three-factor challenge (caller name, org, callback number verified against CRM). Outbound callbacks mandatory if disconnection. | Severity 1 clinical outage, urgent HealthPay transaction issue, or patient data integrity questions. | PHI discussed verbally only after full identity verification. Agent creates ticket within 90 seconds of call initiation and marks severity. |

### 5.2 Triage and Severity Assignment

Upon ticket creation, regardless of channel origin, the agent must assign a severity level based on the business impact matrix below. Severity dictates response and resolution SLA timers.

| Severity | Definition (Impact) | Initial Response SLA | Resolution SLA (Target) | Applies to Channels |
|----------|---------------------|----------------------|-------------------------|---------------------|
| **Sev 1 – Critical** | System down / complete loss of clinical or financial transaction processing capability affecting multiple customers; potential patient safety incident. | 15 minutes (24x7) | 1 hour (or activated workaround) | All channels. Phone automatically triggers Sev 1 timer. |
| **Sev 2 – High** | Major functionality impaired; no workaround available; single hospital or large HealthPay customer unable to process. | 30 minutes (business hours); 1 hour (off-hours) | 4 hours | All channels. |
| **Sev 3 – Medium** | Partial loss of function; workaround available; non-urgent configuration error. | 2 business hours | 1 business day | Portal, Email, Chat. |
| **Sev 4 – Low** | Cosmetic issues, documentation errors, general inquiries. | 4 business hours | 3 business days | All channels. |

**SOC 2 Control:** Monthly review of Sev 1 and Sev 2 tickets against contractual SLAs is performed by the VP, Customer Operations, and reported to the Management Review Board (MRB). Evidence is retained for SOC 2 audit testing of the Availability and Processing Integrity criteria.

### 5.3 Channel-to-Channel Handoff (Warm Transfer)

A handoff occurs when a support interaction requires transfer from one channel to another, or from one support tier to another, while the customer remains engaged.

1.  **Initiation:** The handing-off agent (Agent A) informs the customer of the need to transfer to a specialist (e.g., from Chat to Phone, or from Tier 1 to Tier 2). Agent A briefs the receiving party.
2.  **Warm Transfer Protocol:**
    - Agent A opens a conference bridge or internally transfers the chat transcript to Tier 2.
    - For phone-to-phone, Agent A performs a warm transfer. If the call is dropped, Agent A is accountable for immediate outbound callback using the CRM-verified number.
    - All PHI discussed in the pre-transfer phase is flagged in the TSM ticket; receiving agent (Agent B) must verbally confirm they have accessed the secure ticket before proceeding.
3.  **Documentation:** Agent A documents the transfer time, receiving agent’s name, and a summary of the transfer in the TSM ticket. The ticket remains open.
4.  **Channel Shift to PHI-Safe Mode:** If a customer on Chat attempts to paste plain-text PHI, Agent A must immediately request the customer use the Portal (Secure Upload) or Phone. Agent A pastes a pre-approved message: *“For your security, this information cannot be accepted here. Please upload it via your secure portal ticket [Ticket-ID].”* Agent A then closes the chat transcript to new text and marks it for PII Review.

### 5.4 Ticket Closure and Quality Assurance

Before closing a ticket, the Tier 1 or Tier 2 agent must complete the “Closure Checklist” embedded in the TSM workflow:

- [ ] Customer verified and satisfied with resolution (verbal / written confirmation).
- [ ] All temporary access grants (e.g., vendor remote access, temporary PHI view permissions) have been revoked.
- [ ] Root cause analysis (if applicable) is linked to the Major Case Record in Confluence.
- [ ] Incident classification confirmed: “Actual Security Incident,” “PHI Slip-Up (Training Opportunity),” or “None.”
- [ ] If PHI was inadvertently disclosed during the support interaction, the incident has been logged and the DPO auto-notified via the TSM “Privacy Incident” tag. This feeds the organization’s breach notification log, which tracks all incidents. The organization then evaluates its breach notification obligations under HIPAA, recognizing the specific timelines for reporting.

A daily QA sample of 10% of all closed tickets is drawn. A dedicated QA Specialist analyzes for:
- Adherence to identity verification protocol.
- Correct severity assignment per business impact.
- Proper handoff documentation.
- Absence of PHI in insecure channel logs.

Findings are logged in the QA module within Zendesk WFM and presented at the weekly VOC/Customer Experience review.

---

## 6. Controls and Safeguards

This SOP implements specific technical and administrative controls to satisfy SOC 2 Trust Services Criteria, with particular focus on Security, Availability, and Confidentiality.

### 6.1 Technical Controls

| Control ID | Control Name | Description | SOC 2 Criteria Met |
|------------|--------------|-------------|---------------------|
| **TAC-01** | Jira SSO & MFA Enforcement | All access to TSM requires Okta-based SSO with MFA. Password-only access is prohibited. Session timeout set to 15 minutes of inactivity. | Security (CC6.1), Availability |
| **TAC-02** | DLP on Email & Chat | Data Loss Prevention engine scans all outbound email and chat transcripts for PHI patterns (SSN, MRN, etc.) and blocks/quarantines violations. | Confidentiality (CC6.7), Privacy |
| **TAC-03** | Immutable Ticket Logs | Jira audit logs track every field change, access, and export. Logs are shipped to Splunk for SOC monitoring and are non-repudiable. | Processing Integrity (PI1.3) |
| **TAC-04** | Call Recording Encryption | All call recordings are encrypted at rest (AES-256) and in transit (TLS 1.3). Access restricted to QA Manager and internal Tier 3 investigation leads. | Security (CC6.1), Confidentiality |
| **TAC-05** | PHI Masking API | A middleware API sits between TSM and external notification services (SMS, push). Any outbound notification containing ticket data is scanned; PHI is replaced with a secure link forcing Okta re-authentication. | Confidentiality |

### 6.2 Administrative Controls

| Control ID | Control Name | Description | Frequency | Audited By |
|------------|--------------|-------------|-----------|------------|
| **AAC-01** | User Access Review (Support Tools) | All accounts with access to TSM, Intercom, Aircall, and Jira admin panels are reviewed. Orphan accounts terminated, privileges matched to current HR roster. | Quarterly | CISO, DPO |
| **AAC-02** | Agent Session Audit | Random sampling of agent screen recordings (with PII/PHI redaction in audit view) assessed for procedural compliance and secure handling. | Weekly (10 samples) | QA Manager, CHRO |
| **AAC-03** | BPO & Vendor Audit | Audit of the external BPO provider’s adherence to clean desk, secure network, and agent identity management. Includes review of BAAs and SOC reports of the sub-service organization. | Semi-Annually | VP, Cust Ops, DPO |
| **AAC-04** | Escalation Path Integrity Test | Unannounced simulated “Sev 1” ticket submitted via each channel to verify alert routing, DPO notification, and CISO on-call pager activation within SLA timeframes. | Monthly | CAIO |

---

## 7. Monitoring, Metrics, and Reporting

Continuous monitoring and quantitative measurement are essential to demonstrate the efficacy of support controls and ensure SLA compliance. All metrics are aggregated in an executive dashboard (built on Tableau, sourced from Jira and Intercom).

| Metric KPI | Target | Measurement Method | Reporting Cadence | Responsible Owner |
|------------|--------|--------------------|--------------------|--------------------|
| **First Contact Resolution (FCR)** | ≥ 70% for Tiers 1&2 combined | TSM Ticket Resolve count / Total Tickets | Weekly | VP, Customer Ops |
| **Average Speed to Answer (Phone)** | ≤ 90 seconds (24x7 for Sev1 capable line) | Aircall analytics | Daily | BPO Manager |
| **CSAT Score** | ≥ 4.5 / 5.0 | Post-interaction survey (Medallia) triggered on ticket close | Weekly (aggregated); Monthly (per-agent) | VP, Customer Ops |
| **Sev 1 Resolution SLA Compliance** | 99.5% within 1 hour | TSM data; time from Sev 1 designation to status ‘Resolved’ or ‘Workaround Provided’ | Monthly | CAIO |
| **Ticket Volume Trend (by Channel)** | Monitor for anomalies (±30% week-over-week) | TSM and Tableau trend analysis | Weekly | VP, Customer Ops |
| **QA Audit Score** | Average ≥ 95% adherence to SOP-COPS-016 controls | QA checklist randomized sampling (10% of closed tickets) | Bi-Weekly | CHRO |

**SOC 2 Reporting:** The outputs of these monitoring activities—specifically FCR, Sev 1 compliance, and CSAT—are compiled quarterly into the SOC 2 Management Assertion report for the Availability and Processing Integrity criteria. The system-generated logs of the monitoring process itself (TSM audit log, Tableau access log) are retained for the full audit period.

---

## 8. Exception Handling and Escalation

Deviations from the standard procedures defined in this SOP must be meticulously documented and approved to maintain our SOC 2 control integrity. Any ad-hoc circumvention of channel controls (e.g., sharing PHI via unauthorized channel in an emergency) constitutes an exception.

### 8.1 Exception Procedure

1.  **Identification:** An agent identifies a legitimate need to deviate from SOP-COPS-016 (e.g., a Sev 1 outage where the secure portal is also down, requiring PHI to be verbally relayed and manually documented in a temporary offline encrypted log).
2.  **Immediate Authorization:** The agent contacts their Tier 2 Lead or above. If the CAIO or CISO is available, they grant verbal authorization, which is immediately logged in a special “Emergency Exception” channel of the incident war room chat.
3.  **Documentation:** Within 1 hour of resolution, the agent who executed the exception completes an Exception Report Form in Jira (linked to the ticket), detailing the channel used, the data exposed, the reason, and the authorizing party.
4.  **Review & Mitigation:** Within 24 hours, the DPO and CISO review the exception log. If the deviation involved PHI, a mini-mitigation assessment is completed. This informs future technical hardening. Repeated exceptions for the same scenario trigger a mandatory architectural review within the sprint backlog.
5.  **Approval of Permanent Exception:** Any request to become a permanent, documented alternative process (e.g., a dedicated fax intake for a specific legacy clinical partner unable to use the portal) must be approved by the CAIO, CHRO, and DPO, and recorded as an addendum to this SOP.

### 8.2 Escalation Matrix

| Issue Type | First Point of Escalation | Secondary Escalation |
|------------|---------------------------|----------------------|
| **Suspected PHI Breach (live interaction)** | DPO (immediate phone alert) | CISO, General Counsel |
| **Tier 2 unable to resolve within 50% of SLA window** | Tier 3 designated pod lead (Clinical AI, HealthPay, etc.) | CAIO |
| **Customer refusal to comply with SSO identity verification** | VP, Customer Ops | Account’s designated CSM for corrective negotiation. Ticket remains unresolved. |
| **Technical failure of official channel (e.g., Jira outage)** | IT Operations (activated via PagerDuty) for restoration. Support ops switch to manual backup Excel tracker hosted on secured SharePoint until Jira restored. | CAIO to approve manual operations. DPO to approve backup PHI handling (read-only from CRM). |

---

## 9. Training Requirements

All personnel subject to this SOP must undergo training to ensure consistent procedural adherence to maintain SOC 2 and HIPAA compliance.

| Training Module | Target Audience | Frequency | Method | Assessed By |
|-----------------|-----------------|-----------|--------|-------------|
| **SOP-COPS-016 Procedural Training** | All Tier 1, Tier 2, Tier 3, and CSMs | Onboarding; Refresher upon major version change (>0.1 increment) | LMS (Workday), with scenario-based branching | VP, Customer Ops |
| **PHI Handling & HIPAA Privacy for Support** | All Tier 1, Tier 2, Tier 3, CSMs, and BPO agents. This program covers the required topics of permissible uses, minimum necessary access, and the process for documenting inadvertent disclosures that feed the organizational breach notification evaluation. | Annually | Instructor-led (via recorded webinar and live Q&A session) | DPO |
| **Secure Communication & DLP Awareness** | All support staff | Onboarding; Annually | Computer-Based Training (CBT) module with phishing and channel misuse simulation | CISO |
| **Customer-Facing Incident Response Drill** | Tier 2 & Tier 3 escalation pods | Biannually | Tabletop exercise simulating a Sev 1 clinical outage requiring multi-channel customer communication | CAIO, CMO |
| **SOC 2 Controls Awareness** | All internal support staff (excludes BPO) | Annually | CBT module on how individual actions affect Meridian’s SOC 2 report, focused on Availability and Confidentiality | VP, Customer Ops |

**Training Compliance:** The CHRO will track training completion rates quarterly. Any support agent whose mandatory training is past due will have their TSM account suspended until completion is verified, directly impacting operational readiness as a control failure under AAC-01.

---

## 10. Related Policies and References

This SOP operates within a broader ecosystem of Meridian governance, technical, and regulatory documents.

**Internal Meridian SOPs & Policies:**
- **SOP-SEC-011:** Vendor Management and Third-Party Risk (includes BPO oversight and BAA compliance)
- **SOP-LEG-001:** Breach Notification and Incident Response (defines legal timelines beyond the operational escalation outlined here)
- **SOP-PLAT-008:** Jira and Atlassian Cloud Management (covers backend administration of TSM)
- **SOP-HR-004:** Employee Disciplinary Procedures (for non-compliance corrective actions)
- **SOP-CLIN-022:** Clinical AI Model Output Issue Triage (specifies Tier 3 handling for clinical model errors)
- **SOP-FIN-019:** HealthPay Dispute and Error Resolution (specific to financial services support workflows)
- **SOP-CISO-003:** Data Classification and Handling Standard

**External Regulatory and Industry References:**
- **AICPA SOC 2 Trust Services Criteria (TSP Section 100):** Foundational to the controls designed in Section 6. Specifically addresses Security (CC6), Availability (CC9), and Confidentiality (CC10).
- **HIPAA Privacy Rule (45 CFR §164.500 et seq.) and Security Rule (45 CFR §164.300 et seq.):** Governs the PHI-specific constraints and training requirements.
- **Federal Reserve SR 11-7:** Model Risk Management guidance that informs the criticality tiering for HealthPay support tickets.

---

## 11. Revision History

| Version | Effective Date | Author(s) | Summary of Changes |
|---------|----------------|-----------|--------------------|
| 3.2 | 2024-07-20 | M. Chang, A. Petrov (QA Lead) | Major revision: Updated SLA timelines for Sev 2 to 1 hour off-hours; incorporated new Okta SSO verification for phone channel; added DLP quarantine procedure for email attachments (TAC-02 refinement); revised escalation matrix for Tier 2 SLA breach; updated QA sampling to 10%. |
| 3.1 | 2024-02-01 | M. Chang, J. Reyes (DPO) | Minor revision: Added the “Closure Checklist” QA requirement; strengthened language around BPO clean desk audits; updated exception handling for PHI during Sev 1 portal outages. Annual review cycle change approved. |
| 3.0 | 2023-08-15 | M. Chang, R. Liu | Major overhaul: Unified support channels under Jira Service Management (TSM) following deprecation of Zendesk. Introduced formal SOC 2 control mapping in Section 6. Added live chat and in-app channel procedures. Approved by incoming VP of Financial Services. |
| 2.0 | 2022-10-10 | M. Chang | Introduced Tier 2 specialized support for HealthPay and Clinical AI. Formalized Identity Verification policy. Integrated with new Okta SSO rollout. |
| 1.0 | 2021-03-21 | K. Sharma (former VP) | Initial document release. Established email and phone support procedures. |

---
*This document has been classified as “Internal” by Meridian Health Technologies. Distribution outside of authorized personnel is prohibited. For questions regarding this SOP, contact the CHRO’s office.*
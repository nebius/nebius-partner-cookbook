---
sop_id: "SOP-COPS-005"
title: "Customer Communication Standards"
business_unit: "Customer Operations"
version: "3.6"
effective_date: "2025-12-23"
last_reviewed: "2026-07-08"
next_review: "2027-01-10"
owner: "Michael Chang, VP of Customer Operations"
approver: "Robert Liu, VP of Financial Services"
classification: "Internal"
regulations:
  - "HIPAA"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Customer Communication Standards
**SOP-COPS-005 | Version 3.6**
**Effective: 2025-12-23 | Classification: Internal**

---

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the uniform standards, protocols, and controls governing all external communications between Meridian Health Technologies, Inc. ("Meridian") personnel and its customers, partners, and end-users. This document formalizes the mechanisms for ensuring that all customer interactions are compliant, consistent, and protect the confidentiality, integrity, and availability of sensitive data, including Protected Health Information (PHI).

### 1.2 Scope
This SOP applies to all employees, contractors, vendors, and temporary staff of Meridian ("Personnel") who engage in formal written communication with external parties. This includes, but is not limited to, interactions originating from the following Business Units:

- **Customer Operations:** Support tickets, incident response, onboarding.
- **HealthPay Financial Services:** Adverse action notices, loan status, payment processing.
- **Clinical AI Platform:** Clinical decision support alerts, system downtime notifications.
- **MedInsight Analytics:** Data sharing agreements, gap reports.
- **Sales and Account Management:** Proposals, contract amendments, general inquiries.

This SOP covers communication modalities including: Email (via Microsoft 365), Secure Messaging (Meridian Client Portal), ticketing system notes (ServiceNow), and SMS alerts (Twilio). It does *not* govern internal instant messaging (Slack) or real-time voice communications (Zoom/phone), though records of verbal decisions that impact customers must be documented in writing per Section 5.3.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **PHI** | Protected Health Information. Individually identifiable health information held or transmitted by a covered entity or its business associate. |
| **PII** | Personally Identifiable Information. Any data that could potentially identify a specific individual. |
| **ePHI** | Electronic Protected Health Information. PHI transmitted by or maintained in electronic media. |
| **MCP** | Meridian Client Portal. The secure web-based interface for customer interactions. |
| **ServiceNow** | The ITSM and Customer Service Management platform used for ticketing and incident management. |
| **DataSpike** | Meridian’s integrated Data Loss Prevention (DLP) agent, scanning outbound communications. |
| **SLA** | Service Level Agreement. Contractual commitment for response and resolution times. |
| **Adverse Action** | A notice required under the Fair Credit Reporting Act (FCRA) when a credit decision is made based on a credit report. |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Matrix (RACI)

| Activity / Decision | VP Cust. Ops (M. Chang) | CISO (R. Kim) | Chief Privacy (K. Weber) | Cust. Ops Staff | Account Executives | Eng. (D. Park) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Communication Policy Approval** | A | C | C | I | I | I |
| **Template Authorization** | R, A | C | C | R | C | I |
| **PHI Transmission Authorization** | I | C | A | R | I | I |
| **Incident Drafting (Urgent)** | A | R | C | R | I | C |
| **Communication Monitoring** | I | A | R | R | I | I |
| **Client Data Subject Requests** | I | I | I | R | I | I |

**Key: R=Responsible, A=Accountable, C=Consulted, I=Informed**

### 3.2 Detailed Role Descriptions
- **VP of Customer Operations (Michael Chang):** Executive owner of this SOP. Approves all standardized templates and communication workflows.
- **Chief Information Security Officer (Rachel Kim):** Authority over technical controls for ePHI transmission. Owns the DataSpike DLP ruleset.
- **Chief Privacy Officer/DPO (Dr. Klaus Weber):** Authority on GDPR handling, retention periods, and privacy notice verbiage.
- **Customer Operations Staff:** Responsible for executing communications within SLA, selecting correct templates, and escalating exceptions.

---

## 4. Policy Statements

Meridian Health Technologies is committed to clear, accurate, and compliant customer engagement. The following statements constitute the non-negotiable obligations of all Personnel.

1.  **No Unprotected PHI:** PHI shall never be transmitted via standard, unencrypted email (SMTP) outside the Meridian M365 tenant without specific, documented authorization and the use of the Meridian Secure Email Gateway.
2.  **Data Minimization:** Communications must contain the minimum necessary PHI required to accomplish the specific task. Mass disclosures or "reply-all" threading containing PHI is strictly prohibited.
3.  **Transparency:** Automated decisions, particularly those produced by the Clinical AI Platform or HealthPay lending models, must be clearly identified as automated when communicated to the customer.
4.  **Channel Authenticity:** Customers must be directed to use the Meridian Client Portal (MCP) for the sharing of sensitive documents. Unsolicited email attachments containing PHI from customers should be treated as misrouted and handled per the Incident Response policy.
5.  **Retention:** All communications must be preserved in accordance with the Meridian Records Retention Schedule. Communications containing clinical decision logic shall not be deleted outside of standard litigation hold procedures.

---

## 5. Detailed Procedures

### 5.1 Standard Inquiry Handling (Email and Web)
This procedure applies to general support tickets generated via email (support@meridianht.com) or the MCP.

1.  **Ticket Generation:** ServiceNow automatically generates a ticket (INC prefix for incidents, REQ for service requests). The system parses the subject line and body for PII/PHI patterns and triggers a "CONFIDENTIAL" flag if detected.
2.  **Triage (Time Target: < 15 mins):** Support Agent reviews the ticket. If the email contains unsolicited PHI without encryption, the Agent must immediately move the email to a quarantine mailbox and log a security incident in ServiceNow per SOP-SEC-002. They must not reply directly to the email chain.
3.  **Response and Resolution:** Agent selects the correct template from the Template Manager (see Section 5.2). The template must match the query category.
4.  **Closure:** Upon resolution, the agent captures the customer's acknowledgment of satisfaction. The ticket is set to "Resolved," triggering a feedback survey via Medallia.
5.  **Retention:** Resolved tickets are archived in the ServiceNow database. Transcripts containing customer PII are stored for 7 years per standard retention rules.

### 5.2 Template Management
All templated communications must pass Legal and Compliance review before publication.

**Template Catalog Structure:**
- **T-CA-01:** Clinical Alert – Normal Risk Score.
- **T-CA-02:** Clinical Alert – Elevated Risk Score (Physician Alert).
- **T-FS-01:** HealthPay Pre-Approval Letter.
- **T-FS-02:** HealthPay Adverse Action Notice.
- **T-GEN-01:** General Account Notification (Billing).
- **T-PRY-01:** Privacy Notice Update Notification.

**Template Filling Rules:**
- **Merge Fields:** Templates use double-bracket merge fields (`{{Patient_Name}}`, `{{Loan_ID}}`).
- **Validation:** The "Preview and Send" interface in ServiceNow forces a validation check. If a merge field fails to populate (e.g., missing data from Snowflake), the system blocks the send and alerts the Data Engineering team.
- **Logos and Signatures:** Disable "Reply All" and auto-populate the sender’s Docusign-stamped signature block to prevent unauthorized disclaimer modification.

### 5.3 Incident and Outage Communication (Clinical AI Platform)
In the event of a Severity 1 (Sev 1) outage affecting the Clinical AI Platform (e.g., real-time inference API latency > 5000ms):

1.  **Detection:** Datadog monitor alerts the Incident Commander (Engineer on Call).
2.  **Drafting (First 30 mins):** Customer Operations Manager drafts a "Monitoring" update. **It is critical that this communication does not speculate on root cause.** The draft must be reviewed by the Clinical VP (Dr. Aisha Okafor) if it contains any language suggesting a defect in diagnostic sensitivity.
3.  **Distribution:** The communication is pushed via the MCP alert banner and email. For hospital administrators, a high-priority SMS (using the Twilio integration) is dispatched.
4.  **Updates:** Updates must be provided every 60 minutes until resolution. A post-mortem summary (de-identified) is sent within 5 business days.

### 5.4 HealthPay Financial Services Communications
Due to SR 11-7 implications, all automated credit decision communications must strictly mirror the model output without manual softening of language that could be construed as overriding the model.

1.  **Approval Pathway:** For standard medical loans ($500 - $5000), the automated T-FS-01 template is sent via email with a secure link to view the Truth in Lending Act (TILA) disclosure.
2.  **Adverse Action:** If the credit model returns "Denied" or "Manual Review Required," the T-FS-02 template must be sent *within 24 hours*. This email must contain the specific reason codes generated by the model (e.g., "Debt-to-income ratio above threshold").
3.  **Manual Override:** If a manual review overturns a model decision, the approving underwriter (Level 2 agent) must attach a memo to the ticket specifying the overriding rationale. This memo is not shared with the customer but is retained for model validation (MRM committee) audits per SOP-FS-110.

### 5.5 Data Subject Communications
If a customer requests communication via a specific channel (e.g., "please do not call me, use email only"), the agent must update the "Contact Preferences" field in the CRM (Salesforce). This preference flag is binding and overrides generalized outreach campaigns.

Regarding privacy, customers are provided with a notice at the point of data collection. This notice outlines the types of data collected and the purposes for processing.

### 5.6 Secure Transmission of PHI
When an agent needs to send a file containing PHI:
1.  Agent clicks "Secure Send" within the ServiceNow ticket.
2.  The file is processed via the Meridian Secure Email Gateway (MSEG) utilizing TLS 1.3.
3.  The recipient receives a "Fetch" link to the MCP, not the file itself.
4.  Access to the fetch link requires multi-factor authentication (MFA). Guest access tokens expire after 72 hours.

### 5.7 International Communications
For communications directed to data subjects located in the European Economic Area (EEA) or the United Kingdom, the following applies:
- **Language:** Communications will default to English unless the recipient profile specifies German (DE) or French (FR), in which case a translation service (DeepL API integration) is employed for the initial draft, followed by a review by the Berlin office.
- **Data Transfers:** Customer data hosted in us-east-1 is accessible by the EU support team via a VPC peering connection. This cross-border access is logged as a "User Access Review" event.

### 5.8 Prohibited Practices
The following actions are explicitly prohibited and constitute a Policy Violation:
- Copying a customer’s personal email (e.g., Gmail) into a thread containing another patient’s billing details.
- Using emojis or casual vernacular in official clinical communications.
- Sharing screenshots of the Clinical AI Platform or ServiceNow interface with customers unless the screenshot feature has been approved by IT Security and specific data points redacted by the native tool.
- Sending "test" communications to real customer email addresses.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls
| System | Control | Description |
| :--- | :--- | :--- |
| **Microsoft 365** | DLP Policy "Global-FIN-HEALTH" | Scans outbound emails for regular expressions matching credit card tracks, SSN, and medical record numbers. Triggers an automatic block and manager notification. |
| **DataSpike (Agent)** | Endpoint Watermarking | Automatically applies a "Confidential - Meridian Internal" header and footer to emails exceeding a PHI density score of 0.7. |
| **ServiceNow** | Content Filter Validation | Prevents sending a ticket reply if the body contains a credit card PAN in an unredacted format. Force-clears CC and BCC fields if a High-Risk template is selected. |
| **AWS KMS** | Encryption Key Rotation | Keys used for encrypting MCP static assets (attachments) rotate quarterly. |

### 6.2 Administrative Controls
- **Quarterly Access Review:** Managers must certify that their team members still require the "Secure Send" elevated permission to transmit PHI externally.
- **Peer Review Cohort:** A random 5% of all closed ServiceNow tickets are pulled monthly for a communication audit by the QA team.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)
The operational health of communication standards is tracked via the following KPIs displayed on the Customer Operations Datadog Dashboard:

| Metric | Target | Alert Threshold |
| :--- | :--- | :--- |
| **Mean Time to Acknowledge (MTTA)** | < 1 Hour (Standard) | > 4 Hours (High Priority) |
| **DLP False Positive Rate** | < 2% of blocked emails | > 5% |
| **Template Adherence Rate** | 98% | < 90% |
| **MCP Guest Token Abuse (Failed MFA)** | 0 | > 5 attempts / hour |

### 7.2 Reporting Cadence
- **Weekly:** VP of Customer Operations receives automated "Outbound DLP Block" report.
- **Monthly:** Chief Privacy Officer receives "International Access Log" report detailing support access from non-US geographies.
- **Quarterly:** Executive summary presented to the Board AI Governance Committee focusing on clinical communication failures.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Requests
Situations requiring deviation from this SOP (e.g., bulk sharing of PHI with a third-party researcher) must be managed via the Governance, Risk, and Compliance (GRC) platform (AuditBoard).

1.  **Initiation:** Personnel files a "Policy Exception" request in AuditBoard, specifying the SOP-COPS-005 clause violated, the technical justification, and the compensating control.
2.  **Risk Assessment:** CISO (Kim) and Privacy (Weber) jointly score the risk.
3.  **Approval Matrix:**
    - **Low Risk:** Approved by immediate Director.
    - **Medium Risk:** Approved by VP Customer Operations.
    - **High/Unacceptable Risk:** Escalated to General Counsel (Maria Gonzalez) for executive review.

### 8.2 Escalation Path
- **Clinical Error in Communication (e.g., wrong dosage alert sent):** Immediately escalate to Clinical VP (Dr. Patel) and CISO via the PagerDuty "Clinical Safety" service. A retraction notice must be drafted within 15 minutes.
- **Potential Mass Data Breach:** Initiate SOP-SEC-002 (Data Breach Response). Do not issue customer notification until authorized by the Breach Response Team Lead.

---

## 9. Training Requirements

All personnel subject to this SOP must complete the following training modules:

| Module Code | Title | Frequency | Audience |
| :--- | :--- | :--- | :--- |
| **COM-101** | Customer Communication Basics & Tone | Annual | All Customer-Facing Staff |
| **PHI-201** | HIPAA Privacy & Secure Messaging | Annual | All Staff |
| **EU-301** | GDPR in Customer Operations (Berlin-based staff) | Bi-annual | EEA Support Team |
| **SEC-401** | Phishing and Pretexting Awareness | Quarterly | All Staff |

**Tracking:** Completion is tracked via Litmos LMS. Non-completion within 30 days of the assigned date results in temporary suspension of ServiceNow access credentials until the training is signed off by HR.

---

## 10. Related Policies and References

- **SOP-SEC-002:** Incident Response and Data Breach Notification
- **SOP-SEC-008:** Access Control and Authentication Standards
- **SOP-FS-110:** HealthPay Model Risk Management (SR 11-7 Compliance)
- **SOP-DE-015:** Data Classification and Handling Standards
- **SOP-PRV-001:** Data Subject Rights Processing
- **NIST AI RMF 1.0:** AI Risk Management Framework (Advisory Reference)
- **Meridian Employee Handbook:** Code of Conduct

---

## 11. Revision History

| Version | Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2020-03-15 | J. Walsh | Initial creation covering basic email standards. |
| 2.1 | 2022-11-01 | M. Chang | Major revision to incorporate HealthPay FCRA requirements and ServiceNow integration. |
| 3.2 | 2024-05-07 | K. Weber | Added international data transfer section and privacy notice templates to align with GDPR updates. |
| 3.5 | 2025-08-22 | S. Torres | Enhanced Clinical AI outage communication loop and added Human Oversight flags for EU AI Act Article 14 compliance. |
| 3.6 | 2025-12-23 | M. Chang | Updated retention periods, refined adverse action communication chain, and finalized Secure Send technical controls. Added cross-border logging metrics. |
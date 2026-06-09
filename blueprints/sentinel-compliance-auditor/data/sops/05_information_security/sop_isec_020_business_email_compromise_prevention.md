---
sop_id: "SOP-ISEC-020"
title: "Business Email Compromise Prevention"
business_unit: "Information Security"
version: "3.2"
effective_date: "2024-01-09"
last_reviewed: "2025-11-18"
next_review: "2026-05-15"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Business Email Compromise Prevention

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for preventing, detecting, responding to, and recovering from Business Email Compromise (BEC) attacks at Meridian Health Technologies, Inc. BEC represents one of the most financially damaging cyber threats facing the organization, given the company's role in processing approximately $4.2B annually through HealthPay Financial Services, its access to protected health information (PHI) for approximately 12M patients through MedInsight Analytics, and its deployment of high-risk AI systems classified under the EU AI Act.

The purpose of this SOP is to:

- Define technical controls, administrative safeguards, and behavioral requirements that reduce Meridian's attack surface for BEC and email-borne fraud
- Establish a multi-layered verification framework, with particular emphasis on wire transfers, payment instructions, and changes to supplier or payroll data
- Ensure compliance with SOC 2 Trust Services Criteria, specifically the Security and Availability criteria within the 2024 AICPA SOC 2 guide, as well as related obligations under HIPAA, GDPR, SR 11-7, and NIST AI RMF
- Create clear, auditable processes that demonstrate management's commitment to security and provide reasonable assurance over the integrity of financial and operational communications

### 1.2 Scope

This SOP applies to:

- **All Personnel:** Full-time employees, part-time employees, contractors, consultants, interns, and temporary staff ("Personnel") who use Meridian-managed email systems (meridianhealth.com, medinsight.com, healthpayfin.com, and any subsidiary domains) or who handle financial transactions, PHI, or other sensitive data on behalf of Meridian
- **All Systems:** Meridian-managed email infrastructure, including Microsoft 365 tenants, Google Workspace (used by the Berlin and Singapore offices), AWS WorkMail for system-generated alerts, and any mobile device management (MDM)-enrolled device accessing corporate email
- **All Third Parties:** Vendors, suppliers, business associates, and partners who send or receive email communications representing Meridian business, or who receive payment instructions from Meridian systems or personnel
- **All Transaction Types:** Wire transfers, ACH payments, supplier invoice payments, payroll changes, direct deposit modifications, and any other financial instructions transmitted via email or email-linked platforms

This SOP does **not** cover:
- Phishing attacks that do not involve impersonation or financial fraud (refer to SOP-ISEC-015, "Phishing Awareness and Response")
- General email retention and e-discovery (refer to SOP-LEG-008, "Email Retention and Legal Hold")
- Secure file transfer protocols for PHI (refer to SOP-CPO-012, "PHI Transmission Standards")

### 1.3 Applicability by Business Unit

| Business Unit | Key Risk Factors | Applicability |
|---|---|---|
| Clinical AI Platform | Vendor impersonation; EU AI Act transparency chain compromise | Full |
| HealthPay Financial Services | Wire transfer fraud; SR 11-7 model notification integrity | Full; enhanced wire verification |
| MedInsight Analytics | PHI exfiltration via impersonation; business associate compromise | Full |
| Meridian SaaS Platform | Infrastructure configuration change requests; SOC 2 control integrity | Full |
| Corporate Functions (Finance, HR, Legal) | Payroll diversion; supplier payment fraud; executive impersonation | Full; enhanced verification for all payment changes |

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|---|---|
| **BEC (Business Email Compromise)** | A sophisticated scam targeting organizations that conduct wire transfers or handle sensitive data, involving either account compromise (gaining access to a legitimate email account) or display-name/domain spoofing to impersonate executives, vendors, or partners. |
| **Display-Name Spoofing** | An attack where the attacker uses a email display name matching a Meridian executive or trusted contact, but sends from an external, often look-alike, domain. |
| **Domain Spoofing** | An attack in which the sender forges the envelope-from or header-from address to appear as if the email originates from a Meridian-owned domain. |
| **DMARC (Domain-based Message Authentication, Reporting, and Conformance)** | An email authentication protocol (RFC 7489) that builds on SPF and DKIM, allowing domain owners to publish a policy specifying how receiving mail servers should handle messages that fail authentication checks. |
| **DKIM (DomainKeys Identified Mail)** | An email authentication method (RFC 6376) that allows an organization to take responsibility for transmitting a message by affixing a digital signature verified using a public key published in the domain's DNS. |
| **SPF (Sender Policy Framework)** | An email authentication protocol (RFC 7208) that allows domain owners to specify which mail servers are authorized to send email on behalf of their domain. |
| **MFA (Multi-Factor Authentication)** | An authentication method requiring two or more verification factors: something you know (password), something you have (Okta Verify push or YubiKey), and/or something you are (Windows Hello biometric). Meridian requires phishing-resistant MFA for all email access. |
| **Wire Transfer Verification (WTV)** | The out-of-band, multi-factor process used at Meridian to confirm the authenticity and accuracy of any payment instruction received via email before processing. |
| **SOC 2** | AICPA Service Organization Control 2 framework; Meridian maintains SOC 2 Type II certification for the SaaS Platform, evaluated against Security and Availability Trust Services Criteria within the 2024 AICPA guide. |
| **TTPs (Tactics, Techniques, and Procedures)** | The behavioral patterns, methods, and tools used by threat actors to execute BEC attacks. |
| **AI-based Email Security** | Meridian's deployed email security layer (Abnormal Security) that uses machine learning and behavioral AI to detect anomalous email patterns indicative of BEC, including analysis of communication graphs, sentiment analysis, and anomaly detection on payment-related language. |
| **SEF (Secure External Finance)** | Meridian's secure vendor portal where approved suppliers manage banking details; changes made here bypass email entirely and follow a separate verification flow. |
| **SIM-swap** | A fraud technique where an attacker convinces a mobile carrier to transfer a victim's phone number to a SIM card in the attacker's possession; relevant because it can defeat SMS-based MFA. |
| **VEC (Vendor Email Compromise)** | A subset of BEC where an attacker compromises a legitimate vendor's email account and uses it to send fraudulent invoices or payment instruction changes to the target organization (Meridian). |

---

## 3. Roles and Responsibilities

### 3.1 RACI Matrix

| Activity | CISO (Rachel Kim) | VP IT Ops (Samantha Torres) | CCO (Thomas Anderson) | CFO (James Thornton) | VP Financial Services (Robert Liu) | CPO/DPO (Dr. Klaus Weber) | All Personnel | Security Operations Center |
|---|---|---|---|---|---|---|---|---|
| Email Security Architecture & DMARC Enforcement | **A** | R | I | I | I | C | I | R |
| Wire Transfer Verification Execution | I | I | I | **A** | **R** | I | I | I |
| BEC Incident Response | **R / A** | R | C | C | C | C | I | **R** |
| Supplier Banking Change Verification | I | I | I | **A** | R | I | I | I |
| Email Security Awareness Training | I | R | R | I | I | I | **R** (completion) | I |
| SOC 2 Control Evidence Collection | R | R | **R / A** | I | I | I | I | R |
| Reporting Suspicious Emails | I | I | I | I | I | I | **R** | I |
| GDPR Breach Notification (if personal data breached) | C | C | C | I | I | **R / A** | I | C |

**Key:** R = Responsible (doer); A = Accountable (approver); C = Consulted (subject-matter input); I = Informed (kept up to date)

### 3.2 Named Role Responsibilities

**Rachel Kim, Chief Information Security Officer (CISO)**
- Owns this SOP and all BEC-related technical controls
- Approves all architectural changes to email security infrastructure
- Authorizes exceptions to DMARC enforcement posture or wire transfer verification steps
- Reports BEC metrics to the Board-level AI Governance Committee and Audit Committee quarterly
- Serves as incident commander for any confirmed BEC incident exceeding $50,000 in impact

**Samantha Torres, VP of IT Operations**
- Manages the operational execution of email authentication (DMARC/DKIM/SPF) across all Meridian domains
- Maintains the AI-based email security platform and ensures continuous tuning of detection models
- Oversees the Security Operations Center's 24/7 monitoring for BEC indicators
- Produces monthly email security posture reports

**James Thornton, Chief Financial Officer (CFO)**
- Co-owns the Wire Transfer Verification procedure with the VP of Financial Services
- Approves any payment exceeding $100,000 following successful WTV execution
- Reviews and approves all changes to the Wire Transfer Verification call tree
- Leads financial recovery efforts in the event of a successful BEC fraud

**Robert Liu, VP of Financial Services**
- Manages the day-to-day execution of Wire Transfer Verification for HealthPay operations
- Maintains the SEF vendor portal and ensures all supplier banking changes route through this channel
- Audits payment change requests monthly for anomalies
- Coordinates with banking partners (JPMorgan Chase, Silicon Valley Bank) on BEC-related fraud alerts

**Thomas Anderson, Chief Compliance Officer (CCO)**
- Maps BEC controls to SOC 2 Trust Services Criteria CC6.1, CC6.6, CC7.1, and PI1.3
- Collects, reviews, and retains evidence for SOC 2 Type II audits
- Ensures BEC incident documentation meets audit trail requirements
- Manages the exception process for compensating controls

**Dr. Klaus Weber, Chief Privacy Officer / Data Protection Officer**
- Assesses BEC incidents for personal data breach implications under GDPR
- Leads 72-hour notification to supervisory authorities when BEC results in EU personal data compromise
- Advises on email data handling practices for EU-based employees and patient data subjects

**All Personnel**
- Complete annual BEC-specific awareness training
- Report suspicious emails by clicking the "Report Phishing" button in Outlook/Gmail or forwarding to phish@meridianhealth.com
- Never bypass verification processes for payment or sensitive data requests received via email
- Verify any unusual request via out-of-band communication before acting

---

## 4. Policy Statements

### 4.1 Email Authentication Policy

Meridian Health Technologies mandates the following email authentication posture:

- **All Meridian-owned domains, including parked domains and domains used solely for email-sending purposes, MUST implement DMARC with a minimum policy of `p=reject` (100%).**
- DMARC aggregate reports (`rua`) MUST be delivered to dmarcreports@meridianhealth.com and ingested into the Observability platform (Datadog) for continuous monitoring.
- DKIM signing MUST be enabled for all authorized email senders, with key rotation every 180 days.
- SPF records MUST be hardened with the `-all` mechanism; the use of `?all` or `~all` qualifiers is prohibited for any production domain.
- All domains MUST achieve and maintain a DMARC compliance rate of ≥99.5% as measured by aggregate reports.

### 4.2 Wire Transfer Verification Policy

- **No wire transfer, ACH batch, or supplier payment exceeding $10,000 may be executed based solely on email instructions.**
- All payment instruction changes (banking details, payment amounts, destination accounts) received via email MUST undergo out-of-band voice verification using a pre-established, independently verified callback number.
- Verification MUST involve confirmation of a shared secret or transaction-specific code with an authorized individual listed in Meridian's Verified Contact Registry (VCR).
- The Verified Contact Registry MUST be maintained independent of email and updated only through in-person verification, video call with biometric confirmation, or secure physical token exchange.
- Any payment request characterized as "urgent," "confidential," or pressuring bypass of normal processes triggers a mandatory escalation to the CFO or VP Financial Services.

### 4.3 Account Security Policy

- All email accounts used for Meridian business—including contractor and third-party accounts—MUST be protected by phishing-resistant MFA (Okta Verify with FIDO2 WebAuthn or YubiKey hardware tokens).
- SMS-based MFA for email access is prohibited.
- Generic or shared email accounts used for financial processing (e.g., payments@meridianhealth.com) MUST have their associated credentials stored exclusively in HashiCorp Vault with just-in-time access provisioning; credentials must not be known by any individual.
- Any email account showing anomalous login patterns (impossible travel, unusual client or location, mass forwarding rule creation) MUST be automatically quarantined via the CrowdStrike Identity Protection integration with Microsoft 365.

### 4.4 Reporting Culture Policy

- Meridian maintains a "no-blame" culture for reporting suspected BEC attempts. Personnel who report an email they mistakenly engaged with before recognizing it as fraudulent will not face disciplinary action, provided they report promptly.
- **Willful failure to report a known or suspected BEC attempt, or deliberate circumvention of verification procedures, constitutes a violation of the Meridian Code of Conduct and may result in disciplinary action up to and including termination.**

---

## 5. Detailed Procedures

### 5.1 Email Authentication Configuration and Management

#### 5.1.1 DMARC Implementation and Escalation

This procedure is owned by VP of IT Operations (Samantha Torres) with architectural approval from the CISO.

**Step 1: Baseline Discovery (Continuous)**
1. The IT Operations Email Team maintains a current inventory of all Meridian-managed domains in the "Domain Asset Registry" (ServiceNow CMDB, table `sn_domain_asset`).
2. Each domain is classified as: **Sending** (actively sends email), **Defensive** (registered to prevent squatting, does not send), or **Transitional** (acquired through M&A, undergoing consolidation).
3. All domains, regardless of classification, must have SPF, DKIM, and DMARC records in public DNS.

**Step 2: DMARC Policy Enforcement Escalation**
1. **Phase 1 (Monitoring):** Newly provisioned sending domains begin at `p=none` with `rua` and `ruf` reporting enabled. Duration: maximum 30 days.
2. **Phase 2 (Quarantine):** After confirming no legitimate email streams are failing DMARC checks, policy is escalated to `p=quarantine`. Duration: maximum 15 days.
3. **Phase 3 (Reject):** After confirming zero false-positive rejections causing business impact, policy is elevated to `p=reject; pct=100`. This is the mandatory steady state for all Meridian sending domains.
4. **Approval Gate:** Elevation from Phase 1 to Phase 2 requires VP IT Ops approval. Elevation from Phase 2 to Phase 3 requires CISO approval.

**Step 3: Ongoing Monitoring**
1. DMARC aggregate XML reports are collected from `dmarcreports@meridianhealth.com` daily and parsed into Datadog Logs.
2. The Datadog dashboard "DMARC Compliance Overview" (Dashboard ID: `dmarc-ov-01`) displays:
   - Per-domain DMARC pass percentage (target: ≥99.5%)
   - Top 10 sending sources failing DMARC
   - Policy enforcement status per domain
   - Forwarding-induced DMARC failures (noted for compatibility monitoring)
3. Alerts trigger via PagerDuty if pass percentage drops below 99.0% for any domain in a rolling 24-hour window.

#### 5.1.2 SPF Record Management

1. All SPF records must terminate with `-all` (hard fail).
2. The `include:` mechanism must be used instead of manually listing IP addresses wherever an authorized sending service supports it.
3. The total DNS lookup count for SPF must remain ≤10 to comply with RFC 7208. If a domain's email footprint requires more than 10 lookups, the Email Team must implement dynamic SPF flattening via the Valimail platform.
4. Any change to SPF records must undergo a peer review by a second member of the Email Team and be logged in the "DNS Change Log" (ServiceNow change request required, category: "Email Security").

#### 5.1.3 DKIM Key Lifecycle

1. DKIM keys (1024-bit minimum; 2048-bit required for financially sensitive domains including healthpayfin.com) are generated and stored in AWS KMS.
2. Key rotation is executed automatically via a scheduled AWS Lambda function (`dkim-rotator-prod`) on a 180-day cycle.
3. Post-rotation, old public keys remain in DNS for 7 days (as `selector._domainkey.old`) to allow in-transit email validation before removal.

### 5.2 Wire Transfer Verification Procedure

This is the most financially impactful procedure in this SOP. It applies to the Finance Department, HealthPay Financial Services operations team, and any personnel authorized to initiate or approve payments.

#### 5.2.1 Pre-Conditions for Wire Transfer Verification

Before the Wire Transfer Verification (WTV) process can be utilized for a given payee/vendor/payroll recipient, the following pre-conditions must be established and recorded in the Verified Contact Registry (VCR), which is a secure database maintained in a dedicated Snowflake schema (`FIN_VCR`) with access restricted to authorized Finance and Financial Services personnel via Okta SSO and row-level security:

1. **Identity Verification:** The authorized contact's identity has been verified through one of:
   - In-person meeting with government-issued photo ID confirmation
   - Live video call where the individual displays government-issued photo ID and matches Meridian's biometric identity proofing (conducted via Okta Verify identity proofing flow)
   - Secure physical token exchange (MFA token registered in person)
2. **Verified Callback Number:** A telephone number has been designated as the Verified Callback Number. This number must be independently confirmed—it cannot be extracted from the email signature or email body of the contact.
3. **Shared Secret Establishment:** A unique, randomly generated shared secret (alphanumeric, 12 characters) has been established and communicated to the contact during the identity verification session. This secret is stored as a salted hash in the VCR and must be quoted in full during every WTV call.

**Re-verification Trigger:** If more than 12 months have elapsed since the last successful WTV call for a given contact, the contact record is marked "EXPIRED" in the VCR and must undergo the full identity verification process again before any payment instructions are accepted.

#### 5.2.2 Step-by-Step Wire Transfer Verification

**Trigger:** A Meridian employee in Finance or Financial Services receives an email requesting one of the following:
- A new wire transfer or ACH payment
- A change to existing payment instructions (bank name, routing number, account number, account holder name)
- A change to payroll direct deposit instructions
- A "rush" or "urgent" payment outside normal payment cycles

**Procedure Steps:**

| Step | Action | Responsible Role | Record-Keeping |
|---|---|---|---|
| **WTV-1** | **DO NOT** reply to the email, forward it to colleagues, or click any links/attachments until verification is complete. | Payment Processor | N/A |
| **WTV-2** | Open the Verified Contact Registry in Snowflake (URL: snowflake.meridianhealth.com > `FIN_VCR` schema > `APPROVED_CONTACTS` view). Search for the entity and contact name from which the request appears to originate. | Payment Processor | Access log auto-recorded in Snowflake `ACCESS_HISTORY`. |
| **WTV-3** | If the contact is listed with status "ACTIVE," note the Verified Callback Number and Shared Secret indicator (you will see a 4-character prefix hint; the full secret is verified during the call). If the contact is NOT listed or is "EXPIRED," escalate to your manager; **do not proceed.** | Payment Processor | Screenshot of search result saved to WTV case file. |
| **WTV-4** | Initiate an outbound call to the Verified Callback Number. If you reach voicemail, do NOT leave a detailed message. State only: "This is [Your Name] from Meridian Health Technologies calling regarding a verification matter. I will call back in 15 minutes." Document the attempt. | Payment Processor | Call record noted in WTV log. |
| **WTV-5** | Upon reaching the authorized contact, state: "I am calling to verify a payment instruction we received via email on [date] regarding [purpose/payment reference]. For security purposes, I need you to confirm your shared verification phrase—please give me the full phrase." | Payment Processor | N/A |
| **WTV-6** | Compare the phrase provided against the hashed secret in the VCR (the VCR interface has a "Verify Phrase" button that compares the input against the stored salted hash). If match: proceed to WTV-7. If NO match: **terminate the call immediately** and escalate to Information Security and Finance management. | Payment Processor | Result logged in VCR with timestamp. |
| **WTV-7** | Verbally confirm the full payment details: amount, currency, destination bank name, routing/transit number, account number (last 4 digits only may be spoken; have the contact confirm the first 4 and last 4 digits of the account number), and payment reference. | Payment Processor | Audio recording (where legally permitted; all Meridian call center and recorded lines are identified with a pre-call announcement). |
| **WTV-8** | If all details match the email exactly, document the successful verification. The payment may then proceed to standard approval workflow. Note: payment approval is a SEPARATE step from verification. The WTV record must be attached to the payment request in the ERP system (NetSuite). | Payment Processor / Approver | WTV completion record with unique WTV ID, attached to NetSuite payment request. |
| **WTV-9** | If ANY detail does not match, terminate the call, quarantine the email, and escalate per Section 8 (Exception Handling and Escalation). Do NOT negotiate or "correct" the details on the call. | Payment Processor | Incident ticket opened (ServiceNow, category "BEC Suspected"). |

**Enhanced Verification for Payments ≥ $500,000:**
Payments meeting or exceeding $500,000 require a **second independent WTV call** to a different Verified Contact at the same entity, or a two-person verification where a second Meridian Finance employee is physically present or on a bridged line to witness the call.

### 5.3 BEC Email Triage and Response

#### 5.3.1 End-User Reporting Procedure

When any Personnel member identifies a suspicious email—characteristics include unexpected payment requests, executive impersonation, urgency/pressure language, requests for secrecy, or mismatched reply-to addresses—they must:

1. **Immediately** click the "Report Phishing" button in Outlook (Microsoft 365) or "Report Spam/Phishing" in Google Workspace (Berlin and Singapore offices).
   - **Alternative:** Forward the email as an attachment to phish@meridianhealth.com.
2. **Do not** forward the email inline to colleagues, as this can propagate any malicious payload.
3. **If the email appears to be a BEC attempt specifically involving financial or sensitive data requests, also call the Security Operations Center (SOC) hotline at x4-7272 (or +1-617-555-7272) within 15 minutes.**
4. **Do not delete the email** until instructed by the SOC; preserve it for forensic analysis.

#### 5.3.2 SOC Initial Triage

Upon receipt of a reported suspicious email (automatic via "Report Phishing" or manual via phish@meridianhealth.com):

1. **Priority Classification:**
   - **Priority 1 (P1):** Email contains a wire transfer request, payment instruction change, payroll change, or executive impersonation with a request for sensitive data. SLA: 15-minute initial triage.
   - **Priority 2 (P2):** Email involves impersonation without financial request (e.g., generic "Are you available?" from spoofed executive). SLA: 30-minute initial triage.
   - **Priority 3 (P3):** Mass phishing or generic credential harvesting. SLA: 60-minute initial triage.

2. **Automated Analysis:** The Abnormal Security platform automatically analyzes the email for:
   - DMARC/SPF/DKIM pass/fail status
   - Sender domain age (domains registered <30 days flagged)
   - Display name match against Meridian executive roster
   - Natural language processing for payment-related terms and urgency markers
   - Communication graph anomaly (does the sender typically communicate with this recipient?)

3. **Manual SOC Triage for P1/P2:**
   - Review full email headers in MxToolbox or equivalent
   - Examine any URLs in a sandbox environment (CrowdStrike Falcon Sandbox)
   - Check for mailbox rule creation (if internal account suspected compromised, query Microsoft 365 for `New-InboxRule` or `Set-InboxRule` created in last 24 hours)
   - If message originated from internal Meridian account, initiate account compromise investigation per SOP-ISEC-022 ("Account Compromise Response")

4. **Containment Actions (if malicious confirmed):**
   - Purge email from all recipient inboxes via Microsoft 365 Compliance Center "Search and Purge"
   - Block sender domain and similar look-alike domains in the email security gateway
   - If internal account compromised: force password reset, revoke all sessions, revoke MFA tokens, initiate forensic mailbox audit
   - Add indicators of compromise (domains, email addresses, subject patterns) to the global block list in Abnormal Security
   - Notify recipients if they interacted with the email (clicked link, replied, provided information)

#### 5.3.3 User Follow-Up for Compromised Interaction

If a user reports that they **engaged** with a suspected BEC email—replied to the email, clicked a link and entered credentials, provided information, or (worst case) initiated a payment—the SOC will:

1. **Immediately** have the user disconnect their device from the network (disable Wi-Fi, unplug Ethernet) but do NOT power off the machine.
2. Deploy a CrowdStrike Falcon forensic collector to the endpoint and initiate a full scan.
3. For credential exposure: force password reset across all federated systems, revoke all Okta sessions, re-issue MFA tokens.
4. For financial action taken: immediately contact the CFO and VP Financial Services to initiate the financial recovery procedure (Section 5.4).
5. For PHI exposure suspected: immediately notify the CPO/DPO (Dr. Klaus Weber) for GDPR breach assessment.

### 5.4 Financial Recovery and Banking Intervention

In the event that a payment has been executed based on fraudulent BEC instructions, time is measured in minutes, not hours. This procedure is rehearsed quarterly in tabletop exercises run jointly by Finance and Information Security.

**Step 1: Immediate Notification (Target: within 15 minutes of discovery)**
1. The person discovering the potential fraud (or the SOC on their behalf) initiates a conference bridge using the pre-configured "BEC Financial Emergency" bridge (Bridge ID: 888-555-0199, passcode stored in HashiCorp Vault under `prod/bec-emergency-bridge`).
2. Required participants: CFO (James Thornton), VP Financial Services (Robert Liu), CISO (Rachel Kim), General Counsel (Maria Gonzalez), and the relevant relationship manager from Finance.
3. If any principal is unreachable within 5 minutes, their delegate (pre-defined in the BEC Emergency Contact Tree, a sealed document maintained by the CFO's office) is contacted.

**Step 2: Bank Notification (Target: within 30 minutes of discovery)**
1. The CFO or VP Financial Services immediately contacts Meridian's banking partners' fraud hotlines:
   - **JPMorgan Chase Commercial Banking Fraud:** +1-855-555-2425 (Meridian client code: MHT-4429)
   - **Silicon Valley Bank Fraud Operations:** +1-800-555-7723
2. Provide the following information:
   - Meridian account number and entity name
   - Date, time, and amount of the fraudulent transaction
   - Destination bank name, routing number, and account number
   - Federal Reference Number or SWIFT UETR (Unique End-to-End Transaction Reference) if available
3. Request the bank initiate a **SWIFT Recall** (for international wires) or **ACH Reversal** (for domestic ACH) under the NACHA rules "erroneous entry" provisions.

**Step 3: Law Enforcement and Regulatory Notification**
1. General Counsel (Maria Gonzalez) determines law enforcement notification strategy; typical contacts include FBI Boston Field Office (Cyber Task Force) and, for EU-based fraud, the appropriate national cybercrime unit.
2. CPO/DPO (Dr. Klaus Weber) assesses whether the incident constitutes a personal data breach under GDPR; if yes, notification to the relevant supervisory authority within 72 hours.
3. Compliance (Thomas Anderson) determines if the incident meets any breach notification requirements under HIPAA or state laws, or if it impacts SOC 2 control assertions.

**Step 4: Insurance Notification**
1. The CFO or General Counsel notifies Meridian's cyber insurance carrier (policy details maintained confidentially by the CFO's office).
2. Preserve all forensic evidence, logs, and documentation for the insurance claim process.

### 5.5 Vendor and Supplier Email Security

#### 5.5.1 Mandatory Supplier Communication
1. All suppliers and vendors who receive payment from Meridian must be informed in writing during the onboarding process and annually that:
   - Meridian will NEVER change payment instructions via email without out-of-band telephone verification
   - Meridian will NEVER send "urgent" payment requests that bypass the standard Purchase Order and invoicing process
   - Any email requesting a change to payment instructions should be treated as suspicious
   - They must verify any such request by calling their established Meridian contact using a number already on file, NOT a number provided in the email
2. This communication is managed as part of the Supplier Onboarding Package in the SEF (Secure External Finance) portal. The CFO's office ensures 100% of active suppliers have acknowledged this policy.

#### 5.5.2 Vendor Email Compromise Response
1. If a vendor reports to Meridian that their own email system has been compromised, and Meridian has received invoices or payment requests from that vendor in the prior 90 days, Meridian Finance must:
   - Immediately halt all pending payments to that vendor
   - Review all payments made in the prior 90 days for divergence from established banking details
   - Require the vendor to complete the full identity re-verification process before any new payments are processed

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control ID | Control Description | Technology | Coverage | SOC 2 Criteria Reference |
|---|---|---|---|---|
| TEC-01 | DMARC enforcement at `p=reject` for all sending domains | DNS / Valimail | 100% of Meridian domains | CC6.1, CC6.6 |
| TEC-02 | AI-based anomalous email detection (behavioral graph analysis + NLP) | Abnormal Security | All inbound email to Meridian | CC7.1, PI1.3 |
| TEC-03 | Anti-spoofing controls: explicit deny for external emails using Meridian executive display names | Abnormal Security + Microsoft 365 Transport Rule | All inbound email | CC6.6 |
| TEC-04 | URL rewriting and click-time protection for all external links in email | Microsoft Defender for Office 365 Safe Links | All inbound email | CC7.1 |
| TEC-05 | Attachment sandbox detonation for all executable and macro-enabled file types | CrowdStrike Falcon Sandbox + Microsoft Defender Safe Attachments | All inbound email | CC7.1 |
| TEC-06 | Phishing-resistant MFA (FIDO2 WebAuthn) on all email accounts | Okta Verify + YubiKey | 100% of email-accessible accounts | CC6.1, CC6.3 |
| TEC-07 | Mailbox forwarding rule detection and automated quarantine | CrowdStrike Identity Protection + Microsoft 365 Alert Policy | All Meridian mailboxes | CC6.6 |
| TEC-08 | Impossible travel / anomalous sign-in detection and automated block | Okta Identity Engine + CrowdStrike Identity Protection | All user authentications | CC6.6 |
| TEC-09 | External email banner (configurable, currently: yellow banner "EXTERNAL SENDER - Do not click links or open attachments unless you trust the sender") | Microsoft 365 Transport Rule | All inbound email from external domains | CC7.1 (user awareness) |
| TEC-10 | Encryption of Verified Contact Registry data at rest and in transit | AWS KMS (at rest) / TLS 1.3 (in transit) | VCR data in Snowflake | CC6.1 |

### 6.2 Administrative Controls

| Control ID | Control Description | Owner | Frequency | SOC 2 Criteria Reference |
|---|---|---|---|---|
| ADM-01 | Wire Transfer Verification procedure (Section 5.2) | CFO / VP Financial Services | Every payment request from email | CC6.6, PI1.3 |
| ADM-02 | DMARC compliance monitoring and reporting | VP IT Ops | Continuous / monthly report | CC6.1, CC7.2 |
| ADM-03 | Verified Contact Registry audit: review for dormant, stale, or anomalous contacts | VP Financial Services / CISO | Monthly | CC6.6 |
| ADM-04 | Supplier BEC awareness communication and acknowledgement tracking | CFO's office | Annually + onboarding | CC6.6 |
| ADM-05 | BEC tabletop exercise (rehearsal of Section 5.4 recovery and bridge assembly) | CISO / CFO | Quarterly | CC7.4 |
| ADM-06 | Email security configuration review (DMARC, SPF, DKIM, email gateway rules) | VP IT Ops | Quarterly | CC7.2 |
| ADM-07 | Third-party risk assessment for email service providers and email security vendors | CISO / Vendor Risk Management | Annually | CC6.6, CC9.2 |
| ADM-08 | Review and update of this SOP | CISO | Semi-annually (next: 2026-05-15) | CC7.2 |

### 6.3 Physical Controls

Meridian's physical security controls are secondary in the BEC context, as BEC is primarily a digital attack vector. However, the following controls are relevant:

- **Secure Operations Center:** The SOC (Boston HQ, 4th Floor) is protected by biometric access control. Workstations used for BEC response are on an isolated network segment.
- **Hardware Token Storage:** YubiKey tokens are stored in tamper-evident sealed bags and distributed in person with ID verification.
- **Executive Suite:** Executive offices containing printed Verified Contact Registry backups are secured with HID badge access and separate alarm zones.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance and Risk Indicators (KPIs/KRIs)

| Metric ID | Metric | Target | Measurement Method | Reporting Cadence | Audience |
|---|---|---|---|---|---|
| BEC-M01 | DMARC pass rate (aggregate) | ≥99.5% | DMARC aggregate report parsing (Datadog) | Monthly | CISO, VP IT Ops, CCO (for SOC 2) |
| BEC-M02 | BEC attempts detected and blocked by AI security platform | N/A (monitor trend) | Abnormal Security dashboard | Weekly | CISO, SOC Manager |
| BEC-M03 | User-reported suspicious emails (Phish Alert Button rate) | >90% of simulated BEC tests | KnowBe4 / Abnormal Security phishing simulation platform | Quarterly | CISO, VP IT Ops, CHRO |
| BEC-M04 | Mean time to triage for P1 BEC reports | ≤15 minutes | ServiceNow incident data | Monthly | CISO, SOC Manager |
| BEC-M05 | Wire Transfer Verification compliance rate (WTV completed vs. required) | 100% | NetSuite WTV attachment audit | Monthly | CFO, CCO |
| BEC-M06 | Supplier BEC policy acknowledgement rate | 100% | SEF portal tracking | Quarterly | CFO |
| BEC-M07 | BEC-related financial loss (rolling 12 months) | $0 | Finance incident log | Quarterly | CEO, CFO, CISO, Board Audit Committee |
| BEC-M08 | Time to deploy BEC-related email blocks (from SOC identification to gateway block) | ≤5 minutes | ServiceNow / Abnormal Security logs | Monthly | CISO, VP IT Ops |
| BEC-M09 | Dormant domains without DMARC | 0 | Domain Asset Registry vs. DNS scan | Weekly automated scan | VP IT Ops |
| BEC-M10 | Employee training completion rate (BEC-specific module) | ≥98% | Workday Learning | Annually (due Q1) | CHRO, CISO |

### 7.2 Dashboards and Reporting

**Operational Dashboard:** A live Datadog dashboard ("BEC Prevention Operations," Dashboard ID: `bec-ops-01`) is maintained and accessible to the SOC, CISO, and VP IT Ops. It displays:
- Real-time inbound email volume and AI-detected threat rate
- Active P1/P2 BEC incidents
- DMARC pass rates per domain
- Recently registered look-alike domains (Detectify Domain Watch integration)
- External email banner click-through rates (anomaly detection)

**Monthly BEC Prevention Report:** The CISO's office produces a monthly report, distributed to the Executive Leadership Team, containing:
- Executive summary of BEC threats and incidents for the month
- Trends in BEC-M01 through BEC-M09 metrics
- Notable BEC incidents and lessons learned
- Compliance status of DMARC, WTV, and training metrics for SOC 2
- Planned improvements or control changes

**Quarterly Board Report:** The CISO presents BEC posture to the Board-level AI Governance Committee (which also oversees cybersecurity) quarterly. The report focuses on BEC-M07 (financial loss), risk trends, and strategic improvements.

**SOC 2 Evidence Package:** The CCO (Thomas Anderson) collects and retains evidence monthly for the controls mapped to SOC 2 criteria (TEC-01 through TEC-10 and ADM-01 through ADM-07). Evidence includes screenshots of DMARC reports, sample WTV records, incident response timelines, and training completion records. This evidence is retained in the SOC 2 Evidence Repository (AWS S3 bucket `soc2-evidence-prod`, retention: 7 years).

---

## 8. Exception Handling and Escalation

### 8.1 Exception Requests

Any Personnel member or business unit seeking an exception to the controls outlined in this SOP must submit a formal exception request.

**Procedure for Exception Requests:**
1. **Initiation:** The requestor completes the "Information Security Exception Request" form in ServiceNow (Service Catalog > Information Security > Exception Request). The form requires:
   - Specific SOP section(s) for which exception is sought
   - Business justification with a risk-based rationale
   - Proposed compensatory controls
   - Time period for the exception (exceptions are time-bound; permanent exceptions are prohibited)
   - Manager approval
2. **Risk Assessment:** The CISO's office, with consultation from the CCO, conducts a risk assessment evaluating the residual risk if the exception is granted.
3. **Approval Authority:**
   - Exceptions to TEC-01 through TEC-10 (technical controls): CISO approval required
   - Exceptions to WTV procedure (ADM-01): **CFO + CISO joint approval required**; a temporary compensating control must be documented (e.g., dual video verification if voice callback is not possible)
   - Exceptions to training requirements (ADM-08): CHRO + CISO approval required
   - Any exception increasing BEC risk beyond Meridian's stated risk appetite (defined as any residual risk rated "High" or above on the Meridian Risk Matrix): **CEO approval required** per the Risk Appetite Statement (SOP-RISK-001)
4. **Tracking:** All approved exceptions are logged in the "IS Exceptions Register" (ServiceNow `sn_sec_exception` table), reviewed quarterly by the CISO, and presented to the Board Audit Committee annually.

### 8.2 Escalation Paths for BEC Incidents

| Scenario | First Escalation | Second Escalation | Ultimate Escalation |
|---|---|---|---|
| Suspected BEC email reported (P1/P2) | SOC Manager (within 15 min) | CISO | N/A |
| Confirmed BEC with credential compromise but no financial loss | CISO | CCO, CPO (if PHI/PII involved) | General Counsel |
| Confirmed BEC with financial loss <$50,000 | CFO, CISO | General Counsel | N/A |
| Confirmed BEC with financial loss ≥$50,000 | CFO, CISO, General Counsel | CEO (Dr. Sarah Chen) | Board Audit Committee Chair |
| Vendor Email Compromise affecting Meridian payments | VP Financial Services, CISO | CFO, CCO | General Counsel |
| BEC incident involving patient PHI (potential HIPAA breach) | CISO, CCO, CPO | General Counsel | CEO |
| BEC incident involving EU personal data (potential GDPR breach) | CPO (Dr. Klaus Weber) | CISO, General Counsel | CEO; supervisory authority (72hr) |

### 8.3 Whistleblower Reporting

Personnel who believe BEC prevention procedures are being deliberately circumvented or who are pressured to bypass verification processes may report their concerns confidentially through:
- Meridian's Ethics Hotline (managed by Navex Global): 1-800-555-3847 or meridianhealth.ethicspoint.com
- Direct communication with the General Counsel, Chief Compliance Officer, or Chair of the Audit Committee

Meridian's Non-Retaliation Policy (SOP-HR-014) protects good-faith reporters.

---

## 9. Training Requirements

### 9.1 Annual BEC-Specific Training

All Personnel must complete BEC-specific training as a module within the annual Information Security Awareness curriculum, delivered through Workday Learning.

**Training Module: "Defending Against Business Email Compromise" (Course Code: SEC-BEC-ANNUAL)**

| Module Section | Topics Covered | Duration | Assessment |
|---|---|---|---|
| Understanding BEC | BEC definition, TTPs, real-world examples (anonymized), cost to healthcare industry | 10 minutes | Knowledge check (80% pass mark) |
| Spotting the Red Flags | Display-name spoofing, urgency/pressure language, look-alike domains, "confidential" requests, time-sensitive payment demands, grammatical anomalies | 15 minutes | Simulated email identification (must correctly flag 4/5) |
| WTV Procedure Awareness | Overview of the verification requirement, how Finance will execute verification (so requestors understand the process), prohibition against bypassing | 10 minutes | Scenario-based question |
| Reporting Procedure | How to use "Report Phishing" button, when to call the SOC, what NOT to do (do not forward, do not reply, do not delete until instructed) | 5 minutes | Knowledge check |
| Consequences and Culture | Reiteration of no-blame culture for reporting; consequences for willful circumvention | 5 minutes | Acknowledgement |

**Total Duration:** 45 minutes
**Passing Threshold:** 80% on composite assessment; unlimited retakes permitted
**Completion Tracking:** Workday Learning auto-enrollment; non-completion triggers manager notification at 30- and 15-days prior to deadline, and CHRO escalation at deadline.

### 9.2 Role-Based Supplementary Training

| Role Group | Supplementary Training | Frequency | Provider |
|---|---|---|---|
| Finance & Financial Services Personnel | WTV procedure hands-on workshop; tabletop exercise participation | Annually + quarterly tabletops | VP Financial Services + CISO team |
| Executive Leadership Team | Executive impersonation awareness (personal digital hygiene, social media exposure awareness, family office security) | Semi-annually | CISO + external executive protection firm |
| SOC Analysts | BEC forensics and email header analysis; Abnormal Security platform deep-dive | Quarterly | VP IT Ops + Abnormal Security SE |
| Accounts Payable / Treasury | SEF portal operation and VCR access training; payment fraud red flags | Semi-annually | VP Financial Services |
| HR / Payroll | Payroll diversion BEC awareness (direct deposit change verification) | Annually | CHRO + CISO |
| Executive Assistants | High-touch executive impersonation identification; calendar and email hygiene | Quarterly | CISO office |

### 9.3 Simulated BEC Testing

Meridian conducts simulated BEC exercises through the KnowBe4 / Abnormal Security integrated platform:

- **Frequency:** Quarterly, with unannounced "spot tests" at the CISO's discretion
- **Targeting:** All Personnel, with weighted targeting towards Finance, HR, and Executive Assistants
- **Metric:** BEC-M03 (click-through and engagement rate); organizational target <5% engagement
- **Remediation:** Personnel who engage with a simulated BEC email are automatically enrolled in a 15-minute just-in-time remediation training module; repeat engagement (2+ in a rolling 12-month period) triggers a mandatory 1-on-1 coaching session with the Information Security Awareness Team

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs and Policies

| Document ID | Title | Relationship to This SOP |
|---|---|---|
| SOP-ISEC-015 | Phishing Awareness and Response | General phishing procedures; BEC is a specialized subset |
| SOP-ISEC-022 | Account Compromise Response | Procedure for handling confirmed email account compromise |
| SOP-ISEC-010 | Identity and Access Management | MFA requirements; privileged access management |
| SOP-ISEC-030 | Third-Party Security Management | Vendor risk assessments; supplier security requirements |
| SOP-RISK-001 | Enterprise Risk Management Framework | Risk appetite statement; risk acceptance thresholds |
| SOP-LEG-008 | Email Retention and Legal Hold | Email preservation for legal matters |
| SOP-CPO-012 | PHI Transmission Standards | Secure transmission of protected health information |
| SOP-FIN-045 | Payment Authorization and Wire Transfer | General finance authorization thresholds and workflow |
| SOP-HR-014 | Non-Retaliation Policy | Protection for good-faith reporting |
| SOP-CPO-025 | GDPR Data Breach Response | 72-hour notification procedure for EU personal data breaches |

### 10.2 External Standards and Frameworks

| Standard / Regulation | Relevance | Reference |
|---|---|---|
| AICPA SOC 2 | Trust Services Criteria for Security and Availability | 2024 AICPA SOC 2 Guide, CC6.1, CC6.3, CC6.6, CC7.1, CC7.2, CC7.4, PI1.3 |
| NIST SP 800-45 Version 2 | Email Security Guidelines | Federal email security best practices, adapted for commercial use |
| NIST AI RMF (AI 100-1) | AI Risk Management Framework | Governs the AI-based email security platform (Abnormal Security ML) as an AI system; relevant to explainability and monitoring |
| MITRE ATT&CK Framework | Enterprise Techniques | Initial Access (T1566), Execution (T1204), Defense Evasion (T1564) |
| ISO 27001:2022 | Information Security Management System | Annex A Controls: A.5.14 (Information Transfer), A.8.1 (User Endpoint Devices), A.8.7 (Protection Against Malware) |
| EU AI Act, Annex III | High-Risk AI Systems | Classification of AI email security as a protective system (not high-risk itself, but its failure could lead to compromise of high-risk Clinical AI Platform) |
| GDPR Art. 32, 33, 34 | Security of Processing, Breach Notification | EU personal data handling and breach notification |

---

## 11. Revision History

| Version | Date | Author | Approver | Change Summary |
|---|---|---|---|---|
| 1.0 | 2021-03-22 | Michael Tran (former CISO) | Dr. Sarah Chen, CEO | Initial SOP created in response to increasing healthcare-sector BEC attacks. Established DMARC monitoring (`p=none`) and basic wire verification. |
| 2.0 | 2022-11-15 | Rachel Kim, CISO | Dr. Sarah Chen, CEO | Major revision: DMARC policy escalated to `p=quarantine`; introduced Verified Contact Registry; added SOC 2 control mapping; incorporated Abnormal Security AI platform post-deployment. |
| 2.1 | 2023-06-08 | Rachel Kim, CISO | Dr. Sarah Chen, CEO | Minor revision: Updated callback verification to include shared secret requirement post-industry guidance (FBI PSAs on BEC call-back bypass); added vendor email compromise section (VEC). |
| 3.0 | 2024-01-09 | Rachel Kim, CISO | Dr. Sarah Chen, CEO | Major revision: DMARC policy hardened to `p=reject` (100%) for all sending domains; SEF vendor portal launched as mandatory path for supplier banking changes; phishing-resistant MFA mandated (SMS deprecated); SOC 2 evidence collection formalized for 2024 AICPA guide; EU AI Act considerations added for email security AI systems. |
| 3.1 | 2025-07-22 | Rachel Kim, CISO | Dr. Sarah Chen, CEO | Interim revision: Enhanced vendor onboarding communication requirement; added quarterly tabletop mandate; updated bank contact details post-merger; added DKIM key rotation automation via Lambda. |
| 3.2 | 2025-11-18 | Rachel Kim, CISO | Dr. Sarah Chen, CEO | Post-audit revision: SOC 2 auditor observation addressed—added explicit MFA requirement for contractor email accounts (Section 4.3); enhanced WTV documentation requirements with unique WTV ID and NetSuite attachment; added M09 and M10 metrics; expanded training section with role-based supplementary modules; updated escalation paths for GDPR breach scenarios. |

---

**Document Owner:** Rachel Kim, Chief Information Security Officer  
**Approver:** Dr. Sarah Chen, Chief Executive Officer  
**Last Reviewed:** 2025-11-18  
**Next Scheduled Review:** 2026-05-15  

*This document contains proprietary information of Meridian Health Technologies, Inc. Dissemination, distribution, or reproduction outside of Meridian without prior written authorization is strictly prohibited. This document is classified as "Internal" within the Meridian Data Classification Policy (SOP-ISEC-003).*
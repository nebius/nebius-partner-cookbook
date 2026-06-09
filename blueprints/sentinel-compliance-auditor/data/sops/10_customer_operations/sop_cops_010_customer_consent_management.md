---
sop_id: "SOP-COPS-010"
title: "Customer Consent Management"
business_unit: "Customer Operations"
version: "5.6"
effective_date: "2024-06-25"
last_reviewed: "2025-10-03"
next_review: "2026-04-25"
owner: "Michael Chang, VP of Customer Operations"
approver: "Robert Liu, VP of Financial Services"
classification: "Internal"
regulations:
  - "GDPR"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Customer Consent Management

## 1. Purpose and Scope

### 1.1 Purpose

The purpose of this Standard Operating Procedure (SOP) is to establish a consistent, auditable, and enterprise-wide framework for capturing, storing, tracking, and honoring customer consent preferences across Meridian Health Technologies, Inc. ("Meridian"). This SOP defines the operational processes necessary to manage the full consent lifecycle, from initial collection through preference modification, withdrawal, and eventual data subject offboarding, ensuring that customer autonomy is respected and that processing activities align with the stated preferences of the individual.

This document operationalizes Meridian's commitment to transparency and individual control by defining how the Customer Operations ("CustomerOps") team interfaces with the technology stack and other business units to execute consent directives. The procedures herein govern both digital consent mechanisms (web forms, API-based preferences, in-app consent modals) and manual consent collection channels (paper forms, verbal consent recorded during customer service interactions).

### 1.2 Scope

This SOP applies to the following populations, systems, and processing contexts:

**In-Scope Populations:**
- All prospective, current, and former direct customers of Meridian's HealthPay Financial Services platform (patient financing applicants, payment processing users).
- All authorized users of the MedInsight Analytics platform (health system administrators, clinical analysts, population health managers) who hold individual user accounts with distinct consent profiles.
- All patient end-users whose data is processed through Meridian's diagnostic imaging AI products (FDA 510(k)-cleared and CE-marked modules).
- Guardians, authorized representatives, and legal proxies acting on behalf of a data subject.

**In-Scope Consent Activities:**
- **Marketing Consent:** Preferences regarding promotional communications, product announcements, Meridian-sponsored events, and newsletter distributions via email, SMS, in-app notifications, and telephone.
- **Transactional Consent:** Preferences regarding operational communications (payment confirmations, service alerts, maintenance notifications). Note that certain transactional communications may be mandatory during active customer relationships; mandatory designation is governed by SOP-LEGL-045 (Communications Classification).
- **Analytics & Product Improvement Consent:** Preferences regarding the use of anonymized, pseudonymized, or aggregated usage data for product development and quality improvement initiatives.
- **Third-Party Data Sharing Consent:** Preferences regarding the disclosure of personal data to Meridian's strategic partners, integrated service providers, and marketplace participants.
- **Cookie & Web Tracking Consent:** Preferences set via the Meridian Consent Management Platform (OneTrust) for browser-based tracking technologies.

**Out of Scope:**
- Clinical research consent, which is governed by Meridian's Institutional Review Board (IRB) procedures (SOP-CLIN-201).
- Contractual terms of service acceptance, which are managed by Legal via SOP-LEGL-012.
- Employee data processing consent, which is governed by the Employee Privacy Notice.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|---|---|
| **Consent** | A freely given, specific, informed, and unambiguous indication of the data subject's wishes by which they, by a statement or by a clear affirmative action, signify agreement to the processing of personal data relating to them for a defined purpose. |
| **Consent Management Platform (CMP)** | The centralized technology solution used to collect, store, and propagate consent signals. For Meridian, the enterprise CMP is **OneTrust**, deployed across all customer-facing digital properties. |
| **Consent Record** | The immutable, auditable data object containing the data subject identifier, the purpose(s) consented to, the consent text version shown, the timestamp of the action, the IP address/geolocation, and the active status. Stored in the Consent Database (OneTrust Universal Consent Record). |
| **Consent Receipt** | A standardized, machine-readable token provided to the data subject following a consent action, containing the details of the record. |
| **Preference Center** | The self-service, authenticated portal (powered by OneTrust) where customers may view their current consents and modify their preferences at any time. |
| **Customer Operations Platform (COP)** | The unified agent desktop, built on **Salesforce Service Cloud**, where agents view customer consent status and execute manual consent changes during support interactions. |
| **Withdrawal** | The formal act by a data subject of revoking previously granted consent. Withdrawal does not render unlawful processing based on consent before its withdrawal. |
| **Soft Opt-In** | A permissible method for marketing to existing customers concerning similar products/services, provided the customer was given a clear opportunity to refuse (opt-out) at the point of initial collection and in every subsequent communication. Use of Soft Opt-In requires documented review by the Legal team. |
| **PIMS** | Meridian's Patient Identity Management System, the authoritative source of truth for patient demographic records. |
| **PUR** | Processing Usage Record - an internal data object linking a specific consent grant to a specific processing activity in the Meridian Data Catalog. |

---

## 5. Detailed Procedures

### 5.1 Consent Collection: Initial Capture

The collection of consent must occur at the point of data collection, prior to initiating the intended processing activity. Consent requests must be presented in plain language, clearly separated from general terms and conditions.

#### 5.1.1 Digital Acquisition (Web & Application)

**Pre-Conditions:**
- User navigates to a Meridian digital property: `healthpay.meridian.com` (customer portal), `insights.meridian.com` (MedInsight), or the mobile application.
- The relevant Customer Data Record (CDR) has been created (SOP-DATA-200).

**Procedure Steps:**
1.  The Customer Experience Platform (Adobe Experience Manager) renders the **Consent Capture Modal** via the OneTrust API integration.
2.  The modal presents the data subject with a **tiered consent interface**, starting with mandatory cookie/functional consent, then presenting Marketing, Third-Party Sharing, and Analytics as separate, non-pre-ticked checkboxes.
3.  For Marketing consent, the subject must select at least one channel preference (Email, SMS, In-App) to activate the consent grant. A "Select All" toggle is available but defaults to "off."
4.  Upon clicking "Save Preferences," the system generates a unique Consent Interaction ID and writes the Consent Record to the OneTrust Universal Consent Repository.
5.  The CMP invokes the **SOP-COPS-010 Consent Webhook**, which posts the Consent Record to the Salesforce Service Cloud Individual object.
6.  The Customer Data Platform (mParticle) syndicates the marketing opt-in status to downstream marketing automation platforms (Braze, Salesforce Marketing Cloud) in near real-time (latency SLA: < 3 minutes).
7.  A **Consent Summary Receipt** is dispatched asynchronously to the customer's primary email address on file.

#### 5.1.2 Assisted Collection (Agent-Guided)

This procedure applies when a customer provides consent verbally during a telephony interaction (1-800-MERIDIAN) or through a paper/PDF form processed by an agent.

**Agent Guidance Steps (Salesforce Service Cloud):**
1.  Agent authenticates the customer following the standard identity verification procedure (SOP-SEC-015).
2.  Agent navigates to the "Consent Management" tab on the customer's Contact record.
3.  Agent confirms the customer's current contact information (Email, Mobile) is correct; if not, agent must update the record before proceeding.
4.  Agent reads the **Consent Script** (Knowledge Article KA-01021 "Verbal Consent Script - General").
    - *Script excerpt:* "Meridian would like your permission to send you product updates and health insights via email and SMS. You can change your mind at any time by visiting our Preference Center or calling us back. Do I have your permission to enable Marketing communications?"
5.  Agent accurately records the customer's verbal response, indicating the channel and scope of consent.
6.  Agent clicks the "Log Assisted Consent" button. This generates a Consent Record stamped with the agent's user ID, the interaction ID, and the "Assisted Capture" methodology tag.
7.  The system automatically queues a Consent Confirmation email to the customer, providing a direct link to the Preference Center to verify their selections. The consent becomes operational immediately upon agent submission but is marked as "Pending Confirmation" for 72 hours. If the customer actively rejects the confirmation, the consent is automatically withdrawn and flagged for review.

---

### 5.2 Consent Tracking & The Preference Center

Meridian maintains a self-service **Consent & Preference Center** that enables customers to view the active, withdrawn, and expired consents associated with their profile.

#### 5.2.1 Customer Access & Navigation

Customers access the Preference Center via:
- A unique link embedded in the footer of every Marketing and Transactional communication (`Update Your Preferences`).
- A direct link from their authenticated dashboard (`Settings > Consent & Privacy`).
- Authenticated access via the Meridian Mobile App (`Profile > My Preferences`).

**Procedure (Customer Self-Service):**
1.  Upon authentication, the Preference Center renders a **Current Consent Status Dashboard**, displaying each Processing Purpose (Marketing, Analytics, 3rd Party Sharing) with its associated Status (Active / Withdrawn / Expired), Date of Initial Collection, and the Mechanism of Collection (e.g., "Online Signup 2024-06-25").
2.  Each active consent is accompanied by a clearly labeled, one-click "Withdraw" button.
3.  Modifying consent from "Opted-Out" to "Opted-In" requires an explicit **Positive Action** — the user must activate a toggle and then click a secondary "Confirm Opt-In" button.

---

### 5.3 Withdrawal Handling (Full and Partial)

A withdrawal request is the formal revocation of previously granted consent. The mechanism to withdraw must be as easily executed as the mechanism to grant.

#### 5.3.1 Processing a Full Withdrawal

A "Full Withdrawal" signifies the data subject's intent to revoke all non-mandatory consents and objects to further marketing communications.

**Operational Workflow:**
1.  The Withdrawal request is received via one of three channels:
    - **Self-Service:** Preference Center "Withdraw All" action.
    - **Agent-Assisted:** Customer contacts the 1-800-MERIDIAN support line.
    - **Written Request:** Customer sends an email to `privacy@meridian.com`.
2.  The receiving system or agent logs the request in the OneTrust Universal Consent Record. The Status for all relevant Purposes is set to `REVOKED`, with a time-stamp of record.
3.  A **Propagation Event** is published to the Meridian Event Bus (Apache Kafka), which triggers the following downstream actions:
    - **Salesforce Marketing Cloud:** Suppression list updated within 15 minutes. All active journeys and automations execute contact exclusion.
    - **Braze:** User profile flag `marketing_consent_status` set to `false`. All campaign canvas steps check this flag.
    - **Data Lake (Snowflake):** The marketing contactability column in the `CDP_GOLDEN_PROFILE` table is updated.
4.  For full withdrawals, the customer record is segmented as "Do Not Contact - Marketing" in the Customer Operations Platform.
5.  The agent or automated system closes the interaction with a confirmation message to the customer: "As requested, we have removed you from all marketing communications. Please allow up to 48 hours for all systems to fully synchronize. Transactional communications related to your active account(s) will continue."

#### 5.3.2 Processing a Partial Withdrawal

A partial withdrawal targets specific channels (e.g., "Stop SMS, but keep Emails") or specific purposes (e.g., "Keep HealthPay Transactional emails, but no Marketing emails").

**Operational Workflow:**
1.  Agent or self-service tool modifies the specific Purpose/Channel combination.
2.  The targeted downstream platform is updated. For example, a "No SMS" partial withdrawal triggers an update to the SMS gateway (Twilio) and ensures the mobile number is placed on the SMS suppression list, but Email consent remains untouched.
3.  The Consent Record reflects a `REVOKED` status only for the specific channel.

**Timeline SLA:**
| Withdrawal Type | Propagation Trigger | Max Sync Time Across Platforms |
|---|---|---|
| Full Withdrawal | Real-time event | 2 hours |
| Channel-Specific (Email) | Real-time event | 45 minutes |
| Channel-Specific (SMS) | Real-time event | 15 minutes |
| Purpose-Specific (Analytics) | Batch sync | 24 hours |

---

### 5.4 Marketing Consent Management

Marketing consent is managed as a distinct processing purpose, separate from consent for product analytics or service improvement. This ensures that the decision to avoid marketing does not impact the customer's experience of the core product.

#### 5.4.1 Acquisition Standards

Marketing consent shall be:
- **Active Opt-In:** Pre-ticked boxes or implied consent are prohibited.
- **Granular:** Customers must consent to specific channels (Email, SMS, Push Notification) independently. A "Global Opt-In" is permissible if each channel can be deselected individually.
- **Unbundled:** Acceptance of Terms of Service for the Meridian platform must not be a condition of marketing consent.

#### 5.4.2 Marketing Re-Consent Campaigns

In the event of a material change to the Privacy Notice or a change in the entity processing the marketing data, a Re-Consent Campaign shall be initiated.
1.  The Campaign Manager identifies the cohort of active customers requiring re-consent.
2.  A campaign is designed in Salesforce Marketing Cloud with a single, clear Call to Action ("Update Your Preferences Now").
3.  The campaign is sent a maximum of 3 times over a 30-day period.
4.  If no positive re-consent action is taken by the end of the 30-day window, the system automatically transitions the campaign cohort's marketing consent status to `EXPIRED` and suppresses further marketing communications.

---

### 5.5 Minor's Consent

For products that may collect data from individuals under the age of 16 (digital consent age threshold), a verifiable parental or guardian consent process must be executed. This is managed via the OneTrust Minor Consent module. The Customer Operations team will route all suspected minor account cases to the dedicated Minor Consent queue for specialized handling as defined by SOP-LEGL-110.

---

## 6. Controls and Safeguards

The following technical and administrative controls are established to ensure the integrity and confidentiality of the consent management process:

### 6.1 Technical Controls

| Control ID | Control Description | Technology |
|---|---|---|
| **T-010** | **Immutable Ledgering:** All Consent Records (grant, modification, withdrawal) are appended to an immutable audit log. No record can be deleted or overwritten. | OneTrust Audit Trail, SIEM (Splunk) integration |
| **T-011** | **Automated Sync Verification:** A delta-detection script runs hourly, comparing active Marketing consent counts in OneTrust against the suppression list in Salesforce Marketing Cloud. Mismatches > 5 records trigger a P2 Incident. | Custom Python Script (AWS Lambda) |
| **T-012** | **API Gateway Throttling:** Consent Preference Center API endpoints are rate-limited to prevent malicious bulk withdrawal attempts. Limit: 30 requests per minute per IP address. | AWS API Gateway |
| **T-013** | **Encryption at Rest:** The PII associated with a consent profile (email, phone) is stored in Salesforce Shield with AES-256 encryption. | Salesforce Shield Platform Encryption |
| **T-014** | **Change Data Capture (CDC):** Any modification to a high-sensitivity consent field fires a CDC event logged to Splunk for Security Operations Center (SOC) review. | Salesforce CDC, Splunk |

### 6.2 Administrative Controls

- **Quarterly Access Review:** The VP of Customer Operations and the CISO will jointly review all active accounts with administrative access to the OneTrust platform to ensure principle of least privilege.
- **Change Management (ITIL):** Any modifications to the Consent Capture Modal or the Preference Center UI code must follow the standard IT Change Management process per SOP-IT-200-CAB, including a mandatory compliance review by the Legal Operations team.
- **Semi-Annual Consent Audit:** An independent audit team (Internal Audit or External Auditor) will perform a semi-annual review of a statistically significant sample of consent records to verify alignment between source documents, CMP logs, and downstream provisioning.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

Customer Operations leadership tracks the following KPIs to measure the effectiveness and health of the consent management ecosystem:

| KPI | Measurement | Target | Review Cadence |
|---|---|---|---|
| **Consent Capture Rate** | Percentage of active customer profiles with a valid, complete Consent Record. | ≥ 98% | Monthly (MOAR) |
| **Sync Latency (Marketing)** | Time from Consent Action (opt-in/out) to effective suppression/provisioning in Braze. | P95 < 45 min | Weekly |
| **Customer Withdrawal Processing Time** | Time from receipt of a manual withdrawal request (via call or email) to full propagation and customer confirmation of completion. | Mean < 8 business hours | Weekly Operations Review |
| **Preference Center Utilization** | Ratio of self-service consent modifications versus agent-assisted modifications. | ≥ 75% Self-Service | Quarterly |
| **Complaint Volume (Consent-Related)** | Number of complaints logged via support channels citing "unwanted communications" or "unable to withdraw." | < 0.01% of active contacts | Monthly |

### 7.2 Reporting

- **Weekly Consent Operations Dashboard:** An automated dashboard in Tableau provides near-live data on agent-assisted consent volume, by agent, including call reason disposition codes.
- **Monthly Consent Management Report (MCMR):** A comprehensive PowerPoint deck delivered by the Director of Customer Operations to the VPs of Customer Ops, Financial Services (for HealthPay consent implications), and the Chief Privacy Officer. The report covers KPI trend analysis, exception logs, and summaries of any privacy-impacting incidents.
- **Annual Consent Management Review (ACMR):** A formal, audited report that feeds into Meridian's annual regulatory compliance assessment for privacy and data governance.

---

## 8. Exception Handling and Escalation

An "Exception" is defined as any processing activity that deviates from the standard procedures defined in Section 5 of this policy, or any system condition where consent is not propagated as per the defined Technical Controls in Section 6.

### 8.1 Exception Scenarios & Handling Procedures

#### 8.1.1 Scenario: Backdated Consent (Legacy Migration)

A customer record is discovered (often during a migration or M&A activity) that was loaded into the Meridian platform without a properly formatted digital Consent Record, but where the business unit asserts "valid consent was obtained historically."

**Procedure:**
1.  The owning Business Unit Manager must create a **Legacy Consent Declaration** in the ServiceNow Governance, Risk, and Compliance (GRC) module.
2.  The declaration must include: the data source, the total number of affected records, the mechanism of original collection, and a copy of the original consent language used.
3.  The Legal Operations team reviews the declaration. If the historical language meets current corporate standards, Legal Operations approves the Legacy Consent Declaration.
4.  Customer Operations may then re-consent the user on their next interaction, or, for low-risk cohorts, batch-upload a "Historical - Migration" consent tag in OneTrust. This tag is tracked as an exception.

#### 8.1.2 Scenario: System Sync Failure (Breach of Sync SLA)

A significant mismatch is identified by Control T-011 (Automated Sync Verification), or a critical platform (e.g., Salesforce Marketing Cloud) fails to process the propagation event from the Event Bus.

**Procedure:**
1.  The IT Operations Center (ITOC) declares a **P2 Consent Sync Incident**.
2.  Customer Operations initiates a manual sync process: exporting the delta file from OneTrust and performing a controlled import into the affected downstream system, as per the manual override runbook (KA-01055).
3.  All affected contacts are placed in a "Communication Hold" status in the COP until the manual sync is complete and verified by the ITOC.
4.  The VP of Customer Operations will determine if a post-incident notification to the cohort is required based on the risk of mis-sent communications.

### 8.2 Exception Approval Authority

| Exception Type | Impact Threshold | Approval |
|---|---|---|
| Standard Procedural Exception (e.g., minor deviation from script) | Individual Record | Team Lead, Customer Operations |
| Technical Workaround (e.g., manual sync) | Cohort (< 5,000 records) | Director, Customer Operations & IT Operations Manager |
| Policy Exception (e.g., waiver of re-consent) | Cohort (> 5,000) or Policy | VP, Customer Operations & Chief Privacy Officer |

---

## 9. Training Requirements

All personnel with access to customer records and consent management tools must complete the mandatory training curriculum outlined below. Completion is tracked via the Meridian Learning Management System (Cornerstone).

| Training Module | Code | Target Audience | Frequency | Content |
|---|---|---|---|---|
| **Foundation: Data Privacy & Consent** | TRN-COPS-010A | All Customer Ops Agents (Tier 1-3), Account Managers | Annual, and upon hire | Principles of consent, Meridian Privacy Notice overview, data subject rights, Meridian's ethical commitment to transparency. |
| **Operational: COP Consent Management** | TRN-COPS-010B | Customer Ops Agents (Tier 1-2) | Quarterly refresher | Hands-on workshop in Salesforce sandbox: executing an Assisted Consent, processing a Full and Partial Withdrawal, locating the Consent Script, handling an agitated customer requesting deletion. |
| **Technical: Governance for Engineers** | TRN-ENG-010C | Platform Engineers, DevOps (IT) | Biannual | Technical deep dive on the consent data model, OneTrust API architecture, Kafka topic schemas, incident response runbooks for sync failures. |
| **Specialized: Marketing Consent Compliance** | TRN-MKTG-010D | Marketing Automation Managers, Campaign Managers | Biannual | Granular consent in campaigns, the prohibition against bundled consent, Re-Consent Campaign procedures, the absolute suppression list policy. |

Non-compliance with training requirements results in the progressive revocation of user access: a 14-day grace period past due notification, followed by suspension of access to the Customer Operations Platform and OneTrust administrative interfaces until the training is completed.

---

## 10. Related Policies and References

| Internal Reference ID | Document Title |
|---|---|
| SOP-DATA-200 | Customer Data Record Creation and Maintenance |
| SOP-SEC-015 | Customer Identity Verification & Authentication Standards |
| SOP-LEGL-045 | Legal Classification of Communications (Transactional vs. Marketing) |
| SOP-LEGL-012 | Terms of Service and Contract Acceptance Management |
| SOP-IT-200-CAB | IT Change Management & Control Advisory Board Procedures |
| SOP-LEGL-110 | Processing of Minor's Personal Data & Verifiable Parental Consent |
| KA-01021 | Verbal Consent Script - Agent Guidance (Knowledge Article) |
| KA-01055 | Manual Consent Sync Runbook - Emergency Operations (Knowledge Article) |
| POL-DATA-001 | Meridian Corporate Data Governance & Ethics Charter |
| POL-PRIV-001 | Customer Privacy Notice (Internal Reference Version) |

---

## 11. Revision History

| Version | Date | Author/Editor | Summary of Changes |
|---|---|---|---|
| 5.0 | 2023-03-15 | J. Kim, Legal Operations | Major rewrite. Introduced granular channel consent, OneTrust Preference Center integration, and updated marketing consent rules for new SMS standards. |
| 5.1 | 2023-07-20 | M. Chen, Customer Ops | Added Section 5.1.2 (Assisted Collection) and updated agent scripts following Service Cloud migration. |
| 5.2 | 2023-10-05 | A. Patel, IT Security | Incorporated Technical Controls for immutable ledgering and encryption requirements (Salesforce Shield). Updated Sync failure runbook. |
| 5.3 | 2024-01-18 | S. Davis, Training | Added Section 9 (Training Requirements) and defined new quarterly refresher modules. |
| 5.4 | 2024-04-10 | M. Chang, VP CustOps | Full review cycle. Updated KPI targets (Section 7.1), revised exception approval tiers (Section 8.2), and formalized semi-annual audit control. |
| 5.5 | 2024-06-25 | M. Chang, VP CustOps | Approved changes to Re-Consent Campaign procedures (Section 5.4.2) and updated Propagation Timeline SLA. Effective date version. |
| 5.6 | 2025-10-03 | A. Reyes, Compliance | Periodic review. Updated Minor's Consent reference to new SOP-LEGL-110. Refined definitions and aligned cross-references. No procedural changes. |
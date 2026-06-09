---
sop_id: "SOP-COPS-014"
title: "Knowledge Base Management"
business_unit: "Customer Operations"
version: "4.3"
effective_date: "2024-08-13"
last_reviewed: "2025-09-11"
next_review: "2026-03-13"
owner: "Michael Chang, VP of Customer Operations"
approver: "Robert Liu, VP of Financial Services"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Knowledge Base Management

## 1. Purpose and Scope

### 1.1 Purpose
The purpose of this Standard Operating Procedure (SOP) is to establish a standardized, auditable, and controlled framework for the creation, review, approval, publication, maintenance, and archival of knowledge base (KB) articles within Meridian Health Technologies, Inc. This SOP ensures that all customer-facing and internal support documentation is accurate, secure, consistent, and compliant with SOC 2 Trust Services Criteria, specifically within the Common Criteria (CC) series and the Availability and Confidentiality categories.

### 1.2 Scope
This SOP applies to all knowledge base content managed and published by the Customer Operations business unit across all Meridian product lines:
- Clinical AI Platform
- HealthPay Financial Services
- MedInsight Analytics
- Meridian SaaS Platform

This SOP governs the **Meridian Knowledge Portal** (powered by ServiceNow Knowledge Management) and the **Internal Support Wiki** (Confluence Cloud). It applies to all employees, contractors, and third-party service desk agents (collectively "Contributors") who author, review, edit, or approve KB content.

### 1.3 Out of Scope
- Machine learning model technical documentation maintained by the AI Governance Committee (refer to SOP-AIG-002).
- Code-level documentation maintained within GitHub repositories.
- Legal contracts and policy documents maintained by General Counsel’s office.

---

## 2. Definitions and Acronyms

| Term | Definition |
|------|------------|
| **Article** | A single document within the Knowledge Base containing text, images, links, and attachments designed to address a specific topic or issue. |
| **KB** | Knowledge Base. The centralized repository of information stored in ServiceNow or Confluence. |
| **KPI** | Key Performance Indicator. A measurable value demonstrating how effectively the KB is achieving key objectives. |
| **PHI** | Protected Health Information. Any information about health status, provision of health care, or payment for health care that can be linked to an individual. |
| **PII** | Personally Identifiable Information. Any data that could potentially identify a specific individual. |
| **SME** | Subject Matter Expert. An individual with deep knowledge of a specific product, feature, or regulatory requirement. |
| **KBOM** | Knowledge Base Operations Manager. The designated owner of the KB process within Customer Operations. |
| **TSC** | Trust Services Criteria. The criteria used by SOC 2 auditors to evaluate controls. |
| **CC5.1 / CC5.2** | SOC 2 Common Criteria related to control environment and communication. |
| **A1.2** | SOC 2 Availability criterion related to system recovery and continuity. |
| **C1.1** | SOC 2 Confidentiality criterion related to identification and protection of confidential information. |

---

## 3. Roles and Responsibilities

### 3.1 RACI Matrix
The following matrix defines the Responsible, Accountable, Consulted, and Informed parties for all KB lifecycle stages.

| Activity | KB Contributor (Author) | KB Editor | SME / Product Lead | KBOM | VP Customer Ops | CISO / DPO |
|----------|------------------------|-----------|--------------------|------|-----------------|------------|
| **Content Creation** | R | C | C | I | I | I |
| **Technical Accuracy Review** | I | - | R/A | C | I | - |
| **Confidentiality Review (PHI/PII/PCI)** | C | R | - | A | - | R/A |
| **SOC 2 Compliance Alignment** | - | C | - | R | I | A |
| **Final Publication Approval** | I | I | C | R | A | I |
| **Quarterly Audit** | I | I | C | R/A | I | C |
| **Emergency Removal** | I | R | I | A | I | I |

### 3.2 Role Definitions
- **KB Contributor (Author):** Any Tier 2 or Tier 3 support agent, product analyst, or designated developer creating a new article. Responsible for drafting content that is technically accurate and free of sensitive data.
- **KB Editor:** A member of the Customer Operations Content Team responsible for enforcing style guides, formatting, and initial vetting for PII/PHI violations using automated scanning tools.
- **SME / Product Lead:** For HealthPay Financial Services, the SME must be a certified SR 11-7 model validator. For Clinical AI, the SME must hold an MD or equivalent clinical informatics certification. SMEs are Accountable for factual accuracy.
- **Knowledge Base Operations Manager (KBOM):** Reports to VP of Customer Operations. Owns the SOP, manages the backlog of articles, and ensures SLA compliance for review cycles.
- **VP of Customer Operations (Michael Chang):** Approves the overall strategy and any high-risk article publications that impact regulatory standing.
- **CISO/DPO (Rachel Kim / Dr. Klaus Weber):** Provide consultation on data classification. The DPO has veto power over any article containing potential EU personal data risks.

---

## 4. Policy Statements

Meridian Health Technologies is committed to maintaining a "single source of truth" for all customer and internal operational knowledge.

1.  **Confidentiality and Privacy:** No article shall contain PII, PHI, or PCI data. All article content is classified as `Internal` or `Public` per the Meridian Data Classification Policy (SOP-INFOSEC-005). Screen captures must be de-identified using the approved Meridian Blur Tool prior to upload.
2.  **SOC 2 Availability (A1.2):** The KB platform must achieve 99.9% uptime to support customer self-service and business continuity. A static HTML copy of critical incident response articles must be stored in an offline Azure blob storage container for access during major AWS service disruptions.
3.  **SOC 2 Communication (CC5.1/CC5.2):** The KB serves as a formal mechanism for communicating the design and operation of our services to users and internal auditors. All articles must be version-controlled.
4.  **Accuracy and Timeliness:** All KB articles must be reviewed and recertified at intervals not exceeding 180 days. Articles related to financial regulations (HealthPay) must be reviewed within 30 days of any regulatory update published by the Federal Reserve, CFPB, or relevant state bodies.

---

## 5. Detailed Procedures

### 5.1 Article Creation Request Intake
This procedure outlines how a new KB article is requested when a gap is identified during a support case closure or a product release.

1.  **Gap Identification:** A Tier 2 agent identifies that a case required an answer not present in the KB. During case closure in ServiceNow, the agent checks the `KB Candidate` box.
2.  **Queue Review:** The KBOM reviews the `KB Candidate` queue every business day at 10:00 AM EST. The KBOM triages requests based on:
    - **Urgency:** High (Defect/Workaround), Medium (Feature clarification), Low (Cosmetic).
    - **Impact:** Number of cases deflected (estimated).
3.  **Assignment:** If approved, the KBOM assigns the draft to a Contributor within the relevant product pod. The task appears in the `KB_Contribution` assignment group in ServiceNow.
4.  **Template Selection:** The Contributor selects the appropriate template:
    - `SOP-KB-T01` (Troubleshooting)
    - `SOP-KB-T02` (Procedural/How-to)
    - `SOP-KB-T03` (FAQ)
    - `SOP-KB-T04` (Release Notes)

### 5.2 Content Drafting and Submission
This procedure describes the authoring controls specific to protected data and external references.

1.  **Drafting Environment:** Authors must draft directly in ServiceNow. Copying and pasting from external sources (email, chat logs) is strictly prohibited due to the risk of metadata leak.
2.  **Image Handling:** All screenshots must be captured using the Meridian SecureCapture browser extension, which automatically redacts client names and ID fields. Images must be uploaded as `.png` files with accessibility alt-text.
3.  **Data Obfuscation Script:** If an article requires an example API payload or log output, the author must run the `meridian-sanitizer --mode strict` CLI tool to replace real tokens with dummy data before pasting.
4.  **Linking:** Hyperlinks to internal systems (e.g., `confluence.internal.meridian.io`) must be reviewed to ensure they do not expose private endpoints to the public network if the article is later promoted to Public.

### 5.3 Review Workflow
Every article must pass through three gates before publication. This is enforced by the ServiceNow workflow engine (Workflow ID: KB_APPROVAL_GRP_01).

#### Gate 1: Editorial Review
- **Owner:** KB Editor pool.
- **Action:** The automated system scans the article body for pattern-matching regex (e.g., `SSN`, `Credit Card numbers`, `MM/DD/YYYY` specific date formats associated with PHI).
- **SLAs:** High urgency articles must be edited within 4 business hours. Standard urgency within 48 hours.

#### Gate 2: Technical Peer Review
- **Owner:** Designated SME for the specific business line.
- **Action:** The SME logs into a sandbox/test environment and follows the article steps literally (click-by-click). If the steps fail, the article is rejected with the tag `failed_sandbox`.
- **HealthPay Specific:** The SME must confirm the content does not violate SR 11-7 by implying guaranteed financial outcomes or misrepresenting model risk. The SME must attach the `SR11-7_Review_Checklist` to the ServiceNow task.

#### Gate 3: Final Release Approval
- **Owner:** KBOM or Delegate.
- **Action:** Confirms all previous gates are green. Assigns the appropriate audience to the article:
    - `wsc_public` (Customer-facing)
    - `wsc_authenticated` (Login required)
    - `wsc_internal` (Staff only, contains proprietary system architecture)

### 5.4 Periodic Review and Recertification Cycle
This procedure ensures compliance with the 180-day recertification SLA documented in SOC 2 Control Control ID: COPS-014-C04 (Content Accuracy Assurance).

1.  **Automated Trigger:** A scheduled job runs every Sunday at 02:00 UTC. It queries `kb_knowledge` for articles where `last_published + 180 days < today()`.
2.  **Assignment:** A batch task is created in the `KB_Recertification` queue.
3.  **Review Process:**
    - The assigned SME tests the article against the current production UI.
    - If still valid, the SME updates the `workflow_state` to `validated` and adds a comment indicating the recertification date. The `last_reviewed` field auto-updates.
    - If obsolete, the SME sets the state to `retired`. Retired articles remain searchable for historical audit purposes but show a yellow banner: *"This article is archived and may not reflect the latest product version."*
4.  **Escalation:** If an article is not recertified within 14 days of the due date, the KBOM receives a PagerDuty alert. At 21 days overdue, the VP of Customer Operations is notified, and the article is automatically unpublished (state moved to `draft`).

### 5.5 Access Control and Promotion
This procedure enforces the SOC 2 Confidentiality Criterion (C1.1).

1.  **Classification Matrix:**
    - **Internal (Confidential):** Contains architecture diagrams, internal IP ranges, vendor secrets (masked), or non-public product roadmaps. Access requires Okta SSO and membership in the `KB_Internal_Readers` group.
    - **Public:** General support, troubleshooting, and user guides. Accessible from the public internet via Zendesk Guide.

2.  **Access Review:** The KBOM conducts a quarterly "Entitlement Review." The `KB_Internal_Readers` group member list is compared against active Meridian employees. Terminated employees must have their access removed within 1 business day per HR termination ticketing integration.

---

## 6. Controls and Safeguards

This section maps specific administrative and technical controls to the SOC 2 Trust Services Criteria.

| Control ID | Control Description | TSC Mapping | Mechanism |
|------------|---------------------|-------------|-----------|
| **COPS-014-C01** | Sensitive data is prevented from entering the KB. | CC6.1 (Logical Access Security), C1.1 | Automated DLP scanning via Nightfall AI integration on ServiceNow attachments. Regex blocks PHI patterns. |
| **COPS-014-C02** | Author rights are restricted to authorized personnel. | CC6.2 | SSO via Okta with MFA. Write access restricted to `Customer_Ops_Contributors` and `Engineering_T3` groups. |
| **COPS-014-C03** | Audit trail is immutable for article changes. | CC7.2 | ServiceNow audit tables capture every `update` and `delete` event. Logs shipped to Sumo Logic encrypted SIEM. |
| **COPS-014-C04** | Articles are accurate and reviewed periodically. | CC8.1 | 180-day forced recertification workflow described in Section 5.4. Dashboard monitors overdue ratio. |
| **COPS-014-C05** | Customer self-service availability during disaster recovery. | A1.2, A1.3 | Static backup of top 200 critical articles synced to Azure Blob (Cool tier) every 24 hours. |
| **COPS-014-C06** | Segregation of duties for content approval. | CC5.3 | Author cannot approve own content. Mandatory dual approval (Editor + SME) before publication. |

### 6.1 Secure Content Controls
- **Encryption:** All attachments are encrypted at rest using AES-256 (AWS KMS keys managed automatically by ServiceNow cloud infrastructure).
- **Data Classification Tags:** Automated tags are applied if the system detects a specific product name (e.g., `tag:healthpay_financial`). This tag triggers the additional SR 11-7 review workflow.

---

## 7. Monitoring, Metrics, and Reporting

The following KPIs are tracked by the Customer Operations management team to ensure operational efficiency and SOC 2 compliance.

### 7.1 Key Performance Indicators (KPIs)

| KPI | Target | Measurement Tool | Frequency | Responsible |
|-----|--------|------------------|-----------|-------------|
| **KB Deflection Rate** | > 35% | Google Analytics / ServiceNow Link Tracking | Weekly | KBOM |
| **Recertification Compliance** | 100% completion within 30 days of due date | ServiceNow Performance Analytics | Weekly | KBOM |
| **Average Review Time** | < 48 hours for Standard | ServiceNow Workflow Analytics | Monthly | Customer Ops Dir |
| **DLP False Positive Rate** | < 5% of scanned documents | Nightfall AI Dashboard | Monthly | CISO Office |
| **System Uptime (SaaS KB)** | 99.95% | Datadog Synthetics | Real-time | IT Operations |

### 7.2 Incorrect Content Metric (SOC 2 Control COPS-014-C04 Addendum)
A specific metric tracks articles flagged as "Incorrect" by users via the feedback function.
- **Formula:** `(Number of "Incorrect" reports verified as true) / (Total articles viewed) * 100`
- **Threshold:** Cannot exceed 0.1%.
- **Action:** If threshold exceeds, a mandatory Full Inventory Review is triggered within 5 business days.

### 7.3 Reporting Cadence
- **Monthly:** A KB Health Report is sent to the VP of Customer Operations, including deflection rates and top 10 underperforming articles.
- **Quarterly:** A SOC 2 Compliance Deck is prepared for the Internal Audit team summarizing access reviews, recertification rates, and control failures.
- **Annually:** A comprehensive audit is conducted by an external auditor (currently Deloitte) as part of the SOC 2 Type II examination.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Process
Any deviation from this SOP (e.g., publishing without SME review, bypassing the 4-hour editorial SLA, publishing a draft containing redacted but potentially sensitive metadata) requires an exception.

1.  **Submission:** The requestor submits a `KB_Exception_Request` form in ServiceNow. The form must specify:
    - Article ID
    - Nature of exception
    - Justification (e.g., Emergency security hotfix requiring immediate publication)
    - Duration of exception (e.g., "Review will occur within 24 hours post-publication instead of pre-publication")
2.  **Approvals:**
    - *Routine Exceptions:* Approved by the KBOM.
    - *Emergency Exceptions (P1 Outage):* Approved by the Incident Commander (as defined in the Incident Response SOP, SOP-IT-003) with post-hoc briefing to KBOM within 3 business days.
    - *High-Risk Exceptions (Potential PHI exposure):* Requires joint approval from the **Chief Privacy Officer (Dr. Klaus Weber)** and the **VP of Customer Operations (Michael Chang)**. This is a non-delegable duty.

### 8.2 Emergency Removal Protocol
If PHI or PCI is confirmed to be publicly exposed in a KB article (confirmed Nightfall AI alert Severity 1):

1.  **Immediate Action:** The KBOM or CISO invokes the "Break Glass" procedure in ServiceNow to instantly unpublish the article. This does not delete the revision history for forensic analysis.
2.  **Containment:** The IT Security team (CrowdStrike/Cyber Incident Response) analyzes if the page was cached by search engines and issues takedown requests.
3.  **Notification:** Legal and DPO notified. If EU citizen data was involved, a 72-hour notification to the supervisory authority may be required under GDPR.

---

## 9. Training Requirements

### 9.1 Initial Training
All new hires in Customer Operations, Tier 2 Support, and Product Content teams must complete the following within their first week of onboarding:

- **Course ID:** LMS-KB-101 ("Effective KB Writing for Healthcare IT").
- **Course ID:** LMS-DP-102 ("HIPAA and You: Handling Patient Data in Text").
- This SOP Document sign-off.

### 9.2 Annual Refresher Training
Prior to the annual refresher, the KBOM reviews the error logs from the previous year to identify authors who consistently trigger DLP warnings.

- **Target Group:** Authors with > 2 DLP warnings in 12 months must attend a remedial "Clean Writing" workshop.
- **Content Update:** The annual training must include a review of the latest phishing simulation results to remind authors that KBs must not become targets for internal knowledge scraping.

### 9.3 Training Records
Training completion is tracked via the Workday LMS. The KBOM validates that 100% of active KB Contributors have completed the latest training before granting ServiceNow write access for the new fiscal year. Non-compliant users have their write access revoked automatically by a nightly background job.

---

## 10. Related Policies and References

### 10.1 Internal SOPs
- **SOP-INFOSEC-005:** Data Classification Policy
- **SOP-IT-003:** Incident Response Plan
- **SOP-HR-001:** Employee Offboarding (Access Revocation)
- **SOP-AIG-002:** AI Model Documentation Standards
- **SOP-SW-D-010:** Secure Software Development Lifecycle (SSDLC)

### 10.2 External Standards
- **AICPA TSC 2017 (SOC 2):** Availability (A1.2), Confidentiality (C1.1), Communication (CC5.1/CC5.2).
- **ISO 30401:2018:** Knowledge management systems — Requirements. Referenced for overall KM framework structuring.
- **NIST SP 800-53 Rev 5:** AC-3 (Access Enforcement), AU-12 (Audit Record Generation), MP-6 (Media Sanitization).

---

## 11. Revision History

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| 1.0 | 2021-02-15 | J. Smith | Initial document creation. Basic writing standards. |
| 2.0 | 2022-08-01 | M. Jones | Added SOC 2 specific controls. Introduced 180-day review cycle. |
| 3.0 | 2023-05-20 | A. Williams | Migrated platform from Zendesk to ServiceNow. Updated roles to reflect new org chart. |
| 4.0 | 2024-03-10 | D. Garcia | Added strict DLP monitoring, removed ability for L1 agents to draft. |
| 4.1 | 2024-08-13 | K. Weber | Pre-audit hardening. Added Section 6 controls table mapping to TSC. |
| 4.2 | 2025-04-02 | L. Chen | Introduced Emergency Removal Protocol (8.2) and updated escalation matrix for HealthPay. Added regulatory change trigger (30-day rule). |
| 4.3 | 2025-09-11 | K. Weber | Annual review. Updated metrics threshold in 7.2 per auditor feedback. Added Appendix A (DPO Veto process). Approved by R. Liu. |
---
sop_id: "SOP-COPS-018"
title: "Third-Party Support Provider Management"
business_unit: "Customer Operations"
version: "5.5"
effective_date: "2024-07-28"
last_reviewed: "2025-06-15"
next_review: "2025-12-05"
owner: "Michael Chang, VP of Customer Operations"
approver: "Robert Liu, VP of Financial Services"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Third-Party Support Provider Management

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework for the selection, engagement, training, performance monitoring, and termination of Third-Party Support Providers (TSPs) engaged by Meridian Health Technologies, Inc. ("Meridian"). The purpose of this SOP is to ensure that all customer-facing and technical support functions delivered by external entities meet Meridian's quality standards, protect the confidentiality and integrity of customer data, and maintain compliance with applicable contractual, security, and availability commitments.

### 1.2 Scope

This SOP applies to all external entities and their personnel who provide support services on behalf of Meridian's Customer Operations division, including but not limited to:

| Service Category | Description | Applicable Product Lines |
|---|---|---|
| Tier 1 Customer Support | First-response patient and provider inquiries via phone, email, and chat | HealthPay, MedInsight Analytics, Meridian SaaS Platform |
| Tier 2 Technical Support | Escalated troubleshooting and product configuration support | All product lines |
| Clinical Application Support | Workflow guidance and non-diagnostic support for clinical users | Clinical AI Platform |
| Financial Services Support | Payment processing inquiries, claims status, lending questions | HealthPay Financial Services |
| Linguistic and Regional Support | Multilingual support for EU and APAC markets | All product lines |
| After-Hours and Overflow Support | Supplemental coverage outside standard business hours | All product lines |

**Inclusions:**
- All TSPs with access to Meridian systems, data, or facilities
- TSP personnel performing remote or on-site support functions
- Subcontractors engaged by primary TSPs (sub-tier suppliers)

**Exclusions:**
- Independent contractors engaged directly as individual contributors (see SOP-HR-042)
- Managed service providers for infrastructure operations (see SOP-IT-076)
- External legal counsel and audit firms
- Clinical advisory board members not providing operational support

### 1.3 Geographic Applicability

This SOP applies to TSP engagements servicing Meridian's operational regions: North America, the European Union, the United Kingdom, and the Asia-Pacific region. TSPs operating from, or supporting end-users in, multiple jurisdictions must operate in accordance with the most restrictive requirements applicable to their service territory.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|---|---|
| **TSP** | Third-Party Support Provider — An external organization contracted to deliver customer or technical support services on behalf of Meridian. |
| **BA** | Business Associate — As defined under HIPAA, a person or entity that performs functions or activities involving the use or disclosure of Protected Health Information on behalf of Meridian. |
| **PHI** | Protected Health Information — Individually identifiable health information handled by Meridian systems. |
| **PII** | Personally Identifiable Information — Information that can identify an individual, alone or in combination with other data. |
| **SOC 2** | Service Organization Control 2 — An auditing standard developed by the AICPA evaluating controls relevant to security, availability, processing integrity, confidentiality, and privacy. |
| **NDA** | Non-Disclosure Agreement — A legal contract establishing confidentiality obligations. |
| **MSA** | Master Services Agreement — The overarching contractual framework governing the relationship with a TSP. |
| **SOW** | Statement of Work — A document detailing the specific services, deliverables, timelines, and pricing for a TSP engagement. |
| **OLA** | Operational Level Agreement — An internal agreement defining the working relationship between Meridian teams and a TSP. |
| **KPI** | Key Performance Indicator — A quantifiable measure used to evaluate the performance of a TSP against defined targets. |
| **CSAT** | Customer Satisfaction Score — A metric measuring end-user satisfaction with a support interaction. |
| **FCR** | First Contact Resolution — The percentage of support inquiries resolved during the initial interaction without requiring escalation or follow-up. |
| **AHT** | Average Handle Time — The average duration of a support interaction from initiation to resolution. |
| **RBAC** | Role-Based Access Control — A method of restricting system access based on an individual's role within the organization. |
| **SSO** | Single Sign-On — An authentication scheme allowing users to log in with a single set of credentials across multiple systems. |
| **MFA** | Multi-Factor Authentication — An authentication method requiring two or more verification factors. |
| **AWS KMS** | Amazon Web Services Key Management Service — The encryption key management service used by Meridian. |
| **SageMaker** | AWS SageMaker — Machine learning platform used for model training and hosting. |
| **DPO** | Data Protection Officer — Dr. Klaus Weber, Meridian's appointed DPO based in Berlin. |
| **ISIRT** | Information Security Incident Response Team — Meridian's designated team for managing security incidents, led by the CISO. |
| **VPCO** | Vice President of Customer Operations — Michael Chang, owner of this SOP. |
| **VPFS** | Vice President of Financial Services — Robert Liu, approver of this SOP. |
| **CCO** | Chief Compliance Officer — Thomas Anderson. |
| **CISO** | Chief Information Security Officer — Rachel Kim. |

---

## 3. Roles and Responsibilities

The following RACI (Responsible, Accountable, Consulted, Informed) matrix defines the roles and responsibilities for TSP management lifecycle activities.

| Activity | VPCO | VPFS | CISO | CCO | Legal | TSP Manager | Quality Lead | Training Lead |
|---|---|---|---|---|---|---|---|---|
| **TSP Selection & Due Diligence** | A | R | C | C | C | R | I | I |
| **Contract Development & SOW Approval** | A | R | C | C | R | C | I | I |
| **Security Assessment** | I | I | A/R | C | C | C | I | I |
| **Access Provisioning** | I | I | A | I | I | R | I | I |
| **Role-Specific Training** | A | I | C | C | I | R | C | R |
| **Quality Monitoring (QA)** | I | I | I | C | I | I | A/R | I |
| **KPI Tracking & Reporting** | A | C | I | I | I | R | R | I |
| **Performance Review (QBR)** | C | C | C | C | C | A/R | C | C |
| **Incident Handling** | I | I | A/R | C | C | R | I | I |
| **Access Revocation** | I | I | A/R | I | I | R | I | I |
| **Contract Termination** | A | R | C | C | R | R | I | I |

### 3.1 Key Roles Defined

**Vice President of Customer Operations (Michael Chang)** — Serves as the executive owner of this SOP. Accountable for the overall performance of the TSP program and ensuring alignment with Customer Operations strategic objectives.

**Vice President of Financial Services (Robert Liu)** — Approver of this SOP. Responsible for TSP engagements supporting HealthPay Financial Services, including ensuring alignment with SR 11-7 model risk management requirements for any support providers interacting with credit scoring or lending model outputs.

**Chief Information Security Officer (Rachel Kim)** — Accountable for all security aspects of TSP engagements, including access control design, security assessments, and incident response oversight. Holds sole authority to approve or deny TSP access to Meridian systems.

**Chief Compliance Officer (Thomas Anderson)** — Consulted on regulatory compliance aspects of TSP engagements, including SOC 2 control alignment and healthcare compliance requirements.

**General Counsel (Maria Gonzalez)** — Responsible for legal review of all TSP contracts, NDAs, and data protection terms. Must approve all MSA and SOW documents prior to execution.

**TSP Relationship Manager** — A designated individual within Customer Operations responsible for day-to-day management of one or more TSP relationships. Manages onboarding, offboarding, performance monitoring, and serves as the primary escalation point.

**Quality Assurance Lead** — Responsible for designing and executing the quality monitoring program for TSP interactions, including call scoring, ticket review, and calibration sessions.

**Training Lead** — Responsible for developing, delivering, and tracking all role-specific training curricula for TSP personnel.

---

## 4. Policy Statements

### 4.1 General Principles

**Commitment to Quality:** Meridian is committed to ensuring that all support services, whether delivered by internal employees or TSPs, meet or exceed defined quality standards. TSPs are an extension of Meridian's Customer Operations team and are held to equivalent standards of professionalism, accuracy, and customer-centricity.

**Security and Confidentiality:** TSPs shall implement and maintain security controls commensurate with Meridian's internal standards. All TSP personnel with access to Meridian systems or data are bound by confidentiality obligations and must adhere to Meridian's Information Security policies.

**Regulatory Alignment:** TSP engagements shall be structured and managed to support Meridian's compliance obligations under SOC 2, HIPAA, and other applicable frameworks as specified in contractual agreements.

**Data Minimization:** TSP access to systems and data shall be limited to the minimum necessary to perform defined support functions.

**Continuous Improvement:** Meridian shall regularly assess TSP performance and drive continuous improvement through structured feedback, coaching, and performance management.

### 4.2 Prohibited Activities

TSP personnel are expressly prohibited from:

1. Accessing any Meridian system or data not explicitly authorized in their access profile.
2. Modifying, deleting, or exporting production data outside of approved ticketing or support workflows.
3. Using Meridian systems or data for any purpose other than providing contracted support services.
4. Sharing credentials, access tokens, or authentication materials with any other individual.
5. Circumventing any security control, including MFA, logging, or monitoring mechanisms.
6. Providing clinical advice, interpretations, or diagnostic opinions while supporting the Clinical AI Platform. Support interactions involving clinical products must be escalated to Meridian clinical personnel in accordance with Section 5.4.3.
7. Processing, storing, or transmitting Meridian data on personal devices or unauthorized systems.
8. Subcontracting any support function without prior written authorization from Meridian.

### 4.3 Policy Compliance

Violation of these policies by TSP personnel may result in immediate suspension of access, termination of the individual's assignment, and potential termination of the TSP agreement. Meridian reserves the right to pursue legal remedies for breaches of confidentiality or security.

---

## 5. Detailed Procedures

### 5.1 TSP Selection and Due Diligence

#### 5.1.1 Sourcing and Initial Screening

The process for identifying and screening potential TSPs shall follow these steps:

**Step 1: Requirements Definition**
The TSP Relationship Manager, in collaboration with the relevant product and operations stakeholders, shall document the business requirements for external support, including:
- Scope of services (tier, channels, hours of coverage)
- Language requirements
- Estimated interaction volumes
- Required technical competencies
- Any product-specific certifications needed

**Step 2: Market Scan and Longlist**
Procurement, in coordination with the TSP Relationship Manager, shall identify potential providers through:
- Industry analyst reports (e.g., Gartner, Forrester)
- Peer referrals and industry networks
- Existing Meridian-approved vendor lists
- RFI (Request for Information) responses

**Step 3: Initial Screening Questionnaire**
All prospective TSPs must complete the Meridian Third-Party Pre-Qualification Questionnaire (Template: TSP-Q-001), which assesses:
- Company profile, ownership, and financial stability
- Relevant experience in healthcare or fintech support
- Existing certifications (SOC 2, ISO 27001, HITRUST)
- Geographic presence and delivery locations
- Language capabilities
- Minimum operational maturity indicators

**Step 4: Shortlist Selection**
The TSP Relationship Manager and Procurement shall evaluate responses and select a shortlist of 3–5 providers for detailed evaluation.

#### 5.1.2 Detailed Evaluation

**Step 5: Capability Presentation**
Each shortlisted TSP shall deliver a capability presentation demonstrating:
- Relevant case studies and client references
- Proposed team structure and management model
- Training and quality assurance frameworks
- Technology and telephony infrastructure
- Business continuity and disaster recovery capabilities

**Step 6: Security Assessment**
The CISO's office shall conduct a security assessment of each shortlisted TSP prior to any data exchange or system access. The assessment includes:

| Assessment Area | Method | Evaluation Criteria |
|---|---|---|
| Information Security Policy | Documentation review | Existence of formal policy; alignment with ISO 27001 framework |
| Access Control | Documentation review and demonstration | Role-based access, least privilege principle, periodic access reviews |
| Encryption | Documentation review | Encryption at rest (AES-256 or equivalent) and in transit (TLS 1.2+); key management practices |
| Incident Response | Documentation review | Existence of formal incident response plan; documented procedures for detection, containment, and notification |
| Physical Security | Documentation review or site audit | Facility access controls, surveillance, environmental controls |
| Background Screening | Documentation review | Pre-employment screening practices for support personnel |
| Subcontractor Management | Documentation review | Processes for managing sub-tier suppliers |
| Network Security | Documentation review | Network segmentation, firewalls, intrusion detection/prevention |

The CISO shall document findings in the TSP Security Assessment Report (Template: TSP-SEC-002) and assign one of the following ratings:

- **Approved:** No material findings; TSP meets or exceeds Meridian security requirements.
- **Conditionally Approved:** Findings identified that require remediation within a defined timeframe; TSP may be provisioned limited access pending remediation.
- **Denied:** Material findings that preclude engagement.

**Step 7: Reference Checks**
The TSP Relationship Manager shall conduct reference checks with a minimum of three current or former clients of the TSP, with at least one reference in healthcare or financial services support.

**Step 8: Final Selection**
The evaluation committee, comprising the VPCO, CISO, Legal representative, and relevant product stakeholders, shall review all evaluation materials and select the preferred TSP. The VPFS must concur on selections supporting HealthPay.

### 5.2 Contracting and Onboarding

#### 5.2.1 Contractual Framework

**Step 9: Master Services Agreement Execution**
Prior to any service delivery, Legal shall execute an MSA with the selected TSP that includes:
- Scope of services and performance standards
- Data protection and confidentiality provisions
- Indemnification and liability terms
- Termination rights, including termination for convenience
- Insurance requirements (minimums: General Liability $5M, Professional Liability/E&O $10M, Cyber Liability $10M)
- Compliance with SOC 2 control requirements as applicable

**Step 10: Statement of Work**
The TSP Relationship Manager shall develop a SOW detailing:
- Specific services, deliverables, and acceptance criteria
- Service Level Agreements (SLAs) and Key Performance Indicators (KPIs)
- Pricing structure and payment terms
- Staffing plan and key personnel
- Transition and knowledge transfer plan
- Reporting requirements and cadence

**Step 11: Security Schedule**
The CISO shall ensure a Security Schedule or Data Protection Addendum is incorporated into the contract, specifying:
- Permitted data processing activities
- Technical and organizational security measures
- Incident notification timelines (within 4 hours of discovery for security incidents; within 24 hours for privacy incidents)
- Audit rights (Meridian retains the right to audit TSP controls, including through independent third-party auditors)

#### 5.2.2 Operational Onboarding

**Step 12: Access Provisioning**
Upon contract execution, the TSP Relationship Manager shall initiate access provisioning for TSP personnel. Access provisioning follows these principles:

- **Least Privilege:** TSP personnel shall be granted the minimum access necessary to perform their defined support functions.
- **Role-Based Access Control:** Access shall be assigned based on defined roles (e.g., Tier 1 Support Agent, Tier 2 Technical Specialist, Financial Services Support Agent) using RBAC groups configured in Meridian's identity management system.
- **Unique Identifiers:** Each TSP personnel shall be assigned a unique user ID. Shared or generic accounts are prohibited.
- **Multi-Factor Authentication:** MFA shall be enforced for all remote access to Meridian systems.
- **Single Sign-On:** TSP personnel shall authenticate via Meridian's SSO platform (Okta) for applicable applications.

The TSP Relationship Manager shall submit an Access Request Form (Template: TSP-ACC-003) for each TSP role, specifying required systems and permission levels. The CISO's office shall review and provision access within the following timelines:

| Access Type | Target Provisioning Time |
|---|---|
| Standard support tools (Zendesk, Jira, Confluence) | 3 business days |
| Financial services platform (HealthPay) | 5 business days |
| Clinical support systems (Clinical AI Platform — non-diagnostic) | 7 business days, requires additional clinical safety sign-off |
| Backend systems and databases | 10 business days, requires CISO direct approval |

**Step 13: Environment Setup**
IT shall provision TSP personnel with access to:
- Meridian's ticketing platform (Zendesk)
- Knowledge base and documentation (Confluence)
- Communication tools (Slack, Zoom) with restrictions on external file sharing
- Any product-specific support interfaces

**Step 14: Training Assignment**
The Training Lead shall assign role-specific training curricula as defined in Section 9.

**Step 15: Go-Live Certification**
Before a TSP personnel may begin handling live customer interactions, they must complete:
- All assigned training modules with a passing score of 85% or higher
- A minimum of 20 hours of shadowing experienced support personnel (internal or incumbent TSP)
- A go-live readiness assessment, including a quality calibration exercise scored at 90% or higher

The TSP Relationship Manager shall maintain a Go-Live Certification Record (Template: TSP-CERT-004) for each cohort.

### 5.3 Ongoing Operations

#### 5.3.1 Daily Operations

**Shift Management**
The TSP Relationship Manager or designee shall:
- Publish shift schedules at least two weeks in advance
- Monitor real-time adherence to schedules
- Coordinate with Workforce Management for intraday adjustments based on volume

**Escalation Management**
TSP personnel shall adhere to the Meridian Escalation Matrix (SOP-COPS-022) for all issues requiring Meridian involvement. The escalation matrix defines:

| Priority | Escalation Trigger | Escalation Target | Response Time |
|---|---|---|---|
| P1 — Critical | System outage or critical functionality unavailable affecting multiple customers | Meridian Incident Management (ISIRT if security-related) | Within 15 minutes |
| P2 — High | Major feature not functioning; workaround may exist; multiple users impacted | Product Operations Lead | Within 1 hour |
| P3 — Medium | Partial feature impairment; single user impacted | Tier 3 Engineering Queue | Within 4 business hours |
| P4 — Low | Minor issues; cosmetic defects; feature requests | Standard ticketing workflow | Within 1 business day |

**Clinical Escalation**
For inquiries related to the Clinical AI Platform, TSP personnel must follow the Clinical Support Escalation Protocol: Any question that could reasonably be interpreted as seeking clinical guidance, interpretation of AI-generated findings, or diagnostic support must be immediately escalated to Meridian's Clinical Support Team. TSP personnel shall use the template response: "This appears to be a clinical question that requires review by our clinical support team. I am transferring your inquiry now."

#### 5.3.2 Access Management

**Access Modifications**
Changes to TSP personnel access levels (e.g., role change, expanded scope) must follow the same Access Request process as initial provisioning. The TSP Relationship Manager shall review access appropriateness on a quarterly basis.

**Access Revocation**
Access must be revoked within 24 hours under the following circumstances:
- Termination of an individual TSP personnel's assignment
- Suspension or termination of the TSP agreement
- Security incident involving the TSP personnel
- Extended leave of absence exceeding 30 days

The TSP Relationship Manager shall submit an Access Revocation Request (Template: TSP-ACC-005) immediately upon awareness of a revocation trigger. IT shall confirm revocation within the specified timeframe.

### 5.4 Quality Assurance and Monitoring

#### 5.4.1 Quality Monitoring Program

The Quality Assurance Lead shall implement and maintain a monitoring program for TSP interactions.

**Sampling Methodology**

| Interaction Channel | Sample Size | Frequency |
|---|---|---|
| Phone (recorded) | 8 interactions per agent per month | Monthly |
| Email / Web Form | 12 tickets per agent per month | Monthly |
| Chat | 15 transcripts per agent per month | Monthly |
| Clinical AI Platform — Support | 100% review by Clinical QA Team | Continuous |

**Scoring Criteria**
Each sampled interaction shall be scored on a scale of 0–100 against a standardized evaluation form (Template: TSP-QA-006):

| Evaluation Category | Weight | Criteria |
|---|---|---|
| Accuracy | 30% | Correct resolution provided; accurate information delivered; appropriate knowledge base articles referenced |
| Compliance | 20% | Proper authentication; privacy notices delivered where required; no unauthorized disclosure of information |
| Professionalism | 15% | Courteous and empathetic communication; appropriate tone; professional language |
| Efficiency | 15% | Appropriate handle time; effective troubleshooting path; minimal unnecessary hold/transfer |
| Documentation | 15% | Complete and accurate ticket notes; correct categorization; proper disposition codes |
| Escalation Adherence | 5% | Correct escalation path followed when applicable; proper handoff documentation |

**Performance Thresholds**

| Metric | Target | Minimum Acceptable | Remediation Trigger |
|---|---|---|---|
| Average QA Score | ≥ 90% | ≥ 85% | Below 85% for two consecutive months |
| First Contact Resolution (FCR) | ≥ 75% | ≥ 70% | Below 70% for three consecutive months |
| Customer Satisfaction (CSAT) | ≥ 4.5/5 | ≥ 4.0/5 | Below 4.0 for three consecutive months |
| Average Handle Time (AHT) | Per-line targets (±15%) | ±25% of target | Exceeding ±25% for two consecutive months |

#### 5.4.2 Calibration

The QA Lead shall conduct monthly calibration sessions involving Meridian QA reviewers and TSP quality leads. During calibration sessions:
- A minimum of 10 interactions shall be independently scored by each participant.
- Inter-rater reliability shall be measured; a variance of >10 points on any interaction triggers discussion and re-alignment.
- Calibration session minutes and action items shall be documented.

#### 5.4.3 Coaching and Remediation

TSP personnel scoring below 85% on any individual evaluation shall receive documented coaching from the TSP's quality team within 5 business days. Personnel scoring below 85% for two consecutive months shall be placed on a Performance Improvement Plan (PIP) with weekly monitoring.

TSP personnel on a PIP who do not achieve 85% within 30 days shall be removed from Meridian support duties. The TSP Relationship Manager must approve any exceptions.

### 5.5 Contract Renewal and Termination

#### 5.5.1 Quarterly Business Review (QBR)

The TSP Relationship Manager shall conduct a formal QBR with each active TSP on a quarterly basis. The QBR agenda shall include:
- KPI performance review against SLA targets
- Quality scores and trends
- Customer satisfaction metrics and verbatim feedback
- Operational highlights and challenges
- Continuous improvement initiatives
- Security posture updates (any changes to security controls, personnel, or facilities)
- Forward-looking volume forecasts and staffing plans

The QBR shall be documented in a QBR Report (Template: TSP-QBR-007) and distributed to the VPCO, VPFS (for HealthPay TSPs), CISO, and CCO.

#### 5.5.2 Contract Renewal Decision

At least 90 days prior to contract expiration, the TSP Relationship Manager shall prepare a Contract Renewal Recommendation, evaluating:
- Aggregate performance over the contract term
- Trend analysis of KPIs
- Any security incidents or compliance findings
- Relationship health and strategic alignment
- Cost competitiveness against current market

The renewal recommendation shall be reviewed by the VPCO and VPFS and approved by Legal.

#### 5.5.3 Termination Procedure

Upon decision to terminate a TSP relationship, whether for cause or convenience, the following procedure shall be followed:

**Step 1: Notification**
The TSP Relationship Manager shall issue formal notice to the TSP in accordance with contractual notice periods. A termination communication plan shall be developed and executed.

**Step 2: Knowledge Transfer**
A comprehensive knowledge transfer plan shall be executed to ensure continuity of support. Open tickets, pending escalations, and in-progress projects shall be documented and transitioned to the successor support team.

**Step 3: Access Revocation**
All TSP personnel access to Meridian systems shall be revoked within 24 hours of the termination effective date, or immediately upon notice of termination for cause. The CISO shall verify completion of all access revocations.

**Step 4: Data Return or Destruction**
The TSP shall be instructed to return all Meridian data in its possession and to certify in writing the destruction of any Meridian data remaining on its systems, in accordance with contractual data disposition requirements.

**Step 5: Exit Interview**
The TSP Relationship Manager shall conduct a formal exit interview to document lessons learned and inform future TSP engagements.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control | Description | Applicable Systems |
|---|---|---|
| **Multi-Factor Authentication** | All TSP access to Meridian systems requires MFA via Okta Verify or YubiKey hardware tokens provided by Meridian. SMS-based MFA is prohibited. | All Meridian systems and applications |
| **Single Sign-On (SSO)** | TSP personnel authenticate through centralized SSO (Okta) with federated identity where technically feasible. | Zendesk, Jira, Confluence, Slack, Zoom, HealthPay Platform |
| **Role-Based Access Control** | Pre-defined RBAC groups map to TSP support functions. Access is provisioned to groups, not individuals. Group membership is reviewed quarterly by the system owner. | All systems |
| **Session Timeout** | Interactive sessions automatically terminate after 30 minutes of inactivity. Re-authentication required. | All web-based applications |
| **Conditional Access Policies** | Access restricted by IP range (TSP-approved facility IPs) and device compliance status. Access from non-approved locations requires explicit CISO approval and is time-limited. | Okta, VPN |
| **Full Session Recording** | All support sessions (including screen activity and keystrokes for privileged sessions) are recorded and retained for 12 months. | Zendesk, HealthPay Agent Console, AWS SageMaker (read-only sessions) |
| **DLP (Data Loss Prevention)** | Egress filtering prevents unauthorized exfiltration of data. Clipboard restrictions, print restrictions, and USB storage blocking enabled on Meridian-managed endpoints. File uploads restricted to approved ticketing workflows. | Meridian-managed workstations, VDI |
| **Encryption** | All data in transit encrypted via TLS 1.2+. All data at rest encrypted using AES-256 via AWS KMS. | All platforms and data stores |

### 6.2 Administrative Controls

| Control | Description | Frequency |
|---|---|---|
| **Background Checks** | TSP must confirm completion of criminal background checks, employment verification, and education verification for all personnel assigned to Meridian accounts. Meridian retains right to audit background check records. | Prior to assignment; refreshed every 24 months |
| **Confidentiality Agreements** | All TSP personnel must execute individual confidentiality agreements (NDAs) prior to accessing Meridian systems or data. | Prior to access |
| **Acceptable Use Policy Acknowledgment** | TSP personnel must acknowledge and agree to Meridian's Acceptable Use Policy (SOP-IS-012) and Information Security Policy (SOP-IS-001). | Prior to access; re-acknowledged annually |
| **Security Awareness Training** | TSP personnel must complete Meridian's Security Awareness Training curriculum (see Section 9). | Prior to access; annually thereafter |
| **Change Management** | Changes to TSP access permissions, system configurations impacting TSP operations, or TSP management processes require documented change requests approved per SOP-IT-008. | As needed |

### 6.3 Physical Security

For TSP personnel performing on-site support at Meridian facilities:
- Badge access required; badges issued by Meridian Facilities upon verification of identity
- Escort required for visitors to restricted areas (data centers, network rooms, executive areas)
- Clean desk policy enforced for all workstations

For TSP facilities where Meridian data is accessed:
- TSP must maintain facility access controls including badge access, visitor logs, and surveillance (CCTV) for areas where Meridian work is performed
- Workstations must be positioned to prevent unauthorized viewing of screens
- Clean desk policy enforced

### 6.4 Incident Response

#### 6.4.1 TSP Incident Notification Requirements

TSPs shall notify Meridian's Information Security Incident Response Team (ISIRT) of any actual or suspected security incident within the following timeframes:

| Incident Severity | Notification Requirement | Method |
|---|---|---|
| Critical — Confirmed data breach involving Meridian data | Within 1 hour of discovery | Phone call to ISIRT hotline + email to security@meridian.com |
| High — Suspected unauthorized access; malware infection affecting Meridian systems | Within 4 hours of discovery | Email to security@meridian.com |
| Medium — Policy violation; lost/stolen device without data exposure | Within 24 hours | Email to TSP Relationship Manager |

#### 6.4.2 Meridian ISIRT Response

Upon notification, ISIRT shall:
1. Acknowledge receipt and assign incident coordinator within 1 hour (Critical) or 4 hours (High).
2. Convene incident response bridge including TSP security point of contact.
3. Initiate containment, investigation, and evidence preservation.
4. Develop communications plan, including regulatory notification determinations.
5. Coordinate remediation and root cause analysis.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators

The following KPIs shall be tracked for all TSP engagements, with defined targets established per engagement in the relevant SOW:

| KPI Category | Metric | Definition | Reporting Frequency |
|---|---|---|---|
| **Quality** | QA Score | Average score across all monitored interactions | Monthly |
| **Quality** | Critical Error Rate | Percentage of interactions with errors that could result in patient harm, financial loss, or regulatory violation | Monthly (target: 0%) |
| **Effectiveness** | First Contact Resolution (FCR) | Percentage of inquiries resolved without escalation or callback | Monthly |
| **Effectiveness** | Escalation Rate | Percentage of inquiries escalated to Tier 2 or Tier 3 | Monthly |
| **Customer Experience** | CSAT | Post-interaction survey average (1–5 scale) | Monthly |
| **Customer Experience** | Net Promoter Score (NPS) | Derived from post-interaction survey | Quarterly |
| **Efficiency** | Average Handle Time (AHT) | Average duration of interaction including after-call work | Monthly |
| **Efficiency** | Average Speed to Answer (ASA) | Average time to answer for phone inquiries | Monthly |
| **Service Level** | Service Level (SL) | Percentage of calls answered within defined threshold (e.g., 80% in 60 seconds) | Weekly |
| **Service Level** | Abandonment Rate | Percentage of callers hanging up before answer | Weekly |
| **Compliance** | Authentication Compliance | Percentage of interactions with proper caller authentication per procedure | Monthly (target: 100%) |
| **Compliance** | Security Incidents | Count of security incidents attributable to TSP | Monthly |

### 7.2 Dashboards and Reporting

**Daily Operational Dashboard:**
Automated real-time dashboard (powered by Tableau, sourced from Zendesk Explore and telephony platform) displaying:
- Current queue volumes and wait times
- Agent availability and adherence
- Incoming volume trend vs. forecast

**Weekly Performance Summary:**
The TSP Relationship Manager shall distribute a Weekly TSP Performance Summary to the VPCO, relevant Product Operations leads, and QA Lead, including:
- Weekly KPI performance vs. targets
- Notable escalation events
- Staffing updates
- Upcoming risks or changes

**Monthly Governance Review:**
A formal monthly review between the TSP Relationship Manager and TSP service delivery manager covering:
- All KPIs for the month
- Quality trends and coaching outcomes
- Incident reviews (if any)
- Continuous improvement action item status
- Forecast review for the upcoming 90 days

**Quarterly Business Review:**
As defined in Section 5.5.1, a formal QBR documented and distributed to senior leadership.

### 7.3 Audit Logging

All TSP personnel activity within Meridian systems shall be logged with the following minimum data elements:
- User ID (unique identifier)
- Timestamp (UTC)
- Action performed (view, create, modify, delete, export)
- Object accessed (ticket ID, customer record ID, system component)
- Source IP address
- Session ID

Logs shall be retained for a minimum of 12 months and be available for review by the CISO, Internal Audit, or authorized compliance personnel. Log integrity controls (immutable storage, cryptographic verification) shall be applied.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Requests

Any deviation from the procedures or requirements defined in this SOP must be documented and approved through the formal exception process. Exceptions may be requested for:
- Temporary access outside standard provisioning (e.g., emergency coverage)
- Deviation from standard QA sampling rates due to volume anomalies
- Temporary staffing adjustments due to unforeseen circumstances
- Use of non-standard tools or communication channels
- Any other deviation from prescribed procedures

### 8.2 Exception Approval Authority

| Exception Type | Approver | Maximum Duration | Documentation Required |
|---|---|---|---|
| Access-related exceptions | CISO | 30 days (renewable once) | Exception Request Form with justification |
| Quality process deviation | QA Lead + TSP Relationship Manager | 60 days | Documented in QA program records |
| Staffing or coverage exception | VPCO | 90 days | Exception Request with impact assessment |
| Tooling or channel exception | CISO + VPCO | 30 days | Security review + Exception Request |
| Policy deviation (any other) | VPCO | Case-by-case | Exception Request Form with justification |

### 8.3 Exception Request Process

1. Requester completes the Exception Request Form, documenting:
   - Specific policy or procedure provision being excepted
   - Business justification for exception
   - Risk assessment and compensating controls
   - Duration of exception
   - Impacted systems, data, and stakeholders

2. The TSP Relationship Manager reviews the request for completeness and operational impact.

3. Request is routed to the designated approver per Section 8.2.

4. Approver may approve, deny, or approve with conditions. All conditions must be documented.

5. Approved exceptions are logged in the Exception Register (maintained by the TSP Relationship Manager) with a unique exception ID.

6. All active exceptions shall be reviewed monthly by the TSP Relationship Manager. Expired exceptions must be formally closed (return to standard procedure) or re-submitted for renewal.

### 8.4 Escalation of TSP Performance Issues

Performance issues that are not resolved through standard coaching and performance management shall be escalated as follows:

| Escalation Level | Trigger | Escalation Target | Response Time |
|---|---|---|---|
| Level 1 | Individual agent below threshold for 2 months | TSP Service Delivery Manager | 5 business days for remediation plan |
| Level 2 | Team-level KPI misses for 2 consecutive months | VPCO + TSP Account Executive | 10 business days for corrective action plan |
| Level 3 | Persistent systemic issues; security incident | VPCO, VPFS (if applicable), CISO, Legal | Immediate escalation; formal performance review meeting within 5 business days |

### 8.5 Dispute Resolution

Disagreements regarding TSP performance assessments, quality scoring, or compliance findings shall be escalated to the VPCO for adjudication. The VPCO may consult with the CISO, CCO, or Legal as appropriate. The VPCO's determination is final for operational matters; contractual disputes shall be managed per the dispute resolution provisions of the MSA.

---

## 9. Training Requirements

### 9.1 Training Curriculum

All TSP personnel assigned to Meridian support functions must complete the following training curriculum prior to handling live customer interactions:

| Module ID | Module Name | Description | Duration | Passing Score |
|---|---|---|---|---|
| **TSP-SEC-101** | Security and Confidentiality | Information security fundamentals; PHI/PII handling; password policies; clean desk; reporting suspicious activity | 2 hours | 90% |
| **TSP-PROD-XXX** | Product-Specific Training | Product-specific functional training (curriculum varies by support assignment; HealthPay modules include SR 11-7 awareness content) | 20–40 hours (varies) | 85% |
| **TSP-QA-101** | Quality Standards and Procedures | Overview of QA program; scoring criteria; what constitutes a critical error; documentation standards | 1.5 hours | 85% |
| **TSP-OPS-101** | Operational Procedures | Ticketing workflow; escalation procedures; shift management; outage communication protocols | 2 hours | 85% |
| **TSP-COMP-101** | Compliance Awareness | Privacy and data protection obligations; anti-bribery and corruption; code of conduct | 1 hour | 85% |
| **TSP-CLIN-101** | Clinical Support Boundaries (Clinical AI Platform only) | Clinical escalation protocols; prohibited activities; recognizing clinical inquiry red flags | 1.5 hours | 90% |

### 9.2 Ongoing Training Requirements

| Requirement | Frequency | Description |
|---|---|---|
| Security Refresher Training | Annually | Updated security awareness content and phishing simulation |
| Product Update Training | As released (minimum quarterly) | Delta training on new features, changes, and known issues |
| Quality Calibration Participation | Monthly (for QA-designated personnel) | Participation in monthly calibration sessions |
| Remedial Training | As triggered | Targeted training assigned based on quality monitoring findings or performance issues |

### 9.3 Training Tracking and Compliance

The Training Lead shall maintain training records for all TSP personnel in Meridian's Learning Management System (LMS) or equivalent tracking mechanism. Records shall include:
- Personnel name and unique identifier
- TSP organization
- Assigned curriculum
- Module completion dates
- Assessment scores
- Expiration dates for time-limited certifications

**Compliance Reporting:**
The Training Lead shall generate a monthly Training Compliance Report for the TSP Relationship Manager, showing:
- Overall training completion rates (target: 100%)
- Overdue training items
- New hire training pipeline status

TSP personnel with overdue training requirements shall be restricted from handling live customer interactions until training is completed.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| Policy Reference | Title | Relationship |
|---|---|---|
| SOP-IS-001 | Information Security Policy | Overarching security requirements applicable to TSPs |
| SOP-IS-012 | Acceptable Use Policy | Defines acceptable use of Meridian systems by all users |
| SOP-IS-008 | Access Control Policy | Defines access provisioning, review, and revocation standards |
| SOP-IS-014 | Incident Response Policy | Defines ISIRT procedures and notification requirements |
| SOP-COPS-022 | Escalation Management Policy | Defines standard escalation paths and response times |
| SOP-HR-042 | Contractor and Temporary Worker Management | Governs individual contractor (non-TSP) engagements |
| SOP-IT-076 | Managed Service Provider Governance | Governs infrastructure MSP engagements |
| SOP-IT-008 | Change Management Policy | Governs system and configuration changes |
| SOP-LEG-004 | Third-Party Contract Review Process | Legal review requirements for vendor contracts |

### 10.2 External Standards and Frameworks

| Standard | Relationship |
|---|---|
| AICPA Trust Services Criteria (SOC 2) | Control framework for security, availability, and confidentiality |
| ISO 27001:2022 | Reference framework for TSP security assessments |
| NIST SP 800-53 Rev. 5 | Reference control catalog for technical safeguards |

### 10.3 Templates and Forms

| Template ID | Document Name | Location |
|---|---|---|
| TSP-Q-001 | Third-Party Pre-Qualification Questionnaire | Meridian Procurement Portal |
| TSP-SEC-002 | TSP Security Assessment Report | CISO SharePoint |
| TSP-ACC-003 | Access Request Form — TSP Personnel | ServiceNow Catalog |
| TSP-CERT-004 | Go-Live Certification Record | Customer Operations SharePoint |
| TSP-ACC-005 | Access Revocation Request | ServiceNow Catalog |
| TSP-QA-006 | Quality Evaluation Form | QA Platform (Playvox) |
| TSP-QBR-007 | Quarterly Business Review Report Template | Customer Operations SharePoint |
| TSP-EXC-008 | Exception Request Form | Customer Operations SharePoint |

---

## 11. Revision History

| Version | Date | Author | Description of Changes |
|---|---|---|---|
| 1.0 | 2021-03-15 | Sarah Chen, Director of Support Operations | Initial publication. Established foundation for TSP management covering HealthPay and SaaS platform support only. |
| 2.0 | 2021-11-08 | Sarah Chen, Director of Support Operations | Added Clinical AI Platform support provisions following CE marking approval. Expanded security assessment criteria. Incorporated lessons learned from initial TSP engagements. |
| 3.0 | 2022-07-22 | James Okonkwo, TSP Program Manager | Comprehensive revision. Added detailed QBR procedure, expanded training curriculum, introduced formal exception handling process. Aligned with new Zendesk implementation and updated telephony platform. |
| 4.0 | 2023-03-10 | James Okonkwo, TSP Program Manager | Updated to reflect expanded EU operations. Added multilingual support requirements. Revised incident notification timeframes. Updated QA scoring weights to increase compliance emphasis. |
| 5.0 | 2024-01-19 | Patricia Mueller, Sr. Manager, Vendor Operations | Major revision. Restructured RACI matrix. Added detailed access provisioning timelines and role definitions. Expanded Section 5 procedures with step-level detail. Updated all template references. Incorporated HealthPay-specific provisions per VPFS requirements. |
| 5.1 | 2024-04-15 | Patricia Mueller, Sr. Manager, Vendor Operations | Interim update: Revised QA sampling methodology for chat interactions from 10 to 15 per agent per month. Added session recording retention period (12 months). Updated CISO assessment rating categories. |
| 5.2 | 2024-05-08 | Patricia Mueller, Sr. Manager, Vendor Operations | Interim update: Corrected cross-reference to SOP-COPS-022 (was SOP-OPS-091). Updated exception approval authority table. Added Clinical AI Platform 100% QA review requirement. |
| 5.3 | 2024-06-20 | Patricia Mueller, Sr. Manager, Vendor Operations | Aligned access provisioning timelines with new Okta workflow implementation. Added prohibited activity #6 (clinical advice prohibition). Updated data disposition procedure in termination section. |
| 5.4 | 2024-07-15 | Patricia Mueller, Sr. Manager, Vendor Operations | Incorporated feedback from Internal Audit regarding documentation of calibration sessions. Added logging requirements (Section 7.3). Updated MFA requirements to prohibit SMS-based MFA. |
| 5.5 | 2024-07-28 | Patricia Mueller, Sr. Manager, Vendor Operations | Approved version. Updated effective date. Incorporated final Legal review feedback on termination data disposition language. Updated approver from interim to permanent VPFS (Robert Liu). Added cross-reference to SOP-LEG-004. |
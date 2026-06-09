---
sop_id: "SOP-LEGC-016"
title: "Vendor Compliance Assessment"
business_unit: "Legal & Compliance"
version: "1.8"
effective_date: "2025-11-19"
last_reviewed: "2026-07-20"
next_review: "2027-01-16"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Vendor Compliance Assessment

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the framework, methodology, and operational processes for assessing, tiering, monitoring, and managing compliance risk across all third-party vendors, suppliers, and service providers engaged by Meridian Health Technologies, Inc. (“Meridian”). The purpose of this SOP is to ensure that all vendor relationships that involve the access, processing, transmission, or storage of Meridian’s sensitive data—including Protected Health Information (PHI), personally identifiable information (PII), financial data, and proprietary algorithms—meet Meridian’s security, privacy, and regulatory compliance requirements throughout the full vendor lifecycle.

This SOP is designed to operationalize Meridian’s commitment to protecting patient data, maintaining the integrity of clinical AI systems, and ensuring the continuous availability of financial services platforms by extending the company’s control environment to its extended enterprise.

### 1.2 Scope

**In-Scope Vendor Relationships:**

This SOP applies to all third-party entities that provide products, services, or intellectual property to any business unit of Meridian Health Technologies, including but not limited to:

- **Clinical AI Platform Vendors:** Providers of training data, annotation services, model validation tools, LLM APIs, clinical content, and algorithm development partners.
- **HealthPay Financial Services Vendors:** Payment processors, credit bureaus, collections agencies, banking partners, lending-as-a-service platforms, and fraud detection services.
- **MedInsight Analytics Vendors:** Data aggregators, data brokers, analytics tooling providers, and population health data sources.
- **Meridian SaaS Platform Vendors:** Cloud infrastructure providers (AWS, Azure), SaaS tooling vendors, observability platforms, identity providers, and managed security service providers.
- **Corporate Services Vendors:** HR platforms, payroll processors, benefits administrators, legal services, consulting firms, and any other vendor receiving Meridian data.

**Data Classifications Covered:**

- **Regulated Data:** Protected Health Information (PHI) as defined under HIPAA; personal data of EU data subjects as defined under applicable regulations.
- **Sensitive Data:** Personally Identifiable Information (PII), financial account information, payment card data, proprietary algorithms, source code, clinical models, and patient risk scores.
- **Confidential Data:** Internal business documents, strategic plans, employee records, and security configuration data.
- **Public Data:** Approved marketing materials, public-facing documentation.

**Geographic Scope:**

This SOP applies globally to all Meridian offices (Boston HQ, London, Berlin, Singapore, Toronto) and all vendor engagements regardless of the vendor’s geographic location. Business Unit leads and Legal & Compliance must ensure that vendor assessments account for jurisdiction-specific requirements where applicable.

**Out of Scope:**

- Temporary staff and independent contractors engaged through Meridian’s HR department (these are assessed via SOP-HR-004, Workforce Screening and Onboarding).
- Open-source software libraries consumed without a direct vendor relationship (governed by SOP-ENG-012, Open Source Software Management).

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|----------------|------------|
| **BAA** | Business Associate Agreement. A legally binding contract required by HIPAA between a covered entity and a business associate that creates, receives, maintains, or transmits PHI on behalf of the covered entity. |
| **Business Associate** | As defined at 45 CFR § 160.103, a person or entity that performs functions or activities on behalf of, or provides services to, a covered entity that involve the use or disclosure of PHI. |
| **CISO** | Chief Information Security Officer (Rachel Kim). |
| **CPO/DPO** | Chief Privacy Officer / Data Protection Officer (Dr. Klaus Weber). |
| **Covered Entity** | Meridian Health Technologies, Inc., as a healthcare provider and health plan services provider under HIPAA. |
| **Critical Vendor** | A vendor whose service disruption would cause material impact to patient safety, clinical operations, financial operations, or regulatory compliance. All Critical Vendors are Tier 1. |
| **CRO** | Chief Risk Officer (vacant; duties shared between CISO and Chief Compliance Officer). |
| **Data Protection Impact Assessment (DPIA)** | A risk assessment required for high-risk processing activities under certain international regulations. |
| **EU AI Act** | Regulation (EU) 2024/1689 laying down harmonized rules on artificial intelligence. |
| **HIPAA** | Health Insurance Portability and Accountability Act of 1996, including the Privacy Rule (45 CFR Part 160 and Subparts A and E of Part 164) and the Security Rule (45 CFR Part 160 and Subparts A and C of Part 164). |
| **HITECH** | Health Information Technology for Economic and Clinical Health Act, part of the American Recovery and Reinvestment Act of 2009, which strengthened HIPAA enforcement. |
| **Inherent Risk** | The level of risk posed by a vendor engagement before considering any mitigating controls. |
| **NIST AI RMF** | National Institute of Standards and Technology Artificial Intelligence Risk Management Framework (NIST AI 100-1). |
| **PHI** | Protected Health Information, as defined at 45 CFR § 160.103, meaning individually identifiable health information held or transmitted in any form or medium. |
| **Residual Risk** | The level of risk remaining after controls and mitigation strategies are applied. |
| **Security Incident** | As defined at 45 CFR § 164.304, the attempted or successful unauthorized access, use, disclosure, modification, or destruction of information or interference with system operations in an information system. |
| **SR 11-7** | Federal Reserve Board Supervision and Regulation Letter 11-7, “Guidance on Model Risk Management.” |
| **Standard Vendor** | A vendor that does not meet the definition of a Critical Vendor and poses lower inherent risk (Tier 2 or Tier 3). |
| **Subcontractor** | A downstream entity engaged by a Meridian vendor to assist in fulfilling the vendor’s obligations to Meridian. |
| **Vendor Compliance Assessment (VCA)** | The formal review process defined in this SOP to evaluate a vendor's security, privacy, and regulatory compliance posture. |
| **Vendor Risk Tier** | The classification assigned to a vendor (Tier 1, Tier 2, or Tier 3) based on the inherent risk of the engagement. |

---

## 3. Roles and Responsibilities

The following RACI matrix defines the roles and responsibilities for the Vendor Compliance Assessment lifecycle.

**Responsible (R) =** Performs the work
**Accountable (A) =** Ultimately answerable for completion and approval
**Consulted (C) =** Provides input and subject matter expertise
**Informed (I) =** Kept up to date on progress and decisions

| Role / Individual | Vendor Identification & Intake | Risk Tiering | Initial VCA | Contract Review & BAA | Ongoing Monitoring | Remediation Management | Offboarding |
|---|---|---|---|---|---|---|---|
| **Business Unit Owner** (e.g., VP Clinical AI, VP Financial Services) | R, A | C | C | C | I | R | R, A |
| **Chief Compliance Officer** (Thomas Anderson) | I | A | A | A | A | A | I |
| **CISO** (Rachel Kim) | I | C | R, A (Security Assessment) | C | R | C | C |
| **CPO/DPO** (Dr. Klaus Weber) | I | C | R (Privacy Assessment) | R | C | C | C |
| **General Counsel** (Maria Gonzalez) | I | I | I | A | I | I | A (Termination) |
| **VP IT Operations** (Samantha Torres) | I | C | R (Technical Review) | C | R | R | R |
| **VP of Engineering** (David Park) | C | C | C | I | I | I | I |
| **Chief AI Officer** (Dr. Marcus Rivera) | C (for AI vendors) | C | R (AI Model Risk) | C | C | C | C |
| **Privacy Team** (reporting to CPO/DPO) | I | C | R | R | R | C | C |
| **Compliance Team** (reporting to CCO) | I | R | R | C | R | R | C |
| **Procurement** (Finance) | R | I | I | R (Commercial Terms) | I | I | R |
| **Vendor** (External) | I | I | C | C | I | R | I |

### 3.1 Specific Named Role Responsibilities

**Thomas Anderson, Chief Compliance Officer:**
- Serves as the executive owner of this SOP.
- Approves the overall vendor risk tiering methodology annually.
- Approves all Tier 1 vendor engagements and any exceptions to this SOP.
- Reports quarterly to the Board AI Governance Committee on vendor risk posture.
- Escalates material vendor non-compliance to the CEO and General Counsel.

**Rachel Kim, Chief Information Security Officer:**
- Owns the security domain of the Vendor Compliance Assessment questionnaire and evidence review.
- Approves the security assessment portion of all Tier 1 vendor VCAs.
- Monitors vendor security incidents in conjunction with the SOC (via CrowdStrike and Datadog integrations where applicable).
- Validates vendor security certifications (SOC 2, ISO 27001, HITRUST, etc.).

**Dr. Klaus Weber, Chief Privacy Officer / DPO:**
- Owns the privacy domain of the Vendor Compliance Assessment.
- Ensures all vendor engagements processing PHI or EU personal data have appropriate contractual protections (including BAAs).
- Approves vendor data flow diagrams and data mapping documents.
- Serves as the point of contact for regulatory inquiries related to vendor data processing.

**Business Unit Owners (VP-level designees):**
- Dr. Aisha Okafor (VP Clinical AI Products): Responsible for all vendors supporting Clinical AI Platform.
- Robert Liu (VP Financial Services): Responsible for all vendors supporting HealthPay Financial Services.
- Michael Chang (VP Customer Operations): Responsible for vendors supporting MedInsight Analytics and customer-facing operations.
- Samantha Torres (VP IT Operations): Responsible for SaaS infrastructure and IT tooling vendors.
- Business Unit Owners are responsible for identifying vendors, initiating the VCA process, and managing remediation activities for vendors within their portfolio.

---

## 4. Policy Statements

Meridian Health Technologies is committed to maintaining a vendor ecosystem that upholds the highest standards of security, privacy, and regulatory compliance. The following high-level policy statements govern all vendor relationships:

**PS-01: Mandatory Assessment.** No vendor shall be engaged, and no data shall be shared with any third party, until a Vendor Compliance Assessment (VCA) has been completed and approved commensurate with the vendor's risk tier. This applies to new engagements and material changes to existing engagements.

**PS-02: Risk-Based Tiering.** All vendors shall be assigned a risk tier (Tier 1, Tier 2, or Tier 3) based on a standardized inherent risk scoring methodology. The assessment rigor, frequency of monitoring, and approval authority shall escalate with each tier.

**PS-03: HIPAA Data Protection.** Any vendor that creates, receives, maintains, or transmits PHI on behalf of Meridian shall be classified as a Business Associate under HIPAA. Meridian shall execute a Business Associate Agreement (BAA) with such vendors prior to any disclosure of PHI. The BAA shall, at minimum, comply with the requirements of 45 CFR § 164.504(e) and include obligations for the vendor to: (a) implement administrative, physical, and technical safeguards that reasonably and appropriately protect the confidentiality, integrity, and availability of the electronic PHI it creates, receives, maintains, or transmits on behalf of Meridian, as required by 45 CFR Part 164, Subpart C; (b) ensure that any subcontractors that create, receive, maintain, or transmit electronic PHI on behalf of the vendor agree to the same restrictions and conditions; (c) report to Meridian any security incident involving PHI, including breaches of unsecured PHI as defined by 45 CFR § 164.402, within 24 hours of confirmed discovery; (d) make available PHI for access, amendment, and accounting of disclosures as required by 45 CFR §§ 164.524, 164.526, and 164.528.

**PS-04: AI Vendor Governance.** Vendors providing AI models, training data, or algorithmic services that integrate with or influence Meridian’s Clinical AI Platform (classified as high-risk under EU AI Act Annex III) shall undergo enhanced AI-specific assessment aligned with NIST AI RMF. The Chief AI Officer shall review all such engagements for model risk, bias, and transparency obligations.

**PS-05: Financial Services Model Risk.** Vendors providing models, algorithms, or scoring systems used in HealthPay credit decisions, fraud detection, or underwriting shall comply with SR 11-7 model risk management standards. The Chief AI Officer and VP Financial Services shall jointly approve such engagements.

**PS-06: Continuous Monitoring.** Vendor compliance is not a point-in-time assessment. All Tier 1 vendors shall be subject to continuous monitoring via security ratings platforms (e.g., BitSight), automated certificate validation, and annual re-assessments. Tier 2 vendors shall undergo biennial re-assessments. Tier 3 vendors shall be re-assessed triennially or upon trigger events.

**PS-07: Right to Audit.** All contracts with Tier 1 and Tier 2 vendors shall include a right for Meridian (or a qualified assessor appointed by Meridian) to audit the vendor’s compliance with security, privacy, and regulatory requirements. For Tier 1 vendors, Meridian shall exercise this right at least biennially, either through on-site assessment, virtual audit, or review of the vendor's independent audit reports (e.g., SOC 2 Type II, ISO 27001 certification, HITRUST CSF assessment).

**PS-08: Subcontractor Accountability.** Vendors shall not subcontract any material portion of the services provided to Meridian—especially any services involving access to PHI—without Meridian’s prior written consent. The Vendor shall flow down all Meridian security and privacy obligations to approved subcontractors via written agreement and shall remain fully liable for subcontractor performance.

**PS-09: Data Localization and Residency.** Vendors processing data originating from the EU shall maintain data storage and processing within the European Economic Area (EEA) or a jurisdiction recognized as providing adequate protection by the European Commission, unless Meridian has specifically approved an alternative arrangement and documented appropriate safeguards.

**PS-10: Termination and Offboarding.** Upon termination or expiration of a vendor relationship, the vendor shall, at Meridian’s direction, return or securely destroy all Meridian data in its possession, including PHI, within 30 calendar days. The vendor shall provide a certificate of destruction to Meridian’s Privacy Team. The VP of IT Operations shall verify the revocation of all logical and physical access credentials.

---

## 5. Detailed Procedures

This section describes the operational procedures for the end-to-end vendor compliance assessment lifecycle. The Business Unit Owner is responsible for initiating the process by submitting a Vendor Intake Request via the Meridian ServiceNow Vendor Management Module (ServiceNow VMM).

### 5.1 Vendor Identification and Intake

**Step 1: Submission of Vendor Intake Request**

The Business Unit Owner (or their delegate) shall submit a Vendor Intake Request in ServiceNow VMM at least 45 calendar days prior to the anticipated engagement start date. The request shall include:

| Field | Description |
|-------|-------------|
| Vendor Legal Name | Full registered legal name and DBA if applicable |
| Vendor HQ Address | Physical headquarters location |
| Vendor Website | Primary corporate domain |
| Service Description | Detailed description of services/products to be provided |
| Data Interaction Summary | What categories of Meridian data will be accessed, processed, stored, or transmitted? |
| Data Flow Description | High-level description of how data will flow between Meridian and the vendor |
| Estimated Contract Value | Annual spend estimate (USD) |
| Business Unit Sponsor | Name and title of VP-level sponsor |
| Engagement Type | New Vendor / Renewal / Expansion of Services |
| Criticality to Operations | Is this service essential to patient safety, clinical operations, or financial settlement? (Y/N) |
| EU Data Subjects | Will the vendor process personal data of EU data subjects? (Y/N) |

**Step 2: Intake Validation**

Within 3 business days of submission, the Compliance Team shall validate the intake request for completeness. Incomplete requests shall be returned to the Business Unit Owner with specific requests for additional information. Complete requests shall be assigned a Vendor Assessment ID (VA-YYYY-NNNN) and routed to the Risk Tiering stage.

### 5.2 Vendor Risk Tiering

The Vendor Risk Tiering process assigns every vendor to one of three risk tiers based on the inherent risk of the engagement. The inherent risk score is calculated based on weighted criteria.

**Tiering Criteria and Scoring Matrix:**

| Criterion | Option | Score |
|-----------|--------|-------|
| **Data Classification** (Select highest) | PHI | 40 |
| | PII / Financial Data / Payment Card Data | 30 |
| | Confidential (internal business, source code, algorithms) | 20 |
| | Public only | 5 |
| **EU Data Processing** | Yes | 15 |
| | No | 0 |
| **Operational Criticality** | Critical (vendor failure impacts patient safety or financial settlement—$1M+/day) | 25 |
| | High (significant disruption to clinical or business operations) | 15 |
| | Moderate (limited impact, workarounds available) | 10 |
| | Low (easily replaced, minimal impact) | 5 |
| **Access Model** | Persistent network connection or API integration with production systems | 20 |
| | Data uploaded/manually transmitted to vendor | 10 |
| | Vendor has no access to Meridian systems (receive-only) | 5 |
| **AI / Model Involvement** | Vendor provides AI models used in high-risk clinical or credit decisions | 15 |
| | Vendor provides non-clinical AI/automation tools | 5 |
| | No AI component | 0 |

**Tier Assignment Thresholds:**

| Tier | Score Range | Classification | Default Re-Assessment Cadence |
|------|-------------|----------------|-------------------------------|
| **Tier 1 – Critical** | 65–115 | High inherent risk | Annually |
| **Tier 2 – Standard** | 30–64 | Moderate inherent risk | Biennially (every 2 years) |
| **Tier 3 – Low Risk** | 0–29 | Low inherent risk | Triennially (every 3 years) or upon trigger |

The Compliance Team performs the initial tiering within 5 business days of intake validation. The Chief Compliance Officer reviews and approves Tier 1 classifications. Any disputes regarding tiering are escalated to the General Counsel for final determination.

**Trigger Event Re-Assessment:** A vendor’s tier shall be re-assessed immediately upon the occurrence of any of the following trigger events:
- Change in services provided by the vendor that affects data classification, access model, or operational criticality.
- A confirmed security incident or data breach at the vendor involving Meridian data.
- Regulatory enforcement action or litigation involving the vendor that is materially relevant to the services provided.
- Change in the regulatory landscape that affects the risk profile of the vendor engagement.
- Merger, acquisition, or change of control of the vendor.

### 5.3 Initial Vendor Compliance Assessment (VCA)

The Initial VCA is the core due diligence process. The depth of assessment varies by risk tier.

#### 5.3.1 VCA Workflow by Tier

| Activity | Tier 1 | Tier 2 | Tier 3 |
|----------|--------|--------|--------|
| Security Questionnaire | Full (SIG Lite or CAIQ v4) | Abbreviated Meridian Questionnaire | Abbreviated Meridian Questionnaire |
| Privacy Questionnaire | Full Meridian Privacy Questionnaire | Standard Meridian Privacy Questionnaire | N/A (self-attestation) |
| AI/Model Risk Assessment | Required if AI vendor (NIST AI RMF) | N/A | N/A |
| Financial Viability Check | Yes (D&B report) | Yes (credit check) | No |
| BAA Required? | Yes, if PHI involved | Yes, if PHI involved | Yes, if PHI involved |
| Audit Report Review | Required (SOC 2 Type II, ISO 27001, or HITRUST) | Requested; reviewed if available | Not required |
| On-Site Assessment | Biennially | At discretion of CISO | No |
| Independent Penetration Test | Reviewed if available | N/A | N/A |
| Subcontractor Review | Yes – full mapping | Yes – list required | No |
| DPIA Required? | Refer to Section 5.4.1 | Refer to Section 5.4.1 | No |

**Step 1: Questionnaire Distribution**

The Compliance Team sends the appropriate questionnaire package to the vendor’s designated compliance or security contact via the ServiceNow VMM portal. Vendors are given 15 business days to complete and return questionnaires.

**Step 2: Questionnaire Review and Scoring**

Upon receipt, the following teams review responses in parallel within 10 business days:

- **CISO (Security Review):** Reviews security controls, encryption standards, access management, incident response capabilities, and physical security. Assesses alignment with NIST 800-53 controls where applicable. Assigns a Security Maturity Score (1-5 scale).
- **CPO/DPO (Privacy Review):** Reviews data handling practices, purpose limitation, data minimization, and compliance with contractual privacy obligations. Assigns a Privacy Maturity Score (1-5 scale).
- **Chief AI Officer (AI Risk Review – if applicable):** Reviews model development practices, training data provenance, bias testing, explainability, and alignment with NIST AI RMF. Assigns an AI Maturity Score (1-5 scale).
- **VP IT Operations (Technical Review):** Reviews integration architecture, API security, identity federation compatibility (Okta SAML/OIDC), encryption protocols, and network connectivity requirements.
- **Chief Compliance Officer (Overall):** Reviews sanctions screening, anti-bribery/anti-corruption (ABAC), code of conduct, and export control compliance.

**Step 3: Scoring and Residual Risk Determination**

Each domain reviewer assigns a maturity score. The Compliance Team compiles a composite Residual Risk Rating using the following methodology:

- For each gap identified, the inherent risk impact and likelihood are assessed.
- Applied controls (both vendor controls and Meridian’s compensating controls) are factored in.
- **Residual Risk Rating Scale:** Low (Green), Medium (Yellow), High (Orange), Critical (Red).

Any domain score of 2 or below, or any identified "Critical" residual risk, automatically triggers the Remediation pathway (Section 5.6) prior to contract execution.

**Step 4: VCA Report and Approval**

The Compliance Team compiles all findings into a single VCA Report, which includes:
- Executive Summary
- Risk Tier and Inherent Risk Score
- Domain Maturity Scores (Security, Privacy, AI if applicable)
- Residual Risk Rating and Heat Map
- Identified Gaps and Control Deficiencies
- Recommended Mitigations and Compensating Controls
- Go/No-Go Recommendation

**Approval Authority:**
- **Tier 3:** Compliance Team Lead (Director-level) + Business Unit Owner.
- **Tier 2:** Chief Compliance Officer + CISO + Business Unit Owner.
- **Tier 1:** Chief Compliance Officer + CISO + CPO/DPO + General Counsel + Business Unit VP.

Approvals are recorded electronically in ServiceNow VMM. No contract shall be executed without all required approvals.

### 5.4 Contractual Requirements

#### 5.4.1 Business Associate Agreement (BAA) – HIPAA Requirements

Prior to the disclosure of any PHI to a vendor, a Business Associate Agreement (BAA) must be fully executed between Meridian (as Covered Entity) and the vendor (as Business Associate). The BAA template is maintained by General Counsel and shall contain, at minimum:

**Required BAA Provisions per 45 CFR § 164.504(e):**

1. **Establish the Permitted and Required Uses and Disclosures of PHI:** The BAA shall specify that the Business Associate may use or disclose PHI only as necessary to perform the services specified in the underlying agreement, or as required by law, or for the proper management and administration of the Business Associate’s business.

2. **Prohibition on Use for Other Purposes:** The BAA shall explicitly prohibit the Business Associate from using or disclosing PHI in any manner that would violate the HIPAA Privacy Rule (45 CFR Part 164, Subpart E) if done by Meridian directly, except as specified in the BAA.

3. **Administrative, Physical, and Technical Safeguards:** The BAA shall require the Business Associate to implement administrative, physical, and technical safeguards that reasonably and appropriately protect the confidentiality, integrity, and availability of electronic PHI, consistent with the HIPAA Security Rule (45 CFR Part 164, Subpart C).

4. **Breach Notification Obligations:** The BAA shall require the Business Associate to report to Meridian’s CISO (Rachel Kim) and CPO/DPO (Dr. Klaus Weber) any use or disclosure of PHI not provided for by the BAA, any Security Incident involving PHI, and any Breach of Unsecured Protected Health Information, within 24 hours of the Business Associate’s confirmed discovery. The notification shall include the identification of each individual whose PHI is reasonably believed to have been accessed, acquired, used, or disclosed during the Breach, as specified at 45 CFR § 164.410.

5. **Subcontractor Obligations:** The BAA shall require that any subcontractors engaged by the Business Associate that create, receive, maintain, or transmit PHI on behalf of the Business Associate agree, via written contract, to the same restrictions, conditions, and requirements that apply to the Business Associate under the BAA.

6. **Access, Amendment, and Accounting:** The BAA shall require the Business Associate to:
   - Make available PHI in designated record sets to Meridian (or directly to the Individual) for access and amendment as required by 45 CFR §§ 164.524 and 164.526.
   - Make available information required for an accounting of disclosures as required by 45 CFR § 164.528.
   - Maintain such information for a period of six (6) years from the date of disclosure.

7. **Internal Practices and Recordkeeping:** The BAA shall require the Business Associate to make its internal practices, books, and records relating to the use and disclosure of PHI available to the Secretary of the U.S. Department of Health and Human Services (HHS) for purposes of determining Meridian’s compliance with HIPAA.

8. **Termination Provisions:** The BAA shall authorize Meridian to terminate the BAA and the underlying services agreement if Meridian determines that the Business Associate has violated a material term of the BAA, as per 45 CFR § 164.504(e)(2)(iii).

9. **Return or Destruction of PHI:** The BAA shall require the Business Associate, upon termination, to return or securely destroy all PHI in its possession, and to certify such destruction in writing to Meridian’s Privacy Team within 30 calendar days. If return or destruction is infeasible, the BAA shall extend protections to the retained PHI and limit further uses to those purposes that make return or destruction infeasible.

**Execution and Tracking:**
- The BAA must be fully executed prior to any PHI disclosure.
- All BAAs are tracked in the Meridian Contract Lifecycle Management (CLM) system (Ironclad) and linked to the vendor record in ServiceNow VMM.
- The Compliance Team conducts a quarterly audit of all active vendors processing PHI to ensure a valid, executed BAA is on file. Any vendor found lacking a BAA shall have data access suspended within 48 hours.

### 5.4.2 Standard Contractual Terms

All vendor contracts, regardless of data classification, must include the following standard compliance clauses:

- **Right to Audit:** Meridian reserves the right to audit vendor compliance with security and privacy obligations.
- **Data Breach Notification:** Notification within 24 hours of confirmed discovery of any incident involving Meridian data.
- **Insurance Requirements:** Tier 1 vendors must maintain Cyber Liability Insurance with coverage of at least $10M per occurrence. Tier 2 vendors must maintain at least $5M coverage. Certificates of Insurance must be provided annually.
- **Background Checks:** Vendor must warrant that all personnel with access to Meridian data have passed criminal background checks.
- **Termination and Transition Assistance:** Defined transition assistance obligations to ensure no service disruption or data integrity loss.

### 5.5 Ongoing Monitoring

Vendor compliance is continuously monitored throughout the vendor lifecycle.

**Monitoring Activities:**

| Activity | Tier 1 | Tier 2 | Tier 3 |
|----------|--------|--------|--------|
| **Continuous Security Ratings** | Yes (BitSight / SecurityScorecard) monitored weekly by SOC | Yes, reviewed quarterly | No |
| **Certificate Expiration Monitoring** | Automated via ServiceNow Discovery – TLS/SSL, SOC 2, ISO certs | Reviewed at re-assessment | No |
| **Vendor Security Incident Notification** | 24-hour SLA per contract; SOC validates and logs in PagerDuty | 48-hour SLA per contract | As reported |
| **Annual Re-Assessment (Full VCA)** | Yes | N/A (Biennial) | N/A (Triennial) |
| **BAA Compliance Audit** | Quarterly internal audit by Compliance Team | Quarterly internal audit by Compliance Team | N/A (no PHI) |
| **Privacy Inquiries Review** | CPO/DPO reviews vendor posture quarterly | Reviewed biennially | N/A |
| **Business Continuity / DR Test Review** | Annually (CISO reviews vendor DR test results) | Reviewed if critical | No |
| **Vendor Termination / Offboarding Verification** | Within 30 days of termination – access revocation, data destruction certificate verified by VP IT Operations and CPO | Within 30 days | Within 30 days |

### 5.6 Remediation and Corrective Action

When a vendor is found to have non-conformities, control deficiencies, or is the subject of a security incident, a formal remediation process is initiated.

**Step 1: Issue Identification and Severity Classification**

Issues are identified through Initial VCA, re-assessment, continuous monitoring, or incident notification. The Compliance Team classifies the issue:

| Severity | Definition | Remediation Timeline Expectation |
|----------|------------|----------------------------------|
| **Critical** | Active data breach; total loss of confidentiality; systemic non-compliance that would cause Meridian to be in material violation of HIPAA if unremediated. | Immediate containment. Remediation plan within 48 hours. |
| **High** | Significant control gap with high residual risk; missing encryption of PHI at rest; no incident response plan; failed audit with no remediation plan. | Remediation plan within 1 week. Correction within 30 days. |
| **Medium** | Control gap with moderate risk; incomplete documentation; delayed patching; no annual pen test. | Remediation plan within 30 days. Correction within 90 days. |
| **Low** | Minor policy documentation gap; best practice recommendation. | Tracked for next re-assessment. |

**Step 2: Remediation Communication**

The Meridian Business Unit Owner, in partnership with the Compliance Team, formally communicates the required remediation to the vendor via ServiceNow VMM. This communication includes:
- Specific non-conformity and the associated Meridian control requirement.
- Required corrective action and evidence required.
- Severity-based timeline for remediation submission.
- Statement of consequences for failure to remediate (see Step 4).

**Step 3: Vendor Remediation and Evidence Submission**

The vendor submits a corrective action plan (CAP) and evidence of remediation by the specified deadline.

**Step 4: Validation and Consequences**

The Compliance Team and, where applicable, the CISO review the evidence and either close the finding or issue an extension. Extensions are approved by the Chief Compliance Officer.

**Consequences for Failure to Remediate:**
- **Critical Severity – Failure to respond within 48 hours:** Immediate suspension of access; General Counsel initiates contract termination review.
- **High Severity – Failure to remediate within 30 days:** Escalation to vendor executive leadership; implementation of compensating controls by Meridian at vendor’s cost (if contractually permissible); initiation of offboarding plan.
- **Medium Severity – Failure to remediate within 90 days:** Downgrade of vendor relationship status; limitation on service expansion; escalation to business unit VP.
- **Low Severity:** Noted in vendor performance record for next re-assessment.

---

## 6. Controls and Safeguards

*(Continuation from Detailed Procedures)*

The following table summarizes the key administrative and technical controls that Meridian, the vendor, or both parties implement as part of the Vendor Compliance Assessment framework. These controls are designed to ensure PHI confidentiality, integrity, and availability, and align with HIPAA Security Rule (45 CFR Part 164, Subpart C) requirements.

| Control Area | Meridian Control | Vendor Control (Contractually Obligated) |
|--------------|------------------|------------------------------------------|
| **Access Control** (§ 164.312(a)) | Unique user IDs enforced via Okta SSO. Vendor access requires Just-In-Time (JIT) provisioning via ServiceNow VMM and approval by Business Unit Owner + VP IT Operations. | Vendor shall implement unique user IDs, automatic logoff (15-min inactivity), and role-based access controls. Multi-factor authentication required for all remote access to systems containing PHI. |
| **Audit Controls** (§ 164.312(b)) | Meridian logs all vendor access to Meridian systems in Splunk SIEM. Logs retained for 1 year online, 6 years offline. | Vendor shall implement audit logging on systems processing Meridian data, retain logs for minimum 1 year, and provide logs to Meridian within 72 hours upon request. |
| **Integrity Controls** (§ 164.312(c)(1)) | Data integrity verified via checksums (SHA-256) on all data exchanged via Secure File Transfer Protocol (SFTP) between Meridian and vendors. | Vendor shall implement mechanisms to corroborate that electronic PHI has not been altered or destroyed in an unauthorized manner. |
| **Person or Entity Authentication** (§ 164.312(d)) | Meridian federates vendor identities through Okta using SAML 2.0 assertions. | Vendor shall ensure that any person seeking access to electronic PHI is the one claimed. MFA mandatory. |
| **Transmission Security** (§ 164.312(e)(1)) | All Meridian-to-vendor data transmissions enforced over TLS 1.2 or higher with mutual authentication. SFTP (SSH key-based) for bulk data transfers. | Vendor shall implement encryption measures (AES-256 or equivalent) to guard against unauthorized access to electronic PHI transmitted over electronic communication networks. No PHI permitted over unencrypted email. |
| **Encryption at Rest** (§ 164.312(a)(2)(iv)) | All PHI stored on Meridian infrastructure encrypted with AES-256. AWS KMS used for key management. | Vendor shall encrypt all PHI at rest using AES-256 or equivalent encryption with key management separate from encrypted data. |
| **Business Continuity / DR** | Meridian maintains a SOC 2 Type II attested BCP/DR program. | Tier 1 vendors must provide annual proof of DR testing. Recovery Time Objective (RTO) must be 4 hours or less for critical services, Recovery Point Objective (RPO) 1 hour or less. |
| **Media Controls** (§ 164.310(d)) | Not applicable to Meridian for vendor process. | Vendor shall implement procedures for disposal of media containing PHI (NIST SP 800-88 compliant wipe or physical destruction). Certificate of destruction provided to Meridian. |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs) and Key Risk Indicators (KRIs)

The Legal & Compliance team, in coordination with the CISO and CPO/DPO, tracks the following metrics and reports them to Executive Leadership and the Board as described in Section 7.2.

| Metric ID | Metric Name | Description | Type | Target | Reporting Frequency | Responsible Team |
|-----------|-------------|-------------|------|--------|---------------------|------------------|
| VCA-01 | **Vendor Intake to Approval Cycle Time** | Median elapsed calendar days from complete intake submission to fully approved VCA. | KPI | Tier 1: <30 days; Tier 2: <20 days; Tier 3: <10 days | Monthly | Compliance Team |
| VCA-02 | **BAA Coverage** | Percentage of active Tier 1 and Tier 2 vendors known to process PHI that have a valid, executed BAA on file in Ironclad CLM. | KRI | **100%**. Any value <100% triggers an immediate remediation sprint. | Monthly | Privacy Team |
| VCA-03 | **Overdue Re-Assessments** | Number of vendors past their scheduled re-assessment date (annual/biennial/triennial) by more than 30 days. | KRI | Target: 0. Threshold: 5. | Monthly | Compliance Team |
| VCA-04 | **Open High/Critical Remediation Items** | Count of vendor remediation findings classified as "High" or "Critical" where the vendor has exceeded the remediation SLA without an approved extension. | KRI | Target: 0. Threshold: 3. | Monthly | Compliance Team |
| VCA-05 | **Vendor Security Rating Changes** | Number of Tier 1 vendors whose external security rating (BitSight) decreased by more than 50 points in a rolling 30-day period. | KRI | Monitor for trends. Investigation triggered for any >50 drop. | Weekly | CISO / SOC |
| VCA-06 | **Reported Vendor Incidents** | Number of vendor-reported security incidents (as per BAA/contract). | KRI | Monitor for trends. Any single incident involving PHI is an immediate CISO/CPO/DPO and CCO notification trigger. | Per Event | CISO / SOC |
| VCA-07 | **Vendor Offboarding SLA Compliance** | Percentage of offboarded vendors where access revocation was completed within 24 hours of termination effective date, and data destruction certification received within 30 days. | KPI | >95% completed within SLA. | Monthly | VP IT Operations |

### 7.2 Reporting and Dashboarding

**ServiceNow VMM Dashboard:**
A real-time operational dashboard is maintained in ServiceNow VMM, accessible to Compliance Team, CISO Office, CPO/DPO, IT Operations, and Business Unit Owners. The dashboard displays:
- Active vendor count by risk tier.
- Vendors in assessment pipeline with current stage and aging.
- BAA coverage chart (red/amber/green).
- Remediation status tracking (count by severity, days open).
- Upcoming re-assessments (next 90 days).

**Quarterly Compliance Report:**
The Chief Compliance Officer shall publish a Quarterly Vendor Compliance Report to the CEO, Executive Leadership Team, and the Board Audit & Compliance Committee. This report includes:
- Trend analysis of all KPIs/KRIs over the trailing 12 months.
- Summary of newly onboarded Tier 1 vendors.
- Report of any vendor-related security or privacy incidents.
- Status of all open remediation items classified as High or Critical.
- Regulatory update assessment relevant to vendor risk management.
- Summary of audit activity (Meridian audits of vendors and external audits of Meridian's vendor management program).

**Annual Report to Board AI Governance Committee:**
In alignment with the NIST AI RMF, the Chief AI Officer and Chief Compliance Officer shall provide an annual report specifically covering AI/ML vendors, including model risk, algorithmic bias testing, and adherence to the EU AI Act requirements.

---

## 8. Exception Handling and Escalation

Meridian recognizes that business needs may occasionally necessitate deviations from this SOP. All exceptions must be formally documented, risk-assessed, and approved prior to taking the non-conforming action.

### 8.1 Exception Request Procedure

**Step 1: Submission of Exception Request**

The Business Unit Owner submits a “Vendor Compliance Exception Request” in ServiceNow VMM. The request shall include:
- **SOP Reference:** Specific section(s) of SOP-LEGC-016 for which the exception is sought.
- **Vendor and Engagement Details:** VA-ID, vendor name, service description.
- **Business Justification:** Clear, compelling business rationale explaining why the standard process cannot be followed. This must include the business impact of not engaging the vendor under the exception (e.g., deal velocity, unique capability).
- **Risk Description:** Description of the risk(s) introduced by the non-standard condition.
- **Compensating Controls:** Detailed description of compensating controls Meridian will implement to reduce residual risk.
- **Duration:** Whether the exception is permanent (life of engagement) or temporary. If temporary, a specific expiration date (not exceeding 12 months) must be proposed.

**Step 2: Risk Assessment and Review**

- **Compliance Team:** Reviews for completeness and conducts an initial risk assessment.
- **CISO (for security/access exceptions):** Reviews compensating technical controls and provides a security risk opinion.
- **CPO/DPO (for PHI/privacy exceptions):** Reviews legal and privacy implications.
- **Chief AI Officer (for AI-related exceptions):** Reviews AI/ML model risk implications.

**Step 3: Approval**

Exception approvals follow a tiered authority matrix:

| Exception Type | Tier 3 | Tier 2 | Tier 1 |
|----------------|--------|--------|--------|
| Temporary extension of re-assessment deadline (< 6 months) | CCO | CCO | CCO |
| Temporary security questionnaire deferral (< 8 weeks) | CISO + CCO | CISO + CCO | CISO + CCO + GC |
| Permanent waiver of a non-regulatory required assessment component | CCO | CISO + CCO | CISO + CCO + GC + CEO |
| PHI data sharing without fully executed BAA | N/A (Not Permitted) | N/A (Not Permitted) | N/A (Not Permitted) |
| Any exception that reduces a HIPAA-required safeguard | N/A (Not Permitted) | N/A (Not Permitted) | N/A (Not Permitted) |

**Note:** No exception can waive a mandated regulatory requirement under HIPAA, HITECH, or applicable state data breach notification laws. Specifically, **no PHI shall be disclosed to any vendor without a fully executed BAA**. Any attempt to create such an exception shall be rejected by the General Counsel and reported immediately to the Chief Compliance Officer as a potential compliance violation.

### 8.2 Approved Exception Management

- All approved exceptions are tracked in the Exceptions Register within ServiceNow VMM.
- For temporary exceptions, ServiceNow triggers an automated notification to the Business Unit Owner and Compliance Team 30 days before expiration.
- A renewal request uses the same procedure as an initial exception request and must be submitted before expiration.

### 8.3 Escalation Path

Vendor compliance issues that cannot be resolved at the Business Unit Owner/Compliance Team level shall be escalated according to the following matrix:

| Issue | Escalation Level 1 | Escalation Level 2 | Escalation Level 3 |
|-------|-------------------|-------------------|-------------------|
| Vendor refuses required VCA | CCO notifies BU VP | GC sends breach-of-contract notice | CEO approves termination |
| Vendor fails to remediate Critical finding | CISO notifies CCO and GC; access suspended per Section 5.6 | GC initiates formal legal correspondence | CEO and Board notified; engagement terminated |
| Vendor security incident involving PHI | CISO alerts CPO/DPO and CCO | CCO convenes Incident Response Team (per SOP-SEC-003) | GC determines external reporting obligations; CEO approval for external comms |
| Business Unit bypasses VCA process | CCO reports to GC and BU VP | GC notifies CEO | CEO initiates disciplinary action per HR policy |

---

## 9. Training Requirements

Meridian ensures that all personnel with responsibilities under this SOP receive appropriate training to fulfill their duties competently.

### 9.1 Training Curriculum

| Target Audience | Training Module | Content | Duration | Frequency |
|-----------------|-----------------|---------|----------|-----------|
| **All Employees** | General Data Privacy and Security Awareness (SOP-SEC-001) | - Introduction to PHI and PII<br>- Employee responsibilities in protecting data<br>- Reporting security incidents | 30 minutes (eLearning) | Annually (mandatory for system access) |
| **Business Unit Owners & Delegates (Procurement Initiators)** | Vendor Compliance Assessment 101 (this SOP) | - How to initiate a Vendor Intake Request<br>- Understanding risk tiering<br>- Their role in remediation management<br>- ServiceNow VMM navigation | 45 minutes (eLearning + 15 min recorded walkthrough) | Annually |
| **Legal & Compliance Team, CISO Team, Privacy Team** | Advanced Vendor Risk Assessor Training | - Deep dive on VCA methodology<br>- HIPAA/HITECH vendor obligations<br>- Contractual review: BAAs red flags<br>- Mock Assessment Workshop<br>- Using BitSight and ServiceNow advanced modules | 4 hours (Instructor-led, annual) + 2 refreshers (quarterly webinars, 30 min each) | Initial (within 60 days of role start), Annual refresher |
| **Executive Leadership (ELT)** | Vendor Risk Governance for Leaders | - Board-level vendor risk reporting metrics<br>- Escalation triggers and response expectations | 1 hour (Instructor-led by CCO) | Biennially |

### 9.2 Training Tracking and Enforcement

- All training is assigned and tracked via the Meridian Learning Management System (LMS – Workday Learning).
- **Compliance Tracking:** The Compliance Team's Workday dashboard tracks completion rates.
- **Consequence for Non-Completion:**
  - Employees who fail to complete mandatory annual training within 60 days of assignment shall have their access to procurement systems and ServiceNow VMM suspended until training is completed.
  - Business Unit Owners with overdue training shall be reported to the Chief Compliance Officer and the EVP of their respective business unit at the monthly compliance review.
- **Onboarding:** New hires in roles requiring this training must complete applicable modules within 30 calendar days of their start date as a condition of their probationary clearance.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Standard Operating Procedures

| SOP ID | Document Title | Relationship |
|--------|----------------|--------------|
| SOP-LEGC-015 | Third-Party Contracting and Legal Review | Mandates legal review process for all vendor contracts prior to execution. |
| SOP-SEC-003 | Security Incident Response and Breach Notification | Governs Meridian’s internal response to security incidents, including vendor-originated incidents. References Breach notification timelines per HIPAA and HITECH. |
| SOP-ENG-012 | Open Source Software Management | Governs the consumption of open-source software, which is out of scope for vendor assessment unless a formal commercial support agreement exists. |
| SOP-DATA-008 | Data Classification and Handling | Defines the data classification taxonomy used in vendor risk tiering. |
| SOP-AI-002 | AI Model Risk Management | Governs internal model risk management per SR 11-7 and NIST AI RMF, references external AI vendor assessment criteria. |
| SOP-HR-004 | Workforce Screening and Onboarding | Defines the screening process for internal personnel; distinct from vendor assessment. |
| SOP-BCP-005 | Business Continuity and Disaster Recovery Planning | Contains requirements for Tier 1 vendor DR test review. |

### 10.2 External Standards and Regulatory References

- **HIPAA Privacy Rule:** 45 CFR Part 160 and Subpart E of Part 164.
- **HIPAA Security Rule:** 45 CFR Part 160 and Subparts A and C of Part 164.
- **HIPAA Breach Notification Rule:** 45 CFR §§ 164.400-414.
- **HITECH Act:** Title XIII of the American Recovery and Reinvestment Act of 2009.
- **NIST AI Risk Management Framework:** NIST AI 100-1.
- **EU Artificial Intelligence Act:** Regulation (EU) 2024/1689.
- **Federal Reserve SR 11-7:** Guidance on Model Risk Management.
- **NIST SP 800-53 Rev. 5:** Security and Privacy Controls for Information Systems and Organizations (used as reference control catalog).

### 10.3 Tools and Systems

- **ServiceNow Vendor Management Module (VMM):** Primary workflow automation for VCA intake, assessment, tiering, remediation, and dashboarding.
- **Ironclad (Contract Lifecycle Management – CLM):** Repository for BAAs and vendor contracts.
- **BitSight Security Ratings:** Continuous external monitoring for Tier 1 vendor cybersecurity posture.
- **Workday Learning:** LMS for training assignments and compliance tracking.
- **Splunk SIEM:** Logging and monitoring for privileged vendor access sessions.
- **PagerDuty:** Incident alerting and escalation.
- **Dun & Bradstreet (D&B):** Financial viability and sanctions screening data.

---

## 11. Revision History

| Version | Effective Date | Author / Editor | Summary of Changes |
|---------|----------------|-----------------|-------------------|
| 1.8 | 2025-11-19 | Thomas Anderson, CCO | Major revision. Updated vendor tiering scoring thresholds; added mandatory AI model risk review workflow for AI vendors (aligning with SOP-AI-002); revised BAA provisions to fully reference 45 CFR § 164.504 and Breach Notification Rule; added Section 5.6 Remediation framework with defined severity SLA; added KPI VCA-07 (Offboarding SLA); updated training audience and content. Approved by Maria Gonzalez (GC). |
| 1.7 | 2025-02-18 | Thomas Anderson, CCO | Refined roles and responsibilities (RACI) to clarify ownership of remediation by Business Unit Owner; added VP IT Operations technical review step; integrated ServiceNow VMM as primary workflow for intake and assessment; expanded exception handling matrix to explicitly forbid any PHI sharing without BAA. |
| 1.6 | 2024-09-10 | Rachel Kim, CISO (Interim) | Updated security domain of VCA to align with new cloud security architecture (AWS KMS integration); updated monitoring section to include BitSight; revised access control and authentication requirements for vendor remote access. |
| 1.5 | 2024-03-22 | Thomas Anderson, CCO | Incorporated EU AI Act and NIST AI RMF references in anticipation of Clinical AI Platform regulatory classification; added Chief AI Officer to RACI for AI vendors; established AI Maturity Score in VCA. |
| 1.4 | 2023-11-05 | Elena Rossi, VP Legal | Initial structural revision: separated policy statements from detailed procedures; standardized templates for BAA provisions. Adopted Ironclad CLM for contract tracking. |
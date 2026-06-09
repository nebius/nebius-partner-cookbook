---
sop_id: "SOP-LEGC-014"
title: "Sanctions and Export Control"
business_unit: "Legal & Compliance"
version: "2.3"
effective_date: "2024-11-18"
last_reviewed: "2025-01-14"
next_review: "2025-07-04"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Sanctions and Export Control

## 1. Purpose and Scope

### 1.1 Purpose
The purpose of this Standard Operating Procedure (SOP) is to establish the framework, controls, and operational processes by which Meridian Health Technologies, Inc. ("Meridian" or the "Company") ensures full compliance with all applicable economic sanctions, trade embargoes, and export control laws and regulations across its global operations. This SOP operationalizes Meridian’s commitment to preventing transactions with sanctioned parties, prohibiting the unlicensed export of controlled technology, and fostering a culture of compliance that aligns with the Company’s SOC 2 Type II trust services criteria, specifically those related to risk management, governance, and compliance.

### 1.2 Scope
This SOP applies globally and without exception to all:
- **Employees, contractors, and consultants** of Meridian, regardless of location.
- **Subsidiaries and affiliates** under Meridian’s operational control (London, Berlin, Singapore, Toronto).
- **Products and Services**: Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform.
- **Transactions**: All exports, re-exports, transfers (in-country), and provision of services involving dual-use or military goods, software, technology, or technical data, including deemed exports to foreign persons within the United States.
- **Third-Party Relationships**: Customers, vendors, payers, providers, research partners, and any other counterparties engaged with Meridian.
- **Data and Technology**: All proprietary AI/ML models, encryption software integrated within the SaaS Platform, clinical algorithms, and technical specifications.

Sanctions and export control compliance is a foundational element of Meridian’s internal control environment, directly supporting the achievement of SOC 2’s Common Criteria 3 (Risk Assessment), 5 (Control Activities), and 7 (Monitoring Activities).

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
| :--- | :--- |
| **BIS** | Bureau of Industry and Security, U.S. Department of Commerce. Administers the Export Administration Regulations (EAR). |
| **CCL** | Commerce Control List. A list of items under the export control jurisdiction of the BIS. |
| **Deemed Export** | The release of controlled technology or source code to a foreign person within the United States. |
| **DDTC** | Directorate of Defense Trade Controls, U.S. Department of State. Administers the International Traffic in Arms Regulations (ITAR). |
| **EAR** | Export Administration Regulations (15 C.F.R. §§ 730-774). Governs dual-use items. |
| **ECCN** | Export Control Classification Number. An alpha-numeric code on the CCL that categorizes an item for export control purposes. |
| **EU Dual-Use Regulation** | Regulation (EU) 2021/821 of the European Parliament and of the Council of 20 May 2021, setting up a Union regime for the control of exports, brokering, technical assistance, transit, and transfer of dual-use items. |
| **Export** | An actual shipment or transmission of an item out of a country; the release of technology or source code to a foreign person. |
| **FinCEN** | Financial Crimes Enforcement Network, U.S. Department of the Treasury. |
| **ITAR** | International Traffic in Arms Regulations (22 C.F.R. §§ 120-130). Governs defense articles and munitions. |
| **License** | An authorization issued by a competent government authority (e.g., BIS) permitting a specific export or sanctioned activity that would otherwise be prohibited. |
| **OFAC** | Office of Foreign Assets Control, U.S. Department of the Treasury. Administers and enforces U.S. economic and trade sanctions. |
| **OFSI** | Office of Financial Sanctions Implementation, HM Treasury. Administers and enforces UK financial sanctions. |
| **Sanctions List** | A list of individuals, entities, and vessels designated by a government authority (e.g., OFAC’s SDN List) with which transactions are restricted or prohibited. |
| **SDN** | Specially Designated Nationals and Blocked Persons List (OFAC). |
| **SSI** | Sectoral Sanctions Identifications List (OFAC). |
| **TTS** | Trade Transaction Systems (Meridian’s proprietary export documentation and classification management tool). |
| **Vistra** | Meridian’s third-party due diligence and sanctions screening SaaS platform. |

## 3. Roles and Responsibilities

The following matrix delineates roles and responsibilities using a RACI model (Responsible, Accountable, Consulted, Informed).

| Role | Responsibility | RACI |
| :--- | :--- | :--- |
| **Chief Compliance Officer (CCO)** | Thomas Anderson. Overall responsibility for the Sanctions and Export Control Program (SECP). Owns the risk assessment, policy framework, and annual effectiveness review. | A |
| **General Counsel (GC)** | Maria Gonzalez. Provides ultimate legal interpretation of regulations, approves exceptions and self-disclosures, and acts as a final arbiter for ambiguous classifications. | C, A (Exceptions) |
| **Senior Compliance Manager, Trade** | Designated role reporting to the CCO. Manages the day-to-day operational execution of this SOP, including screening hit adjudication, classification reviews, license applications, and training delivery. | R |
| **Compliance Analysts** | Team members reporting to the Senior Compliance Manager. Perform first-level sanctions screening reviews, maintain classification records in TTS, and monitor regulatory updates. | R |
| **Engineering & Product Leads** | CTO, VP of Engineering, and AI Product Directors. Responsible for providing detailed technical specifications for all products and algorithms to enable accurate export classification. Must consult with the Trade Compliance team before releasing new products/features externally. | R, I |
| **Sales & Business Development** | All territory managers and account executives. Responsible for submitting new customer requests to the screening queue in Vistra, identifying red flags, and notifying Compliance of any potential restricted end-use. | R |
| **People Operations (HR)** | Responsible for integrating trade compliance screening into the recruitment and onboarding processes for non-U.S. persons and roles with access to controlled technology. | R |
| **Internal Audit** | Provides independent assurance on the effectiveness of the SECP controls, reports findings to the Audit Committee and CCO. | C |
| **All Employees** | Must complete annual training, understand reporting obligations, and immediately escalate any red flags or concerns to `compliance@meridianhealth.com`. | R |

## 4. Policy Statements

Meridian Health Technologies, Inc. is unconditionally committed to full compliance with all applicable sanctions and export control laws and regulations of the United States, the United Kingdom, the European Union, Singapore, and other jurisdictions where it operates.

1.  **Zero-Tolerance for Sanctions Violations:** Meridian prohibits transactions, services, or dealings of any kind, directly or indirectly, with individuals, entities, organizations, or vessels designated on applicable sanctions lists, including but not limited to the OFAC SDN List, the EU Consolidated List, the UK OFSI Consolidated List, and any country or region subject to a comprehensive territorial embargo (e.g., OFAC sanctions on Cuba, Iran, North Korea, Syria, and the Crimea, Donetsk, and Luhansk regions of Ukraine). This zero-tolerance stance supports the SOC 2 Common Criteria 5.1 (Logical and Physical Access Controls) and 5.2 (Risk Mitigation), ensuring that sanctioned entities cannot access Meridian’s systems or services.

2.  **Mandatory Export Classification:** No Meridian product, software, technology, or technical data—including any AI/ML model, algorithm, encryption software, or associated technical documentation—shall be exported, transferred, or released (including as a deemed export) without first receiving a formal, documented export classification (ECCN and/or EU Dual-Use classification).

3.  **Prohibition on Unlicensed Exports:** Exports of any item controlled for a restrictive end-use, end-user, or destination require a valid, specific, or general license issued by the competent government authority. Exports shall not proceed without documented authorization matching the specific transaction. This directly supports SOC 2 CC5.3 (Control Activities) by establishing a mandatory check-point before deployment or delivery.

4.  **Mandatory Screening Protocol:** All counterparties—including customers, vendors, payers, providers, and third-party researchers—must undergo a rigorous, risk-based sanctions screening process during onboarding and must be re-screened on a scheduled, risk-tiered basis throughout the relationship lifecycle.

5.  **Immediate Voluntary Self-Disclosure:** Meridian will promptly assess and, where substantiated, will make a voluntary self-disclosure of any apparent, suspected, or confirmed violation of sanctions or export controls to the cognizant regulatory authority. This commitment supports SOC 2 CC7.4 (Incident Response and Recovery).

6.  **No Facilitation:** No Meridian employee, contractor, or agent may approve, facilitate, or otherwise participate in any transaction that would be prohibited for a U.S. or EU person to perform directly.

## 5. Detailed Procedures

### 5.1 Sanctions Screening Procedure
This procedure supports the SOC 2 Control Activities Common Criteria 5.1 and 5.2 by preventing unauthorized access and system operations, and monitoring risks.

1.  **Counterparty Identification (R: Sales/Business Development):**
    - Any Meridian employee seeking to initiate a new business relationship, a pilot, a data-sharing agreement, or a vendor contract must initiate an onboarding request through **Vistra**.
    - The requester must provide the counterparty’s full legal name, primary physical address, all known beneficial owners (with a ≥ 25% ownership threshold), and any associated shipping or billing addresses. For legal entities, the jurisdiction of incorporation must be unambiguously stated.

2.  **Automated Screening (R: Vistra System):**
    - Upon submission, Vistra automatically screens the entity and all associated data points against 1,500+ global sanctions, enforcement, and Politically Exposed Person (PEP) lists, including OFAC, UN, EU, UK OFSI, and Singaporean MAS lists.
    - Vistra employs fuzzy logic matching (≥ 85% threshold) to flag potential phonetic, partial, or alternate-spelling matches.

3.  **Alert Adjudication (R: Compliance Analyst):**
    - **Level 1 Review (Triage, SLA: 4 business hours):** A Compliance Analyst opens all newly generated "amber" and "red" alerts. Analysts rule out obvious false positives (e.g., name matches an SDN but the entity’s country of incorporation and physical address are in a non-sanctioned jurisdiction with no nexus). All Level 1 decisions must be documented with explicit rationale and supporting evidence (e.g., a corporate registry excerpt) in Vistra’s audit trail.
    - **Level 2 Review (Escalated Hits, SLA: 24 business hours):** Any alert the Level 1 Analyst cannot definitively clear as a false positive is escalated to the **Senior Compliance Manager, Trade**. The Senior Manager conducts enhanced due diligence, which may include:
        - Directly contacting the counterparty to request clarification on ownership or location, without disclosing the specific sanctions query.
        - Consulting OFAC’s 50 Percent Rule for entities owned in aggregate by blocked persons.
        - Engaging external legal counsel in the relevant jurisdiction for complex corporate structures.
    - **Final Determination:** The Senior Compliance Manager records a final disposition of "Cleared" or "Blocked/Rejected" with a detailed narrative explanation. A "Blocked/Rejected" disposition halts the onboarding process immediately. No appeal is permitted for a "Blocked" determination.

4.  **Periodic Re-Screening (R: Trade Compliance Team):**
    - Every active counterparty is automatically rescanned against updated sanctions lists by Vistra on a mandatory 30-day cycle.
    - An emergency, unscheduled re-screening of all active counterparties is initiated within 2 hours of OFAC, OFSI, or EU Commission publishing a new major sanctions action.
    - New hits arising from re-screening are adjudicated with the highest urgency, following the Level 1 and Level 2 process, with an SLA of 4 business hours for resolution. The CCO is personally briefed on any new, substantive hits on existing counterparties.

5.  **Geographic IP and Geo-Blocking Controls (R: CISO & Engineering):**
    - Meridian’s network architecture, managed by the CISO, maintains a dynamic blocklist of IP ranges associated with comprehensively sanctioned jurisdictions (e.g., Cuba, Iran, North Korea, Syria, and the Crimea, Donetsk, and Luhansk regions of Ukraine). Access to the Meridian SaaS Platform and Clinical AI Platform from these specific IP ranges is technically prohibited, enforcing controls inline with SOC 2 CC5.1.

### 5.2 Export Classification and License Management Procedure
This procedure operationalizes the accurate classification of all Meridian proprietary technology, a non-negotiable step before any export or deemed export.

1.  **Technical Specification Intake (R: Engineering/Product Lead):**
    - Before a new product release (e.g., a new AI diagnostic model, a HealthPay feature update involving encryption), the Product Lead completes the **Product Classification Worksheet (PCW)** (Form-LEGC-014-A) in TTS. The PCW includes technical parameters: the principal algorithm’s function, maximum encryption key length, if any custom cryptographic protocols are used, and if the AI model has any military or intelligence application capabilities.

2.  **Classification Analysis (R: Senior Compliance Manager, Trade):**
    - The Senior Manager analyzes the PCW against the CCL to determine the ECCN. Primary classification gates include:
        - **ECCN 0A (Nuclear):** Checked against nuclear-related medical device controls.
        - **ECCN 3D (Software)/3E (Technology):** Scrutinized for any AI/ML models for vision enhancement or target tracking.
        - **ECCN 4D (Software)/4E (Technology):** Scrutinized for cybersecurity and encryption items. All AI-driven cybersecurity modules in the SaaS platform are reviewed here.
        - **ECCN 5D (Software, Part 2):** Information security. The HealthPay encryption software is always reviewed under Category 5, Part 2.
    - The analysis is documented in TTS, referencing specific CCL paragraphs (e.g., ECCN 5D002.c.1.d). If an item is subject to the EAR but not listed on the CCL, it is classified as EAR99.

3.  **Classification Finalization and Recordkeeping (R: Senior Compliance Manager, Trade):**
    - The Senior Manager records the final, affirmative ECCN in TTS. A written, detailed classification analysis memorandum is created for all items classified outside of EAR99. This memo is a legal record.
    - Record Retention: All export classification records (worksheets, memos, licenses) are retained for a minimum of 5 years from the date of export or last transaction, consistent with BIS recordkeeping requirements and SOC 2 CC7.6 (Audit Logging).

4.  **License Application (R: Senior Compliance Manager):**
    - If an export requires a specific license (e.g., an AI model with a sensitive ECCN to a restricted end-user in a non-embargoed country), the Senior Manager prepares the license application (e.g., BIS SNAP-R form).
    - The application, with a cover memo explaining the transaction, is reviewed by the CCO and approved by the General Counsel before submission.
    - **License Tracking:** All active licenses (license number, expiration date, authorized parties, provisos/conditions) are tracked in a central register in TTS. The system sends automated alerts to the Trade Team 60 days before license expiration and 90 days before the requirement for an annual shipment report.

5.  **Deemed Export Protocol (R: People Operations & Engineering):**
    - For any non-U.S. citizen employee or contractor requiring access to controlled technology classified as requiring a license (e.g., an ECCN 3E001 for an AI algorithm), a deemed export review is triggered.
    - Prior to granting system access, People Operations completes the **Deemed Export Access Form** (Form-LEGC-014-B) and submits it to the Trade Compliance team.
    - The Senior Compliance Manager evaluates the individual's most recent citizenship and permanent residence status against the "See" conditions for that ECCN. Access to controlled technology is not provisioned until the Compliance team explicitly clears the individual in writing.

| Export Classification Matrix |
| :--- |
| **Clinical AI Platform:** ECCN 3E991 (Technology for medical AI not elsewhere specified, controlled for AT reasons only). No license required (NLR) for any destination except AT-embargoed countries. |
| **HealthPay Encryption:** ECCN 5D002 (Encryption software). Classified under License Exception ENC (Unrestricted) for most end-users, excluding government end-users in E:1 countries. Semi-annual reporting to BIS and the EU's encryption notification required. |
| **MedInsight Analytics:** EAR99. Subject to EAR but no specific ECCN. May be exported without a license, but OFAC sanctions screening remains mandatory. |

## 6. Controls and Safeguards

This section formalizes the technical and administrative controls that support the Trust Services Criteria, specifically mapped to SOC 2 requirements.

### 6.1 SOC 2 Control Mapping and Implementation

| SOC 2 Criterion | Ref. | Control Activity | Maturity |
| :--- | :--- | :--- | :--- |
| **Risk Assessment** | CC3.1 | The CCO performs an annual, documented Sanctions and Export Control Risk Assessment (SECRA). The assessment evaluates inherent risk based on product dual-use potential, encryption sales, and geographic footprint, identifying and scoring residual risk after controls. | High |
| **Control Activities** | CC5.3 | A formal **Technology Control Plan (TCP)** is in place for items classified above EAR99. The TCP defines the physical, logical, and administrative controls protecting the item, including multi-factor-authentication (MFA) gated repositories and segregated development networks. | High |
| **Control Activities** | CC5.1, CC5.3 | **Automated Transactional Lock:** The Vistra and Salesforce integration is configured with a hard transactional lock. A "Blocked/Rejected" status on a counterparty record in Vistra programmatically prevents the creation of an opportunity, contract record, or invoice for that counterparty in Salesforce and NetSuite. This provides a preventative control, eliminating reliance on a manual check. | High |
| **Logical & Physical Access** | CC6.1, CC6.7 | **Role-Based Access Control (RBAC):** Access to the TTS and Vistra adjudication modules is restricted via RBAC using Okta SSO integrated with active directory groups `TradeCompliance_Adjudicators` and `TradeCompliance_Managers`. All login attempts and changes to classification or screening status require a non-repudiable e-signature. | Optimized |
| **Monitoring Activities** | CC7.2, CC7.3 | **Continuous Control Monitoring (CCM):** An automated, serverless script in AWS Lambda performs a nightly reconciliation between the master counterparty list in Vistra and active customer accounts in NetSuite. Any active NetSuite account (i.e., an entity that can be transacted with) that does *not* have a corresponding "Active/Cleared" status in Vistra generates a Critical Severity ticket in ServiceNow (Configuration Item: Trade Compliance). | Optimized |
| **Change Management** | CC8.1, CC8.5 | **Infrastructure-as-Code (IaC) Review:** All proposed changes to the geo-blocking IP tables, screening logic, or the transactional lock code in Salesforce/NetSuite must be submitted as a Pull Request in the central `trade-compliance-controls` GitHub repository. The Senior Compliance Manager, Trade, is a mandatory approver on all PRs modifying these specific files. | High |

### 6.2 Data Retention and Recordkeeping
- **Retention Schedule:** All sanctions screening adjudications, final classification determinations, license applications, filed reports, Deemed Export Access Forms, and SECRA documents are retained for a minimum of **10 years** from the date of creation.
- **Archival:** 90 days after a counterparty relationship is terminated, its compliance records are moved from Vistra's live database to an immutable, encrypted Amazon S3 Glacier Deep Archive vault, configured with a legal hold.

## 7. Monitoring, Metrics, and Reporting

Continuous monitoring is a cornerstone of the SECP, providing evidence of control effectiveness for the SOC 2 Common Criteria 7 (Monitoring Activities) requirements (CC7.1–CC7.5).

### 7.1 Key Performance Indicators (KPIs) and Key Risk Indicators (KRIs)

| Metric | Type | Target/Threshold | Measurement Tool | Reporting Owner | Frequency |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Average Time to Adjudicate Level 1 Alert** | KPI | **≤ 4 business hours** | Vistra Dashboard | Senior Compliance Manager | Monthly |
| **Average Time to Adjudicate Level 2 Alert** | KPI | **≤ 24 business hours** | Vistra Dashboard | Senior Compliance Manager | Monthly |
| **Percentage of Onboarding Requests Screened Pre-Contract** | KRI | **100%** | NetSuite-Vistra Reconciliation Script | CCO | Real-time (monitored monthly) |
| **Overdue Export Licenses (> 30 days from expiration)** | KRI | **0** | TTS License Register | Senior Compliance Manager | Weekly |
| **Periodic Re-Screening Completeness** | KPI | **99.9% every 30-day cycle** | Vistra System Audit Log | Senior Compliance Manager, CISO | Monthly |
| **Geo-Block Access Attempts from Sanctioned Jurisdictions** | KRI | Investigate each event | AWS CloudTrail, WAF Logs | CISO | Monthly Report to CCO |
| **Annual SECRA Completion** | KPI | **By end of Q4 each year** | Compliance Calendar | CCO | Annually |

### 7.2 Reporting Cadence
- **Monthly Reporting:** The Senior Compliance Manager, Trade, delivers a "Trade Controls Dashboard" report to the CCO containing all monthly KPIs, a summary of all Level 2 screening alerts, status of all open license applications, and a register of blocked counterparties.
- **Quarterly Reporting:** The CCO presents a "Quarterly Risk and Compliance Update" to the General Counsel and CEO. This report summarizes SECP operations, KPI trends, regulatory horizon scanning, and the results of any internal audit spot-checks.
- **Annual Reporting:** The CCO produces the "Annual Sanctions and Export Control Program Effectiveness Review" for the Board of Directors’ Risk and Audit Committee. This report assesses the state of compliance, the effectiveness of controls as mapped to SOC 2 criteria, significant regulatory changes, and the results of the annual risk assessment.

## 8. Exception Handling and Escalation

### 8.1 Exception Handling
A request for an exception to any procedure in this SOP is a high-risk event and will be processed as follows:
1.  **Formal Request:** The requester must submit a fully completed **Sanctions and Export Control Exception Request** (Form-LEGC-014-C) via the ServiceNow "Trade Compliance" portal. The form requires a detailed business justification, a full description of the proposed transaction or activity, and a risk mitigation plan.
2.  **Risk Assessment:** The Senior Compliance Manager, Trade, conducts a documented risk assessment, assessing the legal, operational, and reputational risk of the potential exception.
3.  **Legal Review:** The General Counsel reviews the request and the risk assessment.
4.  **Final Approval Authority:**
    - **Operational Exceptions** (e.g., granting a 24-hour extension for a low-risk Level 1 screening adjudication SLO): CCO.
    - **Procedural Exceptions** (e.g., bypassing the classification process for a specific, low-risk internal tool): CCO and General Counsel jointly.
    - **Policy Exceptions** (e.g., authorizing a transaction with a red-flagged entity): The Chief Executive Officer (CEO), based on a written joint recommendation from the CCO and General Counsel, who will outline potential personal liability. *No policy exception will be made if it violates the law.*
5.  **Record:** All exceptions are logged in a central, immutable register. Any exception granted is temporary (e.g., for one transaction, for 30 days) and requires specific, compelling conditions that mitigate the elevated risk.

### 8.2 Escalation
The following escalation path is mandatory:
- **Employee Suspects a Violation:** Immediately halt the transaction/project and report the concern directly to `compliance@meridianhealth.com` or the anonymous whistleblower hotline, `ethics@meridianhealth.com`.
- **Legal & Compliance Receives Report:** Within 24 hours, the CCO and General Counsel perform an initial assessment. If a potential violation is credible, the Company's external international trade counsel is engaged immediately.
- **Voluntary Self-Disclosure Decision:** The General Counsel and CCO make a recommendation to the CEO and Audit Committee Chair on whether to submit a voluntary self-disclosure to the relevant agency (e.g., OFAC, BIS, OFSI). The final decision rests with the Board’s Risk and Audit Committee. The decision timeline is a maximum of 48 hours from credible knowledge of the violation.

## 9. Training Requirements

Training is a required component of Meridian’s control environment, per SOC 2 CC2.2.

| Training Module | Target Audience | Frequency | Delivery Method | Tracking System |
| :--- | :--- | :--- | :--- | :--- |
| **SECP 101: Core Principles** | **All Employees, Contractors, Board Members** | **Annually** (within 30 days of hire and by Sept 30 each fiscal year) | Computer-Based Training (CBT) in Litmos LMS | Litmos LMS and SuccessFactors HRIS |
| **SECP 201: Operational Screening & Red Flags for Sales** | **Global Sales, Business Development, Marketing** | **Annually** + **Bi-Annual Micro-Learning Modules** | Instructor-Led Virtual Training (ILT) by Senior Compliance Manager, Trade | Litmos LMS |
| **SECP 301: Advanced Classification & Licensing for Engineers** | **Product, Engineering, R&D, IT Security Staff** | **Annually** (specific to new product feature rollouts) | ILT, combined with a hands-on session on completing a PCW in TTS | Litmos LMS and TTS Training Log |
| **SECP Executive Briefing** | **C-Suite, Board Risk & Audit Committee** | **Annually** | In-person briefing by the CCO | Board of Directors Minutes |

**Training Effectiveness:** The Compliance Team measures training effectiveness through pre- and post-training assessments within Litmos. A passing score of ≥ 80% is required. The annual SECRA reviews the training matrix and failure/completion rates to gauge the strength of the compliance culture. Failure to complete required training within the specified timeframe results in an immediate escalation to the employee's People Operations (HR) business partner for a formal performance discussion.

## 10. Related Policies and References

### 10.1 Internal Meridian Policies
- **SOP-LEGC-010:** Code of Business Conduct and Ethics
- **SOP-LEGC-012:** Anti-Bribery and Anti-Corruption (ABAC) Compliance
- **SOP-LEGC-018:** Third-Party Risk Management (TPRM)
- **SOP-SEC-009:** Information Security Policy (Data Classification and Handling)
- **SOP-SEC-014:** Encryption and Key Management
- **SOP-ENG-003:** Product Development Life-Cycle (PDLC)
- **SOP-HR-022:** Global Hiring and Onboarding Verification Standards
- **Policy-LEGC-005:** Whistleblower and Non-Retaliation Policy

### 10.2 External Regulatory References
- **U.S. Department of Commerce, Bureau of Industry and Security (BIS):** Export Administration Regulations (EAR), 15 C.F.R. §§ 730-774.
- **U.S. Department of the Treasury, Office of Foreign Assets Control (OFAC):** Sanctions Programs and the Specially Designated Nationals (SDN) List.
- **U.S. Department of State, Directorate of Defense Trade Controls (DDTC):** International Traffic in Arms Regulations (ITAR), 22 C.F.R. §§ 120-130.
- **Regulation (EU) 2021/821 of the European Parliament and of the Council:** Setting up a Union regime for the control of exports, brokering, technical assistance, transit, and transfer of dual-use items.
- **United Kingdom:** The Export Control Order 2008; Sanctions and Anti-Money Laundering Act 2018; OFSI guidance.
- **Singapore:** Strategic Goods (Control) Act 1993.
- **SOC 2 Trust Services Criteria (TSP Section 100, 2017):** Common Criteria 3 (Risk Assessment), 5 (Control Activities), 6 (Logical and Physical Access), and 7 (Monitoring Activities).

## 11. Revision History

| Version | Date | Author | Description of Changes | Approver |
| :--- | :--- | :--- | :--- | :--- |
| 2.3 | 2025-01-14 | Thomas Anderson, CCO | Annual periodic review. Updated SOC 2 control mapping table for CCM script. Added reference to new PDLC SOP. No substantive procedure changes. | Maria Gonzalez, GC |
| 2.2 | 2024-11-18 | Jane Doe, Sr. Mgr Trade | Major update: Added automated transactional lock procedure (Sec 6.1); Updated KRI for reconciliation to 100% (Sec 7.1); Implemented new AWS Lambda CCM script (Sec 6.1); Integrated new EU Dual-Use Regulation reference. | Thomas Anderson, CCO |
| 2.1 | 2024-07-12 | Jane Doe, Sr. Mgr Trade | Revised training frequencies from bi-annual to annual for core modules; Updated escalation path to include CEO/Audit Committee Chair (Sec 8.2); Added definitions for EU Dual-Use Regulation and ITAR (Sec 2). | Thomas Anderson, CCO |
| 2.0 | 2024-03-04 | William Smith, Sr. Mgr Trade | Comprehensive rewrite to align with SOC 2 Type II audit requirements. Introduced full control mapping matrix (Sec 6), detailed RACI chart (Sec 3), and formalized monitoring and metrics section with quantitative thresholds (Sec 7). | Thomas Anderson, CCO |
| 1.2 | 2023-09-20 | William Smith, Trade Analyst | Clarified deemed export procedure for Engineering roles; Added reference to Singapore Strategic Goods Act; Corrected minor typographical errors. | Jane Doe, Sr. Mgr Trade |
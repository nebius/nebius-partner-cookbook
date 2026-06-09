---
sop_id: "SOP-FIN-012"
title: "Collections and Recovery Procedures"
business_unit: "Financial Services"
version: "1.3"
effective_date: "2024-01-02"
last_reviewed: "2025-09-14"
next_review: "2026-03-06"
owner: "Robert Liu, VP of Financial Services"
approver: "James Thornton, Chief Financial Officer"
classification: "Internal"
regulations:
  - "GDPR"
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Collections and Recovery Procedures

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the standardized framework governing all accounts receivable management, collections activities, and recovery operations within Meridian Health Technologies' HealthPay Financial Services division. The purpose of this document is to define consistent, compliant, and ethical procedures for managing delinquent accounts, administering hardship assistance programs, executing recovery strategies, and tracking recovery performance across all operational jurisdictions. This SOP ensures that all collections activities comply with applicable regulatory requirements, maintain patient dignity and privacy, and optimize recovery outcomes while minimizing reputational and operational risk.

### 1.2 Scope

This SOP applies to:

| **In-Scope Activities** | **Out-of-Scope Activities** |
|--------------------------|-----------------------------|
| Patient financing repayment collections | Clinical billing disputes (handled by Customer Operations) |
| Medical lending portfolio delinquency management | Insurance claim denials and appeals |
| HealthPay payment plan default resolution | Provider reimbursement reconciliation |
| Pre-collections communication (30-180 days past due) | Initial account provisioning and underwriting |
| Formal collections placement (180+ days past due) | Fraud investigation and chargeback processing |
| Hardship program administration and eligibility | Tax credit or government subsidy determinations |
| Recovery payment processing and allocation | Third-party debt buyer negotiations (managed by Treasury) |
| Debt validation and dispute resolution | Litigation and legal judgments (managed by General Counsel) |
| Skip tracing and asset location activities | Bankruptcy case management (managed by Legal) |

### 1.3 Target Audience

This SOP is binding upon all Meridian employees, contractors, and third-party vendors engaged in collections, recovery, or related support functions, including but not limited to:

- HealthPay Financial Services Operations Team
- Customer Account Management Specialists
- Collections and Recovery Agents (internal and third-party)
- Payment Operations and Cash Application Team
- Compliance and Quality Assurance Personnel
- Data Analytics and Reporting Team supporting Collections
- Information Technology staff managing collections systems

### 1.4 Geographic and Regulatory Applicability

| **Jurisdiction** | **Applicable Regulations** | **Operational Region** |
|------------------|----------------------------|------------------------|
| United States (Federal) | Fair Debt Collection Practices Act (FDCPA), Fair Credit Reporting Act (FCRA), HIPAA, SR 11-7 | All US states and territories |
| United States (State) | State-specific debt collection licensing laws, usury limits, statute of limitations | Determined by patient residency |
| European Union | General Data Protection Regulation (GDPR), EU AI Act | All EU member states |
| United Kingdom | UK GDPR, Financial Conduct Authority (FCA) Consumer Duty | England, Scotland, Wales, Northern Ireland |
| Canada | Personal Information Protection and Electronic Documents Act (PIPEDA), provincial health privacy laws | All provinces and territories |
| Germany | Bundesdatenschutzgesetz (BDSG), specific patient data protections | EU operations primarily managed from Berlin office |

---

## 2. Definitions and Acronyms

### 2.1 General Definitions

| **Term** | **Definition** |
|----------|----------------|
| **Account Owner** | The individual legally responsible for repayment of a HealthPay financial obligation |
| **Adverse Action** | Any action that negatively affects an account owner, including reporting to credit bureaus, placing accounts with external collections agencies, or initiating legal proceedings |
| **Charge-off** | The accounting determination that an account is unlikely to be collected, resulting in removal from active receivables (occurs at 180 days past due unless otherwise specified by product terms) |
| **Cure Period** | The timeframe during which an account owner may bring a delinquent account current without escalation (varies by product, typically 15-30 days from initial delinquency) |
| **Delinquency Bucket** | Classification of accounts by days past due (DPD): Current (0 DPD), Early (1-30 DPD), Moderate (31-60 DPD), Advanced (61-90 DPD), Severe (91-179 DPD), Charge-off (180+ DPD) |
| **Forbearance** | Temporary suspension or reduction of payment obligations for a defined period due to documented hardship |
| **Hardship Program** | Structured alternative repayment arrangement approved for account owners experiencing documented financial difficulty |
| **Payment Plan Restructure** | Modification of existing payment plan terms including extended duration, reduced periodic payment amounts, or temporary interest rate reduction |
| **Right to Cure Notice** | Written communication sent to account owners providing formal notification of default and the opportunity to remedy within a specified timeframe |
| **Skip Tracing** | Investigative process to locate account owners when contact information on file is no longer valid |
| **Workout Plan** | Customized resolution strategy for severely delinquent accounts, potentially including settlement offers or structured repayment schedules |

### 2.2 Acronyms

| **Acronym** | **Full Form** |
|-------------|---------------|
| ACH | Automated Clearing House |
| AOD | Acknowledgment of Debt |
| CFPB | Consumer Financial Protection Bureau |
| CMS | Collections Management System (Meridian internal system: HealthPay Collect) |
| CRA | Credit Reporting Agency |
| DPD | Days Past Due |
| DPO | Data Protection Officer |
| DSAR | Data Subject Access Request (GDPR) |
| FDCPA | Fair Debt Collection Practices Act |
| FICO | Fair Isaac Corporation (credit scoring) |
| GDPR | General Data Protection Regulation |
| HIPAA | Health Insurance Portability and Accountability Act |
| IVR | Interactive Voice Response |
| KPI | Key Performance Indicator |
| LGD | Loss Given Default |
| MRC | Model Risk Committee |
| NIST AI RMF | National Institute of Standards and Technology Artificial Intelligence Risk Management Framework |
| PHI | Protected Health Information |
| PIF | Paid in Full |
| PIPEDA | Personal Information Protection and Electronic Documents Act |
| PII | Personally Identifiable Information |
| QA | Quality Assurance |
| RC | Recovery Coordinator |
| SLA | Service Level Agreement |
| SOP | Standard Operating Procedure |
| TPV | Third-Party Vendor |

---

## 3. Roles and Responsibilities

### 3.1 RACI Matrix

| **Role / Function** | **RACI Code** | **Key Responsibilities** |
|---------------------|---------------|--------------------------|
| VP of Financial Services (Robert Liu) | **A** - Accountable | Ultimate accountability for collections strategy, recovery performance, regulatory compliance, and model risk management |
| Director of Collections Operations | **R** - Responsible | Day-to-day management of collections operations, team supervision, strategy execution, vendor oversight |
| Collections Agents (Internal) | **R** - Responsible | Direct account owner communication, negotiation of payment arrangements, accurate system documentation, adherence to scripts and compliance protocols |
| Recovery Coordinators | **R** - Responsible | Management of severely delinquent accounts (120+ DPD), external agency placement, settlement negotiations, skip tracing activities |
| Payment Operations Team | **R** - Responsible | Payment processing, cash application, reconciliation of recovery payments, maintenance of payment allocation logic |
| Compliance Officer - Financial Services | **C** - Consulted | Regulatory interpretation, QA program oversight, incident investigation, training content approval |
| Data Protection Officer (DPO) | **C** - Consulted | GDPR compliance guidance, DSAR processing oversight, data protection impact assessments for collections systems |
| Chief Financial Officer (James Thornton) | **A** - Accountable | Enterprise-level accountability for financial controls, charge-off approval thresholds above $500,000 aggregate |
| Chief Privacy Officer | **C** - Consulted | HIPAA compliance guidance for PHI handling in collections context, patient privacy impact assessments |
| General Counsel | **C** - Consulted | Legal action approval, regulatory examination response, settlement authority above defined thresholds |
| Model Risk Committee (MRC) | **C** - Consulted | Review and approval of collections scoring models, AI/ML model governance per SR 11-7 and NIST AI RMF |
| Customer Account Management Team | **I** - Informed | Notification of accounts transitioning to formal collections, awareness of recovery status for account owner inquiries |
| Third-Party Collection Agencies | **R** - Responsible | External recovery activities per contractual requirements, adherence to Meridian compliance standards, accurate reporting |
| IT Application Support | **I** - Informed | System issue notifications, data export requirements, integration maintenance |

### 3.2 Authority Delegation

| **Decision Type** | **Authority Threshold** | **Required Approval** |
|-------------------|-------------------------|----------------------|
| Standard payment plan restructure | Up to 12-month term extension | Collections Agent (documented in CMS) |
| Extended payment plan restructure | 12-24 month term extension | Team Lead, Collections Operations |
| Hardship program enrollment | Per standard eligibility | Collections Agent Level II or higher |
| Settlement offer | Up to 25% principal reduction | Director of Collections Operations |
| Settlement offer | 25-50% principal reduction | VP of Financial Services |
| Settlement offer | >50% principal reduction or >$50,000 | VP of Financial Services + CFO |
| Charge-off determination | Standard 180 DPD | Automated per system rules |
| Charge-off determination | Early (<180 DPD) | Director of Collections Operations |
| External agency placement | Routine placement | Director of Collections Operations |
| Legal action referral | Any | VP of Financial Services + General Counsel |
| Credit bureau deletion request | Any | Compliance Officer + Director of Collections Operations |

---

## 4. Policy Statements

### 4.1 Ethical Collections Principles

Meridian Health Technologies is committed to conducting all collections and recovery activities with integrity, respect, and transparency. All communications and actions shall:

- Treat all account owners with dignity and respect, recognizing the sensitive nature of healthcare financing
- Provide clear, accurate, and complete information regarding account status, available options, and potential consequences
- Never employ harassment, oppression, or abuse in any communication
- Maintain strict confidentiality of Protected Health Information (PHI) and Personally Identifiable Information (PII)
- Honor all commitments made to account owners, including hardship program terms and settlement agreements
- Ensure all communications are accessible and understandable to account owners regardless of language proficiency or disability status (translation and accessibility services available upon request)

### 4.2 Regulatory Compliance Commitment

All collections operations shall comply with applicable federal, state, and international regulations including but not limited to:

| **Regulation** | **Key Compliance Commitments** |
|----------------|-------------------------------|
| FDCPA (15 USC §1692-1692p) | Prohibition on harassment, false representations, and unfair practices; validation of debts; cease communication upon written request; time/place restrictions on communications |
| FCRA (15 USC §1681) | Duties of furnishers of information to credit reporting agencies; accuracy and integrity of furnished information; dispute investigation procedures; adverse action notifications |
| HIPAA Privacy Rule (45 CFR §164) | Minimum necessary standard for PHI disclosure; restrictions on use of PHI for payment purposes; accounting of disclosures; patient rights regarding PHI |
| GDPR (EU Regulation 2016/679) | Lawful basis for processing (Article 6); explicit consent where required (Article 7); Data Protection Impact Assessments for high-risk processing (Article 35); Data Subject rights including access, rectification, erasure, and restriction (Articles 15-18, 21); Data breach notification (Articles 33-34); Records of processing activities (Article 30); Data Protection by Design and Default (Article 25) |
| CFPB Regulation F (12 CFR Part 1006) | Model validation notice; limited content messages; call frequency presumptions; consumer cease communication requests |
| State Debt Collection Licensing | Maintenance of required state licenses; timely renewal; notification of material changes to licensing authorities |
| FCA Consumer Duty (UK) | Act to deliver good outcomes for retail customers; products and services designed to meet needs; consumer understanding; consumer support |

### 4.3 Data Protection and Privacy (GDPR Article-Specific Controls)

This section provides thorough GDPR compliance controls specific to collections activities involving EU/UK data subjects.

#### Article 6: Lawfulness of Processing

| **Processing Activity** | **Lawful Basis** | **Justification** |
|-------------------------|------------------|-------------------|
| Contacting account owner for payment | Article 6(1)(b) - Contractual necessity | Performance of the lending agreement to which the data subject is party |
| Skip tracing to locate account owner | Article 6(1)(f) - Legitimate interests | Meridian's legitimate interest in recovering owed amounts, balanced against data subject's rights |
| Reporting to credit reference agencies | Article 6(1)(f) - Legitimate interests with legitimate interest assessment (LIA) documented | Necessity of accurate credit reporting; LIA reviewed quarterly by DPO |
| Automated decision-making (risk scoring) | Article 6(1)(f) with Article 22 safeguards | Documented legitimate interest with human intervention rights preserved; MRC-reviewed models |
| Processing special category data (health data in hardship context) | Article 9(2)(a) - Explicit consent | Separate explicit consent obtained at hardship application; not bundled with general terms |

#### Article 7: Conditions for Consent

Where consent serves as the lawful basis (particularly hardship program health information processing):

- Consent request presented in clear, plain language, separate from other terms and conditions
- Account owner informed of right to withdraw consent at any time without detriment to core collections arrangements
- Consent withdrawal mechanism available via: HealthPay portal, written request to Berlin Privacy Office, or verbal request documented in CMS
- Consent records maintained with timestamp, IP address, consent text version, and method of consent capture
- Annual consent refresh for ongoing hardship programs requiring continued health data processing
- Consent audit trail maintained in CMS; quarterly audit by Compliance Officer

#### Article 15: Right of Access by Data Subject

Account owners within GDPR jurisdiction have the right to obtain confirmation of whether Meridian processes their personal data and access to that data. Controls:

- DSAR intake points: dedicated email (privacy@meridianhealth.com), Berlin office postal address, online portal form
- Response SLA: within 30 calendar days of verified request receipt (extendable by additional 60 days for complex/multiple requests per Article 12(3))
- Identity verification: Two-factor verification required before DSAR fulfillment (knowledge-based + possession-based factor)
- DSAR response package includes: categories of personal data processed, purposes of processing, categories of recipients (including CRAs and external agencies named specifically), retention periods or criteria, existence of automated decision-making including meaningful logic information
- DSAR log maintained by DPO; quarterly reporting to VP of Financial Services on DSAR volume, response timeliness, and outcomes
- DSAR fulfillment coordinated by Privacy Team with Collections Operations providing account-specific data extraction

#### Article 16: Right to Rectification

Account owners may request correction of inaccurate personal data:

- Rectification requests triaged within 5 business days
- Substantiated corrections completed within 10 business days of verification
- If data has been disclosed to third parties (CRAs, external agencies), Meridian communicates rectification to each recipient unless impossible or disproportionate effort
- Account owner notified of recipients informed of rectification
- Disputed account data flagged in CMS with "DISPUTE-RECTIFICATION PENDING" marker; collections activities suspended during investigation of rectification request when dispute materially affects alleged obligation

#### Article 17: Right to Erasure ("Right to be Forgotten")

Erasure requests evaluated per Article 17 conditions:

- **Applicable circumstances**: Data no longer necessary for original purpose; consent withdrawn (and no other legal basis); data subject objects and no overriding legitimate grounds; data unlawfully processed
- **Limitations**: Erasure right NOT absolute where processing necessary for: exercise or defense of legal claims; compliance with legal obligation (e.g., statutory record retention requirements under financial services regulations)
- **Evaluation workflow**: DPO evaluates erasure request within 30 days; if denied, comprehensive written explanation provided to account owner citing specific Article 17(3) exception
- **Partial erasure**: Where full erasure not applicable, Meridian implements data minimization by archiving non-essential data, restricting access to essential retention data, and ceasing active processing
- **Metrics**: Number of erasure requests, approval/denial ratio, and justification categories tracked monthly

#### Article 18: Right to Restriction of Processing

Processing restriction applies while Meridian verifies accuracy of contested data or evaluates objection to processing:

- "PROCESSING-RESTRICTED" flag in CMS prevents all automated and manual processing EXCEPT storage
- Restricted accounts excluded from all collections communications, credit reporting updates, and external agency placement
- Flag duration: until verification/evaluation complete (SLA: 15 business days maximum)
- Account owner notified of restriction commencement, duration, and lifting

#### Article 21: Right to Object

Account owners may object to processing based on legitimate interests:

- Objection evaluated by DPO in consultation with VP of Financial Services; written response provided within 30 days
- If objection upheld, processing ceases for specified activities
- If objection overridden, compelling legitimate grounds documented with specific reference to balance of interests assessment
- Collections activities suspended during evaluation period (risk of statute of limitations tolling evaluated by Legal)

#### Article 22: Automated Individual Decision-Making

Collections scoring and delinquency prediction models constitute automated decision-making:

- Account owners notified of automated decision-making at account origination (Privacy Notice) and in all collections-related communications
- Right to human intervention: Any account owner subject to automated adverse decision (e.g., risk-based routing to accelerated collections pathway) may request human review
- Human review conducted by Collections Team Lead Level III within 10 business days
- Human reviewer has authority to override automated decision with documented rationale
- Model logic transparency: Meaningful information about the logic involved provided upon request (excluding proprietary model weights; but including factors considered, relative importance categories, and outcome ranges)
- All collections scoring models reviewed quarterly by MRC per SR 11-7 and NIST AI RMF requirements

#### Article 25: Data Protection by Design and Default

- Data minimization: Collections communications systems configured to access only data fields strictly necessary for the specific communication purpose; full account data accessible only with documented business need
- Retention default: By default, personal data retained only for legal/regulatory obligation periods; longer retention requires active opt-in justification approved by DPO
- Pseudonymization: Collections analytics datasets pseudonymized where possible; re-identification restricted to authorized personnel with documented purpose
- System design: HealthPay Collect CMS designed with privacy controls embedded; access controls per least-privilege principle; audit logging of all personal data access

#### Article 30: Records of Processing Activities

- Records maintained for all collections processing activities involving EU/UK personal data
- Entries include: name and contact details of controller (Meridian Health Technologies) and DPO; purposes of processing; categories of data subjects and personal data; categories of recipients (including CRAs: Equifax, Experian, TransUnion; external agencies named specifically); international transfer documentation; retention schedules; technical and organizational security measures
- Records reviewed and updated quarterly; maintained in permanent form (Meridian GRC platform: Archer)
- Available to supervisory authorities upon request

#### Article 33-34: Personal Data Breach Notification

- Breach detection: SIEM monitoring of CMS and related systems; anomalous access pattern alerts
- Breach assessment: DPO-led assessment within 24 hours of detection; determination of risk to data subject rights and freedoms
- Supervisory authority notification: Within 72 hours of becoming aware of notifiable breach (Article 33)
- Data subject notification: Without undue delay where breach likely to result in high risk (Article 34); clear and plain language communication; description of nature of breach; likely consequences; measures taken or proposed; recommendations for data subject mitigation
- Breach documentation: All breaches documented regardless of notification obligation; internal investigation reports retained permanently

#### Article 35: Data Protection Impact Assessment (DPIA)

- DPIA performed for: implementation of new collections scoring models; deployment of automated dialer/communication systems processing EU data; external agency data sharing arrangements; skip tracing operations involving EU data subjects
- DPIA includes: systematic description of processing; necessity and proportionality assessment; risk assessment; mitigation measures
- DPO consultation required for all DPIAs
- DPIA reviewed: prior to processing; annually thereafter; upon material system or process change
- Current collections DPIAs: Collections Automated Dialer DPIA (2023-004); External Agency Data Transfer DPIA (2023-007); Skip Tracing Operations DPIA (2024-002)

### 4.4 SOC 2 Trust Services Criteria Controls

This section provides thorough SOC 2 controls aligned with the Trust Services Criteria (TSC) relevant to collections operations.

#### Security (Common Criteria - CC Series)

| **Control ID** | **Control Description** | **Implementation Detail** |
|----------------|------------------------|---------------------------|
| CC6.1-SEC-001 | Logical access controls for CMS | HealthPay Collect CMS authenticated via Meridian SSO with MFA required; role-based access control (RBAC) enforced with granular permission sets |
| CC6.1-SEC-002 | Network segmentation | Collections systems reside in dedicated VLAN segment (FIN-COLL-ZONE) with firewall rules restricting traffic to/from general Meridian corporate network; access restricted to authorized personnel |
| CC6.1-SEC-003 | Privileged access management | CMS administrator accounts (4 total: 2 primary, 2 backup) require separate privileged access workstation (PAW); all privileged session activities logged and reviewed monthly by IT Security |
| CC6.2-SEC-004 | Access provisioning and deprovisioning | Collections system access provisioned via ServiceNow workflow requiring VP of Financial Services or delegate approval; access reviewed quarterly via user access review (UAR); deprovisioning within 24 hours of termination/role change |
| CC6.3-SEC-005 | Vendor access controls | Third-party collection agencies access Meridian data via dedicated API gateway with unique credentials; VPN tunnel with IP restriction; session timeout after 15 minutes idle; activity logged to SIEM |
| CC7.1-SEC-006 | Vulnerability management | CMS vulnerability scans performed weekly; critical vulnerabilities remediated within 7 days, high within 30 days; penetration testing annually (external firm: CyberGuard Partners) |
| CC7.2-SEC-007 | Security monitoring and alerting | SIEM (Splunk) monitoring of CMS with alert rules for: multiple failed login attempts (>5 in 5 minutes), off-hours access, anomalous data export volumes, privilege escalation attempts |
| CC8.1-SEC-008 | Change management | CMS changes follow Meridian Change Management Policy (SOP-IT-005); peer review of code changes; change advisory board (CAB) approval for production deployment; rollback plan documented |
| CC9.1-SEC-009 | Risk assessment | Collections-specific risk assessment performed annually and upon material operational changes; risks logged in Meridian GRC platform (Archer); treatment plans assigned to risk owner (VP of Financial Services) |

#### Availability

| **Control ID** | **Control Description** | **Implementation Detail** |
|----------------|------------------------|---------------------------|
| A1.1-AVAIL-001 | CMS availability monitoring | HealthPay Collect CMS monitored 24/7 via Nagios; uptime target 99.9% (excluding planned maintenance); alert escalation: L1 NOC → L2 Infrastructure within 5 minutes if not acknowledged |
| A1.2-AVAIL-002 | Disaster recovery | CMS disaster recovery plan documented; RPO: 1 hour; RTO: 4 hours; DR test performed semi-annually with documented results and remediation items |
| A1.3-AVAIL-003 | Capacity management | CMS infrastructure capacity reviewed monthly; thresholds: CPU <75% sustained, storage <80% utilized, concurrent user capacity >110% of peak historical |

#### Processing Integrity

| **Control ID** | **Control Description** | **Implementation Detail** |
|----------------|------------------------|---------------------------|
| PI1.1-PROC-001 | Payment processing accuracy | Daily reconciliation of payment transactions between CMS and general ledger (Oracle Fusion); reconciliation variance investigation threshold: >$100 or >0.1% of daily volume; reconciliation completed by 12:00 ET next business day |
| PI1.2-PROC-002 | Data input validation | CMS validates all manual data entries including: payment amounts (positive, ≤ total outstanding), settlement figures (within delegation authority), payment plan terms (duration ≤24 months without approval override) |
| PI1.3-PROC-003 | Processing monitoring | Daily operations checklist completed by Collections Operations Team Lead: system availability verified, batch jobs completed, interface files processed, critical reports generated. Checklist logged in Jira Operations |

#### Confidentiality

| **Control ID** | **Control Description** | **Implementation Detail** |
|----------------|------------------------|---------------------------|
| C1.1-CONF-001 | Data classification and handling | Collections data classified as "Confidential - Personal Financial & Health Data" per Meridian Data Classification Standard (SOP-IS-003); handling controls: encrypted at rest (AES-256) and in transit (TLS 1.2+), restricted to authorized personnel, no export to unmanaged devices |
| C1.2-CONF-002 | Data disposal | Account data retained per retention schedule (Section 6.5); disposal via NIST 800-88 compliant sanitization (cryptographic erase for cloud storage, secure wipe utilities for on-premise); disposal certificate maintained |
| C1.3-CONF-003 | Confidentiality agreements | All personnel accessing collections data sign Meridian Confidentiality Agreement; annual re-affirmation; violation consequences up to and including termination and legal action |

#### Privacy (SOC 2 Supplemental Criteria)

| **Control ID** | **Control Description** | **Implementation Detail** |
|----------------|------------------------|---------------------------|
| P1.1-PRIV-001 | Privacy notice provision | Account owners provided Meridian Privacy Notice at account origination and annually thereafter; notice describes: categories of personal information collected, purposes of use, categories of third-party disclosure, account owner rights, contact information for Privacy Office, data retention periods |
| P2.1-PRIV-002 | Consent and choice | Opt-in consent for non-essential data uses (marketing, data sharing beyond collections purpose); withdrawal mechanism provided (privacy portal, toll-free number, written request); withdrawal processed within 5 business days |
| P3.1-PRIV-003 | Collection limitation | Collections personnel collect only personal information specified as necessary for collections function; field limitations enforced in CMS; new data collection fields require Privacy Impact Assessment |
| P4.1-PRIV-004 | Use, retention, and disposal limitation | Personal data used only for specified purposes; retention per defined schedule; disposal per C1.2-CONF-002 |
| P5.1-PRIV-005 | Access and disclosure | Account owner access to personal data per SOP-PRIV-001 (Data Subject Access Requests); disclosures to third parties logged; quarterly review of disclosure logs by Privacy Office |
| P6.1-PRIV-006 | Quality and accuracy | Periodic review of data accuracy: address verification via USPS NCOA-Link quarterly; phone validation upon account contact; dispute investigation per SOP-FIN-003 |
| P7.1-PRIV-007 | Monitoring and enforcement | Annual privacy compliance audit of collections operations; results reported to Chief Privacy Officer and VP of Financial Services; remediation plans for findings |

---

## 5. Detailed Procedures

### 5.1 Pre-Collections Strategy (1-30 Days Past Due)

#### 5.1.1 Communication Cadence

| **Day** | **Communication Method** | **System** | **Message Purpose** |
|---------|-------------------------|------------|---------------------|
| D+1 | Email (automated) | HealthPay CMS - Email Module | Payment reminder; link to payment portal; contact information for Customer Account Management |
| D+7 | SMS/Text (if opted in) | HealthPay CMS - SMS Gateway | Brief payment reminder; link to payment portal (no account details in SMS per SOP-FIN-009) |
| D+14 | Email (automated) | HealthPay CMS - Email Module | Second reminder with escalation language; available assistance options; link to Hardship Program application |
| D+21 | Letter (USPS) / Email (EU) | HealthPay CMS - Document Generation | Formal notice per product terms; statement of account; Right to Cure notice if applicable |
| D+28 | Outbound call attempt 1 | HealthPay CMS - Dialer Module | Personal contact; discussion of repayment options; verification of contact information |

**Communication Controls:**

- **Attempt Limits:** Maximum 7 communication attempts (all methods combined) per 7-day period per account owner per SOP-FDCPA-001
- **Time Restrictions:** No communications before 8:00 AM or after 9:00 PM account owner local time
- **Workplace Contact:** Workplace contact only if: (1) home contact information unavailable, (2) reasonable belief account owner cannot be contacted at home, or (3) account owner has provided workplace contact preference. No workplace contact if account owner indicates employer prohibits such communications.
- **Representation by Counsel:** All communications cease upon notification that account owner is represented by counsel; all communications directed to attorney

#### 5.1.2 Account Work Queue Assignment

Upon entry into pre-collections (DPD 1), accounts are automatically assigned to work queues based on the following criteria:

| **Queue Name** | **Assignment Criteria** | **Agent Ratio** (Accounts:Agent) |
|----------------|------------------------|----------------------------------|
| PREM-STD | Standard accounts; balance <$5,000; no prior delinquency | 500:1 |
| PREM-HIGH | High-balance accounts (>$5,000); automated communication preference | 250:1 |
| PREM-VIP | Healthcare professional financing accounts; special handling protocol | 100:1 |
| PREM-RISK | Prior delinquency within last 24 months; credit score decline >50 points since origination | 300:1 |
| PREM-EU | EU/UK jurisdiction accounts; GDPR-specific handling requirements | 200:1 |
| PREM-CAN | Canada jurisdiction accounts; PIPEDA-specific handling requirements | 200:1 |

Accounts must be worked in priority order: highest balance within oldest DPD first.

### 5.2 Early-Stage Collections (31-60 Days Past Due)

#### 5.2.1 Enhanced Communication Protocol

At DPD 31, accounts transition from pre-collections automated communications to active collections management:

| **DPD** | **Action** | **Responsible Role** | **Required Documentation** |
|---------|------------|----------------------|----------------------------|
| 31 | Account reviewed by assigned agent; payment history analysis; contact strategy updated | Collections Agent Level I | Contact log entry in CMS |
| 35 | Outbound call attempt (if no contact established) | Collections Agent Level I | Call disposition logged |
| 38 | Personalized email with specific payment options; link to payment plan calculator | Collections Agent Level I | Email template logged |
| 42 | Second outbound call; escalation to Team Lead if no contact | Collections Agent Level II | Supervisor review note |
| 45 | Physical letter (Right to Cure Notice if state law requires) | Collections Agent Level II | Letter template ID logged |
| 52 | Final outreach before escalation; documented in CMS | Collections Agent Level II | Final contact attempt note |
| 60 | Account escalation review; determination of next delinquency bucket strategy | Team Lead, Collections | Escalation decision documented |

#### 5.2.2 Payment Arrangement Options (31-60 Days)

During early-stage collections, agents may offer the following standard arrangements:

| **Option** | **Terms** | **Eligibility** | **Agent Authority** |
|------------|-----------|-----------------|---------------------|
| Bring Current (Cure) | Payment of total past-due amount within 15 days | Any account | Direct |
| 3-Month Catch-Up Plan | Past-due amount divided into 3 equal installments added to regular payment | First delinquency event in 24 months | Direct |
| Short-Term Forbearance (30-Day) | One month payment suspension; interest continues to accrue | Documented temporary hardship (medical event, job loss) | Requires Team Lead approval |
| Reduced Payment (3-Month) | Minimum 50% of contractual payment for 3 months; balance deferred | Demonstrated financial hardship | Requires Team Lead approval |

#### 5.2.3 Documentation Requirements

All collections interactions must be documented in CMS within 24 hours of contact or attempt. Documentation must include:
- Date, time, and method of communication
- Name of Meridian agent and account owner contacted (or notation of attempt)
- Summary of conversation including account owner representations
- Payment arrangements proposed and accepted/declined
- Next action and scheduled follow-up date
- Any dispute raised by account owner (requires immediate flagging per Section 8)

### 5.3 Mid-Stage Collections (61-90 Days Past Due)

#### 5.3.1 Escalation Communication Protocol

| **DPD** | **Action** | **Responsible Role** | **Escalation Indicator** |
|---------|------------|----------------------|--------------------------|
| 61 | Account re-assigned to Collections Agent Level II | Supervisor Assignment | Queue transfer logged |
| 63 | Comprehensive account review; previous contact attempts analysis | Collections Agent Level II | Account strategy document |
| 65 | Direct supervisor call attempt; manager escalation notification | Team Lead, Collections | Manager involvement flag |
| 70 | Formal Notice of Default letter sent (certified mail if regulatory requirement applies) | Collections Agent Level II | Letter tracking number logged |
| 75 | Hardship program eligibility evaluation; application solicitation | Collections Agent Level II | Hardship flag if discussed |
| 80 | Final voluntary resolution outreach; notification of impending escalation consequences | Collections Agent Level II | Consequences disclosure logged |
| 85 | Pre-legal review (accounts >$10,000 or specific risk criteria) | Director of Collections Operations | Legal referral flag if criteria met |
| 90 | Account moves to Advanced Collections (91+) or Hardship Program enrollment confirmed | Collections Agent Level II | Delinquency bucket transition logged |

#### 5.3.2 Hardship Program Administration

Account owners experiencing genuine financial difficulty may qualify for the Meridian HealthPay Hardship Assistance Program:

**Eligibility Criteria:**
- Documented hardship event: job loss, reduction in income (>25%), significant medical expenses, divorce, death of primary earner, natural disaster impact
- Account not previously in hardship program within prior 12 months (exceptions for documented new hardship)
- Account owner demonstrates willingness and ability to meet modified payment terms
- Account owner completes Hardship Application (Form HAP-001) with supporting documentation

**Application Process:**
1. **Initiation:** Account owner expresses hardship or agent identifies potential hardship indicators during collections interaction
2. **Application Provision:** Agent provides Hardship Application via preferred method (email link to portal, physical mail)
3. **Documentation Submission:** Account owner submits application with supporting documentation:
   - Income verification: last 2 pay stubs, unemployment benefit statement, or affidavit of income
   - Hardship documentation: termination letter, medical bills (>$5,000), divorce decree, disaster declaration, or similar
   - Expense statement: standardized Hardship Financial Statement (Form HAP-002)
4. **Application Review:** Collections Agent Level II reviews within 5 business days of complete submission
5. **Decision:** 
   - **Approval:** Standard hardship plan terms applied (see below); written agreement (Hardship Agreement Form HAP-003) executed via DocuSign
   - **Conditional Approval:** Modified terms may require Team Lead approval
   - **Denial:** Written explanation provided; alternative payment arrangements offered
6. **Appeal:** Account owner may appeal denial within 15 calendar days; appeal reviewed by Director of Collections Operations; decision final

**Standard Hardship Plan Terms:**

| **Hardship Tier** | **Criteria** | **Terms** | **Maximum Duration** |
|-------------------|--------------|-----------|----------------------|
| Tier 1: Temporary | Income reduction 25-50%; expected recovery within 6 months | 50% payment reduction; interest continues at 50% of contractual rate | 6 months |
| Tier 2: Extended | Income reduction >50%; recovery timeline uncertain | 75% payment reduction or payment suspension; interest continues at 25% of contractual rate | 12 months |
| Tier 3: Severe | Complete loss of income; no foreseeable recovery | Full payment suspension; interest frozen | 6 months (requires re-certification) |
| Tier 4: Permanent | Permanent disability; fixed income insufficient for original terms | Payment restructure with extended amortization (up to 60 months); interest rate reduction per policy | Life of loan restructure |

**Hardship Program Monitoring:**
- Tier 1 and 2: Monthly status check-in; automated payment confirmation
- Tier 3: Bi-monthly status check; re-certification at month 3 and month 6
- Tier 4: Quarterly reviews; annual re-certification
- All hardship accounts flagged in CMS with "HARDSHIP-ACTIVE" and tier designation; excluded from standard collections communication cadence

### 5.4 Advanced Collections (91-179 Days Past Due)

#### 5.4.1 High-Intensity Recovery Protocol

| **DPD** | **Action** | **Responsible Role** | **Documentation** |
|---------|------------|----------------------|-------------------|
| 91 | Full skip trace (if contact lost); comprehensive asset/location investigation | Recovery Coordinator | Skip trace report logged to CMS |
| 100 | Formal demand letter; 30-day notice of intent to escalate to formal collections | Recovery Coordinator | Demand letter ID; delivery confirmation |
| 105 | Settlement evaluation: LGD model run; settlement range calculated | Recovery Coordinator | Model output attached to account |
| 110 | Settlement offer communication (if authorized per delegation) | Recovery Coordinator | Offer details logged; expiration 30 days |
| 120 | External agency placement preparation; due diligence review; agency selection | Director of Collections Operations | Agency placement approval |
| 130 | Account transferred to external agency (if no resolution); placement documentation | Recovery Coordinator | Agency referral package logged |
| 150 | Agency performance review; escalation to secondary agency if no progress | Director of Collections Operations | Agency review form |
| 170 | Final recovery assessment: charge-off recommendation or litigation referral | Director of Collections Operations | Final recommendation to VP |
| 180 | Charge-off (system automated) OR litigation referral (if approved) | VP of Financial Services | Charge-off or litigation authorization |

#### 5.4.2 Skip Tracing Procedures

When account owner contact information is no longer valid, skip tracing is initiated following these procedures:

**Authorized Skip Tracing Sources:**
- Credit reporting agency updated address information (soft pull only; permissible purpose per FCRA §604(a)(3)(A))
- USPS National Change of Address (NCOA) database
- Public records search (property records, professional licensing)
- Social media public profiles (limited to locating contact information; no account-specific communications via social media - ABSOLUTE PROHIBITION)
- Alternative contact numbers provided at account origination

**Prohibited Skip Tracing Activities:**
- Contact with employer beyond confirming employment status and location (no disclosure of debt)
- Communication with family members, friends, or neighbors beyond confirming location (no disclosure of debt to any third party - FDCPA §805(b))
- Pretext calling or misrepresentation of identity
- Accessing credit reports without permissible purpose
- Any GDPR jurisdiction skip tracing beyond publicly available information (restricted per Article 6 legitimate interest assessment)

**Skip Tracing Documentation:**
- All skip trace activities logged to CMS Skip Trace Module
- Sources utilized identified
- Information obtained documented
- Date and agent name recorded
- Skip trace success/failure outcome logged

#### 5.4.3 Settlement Procedures

Settlements offer resolution of delinquent accounts for less than full balance. All settlements must:

1. **Settlement Calculation:**
   - LGD model run to determine expected recovery
   - Settlement floor: 40% of outstanding principal for accounts 120+ DPD (exceptions require VP approval)
   - Settlement must be documented as full and final resolution
   - Tax reporting consequences communicated to account owner (Form 1099-C may be issued for forgiven amounts exceeding $600)

2. **Settlement Agreement Terms:**
   - Lump-sum payment due within 30 days of agreement execution OR
   - Structured settlement: up to 3 equal monthly payments (total duration ≤90 days)
   - Default on settlement agreement voids agreement and reinstates full balance (minus payments received)
   - Agreement documented in Settlement and Release Agreement (Form SET-001)
   - Executed via DocuSign; executed agreement stored in CMS Document Repository

3. **Settlement Approval Workflow:**
   - Agent prepares settlement proposal using CMS Settlement Calculator
   - Proposal reviewed by Team Lead (within delegation)
   - If within delegation: Team Lead approval logged
   - If exceeding delegation: Routed to Director/VP per Approval Delegation Matrix (Section 3.2)
   - Settlement offer communicated to account owner; expiration 30 days
   - Accepted settlements: Payment processing monitored; upon PIF per settlement, account closed-settled

### 5.5 External Agency Management

#### 5.5.1 Agency Selection and Onboarding

Third-party collection agencies must meet Meridian's rigorous selection criteria:

| **Criteria** | **Requirement** | **Verification Method** |
|--------------|-----------------|------------------------|
| Licensing | Valid debt collection licenses in all jurisdictions where Meridian accounts will be placed | License verification; quarterly re-verification |
| Insurance | Errors & Omissions coverage ≥$5M; Cyber liability ≥$10M; evidence of PHI coverage | Certificate of Insurance; annual renewal verification |
| Data Security | SOC 2 Type II report (clean opinion); ISO 27001 certification or equivalent; annual penetration test results | Report review by Meridian Information Security |
| Compliance Program | FDCPA compliance program; documented consumer complaint handling; CFPB complaint history reviewed | Compliance program assessment; CFPB portal review |
| Data Handling | Ability to meet GDPR data processor requirements; EU Standard Contractual Clauses executed if EU data processed | Data Processing Agreement (DPA) with SCCs |
| Financial Stability | Annual financial review; bonding if significant recovery volumes | Annual review by Vendor Management Office |
| Performance References | Minimum 3 healthcare financing client references; recovery performance data | Reference checks; performance data analysis |

**Agency Contracting Requirements:**
- Data Processing Agreement (DPA) executed per GDPR Article 28 requirements
- Business Associate Agreement (BAA) executed per HIPAA requirements (if agency may encounter PHI)
- Service Level Agreement with performance metrics defined
- Audit rights: Meridian retains right to conduct on-site audits with 30 days' notice; for-cause audits with 48 hours' notice
- Data breach notification: Agency must notify Meridian within 4 hours of confirmed breach
- Data return/destruction: Upon contract termination, all Meridian data returned or destroyed with certificate of destruction within 30 days

#### 5.5.2 Agency Placement and Oversight

**Placement Process:**
1. Account identified for placement per 5.4 criteria
2. Placement package prepared: account summary, payment history, contact information, balance verification
3. Secure file transfer to agency (SFTP with PGP encryption; API integration for high-volume agencies)
4. Placement acknowledgment received within 2 business days
5. Agency assigns account to collector within 5 business days

**Oversight Requirements:**
- **Weekly:** Agency submits placement activity report (accounts placed, contacts made, promises secured, payments received)
- **Monthly:** Agency performance review against SLA metrics; Meridian Collections Agency Manager conducts call monitoring (minimum 10 calls/month per agency)
- **Quarterly:** Comprehensive agency review including: recovery rate, liquidation rate, consumer complaint ratio, compliance audit findings, data security attestation
- **Annually:** Full agency audit: on-site visit, compliance program review, financial review, SOC 2 review

**Agency Communication Standards:**
All agencies must adhere to Meridian's Communication Policy (SOP-FIN-009) including:
- Call attempt limits: 7 attempts per 7-day period
- Time restrictions: 8:00 AM - 9:00 PM local time
- No communication via social media
- All communications documented and available for Meridian review
- Account owner disputes immediately communicated to Meridian
- Cease communication requests honored immediately

### 5.6 Recovery Payment Processing

#### 5.6.1 Payment Allocation Logic

Recovery payments received (via agency collection, direct payment during collections, or settlement proceeds) are allocated in the following order per Meridian Payment Allocation Policy (SOP-FIN-006):

| **Priority** | **Allocation Category** | **Detail** |
|-------------|------------------------|------------|
| 1 | External collection costs | If applicable and contractually permitted |
| 2 | Accrued interest | Contractual rate, calculated to payment receipt date |
| 3 | Late fees | Per product terms; maximum late fee caps per state law enforced |
| 4 | Principal | Remaining amount applied to outstanding principal |

#### 5.6.2 Payment Method Processing

| **Payment Method** | **Processing Time** | **Posting Delay** | **Verification** |
|--------------------|---------------------|-------------------|------------------|
| ACH / E-Check | Same day if before 3:00 PM ET | 1 business day | Pre-note verification; NACHA compliance |
| Debit Card | Real-time authorization | Immediate posting | PCI-DSS compliant gateway (Stripe for HealthPay) |
| Credit Card | Real-time authorization | Immediate posting | Convenience fee disclosed if applicable (prohibited in certain states) |
| Check (Paper) | 3-5 business days deposit | Date of deposit + 1 | Remote deposit capture; check image retained |
| Money Order | 3-5 business days | Date of deposit + 1 | Remote deposit capture |
| Agency Remittance | Per agency contract (typically weekly wire/ACH) | Date of receipt | Remittance report reconciled to Meridian system |

#### 5.6.3 Account Closure

Upon full satisfaction (payment in full or settlement completion):
1. Payment verified as cleared (no chargeback period expired for card payments)
2. Account status updated to "CLOSED-SETTLED" or "CLOSED-PAID" in CMS
3. Satisfaction letter generated and sent to account owner within 10 business days
4. Credit reporting updated: account reported as "Paid in Full" or "Settled" within 30 days per FCRA requirements
5. Lien releases or UCC-3 terminations filed within 15 business days if applicable

### 5.7 Charge-Off and Post-Charge-Off Recovery

#### 5.7.1 Charge-Off Processing

At 180 DPD (or earlier with VP approval), accounts are charged off:
1. CMS automatically transitions account to "CHARGE-OFF" status
2. General ledger: Balance moved from active receivable to "Charged-Off Receivables" (GL 1230-500)
3. Reserve analysis: Allowance for credit losses updated per CECL methodology
4. 1099-C issued per IRS requirements (when applicable)
5. Account designated for one of three post-charge-off pathways:

| **Pathway** | **Criteria** | **Action** |
|------------|--------------|------------|
| Internal Recovery | Balance >$1,000; account owner contact information valid; no bankruptcy | Assigned to Recovery Coordinator for internal continuing recovery efforts |
| Secondary Agency Placement | Balance >$500; initial agency unsuccessful; secondary agency specialization aligns | Placed with secondary/specialty agency for 12-month additional recovery effort |
| Recovery Suspension | Balance <$500; or bankruptcy filed; or account owner deceased with no estate | Recovery efforts suspended; annual review for status change |

#### 5.7.2 Sale to Debt Buyer (Final Recovery Option)

For accounts that have exhausted internal and external recovery efforts, sale to debt buyer may be considered:
1. Portfolio analysis: Recovery Coordinator identifies eligible accounts (typically 365+ days post-charge-off with no active recovery)
2. Portfolio valuation: Expected sale price analyzed; sale only if net present value of sale exceeds expected continued recovery effort value
3. Approval: VP of Financial Services and Treasurer approval required
4. Sale documentation: Purchase and Sale Agreement; representations and warranties limited
5. Data transfer: Encrypted file transfer; PHI handling per HIPAA-compliant agreement
6. Post-sale: Credit reporting updated to "Transferred/Sold"; account owner notification if required by applicable law

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| **Control ID** | **Control Name** | **Implementation** | **SOC 2 Mapping** | **GDPR Article** |
|----------------|------------------|-------------------|-------------------|------------------|
| TECH-001 | Multi-Factor Authentication | Okta MFA enforced for all CMS access; FIDO2 hardware tokens for privileged accounts | CC6.1 | Art. 32(1)(a) (pseudonymisation and encryption) |
| TECH-002 | Role-Based Access Control | Granular RBAC in CMS: 9 defined roles with least-privilege permissions; quarterly UAR | CC6.1, CC6.3 | Art. 25(2) (data minimization) |
| TECH-003 | Data Encryption-at-Rest | AES-256 encryption for all stored data in CMS database; AWS KMS key management | CC6.1 | Art. 32(1)(a) |
| TECH-004 | Data Encryption-in-Transit | TLS 1.2+ minimum for all communications; SFTP for file transfers; PGP for email attachments containing PII | CC6.1 | Art. 32(1)(a) |
| TECH-005 | Audit Logging | All CMS user activities logged; log retention 1 year online, 7 years archive; immutable log storage | CC7.2, CC7.3 | Art. 30 (records of processing) |
| TECH-006 | Database Activity Monitoring | Imperva DAM deployed; alerts for anomalous query patterns; bulk data access requires secondary approval | CC7.2 | Art. 32(1)(b) (ongoing confidentiality) |
| TECH-007 | Data Loss Prevention | Symantec DLP monitoring outbound channels (email, web, USB); PHI/PII pattern matching; block/quarantine for policy violations | CC6.6 | Art. 32(2) (appropriate measures) |
| TECH-008 | Vulnerability Scanning | Tenable.io weekly scans; authenticated scanning where possible; critical vulns remediated 7 days | CC7.1 | Art. 32(1)(d) (regular testing) |
| TECH-009 | Endpoint Protection | CrowdStrike Falcon deployed on all collections endpoints; USB device control; application whitelisting | CC6.8 | Art. 32(1) |
| TECH-010 | Secure Development | CMS developed per OWASP Top 10; SAST (SonarQube) and DAST (Burp Suite Enterprise) in CI/CD pipeline; manual penetration testing annually | CC8.1 | Art. 25(1) (data protection by design) |

### 6.2 Administrative Controls

| **Control ID** | **Control Name** | **Implementation Frequency** | **Responsible** |
|----------------|------------------|-----------------------------|-----------------|
| ADMIN-001 | User Access Review | Quarterly | IT Identity Management + VP Financial Services |
| ADMIN-002 | Collections Strategy Review | Semi-annually | Director of Collections Operations + MRC |
| ADMIN-003 | Third-Party Vendor Risk Assessment | Annually + upon material change | Vendor Management Office |
| ADMIN-004 | Business Continuity / DR Test | Semi-annually | IT Disaster Recovery + VP Financial Services |
| ADMIN-005 | Collections Policy Compliance Audit | Annually | Internal Audit |
| ADMIN-006 | Model Validation (SR 11-7) | Annually | Independent Model Risk Management |
| ADMIN-007 | QA Call Monitoring | Monthly minimum 5 calls/agent | Compliance Officer |
| ADMIN-008 | DPIA Review | Annually + upon material change | DPO + Director of Collections Operations |
| ADMIN-009 | Records Retention Review | Annually | Records Management + Legal |
| ADMIN-010 | Complaint Analysis Review | Monthly | Compliance Officer + VP Financial Services |

### 6.3 Complaints Handling

Account owner complaints received via any channel (phone, email, portal, regulatory agency referral) follow standardized complaint handling:

1. **Intake:** Complaint logged in CMS Complaint Module with unique Complaint ID; date/time; channel; account owner details; nature of complaint categorized
2. **Acknowledgment:** Written acknowledgment to account owner within 5 business days (or sooner if CFPB/regulatory timeline applies)
3. **Investigation:** Assigned to Collections Compliance Specialist; investigation includes: call recording review, system log review, agent interview if needed, relevant policy/procedure review
4. **Resolution:** Findings documented; corrective action identified if warranted; response to account owner within 30 calendar days (or regulatory deadline if sooner)
5. **Escalation:** Unresolved complaints or those involving potential regulatory violation escalated to Compliance Officer and VP of Financial Services
6. **Trending:** Monthly complaint analysis: category trends, root cause identification, process improvement recommendations

### 6.4 Dispute Handling

Per FDCPA §809(b) and FCRA §623(a)(8), disputes regarding account validity or amount require specific handling:

1. **Dispute Receipt:** Account owner dispute received (verbal or written); logged immediately to CMS with "DISPUTE-ACTIVE" flag
2. **Collections Suspension:** All collections activities suspended pending dispute investigation (except for internal status updates, no external communications)
3. **Credit Reporting:** If debt disputed, credit reporting updated to reflect "Account Disputed" per FCRA §623(a)(3) within 30 days
4. **Verification:** Meridian verifies debt validity: original contract documentation, payment history, balance calculations, applicable interest and fees
5. **Resolution Timeline:**
   - **Written dispute (FDCPA §809(b)):** Verification provided within 30 days OR collections cease
   - **FCRA direct dispute (§623(a)(8)):** Investigation completed within 30 days (extendable to 45 days with account owner notification)
6. **Outcomes:**
   - **Debt Validated:** Verification documentation provided to account owner; dispute flag removed; collections resume per standard cadence
   - **Debt Partially Validated:** Adjustment applied to balance; revised documentation provided; dispute flag removed
   - **Debt Not Validated:** Balance adjusted to zero or appropriate corrected amount; credit reporting corrected; written confirmation to account owner

### 6.5 Data Retention Schedule

| **Data Category** | **Retention Period** | **Disposition** | **Legal/Regulatory Basis** |
|-------------------|----------------------|-----------------|---------------------------|
| Active account records | Duration of account + 7 years post-closure | Secure deletion | Statute of limitations; tax record retention |
| Charged-off account records | 7 years post-charge-off | Secure deletion | IRS 1099-C requirements; CECL documentation |
| Collections communications logs (calls, emails, letters) | 7 years post-last communication | Secure deletion | FDCPA statute of limitations; CFPB examination |
| Hardship program applications and documentation | 7 years post-program exit | Secure deletion | Fair lending compliance; regulatory examination |
| Settlement agreements | 10 years post-settlement | Secure deletion | Contract statute of limitations |
| Complaint records | 7 years post-resolution | Secure deletion | Regulatory examination; trend analysis |
| Consent records (GDPR Article 7) | Duration of processing + 6 years post-withdrawal | Secure deletion | Supervisory authority demonstration |
| DSAR logs and responses | 6 years post-response | Secure deletion | Supervisory authority demonstration |
| DPIA records | Permanent | Archival (not deletion) | Ongoing processing evidence |
| Audit logs (TECH-005) | 1 year online; 7 years archive | Secure deletion after 7 years | Security investigation; regulatory examination |

### 6.6 System Controls - HealthPay Collect CMS

**Core System Specifications:**
- **Platform:** Meridian HealthPay Collect v3.4.2 (SaaS, AWS us-east-1 primary; eu-central-1 for EU data residency)
- **Integration Points:** Oracle Fusion GL (payment posting); Salesforce CRM (customer communication history); Twilio (SMS gateway); Amazon Connect (Contact Center); DocuSign (agreement execution); Equifax/Experian/TransUnion (credit reporting)

**System Access Controls:**
- SSO via Okta with MFA enforced
- Session timeout: 30 minutes idle (configurable per role)
- Concurrent session limit: 1 per user
- Geo-IP restriction: access limited to US, Canada, UK, EU countries (exceptions require VP approval)
- Privileged access: Just-In-Time (JIT) access via CyberArk PAM; session recording enabled

**Data Validation Controls:**
- Payment amount validation: positive value ≤ outstanding balance
- Settlement calculator: automated approval routing based on delegation limits
- Date validation: no future-dated effective dates for adverse actions
- Contact attempt counter: automated enforcement of 7-attempt weekly limit per account owner

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| **Metric Category** | **KPI** | **Target** | **Measurement Frequency** | **Owner** |
|---------------------|---------|------------|--------------------------|-----------|
| **Operational Efficiency** | Right Party Contact Rate | ≥65% of outbound attempts | Weekly | Director of Collections |
| | Promise-to-Pay Rate (% of contacts resulting in payment arrangement) | ≥40% | Weekly | Director of Collections |
| | Promise-to-Pay Kept Rate (% of promises kept) | ≥75% | Monthly | Director of Collections |
| | Average Handle Time (call duration) | ≤12 minutes | Weekly | Director of Collections |
| **Recovery Performance** | Net Recovery Rate (recoveries / total charged-off) | ≥18% annualized | Monthly | VP of Financial Services |
| | Roll Rate: Current → 30 DPD | ≤3% monthly | Monthly | VP of Financial Services |
| | Roll Rate: 30 → 60 DPD | ≤25% monthly | Monthly | Director of Collections |
| | Roll Rate: 60 → 90 DPD | ≤20% monthly | Monthly | Director of Collections |
| | Cure Rate: 30 DPD → Current | ≥40% monthly | Monthly | Director of Collections |
| | Charge-off Rate (% of portfolio charged off) | ≤5% annualized | Monthly | VP of Financial Services |
| **External Agency** | Agency Net Recovery Rate | ≥12% annualized (per agency) | Monthly | Director of Collections |
| | Agency Liquidation Rate | ≥20% of placed accounts resolved | Quarterly | Director of Collections |
| | Agency Complaint Ratio | ≤0.5% of placed accounts | Monthly | Compliance Officer |
| **Compliance & Quality** | QA Monitoring Score | ≥90% average | Monthly | Compliance Officer |
| | FDCPA/Regulatory Complaint Rate | ≤0.1% of accounts | Monthly | Compliance Officer |
| | Dispute Resolution Timeliness | ≥95% within regulatory timeline | Monthly | Compliance Officer |
| | Training Completion Rate | 100% within required timeframe | Quarterly | Training Coordinator |
| **Financial** | Net Charge-off (NCO) Rate | ≤4% annualized | Monthly | VP of Financial Services |
| | Recovery to Charge-off Ratio | ≥15% | Monthly | CFO |
| | Cost-to-Collect (operational cost/recoveries) | ≤$0.25 per $1.00 recovered | Quarterly | VP of Financial Services |
| **GDPR-Specific** | DSAR Response Timeliness (within 30-day SLA) | 100% | Monthly | DPO |
| | Consent Withdrawals Processed (within 5 days) | 100% | Monthly | DPO |
| | Breach Notification Timeliness (within 72 hours) | 100% | Event-driven | DPO |

### 7.2 Dashboards and Reporting

**Operational Dashboards (Real-time, Tableau):**
- Collections Agent Scoreboard: Individual and team metrics; call volume, RPC rate, PTP rate, quality scores; refreshed every 15 minutes
- Delinquency Roll Rate Dashboard: Portfolio delinquency transitions; by product type, vintage, delinquency bucket; refreshed daily
- Queue Management Dashboard: Account queue volumes; agent capacity; aging within queue; real-time SLA monitoring

**Management Reports (Scheduled, delivered via Tableau and automated email):**

| **Report Name** | **Frequency** | **Audience** | **Content** |
|-----------------|---------------|--------------|-------------|
| Daily Collections Flash Report | Daily by 8:00 AM ET | Director of Collections, VP of Financial Services | Prior day call volume, contacts, PTPs, payments; aging summary; red flag accounts |
| Weekly Collections Operations Report | Weekly (Monday) | Director of Collections, VP of Financial Services, CFO | KPI performance vs. targets; staffing and capacity; delinquency bucket trends; agency performance |
| Monthly Portfolio Performance Report | Monthly (5th business day) | VP of Financial Services, CFO, MRC, Board Risk Committee | Roll rate analysis; charge-off analysis; recovery analysis; vintage performance; model performance metrics |
| Quarterly Collections Strategy Review | Quarterly | VP of Financial Services, CFO, Chief Risk Officer, MRC | Comprehensive portfolio analysis; strategy effectiveness; model governance update; regulatory compliance update; competitive benchmarking |
| Monthly Agency Performance Scorecard | Monthly (10th business day) | Director of Collections, VP of Financial Services | Per-agency recovery metrics; placement vs. liquidation; complaint ratio; compliance score |
| GDPR Compliance Dashboard | Monthly | DPO, VP of Financial Services, Chief Privacy Officer | DSAR volume and timeliness; consent management metrics; data subject complaints; breach incidents; DPIA status |

### 7.3 Model Risk Monitoring (SR 11-7 / NIST AI RMF)

Collections models (scoring, segmentation, LGD) are subject to ongoing monitoring:

- **Monthly Monitoring:** Model performance metrics (Gini, KS, population stability index); overrides analysis; fair lending analysis (disparate impact testing by protected class where data available)
- **Quarterly Monitoring Report:** Comprehensive model performance; comparison to development expectations; trigger thresholds (PSI >0.15 triggers review; Gini decline >5% triggers review)
- **Annual Model Validation:** Independent validation by Model Risk Management; full re-estimation if warranted
- **Findings and Remediation:** Model findings tracked; remediation timeline 90 days for medium severity, 30 days for high severity; MRC approval for continued use beyond remediation deadline

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types and Handling

| **Exception Category** | **Definition** | **Approval Authority** | **Documentation** |
|------------------------|----------------|------------------------|-------------------|
| **Policy Exception** | Departure from standard collections policy (e.g., extended forbearance beyond policy limits) | Director of Collections Operations | Exception Request Form (EXC-001) submitted; justification documented; approval logged; exception tracked in Exception Log |
| **Regulatory Exception** | Potential departure from regulatory requirement (e.g., communication outside time window due to documented time zone error) | Compliance Officer + VP of Financial Services | Immediate incident report filed (IR-001); root cause analysis within 5 business days; Corrective Action Plan (CAP) within 10 business days |
| **System Exception** | Automated processing failure requiring manual intervention | Team Lead, Collections (tactical resolution) + IT Support (system fix) | Incident ticket in ServiceNow; manual workaround documented; root cause addressed per IT incident management policy |
| **Financial Exception** | Settlement or write-off exceeding standard delegation | Per Delegation Matrix (Section 3.2) | Business case with financial analysis; approval documentation; General Counsel review if >$50,000 individual or >$500,000 aggregate |
| **Data Subject Rights Exception** | Extension of DSAR response timeline beyond 30 days | DPO + VP of Financial Services (notification to supervisory authority if required) | Extension justification documented; account owner notified of extension per Article 12(3); revised timeline communicated |

### 8.2 Escalation Hierarchy

Collections issues follow a tiered escalation structure:

| **Escalation Level** | **Role** | **Escalation Trigger** | **Response SLA** |
|----------------------|----------|------------------------|------------------|
| Level 1 | Collections Agent Level II / Team Lead | Account owner escalation request; complex payment arrangement; hardship application decision | Immediate (during call) or within 2 hours (call-back) |
| Level 2 | Supervisor, Collections Operations | Agent unable to resolve; account owner unsatisfied with Level 1 response; potential complaint situation | Within 4 business hours |
| Level 3 | Manager, Collections Operations | Level 2 resolution unsuccessful; potential regulatory involvement; media inquiry risk; litigation threat | Within 1 business day |
| Level 4 | Director of Collections Operations | Systemic issue identified; significant financial exposure (>$100,000); regulatory examination inquiry | Within 1 business day |
| Level 5 | VP of Financial Services + General Counsel | Litigation commenced; regulatory enforcement action; significant reputational risk | Immediate |

### 8.3 Cease Communication Requests

Per FDCPA §805(c) and equivalent regulations, account owners may request cessation of communications:

1. **Request Receipt:** Cease communication request logged immediately; verified as from account owner (or authorized representative)
2. **Communication Suspension:** All communications (phone, email, SMS, letter) immediately suspended EXCEPT:
   - One final communication to advise of: (a) communication cessation confirmation, (b) potential for specific remedies (legal action) that Meridian may invoke
   - Legally required communications (e.g., regulatory notices)
3. **Account Processing:** Account flagged "CEASE-COMM" in CMS; work queue removed; automated communications suppressed
4. **Escalation:** Account reviewed for next steps: (a) if pre-charge-off: account progresses to charge-off per timeline; (b) if post-charge-off: account referred for legal action evaluation
5. **No Waiver:** Cease communication request does not waive Meridian's rights to pursue legal remedies

### 8.4 Bankruptcy Notification

Upon notification of bankruptcy filing:

1. **Immediate Action:** All collections activities CEASE immediately per automatic stay (11 USC §362)
2. **Verification:** Bankruptcy case number and filing date verified via PACER or account owner attorney
3. **System Update:** CMS flagged "BANKRUPTCY-STAY" with case number and filing date
4. **Proof of Claim:** Account referred to Legal (General Counsel) for Proof of Claim filing within bar date
5. **Post-Discharge:** Upon discharge, account updated per discharge order; remaining collectible balance determined; discharge documentation maintained
6. **Credit Reporting:** Credit reporting updated to reflect bankruptcy per FCRA requirements

---

## 9. Training Requirements

### 9.1 Role-Based Training Curriculum

| **Role** | **Training Program** | **Initial Duration** | **Frequency** | **Delivery Method** |
|----------|---------------------|----------------------|---------------|---------------------|
| Collections Agent Level I | New Hire Collections Program | 80 hours (2 weeks) | One-time initial | Classroom + eLearning + nesting/coaching |
| Collections Agent Level II | Experienced Agent Program | 40 hours | Level I → Level II transition | Classroom + scenario-based |
| All Collections Agents | FDCPA/Regulatory Compliance Refresher | 4 hours | Semi-annually | eLearning with assessment |
| All Collections Agents | Fair Lending and UDAAP | 2 hours | Annually | eLearning with assessment |
| All Collections Agents | GDPR & Privacy Awareness | 2 hours | Annually | eLearning with assessment |
| All Collections Agents | HIPAA Privacy Rule | 2 hours | Annually | eLearning with assessment |
| All Collections Agents | Information Security Awareness | 1 hour | Annually + phishing simulation quarterly | eLearning + simulation |
| Recovery Coordinators | Advanced Recovery and Skip Tracing | 16 hours | One-time initial + refresher every 2 years | Classroom |
| External Agencies | Meridian Collections Compliance | 20 hours initial + 8 hours annually | Initial onboarding + annual recertification | Meridian-provided materials; agency certifies completion |
| Supervisors/Managers | Collections Leadership | 24 hours | Initial promotion + refresher every 2 years | Classroom + scenario simulation |
| All Collections Personnel | Collections Systems Training (CMS) | System-specific | Initial + upon major release (≥v1.0 increment) | Hands-on lab |

### 9.2 Training Content Standards

All training materials:
- **Regulatory Accuracy:** Reviewed by Compliance Officer for regulatory accuracy semi-annually; updated within 30 days of material regulatory change
- **Policy Alignment:** Aligned with current SOP versions; updated within 15 days of SOP revision
- **Accessibility:** Available in Meridian Learning Management System (LMS - Workday Learning); accessible via SSO; completion records maintained permanently
- **Assessment:** Each module includes knowledge assessment; passing score ≥80%; remediation for failed assessments: additional training + re-assessment within 5 business days
- **Effectiveness Measurement:** Training effectiveness measured via: post-training QA score improvement (target: ≥5% improvement within 60 days); complaint rate comparison (pre/post training)

### 9.3 Training Compliance Tracking

| **Metric** | **Target** | **Reporting Frequency** | **Owner** |
|------------|------------|------------------------|-----------|
| Training Completion Rate | 100% within required timeframe | Monthly | Training Coordinator |
| New Hire Time-to-Proficiency | ≤90 days from hire to independent call handling | Monthly | Director of Collections |
| QA Score Correlation with Training | Positive correlation analysis | Quarterly | Training Coordinator + Director of Collections |
| Compliance Violations Post-Training | ≤2% of agents with any violation | Monthly | Compliance Officer |

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| **SOP ID** | **Document Title** | **Relationship** |
|------------|-------------------|------------------|
| SOP-FIN-001 | HealthPay Financial Services Origination and Underwriting | Describes account origination that establishes obligations managed under this SOP |
| SOP-FIN-003 | Dispute Resolution and Debt Validation | Detailed procedures for handling account owner disputes and validation requests |
| SOP-FIN-006 | Payment Allocation and Cash Application | Governs payment posting priority and allocation logic referenced in Section 5.6.1 |
| SOP-FIN-009 | Collections Communications Standards | Detailed communication content, channel, and frequency standards; referenced in Section 5.1 |
| SOP-FIN-013 | Third-Party Collections Agency Management | Detailed agency selection, contracting, oversight, and termination procedures |
| SOP-FIN-014 | Hardship Program Design and Administration | Comprehensive hardship program policy; eligibility models; program design principles |
| SOP-RISK-003 | Model Risk Management Framework | Model governance; validation standards; SR 11-7 compliance requirements |
| SOP-PRIV-001 | Data Subject Access Request Processing | DSAR intake, verification, fulfillment, and logging procedures |
| SOP-PRIV-004 | Cross-Border Data Transfer | EU-US data transfer mechanisms; Standard Contractual Clauses; Transfer Impact Assessments |
| SOP-IS-003 | Data Classification and Handling Standard | Data classification levels; handling controls per classification |
| SOP-IT-005 | IT Change Management Policy | Production change management; CAB review requirements |
| SOP-COMP-001 | Regulatory Complaint Handling | Consumer complaint intake, investigation, response, and regulatory reporting |
| SOP-VEND-002 | Third-Party Vendor Risk Management | Vendor assessment, due diligence, monitoring, and offboarding |

### 10.2 External Standards and Regulations

| **Standard/Regulation** | **Reference** | **Applicability** |
|-------------------------|---------------|-------------------|
| Fair Debt Collection Practices Act | 15 USC §1692-1692p | All US consumer collections |
| Fair Credit Reporting Act (Furnisher Rules) | 15 USC §1681s-2 | Credit reporting activities |
| HIPAA Privacy Rule | 45 CFR §164.500-534 | PHI handling in healthcare financing collections |
| GDPR | EU Regulation 2016/679 | EU/UK account owner data processing |
| CFPB Debt Collection Rule | 12 CFR Part 1006 | All consumer debt collection |
| SR 11-7 (Federal Reserve) | Guidance on Model Risk Management | Collections scoring model governance |
| NIST AI Risk Management Framework | NIST AI 100-1 | AI/ML model governance, including GDPR Art. 22 automated decision-making |
| SOC 2 Trust Services Criteria | AICPA TSP Section 100 | SOC 2 audit scope |
| FCA Consumer Duty | FCA PS22/9 | UK collections operations |
| PIPEDA | SC 2000, c 5 | Canadian collections data handling |
| US State Debt Collection Licensing | State-specific statutes | State licensing compliance |

---

## 11. Revision History

| **Version** | **Date** | **Author** | **Description of Changes** | **Approver** |
|------------|----------|------------|---------------------------|--------------|
| 1.0 | 2022-06-15 | Maria Santos, Director of Collections | Initial document creation; established foundational collection procedures and compliance framework | James Thornton, CFO |
| 1.1 | 2023-03-22 | Maria Santos, Director of Collections | Added Section 5.3 (Hardship Program Administration); expanded GDPR controls per DPO recommendations; added external agency oversight requirements; updated reporting metrics | James Thornton, CFO |
| 1.2 | 2023-08-10 | Robert Liu, VP of Financial Services (interim author) | Comprehensive update to address CFPB Regulation F implementation; added SOC 2 detailed control mapping; updated collections communication cadence to align with Regulation F call frequency presumptions; revised skip tracing procedures; added bankruptcy handling section (8.4);
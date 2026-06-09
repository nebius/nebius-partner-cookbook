---
sop_id: "SOP-FIN-004"
title: "Anti-Money Laundering Procedures"
business_unit: "Financial Services"
version: "5.6"
effective_date: "2025-01-22"
last_reviewed: "2026-08-08"
next_review: "2027-02-08"
owner: "Robert Liu, VP of Financial Services"
approver: "James Thornton, Chief Financial Officer"
classification: "Internal"
regulations:
  - "SOC 2"
  - "GDPR"
status: "Active"
---

# STANDARD OPERATING PROCEDURE: ANTI-MONEY LAUNDERING PROCEDURES

**SOP ID:** SOP-FIN-004
**Business Unit:** Financial Services
**Owner:** Robert Liu, VP of Financial Services
**Approver:** James Thornton, Chief Financial Officer

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure establishes the framework for Meridian Health Technologies, Inc.’s (“Meridian” or the “Company”) Anti-Money Laundering (AML) and Counter-Terrorist Financing (CTF) compliance program. This SOP defines the governance structures, operational procedures, internal controls, and reporting mechanisms designed to detect and prevent the use of Meridian’s HealthPay Financial Services platform for money laundering, terrorist financing, sanctions evasion, or other illicit financial activities. This document operationalizes the Board-level commitments set forth in the Meridian Financial Crimes Policy and translates regulatory obligations under applicable laws into auditable, repeatable processes.

### 1.2 Scope

#### 1.2.1 Business Unit Scope
This SOP applies exclusively to the **HealthPay Financial Services** business unit, including all associated sub-services:
- Healthcare payment processing (provider-to-payer, patient-to-provider)
- Patient financing origination and servicing
- Medical lending underwriting and disbursement
- Claims automation and adjudication payment flows
- Merchant acquiring services for healthcare providers
- Virtual credit card issuance for healthcare expense management

#### 1.2.2 Product and Platform Scope
- **HealthPay Core Processing Engine:** All payment instructions, settlement batches, and ACH/wire transfers processed through the HealthPay platform ($4.2B annual volume).
- **MedLend Patient Financing Portal:** Loan applications, credit decisioning, disbursement, and repayment processing.
- **ClaimsPay Automation Module:** Automated claims payments between payers and providers.
- **Provider Billing and Collections:** Payment receipt and reconciliation for provider clients.
- **HealthPay API Gateway:** All programmatic access to payment initiation and data retrieval endpoints used by integrated third-party healthcare platforms.

#### 1.2.3 Geographical Scope
The procedures herein apply to all HealthPay operations conducted from Meridian offices globally, including but not limited to operations originating in:
- **United States (Boston, MA):** Primary HealthPay operations.
- **Canada (Toronto):** Canadian payment processing through Meridian’s registered Money Services Business (MSB) subsidiary.
- **European Union (Berlin, Germany):** Operations subject to the EU’s 6th Anti-Money Laundering Directive (AMLD6) and German GwG (Geldwäschegesetz).
- **Singapore:** Asia-Pacific payment facilitation operations, subject to Monetary Authority of Singapore (MAS) Notice 626.

#### 1.2.4 Entity and Relationship Scope
This SOP applies to all relationships managed by the HealthPay business unit:
- **Provider Clients (Merchants):** Hospitals, clinics, medical groups, and dental practices utilizing Meridian for payment acceptance.
- **Borrowers:** Individual patients applying for or holding MedLend financing products.
- **Payer Partners:** Insurance companies and health plans using ClaimsPay for automated disbursements.
- **Third-Party Payment Facilitators:** Independent Sales Organizations (ISOs) and referral partners.
- **Vendors and Service Providers:** Third parties with access to payment systems or customer data.

#### 1.2.5 Exclusionary Scope
This SOP does **not** apply to:
- Internal Meridian payroll processing (governed by SOP-HR-007: Payroll Administration).
- Corporate treasury operations (governed by SOP-FIN-002: Treasury Management).
- Equity transactions or investor relations activities.
- Clinical AI Platform, MedInsight Analytics, or Meridian SaaS Platform operations, except where those platforms provide data inputs to HealthPay AML screening tools as specified in Section 5.8 (Data Integration for Enhanced Due Diligence).

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Adverse Media** | Negative news or information from reputable sources concerning an individual’s or entity’s potential involvement in financial crime, corruption, or other predicate offenses. |
| **Beneficial Ownership** | Any individual who, directly or indirectly, owns 25% or more of the equity interests of a legal entity customer, or exercises substantial control over the entity. |
| **Cash-Intensive Healthcare Business (CIHB)** | A designation applied to provider clients operating in specialties known for high volumes of patient cash payments, including but not limited to cosmetic surgery, pain management clinics, and alternative medicine practices. Subject to enhanced due diligence per Section 5.4. |
| **Correspondent Banking** | The provision of payment or settlement services by Meridian to a foreign financial institution. Currently prohibited under this SOP without explicit Board-level waiver. |
| **Customer Due Diligence (CDD)** | The baseline process of identifying and verifying the identity of a customer, understanding the nature and purpose of the account relationship, and developing a customer risk profile. |
| **Enhanced Due Diligence (EDD)** | Additional investigative steps applied to high-risk customers, including source of funds verification, beneficial ownership certification, and senior management approval for onboarding. |
| **FATF High-Risk and Non-Cooperative Jurisdictions** | Countries identified by the Financial Action Task Force as having significant strategic deficiencies in their AML/CFT regimes. Updated list maintained by the AML Compliance team. |
| **Layering** | The second stage of money laundering involving the separation of illicit proceeds from their source through complex layers of financial transactions designed to obscure the audit trail. |
| **Medical Lending Vehicle (MLV)** | A shell or front entity posing as a medical provider to process fraudulent transactions through the HealthPay platform. |
| **Money Services Business (MSB)** | A category of financial institution as defined by FinCEN (31 CFR § 1010.100(ff)) that includes money transmitters and payment processors. Meridian’s Canadian subsidiary holds this registration. |
| **Politically Exposed Person (PEP)** | An individual entrusted with a prominent public function, including senior government officials, members of parliament, senior military officers, or heads of state-owned healthcare enterprises, along with their immediate family members and close associates. |
| **Sanctions** | Economic and trade restrictions administered by OFAC (U.S.), HM Treasury’s Office of Financial Sanctions Implementation (UK), the European Union Consolidated Sanctions List, and the United Nations Security Council. |
| **Suspicious Activity Report (SAR)** | A confidential report filed with FinCEN (or equivalent FIU) documenting known or suspected violations of law or suspicious activity observed during the course of business. |
| **Transaction Monitoring** | The automated, rules-based and machine learning-driven process of reviewing payment transactions in real-time or near-real-time to identify patterns indicative of money laundering, fraud, or sanctions violations. |
| **White-Label Platform Client** | A third-party healthcare technology company that embeds HealthPay payment processing capabilities within its own branded interface, where Meridian maintains the direct regulatory obligation for the underlying payment flows. |

### 2.2 Acronyms

| Acronym | Full Term |
|---|---|
| AML | Anti-Money Laundering |
| AMLA | Anti-Money Laundering Act of 2020 (U.S.) |
| AMLD6 | 6th Anti-Money Laundering Directive (EU) |
| BSA | Bank Secrecy Act |
| CDD | Customer Due Diligence |
| CFT | Counter-Terrorist Financing |
| CISO | Chief Information Security Officer |
| CIHB | Cash-Intensive Healthcare Business |
| CTR | Currency Transaction Report |
| DPO | Data Protection Officer |
| EDD | Enhanced Due Diligence |
| FATF | Financial Action Task Force |
| FCRM | Financial Crimes Risk Management (Meridian internal system) |
| FinCEN | Financial Crimes Enforcement Network |
| FIU | Financial Intelligence Unit |
| GDPR | General Data Protection Regulation |
| KYC | Know Your Customer |
| MLRO | Money Laundering Reporting Officer |
| MSB | Money Services Business |
| NIST AI RMF | National Institute of Standards and Technology Artificial Intelligence Risk Management Framework |
| OFAC | Office of Foreign Assets Control |
| PEP | Politically Exposed Person |
| PHI | Protected Health Information |
| RBA | Risk-Based Approach |
| SAR | Suspicious Activity Report |
| SDN | Specially Designated Nationals (OFAC list) |
| SOC 2 | System and Organization Controls 2 |
| STR | Suspicious Transaction Report (EU equivalent of SAR) |

---

## 3. Roles and Responsibilities

### 3.1 Governance and Oversight Structure

The following table establishes a RACI matrix (Responsible, Accountable, Consulted, Informed) for core AML processes. Named roles correspond to Meridian organizational positions defined in the Meridian Governance Charter.

| Activity / Process | Responsible (Doer) | Accountable (Owner) | Consulted | Informed |
|---|---|---|---|---|
| AML Program Governance | VP of Financial Services | Chief Financial Officer | General Counsel; Chief Compliance Officer | Board AI Governance Committee; Audit Committee |
| KYC/CDD Execution | AML Operations Team (FCRM Analysts) | Senior AML Manager | Provider Onboarding Team | VP of Financial Services |
| EDD for High-Risk Accounts | Senior EDD Analysts | Senior AML Manager | General Counsel (for PEP determinations) | MLRO |
| Suspicious Activity Investigation | AML Investigations Lead | Money Laundering Reporting Officer (MLRO) | General Counsel; DPO (for PHI considerations) | VP of Financial Services; Chief Compliance Officer |
| SAR/STR Filing | MLRO | MLRO | General Counsel | Chief Financial Officer; Chief Compliance Officer |
| Sanctions Screening Execution | Sanctions Screening Team (automated + manual) | Senior AML Manager | General Counsel | VP of Financial Services |
| Transaction Monitoring Tuning | Data Science – Financial Crimes Team | VP of Financial Services | AI Governance Committee; Model Risk Management (per SR 11-7) | Chief AI Officer |
| AML System Access Control | CISO | CISO | IAM Team; AML Operations Team | VP of Financial Services |
| Independent Audit of AML Program | Internal Audit Director | Audit Committee | External Auditors (SOC 2 / HITRUST) | Chief Financial Officer; Board |
| GDPR Data Subject Rights in AML Context | Data Protection Officer (DPO) | DPO | MLRO; General Counsel | Chief Privacy Officer |
| AML Training Development & Delivery | AML Compliance Training Specialist | Senior AML Manager | Learning & Development Team | VP of Financial Services; Human Resources |

### 3.2 Key Role Descriptions

#### 3.2.1 Money Laundering Reporting Officer (MLRO)
**Role Designated To:** Director of AML Compliance
**Current Appointee (as of 2025-01-22):** [Name Redacted - Internal Directory]
**Core Authorities:**
- Sole authority to submit Suspicious Activity Reports (SARs) to FinCEN and equivalent filings to international FIUs.
- Authority to issue "freeze" instructions on suspect transactions pending investigation outcome, for a maximum of 7 business days without court extension.
- Authority to recommend account termination or exit to the VP of Financial Services.
- Autonomous reporting line to the Audit Committee of the Board of Directors.
- Authority to retain external legal counsel for AML matters in consultation with the General Counsel.

#### 3.2.2 AML Operations Team
**Structure:** 14 FTE Analysts (Levels I-III), 4 Senior EDD Analysts, 2 Investigations Leads, 4 Sanctions Screening Analysts, 1 Senior AML Manager.
**Location:** Boston (9), Berlin (5), Toronto (2), Singapore (2).
**24/7 Coverage Model:** Follow-the-sun operational schedule: US East Coast (08:00–20:00 ET), EU (09:00–18:00 CET), APAC (09:00–18:00 SGT). After-hours alerts are escalated to the on-call Senior AML Manager per the PagerDuty rotation.

#### 3.2.3 Data Science – Financial Crimes Team
**Reporting To:** VP of Financial Services, with dotted line to Chief AI Officer.
**Composition:** 3 Data Scientists, 1 ML Engineer, 1 Model Risk Analyst.
**Responsibilities:** Develop, maintain, validate, and tune the transaction monitoring models and sanctions screening algorithms. Subject to SR 11-7 model risk management requirements for HealthPay credit and fraud models, extended voluntarily to AML models per Board mandate.

#### 3.2.4 Enterprise AI Governance Committee (AML Responsibilities)
Per the Meridian AI Governance Charter, the Committee provides oversight for:
- Review of all AI/ML-based transaction monitoring models prior to production deployment.
- Annual bias audit of AML models to ensure no discriminatory outcomes based on protected patient/provider characteristics.
- Approval of AML model risk tiering (Tier 1: SAR prediction models; Tier 2: Sanctions fuzzy matching; Tier 3: Rule-based controls).

---

## 4. Policy Statements

### 4.1 Zero-Tolerance Policy

Meridian Health Technologies maintains a zero-tolerance policy toward money laundering, terrorist financing, and sanctions violations. The Company will not knowingly conduct business with any individual or entity engaged in illicit financial activities. Any employee who knowingly facilitates, ignores, or fails to report evidence of money laundering will be subject to disciplinary action up to and including termination of employment, forfeiture of unvested equity, and referral to law enforcement authorities.

### 4.2 Risk-Based Approach (RBA)

Meridian adopts a Risk-Based Approach to AML compliance, consistent with FATF Recommendation 1 and FinCEN’s 2016 CDD Rule. Resource allocation, monitoring intensity, and due diligence depth shall be calibrated to the assessed ML/TF risk presented by each customer, product, geography, and delivery channel. Risk assessments are reviewed semi-annually and updated upon material trigger events.

### 4.3 Prohibition on Facilitation of Tax Evasion

Consistent with the U.S. Foreign Account Tax Compliance Act (FATCA), the EU Directive on Administrative Cooperation (DAC6), and the UK Criminal Finances Act 2017, Meridian prohibits the use of its payment systems to facilitate tax evasion by any customer or counterparty.

### 4.4 Prohibition on Shell Banks and Anonymous Accounts

Meridian will not establish, maintain, administer, or process payments for shell banks. The Company will not open or maintain anonymous accounts or accounts in fictitious names. All customers are subject to identity verification prior to account activation per Section 5.1.

### 4.5 Prohibition on Correspondent Banking

As of the date of this SOP, Meridian does not engage in correspondent banking relationships. Any prospective correspondent banking relationship shall require a formal business case, a comprehensive EDD report, and explicit prior approval from the Board of Directors upon recommendation of the Audit Committee and the Chief Financial Officer.

### 4.6 Data Minimization and GDPR Compliance

AML-related personal data processing shall be limited to what is necessary and proportionate for the prevention of money laundering and terrorist financing. Per GDPR Article 23 and Recital 73, certain data subject rights (including the right of access under Article 15, the right to restriction of processing under Article 18, and the obligation to provide notification under Article 19) may be restricted where their exercise would prejudice the prevention, detection, or investigation of financial crime. Any such restriction shall be documented in the FCRM system and must be approved jointly by the MLRO and the DPO. The customer onboarding flow shall include explicit notice that personal data will be processed for AML purposes per GDPR Article 6(1)(c) (legal obligation).

### 4.7 Employee Confidentiality and SAR Non-Disclosure

All employees are strictly prohibited from disclosing the existence or contents of a Suspicious Activity Report, or the fact that a SAR investigation is being conducted, to any person other than authorized compliance, legal, or law enforcement personnel. Unauthorized disclosure of a SAR is a federal criminal offense under 31 U.S.C. § 5318(g)(2). All internal communications regarding specific SAR investigations must be transmitted via encrypted channels and marked with the header "CONFIDENTIAL – SAR PRIVILEGE – ATTORNEY-CLIENT WORK PRODUCT" where legal counsel is involved in the investigation.

### 4.8 Cooperation with Law Enforcement

Meridian will respond promptly and fully to all lawful requests for information from authorized law enforcement agencies and Financial Intelligence Units, including FinCEN 314(a) requests received through the USA PATRIOT Act information-sharing mechanism. Response timelines are established in Section 6.9.

---

## 5. Detailed Procedures

### 5.1 Customer Identification Program (CIP)

#### 5.1.1 Identity Verification – Provider Clients (Legal Entities)

All prospective provider clients (hospitals, clinics, medical groups) must complete the Meridian HealthPay Provider Application (Form HP-APP-001) via the Meridian Partner Portal. The following minimum data elements must be collected and verified before an account can be activated:

**Required Data Elements:**
| Data Element | Required For | Verification Method |
|---|---|---|
| Legal Business Name | All entities | Secretary of State business registry; Dun & Bradstreet D-U-N-S verification |
| Tax Identification Number (TIN/EIN) | U.S. entities | IRS TIN Matching program (via API integration) |
| Business Registration Number | Non-U.S. entities | Respective national company registry |
| Physical Business Address | All entities | Physical site verification for high-risk categories; geolocation validation via third-party data provider (LexisNexis Risk Solutions) |
| Mailing Address (if different) | If applicable | USPS/National Postal Service validation |
| Primary Business Phone Number | All entities | Telephonic verification call (logged in FCRM) |
| Doing Business As (DBA) Names | If applicable | State/county fictitious business name registry |
| Nature of Business / Medical Specialties | All entities | Cross-referenced against credentialing databases (e.g., NPI Registry for U.S. providers) |
| Estimated Monthly Processing Volume | All entities | Used for risk tiering; verified 90 days post-go-live against actual volumes |
| Standard Industrial Classification (SIC) / NAICS Code | All entities | Assigned by AML analyst based on business description; verified annually |
| Website URL | Applicable entities | Screened for legitimacy and risk indicators |
| Bank Account Details for Settlement | All entities | Micro-deposit verification or bank letter confirmation |

#### 5.1.2 Identity Verification – Patient Borrowers (Individuals)

For MedLend patient financing, the following minimum data elements are required:

| Data Element | Required For | Verification Method |
|---|---|---|
| Full Legal Name | All borrowers | Synthesized match against credit bureau data; name-match algorithm thresholds set at ≥90% confidence |
| Date of Birth | All borrowers | Credit bureau validation |
| Residential Address | All borrowers | Credit bureau; USPS address validation |
| Social Security Number (or National ID) | U.S. borrowers (SSN); Non-U.S. (per jurisdiction) | SSN validation via credit bureau; soft-pull credit inquiry |
| Government-Issued Photo ID | Non-U.S. borrowers; EDD-triggered reviews | Document verification via Jumio ID verification API; liveness detection required |
| Contact Telephone Number | All borrowers | SMS OTP verification at application submission |
| Email Address | All borrowers | Verification email with unique link |

#### 5.1.3 Beneficial Ownership Identification

For legal entity customers, per FinCEN’s CDD Rule (31 CFR § 1010.230), Meridian must identify and verify the identity of:
- Each individual owning, directly or indirectly, 25% or more of the equity interests of the legal entity; and
- One individual with significant managerial control (e.g., CEO, Managing Member, General Partner).

**Procedure:**
1. The Provider Application form requires the completion of a Beneficial Ownership Certification (Appendix B to Form HP-APP-001).
2. The AML Operations Team shall verify the identity of each identified beneficial owner against government-issued photo ID or, for non-U.S. entities, equivalent reliable documentation.
3. Beneficial ownership information shall be stored in the FCRM customer profile and cross-referenced against PEP and sanctions databases.
4. Any legal entity that fails or refuses to provide complete beneficial ownership information shall not be onboarded.
5. Beneficial ownership information shall be re-certified annually for high-risk customers and biennially for standard-risk customers.

### 5.2 Customer Risk Assessment and Tiering

#### 5.2.1 Risk Factor Scoring

All HealthPay customers are assigned a composite AML risk score upon onboarding and at each periodic review. The risk score is calculated using the Meridian Customer Risk Assessment Model (CRAM) embedded in the FCRM platform. CRAM aggregates the following weighted factors:

| Risk Factor | Weight (%) | Data Sources |
|---|---|---|
| **Geographic Risk** (country of incorporation, primary operations, transaction counterparty locations) | 25% | FATF lists; Transparency International CPI; OFAC/HMT/EU sanctions lists; internal geographic risk heat map |
| **Product/Service Risk** (processing volumes, use of cross-border payments, virtual credit card issuance) | 20% | HealthPay Core; ClaimsPay configuration |
| **Entity Type Risk** (legal structure complexity, non-profit status, MSB registration, PEP involvement) | 20% | Beneficial ownership registry; LexisNexis WorldCompliance |
| **Industry/Sector Risk** (medical specialty designation, CIHB status, telemedicine vs. in-person) | 20% | NPI specialty taxonomy; internal CIHB classification |
| **Transaction Pattern Risk** (volume velocity, average ticket size deviations, chargeback ratios) | 15% | HealthPay transaction monitoring feed; chargeback system |

#### 5.2.2 Risk Tier Definitions

| Risk Tier | Score Range | CDD/EDD Requirements | Periodic Review Cycle | Transaction Monitoring Intensity |
|---|---|---|---|---|
| **Tier 1 – Low Risk** | 0 – 34 | Standard CDD | Biennial (24 months) | Baseline – All standard scenario rules active |
| **Tier 2 – Medium Risk** | 35 – 64 | Standard CDD + Enhanced ownership verification | Annual (12 months) | Elevated – Additional healthcare-specific scenarios (e.g., pharmacy volume monitoring) |
| **Tier 3 – High Risk** | 65 – 84 | Full EDD (see Section 5.4) | Semi-annual (6 months) | Heightened – Lower dollar thresholds for alert generation; mandatory manual review of 100% of alerts within 4 hours |
| **Tier 4 – Prohibited** | 85 – 100 | Onboarding denied | N/A | N/A – Accounts are not permitted; existing accounts transitioning to this tier due to review are subject to mandatory exit (Section 5.7) |

### 5.3 Customer Due Diligence (CDD) – Standard Procedures

The following standard CDD procedures apply at onboarding and at each periodic review cycle. All CDD artifacts are stored as immutable records in the FCRM system with complete audit trail.

**CDD Procedure Checklist (Form AML-CDD-001):**
- [ ] Customer Identification Program (CIP) completed per Section 5.1.
- [ ] Business nature and anticipated activity documented and corroborated.
- [ ] Expected monthly processing volume and average transaction value recorded.
- [ ] All beneficial owners (≥25%) and one controller identified and verified.
- [ ] Sanctions and PEP screening completed with results attached.
- [ ] Adverse media screening performed (negative keywords: "fraud," "indictment," "sanctions," "corruption," "money laundering," "Medicare fraud," "False Claims Act").
- [ ] Customer risk tier assigned and approved.
- [ ] Initial transaction monitoring profile configured based on risk tier.
- [ ] Customer agreement (Meridian HealthPay Services Agreement) executed and uploaded.
- [ ] OFAC/SDN screening confirmation received.
- [ ] Case file reviewed and approved by AML Analyst Level II or higher.

**Turnaround Time SLA:**
- Standard-Risk Onboarding (Tiers 1–2): 3 business days from completed application.
- High-Risk Onboarding (Tier 3): 7 business days from completed application (subject to EDD per Section 5.4).

### 5.4 Enhanced Due Diligence (EDD)

#### 5.4.1 EDD Triggers

EDD is mandatory for any customer that meets one or more of the following criteria:

1.  **CRAM Score ≥ 65 (Tier 3 – High Risk).**
2.  **PEP Status:** The customer, a beneficial owner, or a controller is identified as a Politically Exposed Person (Foreign PEP, Domestic PEP, or International Organization PEP).
3.  **FATF High-Risk Jurisdiction:** The customer is incorporated in, headquartered in, or conducts a material portion (>10%) of transactions with counterparties in FATF-listed jurisdictions.
4.  **Cash-Intensive Healthcare Business (CIHB):** The provider operates in a Meridian-designated CIHB specialty.
5.  **Complex Ownership Structure:** The presence of bearer shares, trusts in non-transparent jurisdictions, multiple layers of offshore holding companies, or a refusal to provide identifying documentation.
6.  **Adverse Media:** Negative news identified during CDD that requires further investigation to determine ML/TF relevance.
7.  **White-Label Platform Client:** Any third-party technology platform embedding HealthPay services.
8.  **Unusual Activity During Onboarding:** Inconsistencies in application information, reluctance to provide documentation, or attempts to structure the relationship in unusual ways.

#### 5.4.2 EDD Procedure

EDD investigations are assigned to Senior EDD Analysts. The EDD procedure (Form AML-EDD-001) requires:

1.  **Source of Wealth and Source of Funds Verification:**
    - Document the origin of the wealth used to establish and capitalize the business.
    - For MedLend loans with face value >$250,000, verify source of funds for any down payment or collateral.
    - Obtain and review 3 years of audited financial statements (or equivalent tax filings for private entities).
    - Document the anticipated and actual source of funds flowing through the HealthPay account (e.g., patient payments, insurance reimbursements, practice group contributions).

2.  **Beneficial Ownership Deep Dive:**
    - Map the complete ownership chain to ultimate natural persons.
    - Verify the identity of **all** individuals holding ≥10% ownership (lowered threshold from 25% for EDD).
    - For trusts: Identify settlor, trustee(s), protector(s), beneficiaries, and any individuals with power to revoke.

3.  **Background Investigation:**
    - Comprehensive global sanctions, PEP, and adverse media screening via LexisNexis WorldCompliance.
    - Review of U.S. federal/state healthcare exclusion lists (OIG LEIE, SAM.gov exclusions).
    - Professional license verification against state medical boards.
    - Litigation history search (PACER and equivalent international databases).

4.  **Site Visit or Virtual Verification:**
    - For provider clients, a physical site visit or certified virtual verification (via live video walkthrough) to confirm the physical premise matches legitimate medical operations.
    - Site visit reports are uploaded to FCRM with geotagged photographs.

5.  **Senior Management Approval:**
    - EDD case file, including the completed EDD report and a risk acceptance memorandum, must be reviewed and approved by the **Senior AML Manager**. For PEPs and FATF-jurisdiction clients, additional approval is required from the **VP of Financial Services**.
    - Approval must be documented with an electronic signature and audit timestamp in FCRM.

6.  **Ongoing Enhanced Monitoring Configuration:**
    - Upon approval, the customer’s transaction monitoring profile is configured for Tier 3 heightened monitoring (see Section 5.6.3).
    - Specific monitoring scenarios may be activated based on the customer’s risk profile (e.g., pharmacy-specific controls for pharmacies, PEP transaction monitoring for PEP-linked accounts).

### 5.5 Sanctions Screening

#### 5.5.1 Screening Infrastructure

Meridian employs a real-time sanctions screening engine (integrated with the LexisNexus Bridger Insight XG platform) configured to screen against the following lists at the cadences specified:

| Sanctions List | Screening Cadence |
|---|---|
| **OFAC Specially Designated Nationals (SDN) and Blocked Persons List** | Real-time (pre-transaction); daily batch re-screening of active customer base |
| **OFAC Consolidated Sanctions List (Non-SDN)** | Real-time; daily batch |
| **EU Consolidated Financial Sanctions List** | Real-time (EU operations); daily batch |
| **HM Treasury Office of Financial Sanctions Implementation (OFSI)** | Daily batch |
| **United Nations Security Council Consolidated List** | Daily batch |
| **Monetary Authority of Singapore (MAS) Sanctions List** | Daily batch (APAC operations) |
| **Bureau of Industry and Security (BIS) Entity List** | Weekly batch screening of provider vendors |
| **OIG List of Excluded Individuals/Entities (LEIE)** | Daily batch – healthcare-specific screening |

#### 5.5.2 Screening Procedure

1.  **Pre-Transaction Screening:** All payment instructions, returns, and settlement instructions are screened synchronously before processing. A positive hit triggers an automatic block and escalation to the Sanctions Screening Team.
2.  **Onboarding Screening:** All entities, beneficial owners, controllers, and associated parties are screened against all applicable lists before account activation.
3.  **Periodic Re-Screening:** The entire customer and counterparty database is re-screened against updated sanctions lists on a nightly batch cycle.
4.  **Alias and Fuzzy Logic:** The screening engine is configured to use fuzzy matching algorithms (≥85% confidence threshold for alert generation). Alerts below 95% confidence but above 85% are queued for manual "discard or escalate" review by a Sanctions Screening Analyst within 2 business hours.
5.  **True Match Procedure:** A confirmed true match (≥95% confidence or analyst-confirmed) triggers an immediate escalation to the MLRO. The transaction or account is frozen pending a legal determination. The MLRO shall, within 24 hours, determine if a blocked property report must be filed with OFAC within 10 business days (31 CFR § 501.603).
6.  **OFAC Licensing:** If a transaction involves an entity subject to sanctions but a specific or general OFAC license may apply, the MLRO shall consult with General Counsel before processing.

### 5.6 Transaction Monitoring

#### 5.6.1 Monitoring System

The HealthPay Transaction Monitoring System (HTMS) is a hybrid rules-engine and machine learning platform that ingests all financial messages (payment instructions, settlement batches, ACH entries, wire transfer instructions, MedLend loan disbursements) in real-time. The system operates on a streaming architecture (Apache Kafka topic: `healthpay.txn.financial.v2`) with sub-second latency for critical scenarios.

#### 5.6.2 Monitoring Scenarios (Rules-Based)

The following scenarios are actively maintained. Thresholds are tier-specific per the CRAM risk rating. Tuning is performed quarterly by the Data Science – Financial Crimes team per the Model Risk Management Framework (SOP-DS-012).

| Scenario ID | Scenario Name | Tier 1 Threshold | Tier 2 Threshold | Tier 3 Threshold | Description |
|---|---|---|---|---|---|
| **HP-TM-001** | Rapid-Fire Micro-Transactions | >20 txns in 30 min | >15 txns in 30 min | >10 txns in 30 min | Multiple small transactions designed to stay below reporting thresholds (structuring) |
| **HP-TM-002** | Unusual Large Transaction | Single txn >$100K | Single txn >$50K | Single txn >$25K | Large-value transaction inconsistent with customer profile |
| **HP-TM-003** | Cross-Border Velocity Anomaly | >$200K cross-border in 7 days | >$100K cross-border in 7 days | >$25K cross-border in 7 days | Rapid accumulation of cross-border flows |
| **HP-TM-004** | New Account Surge | >$500K in first 30 days | >$250K in first 30 days | >$100K in first 30 days | High volume on newly opened accounts before activity patterns are established |
| **HP-TM-005** | Peak vs. Off-Peak Deviation | >3σ from historical profile | >2.5σ from historical profile | >2σ from historical profile | Statistical deviation from established transaction timing patterns |
| **HP-TM-006** | Intermediary Payment Chain (Layering) | >3 intermediary hops | >2 intermediary hops | >1 intermediary hop | Payments routed through multiple unrelated providers |
| **HP-TM-007** | Unusual Payer-Provider Distance | >3000 miles radius; no established referral pattern | >2000 miles radius | >1000 miles radius | Patient-to-provider transactions with disproportionate geographic separation |
| **HP-TM-008** | Round-Dollar Structuring | >10 round-dollar txns ($X,000.00) in 24h | >5 round-dollar txns in 24h | >3 round-dollar txns in 24h | Transactions exhibiting intentional round-dollar amounts |
| **HP-TM-009** | CIHB Volume Spike | N/A | N/A | +300% MoM volume increase | Volume anomaly specifically for Cash-Intensive Healthcare Businesses |
| **HP-TM-010** | MedLend Rapid Payoff | Loans >$100K paid off within 90 days of origination with funds from non-originating institution | Loans >$50K paid off within 60 days | Loans >$25K paid off within 30 days | Use of medical loans for rapid fund cycling |

#### 5.6.3 Alert Handling Procedure

1.  **Alert Generation:** HTMS generates an alert, assigns a unique Alert ID, and posts it to the AML Operations queue in FCRM.
2.  **Initial Triage (T+0 to T+1 Hour):** An AML Operations Analyst (Level I) acknowledges the alert within **1 hour** for Tier-3 accounts and **4 hours** for all others. The analyst conducts an initial triage:
    - Review transaction details in HealthPay Core.
    - Examine customer profile, risk tier, and historical activity.
    - Check counterparty details for any sanctions, PEP, or adverse media flags.
    - Review linked cases for previous alerts.
3.  **Investigation (T+1 to T+24 Hours):** If the analyst determines the alert has merit, it is escalated to an AML Investigations Lead for deeper investigation:
    - Request additional information from the Provider Relationship Manager (without disclosing investigation details).
    - Analyze multi-transaction patterns across related entities.
    - Conduct open-source intelligence (OSINT) research on involved parties.
    - Document findings, analysis, and preliminary disposition in the FCRM Case Management module.
4.  **Disposition Decision (T+24 to T+72 Hours):**
    - **False Positive:** Alert is closed with rationale. Data is captured and fed back to the Data Science team for model tuning. Closed within 72 hours.
    - **Merit – No SAR Required:** Investigation reveals a benign explanation. Case is closed with comprehensive documentation. Customer risk score may be adjusted upward.
    - **Merit – SAR Referral:** Investigation yields reasonable grounds to suspect money laundering, terrorist financing, or structuring. A **SAR Referral Package** is prepared and submitted to the MLRO per Section 5.8.1.
5.  **Alert Aging SLA:** No alert shall remain in "Pending" status for more than **7 calendar days** from generation date. Alerts approaching this threshold are escalated to the Senior AML Manager.

### 5.7 Suspicious Activity Reporting

#### 5.7.1 Internal SAR Referral and Decision

1.  **SAR Referral Package Preparation:** The AML Investigations Lead assembles a **Confidential SAR Referral Package** containing:
    - Chronological narrative of identified activity.
    - Transaction aggregation (dates, amounts, counterparties, account numbers).
    - Subject identification information (legal name, TIN/SSN, address, account number).
    - Risk profile summary.
    - Supporting evidence (transaction logs, copies of suspicious documents, screenshots from investigation).
    - Preliminary recommendation (File / Do Not File / Continue Investigation).

2.  **MLRO Review and Determination:** The **MLRO** reviews the package, may request additional analysis, and makes the final determination on whether reasonable grounds exist to suspect money laundering. The MLRO decision is documented in FCRM with a formal `MLRO Disposition Memorandum`.

3.  **Attorney-Client Work Product Designation:** Where the legal risk is elevated or the MLRO desires legal privilege protection over the investigative file, the MLRO requests General Counsel’s office to formally join the investigation. Subsequent communications are marked **"CONFIDENTIAL – ATTORNEY-CLIENT WORK PRODUCT – SAR INVESTIGATION."**

4.  **Consensus Disagreement Escalation:** If the AML Investigations Lead and MLRO disagree on whether to file a SAR, and the Investigations Lead recommends filing, the matter is escalated to the General Counsel and Chief Compliance Officer for a final joint determination. The decision and rationale are documented and retained.

#### 5.7.2 SAR Filing Procedure (FinCEN – U.S.)

1.  **Filing System:** SARs are filed electronically via the FinCEN SAR Portal (BSA E-Filing System).
2.  **Form Preparation:** The MLRO (or designated analyst under direct MLRO supervision) completes FinCEN SAR (Form 111).
3.  **Filing Deadline:** SARs must be filed with FinCEN no later than **30 calendar days** from the date of the initial detection of the suspicious activity. If a suspect cannot be identified, filing may be delayed an additional **30 calendar days** (maximum 60 calendar days from initial detection), provided the reason for delay is documented in FCRM.
4.  **SAR Supporting Documentation:** All supporting documentation referenced in the SAR shall be maintained in the FCRM Confidential SAR Case File and made available to FinCEN or law enforcement upon request. Records of all SAR filings are retained for a period of **5 years** from the filing date.
5.  **Ongoing Activity – Supplemental SAR:** If suspicious activity continues after the initial SAR filing, a supplemental SAR shall be filed at **90-day intervals** (or earlier if a material new fact emerges) for as long as the activity continues.
6.  **SAR Confidentiality Log:** Access to SAR files within FCRM is restricted to named individuals: MLRO, AML Investigations Lead, General Counsel, Chief Compliance Officer, and designated Internal Audit personnel. All access events are logged and audited quarterly.

#### 5.7.3 STR Filing Procedure (EU / Germany – FIU)

1.  **Reporting Obligation:** For Meridian’s Berlin operations, Suspicious Transaction Reports (STRs) are filed with the German Financial Intelligence Unit (Zentralstelle für Finanztransaktionsuntersuchungen) under Section 43 of the GwG.
2.  **Form and Submission:** STRs are filed via the goAML platform maintained by the German FIU.
3.  **Timeline:** The STR must be filed **immediately** (unverzüglich) upon the MLRO becoming aware of facts giving rise to the suspicion. "Immediately" is operationally defined as within **24 hours** in accordance with BaFin interpretive guidance.
4.  **Prohibition on Transaction Execution (Section 46 GwG):** If the MLRO files an STR, the transaction forming the basis of the suspicion must **not** be executed unless (a) postponement is impossible or (b) the postponement would frustrate law enforcement efforts and the FIU has been notified. The Meridian HealthPay platform is configured to allow the MLRO to place a "regulatory hold" on suspect transactions for 7 business days.

### 5.8 Data Integration for Enhanced Due Diligence

To strengthen the risk-based approach without duplicating data collection, the AML Operations Team may ingest de-identified risk indicators from Meridian’s broader healthcare data ecosystem (subject to strict data minimization and PHI de-identification controls mandated by the CISO and DPO).

**Permissible Ingest Indicators:**
| Source System | Indicator | Relevance | PHI Status |
|---|---|---|---|
| MedInsight Analytics (fraud module) | Provider cluster identified in aberrant billing pattern analysis (e.g., upcoding, phantom billing) | Potential predicate offense indicating fraud-linked laundering | De-identified; aggregate cluster ID |
| Clinical AI Platform (credentialing module) | Provider license suspensions or adverse credentialing actions flagged in Provider Data Management | Elevated risk of predicate crime involvement | Non-PHI administrative data |
| Meridian SaaS (access logs) | Provider Portal access from high-risk IP ranges (TOR exit nodes, sanctioned country IPs) | Geographic risk indicator | Non-PHI technical metadata |

**Prohibition:**
The AML team is **strictly prohibited** from accessing individual patient Protected Health Information (PHI) for transaction monitoring purposes. Any investigation requiring a review of PHI (e.g., confirming a specific procedure matches a billing code) must be conducted under the joint oversight of the DPO and General Counsel with patient consent or in compliance with a HIPAA regulatory exception (45 CFR § 164.512(f) – law enforcement purposes). All such access shall be logged.

### 5.9 PEP Identification and Monitoring

1.  **Identification:** PEP identification occurs through WorldCompliance screening during onboarding and periodic re-screening. Meridian defines PEPs consistent with the FATF definition: Foreign PEPs, Domestic PEPs, and International Organization PEPs, including their Family Members and Close Associates.
2.  **EDD Application:** Once identified, the relationship is subject to full EDD per Section 5.4, regardless of CRAM score.
3.  **Senior Management Approval:** All PEP relationships (including where a PEP is identified post-onboarding) must be approved by the **VP of Financial Services**. The approval is re-certified annually.
4.  **Source of Wealth Review:** The source of wealth of the PEP (or the PEP-linked entity) must be established and corroborated using independent documentary evidence (e.g., asset declarations, public salary records for the position). A "Source of Wealth Memorandum" is prepared and filed in FCRM.
5.  **Enhanced Ongoing Monitoring:** PEP relationships are subject to semi-annual EDD review and mandatory manual review of 100% of transaction monitoring alerts.
6.  **Declination or Exit:** If, on review, the PEP presents an ML/TF risk that exceeds Meridian’s risk appetite, the relationship may be exited per Section 5.7.

### 5.10 Recordkeeping and Data Retention

1.  **BSA Recordkeeping (5-Year Rule):** All records required under the Bank Secrecy Act (31 CFR § 1010.430), including SARs and accompanying documentation, CIP records, and transaction records used to reconstruct customer activity, shall be maintained for a period of **5 years** from the date of the record creation or the date of the transaction, whichever is later.
2.  **GDPR-Compliant Retention (AML Exception):** Per GDPR Article 5(1)(e) and Recital 64, personal data processed solely for AML/CFT purposes may be retained beyond the standard "purpose limitation" period for a duration of **10 years** following the termination of the customer relationship, consistent with AMLD6 Article 40 requirements. Retention beyond 10 years is subject to MLRO and DPO joint approval and must be legally justified. All other personal data held in customer relationship management systems shall be deleted or anonymized per Meridian’s Data Retention Policy (SOP-DRM-001).
3.  **FCRM Immutable Storage:** FCRM records (case files, dispositions, SAR filings) are stored in a WORM-compliant (Write Once, Read Many) configuration to prevent tampering or deletion. All modifications to records are appended as new immutable entries, preserving the original record.

### 5.11 Proactive Account Reviews and Refreshes

| Review Type | Trigger | Procedure | SLA |
|---|---|---|---|
| **Event-Triggered Review** | MLRO determination; 300% volume spike; adverse media hit; sanctions screening alert; change of control notification; change of business model | Full KYC re-verification; reassessment of CRAM score; EDD if risk score increases. Initiated by FCRM system-generated task. | 5 business days from trigger event |
| **Periodic Review** | Per risk tier cadence (Section 5.2.2) | Full CDD refresh: updated CIP, beneficial ownership re-certification, adverse media re-screen, expected vs. actual activity analysis. CDD form (AML-CDD-002) completed. | 30 calendar days from review date assigned |
| **Trigger-Based Monitoring Profile Update** | Customer reaches 6 months of stable processing history at volume ≥ 80% of initial estimate | Recalibration of HTMS monitoring thresholds from "initial estimates" to "historical baseline" | 15 calendar days |

### 5.12 Exiting a Relationship or Freezing Funds

1.  **Risk-Based Exit:** The VP of Financial Services, upon recommendation of the MLRO, may determine that a customer must be exited due to ML/TF risk exceeding Meridian’s stated risk appetite even where no SAR is filed (e.g., repeated failure to provide EDD documentation, confirmed association with an organization promoting violence).
2.  **Mandatory Exit:** Any account where the MLRO has reasonable grounds to suspect ongoing money laundering and has filed a SAR recommending relationship termination.
3.  **Exit Procedure:**
    - Formal Exit Notice drafted by Legal and signed by the Senior AML Manager.
    - Notice is delivered to the customer. No transaction processing capability is suspended *until* all in-flight legitimate patient transactions have settled, unless the MLRO issues a "Regulatory Freeze" instruction to prevent dissipation of suspect funds.
    - Settlement account is closed after final reconciliation; remaining funds are remitted via official bank check to the entity’s verified business address on file.
    - All exit documentation is stored in FCRM.
4.  **Funds Freeze:** The MLRO Regulatory Freeze may be placed on any account or specific transaction for up to **7 business days** pending the filing of a SAR or cooperation with a law enforcement directive. Extensions beyond 7 business days require a court order or formal written directive from an authorized law enforcement agency.

---

## 6. Controls and Safeguards

### 6.1 SOC 2 Common Criteria 5.2 (CC5.2) – Control Activities: Establishment and Review of Control Activities

Detailed AML-specific control activities are established to mitigate risks to the Security, Availability, and Confidentiality criteria of the HealthPay platform, reflecting the integration of SOC 2 trust services criteria within the AML framework.

**Controls (CC5.2 mapping):**
- **FIN-AML-C01 (Entity-Level):** The Board Audit Committee reviews and approves the AML/CTF Compliance Program and this SOP on an annual basis. Meeting minutes document this review, demonstrating Tone at the Top. (SOC 2: COSO Principle 1).
- **FIN-AML-C02 (Risk Assessment):** A comprehensive ML/TF Business Risk Assessment (BRA) is conducted and documented semi-annually by the VP of Financial Services. The BRA includes analysis of inherent risks by product (HealthPay processing, MedLend lending, ClaimsPay automation), geography, and delivery channel, and assesses the effectiveness of mitigating controls. (SOC 2: COSO Principle 6, 7, 9).
- **FIN-AML-C03 (Segregation of Duties):** SOC 2 logical access controls in FCRM enforce segregation of duties: (a) Analysts conducting CDD cannot approve their own CDD cases; (b) Investigators preparing SAR referral packages cannot approve SAR filing; (c) Data Scientists tuning model parameters cannot approve model deployment. Role permissions are defined in IAM policies `arn:aws:iam::meridian-prod:policy/AML-FCRM-Segregation`.
- **FIN-AML-C04 (Technology Controls):** All AML systems are subject to the Meridian System Development Lifecycle (SDLC) (SOP-IT-003). Sanctions screening and transaction monitoring engines are deployed in a highly available, multi-AZ configuration with 99.99% uptime SLA for synchronous screening calls. Database backups are hourly with 30-day retention; all backups are encrypted at rest with AES-256 keys managed by the Meridian Key Management Service.
- **FIN-AML-C05 (Policies and Procedures):** This SOP constitutes the formal, documented operational procedure for the AML control activities. Annual review and acknowledgment is enforced via the Meridian Policy Compliance Platform (SOP-GRC-001).

### 6.2 GDPR Article 25 (Data Protection by Design and Default) Controls

The FCRM platform and related AML processes are configured with the following technical and organizational measures to ensure data protection by design and by default:

- **FIN-AML-GDPR-C01 (Data Minimization in FCRM):** FCRM data model limits personal data collection to fields explicitly required in the CDD/EDD procedures. Free-text "notes" fields include a character limit (2,000 characters) and a mandatory drop-down categorization to discourage unstructured personal data dumping.
- **FIN-AML-GDPR-C02 (Pseudonymization for Model Training):** Patient borrower personally identifiable information (PII) used for training the transaction monitoring ML models is pseudonymized via tokenization before ingestion into the Data Science sandbox. The tokenization map is stored separately in an isolated encryption vault accessible only to the Lead ML Engineer and the Data Protection Officer.
- **FIN-AML-GDPR-C03 (Automated Data Subject Rights Handling – AML Exemption):** A digital Rights Request Management (RRM) workflow routes incoming GDPR data subject access requests (DSARs) that relate to FCRM data through a joint DPO/MLRO review. The MLRO validates whether the DSAR must be restricted per Article 23. If restricted, an automated "Restriction Notice" (Form GDPR-R-023) is generated, documented, and sent to the DPO for formal response to the data subject per the 30-day Article 12 deadline.
- **FIN-AML-GDPR-C04 (Retention Enforcement):** Automated scripts in the FCRM back-end execute quarterly against a 10-year retention marker. Personal data associated with exited customers exceeding the 10-year mark is subject to automated logical deletion from the FCRM operational database, with an archival copy retained in encrypted format solely for regulatory audit purposes. Deletion logs are reviewed by the DPO.

### 6.3 Access Controls

| Control Area | Control Specification | Responsible |
|---|---|---|
| **Logical Access** | FCRM and HealthPay Core AML interfaces require unique user IDs (no shared accounts). MFA required (Okta push + YubiKey PIV for sensitive roles (MLRO, SAR investigators, data scientists)). | CISO; IAM Team |
| **Role-Based Access Control (RBAC)** | Five distinct FCRM roles: `AML_Viewer`, `AML_Analyst_L1`, `AML_Analyst_L2`, `AML_Investigator`, `AML_MLRO`. Permissions aligned to RACI (Section 3). Quarterly user access review performed. | CISO; Senior AML Manager (Attestor) |
| **Privileged Access Management (PAM)** | FCRM system administrators (DevOps) must check out privileged credentials via CyberArk PAM. All admin session activities are recorded and replayed-able. | CISO |
| **Segregation of Duties (SOD)** | IAM rules prevent simultaneous assignment of `AML_Analyst_L2` and `AML_MLRO` or `AML_Investigator` and `AML_MLRO` roles. SOD violations generate automatic PagerDuty alerts to IAM and Compliance. | CISO |
| **PHI Access Logging** | Any access to PHI within the AML investigation context (permitted per Section 5.8) is logged to a immutable SIEM (Splunk) log stream with alerting for anomalous access patterns. | CISO; DPO |

### 6.4 Change Management

All changes to the HTMS models, FCRM codebase, or sanctions screening rules follow the Meridian Change Management Policy (SOP-IT-002):
- Changes are documented in a Request for Change (RFC) ticket.
- All changes are subject to peer review and approval by the Senior AML Manager and a qualified IT Change Authority.
- Emergency changes may be expedited but require post-implementation review within one business day.
- Model changes are subject to Model Risk Management per SR 11-7 (Section 6.6).
- Change logs are audited semi-annually.

### 6.5 Technology Resilience and Availability

Per the SOC 2 Availability criterion:
- The HealthPay synchronous sanctions screening API maintains a **99.99%** availability SLA. Fail-open vs. fail-closed configuration: **Fail-Closed**. All transactions are declined if the sanctions screening service is unreachable.
- Recovery Time Objective (RTO) for FCRM: **2 hours**.
- Recovery Point Objective (RPO) for FCRM: **15 minutes**.
- The Disaster Recovery Plan (SOP-DRP-IT-001) includes a specific annex for HealthPay Financial Crimes applications, tested on a semi-annual basis. Test results are reported to the VP of Financial Services.

### 6.6 Model Risk Management (SR 11-7 Extension)

Although SR 11-7 is a Federal Reserve supervisory guidance for banks, Meridian voluntarily extends its model risk management principles to all AML/CTF models:
- **Model Inventory:** All models (rules and ML) are registered in the Enterprise Model Inventory.
- **Model Documentation:** Each model has comprehensive documentation detailing purpose, methodology, data inputs, limitations, and monitoring parameters.
- **Independent Validation:** The Model Risk Analyst, reporting independently from the Data Science – Financial Crimes team, conducts annual independent validation of Tier 1 and Tier 2 models. Validation assesses conceptual soundness, outcome analysis (false positive rates, SAR conversion yield), and detection of population drift.
- **Backtesting and Benchmarking:** Tier 1 models are backtested annually.
- **Ongoing Monitoring:** Monthly performance monitoring reports are generated for all Tier 1 and Tier 2 models, tracking key metrics (alert volumes, aging, false positive rates, SAR yield). Reports are reviewed by the AI Governance Committee.

### 6.7 Physical Security Controls

Per access control procedures (SOP-SEC-001), all Financial Services workspaces (including the AML Operations Center in Boston) are secured via Meridian badge access and biometric verification. Visitor access requires escort and logging. Paper files containing customer PII or SAR-confidential material are stored in locked, fire-rated cabinets when not in active use. Clean-desk policy is enforced.

### 6.8 Independent Testing and Audit

Per SOC 2 Monitoring Activities (COSO Principle 14) and BSA Independent Testing Requirement (31 CFR § 1022.210(d)):
- **Internal Audit:** The Internal Audit function conducts a risk-based audit of the AML/CTF program on an **annual** basis. The audit scope includes testing the operating effectiveness of controls FIN-AML-C01 through C05, adherence to CDD/EDD procedures, SAR decisioning accuracy, and model governance.
- **External Audit:** As part of the annual SOC 2 Type II examination, the external auditor assesses the design and operating effectiveness of AML-related controls included in the SOC 2 control matrix.
- **Regulatory Examination Readiness:** The AML program is maintained in a state of readiness for examination by regulators (including FinCEN, the Office of the Comptroller of the Currency, state financial services examiners, or international FIUs).
- **Audit Findings Remediation:** Any audit finding rated "Moderate" or "High" must have a remediation plan entered into the GRC platform within 30 business days. Remediation progress is tracked monthly by the VP of Financial Services until closure.

### 6.9 Law Enforcement Response SLAs

| Request Type | Governing Authority | Response SLA | Responsible Party |
|---|---|---|---|
| USA PATRIOT Act 314(a) | FinCEN | **14 calendar days** from transmission date | MLRO; AML Operations Team |
| FinCEN 314(a) (Expedited) | FinCEN | **5 business days** | MLRO |
| Grand Jury Subpoena | U.S. District Court | Per subpoena deadline; typically 14–30 days | General Counsel; VP, Financial Services |
| FIU Information Request (EU) | German FIU / BaFin | **10 business days** | MLRO, EU Operations |
| Mutual Legal Assistance Treaty (MLAT) Request | U.S. DOJ / International Authority | Per request; managed by General Counsel | General Counsel |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The following KPIs measure AML operational performance. Data is sourced from FCRM dashboards and aggregated into the HealthPay Financial Crimes Operations Scorecard.

| KPI ID | Metric | Target | Owner | Review Cadence |
|---|---|---|---|---|
| **KPI-AML-01** | CDD Onboarding Cycle Time (Standard-Risk) | < 3 business days (95% adherence) | Senior AML Manager | Monthly |
| **KPI-AML-02** | EDD Onboarding Cycle Time (High-Risk) | < 7 business days (95% adherence) | Senior AML Manager | Monthly |
| **KPI-AML-03** | Periodic Review Completion Rate | > 98% completed within 30-day SLA window | AML Operations Team Lead | Monthly |
| **KPI-AML-04** | Transaction Monitoring Alert Aging (Tier 3) | 100% of alerts acknowledged within 1 hour; 100% disposed within 7 calendar days | AML Investigations Lead | Weekly (Ops); Monthly (Mgmt) |
| **KPI-AML-05** | SAR Filing Timeliness (FinCEN) | 100% filed within 30 calendar days of initial detection | MLRO | Quarterly |
| **KPI-AML-06** | Model False Positive Rate | < 7% average across all active monitoring scenarios | Data Science – Financial Crimes | Monthly |
| **KPI-AML-07** | SAR Conversion Rate | > 4% of alerts result in SAR filing (indicates alert quality) | VP of Financial Services | Quarterly |
| **KPI-AML-08** | PEP Designation Timeliness | 100% PEPs identified during onboarding; 100% post-onboarding PEP identifications acted upon within 2 business days | Senior AML Manager | Quarterly |
| **KPI-AML-09** | Law Enforcement Response Timeliness | 100% adherence to SLAs in Section 6.9 | MLRO | Quarterly |
| **KPI-AML-10** | AML Training Completion Rate | 100% of assigned personnel within 30 days of hire/assignment; 98% by annual refresh deadline | SVP of Human Resources (reporting); AML Compliance Training Specialist (execution) | Semi-annual |

### 7.2 Management Information (MI) and Dashboarding

The HealthPay Financial Crimes Operations Scorecard is published as a Tableau dashboard, refreshed daily from FCRM ETL pipelines.

**Dashboard Tabs:**
1.  **Executive View (VP, CFO, Audit Committee):** SARs filed trends (rolling 12-month), high-risk customer population count and movement, audit finding remediation status, top-line operational KPIs.
2.  **Operational View (AML Operations Manager):** Alert queue depth, aging buckets (0-4h, 4-24h, 24-72h, >7d), CDD queue volume, per-analyst productivity (alerts cleared per FTE day).
3.  **Model Health View (Data Science):** Alert generation volumes per scenario, false-positive rate trends, population drift indicators, model tuning log.
4.  **Risk Profile View (AML Management):** Aggregate customer risk tier distribution and migration over time.

### 7.3 Reporting Cadences

| Report | Recipient(s) | Cadence | Format |
|---|---|---|---|
| HealthPay Financial Crimes Operations Scorecard | VP of Financial Services; Senior AML Manager | Weekly (Operations View); Monthly (All Views) | Tableau Dashboard – automated email snapshot |
| Quarterly AML Report to Board Audit Committee | Audit Committee; General Counsel; Chief Compliance Officer | Quarterly | Formal written report; includes SAR metrics (aggregate), regulatory developments, audit status, and significant cases |
| AML Model Performance Report | Chief AI Officer; AI Governance Committee | Monthly | Written report with quantitative analysis of alert quality and trend data |
| Annual AML Risk Assessment (BRA) | Chief Financial Officer; Chief Compliance Officer; Audit Committee | Annually | Formal written risk assessment document |
| Suspicious Activity – Immediate Briefing | VP of Financial Services; Chief Financial Officer | Per event (significant SAR or law enforcement contact involving senior management scrutiny) | Secure verbal briefing + encrypted written memorandum |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types

An "Exception" is any proposed deviation from the standard procedures mandated by this SOP. Exceptions are categorized as:

- **Category A – Transactional Exception:** Time-bound exception (e.g., extension of a CDD deadline for a specific, documented business reason).
- **Category B – Procedural Exception:** Circumstance-bound exception (e.g., accepting an alternative identity verification document due to customer inability to produce standard documentation).
- **Category C – Policy Exception:** Deviation from a policy statement (e.g., onboarding a customer in a jurisdiction exceeding the standard geographic risk tolerance).

### 8.2 Exception Handling Procedure

1.  **Exception Request:** The requestor (typically the Provider Onboarding Manager, a Relationship Manager, or an AML Analyst) documents the exception request in FCRM (Form AML-EXC-001), detailing:
    - Customer identification.
    - Specific SOP section(s) from which deviation is sought.
    - Detailed business rationale and justification.
    - Proposed compensating controls to mitigate incremental risk.
    - Proposed duration (for Category A exceptions).

2.  **Risk Assessment:** The Senior AML Manager assesses the incremental ML/TF risk introduced by the exception and documents the residual risk rating (Low/Medium/High/Critical).

3.  **Approval Authority:**
    | Exception Category | Residual Risk Level | Approval Required |
    |---|---|---|
    | Category A | Low, Medium | Senior AML Manager |
    | Category A | High | MLRO |
    | Category B | Low, Medium | MLRO |
    | Category B | High | VP of Financial Services |
    | Category C | Low, Medium, High | VP of Financial Services |
    | Category C | Critical | Chief Financial Officer |

4.  **Exception Log and Tracking:** All approved exceptions are logged in the FCRM Exception Register. The register tracks the approval date, approving authority, expiration date (if applicable), and any compensating controls. Expired exceptions not renewed are automatically flagged for remediation (return to standard procedure).

5.  **Exception Renewal:** Category A exceptions may be renewed for a maximum of two additional periods. Permanent exceptions are not permitted; any permanent deviation requires formal amendment of this SOP per the Policy Management Policy (SOP-GRC-001).

### 8.3 Escalation Protocol for Urgent Matters

| Scenario | Escalation Path | Response SLA |
|---|---|---|
| **Confirmed OFAC SDN match on an active transaction** | Sanctions Screening Analyst → Senior AML Manager → MLRO (immediate) | Immediate freeze; MLRO notification within 15 minutes |
| **Law Enforcement "Freeze and Cease" directive received** | AML Operations → MLRO → VP, Financial Services → General Counsel → CFO | Immediate acknowledgment; legal review within 2 hours |
| **SAR filing revealing systemic or high-dollar ($10M+) activity** | AML Investigations Lead → MLRO → General Counsel → CFO → Audit Committee Chair (discreet communication) | MLRO to CFO within 24 hours of SAR filing |
| **Critical vulnerability in FCRM or sanctions screening system** | Any → CISO Security Operations Center (SOC) hotline; PagerDuty `financial-crimes-p1` | Incident declared within 15 minutes; per SOP-IS-001 |
| **Data breach involving SAR-confidential or CIP/KYC data** | Any → CISO SOC hotline; MLRO; DPO (parallel escalation) | Per SOP-IS-002 (Data Breach Response); regulatory notification timeline applies |

---

## 9. Training Requirements

### 9.1 Role-Based AML Training Curriculum

All training is assigned, delivered, and tracked via the Meridian Learning Management System (LMS – Workday Learning).

| Role Group | Required Training Modules | Delivery Frequency | Duration |
|---|---|---|---|
| **All Meridian Employees** | `AML-101: Meridian’s Anti-Money Laundering Commitment & Your Responsibilities` | Within 30 days of hire; annually thereafter | 45 minutes (e-learning) |
| **Financial Services Staff (All)** | `AML-101` + `AML-201: Fundamentals of BSA/AML in FinTech` | Within 30 days of assignment; biennially thereafter | 2 hours (instructor-led or live virtual) |
| **AML Operations Team (Analysts L1 & L2)** | `AML-101` + `AML-201` + `AML-301: Operationalizing CDD and Transaction Monitoring in Healthcare` | Within 30 days of hire; annually | 4 hours (instructor-led) |
| **Senior EDD Analysts; Investigations Leads** | `AML-101` + `AML-201` + `AML-301` + `AML-401: Advanced EDD, PEP & Complex Structure Investigations` | Within 30 days of promotion/hire; annually | 6 hours (instructor-led + case study workshop) |
| **Money Laundering Reporting Officer (MLRO)** | All above + `AML-501: MLRO Designation – Duties, SAR Decisioning, and Law Enforcement Engagement` | Within 30 days of designation; biennially | 8 hours (instructor-led by external AML counsel or certified body (ACAMS)); plus annual ACAMS conference attendance |
| **VP of Financial Services; CFO; General Counsel** | `AML-601: AML Governance for Financial Services Leadership` | Annually | 2 hours (briefing by MLRO and external AML counsel) |
| **Board Audit Committee Members** | `AML-701: Board-Level Financial Crimes Compliance and Oversight` | Annually | 1.5 hours (in-person briefing by MLRO and Chief Compliance Officer) |

### 9.2 Specialized Supplemental Training

- **Sanctions Compliance:**
    - All Sanctions Screening Analysts must complete `SC-201: OFAC Sanctions Compliance in Action` upon assignment and annually.
    - Relevant staff in Berlin and Singapore must complete jurisdiction-specific sanctions modules (`SC-DE-001` for German GwG; `SC-SG-001` for MAS Notice 626).

- **GDPR and AML Intersection:**
    - All AML staff based in or processing data of EU subjects must complete `DP-301: Data Protection for AML Investigators – Balancing GDPR and Financial Crime Prevention` within 30 days of assignment and annually. This module, developed jointly by the AML Compliance Training Specialist and the Data Protection Officer, covers lawful bases, data subject rights restrictions, and secure handling.

### 9.3 Training Records and Compliance Tracking

- **Records:** Completion records (including dates, scores on knowledge checks, and certificates) are maintained in the LMS and are discoverable by Internal Audit and external auditors.
- **Non-Compliance:**
    - Failure to complete assigned training within the prescribed window triggers an automated escalation: first, to the employee’s manager; second, to the SVP of Human Resources.
    - Employees who are non-compliant for 30 days beyond the deadline may be subject to temporary suspension of system access for Financial Services platforms and formal disciplinary review.
- **Effectiveness Review:** The AML Compliance Training Specialist shall review post-training survey data and knowledge check aggregate scores quarterly and provide a training effectiveness report to the Senior AML Manager. The curriculum is reviewed annually and updated to reflect changes in law, regulation, typologies (healthcare-specific laundering), and this SOP.

---

## 10. Related Policies and References

### 10.1 Meridian Internal Policies and SOPs

| SOP / Policy ID | Title | Relationship |
|---|---|---|
| SOP-FIN-001 | Financial Crimes Policy (Board-Level) | High-level policy that this SOP operationalizes |
| SOP-FIN-002 | Treasury Management and Bank Account Administration | Interface for settlement account management |
| SOP-FIN-005 | Fraud Prevention and Response for HealthPay | Parallel financial crime control; shared intelligence (where legally permissible) |
| SOP-FIN-006 | Third-Party Payment Facilitator Oversight | CDD/EDD procedures for ISOs and referral partners |
| SOP-IT-002 | IT Change Management Policy | Governance for HTMS/FCRM system changes |
| SOP-IT-003 | System Development Lifecycle (SDLC) | Secure development of Financial Crimes technology |
| SOP-DS-012 | Model Risk Management Framework | Governance for AML/CTF ML models (SR 11-7) |
| SOP-GRC-001 | Policy Management Policy | Exception and waiver tracking, policy lifecycle |
| SOP-IS-001 | Information Security Incident Response | Escalation for AML system vulnerabilities |
| SOP-IS-002 | Data Breach Response Procedure | Escalation for CIP/KYC or SAR data breach |
| SOP-DRM-001 | Data Retention and Destruction Management | Defines retention schedules, including AML exception |
| SOP-HR-007 | Payroll Administration | Explicitly out of scope for this SOP |
| SOP-VDR-001 | Vendor Risk Management | Risk assessment of LexisNexis, Jumio, and other AML technology vendors |
| SOP-PRIV-GDPR-001 | GDPR Data Subject Rights Processing | Procedures for handling DSARs intersecting AML data |

### 10.2 External Regulatory, Standards, and Guidance References

| Reference | Full Title / Description |
|---|---|
| **31 CFR Chapter X (FinCEN Regulations)** | Bank Secrecy Act implementing regulations for financial institutions, including 1020.210 (AML program requirement), 1020.220 (CDD Rule), 1020.320 (SAR filing) |
| **Bank Secrecy Act (BSA) – 31 U.S.C. 5311 et seq.** | Principal U.S. AML statute |
| **USA PATRIOT Act (Pub. L. 107-56) Title III** | International Money Laundering Abatement and Anti-Terrorist Financing Act of 2001 |
| **Anti-Money Laundering Act of 2020 (AMLA)** | U.S. statute expanding whistleblower provisions and beneficial ownership database (CTA) |
| **FFIEC BSA/AML Examination Manual** | Interagency guidance governing U.S. AML program expectations |
| **OFAC Sanctions Regulations (31 CFR Parts 500-598)** | U.S. economic sanctions programs |
| **EU 6th Anti-Money Laundering Directive (AMLD6) – Directive (EU) 2018/1673** | Amends AMLD4; harmonizes predicate offenses |
| **EU Regulation 2015/847 (Funds Transfer Regulation)** | Information on payers accompanying transfers of funds |
| **German GwG (Geldwäschegesetz)** | Germany’s AML Act, transposing AMLD6, Sections 10 (CDD), 15 (EDD), 43 (SAR/STR) |
| **General Data Protection Regulation (GDPR) – Regulation (EU) 2016/679** | EU data protection law; Articles 5, 6(1)(c), 23, 25, 32, and 35 |
| **Canadian Proceeds of Crime (Money Laundering) and Terrorist Financing Act (PCMLTFA)** | Canadian AML/CTF legal framework |
| **MAS Notice 626 – Prevention of Money Laundering and Countering the Financing of Terrorism** | Singapore AML framework for financial institutions |
| **FATF 40 Recommendations** | International standards on combating money laundering and the financing of terrorism & proliferation |
| **SOC 2 Trust Services Criteria (TSC 2017 Revision)** | CC5.2 (Control Activities), CC6.x (Logical and Physical Access), CC7.x (System Operations) |
| **NIST AI Risk Management Framework (AI RMF 1.0)** | Framework for governing AI/ML used in transaction monitoring |
| **SR Letter 11-7 (FRB/OCC/FDIC)** | Supervisory Guidance on Model Risk Management |

---

## 11. Revision History

| Version | Effective Date | Author / Owner | Summary of Changes |
|---|---|---|---|
| 1.0 | 2018-06-15 | Initial VP, Risk & Compliance | Initial AML Program documentation and CIP procedures established. |
| 2.1 | 2019-11-01 | John Morrison, AML Manager | Updated CDD procedures to reflect FinCEN 2016 CDD Rule. Added Beneficial Ownership Certification. Added Section 5.4 (EDD). |
| 3.0 | 2021-03-15 | Sarah Chen, VP, Financial Services | Major revision to incorporate AMLA 2020 changes; expanded sanctions screening to include new global lists; introduced FCRM platform and automated KYC workflow; added Data Science Team for ML monitoring models. |
| 4.2 | 2022-09-01 | Maria Diaz, MLRO | Integrated GDPR Article 23 and DPO collaboration procedures. Updated data retention to comply with AMLD6. Incorporated SOC 2 mapping (CC5 series) into Section 6. Expanded training curriculum. Renamed "Suspicious Activity Reporting" section with expanded EU STR procedures. |
| 5.4 | 2024-03-01 | Robert Liu, VP, Financial Services | Full document restructure. Added Singapore (MAS 626) operations. Migrated from legacy CTR model to risk-based HealthPay Transaction Monitoring System (HTMS). Established Tier 1-4 risk framework. Incorporated SR 11-7 extension for AML models. Added Section 5.8 data integration.
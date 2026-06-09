---
sop_id: "SOP-FIN-005"
title: "Know Your Customer Verification"
business_unit: "Financial Services"
version: "4.1"
effective_date: "2025-10-28"
last_reviewed: "2026-08-18"
next_review: "2027-02-22"
owner: "Robert Liu, VP of Financial Services"
approver: "James Thornton, Chief Financial Officer"
classification: "Internal"
regulations:
  - "GDPR"
  - "SOC 2"
status: "Active"
---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the mandatory framework for Know Your Customer (KYC) verification processes within the HealthPay Financial Services division of Meridian Health Technologies, Inc. The purpose of this document is to ensure the accurate identification, verification, and ongoing risk assessment of all prospective and existing customers—both individual patients seeking medical financing and institutional healthcare providers establishing payment processing relationships—to satisfy regulatory obligations, mitigate financial crime risk, and uphold the integrity of the HealthPay platform, which processes approximately $4.2 billion annually.

This SOP defines the minimum standards for customer due diligence (CDD), enhanced due diligence (EDD), identity verification, beneficial ownership determination, and ongoing monitoring. It applies a risk-based approach consistent with the Federal Financial Institutions Examination Council (FFIEC) guidance, Financial Crimes Enforcement Network (FinCEN) rules, and global anti-money laundering (AML) standards, while simultaneously embedding the data protection principles mandated by the General Data Protection Regulation (GDPR) for all personal data processed during the KYC lifecycle.

### 1.2 Scope

This SOP applies to the following entities, personnel, and activities:

**In-Scope Entities:**
- Meridian Health Technologies, Inc. corporate headquarters, Boston, MA
- HealthPay Financial Services offices in London, Berlin, Singapore, and Toronto
- Any Meridian subsidiary or branch that processes, reviews, or stores KYC data
- Third-party service providers acting as data processors on HealthPay's behalf (subject to data processing agreements governed under SOP-PRIV-012)

**In-Scope Personnel:**
- All Financial Services division employees, contractors, and temporary staff
- Compliance Operations team members within the Office of the Chief Compliance Officer
- Customer Operations representatives involved in onboarding workflows
- Any Meridian personnel with access to the KYC module within the Meridian SaaS Platform
- Product and engineering teams maintaining the automated identity verification subsystems

**In-Scope Customer Categories:**
1. **Individual Borrowers (P2P):** Patients and individuals applying for medical loans, patient financing, or healthcare payment plans through HealthPay. This includes co-signers and guarantors.
2. **Healthcare Provider Merchants (B2B):** Hospitals, clinics, dental practices, veterinary practices, and other healthcare providers establishing payment processing or merchant accounts with HealthPay.
3. **Institutional Payers:** Insurance companies, third-party administrators, and employer-sponsored health plans integrating with the HealthPay claims automation module.
4. **Platform Partners:** Financial institutions, credit reporting agencies, and lending partners participating in HealthPay's credit origination ecosystem.

**Out-of-Scope:**
- Employee background verification processes (governed by SOP-HR-008)
- Clinical AI Platform user credentialing for clinicians (governed by SOP-CLIN-019)
- General vendor procurement due diligence not involving direct financial services (governed by SOP-PROC-004)

### 1.3 Regulatory Alignment

This SOP is designed to operationalize compliance with the following regulatory frameworks:

| Regulation / Standard | Applicability | Jurisdiction |
|---|---|---|
| GDPR (Regulation (EU) 2016/679) | All KYC data pertaining to natural persons in the EU | European Union / EEA |
| USA PATRIOT Act Section 326 | Customer Identification Program (CIP) for US accounts | United States |
| FinCEN CDD Rule (31 CFR § 1010.230) | Beneficial ownership identification and verification for legal entity customers | United States |
| EU 5th Anti-Money Laundering Directive (Directive (EU) 2018/843) | CDD, EDD, PEP screening, UBO registers | European Union |
| Proceeds of Crime (Money Laundering) and Terrorist Financing Act (PCMLTFA) | Canadian KYC obligations | Canada |
| Monetary Authority of Singapore Notice 626 | AML/CFT requirements for financial institutions | Singapore |
| SOC 2 Trust Services Criteria | Security and confidentiality control objectives (see Section 6) | Global |
| NIST AI RMF | Risk management for automated decision-making in KYC | Global (voluntary adoption) |

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Beneficial Owner** | Any natural person who, directly or indirectly, exercises substantial control over a legal entity customer or owns 25% or more of the equity interests. For EU entities, the threshold is "any natural person who ultimately owns or controls the customer and/or the natural person(s) on whose behalf a transaction or activity is being conducted" (AMLD5, Article 3(6)). |
| **Customer Due Diligence (CDD)** | The baseline process of collecting and verifying customer identification information, assessing the nature and purpose of the customer relationship, and conducting ongoing monitoring. |
| **Enhanced Due Diligence (EDD)** | Additional investigative measures applied to high-risk customers, including source of funds verification, senior management approval, and intensified transaction monitoring. |
| **Know Your Customer (KYC)** | The comprehensive set of policies, procedures, and controls implemented to identify, verify, and risk-rate customers. |
| **Politically Exposed Person (PEP)** | An individual who is or has been entrusted with a prominent public function, including their immediate family members and close associates. PEP status extends for 12 months after leaving office (FATF Recommendation 12). |
| **Customer Identification Program (CIP)** | The specific US-mandated component of KYC requiring collection of name, date of birth, address, and identification number prior to account opening. |
| **Identity Verification** | The process of using documentary, non-documentary, or electronic identity proofing methods to confirm a customer's claimed identity against independent, reliable sources. |
| **Non-Documentary Verification** | Identity verification performed through electronic means, including knowledge-based authentication (KBA), biometric comparison, or authoritative database queries without physical document submission. |
| **Risk Rating** | A calculated assessment of the money laundering, terrorist financing, or fraud risk posed by a customer, expressed as Low, Medium, or High. |
| **Ultimate Beneficial Owner (UBO)** | The natural person(s) who ultimately owns or controls a legal entity, identified by tracing ownership and control chains through all intermediate entities. |
| **Watchlist Screening** | Automated comparison of customer identifiers against sanctions lists, law enforcement wanted lists, and adverse media databases. |
| **Ongoing Due Diligence** | Periodic review of customer information, risk ratings, and transaction patterns conducted at defined intervals throughout the customer lifecycle. |
| **Data Subject** | Any identified or identifiable natural person whose personal data is processed during KYC activities (GDPR Article 4(1)). |
| **Processing** | Any operation performed on KYC personal data, including collection, recording, storage, adaptation, retrieval, consultation, and erasure (GDPR Article 4(2)). |
| **Legal Entity Customer** | A corporation, limited liability company, partnership, trust, or other business entity that opens a financial services account with HealthPay. Sole proprietorships are classified as individual customers for KYC purposes unless they operate under a registered trade name. |

### 2.2 Acronyms

| Acronym | Full Term |
|---|---|
| AML | Anti-Money Laundering |
| BSA | Bank Secrecy Act |
| CDD | Customer Due Diligence |
| CIP | Customer Identification Program |
| CTF | Counter-Terrorist Financing |
| DPA | Data Processing Agreement |
| DPIA | Data Protection Impact Assessment |
| DSRR | Data Subject Rights Request |
| EDD | Enhanced Due Diligence |
| FATF | Financial Action Task Force |
| FCRM | Financial Crime Risk Management (Meridian internal platform) |
| FinCEN | Financial Crimes Enforcement Network |
| FIU | Financial Intelligence Unit |
| ID&V | Identity and Verification |
| IDV | Identity Verification (specific Meridian automated system) |
| KBA | Knowledge-Based Authentication |
| KYC | Know Your Customer |
| OFAC | Office of Foreign Assets Control |
| PEP | Politically Exposed Person |
| PII | Personally Identifiable Information |
| RBAC | Role-Based Access Control |
| SAR | Suspicious Activity Report |
| SIEM | Security Information and Event Management |
| SR-EDD | Senior Relationship Manager-Enhanced Due Diligence (internal role designation) |
| STR | Suspicious Transaction Report |
| UBO | Ultimate Beneficial Owner |

---

## 3. Roles and Responsibilities

### 3.1 RACI Matrix

The following Responsibility Assignment Matrix (RACI) defines the roles for each KYC-related function:

| Activity | VP of Financial Services (R. Liu) | Chief Compliance Officer (S. Chen) | Compliance Operations Lead | Customer Operations Agent | IDV System Administrator | Data Protection Officer (J. Müller) | Senior Management (Exec Committee) |
|---|---|---|---|---|---|---|---|
| KYC Policy Approval | **A** | R | C | I | I | C | I |
| CDD Case Review (Standard Risk) | I | **A** | R | C | I | I | I |
| EDD Case Review (High Risk) | C | R | R | I | I | I | **A** |
| PEP Determination | I | **A** | R | I | I | I | I |
| Automated IDV Rule Configuration | C | **A** | R | I | R | C | I |
| Manual Identity Document Verification | I | I | **A/R** | I | I | I | I |
| Data Subject Rights Response | C | I | R | I | I | **A** | I |
| Sanctions Screening Alert Disposition | I | **A** | R | I | I | I | I |
| Exception Approval (Standard Risk) | **A** | C | R | — | — | — | — |
| Exception Approval (High Risk) | C | R | R | — | — | — | **A** |
| KYC Training Completion Tracking | I | I | **R** | — | — | — | — |
| Third-Party KYC Data Processor Oversight | C | R | **A** | — | — | R | C |
| SAR/STR Filing Decision | I | **A** | R | I | I | I | I |

**Key:** R = Responsible (performs the task); A = Accountable (final approval authority); C = Consulted (provides input); I = Informed (receives notification)

### 3.2 Role Descriptions

**Robert Liu, VP of Financial Services (SOP Owner):**
- Owns the content, effectiveness, and annual review of this SOP
- Approves all standard-risk KYC exceptions
- Reviews quarterly KYC effectiveness metrics and authorizes resource adjustments
- Escalates systemic KYC control failures to the CFO within 48 hours

**Chief Compliance Officer (Sarah Chen):**
- Designates the AML Compliance Officer per regulatory requirements
- Provides final approval on EDD risk determinations
- Reviews and approves SAR/STR recommendations prior to filing with FinCEN or relevant FIU
- Authorizes PEP risk assessments and ongoing monitoring parameters
- Maintains direct reporting line to the Board of Directors' Risk and Compliance Committee

**Data Protection Officer (Jurgen Müller):**
- Reviews all KYC data processing activities for GDPR Article 6 and Article 9 compliance
- Conducts or commissions the Data Protection Impact Assessment (DPIA) for KYC processing
- Approves data subject rights responses related to KYC data within the timelines specified in Section 5.8
- Maintains the Record of Processing Activities (ROPA) entry for the KYC function
- Serves as the point of contact for EU supervisory authorities on KYC data matters

**Compliance Operations Lead:**
- Manages the daily KYC case queue within the FCRM platform
- Supervises the team of KYC analysts responsible for manual reviews
- Escalates adverse findings to the Chief Compliance Officer within 4 hours of discovery
- Ensures PEP screening results are documented and risk-rated
- Maintains the KYC procedure playbook and desk-level guides

**Customer Operations Agent:**
- Initiates KYC data collection during customer onboarding within the Meridian SaaS Platform HealthPay module
- Validates document completeness and image quality against IDV system requirements
- Communicates KYC status to the customer using approved templates
- Creates manual review tickets when automated IDV returns "Refer" or "Indeterminate" results

**IDV System Administrator (IT Security — Identity Services Team):**
- Maintains the configuration and operating parameters of the automated identity verification system
- Applies rule updates, watchlist imports, and sanctions list updates within the timelines specified in Section 5.2
- Monitors IDV system availability and establishes performance thresholds
- Conducts quarterly tuning reviews of the risk-scoring algorithm in collaboration with Compliance Operations

**Senior Management (Executive Committee):**
- Approves all EDD-related exceptions and high-risk customer onboarding decisions
- Reviews and acknowledges the Annual KYC Risk Assessment
- Ensures adequate budget and staffing resources for the KYC compliance program

---

## 4. Policy Statements

The Financial Services division of Meridian Health Technologies, Inc. commits to the following high-level policy mandates governing the KYC verification program:

**PS-KYC-001: Mandatory Customer Identification**
No customer account shall be established, and no financial service shall be rendered, until the customer's identity has been verified in accordance with the procedures defined in Section 5 of this SOP and a risk rating has been assigned. This applies to all customer categories enumerated in Section 1.2.

**PS-KYC-002: Risk-Based Due Diligence**
Meridian shall apply a graduated due diligence approach commensurate with the assessed risk profile of each customer. Customers classified as Low Risk are subject to Standard CDD. Customers classified as Medium Risk undergo Standard CDD with supplemental verification. Customers classified as High Risk are subject to Enhanced Due Diligence (EDD) and require the explicit approval of Senior Management prior to account activation.

**PS-KYC-003: Prohibition of Anonymous and Fictitious Accounts**
The HealthPay platform shall not establish, maintain, administer, or manage any accounts in fictitious names. Any account that cannot be associated with a verified natural person (in the case of individual customers) or verified beneficial owners (in the case of legal entity customers) shall be immediately suspended pending investigation, in accordance with the escalation procedures defined in Section 8.

**PS-KYC-004: Beneficial Ownership Transparency**
For all legal entity customers, Meridian shall identify and verify, using independent and reliable sources, the natural persons who serve as beneficial owners. The identification threshold is any natural person owning 25% or more of the equity interests and any natural person with significant managerial control. Ownership chains shall be traced through intermediate corporate layers until the natural person(s) are identified. Anonymous bearer share entities and shell banks are prohibited from onboarding.

**PS-KYC-005: Ongoing Monitoring and Periodic Refresh**
Customer KYC profiles are not static records. Each customer profile must undergo periodic review at intervals defined by the customer's risk rating, as specified in Section 5.6. Trigger events—including material changes in ownership, adverse media reports, law enforcement inquiries, or anomalous transaction patterns—shall initiate an out-of-cycle review.

**PS-KYC-006: PEP Identification and Enhanced Scrutiny**
All new and existing customers shall be screened against authoritative PEP databases, including the World-Check One database and national PEP registries in the jurisdictions where HealthPay operates. Any customer identified as a PEP (including foreign PEPs, domestic PEPs, and heads of international organizations) shall be automatically classified as High Risk and subject to EDD.

**PS-KYC-007: Sanctions and Watchlist Compliance**
Meridian shall not establish or maintain any customer relationship with any individual or entity appearing on sanctions lists maintained by the US Department of the Treasury's OFAC, the UK HM Treasury, the European Union Consolidated Financial Sanctions List, the United Nations Security Council Sanctions List, the Monetary Authority of Singapore Sanctions List, or any other sanctions authority with jurisdiction over HealthPay operations. Matches identified during onboarding shall result in immediate account denial and, if applicable, filing of a blocked property report.

**PS-KYC-008: Data Minimization and Purpose Limitation (GDPR Article 5(1)(c) and 5(1)(b))**
All KYC data collected shall be adequate, relevant, and limited to what is necessary for the declared purposes of identity verification, AML compliance, and fraud prevention. KYC data shall not be repurposed for marketing, credit scoring beyond AML/fraud indicators, or any secondary processing activity not explicitly communicated to the data subject in the Fair Processing Notice (SOP-PRIV-001).

**PS-KYC-009: Lawful Basis for Processing (GDPR Article 6)**
The lawful basis for processing personal data for KYC purposes is established as "Legal Obligation" under GDPR Article 6(1)(c) for data required by AML/CTF regulations, and "Performance of a Contract" under GDPR Article 6(1)(b) for data collected as a necessary pre-requisite to entering into a financial services agreement.

**PS-KYC-010: Automated Decision-Making Transparency (GDPR Article 22)**
Where KYC identity verification involves automated decision-making (including the automated IDV risk-scoring engine), Meridian shall implement appropriate safeguards including the right to obtain human intervention as defined in Section 5.4, Step 14 of this SOP. Automated decisions that result in refusal of service shall be communicated to the data subject with meaningful information about the logic involved.

---

## 5. Detailed Procedures

### 5.1 Customer Onboarding Workflow — Individual Borrowers (P2P)

This procedure defines the end-to-end KYC onboarding journey for individual patients using the HealthPay patient financing portal (`patientportal.healthpay.com`).

**Step 1: Portal Initiation**
The prospective borrower initiates a financing application by entering their first name, last name, email address, and state/province of residence on the HealthPay landing page. At this stage, the individual is classified in the system as a "Prospect" rather than a "Customer." No credit inquiry is initiated.

**Step 2: Fair Processing Notice Presentation (GDPR Article 13)**
Upon capturing the prospect's email and jurisdiction, the Meridian SaaS Platform dynamically selects and presents the jurisdiction-appropriate Fair Processing Notice (FPN). For EU/EEA residents, the FPN includes a layered privacy notice containing:
- Identity and contact details of the Data Controller (Meridian Health Technologies, Inc., Boston, MA)
- Contact details of the Data Protection Officer (Jurgen Müller, dpo@meridianhealth.com)
- Purpose and legal basis for each category of KYC data to be collected
- Legitimate interests pursued (fraud prevention, AML compliance)
- Recipients or categories of recipients of KYC data
- Transfer mechanism information for international data flows (e.g., Standard Contractual Clauses)
- Retention periods for KYC records (see Section 5.9)
- Data subject rights as enumerated in GDPR Articles 15-22
- The right to lodge a complaint with a supervisory authority
- Whether the provision of data is a statutory or contractual requirement

The prospect must affirmatively acknowledge the FPN (active opt-in checkbox) before proceeding. Passive consent or pre-ticked boxes are prohibited (GDPR Article 7). The acknowledgment timestamp, IP address, and FPN version are recorded in the audit log.

**Step 3: CIP Data Collection**
The prospect is presented with a structured data collection form. The following mandatory fields are required at minimum for KYC identification:

| Field | Source | GDPR Legal Basis |
|---|---|---|
| Full Legal Name (First, Middle, Last) | Self-reported by customer | GDPR Art. 6(1)(c) — Legal Obligation |
| Date of Birth | Self-reported by customer | GDPR Art. 6(1)(c) |
| Residential Address (Street, City, State/Province, Postal Code, Country) | Self-reported by customer | GDPR Art. 6(1)(c) |
| Government-Issued Identification Number | Self-reported and verified (see Step 4) | GDPR Art. 6(1)(c) |
| Government-issued ID document type and issuing jurisdiction | Self-reported | GDPR Art. 6(1)(c) |
| Nationality (if different from residence) | Self-reported | GDPR Art. 6(1)(c) |
| Mobile telephone number | Self-reported | GDPR Art. 6(1)(b) — Contractual necessity for communication |

**Step 4: Document-Based Identity Verification**
The prospect is directed to the Meridian IDV subsystem (`idv.meridianhealth.com`), which utilizes the Onfido document verification and facial biometric engine integrated into the Meridian SaaS Platform.

The prospect must:
1. Capture an image of their government-issued identification document (passport, national ID card, or driver's license) using a mobile device camera or webcam
2. Capture a live selfie photograph or short video for biometric facial comparison
3. Consent to automated identity verification, including biometric processing for the purpose of verifying identity against the presented document

The IDV system performs:
- Document authenticity assessment (security features, format validation, MRZ validation for passports)
- Data extraction and integrity verification (no evidence of tampering or alteration)
- Facial comparison between the document portrait and the live selfie (match confidence score >= 85%)
- Document expiration validation (must not be expired as of the date of onboarding)

**Step 5: Non-Documentary Verification (Supplemental) — US Persons Only**
If the prospect is a US person and selected "I do not have access to my ID document" during Step 4, the IDV subsystem may invoke a Knowledge-Based Authentication (KBA) supplementary module provided by LexisNexis Risk Solutions. The prospect must correctly answer at least 4 out of 5 dynamic multiple-choice questions derived from their credit header and public records within a 4-minute window. Failure of KBA requires escalation to manual review per Step 8.

*Note: KBA is not deployed for EU/EEA data subjects due to proportionality concerns under GDPR Article 5(1)(c) (data minimization).*

**Step 6: Automated Decision (IDV Outcome)**
Upon completion of Step 4 (and Step 5, if applicable), the IDV system returns one of three outcomes:

| Outcome | Confidence Threshold | Action |
|---|---|---|
| **Verified** | >= 90% overall match score; no document integrity alerts; biometric match >= 85% | Proceed to Step 10 (Watchlist Screening) |
| **Refer** | 70-89% overall match score; or low-confidence biometric match (70-84%); or document quality issues | Route to manual review queue (Step 8) |
| **Rejected** | < 70% overall match score; or document integrity alert; or identity mismatch detected; or document expired | Auto-generated adverse decision notification (Step 9) |

**Step 7: Automated IDV — Biometric Retention Controls (GDPR)**
For EU/EEA data subjects, raw biometric templates extracted during facial comparison are processed transiently for the sole purpose of one-to-one identity comparison. The biometric template is:
- Encrypted in transit (TLS 1.3) and at rest (AES-256-GCM)
- Logically segregated from the customer's PII record
- Deleted from the IDV processing environment within 48 hours of identity verification completion
- Not retained for any secondary purpose

**Step 8: Manual Review Procedure**
Cases routed to manual review are queued in the FCRM platform with a priority SLA based on customer type:

| Customer Type | Manual Review Queue SLA |
|---|---|
| Individual Borrower (Standard) | 4 business hours from queue assignment |
| Individual Borrower (EDD Candidate) | 2 business hours from queue assignment |

The assigned KYC Analyst performs the following review steps:

1. **Document Quality Re-Inspection:** Verify that the submitted document images are legible, complete, and not digitally manipulated. Re-run document through Onfido's forensic analysis module if image quality was the primary reason for "Refer" outcome
2. **Data Consistency Check:** Cross-reference the name, date of birth, and address across all submitted forms and the extracted document data. Flag any material inconsistencies for investigation
3. **Address Verification:** Validate the residential address against an independent utility bills database (US and Canada — Thomson Reuters CLEAR address verification module) or accept a supplementary document (utility bill, bank statement) dated within 90 days
4. **Negative News Screening:** Conduct a manual adverse media search using the customer's full name and date of birth
5. **Decision: Approve / Escalate for EDD / Deny:**
   - **Approve:** If all manual checks are satisfactory and the initial IDV score was >= 70%
   - **Escalate for EDD:** If adverse media is found, PEP potential identified, or inconsistencies cannot be resolved
   - **Deny:** If the KYC Analyst concludes the identity cannot be verified to the required standard, or if material misrepresentation is detected

**Step 9: Adverse Decision Notification (Automated Denied or Manual Deny)**
If the IDV outcome is "Rejected" or a manual review results in "Deny," the prospect receives an adverse action notification:
- **General Notification:** "Meridian HealthPay was unable to verify your identity based on the information provided. This application will not proceed at this time. You may submit additional documentation..."
- **GDPR-Extended Notification:** Additionally includes information about the right to request human review of the automated decision (GDPR Article 22(3)); contact details for the DPO; and the right to lodge a complaint with the Information Commissioner's Office (UK) or relevant EU DPA

**Step 10: Watchlist and Sanctions Screening**
All "Verified" and manually "Approved" customers are screened against sanctions, watchlist, and PEP databases using the LexisNexis Bridger Insight XG screening engine integrated via API into the FCRM platform.

Databases screened:
- OFAC Specially Designated Nationals (SDN) and Consolidated Sanctions Lists
- UN Security Council Consolidated List
- EU Consolidated Financial Sanctions List
- UK HM Treasury Sanctions List
- Monetary Authority of Singapore Sanctions List
- World-Check One PEP and adverse media database

Match disposition: True positive sanctions matches (exact name + date of birth + jurisdiction match) result in automatic block and immediate escalation to the Chief Compliance Officer for evaluation of a blocked property / suspicious activity report filing obligation. Potential PEP matches trigger routing to the EDD procedure (Section 5.5).

**Step 11: Risk Rating Assignment**
The FCRM platform auto-calculates a risk rating using the following weighted scoring model:

| Risk Factor | Weight | Low Risk Indicator (1 point) | Medium Risk Indicator (5 points) | High Risk Indicator (15 points) |
|---|---|---|---|---|
| Customer Type | 25% | Individual, US resident | Individual, non-US; or SME with simple UBO structure | Complex corporate entity; multi-jurisdictional UBO chain; trust or foundation |
| Jurisdiction | 30% | US, CA, UK, DE, FR, AU, NZ, JP | All other FATF member jurisdictions | High-risk third countries (FATF grey/black list); OFAC sanctioned jurisdictions |
| PEP Status | 20% | Not a PEP | — | Confirmed PEP (or RCA) |
| Product/Service Risk | 15% | Patient financing < $50,000, unsecured | Merchant acquiring for standard-risk healthcare MCC codes; invoicing financing | High-risk merchant codes; cross-border acquiring; correspondent banking |
| Adverse Media / News | 10% | No adverse media | Minor adverse media (financial difficulties, regulatory fines not related to financial crime) | Serious adverse media (fraud, ML, sanctions evasion allegations); ongoing law enforcement investigation |

**Risk Scoring Thresholds:**
- **Low Risk:** Score < 3.0
- **Medium Risk:** Score 3.0 – 7.5
- **High Risk:** Score > 7.5

### 5.2 Customer Onboarding Workflow — Healthcare Provider Merchants (B2B)

This procedure defines the KYC onboarding workflow for legal entity customers—hospitals, clinics, and other healthcare providers establishing HealthPay payment processing merchant accounts.

**Step 1: Account Initiation via HealthPay Merchant Portal**
The authorized representative of the applying entity creates an account via `merchant.healthpay.com`, enters the entity's legal name, jurisdiction of incorporation, Tax Identification Number (TIN) / Employer Identification Number (EIN) / VAT registration number, and estimated monthly processing volume.

**Step 2: Entity Documentation Collection**
The system generates a tailored document request list based on the entity's jurisdiction and legal form:

| Entity Type | Required Documents |
|---|---|
| US Corporation / LLC | Certificate of Incorporation / Articles of Organization; IRS CP-575 EIN confirmation letter or W-9; Operating Agreement or Bylaws designating the authorized signatory |
| US Non-Profit | IRS 501(c)(3) determination letter; Articles of Incorporation; Board resolution authorizing the banking relationship |
| UK Limited Company | Certificate of Incorporation (Companies House); Memorandum and Articles of Association; Extract from Companies House listing current Directors and Persons with Significant Control (PSC register) |
| EU GmbH / BV / SARL / SAS | Commercial Register Extract (Handelsregister / Kamer van Koophandel / Registre du Commerce et des Sociétés / Registre National des Entreprises) not older than 90 days; Articles of Association; Valid VAT Identification Number |
| Singapore Private Limited | ACRA Business Profile (not older than 14 days); Memorandum and Articles of Association; Board Resolution appointing authorized signatories |
| Canada Corporation | Certificate of Incorporation / Articles of Incorporation; Canada Revenue Agency Business Number confirmation; Minute book extract confirming director and officer appointments |

**Step 3: Beneficial Ownership Identification**
The authorized representative must complete the "Beneficial Ownership Certification Form" (MHL-UBO-001, generated within the FCRM platform). The form captures:

For each natural person identified as a Beneficial Owner:
- Full legal name (including all middle names)
- Date of birth
- Citizenship / nationality
- Residential address (not a PO Box or Registered Agent address)
- National identification number (passport number or national ID)
- Percentage of equity interest held (if ownership prong)
- Description of the nature of substantial control exercised (if control prong)

**Step 4: Beneficial Ownership Verification**
Each identified beneficial owner (threshold: >=25% ownership OR exercises substantial control) must be identity-verified using the individual verification procedure (Section 5.1, Steps 3-8). Each UBO must submit their own documentary identity verification independently. Entity onboarding may not proceed until all UBOs are verified.

**Step 5: Enhanced Entity Verification**
The KYC Analyst performs additional verification steps:
1. **Business Registry Extract Verification:** Independently obtain and cross-reference the entity's details against the official business registry of the jurisdiction of incorporation (e.g., Companies House API, EDGAR for US public companies, Dun & Bradstreet for private entities)
2. **Physical Site Verification:** Confirm the entity has a physical operating presence (not solely a registered agent address). Accept office lease agreement, utility bill in entity name, or independent site visit report
3. **Authorized Signatory Verification:** Verify the identity and authority of the individual(s) authorized to bind the entity, via board resolution or secretary's certificate

**Step 6: Merchant Category Code (MCC) and Transaction Risk Assessment**
Assign the appropriate MCC and analyze the nature and purpose of the account based on the healthcare services provided. Assess the expected processing volume, average ticket size, chargeback ratio, and international transaction ratio against HealthPay's risk appetite thresholds.

| Risk Indicator | Threshold | Action |
|---|---|---|
| Expected Monthly Volume | > $500,000 | EDD trigger — Requires CFO approval |
| Average Ticket Size | > $25,000 | Elevated monitoring; Source of Funds verification |
| Estimated Chargeback Ratio | > 1.5% | Enhanced monitoring; Reserve account may be required |
| Cross-Border Processing | > 20% of volume | EDD — Confirm business rationale for multi-jurisdictional acquiring |

### 5.3 Identity Verification Methods and Acceptable Documents

#### 5.3.1 Acceptable Identity Documents — Natural Persons

| Document Tier | Document Type | Requirements |
|---|---|---|
| Primary | Valid, unexpired Passport (any jurisdiction) | Machine-readable zone (MRZ) must be legible; must contain photograph and signature |
| Primary | National Identity Card (EU/EEA jurisdictions) | Chip-based preferred; must contain photograph |
| Primary | US State Driver's License or State ID Card | Must comply with REAL ID Act standards; enhanced/digital licenses must be verifiable via issuing state API |
| Secondary (US only, supplementary only) | Social Security Card | Acceptable only for TIN verification; not acceptable as stand-alone identity document |
| Secondary (supplementary only, for address verification) | Utility Bill, Bank Statement, Council Tax Bill | Dated within 90 days; must show residential address matching the application; PO Box not acceptable |

**Unacceptable Documents:**
- Expired documents of any type
- Photocopies of documents without original presentation (digital onboarding: high-resolution capture required)
- Hospital-issued patient ID cards
- Student ID cards
- Library cards
- Temporary/paper driver's license without secondary photo ID

#### 5.3.2 Identity Document Verification Standards

| Verification Element | Standard |
|---|---|
| Photograph Match | Biometric facial comparison score >= 85% (Onfido) or manual visual comparison by Compliance Operations analyst confirming substantial likeness |
| Document Authenticity | Forensic document analysis: no pixel manipulation, no font substitution, security feature validation (holograms, UV features, microprinting) |
| Data Integrity | No evidence of name, date of birth, document number, or expiration date alteration |
| Expiration | Document must be valid as of the date of onboarding. Expired documents, even if recently expired, are not acceptable for initial verification |
| Liveness Detection | Passive and active liveness detection for biometric selfie; injection attack detection (not a virtual camera); presentation attack detection (not a photo-of-a-photo, not a mask) |

### 5.4 Enhanced Due Diligence (EDD) Procedure

EDD is mandatory for all customers classified as High Risk (Risk Score > 7.5) and for any customer designated by the Compliance Operations Lead or Chief Compliance Officer as warranting enhanced scrutiny.

**Step 1: EDD Trigger and Case Creation**
The FCRM system automatically creates an EDD case upon:
- Risk Score exceeding 7.5 on initial risk rating
- Positive PEP determination
- Sanctions screening alert that, upon investigation, is determined to be a false positive but warrants enhanced monitoring
- Manual referral by a KYC Analyst

**Step 2: Source of Funds and Source of Wealth Verification**
For individual customers: The customer must provide documentation substantiating the origin of the funds to be used for the medical procedure or financing arrangement. Acceptable documentation includes:
- Bank statements from the past 6 months (all pages, not summaries)
- Investment portfolio statements
- Pay stubs / employment income verification (past 3 months)
- Tax returns for the most recent 2 tax years
- Sale proceeds documentation (property sale, business sale)
- Inheritance documentation (probate grant, will, executor statement)

For legal entity customers: Audited financial statements for the past 2 fiscal years; Bank reference letter from a recognized financial institution; Narrative description of the entity's business model, client base, and revenue streams.

**Step 3: Senior Management Approval**
No EDD-level customer may be onboarded or have High Risk status reduced without the documented approval of at least one member of the Senior Management committee (CFO, CEO, or their expressly delegated designee). The approval must be recorded in the FCRM case record with:
- Name and title of the approving official
- Date and time of approval
- Explicit acknowledgment that the elevated risk has been reviewed and accepted
- Any conditions or limitations imposed on the account (e.g., transaction amount limits, geographic restrictions)

**Step 4: Enhanced Ongoing Monitoring Parameters**
EDD customers are assigned a monitoring regime that includes:
- Transaction monitoring rules set to heightened sensitivity thresholds (25% lower than standard thresholds)
- Monthly account activity review (versus the standard quarterly review for Medium Risk and annual review for Low Risk)
- Mandatory 6-month review cycle for the EDD profile itself (full re-verification of identity, beneficial ownership, PEP status, and source of funds)

**Step 5: EDD — GDPR Supplementary Processing Notice**
Upon being identified as subject to EDD, the EU/EEA data subject receives an additional supplementary processing notice informing them that enhanced AML/CTF measures will process additional categories of their personal data, including financial data (GDPR Article 14 — information not obtained directly from the data subject is obtained from financial reference sources). This notice is issued within 30 days of obtaining the financial data.

### 5.5 PEP Identification and Management

**Step 1: PEP Screening at Onboarding**
All prospects and authorized representatives/UBOs are automatically screened against the World-Check One PEP database during Step 10 of the onboarding workflow (Section 5.1).

**Step 2: PEP Determination Validation**
A positive PEP indicator requires a manual validation by a designated Senior KYC Analyst. The analyst must:
1. Confirm the individual's identity matches the PEP database entry
2. Determine the PEP category: Foreign PEP, Domestic PEP, International Organization Head, Family Member (F), or Close Associate (CA)
3. Assess the PEP's jurisdiction and the level of public prominence

**Step 3: PEP Risk Assessment**
For confirmed PEPs, the analyst completes the "PEP Risk Assessment" form (MHL-PEP-001) within the FCRM platform, evaluating:
- The PEP's position and level of influence
- The corruption risk of the PEP's country/jurisdiction (Transparency International Corruption Perceptions Index reference)
- The nature and duration of the business relationship
- The anticipated transaction volume and complexity

**Step 4: PEP Enhanced Due Diligence Application**
All confirmed PEP relationships are automatically classified as High Risk. All elements of the EDD procedure (Section 5.4) apply, with the additional requirement that the Source of Wealth verification must be particularly rigorous — a simple bank statement is insufficient. Independent verification of the source of wealth is required, which may include real property records, business ownership registry extracts, salary scales for public officials in the relevant jurisdiction, or other independent corroborating documentation.

**Step 5: PEP Declassification**
PEP status persists for a minimum of 12 months after the individual leaves their prominent public function (FATF Recommendation 12). After this period, the Chief Compliance Officer may authorize a reassessment to reclassify the individual to a lower risk tier, provided that a documented risk assessment concludes that the individual no longer presents a heightened ML/TF risk.

**Step 6: Ongoing PEP Screening**
All existing customers are re-screened against the PEP database on a nightly batch basis. Any new PEP identification triggers an immediate account flag and the creation of an EDD case the following business day.

### 5.6 Ongoing Due Diligence and Periodic Review

**Standard Review Cadence:**

| Risk Rating | Periodic KYC Review Cycle | Trigger Events Requiring Immediate Review |
|---|---|---|
| Low Risk | 36 months from last review date | Change in beneficial ownership (>=25%); legal name change; notification from law enforcement or FIU; sanctions list re-designation |
| Medium Risk | 18 months from last review date | Same as Low Risk, plus: material increase in transaction volume (>150% of baseline); expansion into new jurisdiction; adverse media identified |
| High Risk | 6 months from last review date | Same as Medium Risk, plus: any adverse media; any law enforcement inquiry; any transaction pattern deviation identified by the FCRM monitoring rules |

**Periodic Review Procedure:**
1. **Profile Refresh Trigger:** 30 days prior to the scheduled review date, the FCRM platform generates an automated review task assigned to the Compliance Operations queue
2. **Identity Re-verification:** Request updated identity documentation if the identity document on file has expired; otherwise, confirm no material changes to name, date of birth, or identification number
3. **Beneficial Ownership Re-verification:** For legal entity customers, the authorized signatory must re-certify the beneficial ownership structure or notify Meridian of material changes. If the entity fails to respond within 45 days, the account may be restricted per Section 8 escalation procedures
4. **Risk Re-assessment:** Re-run the risk scoring model (Section 5.1, Step 11) with current data points
5. **Documentation:** Record the review in the customer's KYC profile in FCRM, noting any changes, the updated risk rating, and the date of the next scheduled review

### 5.7 Watchlist and Sanctions Screening — Ongoing Monitoring

**Nightly Batch Screening:**
Every 24 hours (execution at 02:00 UTC), the entire active customer base is re-screened against updated sanctions and watchlist databases. The LexisNexis Bridger Insight XG delta file import process updates all sanctions lists within 60 minutes of a new file being published by the issuing authority.

**True Positive Match Protocol:**
For any confirmed true positive sanctions match (Level 1 match: exact name + date of birth + jurisdiction match):
1. Immediate account suspension (automated system action)
2. Immediate notification to the Chief Compliance Officer, VP of Financial Services, and DPO (within 15 minutes by PagerDuty alert)
3. Compliance Operations Lead manually reviews the match within 1 hour
4. If confirmed, Chief Compliance Officer determines regulatory reporting obligations (OFAC blocked property report, SAR, or equivalent) within 24 hours
5. No funds may be released from the account pending resolution

### 5.8 Data Subject Rights Under GDPR — KYC-Specific Procedures

#### 5.8.1 Right of Access (GDPR Article 15)
A data subject who has undergone KYC verification may submit a Data Subject Rights Request (DSRR) via the Meridian Privacy Portal (`privacy.meridianhealth.com`), via email to `dpo@meridianhealth.com`, or via written correspondence to the DPO. The DPO's office will acknowledge the request within 5 business days and provide a final, comprehensive response within 45 calendar days of request verification. The response will include a structured, machine-readable export (JSON format) of all KYC data held about the individual, extracted from both the FCRM platform and the IDV processing subsystem.

#### 5.8.2 Right to Rectification (GDPR Article 16)
Individuals who identify inaccurate KYC data (e.g., misspelled name, incorrect address) will have such data corrected within 30 calendar days of receiving a substantiated rectification request, provided that the individual supplies documentary evidence supporting the correction. The rectification will be propagated to all downstream systems within the HealthPay platform within 5 business days of the correction being applied in the FCRM system of record.

#### 5.8.3 Right to Erasure (GDPR Article 17) — KYC Constraints
A request for erasure of KYC data is subject to the AML regulatory retention obligation (Section 5.9). Where the statutory retention period has not elapsed, the DPO will inform the data subject that the processing is necessary for compliance with a legal obligation (Article 17(3)(e)) and that erasure cannot be honored until the retention period expires. The data will, however, be restricted from further processing (Article 18(2)) except for storage and AML record-keeping purposes. A formal determination letter will be provided to the data subject within 45 days.

#### 5.8.4 Right to Restriction of Processing (GDPR Article 18)
Where the accuracy of KYC data is contested, processing will be restricted pending verification — typically within a 30-day investigation window. During this period, the customer's account will remain active but flagged as "KYC Data Contested," and any new credit decisions will be held pending resolution.

#### 5.8.5 Right to Object (GDPR Article 21)
Automated KYC decisions (including adverse decisions rendered by the IDV subsystem) may be objected to. An objection triggers a guaranteed human review of the automated decision within 21 calendar days. The human reviewer will be an individual not previously involved in the automated decision chain, designated from the Compliance Operations team, and authorized to override the automated decision upon confirming the individual's identity through alternative documentary means.

### 5.9 KYC Record Retention

| Record Category | Retention Period | Trigger for Retention Period Start |
|---|---|---|
| Customer Identification Records (all customer types) | 7 years | Date of account closure or termination of the customer relationship |
| Beneficial Ownership Certification Forms (MHL-UBO-001) | 7 years | Date of the most recent certification |
| EDD Case Files | 10 years | Date of case closure |
| SAR / STR filings and underlying documentation | 10 years | Date of filing |
| Adverse Decision Records (applicants not onboarded) | 5 years | Date of adverse decision notification |
| IDV Biometric Logs (not raw biometric data — see Section 5.1, Step 7) | 18 months | Date of IDV transaction |
| Data Subject Rights Request Logs | 3 years | Date of final response |

All retention periods are aligned with BSA/AML recordkeeping requirements (31 CFR § 1010.410) and, for EU/EEA data subjects, compliant with the storage limitation principle (GDPR Article 5(1)(e)). Upon expiration of the applicable retention period, KYC records will be securely and irreversibly purged from the FCRM platform and all backup systems using NIST SP 800-88-compliant data sanitization methods. An automated deletion log entry will be generated.

---

## 6. Controls and Safeguards

### 6.1 Access Control — Role-Based Access Control (RBAC)

Access to KYC data within the Meridian SaaS Platform is governed by a tiered RBAC model enforced through Azure Active Directory integration with multi-factor authentication (MFA) mandatory for all access tiers.

| Role | Access Level | Permissions |
|---|---|---|
| KYC Analyst (Compliance Ops) | Level 3 — Full Read, Limited Write | View and edit customer KYC profiles; approve/refer IDV cases; view risk scores and watchlist screening results; upload identity documents; export case reports. Cannot modify risk scoring rules; cannot delete records; cannot access SAR/STR filing records |
| Senior KYC Analyst (Compliance Ops Lead) | Level 4 — Full Read, Full Write, Approval | All Level 3 permissions; Approve EDD case decisions; Override risk scores with documented justification; Access and modify PEP assessment forms; View (but not file) draft SAR/STR reports |
| Customer Operations Agent | Level 1 — Limited Read, No Write | View high-level KYC status (Verified/In Progress/Failed); View customer name and KYC case ID; No access to identity documents, address, date of birth, or watchlist screening results |
| Data Protection Officer | Level 5 — Full Read, Export, Purge Authorization | Full read access to all KYC records for DSRR fulfillment purposes; Authorized to initiate record purges upon retention period expiry; Access all audit logs; No write/edit capability except for DSRR rectification under documented procedure |
| IDV System Administrator (IT) | Level 2 — Configuration Write, No PII Read | Modify IDV rule thresholds; Update sanctions list configurations; Monitor IDV system performance; Access masked/anonymized logs; No access to PII data within KYC records |
| Senior Management (Exec Committee) | Level 5 — Read-Only, Except for EDD Approval | View complete KYC profiles for EDD cases requiring approval; Execute approval workflows; No general browse access; All access logged |

**Access Control Principles:**
- Principle of Least Privilege enforced; no user shall have access beyond what is explicitly required for their role
- All access to KYC records is logged with timestamp, username, IP address, and record identifier in the Meridian SIEM (Splunk Cloud)
- Privileged access (Level 3 and above) requires quarterly access recertification by the role owner's direct manager
- Break-glass (emergency access) procedures exist for Level 5 access and require the simultaneous authorization of the VP of Financial Services and the Chief Compliance Officer; all such access is subject to post-event audit within 72 hours

### 6.2 Encryption Standards

| Data State | Encryption Standard | Implementation |
|---|---|---|
| Data in Transit | TLS 1.3 | Enforced across all Meridian network segments, API gateways, and external partner integrations. TLS 1.2 permitted only for legacy partner systems with a documented exception; all TLS versions below 1.2 are deprecated and blocked at the network perimeter |
| Data at Rest — Structured KYC Data (FCRM platform) | AES-256-GCM | AWS RDS encryption with Customer-Managed Key (CMK) via AWS Key Management Service (KMS); key rotation every 365 days |
| Data at Rest — Document Images (S3 buckets) | AES-256-CBC, Server-Side Encryption with Customer-Provided Keys (SSE-C) | Document images (ID documents, proof of address, EDD supporting documents) encrypted with SSE-C keys managed within the Meridian on-premises Luna HSM; keys not accessible to AWS personnel |
| Data at Rest — Biometric Templates (segregated IDV storage) | AES-256-GCM with ephemeral key | Ephemeral volume encryption; volume destroyed upon template deletion (Section 5.1, Step 7) |

### 6.3 Audit Logging and Monitoring

The FCRM platform and IDV subsystem generate comprehensive audit logs capturing all access, modification, and decision events related to KYC records. The logging schema captures:

| Event Type | Captured Attributes |
|---|---|
| Record Creation | Timestamp, User ID, IP Address, Customer ID, Channel (Portal/API/Manual), Geographic Origin |
| Record Modification | Timestamp, User ID, Field Modified, Old Value (hashed), New Value, Reason Code |
| Record Deletion (Retention Purge) | Timestamp, Authorization ID (DPO + CFO conjoint), Deletion Method Verifier, Record Reference |
| Access (View/Export) | Timestamp, User ID, Customer ID, Records Accessed, Access Duration, IP Address, Session ID |
| Authentication Events | Timestamp, User ID, Authentication Method, Success/Failure, IP Address, Geolocation |
| Decision Events (Approve/Deny/Refer) | Timestamp, Decision, Decision Source (Automated/Manual), Reviewer ID (if manual), Confidence Score, Risk Rating, Decision Notes |

Logs are shipped to Splunk Cloud in real-time, retained for 7 years (aligned with KYC record retention), and monitored by the Meridian SOC for anomalous access patterns, privilege escalation attempts, and bulk export activity.

### 6.4 Segregation of Duties

No single individual shall be capable of both initiating a KYC review and approving a high-risk or contested decision. The following segregation of duties matrix is enforced:

| Duty Pair | Segregation Enforcement |
|---|---|
| Initiating Customer Onboarding vs. Approving Adverse Decision Override | System-enforced: A Customer Operations Agent who initiates onboarding cannot be assigned as the manual reviewer for an adverse decision on the same case |
| Conducting EDD Investigation vs. Approving Senior Management Sign-off | Procedural enforcement: No individual who serves as the primary EDD investigator may serve as the approving Senior Management official on the same case |
| Submitting SAR Recommendation vs. Filing Decision | The KYC Analyst recommending a SAR filing cannot be the same person who makes the final filing decision (CCO or designated AML Officer) |

### 6.5 Physical Security

All physical servers, workstations, and data storage devices housing KYC processing systems are secured within Meridian-controlled data center environments (Equinix colocation facilities in Ashburn, VA, and Amsterdam, Netherlands) and office locations. Physical access controls include biometric (fingerprint and iris scan) access to server cages; 24/7 CCTV with 90-day retention; mandatory escorted access for all non-Meridian personnel; and logged access events correlated with electronic access logs.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The effectiveness of the KYC verification program is measured through the following quantitative metrics:

| KPI | Target | Measurement Method | Reporting Cadence |
|---|---|---|---|
| **Automated IDV "Verified" Rate** | >= 85% for Low-Risk jurisdictions; >= 70% for all jurisdictions | (Total Verified / Total IDV Attempts) * 100, excluding technical failures | Weekly operational dashboard |
| **Manual Review Queue — Time to Decision** | <= 4 business hours for standard cases; <= 2 business hours for expedited cases; 95th percentile compliance | Cycle time from manual review case creation to decision timestamp | Weekly; Monthly trend report |
| **Watchlist Screening False Positive Rate** | <= 3% of screened records require manual disposition; 0 true positives acceptable for onboarding | (Records triggering manual review / Total records screened) * 100 | Monthly |
| **EDD Case Approval Timeliness** | EDD cases fully documented and presented for Senior Management approval within 5 business days of EDD trigger | Cycle time from EDD case creation to approval-ready status | Monthly |
| **Periodic Review Completion Rate** | >= 95% of scheduled reviews completed within 30 days of scheduled review date | (Reviews completed within window / Reviews scheduled) * 100 | Monthly |
| **Adverse Decision Overturns on Human Appeal** | <= 5% of automated adverse decisions overturned upon human review | (Overturned decisions / Total human appeals) * 100 | Monthly |
| **GDPR Data Subject Rights Response — Timeliness** | Acknowledgment: 100% within 5 business days; Full Response: 100% within the timeline specified in Section 5.8.2 | Measured from DSRR receipt timestamp to response transmitted timestamp | Monthly; Quarterly DPO report to Board |

### 7.2 Dashboard Configuration

The "KYC Program Health" dashboard (Tableau, sourced from FCRM and IDV system data warehouses) is available to the Financial Services leadership, Compliance Operations, and the DPO. The dashboard includes:

- **Operational Panel (Real-time/Near-real-time):**
  - Current manual review queue depth (count, aging by hours)
  - Automated IDV pass/refer/reject rates by jurisdiction and document type
  - Sanctions screening match rate and disposition breakdown
- **Risk Panel (Daily Refresh):**
  - Customer population distribution by risk rating (Low/Medium/High)
  - PEP population count and jurisdiction distribution
  - EDD case volume and aging
- **Compliance and Audit Panel (Monthly Refresh):**
  - Periodic review completion trend (12-month rolling)
  - Exception count and type distribution
  - Training completion percentage by role
  - Data subject rights request volume and response timeliness

### 7.3 Reporting Cadence

| Report | Audience | Frequency | Content |
|---|---|---|---|
| KYC Operations Weekly Brief | VP of Financial Services; Compliance Operations Lead | Weekly (Monday 09:00) | Queue volumes, IDV rates, critical escalations, resource utilization |
| KYC Risk and Compliance Monthly Report | Chief Compliance Officer; VP of Financial Services; DPO | Monthly (5th business day) | All KPIs vs. targets; PEP statistics; EDD case summaries; SAR/STR filing volume; training compliance; exception register summary |
| Quarterly KYC Program Review | CFO; Chief Compliance Officer; Board Risk and Compliance Committee | Quarterly | Program effectiveness assessment; regulatory landscape update; resource adequacy review; risk appetite statement reaffirmation; material control changes or deficiencies |
| Annual KYC Risk Assessment | Board of Directors | Annually (Q4 board meeting) | Comprehensive assessment of inherent risk, control environment, and residual risk for the KYC/AML program; proposed changes to risk appetite, thresholds, or policy |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Definition

A KYC exception is a documented, approved deviation from the standard procedures defined in Section 5. Exceptions are granted only when strict adherence to the standard procedure is impossible or commercially unreasonable, and the underlying risk of the deviation has been assessed, documented, and accepted at the appropriate level.

### 8.2 Exception Categories and Approval Authority

| Exception Type | Examples | Approval Authority | Maximum Duration |
|---|---|---|---|
| **Document Deficiency Exception** | Customer unable to provide standard primary ID document; alternative ID accepted (e.g., refugee travel document, temporary protected status documentation) | Compliance Operations Lead | 90 days (remediation deadline to obtain standard documentation) |
| **Beneficial Ownership Verification Delay** | UBO located in jurisdiction with restricted registry access; UBO verification pending manual process | VP of Financial Services (Robert Liu) | 60 days from account opening; account restricted to receiving only until UBO verification completed |
| **PEP Declassification (Early)** | Former PEP requesting risk downgrade before standard 12-month period | Chief Compliance Officer (Sarah Chen) | Permanent (subject to annual re-review) |
| **High-Risk Customer Onboarding** | Approval to onboard despite High risk score where commercial rationale compelling | CFO (James Thornton) or CEO | Permanent, but subject to 6-month mandatory EDD review cycle |
| **Retention Period Extension** | Extension of standard 7-year retention for records subject to litigation hold, law enforcement preservation order, or ongoing investigation | General Counsel (via Litigation Hold Notice) and DPO | Duration of legal hold plus 6 months post-release |

### 8.3 Exception Request Procedure

1. **Identification:** The KYC Analyst or Customer Operations Agent identifies the need for an exception
2. **Documentation:** The requestor completes the "KYC Exception Request Form" (MHL-KYC-EXC-001) within the FCRM platform, documenting:
   - Customer identifier and type
   - Specific SOP section from which deviation is sought
   - Rationale for the deviation
   - Risk assessment (impact of not performing the standard control)
   - Proposed compensating controls
   - Proposed remediation plan and deadline
3. **Compliance Review:** The Compliance Operations Lead reviews the exception request and appends their risk assessment and recommendation (Approve / Reject / Escalate to next level)
4. **Approval:** The exception is routed to the designated Approver per the matrix in Section 8.2. The Approver must respond within 2 business days for standard exceptions and 24 hours for urgent exceptions
5. **Recording:** All exceptions, including rejected ones, are recorded in the central Exception Register maintained by the Compliance Operations Lead. The register is reviewed at each monthly KYC Risk and Compliance Meeting
6. **Remediation Tracking:** Approved exceptions with a remediation deadline are tracked in the FCRM platform. Reminders are generated at 14 days and 7 days prior to the deadline. Overdue remediations are escalated to the VP of Financial Services

### 8.4 Escalation Matrix

| Event | Escalation Path | Timeframe |
|---|---|---|
| True Positive Sanctions Match | IDV System → Compliance Operations Lead → Chief Compliance Officer → CFO + General Counsel | 15 minutes (alert); 1 hour (review); 24 hours (filing decision) |
| Law Enforcement Inquiry (Subpoena, National Security Letter, Production Order) | Front-line recipient → General Counsel + Chief Compliance Officer + DPO | Immediate; no action taken without General Counsel approval |
| Internal Fraud / Employee Misconduct in KYC Process | Compliance Operations Lead → Chief Compliance Officer → VP of Financial Services → Chief People Officer (if employee) | 1 hour (detection); 24 hours (initial report); 5 business days (investigation plan) |
| Widespread IDV System Failure (>= 25% of onboarding attempts failing due to technical error) | IDV System Administrator → VP of Engineering (HealthPay) → VP of Financial Services → DPO (if EU data subjects affected) | 30 minutes (detection); 1 hour (initial assessment); 4 hours (status update to leadership) |
| Data Subject Rights Complaint to Supervisory Authority | DPO → Chief Compliance Officer → General Counsel → Executive Committee | 24 hours (notification of complaint); 5 business days (preliminary response plan) |

---

## 9. Training Requirements

### 9.1 Role-Based Training Curriculum

All personnel identified in the RACI matrix (Section 3.1) as Responsible, Accountable, or Consulted must complete the following training curriculum:

| Training Module | Target Audience | Duration | Frequency | Delivery Method |
|---|---|---|---|---|
| **KYC Fundamentals and Regulatory Landscape** | All Financial Services employees; Compliance Operations; Customer Operations | 3 hours | Initial (on hire); Annual refresher | Meridian LMS (Workday Learning) — self-paced eLearning with end-of-module assessment |
| **Identity Verification Procedures** | Compliance Operations team; IDV System Administrator; relevant Product and Engineering | 4 hours | Initial; Annual refresher (2 hours) | Instructor-led (virtual or in-person) by the Compliance Operations Lead or external AML training provider |
| **Enhanced Due Diligence and PEP Management** | Senior KYC Analysts; Compliance Operations Lead; Chief Compliance Officer | 4 hours | Initial; Biannual refresher | Classroom-based, case-study method, delivered by external AML/FCC training provider |
| **GDPR KYC-Specific Data Protection** | All KYC personnel; DPO office; any role with access to EU/EEA KYC data | 2 hours | Initial; Annual refresher (1 hour) | Meridian LMS — module includes Meridian-specific data flow diagrams, DSRR handling procedures, and case scenarios |
| **Sanctions and Watchlist Screening Operation** | Compliance Operations; IDV System Administrator | 2 hours | Initial; Ad-hoc upon major sanctions program change (e.g., new country sanctions) | Instructor-led by Chief Compliance Officer or external sanctions counsel |
| **Automated Decision Systems and Bias Awareness** | IDV System Administrator; Product Managers; Compliance Operations; DPO | 1.5 hours | Initial; Biennial | Meridian LMS, joint module developed by Compliance, Data Science, and DPO office |

### 9.2 Assessment and Competency

Each training module requires an end-of-module assessment with a passing score of 80% or higher. Personnel who fail the assessment must re-take the training module within 10 business days and pass the re-assessment. Personnel who fail the re-assessment are restricted from performing KYC-related duties until competency is demonstrated. For the instructor-led modules, competency is assessed through practical exercises (e.g., completing a mock EDD case file to defined standards).

### 9.3 Training Tracking and Reporting

All training assignments, completion status, and assessment scores are tracked in Workday Learning. At each monthly KYC Risk and Compliance Meeting, the Compliance Operations Lead reports on:
- Training completion rates by role (target: 100% completion by due date for all mandatory modules)
- Assessment pass rates
- Any overdue or outstanding training requirements

### 9.4 New Hire Onboarding

New hires in any KYC-relevant role must complete all applicable Initial training modules within 30 calendar days of their start date. They may not independently conduct manual reviews, approve exceptions, or perform EDD investigations until all mandatory initial training has been completed with a passing assessment score and their access has been provisioned under the supervision of a qualified Senior KYC Analyst.

---

## 10. Related Policies and References

### 10.1 Meridian Health Technologies Internal SOPs

| SOP ID | Title | Relationship to KYC |
|---|---|---|
| SOP-FIN-001 | Anti-Money Laundering / Counter-Terrorist Financing Program | Overarching AML/CTF policy; KYC/CDD is a core pillar. Referenced for SAR/STR filing obligations and AML governance structure |
| SOP-FIN-006 | Customer Risk Assessment Methodology | Detailed description of the risk scoring model, factor weightings, and validation methodology; supplements Section 5.1 (Step 11) of this SOP |
| SOP-FIN-008 | Suspicious Activity Report Filing Procedures | Referenced in Section 5.7 (sanctions match protocol) and Section 8.4 (escalation for law enforcement inquiries) |
| SOP-PRIV-001 | Data Subject Rights and Privacy Request Handling | General privacy policy; this KYC SOP provides the KYC-specific procedural overlay for GDPR rights |
| SOP-PRIV-003 | International Data Transfer Mechanism | Defines the Standard Contractual Clauses and supplementary measures governing cross-border KYC data flows between Meridian entities and processors |
| SOP-PRIV-008 | Data Protection Impact Assessment Methodology | Defines when a DPIA is required; KYC processing (including biometric identity verification and large-scale processing of PII) was subject to DPIA completed on 2025-01-22 |
| SOP-IS-004 | Identity and Access Management | RBAC framework, MFA enforcement, access recertification referenced in Section 6.1 |
| SOP-IS-012 | Encryption and Key Management Standards | Encryption standards and key lifecycle management as referenced in Section 6.2 |
| SOP-CUST-003 | Customer Communication Templates and Fair Processing Notices | Templates for adverse decision notifications and fair processing notices referenced in Section 5.1, Steps 2 and 9 |

### 10.2 External Regulatory References

| Reference | Description |
|---|---|
| Regulation (EU) 2016/679 (General Data Protection Regulation) | Articles 5, 6, 7, 13, 14, 15, 16, 17, 18, 21, 22, 25, 32, 35 |
| USA PATRIOT Act (Public Law 107-56) Section 326 | Customer Identification Program requirements |
| 31 CFR § 1010.230 | Beneficial ownership requirements for legal entity customers (FinCEN CDD Rule) |
| Directive (EU) 2018/843 (5th Anti-Money Laundering Directive) | CDD/EDD obligations, PEP definition, UBO register access |
| Directive (EU) 2015/849 (4th Anti-Money Laundering Directive) | Foundational CDD obligations, retained where not superseded by AMLD5 |
| FATF (2012, updated 2022, 2023, 2024, 2025) 40 Recommendations | Global AML/CTF standards, particularly Recommendations 10 (CDD), 12 (PEPs), 22 (DNFBPs), and 24 (Transparency and beneficial ownership of legal persons) |
| Monetary Authority of Singapore Notice 626 | Prevention of Money Laundering and Countering the Financing of Terrorism — applicable to Singapore operations |
| Proceeds of Crime (Money Laundering) and Terrorist Financing Act (S.C. 2000, c. 17) and associated Regulations | Canadian CDD and beneficial ownership requirements |
| AICPA TSP Section 100 (2017) Trust Services Principles | Confidentiality criterion, applicable to the KYC data environment |

---

## 11. Revision History

| Version | Effective Date | Author | Approver | Summary of Changes |
|---|---|---|---|---|
| 1.0 | 2021-03-15 | A. Patel (Compliance Manager) | J. Thornton (CFO) | Initial publication of KYC SOP for HealthPay Patient Financing product launch |
| 2.0 | 2022-09-01 | M. Chen (Compliance Ops Lead) | J. Thornton (CFO) | Major revision: Added Section 5.2 (B2B Onboarding) for Healthcare Provider Merchant launch; integrated LexisNexis Bridger Insight XG configuration details |
| 3.0 | 2023-11-12 | K. Williams (VP Compliance, interim) | J. Thornton (CFO) and M. Johansson (DPO) | Post-regulatory examination revision: Strengthened EDD source of wealth procedures (Section 5.4, Step 2); enhanced PEP ongoing screening (Section 5.5, Step 6); added GDPR Article 22 automated decision-making transparency provisions; expanded training requirements for GDPR modules |
| 3.1 | 2024-06-05 | S. Chen (CCO) | R. Liu (VP Financial Services) | Minor revision: Updated retention periods for IDV biometric logs; adjusted manual review queue SLA targets; incorporated NIST AI RMF reference for automated KYC decision systems; approved by incoming VP (Robert Liu) |
| 4.0 | 2025-01-20 | Compliance Operations Team (S. Chen, CCO as lead) | J. Thornton (CFO) | Comprehensive re-write for major system migration: FCRM platform upgrade (v8.0); Onfido IDV engine integration v3.2; transition to AES-256-GCM encryption standard. Expanded beneficial ownership cascading requirements for multi-layer corporate structures. Streamlined EU/EEA biometric handling controls post-EDPB guidance on facial recognition in financial services. Added Section 8.3 Exception Request Procedure and MHL-KYC-EXC-001 form. |
| 4.1 | 2025-10-28 | Compliance Operations Lead (L. Okonkwo) | R. Liu (VP Financial Services) and J. Thornton (CFO) | Post-Singapore MAS audit remediation: Enhanced Monetary Authority of Singapore Notice 626 alignment; updated PEP database integration to include Singapore Ministry of Home Affairs PEP list; added Singapore-specific entity documentation requirements (Section 5.2, Step 2); revised escalation matrix to include Monetary Authority of Singapore notification protocol for sanctions matches. Incorporated updated FATF 2025 interpretive note changes to Recommendation 24 (UBO threshold precision). Approved and effective 2025-10-28. |
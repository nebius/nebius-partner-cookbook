---
sop_id: "SOP-FIN-006"
title: "Lending Decision Documentation"
business_unit: "Financial Services"
version: "5.7"
effective_date: "2025-12-06"
last_reviewed: "2026-09-21"
next_review: "2027-03-10"
owner: "Robert Liu, VP of Financial Services"
approver: "James Thornton, Chief Financial Officer"
classification: "Internal"
regulations:
  - "SR 11-7"
  - "EU AI Act"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Lending Decision Documentation

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, controls, and operational requirements for documenting all lending decisions made through the Meridian HealthPay Financial Services platform. The purpose is to ensure that every credit decision—whether automated, hybrid, or manual—is thoroughly documented in a manner that satisfies model risk management requirements under SR 11-7, transparency and human oversight obligations under the EU AI Act, fair lending obligations under the Equal Credit Opportunity Act (ECOA) and Regulation B, and data subject rights under the General Data Protection Regulation (GDPR). This SOP operationalizes the Board-approved AI Governance Charter by translating high-level principles into auditable, repeatable processes.

### 1.2 Scope

This SOP applies to:

**Geographic Scope:**
- All lending activities originated, adjudicated, or serviced through the HealthPay Financial Services platform in the United States, Canada, United Kingdom, Germany, France, Netherlands, and any other jurisdiction where Meridian Health Technologies, Inc. operates as a licensed lender or technology service provider to regulated lending institutions.

**Product Scope:**
- Patient financing installment loans (3, 6, 12, 24, 36, 48, and 60-month terms)
- Medical procedure-specific lending products (elective, non-elective, emergency)
- Provider-embedded financing programs (white-label lending solutions deployed at partner hospitals and clinics)
- Medical credit card receivables purchasing programs
- Healthcare practice acquisition and expansion financing
- Medical equipment leasing and financing

**System Scope:**
- HealthPay Credit Engine (decisioning models v4.3 through v5.2)
- HealthPay Document Management System (DMS)
- HealthPay Adverse Action Notification System (AANS)
- AWS S3 lending decision archives (us-east-1, eu-west-1)
- Snowflake lending analytics data warehouse
- MLflow model registry and experiment tracking
- LangSmith AI tracing infrastructure

**Exclusions:**
- Claims advance factoring products (governed by SOP-FIN-008)
- Vendor payment processing float (governed by SOP-FIN-004)
- Internal corporate credit card programs (governed by SOP-CORP-012)

### 1.3 Target Audience

This SOP is binding upon all personnel involved in the lending lifecycle, including but not limited to: credit analysts, underwriting managers, model developers, model validators, compliance officers, legal counsel, customer operations representatives, data engineers supporting credit model pipelines, and any third-party vendors or consultants with access to lending decision systems or data.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Adverse Action** | A refusal to grant credit in the amount or on substantially the terms requested, a termination of an account or an unfavorable change in the terms of an account, or a refusal to increase the amount of credit available. Also includes any action defined as adverse under ECOA/Regulation B or Article 22 of the GDPR (automated individual decision-making). |
| **Automated Decision-Making** | A credit decision generated entirely by algorithmic means without substantive human intervention in the approval, denial, or terms-setting process. Defined per GDPR Article 22 and EU AI Act Article 14. |
| **Challenge Event** | A formal dispute initiated by an applicant or borrower regarding a lending decision, triggering the reinvestigation procedures detailed in Section 5.9. |
| **Composite Decision Score** | The weighted aggregate output of all HealthPay Credit Engine sub-models (ability-to-pay, propensity-to-repay, fraud risk, regulatory eligibility, and affordability assessment) that informs the final credit adjudication. Scale: 200-850. |
| **Documentation Package** | The complete, immutable record set required for each lending decision, consisting of the Decision Rationale Record (DRR-01), input data snapshot, model version attestation, override justification (if applicable), and adverse action notice (if applicable). |
| **Human-in-the-Loop (HITL)** | A decision architecture where an automated recommendation is subject to meaningful human review, intervention, and override capability before becoming final. Required for all EU/UK lending decisions exceeding the Automated Decision Threshold (see Section 5.3.4). |
| **Meaningful Human Review** | A substantive evaluation by a qualified, trained credit professional who exercises independent judgment, reviews all model inputs and outputs, considers factors outside the model scope, and documents their rationale before affirming, modifying, or rejecting the automated recommendation. Rote ratification does not constitute meaningful review. |
| **Model Deviation** | Any instance where a final credit decision (approval, denial, terms, pricing) differs from the unmodified output of the current production Credit Engine model version. All deviations require override documentation per Section 5.6. |
| **Protected Characteristics** | Any applicant or borrower attribute protected under applicable anti-discrimination law, including but not limited to race, color, national origin, sex/gender, marital status, age, religion, disability, receipt of public assistance, sexual orientation, gender identity, and any other class protected in the relevant jurisdiction. |
| **Prohibited Basis Variable** | Any data element, model feature, or proxy variable that, if used in a credit decision, would create unlawful discrimination or constitute use of a protected characteristic prohibited by Regulation B, ECOA, or equivalent jurisdictional statute. |
| **Secondary Review** | A manual re-evaluation of a denied application conducted by a Senior Underwriter who was not involved in the initial credit decision, performed upon applicant request within the timeframes specified in Table 5.4. |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| AAN | Adverse Action Notice |
| AANS | Adverse Action Notification System |
| AFS | Annual Fair Lending Statement |
| CDS | Composite Decision Score |
| CFPB | Consumer Financial Protection Bureau (United States) |
| CMS | Case Management System (HealthPay Compliance module) |
| DMS | Document Management System |
| DRR | Decision Rationale Record |
| DPA | Data Protection Authority (EU/UK) |
| DPIA | Data Protection Impact Assessment |
| DSAR | Data Subject Access Request |
| ECOA | Equal Credit Opportunity Act (United States) |
| EIDA | Enhanced Impact-Driven Assessment |
| EUAIA | European Union Artificial Intelligence Act (Regulation 2024/1689) |
| FCA | Financial Conduct Authority (United Kingdom) |
| FRL | Fair Lending Review |
| GDPR | General Data Protection Regulation (EU) |
| HITL | Human-in-the-Loop |
| HOEPA | Home Ownership and Equity Protection Act (not applicable, but referenced for completeness in multi-product audits) |
| ICO | Information Commissioner's Office (United Kingdom) |
| KRI | Key Risk Indicator |
| MDR | Medical Device Regulation (EU) |
| ML | Machine Learning |
| MRM | Model Risk Management |
| MRSG | Model Risk Steering Group |
| NIST | National Institute of Standards and Technology |
| PRA | Prudential Regulation Authority (United Kingdom; relevant where Meridian acts as technology service provider to PRA-regulated lenders) |
| RACI | Responsible, Accountable, Consulted, Informed |
| RB | Regulation B (Equal Credit Opportunity, 12 CFR Part 1002) |
| SLA | Service Level Agreement |
| SR | Supervision and Regulation Letter (Federal Reserve) |
| TILA | Truth in Lending Act |
| UR | User Research |
| XAI | Explainable Artificial Intelligence |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix

The following matrix defines accountability for each function within the lending decision documentation lifecycle. All named role-holders must complete the mandatory training specified in Section 9 prior to assuming these responsibilities.

| Role | Responsible Individual(s) | Decision Documentation | Adverse Action Issuance | Model Deviation Approval | Fair Lending Review | DSAR Response | Regulatory Filing |
|---|---|---|---|---|---|---|---|
| Chief Financial Officer | James Thornton | Informed | Informed | **Accountable** (escalations) | Informed | Informed | **Accountable** |
| VP, Financial Services | Robert Liu | **Accountable** | Informed | Responsible (escalations) | **Accountable** | Informed | Responsible |
| Director, Credit Operations | Sarah Chen-Patel | Responsible | **Accountable** | **Accountable** (Tier 1) | Responsible | Informed | Consulted |
| Chief Compliance Officer | Dr. Marcus Okonkwo | Consulted | Responsible | Consulted | **Accountable** (escalations) | **Accountable** | Responsible |
| Lead Model Risk Analyst | Javier Rodriguez-Garcia | Responsible | Consulted | Responsible (MRM validation) | Responsible | Consulted | Consulted |
| Senior Underwriting Manager, US | Patricia Kowalski | Responsible | Responsible | Consulted | Responsible | Consulted | Consulted |
| Senior Underwriting Manager, EU/UK | Alistair Finch-Morley | Responsible | Responsible | Responsible (Tier 2, EU) | Responsible | Informed | Consulted |
| Data Protection Officer | Elena Vasquez-Richter | Consulted | Consulted | Consulted | Consulted | **Accountable** | Responsible (GDPR Art. 35-36) |
| Fair Lending Officer | Dr. Amina Bakari-Thomas | Consulted | Consulted | **Accountable** (fair lending veto) | Responsible | Consulted | Consulted |
| AI Ethics Officer | Professor Kenneth Liu | Consulted | Consulted | Consulted (AI Act Art. 14) | Consulted | Consulted | Consulted |
| Head of Legal, Financial Services | Victoria Sterling-Hale | Consulted | Responsible | **Accountable** (regulatory interpretation) | Consulted | Responsible | **Accountable** |

### 3.2 Role Descriptions

#### 3.2.1 VP, Financial Services (Robert Liu)
Serves as the SOP Owner. Accountable for the overall effectiveness of this SOP, resource allocation, and escalation of material issues to the Chief Financial Officer. Chairs the quarterly Fair Lending Review Committee. Holds authority to approve model deviations exceeding $250,000 aggregate exposure or affecting more than 50 applicants in any rolling 30-day period.

#### 3.2.2 Director, Credit Operations (Sarah Chen-Patel)
Responsible for day-to-day operational execution of all procedures herein. Maintains the Decision Rationale Record template library, oversees Credit Analyst team adherence to documentation SLAs, and serves as primary contact for internal audit inquiries related to lending documentation completeness and accuracy.

#### 3.2.3 Lead Model Risk Analyst (Javier Rodriguez-Garcia)
Responsible for ensuring all Credit Engine model documentation meets SR 11-7 Model Risk Management standards (SR Letter 11-7, "Supervisory Guidance on Model Risk Management"). Validates all model deviation justifications against model risk appetite thresholds. Maintains the model version inventory and coordinates with the Model Risk Steering Group on significant findings.

#### 3.2.4 Fair Lending Officer (Dr. Amina Bakari-Thomas)
Holds an independent veto over any model variable, override practice, or documentation gap that presents fair lending risk—specifically the risk of disparate impact on protected classes. This veto authority extends to model deployment, override approval, and product launch decisions. Reports directly to the Chief Compliance Officer with a dotted line to the Board Audit Committee.

#### 3.2.5 Data Protection Officer (Elena Vasquez-Richter)
Responsible for GDPR compliance oversight, including Article 35 Data Protection Impact Assessments for automated decision-making. Serves as primary liaison to EU Data Protection Authorities (DPAs) and the UK Information Commissioner's Office (ICO). Manages DSAR intake, tracking, and response coordination for all EU/UK lending data subject requests.

---

## 4. Policy Statements

### 4.1 Core Documentation Principle

Meridian Health Technologies, Inc. shall create, maintain, and retain a complete Decision Documentation Package for every credit application processed through the HealthPay Financial Services platform. This package shall be sufficient to enable an independent third party—such as a regulatory examiner, external auditor, or court—to reconstruct, understand, and evaluate the decision in its entirety, including all model inputs, outputs, overrides, and human judgments applied.

### 4.2 Non-Discrimination and Fair Lending

4.2.1 Meridian shall not discriminate against any applicant on any prohibited basis in any aspect of a credit transaction, including information collection, underwriting, pricing, servicing, or collections.

4.2.2 All credit models and decision rules shall be subject to annual disparate impact testing conducted by an independent third-party vendor engaged by the Fair Lending Officer. Testing results shall be reviewed at the Q4 Fair Lending Review Committee meeting and reported to the Board Audit Committee within 45 calendar days of receipt.

4.2.3 Documentation for each denied application shall include a plain-language statement of the principal reason(s) for denial, sufficient to satisfy ECOA/Regulation B §1002.9 and equivalent jurisdictional requirements (UK FCA Consumer Credit sourcebook CONC 5; EU Consumer Credit Directive Article 8).

### 4.3 Adverse Action Notification

4.3.1 All applicants who are denied credit or offered credit on materially less favorable terms than requested ("adverse action") shall receive a written Adverse Action Notice (AAN) within the regulatory timeframes specified in Table 4.1 below.

**Table 4.1: Adverse Action Notification Timeframes by Jurisdiction**

| Jurisdiction | Notification Deadline | Delivery Method(s) | Regulation Reference |
|---|---|---|---|
| United States | Within 30 calendar days of completed application receipt | Electronic (primary), USPS First Class Mail (upon applicant preference or electronic delivery failure) | ECOA § 701(d); Reg B §1002.9 |
| United Kingdom | Within 14 calendar days of decision | Electronic (secure portal), Royal Mail First Class | FCA CONC 5.2.3; Consumer Credit Directive 2008/48/EC |
| European Union (non-UK) | Within 14 calendar days of decision; additional Article 22(3) GDPR notification required for automated decisions | Electronic (secure portal), Deutsche Post/La Poste/PostNL as applicable | EU Consumer Credit Directive 2008/48/EC Art 8; GDPR Art 13-15, 22 |
| Canada | Within 30 calendar days | Electronic (secure portal), Canada Post Regular Mail | Provincial consumer protection statutes; Federal Consumer Protection Acts (varies by province) |

4.3.2 Each AAN shall include, at minimum:

- **Statement of Action:** Clear description of the adverse action taken.
- **Principal Reason(s):** Specific, plain-language reason(s) for denial or adverse terms; no more than four principal reasons listed in descending order of impact on the decision. Use of "credit bureau report" alone is insufficient; specific factor codes must be referenced.
- **ECOA Notice (US):** Standardized notice of rights under ECOA, including contact information for the CFPB.
- **Credit Bureau Information:** Name, address, and telephone number of the consumer reporting agency(ies) that furnished the credit report, if used in the decision.
- **Model-Based Decision Disclosure:** Notice that an automated model was used in the decision process and that the applicant has the right to request human review (mandatory for EU/UK decisions under GDPR Art 22(3); discretionary but recommended for US).
- **Secondary Review Right:** Explanation of the applicant's right to request a secondary manual review and instructions for doing so, including applicable timelines (see Table 5.4).
- **Lending Inquiry Contact:** Dedicated telephone number (+1-833-MERIDIAN-US; +44-800-MERIDIAN-UK; +49-800-MERIDIAN-EU) and email address (lendingreview@meridianhealthpay.com) for questions.

### 4.4 Record Retention

4.4.1 Lending Decision Documentation Packages shall be retained for the longer of: (a) seven (7) years from the date of final action on the application; (b) the statute of limitations for any claim arising from the transaction in the relevant jurisdiction plus three (3) years; or (c) any longer period specified by applicable regulation.

4.4.2 Retention shall be in tamper-evident, WORM-compliant (Write Once, Read Many) storage implemented through AWS S3 Object Lock with governance mode enabled. Immutability shall be applied within 24 hours of decision finalization.

4.4.3 Documentation for EU/UK data subjects shall additionally comply with the storage limitation principle of GDPR Article 5(1)(e) and shall be subject to annual retention justification review coordinated by the DPO.

### 4.5 EU AI Act High-Risk Classification Acknowledgment

Per Meridian's board-approved regulatory assessment dated September 12, 2026, the HealthPay Credit Engine v5.x series is classified as a "high-risk AI system" under Annex III, paragraph 5(b) of EU AI Act Regulation 2024/1689 (systems intended to evaluate the creditworthiness of natural persons or establish their credit score). Meridian acknowledges and accepts all obligations applicable to providers and deployers of high-risk AI systems under Title III, Chapters 2-4, including but not limited to: risk management system (Art 9), data governance (Art 10), technical documentation (Art 11), record-keeping (Art 12), transparency (Art 13), and human oversight (Art 14). This SOP constitutes a core element of the human oversight mechanism required by Art 14(2).

---

## 5. Detailed Procedures

### 5.1 Application Intake and Preliminary Eligibility Screening

**5.1.1 Digital Application Capture**

All lending applications shall be captured through the HealthPay Applicant Portal (US/Canada) or the HealthPay EU Applicant Gateway (UK/EU). The intake system shall:

1. Present jurisdiction-specific consent language for credit bureau access, affordability data sharing, and open banking permissions, with granular opt-in controls.
2. Capture the full application payload as a JSON object with SHA-256 hashing at submission timestamp.
3. Assign a unique, immutable Application Reference Number (ARN) formatted as `HP-APP-[YYYY]-[NNNNNN]` (e.g., `HP-APP-2025-482901`).
4. Perform real-time jurisdictional classification based on the applicant's declared country of residence, verified against government-issued identification document analysis where applicable.
5. Apply jurisdictional lending eligibility rules: specific excluded jurisdictions (OFAC-sanctioned countries, FATF grey-list countries with enhanced due diligence requirements) shall trigger automatic referral to the Compliance Review Queue for manual assessment.

**5.1.2 Preliminary Eligibility Gate**

Prior to Credit Engine invocation, all applications shall pass through the Preliminary Eligibility Gate, which applies deterministic, non-ML rules:

| Gate Rule | Threshold | Action if Failed |
|---|---|---|
| Minimum applicant age | 18 years (UK), 18 years (EU), 18 years (US, except 19 in AL and 21 in MS, PR) | Instant decline with jurisdictional age notice |
| Valid government ID verification | 95% confidence threshold through Onfido IDV v3.8 | Refer to Manual KYC Queue; no automated decision until cleared |
| Active OFAC/SDN/UK HMT/EU Consolidated List screening | Zero positive matches | Freeze application; escalate to Chief Compliance Officer within 2 hours |
| Minimum requested amount | $500 USD / £400 GBP / €450 EUR | Instant decline with "Below Minimum Loan Amount" notice |
| Maximum requested amount (consumer) | $100,000 USD (US), £75,000 GBP (UK), €85,000 EUR (EU) | Refer to Senior Underwriter for exception review per Section 8 |
| Debt-to-Income Ratio ceiling (preliminary estimate) | >65% DTI | Flag as "High DTI – Enhanced Review Required" but continue processing |

Any application failing a gate rule marked "Instant decline" shall be terminated immediately, and the AANS shall queue an Adverse Action Notice for delivery within the applicable jurisdictional timeframe (see Table 4.1). The preliminary eligibility decision and gate rule outcomes shall be recorded in the DRR-01 Section A.

### 5.2 Credit Engine Model Invocation and Decisioning

**5.2.1 Model Version Assignment**

All applications shall be processed by the current production version of the HealthPay Credit Engine, as specified in the Model Version Registry maintained by the Lead Model Risk Analyst. As of the effective date of this SOP version 5.7, the production models are:

| Model Component | US/Canada Version | UK/EU Version | Model Registry ID |
|---|---|---|---|
| Ability-to-Pay (ATP) Model | v5.2.1 | v5.2.1-eu | MRM-ATP-2025-Q4 |
| Propensity-to-Repay (PTR) Model | v5.2.0 | v5.2.0-eu | MRM-PTR-2025-Q4 |
| Fraud Risk Score | v3.1.4 | v3.1.4-eu | MRM-FRD-2025-Q4 |
| Affordability Assessment (UK/EU only) | N/A | v2.3.7 | MRM-AFF-2025-Q3 |
| Fair Lending Overlay | v4.0.2 | v4.0.2-eu | MRM-FLO-2025-Q4 |

Any model version upgrade or hotfix shall be approved through the Model Risk Steering Group change management process (see SOP-RSK-004) prior to production deployment. No lending decision shall be made using a model version that has not been registered, validated, and approved for production use.

**5.2.2 Model Invocation Logging**

Each model invocation shall generate an immutable log entry in the HealthPay Lending Decision Ledger (Amazon QLDB) containing:

- Application Reference Number (ARN)
- Model identifier and version for each invoked model component
- Complete input feature vector, including all raw and transformed variables
- All intermediary outputs (ATP score, PTR score, Fraud Risk score, Affordability score [UK/EU])
- Composite Decision Score (CDS: 200-850 scale)
- Automated decision recommendation (APPROVE / APPROVE WITH CONDITIONS / REFER / DECLINE)
- Credit limit and term recommendation, if applicable
- Pricing tier assignment (Tier 1 [preferred] through Tier 7 [subprime])
- Model invocation timestamp (ISO 8601, UTC)
- SHAP (SHapley Additive Explanations) values for the top 20 contributing features, mapped to plain-language reason codes
- LangChain tracing ID for full decision audit trail

The complete payload shall be archived as a JSON Lines file in the AWS S3 Decision Log Archive bucket (`s3://meridian-lending-decisions-[region]/[YYYY]/[MM]/[DD]/[ARN].jsonl.gz`) with SSE-KMS encryption using the dedicated Lending Decisions KMS key.

**5.2.3 Composite Decision Score Thresholds**

The following thresholds govern automated decision routing:

| CDS Range | Automated Recommendation | Action |
|---|---|---|
| 700-850 | APPROVE | Automatically approved at Pricing Tier 1-3; proceed to terms generation |
| 600-699 | APPROVE WITH CONDITIONS | Automatically approved at Pricing Tier 4-6; may include lower credit limit, shorter term, or rate adjustment |
| 500-599 | REFER | Application placed in Manual Underwriting Queue for human review; no automated decline |
| 350-499 | DECLINE (with Human Review required in EU/UK; see Section 5.3.4) | AAN queued; human review mandatory for UK/EU applicants; optional but available for US applicants upon request |
| <350 | Flagged for Fraud Review | Application frozen; referred to Fraud Review Team within 4 business hours |

**5.2.4 Secondary Credit Attributes Assessment (US only)**

For US applications receiving a CDS between 480-550, the system shall perform a secondary review of credit attributes before generating the final automated recommendation. This step evaluates thin-file or near-prime applicants for potential manual underwriting referral using the following criteria:

- Applicant has a credit score but fewer than three trade lines reporting within the last 24 months
- The primary decline reason is "Insufficient Credit History" or "Length of Credit History"
- Applicant DTI is below 50% and employment tenure exceeds 12 months

If all three criteria are met, the application shall be overridden from DECLINE to REFER and routed to Manual Underwriting Queue with a "Thin File Exception Flag."

### 5.3 Human Review Requirements

**5.3.1 Manual Underwriting Queue Assignment**

Applications receiving an automated recommendation of REFER, or those routed for manual review per EU/UK requirements, shall be assigned to the next available Credit Analyst through the HealthPay Credit Review Workbench using round-robin assignment weighted by analyst specialization (Medical Procedure Lending Specialist vs. General Consumer Lending Specialist).

**5.3.2 Credit Analyst Review Standards**

Each manual review shall include, at minimum:

1. **Income Verification:** Review of pay stubs, tax returns, or bank transaction data (via Plaid open banking integration) to validate stated income against documented income within a 15% tolerance threshold.
2. **Employment Stability Assessment:** Review of employment history gaps exceeding 60 days within the prior 24 months; each gap requires documented explanation from the applicant or analyst notation of "unexplained employment gap."
3. **Debt Obligation Reconciliation:** Cross-reference of applicant-stated obligations against credit bureau tradeline data; discrepancies exceeding 20% or $200/month (whichever is greater) require resolution.
4. **Medical Procedure Purpose Assessment (Medical Lending Products):** For procedure-specific loans, confirmation from the provider portal that the procedure is scheduled and the quoted amount matches the loan request within 10%.
5. **Compensating Factor Identification:** Explicit documentation of any positive factors not captured by the automated model that support approval (e.g., high liquid reserves, co-signer availability, exceptional employment stability, recent professional licensure).
6. **Override Justification:** If the analyst's recommendation differs from the automated recommendation, completion of the Override Justification Form DRR-02 per Section 5.6.

**5.3.3 Credit Analyst Decision Authority**

| Analyst Level | Maximum Approval Authority | Maximum Deviation Authority | Override Approval Required |
|---|---|---|---|
| Credit Analyst I | $25,000 | Not authorized | All deviations require Senior Underwriter review |
| Credit Analyst II | $50,000 | $10,000 aggregate/month | Manager approval for >$5,000 per decision |
| Senior Credit Analyst | $100,000 | $25,000 aggregate/month | Self-authorizing; reportable |
| Senior Underwriter | $250,000 | $50,000 aggregate/month | Self-authorizing; reportable to Director, Credit Operations |
| Director, Credit Operations | No limit within risk appetite | $100,000 per decision | Reported to VP, Financial Services within 24 hours |

**5.3.4 EU AI Act Article 14 Human Oversight Requirements (EU/UK Applications Only)**

For all lending applications involving EU or UK data subjects, the following mandatory human oversight controls shall apply:

1. **Automated Decision Threshold:** No fully automated credit denial shall become effective without review by a qualified Credit Analyst II or higher, regardless of CDS. The automated recommendation shall be presented as advisory input, not a final determination. This implements the "human-in-the-loop" requirement under EU AI Act Article 14(2).

2. **Override Capability Recording:** The Credit Review Workbench shall record, with keystroke-level granularity, every action taken by the reviewing analyst, including:
   - Time spent reviewing each section of the application
   - Whether the analyst accessed and reviewed the SHAP explanation for the model recommendation
   - Any changes made to the model's automated recommendation
   - The explicit textual justification provided for the final decision

3. **Meaningful Human Review Certification:** Before finalizing any EU/UK lending decision, the reviewing analyst shall certify, by clicking the "Meaningful Review Certified" button, the following attestation (displayed on-screen):

   > "I, [Analyst Name], certify that I have conducted a meaningful and substantive review of this application. I have examined the model recommendation and its explanation, considered factors both within and outside the model's scope, exercised independent professional judgment, and am not merely ratifying or rubber-stamping the automated output. I understand that a record of my review actions, including time spent and screens accessed, is retained for regulatory audit purposes."

4. **Human Oversight Logging:** All HITL reviews shall generate a Human Oversight Record (HOR-01) appended to the Decision Documentation Package. The HOR-01 shall include:
   - Analyst name, employee ID, and authorization level
   - Time-stamped sequence of review actions
   - Model recommendation vs. final decision comparison
   - Explicit override justification (if applicable)
   - Meaningful Human Review Certification timestamp

5. **Article 14(4) Reporting:** The EU/UK Senior Underwriting Manager (Alistair Finch-Morley) shall prepare a monthly Human Oversight Effectiveness Report summarizing override rates, override reason distributions, and any instances of "automated rubber-stamping" (defined as analyst approval of a model recommendation with no substantive interaction or comment within 120 seconds of opening the review). This report shall be submitted to the Model Risk Steering Group and the AI Ethics Officer within 10 business days of month-end.

### 5.4 Decision Rationale Record (DRR-01) Completion

**5.4.1 DRR-01 Template**

Every lending decision, whether automated, hybrid, or manual, shall generate a Decision Rationale Record on Form DRR-01 (current version 3.2). The DRR-01 shall be auto-populated with system-generated fields and completed with mandatory analyst inputs as specified below.

**Section A: Application Summary (System-Generated)**
- ARN, Application Timestamp, Jurisdiction, Product Type, Requested Amount, Requested Term
- Applicant Name, Verified Identity Indicator, KYC Clearance Timestamp
- Preliminary Eligibility Gate Results (all rules, pass/fail status)

**Section B: Model Decision Summary (System-Generated)**
- Model Version(s) invoked
- CDS and component scores (ATP, PTR, Fraud, Affordability)
- Top 5 contributing features and their SHAP values (plain-language descriptions)
- Automated Recommendation (APPROVE / APPROVE WITH CONDITIONS / REFER / DECLINE)
- Automated credit limit, term, APR, and monthly payment recommendation
- Any model flags or warnings generated (e.g., "High Model Uncertainty – Input data quality flag")

**Section C: Human Review and Final Decision**

| Field | System/Manual | Requirement |
|---|---|---|
| C.1 Human Review Conducted? | Manual (checkbox) | Mandatory boolean |
| C.2 Reviewer Name and ID | System (auto-populated from SSO) | Mandatory if C.1 = Yes |
| C.3 Review Start and End Timestamps | System (auto-captured) | Mandatory if C.1 = Yes |
| C.4 Final Decision | Manual (dropdown: APPROVE / APPROVE WITH CONDITIONS / DECLINE / COUNTER-OFFER) | Mandatory |
| C.5 Final Credit Limit | Manual (numeric, USD/GBP/EUR) | Mandatory if approved |
| C.6 Final Term (months) | Manual (dropdown: 3,6,12,24,36,48,60) | Mandatory if approved |
| C.7 Final APR (%) | Manual (numeric, 4 decimal places) | Mandatory if approved |
| C.8 Decision Deviates from Model Recommendation? | Manual (boolean) | Mandatory; if True, triggers DRR-02 requirement |
| C.9 Principal Reason(s) for Decision | Manual (ranked text, up to 4 reasons) | Mandatory. Must be specific and non-generic; "Credit score" alone is insufficient; use "Credit score below 620 due to recent delinquency and high credit utilization" or equivalent specificity. |
| C.10 Secondary Review Offered? | System (auto-calculation based on jurisdiction + decision type) | System-applied flag |
| C.11 EU/UK Article 14 Human Oversight Certification | Manual (button certification per 5.3.4.3) | Mandatory for all EU/UK applications |
| C.12 Override Form DRR-02 Attached? | System (auto-validation) | Mandatory if C.8 = True |

**5.4.2 DRR-01 Completeness Validation**

Prior to decision finalization, the HealthPay Credit Review Workbench shall execute an automated completeness check against all mandatory fields. Applications with incomplete DRR-01 forms shall not be eligible for decision finalization (i.e., the "Finalize Decision" button shall remain greyed out until all mandatory fields are populated).

The DMS shall timestamp the DRR-01 at finalization and compute a SHA-256 hash of the complete PDF rendering for tamper-evident archival. The hash shall be stored both in the QLDB lending decision ledger and in the applicant's permanent lending record in Snowflake.

**5.4.3 Adverse Action Notice Generation**

Upon any decision categorized as DECLINE or COUNTER-OFFER (where the counter-offer represents materially less favorable terms, defined as APR increase >5 percentage points, term reduction >12 months, or loan amount reduction >30%), the AANS shall:

1. Auto-generate an AAN in the applicant's declared language preference (English, Spanish, French, German, Dutch supported).
2. Populate the AAN with the principal reason(s) from DRR-01 Section C.9.
3. Include all disclosures required per Section 4.3.2 herein.
4. Include the data subject rights notice per Section 5.8 for EU/UK applicants.
5. Route the AAN through the following delivery waterfall:
   - Primary: Secure HealthPay Applicant Portal messaging (push notification + email alert)
   - Secondary (within 48 hours if primary not acknowledged): Email to verified applicant email address with encrypted PDF attachment
   - Tertiary (within 5 calendar days if secondary not acknowledged): Physical mail to verified applicant mailing address via USPS First Class / Royal Mail / Deutsche Post / equivalent
6. Log delivery status and timestamps in the HealthPay Communication Log.

### 5.5 Counter-Offer Documentation

When a credit decision results in a counter-offer (offering credit on terms less favorable than requested but not constituting a full denial), the following additional documentation requirements apply:

1. **Counter-Offer Matrix:** The DRR-01 shall auto-populate a comparison table showing Requested vs. Offered terms across amount, term, APR, and monthly payment side-by-side.
2. **Counter-Offer Rationale:** Section C.9 shall include, as the first principal reason, a statement explaining why the requested terms were not extended and what specific risk factor(s) drove the counter-offer terms.
3. **Auto-Expiry:** All counter-offers shall have an expiry date of 30 calendar days from issuance. The expiry date shall be prominently displayed on the counter-offer notice.
4. **Counter-Offer Tracking:** The CMS shall track all counter-offers issued, distinguishing between:
   - Counter-offers accepted (converted to originated loans)
   - Counter-offers declined (treated as adverse action; supplemental AAN issued confirming declination)
   - Counter-offers expired (treated as withdrawn by applicant after 30 days; no further AAN required)

### 5.6 Model Deviation and Override Documentation (DRR-02)

**5.6.1 Definition of Model Deviation**

A Model Deviation occurs in any instance where the final credit decision differs from the unmodified Credit Engine automated recommendation in any of the following dimensions:

- Decision outcome (Approved despite automated DECLINE, or Declined despite automated APPROVE)
- Credit limit deviates from automated recommendation by >20% or >$5,000 (whichever is greater)
- APR deviates from automated recommendation by >3 percentage points
- Term deviates from automated recommendation by >12 months
- Pricing tier assignment changed by more than one tier

**5.6.2 DRR-02 Override Justification Form**

All Model Deviations require completion of the Override Justification Form (DRR-02 v2.1). The DRR-02 shall contain:

| Field | Description |
|---|---|
| Linked Application ARN | Auto-populated |
| Override Type | Dropdown: Decision Outcome / Credit Limit / APR / Term / Pricing Tier / Multi-factor |
| Model Recommendation | Auto-populated from DRR-01 |
| Final Decision | Auto-populated from DRR-01 |
| Override Direction | Favorable to Applicant / Unfavorable to Applicant |
| Justification Category | Dropdown: Compensating Factor(s) Identified / Adverse Information Not in Model / Model Uncertainty Flag / Fair Lending Adjustment / Fraud Review Outcome / Income Verification Discrepancy / Employment Gap Resolution / Other (free text required) |
| Detailed Justification (minimum 250 characters) | Free text narrative explaining: (a) the specific factor(s) justifying deviation from the model; (b) why the model did not adequately capture this factor; (c) how the final decision aligns with Meridian credit policy and fair lending obligations; and (d) if the override is favorable to the applicant, rationale for why this does not constitute preferential treatment on a prohibited basis. |
| Supporting Documentation Reference(s) | File path(s) to supporting documents uploaded to DMS (bank statements, tax returns, verification reports, etc.) |
| Approver Name and ID | Per approval authority defined in Table 5.3.3 |

**5.6.3 Override Approval Workflow**

1. Analyst completes DRR-02 and clicks "Submit for Approval."
2. The CMS routes the override to the appropriate approver based on the analyst's authority level (Table 5.3.3) and the override exposure amount.
3. The approver reviews the DRR-02 within 8 business hours for consumer applications and 4 business hours for time-sensitive medical procedure lending.
4. The approver may: (a) Approve (DRR-02 attached, decision finalized); (b) Reject with Comments (returned to analyst for revision); (c) Escalate (routed to next higher authority with notation).
5. **Fair Lending Officer Veto:** Overrides meeting any of the following criteria shall be automatically flagged for Fair Lending Officer review prior to final approval:
   - Override is favorable (approval where model recommended decline) AND the applicant is a member of a protected class (as identified through the proxy methodology approved under SOP-RSK-011)
   - The override justification references compensating factors that could serve as proxies for prohibited basis variables
   - The override is the 5th or greater favorable override by the same analyst in the current calendar month, analyzed across all protected class dimensions
6. The Fair Lending Officer has 48 hours from flag to review and either approve, reject, or request modification. The Fair Lending Officer's decision is binding and may only be overturned by the Chief Compliance Officer in consultation with the Chief Financial Officer (joint sign-off required).

**5.6.4 Override Monitoring**

The Lead Model Risk Analyst shall generate a Monthly Override Monitoring Report analyzing:

- Total override count and rate (overrides / total decisions)
- Override distribution by type, analyst, jurisdiction, and protected class dimensions
- Performance of overridden loans vs. model-recommended loans (vintage-level comparison of delinquency, default, and prepayment rates at 6-month and 12-month horizons)
- Identification of analysts with override rates exceeding 2 standard deviations above the team mean

Results shall be presented to the Model Risk Steering Group monthly and summarized in the Quarterly Fair Lending Report to the Board Audit Committee.

### 5.7 Fair Lending Comparative File Review

**5.7.1 Monthly Disparate Treatment Analysis**

The Fair Lending Officer shall oversee a monthly comparative file review of lending decisions, conducted using the Meridian Fair Lending Analytics Dashboard (Snowflake + Tableau). The analysis shall include:

- Approval/denial rates disaggregated by race, ethnicity, sex, age group, and geography (Census tract/MSA) for US applications
- Approval/denial rates disaggregated by jurisdiction, product type, and estimated income quartile for UK/EU applications
- APR distribution analysis by protected class dimension (mean, median, standard deviation, interquartile range)
- Adverse action reason code distribution comparison (approval-eligible vs. denied populations)
- Matched-pair testing: statistical comparison of marginal outcomes for applicants matched on all objective credit characteristics, differing only on protected class proxy variables

Any disparity exceeding the statistical threshold of 10% relative difference with p <0.05 significance shall be escalated as a "Fair Lending Disparity Flag" and investigated per Section 8.5.

**5.7.2 Quarterly Fair Lending Review Committee**

The Fair Lending Review Committee, chaired by the VP, Financial Services, shall convene quarterly to review:

- All Fair Lending Disparity Flags raised in the preceding quarter and their resolution status
- Annual independent disparate impact analysis results (or quarterly interim results if testing is continuous)
- Override analysis results and any analyst-specific patterns
- Pending or anticipated regulatory changes affecting fair lending obligations
- Training completion and effectiveness metrics

### 5.8 Data Subject Rights and Privacy Notices (EU/UK)

**5.8.1 Transparency and Privacy Information**

All EU/UK applicants shall receive a Privacy Notice at the point of application intake via the HealthPay EU Applicant Gateway. The notice shall be presented as a layered notice with a brief "key information" panel and a link to the full Privacy Notice document.

The Privacy Notice shall address the following processing purposes, as required under Article 13(1)(c) and Article 14(1)(c):

- Processing for credit eligibility assessment and automated decision-making
- Sharing of application data with credit reference agencies (TransUnion UK, Experian EU, Equifax, etc.)
- Sharing of application data with the applicant's named healthcare provider (for medical lending product purposes)
- Retention of lending decision data
- Data subject rights (access, rectification, erasure, restriction, portability, objection)

Applicants are informed that the lawful bases for processing include contractual necessity (processing necessary for steps prior to entering into a credit agreement), compliance with legal obligations (regulatory reporting, AML/KYC), and legitimate interests (fraud prevention, model improvement). The notice provides the Meridian contact information and the contact information for the relevant supervisory authorities.

**5.8.2 Automated Decision-Making Safeguards (Article 22(3) GDPR)**

Where lending decisions are based solely on automated processing (including profiling) and produce legal effects concerning the data subject or similarly significantly affect them—as is the case with automated credit denials—Meridian shall implement suitable measures to safeguard the data subject's rights, freedoms, and legitimate interests. These measures, implemented through this SOP, include:

1. The right to obtain human intervention on the part of Meridian (exercised through the Secondary Review request process per Section 5.9)
2. The opportunity for the data subject to express their point of view (exercised through the provision of supplementary information during the Secondary Review)
3. The ability to contest the automated decision (exercised through the Challenge Event process per Section 5.9)

Data subjects are informed of these rights at the point of automated decision notification (in the AAN or approval disclosure, as applicable).

**5.8.3 Data Subject Access Request (DSAR) Handling**

All DSARs related to lending decisions shall be logged in the Meridian Privacy Request Tracker (OneTrust) upon receipt through any channel. The DPO shall acknowledge the DSAR within 5 calendar days and coordinate delivery of responsive records within 30 calendar days (extendable to 90 days for complex or voluminous requests, with notification to the data subject of the extension and reasons within the initial 30-day period).

The responsive package shall include a copy of the DRR-01 (redacted for third-party confidential information and trade secrets as permitted under Article 15(4), with redactions logged and justified), relevant credit bureau reference data, and any override justifications. Model inputs and SHAP explanations shall be provided in a readable, non-technical format. The DPO shall consult with Legal (Victoria Sterling-Hale) on any proposed redactions prior to release.

### 5.9 Secondary Review and Challenge Event Procedures

**5.9.1 Secondary Review Request Intake**

Applicants may request a Secondary Review of an adverse credit decision through the following channels:

- HealthPay Applicant Portal (automated workflow; preferred)
- Lending Review telephone line (+1-833-MERIDIAN-US; +44-800-MERIDIAN-UK; +49-800-MERIDIAN-EU)
- Email to lendingreview@meridianhealthpay.com
- Written correspondence to Meridian Health Technologies, Attn: Lending Review Department

All requests shall be logged in the CMS within 4 business hours of receipt.

**Table 5.4: Secondary Review Timelines**

| Jurisdiction | Request Window | Acknowledgment | Review Completion | Final Response |
|---|---|---|---|---|
| United States | 60 calendar days from AAN date | 2 business days from receipt | 15 business days from receipt | 5 business days from review completion |
| United Kingdom | 30 calendar days from AAN date | 2 business days from receipt | 10 business days from receipt | 5 business days from review completion |
| European Union | 30 calendar days from AAN date | 2 business days from receipt | 10 business days from receipt | 5 business days from review completion |

**5.9.2 Secondary Review Procedure**

1. The CMS assigns the Secondary Review to a Senior Underwriter who was NOT the original reviewing analyst.
2. The Senior Underwriter reviews the complete DRR-01, all model inputs and outputs, any override justifications, and any additional information provided by the applicant.
3. The applicant may submit supplementary information (updated income verification, explanation of derogatory credit items, proof of closed accounts, etc.) within the review window.
4. The Senior Underwriter produces a Secondary Review Decision Record (DRR-03), documenting:
   - All additional information considered
   - Re-analysis of the principal denial reasons
   - Final determination: DECISION UPHELD / DECISION MODIFIED / DECISION OVERTURNED
   - Updated terms if decision is modified or overturned
5. If the decision is overturned to an approval, the Senior Underwriter shall complete the override justification DRR-02 with the override reason "Secondary Review."
6. The final determination and a plain-language explanation shall be communicated to the applicant through the same channel(s) as the original AAN.

**5.9.3 Formal Challenge Event Escalation**

If the applicant disputes the Secondary Review outcome, the matter shall be escalated as a Formal Challenge Event:

1. The CMS assigns a Challenge Event case number (CH-YYYY-NNNN).
2. The Director, Credit Operations (or EU/UK Senior Underwriting Manager for EU/UK cases) assumes ownership.
3. A Challenge Review Panel shall be convened, consisting of:
   - Director, Credit Operations (or delegate)
   - Lead Model Risk Analyst (or delegate)
   - Fair Lending Officer (or delegate, mandatory for protected class members)
   - Head of Legal, Financial Services (or delegate)
4. The Panel reviews all prior documentation and may request independent model audit data, external credit report re-pulls, or additional third-party verifications.
5. The Panel's determination shall be issued within 30 calendar days of formal challenge escalation and shall be final, subject only to external regulatory or judicial review.

All Challenge Event documentation shall be retained per Section 4.4 and flagged for heightened retention (indefinite pending litigation hold assessment).

---

## 6. Controls and Safeguards

### 6.1 SR 11-7 Model Risk Management Controls

In alignment with the principles of SR Letter 11-7 ("Supervisory Guidance on Model Risk Management"), Meridian implements the following specific controls throughout the lending decision documentation lifecycle:

**6.1.1 Model Inventory and Version Control (SR 11-7 Section III.B)**

- The Lead Model Risk Analyst maintains the authoritative Model Registry (ServiceNow CMDB module, Meridian custom schema) cataloging every model version, its development lead, validation status, approved use cases, known limitations, and retirement date.
- No lending decision shall reference an unregistered model version. The HealthPay Credit Engine shall perform production-time validation by querying the Model Registry API; invocation with an unregistered version ID shall fail closed (application routed to Manual Underwriting Queue with "Model Version Validation Failure" flag).
- Model version changes shall follow the change management process documented in SOP-RSK-004 (Model Change Management and Validation).

**6.1.2 Model Validation and Ongoing Monitoring (SR 11-7 Section IV)**

- Independent model validation (conducted by Meridian's Internal Model Validation team, functionally separated from the Model Development team reporting to the Lead Model Risk Analyst) shall be completed and documented prior to production deployment of any new model version or material change to an existing model.
- The validation report (MRM-VAL-YYYY-QX) shall assess:
  - Conceptual soundness and developmental evidence
  - Data quality and representativeness
  - Outcomes analysis including back-testing against historical data
  - Sensitivity testing and robustness
  - Fair lending impact assessment (disparate impact testing)
- Ongoing monitoring metrics (see Section 7.1) shall be reviewed monthly against model risk appetite thresholds. A model shall be flagged for re-validation if: (a) any monitoring metric breaches its threshold for two consecutive months; (b) population drift exceeds the pre-defined stability index threshold (PSI >0.25); or (c) a material regulatory change affects the model's operating environment.

**6.1.3 Documentation Standards (SR 11-7 Section V.A)**

The Decision Documentation Package (DRR-01 + DRR-02 if applicable + HOR-01 if applicable) satisfies the SR 11-7 expectation that documentation "should be sufficiently detailed that parties unfamiliar with a model can understand how the model operates, its limitations, and its key assumptions." Specifically, the DRR-01 captures:

- Model purpose and design (Section A)
- Model methodology and component scores (Section B)
- Data used and data quality assessments (model input feature vector, SHAP values)
- Model output interpretation and decision rationale (Section B and C)
- Any deviations from model output with justification (Section C, DRR-02)

### 6.2 EU AI Act High-Risk AI System Controls

**6.2.1 Risk Management System (Article 9)**

Meridian's Model Risk Management Framework (MRMF v3.1), of which this SOP is a component, serves as the risk management system for the HealthPay Credit Engine as a high-risk AI system. The MRMF addresses the four required risk management elements:

1. **Identification of reasonably foreseeable risks** to health, safety, or fundamental rights: Fair lending risk, privacy risk (automated profiling), and consumer protection risk are explicitly identified in the MRMF Risk Register (RSK-LEND-001).
2. **Estimation and evaluation of risks** emerging when the high-risk AI system is used in accordance with its intended purpose and under conditions of reasonably foreseeable misuse: Documented in the annual Enhanced Impact-Driven Assessment (EIDA) conducted by the AI Ethics Officer, with the most recent dated August 14, 2026.
3. **Evaluation of other possibly arising risks** based on analysis of data gathered from the post-market monitoring system (Section 7.2).
4. **Adoption of suitable risk management measures**: The approval workflow controls, Fair Lending Officer veto authority, override monitoring, and human oversight certification procedures constitute the primary risk management measures operationalized through this SOP.

**6.2.2 Technical Documentation (Article 11 and Annex IV)**

Meridian maintains a Technical Documentation package for the HealthPay Credit Engine, referenced as `TECHDOC-CREDIT-ENGINE-v5.2.x`. This package contains the detailed technical description required by Annex IV, including:

- General description of the AI system (Section 1)
- Detailed description of the system elements and development process (Section 2)
- Detailed information about monitoring, functioning, and control (Section 3)
- Description of the performance metrics (Section 4)
- Description of the risk management system (Section 5) — *this SOP constitutes a core element*
- Description of relevant changes to the system through its lifecycle (Section 6)

The Technical Documentation is maintained by the Lead Model Risk Analyst and updated concurrently with any model version change or material SOP revision. It is available to competent authorities upon request within 10 business days.

**6.2.3 Record-Keeping (Article 12 and Article 20)**

For high-risk AI systems, Article 12 requires that the system automatically record events ("logs") over the duration of the system's lifetime. The HealthPay Lending Decision Ledger (QLDB) and LangSmith AI tracing infrastructure jointly satisfy this requirement. All logs are:

- Immutable upon write (WORM compliance through S3 Object Lock)
- Retained for the period required by applicable law (minimum 7 years per Section 4.4.1, with EU-specific retention justification review annually)
- Sufficient to enable the traceability of the system's functioning throughout its lifecycle as required by Article 12(2)

**6.2.4 Transparency and Provision of Information (Article 13)**

This SOP ensures that deployers of the high-risk AI system (Credit Analysts, Senior Underwriters) have the information required in the instructions for use. The Model Registry provides all necessary operating instructions, performance characteristics, and limitations to ensure safe and compliant use.

### 6.3 Technical Access Controls

| Control | Implementation | Review Frequency |
|---|---|---|
| Role-Based Access Control (RBAC) for Lending Decision Systems | Okta SSO integrated with AWS IAM; HealthPay Credit Review Workbench permission sets defined by role (Credit Analyst I/II/Senior vs. Manager vs. Administrator); all privilege escalation requests require Director, Credit Operations approval | Quarterly access review by Information Security |
| Segregation of Duties Enforcement | Automated conflict detection: No user may hold both the "Model Developer" and "Credit Decision Approver" roles; override approval is prohibited for the originating analyst (enforced by CMS workflow) | Real-time enforcement; monthly audit log review |
| Audit Trail Integrity | All lending decision actions logged in QLDB with SHA-256 chaining; log integrity verification performed daily by automated script (CloudWatch Synthetics canary) | Daily automated verification; quarterly manual audit sample |
| Data Encryption | AES-256 encryption at rest (AWS KMS managed keys); TLS 1.3 encryption in transit for all lending decision API endpoints; envelope encryption for offline archival media | Annual cryptographic control review; updated per NIST standards |
| Privileged Access Monitoring | All privileged access to production lending decision systems generates a ServiceNow incident ticket automatically; privileged session recording enabled through CyberArk PSM; quarterly privileged access review by VP, Financial Services and CISO | Quarterly review |

### 6.4 Data Governance Controls

- **Feature Prohibition Verification:** Prior to each model version deployment, the Fair Lending Officer shall execute an automated scanning script (`fair-lend-scan-v2.3.py`) against the model feature list to flag any variable that matches the Prohibited Basis Variable dictionary (curated list of known direct variables, strong proxies, and jurisdiction-specific prohibited variables). Any flagged variable shall be automatically blocked from model ingestion.
- **Input Drift Monitoring:** The Lead Model Risk Analyst shall monitor the Population Stability Index (PSI) between the model development sample and the current applicant population monthly. A PSI exceeding 0.25 for any top-20 feature shall trigger a feature review and potential model recalibration.
- **Minimum Sample Size Rule:** No model component shall be trained, retrained, or recalibrated on a sample of fewer than 5,000 unique, non-synthetic applications. This ensures statistical validity of all model parameters and disparate impact testing.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs) and Service Level Agreements (SLAs)

**Table 7.1: Lending Decision Documentation SLAs**

| Metric | Target | Measurement Frequency | Owner |
|---|---|---|---|
| DRR-01 Completeness Rate (all mandatory fields populated at decision finalization) | ≥99.9% | Continuous (real-time validation) | Director, Credit Operations |
| Adverse Action Notice Delivery Timeliness (US: ≤30 calendar days; UK/EU: ≤14 calendar days) | ≥99.5% for UK/EU; ≥98.0% for US | Weekly sample audit (n=100 per jurisdiction) | Director, Credit Operations |
| Secondary Review Acknowledgment (≤2 business days) | ≥95% within target | Monthly aggregation | Director, Credit Operations |
| Secondary Review Completion (≤10/15 business days per Table 5.4) | ≥90% within target | Monthly aggregation | Director, Credit Operations |
| Model Deviation Documentation Completeness (DRR-02 attached and approved for all deviations) | 100% (zero tolerance) | Continuous (automated enforcement) | Lead Model Risk Analyst |
| DSAR Response Timeliness (acknowledgment ≤5 calendar days; completion ≤30 calendar days) | ≥95% within target | Monthly aggregation | Data Protection Officer |
| Application to Decision Turnaround Time (automated decisions) | Median ≤60 seconds; 99th percentile ≤180 seconds | Continuous (CloudWatch metrics) | VP, Engineering (HealthPay platform) |
| Manual Underwriting Queue Turnaround Time | ≤4 hours for time-sensitive medical products; ≤24 hours for general consumer | Real-time (ServiceNow dashboard) | Director, Credit Operations |

### 7.2 Model Risk Monitoring Metrics

The Lead Model Risk Analyst shall maintain a Model Performance Dashboard (Tableau, data refreshes daily) tracking:

| Metric Group | Specific Metrics | Warning Threshold | Breach Threshold |
|---|---|---|---|
| Model Stability | Population Stability Index (PSI) per feature | PSI >0.15 | PSI >0.25 |
| Model Stability | Characteristic Stability Index (CSI) for composite score | CSI >0.10 | CSI >0.20 |
| Model Discrimination | Gini coefficient / AUC (quarterly) | AUC decline >0.03 | AUC decline >0.05 |
| Model Discrimination | Kolmogorov-Smirnov (KS) statistic | KS decline >10% | KS decline >20% |
| Model Calibration | Hosmer-Lemeshow goodness-of-fit (decile) | p <0.10 | p <0.05 |
| Outcome Performance | Vintage-level default rate vs. expected | Actual/Expected >1.2 | Actual/Expected >1.5 |
| Outcome Performance | Delinquency rate (30+ DPD) at 6 months | >5% | >8% |
| Fair Lending | Marginal effect disparity by protected class (monthly) | >5% relative difference | >10% relative difference with p<0.05 |
| Override Performance | Default rate of overridden (favorable) vs. model-recommended approvals | Overridden default rate >1.3x control | Overridden default rate >1.5x control |

### 7.3 Reporting Cadence

| Report | Audience | Frequency | Delivery Mechanism | Owner |
|---|---|---|---|---|
| Lending Operations Dashboard | Director, Credit Operations; VP, Financial Services | Real-time (daily review required) | Tableau dashboard; automated email summary at 09:00 UTC daily | Director, Credit Operations |
| Model Performance Monitoring Report | Model Risk Steering Group; Lead Model Risk Analyst | Monthly (by 10th business day) | PDF report distributed via ServiceNow GRC | Lead Model Risk Analyst |
| Override Analysis Report | Model Risk Steering Group; Fair Lending Officer | Monthly (by 10th business day) | PDF report with analyst-level detail | Lead Model Risk Analyst |
| Fair Lending Comparative Analysis | Fair Lending Officer; Chief Compliance Officer | Monthly (by 15th business day) | PDF report; disparity flag detail appendix | Fair Lending Officer |
| EU AI Act Article 14 Human Oversight Effectiveness Report | AI Ethics Officer; Model Risk Steering Group; EU/UK Senior Underwriting Manager | Monthly (by 10th business day) | PDF report; includes rubber-stamping analysis per Section 5.3.4.5 | EU/UK Senior Underwriting Manager |
| Quarterly Fair Lending Review Committee Package | Committee members; Board Audit Committee (summary) | Quarterly (two weeks prior to committee meeting) | Compiled PDF; includes override trends, disparity analysis, regulatory change tracker | Fair Lending Officer; VP, Financial Services |
| Annual Model Validation Summary | Board Audit Committee; Model Risk Steering Group | Annual (Q1) | Full validation report MRM-VAL-YYYY-QX | Lead Model Risk Analyst |
| EU AI Act Annual Conformity Assessment | EU Notified Body; AI Ethics Officer | Annual (by anniversary of CE marking, August 2025) | Conformity assessment documentation package | AI Ethics Officer; Head of Legal, Financial Services |

### 7.4 Regulatory Filing Triggers

The following events shall trigger regulatory notification or filing obligations:

| Event | Notification Requirement | Timeline | Responsible Role |
|---|---|---|---|
| Material model failure resulting in >$500,000 unexpected credit losses | Notification to primary federal regulator(s) and UK FCA/PRA where applicable | Within 30 calendar days of identification | Chief Compliance Officer; Head of Legal, Financial Services |
| Data breach affecting EU lending applicants (personal data) | Notification to relevant EU DPA per GDPR Art 33 | Within 72 hours of becoming aware | Data Protection Officer |
| Serious incident under EU AI Act Art 62 (malfunction of high-risk AI system leading to harm) | Notification to national supervisory authority | Without undue delay; no later than 72 hours | AI Ethics Officer; Chief Compliance Officer |
| Identification of potential fair lending violation | Notification to Board Audit Committee; engagement of external counsel for privilege review | Within 5 business days of identification | Fair Lending Officer; Chief Compliance Officer |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types and Handling Matrix

| Exception Type | Examples | Approval Authority | Maximum Validity | Documentation Required |
|---|---|---|---|---|
| Policy Exception | Loan amount exceeds policy maximum; term outside standard range; product offered outside defined scope | Director, Credit Operations | Single transaction only | Exception Request Form (EXC-01) with justification and compensating factor analysis |
| Procedural Exception | DRR-01 completed after decision finalization (system failure scenario); AAN delivered outside SLA (force majeure) | VP, Financial Services | 30 calendar days; requires corrective action plan | Incident Report; Corrective Action Plan submission to compliance |
| Model Exception | Processing through non-production model version (emergency model rollback scenario); use of alternative scoring due to bureau outage | Lead Model Risk Analyst + Director, Credit Operations (joint approval) | Maximum 72 hours; requires emergency model governance documentation within 5 business days | Emergency Model Use Request (EMU-01); retrospective validation review |
| Regulatory Exception | Lending in jurisdiction without finalized lending license (incidental, e.g., temporary relocation of existing customer) | Chief Compliance Officer + Head of Legal, Financial Services (joint approval) | Single transaction only, subject to legal review | Legal Opinion Memorandum; regulatory analysis |

### 8.2 Exception Submission and Review Process

1. Requestor completes the appropriate Exception Request Form (EXC-01, EMU-01, or custom), providing detailed justification, compensating controls, and proposed resolution timeline.
2. The form is routed through ServiceNow GRC workflow to the designated approval authority (Table 8.1).
3. The approval authority reviews within: 4 business hours (urgent, time-sensitive medical lending); 24 hours (standard consumer lending); 5 business days (non-urgent policy review).
4. All approved exceptions shall be logged in the Exceptions Register (ServiceNow GRC module) with unique identifier, tracked to closure, and reported to the Model Risk Steering Group monthly.

### 8.3 System Outage and Business Continuity

In the event of a Credit Engine or HealthPay platform outage exceeding 60 minutes:

1. The Director, Credit Operations shall declare a "Manual Decisioning Event" per the Business Continuity Plan (BCP-FIN-003).
2. All lending decisions during the outage shall be processed manually using the Manual Decisioning Worksheet (MDW-01), which captures all standard DRR-01 fields offline.
3. All manual decisions shall be retroactively entered into the HealthPay platform within 24 hours of system restoration.
4. No automated model shall be invoked during the manual decisioning period. Decisions shall be based on Credit Analyst judgment using available credit bureau data (accessed through backup bureau access channels) and the Manual Underwriting Decision Guide (MDG-01).
5. The Director, Credit Operations shall prepare a Post-Incident Review within 10 business days of resolution, assessing decision quality during the outage period against a matched sample of system-processed decisions from the prior 60-day period.

### 8.4 Model Failure Escalation

The following conditions constitute a potential model failure requiring immediate escalation:

- Approval rate change exceeding 30% week-over-week (measured Friday vs. prior Friday)
- Default rate on recent vintages exceeding the model's expected default rate by >50% (vintage 3-month observation window)
- Two consecutive months of PSI breach (>0.25) on any core model feature
- Unusual concentration of approvals or denials in a single protected class dimension detected by automated daily monitoring

Upon triggering, the Lead Model Risk Analyst shall:

1. Immediately (within 2 hours) notify the Director, Credit Operations, VP, Financial Services, and Chief Compliance Officer.
2. Within 24 hours, conduct a preliminary root cause analysis.
3. Determine whether model suspension is required. If the failure presents fair lending risk or material financial risk, the model shall be suspended (production routing shifted to previous validated model version or manual underwriting exclusively) pending full investigation.
4. Within 15 business days, deliver a Model Incident Report (MRM-INC-YYYY-NNN) to the Model Risk Steering Group detailing findings, corrective actions, and timeline for resolution.

### 8.5 Fair Lending Disparity Flag Investigation

Upon identification of a Fair Lending Disparity Flag (statistical disparity exceeding threshold per Section 5.7.1):

1. The Fair Lending Officer shall open a privileged and confidential investigation case (FL-INV-YYYY-NNN) within 5 business days.
2. The investigation shall include, where appropriate, matched-pair statistical analysis, file review of a stratified sample of affected applications, model variable contribution analysis for the disparity dimension, and review of override activity affecting the relevant population.
3. The Fair Lending Officer shall engage external counsel prior to preparing any written analysis or report, to preserve attorney-client privilege where applicable.
4. Preliminary findings shall be presented to the Chief Compliance Officer within 30 calendar days of flag identification.
5. If the investigation confirms a likely fair lending violation (disparate treatment or disparate impact without a legitimate, non-discriminatory business justification), the Chief Compliance Officer shall notify the Board Audit Committee and initiate external regulatory engagement within 15 calendar days.

---

## 9. Training Requirements

### 9.1 Required Training Modules

All personnel with roles defined in Section 3 shall complete the following training:

| Training Module | Description | Audience | Frequency | Delivery Method | Tracking System |
|---|---|---|---|---|---|
| LND-TRN-001: Lending Decision Documentation | Comprehensive training on SOP-FIN-006 procedures, DRR-01/DRR-02/DRR-03 completion, AAN issuance, and CMS workflows | All Credit Analysts, Senior Underwriters, Underwriting Managers | Initial (prior to system access grant); refresher annually | Instructor-led virtual (2 days) + knowledge assessment (passing score ≥85%) | Workday Learning; completion certificate required for system access |
| LND-TRN-002: Fair Lending and Non-Discrimination | ECOA/Regulation B requirements, fair lending principles, recognizing disparate treatment and disparate impact, protected class identification, fair lending proxy awareness | All personnel listed in Section 3; Fair Lending Officer (enhanced module) | Initial; annual refresher | Self-paced e-learning (4 hours) + scenario-based assessment (6 case studies, all must be correctly analyzed) | Workday Learning |
| LND-TRN-003: SR 11-7 Model Risk Management Awareness | Overview of model risk management principles, model developer vs. model user responsibilities, override documentation requirements, model limitation awareness | All Credit Analysts II+, Senior Underwriters, Underwriting Managers, Model Developers | Initial; biennial refresher | Instructor-led virtual (1 day) + knowledge assessment (passing score ≥80%) | Workday Learning |
| LND-TRN-004-EU: EU AI Act Human Oversight (Mandatory for EU/UK personnel) | Article 14 human oversight requirements, meaningful human review standards, rubber-stamping avoidance, Human Oversight Record completion, Article 14(4) reporting awareness | All EU/UK-based Credit Analysts, Senior Underwriters, Underwriting Managers; AI Ethics Officer (trainer qualification) | Initial prior to EU/UK decision authority; annual refresher | Instructor-led (1 day) with practical simulation: analysts review 10 mock applications with varying levels of model recommendation quality and must demonstrate meaningful interaction | Workday Learning; regulatory audit evidence retained |
| LND-TRN-005: GDPR and Data Subject Rights (EU/UK) | GDPR principles, Article 22 automated decision-making rights, DSAR handling procedures, secondary review as Article 22(3) safeguard | All personnel handling EU/UK lending decisions; DPO (specialized module) | Initial; annual refresher | Self-paced (3 hours) + case study assessment | Workday Learning |

### 9.2 Training Compliance Monitoring

- The Director, Credit Operations shall receive a monthly Training Compliance Report from Workday Learning, showing completion status for all assigned personnel.
- Any personnel with expired or incomplete mandatory training shall be automatically restricted from system access (CMS workflow permission suspended until training completion is confirmed).
- Training effectiveness shall be assessed through: (a) pre- and post-training knowledge assessments; (b) correlation of training completion with override quality metrics and DRR-01 completeness rates; and (c) annual survey of trained personnel on confidence in applying SOP procedures.
- Training materials shall be reviewed and updated within 30 calendar days of any material SOP revision.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies and SOPs

| Document ID | Title | Relationship |
|---|---|---|
| SOP-FIN-004 | Payment Processing Float Management | Related underwriting for vendor financing products |
| SOP-FIN-008 | Claims Advance Factoring Documentation | Excluded product from this SOP; separate documentation regime |
| SOP-RSK-004 | Model Change Management and Validation | Governs model version change process referenced in Section 5.2.1 |
| SOP-RSK-011 | Fair Lending Proxy Methodology | Governs the proxy methodology used for protected class identification referenced in Section 5.6.3 |
| SOP-CMP-002 | Regulatory Examination Management | Governs interaction with regulatory examiners requesting lending decision documentation |
| SOP-PRV-003 | Data Subject Access Request Handling | Governs all DSAR intake, tracking, and fulfillment; referenced in Section 5.8.3 |
| SOP-INC-001 | Information Security Incident Response | Governs response to data breaches referenced in Section 7.4 |
| BCP-FIN-003 | Financial Services Business Continuity Plan | Referenced in Section 8.3 for outage procedures |
| POL-AI-001 | AI Ethics and Governance Charter | Board-approved charter establishing AI governance framework |
| POL-FL-001 | Fair Lending Policy | Overarching fair lending commitments and governance structure |

### 10.2 External Regulatory References

| Regulation/Standard | Citation | Applicability |
|---|---|---|
| SR Letter 11-7 | "Supervisory Guidance on Model Risk Management" (Federal Reserve, OCC, FDIC, NCUA, FHFA, 2011) | US model risk management standards |
| Equal Credit Opportunity Act (ECOA) | 15 U.S.C. §1691 et seq. | US anti-discrimination in credit |
| Regulation B | 12 CFR Part 1002 | US adverse action, fair lending, appraisal rules |
| Fair Credit Reporting Act (FCRA) | 15 U.S.C. §1681 et seq. | US credit reporting and adverse action based on consumer reports |
| General Data Protection Regulation (GDPR) | Regulation (EU) 2016/679; particularly Articles 12-15, 22, 35 | EU/UK automated decision-making, transparency, DSARs |
| EU AI Act | Regulation (EU) 2024/1689; particularly Title III, Chapters 2-4, Annex III para 5(b) | EU high-risk AI system classification for creditworthiness assessment |
| Consumer Credit Directive | Directive 2008/48/EC (repealed and replaced by Directive (EU) 2023/2225, effective November 2026) | EU consumer credit information and rights |
| UK Data Protection Act 2018 | 2018 c. 12 | UK GDPR implementation |
| FCA Consumer Credit Sourcebook (CONC) | CONC 5.2 (pre-contractual explanations and creditworthiness) | UK consumer credit regulatory standards |
| UK AI Regulation | Currently under development; interim guidance from ICO and FCA applied | UK AI governance expectations |

---

## 11. Revision History

| Version | Date | Author(s) | Description of Changes | Approval |
|---|---|---|---|---|
| 1.0 | 2021-03-15 | Marcus Chen (former Director, Credit Operations) | Initial SOP creation; established basic lending documentation framework for US consumer lending | Robert Liu, VP Financial Services |
| 2.0 | 2022-11-08 | Sarah Chen-Patel; Javier Rodriguez-Garcia | Major revision: incorporated SR 11-7 model risk management documentation standards; added model deviation and override procedures; introduced DRR-01 standardized template | Robert Liu, VP Financial Services; James Thornton, CFO |
| 3.0 | 2023-08-01 | Sarah Chen-Patel; Dr. Amina Bakari-Thomas | Added comprehensive fair lending controls; established Fair Lending Officer role and veto authority; introduced Fair Lending Review Committee governance | James Thornton,
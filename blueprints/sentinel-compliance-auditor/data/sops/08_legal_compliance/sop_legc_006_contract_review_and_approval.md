---
sop_id: "SOP-LEGC-006"
title: "Contract Review and Approval"
business_unit: "Legal & Compliance"
version: "3.7"
effective_date: "2025-11-07"
last_reviewed: "2026-05-08"
next_review: "2026-11-13"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
  - "HIPAA"
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Contract Review and Approval

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the standardized framework for the intake, triage, review, negotiation, risk assessment, approval, execution, and archival of all contractual agreements entered into by Meridian Health Technologies, Inc. and its global subsidiaries. The purpose of this document is to ensure that all contracts are subjected to a consistent, risk-based review process that protects Meridian's commercial, clinical, intellectual property, and operational interests while ensuring operational efficiency across all business lines.

This SOP operationalizes Meridian's commitment to structured legal review and financial controls. It defines the thresholds at which contracts must be escalated, the standardized clause library that governs acceptable risk, and the approval authority matrix that binds the organization.

### 1.2 Scope

This SOP applies to all employees, contractors, officers, and authorized agents of Meridian Health Technologies, Inc. who are involved in the origination, drafting, negotiation, approval, or signature of any legally binding agreement on behalf of the company.

**In-Scope Agreements:**
- Customer agreements for the Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and Meridian SaaS Platform
- Business Associate Agreements (BAAs)
- Data Processing Agreements (DPAs), Standard Contractual Clauses (SCCs), and international data transfer agreements
- Master Services Agreements (MSAs), Statements of Work (SOWs), and Order Forms
- Vendor, supplier, and procurement agreements exceeding $50,000 in annual value
- Licensing agreements, software-as-a-service (SaaS) subscription agreements
- Clinical collaboration and research agreements with hospitals and academic medical centers
- Non-Disclosure Agreements (NDAs), Memoranda of Understanding (MOUs), and Letters of Intent (LOIs)
- Settlement agreements, release agreements, and litigation-related contracts
- Employment, consulting, and independent contractor agreements
- Real property leases and capital equipment financing agreements
- Any agreement containing indemnification, limitation of liability, intellectual property assignment, or exclusivity clauses regardless of dollar value

**Out-of-Scope:**
- Purchase Orders issued under an existing, fully-executed MSA that has been reviewed under this SOP
- Routine office supply purchases under $10,000 processed via the Procurement Card program
- Internal memoranda and intra-company SLAs

### 1.3 Geographic Applicability

This SOP applies globally to all Meridian offices, including the headquarters in San Francisco, CA, and subsidiaries in London, UK; Dublin, IE; and Singapore, SG. Regional counsel in each jurisdiction are responsible for ensuring local law compliance within the framework established herein.

---

## 2. Definitions and Acronyms

| Term | Definition |
|---|---|
| **Agreement** | Any written or electronic document that creates a legally binding obligation upon Meridian upon execution. |
| **Approval Authority Matrix (AAM)** | The structured table defining the dollar thresholds and risk categories that determine who may approve and sign a contract. |
| **CLM** | Contract Lifecycle Management system (currently Conga CLM integrated with Salesforce). The system of record for all contracts from intake through archival. |
| **Clause Library** | A curated, pre-approved collection of standard, fallback, and alternative clauses maintained by Legal & Compliance. |
| **Commercially Reasonable Efforts (CRE)** | The standard of effort that Meridian is obligated to apply, as interpreted by the General Counsel's office. |
| **Contract Owner** | The business stakeholder responsible for initiating the contract request and managing the commercial relationship throughout the contract lifecycle. |
| **DPA** | Data Processing Agreement, governing the processing of any data on behalf of a controller. |
| **Fallback Clause** | A clause that is acceptable to Meridian but represents a concession from the preferred position; typically used in Tier 2 negotiations. |
| **Material Change** | Any modification to a fully-executed agreement that alters scope, fees, term, service levels, liability caps, data usage, or indemnity obligations. |
| **NDA** | Non-Disclosure Agreement, governing the exchange of confidential information. |
| **Preferred Clause** | The Meridian-standard clause position that represents the company's ideal commercial and legal posture. |
| **Risk Tier** | Classification of an agreement as Low, Moderate, High, or Critical risk based on the Risk Assessment Matrix (Section 5.4). |
| **SCC** | Standard Contractual Clauses, as adopted by the European Commission for international data transfers. |
| **SOW** | Statement of Work, describing specific services, deliverables, milestones, and fees under a governing MSA. |
| **Triager** | The Legal Operations Specialist or paralegal responsible for initial contract intake and routing. |
| **Unacceptable Clause** | A clause position that Meridian cannot accept under any circumstances; defined in the Clause Library as "Hard Stop." |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix

The following matrix assigns responsibility for each phase of the contract lifecycle. The legend is as follows:

- **R** = Responsible (performs the task)
- **A** = Accountable (approves and owns outcome)
- **C** = Consulted (provides input)
- **I** = Informed (receives status updates)

| Activity | Contract Owner | Legal Operations | Commercial Counsel | Privacy Counsel | InfoSec | Finance | Regional Counsel | Sales VP | CPO / CTO | CEO |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Contract Intake & Request | R/A | C | I | I | I | I | I | C | I | I |
| Triage & Routing | C | R/A | C | C | I | I | I | I | I | I |
| Legal Review (Tier 1-2) | C | I | R/A | C | I | I | I | I | I | I |
| Legal Review (Tier 3-4) | C | I | R | C | C | C | R | C | C | C |
| Clause Library Deviation Check | I | I | R | R | I | I | R | I | I | I |
| Risk Assessment Scoring | C | C | R/A | R | R | C | R | I | C | I |
| Commercial Terms Review | R | I | I | I | I | R/A | I | C | I | I |
| InfoSec Appendix Review | I | I | I | I | R/A | I | I | I | R | I |
| Pricing Approval (≤$250K) | R | I | I | I | I | C | I | R/A | I | I |
| Pricing Approval (>$250K) | C | I | I | I | I | C | I | C | R/A | I |
| Final Signature (≤$1M / Low-Mod Risk) | I | I | I | I | I | I | I | R/A | I | I |
| Final Signature (>$1M or High/Critical Risk) | I | I | I | I | I | I | I | I | R/A | R/A |

### 3.2 Detailed Role Definitions

**Contract Owner:** The individual within the business unit who initiates the contract request. The Contract Owner is typically a Director or above in Sales, Business Development, Product Management, or Procurement. Responsibilities include completing the Contract Intake Form (CIF-001), securing budget approval prior to Legal submission, managing the commercial negotiation timeline, and ensuring the executed contract is properly operationalized within their team.

**Legal Operations Specialist (Triager):** Reports to the Legal Operations Manager. Responsible for all contract intake review, completeness checks, initial risk tier classification, routing to the appropriate reviewing counsel, and tracking contract cycle times. The Triager is the first point of contact for all contract status inquiries.

**Commercial Counsel:** An attorney within the Legal & Compliance department responsible for reviewing and negotiating non-standard contractual terms, redlining, and providing legal risk guidance. Commercial Counsel are assigned by geography and business line. The Commercial Counsel assigned to Clinical AI Platform has specialized knowledge of FDA and MDR implications for commercial agreements.

**Privacy Counsel:** A designated attorney within Legal & Compliance with subject matter expertise on global privacy laws. Privacy Counsel must be consulted on any agreement involving cross-border data transfers, sensitive data processing, or novel uses of patient or provider data.

**Information Security Officer (InfoSec):** Responsible for reviewing and approving all information security schedules, exhibits, and appendices incorporated into Meridian agreements. InfoSec maintains the standard security exhibit (Exhibit-SEC-2025-01) and evaluates any customer-requested modifications.

**Finance Reviewer:** A member of the FP&A or Revenue Operations team responsible for validating pricing, payment terms, revenue recognition implications, and budget availability prior to final approval.

**Regional Counsel:** An attorney located in Meridian's London, Dublin, or Singapore offices responsible for ensuring that agreements governed by non-US law comply with applicable local legal requirements.

**Sales Vice President:** The VP-level leader accountable for the commercial relationship, responsible for approving non-standard pricing concessions and signing standard agreements below the defined threshold.

**Chief Product Officer / Chief Technology Officer:** Responsible for approving any agreement that commits Meridian to product roadmap deliveries, custom development obligations, or technical integration commitments that deviate from the standard product offering.

**Chief Executive Officer:** The ultimate approval authority for all contracts exceeding $1,000,000 in Total Contract Value (TCV) or classified as Critical Risk.

---

## 4. Policy Statements

### 4.1 General Contracting Principles

**4.1.1 Written Agreement Requirement:** No binding obligation shall be created on behalf of Meridian Health Technologies, Inc. without a written, fully-executed agreement that has been reviewed and approved in accordance with this SOP. Oral agreements, "handshake deals," and email exchanges purporting to bind the company are void and unenforceable.

**4.1.2 Signature Authority:** Only individuals who are expressly listed in the Approval Authority Matrix (Section 5.5, Table 5) and who have completed the Signature Authority Delegation training (TRN-LEGC-006-01) may execute agreements on behalf of Meridian. Signature authority is role-based and may not be re-delegated without General Counsel approval.

**4.1.3 Use of Standard Templates:** For all recurring agreement types, Meridian standard templates maintained in the CLM shall be used as the starting point for negotiation. Deviations from standard templates must be documented and justified through the risk assessment process.

**4.1.4 Clause Library Adherence:** All contractual language must conform to the Clause Library maintained by Legal & Compliance. Use of non-standard clauses requires a Clause Deviation Request (CDR-001) and approval per Section 8.

**4.1.5 No-Self-Review:** No individual may serve as the sole legal reviewer for a contract where they are also the primary commercial negotiator. Where a conflict arises, an alternate reviewer shall be assigned by the General Counsel.

**4.1.6 Contracting Without Legal Review — Zero Tolerance:** Any employee who enters into a contract, MOU, letter of intent, or any other legally binding instrument without completing the review workflow defined in this SOP shall be subject to disciplinary action up to and including termination. Meridian does not recognize the concept of "implied" legal review; affirmative documented approval in the CLM is required.

### 4.2 Data Protection and Privacy Commitments

**4.2.1 Privacy by Contract:** All agreements involving the processing of personal data must incorporate Meridian's standard data processing terms. The Privacy Counsel must pre-approve any contractual language relating to data subject rights, cross-border data transfers, or data breach notification timelines.

**4.2.2 Regulated Data:** Agreements involving patient health data, clinical trial data, or data subject to regulated industry frameworks must include specific data handling provisions approved by Privacy Counsel and the Chief Medical Information Officer.

### 4.3 Information Security Commitments

**4.3.1 Standard Security Exhibit:** All customer agreements for Meridian software products shall include the current Meridian Standard Security Exhibit as an attachment. This exhibit describes Meridian's administrative, technical, and physical safeguards. Any modification to this exhibit requires InfoSec and Legal approval.

**4.3.2 Customer Security Audits:** Provisions granting customers the right to conduct on-site security audits of Meridian facilities are generally unacceptable. Remote audits based on Meridian's SOC 2 report or other third-party attestations may be negotiated on a case-by-case basis with InfoSec and General Counsel approval.

### 4.4 Revenue Recognition

All contracts involving recurring subscription revenue, milestone-based payments, or non-standard payment terms must be reviewed by the Finance Reviewer to ensure compliance with ASC 606 revenue recognition standards before final signature.

---

## 5. Detailed Procedures

### 5.1 Contract Intake and Initiation

**Step 1: Determine Contract Type and Need**
The Contract Owner determines that a new contractual relationship or a material change to an existing contract is required. The Contract Owner identifies the appropriate Meridian standard template (if applicable) from the CLM Template Library or identifies that a third-party paper is being used.

**Step 2: Complete the Contract Intake Form (CIF-001)**
The Contract Owner shall complete and submit the Contract Intake Form (CIF-001) available within the CLM at `https://clm.meridian.com/intake`. The CIF-001 requires the following information:

| Field | Required? | Description |
|---|---|---|
| Contract Owner Name & Dept | Yes | Individual accountable for the business relationship |
| Counterparty Legal Name | Yes | Full legal entity name, not trade name |
| Counterparty Entity Type | Yes | Dropdown: Hospital/IDN, Ambulatory Provider, Payer, Life Sciences, Vendor/Supplier, Academic, Other |
| Agreement Type | Yes | Dropdown: MSA, SOW, Order Form, Amendment, NDA, BAA, DPA, Vendor Agreement, Employment, Other |
| Total Contract Value (TCV) | Yes | Numeric value in USD; include all fees over the full term |
| Contract Term (months) | Yes | Initial term including any auto-renewal |
| Governing Law Jurisdiction | Yes | Dropdown reflecting likely choice of law |
| Third-Party Paper? | Yes | Boolean: Is Meridian responding to a third-party's template? |
| Data Involved? | Yes | Boolean: Does the contract involve access to, processing of, or storage of data? |
| Data Classification | Conditional | If data involved: Public, Internal, Confidential, or Regulated (PHI, PCI, PII) |
| Regulatory Trigger? | Conditional | Dropdown: None / FDA-QSR / EU-MDR / PCI-DSS / Other (specify) |
| Budget Approved? | Yes | Boolean: Has the expenditure or pricing been approved by Finance? |
| Target Execution Date | Yes | Calendar date |
| Urgency Justification | Conditional | Required if target execution date is <10 business days from intake |
| Special Instructions | Optional | Free text for any context the Contract Owner wishes to communicate |

**Step 3: Attach the Contract Document**
The Contract Owner attaches the proposed contract document (Word format required for redlining; PDF acceptable for counterparty-originated documents that will be converted). If no document exists yet, the Contract Owner may request template generation by the Triager.

**Step 4: Submit**
Upon submission, the CLM assigns a unique Contract ID in the format `CON-YYYY-NNNNNN` and sends an automated confirmation email to the Contract Owner.

### 5.2 Initial Triage and Routing

Upon submission, the Legal Operations Triager has one (1) business day to perform initial triage.

**Triage Activities:**
1. Verify that all required fields on CIF-001 are complete. If incomplete, the Triager returns the request to the Contract Owner with a notation of missing fields. The one-day triage SLA resets upon resubmission.
2. Perform a conflict check using the CLM's party search and the Intapp conflict management integration. If a potential conflict is flagged, the Triager escalates to the General Counsel's office before proceeding.
3. Assign an initial Risk Tier (see Section 5.4 for methodology) based on CIF-001 data.
4. Route the contract to the appropriate reviewing queue based on:

| Business Line | Primary Review Queue |
|---|---|
| Clinical AI Platform | Clinical & Regulatory Contracts |
| HealthPay (Financial Services) | Commercial Contracts — FinTech |
| MedInsight Analytics | Commercial Contracts — Data & Analytics |
| SaaS Platform (Horizon Suite) | Commercial Contracts — Technology |
| Vendor / Procurement | Procurement & Vendor Contracts |
| Corporate (HR, Facilities, Marketing) | Corporate & Operations Contracts |

5. Assign a Primary Reviewer (Commercial Counsel) and, if required by the Risk Tier, flag for Privacy Counsel and InfoSec review.

If the Triager cannot determine routing within the one-day SLA, the contract is escalated to the Legal Operations Manager for resolution within an additional four (4) business hours.

### 5.3 Contract Review and Redlining Process

#### 5.3.1 First-Pass Review (Meridian Template)

When Meridian's standard template is the starting document:

1. **Commercial Counsel Review (3 Business Days):** The assigned Commercial Counsel reviews the completed template for accuracy of populated fields, ensures all schedules and exhibits are attached, confirms clause selections are appropriate for the Risk Tier, and prepares the document for counterparty delivery. If non-standard clauses are required, the Commercial Counsel initiates a Clause Deviation Request.

2. **Cross-Functional Review (Concurrent, 2 Business Days):** If flagged for InfoSec or Privacy review, the Commercial Counsel sends the draft to those reviewers concurrently with their own review. InfoSec and Privacy reviewers have two (2) business days each to approve, reject, or request modifications to their respective sections.

3. **Finalization:** The Commercial Counsel consolidates any feedback, finalizes the document, and releases it to the Contract Owner for delivery to the counterparty.

#### 5.3.2 Third-Party Paper Review (Counterparty Template)

When responding to a counterparty's paper:

1. **Document Prep by Triager (0.5 Business Days):** The Triager converts the counterparty document to a Meridian-standard redlining format, runs an automated clause comparison against the Clause Library using the CLM's AI-assisted markup tool, and attaches the Clause Library comparison report.

2. **Commercial Counsel Review and Redline (5 Business Days):** The assigned Commercial Counsel performs a full review of the counterparty paper, redlines all clauses to align with Meridian's Clause Library positions, and prepares a Meridian counter-draft. The review must address, at minimum:
   - Indemnification scope and caps
   - Limitation of liability (exclusions and aggregate cap)
   - Warranty scope and disclaimers
   - Intellectual property ownership and license grants
   - Service level commitments and remedies
   - Data usage, security, and confidentiality
   - Term, termination, and transition assistance
   - Governing law, venue, and dispute resolution

3. **Redline Memorandum:** For contracts with TCV exceeding $500,000 or classified as High Risk, the Commercial Counsel shall prepare an internal Redline Memorandum summarizing key deviations from Meridian's preferred positions, the rationale for acceptance or escalation, and any open negotiation items requiring approval.

4. **Escalation Triggers During Review:** The Commercial Counsel must escalate to the General Counsel any counterparty position that:
   - Seeks uncapped liability for Meridian
   - Demands Meridian indemnify the counterparty for Meridian's own negligence in a manner that vitiates Meridian's insurance coverage
   - Requires Meridian to assign or exclusively license core intellectual property
   - Imposes service level credits exceeding 100% of monthly fees
   - Requests a Most Favored Nation (MFN) pricing clause
   - Seeks audit rights broader than standard
   - Insists on a governing law or venue outside of: California (US contracts), England & Wales (EMEA contracts), or Singapore (APAC contracts)

#### 5.3.3 Negotiation and Turnaround

1. **Contract Owner Manages Commercial Negotiation:** The Contract Owner serves as the primary point of contact with the counterparty for all commercial and scheduling discussions. Legal & Compliance does not communicate directly with the counterparty unless specifically requested by the Contract Owner for legal issue resolution.

2. **Subsequent Review Turns:** Each subsequent redline review by Commercial Counsel shall be completed within two (2) business days of resubmission. If a contract exceeds five (5) redline turns without resolution, the Commercial Counsel shall schedule a negotiation strategy call with the Contract Owner and the Sales VP to identify open issues and a path to closure.

3. **Redline Purgatory Prevention:** Any contract that remains in "Redline In Progress" status in the CLM for more than thirty (30) calendar days without documented counterparty activity shall be flagged by the CLM system. The Triager will notify the Contract Owner and the reviewing Commercial Counsel. If status remains unchanged at forty-five (45) days, the contract is automatically moved to "Stalled" and the General Counsel is notified.

### 5.4 Risk Assessment

All contracts shall be assigned a Risk Tier using the following Risk Assessment Matrix. The overall Risk Tier is determined by the highest score across any single dimension.

**Scoring Dimensions:**

| Dimension | Weight | Low (1) | Moderate (2) | High (3) | Critical (4) |
|---|---|---|---|---|---|
| Total Contract Value (TCV) | 25% | <$50K | $50K–$500K | $500K–$1M | >$1M |
| Data Classification | 30% | Public Data Only | Internal/Confidential | PII (non-health) | PHI / Regulated Health Data |
| Indemnification Scope | 15% | Standard mutual | One-way in our favor | One-way in their favor | Uncapped or third-party indemnity |
| Limitation of Liability Deviation | 10% | Standard caps | 1.5x fees | 2-3x fees | Uncapped or >3x fees |
| Term (including auto-renewal) | 10% | ≤12 months | 13–36 months | 37–60 months | >60 months |
| Exclusive or MFN Commitments | 5% | None | Exclusivity for <1yr | Exclusivity >1yr / MFN | Both |
| Custom Development Obligations | 5% | None | Minor configuration | Custom module | Full custom development with IP risk |

**Composite Risk Score Calculation:**

A weighted composite score is calculated automatically by the CLM. The Risk Tier is assigned as follows:

| Composite Score Range | Risk Tier | Required Approvals |
|---|---|---|
| 1.00 – 1.49 | Tier 1 (Low) | Commercial Counsel + Contract Owner |
| 1.50 – 2.49 | Tier 2 (Moderate) | Commercial Counsel + Contract Owner + Sales VP or relevant VP |
| 2.50 – 3.49 | Tier 3 (High) | Commercial Counsel + Privacy Counsel + InfoSec + CPO/CTO (if custom dev) + Finance |
| 3.50 – 4.00 | Tier 4 (Critical) | All Tier 3 approvers + General Counsel + CEO |

### 5.5 Approval Authority Matrix

Approval and signature authority is defined by the combination of Risk Tier and Total Contract Value (TCV). An individual may not approve a contract in which they have a personal financial interest.

**Table 5-1: Approval and Signature Authority**

| Risk Tier | TCV Range | Commercial Approver | Legal Approver | Signature Authority |
|---|---|---|---|---|
| Tier 1 | <$50K | Contract Owner | Commercial Counsel | Director or above in requesting BU |
| Tier 1 | $50K–$250K | Contract Owner | Commercial Counsel | Vice President, requesting BU |
| Tier 2 | <$250K | Sales VP / BU VP | Commercial Counsel | Vice President, Sales or BU |
| Tier 2 | $250K–$500K | Sales VP / BU VP + Finance | Senior Commercial Counsel | SVP, Commercial Operations |
| Tier 3 | <$1M | BU General Manager + Finance | General Counsel or designee | Chief Revenue Officer or CPO |
| Tier 3 | ≥$1M | CRO/CPO + CFO | General Counsel | CEO |
| Tier 4 | Any | CEO + CFO | General Counsel | CEO |

Approvals shall be recorded sequentially in the CLM. No contract may proceed to signature until all required approval steps display a "green" status in the CLM approval workflow.

### 5.6 Contract Execution

**5.6.1 Signature Process**

1. Upon completion of all approvals, the CLM automatically generates the final execution copy of the agreement in PDF format, applying the Meridian-standard signature block format.
2. The CLM routes the execution copy to the designated Signatory (as determined in Table 5-1) via DocuSign integration.
3. Meridian policy is that Meridian signs last. The Contract Owner is responsible for managing the counterparty signature process first. Exceptions require justification and approval from the Commercial Counsel.
4. Electronic signatures executed via the DocuSign platform are the preferred and default method. Wet-ink signatures are permitted only when required by the counterparty or applicable law. Where wet-ink signatures are used, the original signed document must be scanned and uploaded to the CLM within two (2) business days of receipt.
5. The Commercial Counsel or Triager performs a final review of the counterparty-signed version to confirm no unauthorized changes were made before Meridian executes.

**5.6.2 Post-Execution Archival**

Upon full execution (both parties signed), the CLM automatically:
1. Applies the "Executed" status tag.
2. Logs the execution date, triggering any obligation tracking dates (renewal notices, termination windows, price increase notifications).
3. Stores the fully-executed PDF as the authoritative record.
4. Sends execution notification to the Contract Owner, the Commercial Counsel, and Finance for revenue recognition setup.

### 5.7 Contract Obligation Management and Renewals

**5.7.1 Obligation Tracking**

Within ten (10) business days of execution, the Contract Owner shall extract all material operational obligations from the agreement and enter them into the CLM's Obligations module. Material obligations include:
- Delivery milestones and acceptance criteria
- Reporting obligations (e.g., SOC 2 report distribution, uptime reports)
- Renewal notice deadlines (flagged with an alert 90, 60, and 30 days prior)
- Price increase notification deadlines
- Termination for convenience windows

Failure to populate obligations does not excuse Meridian's performance of those obligations.

**5.7.2 Renewal Process**

The CLM automatically flags contracts approaching their renewal decision window (typically 90 days prior to termination notice deadline). The Triager sends a Renewal Notification to the Contract Owner with a copy to Finance. The Contract Owner shall make a renewal decision (renew, renegotiate, terminate, or allow to expire) and document the decision in the CLM at least thirty (30) days prior to any auto-renewal date or notice deadline.

---

## 6. Controls and Safeguards

### 6.1 Access Controls and Segregation of Duties

**6.1.1 CLM Role-Based Access Control (RBAC):** Access to the CLM is governed by role. The following roles are defined:

| Role | Permissions |
|---|---|
| Contract Requester | Create intake requests; view status of own requests |
| Contract Owner | Create intake; view/edit own contracts pre-execution; view all executed contracts for their BU; initiate amendments |
| Legal Operations (Triager) | View all contracts; edit metadata; assign reviewers; run reports |
| Commercial Counsel | Full edit on assigned contracts; approve legal terms; view all contracts within their assigned BU |
| Privacy Counsel | View/edit all contracts where data classification is PII/PHI; approve data processing terms |
| InfoSec Reviewer | View/edit InfoSec schedules; approve security terms |
| Finance Reviewer | View financial terms; approve pricing and payment terms; run TCV reports |
| Legal Approver (Senior) | Final legal approval for Tier 3-4; manage Clause Library |
| Executive Signatory | Execute contracts within delegated authority; view all executed contracts |
| System Administrator | Technical configuration; user provisioning; audit log access |

**6.1.2 Segregation of Duties Enforcement:** The CLM workflow engine enforces segregation of duties. The same individual cannot serve as both the requesting Contract Owner and the Legal Approver for the same contract. The CLM prevents a user from approving a workflow step if they initiated the request.

### 6.2 Clause Library Governance

**6.2.1 Clause Library Structure:** The Meridian Clause Library, maintained in the CLM, categorizes all clauses as:

- **Preferred (Green):** Meridian's standard, proponent position. Use without additional approval.
- **Fallback (Yellow):** Acceptable negotiated compromise. Use is permitted; any concession beyond Fallback requires escalation.
- **Escalation Required (Orange):** May only be accepted with documented approval from the General Counsel or designee.
- **Hard Stop (Red):** Meridian will not accept. No exceptions are permitted. Examples include uncapped indemnity for counterparty's breach, assignment of Meridian's background IP, and non-mutual termination for convenience in favor of the counterparty only.

**6.2.2 Clause Library Updates:** The Clause Library is reviewed quarterly (January, April, July, October) by the Commercial Contracts team under the General Counsel's direction. Proposed additions or changes must be justified by a business case and approved by the General Counsel.

### 6.3 Segregation of Meridian Entities

All contracts must be executed in the name of the correct legal entity. The following rules apply:

| Geography / Product | Contracting Entity |
|---|---|
| US — Clinical AI Platform | Meridian Health Technologies, Inc. (Clinical AI Division) |
| US — HealthPay | Meridian HealthPay, LLC |
| US — MedInsight / SaaS | Meridian Health Technologies, Inc. |
| UK / EMEA | Meridian Health Technologies UK Ltd. |
| Ireland — EU Data Processing | Meridian Health Technologies Ireland Ltd. |
| Singapore / APAC | Meridian Health Technologies Singapore Pte. Ltd. |

No contract may be executed by an entity that does not have operational nexus to the jurisdiction and product line.

### 6.4 Attorney-Client Privilege Preservation

All legal review communications, redline memoranda, risk assessments, and clause deviation justifications stored in the CLM are designated as "Attorney-Client Privileged — Legal Department Confidential." Access to these records is restricted to Legal & Compliance personnel. Under no circumstances shall negotiation memoranda, internal risk scores, or fallback position analyses be shared with any external party without the express, documented permission of the General Counsel.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The Legal Operations team shall track and report the following KPIs on a monthly basis:

| KPI | Target | Calculation |
|---|---|---|
| Intake-to-Triage Cycle Time | ≤1 Business Day | Average elapsed time from CIF-001 submission to Triager assignment |
| First-Pass Review Cycle Time (Standard) | ≤3 Business Days | Average elapsed time from assignment to first-pass complete |
| First-Pass Review Cycle Time (Third-Party Paper) | ≤5 Business Days | Average elapsed time from assignment to redline complete |
| Total Contract Cycle Time (Intake to Execution) | ≤20 Business Days (Median) | Median elapsed calendar days across all executed contracts |
| Contract Cycle Time — Tier 3/4 | ≤45 Business Days (Median) | Median elapsed calendar days for High and Critical Risk contracts |
| Stalled Contract Rate | <10% | Percentage of open contracts with no activity in 30+ days |
| Clause Deviation Rate | <15% | Percentage of executed contracts containing at least one approved Clause Deviation |
| Approval Bottleneck Time | <8 Business Hours per Stage | Average time a contract spends awaiting approval at each approval stage |
| Post-Execution Obligation Entry | 95% within 10 days | Percentage of executed contracts with obligations entered within SLA |

### 7.2 Reporting and Dashboard

The Legal Operations Manager shall maintain a real-time dashboard in the CLM visible to the General Counsel, Chief Compliance Officer, and the CEO's Chief of Staff. The dashboard displays:

- All contracts in process, with current stage and aging
- KPI performance against targets, with month-over-month trend lines
- Approval queue depths for each stage
- Stalled contract list with Contract Owner and days stalled
- Clause Deviation Requests open and approved
- Top 10 longest-cycle-time contracts (for root cause analysis)

### 7.3 Quarterly Business Review

The General Counsel shall present a Quarterly Contract Review to the Executive Leadership Team covering:

- Volume: Total contracts submitted, executed, and terminated/expired
- Cycle time trends and outliers
- Risk distribution (percentage of Tier 3 and Tier 4 contracts executed)
- Clause Library deviation trends and emerging negotiation patterns
- Top counterparty negotiation challenges and market intelligence
- Resource utilization and capacity planning for the Legal & Compliance team

---

## 8. Exception Handling and Escalation

### 8.1 Clause Deviation Requests

**8.1.1 When a Clause Deviation Request is Required:**
A formal Clause Deviation Request (CDR-001) must be submitted via the CLM whenever:
- A contractual clause falling outside the Preferred or Fallback positions in the Clause Library is proposed
- The Commercial Counsel believes a business justification exists to accept a clause designated as "Escalation Required"
- The Contract Owner requests an exception to Signature Authority policy
- A contract requires execution on less than five (5) business days' notice ("Emergency Execution")

**8.1.2 CDR-001 Submission and Approval Workflow:**

1. **Requestor Initiates:** The Commercial Counsel or Contract Owner completes the CDR-001 form within the CLM, specifying the clause in question, the proposed deviation, the business justification (including risk assessment and mitigation), and the commercial impact of rejection.

2. **Risk Evaluation:** The Commercial Counsel assigned to the contract evaluates the deviation and provides a written legal risk assessment, categorizing the risk as:
   - **Acceptable:** Risk is within Meridian's risk appetite; approve
   - **Acceptable with Mitigation:** Risk can be offset by commercial terms (e.g., higher pricing, shorter term); approve with noted mitigation
   - **Significant:** Risk represents a material departure from standard protections; requires escalation

3. **Approval Authority for CDRs:**

| CDR Risk Level | Approval Required |
|---|---|
| Acceptable | Commercial Counsel |
| Acceptable with Mitigation | Commercial Counsel + BU Vice President |
| Significant | General Counsel (or designee); CEO if TCV >$1M |

4. **Documentation:** All CDRs, whether approved or denied, are permanently recorded in the contract record in the CLM, creating an auditable record of the exception and its justification.

### 8.2 Escalation Paths

**8.2.1 Contract Dispute / Impasse Escalation:**
If negotiations reach an impasse, the escalation path is:

1. Commercial Counsel and Contract Owner convene to discuss strategy and alternatives.
2. If unresolved, escalate to the Commercial Counsel's managing Senior Counsel and the Sales VP.
3. If still unresolved and the contract is Tier 3 or above, or if the impasse involves a Clause Library Hard Stop, escalate to the General Counsel and the relevant Executive (CRO, CPO, or CEO).
4. The General Counsel has final authority on all legal positions. A decision to accept a Hard Stop clause requires a CDR approved by the General Counsel and the CEO.

**8.2.2 Urgent / Emergency Contract Requests:**
A contract requiring execution in fewer than five (5) business days from intake must be accompanied by a CDR-001 with an urgency justification. The Triager will expedite the request within the CLM, but the standard review steps may not be bypassed. The General Counsel or Deputy General Counsel must personally approve the Legal Review phase for all emergency requests.

### 8.3 Contract Disputes Post-Execution

Any dispute arising under an executed contract must be immediately reported to the Legal & Compliance department through the Litigation & Disputes notification email (`litigation@meridian.com`). The Contract Owner shall not make any admissions of liability, offer settlements, or modify contractual obligations in response to a dispute without Legal & Compliance direction.

---

## 9. Training Requirements

### 9.1 Required Training Modules

All individuals involved in the contracting process must complete the following training modules, assigned via the Meridian Learning Management System (LMS) — `https://lms.meridian.com`:

| Training Module | Code | Audience | Frequency | Duration |
|---|---|---|---|---|
| Contracting Fundamentals at Meridian | TRN-LEGC-006-01 | All Contract Owners, all Sales staff | Upon hire; annual refresher | 90 minutes |
| CLM System Training: Requesters | TRN-LEGC-006-02 | Contract Owners | Upon hire; update training on new releases | 60 minutes |
| CLM System Training: Approvers & Reviewers | TRN-LEGC-006-03 | Commercial Counsel, Finance, InfoSec, Exec Approvers | Upon role assignment; update training on new releases | 120 minutes |
| Clause Library and Risk Assessment Workshop | TRN-LEGC-006-04 | Commercial Counsel, Legal Operations | Semi-annual (live workshop) | 3 hours |
| Revenue Recognition for Contract Approvers | TRN-FIN-004-01 | Finance Reviewers, Directors+ in Sales | Annual | 60 minutes |
| Signature Authority Delegation and Compliance | TRN-LEGC-006-05 | All Signatories (VP and above) | Annual | 45 minutes |

### 9.2 Training Tracking and Compliance

**9.2.1 LMS Tracking:** Completion of all assigned training modules is tracked in the LMS. Reports are generated monthly and reviewed by the Legal Operations Manager. Non-completion of required training is reported to the individual's supervisor.

**9.2.2 Certification:** Individuals must achieve a passing score of 85% or higher on the knowledge assessment associated with each training module. Failure to pass within two attempts requires in-person remediation with a member of the Legal & Compliance training team.

**9.2.3 System Access Gating:** CLM access is gated behind training completion. A user account will not be provisioned with "Contract Owner" or "Approver" permissions until the required training modules are marked as complete in the LMS. If an individual's annual refresher training becomes overdue by more than thirty (30) days, their CLM permissions are automatically suspended until the training is completed.

### 9.3 Training for New Hires

All new hires in Sales, Business Development, Procurement, and any manager-level or above role that may originate a contract shall complete TRN-LEGC-006-01 and TRN-LEGC-006-02 within their first two weeks of employment. Managers are responsible for ensuring direct reports are enrolled.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs and Policies

| Document ID | Document Title | Relationship |
|---|---|---|
| SOP-LEGC-001 | Legal Hold and Litigation Response | Governs preservation obligations that may affect contracts in dispute |
| SOP-LEGC-003 | Intellectual Property Protection and Patent Filing | IP ownership and assignment clauses must align with this SOP |
| SOP-FINC-002 | Revenue Recognition: ASC 606 Compliance | Finance review criteria are derived from this policy |
| SOP-SEC-005 | Information Security Exhibit Management | Standard security exhibit and InfoSec review procedures |
| SOP-PRIV-001 | Cross-Border Data Transfer Procedures | Governs SCC and DPA integration into contracts |
| SOP-PROC-003 | Vendor Qualification and Procurement | Vendor contract initiation process and thresholds |
| SOP-RISK-001 | Enterprise Risk Management Framework | Risk Tier definitions align with ERM risk appetite statements |
| POL-HR-007 | Employee Code of Conduct and Business Ethics | Conflict of interest and ethical contracting principles |
| SOP-CLIN-002 | Clinical Partnership Governance | Specialized contracting requirements for clinical AI deployments |
| SOP-TECH-004 | Product Development and Customization | Governs approval of custom development commitments in contracts |

### 10.2 External Standards and Frameworks

- ASC 606: Revenue from Contracts with Customers
- International Commercial Terms (Incoterms 2020)
- UNIDROIT Principles of International Commercial Contracts 2016

### 10.3 Meridian Systems Referenced

| System | Purpose |
|---|---|
| Conga CLM (integrated with Salesforce) | Contract Lifecycle Management — system of record |
| DocuSign | Electronic signature execution |
| Intapp | Conflict checking and new business intake |
| Intapp Time | Matter tracking and time recording for Legal |
| Salesforce Sales Cloud | Opportunity and account management; CLM integration source |
| NetSuite | Financial system; TCV validation and revenue scheduling |
| LMS (Workday Learning) | Training assignment, completion tracking, and certification |

---

## 11. Revision History

| Version | Effective Date | Author | Description of Changes |
|---|---|---|---|
| 1.0 | 2020-03-12 | Thomas Anderson, CCO | Initial publication. Established foundational contract review workflow, basic intake form, and approval matrix. |
| 2.0 | 2021-09-01 | Maria Gonzalez, GC | Major revision. Introduced Clause Library concept, Risk Tier classification system, expanded roles to include Privacy Counsel, and added CDR process. Updated signature authority to reflect organizational growth. |
| 2.5 | 2022-06-14 | Sarah Chen, Legal Ops Mgr | Mid-cycle update. Integrated Conga CLM system following migration from manual SharePoint tracking. Added system-specific procedures, established first formal KPIs. |
| 3.0 | 2023-11-01 | Thomas Anderson, CCO | Substantive rewrite. Expanded scope to international subsidiaries, added Regional Counsel roles, aligned Risk Assessment Matrix with ERM framework (SOP-RISK-001), added Section 9 (Training Requirements), and increased approval thresholds to reflect company growth. |
| 3.2 | 2024-03-28 | David Okafor, Sr. Commercial Counsel | Minor revision. Updated Clause Library governance following EU MDR CE marking (2025). Revised Clinical AI contracting procedures. Added HealthPay-specific review queue and regulatory overlay. |
| 3.5 | 2024-10-15 | Sarah Chen, Legal Ops Mgr | Revisions to KPIs and reporting cadence based on two years of CLM data. Adjusted cycle time targets. Added "No-Self-Review" policy. Incorporated Finance review step for ASC 606 alignment. |
| 3.7 | 2025-11-07 | Thomas Anderson, CCO | Current version. Updated Contracting Entity list for Ireland subsidiary. Revised CIF-001 fields to add Data Classification and Regulatory Trigger. Clarified obligation management procedures. Updated Approval Authority Matrix thresholds for inflation. Revised training module codes. |

---

**END OF DOCUMENT**

*This document is classified as "Internal" and is proprietary to Meridian Health Technologies, Inc. Distribution outside of the intended audience requires approval from the Document Owner. Printed copies are uncontrolled; refer to the CLM for the current authoritative version.*
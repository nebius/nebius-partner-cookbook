---
sop_id: "SOP-FIN-014"
title: "Third-Party Payment Provider Management"
business_unit: "Financial Services"
version: "3.1"
effective_date: "2025-03-28"
last_reviewed: "2026-07-14"
next_review: "2027-01-17"
owner: "Robert Liu, VP of Financial Services"
approver: "James Thornton, Chief Financial Officer"
classification: "Internal"
regulations:
  - "SOC 2"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Third-Party Payment Provider Management

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework and governance model for the end-to-end lifecycle management of all third-party payment providers engaged by Meridian Health Technologies, Inc. (“Meridian”). The document sets forth the uniform requirements for identifying, evaluating, selecting, contracting, onboarding, monitoring, and offboarding external entities that process, transmit, store, or facilitate payment transactions on behalf of Meridian’s HealthPay Financial Services business line or any other Meridian business unit that handles patient financial data.

The objectives of this SOP are to:

- Ensure that all third-party payment providers meet Meridian’s operational resilience, security, compliance, and performance standards before and throughout the engagement lifecycle.
- Establish consistent due diligence procedures commensurate with the risk profile of each provider engagement.
- Define ongoing monitoring responsibilities to detect and remediate service degradation, control failures, or regulatory non-compliance in a timely manner.
- Maintain a comprehensive inventory of payment provider relationships with associated contractual obligations, risk ratings, and performance metrics.
- Protect the confidentiality and integrity of patient financial information and payment data throughout the third-party relationship.

### 1.2 Scope

This SOP applies to all external entities classified as "Third-Party Payment Providers," defined as any organization outside Meridian that performs one or more of the following functions:

| Category | Examples |
| --- | --- |
| Payment Gateways and Processors | Entities that authorize, capture, settle, or route payment card, ACH, or real-time payment transactions |
| Merchant Acquirers | Entities that manage merchant accounts and fund settlement on Meridian’s behalf |
| Alternative Payment Facilitators | Digital wallet providers, Buy-Now-Pay-Later platforms, healthcare-specific financing partners |
| Payment Data Aggregators | Services consolidating payment reporting across multiple channels |
| Payer Reimbursement Intermediaries | Third-party services that facilitate insurance payer reimbursements to patient payment accounts |
| Payment Fraud and Risk Scoring Services | External fraud detection engines processing HealthPay transaction data |
| Payment-related Subprocessors | Any subcontractor of a contracted payment provider that touches patient payment data |

**In-Scope Business Units and Systems:**

- HealthPay Financial Services (primary)
- Patient Billing and Revenue Cycle platforms that interface with external payment rails
- Any Meridian-developed or managed application transmitting payment instructions to external providers
- All environments (production, staging, disaster recovery) where payment provider integrations are deployed

**Out of Scope:**

- Internal Meridian payment processing capabilities built and operated entirely by Meridian personnel on Meridian-owned infrastructure
- Banking relationships where Meridian is the account holder and the bank does not perform payment facilitation on behalf of Meridian’s patients or payers (these are governed by SOP-TREAS-002)
- Insurance payer direct connections for claims adjudication that do not involve patient payment facilitation

### 1.3 Applicability

This SOP applies to the following personnel:

- All Financial Services employees and contractors
- IT Operations & Infrastructure personnel responsible for payment system connectivity
- Information Security team members involved in third-party risk assessments
- Legal and Procurement personnel supporting HealthPay vendor contracting
- Compliance personnel overseeing payment-related regulatory obligations
- Any Meridian employee who participates in a project involving integration with an external payment provider

Adherence to this SOP is mandatory. Violations may result in disciplinary action up to and including termination of employment.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
| --- | --- |
| **Business Continuity Plan (BCP)** | A documented set of procedures enabling Meridian to maintain essential functions during a disruption; for payment providers, the focus is the provider’s own BCP |
| **Critical Payment Provider** | A third-party payment provider whose failure would cause material financial loss, significant regulatory exposure, or severe reputational harm to Meridian, as determined by the inherent risk assessment |
| **Inherent Risk** | The risk level posed by a provider engagement before considering mitigating controls |
| **Material Subcontractor** | A subcontractor engaged by a payment provider to perform a function that is integral to the payment service and whose failure would impact Meridian’s operations |
| **Offboarding** | The process of terminating a payment provider relationship securely, including settlement of final funds, revocation of access, and destruction or return of Meridian data |
| **Payment Data** | Any cardholder data, bank account information, patient payment instrument details, transaction records, or associated metadata handled by a provider on Meridian’s behalf |
| **Provider Risk Tier** | Classification assigned during due diligence (Tier 1 – Low, Tier 2 – Medium, Tier 3 – High, Tier 4 – Critical) determining the depth of assessment required |
| **Residual Risk** | The risk remaining after controls and mitigating factors are applied |
| **Service Organization Control (SOC) Report** | An attestation report issued by an independent auditor on a service organization’s controls |
| **Third-Party Payment Provider** | As defined in Section 1.2 |

### 2.2 Acronyms

| Acronym | Definition |
| --- | --- |
| **ACH** | Automated Clearing House |
| **BCP** | Business Continuity Plan |
| **CISO** | Chief Information Security Officer |
| **DR** | Disaster Recovery |
| **IS** | Information Security |
| **KPI** | Key Performance Indicator |
| **KRI** | Key Risk Indicator |
| **MNDA** | Mutual Non-Disclosure Agreement |
| **MSA** | Master Services Agreement |
| **PCI** | Payment Card Industry |
| **PIA** | Privacy Impact Assessment |
| **QSA** | Qualified Security Assessor |
| **RACI** | Responsible, Accountable, Consulted, Informed |
| **RFI** | Request for Information |
| **RFP** | Request for Proposal |
| **ROI** | Return on Investment |
| **RTO** | Recovery Time Objective |
| **RPO** | Recovery Point Objective |
| **SIG** | Standard Information Gathering (questionnaire) |
| **SLA** | Service Level Agreement |
| **TPRM** | Third-Party Risk Management |
| **VRM** | Vendor Risk Management |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix

The following RACI matrix delineates responsibilities for the major phases of this SOP:

| Activity / Deliverable | VP, Financial Services (Owner) | VP, Engineering (Approver) | Sr. Director, Procurement | CISO / InfoSec TPRM Lead | Business Owner / Product Lead | Treasury Manager | Compliance Officer |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Provider Identification & Business Case | A | I | C | I | R | C | I |
| Inherent Risk Assessment | A | I | I | R | C | I | C |
| RFI / RFP Process | A | I | R | C | C | I | I |
| Due Diligence Execution | A | I | R | R | C | C | I |
| Contract Review & Approval | A | A | R | C | C | R | I |
| SOC Report Review & Gap Analysis | A | I | C | R | I | I | I |
| Security Architecture Review | A | A | I | R | C | I | I |
| Integration & Onboarding | A | R | I | C | R | I | I |
| Ongoing Monitoring & Scorecards | A | I | C | R | C | C | C |
| Issue Remediation Oversight | A | R | C | R | C | I | I |
| Annual Risk Re-Assessment | A | I | I | R | C | I | C |
| Offboarding & Termination | A | I | R | R | R | R | I |

**R = Responsible** (performs the work); **A = Accountable** (approves and owns outcome); **C = Consulted** (provides input); **I = Informed** (receives communications)

### 3.2 Specific Role Descriptions

**VP of Financial Services (Robert Liu)** — Executive owner of this SOP. Accountable for the overall effectiveness of the third-party payment provider program. Approves all Tier 3 and Tier 4 provider engagements. Chairs the quarterly Payment Provider Oversight Committee.

**VP of Engineering (David Park)** — Approver of this SOP. Accountable for the technical integration architecture and ensuring that payment provider connections do not introduce unacceptable technical debt or instability into the HealthPay platform.

**Sr. Director, Procurement (currently vacant; interim: Maria Okonkwo, Director of Strategic Sourcing)** — Leads all sourcing events. Negotiates commercial terms and SLAs. Maintains the contract repository in Coupa. Ensures all contracts contain required Meridian standard terms.

**CISO / Information Security TPRM Lead (Jennifer Yee)** — Executes all information security risk assessments of payment providers. Reviews SOC reports, penetration test results, and SIG questionnaire responses. Assigns the security residual risk rating.

**Business Owner / Product Lead (varies by engagement)** — Originates the business need. Drafts business requirements and acceptance criteria. Serves as the primary day-to-day relationship manager post-onboarding.

**Treasury Manager (Amit Patel)** — Reviews provider financial statements and Dun & Bradstreet reports. Advises on provider financial viability. Ensures settlement timing aligns with Meridian cash management objectives.

**Compliance Officer (Angela Okonkwo)** — Advises on regulatory impacts of proposed payment provider engagements. Conducts periodic compliance spot-checks of in-flight provider relationships.

**Vendor Management Office (VMO) Lead (Thomas Reinhardt)** — Maintains the central vendor inventory in the Archer GRC platform. Tracks all provider risk tiers, contract renewal dates, and monitoring schedules. Issues quarterly aggregated provider performance reports.

---

## 4. Policy Statements

The following high-level policy commitments govern all interactions with third-party payment providers:

**PS-01 — Risk-Based Due Diligence:** All third-party payment providers shall undergo due diligence prior to contract execution. The depth and intensity of due diligence shall be proportional to the inherent risk tier assigned to the engagement.

**PS-02 — No Payment Data Handling Without Contract:** No third party shall be granted access to Meridian’s payment data, systems, or networks without a fully executed written agreement containing the mandatory contractual provisions enumerated in Section 6.2.

**PS-03 — Continuous Monitoring:** All Critical Payment Providers shall be subject to continuous performance and control monitoring. Tier 1 providers shall undergo annual re-assessment; Tier 4 providers shall undergo quarterly reviews.

**PS-04 — Provider Concentration Risk:** Meridian shall not concentrate more than 70% of total annual payment transaction volume with any single Critical Payment Provider. Transaction volume concentration shall be measured quarterly by the Treasury Manager.

**PS-05 — Subcontractor Visibility:** All contracts shall require the provider to disclose any material subcontractors involved in payment processing functions and to notify Meridian at least 30 days prior to adding or changing such subcontractors. Meridian reserves the right to conduct due diligence on material subcontractors.

**PS-06 — Right to Audit:** All contracts shall include a right for Meridian (or its designated third-party assessor) to audit the provider’s compliance with security, operational, and regulatory requirements. For Critical Payment Providers, at least one on-site audit shall be conducted every 24 months unless a current SOC 2 Type II report covering the relevant trust services criteria is provided and accepted by the CISO.

**PS-07 — Payment Data Localization:** No payment provider shall store patient payment data (card numbers, routing numbers, account numbers) in clear text. All providers must attest to encryption-at-rest for all payment data repositories.

**PS-08 — Termination Assistance:** All Critical Payment Provider contracts shall include a termination assistance clause obligating the provider to support an orderly transition of services for a period not less than 180 days following notice of termination.

---

## 5. Detailed Procedures

### 5.1 Phase 1: Provider Identification and Preliminary Screening

#### 5.1.1 Business Need Articulation

1. The Business Owner or Product Lead shall document the business need on the “Third-Party Services Intake Form” (Meridian Form ID: FIN-TPI-001), hosted in ServiceNow. The form shall capture:
   - Description of the payment function required
   - Expected annual transaction volume and average transaction value
   - Geographic coverage requirements (domestic, cross-border, specific corridors)
   - Required payment rails (card networks, ACH, real-time payments, digital wallets)
   - Patient experience implications
   - Anticipated timeline for selection and go-live
2. The completed form shall be submitted to the Vendor Management Office via ServiceNow workflow. The VMO Lead shall log the intake and assign a unique Opportunity ID.

#### 5.1.2 Market Scan and Longlist

1. The Procurement lead, in consultation with the Business Owner, shall conduct a market scan to identify potential providers. Sources may include industry analyst reports (e.g., Gartner, Forrester), peer referrals, and Meridian’s existing provider relationship network.
2. The output shall be a “Longlist” of 5–10 candidate providers documented in a standardized Comparison Matrix spreadsheet maintained in the Meridian SharePoint Vendor Management library.

#### 5.1.3 Preliminary Inherent Risk Screening

1. Before any substantive engagement with providers, the Business Owner and the Information Security TPRM Lead shall jointly complete a Preliminary Inherent Risk Questionnaire in Archer. The questionnaire evaluates:
   - Payment data sensitivity (cardholder data, PHI linkage)
   - Transaction volume magnitude
   - Integration complexity (API vs. batch vs. hosted payment page)
   - Provider access scope (network ingress, database access, administrative console)
2. The Archer workflow shall auto-calculate a Preliminary Risk Tier using the algorithm below:

| Criterion | Weight | Low (1) | Medium (3) | High (5) | Critical (7) |
| --- | --- | --- | --- | --- | --- |
| Data Sensitivity | 35% | Non-sensitive reference data only | Tokenized or masked payment data | Raw payment instruments, no PHI linkage | Raw payment instruments linked to PHI |
| Annual Transaction Volume | 25% | < $10M | $10M–$100M | $100M–$500M | > $500M |
| Integration Depth | 20% | Hosted page, no backend integration | API with limited scope | Deep API integration with multiple endpoints | On-premise appliance or direct database access |
| Provider Access Scope | 20% | Read-only dashboard | Configuration access | System administration capability | Physical or network-level access to Meridian infrastructure |

**Risk Tier Thresholds:** Tier 1: Score < 1.9 | Tier 2: 2.0–3.9 | Tier 3: 4.0–5.9 | Tier 4: 6.0–7.0

3. The CISO or delegate shall review and approve the risk tier assignment within 5 business days.

---

### 5.2 Phase 2: Formal Due Diligence

#### 5.2.1 Due Diligence Scoping by Risk Tier

The VMO shall coordinate the assembly of a Due Diligence Package based on the assigned risk tier as follows:

**Tier 1 (Low Risk):**
- Standard Meridian MNDA execution
- Completed Meridian Vendor Profile Questionnaire
- Evidence of valid business license
- One bank reference
- Review of publicly available financial information

**Tier 2 (Medium Risk):** All Tier 1 items plus:
- Standard Information Gathering (SIG) Questionnaire completion
- SOC 2 Type II report covering the Security trust services category (or equivalent, e.g., ISO 27001 certificate with Statement of Applicability)
- Penetration test summary report (external-facing infrastructure)
- Dun & Bradstreet credit report
- Two client references from healthcare or adjacent regulated industries

**Tier 3 (High Risk):** All Tier 2 items plus:
- SIG Questionnaire (Core version, full completion)
- SOC 2 Type II report covering Security and Availability trust services categories
- Annual penetration test full report (external and internal infrastructure, application layer)
- PCI DSS Attestation of Compliance (AOC) if cardholder data is in scope
- On-site assessment visit by Meridian Information Security team or designated auditor
- Review of provider’s Business Continuity and Disaster Recovery plans
- Financial statement analysis (last 3 fiscal years) by Treasury Manager

**Tier 4 (Critical Risk):** All Tier 3 items plus:
- SIG Questionnaire (Lite or Core version spanning all applicable trust services criteria)
- SOC 2 Type II report covering Security, Availability, and Confidentiality trust services categories
- Provider’s subcontractor register with associated due diligence summaries
- Independent third-party code review for any custom software components integrated with Meridian
- Live Disaster Recovery exercise observation by Meridian personnel (within 12 months prior to contract)
- On-site assessment including physical security controls review
- Board-level attestation of risk management program effectiveness

#### 5.2.2 Information Security Assessment

1. The Information Security TPRM Lead shall review all submitted materials (SOC reports, pen test results, SIG responses) and prepare a Security Assessment Report (SAR) using the standard template in Archer.
2. The SAR shall assign a Security Control Maturity Rating using a 5-point scale:
   - Level 1: Initial (ad hoc, undocumented)
   - Level 2: Repeatable (process exists, inconsistently applied)
   - Level 3: Defined (documented, standardized)
   - Level 4: Managed (measured, monitored)
   - Level 5: Optimized (continuous improvement, automation)
3. For any control area scored below Level 3, the report shall identify a compensating control or remediation requirement to be included in the contract.
4. The CISO shall review and approve the SAR within 10 business days of submission. Any unresolved “High” or “Critical” findings shall prevent contract execution until remediated or accepted with a documented risk acceptance (see Section 8).

#### 5.2.3 Business and Financial Assessment

1. The Treasury Manager shall assess the provider’s financial viability by reviewing audited financial statements, credit ratings, and market reputation.
2. The Business Owner shall validate functional requirements against provider capabilities via a structured Request for Proposal (RFP) process (for engagements exceeding $500,000 annual spend) or a Request for Information (RFI) process (for engagements below that threshold).
3. At least three client references shall be contacted for Tier 3 and Tier 4 providers. The reference check shall cover operational reliability, responsiveness to issues, and overall satisfaction.

#### 5.2.4 Due Diligence Summary and Go/No-Go Decision

1. Upon completion of all due diligence activities, the VMO Lead shall convene a Due Diligence Review Meeting with the following required attendees:
   - Business Owner
   - VP of Financial Services (or delegate)
   - Information Security TPRM Lead
   - Treasury Manager
   - Compliance Officer
   - Procurement Lead
2. The meeting shall review the Consolidated Risk Scorecard, which aggregates:
   - Inherent Risk Tier
   - Security Control Maturity Rating
   - Financial Stability Score (Treasury assessment)
   - Operational Maturity Score (reference checks, DR plan adequacy)
3. Each attendee shall cast a vote: **“Proceed,” “Proceed with Conditions,”** or **“Do Not Proceed.”** Any “Do Not Proceed” vote shall be accompanied by a written rationale. A single “Do Not Proceed” from the CISO based on an unresolved Critical security finding shall be binding.
4. The outcome shall be documented in Archer and communicated to all stakeholders within 2 business days.

---

### 5.3 Phase 3: Contracting

#### 5.3.1 Mandatory Contractual Provisions

All contracts with third-party payment providers shall include, at minimum, the following provisions:

| Provision | Description | Applicability |
| --- | --- | --- |
| Scope of Services | Detailed description of all services, deliverables, and geographies | All tiers |
| Service Level Agreements (SLAs) | Specific quantitative commitments for availability, transaction processing time, error resolution, and support responsiveness with associated remedies | Tier 2+ |
| Information Security Requirements | Detailed controls based on Meridian’s Information Security Addendum (MSA Schedule C) | All tiers |
| Incident Notification | Obligation to notify Meridian of any security incident affecting Meridian data within 4 hours of detection | All tiers |
| Right to Audit | As per Policy PS-06 | Tier 3+ |
| Subcontractor Disclosure | As per Policy PS-05 | All tiers |
| Termination Assistance | As per Policy PS-08 | Tier 3+ at minimum; recommended for all |
| Data Return and Destruction | Procedures and timelines for returning or securely destroying all Meridian data upon termination | All tiers |
| Insurance Requirements | Minimum coverage limits: Cyber Liability ($10M), Technology E&O ($5M), Commercial General Liability ($2M). Meridian named as additional insured. | Tier 3+ |
| Financial Penalties for Critical Breaches | Specific liquidated damages or service credits for failure to meet SLAs or material control failures | Tier 4 |
| Business Continuity | Provider obligation to maintain and test a BCP/DR plan; provision of test results upon request | Tier 2+ |
| Price Protection | Limitation on annual price increases (CPI + 3% cap unless otherwise negotiated) | All tiers |

#### 5.3.2 Contract Review and Approval Workflow

1. Procurement Lead shall draft the contract using the standard Meridian MSA template augmented with the Payment Services Addendum (Meridian Template ID: MSA-PAY-ADD-2024.1).
2. The draft shall be circulated for review in the following sequence:
   - **Legal Review** (5 business days SLA): Meridian General Counsel or designated external counsel reviews for legal sufficiency, indemnification, limitation of liability, governing law, and dispute resolution.
   - **Information Security Review** (5 business days SLA): CISO or delegate confirms all Information Security Addendum requirements are incorporated.
   - **Treasury Review** (3 business days SLA): Confirms payment terms, settlement timing, termination fees.
   - **Business Owner Review** (3 business days SLA): Confirms SLAs and functional scope.
   - **Final Executive Review** (3 business days SLA): VP of Financial Services and CFO for any contract with total contract value exceeding $1,000,000.
3. All approvals shall be captured in Coupa with auditable timestamps. No contract shall be executed without all required Coupa workflow approvals.

---

### 5.4 Phase 4: Onboarding and Integration

#### 5.4.1 Technical Integration Planning

1. The VP of Engineering shall designate a Technical Integration Lead who shall develop a detailed Integration Plan covering:
   - Architecture diagram depicting data flows and integration touchpoints
   - Network connectivity requirements (VPN, dedicated circuit, API gateway configuration)
   - Authentication and authorization mechanism (OAuth 2.0 with client credentials grant preferred; mutual TLS acceptable)
   - API endpoint inventory with request/response schemas
   - Certificate management and rotation schedule
   - Encryption-in-transit requirements (TLS 1.3 minimum for all payment data flows)
2. The Integration Plan shall be reviewed by the Meridian Security Architecture Board (meets bi-weekly) and approved before any connection is established.

#### 5.4.2 Non-Production Environment Validation

1. All payment provider integrations shall be built and tested first in the Meridian Sandbox environment (M-SANDBOX-PAY) and then in the Staging environment (M-STAGE-PAY).
2. The following test cases shall be executed and results documented in a Test Evidence Report:
   - **Happy Path:** Successful authorization, capture, settlement, and refund for each payment rail
   - **Error Handling:** Simulated declines, timeouts, network interruptions, malformed responses, and rate limiting
   - **Idempotency:** Duplicate submission handling
   - **Reconciliation:** End-of-day settlement file ingestion and matching against internal transaction logs
   - **Failover:** Provider-side failover and Meridian-side circuit breaker activation
3. The Quality Engineering team shall certify test completion. No production traffic shall be routed until the Test Evidence Report is approved by the VP of Engineering or delegate.

#### 5.4.3 Go-Live and Hypercare

1. Go-live shall occur during a pre-scheduled maintenance window communicated to all stakeholders at least 7 calendar days in advance.
2. A “Hypercare” period of 14 calendar days post go-live shall be observed, during which:
   - The Technical Integration Lead and a designated provider escalation contact shall be on standby 24/7.
   - Daily stand-up meetings shall be held to review transaction success rates, latency, and any logged errors.
   - Any Priority 1 or Priority 2 incidents shall trigger the Incident Management process (SOP-ITOP-002).
3. On Day 15, assuming no unresolved Critical issues, the engagement shall transition to “Steady State” and ongoing monitoring procedures (Section 5.5) shall commence.

---

### 5.5 Phase 5: Ongoing Monitoring

#### 5.5.1 Monitoring Cadence by Risk Tier

| Monitoring Activity | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
| --- | --- | --- | --- | --- |
| Quarterly Business Review (QBR) | Not required | Annually | Semi-annually | Quarterly |
| SLA/Performance Scorecard Review | Not required | Quarterly | Monthly | Monthly |
| Security and Compliance Re-Assessment | Annually | Annually | Semi-annually | Quarterly |
| Financial Health Review | Not required | Annually | Semi-annually | Quarterly |
| DR Test Results Review | Not required | Annually | Annually | Semi-annually |
| On-Site Audit | Not required | Not required | Every 24 months | Every 18 months |

#### 5.5.2 Quarterly Business Review Structure

For Tier 3 and Tier 4 providers, each QBR shall cover, at minimum:

1. **Performance Against SLAs (Quantitative):** Trailing 90-day SLA attainment percentages for all contractual service levels.
2. **Incident Review:** Summary of all Priority 1 and Priority 2 incidents in the period, root cause analyses completed, and preventative actions implemented.
3. **Change Management Review:** Summary of significant changes on both Meridian and provider sides that could impact the service.
4. **Security Posture Update:** Any new audit reports, penetration test results, certifications obtained, or security incidents experienced by the provider.
5. **Roadmap Alignment:** Provider product roadmap vs. Meridian’s anticipated needs.
6. **Financial Performance:** Transaction volume trends, billing accuracy, cost optimization opportunities.
7. **Action Item Tracker Review:** Status of all open action items from previous reviews.

Minutes shall be documented in the Archer engagement record within 5 business days of the meeting.

---

### 5.6 Phase 6: Offboarding and Termination

#### 5.6.1 Termination Triggers

A third-party payment provider relationship may be terminated for any of the following reasons (“Termination Triggers”):

- Contract expiration without renewal
- Material breach of contract not cured within the cure period
- Persistent failure to meet SLAs (defined as SLA below 95% attainment for any Critical SLA metric for two consecutive measurement periods)
- Material security incident involving Meridian data that is not satisfactorily remediated within 30 days
- Provider financial insolvency, bankruptcy filing, or material adverse change in financial condition
- Strategic decision by Meridian to insource or transition to an alternative provider
- Regulatory or legal action that prohibits the provider from continuing services

#### 5.6.2 Offboarding Procedure

1. **Offboarding Plan:** Within 10 business days of the termination decision, the Business Owner and VMO Lead shall jointly develop a detailed Offboarding Plan covering:
   - Data inventory and disposition (return, destruction, format)
   - Settlement of all outstanding financial transactions and final invoice
   - Communication to impacted internal and external stakeholders
   - Transition timeline with milestones
   - Revocation of all provider access credentials
2. **Data Recovery:** All Meridian data held by the provider shall be returned in a structured, machine-readable format (CSV, JSON, or Parquet) within the timeline specified in the contract.
3. **Data Destruction Certification:** The provider shall provide a written certification of secure destruction of all remaining copies of Meridian data within 30 days of data return confirmation.
4. **Access Revocation:** All provider access (API keys, VPN credentials, system accounts, physical badges) shall be revoked within 24 hours of the final settlement confirmation. The IS team shall execute a formal access review to confirm no residual access persists.
5. **Closure Documentation:** The VMO Lead shall update the Archer record to “Closed” status and upload all relevant offboarding documentation, including the data destruction certification and a final engagement summary.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control ID | Control Description | Implementation Mechanism |
| --- | --- | --- |
| TC-01 | All payment data in transit to/from third-party providers shall be encrypted using TLS 1.3 or higher | Enforced at Meridian API Gateway (Apigee) and via contract specification; lower TLS versions rejected at handshake |
| TC-02 | API authentication shall use OAuth 2.0 client credentials grant with short-lived access tokens (15-minute expiry) | Apigee OAuth policy enforcement |
| TC-03 | Payment provider API calls shall be subject to rate limiting (1,000 requests/minute per provider tenant) to prevent runaway consumption | Apigee Spike Arrest and Quota policies |
| TC-04 | All payment provider connections shall terminate at a dedicated, segmented network zone (PCI-DSS CDE boundary) | Palo Alto firewall segmentation; zone “EXT-PMT-PROV” |
| TC-05 | Database credentials, API keys, and certificates used for provider integrations shall be stored in HashiCorp Vault; plaintext secrets prohibited in code repositories or config files | Vault secret engine, CI/CD pipeline integration with Vault Agent |
| TC-06 | Multi-Factor Authentication (MFA) shall be enforced for any provider personnel accessing Meridian administrative consoles | Okta MFA with FIDO2/WebAuthn or TOTP; username/password only prohibited |
| TC-07 | All provider API interactions shall be logged, with logs shipped to the centralized SIEM (Splunk) in real time | Fluentd log shippers on API Gateway; Splunk HTTP Event Collector |

### 6.2 Administrative Controls

| Control ID | Control Description |
| --- | --- |
| AC-01 | Third-Party Payment Provider Inventory shall be maintained in Archer with complete engagement records, risk tiers, and monitoring schedules |
| AC-02 | All provider engagements require a fully executed contract before access to any production payment data is granted |
| AC-03 | Annual review of this SOP by the VP of Financial Services and feedback incorporation from all stakeholders |
| AC-04 | Segregation of duties: the individual who approves a provider contract shall not be the same individual who performs ongoing SLA monitoring for that provider; VP of Financial Services approval; VMO performs monitoring |
| AC-05 | All Critical Payment Provider engagements shall have a designated “Executive Sponsor” at the VP level or above within Meridian, documented in the Archer record |
| AC-06 | Access reviews: All provider access credentials shall be reviewed quarterly by the IS team; inactive credentials disabled after 90 days and revoked after 180 days |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The following KPIs shall be tracked and reported monthly via the Payment Provider Performance Dashboard hosted in Grafana:

| KPI | Definition | Target | Measurement Frequency | Owner |
| --- | --- | --- | --- | --- |
| Transaction Success Rate | Completed / Total Attempted transactions | ≥ 99.5% | Continuous, reported monthly | Technical Integration Lead |
| API Latency (p99) | 99th percentile round-trip time for payment API calls (Meridian-to-provider) | < 800 ms | Continuous | SRE Team |
| SLA Attainment Percentage | Weighted % of contractual SLAs met in the measurement period | ≥ 98% | Monthly | VMO Lead |
| Incident Volume (P1/P2) | Number of Priority 1 or Priority 2 incidents attributed to the provider | 0 P1; ≤ 2 P2 per quarter | Quarterly | Incident Manager |
| Time-to-Remediate Findings | Mean calendar days from finding identification to verified closure | ≤ 45 days for High; ≤ 90 for Medium | Quarterly | IS TPRM Lead |

### 7.2 Key Risk Indicators (KRIs)

| KRI | Threshold | Escalation |
| --- | --- | --- |
| Provider SOC Report Lapse | SOC report not renewed within 90 days of prior report expiration | Immediate notification to CISO and VP of Financial Services; provider placed on “Watch” status |
| Financial Viability Concern | Credit rating downgrade by two or more notches, or public reporting of material financial difficulty | Treasury Manager escalates to CFO within 5 business days |
| Unremediated Critical Finding | Any IS finding rated “Critical” not remediated within 30 days of due date | Escalated to CISO; risk acceptance required within 5 days or suspension of new transaction routing |
| Material Subcontractor Change | Addition or change of material subcontractor without 30-day prior notice (contract violation) | Immediate QBR convened; potential contract breach proceedings |

### 7.3 Reporting Cadence

| Report | Audience | Frequency | Medium |
| --- | --- | --- | --- |
| Payment Provider Performance Scorecard | VP of Financial Services, Business Owners, Engineering Leads | Monthly | Grafana dashboard + PDF summary distributed via email |
| Aggregated Provider Risk Report | CISO, Compliance Officer, VP of Financial Services | Quarterly | Archer-generated report, reviewed at Payment Provider Oversight Committee |
| Annual Program Effectiveness Report | CFO, CISO, General Counsel, Board Audit Committee | Annually | Formal written report covering all providers, program KPIs, significant incidents, and continuous improvement initiatives |

### 7.4 Payment Provider Oversight Committee

The Payment Provider Oversight Committee (“PPOC”) shall convene quarterly with the following standing membership:

- VP of Financial Services (Chair)
- VMO Lead (Secretary)
- CISO or Information Security TPRM Lead
- Treasury Manager
- Compliance Officer
- Sr. Director of Engineering for HealthPay platform
- General Counsel or delegate

The PPOC agenda shall include review of the Aggregated Provider Risk Report, any providers on Watch status, significant incidents, and strategic changes to the provider portfolio.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types

Exceptions to this SOP may arise in the following categories:

| Exception Type | Example |
| --- | --- |
| **Urgent Business Need** | A new payment rail must be enabled within 14 days to meet a regulatory mandate, and full Tier 3 due diligence cannot be completed in time |
| **Due Diligence Waiver** | A provider is unwilling to share a penetration test report but is otherwise fully qualified |
| **Contract Term Deviation** | Business Owner requests a contract term longer than the standard 3-year maximum |
| **Control Implementation Variance** | Technical limitation prevents enforcement of MFA for a specific legacy provider integration |

### 8.2 Exception Request Process

1. The requestor shall complete the “Policy Exception Request” form (Meridian Form ID: GRC-EXC-001) in ServiceNow, specifying:
   - The specific provision of this SOP from which deviation is sought
   - Business justification for the exception
   - Compensating controls proposed
   - Duration of exception (not to exceed 12 months without renewal)
   - Risk assessment of operating without the standard control
2. The request shall route for approval according to the following delegation:

| Risk Impact of Exception | Approval Required |
| --- | --- |
| Affects Tier 1 or Tier 2 provider only; no increase in residual risk above Medium | VP of Financial Services |
| Affects Tier 3 or Tier 4 provider; residual risk remains Medium or below | VP of Financial Services + CISO |
| Residual risk increases to High | VP of Financial Services + CISO + Compliance Officer |
| Residual risk increases to Critical | CFO approval required; Board Risk Committee notified |

3. All approved exceptions shall be logged in the Archer engagement record with the expiration date. The VMO Lead shall track all open exceptions and notify owners 30 days prior to expiration.
4. Exceptions shall not be automatically renewed. A new request with updated justification is required for any extension.

### 8.3 Escalation Path

Incidents, control failures, or performance degradations requiring escalation shall follow the path below:

**Operational Escalation (Service Disruption):**
- Level 1: Business Owner + Technical Integration Lead
- Level 2: VP of Engineering + VP of Financial Services
- Level 3: CFO + CISO (for any incident involving confirmed data exfiltration or service outage exceeding 4 hours during business hours)

**Contractual/Commercial Escalation:**
- Level 1: Procurement Lead
- Level 2: Sr. Director, Procurement + Business Owner
- Level 3: VP of Financial Services + General Counsel

**Provider Risk Escalation (e.g., material security finding, financial distress):**
- Immediate notification to VMO Lead → VMO convenes ad hoc PPOC within 5 business days → Decision recorded in Archer

---

## 9. Training Requirements

### 9.1 Role-Based Training Curriculum

All personnel with responsibilities under this SOP shall complete the following training:

| Role Group | Required Training Module | Delivery Method | Frequency | Tracking System |
| --- | --- | --- | --- | --- |
| All Financial Services personnel | “Third-Party Risk Management Fundamentals” (Course ID: LMS-TPRM-101) | Online, self-paced (45 min) | Annually | Workday Learning |
| Business Owners and Product Leads | “Managing Third-Party Payment Relationships” (Course ID: LMS-PAY-201) | Instructor-led virtual (2 hours) | Annually | Workday Learning |
| Procurement and VMO personnel | “Advanced Vendor Due Diligence for Healthcare Payments” (Course ID: LMS-PAY-301) | Instructor-led (half-day) + case study | Bi-annually | Workday Learning |
| Information Security TPRM assessors | “Conducting Payment Provider Security Assessments” (Course ID: LMS-IS-401) | Workshop (1 day) | Annually + on material updates to assessment methodology | Workday Learning |
| All roles | “Payment Data Handling Policy Refresher” (SOP-IS-008 awareness module) | Online micro-learning (15 min) | Quarterly | Workday Learning |

### 9.2 Training Compliance Tracking

1. The VMO Lead, in coordination with the Learning & Development team, shall generate a monthly training compliance report from Workday. Any individual more than 30 days past due on required training shall:
   - Receive an automated reminder with their direct manager copied.
   - At 60 days past due: escalation to VP-level manager.
   - At 90 days past due: temporary suspension of access to provider management systems (Coupa, Archer) until training is completed.
2. Training compliance metrics shall be included in the quarterly PPOC report.

### 9.3 New-Hire and Role-Change Requirements

- Any new hire joining a role covered by this SOP shall complete all required training modules within 30 calendar days of their start date.
- Any employee transferring into a role with additional training requirements shall complete the applicable modules within 45 calendar days of the transfer effective date.

---

## 10. Related Policies and References

### 10.1 Meridian Internal Policies

| SOP / Policy ID | Title | Relationship to This SOP |
| --- | --- | --- |
| SOP-IS-008 | Payment Card Data Handling and Security | Defines technical controls for payment data handling referenced in this SOP’s control sections |
| SOP-TREAS-002 | Treasury and Banking Relationship Management | Governs banking relationships outside the third-party payment provider scope |
| SOP-PROC-005 | Third-Party Risk Management Program | Overarching TPRM framework; this SOP operationalizes for payment providers specifically |
| SOP-ITOP-002 | Incident Management and Response | Incident handling procedures invoked during provider-related service disruptions |
| SOP-ENG-011 | API Security and Gateway Configuration | Technical standards for API integration referenced in onboarding procedures |
| SOP-IS-012 | Vendor Access Management | Detailed access provisioning and deprovisioning procedures for external parties |
| SOP-LEG-003 | Contract Review and Approval Standards | Legal review process standards; this SOP defers to that process with payment-specific addenda |
| SOP-COMP-004 | Regulatory Change Management | Governs how Meridian tracks and responds to regulatory changes affecting payment processing |

### 10.2 External Standards and Frameworks

- **PCI DSS v4.0.1** — Payment Card Industry Data Security Standard (applicable to all card-processing relationships)
- **NIST SP 800-53 Rev 5** — Security and Privacy Controls for Information Systems and Organizations
- **ISO/IEC 27001:2022** — Information security, cybersecurity and privacy protection
- **Shared Assessments Program** — Standard Information Gathering (SIG) Questionnaire toolset
- **NACHA Operating Rules (2025 Edition)** — For ACH processing relationships

---

## 11. Revision History

| Version | Effective Date | Author / Reviewer | Summary of Changes |
| --- | --- | --- | --- |
| 1.0 | 2022-11-01 | Robert Liu (author); James Thornton (approver) | Initial publication. Established baseline framework for third-party payment provider lifecycle management. |
| 1.1 | 2023-04-15 | VMO Lead Thomas Reinhardt (reviewer) | Minor update: Clarified RACI matrix roles for Procurement vs. VMO; added definitions for Critical Payment Provider and Material Subcontractor. |
| 2.0 | 2024-01-22 | Robert Liu (author); CISO Jennifer Yee (co-author); James Thornton (approver) | Major revision: Introduced formal 4-tier risk classification; expanded due diligence requirements; added mandatory QBR structure; integrated Archer GRC platform references; added Section 7 (Monitoring, Metrics, and Reporting) with specific KPIs and KRIs; revised escalation paths. Triggered by post-acquisition integration learnings. |
| 2.1 | 2024-09-03 | Compliance Officer Angela Okonkwo (reviewer) | Updated PCI references to v4.0.1; added mandatory MFA control TC-06; clarified offboarding data destruction certification requirements. |
| 3.0 | 2025-03-28 | Robert Liu (author); James Thornton (approver) | Major revision: Restructured due diligence tiers to align with updated TPRM program (SOP-PROC-005 v4.0); introduced Preliminary Inherent Risk Screening algorithm; expanded onboarding to include mandatory Hypercare period; added TC-07 (SIEM log integration); revised Section 9 training curriculum to reflect Workday Learning migration; added reference to SOP-COMP-004. |
| 3.1 | 2026-07-14 | Robert Liu (reviewer); VMO Lead Thomas Reinhardt (reviewer) | Minor revision: Updated Procurement Sr. Director vacancy note; adjusted SLA Attainment KPI threshold from 99% to 98% based on 18-month trend data; clarified that PPOC agenda must include Watch-status providers; revised hypercare duration from 7 to 14 calendar days; added requirement for provider Board-level attestation on risk programs for Tier 4; minor terminology updates. |
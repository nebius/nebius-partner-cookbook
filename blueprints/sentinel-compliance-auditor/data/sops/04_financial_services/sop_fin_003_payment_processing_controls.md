---
sop_id: "SOP-FIN-003"
title: "Payment Processing Controls"
business_unit: "Financial Services"
version: "2.7"
effective_date: "2025-10-09"
last_reviewed: "2026-06-22"
next_review: "2026-12-09"
owner: "Robert Liu, VP of Financial Services"
approver: "James Thornton, Chief Financial Officer"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Payment Processing Controls

**SOP-FIN-003 | Version 2.7**

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the control framework governing all payment processing activities within Meridian Health Technologies, Inc.’s HealthPay Financial Services business unit. The purpose of this document is to define standardized, auditable, and compliant procedures for the end-to-end lifecycle of payment transactions—from authorization to settlement and reconciliation—ensuring the confidentiality, integrity, and availability of financial data in alignment with the organization's SOC 2 Type II trust services criteria, Payment Card Industry Data Security Standard (PCI DSS) requirements, and SR 11-7 model risk management guidance where payment models intersect with credit extension features.

### 1.2 Scope

This SOP applies to:

| Scope Area | Coverage Details |
|------------|------------------|
| **Business Units** | HealthPay Financial Services (primary), MedInsight Analytics (patient payment analytics modules only), Meridian SaaS Platform (underlying infrastructure components) |
| **Systems** | HealthPay Core Transaction Engine, Stripe Connect integration layer, Snowflake reconciliation data warehouse, Kafka event streaming pipelines, AWS KMS key management, HashiCorp Vault secrets management |
| **Transaction Types** | Healthcare provider payment processing, patient financing disbursements, medical lending origination and servicing, claims automation settlement, patient portal payment collections |
| **Geographies** | North America (USD/CAD), European Union (EUR/GBP), Singapore (SGD) |
| **Personnel** | All employees, contractors, and third-party service providers with access to payment processing systems, transaction data, or supporting infrastructure |
| **Exclusions** | Payroll processing (see SOP-HR-012), corporate accounts payable (see SOP-FIN-008), equity-based compensation disbursements |

### 1.3 Annual Processing Volume Reference

As of the most recent fiscal year, HealthPay processes approximately $4.2 billion in annual transaction volume across 12,400+ provider clients and 3.8 million patient accounts. This SOP governs all associated transaction data flows.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|------|------------|
| **Authorization** | The process by which a card issuer or financial institution approves or declines a transaction based on available funds, fraud scoring, and account status |
| **Capture** | The submission of an authorized transaction for settlement, transferring funds from the cardholder's issuing bank to the merchant's acquiring bank |
| **Settlement** | The final movement of funds between acquiring and issuing banks, resulting in the credit to the merchant account and debit to the cardholder account |
| **Reconciliation** | The systematic comparison of internal transaction records against external settlement reports, bank statements, and processor feeds to identify discrepancies |
| **Chargeback** | A transaction reversal initiated by the cardholder's issuing bank, typically due to dispute, fraud, or processing error |
| **Exception Item** | Any transaction that cannot be automatically processed through standard workflows, requiring manual review and intervention |
| **Idempotency Key** | A unique, client-generated identifier ensuring that duplicate submission of the same payment request does not result in multiple charges |
| **Cardholder Data Environment (CDE)** | The people, processes, and technology that store, process, or transmit cardholder data or sensitive authentication data |
| **Segregation of Duties (SoD)** | The practice of dividing transaction processing responsibilities among multiple individuals to prevent single-point fraud or error |
| **Payment Model** | Any statistical or machine learning algorithm used for fraud detection, credit underwriting, or transaction routing as defined under SR 11-7 guidance |

### 2.2 Acronyms

| Acronym | Full Form |
|---------|-----------|
| ACH | Automated Clearing House |
| API | Application Programming Interface |
| BIN | Bank Identification Number |
| CDE | Cardholder Data Environment |
| CIP | Customer Identification Program |
| CISO | Chief Information Security Officer |
| DPO | Data Protection Officer |
| EFT | Electronic Funds Transfer |
| ERP | Enterprise Resource Planning |
| GL | General Ledger |
| IDS/IPS | Intrusion Detection System / Intrusion Prevention System |
| KPI | Key Performance Indicator |
| KYC | Know Your Customer |
| MID | Merchant Identification Number |
| MTTD | Mean Time to Detect |
| MTTR | Mean Time to Resolve |
| NACHA | National Automated Clearing House Association |
| PCI DSS | Payment Card Industry Data Security Standard |
| PHI | Protected Health Information |
| PII | Personally Identifiable Information |
| PSP | Payment Service Provider |
| QSA | Qualified Security Assessor |
| RTO | Recovery Time Objective |
| RPO | Recovery Point Objective |
| SLA | Service Level Agreement |
| SoD | Segregation of Duties |
| WAF | Web Application Firewall |

---

## 3. Roles and Responsibilities

The following RACI matrix defines accountability, responsibility, consultation, and information flows for payment processing controls:

| Activity / Decision Area | VP Financial Services (Robert Liu) | CFO (James Thornton) | CISO (Rachel Kim) | VP IT Ops (Samantha Torres) | Dir. Payment Ops | Compliance Officer (Thomas Anderson) | Engineering Lead (Payments) | Customer Ops (Michael Chang) |
|---------------------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Payment processing policy approval | A | A | C | C | R | C | I | I |
| Daily reconciliation sign-off | I | I | - | - | A | - | R | - |
| Exception item resolution (Tier 2) | I | - | - | - | A | I | R | C |
| Payment gateway configuration changes | A | C | C | R | R | I | C | I |
| Fraud rule modification | A | I | C | - | R | C | R | - |
| PCI DSS control implementation | I | - | A | R | I | R | C | - |
| SR 11-7 model validation | A | C | - | - | I | R | C | - |
| Incident response declaration | I | A | R | C | I | C | I | I |
| Third-party processor due diligence | A | C | R | C | R | C | - | - |
| Customer-facing SLA definition | C | I | - | - | I | - | - | A |
| Access provisioning to payment systems | I | - | A | R | I | I | - | - |
| Quarterly control attestation | A | I | C | C | R | C | - | - |

**R = Responsible** (executes the work) | **A = Accountable** (signs off / owns outcome) | **C = Consulted** (provides input) | **I = Informed** (receives updates)

### 3.1 Additional Role Specifications

**Director of Payment Operations (currently recruiting, interim: Robert Liu)**
- Oversees day-to-day transaction processing operations
- Manages the Payment Operations team (8 FTE, 24/7 coverage across Boston and Singapore offices)
- Serves as primary escalation point for exception items exceeding $50,000 or 100 transactions per batch
- Maintains reconciliation SLAs and exception aging reports

**Payment Operations Analysts (Level I-III)**
- Execute daily reconciliation procedures per Section 5
- Investigate and resolve Tier 1 exception items
- Document resolution actions in Jira Service Management with required evidence attachments
- Escalate Tier 2 items per exception handling procedures (Section 8)

**Engineering Lead, Payments (Reports to David Park, VP of Engineering)**
- Maintains HealthPay Core Transaction Engine infrastructure
- Implements payment gateway configuration changes through approved change management
- Ensures idempotency key enforcement and transaction deduplication
- Supports incident response with technical root cause analysis

---

## 4. Policy Statements

### 4.1 Transaction Processing Integrity

All payment transactions processed through HealthPay Financial Services shall adhere to the following core policy commitments:

**4.1.1 Idempotency**
Every payment initiation request shall include a client-generated idempotency key. The HealthPay Core Transaction Engine shall enforce strict idempotency for a window of no less than 72 hours from initial submission. Duplicate requests with identical idempotency keys shall return the original transaction state without creating new financial entries. The idempotency key structure shall conform to the format: `{MID}-{YYYYMMDD}-{sequential_32_hex}`.

**4.1.2 Dual Authorization Thresholds**
The following manual approval tiers shall apply to non-automated transactions:

| Transaction Amount | Required Approvals | Authorized Roles |
|--------------------|-------------------|------------------|
| $0 - $50,000 | Single approval | Payment Operations Analyst II+ |
| $50,001 - $250,000 | Dual approval | Payment Ops Analyst III + Director of Payment Ops |
| $250,001 - $1,000,000 | Dual approval + post-review | Director of Payment Ops + VP Financial Services |
| > $1,000,000 | Triple approval | Above + CFO notification within 4 hours |

**4.1.3 Transaction Logging**
The transaction processing pipeline shall emit structured, immutable log events to the Kafka `payment.transactions.v2` topic for every state transition in the payment lifecycle. Logs shall include:

- Timestamp (ISO 8601, UTC, millisecond precision)
- Transaction reference ID (Meridian internal)
- Processor reference ID (external PSP)
- Idempotency key
- Merchant identifier (MID)
- Amount (decimal, in transaction currency)
- Currency code (ISO 4217)
- Transaction type (authorization, capture, settlement, refund, chargeback)
- Processing state (PENDING, AUTHORIZED, CAPTURED, SETTLED, REFUNDED, CHARGED_BACK, FAILED, DECLINED)
- Source system identifier
- User ID or service account ID initiating the action
- Hash of cardholder data token (PCI-compliant token reference)

All transaction logs shall be retained for a minimum of 7 years in Snowflake, with the first 90 days maintained in hot storage and cold storage thereafter, in compliance with financial record-keeping requirements and NACHA rules.

### 4.2 Reconciliation Requirements

**4.2.1 Daily Reconciliation**
Transactional reconciliation between internal HealthPay records and external settlement reports from payment processors (Stripe, Adyen, JPMorgan Chase Merchant Services) shall be completed daily by 14:00 UTC for all transactions settled through the prior business day cutoff (23:59 UTC).

**4.2.2 Reconciliation Tolerances**
The following break thresholds shall trigger formal investigation:

| Reconciliation Category | Acceptable Variance | Investigation Trigger | Mandatory Escalation |
|-------------------------|---------------------|----------------------|----------------------|
| Transaction count mismatch | 0 | Any mismatch | >10 mismatches |
| Settlement amount variance (USD) | ±$0.00 | >$0.00 | >$1,000 aggregate |
| Currency conversion discrepancy | ±0.01% | >0.01% | >0.05% |
| Unmatched settlements | 0 | Any item | >5 items per MID |
| Unmatched refunds | 0 | Any item | >3 items per MID |

### 4.3 PCI DSS Alignment

HealthPay Financial Services maintains a Level 1 PCI DSS merchant status. The following policy commitments support ongoing compliance:

- Cardholder data shall never be stored in plaintext within any Meridian system. All card data transmission and temporary processing shall use PCI-validated point-to-point encryption (P2PE) or tokenization via the Stripe vault.
- The Cardholder Data Environment (CDE) shall be logically segmented from the Meridian SaaS Platform general-purpose network using AWS VPC isolation, dedicated security groups, and network ACLs.
- Access to the CDE shall require multi-factor authentication (Okta Verify or YubiKey FIPS 140-2 certified hardware token) and shall be restricted to named individuals in the Payment Operations and Security Engineering teams.
- Quarterly network vulnerability scans shall be conducted by the approved ASV (Approved Scanning Vendor), currently Coalfire, with remediation SLAs per SOP-IS-015 (Vulnerability Management).
- Penetration testing of payment processing infrastructure shall occur semi-annually, with the next scheduled engagement in Q2 2027.

### 4.4 SR 11-7 Model Risk Management (Payment Models)

Where machine learning models are deployed for credit scoring (medical lending), fraud detection, or dynamic transaction routing, the following SR 11-7 aligned controls shall apply:

- All payment models shall be registered in the Meridian Model Inventory (maintained in MLflow)
- Model validation shall be performed prior to production deployment and annually thereafter by the independent Model Risk Management function reporting to the Chief AI Officer and dotted-line to the Chief Compliance Officer
- Model performance metrics including false positive rates, false negative rates, and demographic fairness indicators shall be tracked monthly and reviewed quarterly by the Payment Model Governance Committee
- Any model with a demonstrated outcome disparity exceeding 20% across protected demographic categories shall be suspended pending remediation

---

## 5. Detailed Procedures

### 5.1 End-to-End Transaction Processing

The HealthPay payment processing lifecycle comprises six distinct phases. Each phase includes mandatory checkpoints and audit trail generation.

#### 5.1.1 Phase 1: Payment Initiation and Validation

**Purpose**: Accept payment requests from authorized channels, validate structural integrity, and perform pre-processing fraud and compliance checks.

**Procedure Steps**:

1. **Request Ingestion**
   - Payment requests shall be accepted exclusively through the HealthPay REST API (`api.healthpay.meridian.com/v3/payments`) or the approved patient portal UI.
   - All API connections shall enforce TLS 1.2 or higher with certificate pinning for server-to-server integrations.
   - API requests shall include mandatory headers: `X-Idempotency-Key`, `X-Meridian-Client-ID`, `Authorization: Bearer <JWT>`.

2. **Structural Validation** (automated, synchronous)
   - The API Gateway (AWS API Gateway with WAF integration) shall validate:
     - JSON schema conformance against the `PaymentRequestV3.json` schema
     - Idempotency key presence and format compliance
     - JWT validity, expiration, and scope
     - Rate limit compliance per client (default: 1,000 requests/sec per MID)
   - Requests failing structural validation shall return HTTP 400 with error code `VALIDATION_ERROR` and a structured error payload.

3. **Pre-Processing Checks** (automated, synchronous, <200ms p95 latency)
   - The Transaction Pre-Processor service shall perform:
     - **Duplicate Detection**: Query transactional ledger in PostgreSQL for existing idempotency key within the 72-hour window. If found, return the cached transaction state with HTTP 200 and `idempotency_replay: true` flag.
     - **Sanctions Screening**: Check merchant and payer against OFAC SDN, EU Consolidated Sanctions List, and internal restricted parties list (maintained by Compliance). Screening uses LexisNexis Bridger via API with response caching (TTL: 24 hours).
     - **Velocity Check**: Calculate transaction velocity per payer token (transactions per 15-minute window). If velocity exceeds 10 transactions per 15 minutes for a given payer token, flag for step-up authentication.
     - **Amount Risk Scoring**: For transactions exceeding $5,000, invoke the Payment Fraud Model (model ID: `fraud-score-v4-2`) hosted on SageMaker endpoint. Transactions scoring above 0.85 (on 0-1 scale) shall be automatically flagged for manual review.

4. **Validation Outcome Routing**
   - **PASS**: Proceed to Phase 2 (Authorization Request)
   - **FLAGGED**: Route to manual review queue in Jira Service Management `PAY-FRAUD-REVIEW` project. Transaction held in `PENDING_REVIEW` state (maximum hold: 4 hours). Notify Payment Operations via PagerDuty (low severity during business hours, high severity for amounts >$50,000 after hours).
   - **BLOCKED**: Reject transaction with appropriate error code. Log blocking reason to Kafka. If sanctions match, notify Compliance Officer via secure channel within 15 minutes.

#### 5.1.2 Phase 2: Authorization

**Purpose**: Obtain real-time authorization from the card network or alternative payment method provider.

**Procedure Steps**:

1. **Processor Selection**
   - The Payment Router service shall determine the optimal processor based on:
     - Card BIN lookup (primary routing table maintained in configuration management)
     - Currency and geographic optimization
     - Processor availability (health check endpoint, 30-second interval)
     - Cost optimization rules (processor fee ranking, updated monthly)
   - For transactions within the EU/EEA, routing preference shall be given to EU-based processors (Adyen) to support data residency objectives.

2. **Tokenization Check**
   - If the payer's payment method is already tokenized in the Stripe vault, retrieve the token via the Stripe API using the customer ID.
   - If token is not present, invoke the tokenization flow, receiving back a `payment_token_id` that is stored in the encrypted `payment_tokens` PostgreSQL table (AES-256-GCM, key managed in AWS KMS, key ID: `arn:aws:kms:us-east-1:123456789:key/payment-token-key`).

3. **Authorization Request**
   - Build ISO 8583 or processor-specific authorization request message with:
     - Tokenized payment credential
     - Amount (in minor currency units: cents, pence, etc.)
     - MID and terminal ID
     - Card acceptor location (provider facility address)
     - MCC code: 8099 (Healthcare Services)
   - Transmit authorization request to selected processor with timeout of 30 seconds and retry policy: maximum 2 retries with exponential backoff (1s, 3s).

4. **Authorization Response Processing**
   - **APPROVED**: Record authorization code, update transaction state to `AUTHORIZED`, emit `AuthorizationEvent` to Kafka.
   - **DECLINED**: Record decline reason code, update transaction state to `DECLINED`, return structured decline message to client. Do NOT expose raw processor decline codes to the client; map to Meridian standard decline reasons.
   - **TIMEOUT / NETWORK ERROR**: Retry per policy. After exhaustion, apply "transaction in doubt" procedure: flag transaction, initiate status inquiry with processor, and notify Payment Operations.

5. **Authorization Hold Management**
   - For card transactions, the authorization hold shall be valid for:
     - 7 days for standard transactions
     - 30 days for healthcare pre-authorization (estimated treatment costs)
   - Holds approaching expiration shall be re-authorized if capture is imminent, using the stored transaction context.

#### 5.1.3 Phase 3: Capture and Settlement

**Purpose**: Initiate the movement of funds from the payer's financial institution to Meridian's settlement account.

**Procedure Steps**:

1. **Capture Trigger**
   - Capture shall be triggered by one of the following events:
     - **Automatic Capture**: Upon provider-defined rule (e.g., "capture upon service completion" triggered by EHR integration webhook). Applied to 73% of HealthPay transactions.
     - **Batch Capture**: Scheduled batch processing at 08:00, 13:00, and 21:00 UTC for accumulated authorizations.
     - **Manual Capture**: Via HealthPay Operations Console, requiring authorization per Section 4.1.2 dual authorization thresholds.

2. **Capture Request Transmission**
   - The Capture Service shall aggregate authorized transactions by processor and MID into batch capture files.
   - Each batch shall contain no more than 5,000 transactions.
   - Capture files shall be transmitted over SFTP (SSH key-pair authentication, keys rotated every 90 days via HashiCorp Vault) to processor endpoints.
   - The batch file shall include a batch header with batch ID, MID, total amount, transaction count, and SHA-256 checksum of the batch body.

3. **Capture Confirmation**
   - Within 1 hour of batch transmission, the Payment Operations reconciliation function shall verify:
     - Processor acknowledgment of batch receipt
     - Processor batch level acceptance (no file-level errors)
     - If batch is rejected, re-process individual transactions within 2 hours
   - Failure to confirm capture within 24 hours of initial authorization shall trigger automatic reversal (authorization release) and customer notification.

4. **Settlement Funds Receipt**
   - Settlement funds shall arrive at Meridian's designated settlement accounts:
     - USD: JPMorgan Chase account ending x4521
     - EUR: Deutsche Bank account ending x7829
     - CAD: RBC account ending x1134
   - Expected settlement timing (per processor agreement):
     - Card transactions: T+1 to T+2 business days
     - ACH: T+1 to T+3 business days
   - Treasury shall monitor settlement receipts daily and escalate any settlement delay exceeding the expected window by more than 1 business day.

#### 5.1.4 Phase 4: Provider Disbursement

**Purpose**: Distribute settled funds to healthcare provider clients net of processing fees.

**Procedure Steps**:

1. **Disbursement Scheduling**
   - Provider disbursements shall be calculated daily: gross settled amount minus HealthPay processing fee minus chargeback holdbacks minus any pending adjustments.
   - The Provider Disbursement Engine (PDE) shall compute net payable amounts per MID per currency.
   - Disbursement files shall be generated in NACHA ACH format for US providers and SEPA Credit Transfer XML format for EU providers.

2. **Disbursement Approval**
   - Disbursement batches exceeding $5,000,000 aggregate shall require explicit approval from the VP of Financial Services or CFO designee.
   - All disbursement batches shall be reviewed by a Payment Operations Analyst II+ before submission to the banking portal.

3. **Disbursement Execution**
   - ACH files transmitted to JPMorgan Chase Treasury Services by 17:00 UTC for next-business-day settlement.
   - SEPA files transmitted to Deutsche Bank by 15:00 CET.
   - International wire transfers (providers without ACH/SEPA capability) shall be initiated individually via the JPMorgan ACCESS portal with dual approval required for wires exceeding $100,000.

4. **Provider Statement Generation**
   - Monthly provider statements shall be generated within 5 business days of month-end.
   - Statements shall include: total processed volume, fee breakdown, chargeback activity, average transaction size, and settlement reconciliation summary.
   - Statements shall be delivered via the HealthPay Provider Portal and optionally via email (encrypted PDF).

#### 5.1.5 Phase 5: Reconciliation

**Purpose**: Detect, investigate, and resolve discrepancies between internal HealthPay records and external settlement reports.

**Procedure Steps**:

1. **Data Collection** (automated, scheduled)
   - The Reconciliation Data Pipeline shall ingest, transform, and load the following sources into Snowflake reconciliation schemas daily:
     - HealthPay internal transaction ledger (`transactions`, `captures`, `refunds`, `chargebacks` tables)
     - Processor settlement reports (Stripe, Adyen, JPMorgan) via SFTP pull at 03:00, 09:00, and 15:00 UTC
     - Bank account transaction feeds via JPMorgan ACCESS and Deutsche Bank db-direct API
     - Kafka transaction event log (for completeness validation)

2. **Automated Reconciliation** (Snowflake stored procedure: `SP_RECONCILE_DAILY`)
   - **Level 1 — Transaction Count Match**: Compare total authorized, captured, and settled transaction counts per processor per MID per day. Tolerances per Section 4.2.2.
   - **Level 2 — Amount Match**: Compare aggregate settlement amounts. Tolerances per Section 4.2.2.
   - **Level 3 — Item-Level Match**: Perform LEFT JOIN reconciliation between internal transaction IDs and processor settlement records by transaction reference. Unmatched items in either direction are flagged as "breaks."
   - **Level 4 — Fee Reconciliation**: Verify that processor fees deducted from settlement match contractual rates by comparing actual fee deductions against contractual rate schedules.

3. **Break Investigation** (manual, by Payment Operations)
   - All reconciliation breaks exceeding thresholds defined in Section 4.2.2 shall be triaged in Jira Service Management using the `PAY-RECON` project.
   - Break categories:
     - **INTERNAL_ONLY**: Transaction exists in HealthPay but not in processor report. Possible causes: authorization expired before settlement, processor processing delay, API error.
     - **PROCESSOR_ONLY**: Transaction settled by processor but missing from HealthPay. Possible causes: orphan transactions, database write failure, integration gap.
     - **AMOUNT_MISMATCH**: Both records exist but amounts differ. Possible causes: partial capture, fee misapplication, currency conversion discrepancy.
   - Investigation steps:
     - Query full transaction lifecycle in Kibana (Elasticsearch observability platform) using transaction reference ID
     - Review Kafka event chain for the transaction
     - Contact processor support via designated channel if processor-side discrepancy suspected
     - Document findings in Jira ticket with evidence attachments

4. **Break Resolution**
   - **INTERNAL_ONLY — Adjust HealthPay**: If transaction is legitimate but not captured in HealthPay, authorized personnel (Payment Ops Analyst III+) may create a manual journal entry via the GL Adjustment Tool. Requires documented justification and manager approval.
   - **PROCESSOR_ONLY — Reconcile**: If transaction was processed but HealthPay missed recording, reconcile retroactively with documented root cause and preventative action.
   - **AMOUNT_MISMATCH**: If processor-side discrepancy, file formal dispute with processor within 5 business days per processor agreement.
   - All break resolutions shall be reviewed by a second Payment Operations team member before closure.

5. **Daily Reconciliation Sign-Off**
   - The Payment Operations Lead (or designated Level III Analyst) shall complete the Daily Reconciliation Checklist:
     - [ ] All reconciliation queries executed successfully
     - [ ] All breaks categorized and assigned to owner
     - [ ] Breaks exceeding escalation thresholds escalated per Section 8
     - [ ] Prior day open breaks reviewed and aged
     - [ ] Daily Reconciliation Report generated (Tableau dashboard refresh verified)
   - Sign-off shall be recorded in the Reconciliation Log (Jira Confluence with audit trail) by 18:00 UTC.

#### 5.1.6 Phase 6: Exception Handling

**Purpose**: Manage transaction exceptions that deviate from standard automated processing flows.

**Exception categories and handling procedures:**

| Exception Category | Examples | First Response SLA | Resolution SLA | Escalation Trigger |
|--------------------|----------|---------------------|----------------|-------------------|
| **Fraud Flag** | ML model score >0.85, velocity exceeded | 4 hours | 48 hours | >$50,000 flagged |
| **Regulatory Hold** | Sanctions screening hit, KYC incomplete | 2 hours | 72 hours | Any sanctions hit |
| **Technical Failure** | API timeout, database deadlock, message queue overflow | 30 minutes | 4 hours | System-wide outage |
| **Customer Dispute** | Payer-initiated chargeback, provider dispute | 1 business day | 15 business days (per card network rules) | Aggregate disputes >1% of volume |
| **Settlement Delay** | Funds not received by expected settlement date+1 | 4 hours | 5 business days | >$250,000 delayed |
| **Reconciliation Break** | Unmatched transactions, amount misalignments | 4 hours | 72 hours | >50 open breaks |

**Exception lifecycle tracking**:
- All exceptions shall be tracked in Jira Service Management with mandatory fields: Exception Category, Transaction Reference ID(s), Amount at Risk, Root Cause (when determined), Resolution Action, and Closure Approval.
- Open exception aging report shall be reviewed at the weekly Payment Operations stand-up (Tuesday 10:00 UTC, Boston office / Google Meet for remote team members in Singapore).

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

#### 6.1.1 Encryption Standards

| Data State | Encryption Standard | Implementation |
|------------|---------------------|----------------|
| **Data in Transit** | TLS 1.2+ (TLS 1.3 preferred), certificate pinning for external processor connections | AWS API Gateway, Application Load Balancer, mutual TLS for SFTP connections |
| **Data at Rest — Transaction DB** | AES-256-GCM, per-table encryption keys managed in HashiCorp Vault | PostgreSQL 15 with pgcrypto extension for column-level encryption of card token references |
| **Data at Rest — Data Warehouse** | AES-256-CBC with envelope encryption | Snowflake, using AWS KMS-managed keys with automatic key rotation (90-day policy) |
| **Data at Rest — Backups** | AES-256, separate backup encryption key | AWS Backup with KMS customer-managed key (key ID: `backup-key-payments-prod`) |
| **Key Management** | FIPS 140-2 Level 2 HSM (AWS KMS), key rotation per SOP-IS-008 | HashiCorp Vault for application-level secrets, AWS KMS for infrastructure encryption |

#### 6.1.2 Network Segmentation

| Network Zone | Purpose | Access Controls | Ingress/Egress Rules |
|--------------|---------|-----------------|----------------------|
| **CDE-Sensitive** | Card payment token processing, PSP communication | Zero Trust, explicit allowlisting of source IPs and service accounts only | Ingress: Payment API Gateway only. Egress: Processor IP ranges only. No internet access. |
| **CDE-Standard** | Payment processing application layer, reconciliation engine | JIT access via Teleport, session recording | Ingress: CDE-Sensitive zone + corporate network. Egress: restricted to approved AWS services + processor endpoints. |
| **Payment-Data** | Transaction data warehouse (Snowflake), Kafka event bus | Service-to-service auth with IRSA roles | Ingress: CDE-Standard zone services. Egress: Monitoring and logging only. |
| **General SaaS** | Meridian SaaS platform, excluding payment components | Standard IAM, Okta SSO | Standard rules; NO connectivity to CDE zones. |

Network ACL violations to CDE zones shall trigger PagerDuty `security-critical` alert with 15-minute response SLA for Security Engineering.

#### 6.1.3 Access Controls

Access to payment processing systems shall be governed by the principle of least privilege and shall follow these access provisioning procedures:

1. **Access Request**
   - All access requests to any payment system, database, or CDE resource shall be submitted via the Jira Service Management `IT-ACCESS` project.
   - Request shall include: User ID, justification, requested role/permission set, manager approval, and expected duration (permanent or time-bound).

2. **Access Approval**
   - **CDE access**: Requires approval from CISO (Rachel Kim) AND Director of Payment Operations.
   - **Payment application access (non-CDE)**: Requires approval from Director of Payment Operations or VP of Financial Services.
   - **Read-only reconciliation data access**: Requires manager approval and Compliance Officer acknowledgment.

3. **Access Provisioning**
   - Access shall be provisioned via Infrastructure as Code (Terraform for AWS IAM, custom automation for application roles) within 1 business day of approval.
   - All access grants shall be logged to the `access_grants` audit table in Snowflake with timestamp, grantor, grantee, and permission set.

4. **Access Review**
   - Managers shall review team members' payment system access quarterly during performance review cycles.
   - Note: Formal, scheduled periodic access review campaigns (e.g., quarterly organization-wide access certification) are not currently mandated by this SOP. Access is reviewed on an as-needed basis during personnel changes, role transitions, and incident post-mortems.

5. **Access Revocation**
   - Upon termination or role change, access shall be revoked within 24 hours (standard) or 4 hours (critical/sensitive roles as designated by the CISO).
   - Emergency revocation (security incident) shall be executed within 1 hour via automated de-provisioning scripts.

#### 6.1.4 Audit Logging and Monitoring

| Log Source | Aggregation | Retention | Alerting |
|------------|-------------|-----------|----------|
| Payment API access logs | Elasticsearch (Elastic Cloud) | 90 days hot, 3 years cold in AWS S3 | 401/403 spike alerts (>50 in 5 min) |
| Transaction state changes | Kafka → Snowflake | 7 years | Failed state transitions exceeding 1% of volume |
| Database audit logs (PostgreSQL pgAudit) | Elasticsearch via Filebeat | 1 year hot, 7 years cold | Schema changes, manual UPDATE/DELETE on financial tables |
| Administrative access to payment consoles | Okta System Log → Splunk (SIEM) | 1 year hot, 7 years cold | Privileged access outside business hours |
| Firewall / WAF logs | Splunk via AWS Firewall Manager | 90 days hot, 3 years cold | SQL injection, XSS attempts (WAF rules: `payment-waf-rules-v2`) |
| Processor communication logs | Splunk via custom forwarders | 1 year hot, 7 years cold | SFTP connection failures, API error rate >2% |

### 6.2 Administrative Controls

#### 6.2.1 Segregation of Duties (SoD)

The following SoD matrix shall be enforced via application role-based access control (RBAC) and monitored through periodic SoD conflict reporting:

| Function | Can Initiate Payments | Can Approve Payments | Can Reconcile | Can Process Refunds | Can Configure Payment Gateway |
|----------|:--:|:--:|:--:|:--:|:--:|
| Payment Operations Analyst I | ✓ | ✗ | ✗ | ✗ | ✗ |
| Payment Operations Analyst II | ✓ | ✗ | ✓ | ✗ | ✗ |
| Payment Operations Analyst III | ✓ | ✓ (≤$50K) | ✓ | ✓ | ✗ |
| Director of Payment Ops | ✓ | ✓ (≤$250K) | ✓ | ✓ | ✗ |
| VP Financial Services | ✓ | ✓ (≤$1M) | ✗ | ✓ (approval) | ✗ |
| Engineering Lead (Payments) | ✗ | ✗ | ✗ | ✗ | ✓ |
| DevOps Engineer | ✗ | ✗ | ✗ | ✗ | ✓ (change mgmt) |

#### 6.2.2 Change Management

All changes to payment processing systems, including gateway configurations, fraud rules, settlement parameters, and reconciliation logic, shall follow the Meridian Change Management policy (SOP-IS-022). Payment-specific requirements:

- Changes with potential financial impact (settlement timing, fee calculation, disbursement logic) require CFO notification prior to implementation
- Emergency changes require post-implementation review within 1 business day
- Payment model updates require pre-deployment validation per SR 11-7 requirements (Section 4.4)

#### 6.2.3 Incident Response

The Payment Processing Incident Response Plan, maintained as a subset of the enterprise Incident Response Plan (SOP-IS-010), defines:

| Incident Severity | Definition | Notification SLA | Response SLA | Recovery SLA |
|--------------------|------------|------------------|--------------|--------------|
| **SEV 1 — Critical** | Complete payment processing outage, transaction loss or duplication >$1M, confirmed data breach | 5 minutes → Payment Ops Director → VP Financial Services → CISO → CFO | All hands on deck, 15-minute update cadence | RTO: 1 hour |
| **SEV 2 — High** | Partial degradation (>20% error rate), single processor outage, reconciliation backlog >12 hours | 15 minutes → Payment Ops Director → VP Financial Services | Dedicated response team, 1-hour update cadence | RTO: 4 hours |
| **SEV 3 — Medium** | Minor degradation (>5% error rate), non-critical system issue, <5 reconciliation breaks >$10K | 1 hour → Payment Ops Lead → Payment Ops Director | During business hours response | RTO: 8 business hours |
| **SEV 4 — Low** | Cosmetic issues, single-transaction anomalies, non-material reconciliation breaks | Next business day → Payment Ops Lead | Routine queue handling | RTO: 3 business days |

The Incident Response Plan includes detailed runbooks for common scenarios (processor outage, database corruption, Kafka topic overflow). **Note**: Periodic tabletop simulation exercises to test these incident response procedures are conducted on an ad-hoc basis when significant system changes occur; formal, regularly-scheduled tabletop exercises (e.g., quarterly or semi-annual) are not currently calendared under this SOP. Coordination with the CISO's office for enterprise-wide incident simulation scheduling is encouraged but not prescribed.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| KPI | Definition | Target | Measurement Frequency | Reporting Dashboard |
|-----|------------|--------|------------------------|---------------------|
| **Transaction Success Rate** | Percentage of submitted transactions reaching SETTLED state | ≥99.5% | Daily rolling, monthly aggregate | Tableau: "Payment Ops — Daily Health" |
| **Authorization Approval Rate** | Percentage of authorization requests approved | ≥92% (varies by payment method) | Weekly | Tableau: "Payment Processing Funnel" |
| **Reconciliation Accuracy** | Percentage of transactions reconciling on first automated pass | ≥99.0% | Daily | Snowflake Reconciliation Dashboard |
| **Reconciliation Timeliness** | Completion of daily reconciliation by 14:00 UTC target | 100% | Daily | Reconciliation Log (Jira Confluence) |
| **Exception Resolution — Age** | Average age of open exception items | ≤48 hours (Fraud: ≤24 hours) | Weekly | Jira Service Management: "Exception Aging Report" |
| **Chargeback Rate** | Chargebacks as percentage of total transactions (by count) | <0.5% (card network threshold: 1%) | Monthly | Tableau: "Dispute & Chargeback Analytics" |
| **Chargeback Win Rate** | Percentage of representments resolved in HealthPay's favor | ≥65% | Monthly | Tableau: "Dispute & Chargeback Analytics" |
| **Customer (Provider) Payout Timeliness** | Disbursement delivered within contracted timeframe | ≥99.9% | Weekly | HealthPay Provider Portal SLA Dashboard |
| **MTTD (Incident)** | Mean time to detect payment processing incidents | ≤5 minutes (automated alerting) | Per incident | PagerDuty Analytics |
| **MTTR (Incident)** | Mean time to resolve payment processing incidents | SEV1: ≤1 hour, SEV2: ≤4 hours | Per incident | PagerDuty Analytics |

### 7.2 Reporting Cadence

| Report | Audience | Frequency | Delivery Channel |
|--------|----------|-----------|------------------|
| Daily Reconciliation Report | Payment Operations, VP Financial Services | Daily by 16:00 UTC | Tableau email subscription + Jira Confluence |
| Weekly Payment Operations Dashboard | VP Financial Services, CISO, Compliance | Weekly (Monday 08:00 UTC) | Tableau |
| Monthly Payment Processing Executive Summary | CFO, VP Financial Services, Compliance, CISO | Monthly (3rd business day) | PDF generated from Tableau, distributed via email |
| Quarterly Payment Model Performance Report | VP Financial Services, Chief AI Officer, Compliance | Quarterly (within 15 days of quarter-end) | MLflow + Tableau combined report |
| Annual Payment Processing Controls Attestation | CFO, External Auditors | Annually (fiscal year-end + 45 days) | Formal attestation letter with control evidence package |

### 7.3 Continuous Monitoring

The following automated continuous monitoring checks shall execute at the specified intervals:

| Check | Frequency | Alerting |
|-------|-----------|----------|
| Transaction throughput deviation (>20% below 30-day moving average) | Every 15 minutes | PagerDuty `payment-warning` |
| Reconciliation completion SLA breach (past 14:00 UTC without sign-off) | Every 30 minutes from 14:00-18:00 UTC | PagerDuty `payment-warning` + email to Payment Ops Director |
| SoD conflict detection (RBAC configuration scan) | Hourly | PagerDuty `security-medium` |
| Processor health check failure (>3 consecutive failures) | Every 30 seconds per processor | PagerDuty `payment-critical` |
| Encryption certificate expiration (<30 days) | Daily | Jira ticket auto-creation, PagerDuty `payment-warning` at T-14 days |
| Database backup completion | Daily | Jira ticket if failed, email to DBA team |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Classification

Exceptions to this SOP are deviations from established procedures, controls, or policy requirements. Exceptions are classified as:

| Type | Definition | Examples |
|------|------------|----------|
| **Procedural Exception** | Deviation from a specified procedure step | Reconciliation completed after 14:00 UTC SLA; manual capture without dual authorization due to urgent provider need |
| **Technical Exception** | System limitation preventing full compliance | Processor API temporarily unavailable, requiring manual workaround |
| **Policy Exception** | Request for permanent or extended deviation from policy requirement | Client integration not supporting idempotency key format; legacy system requiring alternative authentication |
| **Regulatory Exception** | Potential non-compliance with regulatory obligation | Delayed sanctions screening due to vendor API outage; delayed suspicious activity reporting |

### 8.2 Exception Handling Workflow

**Step 1: Exception Identification**
- Any team member identifying a deviation shall create an Exception Record in the Jira Service Management `PAY-EXCEPTION` project within 1 business day of discovery.

**Step 2: Exception Documentation**
The Exception Record shall include:
- Exception description (specific procedure or policy deviated from)
- Root cause (if known)
- Scope (number of transactions, duration, financial impact)
- Mitigation actions already taken
- Proposed remediation and timeline
- Risk assessment (likelihood of recurrence, potential customer impact, regulatory implications)

**Step 3: Exception Triage and Approval**

| Exception Risk Level | Criteria | Approval Required | Resolution Timeline |
|----------------------|----------|-------------------|---------------------|
| **Low** | Isolated procedural deviation, no financial impact, no data exposure | Payment Ops Director | 5 business days |
| **Medium** | Affects >50 transactions, potential financial impact <$10,000, minor data exposure risk | VP Financial Services + CISO notification | 14 business days |
| **High** | Affects >500 transactions, financial impact >$10,000, data exposure, regulatory notification potential | CFO + CISO + Compliance Officer | 30 business days (with interim mitigations within 72 hours) |
| **Critical** | Systemic failure, confirmed data breach, mandatory regulatory reporting | CEO, CFO, CISO, General Counsel | 24 hours containment, 10 business day remediation plan |

**Step 4: Remediation and Closure**
- Approved remediation actions shall be tracked to completion
- Closure evidence shall be attached to the Exception Record
- Exception shall be closed only after remediation verification by an independent reviewer (Payment Ops Director for Low/Medium, Compliance Officer for High/Critical)

### 8.3 Escalation Matrix

| Escalation Trigger | First Point of Contact | Escalation Timeframe | Secondary Escalation |
|--------------------|------------------------|----------------------|----------------------|
| Reconciliation break >$50,000 | Director of Payment Ops | 4 hours | VP Financial Services |
| Suspected fraud (confirmed) | Director of Payment Ops → Compliance Officer | 1 hour | CISO, CFO |
| Data breach (confirmed or suspected) | CISO (per SOP-IS-010) | 15 minutes | CFO, General Counsel |
| Processor outage >2 hours | VP Financial Services | 2 hours | CFO |
| Regulatory inquiry (AML, sanctions) | Compliance Officer | 2 hours | General Counsel |
| Customer-impacting outage >100 transactions | Payment Ops Director → Customer Ops (Michael Chang) | 30 minutes | VP Financial Services |

### 8.4 Whistleblower and Confidential Reporting

Concerns regarding potential fraud, regulatory violations, or policy circumvention may be reported confidentially through the Meridian Ethics Hotline at **(800) 555-ETHICS** or via the web portal `ethics.meridian.com`. Reports related to payment processing shall be triaged directly to the Compliance Officer (Thomas Anderson) and are subject to the Non-Retaliation Policy (SOP-HR-029).

---

## 9. Training Requirements

### 9.1 Role-Based Training Requirements

| Role | Required Training | Frequency | Delivery Method | Tracking |
|------|-------------------|-----------|-----------------|----------|
| **Payment Operations Analysts (All Levels)** | Payment Processing Controls (SOP-FIN-003 Core); PCI DSS Fundamentals; Fraud Awareness; Reconciliation Procedures | Initial: within 30 days of hire. Annual refresher. | Docebo LMS (e-learning) + hands-on workshop with Payment Ops Director | Docebo completion record, manager sign-off for workshop |
| **Payment Operations Analysts III and above** | Above + Advanced Fraud Detection; Dispute Management; Model Risk Awareness | Initial: within 30 days of promotion. Biennial refresher. | Instructor-led (virtual or Boston office) | Docebo + instructor sign-off |
| **Director of Payment Operations** | Above + Management Oversight of Payment Controls; SR 11-7 Management Responsibilities | Annual | External training provider (approved by Compliance) | Certificate of completion uploaded to Docebo |
| **VP Financial Services** | Payment Processing Governance Overview; Regulatory Landscape Update | Annual | Executive briefing by Compliance Officer | Attendance record in Confluence |
| **Engineering Lead (Payments) and DevOps Engineers** | Secure Coding for Payment Applications; PCI DSS for Developers; Change Management in CDE | Initial: within 30 days. Annual secure coding refresher. | Docebo + OWASP training modules | Docebo completion |
| **Compliance Officer** | Payment Systems Audit Techniques; Regulatory Updates (FFIEC, FinCEN, GDPR cross-training) | Annual | Industry conference or external CPE | CPE record |
| **All Employees with CDE Access** | PCI DSS Security Awareness; Phishing Awareness; Data Handling Procedures | Quarterly micro-learning | Docebo LMS (15-minute modules) | Docebo completion |

### 9.2 Training Compliance Tracking

- Training completion shall be tracked in Docebo LMS with monthly compliance reporting to the VP of Financial Services.
- Training delinquency exceeding 30 days past due date shall trigger notification to the employee's manager and the Compliance Officer.
- Delinquency exceeding 60 days shall result in suspension of payment system access until training is completed.

### 9.3 New Procedure Onboarding

- Major revisions to this SOP (version increment to X.0) shall be accompanied by mandatory training for all affected personnel within 45 days of revision effective date.
- Minor revisions (X.Y increments) shall be communicated via the Payment Operations Confluence space with acknowledgment tracking.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|--------|-------|--------------|
| SOP-IS-008 | Encryption and Key Management | Encryption standards for payment data at rest and in transit |
| SOP-IS-010 | Enterprise Incident Response Plan | Incident severity definitions, notification chains |
| SOP-IS-015 | Vulnerability Management | ASV scanning and remediation timelines for CDE |
| SOP-IS-022 | Change Management Policy | Change control for payment gateway and processing systems |
| SOP-IS-035 | Access Management and Identity Governance | Access provisioning and revocation for payment systems |
| SOP-SEC-002 | Fraud Detection and Response | Integration with payment fraud model and manual review queue |
| SOP-CMP-011 | Third-Party Vendor Risk Management | Due diligence for payment processors (Stripe, Adyen, JPMorgan) |
| SOP-CMP-019 | Sanctions Screening Program | OFAC/EU sanctions screening procedures referenced in transaction validation |
| SOP-DAT-004 | Data Retention and Disposal | 7-year transaction log retention; secure disposal of cardholder data |
| SOP-HR-029 | Non-Retaliation Policy | Whistleblower protections for ethics hotline reporting |
| SOP-MDL-001 | Model Risk Management Framework | SR 11-7 governance for payment ML models |

### 10.2 External Standards and Regulatory References

| Standard / Regulation | Applicability |
|-----------------------|---------------|
| SOC 2 Trust Services Criteria | Security, Availability, Processing Integrity, Confidentiality, Privacy — entire SOP scope |
| PCI DSS v4.0.1 | Cardholder data environment controls, SAQ D for Level 1 merchants |
| NACHA Operating Rules | ACH transaction processing, return rates, security framework |
| FFIEC BSA/AML Examination Manual | Customer identification, suspicious activity monitoring |
| SR 11-7 (Federal Reserve) | Model risk management for ML-based payment and fraud models |
| General Data Protection Regulation (GDPR) | Personal data processing for EU/EEA payer data |
| ISO 20022 | Payment messaging standards for SEPA and cross-border transactions |
| ISO 8583 | Financial transaction card originated messages (for legacy processor integrations) |

### 10.3 Processor Documentation

| Processor | Integration Documentation |
|-----------|---------------------------|
| Stripe | Stripe API Reference (v2023-08-01), Stripe Connect Platform Agreement |
| Adyen | Adyen API Reference (v69), Adyen Platform for Healthcare |
| JPMorgan Chase Merchant Services | JPMorgan Merchant Services Technical Specification v4.2 |

---

## 11. Revision History

| Version | Date | Author | Change Summary | Approved By |
|---------|------|--------|----------------|-------------|
| 1.0 | 2022-03-14 | Sarah Chen, Director of Payment Ops (former) | Initial release. Established foundational payment processing controls, reconciliation procedures, and PCI DSS alignment. | James Thornton, CFO |
| 1.1 | 2022-06-22 | Sarah Chen | Minor revision: Updated processor routing logic to incorporate Adyen for EU transactions. Added idempotency key requirements. | James Thornton, CFO |
| 2.0 | 2023-01-11 | Sarah Chen | Major revision: Full restructure per internal audit recommendations. Added SR 11-7 model risk integration for medical lending models. Expanded reconciliation thresholds and escalation procedures. Introduced CDE network segmentation architecture. Updated all processor API references. Full team retraining required. | James Thornton, CFO; Rachel Kim, CISO |
| 2.3 | 2023-08-30 | David Okonkwo, Interim Director of Payment Ops | Minor revision: Updated sanctions screening vendor from World-Check to LexisNexis Bridger. Adjusted Tier 2 exception resolution SLA from 36 to 48 hours based on operational metrics review. Added SEPA instant credit transfer support. | James Thornton, CFO |
| 2.5 | 2024-04-15 | David Okonkwo | Minor revision: Reconciliations schema update in Snowflake. Jira Service Management project consolidation (PAY-RECON moved from separate project to unified project). Added role for Customer Operations (Michael Chang) in SLA definition. Updated chargeback win rate target from 60% to 65%. | James Thornton, CFO; Robert Liu, VP Financial Services |
| 2.6 | 2025-05-09 | Robert Liu, VP Financial Services | Minor revision: Updated annual processing volume from $3.8B to $4.2B. Adjusted dual authorization thresholds for inflation (increased $100K tier to $250K, $500K to $1M). Updated Stripe API version. Added new team structure (8 FTE, 24/7 coverage). Revised encryption standards (AES-256-GCM). Updated access provisioning process. | James Thornton, CFO |
| 2.7 | 2025-10-09 | Robert Liu, VP Financial Services | Minor revision: Comprehensive review cycle. Updated effective date, reviewed all role assignments for personnel changes. Updated related policies cross-references (SOP-IS-035, SOP-MDL-001). Added continuous monitoring section (7.3). Added training compliance tracking details. Revised RACI matrix for Engineering Lead role. Added 72-hour idempotency window specification. Updated PCI DSS reference to v4.0.1. Enhanced transaction logging schema with processor reference ID and state transition details. | James Thornton, CFO |

---

**End of Document — SOP-FIN-003 Version 2.7**

*Document classification: Internal. Do not distribute outside of Meridian Health Technologies, Inc. without written authorization from the Chief Financial Officer or Chief Compliance Officer.*
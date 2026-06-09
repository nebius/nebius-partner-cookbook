---
sop_id: "SOP-FIN-013"
title: "Financial Data Reconciliation"
business_unit: "Financial Services"
version: "4.7"
effective_date: "2024-04-01"
last_reviewed: "2025-07-19"
next_review: "2026-01-08"
owner: "Robert Liu, VP of Financial Services"
approver: "James Thornton, Chief Financial Officer"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Financial Data Reconciliation

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the mandatory framework for reconciling financial data across all Meridian Health Technologies, Inc. financial systems, payment platforms, and general ledger accounts. The purpose of this document is to ensure the completeness, accuracy, and integrity of financial transaction data processed through the HealthPay Financial Services platform, thereby supporting reliable financial reporting, regulatory compliance, and operational excellence.

This SOP defines standardized reconciliation procedures, materiality thresholds, break resolution protocols, and audit trail requirements to mitigate risks associated with financial data discrepancies, unauthorized transactions, processing errors, and fraudulent activity.

### 1.2 Scope

This SOP applies to all financial data reconciliation activities performed by or on behalf of Meridian Health Technologies, Inc., including:

| In-Scope Activities | Out-of-Scope Activities |
|---|---|
| Reconciliation of HealthPay payment transactions ($4.2B annual volume) | Clinical data reconciliation (see SOP-CLIN-042) |
| Settlement reconciliation with acquiring banks, payment networks, and merchant processors | Patient health record reconciliation |
| Reconciliation of medical lending disbursements and repayments | Employee expense report reconciliation (see SOP-FIN-008) |
| General ledger-to-subledger reconciliation for all Financial Services accounts | Payroll reconciliation (see SOP-HR-015) |
| Claims automation payment reconciliation between payers and providers | Inter-company reconciliation for non-Financial Services entities |
| Revenue recognition data reconciliation under ASC 606 | |
| Patient financing origination and servicing reconciliation | |
| Automated Clearing House (ACH), wire transfer, and virtual card transaction reconciliation | |
| SOC 2 control evidence generation for reconciliation processes | |

### 1.3 Applicability

This SOP applies to the following personnel and functions:

- **Financial Services Business Unit**: All employees, contractors, and third-party service providers performing reconciliation activities
- **IT Operations**: Personnel responsible for maintaining reconciliation systems and data pipelines
- **Engineering**: Teams supporting the HealthPay platform, claims automation, and data infrastructure
- **Compliance**: Personnel monitoring adherence to SOC 2, SR 11-7, and internal control requirements
- **Internal Audit**: Team members evaluating reconciliation control effectiveness
- **Third-Party Service Providers**: Any external entity performing reconciliation services on behalf of Meridian

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Break** | A discrepancy or mismatch between two or more data sources during reconciliation, where the variance exceeds the defined materiality threshold |
| **Break Resolution** | The systematic process of investigating, documenting, correcting, and closing identified breaks |
| **Four-Way Reconciliation** | The reconciliation of four distinct data points: (1) Meridian transaction records, (2) Payment network responses, (3) Bank settlement files, and (4) General ledger postings |
| **Materiality Threshold** | The quantitative dollar amount or percentage variance above which a discrepancy requires formal investigation and documentation per this SOP |
| **Reconciliation Window** | The defined time period within which a specific reconciliation cycle must be completed |
| **Settlement File** | A structured data file received from an acquiring bank, payment network, or processor containing confirmed settlement amounts for a defined period |
| **Source of Truth** | The authoritative system or data record against which reconciliation is performed; in the context of this SOP, the HealthPay transaction ledger is the primary source of truth |
| **Unexplained Variance** | A break that remains unresolved after the completion of Level 2 investigation procedures defined in Section 5.5 |
| **Zero-Balance Account (ZBA)** | A cash management account structure where end-of-day balances are automatically swept to a master concentration account |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| **ACH** | Automated Clearing House |
| **AML** | Anti-Money Laundering |
| **ASC 606** | Accounting Standards Codification Topic 606: Revenue from Contracts with Customers |
| **BSA** | Bank Secrecy Act |
| **CC** | Control Criteria |
| **CCO** | Chief Compliance Officer |
| **CFO** | Chief Financial Officer |
| **DRE** | Daily Reconciliation Exception |
| **ERP** | Enterprise Resource Planning system (NetSuite) |
| **EWI** | Early Warning Indicator |
| **GL** | General Ledger |
| **KPI** | Key Performance Indicator |
| **KRI** | Key Risk Indicator |
| **MRE** | Monthly Reconciliation Exception |
| **MTD** | Month-to-Date |
| **OFAC** | Office of Foreign Assets Control |
| **RACI** | Responsible, Accountable, Consulted, Informed |
| **RPO** | Reconciliation Policy Owner |
| **RTO** | Recovery Time Objective |
| **SLA** | Service Level Agreement |
| **SOC 2** | System and Organization Controls 2 |
| **TSYS** | Total System Services (payment processor) |
| **TXN** | Transaction |
| **VR** | Variance Report |
| **WIP** | Work in Progress |

## 3. Roles and Responsibilities

### 3.1 RACI Matrix

The following Responsibility Assignment Matrix (RACI) defines the roles and obligations for all activities governed by this SOP.

| Activity / Deliverable | Financial ReconAnalyst | Senior Recon Analyst | Recon Supervisor | FinOps Manager | VP Financial Services | IT Engineering | Compliance Officer | Internal Audit |
|---|---|---|---|---|---|---|---|---|
| Daily Transaction Reconciliation (T+1) | **R** | A | C | I | I | C | I | I |
| Four-Way Settlement Reconciliation (T+2) | A | **R** | A | C | I | C | I | I |
| Break Identification and Categorization | **R** | A | C | I | I | I | I | I |
| Level 1 Break Investigation | **R** | A | A | I | I | C | I | I |
| Level 2 Break Investigation | C | **R** | A | A | I | C | C | I |
| Escalation to Level 3 (VP Financial Services) | I | C | **R** | A | **A** | C | C | I |
| Materiality Threshold Exception Approval | I | I | C | R | **A** | I | I | C |
| Monthly GL Certification | **R** | R | A | A | I | I | I | I |
| SOC 2 Control Evidence Compilation | C | C | **R** | A | I | I | A | I |
| Reconciliation System Configuration Changes | I | I | C | R | A | **R** | I | I |
| External Audit Support | C | C | R | R | A | I | C | **R** |

**R = Responsible** (Performs the work)  
**A = Accountable** (Approves the work; single point of accountability)  
**C = Consulted** (Provides input prior to the work being completed)  
**I = Informed** (Notified of outcome after completion)

### 3.2 Named Roles

| Role Title | Current Designee | Key Responsibilities |
|---|---|---|
| VP of Financial Services | Robert Liu | Overall process ownership; escalation authority; policy approval; Level 3 break resolution oversight |
| Chief Financial Officer | James Thornton | Executive approver for policy; authority for unexplained variance write-offs exceeding $50,000 |
| FinOps Manager | [Vacant – Interim: Maria Santos] | Daily operational oversight; SLA compliance monitoring; team resource allocation; Level 2 break review |
| Recon Supervisor | Sarah Chen | Daily reconciliation review and approval; break assignment; Level 2 investigation supervision; SOC 2 evidence quality assurance |
| Senior Recon Analyst | Team of 3 FTEs | Four-way settlement reconciliation; Level 2 break investigation; month-end reconciliation package preparation |
| Financial Recon Analyst | Team of 6 FTEs | Daily transaction reconciliation; Level 1 break investigation; data entry; initial discrepancy documentation |
| Director of Compliance | Jennifer Okonkwo | SOC 2 control mapping; regulatory compliance review; exception approval consultation |
| VP of Engineering (Platform) | David Park | Reconciliation automation infrastructure; data pipeline integrity; system availability |
| Manager of Internal Audit | Priya Sharma | Independent control testing; quarterly reconciliation audit |

## 4. Policy Statements

### 4.1 Reconciliation Completeness

All financial transactions processed through the HealthPay platform shall be reconciled on a daily basis (T+1 business day for transaction counts and amounts; T+2 business days for four-way settlement reconciliation). No transaction shall remain unreconciled beyond the defined reconciliation window without a documented exception approved per Section 8.

### 4.2 Materiality Thresholds

Breaks shall be categorized and escalated according to the following quantitative materiality thresholds, which are reviewed and recalibrated annually by the VP of Financial Services in consultation with the CFO and Compliance Officer:

| Tier | Threshold (Single Transaction) | Threshold (Aggregate Daily) | Response Time | Escalation Level |
|---|---|---|---|---|
| Tier 1 – Immaterial | ≤ $10.00 per item OR ≤ $100.00 aggregate per day | ≤ $500.00 aggregate | Documented within 24 hours; resolved within 5 business days | Recon Analyst discretion |
| Tier 2 – Material | $10.01 – $500.00 per item OR $100.01 – $5,000.00 aggregate | $500.01 – $50,000.00 aggregate | Immediate documentation; resolution initiated within 4 hours | Recon Supervisor required |
| Tier 3 – Significant | $500.01 – $5,000.00 per item OR $5,000.01 – $100,000.00 aggregate | $50,000.01 – $500,000.00 aggregate | Immediate escalation; resolution initiated within 1 hour | FinOps Manager notification; VP Financial Services informed |
| Tier 4 – Critical | > $5,000.00 per item OR > $100,000.00 aggregate | > $500,000.00 aggregate | Immediate crisis protocol; escalation within 15 minutes | CFO notification required; VP Financial Services leads response |

### 4.3 Audit Trail Integrity

Every reconciliation activity, including break identification, investigation steps, resolution actions, and approvals, shall generate a complete, immutable, and timestamped audit trail stored in the Meridian Financial Reconciliation System (BlackLine). No reconciliation activity shall be performed outside of the approved system without documented exception approval. All audit trails shall be retained for a minimum of seven (7) years in accordance with Meridian's data retention policy (SOP-CORP-019).

### 4.4 Segregation of Duties

No single individual shall have the authority to both execute a material financial correction (Tier 2 or above) and approve the reconciliation that contains that correction. All corrections exceeding Tier 1 materiality shall require dual approval: the responsible Recon Analyst/Senior Recon Analyst plus the Recon Supervisor or FinOps Manager.

### 4.5 SOC 2 Control Compliance

All reconciliation procedures defined in this SOP are mapped to SOC 2 Trust Services Criteria, specifically:

- **CC5.2**: Control Activities – The design and operating effectiveness of reconciliation controls
- **CC6.1**: Logical and Physical Access Controls – Access to reconciliation systems
- **CC7.1**: System Operations – Monitoring of reconciliation system operations
- **CC8.1**: Change Management – Authorized changes to reconciliation rules and thresholds

Evidence of control operation, including system-generated reconciliation reports, break resolution logs, and exception approvals, shall be compiled monthly by the Recon Supervisor and reviewed by the Compliance Officer prior to inclusion in the SOC 2 control evidence package.

### 4.6 System Availability and Data Integrity

IT Engineering shall maintain the reconciliation data pipeline with a Service Level Objective (SLO) of 99.9% availability for daily reconciliation file delivery. Any failure of automated data feeds shall trigger the manual reconciliation procedures defined in Section 5.9. Data integrity validation checks shall be embedded at each data ingestion point to prevent corrupted or incomplete datasets from entering the reconciliation workflow.

## 5. Detailed Procedures

### 5.1 Daily Transaction Reconciliation (T+1)

The Daily Transaction Reconciliation is performed every business day for the previous business day's transaction activity ("T" day reconciled on "T+1").

#### 5.1.1 Prerequisites

- Access credentials to BlackLine Reconciliation Module (validated via Okta SSO)
- Successful overnight batch processing confirmed by IT Operations monitoring dashboard (Datadog alert cleared)
- Availability of transaction extract from HealthPay Core Transaction Engine (CTE) via the `fin_ops.txn_extract` API endpoint
- Availability of payment gateway settlement summary from Chase Paymentech, Stripe, and Adyen portals

#### 5.1.2 Procedure Steps

**Step 1: Retrieve HealthPay Transaction Extract**

1. Navigate to the Meridian Financial Data Hub (Snowflake instance: `MERIDIAN_FINANCE.PROD.TRANSACTIONS`)
2. Execute query `EXECUTE SP_GET_DAILY_TXN_EXTRACT @TXN_DATE = '{T_DATE}'` where `{T_DATE}` is the prior business day in `YYYY-MM-DD` format
3. Export results to CSV format with the following columns: `transaction_id`, `merchant_id`, `payment_method`, `transaction_amount`, `fee_amount`, `net_amount`, `transaction_type`, `origination_timestamp`, `settlement_batch_id`
4. Save file to `\\meridian-fin-fs01\Reconciliation\Daily\T+1\Source\{YYYY-MM}\TXN_Extract_{YYYY-MM-DD}.csv`
5. Import CSV into BlackLine via the Data Import Module → Transaction Reconciliation → Load Source Data

**Step 2: Retrieve Gateway Settlement Summary**

1. Access each payment gateway portal using the stored credentials in HashiCorp Vault (path: `secret/finance/gateways/{gateway_name}`)
2. For each gateway, download the prior day's settlement summary report in CSV format
3. Standardize each gateway report to the Meridian Settlement Schema using the transformation mappings defined in Appendix A
4. Import standardized settlement files into BlackLine → Transaction Reconciliation → Load Comparison Data

**Step 3: Execute Automated Matching**

1. In BlackLine, navigate to Transaction Reconciliation → Run Matching → Select Profile: "Daily T+1 Standard"
2. Configure matching parameters:
   - Match Key: `transaction_id` (exact match)
   - Amount Tolerance: ± $0.01 (to account for rounding differences)
   - Date Window: -1 to +0 business days (allows for same-day processing variance)
3. Click "Run Matching"
4. Monitor job completion status; expected runtime ≤ 15 minutes for daily volume (~250,000 transactions)
5. Upon completion, review the Reconciliation Summary Report which categorizes transactions as:
   - **Matched**: HealthPay amount equals gateway settlement amount within tolerance
   - **Unmatched – Missing Gateway**: Transaction exists in HealthPay but not in gateway settlement
   - **Unmatched – Missing HealthPay**: Transaction exists in gateway settlement but not in HealthPay
   - **Unmatched – Amount Variance**: Both records exist but amounts differ beyond tolerance
   - **Duplicates**: Multiple identical transactions detected

**Step 4: Review and Document Unmatched Items**

1. Export all unmatched items to the Daily Reconciliation Exception (DRE) Log
2. Categorize each exception using the standard break categories defined in Section 5.4.1
3. For Tier 1 immaterial items ($10.00 or below per item), the Recon Analyst may:
   - Document the variance in the DRE Log with a brief explanation note
   - Apply the automatic "Rounding Variance" categorization if the discrepancy is ≤ $0.05
   - Close the item without formal investigation if the aggregate impact is below $100.00
4. For all items exceeding Tier 1 thresholds, initiate Break Resolution per Section 5.4

**Step 5: Sign-Off**

1. Complete the Daily Reconciliation Checklist (Form FIN-REC-001) in SharePoint
2. Attach the Reconciliation Summary Report (PDF export from BlackLine)
3. Electronically sign the checklist
4. Route to Recon Supervisor for review and approval by 14:00 local time on T+1

### 5.2 Four-Way Settlement Reconciliation (T+2)

The Four-Way Settlement Reconciliation is the core control ensuring that all financial flows are fully accounted for across Meridian's systems, payment network processors, banking partners, and the general ledger.

#### 5.2.1 Four Data Sources

| Source ID | Data Source | Description | Typical Availability |
|---|---|---|---|
| S1 | HealthPay Transaction Ledger | Meridian's internal system of record for all transactions initiated or processed | Real-time; T+0 overnight batch complete by 04:00 ET |
| S2 | Payment Network / Gateway Settlement Reports | Confirmation of transaction processing and net settlement from Chase Paymentech, Stripe, Adyen | Available by 08:00 ET T+1 |
| S3 | Bank Settlement Files (BAI2 format) | Actual funds movement confirmation from JPMorgan Chase, Silicon Valley Bank (First Citizens), Bank of America | Available by 06:00 ET T+2 (BAI2 files via SFTP) |
| S4 | General Ledger Postings (NetSuite) | Actual journal entries posted to the GL for the reconciliation period | Subledger sync complete by 02:00 ET T+2; manual JE posting by 10:00 ET T+3 |

#### 5.2.2 Reconciliation Matching Logic

The Four-Way Reconciliation applies the following matching logic chain:

**Chain 1: Transaction Completeness (S1 ↔ S2)**
- Match: All S1 transactions should have a corresponding settlement confirmation in S2
- Variance indicates: Unsettled transactions, gateway processing errors, or data feed interruptions

**Chain 2: Settlement Funding (S2 ↔ S3)**
- Match: Net settlement amounts reported in S2 should equal actual funds received in S3 per bank statement
- Variance indicates: Funding delays, bank processing errors, fees not accounted for, or misdirected funds

**Chain 3: Financial Recording (S3 ↔ S4)**
- Match: Cash entries in S3 should have corresponding journal entries in S4 for the correct accounts and amounts
- Variance indicates: GL coding errors, timing differences in accruals, or unposted activity

**Chain 4: End-to-End Integrity (S1 ↔ S4)**
- Validation: Originating transaction amounts in S1 should ultimately be reflected in corresponding revenue (or liability) GL accounts in S4, net of known fees and adjustments
- Variance indicates: Systemic processing errors, revenue recognition issues, or unauthorized adjustments

#### 5.2.3 Procedure Steps

**Step 1: Data Ingestion and Validation**

1. Confirm availability of all four data sources per the availability schedule in Section 5.2.1
2. If any source is unavailable, log a Severity 2 (Sev2) incident ticket in ServiceNow → Assignment Group: "FinOps-DataPipeline" and initiate manual data retrieval per Section 5.9
3. Validate file integrity:
   - File size deviation: Warn if current file size is > 20% different from 30-day rolling average
   - Record count deviation: Warn if record count is > 10% different from expected based on prior day's HealthPay volumes
   - Hash verification: Validate SHA-256 checksum against expected value where provided by upstream systems

**Step 2: Execute BlackLine Four-Way Reconciliation**

1. In BlackLine, navigate to Reconciliation → Complex Reconciliation → Create New Job
2. Select Profile: "Four-Way Settlement – Daily"
3. Configure Data Sources: Load S1 through S4 datasets
4. Set matching rules:
   - Chain 1 (S1↔S2): Match on `transaction_id`; validate amount, currency, timestamp
   - Chain 2 (S2↔S3): Match on `batch_settlement_id`; validate net settlement amount by currency by merchant account
   - Chain 3 (S3↔S4): Match on bank account and GL account code; validate amounts and effective dates
5. Execute matching job
6. Upon completion (expected runtime ≤ 45 minutes), review the Four-Way Reconciliation Dashboard

**Step 3: Analyze Chain Breaks**

For each break identified in each chain, perform root cause analysis:

| Chain | Common Break Causes | Investigation Priority |
|---|---|---|
| Chain 1 (S1↔S2) | Gateway timeouts, batch processing failures, merchant ID misconfiguration | High – indicates unprocessed or lost transactions |
| Chain 2 (S2↔S3) | Processing fee variance, intermediary bank fees, wire transfer delays, settlement timing (weekend/holiday) | Medium – indicates funding discrepancy |
| Chain 3 (S3↔S4) | Chart of accounts mapping error, manual journal entry not posted, suspense account not cleared | Medium – indicates GL discrepancy |
| Chain 4 (S1↔S4) | End-to-end reconciliation break flag; typically a cascading error from Chain 1-3 breaks | Critical – indicates systemic issue |

**Step 4: Prepare Four-Way Reconciliation Package**

1. Generate the Daily Four-Way Reconciliation Report from BlackLine
2. Compile supporting documentation:
   - Gateway settlement reports (S2 PDF/CSV extracts)
   - BAI2 bank file import confirmation and cash ledger screenshots
   - NetSuite GL account balance screenshots (S4)
   - Completed break investigation reports for any Tier 2+ items
3. Complete Form FIN-REC-002 (Four-Way Settlement Reconciliation Sign-Off)
4. Submit package to Recon Supervisor for approval by 16:00 ET on T+2

### 5.3 Periodic Reconciliation Procedures

#### 5.3.1 Weekly Reconciliation

In addition to daily procedures, every Monday the following weekly reconciliation tasks shall be completed for the prior week (Monday through Sunday):

| Task | Description | Responsibility | Deadline |
|---|---|---|---|
| W-1 | Reconcile all ZBA sweep accounts to concentration account | Senior Recon Analyst | Monday 14:00 ET |
| W-2 | Review all open breaks older than 3 business days and escalate any without active resolution plans | Recon Supervisor | Monday 16:00 ET |
| W-3 | Reconcile provider settlement payments against claim adjudication data for the HealthPay Claims module | Financial Recon Analyst (2-person team) | Monday 18:00 ET |
| W-4 | Review and approve all DRE Log entries from prior week | Recon Supervisor | Wednesday 12:00 ET |

#### 5.3.2 Month-End Close Reconciliation

Month-end reconciliation procedures shall commence on the first business day following month-end ("ME+1") and conclude no later than the fifth business day ("ME+5").

| Close Day | Activity | Owner |
|---|---|---|
| ME+1 | All daily reconciliations for final business day of month completed and signed off | Recon Analyst Team |
| ME+1 | Cut-off validation: Confirm all month-end transactions are posted to the correct period | Recon Supervisor |
| ME+2 | Month-end Four-Way Reconciliation executed covering entire calendar month | Senior Recon Analyst |
| ME+2 | All open breaks reviewed; Tier 3+ breaks escalated to FinOps Manager with resolution plans | Recon Supervisor |
| ME+3 | Preliminary GL account reconciliations completed for all Financial Services balance sheet accounts (Cash, Settlement Receivable, Provider Payable, Patient Receivable, Revenue) | Senior Recon Analyst |
| ME+4 | Month-end Financial Services reconciliation package prepared (Form FIN-REC-003) | FinOps Manager |
| ME+4 | SOC 2 control evidence compiled for all reconciliation controls operated during the month | Recon Supervisor |
| ME+5 | Month-end reconciliation package reviewed and approved by VP of Financial Services | Robert Liu |
| ME+5 | Approved package submitted to Corporate Controller for GL close | FinOps Manager |

#### 5.3.3 Quarterly Reconciliation Certification

Within 15 business days of quarter-end, the VP of Financial Services shall certify in writing to the CFO and the Audit Committee Chair that:

1. All material reconciliation breaks have been resolved or adequately reserved
2. Reconciliation controls operated effectively throughout the quarter, or any control deficiencies have been documented and remediated
3. The quarterly Financial Services balance sheet is fully substantiated by reconciliation evidence

### 5.4 Break Resolution Procedures

#### 5.4.1 Break Categorization

All breaks shall be categorized upon identification using the following taxonomy:

| Break Category Code | Category | Description | Example |
|---|---|---|---|
| **BRK-TIMING** | Timing Difference | Legitimate transaction processed in different accounting periods | Transaction initiated 23:50 ET on month-end, gateway settlement next day |
| **BRK-FEE** | Fee Variance | Processing, interchange, or gateway fees not correctly applied or predicted | Estimated fee in HealthPay differs from actual fee in settlement file |
| **BRK-DATA** | Data Error | Incorrect data entry, mapping error, or file corruption | Merchant ID misconfigured; settlement sent to wrong account |
| **BRK-SYS** | System Error | Platform bug, batch processing failure, or integration error | Duplicate transaction due to retry logic failure |
| **BRK-FRAUD** | Suspected Fraud | Transaction pattern suggesting unauthorized activity | Unusual spike in high-value patient payments; potential card testing |
| **BRK-UNK** | Unknown | Break not classifiable into above categories after Level 1 investigation | Requires Level 2 escalation |
| **BRK-BANK** | Bank Processing Error | Error attributable to acquiring bank or payment network | Incorrect settlement amount from network; duplicate batch file |

#### 5.4.2 Level 1 Investigation (Initial Diagnosis)

**Responsibility**: Financial Recon Analyst  
**Timeframe**: Within 4 hours of break identification for Tier 2+; within 24 hours for Tier 1

**Procedure**:

1. Document the break in the Break Resolution Tracker (Jira project: `FIN-BREAK`) with:
   - Break ID (auto-generated format: `FIN-BRK-{YYYY}-{NNNNN}`)
   - Source data references (S1-S4 identifiers)
   - Break Category Code
   - Tier classification
   - Initial findings

2. Perform the following diagnostic steps:
   - **Trace the transaction end-to-end**: Follow the transaction ID across all systems
   - **Check system logs**: Review application logs in Splunk (`index=healthpay_prod`) for errors or warnings associated with the transaction during the reconciliation period
   - **Verify batch processing**: Confirm the transaction was included in the correct settlement batch per HealthPay records
   - **Check for duplicate transactions**: Search for identical or near-identical transactions within a ±5 minute window
   - **Validate configuration**: Verify merchant ID, gateway routing, and account mapping configurations in the HealthPay Admin Console

3. If root cause is identified and correction can be applied per authorized procedures:
   - Document root cause in Jira ticket
   - Apply correction (e.g., manual data fix in BlackLine, reprocessing instruction to Engineering)
   - Verify correction resolves the break by re-running the affected reconciliation chain
   - Close the Jira ticket with Root Cause Analysis (RCA) summary

4. If root cause is NOT identified within the Level 1 timeframe:
   - Escalate to Level 2 investigation
   - Notify Recon Supervisor
   - Maintain Jira ticket in "Under Investigation" status

#### 5.4.3 Level 2 Investigation (Deep Dive)

**Responsibility**: Senior Recon Analyst (assigned by Recon Supervisor)  
**Timeframe**: Investigation plan within 2 hours of escalation; resolution target within 24 hours of escalation

**Procedure**:

1. Accept escalation in Jira; acknowledge assignment and estimated time to resolution
2. Assemble cross-functional investigation team as needed:
   - IT Engineering: If system logs indicate platform issue
   - Payment Network Relationship Manager: If gateway-reported issue
   - Bank Relationship Manager: If settlement file discrepancy
   - Compliance Officer: If fraud indicators present (category BRK-FRAUD)

3. Perform deep-dive diagnostic:
   - **Full transaction lifecycle trace**: From patient/provider initiation through to settlement and GL posting, using all available system logs, database records, and audit tables
   - **Network trace**: Request gateway processing logs from payment network for specific transaction ID(s)
   - **Bank communication**: If S2↔S3 break, contact bank operations to verify settlement file accuracy and confirm actual funds received
   - **Code review**: If S1↔S2 break recurring, request Engineering to review transaction processing code for the affected pathway

4. Document findings in the Break Resolution Tracker (Jira) with detailed technical explanation
5. Propose resolution:
   - **System fix**: If root cause is a software defect, create a Sev3 Engineering ticket with reproduction steps
   - **Configuration change**: If misconfiguration, submit Change Request per Meridian Change Management Policy (SOP-IT-007)
   - **Manual correction**: If one-time data correction needed, prepare correction journal entry or system adjustment with full justification
6. Obtain approval from Recon Supervisor before implementing any corrective action affecting financial records
7. Implement approved resolution
8. Re-run affected reconciliation to confirm break resolution
9. Close Jira ticket with comprehensive RCA document attached

#### 5.4.4 Level 3 Escalation (Critical Breaks)

**Criteria for Level 3 Escalation**:
- Single break exceeding Tier 3 threshold ($5,000.01+ per item or $50,000.01+ aggregate)
- Any break categorized as BRK-FRAUD regardless of dollar amount
- Any break unresolved after 48 hours from initial identification
- Systemic break affecting >1,000 transactions in a single day
- Notification from a payment network or bank of a settlement irregularity affecting Meridian

**Procedure**:

1. Recon Supervisor immediately (within 15 minutes) notifies:
   - FinOps Manager (Maria Santos, Interim)
   - VP of Financial Services (Robert Liu)
   - Director of Compliance (Jennifer Okonkwo) – if fraud or regulatory concern
   - VP of Engineering (David Park) – if system-related

2. VP of Financial Services or FinOps Manager declares "Critical Break Incident" and convenes a Critical Incident Response Team via the PagerDuty `fin-critical-break` escalation policy

3. Critical Incident Response:
   - **Containment**: Within 1 hour, determine if active transaction processing should be paused or if specific payment pathways should be disabled (authority: VP Financial Services)
   - **Investigation**: Senior Recon Analyst leads with direct Engineering and Bank support
   - **Client Impact Assessment**: If the break potentially impacts client funds (provider disbursements, patient refunds), the FinOps Manager coordinates with Client Services to assess and prepare client communications
   - **Regulatory Assessment**: Compliance Officer evaluates whether the incident triggers any regulatory notification obligations
   - **Resolution**: Target resolution within 4 hours of Critical Break declaration; if not achievable, publish a status update every 2 hours with revised ETA

4. Post-Incident Review (PIR):
   - Within 5 business days of resolution, the VP of Financial Services conducts a formal PIR
   - PIR document includes: timeline, root cause, impact quantification, remediation actions, control gaps identified, and preventative measures
   - PIR presented to CFO and discussed with Internal Audit

### 5.5 Journal Entry Reconciliation

All manual journal entries (JEs) posted to correct reconciliation breaks or to record period-end adjustments shall themselves be reconciled.

1. **JE Pre-Posting Validation**: Before posting any correction JE exceeding $1,000.00, the preparer shall complete the JE Validation Checklist (Form FIN-REC-010) which includes:
   - Identification of the specific break(s) being corrected (Jira ticket IDs)
   - Calculation demonstrating how the JE corrects the break
   - Confirmation that the correction does not create a new break in a downstream reconciliation
   - Independent review by Recon Supervisor or FinOps Manager (segregation of duties)

2. **JE Post-Posting Reconciliation**: Within 2 business days of posting, a Recon Analyst (different from the preparer) shall:
   - Verify the JE posted correctly to NetSuite
   - Re-run the affected reconciliation chain to confirm the break is resolved
   - Document the JE and verification in the corresponding Jira ticket

3. **Month-End JE Review**: As part of month-end close (Section 5.3.2), the FinOps Manager shall review all manual JEs posted during the month affecting Financial Services accounts. Any JE exceeding $25,000.00 shall be separately itemized in the month-end reconciliation package.

### 5.6 Provider Settlement Reconciliation

For HealthPay's claims automation and provider settlement functionality, additional reconciliation procedures apply:

1. **Daily Provider Settlement Reconciliation**:
   - Match the total dollar amount of claims adjudicated and approved for payment against the total provider settlement disbursements initiated
   - Identify any adjudicated claims not included in the settlement run (e.g., held for review, minimum threshold not met)
   - Verify settlement file transmitted to originating bank against total approved claims

2. **Provider Settlement Error Handling**:
   - Failed disbursements (ACH returns, invalid account) shall be identified same-day via bank return file reconciliation
   - Recon Analyst shall create a Provider Settlement Exception case in Salesforce (`Provider Finance` queue) within 2 hours of identifying a failed disbursement
   - Provider re-engagement for correct banking details shall be initiated by Provider Services within 1 business day

### 5.7 Patient Payment Reconciliation

For patient-facing payment transactions (co-pay, deductible, portal payments):

1. **Daily Patient Payment Reconciliation**:
   - Reconcile patient payment transactions in HealthPay against the patient ledger in the clinical system (Epic MyChart) to ensure payments are correctly credited to patient accounts
   - Interface reconciliation: Validate the HealthPay-to-Epic integration file transmitted daily at 03:00 ET processed successfully

2. **Unapplied Cash Monitoring**:
   - The Recon Supervisor shall review the Unapplied Cash Report daily
   - Any patient payment remaining unapplied for >3 business days shall be escalated to the Revenue Cycle Operations team (SOP-RCM-022) with a target resolution of 5 business days

### 5.8 ASC 606 Revenue Recognition Reconciliation

To support accurate revenue recognition under ASC 606 for the Financial Services business unit:

1. **Monthly Revenue Reconciliation**:
   - Reconcile transaction-level revenue calculated in HealthPay (fees, interchange margin, service fees) against revenue posted to the GL
   - Validate variable consideration estimates (provider rebates, volume incentives) against actuals as data becomes available
   - Document any constrained revenue or uncertain collection positions

2. **Contract Cost Reconciliation**:
   - Amortization of deferred contract costs (sales commissions for HealthPay platform sales) shall be reconciled monthly against the contract cost asset schedule maintained in NetSuite

### 5.9 Manual Reconciliation Procedures (System Outage Contingency)

In the event that BlackLine or a critical upstream data source is unavailable preventing automated reconciliation, the following manual procedures shall be enacted:

1. **Outage Declaration**: Recon Supervisor or FinOps Manager declares a "Reconciliation System Outage" upon confirmation that a critical system is unavailable with an estimated RTO exceeding 2 hours

2. **Manual Data Extraction**:
   - HealthPay data: Run the `TXN_EXTRACT_EMERGENCY.sql` query directly against the HealthPay read replica database (contact DBA on-call via PagerDuty `dba-emergency`)
   - Payment gateway data: Manually download CSV reports from each gateway portal
   - Bank data: Contact JPMorgan Chase Treasury Services (phone: 1-800-XXX-XXXX) to request a manual prior-day BAI2 file emailed to `finops-emergency@meridianhealth.com`
   - GL data: Access NetSuite directly; run saved search "Month to Date Cash Postings – Financial Services"

3. **Manual Reconciliation Execution**:
   - Use the Financial Data Reconciliation Emergency Workbook (`\\meridian-fin-fs01\Reconciliation\Emergency\FIN-REC-Emergency-Workbook_v4.7.xlsm`)
   - Workbook contains pre-built pivot tables and VLOOKUP logic mirroring BlackLine matching rules
   - Perform Step 1 (import HealthPay extract), Step 2 (import gateway summaries), Step 3 (execute matching via pivot table comparison)
   - All manual reconciliation actions must be documented with timestamp, performer name, and explicit cross-references to source data files used

4. **Post-Outage Catch-Up**:
   - Upon system restoration, all manual reconciliations shall be re-entered into BlackLine to create system of record evidence
   - A reconciliation of the manual period to the automated period must be performed to ensure no gaps exist during the transition
   - The outage and manual procedures shall be documented in a Post-Outage Report filed in the Jira `FIN-OUTAGE` project

## 6. Controls and Safeguards

### 6.1 SOC 2 Control Mapping

The following table maps the specific reconciliation controls mandated by this SOP to the applicable SOC 2 Trust Services Criteria (TSC) 2017, as referenced in the Meridian SOC 2 Type II audit scope for the HealthPay system:

| Control ID | Control Description | SOC 2 TSC Reference | Control Type | Frequency | Evidence Source |
|---|---|---|---|---|---|
| **FIN-REC-C01** | All financial transactions are reconciled daily between HealthPay transaction ledger and payment gateway settlement reports. | CC5.2 (Control Activities) – Management has control activities to meet objectives | Automated with Manual Review | Daily | BlackLine Daily Reconciliation Report; DRE Log sign-off |
| **FIN-REC-C02** | Four-way settlement reconciliation performed on T+2 covering all four data sources (HealthPay, Gateway, Bank, GL). | CC5.2, CC7.2 (System Operations – Detection of processing anomalies) | Manual | Daily (T+2) | BlackLine Four-Way Reconciliation Report; Form FIN-REC-002 |
| **FIN-REC-C03** | All reconciliation breaks are categorized, investigated, and resolved per defined materiality tiers and SLAs. | CC5.2, CC7.2 | Manual | Per break | Break Resolution Tracker (Jira); Jira RCA documents |
| **FIN-REC-C04** | Segregation of duties enforced for material financial corrections: preparer and approver must be different individuals. | CC5.2 (Segregation of Duties) | Preventive – Manual Validation | Per correction | JE Validation Checklist (Form FIN-REC-010) showing preparer ≠ approver |
| **FIN-REC-C05** | Access to reconciliation systems (BlackLine, NetSuite, bank portals) is restricted to authorized personnel based on role, and access is reviewed quarterly. | CC6.1 (Logical Access Controls) – User access provisioning and review | Preventive – Technical | Provisioning: On change; Review: Quarterly | Okta group membership report; Quarterly Access Review sign-off (see SOP-IT-004) |
| **FIN-REC-C06** | Automated reconciliation data feeds are monitored for completeness and timeliness; failures generate alerts and trigger manual procedures. | CC7.1 (System Operations – Monitoring), CC7.2 | Detective – Automated | Continuous | Datadog monitoring dashboard; PagerDuty alert logs |
| **FIN-REC-C07** | Changes to reconciliation rules (matching logic, tolerances), materiality thresholds, or the BlackLine configuration are subject to formal change management approval and testing. | CC8.1 (Change Management) – Authorized changes | Preventive – Manual | Change Request tickets (Jira `FIN-CHG` project); Change Advisory Board (CAB) approval records |
| **FIN-REC-C08** | Monthly GL-to-subledger reconciliation performed and reviewed by FinOps Manager; evidence retained for SOC 2 package. | CC5.2 | Manual | Monthly | Month-End Reconciliation Package (Form FIN-REC-003) |
| **FIN-REC-C09** | Unapplied cash (patient payments) monitored daily; items >3 days escalated. | CC5.2, CC7.2 | Detective – Manual Review | Daily | Unapplied Cash Report; escalation email logs |
| **FIN-REC-C10** | Quarterly reconciliation certification provided by VP of Financial Services to CFO and Audit Committee attesting to reconciliation completeness and control effectiveness. | CC5.3 (Monitoring of Controls) | Manual | Quarterly | Signed Quarterly Certification Letter |

### 6.2 Access Controls

1. **BlackLine Access**:
   - Access is provisioned via Okta SSO with Multi-Factor Authentication (MFA) required
   - Role-Based Access Control (RBAC) configured in BlackLine:
     - **Reconciliation Preparer**: Financial Recon Analyst, Senior Recon Analyst; can execute reconciliations, create breaks, propose resolutions
     - **Reconciliation Approver**: Recon Supervisor, FinOps Manager; can approve reconciliations, approve break resolutions, run reports
     - **Reconciliation Administrator**: VP of Financial Services (limited), BlackLine System Administrator; can modify matching rules, tolerances, and system configuration (requires separate CAB approval)
   - Access reviews conducted quarterly per SOP-IT-004 (Access Management)

2. **Bank Portal Access**:
   - Access to JPMorgan Chase, SVB, and Bank of America corporate portals is restricted to named individuals in the Financial Services team
   - Portal entitlements configured to read-only (report download) for Recon Analysts; payment initiation limited to Treasury team per SOP-TREAS-001
   - Dual approval required for any bank portal administrative changes

3. **NetSuite GL Access**:
   - Recon Analysts have "Reconciliation View" role: Read-only access to GL balances, JE detail, and account activity for Financial Services accounts
   - JE posting access restricted to Accounting team per segregation of duties

### 6.3 Data Integrity Controls

1. **File Validation at Ingestion**:
   - All inbound reconciliation files are subjected to automated integrity checks before loading into BlackLine:
     - File format validation (expected schema, column count, data types)
     - Record count vs. expected range
     - Control total (sum of transaction amounts) matched against header trailer record
     - No duplicate file processing (file hash check against previously processed files)

2. **Reconciliation Logging**:
   - All reconciliation activities in BlackLine generate an immutable audit log entry including: user ID, timestamp, action performed, before/after values (for corrections)
   - Audit logs are retained for 7 years and are not modifiable by any user

3. **Data Pipeline Monitoring**:
   - IT Engineering monitors the `fin-ops-data-pipeline` service health via Datadog
   - Alerts configured for:
     - File delivery delay > 30 minutes past expected arrival time
     - File processing failure
     - Record count anomaly > 15% deviation from 30-day average
   - Alerts routed to `#finops-data-alerts` Slack channel and to the FinOps on-call PagerDuty schedule

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| KPI ID | Metric | Target | Measurement Method | Reporting Frequency |
|---|---|---|---|---|
| KPI-01 | Daily Reconciliation Completion Rate | 100% of business days | % of days where T+1 reconciliation completed by 14:00 ET cutoff | Weekly |
| KPI-02 | Four-Way Reconciliation Timeliness | 100% completed by T+2 18:00 ET | % of four-way reconciliations completed by deadline | Weekly |
| KPI-03 | Break Resolution SLA Adherence | ≥ 95% of breaks resolved within tier-defined SLA | (Breaks resolved within SLA / Total breaks identified) × 100 | Weekly |
| KPI-04 | Aged Open Breaks (>5 business days) | ≤ 5 open at any time | Count of Jira tickets in "Under Investigation" or "Open" status with age >5 business days | Daily |
| KPI-05 | Unreconciled Transaction Rate | ≤ 0.01% of total monthly transaction volume | (Number of unreconciled transactions / Total transactions) × 100 | Monthly |
| KPI-06 | Manual JE Volume (indicator of process quality) | ≤ 10 manual correction JEs per month | Count of manual JEs posted with category "Reconciliation Correction" | Monthly |

### 7.2 Key Risk Indicators (KRIs)

| KRI ID | Risk Indicator | Amber Threshold | Red Threshold | Action on Breach |
|---|---|---|---|---|
| KRI-01 | Unexplained variance as % of transaction volume | > 0.005% | > 0.02% | Immediate Level 2 investigation for all contributing breaks; FinOps Manager review |
| KRI-02 | Consecutive days with at least one Tier 3+ break | 3 consecutive days | 5 consecutive days | VP Financial Services initiates systemic issue investigation |
| KRI-03 | Month-end unreconciled balance in suspense account FIN-9999 | > $25,000 | > $100,000 | CFO notification; remediation plan within 5 business days |
| KRI-04 | Overdue SOC 2 control evidence | 1 control, 1 month overdue | Any control, 2+ months overdue | Compliance Officer escalation; Internal Audit notification |
| KRI-05 | BlackLine system unavailability (hours in month) | > 2 hours | > 8 hours | IT Sev1 incident; manual reconciliation contingency invoked |

### 7.3 Dashboards and Reports

1. **Daily Reconciliation Dashboard** (BlackLine):
   - Real-time display of daily reconciliation progress, breaks identified by tier, and aging summary
   - Accessed by all Financial Services staff and reviewed at the 09:00 ET daily stand-up

2. **Weekly Reconciliation Operations Report**:
   - Prepared by Recon Supervisor every Monday by 12:00 ET
   - Contains: Prior week KPI metrics, all open breaks with aging, notable incidents, resource allocation issues
   - Distributed to: FinOps Manager, VP Financial Services, Compliance Officer

3. **Monthly Financial Services Control Report**:
   - Prepared by FinOps Manager by ME+10
   - Contains: Full month KPI/KRI dashboard, month-end reconciliation summary, SOC 2 control operation attestation for the month, material break summary (Tier 3+ items), outstanding remediation actions
   - Distributed to: VP Financial Services, CFO, Corporate Controller, Director of Compliance, Manager of Internal Audit

4. **Quarterly Reconciliation Certification Package**:
   - Prepared by VP of Financial Services
   - Contains: Quarterly KPI/KRI trends, quarterly break summary, control effectiveness evaluation, certification statement, open remediation items from prior periods
   - Presented to: CFO, Audit Committee Chair

### 7.4 SOC 2 Evidence Reporting

Monthly compilation of SOC 2 control evidence:

1. Recon Supervisor runs the "SOC 2 Evidence Export" report in BlackLine for the calendar month
2. Evidence package includes, per control:
   - **FIN-REC-C01**: Daily Reconciliation Summary Reports (30/31 days)
   - **FIN-REC-C02**: Four-Way Settlement Reconciliation Reports (30/31 days)
   - **FIN-REC-C03**: Break Resolution Tracker export (all breaks, with status and resolution timestamps)
   - **FIN-REC-C04**: Approved JE Validation Checklists (sample: all JEs > $5,000)
   - **FIN-REC-C05**: Quarterly Access Review sign-off document
   - **FIN-REC-C07**: Approved Change Requests affecting reconciliation systems
   - **FIN-REC-C08**: Month-End Reconciliation Packages (current and prior month for roll-forward)
   - **FIN-REC-C10**: Latest Quarterly Certification Letter

3. Evidence package reviewed by Compliance Officer for completeness and control adherence
4. Approved package transmitted to external SOC 2 auditors via secure portal within 15 business days of month-end

## 8. Exception Handling and Escalation

### 8.1 Reconciliation Deadline Exceptions

If a reconciliation cannot be completed by the prescribed deadline due to extenuating circumstances (system outage, missing data, resource unavailability):

1. **Notification**: Responsible party notifies Recon Supervisor immediately upon determining deadline will be missed
2. **Exception Documentation**: Create a Reconciliation Exception Request in the Jira project `FIN-EXCEPTION` including:
   - Reconciliation type and affected period
   - Reason for delay
   - Estimated completion time/date
   - Interim compensating controls being applied (e.g., manual monitoring of transaction flow)
3. **Approval**:
   - Delay ≤ 4 hours: Recon Supervisor approval
   - Delay ≤ 24 hours: FinOps Manager approval
   - Delay > 24 hours: VP of Financial Services approval; CFO informed
4. **Tracking**: All approved exceptions are logged in the Reconciliation Exception Register maintained by the Recon Supervisor; register reviewed monthly by FinOps Manager for recurring patterns

### 8.2 Materiality Threshold Exception

In specific circumstances, a break meeting Tier 2+ materiality may be treated as immaterial for reconciliation purposes if:

1. The break is definitively categorized as BRK-TIMING (timing difference that will self-resolve in the next reconciliation cycle)
2. The dollar amount is fully explainable and documented
3. The aggregate impact of all such exceptions does not exceed $5,000.00 at any time

**Exception Process**:
1. Recon Supervisor prepares a Materiality Exception Form (Form FIN-REC-020) documenting: break details, amount, explanation, evidence of self-resolution, and confirmation of no cumulative impact
2. FinOps Manager reviews and may approve exceptions up to $2,500.00 per item
3. VP of Financial Services approval required for exceptions $2,500.01 – $10,000.00
4. CFO approval required for any exception exceeding $10,000.00
5. All approved Materiality Exceptions are logged in a separate register and reviewed quarterly by Internal Audit

### 8.3 Write-Off of Unexplained Variances

If, after exhaustive investigation (Level 2 complete, Level 3 review), a variance remains unexplained and cannot be resolved:

1. FinOps Manager prepares a Variance Write-Off Request including:
   - Complete investigation history (Jira ticket trail)
   - Confirmation that all investigative avenues have been exhausted
   - Justification for write-off (immaterial amount, cost of continued investigation exceeds benefit)
   - Proposed accounting treatment (write-off to "Reconciliation Differences" expense account FIN-8100-001)

2. Approval Authority:
   - ≤ $500.00: FinOps Manager
   - $500.01 – $5,000.00: VP of Financial Services
   - $5,000.01 – $50,000.00: VP of Financial Services + CFO joint approval
   - > $50,000.00: CFO + Audit Committee Chair approval

3. Write-offs shall be tracked in the Write-Off Register, reported monthly to the CFO, and reviewed quarterly by Internal Audit

### 8.4 Whistleblower and Fraud Escalation

Any Recon Analyst or other employee who suspects fraudulent activity (category BRK-FRAUD or otherwise) shall:

1. Immediately escalate to the Recon Supervisor AND the Compliance Officer (Jennifer Okonkwo) via the confidential email address `compliance-hotline@meridianhealth.com` – DO NOT document in standard Jira project
2. Preserve all relevant data and logs; do not attempt independent investigation
3. Compliance Officer assumes control of the investigation per the Meridian Whistleblower and Fraud Investigation Policy (SOP-CORP-003)

## 9. Training Requirements

### 9.1 Initial Training

All personnel assigned to reconciliation roles shall complete the following training before being granted access to reconciliation systems:

| Training Module | Delivery Method | Duration | Assessment |
|---|---|---|---|
| FIN-TRN-001: Introduction to Financial Data Reconciliation at Meridian | LMS (Workday Learning) | 2 hours | Quiz (≥ 80% required) |
| FIN-TRN-002: HealthPay Transaction Lifecycle and Payment Processing | Instructor-led (classroom or virtual) | 4 hours | Practical exercise |
| FIN-TRN-003: BlackLine Reconciliation System Operations | Hands-on lab | 4 hours | Competency demonstration (perform a mock daily reconciliation) |
| FIN-TRN-004: Break Investigation and Root Cause Analysis | LMS + Case studies | 1.5 hours | Case study assessment |
| FIN-TRN-005: SOC 2 and Regulatory Compliance Overview for FinOps | LMS | 1 hour | Quiz (≥ 80% required) |
| SOP-FIN-013-SUP: SOP-Specific Training (this document walkthrough) | On-the-job with Supervisor | 2 hours | Sign-off attestation |

**System Access Provisioning**: BlackLine, NetSuite, and bank portal access credentials are provisioned ONLY after successful completion of all required training modules, as verified by the Learning Management System (Workday Learning) completion records.

### 9.2 Ongoing Training

| Requirement | Frequency | Audience |
|---|---|---|
| SOP Refresher Training on this SOP (including any version updates) | Within 30 days of new version release | All reconciliation staff |
| Annual AML/BSA/OFAC Awareness Training | Annually | All Financial Services staff |
| BlackLine System Update Briefing | As needed (triggered by major BlackLine release) | All BlackLine users |
| Lessons Learned from Critical Incidents | Within 30 days of Critical Break Incident closure | All Financial Services staff |
| SOC 2 Control Awareness Refresh | Annually (prior to audit period) | Recon Supervisor, FinOps Manager, VP Financial Services |

### 9.3 Training Compliance Tracking

1. The FinOps Manager is responsible for monitoring training compliance for all Financial Services personnel
2. A monthly Training Compliance Report is generated from Workday Learning showing:
   - Completed training with dates
   - Overdue training assignments
   - Upcoming training requirements
3. 100% training compliance is required for all personnel with active reconciliation system access
4. Any personnel with overdue training > 15 days shall have their reconciliation system access temporarily suspended by the Recon Supervisor until training is completed; this suspension is logged as a control exception in the monthly SOC 2 evidence package

## 10. Related Policies and References

### 10.1 Meridian Internal Policies and SOPs

| SOP-ID | Document Title | Relationship to This SOP |
|---|---|---|
| SOP-FIN-001 | Financial Services Accounting Policy | Defines overall accounting principles; reconciliation feeds into financial reporting |
| SOP-FIN-008 | Employee Expense Report Reconciliation | Separate reconciliation process for T&E; out of scope but referenced for completeness |
| SOP-FIN-010 | Revenue Recognition Policy (ASC 606) | Defines revenue recognition rules; Section 5.8 implements reconciliation for ASC 606 |
| SOP-FIN-015 | Cash Management and Treasury Operations | Defines bank account structure and cash movement; referenced for ZBA reconciliations |
| SOP-IT-004 | Access Management and User Provisioning | Governs system access; referenced in Section 6.2 for access controls |
| SOP-IT-007 | Change Management Policy | Governs system changes; referenced for reconciliation configuration changes |
| SOP-CORP-003 | Whistleblower and Fraud Investigation | Referenced in Section 8.4 for fraud escalation |
| SOP-CORP-019 | Data Retention and Records Management | Governs retention periods; referenced in Section 4.3 for 7-year audit trail retention |
| SOP-CLIN-042 | Clinical Data Reconciliation | Out of scope; referenced for boundary clarification |
| SOP-HR-015 | Payroll Reconciliation | Out of scope; referenced for boundary clarification |
| SOP-RCM-022 | Revenue Cycle – Unapplied Cash Management | Referenced for escalation of unapplied patient payments |

### 10.2 External Standards and Frameworks

| Reference | Description | Applicability |
|---|---|---|
| AICPA TSC 2017 (SOC 2) | Trust Services Criteria for SOC 2 examinations | Section 6.1 maps controls to TSC; Section 7.4 defines SOC 2 evidence reporting |
| ASC 606 | Revenue from Contracts with Customers | Section 5.8 defines ASC 606 reconciliation |
| Bank Secrecy Act / AML | Federal anti-money laundering regulations | Anti-fraud monitoring and escalation (Section 8.4) |
| NACHA Operating Rules | ACH network rules | Provider and patient ACH transaction reconciliation (Section 5.6, 5.7) |

### 10.3 Meridian Systems Referenced

| System | Purpose | Business Owner |
|---|---|---|
| BlackLine | Financial reconciliation automation platform | VP of Financial Services |
| NetSuite | Enterprise Resource Planning (ERP) / General Ledger | Corporate Controller |
| HealthPay Core Transaction Engine (CTE) | Payment processing platform | VP of Engineering (Platform) |
| Snowflake (MERIDIAN_FINANCE) | Financial data warehouse and analytics | VP of Data & Analytics |
| Jira (FIN-BREAK, FIN-CHG, FIN-EXCEPTION, FIN-OUTAGE) | Break tracking, change management, exceptions, outage management | VP of Financial Services |
| PagerDuty | Incident alerting and escalation | VP of IT Operations |
| Datadog | System monitoring and observability | VP of IT Operations |
| Salesforce (Provider Finance queue) | Provider relationship management and case tracking | VP of Provider Solutions |
| Workday Learning | Learning Management System (LMS) | VP of Human Resources |
| Okta | Identity and access management (SSO) | VP of IT Security |
| HashiCorp Vault | Secrets management (credential storage) | VP of IT Security |
| ServiceNow | IT Service Management (incident and request ticketing) | VP of IT Operations |
| SharePoint | Document management for forms and checklists | VP of IT Operations |

## 11. Revision History

| Version | Date | Author / Owner | Approver | Description of Changes |
|---|---|---|---|---|
| 4.7 | 2024-04-01 | Robert Liu / Maria Santos (FinOps Manager, Interim) | James Thornton, CFO | **Minor Update**: Updated FinOps Manager role to reflect interim appointment (Maria Santos); updated SVB reference to Silicon Valley Bank (First Citizens); revised Section 5.2.1 S3 availability timeline from 05:00 to 06:00 ET to reflect updated bank file delivery schedule; corrected BlackLine profile name in Section 5.2.2; added clarifying language on Tier 1 aggregate threshold; minor typographical corrections throughout |
| 4.6 | 2023-11-15 | Robert Liu | James Thornton, CFO | **Major Revision**: Added Section 5.6 (Provider Settlement Reconciliation) and 5.7 (Patient Payment Reconciliation) to expand scope of HealthPay reconciliation procedures; updated Section 6.1 to add controls FIN-REC-C09 and FIN-REC-C10; revised materiality thresholds in Section 4.2 to align with updated risk assessment; updated all system references to reflect migration of Data Hub to Snowflake; expanded SOC 2 control evidence requirements per auditor feedback; added Form FIN-REC-010 (JE Validation Checklist) |
| 4.5 | 2023-07-22 | Robert Liu | James Thornton, CFO | **Minor Update**: Updated Section 5.1.2 step timing to reflect increased transaction volumes (now ~250K daily); adjusted Recon Analyst team size from 5 to 6 FTEs in Section 3.2; updated HashiCorp Vault paths for gateway credentials; clarified segregation of duties language in Section 4.4; updated cross-references |
| 4.4 | 2023-03-01 | Robert Liu | James Thornton, CFO | **Significant Revision**: Major restructuring of Section 5 (Detailed Procedures) to separate Daily, Four-Way, and Periodic procedures; introduced Four-Way Reconciliation concept replacing previous Three-Way model; added Section 5.8 (ASC 606 reconciliation); updated all SOC 2 references to TSC 2017 mapping; expanded training section to include FIN-TRN-005 and SOP-specific module; added KRI dashboard and expanded reporting in Section 7 |
| 4.3 | 2022-09-12 | Robert Liu | James Thornton, CFO | **Minor Update**: Updated payment gateway list to include Adyen (new gateway); revised Section 5.9 manual procedures to incorporate new Emergency Workbook; updated escalation contact information; quarterly review date updated |
| 4.2 | 2022-04-05 | Robert Liu | James Thornton, CFO | **Major Revision**: Complete document restructure to align with new Meridian SOP template; added RACI matrix; expanded SOC 2 control mapping; introduced materiality tier framework; added explicit SLAs for break resolution; deprecated legacy reconciliation system (ReconArt) in favor of BlackLine; all BlackLine-specific procedures added; Section 9 training requirements significantly expanded |

---

**Document Classification: Internal**

© 2024 Meridian Health Technologies, Inc. All rights reserved. This document contains proprietary and confidential information. Distribution is restricted to authorized personnel with a legitimate business need. Unauthorized reproduction or distribution is prohibited per SOP-CORP-001 (Information Security and Confidentiality).

**END OF DOCUMENT**
---
sop_id: "SOP-FIN-011"
title: "Interest Rate Risk Management"
business_unit: "Financial Services"
version: "4.7"
effective_date: "2024-02-22"
last_reviewed: "2025-02-17"
next_review: "2025-08-27"
owner: "Robert Liu, VP of Financial Services"
approver: "James Thornton, Chief Financial Officer"
classification: "Internal"
regulations:
  - "SR 11-7"
status: "Active"
---

# STANDARD OPERATING PROCEDURE
## Interest Rate Risk Management

### 1. Purpose and Scope

**Purpose**

The purpose of this Standard Operating Procedure (SOP) is to establish a standardized, enterprise-wide framework for identifying, measuring, monitoring, controlling, and reporting interest rate risk (IRR) arising from the financial activities of Meridian Health Technologies, Inc. ("Meridian"). This SOP ensures that all IRR exposures are managed within Board-approved risk appetite limits and are compliant with the Federal Reserve's guidance on model risk management (SR 11-7), as well as market-standard practices for a healthcare fintech organization. The primary objective is to safeguard the net economic value (NEV) and net interest income (NII) of the HealthPay Financial Services business unit against adverse movements in interest rates.

**Scope**

This SOP applies to all on- and off-balance sheet positions that generate Interest Rate Risk within the HealthPay Financial Services business unit. This includes, but is not limited to:
- **Medical Lending Portfolio:** Fixed and floating-rate patient installment loans, healthcare provider practice loans, and medical equipment financing.
- **Patient Financing:** Deferred interest and promotional-rate financing products underwritten under the Meridian PatientPay program.
- **Claims Automation Float:** Cash and cash equivalents held during the claims adjudication and settlement process, where Meridian acts as an intermediary.
- **Investment Securities:** The high-quality liquid asset (HQLA) portfolio held for liquidity coverage and yield enhancement, as managed by Corporate Treasury under the oversight of the Financial Services division.
- **Funding Liabilities:** Warehouse lines of credit, corporate bonds, and intercompany borrowings used to fund lending activities.
- **Derivative Instruments:** Interest rate swaps, caps, floors, and futures used for hedging purposes.
- **Model Risk:** All quantitative models, stress testing frameworks, and valuation tools used to measure and project IRR, in accordance with SR 11-7.

This SOP applies to all employees, contractors, and third-party vendors whose responsibilities impact the interest rate risk profile of Meridian. Compliance is mandatory for the Financial Services, Treasury, Risk Management, and Model Validation functions.

### 2. Definitions and Acronyms

| Term/Acronym | Definition |
| :--- | :--- |
| **ALCO** | Asset-Liability Committee. The primary governance body overseeing IRR. |
| **Basis Risk** | The risk arising from imperfect correlation in the adjustment of rates earned and paid on different instruments with otherwise similar repricing characteristics. |
| **CRO** | Chief Risk Officer. Although oversight is embedded within Financial Services, the enterprise CRO (dotted line to VP Financial Services) provides independent review. |
| **Duration Gap** | The difference between the duration of assets and the duration of liabilities, measuring the sensitivity of the Net Economic Value (NEV) to changes in interest rates. |
| **EAR** | Earnings at Risk. A measure of the potential reduction in Net Interest Income (NII) over a specified horizon due to adverse interest rate movements. |
| **EVE** | Economic Value of Equity. Synonymous with Net Economic Value (NEV). The present value of assets minus the present value of liabilities. |
| **Gap Analysis** | A static measure of the mismatch between rate-sensitive assets (RSAs) and rate-sensitive liabilities (RSLs) over discrete time buckets. |
| **IRR** | Interest Rate Risk. The exposure of Meridian's financial condition to adverse movements in interest rates. |
| **MD&A** | Management Discussion and Analysis, as reported to the Board AI Governance & Risk Committee. |
| **Model Risk** | The potential for adverse consequences from decisions based on incorrect or misused model outputs and reports, as defined by SR 11-7. |
| **NEV** | Net Economic Value. See EVE. |
| **NII** | Net Interest Income. The difference between interest income generated and interest expense paid. |
| **Optionality Risk** | The risk arising from embedded options in assets or liabilities (e.g., prepayment risk on medical loans). |
| **Repricing Risk** | The risk from timing differences in the maturity (for fixed rate) and repricing (for floating rate) of assets and liabilities. |
| **SR 11-7** | Federal Reserve Supervisory Guidance on Model Risk Management (2011-12). |
| **Yield Curve Risk** | The risk from non-parallel shifts in the yield curve (e.g., flattening, steepening). |

### 3. Roles and Responsibilities

A RACI matrix defines the governance structure for IRR management, ensuring direct accountability in line with SR 11-7 standards for segregation of duties.

| Activity/Decision | VP, Fin. Services (R. Liu) | CFO (J. Thornton) | Treasury Manager | Fin. Risk Manager | Model Validation Team | ALCO | Internal Audit |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Policy Ownership & Annual Review** | A | R | C | I | I | I | I |
| **Risk Appetite & Limit Setting** | R | A | C | C | - | I | - |
| **Daily Hedging Execution** | I | - | R/A | C | - | - | - |
| **Risk Measurement & Reporting** | I | I | C | R/A | I | - | - |
| **Model Development** | I | - | C | R | C | - | - |
| **Independent Model Validation** | I | I | - | I | R/A | - | - |
| **Regulatory Compliance (SR 11-7)** | R | A | C | C | R | I | I |
| **Escalation of Limit Breaches** | R | A | I | R | - | A | - |

**Legend:** R=Responsible, A=Accountable, C=Consulted, I=Informed

**Key Role Descriptions:**

- **VP of Financial Services (Robert Liu):** Ultimate business owner of the IRR framework. Accountable for ensuring the SOP aligns with strategic financial objectives. Chairs the ALCO.
- **Chief Financial Officer (James Thornton):** Approves risk appetite statements and significant hedging strategies. Holds the final executive sign-off on model risk management attestations as required by SR 11-7.
- **Treasury Manager:** Executes daily hedging orders, manages laddered funding maturities, and monitors daily liquidity and rate movements through the Bloomberg Terminal and SageMaker dashboards.
- **Financial Risk Manager:** Performs independent risk analytics, including NII/EVE simulation runs in the QRM platform, backtesting, and stress testing. Prepares the monthly IRR pack for ALCO.
- **Model Validation Team:** An independent group, reporting to the Chief Compliance Officer (Thomas Anderson), responsible for the rigorous technical review of all IRR models per SR 11-7 Section V.3. This team runs a separate validation environment in `AWS us-east-1`, isolated from the development SageMaker instance.
- **Internal Audit:** Conducts an annual audit of the IRR control framework, including verification of adherence to this SOP and SR 11-7 compliance.

### 4. Policy Statements

Meridian Health Technologies, Inc. is committed to the following high-level policy statements to govern Interest Rate Risk:

1.  **Risk Appetite Framework:** Meridian’s IRR exposure shall be managed to protect both economic value (NEV) and earnings volatility (NII) within limits approved by the CFO and the Board AI Governance & Risk Committee. The primary objective is capital preservation, with revenue optimization as a secondary goal.
2.  **Prohibited Practices:** Speculative trading on interest rate movements is strictly prohibited. All derivative transactions must be matched to specific, identifiable balance sheet exposures or forecasted transactions. The use of complex, non-vanilla structured derivatives requires explicit prior approval from the CFO.
3.  **Model Risk Management (SR 11-7 Alignment):** All quantitative models used for IRR measurement and management shall be subject to the Meridian Model Risk Management Policy (SOP-RISK-002). This includes rigorous independent validation, ongoing monitoring, and governance processes consistent with the principles of SR 11-7.
4.  **Hedging Strategy:** The primary strategy is to manage interest rate risk through the use of plain-vanilla interest rate swaps, caps, and floors. The hedge ratio, targeting a NEV sensitivity of no more than a 10% decline under a +200 basis point shock, will be reviewed weekly.
5.  **Data Integrity:** IRR data sources, including the loan origination system (HealthPay Core), the treasury management system (Kyriba), and pricing feeds (Bloomberg), are designated as Authoritative Data Sources (ADS). Any modifications to ADS feeds require change management approval and formal re-validation of downstream models.

### 5. Detailed Procedures

This section outlines the operational lifecycle of Interest Rate Risk Management at Meridian. The rhythm is structured around daily, monthly, quarterly, and annual processes, alongside an event-driven rebalancing protocol.

#### 5.1 Daily Position Monitoring and Rate Shock Analysis

The Treasury Manager is responsible for the daily operational review of interest rate exposure.

1.  **Position Aggregation (9:00 AM ET):**
    *   Extract the prior end-of-day (EOD) balance sheet extract from the HealthPay Core GL (`Treasury_Positions_Extract.sql`).
    *   Validate the automated feed against the Kyriba treasury management system. Any discrepancy greater than $50,000 must be investigated and resolved with Capital Markets Operations prior to analysis.
    *   Ingest the current yield curves (SOFR, U.S. Treasury, Prime) from the Bloomberg Terminal data feed into the Real-Time Risk Dashboard, hosted on a dedicated QuickSight instance (`Q-Sight-IRR-Prod-01`).

2.  **Gap Analysis Refresh:**
    *   Execute the automated gap analysis script (`SOP-FIN-011_GAP_Daily.py`), which buckets all RSAs and RSLs into the standard Meridian repricing intervals: 0-3 Months, 3-12 Months, 1-3 Years, 3-5 Years, and >5 Years.
    *   The script generates a "Daily Gap Report" summarizing the cumulative mismatch across all intervals.

3.  **Threshold Breach Screening:**
    *   Review the output against the *Table A: Daily Limit Thresholds* below. The QuickSight dashboard is configured with red/amber/green (RAG) status indicators for each metric.
    *   **Table A: Daily Limit Thresholds**
        | Risk Metric | Red (Mandatory Action) | Amber (Escalation) | Green (No Action) |
        | :--- | :--- | :--- | :--- |
        | NII-at-Risk (1-Year, +50bps) | Decline > 5.0% | Decline 2.5% - 5.0% | Decline < 2.5% |
        | NEV-at-Risk (Instantaneous, +200bps) | Decline > 15.0% | Decline 10.0% - 15.0% | Decline < 10.0% |
        | `KRI-GAP-001` (12-Mo Cum Gap / Asset %) | > ±15% | ± 10% - 15% | < ±10% |
    *   If any metric breaches an **Amber** threshold, the Treasury Manager must send a flash report via MS Teams to the Financial Risk Manager and VP of Financial Services within 1 hour.
    *   If any metric breaches a **Red** threshold, the Treasury Manager must immediately notify the Financial Risk Manager, VP of Financial Services, and the CFO. An emergency ALCO huddle shall be convened within 2 business hours.

4.  **Daily Action Close-out (12:00 PM ET):**
    *   The Treasury Manager logs the daily status and any actions taken in the `IRR_Daily_Log_YYYY-MM-DD` entry within the Confluence `FIN-RISK` space. This establishes the daily audit trail.

#### 5.2 Monthly NEV and NII Simulation

The Financial Risk Manager is responsible for the comprehensive monthly simulation cycle, providing the primary analytics for the ALCO meeting.

1.  **Data Preparation (T+3 Business Days of Month-End):**
    *   Extract month-end static and dynamic cash flows for every instrument on the Meridian balance sheet from the QRM (Quantitative Risk Management) system.
    *   Overlay the "Base Case" yield curve, defined as the month-end spot curve forward rates, sourced directly from the ICE BofA curves via the Bloomberg feed.

2.  **Core Simulation Runs:**
    *   Execute the following deterministic Interest Rate Scenarios (IRS) in the QRM system. The runs must be completed by T+5:
        *   **Scenario 1: Parallel Shock Up (+100, +200, +300 basis points).**
        *   **Scenario 2: Parallel Shock Down (-100, -200 basis points).** (Subject to a floor of 0%).
        *   **Scenario 3: Non-Parallel (Curve Flattening/Steepening):** Defined as a +0/-200 basis point shock on short-end/long-end rates and vice versa.
        *   **Scenario 4: Custom Historical Stress:** Re-run using the actual yield curve movements from the Global Financial Crisis of 2008 and the COVID-19 crash of March 2020.
    *   Generate the NII-at-Risk (12-month horizon) and NEV-at-Risk (instantaneous) for each scenario.

3.  **Behavioral Assumption Adjustment:**
    *   Within the QRM runs, apply the Meridian-approved behavioral models for **Prepayment Risk** and **Deposit Float Duration**:
        *   **Prepayment Model:** A conditional prepayment rate (CPR) model for the patient loan portfolio, calibrated monthly against 12 months of rolling historical prepayment data. The model output (`MOD-BEH-PREPAY-v2.0`) is fed directly into QRM.
        *   **Float Duration:** The claims float non-maturity deposit (NMD) model, which assigns a 3-year duration profile to the core, non-volatile portion of the float.

4.  **Monthly IRR Reporting Pack (T+7):**
    *   Consolidate all simulated results, the gap analysis, and commentary into the standard "Monthly IRR & Balance Sheet Dashboard" (QuickSight Dashboard ID: `QS-MTH-IRR-001`).
    *   The pack must include a model performance validation annex: a comparison of the prior month's 1-month NII forecast against the actual realized NII. A variance greater than 10% triggers the Model Backtesting protocol (see Section 6.3).

#### 5.3 ALCO Meeting Procedure

The ALCO meets on the second Wednesday of each month. The Chair (VP of Financial Services, Robert Liu) conducts the meeting according to the following standing agenda:

1.  **Review of Previous Action Items:** (5 minutes) - The ALCO Secretary reviews and logs closure status in the Jira `ALCO-AGEND` project.
2.  **Economic & Rate Environment Review:** (10 minutes) - Presentation by the Treasury Manager, summarizing key central bank communications, macroeconomic data releases, and the forward swap curve.
3.  **Risk Profile Dashboard Review:** (20 minutes) - The Financial Risk Manager presents the Monthly IRR Reporting Pack, focusing on:
    *   NII and NEV sensitivity against Board-approved limits (Section 5.5, Table A).
    *   Decomposition of risk by source (Repricing, Basis, Optionality).
    *   Duration gap trends.
    *   Model performance backtesting results.
4.  **Hedging Strategy & Execution Review:** (15 minutes) - The Treasury Manager presents the effectiveness of existing hedges and proposes adjustments. ALCO votes on all proposed hedging transactions above a $500,000 notional.
5.  **Forward-Looking Risk Discussion:** (10 minutes) - A deep dive into top and emerging risks, utilizing the "Custom Historical Stress" and a forward-looking internal severe adverse scenario defined by Meridian's Risk Strategy team.

Meeting minutes are recorded in the Meridian Confluence system (`ALCO-MINUTES-YYYY-MM-DD`) and published to attendees within 48 hours.

#### 5.4 Hedging Transaction Execution

When a hedging action is authorized by ALCO or by the daily risk limits, the Treasury Manager executes the trade according to the following procedure:

1.  **Trade Authorization:** Secure formal approval. For trades authorized at ALCO, this is the approved minutes. For daily limit-driven trades, a "Hedging Request" form (`FORM-FIN-IRR-001`) must be completed in ServiceNow and approved electronically by the VP of Financial Services or the CFO (depending on the delegation of authority, see Table B).
2.  **Counterparty Selection:** Solicit quotes via Bloomberg's `IBDE` (Interest Rate Derivatives Execution) platform from Meridian’s approved panel of global systemically important bank (G-SIB) counterparties. A minimum of three competitive quotes is mandatory for any trade over $25 million notional.
3.  **Best Execution:** Select the quote that provides the best net economic outcome for Meridian, considering not only price but also counterparty credit risk (pre-settlement credit exposure) and legal terms. Document the rationale on the Hedging Request form.
4.  **Trade Capture & Confirmation:**
    *   Book the trade details (counterparty, notional, rate, maturity, conventions) into the Kyriba treasury system immediately.
    *   Match the electronic confirmation from the counterparty against the Kyriba record within the same business day.
    *   Upload the final, fully matched term sheet into the Meridian Document Management System (SharePoint, path: `Financial_Services/Hedging/Legal_Documentation/`).

#### 5.5 Model Lifecycle (SR 11-7 Alignment)

This procedure formalizes the rigorous model risk management lifecycle as mandated by SR 11-7 Section V ("Model Validation") and VI ("Ongoing Monitoring").

1.  **Model Inventory:** The Financial Risk Manager maintains a master inventory in ServiceNow of all active IRR models, including `MOD-PD-WS-2023-v3.1` and the QRM valuation engine configuration. The inventory records the Owner, Developer, Validation Status, and Next Review Date.
2.  **Independent Model Validation:**
    *   Before any new model or material change to an existing model can be used for production analysis (i.e., to inform ALCO decisions), it must be validated by the independent Model Validation Team.
    *   The Validation Team evaluates the model’s conceptual soundness, data inputs, statistical methodology, code, and output reasonableness. This is documented in a "Model Validation Report" (`MVR-YYYY-XXX`) that explicitly rates the model (e.g., "Satisfactory," "Satisfactory with Findings," "Unsatisfactory").
    *   A "Satisfactory" rating is required for production use. "Satisfactory with Findings" allows production use but with a documented remediation plan and timeline.
3.  **Annual Model Revalidation:** Every active model, regardless of its prior rating, must undergo an annual revalidation. The VP of Financial Services and the CRO must jointly attest to the CFO annually that all models used by Financial Services are fit for purpose. This attestation is a critical SR 11-7 governance artifact.
4.  **Backtesting and Monitoring (SR 11-7 Section VI.4):**
    *   The Financial Risk Manager conducts monthly backtesting: comparing the 1-month-ahead NII forecast from each active model against the actual realized NII.
    *   The Model Validation Team conducts quarterly sensitivity analysis and stability checks on the model code.
    *   Any sustained, material model underperformance (defined as a backtesting variance exceeding threshold limits for three consecutive months) triggers a mandatory "Model Issue" in ServiceNow and an immediate revalidation review, as per the Model Risk Management Policy (SOP-RISK-002).

### 6. Controls and Safeguards

Meridian has implemented a multi-layered control environment to ensure the integrity, objectivity, and security of the IRR management process.

#### 6.1 Governance Controls (SR 11-7 Section III.2 and IV.2)
- **Three Lines of Defense:**
    1.  **First Line (Functional Management):** Treasury Manager and Financial Risk Manager. Own and manage the risk, executing trades and preparing reports.
    2.  **Second Line (Independent Risk Oversight):** The Model Validation Team and the broader enterprise CRO function provide independent oversight, challenge, and validation.
    3.  **Third Line (Assurance):** Internal Audit provides an independent assessment of the effectiveness of the entire framework on an annual basis.
- **ALCO Charter:** The authority of the ALCO is derived from a formal, Board-approved Charter, which is reviewed and renewed annually.

#### 6.2 Technology and System Controls
- **Segregation of Duties (Access Control):** Access to systems is strictly controlled via Okta SSO integrated with Meridian’s identity governance. The Treasury Manager has the right to initiate trades in Kyriba (Maker), while a separate Financial Risk Manager role is required for trade confirmation and settlement (Checker). The Model Validation Team has read-only access to production models and operates in a separate AWS SageMaker validation environment (`AWS-ENV-VALIDATE-01`).
- **System Change Management:** Any changes to the core IRR systems (QRM, Kyriba, Bloomberg data feeds) must follow the Meridian Technology Change Management SOP (SOP-IT-005). Changes require a documented Request for Change (RFC), peer-reviewed code, and approval before deployment to the `PRD` environment.

#### 6.3 Model Controls
- **Version Control:** All model code is maintained in a strictly controlled GitLab repository (`fin-risk/models`). No manual or un-tracked changes to production model code are permitted.
- **Input Data Validation:** Data ingested into the models from the `HealthPay Core` and `Kyriba` is automatically validated against a comprehensive set of reconciliation and integrity rules (e.g., checksums, range checks) by a pre-processing layer (`AWS Lambda: FinRisk-DataValidator`) before being accepted by the QRM engine. A data quality report is generated as part of the monthly IRR pack.
- **Result Reasonableness Checks:** The QRM engine has built-in automated reasonableness checks. For example, a +300bps shock scenario resulting in an *increase* in NEV for a liability-sensitive balance sheet would be automatically flagged for manual review.

#### 6.4 Segregation of Duties Matrix
| Task | Role 1 | Role 2 | Role 3 |
| :--- | :--- | :--- | :--- |
| Hedge Trade Initiation | Treasury Manager | - | - |
| Hedge Trade Confirmation | Financial Risk Manager | - | - |
| Model Code Development | Financial Risk Manager | - | - |
| Model Code Review / Approve | Model Validation Team | - | - |
| Model Code Deploy to Prod | DevOps (per RFC) | Financial Risk Manager (Approval) | Model Validation Team (Notification) |
| Risk Report Authoring | Financial Risk Manager | - | - |
| Risk Report Review & Challenge | VP, Financial Services | ALCO Members | - |

### 7. Monitoring, Metrics, and Reporting

#### 7.1 Key Performance and Risk Indicators (KPIs/KRIs)
Meridian employs a tiered system of metrics.

- **Tier 1: Board-Level KRIs (Reported Quarterly)**
    *   NEV-at-Risk (Instantaneous, +200bps Shock) vs. Limit: **Must be <15% decline of Base Case NEV.**
    *   NII-at-Risk (12-Month Horizon, +100bps Ramp) vs. Limit: **Must be <7.5% decline of Base Case NII.**
    *   High-Level Model Risk Assessment (Green / Amber / Red status of all IRR models).

- **Tier 2: Financial Services Unit-Level KPIs (Reported Monthly to ALCO)**
    *   Duration Gap vs. Target of 0.0 - 1.0 years.
    *   Hedge Effectiveness Ratio (using the dollar-offset method) for open derivative positions. Target: **>80% effectiveness.**
    *   Economic Value Sensitivity (EVS) decomposition showing contribution to risk from Repricing, Basis, and Optionality.
    *   Operational Risk: Number of daily report generation failures or data feed errors per month. Target: **Zero**.

#### 7.2 Reporting Cadence and SLAs

| Report Name | Medium/Location | Frequency/Deadline | Author | Primary Audience |
| :--- | :--- | :--- | :--- | :--- |
| Daily IRR Dashboard | Q-Sight-IRR-Prod-01 | Daily, 10:30 AM ET | Automated (QC'd by Treasury Mgr) | Treasury Manager, Fin. Risk Mgr |
| Monthly IRR & Balance Sheet Pack | QS-MTH-IRR-001 (Confluence link) | T+7 Business Days of Month-End | Financial Risk Manager | ALCO Members, VP Fin. Services |
| Quarterly Board Risk Report | Confluence Board Portal | 10th Calendar Day of the next Quarter | VP, Financial Services | CFO, Board Risk Committee |
| Annual SR 11-7 Attestation | ServiceNow Governance Module | 15th Calendar Day of December | VP, Financial Services & CRO | CFO, Chief Compliance Officer |
| Hedge Effectiveness Report | Confluence `FIN-RISK` | Monthly, T+7 | Treasury Manager | VP Fin. Services, Financial Risk Manager |

### 8. Exception Handling and Escalation

A defined protocol for managing deviations from this SOP or the limits it mandates is crucial for an effective control environment.

#### 8.1 Limit Breaches
A limit breach is defined as any Tier 1 or Tier 2 KRI/KPI exceeding the thresholds specified in Table A (Daily) or Section 7.1 (Board).

1.  **Immediate Action:** Upon an Amber or Red breach identified in the Daily Monitoring (Section 5.1), trading and new lending activities related to the breached exposure may be temporarily paused at the discretion of the Treasury Manager pending investigation.
2.  **Formal Breach Notification:** Within 24 hours of identifying a Red limit breach, the Financial Risk Manager must document the breach in ServiceNow using the "Risk Limit Breach Notification" (`FORM-RISK-004`). The notification must detail the cause, the current state, and a proposed remediation plan.
3.  **Remediation Approval:** The remediation plan must be approved by the VP of Financial Services and the CFO.
4.  **Board Notification:** All Red limit breaches, regardless of duration, must be reported to the CFO and reported to the Board Risk Committee at the next quarterly meeting.

#### 8.2 Policy and Procedure Exceptions
A request to deviate from a specific procedural step (e.g., using a different yield curve source due to a Bloomberg outage) must be treated as a formal exception.

1.  **Request:** The requestor (e.g., Financial Risk Manager) submits a "Process Exception Request" (`FORM-RISK-005`) in ServiceNow, specifying the exact SOP section, the nature of the deviation, the business justification, and compensating controls.
2.  **Approval Delegation:**
    *   **Temporary (<= 5 business days) exceptions:** Approved by VP of Financial Services, in consultation with the Chief Compliance Officer.
    *   **Permanent or Long-Term exceptions:** Must be approved by the CFO and presented to the Board Risk Committee. A permanent exception necessitates an amendment of this SOP.

#### 8.3 Model Performance Trigger
As per SR 11-7 ongoing monitoring requirements, a "Model Issue" is triggered when backtesting variance exceeds thresholds for three consecutive months (Section 5.5, step 4d). The Financial Risk Manager must create a "Model Issue" ServiceNow ticket, which automatically initiates a Model Revalidation Review by the independent team, per the Model Risk Management Policy (SOP-RISK-002). The issue status and remediation is tracked at each ALCO meeting.

### 9. Training Requirements

All personnel with responsibilities detailed in the RACI matrix (Section 3) are required to complete mandatory training to ensure adherence to this SOP and the broader Meridian risk culture.

| Training Module Title | Target Audience | Method & Provider | Frequency | Tracking Method |
| :--- | :--- | :--- | :--- | :--- |
| SOP-FIN-011: IRR Management Procedures | All roles in the RACI matrix for this SOP. | Online, instructor-led module via Workday Learning. Developed by the Financial Risk Manager. | Annually. Initial training before access to production systems is granted. | 100% completion tracked in Workday Learning L-Codes. |
| Meridian Model Risk: Foundation (SR 11-7) | Model Owners, Developers, Validators (incl. Fin. Risk Manager, Treasury Manager, Validation Team). | Interactive workshop with case studies, delivered by the VP of Model Risk or external consultant. | Biennially (every two years). | Attendance sign-in sheet uploaded to Workday compliance profile. |
| Capital Markets & Derivative Fundamentals | Treasury Manager and Hedging Execution Personnel. | External vendor (e.g., ACI, ISDA Foundations). | Every 3 Years. | External certificate and CPE credits logged in Workday. |

**Non-Compliance:** Failure to complete required training by the due date will result in the suspension of access to the QRM, Kyriba, and Bloomberg systems until training is completed. The ALCO will review all mandatory training non-compliance events quarterly.

### 10. Related Policies and References

| Internal Document ID | Title | Relationship |
| :--- | :--- | :--- |
| SOP-RISK-002 | Enterprise Model Risk Management Policy | Overarching policy that SOP-FIN-011 implements specifically for IRR models. Mandated by SR 11-7. |
| SOP-FIN-008 | Financial Derivatives and Hedging Authorization | Defines the specific instruments, authorized counterparties, and execution procedures for hedging. |
| SOP-FIN-004 | Liquidity and Funding Risk Management | Addresses liquidity risks which are intrinsically linked to IRR and funding strategy. |
| SOP-IT-005 | Technology Change & Release Management | Governs how code and configuration changes to QRM and Kyriba are approved and deployed. |
| FORM-FIN-IRR-001 | Hedging Request Form | The electronic form for authorizing and documenting a hedging trade. |
| FORM-RISK-004 | Risk Limit Breach Notification | ServiceNow form for documenting limit breaches. |
| FORM-RISK-005 | Process Exception Request | ServiceNow form for requesting deviations from this SOP. |
| External Guidance | SR 11-7 (Attachment 1): Supervisory Guidance on Model Risk Management | The primary external regulatory standard for model governance, validation, and controls. |

### 11. Revision History

| Version | Date | Author(s) | Description of Changes |
| :--- | :--- | :--- | :--- |
| 4.0 | 2022-11-15 | R. Liu, A. Chen (Fin. Risk Mgr) | Major re-write. Full alignment with new enterprise SR 11-7 framework. Moved all limits from appendices into core procedure text. Introduced formal model inventory. |
| 4.2 | 2023-03-03 | A. Chen | Minor update to Section 5.1 to add the new QuickSight dashboard ID and revised Amber threshold for NII-at-Risk from 2.0% to 2.5% following a Board risk appetite review. |
| 4.5 | 2023-08-01 | R. Liu, T. Vance (Treasury Mgr) | Revised Hedging Counterparty approval process in Section 5.4 to require three quotes for >$25M notional. Added Section 6.2 on technology controls following an Internal Audit finding. |
| 4.6 | 2024-01-10 | A. Chen, L. Kim (Compliance) | Annual review. Updated Sections 8 and 9 to integrate new ServiceNow forms (FORM-RISK-*) and Workday Learning tracking. No substantive policy changes. |
| 4.7 | 2025-02-17 | R. Liu | Scheduled triennial review. Amended Section 5.2 behavioral models for patient loan prepay to `MOD-BEH-PREPAY-v2.0`. Updated roles to reflect department re-org. Added attestation requirement. Updated next review date. |
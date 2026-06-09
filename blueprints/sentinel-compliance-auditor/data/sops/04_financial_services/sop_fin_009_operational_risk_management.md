---
sop_id: "SOP-FIN-009"
title: "Operational Risk Management"
business_unit: "Financial Services"
version: "4.7"
effective_date: "2025-11-27"
last_reviewed: "2026-04-13"
next_review: "2026-10-20"
owner: "Robert Liu, VP of Financial Services"
approver: "James Thornton, Chief Financial Officer"
classification: "Internal"
regulations:
  - "SR 11-7"
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: SOP-FIN-009

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, governance, and operational processes for the identification, assessment, monitoring, reporting, and mitigation of operational risk within the Financial Services business unit of Meridian Group. The document formalizes the enterprise approach to operational risk management (ORM) and ensures consistent application of risk methodologies across all financial service products, platforms, and supporting functions.

The objectives of this SOP are to:

1.  Establish a unified operational risk taxonomy applicable to all Financial Services activities.
2.  Define the Risk and Control Self-Assessment (RCSA) methodology and cadence.
3.  Implement standardized loss event capture, classification, and remediation tracking.
4.  Design, deploy, and monitor Key Risk Indicators (KRIs) with appropriate governance.
5.  Ensure alignment with the Interagency Guidance on Model Risk Management (SR 11-7) for all quantitative tools supporting the operational risk framework.
6.  Satisfy the operational risk control criteria relevant to the SOC 2 Trust Services Criteria (specifically CC7.1, CC7.2, CC7.3).

### 1.2 Scope

**In-Scope Entities and Functions:**

| In-Scope | Description |
|---|---|
| Business Unit | Financial Services (all sub-departments: Payments, Lending Operations, Treasury Services, Merchant Acquiring, Fraud Operations) |
| Geographic Footprint | Global operations, with specific consideration for North America (NA), European Union (EU) including the United Kingdom (UK), and Asia-Pacific (APAC) processing hubs |
| Technology Assets | All hardware, software, middleware, and network infrastructure supporting the `FIN-SYS-*` asset family as defined in CMDB v6.2 |
| Third-Party Relationships | All vendors, processors, and service providers supporting financial transaction processing, model hosting, and payment switching |
| Data Domains | Transactional data, customer PII, payment credentials, model inputs, and risk reporting data residing in `FIN-DATA-LAKE` and associated reporting marts |

**Out-of-Scope:**

- Market risk and liquidity risk, which are managed under `SOP-TRS-001` and `SOP-TRS-003` respectively.
- Credit risk origination and portfolio management for the Institutional Lending division, governed by `SOP-CRD-012`.
- Strategic risk, which is managed at the Group Executive level.

### 1.3 Applicability

This SOP applies to all permanent employees, contractors, temporary staff, and third-party personnel (“Covered Persons”) whose role involves the design, execution, operation, monitoring, or support of Financial Services processes, systems, or models. Compliance with this SOP is mandatory and a condition of employment or contractual engagement with Meridian Group for the Financial Services business unit.

---

## 2. Definitions and Acronyms

For the purpose of this SOP, the following capitalized terms shall have the meanings set forth below:

| Term | Definition |
|---|---|
| **Operational Risk** | The risk of loss resulting from inadequate or failed internal processes, people, and systems, or from external events. This definition includes legal risk but excludes strategic and reputational risk. |
| **Key Risk Indicator (KRI)** | A quantitative metric used to monitor the level of risk within a specific operational area, providing an early warning signal of potential control failure. |
| **Risk and Control Self-Assessment (RCSA)** | A structured, bottom-up process by which business process owners identify, assess, and document the inherent and residual risks in their area, along with the effectiveness of the controls designed to mitigate those risks. |
| **Loss Event** | An operational incident that results in a realized financial or non-financial (e.g., regulatory penalty, customer detriment) impact. It includes near-misses where a loss was avoided solely by chance. |
| **Inherent Risk** | The raw level of risk exposure before considering the effect of any controls. Assessed on an Impact x Likelihood basis. |
| **Residual Risk** | The level of risk exposure remaining after considering the expected effectiveness of the control environment. Assessed on an Impact x Likelihood basis. |
| **Control** | A specific, documented action, policy, procedure, or system configuration designed to reduce the likelihood or impact of a risk event. |
| **Risk Appetite** | The aggregate level and types of risk that Meridian Financial Services is willing to accept in pursuit of its strategic objectives. |
| **Risk Taxonomy** | A hierarchical, multi-level classification structure used to consistently categorize the root cause of operational risk. |
| **RTO (Recovery Time Objective)** | The targeted duration of time between failure and when a business function must be restored. |
| **RPO (Recovery Point Objective)** | The maximum targeted period in which data might be lost due to a major incident. |

| Acronym | Full Text |
|---|---|
| **ORM** | Operational Risk Management |
| **RCSA** | Risk and Control Self-Assessment |
| **KRI** | Key Risk Indicator |
| **KCI** | Key Control Indicator |
| **BIA** | Business Impact Analysis |
| **ICFR** | Internal Controls over Financial Reporting |
| **ORC** | Operational Risk Committee |
| **GRC** | Governance, Risk, and Compliance (refers to Meridian's centralized `MER-GRC` platform) |
| **WoW** | Ways of Working |

---

## 3. Roles and Responsibilities

The table below outlines the responsible, accountable, consulted, and informed (RACI) parties for the core activities governed by this SOP.

| Activity / Decision | Risk Owner (1st Line) | ORM Partner (2nd Line) | Internal Audit (3rd Line) | VP, Financial Services (Robert Liu) | CFO (James Thornton) |
|---|---|---|---|---|---|
| **RCSA Execution** | **R** | **A** | **I** | **C** | **I** |
| **Loss Event Root Cause Analysis** | **R, A** | **C** | **I** | **C** | **I** (for events >$50K) |
| **KRI Threshold & Escalation Design** | **C** | **R, A** | **I** | **C** | **I** |
| **Operational Risk Policy Approval** | **C** | **R** | **I** | **C** | **A** |
| **Model Documentation & Validation (SR 11-7)** | **R** | **A** | **I** | **C** | **A** |
| **Business Continuity Plan Testing** | **R** | **C** | **I** | **A** | **I** |
| **System Availability Monitoring (SOC 2)** | **R** | **C** | **I** | **A** | **I** |

### 3.1 Specific Role Definitions

- **Process Owner (First Line of Defense - "1LOD")**: The individual directly responsible for the execution of a process. They are accountable for performing the RCSA, identifying risks, implementing controls, and recording loss events in the MER-GRC platform (`GRC-RECORD`) within five (5) business days of discovery. All Process Owners report to **Robert Liu**, VP of Financial Services.

- **Operational Risk Management (ORM) Partner (Second Line of Defense - "2LOD")**: An independent risk management specialist assigned to the Financial Services unit. The ORM Partner facilitates RCSA workshops, challenges the completeness of the risk register and the assessed control effectiveness, monitors KRI dashboards, and provides an aggregated risk profile to the Operational Risk Committee. The ORM function ultimately reports to the Chief Risk Officer (CRO).

- **Operational Risk Committee (ORC)**: A standing governance body co-chaired by the VP of Financial Services and the Head of Operational Risk. The ORC meets monthly to review the operational risk profile, approve exceptions to this SOP, accept residual risks exceeding appetite, and direct remediation priorities. The CFO, **James Thornton**, retains final escalation authority for any revenue-impacting or regulator-reportable risk.

- **Model Owner**: The 1LOD Process Owner for any quantitative tool, spreadsheet, or system that processes inputs into a calculation or decision output. The Model Owner is responsible for maintaining a current model inventory and ensuring documentation is complete, which serves as the first line of defense for compliance with SR 11-7.

---

## 4. Policy Statements

### 4.1 Risk Appetite Framework

The Financial Services business unit operates under a defined Risk Appetite Statement, approved annually by the Meridian Board of Directors. The following aggregate appetite statements apply to operational risk:

| Risk Category | Appetite Statement | Key Metric |
|---|---|---|
| **Transaction Processing Accuracy** | Zero tolerance for systemic errors impacting more than 0.05% of daily transaction volume. | Daily Reconciliation Error Rate |
| **System Availability** | Customer-facing payment processing platforms (`FIN-PAY-*`) shall maintain high availability, with all incidents categorized and resolved under a structured Major Incident Management (MIM) process. | Monthly Uptime % |
| **Third-Party Disruption** | No single outsourced processing failure shall prevent processing of payments for more than a defined, acceptable period. | Business Continuity Time-to-Recovery |
| **Conduct & Regulatory Compliance** | Zero tolerance for deliberate misconduct; risk of regulatory censure from processing failures must be minimized. | Open Regulatory Issues > 90 Days Past Due |

### 4.2 Control Culture

Management is responsible for fostering a risk-aware culture where Covered Persons are empowered and obligated to:

- Report operational errors, near-misses, and loss events immediately, without fear of reprisal.
- Complete RCSA questionnaires accurately, reflecting the true state of the control environment.
- Escalate identified risks, control weaknesses, or overdue remediation actions to their ORM Partner.

### 4.3 Model Risk Management Alignment

All quantitative tools used for risk assessment, KRI calculation, or loss forecasting that are not classified as deterministic, standalone spreadsheets are subject to the standards defined herein and aligned with SR 11-7 principles. Each model must be centrally inventoried and undergo a conceptual soundness review prior to its first use. Documentation for each registered model shall be maintained in `MER-GRC` and contain a clear statement of purpose, data requirements, and operational parameters. All models must be subject to independent review prior to initial deployment and thereafter on a periodic basis. Ongoing monitoring of model performance shall be conducted to verify that the tool continues to perform as expected.

---

## 5. Detailed Procedures

This section forms the operational core of this SOP. All procedures are mandatory unless explicitly marked as advisory.

### 5.1 Operational Risk Taxonomy

All risks, controls, loss events, and KRIs must be classified using Meridian’s Operational Risk Taxonomy v3.1. The taxonomy is embedded within the `MER-GRC` platform and structured as a four-tier hierarchy:

| Level 1 (Category) | Level 2 (Sub-Category) | Level 3 (Event Type) | Level 4 (Causal Factor) |
|---|---|---|---|
| **People** | Internal Fraud | Theft / Embezzlement | Segregation of Duties Failure |
| **People** | Internal Fraud | Unauthorized Trading | Management Override |
| **People** | Execution Error | Data Entry Error | Inadequate Procedure (see SOP gap) |
| **Process** | Transaction Capture | Late/Failed Settlement | Reconciliation Failure |
| **Process** | Customer Documentation | Incomplete Legal Agreement | Inadequate Checklist |
| **Systems** | Availability | Hardware Failure | Redundancy Architecture Gap |
| **Systems** | Integrity | Data Corruption | Change Management Failure |
| **External** | Third-Party Failure | Processor Outage | Vendor Bankruptcy |
| **External** | Physical Security | Natural Disaster | Unplanned Power Outage |

Process Owners must classify loss events to Level 3 at a minimum. Major events (gross impact >$100,000 USD) require Level 4 classification.

### 5.2 Risk and Control Self-Assessment (RCSA)

The RCSA is the foundational process for operational risk identification and assessment. It is executed semi-annually.

**Step 1: Planning and Scoping (2LOD Lead)**
1.  ORM Partner extracts the current Business Function Registry from `MER-GRC`.
2.  ORM Partner and VP of Financial Services align on the RCSA campaign calendar. The Q1 campaign focuses on payment initiation to settlement. The Q3 campaign focuses on treasury reconciliation and third-party reporting.
3.  A kick-off communication is sent to all nominated Process Owners, including links to the RCSA questionnaire and supporting data (KRIs, recent loss data).

**Step 2: Risk Identification Workshop (1LOD Lead, 2LOD Facilitator)**
1.  Each Process Owner schedules a 2-hour workshop with their team.
2.  Using the Risk Taxonomy (§5.1), the team identifies all potential operational risks for the in-scope process.
3.  For each identified risk, the team nominates the corresponding key controls that are currently operating.

**Step 3: Risk and Control Assessment (1LOD Lead)**
1.  For each **Inherent Risk**, the Process Owner assigns an Impact score (1-5 scale) and a Likelihood score (1-5 scale) assuming all controls are absent.
2.  For each **Control**, the Process Owner assigns a Design Effectiveness score (1-4 scale) and an Operating Effectiveness score (1-4 scale). Supporting evidence (e.g., `GRC-RECORD` report, latest test script) must be attached to the `MER-GRC` entry.
3.  The system calculates the **Residual Risk** score automatically. The formula used by the GRC engine is: `Residual = Inherent - (Design Effectiveness * 0.4 + Operating Effectiveness * 0.6)`. A residual risk score of “High” (15+) or “Very High” (20+) triggers a mandatory remediation plan.

**Step 4: Review and Challenge (2LOD Lead)**
1.  The ORM Partner reviews every submitted assessment within ten (10) business days.
2.  The ORM Partner challenges assessments where (a) the residual risk seems understated, or (b) control effectiveness is not supported by objective evidence.
3.  Any disagreement is escalated to the VP of Financial Services for resolution.

**Step 5: Sign-Off and Publication**
1.  The final, agreed-upon RCSA results are submitted to the Operational Risk Committee for ratification.
2.  The ratified risk profile is published to the `MER-GRC` “Live Risk Register” dashboard, accessible to all 1LOD leaders.

### 5.3 Loss Event Capture, Classification, and Remediation

A standardized loss data capture process ensures a reliable historical database for risk analysis.

**Step 1: Event Discovery**
Any Covered Person who discovers a realized loss event or near-miss must report it to their Process Owner within twenty-four (24) hours of discovery.

**Step 2: Initial Recording**
1.  The Process Owner must create a new record in the `MER-GRC` “Loss & Near-Miss” Log (Module: `GRC-LOSS`) within two (2) business days of being notified.
2.  The following metadata categories are mandatory:
    - Event Date (Date of occurrence)
    - Discovery Date
    - Classification (using Taxonomy §5.1)
    - Gross Financial Impact (Estimated)
    - Recovery Value (Estimated)
    - Status = “Open: Under Investigation”

**Step 3: Root Cause Analysis (RCA)**
1.  For events with gross impact >$10,000 USD, the Process Owner must complete a formal Root Cause Analysis within ten (10) business days.
2.  The RCA must identify the primary and contributing Level 4 causal factors.
3.  The RCA report is attached to the `GRC-RECORD`.

**Step 4: Remediation Plan Creation**
1.  The Process Owner creates a Corrective Action Plan (CAP) within the `GRC-RECORD`.
2.  The CAP defines specific, measurable actions, an owner for each action, and a target completion date.
3.  The CAP must be approved by the ORM Partner.

**Step 5: Event Closure**
The `GRC-RECORD` can only be closed once all CAP actions are completed and validated, the final gross loss is booked, and any insurance recovery has been finalized. All relevant documentation must be attached.

**Step 6: Near-Miss Tracking**
Near-miss events, where no actual financial loss occurred, follow the same procedure but are marked with `Loss Type = Near-Miss`. The investigation report must detail why a loss was fortuitously avoided. Near-miss data is aggregated monthly to identify emerging risk clusters.

### 5.4 Key Risk Indicator (KRI) Lifecycle

KRIs are critical for forward-looking risk monitoring.

**Step 1: KRI Selection and Design**
1.  The ORM Partner, in consultation with Process Owners, selects a candidate KRI for each “High” or “Very High” residual risk identified in the RCSA.
2.  Each KRI must be formally documented in the `GRC-MODULE-KRI` application with a defined purpose, data source (referencing the `FIN-DATA-LAKE` report ID), formula, and collection frequency.

**Step 2: Threshold Setting**
All KRIs utilize a three-tier threshold system, visually represented as Green, Amber, and Red.

| Threshold Zone | Description | Action Requirement |
|---|---|---|
| **Green** | Risk is operating within appetite. | No action. Routine monitoring. |
| **Amber** | Risk is approaching the boundary of appetite. | Process Owner must investigate and note the rationale for the breach in `MER-GRC` within 5 business days. A remediation plan may be requested by the ORM Partner. |
| **Red** | Risk is out of appetite. | Automatic escalation (see §8.1). A mandatory 48-hour investigative response is required. |

**Step 3: Data Collection and Validation**
1.  The 1LOD Data Steward runs the source data query as per the collection frequency (Daily, Weekly, Monthly).
2.  Data is validated for completeness and imported into `MER-GRC`.

**Step 4: Breach Management and Escalation**
1.  An automated email alert is triggered by `MER-GRC` to the Process Owner and the ORM Partner when an Amber or Red threshold is breached.
2.  The Process Owner follows the escalation protocol defined in §8.1.

### 5.5 Model Risk Management (SR 11-7 Alignment)

This procedure governs quantitative tools used for KRI projection, loss forecasting, transaction monitoring rules, and operational risk capital estimation.

**Step 1: Model Inventory**
The ORM Partner maintains a complete, living inventory of all Financial Services operational risk models in the `MODEL-INVENTORY` database. Each model entry contains:
- Model Name and Version
- Model Owner (1LOD Business Lead)
- Purpose and Use Case (e.g., “Operational Risk Capital Model”, “Real-time Fraud KRI Projection”)
- Input Data Sources and Assumptions
- Output Variables
- Date of Last Independent Review

**Step 2: Model Documentation (Conceptual Soundness)**
Prior to deployment, and after any major revision, the Model Owner prepares a comprehensive documentation package. This package must detail data sources, variable selection rationale, theoretical basis, and methodology.

**Step 3: Independent Review**
The 2LOD Model Validation team performs an independent review of all registered models prior to initial deployment and upon a significant change. The review includes an assessment of conceptual soundness, data quality, and outcomes analysis.

**Step 4: Ongoing Monitoring**
After deployment, the Model Owner performs ongoing monitoring to verify the model’s continued fit-for-purpose. This includes comparing realized losses to projections and analyzing the frequency and severity of risk events against model expectations. Results of the monitoring are reported to the Operational Risk Committee annually.

---

## 6. Controls and Safeguards

The control environment is a multi-layered defense system. This section details specific controls mandated by this SOP.

### 6.1 Preventative Controls

| Control ID | Control Description | Purpose | Automated (Y/N) |
|---|---|---|---|
| `FIN-CTL-001` | Segregation of Duties in `FIN-CORE` | No single user can create and approve a payment instruction over $250,000. | **Y** |
| `FIN-CTL-002` | Input Validation | All data fields on `FIN-ONBOARD` customer-facing portals have strict server-side validation rules for format and value limits. | **Y** |
| `FIN-CTL-003` | Physical Access Biometrics | Access to the primary data center (`DC-ATL-01`) requires two-factor biometric authentication. | **Y** |
| `FIN-CTL-004` | Change Management CAB | All production changes to `FIN-SYS-*` assets require approval from the Change Advisory Board (CAB), documented in `MER-SM-TOOL`. | **N** (Manual Process Flow) |

### 6.2 Detective Controls

| Control ID | Control Description | Purpose | Cadence |
|---|---|---|---|
| `FIN-CTL-010` | Daily Reconciliation | An automated three-way reconciliation between `FIN-CORE` ledger, processor gateway settlement files, and nostro account agent bank reports. Breaks are logged in `GRC-LOSS`. | **Daily** |
| `FIN-CTL-011` | System Health Monitoring | Infrastructure health is monitored via `MON-NODE`. Application-level synthetic transactions test the `FIN-PAY-LOGIN` and `FIN-PAY-SUBMIT` journeys. | **Continuous** |
| `FIN-CTL-012` | Independent RCSA Review | The 2LOD ORM Partner performs an independent review of all RCSAs, challenging the effectiveness of controls where evidence is insufficient. | **Semi-Annual** |

### 6.3 Corrective Controls

| Control ID | Control Description | Trigger |
|---|---|---|
| `FIN-CTL-020` | Root Cause Analysis (RCA) | Triggered by a major incident (P1/P2) or any loss event exceeding $10,000. Formal reporting required in `GRC-RECORD`. |
| `FIN-CTL-021` | Remediation Plan Management | Triggered by an out-of-appetite residual risk, a Red KRI breach, or a critical audit finding. Progress is tracked by the ORM Partner. |
| `FIN-CTL-022` | Business Continuity Plan (BCP) | Triggered by a catastrophic site failure. Defines the transition of critical services (Payment Switching, Reconciliation) to the secondary site (`DC-PHX-02`). |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Monitoring

Operational Risk monitoring is conducted at three levels:

1.  **Real-Time (System-Level):** The Network Operations Center (NOC) monitors `FIN-PAY-*` application health, synthetic transaction success rate, and processing queue depth using dashboards in `MON-NODE`. Alerts are dispatched to Level 1 Engineering.
2.  **Periodic (Process-Level):** Process Owners monitor their KRI dashboards within `MER-GRC` at a frequency defined in the KRI's metadata. The ORM Partner monitors the aggregate suite of all Financial Services KRIs.
3.  **Ad-Hoc (Event-Driven):** Monitoring is automatically escalated when a critical incident is declared via the Major Incident Management (MIM) process.

### 7.2 Key Metrics and Reporting Cadence

The ORM Partner produces a suite of reports on a standard cadence.

| Report Name | Audience | Frequency | Content |
|---|---|---|---|
| **Financial Services ORM Dashboard** | VP, Financial Services (R. Liu) | **Weekly** | Top 5 KRIs by distance from Red threshold; New loss events logged this week; Open MIM incidents; % of past-due CAP actions. |
| **Operational Risk Profile Pack** | Operational Risk Committee (ORC) | **Monthly** | Full KRI catalogue status; Monthly loss data summary (total count, aggregate value); RCSA remediation progress; Top 10 emerging risks. |
| **Operational Risk Capital Update** | CFO (J. Thornton) | **Quarterly** | Projected vs. Actual Loss trends; Summary of model monitoring validation; Qualitative commentary on the top 5 operational risks. |
| **Board Risk Summary** | Audit & Risk Committee (Board) | **Quarterly** | Consolidated risk profile for Financial Services; Major control failures; Material regulatory engagement on operational risk matters. |

### 7.3 System Availability Commitment (SOC 2 Alignment)

Meridian commits to maintaining a high standard of operational resiliency for its Financial Services platforms. The performance of the systems underpinning the `FIN-SYS-*` stack is monitored continuously. A Major Incident Management (MIM) process is invoked whenever a priority-defined degradation of service occurs. Our commitment is to the timely restoration of service, with targets defined based on the business criticality tier of the impacted system, as documented in the `FIN-BCP-PLAN` document.

---

## 8. Exception Handling and Escalation

### 8.1 Escalation Paths

Formal escalation paths ensure that risk information reaches the appropriate level of authority without delay.

| Trigger Event | Immediate Recipient | Escalation To (If unresolved within 24h) | Escalation To (If unresolved within 72h) |
|---|---|---|---|
| **Red KRI Breach** | Process Owner & ORM Partner | VP, Financial Services (R. Liu) | CFO (J. Thornton) |
| **Major Operational Incident (P1)** | Incident Commander (Tech Lead) | Head of Infrastructure & VP Fin Svcs | Group CIO & CFO |
| **Confirmed Internal Fraud** | Head of Compliance & ORM Partner | Group General Counsel | CEO |
| **RCSA Remediation Plan >30 Days Past Due** | ORM Partner | VP, Financial Services | CFO |

### 8.2 Exception Management

An exception is defined as a formal, time-bound approval to deviate from a specific mandatory procedure or control requirement of this SOP.

**Procedure to Request an Exception:**

1.  The Process Owner must log a request in the `MER-GRC` “Exception Manager” module. The request must include:
    - The specific SOP section from which deviation is requested.
    - A detailed justification for the business need.
    - A compensating control proposed to mitigate the risk during the exception period.
    - The requested exception duration (maximum 12 months).
2.  The ORM Partner reviews the request and provides a risk opinion.
3.  For exceptions related to a SOX or ICFR-relevant process, the CFO must be consulted.
4.  Approval Authority:
    - Exceptions with a duration < 90 days and a minimal residual risk increase: **VP, Financial Services (R. Liu)** .
    - All other exceptions: **CFO (J. Thornton)** .

All approved exceptions are centrally logged and reviewed quarterly by the Operational Risk Committee.

---

## 9. Training Requirements

### 9.1 Mandatory Training

| Training Module | Target Audience | Frequency | Method |
|---|---|---|---|
| **ORM Foundations: SOP-FIN-009** | All Financial Services employees | **Annual** | Computer-Based Training (`MER-LMS`) + Knowledge Check |
| **RCSA Facilitator & Process Owner** | 1LOD Process Owners & 2LOD ORM Partners | **Annual** | Live Virtual Workshop |
| **Loss Event Classification & RCA** | 1LOD Process Owners, Team Leads | **Annual** | Case-Study Based Assessment |
| **Conduct Risk and Fraud Reporting** | All Covered Persons | **Semi-Annual** | Computer-Based Training (`MER-LMS`) |

### 9.2 Role-Based Training

A newly appointed Process Owner must complete the “RCSA Facilitator & Process Owner” live workshop within thirty (30) days of assuming the role. The ORM Partner is responsible for tracking completion and following up with any non-compliant individual’s manager.

### 9.3 Records Management

All training completion records are centrally managed in the `MER-LMS` platform. The ORM Partner supplies a training completion report to the VP of Financial Services monthly.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Group Policies

| SOP / Policy ID | Document Title |
|---|---|
| `SOP-TRS-001` | Market Risk Management |
| `SOP-TRS-003` | Liquidity Risk Management |
| `SOP-CRD-012` | Institutional Credit Risk Management |
| `SOP-TECH-014` | Major Incident Management (MIM) |
| `SOP-TECH-003` | Change Management |
| `SOP-GRC-001` | GRC Platform Usage Standards |
| `POL-HR-005` | Code of Conduct and Whistleblower Policy |
| `FIN-BCP-PLAN` | Financial Services Business Continuity Plan |
| `FIN-DATA-GOV` | Financial Data Governance Standard |

### 10.2 External Regulatory and Standards References

- **Board of Governors of the Federal Reserve System, SR Letter 11-7:** "Guidance on Model Risk Management".
- **AICPA TSC 2017 (SOC 2):** CC7.1, CC7.2, CC7.3 (Systems Operations – Change Management, Monitoring of System Components, & Availability).
- **Basel Committee on Banking Supervision (BCBS 195):** "Principles for the Sound Management of Operational Risk".
- **ISO 31000:2018:** Risk Management – Guidelines.

---

## 11. Revision History

The following table records the revision history for this document. Version numbers follow the standard Meridian scheme: `Major.Minor`.

| Version | Date | Author | Section(s) Modified | Summary of Change |
|---|---|---|---|---|
| **1.0** | 2019-03-15 | J. Miller (ORM) | All | Initial creation of the Operational Risk Management SOP for the newly formed Financial Services unit. |
| **2.1** | 2020-09-21 | R. Liu (Fin Svcs) | §5.3, §11 | Revised loss event thresholds from $5,000 to $10,000 to align with updated materiality matrix. Amended RACI for Loss Event process. |
| **3.0** | 2022-01-10 | S. Chen (2LOD) | All | Major revision to incorporate SR 11-7 alignment for model risk, restructure the KRI section, and integrate the `MER-GRC` tool references after system go-live. Version upgraded to 3.0. |
| **4.0** | 2024-06-05 | P. Davies (ORM) | §5.2, §7.2 | Overhauled RCSA procedure to shift from annual to a semi-annual rhythm. Added new monthly ORC reporting template. Updated KRI breach management timelines. |
| **4.5** | 2025-03-22 | R. Liu (Fin Svcs) | §5.5, §6.2 | Refined model risk monitoring procedures and clarified the independent review role of the 2LOD Model Validation team. Amended system health monitoring controls. |
| **4.6** | 2025-08-14 | P. Davies (ORM) | §7.3, §8.2 | Updated SOC 2 alignment statement for system availability. Clarified exception process approval authorities. |
| **4.7** | 2025-11-27 | R. Liu (Fin Svcs) | §5.5, §7.2, §10.2 | Updated model documentation standards and ongoing monitoring requirements to align with SR 11-7. Refreshed reference to internal business continuity plan. Updated next review date. |
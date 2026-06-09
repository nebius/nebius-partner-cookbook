---
sop_id: "SOP-LEGC-012"
title: "Board and Committee Governance"
business_unit: "Legal & Compliance"
version: "1.6"
effective_date: "2025-08-23"
last_reviewed: "2026-08-07"
next_review: "2027-02-21"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "SOC 2"
  - "SR 11-7"
status: "Active"
---

# Standard Operating Procedure: Board and Committee Governance

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the formal governance framework for the Board of Directors (the "Board") of Meridian Health Technologies, Inc. ("Meridian" or the "Company") and all subordinate governance committees. The purpose is to define clear roles, responsibilities, meeting cadences, reporting requirements, and recordkeeping standards to ensure effective oversight of strategic objectives, regulatory compliance, financial integrity, and risk management. This framework is designed to satisfy the governance criteria required under SOC 2 (Trust Services Criteria, specifically CC1.1 through CC5.3) and the model risk management governance expectations set forth in Federal Reserve Supervisory Letter SR 11-7, as they apply to the Company's HealthPay Financial Services business line.

### 1.2 Scope
This SOP applies to all members of the Meridian Health Technologies Board of Directors, all standing and ad-hoc committees of the Board, and all Meridian employees, contractors, and consultants who prepare materials, present reports, or provide administrative support to these governance bodies. The SOP governs the activities of the following standing committees:

- **AI Governance Committee** (Board-level, established 2020)
- **Audit Committee** (Board-level)
- **Risk Committee** (Board-level, encompassing Model Risk Management sub-function)
- **Compensation Committee** (Board-level)
- **Nominating and Governance Committee** (Board-level)
- **Clinical AI Ethics Subcommittee** (Sub-committee of the AI Governance Committee)
- **Model Validation Committee** (Management-level, reporting into the Risk Committee per SR 11-7)

Excluded from this scope are purely operational departmental meetings, Agile scrum ceremonies, and project-specific steering committees unless explicitly chartered by the Board. The governance of Meridian's EU subsidiary (Meridian Health Technologies GmbH) is covered by this SOP solely for matters escalated to the parent Board; local Works Council interactions are out of scope.

---

### 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **ADM** | Automated Decision-Making: The process of rendering a decision with legal or similarly significant effect concerning an individual, executed solely by automated processing without any substantive human analysis or intervention in the final decision logic. |
| **Board** | The Board of Directors of Meridian Health Technologies, Inc. |
| **CC1.x – CC5.x** | The Control Criteria (now Trust Services Criteria) defined by the AICPA for SOC 2 examinations, specifically the Common Criteria series related to Control Environment, Communication & Information, and Risk Assessment. |
| **Charter** | The formal, Board-approved document defining a committee’s mandate, authority, membership, and procedural rules. |
| **Clinical AI** | Any machine-learning model, algorithm, or statistical system used to support, inform, or render clinical diagnostic, prognostic, or triage decisions. This includes CE-marked Software as a Medical Device (SaMD) under EU MDR. |
| **Consent Order** | A formal directive or agreement with a regulatory body (e.g., FTC, OCR) imposing specific corrective governance actions. |
| **Executive Session** | A closed portion of a Board or Committee meeting attended exclusively by non-management directors (and, if applicable, the Chief Compliance Officer as legal counsel) without the presence of the CEO or any other members of management. |
| **KPI** | Key Performance Indicator. |
| **MDM** | Meridian Decision Manager, the Company’s proprietary central rules engine used for credit risk scoring and automated underwriting decisions within the HealthPay Financial Services business line. |
| **NIST AI RMF** | National Institute of Standards and Technology Artificial Intelligence Risk Management Framework 1.0. |
| **Model** | A quantitative method, system, or approach that applies statistical, economic, financial, or machine learning theories, techniques, and assumptions to process input data into quantitative estimates. (Per SR 11-7 definition). |
| **SR 11-7** | Federal Reserve Supervisory Letter SR 11-7, “Guidance on Model Risk Management.” |
| **TSC** | Trust Services Criteria (SOC 2). |

---

### 3. Roles and Responsibilities

This section establishes a Responsibility Assignment Matrix (RACI) for core governance activities. Specific procedural responsibilities are detailed in Section 5.

| Activity / Deliverable | Board Chair (Dr. Elena Rossi) | Committee Chair | Committee Members | CCO (Thomas Anderson) | GC (Maria Gonzalez) | CTO (Dr. Aris Thorne) | Business Unit Owners |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Board & Committee Chartering** | A | R | C | C | C | I | I |
| **Annual Board Effectiveness Evaluation** | A/R | R | C | I | I | I | I |
| **Meeting Agenda Setting** | C | A/R | C | C | C | I | I |
| **Minutes Drafting & Finalization** | I | A | C | R | C | I | I |
| **Retention of Records (Per Policy)** | I | I | I | A/R | I | I | I |
| **Regulatory Reporting (Consent Orders)** | I | I | I | R | A | I | I |
| **Model Inventory Validation (SR 11-7)** | I | A (Risk Comm) | I | I | I | R | I |
| **Material Risk Factor Escalation** | I | A | R | R | I | C | C |
| **SOC 2 Common Criteria Control Oversight** | A | R | I | R | I | I | C |
| **AI Bias Audit Scheduling** | I | A (AI Gov) | I | C | C | R | C |

*R=Responsible (executes), A=Accountable (approves), C=Consulted, I=Informed*

#### 3.1 Named Governance Roles
- **Board Chair:** Dr. Elena Rossi
- **AI Governance Committee Chair:** Dr. Aris Thorne (CTO)
- **Risk Committee Chair:** Dr. Marcus Chen (Independent Director, Financial Risk Expert)
- **Audit Committee Chair:** Sarah Jenkins, CPA (Independent Director)
- **Chief Compliance Officer (CCO) & Corporate Secretary:** Thomas Anderson
- **General Counsel (GC):** Maria Gonzalez

---

### 4. Policy Statements

4.1 **Commitment to Transparency:** Meridian is committed to providing clear, meaningful, and accessible information to individuals subject to purely automated decisions. No automated system shall render a decision with a material legal or financial consequence to a consumer or patient without a documented human override pathway or post-hoc human review capability, consistent with regulatory requirements.

4.2 **Duty of Documentation:** All governance meetings that address financial reporting controls (SOX-scope), model risk evaluation (SR 11-7 scope), or AI trustworthiness characteristics (NIST AI RMF scope) shall be meticulously documented. Meeting minutes shall constitute prima facie evidence of the Board and Committees' exercise of their fiduciary duty of care.

4.3 **Committee Authority:** Committees operate as delegations of the full Board. No Committee shall exceed its chartered authority. Any material policy deviation or waiver must be escalated to the full Board for ratification at the subsequent regular meeting, except in exigent circumstances detailed in Section 8 (Exception Handling).

4.4 **Model Governance Standard:** All models, irrespective of their deployment line (Clinical AI or Financial HealthPay), shall adhere to a three-lines-of-defense model governance standard adapted from SR 11-7: Model Owners (1st Line), Model Validation Committee (2nd Line), and Internal Audit (3rd Line).

---

### 5. Detailed Procedures

#### 5.1 Charter Management

##### 5.1.1 Committee Charter Creation and Amendment
1.  The Committee Chair, in conjunction with the CCO, drafts or redlines the Charter using the official Meridian template (LEGC-TEMP-004) stored in the Diligent Governance Cloud.
2.  The draft must explicitly state:
    - Committee Purpose and Scope Alignment to specific Trust Services Criteria (CC1.1, CC1.2).
    - Specific Financial Delegation Authority limits (e.g., CapEx approval limit of $5M beyond pre-approved budget).
    - Membership requirements, including minimum independence thresholds.
3.  The GC conducts a legal sufficiency review within five (5) business days.
4.  The draft Charter is submitted to the full Board as a consent agenda item. Approval requires a simple majority vote.
5.  **Cadence:** All charters must be reviewed and reaffirmed annually at the first Q1 Board meeting. Amendments outside this cycle follow the steps above and are logged in the Board Resolution Log (LEGC-LOG-022).

#### 5.2 Meeting Cadence and Attendance

##### 5.2.1 Standard Meeting Cadence
The official Meridian governance calendar is published by the CCO’s office annually by November 1st for the subsequent fiscal year via Outlook Calendar, and hosted on the Diligent Boards portal.

| Governance Body | Cadence | Duration | Quorum |
| :--- | :--- | :--- | :--- |
| **Board of Directors** | Quarterly (Q1-Q4), plus Annual Strategy Retreat | 6 hours / 2 days (Retreat) | Simple Majority of seated Directors |
| **AI Governance Committee** | Bi-monthly (6x/year), offset from Board months | 3 hours | Chair + 50% of Members |
| **Audit Committee** | Quarterly (4x/year), pre-aligned to Earnings cycle | 4 hours | Chair + 50% of Members |
| **Risk Committee** | Quarterly (4x/year) | 4 hours | Chair + 50% of Members |
| **Model Validation Committee** | Monthly (12x/year) | 90 minutes | Chair (Chief Model Risk Officer) + 2 Analysts |

##### 5.2.2 Executive Sessions
The Audit Committee and Risk Committee must hold private Executive Sessions immediately following the conclusion of the regular open session. The CCO serves as secretary and counsel exclusively to the Committee members in these sessions. No management minutes are distributed; notes are retained solely by the CCO in a restricted-access folder within the Legal Board Repository.

#### 5.3 Meeting Preparation and Material Distribution

##### 5.3.1 Pre-Reads and Board Books
1.  **T-14 Days:** Agenda owner (usually Committee Chair or CEO) submits agenda and pre-read assignment mapping to CCO.
2.  **T-10 Days:** Business Unit Owners upload final, approved slide decks and written reports to the Diligent Board Portal. Late submissions must be approved by the Committee Chair.
3.  **T-7 Days:** CCO publishes the locked digital Board Book. All materials must include:
    - A “Cover Memo” summarizing the ask (Decision vs. Informational).
    - A “Risk Factors” box highlighting SR 11-7 model changes or SOC 2 control deviations relevant to the presentation.
4.  **Hard Copy Exception:** Physical board books are prohibited except for the Annual Security Breach Tabletop Exercise, where they are distributed and destructed on-site under chain-of-custody control.

#### 5.4 Meeting Execution

##### 5.4.1 Standard Agenda Flow
1.  **Call to Order & Administrative Items:** Approval of prior meeting minutes.
2.  **Strategic & Business Updates:** CEO Report (Board) or Business Unit Deep Dives.
3.  **Core Governance Topics:**
    - **Risk Committee:** Review of “High-Risk” Model Inventory Dashboard (Meridian-Pulse system). Validation of remediation closures per SR 11-7 Section IV.
    - **AI Governance:** Review of Algorithmic Impact Assessments (AIA) for new Clinical AI features. Bias audit disposition.
4.  **Consent Agenda:** Routine, non-controversial approvals voted en bloc.
5.  **Executive Session:** Closed-door governance.
6.  **Wrap-Up & Action Item Review:** Formal assignment of action owners and due dates.

#### 5.5 Reporting Requirements

##### 5.5.1 AI Governance Committee to Board of Directors (Quarterly)
The AI Governance Committee Chair must deliver a “State of AI Risk” report containing:
- A RAG (Red-Amber-Green) status overview of all “Tier 1” Clinical AI models.
- Key Performance Indicators on automated decision override rates (expected threshold: >10% manual review bypass must trigger Risk Committee notification).
- Status of any deviation from NIST AI RMF Playbook.

##### 5.5.2 Risk Committee to Board of Directors (Quarterly)
Report must include explicit SR 11-7 attestation language:
> “The Risk Committee certifies that, to the best of its knowledge, the model risk management function has been performed independently... [the] inventory of models is accurate, and no critical findings remain unmitigated beyond the target remediation date.”

#### 5.6 Minutes and Records

##### 5.6.1 Minutes Content Standard
Minutes shall constitute a written record of the proceedings. Minimum elements:
- Date, Time, Location (Virtual/Physical), Attendance list with guest designation.
- A clear delineation of “Discussions” vs. “Deliberations.”
- A verbatim record of all formal resolutions (e.g., “RESOLVED, that the Board approves...”).
- A specific appendix capturing the “SR 11-7 Model Finding Disposition Log” for Risk Committee meetings.

##### 5.6.2 Approval Process
1.  **Draft Distribution:** CCO distributes draft minutes via Diligent in-suite editor within seven (7) business days.
2.  **Review:** Members provide tracked-changes edits within five (5) business days.
3.  **Finalization:** CCO resolves edits, produces a final “Clean” and “Redline” version.
4.  **Ratification:** Final minutes formally approved via consent agenda at the next regularly scheduled meeting.

---

### 6. Controls and Safeguards

#### 6.1 SOC 2 Trust Services Criteria (TSC) Controls Mapping
The governance oversight controls established in this SOP satisfy the following SOC 2 Common Criteria (COCO principles). The Control Owner for all mapped controls is the CCO, unless otherwise stated.

| SOC 2 Control ID | Control Activity | Frequency | Verification Method |
| :--- | :--- | :--- | :--- |
| **CC1.1** | The Board evaluates its own performance against the chartered duty of care annually via Diligent self-assessment. | Annual | Review of assessment reports by Audit Committee Chair. |
| **CC1.2** | Committee Charters explicitly establish independence requirements (Audit, Risk, Comp Committee must be comprised of 100% independent directors). | Annual Reaffirmation | GC legal opinion memo confirming independence. |
| **CC2.2** | Internal Audit communicates the annual SOC 2 examination scope and plan directly to the Audit Committee without management filtering. | Quarterly | Audit Committee Private Session Agenda item. |
| **CC2.3** | A whistleblower hotline report summary (anonymized) is formally discussed by the Audit Committee. Reporting line is direct: “EthicsPoint > Audit Committee Chair.” | Quarterly | Hotline report metrics reviewed against SOP-HR-005. |
| **CC3.3** | The Board reviews and formally votes on tolerance thresholds for the Risk Appetite Statement (RAS), especially regarding FinTech credit loss models. | Annual | Board Consent Agenda Resolution. |
| **CC5.2** | Deviations from standard vendor risk tiering for “nth-party” AI data sources must be presented to the Audit Committee for ratification. | Ad-hoc / Material Events | GC review of supplier contract deviation. |

#### 6.2 SR 11-7 Specific Controls
These controls are specific to the oversight of models within the HealthPay Financial Services business line, ensuring strict adherence to the Supervisory Guidance.

| SR 11-7 Section | Control Requirement | Implementation Specifics | Control Owner |
| :--- | :--- | :--- | :--- |
| **Section III, Model Validation** | Independent review of model validation reports. | The **Model Validation Committee** reviews validation findings. No Model Owner may approve their own model’s validation. | Chief Model Risk Officer (CMRO) |
| **Section IV, Governance** | Define model materiality tiers. | Tier 1 (High Materiality: MDM Credit Scoring, Clinical SaMD). Tier 2 (Medium: Patient Churn Propensity). Tier 3 (Low: Breakroom vending supply optimization). | Risk Committee Chair |
| **Section V, Internal Audit** | Annual audit of MRM framework. | Internal Audit performs an independent assessment of the Model Validation Committee’s adherence to this SOP and SR 11-7 guidance. The audit report goes directly to the **Audit Committee**. | Director of Internal Audit |
| **Deviation Challenge** | Process for challenging model findings. | Any Tier 1 model finding rated “High Risk” cannot be closed solely by the CTO. Closure must be reviewed and accepted by a Quorum of the **Model Validation Committee**. | CMRO |

#### 6.3 Information Security Safeguards
- **Board Portal:** All governance records are maintained exclusively within the Diligent Boards portal (SOC 2 Type II certified by Diligent Corporation). The Corporate Secretary’s local workstation must not cache Board materials locally.
- **PIM/PAM:** Privileged Identity Management (PIM) on Azure AD enforces Just-In-Time (JIT) access for IT admins accessing the Diligent governance tenant. Access reviews must be conducted by the CCO quarterly.

---

### 7. Monitoring, Metrics, and Reporting

#### 7.1 Governance Performance Metrics (KPIs)
To ensure the governance process is operating effectively, the CCO tracks the following quarterly KPIs and presents a scorecard to the Nominating and Governance Committee:

- **Director Onboarding TAT:** Time (in days) from appointment to completion of regulated entity orientation. (Target: ≤30 days).
- **Materials On-Time Delivery Rate:** Percentage of Board Book items uploaded by the T-10 business day deadline. (Target: ≥95%).
- **Minutes Timeliness:** Average elapsed business days from meeting date to distribution of draft minutes. (Target: ≤7 business days).
- **Action Item Closure Rate:** Percentage of action items closed within the assigned due date before the subsequent meeting. (Target: ≥90%). SR 11-7 remediation items have a zero-tolerance aging policy; they cannot age beyond the agreed date without formal Risk Committee extension approval.

#### 7.2 SR 11-7 Model Inventory Dashboard
The CTO, in coordination with the CMRO, maintains a dynamic dashboard in the Meridian-Pulse system that visualizes:
- Total count of models in the inventory, segmented by Materiality Tier and Business Line.
- “Evergreen Status” — Last validation date; a model that has not been validated within 12 months is flagged “Inactive/Non-Compliant.”
- Findings Severity Treemap (Critical/High/Medium/Low).
- Planned vs. Actual Remediation Progress for all Critical and High findings.

#### 7.3 SOC 2 Governance Maturity Scorecard
Annually, prior to the SOC 2 Type II audit period kick-off, the CCO performs a self-assessment of governance maturity against TSC Criteria. The scale is defined as:
- **Level 1 (Initial):** Ad-hoc, undocumented.
- **Level 2 (Defined):** Processes defined and documented (Current Baseline).
- **Level 3 (Managed):** Metrics tracked and reviewed actively.
- **Level 4 (Optimized):** Machine-learning-driven compliance process re-engineering.

The target is to maintain **Level 3** across all CC1.x and CC5.x criteria. Any regression to Level 2 triggers a remediation plan to be approved by the Audit Committee.

---

### 8. Exception Handling and Escalation

#### 8.1 Charter Emergency Bypass
In the event of a exigent material risk (e.g., a zero-day exploit affecting SaMD models or a sudden risk of insolvency), the Board Chair, CCO, and GC are jointly authorized to execute a written consent resolution in lieu of a formal meeting, bypassing the standard T-10 day material submission rule. This action must be ratified by the full Board via unanimous written consent within 48 hours. The action is retroactively documented in the Diligent portal as “Emergency Consent Resolution.”

#### 8.2 SR 11-7 Model Deviation Exceptions
If a Model Owner requests a temporary waiver from a Critical Finding remediation deadline, the Model Validation Committee reviews the request. Approval requires:
1.  Quantified risk acceptance from the Business Line Owner.
2.  Technical analysis by an independent model validator justifying why the model can remain in production without posing material safety & soundness risk.
3.  Formal vote of the Risk Committee to accept the residual risk.

No Critical Finding waiver shall extend a remediation beyond an original due date + 90 days without a full re-validation exercise.

---

### 9. Training Requirements

#### 9.1 Board Orientation (Role-Specific)
Newly appointed Directors must complete the “Meridian Governance & Compliance Onboarding” Learning Path in Workday Learning within 30 days of appointment. Modules include:
- SOP-LEGC-012 (This document).
- SOP-IS-001 (Data Classification and Handling).
- Anti-Bribery and Anti-Corruption (ABAC) for Directors.
- HealthPay Regulatory Landscape and SR 11-7 Foundations.
- Clinical AI MDR Regulatory 101.

#### 9.2 Continuing Education (Annual)
All standing Board and Committee members must complete the following annual refreshers via Diligent’s integrated Learning Manager:
- **Cybersecurity and AI Risk Oversight (60 mins):** Covers the NIST AI RMF and recent threat actor profiles.
- **Financial Crime Prevention (30 mins):** Sanctions screening, AML.
- **Conflict of Interest Disclosures:** Annual submission using the automated Diligent COI questionnaire workflow.

Completion rates are tracked by the CCO’s office. Failure to complete by October 31st results in an automatic recusal from the Audit and Risk Committees until compliance is achieved.

---

### 10. Related Policies and References

#### 10.1 Internal Meridian SOPs
- **SOP-IS-001:** Data Classification and Handling Policy
- **SOP-HR-005:** Whistleblower Protection and Investigations Policy
- **SOP-RISK-022:** Model Risk Management Framework (HealthPay Business Line)
- **SOP-CLIN-101:** Clinical AI Algorithm Change Management
- **SOP-IA-003:** Internal Audit Charter and Methodology
- **SOP-REC-001:** Record Retention and Litigation Hold Policy

#### 10.2 External Standards and Regulatory Guidance
- **AICPA:** SOC 2 Trust Services Criteria (Current Version, as updated).
- **Federal Reserve:** SR Letter 11-7 (April 4, 2011), “Guidance on Model Risk Management.”
- **NIST:** AI Risk Management Framework 1.0 (AI RMF).
- **ISO/IEC:** 42001:2023 — Artificial Intelligence Management System.
- **EU MDR:** Regulation (EU) 2017/745 (Medical Devices).

---

### 11. Revision History

| Version | Date | Author/Editor | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2020-04-15 | T. Anderson | Initial creation: Established Board and Audit Committee governance. |
| 1.2 | 2022-01-20 | M. Gonzalez | Minor update: Inserted AI Governance Committee charter details post-Cinical SaaS launch. |
| 1.4 | 2023-11-09 | T. Anderson | Major revision: Integrated SR 11-7 specific controls for HealthPay FinTech oversight. Renamed “Risk Sub-committee” to “Model Validation Committee.” |
| 1.5 | 2025-03-01 | T. Anderson / A. Thorne (CTO) | Enhanced Section 5 (Detailed Procedures): Added Clinical AI Ethics Subcommittee. Expanded controls mapping for CC3.3 and CC5.2. |
| 1.6 | 2025-08-23 | T. Anderson | Comprehensive annual review. Updated Section 6.1 SOC 2 controls mapping to reflect updated examination scope. Added CEO and CTO formal review attestation. Updated Section 5.6.2 retention timeline from five years to “permanent” for critical resolutions per GC directive. |
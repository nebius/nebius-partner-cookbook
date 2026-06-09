---
sop_id: "SOP-FIN-002"
title: "Fraud Detection System Operations"
business_unit: "Financial Services"
version: "1.9"
effective_date: "2024-01-23"
last_reviewed: "2025-09-23"
next_review: "2026-03-23"
owner: "Robert Liu, VP of Financial Services"
approver: "James Thornton, Chief Financial Officer"
classification: "Internal"
regulations:
  - "SR 11-7"
  - "SOC 2"
  - "EU AI Act"
status: "Active"
---

# Standard Operating Procedure: Fraud Detection System Operations

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the operational framework governing Meridian Health Technologies, Inc.'s Fraud Detection System (FDS) within the HealthPay Financial Services business unit. The FDS protects the integrity of healthcare payment processing, patient financing, medical lending, and claims automation workflows processing approximately $4.2 billion annually. The purpose of this document is to define standardized procedures for the operation, monitoring, and continuous improvement of both rules-based fraud detection mechanisms and machine learning (ML) fraud detection models, ensuring the timely identification, triage, and resolution of potentially fraudulent transactions while minimizing false positive impacts on legitimate healthcare financial operations.

This SOP establishes the requirements for alert generation, investigation, escalation, and remediation workflows, as well as the governance structures required for model performance monitoring, validation, and change management.

### 1.2 Scope

This SOP applies to the following systems, personnel, and activities:

**In-Scope Systems:**
- HealthPay Transaction Monitoring Engine (HTME) — Real-time rules engine
- HealthPay ML Fraud Model v3.2 (HML-FM) — Production ML scoring model
- Fraud Case Management System (FCMS) — Alert triage and case management platform hosted on Meridian's AWS Private Cloud
- Fraud Analytics Workbench (FAW) — Investigation and reporting console
- Model training pipelines and feature stores supporting fraud detection

**In-Scope Activities:**
- Operation and tuning of fraud detection rules
- ML model inference, monitoring, and retraining
- Alert generation, triage, investigation, and disposition
- False positive analysis and rule/model adjustment
- Suspected fraud escalation to Compliance and Legal
- Regulatory reporting of confirmed fraud incidents
- Model validation and performance review activities

**In-Scope Personnel:**
- HealthPay Fraud Operations Team (Fraud Analysts Tier I-III)
- Fraud Data Science Team
- Financial Services Compliance Officers
- HealthPay Platform Engineering Team
- Model Governance Committee members

**Out of Scope:**
- Credit risk models (governed under SOP-RISK-001)
- Identity verification and Know Your Customer (KYC) controls (governed under SOP-COMP-005)
- Anti-Money Laundering (AML) transaction monitoring (governed under SOP-COMP-003)
- Investigation and prosecution of confirmed fraud by external law enforcement

### 1.3 Applicability

This SOP applies to all employees, contractors, and third-party service providers who operate, monitor, or interact with the HealthPay Fraud Detection System. Compliance with this SOP is mandatory and non-compliance shall be addressed per Meridian's disciplinary policy referenced in the Employee Handbook.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Alert** | A system-generated notification indicating a transaction or pattern has exceeded a defined risk threshold, requiring human review |
| **Case** | A structured investigation record created in FCMS from one or more related alerts, tracking the full lifecycle from triage to disposition |
| **Confirmed Fraud** | A case disposition where the preponderance of evidence supports a determination that fraudulent activity occurred |
| **False Positive (FP)** | An alert or case that, upon investigation, is determined to represent legitimate transaction activity |
| **Fraud Detection Rule** | A deterministic, logic-based condition evaluated against transaction attributes in real time |
| **ML Fraud Score** | A probabilistic risk score (0.000–1.000) output by the HML-FM model, representing the likelihood that a transaction or entity exhibits fraudulent characteristics |
| **Model Drift** | Degradation of model performance over time due to changes in the underlying data distribution, population characteristics, or adversary behavior |
| **Transaction Risk Score (TRS)** | The composite risk score calculated by combining rule triggers and the ML Fraud Score, used to determine alert priority |
| **True Positive Rate (TPR)** | The proportion of actual fraudulent transactions correctly identified by the system, calculated monthly |
| **Investigation SLA** | The maximum time permitted between alert generation and initial case triage action |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| **FDS** | Fraud Detection System |
| **HTME** | HealthPay Transaction Monitoring Engine |
| **HML-FM** | HealthPay Machine Learning Fraud Model |
| **FCMS** | Fraud Case Management System |
| **FAW** | Fraud Analytics Workbench |
| **TRS** | Transaction Risk Score |
| **FP** | False Positive |
| **FPR** | False Positive Rate |
| **TPR** | True Positive Rate |
| **SLA** | Service Level Agreement |
| **PSP** | Payment Service Provider |
| **TPRM** | Third-Party Risk Management |
| **RCA** | Root Cause Analysis |
| **COI** | Conflict of Interest |
| **SOC** | Service Organization Controls |
| **EAA** | EU AI Act |
| **MTTI** | Mean Time to Investigate |
| **MTTD** | Mean Time to Detect |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix

The following matrix defines the Responsible (R), Accountable (A), Consulted (C), and Informed (I) assignments for key FDS operational activities:

| Activity | Fraud Operations Lead | Fraud Analysts | Fraud Data Science | Platform Engineering | Compliance Officer | VP Financial Services | Model Governance Committee |
|---|---|---|---|---|---|---|---|
| Daily Alert Triage & Investigation | A | R | C | — | I | — | — |
| Rule Tuning & Threshold Adjustment | C | C | R | A | I | I | — |
| ML Model Retraining | — | — | R | A | — | I | C |
| False Positive Analysis | A | R | C | — | — | — | — |
| Confirmed Fraud Escalation | R | R | — | — | A | — | — |
| Model Performance Monitoring | — | — | R | C | — | — | A |
| Regulatory Reporting | — | — | — | — | R | I | — |
| Model Decommissioning Decision | — | — | C | — | — | A | R |
| Third-Party Model Validation | — | — | C | — | — | I | A |

### 3.2 Role Descriptions

**Fraud Operations Lead (Manager, Fraud Operations)**
- Owns day-to-day FDS operations and team performance metrics
- Approves rule threshold changes below the materiality threshold ($50,000 aggregate risk impact)
- Ensures staffing levels meet alert volume demands
- Conducts weekly case quality assurance reviews
- Reports monthly operational metrics to VP of Financial Services

**Fraud Analysts (Tier I, Tier II, Tier III)**
- Tier I: Performs initial alert triage, gathers transaction evidence, dispositions low-complexity cases within SLA
- Tier II: Investigates escalated cases, conducts in-depth transaction forensics, drafts Suspicious Activity Reports (SARs)
- Tier III: Performs complex fraud pattern analysis, assists data science with rule efficacy reviews, mentors Tier I/II analysts

**Fraud Data Science Team**
- Develops, trains, and retrains ML fraud detection models
- Conducts model performance monitoring and drift detection
- Performs feature engineering and variable selection
- Executes model validation activities as defined in Section 5.4
- Recommends model retirement or replacement to Model Governance Committee

**Platform Engineering Team (HealthPay)**
- Maintains HTME, FCMS, FAW, and model serving infrastructure
- Implements rule changes and ML model deployments in production
- Ensures system uptime meets 99.95% availability SLA
- Manages data pipelines feeding the FDS

**Compliance Officer (Financial Services)**
- Reviews and approves SAR filings prior to regulatory submission
- Confirms fraud incident classifications meet regulatory reporting criteria
- Liaises with Legal on confirmed fraud matters involving litigation risk
- Conducts semi-annual FDS compliance assessments against SOC 2 CC5.1–CC5.3 and EU AI Act Article 17 requirements

**VP of Financial Services (Robert Liu)**
- Serves as executive sponsor and SOP owner
- Approves material changes to fraud detection rules and ML models
- Authorizes exception requests exceeding standard deviation thresholds
- Represents FDS operations to external auditors during SOC 2 Type II examinations

**Model Governance Committee**
- Reviews and approves new ML model deployments
- Conducts annual model risk assessments
- Approves model retirement recommendations
- Maintains Meridian's enterprise model inventory

---

## 4. Policy Statements

### 4.1 Fraud Detection Principles

Meridian HealthPay Financial Services operates its Fraud Detection System under the following core principles:

**Proportionality:** Fraud detection controls shall be calibrated to the risk profile of the transaction type, payment channel, and merchant category. Screening intensity shall be proportionate to the assessed risk without imposing undue friction on legitimate healthcare financial transactions.

**Defense-in-Depth:** The FDS shall employ a layered detection architecture combining deterministic rules, machine learning models, and human investigation. No single detection mechanism shall serve as the sole basis for a confirmed fraud determination.

**Continuous Improvement:** Fraud detection rules and ML models shall undergo regular performance review. The system shall incorporate feedback loops from investigation outcomes to improve detection accuracy and reduce false positive rates over time.

**Fairness and Non-Discrimination:** ML fraud detection models shall be assessed for bias across protected characteristics relevant to healthcare financial services, consistent with EU AI Act Article 10(2)(f) requirements. No fraud detection rule shall explicitly target a protected class characteristic.

**Explainability:** ML model scores contributing to adverse actions (transaction blocking, account suspension) shall be accompanied by interpretable feature contribution explanations to the extent technically feasible, consistent with EU AI Act Article 14(4)(c) requirements for high-risk AI systems.

### 4.2 Model Governance Policy

All fraud detection models operating within the HealthPay FDS shall be subject to the Model Governance Framework established under this SOP and Meridian's Enterprise AI Governance Policy (SOP-AI-001). The Model Governance Committee maintains an inventory of all active fraud detection models.

Model risk assessments shall be conducted at initial deployment and annually thereafter. The model validation function shall periodically assess model conceptual soundness, data quality, outcomes analysis, and ongoing monitoring processes.

Validation findings are documented in a Model Validation Report and presented to the Model Governance Committee. No model validation activities may be performed by individuals who were directly involved in the model's development during the current validation cycle, in accordance with Meridian's Conflict of Interest Policy (SOP-HR-012).

### 4.3 Data Privacy and Retention

All fraud investigation records shall be retained for a minimum of seven (7) years from the date of case closure, consistent with financial records retention requirements under Meridian's Data Retention Schedule (REF-REC-001). Personally Identifiable Information (PII) within investigation records shall be pseudonymized after five (5) years unless an active legal hold applies.

Access to raw transaction data within the FAW shall be role-restricted. Fraud Analysts may access full transaction details for cases assigned to them. Bulk data export shall require Fraud Operations Lead approval and Compliance Officer acknowledgment.

### 4.4 EU AI Act Compliance (Article 17 — Quality Management System)

As a deployer of a high-risk AI system under the EU AI Act, Meridian maintains a quality management system proportionate to the risk classification of the HML-FM model. This SOP, in conjunction with SOP-AI-001, documents the technical and organizational measures Meridian employs to:

- Ensure the FDS operates in accordance with its intended purpose (Article 17(1)(a))
- Monitor FDS performance throughout its lifecycle (Article 17(1)(b))
- Retain logs automatically generated by the FDS for a period appropriate to the intended purpose (Article 17(1)(c))
- Ensure natural persons to whom human oversight is assigned have the necessary competence, training, and authority (Article 17(1)(d))
- Conduct data governance appropriate to the training, validation, and testing datasets (Article 17(1)(e))

---

## 5. Detailed Procedures

### 5.1 Fraud Detection Rule Management

#### 5.1.1 Rule Lifecycle

All fraud detection rules operating in HTME shall follow the defined lifecycle stages:

**Stage 1: Rule Proposal**
Any Fraud Analyst (Tier II+), Fraud Data Scientist, or Compliance Officer may propose a new fraud detection rule or modification to an existing rule. Rule proposals shall be documented using the **Fraud Rule Change Request Form (FR-CRF-001)** , which captures:
- Rule logic description (pseudocode or decision table)
- Business rationale and fraud typology addressed
- Expected transaction coverage (estimated daily volume impacted)
- Anticipated true positive and false positive rates
- Supporting data or investigation findings
- Proposed rule priority (Critical, High, Medium, Low)

**Stage 2: Impact Assessment**
Upon receipt of a completed FR-CRF-001, the Fraud Operations Lead shall conduct a Rule Impact Assessment within five (5) business days, evaluating:
- Operational impact on alert volumes and analyst workload
- Customer experience impact (legitimate transaction blocking risk)
- Interaction with existing rules (rule conflict detection)
- Regulatory implications (SAR filing thresholds, consumer disclosure requirements)

**Stage 3: Pre-Deployment Testing**
All proposed rule changes shall undergo a minimum fourteen (14) calendar day "shadow mode" evaluation prior to production activation. During shadow mode:
- The rule executes against live transactions but generates no blocking actions
- Alerts are generated in a test sandbox visible only to Fraud Data Science and the proposing party
- Daily shadow alert volumes are logged and reviewed for unexpected behavior
- A Pre-Deployment Test Report is generated summarizing shadow mode performance

**Stage 4: Approval**
Rule changes require the following approvals based on materiality:

| Materiality Tier | Criteria | Required Approvals |
|---|---|---|
| Minor | Expected alert volume change < 50 alerts/day AND no transaction blocking | Fraud Operations Lead |
| Moderate | Expected alert volume change 50–500 alerts/day OR limited blocking (specific merchant/channel) | Fraud Operations Lead + Compliance Officer |
| Major | Expected alert volume change > 500 alerts/day OR broad blocking rules OR new fraud typology | Fraud Operations Lead + Compliance Officer + VP of Financial Services |

**Stage 5: Deployment**
Platform Engineering deploys approved rule changes to HTME production during the standard change window (Tuesday/Thursday 02:00–04:00 UTC). Emergency deployments outside the standard window require VP of Financial Services approval (see Section 8 — Exception Handling).

**Stage 6: Post-Deployment Review**
Within thirty (30) calendar days of rule activation, the Fraud Operations Lead shall complete a Post-Deployment Rule Performance Review, comparing actual alert volumes, true positive rates, and false positive rates against projections documented in FR-CRF-001. Deviations exceeding ±25% shall trigger a Rule Recalibration Review.

#### 5.1.2 Rule Inventory and Documentation

The complete active rule inventory shall be maintained in the Fraud Detection Rule Registry (FDRR), accessible via Meridian's Governance, Risk, and Compliance (GRC) platform. Each rule entry shall include:
- Unique Rule ID (e.g., RULE-HTME-0421)
- Rule description and logic expression
- Deployment date and version
- Rule priority classification
- Associated fraud typology code
- Current status (Active, Shadow, Suspended, Retired)
- Last performance review date and key metrics
- Linked FR-CRF-001 documents for traceability

The Fraud Operations Lead shall conduct a quarterly Rule Inventory Reconciliation, confirming all active rules in HTME production match the FDRR. Discrepancies shall be remediated within five (5) business days and reported to the VP of Financial Services.

### 5.2 ML Fraud Model Operations

#### 5.2.1 Model Inference Pipeline

The HML-FM model operates within the HealthPay Transaction Processing Pipeline. Each transaction submitted to HealthPay shall be scored as follows:

1. **Feature Extraction:** The Feature Engineering Service extracts 247 structured features from the transaction payload, merchant profile, patient/consumer behavioral history, and device fingerprint data.
2. **Model Inference:** The model serving endpoint (AWS SageMaker) returns an ML Fraud Score (0.000–1.000) within the 150ms inference SLA.
3. **Score Integration:** The ML Fraud Score is integrated with active rule triggers in the HTME Scoring Engine to compute the composite Transaction Risk Score (TRS).
4. **Decision Routing:**
   - TRS < 0.30: Transaction proceeds without alert generation
   - TRS 0.30–0.69: Alert generated in FCMS at Priority 3 (standard investigation)
   - TRS 0.70–0.89: Alert generated in FCMS at Priority 2 (expedited investigation)
   - TRS ≥ 0.90: Alert generated in FCMS at Priority 1 (immediate triage); transaction may be held pending review if the rule combination includes a blocking rule

#### 5.2.2 Model Retraining Procedure

The HML-FM model shall be retrained according to the following schedule and triggers:

**Scheduled Retraining:**
- Quarterly full retraining using accumulated labeled data
- Scheduled for the first week of each calendar quarter (January, April, July, October)
- Retraining dataset includes all confirmed fraud cases and legitimate transaction samples from the preceding quarter

**Trigger-Based Retraining:**
Retraining shall be initiated within ten (10) business days when any of the following thresholds are breached:
- Population Stability Index (PSI) > 0.25 for any top-10 feature
- Characteristic Stability Index (CSI) > 0.15 for categorical payment channel features
- Model TPR drops below 0.75 for two consecutive weekly monitoring periods
- Model FPR exceeds 0.08 for two consecutive weekly monitoring periods

**Retraining Workflow:**

| Step | Action | Responsible Role | Timeline |
|---|---|---|---|
| 1 | Label new training data using confirmed case dispositions and stratified legitimate transaction sampling | Fraud Data Science | Days 1–5 |
| 2 | Perform exploratory data analysis; document data quality issues | Fraud Data Science | Days 3–7 |
| 3 | Train candidate models (minimum three architectures) | Fraud Data Science | Days 5–10 |
| 4 | Evaluate candidate models against holdout test set; produce Model Comparison Report | Fraud Data Science | Days 10–12 |
| 5 | Conduct fairness and bias assessment on leading candidate | Fraud Data Science | Days 12–14 |
| 6 | Present Model Retraining Recommendation to Model Governance Committee | Fraud Data Science Lead | Day 15 |
| 7 | Committee review and approval | Model Governance Committee | Day 15–20 |
| 8 | Deploy approved model to production | Platform Engineering | Day 21 |
| 9 | Seven-day parallel run (new model shadow scoring vs. incumbent) | Fraud Data Science | Days 21–28 |
| 10 | Full cutover to new model version | Platform Engineering | Day 29 |

#### 5.2.3 Model Decommissioning

A fraud detection model shall be considered for decommissioning when:
- Sustained TPR < 0.60 for four (4) consecutive months despite retraining
- Model outputs exhibit statistically significant bias (p < 0.01) against a protected characteristic group as defined under EU AI Act Article 10(2)(f)
- A successor model demonstrates statistically superior performance (p < 0.05) across all monitored performance metrics for a minimum three-month parallel run
- The fraud typology the model was designed to detect is no longer relevant

The Model Decommissioning Request shall be prepared by Fraud Data Science, reviewed by the Model Governance Committee, and approved by the VP of Financial Services. A decommissioning plan shall include:
- Timeline for model sun-setting
- Transition plan for any dependent rules or alert workflows
- Archiving of model artifacts and training data
- Communication to affected stakeholders

### 5.3 Alert Triage and Investigation

#### 5.3.1 Alert Prioritization

All alerts generated by the FDS shall be assigned a priority level based on TRS and value-at-risk attributes:

| Priority | TRS Range | Value at Risk | Response SLA | Typical Escalation Path |
|---|---|---|---|---|
| P1 — Critical | ≥ 0.90 | OR > $50,000 | 15 minutes | Tier II immediately; Tier III if confirmed trends |
| P2 — High | 0.70–0.89 | OR > $10,000 | 60 minutes | Tier I triage; Tier II if suspicious |
| P3 — Standard | 0.30–0.69 | OR > $1,000 | 4 hours | Tier I triage |
| P4 — Low | < 0.30 (rule-only trigger) | Any | 24 hours | Tier I batch review |

#### 5.3.2 Tier I Triage Procedure

Upon assignment of a P2, P3, or P4 alert, the Tier I Fraud Analyst shall execute the following triage steps within the applicable SLA:

1. **Alert Acknowledgment:** Acknowledge alert in FCMS to signal active investigation and prevent duplicate assignment.
2. **Entity Lookup:** Query the merchant/patient/account entity in the Meridian Central Entity Registry (MCER) to retrieve entity history, prior alerts, and known relationships.
3. **Transaction Verification:** Verify the transaction details against the HealthPay Transaction Ledger (HTL), confirming:
   - Transaction amount, timestamp, and payment method
   - Merchant identification and healthcare category code
   - Device fingerprint and geolocation data (if available)
4. **Rule Fire Analysis:** Review which specific rules and model features contributed to the TRS. Document rule fires in the FCMS Evidence Log.
5. **Rapid Determination:** Within the initial review, determine if the alert can be immediately classified as:
   - **Likely Legitimate:** All rule fires are explainable by known legitimate patterns (e.g., pre-authorized high-value procedure, documented address change). Disposition as "False Positive — Rapid Close."
   - **Requires Investigation:** One or more rule fires lack obvious legitimate explanation. Escalate to Tier II with complete Case Package.
   - **Pattern Match:** Alert characteristics match a known fraud pattern documented in the Fraud Pattern Library. Escalate to Tier II immediately with Pattern Match reference.

**Rapid Close Criteria (Tier I Authority):**
Tier I Analysts may disposition alerts as "False Positive — Rapid Close" ONLY when all of the following conditions are met:
- TRS < 0.50
- No single rule fire is marked as a "High Severity Rule"
- Entity has ≥ 6 months of legitimate transaction history
- No prior fraud alerts on entity in the preceding 90 days
- Transaction amount < $5,000

All Rapid Close dispositions shall include a written rationale documented in the FCMS case log. The Fraud Operations Lead shall review a random 10% sample of Rapid Close cases during weekly QA review.

#### 5.3.3 Tier II Investigation Procedure

Upon escalation from Tier I or direct assignment of a P1 alert, the Tier II Fraud Analyst shall conduct a thorough investigation:

1. **Case Acceptance:** Review Tier I Case Package; acknowledge escalation in FCMS.
2. **Extended Entity Investigation:**
   - Retrieve full transaction history for the entity (24-month lookback)
   - Analyze velocity patterns (transaction frequency, amount spikes)
   - Cross-reference entity against external fraud databases (via approved third-party data providers)
   - Review device fingerprint linkage across all associated accounts
3. **Link Analysis:** Using the FAW Link Analysis module, identify:
   - Shared device fingerprints across multiple accounts
   - Common IP addresses or geolocation anomalies
   - Shared payment instruments (masked PAN, token hash)
   - Beneficiary account patterns
4. **Evidence Collection:** Document all findings in the FCMS Evidence Package, including:
   - Screenshots of anomalous patterns (timestamped)
   - Transaction ledger exports (CSV format)
   - Link analysis graph exports
   - External database query results (with query reference ID)
5. **Disposition Recommendation:**
   - **Confirmed Fraud:** Evidence supports fraudulent activity determination. Prepare Suspicious Activity Report (SAR) draft.
   - **Suspicious — Requires Enhanced Monitoring:** Evidence inconclusive but risk indicators warrant ongoing monitoring. Recommend Enhanced Monitoring status.
   - **False Positive — Rule Exemption Candidate:** Legitimate activity trapped by overly aggressive rules. Recommend rule tuning and/or entity-level exemption.
6. **Quality Review:** All Tier II Confirmed Fraud dispositions shall be peer-reviewed by a second Tier II or Tier III Analyst prior to finalization.

#### 5.3.4 Tier III Complex Investigation and Pattern Analysis

Tier III Analysts handle:
- Complex, multi-entity fraud rings
- New or evolving fraud typologies not yet captured by existing rules or model features
- Investigations involving merchants in sensitive healthcare categories (e.g., substance abuse treatment, mental health services) requiring heightened privacy considerations

Tier III responsibilities include:
- Conducting network analysis across multiple linked cases
- Drafting Fraud Intelligence Reports (FIRs) documenting new fraud patterns
- Recommending new rule development to Fraud Data Science
- Mentoring Tier I/II analysts on advanced investigation techniques

### 5.4 False Positive Management

#### 5.4.1 False Positive Analysis Framework

False positive management is a critical operational function, as excessive false positives erode investigator efficiency, delay legitimate healthcare payments, and undermine trust in the HealthPay platform. The False Positive Management Framework operates on three levels:

**Level 1: Individual Case Feedback**
Every false positive disposition shall include a structured FP Classification, identifying the primary cause:
- FP-RULE: Specific rule triggered inappropriately (Rule ID documented)
- FP-MODEL: ML Fraud Score elevated without supporting rule evidence (Model Score documented)
- FP-DATA: Data quality issue causing incorrect feature values (Data source documented)
- FP-PATTERN: Legitimate but unusual transaction pattern not yet recognized as benign

**Level 2: Weekly FP Trend Review**
The Fraud Operations Lead shall conduct a weekly False Positive Trend Review every Monday 09:00–10:00 UTC, analyzing:
- FP Rate by rule (top 10 highest FP rules)
- FP Rate by merchant category
- FP Rate by transaction type
- FP Rate trend vs. prior 4-week rolling average
- Analyst FP disposition consistency (inter-analyst agreement rate)

**Level 3: Monthly FP Reduction Initiative**
The Fraud Operations Lead and Fraud Data Science Lead shall co-chair a monthly False Positive Reduction Working Group meeting (third Wednesday of each month, 14:00–16:00 UTC). This meeting shall:
- Review Level 1 and Level 2 findings
- Prioritize rule tuning and model threshold adjustment candidates
- Assign FP reduction initiatives with measurable targets
- Track initiative completion and impact

#### 5.4.2 FP Rate Targets and Thresholds

| Metric | Target | Warning Threshold | Mandatory Action Threshold |
|---|---|---|---|
| Overall System FPR | ≤ 4.0% | ≥ 4.5% | ≥ 5.5% |
| Per-Rule FPR | ≤ 3.0% | ≥ 4.0% | ≥ 5.0% |
| ML Model FPR | ≤ 5.0% | ≥ 5.5% | ≥ 6.5% |
| Rapid Close Reversal Rate | ≤ 2.0% | ≥ 3.0% | ≥ 4.0% |

When a mandatory action threshold is breached, the Fraud Operations Lead shall initiate an FP Surge Response within two (2) business days, including:
- Immediate review of top-contributing rules/models
- Temporary rule threshold adjustment or rule suspension (subject to approval per Section 5.1.1)
- Increased QA sampling rate (from 10% to 25%) for Rapid Close dispositions
- Daily FP monitoring until metric returns below target

### 5.5 Confirmed Fraud Escalation and Reporting

When a case is dispositioned as "Confirmed Fraud," the following escalation and reporting procedures apply:

#### 5.5.1 Internal Escalation

| Fraud Category | Estimated Loss | Escalation Path | Notification Timeline |
|---|---|---|---|
| Category A: Organized fraud ring | Any | VP Financial Services → CISO → General Counsel | 4 hours |
| Category B: Insider threat (Meridian employee) | Any | VP Financial Services → HR Investigations → CISO | 2 hours |
| Category C: High-value single incident | > $100,000 | VP Financial Services → CFO | 4 hours |
| Category D: Standard fraud | < $100,000 | Fraud Operations Lead → Compliance Officer | 24 hours |

#### 5.5.2 Regulatory Reporting

The Compliance Officer shall determine regulatory reporting obligations based on the fraud typology, financial impact, and jurisdictional exposure. Reporting obligations may include:
- Suspicious Activity Report (SAR) filing with relevant Financial Intelligence Units
- Data breach notification if fraud involved unauthorized access to consumer financial data
- EU AI Act Article 62 serious incident reporting if the FDS malfunction contributed to or failed to detect the fraud

All regulatory filings shall be reviewed by Legal prior to submission. Filing deadlines mandated by applicable regulations shall take precedence over internal review timelines.

#### 5.5.3 Victim Remediation

When confirmed fraud has impacted a patient/consumer or merchant, Meridian shall follow the HealthPay Incident Remediation Procedure (SOP-FIN-005), including:
- Notification to affected parties within regulatory timelines
- Reversal of fraudulent transactions where funds remain recoverable
- Credit monitoring services for affected consumers (when PII was compromised)
- Merchant account protection measures

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control ID | Control Description | Control Type | SOC 2 Mapping | EU AI Act Mapping |
|---|---|---|---|---|
| FDS-TC-001 | All access to FCMS and FAW requires multi-factor authentication (MFA) via Meridian SSO | Preventive | CC6.1 | Art. 17(1)(d) |
| FDS-TC-002 | Role-based access control (RBAC) enforced at the application layer; analyst roles limited to assigned case access only | Preventive | CC6.1, CC6.2 | Art. 17(1)(d) |
| FDS-TC-003 | All FDS database transactions logged to immutable audit trail (AWS CloudTrail + custom application logging) | Detective | CC7.2, CC7.3 | Art. 17(1)(c) |
| FDS-TC-004 | Production ML model serving environment logically separated from model development environment | Preventive | CC8.1 | Art. 17(1)(a) |
| FDS-TC-005 | Automated model input validation (schema validation, feature range checks) before inference; invalid inputs rejected and logged | Preventive | CC7.1 | Art. 17(1)(a) |
| FDS-TC-006 | Model performance metrics dashboard refreshed every 15 minutes; automated alerting when drift thresholds breached | Detective | CC7.2 | Art. 17(1)(b) |
| FDS-TC-007 | Weekly automated vulnerability scanning of all FDS infrastructure components (AWS Inspector, dependency scanning) | Preventive | CC7.1 | Art. 17(1)(a) |
| FDS-TC-008 | Encryption at rest (AES-256) for all FCMS case data and model training data stores | Preventive | CC6.1 | Art. 17(1)(c) |
| FDS-TC-009 | Encryption in transit (TLS 1.3) for all inter-service communication within the FDS architecture | Preventive | CC6.1 | Art. 17(1)(a) |
| FDS-TC-010 | Automated backup of FCMS database every 6 hours to geographically separate AWS region; 30-day backup retention | Corrective | CC7.1 | Art. 17(1)(c) |

### 6.2 Administrative Controls

| Control ID | Control Description | Control Type | SOC 2 Mapping | EU AI Act Mapping |
|---|---|---|---|---|
| FDS-AC-001 | Quarterly User Access Review (UAR) for all FDS systems; conducted by Fraud Operations Lead with Compliance Officer oversight | Detective | CC6.2 | Art. 17(1)(d) |
| FDS-AC-002 | Semi-annual FDS procedure walkthrough testing (tabletop exercise) with Fraud Operations, Compliance, and Platform Engineering | Detective | CC5.3 | Art. 17(1)(d) |
| FDS-AC-003 | Annual FDS control effectiveness assessment conducted by Internal Audit or qualified independent assessor | Detective | CC5.1, CC5.2 | Art. 17(1)(b) |
| FDS-AC-004 | Mandatory Conflict of Interest (COI) disclosure for all personnel involved in model validation activities prior to each validation cycle | Preventive | CC1.1 | Art. 17(1)(d) |
| FDS-AC-005 | Investigation case files peer-reviewed for quality; 100% of Confirmed Fraud cases, 20% random sample of False Positive — Rapid Close cases | Detective | CC5.3 | Art. 17(1)(d) |
| FDS-AC-006 | SOC 2 Type II annual examination includes FDS as in-scope system; examination results reviewed by VP Financial Services and CISO | Detective | CC5.1–CC5.3 | Art. 17(1)(b) |
| FDS-AC-007 | Human-in-the-loop requirement: No automated transaction blocking based solely on ML Fraud Score without supporting rule trigger AND human review confirmation | Preventive | CC7.1 | Art. 14(5) |
| FDS-AC-008 | EU AI Act Conformity Assessment documented and maintained for HML-FM model; updated upon material model change | Preventive | — | Art. 16, Art. 17 |

### 6.3 Segregation of Duties

To ensure the integrity of fraud detection operations and comply with SOC 2 CC1.2 requirements regarding ethical values and organizational structure, the following segregation of duties controls are enforced:

| Activity | Authorized Role(s) | Prohibited Role(s) |
|---|---|---|
| Production rule deployment | Platform Engineering | Fraud Analysts (any tier), Fraud Data Science |
| ML model training | Fraud Data Science | Fraud Analysts (any tier), Platform Engineering |
| Investigation case disposition | Fraud Analysts (assigned case) | Fraud Data Science, Platform Engineering |
| Model validation | Model Governance Committee (or designated independent validator) | Fraud Data Science (model developers) |
| SAR filing approval | Compliance Officer | Fraud Analysts (any tier) |

### 6.4 Third-Party Risk Management

Components of the FDS that rely on third-party providers shall be subject to Meridian's Third-Party Risk Management Program (SOP-RISK-003). Specific to FDS:

- **AWS (Cloud Infrastructure):** SOC 2 Type II report reviewed annually by Meridian Information Security
- **External Fraud Database Providers:** Annual due diligence review including data privacy assessment, data quality audit, and contract SLA performance review
- **Model Validation Consultants (if engaged):** Must demonstrate independence from model development teams; engagement reviewed for COI prior to contract execution

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Operational Dashboards

The following dashboards shall be maintained and accessible to relevant stakeholders:

**Real-Time Operations Dashboard (FAW Dashboard 1)**
Accessible to: Fraud Operations Team, Platform Engineering
Refresh Interval: Real-time (sub-60-second latency)
Metrics Displayed:
- Active alert count by priority (P1/P2/P3/P4)
- Alert queue depth and aging (count beyond SLA)
- Analyst availability and case assignment distribution
- HTME rule engine throughput and latency
- HML-FM model inference success rate

**Daily Operations Summary (FAW Dashboard 2)**
Accessible to: Fraud Operations Lead, VP Financial Services
Refresh Interval: Updated hourly
Metrics Displayed:
- Alerts generated (24-hour rolling)
- Cases opened / closed / pending
- Mean Time to Investigate (MTTI) by priority
- Confirmed fraud count and estimated value
- False positive rate (24-hour rolling)
- Rule fire distribution (top 10 rules)

**Model Performance Dashboard (FAW Dashboard 3)**
Accessible to: Fraud Data Science, Model Governance Committee, Compliance Officer
Refresh Interval: Updated daily at 06:00 UTC
Metrics Displayed:
- TPR, FPR, Precision, Recall, F1 Score (7-day, 30-day, 90-day rolling)
- Population Stability Index (PSI) by feature
- Model score distribution (decile analysis)
- Drift detection alerts (last 7 days)
- Feature attribution explainability summaries for blocked transactions

### 7.2 Key Performance Indicators (KPIs)

| KPI ID | Metric | Target | Measurement Frequency | Reporting Audience |
|---|---|---|---|---|
| KPI-FDS-01 | Alert-to-Triage SLA Adherence | ≥ 98% (P1/P2), ≥ 95% (P3), ≥ 90% (P4) | Daily | Fraud Operations Lead |
| KPI-FDS-02 | Mean Time to Investigate (MTTI) — P1/P2 | ≤ 4 hours | Weekly | VP Financial Services |
| KPI-FDS-03 | Mean Time to Detect (MTTD) — Confirmed Fraud | ≤ 24 hours from transaction | Monthly | VP Financial Services, CISO |
| KPI-FDS-04 | False Positive Rate (Overall System) | ≤ 4.0% | Weekly | VP Financial Services, Model Governance Committee |
| KPI-FDS-05 | True Positive Rate (ML Model) | ≥ 0.80 | Weekly | Model Governance Committee |
| KPI-FDS-06 | Confirmed Fraud Detection Rate (Coverage) | ≥ 90% of actual fraud (benchmarked against external fraud reports) | Quarterly | VP Financial Services, CFO |
| KPI-FDS-07 | Investigation Case Quality Assurance Score | ≥ 90% average across all analysts | Weekly (sample) | Fraud Operations Lead |
| KPI-FDS-08 | Rule Efficacy Index (REI) | ≥ 0.30 (TPR minus 3x FPR per rule) | Monthly | Fraud Operations Lead, Fraud Data Science |
| KPI-FDS-09 | Model Drift Index | ≤ 0.15 PSI | Weekly | Fraud Data Science, Model Governance Committee |
| KPI-FDS-10 | Recovery Rate (confirmed fraud loss recovered) | ≥ 40% | Monthly | VP Financial Services, CFO |

### 7.3 Reporting Cadence

| Report Name | Frequency | Prepared By | Reviewed By | Content Summary |
|---|---|---|---|---|
| Daily Operations Brief | Daily (08:00 UTC) | Fraud Operations Lead (automated email) | Fraud Operations Team | Prior day alert volumes, SLA breaches, P1/P2 open cases, staffing notes |
| Weekly Fraud Intelligence Report | Weekly (Monday 12:00 UTC) | Tier III Fraud Analyst | Fraud Operations Lead, Compliance Officer | New fraud patterns, rule performance review, FP trends, upcoming rule changes |
| Monthly FDS Performance Report | Monthly (first business day) | Fraud Operations Lead | VP Financial Services, CISO (cc) | All KPIs, rule/model changes, confirmed fraud summary, staffing and training updates |
| Quarterly Model Performance Review | Quarterly | Fraud Data Science Lead | Model Governance Committee, VP Financial Services | Detailed model performance metrics, drift analysis, retraining summary, bias assessment results |
| Semi-Annual Compliance Assessment | Semi-Annual (Jan/Jul) | Compliance Officer | VP Financial Services, General Counsel | Control effectiveness, regulatory compliance posture (SOC 2, EU AI Act), audit findings and remediation status |

### 7.4 Anomaly Detection and Alerting (Meta-Monitoring)

The FDS itself shall be subject to automated anomaly detection on operational metrics:

| Anomaly Condition | Detection Mechanism | Alert Recipients | Response Expectation |
|---|---|---|---|
| Alert volume spike > 3x 7-day rolling average | HTME throughput monitor | Platform Engineering, Fraud Operations Lead | Acknowledge within 15 min; determine if rule/model malfunction or actual fraud wave |
| Alert volume drop > 50% of 7-day rolling average | HTME throughput monitor | Platform Engineering, Fraud Operations Lead | Acknowledge within 30 min; investigate potential FDS outage or bypass |
| Model inference failure rate > 1% | SageMaker endpoint health check | Platform Engineering, Fraud Data Science | Immediate escalation per Incident Response Plan (SOP-IT-001) |
| FCMS database latency > 500ms | AWS RDS Performance Insights | Platform Engineering | Investigate within 1 hour; implement scaling if sustained |
| Stale case count > 50 cases beyond SLA | FCMS query (hourly) | Fraud Operations Lead | Immediate triage; assess staffing adequacy |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types

Meridian recognizes that strict adherence to all SOP provisions may not be feasible in every operational scenario. The following exception categories are defined:

**Operational Exceptions:**
- Emergency rule deployment outside standard change window
- SLA breach justified by extraordinary alert volume (e.g., fraud wave exceeding 3x normal volume)
- Temporary suspension of a fraud detection rule causing excessive false positives

**Technical Exceptions:**
- Model inference fallback to legacy model version due to production incident
- Scheduled maintenance exceeding the defined change window
- Data pipeline delay impacting model scoring freshness

**Governance Exceptions:**
- Extension of model validation cycle timeline
- Temporary reassignment of validation responsibilities (requires enhanced COI controls)
- Exception to mandatory training completion deadline

### 8.2 Exception Request Procedure

1. **Exception Identification:** Any team member may identify a need for an exception. The individual shall immediately notify the Fraud Operations Lead (or highest-available authority in the Fraud Operations chain).

2. **Exception Request Documentation:** The Fraud Operations Lead (or designee) shall document the exception request using the **FDS Exception Request Form (FDS-EXC-001)** , capturing:
   - Exception type (Operational, Technical, Governance)
   - SOP section(s) from which deviation is requested
   - Detailed justification for the exception
   - Proposed alternative control(s) during the exception period
   - Duration of the exception (start and expected end date/time)
   - Impact assessment (operational, regulatory, customer experience)

3. **Risk Assessment:** The Compliance Officer shall assess the regulatory impact of the exception within:
   - 2 hours for Operational exceptions impacting alert generation or investigation
   - 24 hours for Technical exceptions
   - 5 business days for Governance exceptions

4. **Approval Authority:**

| Exception Materiality | Criteria | Approval Required |
|---|---|---|
| Minor | Duration ≤ 24 hours; no impact to SAR filing timelines; no blocking rule suspension | Fraud Operations Lead |
| Moderate | Duration 24–72 hours; OR impacts ≤ 10% of alert volume; OR suspends one non-critical rule | Fraud Operations Lead + Compliance Officer |
| Major | Duration > 72 hours; OR impacts > 10% of alert volume; OR suspends a blocking rule; OR impacts regulatory reporting | Fraud Operations Lead + Compliance Officer + VP Financial Services |
| Critical | Duration > 7 days; OR suspends ML model entirely; OR impacts > 25% of detection coverage | VP Financial Services + CFO + General Counsel |

5. **Exception Monitoring:** Throughout the exception period, the Fraud Operations Lead shall:
   - Monitor alert volumes and fraud detection coverage daily
   - Document any confirmed fraud that occurred during the exception period that would have been detected under normal operations
   - Escalate any unexpected impacts immediately to the original approver

6. **Exception Closure:** Upon expiration of the exception period:
   - Normal operations shall resume
   - A retrospective review shall be conducted within five (5) business days, documenting the exception outcome, any fraud missed during the exception, and lessons learned
   - The exception record shall be archived in the GRC platform

### 8.3 Escalation Matrix

For incidents and issues not meeting the exception criteria above, the following escalation matrix applies:

| Escalation Level | Trigger | Escalate To | Timeline |
|---|---|---|---|
| Level 1 | Any Tier I Analyst unable to meet alert SLA for > 2 consecutive hours | Fraud Operations Lead | Immediate (via Slack #fds-ops) |
| Level 2 | Confirmed P1/P2 fraud case exceeding $50,000 | Fraud Operations Lead → VP Financial Services | Within 1 hour of confirmation |
| Level 3 | Suspected system breach or unauthorized FDS access | Fraud Operations Lead → CISO (per Incident Response Plan SOP-IT-001) | Immediate (via PagerDuty) |
| Level 4 | Potential regulatory reporting obligation identified | Fraud Operations Lead → Compliance Officer | Within 4 hours |
| Level 5 | Material model failure (TPR < 0.50 sustained > 48 hours) | Fraud Data Science Lead → Model Governance Committee → VP Financial Services | Within 24 hours |
| Level 6 | Fraud event with potential reputational or legal exposure > $500,000 | VP Financial Services → CFO → General Counsel → CEO | Immediate (via executive escalation protocol) |

---

## 9. Training Requirements

### 9.1 Role-Based Training Curriculum

All personnel with FDS responsibilities shall complete the following training requirements:

| Role | Required Training Modules | Initial Training Timeline | Annual Refresher |
|---|---|---|---|
| **Fraud Analyst Tier I** | FDS-101: Fraud Detection Fundamentals; FDS-102: FCMS Operations; FDS-103: Healthcare Fraud Typologies; MER-001: Meridian Code of Conduct; PRI-002: PII Handling and Data Privacy | Before system access granted | FDS-101-R (4 hours) |
| **Fraud Analyst Tier II** | All Tier I modules; FDS-201: Advanced Investigation Techniques; FDS-202: Link Analysis and Network Detection; FDS-203: SAR Drafting Workshop; REG-003: Regulatory Reporting Obligations | Within 30 days of promotion/hire | FDS-201-R (8 hours) |
| **Fraud Analyst Tier III** | All Tier II modules; FDS-301: Fraud Pattern Analysis and Rule Design; FDS-302: Mentorship and QA Oversight; REG-004: Advanced Regulatory and Legal Considerations; AI-001: AI Ethics and Bias Awareness | Within 60 days of promotion/hire | FDS-301-R (8 hours) + AI-001-R (2 hours) |
| **Fraud Data Science** | All Tier I modules (awareness only); FDS-401: ML Model Development Standards; FDS-402: Model Validation Methodology; AI-001: AI Ethics and Bias Awareness; AI-002: EU AI Act Technical Compliance; REG-003: Regulatory Reporting Obligations (awareness) | Within 30 days of hire | FDS-401-R (8 hours) + AI-002-R (4 hours) |
| **Fraud Operations Lead** | All Tier II modules (awareness); FDS-501: FDS Leadership and Governance; FDS-502: Exception Handling and Crisis Management | Within 30 days of promotion/hire | FDS-501-R (4 hours) |
| **Compliance Officer (Financial Services)** | FDS-601: FDS Regulatory Compliance; AI-001, AI-002; REG-003 (advanced); SOC-001: SOC 2 Control Framework | Within 30 days of assignment | FDS-601-R (8 hours) |
| **Model Governance Committee Members** | AI-001, AI-002; FDS-402 (overview); MER-002: Model Risk Governance Framework | Within 30 days of appointment | AI-002-R (4 hours) |

### 9.2 EU AI Act Training Requirements

Consistent with EU AI Act Article 14(4)(a) and Article 17(1)(d), all personnel involved in the operation or oversight of the HML-FM model shall receive specific training on:

- The capabilities and limitations of the ML fraud detection model
- The potential risks of over-reliance on model outputs (automation bias)
- Procedures for interpreting and, when appropriate, disregarding or overriding model outputs
- Recognizing and reporting anomalous model behavior
- Data quality standards for model inputs and the consequences of degraded data quality

This training shall be delivered as module **AI-003: Human Oversight of High-Risk AI Systems**:
- **Initial Training:** 4-hour instructor-led session, including case studies and practical override exercises
- **Annual Refresher:** 2-hour e-learning module with scenario-based assessment (minimum passing score: 85%)
- **New Model Version Briefing:** 1-hour specific briefing delivered within 5 business days of any major model version deployment

### 9.3 Training Tracking and Compliance

- All training completions shall be recorded in Meridian's Learning Management System (LMS), Meridian Learn
- Training compliance shall be reviewed monthly by the Fraud Operations Lead
- Any team member with lapsed training (> 30 days past due) shall have FDS system access temporarily suspended until training is completed and acknowledged
- Annual training compliance metrics shall be included in the Monthly FDS Performance Report

### 9.4 New Hire Onboarding

New Fraud Analysts shall complete a structured 2-week onboarding program before independent case handling:

| Onboarding Week | Activities | Supervision Level |
|---|---|---|
| Week 1 | Complete FDS-101, FDS-102, MER-001, PRI-002; Shadow Tier I Analysts; Review Fraud Pattern Library | 100% supervised (no independent dispositions) |
| Week 2 | Begin supervised case handling on P3/P4 alerts only; All dispositions reviewed by assigned mentor (Tier II or III) | 100% reviewed |
| Week 3–4 | Independent P3/P4 handling with 50% QA review; Begin P2 handling under supervision | 50% QA review |
| Week 5+ | Full independent caseload; Standard QA review rates apply | Standard QA review |

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP-ID | Policy Name | Relationship to This SOP |
|---|---|---|
| SOP-FIN-001 | HealthPay Transaction Processing Standards | Defines transaction processing pipeline into which FDS is integrated |
| SOP-FIN-003 | Payment Dispute Resolution | Governs chargeback and dispute workflows arising from fraud determinations |
| SOP-FIN-005 | HealthPay Incident Remediation | Defines victim notification and remediation procedures triggered by confirmed fraud |
| SOP-COMP-003 | Anti-Money Laundering (AML) Compliance | Defines AML monitoring obligations; fraud investigations may identify concurrent AML concerns |
| SOP-COMP-005 | Know Your Customer (KYC) and Identity Verification | KYC failures may be indicators of synthetic identity fraud |
| SOP-AI-001 | Enterprise AI Governance Policy | Overarching governance for all AI/ML systems, including model inventory, risk tiering, and validation requirements |
| SOP-RISK-001 | Credit Risk Model Governance | Governs credit risk models; shares model governance committee infrastructure but distinct risk domain |
| SOP-RISK-003 | Third-Party Risk Management Program | Governs due diligence and monitoring of third-party providers supporting FDS |
| SOP-IT-001 | Incident Response Plan | Defines incident detection, response, and recovery procedures for FDS-related security or availability incidents |
| SOP-DRM-001 | Data Retention Management | Defines data retention schedules; referenced for FDS investigation data retention |
| SOP-HR-012 | Conflict of Interest Policy | Governs COI disclosures required for model validation personnel |
| SOP-CYB-004 | Access Control Standards | Defines RBAC and authentication standards applied to FDS systems |

### 10.2 External Standards and Regulations

| Reference | Description | Applicability |
|---|---|---|
| SR 11-7 / OCC 2011-12 | Supervisory Guidance on Model Risk Management | Governs model risk management practices for financial institution models, including fraud detection models |
| AICPA TSC 2017 (SOC 2) | Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy | Covers CC5.1–CC5.3 (Control Environment, Risk Assessment, Monitoring Activities) and CC6.1–CC8.1 (Logical and Physical Access Controls, System Operations, Change Management) |
| EU AI Act (Regulation 2024/1689) | Harmonised rules on artificial intelligence | Applies to HML-FM as a high-risk AI system in the financial services domain; Articles 14, 16, 17, 62, and Annex III(5)(a) particularly relevant |
| EU MDR (Regulation 2017/745) | Medical Device Regulation | Relevant for fraud detection in medical device payment transactions (CE-marked products) |
| GDPR (Regulation 2016/679) | General Data Protection Regulation | Governs processing of personal data in fraud investigations; Article 14(5)(c) exception for fraud prevention applies |

### 10.3 Meridian Internal References

| Reference ID | Document Name |
|---|---|
| REF-REC-001 | Meridian Corporate Records Retention Schedule |
| REF-FDS-001 | HealthPay Fraud Pattern Library (Confluence) |
| REF-FDS-002 | FDS System Architecture Diagram (Lucidchart) |
| REF-FDS-003 | HML-FM Model Documentation (v3.2) |
| REF-FDS-004 | Pre-Deployment Test Report Template |
| REF-FDS-005 | Model Comparison Report Template |
| REF-FDS-006 | Fraud Intelligence Report (FIR) Template |
| REF-FDS-007 | FDS Exception Request Form (FDS-EXC-001) |
| REF-FDS-008 | Fraud Rule Change Request Form (FR-CRF-001) |

---

## 11. Revision History

| Version | Effective Date | Author(s) | Description of Changes | Approver |
|---|---|---|---|---|
| 1.0 | 2021-06-15 | M. Chen (Fraud Operations Lead) | Initial SOP publication covering rules-based fraud detection operations | S. Patel, VP Financial Services (interim) |
| 1.5 | 2022-03-01 | M. Chen, J. Kowalski (Fraud Data Science) | Major revision: Added ML fraud model operations (Section 5.2), SOC 2 control mapping (Section 6). Expanded false positive management framework (Section 5.4) | S. Patel, VP Financial Services |
| 1.6 | 2023-01-10 | J. Kowalski, A. Reyes (Compliance) | Updated alert triage procedures; added Tier II peer review requirement; revised SLA targets based on 2022 performance data; incorporated SOC 2 CC5.1–CC5.3 mapping detail | R. Liu, VP Financial Services |
| 1.7 | 2023-07-18 | R. Liu (VP), M. Chen | Reorganized Roles and Responsibilities (Section 3) into RACI matrix; added Proactive Account Review procedures (Section 5.11); added quarterly rule inventory reconciliation requirement; expanded training curriculum for Tier III and Data Science roles | R. Liu, VP Financial Services |
| 1.8 | 2023-11-05 | A. Reyes (Compliance), J. Kowalski | Added EU AI Act compliance framework across Sections 4, 5, 6, and 9; introduced EU AI Act training module AI-003; updated model governance to include Conformity Assessment documentation; added Article 14(5) human-in-the-loop requirement as FDS-AC-007 | J. Thornton, CFO |
| 1.9 | 2024-01-23 | R. Liu, A. Reyes, M. Chen | Comprehensive annual review: Updated all department titles to current org structure; revised FP Rate thresholds based on 2023 operational data; added FDS-AC-008 (EU AI Act Conformity Assessment); updated Related Policies to reference SOP-AI-001; consolidated exception handling procedures; expanded escalation matrix to six levels; updated all cross-references; extended document to address HealthPay platform growth to $4.2B annual volume | J. Thornton, CFO |
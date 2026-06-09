---
sop_id: "SOP-CLIN-007"
title: "Adverse Event Detection and Reporting"
business_unit: "Clinical AI Products"
version: "4.3"
effective_date: "2024-06-05"
last_reviewed: "2025-07-28"
next_review: "2026-01-20"
owner: "Dr. Aisha Okafor, VP of Clinical AI Products"
approver: "Dr. Priya Patel, Chief Medical Officer"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Adverse Event Detection and Reporting

## SOP-CLIN-007 | Version 4.3

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the end-to-end framework for identifying, classifying, documenting, investigating, reporting, and remediating adverse events (AEs) associated with Meridian Health Technologies' Clinical AI Platform. The purpose of this SOP is to ensure that all potential adverse impacts on patient safety, data integrity, model performance degradation, and regulatory non-compliance arising from the use of our high-risk AI systems are captured systematically and addressed within defined timelines.

This document operationalizes the post-market surveillance (PMS) and serious incident reporting obligations mandated under the EU AI Act for high-risk AI systems classified under Annex III, and aligns with the continuous monitoring principles of the NIST AI Risk Management Framework (AI RMF 1.0). It formalizes the feedback loop between clinical deployment, automated telemetry, and human oversight mechanisms required under Article 14 of the EU AI Act.

### 1.2 Scope

This SOP applies to all adverse events, near-misses, and safety signals originating from or related to the following Meridian products and systems:

| Product / System | Scope Coverage |
|---|---|
| Clinical AI Platform (all modules including diagnostic imaging analysis, patient risk scoring, and adverse event prediction) | Full scope – all deployments across 340+ hospitals and clinics in North America and EU |
| MedInsight Analytics (population health and outcomes prediction) | AE detection related to model-driven care gap recommendations and risk stratification outputs that could lead to patient harm if erroneous |
| Clinical AI development, testing, and validation environments | Pre-production incidents that reveal systemic safety issues |
| Third-party models integrated into Clinical AI workflows | Full scope – Meridian assumes responsibility for integrated model outputs |
| HealthPay Financial Services credit scoring models | Out of scope for this SOP; covered under SOP-FIN-014 (SR 11-7 Model Risk Management) |

**In-Scope Personnel**: All employees, contractors, and third-party vendors who design, develop, deploy, monitor, maintain, or support the Clinical AI Platform and MedInsight Analytics. This includes but is not limited to Clinical AI engineering teams, Clinical Informatics, Customer Operations, Quality Assurance, Regulatory Affairs, Legal, and the Office of the Chief Medical Officer.

**Geographic Scope**: All adverse events occurring in deployments across North America (United States, Canada) and the European Union (including European Economic Area countries where Meridian has active deployments).

**Out of Scope**: Adverse events related solely to the Meridian SaaS Platform infrastructure layer (covered under SOP-IT-003, IT Incident Management) unless such infrastructure events directly cause a clinical adverse event. Purely financial adverse events within HealthPay are covered under SOP-FIN-014.

### 1.3 Effective Date and Transition

This version 4.3 is effective as of June 5, 2024. All prior versions are superseded. Personnel have a 30-day transition period from the effective date to align existing open cases with the classification framework in Section 5.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Adverse Event (AE)** | Any incident, malfunction, degradation, or unintended behavior of a Clinical AI system that has resulted in, could have resulted in, or has the potential to result in: (a) patient harm (physical, psychological, or financial), (b) clinically significant misdiagnosis or delayed diagnosis, (c) inappropriate clinical intervention or failure to intervene, or (d) breach of data protection that could cause patient harm. |
| **Serious Adverse Event (SAE)** | An adverse event that results in or has the potential to result in: death, life-threatening illness or injury, inpatient hospitalization or prolongation of existing hospitalization, persistent or significant disability/incapacity, or requires medical or surgical intervention to prevent permanent impairment. Equivalent to "serious incident" under EU AI Act Article 3(44) and Article 73. |
| **Near-Miss** | An event where a Clinical AI system malfunction or erroneous output occurred but was caught by human oversight, automated guardrails, or other controls before reaching the patient or clinical decision-maker. Near-misses are classified as Grade C or D severity (see Section 5.2) but are tracked for trending analysis. |
| **Safety Signal** | A pattern, trend, or statistical deviation identified through continuous monitoring that suggests a previously unknown or incompletely characterized adverse event risk associated with a Clinical AI system. Safety signals may arise from aggregate data analysis, literature reports, or field observations. |
| **Serious Incident** | EU AI Act Article 3(44) definition: "any incident or malfunction of an AI system that directly or indirectly leads to (a) the death of a person or serious harm to the health, property, or environment, (b) a serious and irreversible disruption of the management and operation of critical infrastructure." Meridian applies this definition for all EU deployments and voluntarily extends the reporting framework to North American deployments. |
| **Root Cause Analysis (RCA)** | A structured, evidence-based methodology to identify the fundamental cause(s) of an adverse event. Meridian uses the Ishikawa (fishbone) framework supplemented with the London Protocol for clinical incidents. |
| **Corrective and Preventive Action (CAPA)** | A documented set of actions taken to eliminate the causes of an existing nonconformity (adverse event) and to prevent recurrence. CAPA plans are mandatory for all Grade A and B adverse events. |
| **Human-in-the-Loop (HITL)** | A control mechanism where a qualified human operator reviews, validates, or overrides AI system outputs before they are acted upon. Required for all outputs from high-risk Clinical AI systems per EU AI Act Article 14. |
| **Model Degradation** | A statistically significant decline in AI model performance metrics (e.g., accuracy, sensitivity, specificity, AUC-ROC) below pre-defined thresholds as measured against baseline validation metrics. |
| **Post-Market Surveillance (PMS)** | The systematic process of collecting, analyzing, and acting upon real-world performance data from deployed AI systems. Mandated under EU AI Act Article 61 for high-risk AI systems. |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| AE | Adverse Event |
| SAE | Serious Adverse Event |
| AI | Artificial Intelligence |
| CAPA | Corrective and Preventive Action |
| CMO | Chief Medical Officer |
| CAIO | Chief AI Officer |
| CISO | Chief Information Security Officer |
| CPO / DPO | Chief Privacy Officer / Data Protection Officer |
| CCO | Chief Compliance Officer |
| EU | European Union |
| HITL | Human-in-the-Loop |
| ML | Machine Learning |
| MLOps | Machine Learning Operations |
| PMS | Post-Market Surveillance |
| RCA | Root Cause Analysis |
| RMF | Risk Management Framework (NIST) |
| SLA | Service Level Agreement |
| SOC | Security Operations Center |
| VP-CAI | Vice President of Clinical AI Products |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix (RACI)

The following RACI matrix defines the roles and responsibilities for adverse event management:

| Role | Detect & Triage | Classification | Investigation (RCA) | Reporting to Regulators | CAPA Implementation | CAPA Verification | EU AI Act Art. 73 Notification |
|---|---|---|---|---|---|---|---|
| **Clinical AI Product Owner** | R | C | C | I | A | I | I |
| **Clinical AI Engineering Lead** | R | C | R | I | R | C | I |
| **Site Reliability Engineer (SRE)** | R | I | C | I | C | I | I |
| **Clinical Informatics Specialist** | R | R | C | I | C | I | I |
| **VP of Clinical AI Products (Dr. Aisha Okafor)** | A | A | A | A | A | A | R |
| **Chief Medical Officer (Dr. Priya Patel)** | I | A | A | R | I | A | A |
| **Chief AI Officer (Dr. Marcus Rivera)** | I | I | C | C | A | I | I |
| **Chief Compliance Officer (Thomas Anderson)** | I | I | I | R | I | I | C |
| **Chief Privacy Officer / DPO (Dr. Klaus Weber)** | I | I | I | R (EU) | I | I | R (EU DPA) |
| **General Counsel (Maria Gonzalez)** | I | I | I | C | I | I | C |
| **Customer Operations Lead** | C | I | I | C | C | I | I |
| **Quality Assurance Manager** | I | C | R | I | C | R | I |
| **Clinical Safety Officer** | R | R | R | C | C | C | C |

**Key**: R = Responsible (executes), A = Accountable (approves), C = Consulted, I = Informed

### 3.2 Role Descriptions

**3.2.1 VP of Clinical AI Products (Dr. Aisha Okafor)** — Serves as the designated Authorized Representative for adverse event management. Accountable for the overall effectiveness of this SOP. Approves all Serious Adverse Event classifications, CAPA plans, and regulatory notifications. Escalates to the Chief Medical Officer for clinical safety determinations.

**3.2.2 Chief Medical Officer (Dr. Priya Patel)** — Provides clinical expertise for severity classification and patient harm assessment. Approves all SAE classifications. Serves as the final clinical authority on whether an adverse event constitutes a "serious incident" under EU AI Act Article 73. Reviews and approves all external communications to healthcare providers regarding clinical safety issues.

**3.2.3 Clinical Safety Officer** — A dedicated role within the Clinical AI Products business unit responsible for the day-to-day operation of the adverse event management system. Triages incoming AE reports, maintains the AE registry, coordinates RCA teams, tracks CAPA implementation, and ensures reporting timelines are met. Reports directly to the VP of Clinical AI Products with a dotted line to the Chief Medical Officer.

**3.2.4 Chief AI Officer (Dr. Marcus Rivera)** — Provides strategic oversight of AI model governance. Reviews RCA findings that relate to model architecture, training data, or algorithmic bias. Approves model retraining or architectural changes as part of CAPA plans. Ensures alignment with the NIST AI RMF.

**3.2.5 Chief Privacy Officer / DPO (Dr. Klaus Weber)** — Serves as the point of contact for EU data protection authorities (DPAs) under the EU AI Act Article 73 serious incident reporting obligations for incidents involving personal data. Manages any required data protection impact assessment (DPIA) updates resulting from adverse events. Coordinates cross-border reporting where multiple EU member states are affected.

**3.2.6 General Counsel (Maria Gonzalez)** — Advises on regulatory interpretation, legal privilege for RCA documentation, and liability exposure. Reviews all external regulatory notifications before submission.

**3.2.7 Clinical Informatics Specialists** — Embedded within customer-facing teams; serve as the frontline for detecting and reporting potential adverse events from clinical end-users. Conduct initial triage and gather contextual information from healthcare provider workflows.

**3.2.8 Quality Assurance Manager** — Ensures that CAPA plans are verified for effectiveness through defined testing and validation protocols. Maintains the CAPA tracking system and conducts periodic effectiveness reviews.

---

## 4. Policy Statements

### 4.1 General Principles

**PS-001: Safety-First Culture** — Meridian Health Technologies is committed to a proactive safety culture where all personnel are empowered and obligated to report any suspected adverse event, near-miss, or safety signal without fear of retaliation. Management shall reinforce this commitment through regular safety communications and by modeling transparent incident reporting.

**PS-002: No Retaliation** — Meridian strictly prohibits any form of retaliation, discrimination, or adverse employment action against any employee, contractor, or vendor who reports a suspected adverse event in good faith. This policy extends to reports made through the anonymous ethics hotline.

**PS-003: Continuous Monitoring** — All Clinical AI systems classified as high-risk under the EU AI Act shall be subject to continuous, automated post-market surveillance monitoring. Monitoring telemetry shall be collected, analyzed, and retained in accordance with this SOP.

**PS-004: Timely Reporting** — Meridian commits to meeting or exceeding all regulatory reporting timelines specified in the EU AI Act. Internal escalation timelines are set more aggressively than regulatory requirements to ensure adequate review time.

**PS-005: Transparency** — Meridian will maintain transparency with affected healthcare provider customers, patients, and regulators regarding adverse events, their investigation status, and remediation actions, consistent with legal obligations and privilege protections.

**PS-006: Human Oversight** — All outputs from high-risk Clinical AI systems that could influence clinical decision-making shall be subject to human oversight as required by EU AI Act Article 14. Automated decisions without meaningful human review are prohibited for high-risk clinical applications.

**PS-007: Documentation and Traceability** — Every adverse event shall be documented with a unique identifier, full audit trail, and traceability from detection through final resolution. Records shall be retained for the longer of: (a) 10 years, (b) the lifetime of the affected AI system plus 6 years, or (c) as required by applicable law.

**PS-008: Proportionality** — The depth and formality of investigation and CAPA activities shall be proportional to the actual or potential severity of the adverse event. Near-misses and low-severity events may follow a streamlined process; SAEs always require full formal RCA.

### 4.2 EU AI Act Compliance Commitments

Meridian affirms the following specific commitments under the EU AI Act (Regulation 2024/1689):

| Policy ID | Commitment | EU AI Act Reference |
|---|---|---|
| PS-EU-01 | All high-risk AI systems maintain technical documentation demonstrating conformity with requirements of Title III, Chapter 2. | Article 11, Annex IV |
| PS-EU-02 | Serious incidents as defined in Article 3(44) shall be reported to the relevant market surveillance authority immediately upon determination, and no later than 15 calendar days after becoming aware, unless a justified extension is obtained. | Article 73(1)-(2) |
| PS-EU-03 | Post-market surveillance plans are maintained for each high-risk AI system, updated based on AE data, and documented in the technical file. | Article 61 |
| PS-EU-04 | Human oversight measures are in place and tested to ensure that natural persons to whom human oversight is assigned can: (a) fully understand the capacities and limitations of the system, (b) remain aware of automation bias, (c) correctly interpret system outputs, and (d) override or disregard outputs. | Article 14(4) |
| PS-EU-05 | Any corrective action taken in response to an adverse event shall be documented, and where the action affects the system's conformity, the notified body shall be informed. | Article 61(3), Article 21 |

---

## 5. Detailed Procedures

### 5.1 Adverse Event Detection

#### 5.1.1 Detection Sources

Adverse events may be detected through the following channels. All channels feed into the centralized AE Management System (AEMS) hosted on ServiceNow GRC:

| Detection Channel | Description | Responsibility | Expected Detection Time |
|---|---|---|---|
| **Automated Monitoring Alerts** | Datadog monitors, PagerDuty alerts, and LangSmith AI tracing detect model output anomalies, performance degradation, bias drift, or system errors. Thresholds defined in SOP-CLIN-003 (Model Monitoring). | SRE Team, MLOps Engineers | Real-time to 1 hour |
| **Clinical End-User Reports** | Healthcare providers report suspected AI errors, unexpected outputs, or patient safety concerns through the Meridian Support Portal or direct communication with Customer Operations. | Customer Operations, Clinical Informatics | 0-24 hours from user awareness |
| **Proactive Ad-hoc Review** | Clinical Informatics Specialists conduct retrospective review of model outputs as part of the HITL audit program. See Section 5.1.2. | Clinical Informatics | Typically 1-7 days post-inference |
| **Patient Reports** | Patients or their representatives report concerns through Meridian's Patient Feedback Form or through the healthcare provider. | Customer Operations | Variable |
| **Internal Testing / QA** | Quality assurance testing, red-teaming exercises, or stress testing reveals vulnerabilities or failure modes. | Quality Assurance Manager | During test cycles |
| **Literature / External Alerts** | Published research, FDA MAUDE database alerts, or peer reports identify safety issues with similar AI technologies that may apply to Meridian systems. | Clinical Safety Officer | Proactive monitoring |
| **Security Incidents** | Cybersecurity events that could affect model integrity, training data, or output reliability. Escalated from SOP-IT-005 (Security Incident Response). | CISO, SOC | Per SOP-IT-005 |

#### 5.1.2 Human-in-the-Loop Audit Program

As part of the Article 14 human oversight obligations, Clinical Informatics Specialists shall conduct a weekly retrospective audit of a statistically representative sample of Clinical AI outputs. The sampling methodology is:

- **Sample Size**: For each deployed model, a minimum of 2% of inference outputs per week, with a minimum of 50 outputs, whichever is larger.
- **Stratification**: Samples are stratified by: (a) high-risk vs. standard-risk patient cohorts as defined by the model, (b) model confidence scores in quartiles (with oversampling of the 10% of outputs with the lowest confidence), and (c) geographic region (separate sampling for EU and North American deployments).
- **Review Criteria**: Human reviewers evaluate each output for clinical plausibility, alignment with clinical guidelines, consistency with input data, and any evidence of bias or discrimination.
- **Disposition**: Outputs are classified as: "Concordant," "Discordant - Minor Deviation," "Discordant - Significant Deviation (Potential AE)," or "Indeterminate." All "Significant Deviation" classifications must be logged into AEMS within 4 hours.

#### 5.1.3 Automated Detection Signals

The following automated detection signals shall be configured in Datadog and PagerDuty with direct integration to AEMS via webhook:

| Signal | Threshold | Severity Mapping |
|---|---|---|
| Model prediction error rate exceeds baseline | >2x baseline rolling 7-day average | Preliminary Grade B or C |
| Protected attribute bias exceeds threshold | >5% differential in FPR or FNR between groups | Preliminary Grade A or B |
| Model latency exceeds SLA | >5 seconds for real-time inference (exceeding clinical workflow timeout) | Grade D (unless patient harm resulted) |
| Data drift detected | Maximum Mean Discrepancy (MMD) p-value <0.01 vs. training distribution | Preliminary Grade C |
| Concept drift detected | Target variable distribution shift >2 standard deviations | Preliminary Grade B or C |
| System unavailable / timeout during clinical use | Any unavailability during active clinical hours | Grade D to B depending on clinical context |
| Anomalous cluster of similar outputs | Any statistically improbable output pattern (>3 sigma) not explained by patient population | Preliminary Grade B |

### 5.2 Severity Classification

#### 5.2.1 Classification Framework

All adverse events shall be classified within 4 hours of detection into one of four severity grades. Classification is performed initially by the Clinical Informatics Specialist or SRE detecting the event, then confirmed by the Clinical Safety Officer within 8 hours. For events initially classified as Grade A or B, the Chief Medical Officer shall review and confirm within 24 hours.

**Grade A — Critical (Serious Adverse Event)**

*Criteria (any one is sufficient):*
- AI system output directly contributed to patient death
- AI system output directly contributed to life-threatening injury or condition
- AI system output directly contributed to permanent impairment or disability
- AI system output resulted in patient undergoing unnecessary invasive procedure with serious complications
- Widespread systematic bias resulting in harm to a protected group
- Any event meeting the EU AI Act Article 3(44) "serious incident" definition

*Reporting Timeline:*
- Internal escalation: Immediate (within 1 hour of detection)
- EU AI Act Article 73 notification: Within 15 calendar days, or immediately if urgent safety measures required
- Customer notification: Within 24 hours of internal confirmation

*Investigation Level:* Full formal RCA mandatory

**Grade B — Major**

*Criteria (any one is sufficient):*
- AI system output contributed to patient requiring additional medical intervention (not meeting Grade A criteria)
- AI system output contributed to clinically significant delayed or missed diagnosis with potential for moderate harm
- AI system output contributed to inappropriate medication or treatment with moderate side effects
- Model failure affecting >50 patients simultaneously
- Systematic data quality issue rendering model outputs unreliable for >24 hours
- Patient data affected by event that could cause harm (security incident with clinical impact)

*Reporting Timeline:*
- Internal escalation: Within 2 hours of detection
- EU AI Act Article 73 notification: Within 15 calendar days
- Customer notification: Within 72 hours of internal confirmation

*Investigation Level:* Full formal RCA mandatory

**Grade C — Minor**

*Criteria (any one is sufficient):*
- AI system output contributed to minor inconvenience or transient clinical issue with no lasting harm
- Model output error caught by HITL before reaching clinical decision (near-miss with potential for moderate harm)
- Isolated model performance degradation affecting <10 patients
- Minor documentation or labeling error in model output
- Non-material breach of data policy with no patient harm

*Reporting Timeline:*
- Internal escalation: Within 8 hours
- EU AI Act notification: Not individually reportable; included in periodic summary if trending
- Customer notification: Within 5 business days at Clinical Safety Officer discretion

*Investigation Level:* Abbreviated RCA or trend analysis

**Grade D — Negligible / Near-Miss**

*Criteria (any one is sufficient):*
- AI system anomaly with no clinical impact and no realistic potential for harm
- Cosmetic error in output display that does not affect clinical meaning
- Model performance below SLA but above safety threshold
- Near-miss with low potential for harm

*Reporting Timeline:*
- Internal escalation: Within 24 hours
- Regulatory notification: Not reportable
- Customer notification: Not required

*Investigation Level:* Logged for trending; investigation at discretion of Clinical Safety Officer

#### 5.2.2 Classification Escalation and Dispute Resolution

If there is disagreement on severity classification, the following escalation path applies:
1. Clinical Safety Officer makes initial classification
2. If challenged, VP of Clinical AI Products reviews
3. If unresolved, Chief Medical Officer makes final binding determination
4. If the event is in an EU deployment and could meet the Article 73 threshold, the DPO shall be consulted

Escalation must not delay internal notifications or immediate containment actions.

### 5.3 Immediate Containment Actions

Upon detection of an adverse event classified as Grade A or B, the following containment actions shall be initiated immediately and in parallel with classification and investigation:

| Action | Responsible | Timeline | Documentation Required |
|---|---|---|---|
| **Halt Automated Processing** | SRE / MLOps on call | Within 15 minutes of detection | Change record in ServiceNow, PagerDuty incident log |
| **Activate Human-Only Workflow** | Customer Operations, Clinical Informatics | Within 30 minutes | Notification to all affected customer sites via emergency broadcast |
| **Preserve Evidence** | SRE Lead, CISO | Immediate - before any system changes | Snapshot of model state, input data, output data, logs, telemetry; stored in forensically sound S3 bucket |
| **Notify Clinical Leadership at Affected Sites** | VP of Clinical AI Products or delegate | Within 1 hour (Grade A) or 2 hours (Grade B) | Email template AE-NOTIFY-01 with read receipt tracking |
| **Convene Emergency Response Team** | Clinical Safety Officer | Within 1 hour (Grade A) or 3 hours (Grade B) | Meeting invite with bridge line; record attendance |

For Grade C and D events, containment actions are at the discretion of the Clinical Safety Officer but must be documented in AEMS.

### 5.4 Adverse Event Triage and Intake Workflow

**Step 1: Incident Logging (T+0 to T+1 hour)**
- All adverse events are logged in AEMS (ServiceNow GRC module) using form AE-INTAKE-01.
- Mandatory fields: detection timestamp, source, product/module, model version, affected deployment site(s), preliminary description, detecting person, preliminary severity guess.
- A unique AE identifier is auto-generated in the format: AE-YYYY-NNNNN (e.g., AE-2024-00142).

**Step 2: Initial Triage (T+1 to T+4 hours)**
- Clinical Safety Officer reviews the intake record.
- Assigns severity classification (see Section 5.2).
- Assigns Investigation Lead and team.
- Determines if immediate containment is required.
- If Grade A or B: triggers the Emergency Response Team.
- If event involves EU personal data: notifies DPO (Dr. Klaus Weber).

**Step 3: Evidence Collection (T+0 to T+24 hours)**
- SRE team executes automated evidence preservation runbook AE-RUN-001.
- Evidence collected includes:
  - Model version, configuration, and hyperparameters at time of event
  - Input data payload (full feature vector)
  - Model inference output, confidence scores, and any intermediate representations
  - User session context (de-identified per data minimization principles)
  - System logs (application, infrastructure, security)
  - Datadog dashboards and LangSmith traces for the incident window
  - Any HITL audit records for the affected inference
- Evidence is hashed (SHA-256) and stored in the immutable evidence repository in AWS S3 with legal hold enabled.

**Step 4: Notification (Per timelines in Section 5.2.1)**
- Internal notifications via PagerDuty and email to the distribution list AE-INTERNAL-STEERING@meridian.health
- Customer notifications per SOP-CUST-002 (Customer Incident Communications)
- Regulatory notifications per Section 5.8

### 5.5 Root Cause Analysis (RCA)

#### 5.5.1 RCA Initiation and Methodology

Full formal RCA is mandatory for all Grade A and B adverse events. RCA shall be initiated within 24 hours of event detection and completed within 15 business days. An extension of up to 15 additional business days may be approved by the VP of Clinical AI Products.

**RCA Methodology:**
1. **Problem Statement Development** (Day 1-2): The RCA team develops a precise, factual problem statement describing what occurred, when, where, and the magnitude of impact. The problem statement is reviewed and approved by the Clinical Safety Officer.

2. **Timeline Reconstruction** (Day 1-5): The team creates a minute-by-minute timeline from the earliest relevant precursor through detection, response, and containment. The timeline includes all human actions, automated system events, and external factors.

3. **Ishikawa (Fishbone) Analysis** (Day 3-8): The team systematically examines contributing factors across six dimensions:
   - **People**: Human factors including training, fatigue, workflow pressure
   - **Process**: SOP adequacy, process adherence, workflow design
   - **Technology**: Model architecture, software bugs, infrastructure failures
   - **Data**: Training data quality, input data integrity, distribution shift
   - **Environment**: External factors, clinical setting, integration points
   - **Measurement**: Monitoring gaps, alerting thresholds, metric adequacy

4. **Five Whys Analysis** (Day 5-10): For each significant contributing factor, the "Five Whys" technique is applied to trace back to root cause(s). Root causes must be actionable (something Meridian can correct).

5. **London Protocol Analysis** (Day 7-12): For events involving patient harm, the London Protocol framework is applied to identify contributing factors in the clinical decision-making chain, including:
   - Patient factors
   - Task and technology factors
   - Individual (staff) factors
   - Team factors
   - Work environmental factors
   - Organizational and management factors
   - Institutional context factors

6. **Root Cause Validation** (Day 10-14): Proposed root causes are validated through:
   - Reproduction testing (can the event be reproduced in a controlled environment?)
   - Statistical analysis (is the root cause consistent with the data patterns?)
   - Peer review by an independent qualified individual not involved in the event

7. **RCA Report** (Day 14-15): The RCA report (template RCA-REPORT-01) is drafted, reviewed, and approved. See Section 5.5.3 for report contents.

#### 5.5.2 RCA Team Composition

| Role | Required for Grade A | Required for Grade B |
|---|---|---|
| RCA Lead (appointed by Clinical Safety Officer) | Mandatory | Mandatory |
| Clinical Informatics Specialist (not involved in event) | Mandatory | Mandatory |
| Clinical AI Engineer (model owner) | Mandatory | Mandatory |
| SRE Representative | Mandatory | Recommended |
| Quality Assurance Representative | Mandatory | Mandatory |
| Clinical Subject Matter Expert (e.g., radiologist for imaging AI) | Mandatory | Recommended |
| CISO Representative (if security-related) | Mandatory | Mandatory (if applicable) |
| Legal Representative (for privilege determination) | Mandatory | Recommended |
| Customer Operations Representative | Recommended | Recommended |

#### 5.5.3 RCA Report Contents

The RCA report shall include:
- Executive summary
- Problem statement
- Event timeline
- Severity classification and rationale
- Affected patients/populations (aggregate counts; no PHI in RCA unless clinically necessary)
- Contributing factors across all six Ishikawa dimensions
- Root cause(s) identified with supporting evidence
- Factors that mitigated or amplified harm
- Recommendations for corrective and preventive actions
- Lessons learned
- Attachments: evidence log, reproduction test results, statistical analyses

RCA reports are classified as "Confidential — Attorney-Client Privilege" where legal counsel determines privilege applies. All RCA reports are stored in AEMS with access restricted to the RCA team, Clinical Safety Officer, VP of Clinical AI Products, Chief Medical Officer, and General Counsel.

### 5.6 Corrective and Preventive Action (CAPA)

#### 5.6.1 CAPA Plan Development

A CAPA plan shall be developed for all Grade A and B adverse events. The plan is drafted by the RCA Lead in collaboration with the responsible teams, using template CAPA-PLAN-01.

**CAPA Plan Requirements:**

| Element | Description |
|---|---|
| **Corrective Actions** | Specific actions to correct the immediate nonconformity (e.g., model hotfix, configuration change, retraining) |
| **Preventive Actions** | Actions to prevent recurrence (e.g., enhanced monitoring, training, process redesign, architectural changes) |
| **Action Owner** | Named individual accountable for each action item |
| **Target Completion Date** | Realistic date considering severity; Grade A actions prioritized with aggressive timelines |
| **Success Criteria** | Measurable, verifiable criteria that define when each action is complete |
| **Verification Method** | How the effectiveness of each action will be verified |
| **Risk Assessment** | Residual risk assessment after CAPA implementation |

#### 5.6.2 CAPA Approval Workflow

1. CAPA plan drafted by RCA Lead (within 5 business days of RCA report approval)
2. Review by Clinical Safety Officer (2 business days)
3. Approval by VP of Clinical AI Products (2 business days)
4. For Grade A events: additional approval by Chief Medical Officer and Chief AI Officer
5. For any CAPA requiring model retraining or architectural change: additional approval by Chief AI Officer
6. Final sign-off in ServiceNow GRC

#### 5.6.3 CAPA Implementation and Tracking

- CAPA actions are tracked in ServiceNow GRC with automated status updates and deadline reminders.
- Weekly status reports are generated for all open CAPA actions and reviewed by the Clinical Safety Officer.
- Overdue CAPA actions are escalated: 7 days overdue → Clinical Safety Officer; 14 days → VP of Clinical AI Products; 21 days → Chief Medical Officer.
- CAPA implementation progress is reported monthly to the AI Governance Committee.

#### 5.6.4 CAPA Effectiveness Verification

Within 30-90 days of CAPA implementation (depending on severity and nature), the Quality Assurance Manager conducts an effectiveness check:
- Review of post-CAPA monitoring data to confirm root cause elimination
- Testing of preventive controls
- Review of any new related adverse events
- Documentation of verification results in CAPA-VERIFY-01
- If CAPA is deemed ineffective, a new RCA and CAPA cycle is initiated

### 5.7 Near-Miss and Safety Signal Management

#### 5.7.1 Near-Miss Tracking

All near-misses (Grade C or D events) are logged in AEMS with the designation "Near-Miss" flagged. Near-misses are aggregated monthly for trend analysis. Three or more similar near-misses within a 90-day period shall trigger an automatic escalation to Grade B and require a proactive RCA, even in the absence of actual harm.

#### 5.7.2 Safety Signal Detection and Analysis

The Clinical Safety Officer conducts a monthly safety signal review using:
- Aggregate AE data (all grades)
- Near-miss trends
- Model monitoring telemetry
- Customer feedback themes
- Literature and external database review

If a safety signal is identified:
1. Document in the Safety Signal Register (AEMS module)
2. Conduct preliminary risk assessment within 10 business days
3. If signal is substantiated, initiate proactive RCA and CAPA before additional harm occurs
4. Update the Post-Market Surveillance Plan for the affected AI system
5. Report to AI Governance Committee at next scheduled meeting (or emergency meeting if high-risk)

### 5.8 Regulatory Reporting Procedures

#### 5.8.1 EU AI Act Article 73 Serious Incident Reporting

This section addresses the reporting obligations for serious incidents involving high-risk AI systems deployed in the European Union.

**Determination of Reportability:**
Within 72 hours of becoming aware of a potential serious incident, the Clinical Safety Officer, in consultation with the Chief Medical Officer, DPO (if personal data involved), and General Counsel, shall determine whether the incident meets the Article 3(44) definition of a "serious incident" and therefore requires notification under Article 73.

**Timeline:**
- Notification to the relevant market surveillance authority shall be made immediately upon determination that the incident is reportable, and in any case no later than 15 calendar days after Meridian becomes aware of the serious incident.
- "Becoming aware" is defined as the moment any Meridian employee with AE detection responsibilities (per Section 3.1) has reasonable grounds to suspect a serious incident has occurred.
- If the incident requires urgent safety measures (e.g., immediate model shutdown, urgent field safety notice), the authority shall be notified immediately — without delay — even if the full investigation is incomplete.
- An extension beyond 15 calendar days may be requested from the market surveillance authority with justification. The DPO or General Counsel shall manage extension requests.

**Notification Contents (per Article 73(3)):**
The notification template (EU-AE-NOTIFY-01) shall include:
- AI system identification (name, version, intended purpose, risk classification)
- Description of the incident, including timeline
- Number of individuals affected or potentially affected
- Geographic scope (which EU member states)
- Nature and severity of harm
- Immediate containment actions taken
- Preliminary root cause findings (if available)
- Corrective actions taken or planned
- Contact information for Meridian's DPO and Authorized Representative
- Any relevant technical documentation references

**Follow-up Reporting:**
- Interim reports shall be provided to the market surveillance authority as material new information becomes available during the investigation.
- A final report shall be submitted within 30 calendar days of case closure, summarizing the RCA findings, CAPA implemented, and verification results.

**Market Surveillance Authorities:**
Meridian's DPO maintains the registry of competent market surveillance authorities for each EU member state where Meridian has deployments. As of this SOP version, the primary authorities include:

| Country | Authority |
|---|---|
| Germany | Bundesnetzagentur (BNetzA) — AI oversight |
| France | CNIL (for AI systems processing personal data); DGCCRF (general market surveillance) |
| Ireland | Data Protection Commission (coordinating authority) |
| Netherlands | Autoriteit Persoonsgegevens |
| Spain | Agencia Española de Protección de Datos (AEPD) |

**Coordinated Reporting:**
Where a serious incident affects multiple EU member states, the DPO shall coordinate with the lead market surveillance authority to streamline reporting. Meridian will designate a single point of contact for cross-border incidents.

#### 5.8.2 FDA Adverse Event Reporting

For Clinical AI products that have received FDA 510(k) clearance (currently applicable to the diagnostic imaging AI module), adverse events that meet the FDA's definition of a medical device adverse event shall be reported under 21 CFR Part 803 (Medical Device Reporting). The Clinical Safety Officer shall coordinate with the Regulatory Affairs team (under General Counsel) to ensure compliance with FDA MDR timelines:
- Death or serious injury: Within 30 calendar days
- Other reportable events: Within 30 calendar days of becoming aware
- 5-day reports for events requiring immediate remedial action

**Note**: This section will be expanded when additional Clinical AI products receive FDA clearance beyond the imaging module.

#### 5.8.3 Voluntary Reporting

Even when an adverse event does not meet mandatory reporting thresholds, Meridian may voluntarily report to regulators when:
- The event reveals a systemic safety concern
- Transparency with regulators supports trust and collaborative safety improvement
- The Chief Medical Officer and General Counsel recommend proactive disclosure

Voluntary reports use the same templates as mandatory reports but are marked "VOLUNTARY — NOT REQUIRED UNDER [Regulation]".

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control ID | Control Description | Implementation | Verification |
|---|---|---|---|
| TC-001 | **Automated Model Output Validation**: All model outputs are validated against pre-defined clinical plausibility rules before being presented to end-users. Outputs violating rules are flagged and blocked if configured as "hard stop." | Implemented via AWS Lambda validation layer between SageMaker inference endpoint and application API. Rules defined in collaboration with clinical SMEs. | Rules tested quarterly; blocked output logs reviewed weekly by Clinical Informatics. |
| TC-002 | **Adversarial Robustness Testing**: Models are tested against adversarial inputs as part of the release pipeline and periodically in production. | Integrated into CI/CD pipeline (Jenkins). Production testing via chaos engineering framework (Gremlin) on a monthly cadence, targeting the staging mirror of production models. | Test results reviewed by QA Manager and Clinical AI Engineering Lead. |
| TC-003 | **Immutable Audit Logging**: All model inferences and associated user actions are logged to an append-only, immutable audit trail. | AWS CloudTrail for API-level logging; custom inference logging to append-only S3 bucket with Object Lock in compliance mode (retention: 10 years). | Quarterly audit by CISO team verifying immutability controls. |
| TC-004 | **Automated Bias Detection**: Continuous monitoring for demographic parity, equalized odds, and disparate impact across protected attributes (race, ethnicity, sex, age). | Custom metrics pipeline using Apache Kafka streams, analyzing every inference against patient demographic data. Alerts triggered at >5% disparity. | Bias detection logic reviewed and validated semi-annually by external auditor as part of SOC 2 Type II. |
| TC-005 | **Rollback Capability**: Ability to revert to the last known-good model version within 5 minutes of an adverse event determination. | Implemented via SageMaker multi-model endpoint configuration with weighted routing. Rollback runbook AE-RUN-002 tested quarterly. | Quarterly rollback drills in production by SRE team. |
| TC-006 | **Data Poisoning Defense**: Controls to detect and prevent training data poisoning. | Data validation pipelines check for distribution anomalies, outlier injection, and label flipping before training data ingestion. Hash-based data lineage tracking. | Pre-train data validation reports reviewed by ML Engineering Lead for every training cycle. |
| TC-007 | **Explainability Logging**: SHAP or LIME values logged for every inference to support post-hoc RCA. | LangSmith tracing configured to capture SHAP values for all high-risk inferences; stored alongside inference payload. | Completeness verified monthly. |

### 6.2 Administrative Controls

| Control ID | Control Description | Implementation | Verification |
|---|---|---|---|
| AC-001 | **Segregation of Duties**: No single individual can detect, classify, investigate, and close an adverse event without independent review. | Enforced in ServiceNow GRC through role-based workflow routing. | Access certification review quarterly by CISO. |
| AC-002 | **Post-Market Surveillance Plan**: Each high-risk AI system has a documented PMS plan, reviewed based on AE data. | PMS Plan template PMS-PLAN-01 maintained in the technical documentation repository (Confluence). Annual review with update triggered by any SAE. | Annual review by Clinical Safety Officer; audit trail maintained. |
| AC-003 | **AI Ethics Review**: All Grade A and B adverse events are reviewed by the AI Ethics Advisory Panel. | Panel meets monthly; emergency meetings convened for SAEs. Panel includes external clinical and ethics experts. | Meeting minutes published (with confidential annex). |
| AC-004 | **Change Management Integration**: Any code, model, or configuration change resulting from a CAPA follows the standard change management process with additional CAB review. | SOP-IT-001 (Change Management) applies. CAPA-triggered changes are flagged as "Emergency" or "Urgent" per SOP-IT-001 classification. | Change success rate and rollback instances tracked. |
| AC-005 | **Vendor and Third-Party Model Governance**: Any third-party model integrated into Clinical AI workflows is subject to the same AE management requirements. | Contractual obligation in vendor agreements; right-to-audit clause; vendor must notify Meridian of any AE within 24 hours. | Annual vendor assessment by Clinical Safety Officer and Procurement. |
| AC-006 | **Documented Standard of Care**: Clinical baseline established for each AI use case, against which deviations are measured. | Documented in collaboration with Chief Medical Officer and clinical SMEs; reviewed biennially. | Version controlled in Confluence. |

### 6.3 Physical and Environmental Controls

Not directly applicable to SaaS-based AI systems. However, for on-premises edge deployments at customer sites, physical security of inference hardware is governed by SOP-IT-004 (Physical Security) and the customer's responsibility matrix in the service agreement.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The effectiveness of the adverse event management program is measured through the following KPIs, tracked monthly and reported to the AI Governance Committee quarterly:

| KPI | Target | Measurement Method |
|---|---|---|
| **AE Detection-to-Triage Time** | ≤ 4 hours for 95% of events | AEMS timestamp delta |
| **SAE Detection-to-Containment Time** | ≤ 30 minutes for 99% of Grade A events | AEMS and PagerDuty timestamps |
| **RCA Completion Timeliness** | 90% within 15 business days; 100% within 30 business days | AEMS case tracking |
| **CAPA Implementation On-Time Rate** | ≥ 95% | ServiceNow GRC tracking |
| **CAPA Effectiveness Rate** | ≥ 90% of CAPAs effective on first verification | QA effectiveness check results |
| **AE Reporting Compliance** | 100% of reportable events reported within regulatory timelines | Regulatory submission log vs. AEMS case dates |
| **Repeat AEs** | Zero repeat Grade A or B events from the same root cause within 12 months | AEMS trending analysis |
| **Near-Miss Capture Rate** | Increasing trend quarter-over-quarter (indicating improved safety culture, not increased risk) | AEMS near-miss volume trend |
| **Training Compliance Rate** | ≥ 95% of in-scope personnel completed annual AE training | LMS (Workday Learning) records |

### 7.2 Dashboards and Reporting Cadence

**7.2.1 Real-Time Dashboard**
- A real-time AE dashboard is maintained in Datadog and displayed on the Clinical AI Operations screen in the NOC (Network Operations Center).
- Displays: active events by severity, open investigations, containment status, and regulatory reporting deadlines.
- Integrated with PagerDuty for on-call escalation context.

**7.2.2 Monthly Reports**
- Monthly AE summary report generated by the Clinical Safety Officer.
- Contents: event counts by severity and product, investigation status, CAPA progress, trend analysis, key themes, and any regulatory submissions.
- Distributed to: VP of Clinical AI Products, Chief Medical Officer, Chief AI Officer, CCO, General Counsel, DPO.

**7.2.3 Quarterly Reports**
- Comprehensive quarterly safety report presented to the AI Governance Committee.
- Contents: all monthly data plus trend analysis, safety signals, near-miss aggregation, training compliance, audit findings, and recommendations for SOP revision.
- The AI Governance Committee reviews and may direct changes to risk management practices.

**7.2.4 Annual Report**
- Annual safety and effectiveness report for each high-risk AI system, as part of the EU AI Act technical documentation maintenance requirements.
- Summarizes all AEs, CAPAs, PMS updates, and system improvements for the year.
- Filed in the technical documentation repository and available for regulatory inspection.

### 7.3 Audit and Assurance

- **Internal Audit**: The Internal Audit function (under the Audit Committee of the Board) conducts an annual audit of the AE management program against this SOP and applicable regulations.
- **External Audit**: As part of the annual SOC 2 Type II examination, the external auditor tests controls related to incident management and AE tracking. The HITRUST CSF certification also includes relevant control testing.
- **Regulatory Inspection Readiness**: All AE documentation is maintained in an inspection-ready state. The DPO and General Counsel conduct annual mock inspections.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Requests

Deviations from this SOP may be necessary in limited, justified circumstances. Exception requests are submitted via ServiceNow using form EXCEPTION-REQ-01 and must include:
- Specific SOP section(s) from which deviation is requested
- Business or technical justification
- Risk assessment of the deviation
- Compensating controls proposed
- Duration of the exception (not to exceed 12 months)

### 8.2 Exception Approval Authority

| Exception Type | Approval Authority | Maximum Duration |
|---|---|---|
| Minor procedural deviation (e.g., extended timeline by ≤5 business days) | Clinical Safety Officer | 30 days |
| Moderate procedural deviation (e.g., modified RCA scope, alternative classification) | VP of Clinical AI Products | 90 days |
| Major procedural deviation (e.g., waiver of RCA, deferral of CAPA) | Chief Medical Officer + Chief AI Officer jointly | 12 months with quarterly review |
| Regulatory reporting timeline extension | General Counsel + DPO jointly; may require regulatory approval | As authorized |

### 8.3 Escalation Paths

**Operational Escalation (Timeline Breaches):**
1. AE triage not completed within SLA → Clinical Safety Officer
2. RCA not completed within 15 business days → VP of Clinical AI Products
3. CAPA overdue by 7 days → VP of Clinical AI Products
4. CAPA overdue by 21 days → Chief Medical Officer
5. Regulatory filing deadline approaching with risk of breach → General Counsel + DPO immediately

**Clinical Safety Escalation:**
1. Any disagreement on patient harm severity → Chief Medical Officer
2. Any concern that AE poses ongoing patient risk → Immediate halt of system + Chief Medical Officer + CEO notification (Dr. Sarah Chen)

**Regulatory Escalation:**
1. Any potential Article 73 notifiable incident → DPO within 2 hours of suspicion
2. Any FDA MDR-reportable event → General Counsel + Regulatory Affairs within 4 hours

### 8.4 Whistleblower and External Reporting

Employees who believe that adverse events are not being appropriately managed internally may report concerns through:
- Meridian Ethics Hotline (anonymous, managed by third-party provider EthicsPoint): 1-800-MERIDIAN-ETHICS or www.meridian.ethicspoint.com
- Direct communication to the Chief Compliance Officer (Thomas Anderson)
- Direct communication to the Chair of the AI Governance Committee of the Board

External reporting to regulators by employees is protected under applicable whistleblower protection laws. Meridian policy strictly prohibits retaliation as stated in PS-002.

---

## 9. Training Requirements

### 9.1 Role-Based Training Requirements

| Role | Initial Training | Annual Refresher | Specialized Modules |
|---|---|---|---|
| Clinical AI Engineers and MLOps | AE-SOP Training (4 hours) + AE Detection Tools (2 hours) | 2 hours | RCA Methodology Workshop (for RCA Leads) |
| Clinical Informatics Specialists | AE-SOP Training (4 hours) + AE Triage Simulation (3 hours) | 2 hours | HITL Audit Program Training (annual, 2 hours) |
| SRE Team | AE-SOP Training (3 hours) + Evidence Preservation Runbook (2 hours) | 1.5 hours | Rollback Drill participation (quarterly) |
| Customer Operations | AE-SOP Training (2 hours) + AE Intake Procedures (1 hour) | 1 hour | Communication templates update (as needed) |
| Management (Directors and above in scope) | AE-SOP Training (2 hours) + Regulatory Obligations Briefing (1 hour) | 1.5 hours | Leadership escalation simulation (biennial) |
| Quality Assurance | AE-SOP Training (3 hours) + CAPA Management (2 hours) | 2 hours | CAPA Effectiveness Verification (annual, 2 hours) |
| Legal, Compliance, DPO Office | AE-SOP Training (2 hours) + Regulatory Reporting (2 hours) | 2 hours | EU AI Act Updates (ad hoc, as regulation evolves) |

### 9.2 Training Delivery and Tracking

- All training modules are delivered through Meridian's learning management system (Workday Learning).
- Initial training must be completed within 30 days of role assumption.
- Training records are maintained in Workday and auditable.
- Training completion rate is reported monthly to the Clinical Safety Officer.
- Personnel who fail to complete required training within the grace period (30 days past due date) shall have their access to Clinical AI production systems suspended until training is completed. The VP of Clinical AI Products and the individual's manager are notified of any suspension.

### 9.3 Competency Assessment

Training effectiveness is assessed through:
- Post-training knowledge checks (minimum 80% passing score)
- Annual Tabletop Exercise simulating a Grade A adverse event (mandatory for all personnel with RCA or emergency response responsibilities)
- Direct observation of triage and evidence preservation during simulated events for SRE and Clinical Informatics teams

### 9.4 Training Content Updates

Training content is reviewed and updated by the Clinical Safety Officer:
- Annually as part of SOP review cycle
- Within 30 days of any significant SOP revision
- Within 30 days of any material regulatory change (e.g., EU AI Act delegated acts or guidance)
- Within 60 days of any SAE that reveals a training gap

---

## 10. Related Policies and References

### 10.1 Meridian Internal Documents

| Document ID | Title | Relationship |
|---|---|---|
| SOP-CLIN-001 | Clinical AI System Development Lifecycle | Defines model development and validation processes that produce the systems monitored by this SOP |
| SOP-CLIN-003 | Model Monitoring and Performance Management | Defines automated monitoring thresholds, drift detection, and alerting configuration referenced in Section 5.1.3 |
| SOP-CLIN-004 | Human Oversight and Human-in-the-Loop Operations | Operationally defines HITL audit requirements referenced in Section 5.1.2 |
| SOP-CLIN-005 | Post-Market Surveillance Plan | Contains the system-specific PMS plans required under EU AI Act Article 61; this SOP operationalizes AE management within PMS |
| SOP-CLIN-006 | Clinical AI Risk Management Framework | Defines the overarching risk management approach aligned with NIST AI RMF, under which this SOP operates |
| SOP-FIN-014 | SR 11-7 Model Risk Management for Financial Models | Defines AE management for HealthPay models (out of scope for this SOP but structurally aligned) |
| SOP-IT-001 | IT Change Management | Governs changes resulting from CAPA plans |
| SOP-IT-003 | IT Incident Management | Governs infrastructure incidents that may intersect with clinical AEs |
| SOP-IT-005 | Security Incident Response | Governs security incidents that may become clinical AEs |
| SOP-CUST-002 | Customer Incident Communications | Defines templates and protocols for notifying customers of incidents |
| SOP-LEG-001 | Regulatory Notification and Engagement | Defines legal review process for regulatory submissions |
| SOP-COMP-001 | Whistleblower and Non-Retaliation Policy | Reinforces PS-002 protections |

### 10.2 External Standards and Regulations

| Reference | Title | Applicability |
|---|---|---|
| EU Regulation 2024/1689 | EU AI Act (Artificial Intelligence Act) | Full compliance for high-risk AI systems; Articles 3, 11, 14, 61, 73 specifically |
| NIST AI RMF 1.0 | Artificial Intelligence Risk Management Framework | Voluntarily adopted governance framework; Maps to Govern 3.2, Map 4.1, Measure 2.3, Manage 3.2 |
| ISO 14971:2019 | Medical Devices — Application of Risk Management to Medical Devices | Applied to FDA-cleared and CE-marked clinical AI products |
| IMDRF/GRRP WG/N47 | IMDRF Adverse Event Terminology | Applied for FDA-reportable events |
| ISO 27001:2022 | Information Security, Cybersecurity and Privacy Protection | Controls for evidence preservation, access control, and audit logging |
| SOC 2 | Trust Services Criteria (Security, Availability) | Control framework for the SaaS platform |
| HITRUST CSF v11 | HITRUST Common Security Framework | Certified controls applicable to incident management |

---

## 11. Revision History

| Version | Date | Author | Approver | Summary of Changes |
|---|---|---|---|---|
| 1.0 | 2021-03-15 | Dr. Aisha Okafor | Dr. Priya Patel | Initial version. Established foundational AE detection and reporting framework for Clinical AI Platform. Incorporated FDA MDR requirements for first 510(k)-cleared imaging product. |
| 2.0 | 2022-09-01 | Dr. Aisha Okafor, with Clinical Safety Working Group | Dr. Priya Patel | Major revision. Added automated detection signals and Datadog integration. Expanded RCA methodology to include London Protocol. Added near-miss tracking program. Aligned with new HITRUST CSF certification. |
| 3.0 | 2023-04-20 | Clinical Safety Officer (new role) | Dr. Priya Patel, Dr. Sarah Chen | Added EU AI Act preparatory framework ahead of enforcement. Introduced Grade A-D severity classification replacing previous three-tier system. Established dedicated Clinical Safety Officer role. Integrated LangSmith AI tracing. Added Article 73 reporting workflow (provisional, pending final regulation). |
| 4.0 | 2024-01-10 | Clinical Safety Officer, Dr. Klaus Weber (DPO) | Dr. Priya Patel, Dr. Marcus Rivera | Finalized EU AI Act compliance framework post-regulation publication. Added specific Article 73 notification procedures and market surveillance authority registry. Aligned with NIST AI RMF 1.0. Added CAPA effectiveness verification process. Updated to ISO 27001:2022. |
| 4.1 | 2024-03-28 | Clinical Safety Officer | Dr. Aisha Okafor | Minor revision. Updated notification templates per regulatory guidance. Added specific timelines for human oversight audit sampling. Corrected cross-references to SOP-CLIN-006. |
| 4.2 | 2024-05-15 | Clinical Safety Officer, General Counsel | Dr. Priya Patel | Updated legal review workflow for regulatory notifications. Added privilege guidance for RCA documentation. Expanded vendor AE management requirements (AC-005). Incorporated lessons learned from tabletop exercise conducted March 2024. |
| 4.3 | 2024-06-05 | Clinical Safety Officer | Dr. Priya Patel | Current version. Updated classification dispute resolution process (Section 5.2.2). Added automated bias detection control (TC-004). Refined KPI targets based on 18 months of operational data. Updated market surveillance authority contacts post-Germany designation. Added explicit timelines for evidence hash verification. Extended RCA report peer review requirement to Grade B events. |

---

## Document End

**SOP-CLIN-007 | Version 4.3 | Classification: Internal**

© 2024 Meridian Health Technologies, Inc. All rights reserved. This document contains proprietary and confidential information. Distribution, reproduction, or disclosure outside of Meridian Health Technologies is prohibited without prior written authorization from the VP of Clinical AI Products or General Counsel.
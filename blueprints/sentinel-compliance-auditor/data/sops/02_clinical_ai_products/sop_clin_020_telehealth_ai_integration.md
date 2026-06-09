---
sop_id: "SOP-CLIN-020"
title: "Telehealth AI Integration"
business_unit: "Clinical AI Products"
version: "5.9"
effective_date: "2025-10-28"
last_reviewed: "2026-03-23"
next_review: "2026-09-11"
owner: "Dr. Aisha Okafor, VP of Clinical AI Products"
approver: "Dr. Priya Patel, Chief Medical Officer"
classification: "Internal"
regulations:
  - "HIPAA"
  - "EU AI Act"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Telehealth AI Integration

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the governance framework, operational procedures, technical controls, and monitoring requirements for the integration of Meridian Health Technologies' Clinical AI Platform with telehealth service delivery systems. As telehealth has evolved from a pandemic-era necessity to a permanent care delivery modality—representing approximately 38% of all clinical encounters processed through Meridian's systems—the integration of AI-assisted triage, diagnostic support, and remote patient monitoring capabilities into virtual care workflows requires standardized, auditable, and regulation-compliant operational practices.

This document defines the end-to-end lifecycle management of AI models deployed within telehealth contexts, including model selection, deployment, monitoring, human oversight, data handling, security controls, and decommissioning. It establishes the operational rhythm by which Meridian ensures that AI-augmented telehealth services meet clinical safety standards, regulatory obligations, and contractual commitments to healthcare delivery organization customers.

### 1.2 Scope

This SOP applies to:

- **All Clinical AI Platform models** deployed in or interfacing with telehealth platforms operated by or integrated with Meridian's customers, including but not limited to synchronous video consultation support, asynchronous store-and-forward triage, chatbot-based symptom checking, and remote patient monitoring (RPM) data interpretation.
- **All Meridian personnel** who design, develop, test, deploy, monitor, maintain, or decommission AI models used in telehealth contexts, including full-time employees, contractors, and third-party vendors with system access.
- **All Meridian business units** that contribute to telehealth AI delivery, including Clinical AI Products, MedInsight Analytics, Meridian SaaS Platform, and HealthPay Financial Services where payment or claims models intersect with telehealth encounters.
- **All geographic regions** where Meridian operates, including North America (US, Canada) and the European Union (via EU entities and cross-border processing).
- **All data types** processed in telehealth AI workflows, including Protected Health Information (PHI), personally identifiable information (PII), clinical data, device data from remote monitoring, and patient-reported outcomes.

### 1.3 Out of Scope

- AI models used exclusively for in-person clinical encounters (see SOP-CLIN-015: Clinical AI Model Lifecycle Management).
- General-purpose infrastructure monitoring and operational analytics (see SOP-IT-080: Observability and Monitoring Standards).
- Financial models used exclusively for claims adjudication without clinical data (see SOP-FIN-045: HealthPay Model Risk Management).
- Research and development activities conducted outside of production or pre-production environments without patient-facing impact.

### 1.4 Audience

The primary audiences for this SOP are:
- Clinical AI engineering teams
- Clinical validation and safety teams
- Information security and privacy operations teams
- Compliance and regulatory affairs personnel
- Customer operations and implementation teams
- Quality assurance and testing teams

---

## 2. Definitions and Acronyms

### 2.1 Acronyms

| Acronym | Definition |
|---------|------------|
| AI | Artificial Intelligence |
| API | Application Programming Interface |
| AUC-ROC | Area Under the Receiver Operating Characteristic Curve |
| BA | Business Associate (under HIPAA) |
| BAA | Business Associate Agreement |
| CDS | Clinical Decision Support |
| CI/CD | Continuous Integration / Continuous Deployment |
| CISO | Chief Information Security Officer |
| CMO | Chief Medical Officer |
| CPO | Chief Privacy Officer |
| DPO | Data Protection Officer |
| ePHI | Electronic Protected Health Information |
| FDA | U.S. Food and Drug Administration |
| FHIR | Fast Healthcare Interoperability Resources |
| HITRUST | Health Information Trust Alliance |
| HITL | Human-in-the-Loop |
| KMS | Key Management Service |
| MDR | Medical Device Regulation (EU) |
| ML | Machine Learning |
| MLOps | Machine Learning Operations |
| NIST AI RMF | National Institute of Standards and Technology AI Risk Management Framework |
| PHI | Protected Health Information |
| PII | Personally Identifiable Information |
| RPM | Remote Patient Monitoring |
| SaaS | Software as a Service |
| SLA | Service Level Agreement |
| SOC | System and Organization Controls |
| SOP | Standard Operating Procedure |
| SR 11-7 | Supervision and Regulation Letter 11-7 (Federal Reserve) |
| TLS | Transport Layer Security |
| VPC | Virtual Private Cloud |

### 2.2 Definitions

**AI-Assisted Triage:** The use of machine learning models to analyze patient-reported symptoms, vital signs, and clinical history to generate a recommended acuity level, suggested care pathway, or prioritization score for telehealth encounters. AI-assisted triage provides recommendations to qualified clinical personnel who retain decision-making authority.

**Clinical AI Platform:** Meridian's suite of AI/ML models, infrastructure, and services that provide clinical decision support, diagnostic analysis, risk scoring, and prediction capabilities, deployed across the Meridian SaaS Platform.

**Clinical Safety Incident:** Any event in which an AI model output contributed to or could have contributed to patient harm, delayed appropriate care, recommended inappropriate care, or produced a clinically significant error that reached a clinician or patient.

**Concept Drift:** A degradation in model performance caused by changes in the underlying relationships between input features and target outputs, distinct from data drift which concerns changes in input feature distributions alone.

**Human-in-the-Loop (HITL):** A system design in which AI model outputs are reviewed, validated, overridden, or approved by qualified human operators before affecting clinical decisions or patient care workflows.

**Override Rate:** The percentage of AI model recommendations that are modified or rejected by the reviewing clinician, calculated as (Number of Overrides / Total Recommendations Presented) × 100.

**Remote Patient Monitoring (RPM):** The collection, transmission, and analysis of patient physiological data from devices located outside traditional clinical settings, including wearable sensors, home monitoring equipment, and patient-reported data collected via digital applications.

**Silent Mode:** A model deployment state in which the model generates inferences and recommendations that are logged and monitored but not displayed to clinicians or patients, used for performance validation prior to go-live.

**Telehealth Platform:** The integrated software, hardware, and network infrastructure enabling synchronous and asynchronous remote clinical encounters between healthcare providers and patients, including video conferencing, secure messaging, file exchange, and device data integration.

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix

The following RACI matrix establishes accountability for key activities within this SOP:

| Activity / Decision | VP Clinical AI Products | Chief Medical Officer | CISO / Security | Clinical Validation Lead | MLOps Lead | Customer Ops | Compliance Officer | AI Ethics Board |
|---------------------|------------------------|----------------------|-----------------|-------------------------|------------|---------------|-------------------|-----------------|
| Model approval for telehealth deployment | A | R | C | R | C | I | I | C |
| Clinical safety validation sign-off | C | A | I | R | I | I | I | C |
| Security architecture review | I | I | A | I | R | I | C | I |
| Telehealth-specific model monitoring thresholds | A | C | I | R | R | I | I | I |
| Patient-facing output review | I | A | I | R | I | C | I | C |
| Exception approval for model drift | A | R | I | R | C | I | I | I |
| Customer communication for model issues | I | C | I | I | I | R | A | I |
| Regulatory submission for telehealth AI | C | A | I | R | I | I | R | C |
| Decommissioning decision | A | R | I | C | R | C | I | I |

**R = Responsible (executes), A = Accountable (approves), C = Consulted (provides input), I = Informed (receives notification)**

### 3.2 Role Descriptions

**VP of Clinical AI Products (Dr. Aisha Okafor):** Serves as the executive owner of all telehealth AI models. Accountable for model portfolio strategy, resource allocation, and overall compliance with this SOP. Chairs the monthly Telehealth AI Operations Review.

**Chief Medical Officer (Dr. Priya Patel):** Provides clinical governance for all telehealth AI deployments. Accountable for clinical safety determinations, escalation of safety incidents to the AI Governance Committee, and final approval of patient-facing model outputs.

**Chief Information Security Officer (Rachel Kim):** Accountable for the security architecture of telehealth AI data flows, encryption standards, access controls, and incident response procedures involving potential data compromise.

**Clinical Validation Lead:** Responsible for designing and executing clinical validation protocols for telehealth AI models, including prospective silent-mode testing, retrospective chart review studies, and ongoing performance monitoring against clinical benchmarks.

**MLOps Lead:** Responsible for the technical implementation of model deployment pipelines, monitoring infrastructure, automated alerting, and rollback procedures for telehealth AI models.

**Chief Compliance Officer (Thomas Anderson):** Accountable for regulatory submissions, audit readiness, and compliance monitoring related to telehealth AI. Maintains the inventory of applicable regulatory requirements.

**AI Ethics Board:** A cross-functional governance body including clinical, technical, legal, and ethics expertise. Consults on fairness assessments, bias monitoring, and ethical implications of telehealth AI deployment decisions.

**Customer Operations:** Responsible for customer-facing communications regarding telehealth AI model status, planned maintenance, incidents, and performance reporting.

---

## 4. Policy Statements

### 4.1 Clinical Safety Primacy

All AI models deployed in telehealth contexts shall prioritize patient safety above all other considerations, including operational efficiency, cost reduction, and provider convenience. No AI model shall operate autonomously in any clinical decision context without qualified human oversight. Every AI-generated recommendation, score, or insight presented to a clinician or patient shall be accompanied by:
- A confidence score or equivalent uncertainty quantification
- The date and time of model inference
- The model version identifier
- Documentation of the model's intended use and limitations, accessible within two interactions from the point of output display

### 4.2 Human Oversight Requirement

All telehealth AI models classified as high-risk under the EU AI Act shall operate exclusively in Human-in-the-Loop (HITL) mode for any output that could influence clinical decisions. HITL architecture shall ensure that:
- Clinicians can review all AI-generated recommendations before clinical action is taken
- Clinicians can override any AI recommendation and document the rationale for the override
- Override data is systematically captured and used for model improvement
- The system prevents "automation bias" through user interface design that presents AI recommendations alongside clinical evidence sources
- Clinicians are not measured or incentivized based on their rate of agreement with AI recommendations

### 4.3 Data Minimization and Purpose Limitation

Telehealth AI models shall process only the minimum necessary data required to perform their clinically validated function. Data collected during telehealth encounters for AI processing shall not be repurposed for model training, research, or product development without explicit authorization documented in accordance with applicable data protection requirements. Any secondary use of telehealth data shall require:
- Approval from the Chief Medical Officer
- Approval from the Chief Compliance Officer
- A documented legal basis for processing
- Notification to the AI Ethics Board
- Where applicable, documented patient consent that is specific, informed, and freely given

### 4.4 Model Versioning and Traceability

Every telehealth AI model shall maintain a complete, immutable audit trail connecting each inference output to:
- The specific model version and configuration used
- The training data provenance and temporal window
- The validation results and approval records
- The deployment timestamp and approving authority
- All post-deployment modifications, patches, and parameter adjustments

This audit trail shall be preserved for a minimum period defined by the Legal and Compliance function, consistent with applicable statutes of limitation and medical record retention requirements.

### 4.5 Transparency to Patients

Patients engaged in telehealth encounters augmented by Meridian AI shall be informed:
- That AI tools are being used to support their clinician
- Of the general nature and purpose of the AI tools
- That all clinical decisions are made by their healthcare provider, not by automated systems
- Of their right to request that AI tools not be used during their encounter, where operationally feasible

Meridian provides standardized patient-facing disclosure language to all telehealth customer organizations; customer organizations are contractually obligated to present these disclosures. Meridian shall not deploy models that operate in patient-facing contexts without clinician intermediary unless the model has undergone a specific patient-facing validation protocol approved by the CMO.

### 4.6 Breach Notification

In the event of a breach involving ePHI within any telehealth AI data flow—whether occurring at the point of data ingestion, during model inference processing, in transmission, or at rest—the incident response procedures defined in SOP-IS-120 (Information Security Incident Response) shall be activated immediately. Meridian shall notify affected Covered Entities without unreasonable delay following discovery of the breach, providing sufficient detail to enable the Covered Entity to fulfill its notification obligations to affected individuals and relevant regulatory authorities. All breach notifications shall be coordinated through the CISO and Chief Privacy Officer.

### 4.7 Model Retirement

Telehealth AI models shall be proactively decommissioned when:
- Performance against established clinical benchmarks falls below the defined minimum threshold for a period exceeding 30 days
- A clinical safety incident attributable to model performance has been confirmed
- The clinical use case for which the model was validated changes substantively
- A superior replacement model has completed validation and Silent Mode observation
- Regulatory or legal requirements mandate decommissioning

All model decommissioning shall follow a structured wind-down protocol that ensures no interruption to clinical care and preservation of all audit records.

---

## 5. Detailed Procedures

### 5.1 Telehealth AI Model Candidate Intake and Pre-Deployment Assessment

#### 5.1.1 Model Candidate Submission

Any Meridian team or customer proposing a new AI model for telehealth deployment shall submit a completed Form CLIN-TEL-001: Telehealth AI Model Intake Request through the ServiceNow Clinical AI Intake portal. The form shall include:

- Proposed clinical use case and intended patient population
- Expected telehealth integration modality (synchronous video, asynchronous triage, chatbot, RPM)
- Proposed model architecture, input features, and output type
- Anticipated clinical workflow impact
- Preliminary data requirements and availability assessment
- Proposed go-to-market timeline
- Customer sponsor identification (if customer-driven)

#### 5.1.2 Triage and Classification

Upon submission, the Clinical Validation Lead shall classify the proposed model using the Meridian Telehealth AI Risk Classification Matrix:

| Risk Tier | Criteria | Max Latency to Clinical Review |
|-----------|----------|-------------------------------|
| Tier 1 – Highest Risk | Model outputs directly influence diagnostic decisions, medication recommendations, or acuity-based care prioritization AND operate in real-time synchronous telehealth encounters | 5 business days |
| Tier 2 – Elevated Risk | Model outputs influence care pathway selection, specialist referral, or patient monitoring escalation thresholds | 10 business days |
| Tier 3 – Moderate Risk | Model provides decision support for non-diagnostic workflows, patient scheduling optimization, or administrative triage | 20 business days |
| Tier 4 – Low Risk | Model provides analytics or insights not visible during the clinical encounter (post-hoc quality review, population health analytics) | 30 business days |

The classification methodology considers the combination of clinical impact severity and telehealth delivery modality. Models operating in asynchronous telehealth contexts where clinicians have extended time for review may be classified one tier lower, subject to CMO concurrence.

#### 5.1.3 Pre-Deployment Review

All Tier 1 and Tier 2 models shall undergo a pre-deployment review by the AI Ethics Board. The review shall assess:
- Fairness across demographic subgroups using historical telehealth utilization data
- Potential for differential performance in populations with limited digital literacy
- Accessibility considerations for patients with disabilities
- Language and health literacy considerations for patient-facing elements
- Documentation of known limitations and failure modes

The Pre-Deployment Review summary shall be appended to the model's permanent validation record.

### 5.2 Clinical Validation and Silent Mode Deployment

#### 5.2.1 Retrospective Validation

Before any telehealth AI model is deployed to production, the Clinical Validation team shall complete a retrospective validation study using a minimum dataset defined by model risk tier:

| Risk Tier | Minimum Retrospective Cases | Minimum AUC-ROC | Calibration Metric |
|-----------|----------------------------|-----------------|-------------------|
| Tier 1 | 50,000 | ≥ 0.92 | Brier Score ≤ 0.05 |
| Tier 2 | 25,000 | ≥ 0.85 | Brier Score ≤ 0.08 |
| Tier 3 | 10,000 | ≥ 0.78 | Calibration-in-the-large ≤ 0.10 |
| Tier 4 | 5,000 | ≥ 0.72 | Qualitative assessment |

All performance thresholds must be met across predefined demographic subgroups (age groups, sex assigned at birth, race/ethnicity categories, primary language). Any subgroup with performance below 90% of the overall metric shall trigger an automatic fairness review by the AI Ethics Board, with deployment held pending satisfactory mitigation or documented acceptance of residual disparity by the CMO.

#### 5.2.2 Silent Mode Observation

Following completion of retrospective validation and approval by the Clinical Validation Lead, all Tier 1, Tier 2, and Tier 3 models shall undergo a Silent Mode observation period:

| Risk Tier | Minimum Silent Mode Duration | Minimum Silent Mode Inference Volume | Maximum Acceptable Safety Flag Rate |
|-----------|------------------------------|--------------------------------------|-------------------------------------|
| Tier 1 | 90 calendar days | ≥ 10,000 inferences | ≤ 0.05% safety flags |
| Tier 2 | 60 calendar days | ≥ 5,000 inferences | ≤ 0.10% safety flags |
| Tier 3 | 30 calendar days | ≥ 2,000 inferences | ≤ 0.25% safety flags |

During Silent Mode, the model generates inferences that are logged to the Meridian Clinical AI Monitoring Dashboard (accessible to Clinical Validation and MLOps teams) but NOT displayed to clinicians or patients. The Clinical Validation Lead shall conduct weekly reviews of:
- Safety flag rate and classification
- Subgroup performance parity metrics
- Override rate among mock review (a subset of silent inferences is presented to a panel of three board-certified clinicians in the relevant specialty who are blinded to whether the inference is from the candidate model or a reference standard)
- Any unexpected model behavior or edge case failures

The CMO shall provide written approval to exit Silent Mode before any model becomes visible in production telehealth workflows.

### 5.3 Production Deployment and Go-Live

#### 5.3.1 Go-Live Readiness Checklist

Before production deployment, the following checklist items shall be completed and documented in the Meridian Clinical AI Model Registry:

- [ ] Clinical Validation Report approved by CMO
- [ ] Silent Mode exit approval signed by CMO
- [ ] Security architecture review completed and approved by CISO (or delegate)
- [ ] Monitoring dashboards configured and alerts tested, including:
    - Model performance degradation alert (threshold: ≥ 10% relative decline in AUC-ROC or F1 score versus silent mode baseline)
    - Concept drift alert (threshold: drift magnitude ≥ 0.15 as measured by maximum mean discrepancy)
    - Output distribution shift alert (threshold: ≥ 20% change in 7-day rolling average of prediction distribution)
    - Latency alert (threshold: P99 inference latency ≥ 2000ms for synchronous telehealth models)
    - Safety flag rate alert (threshold: any safety flag, immediate notification)
- [ ] Rollback plan documented and tested (target: rollback initiated within 15 minutes of rollback decision)
- [ ] Customer-facing documentation updated (model card, intended use statement, limitations disclosure)
- [ ] Clinician training materials delivered to Customer Operations for distribution
- [ ] All regulatory submissions completed and acknowledged
- [ ] AI Ethics Board notified of production deployment date

#### 5.3.2 Phased Rollout

Tier 1 and Tier 2 models shall be deployed using a phased rollout strategy:

| Phase | Duration | Scope | Go/No-Go Criteria for Expansion |
|-------|----------|-------|----------------------------------|
| Phase 1 – Pilot | Minimum 14 days | ≤ 5% of target telehealth encounter volume, limited to ≤ 3 customer organizations, limited to specific geographies | No Tier-1 safety incidents; Override rate within 2σ of silent mode rate |
| Phase 2 – Limited Expansion | Minimum 30 days | ≤ 25% of target volume, ≤ 25% of planned customer base | No Tier-1 safety incidents; Performance metrics within 95% confidence interval of silent mode baseline; Sync latency consistently within SLA |
| Phase 3 – Full Scale | Ongoing | 100% of target volume, all planned customers | Phase 2 approval by VP Clinical AI Products and CMO |

Any safety incident classified as Tier-1 (actual or potential patient harm) shall trigger immediate suspension of further expansion and a root cause analysis within 5 business days.

### 5.4 Telehealth-Specific Integration Workflows

#### 5.4.1 Synchronous Video Consultation AI Integration

For AI models integrated into real-time video telehealth encounters, the following technical workflow shall be implemented:

**Step 1 – Encounter Initiation:** Upon telehealth session establishment, the Meridian Clinical AI API receives a session initialization payload including:
- FHIR R4 Patient resource (demographics)
- FHIR R4 Encounter resource (encounter type, reason for visit)
- Relevant clinical history (FHIR Condition, MedicationStatement, Observation resources from the past 12 months, limited to elements specified in the model's Minimum Necessary Data specification)

**Step 2 – Pre-Encounter Inference:** Within 90 seconds of encounter initiation, the Clinical AI Platform executes pre-encounter inference generating:
- Patient summary with highlighted risk factors
- Suggested agenda items based on clinical history and reason for visit
- Any relevant clinical decision support alerts

Outputs are rendered in the clinician's telehealth dashboard sidebar.

**Step 3 – Real-Time Inference:** During the encounter, clinicians may invoke AI model inference through the "AI Insights" button. Real-time inference shall complete within 1500ms of invocation to avoid disrupting clinical conversation flow. All real-time inferences shall display a confidence score and the timestamp of inference.

**Step 4 – Post-Encounter Documentation:** Within 180 seconds of encounter termination, the Clinical AI Platform generates:
- Structured encounter summary for clinician review
- Suggested billing codes (for clinician validation only)
- Follow-up recommendations based on encounter documentation
- Any triggered clinical decision support alerts requiring clinician acknowledgment

All post-encounter outputs shall be queued for clinician review in the telehealth dashboard; no output shall be committed to the patient's permanent medical record without explicit clinician approval.

#### 5.4.2 AI-Assisted Asynchronous Triage

For AI models deployed in asynchronous (store-and-forward) telehealth triage workflows:

**Step 1 – Patient Submission Receipt:** Upon receipt of a patient-submitted asynchronous consultation request (including structured symptom questionnaire, uploaded images, and optionally RPM device data), the Meridian Clinical AI Platform shall within 120 seconds:
- Validate data completeness against the model's required input schema
- Flag any critical alerts (e.g., suicidal ideation keywords, severe symptom patterns) for immediate human review regardless of triage queue position
- Generate a triage recommendation including:
    - Recommended acuity level on a 5-point scale (1 = immediate emergency referral, 5 = routine follow-up)
    - Suggested response timeframe
    - Recommended specialist type if referral indicated

**Step 2 – Clinician Review Queue:** Triage recommendations shall populate the clinician's asynchronous consultation review queue. Cases shall be sorted by recommended acuity level by default; clinicians may re-sort and filter. The AI triage recommendation shall be displayed alongside the original patient submission, with the AI recommendation visually distinguished (amber highlight) from patient-submitted content to prevent automation bias.

**Step 3 – Clinician Disposition:** The reviewing clinician shall:
- Review the AI triage recommendation
- Review the original patient submission
- Document their independent triage determination
- If the clinician's determination differs from the AI recommendation, the system shall prompt the clinician to select a reason for override from a structured dropdown (not free text, to enable systematic analysis):
    - Clinical complexity beyond model scope
    - Patient history not adequately captured
    - Suspicion of inaccurate patient-reported data
    - Concern for urgent condition not captured by model
    - Other (with optional brief comment)

**Step 4 – Feedback Loop:** All override events with their structured reasons shall be logged to the Meridian Clinical AI Monitoring Dashboard and flagged for quarterly review by the Clinical Validation team as potential training data or model architecture improvement opportunities.

#### 5.4.3 Remote Patient Monitoring AI Integration

For AI models processing data from remote patient monitoring (RPM) devices integrated with telehealth platforms:

**Step 1 – Device Data Ingestion:** RPM device data shall be ingested through the Meridian SaaS Platform's FHIR R4 Observation ingestion API. Supported RPM data types include:
- Continuous glucose monitoring (CGM) readings
- Blood pressure readings from validated home monitors
- Pulse oximetry (SpO2) data
- Weight scale readings
- Cardiac rhythm data from FDA-cleared consumer and medical-grade wearables
- Spirometry readings from home spirometers
- Patient-reported outcome measures (PROMs) collected via digital questionnaires

All ingested RPM data shall be associated with:
- Device identifier and manufacturer
- FDA listing/clearance status (if applicable)
- Timestamp of measurement
- Timestamp of data transmission
- Patient identifier

**Step 2 – AI Model Inference Triggering:** AI model inference for RPM data shall be triggered:
- On every new data ingestion (real-time processing; target latency: ≤ 500ms from ingestion to inference completion)
- On a scheduled cadence (configurable per model; default: every 4 hours for models analyzing trends across multiple readings)
- On clinician manual invocation during chart review

**Step 3 – Alert Generation:** When AI model inference on RPM data detects a condition meeting pre-configured alert criteria, the system shall:
- Generate an alert in the Meridian Alerts Service within 30 seconds of detection
- Populate the alert with:
    - The triggering measurement(s)
    - The AI model's interpretation
    - Relevant clinical context (trend data, comparison to baseline)
    - Recommended clinical action
    - Urgency level (Critical, High, Moderate, Informational)
- Route the alert according to the customer organization's configured escalation path (which may include: provider in-basket, push notification to mobile device, secure SMS, escalation to on-call clinician if no acknowledgment within configurable time window)

**Step 4 – Alert Acknowledgment and Closure:** All alerts shall require explicit clinician acknowledgment. Alert lifecycle shall be tracked through the Meridian Alerts Dashboard with timestamps for:
- Alert generation
- Alert delivery to clinician
- Clinician acknowledgment
- Clinical action taken (if documented)
- Alert closure

Alert acknowledgment SLA shall default to:
- Critical: 15 minutes maximum
- High: 60 minutes maximum
- Moderate: 4 hours maximum
- Informational: Next business day

Customer organizations may configure more stringent SLAs; Meridian shall not support less stringent SLAs for Critical alerts.

### 5.5 Model Monitoring and Performance Management

#### 5.5.1 Automated Monitoring Infrastructure

All deployed telehealth AI models shall be continuously monitored through the Meridian Clinical AI Observability Platform (built on Datadog, with clinical-specific dashboards). Automated monitoring shall include:

**Performance Metrics (calculated on a 24-hour rolling window, updated hourly):**
- Model inference volume
- Model output distribution statistics (mean, standard deviation, histogram by decile)
- Override rate (per model, per customer organization, per clinician)
- Override reason distribution
- Safety flag rate
- Inference latency (P50, P95, P99)

**Drift Detection (calculated on a 7-day rolling window, updated daily):**
- Data drift score (Population Stability Index comparing current 7-day input feature distributions to deployment baseline)
- Concept drift proxy (change in override rate and override reason distribution versus baseline)
- Output drift score (Population Stability Index of model output distribution versus baseline)

**Clinical Quality Indicators (calculated monthly, updated on the 5th business day):**
- Concordance rate between model recommendation and final clinician disposition
- Time-to-clinician-review for AI-triaged asynchronous cases (by recommended acuity level)
- Patient safety events reported through customer incident management systems that reference AI model involvement

#### 5.5.2 Performance Threshold Breach Response

| Breach Type | Threshold | Response |
|-------------|-----------|----------|
| Data Drift – Warning | PSI ≥ 0.15 | Automated notification to MLOps Lead and Clinical Validation Lead; investigation initiated within 2 business days |
| Data Drift – Critical | PSI ≥ 0.25 | Automated notification to VP Clinical AI Products; model placed on watch status; manual review of 100 random recent inferences within 5 business days |
| Override Rate Increase – Warning | ≥ 50% relative increase vs. 30-day baseline | Clinical Validation Lead reviews override reasons; report to CMO within 5 business days |
| Override Rate Increase – Critical | ≥ 100% relative increase vs. 30-day baseline, OR absolute override rate > 40% | Model placed on watch status; VP Clinical AI Products notified within 24 hours; CMO notified within 48 hours; decision on continued operation within 5 business days |
| Critical Alert Miss Rate | Any single Critical alert not acknowledged within SLA + 50% | Root cause analysis initiated within 1 business day; report to CMO and Customer Operations |
| Safety Flag | Any safety flag | Immediate notification to Clinical Validation Lead and CMO; manual review of inference chain within 2 business hours; model suspension if confirmed model contribution to unsafe output |

#### 5.5.3 Scheduled Performance Reviews

In addition to automated monitoring, scheduled reviews shall be conducted:

**Weekly:** Clinical AI Operations huddle (30 minutes, standing meeting)
- Review of all safety flags and override anomalies from prior week
- Review of any threshold breaches
- Review of any customer-reported issues

**Monthly:** Telehealth AI Operations Review
- Chair: VP of Clinical AI Products
- Attendees: CMO (or designee), Clinical Validation Lead, MLOps Lead, Customer Operations representative, Compliance representative
- Agenda:
    - Performance trends for all deployed telehealth AI models
    - Override rate trends and analysis
    - Customer satisfaction and feedback
    - Drift status and remediation plans
    - Upcoming model updates or decommissions
    - Regulatory update review

**Quarterly:** AI Ethics Board Telehealth Review
- Fairness and bias audit results for all telehealth AI models
- Subgroup performance analysis
- Patient experience and transparency compliance review
- Recommendations for model remediation or decommissioning

### 5.6 Model Update and Retraining Procedures

#### 5.6.1 Retraining Triggers

Model retraining may be initiated based on:
- **Scheduled Retraining:** Defined in the model's maintenance plan (typically quarterly for active telehealth models)
- **Performance-Triggered Retraining:** Initiated when monitoring detects:
    - Drift thresholds exceeded for ≥ 14 consecutive days (Warning) or ≥ 7 consecutive days (Critical)
    - Override rate sustained elevation above baseline for ≥ 30 days
    - Quarterly subgroup fairness audit revealing performance disparity requiring remediation
- **Event-Triggered Retraining:** Initiated in response to:
    - Clinical safety incident root cause indicating model deficiency
    - Major change in clinical guidelines or standard of care for the model's target condition
    - Major change in telehealth delivery patterns or patient population characteristics

#### 5.6.2 Retrained Model Validation

Retrained models shall follow a compressed but no less rigorous version of the initial validation procedure:
- Retrospective validation on a holdout dataset (minimum size: 50% of the initial validation dataset requirement for Tier 1 and 2; 25% for Tier 3; 10% for Tier 4)
- Silent Mode observation period: 50% of initial duration, subject to minimum 14 days for Tier 1, 7 days for Tier 2
- Phased rollout: Phases 1 and 2 durations reduced by 50%, but Phase 1 scope remains at 5% of target volume

If the retrained model represents a major architectural change rather than a re-training on updated data, the full initial validation procedure applies.

#### 5.6.3 Model Rollback

If a retrained model exhibits unexpected performance degradation or safety concerns during phased rollout, the deployment shall be rolled back to the previously-approved model version. Rollback shall:
- Be initiated within 15 minutes of rollback decision by the VP Clinical AI Products or CMO
- Complete (all inference traffic routed to prior model version) within 60 minutes of initiation
- Trigger automated notification to all affected customer organizations via the Customer Operations communication protocol

### 5.7 Decommissioning Procedures

When a telehealth AI model is to be permanently decommissioned, the following procedure shall be followed:

**Step 1 – Decommissioning Decision:** Formal decision documented by VP Clinical AI Products with CMO concurrence, including rationale for decommissioning.

**Step 2 – Customer Communication Plan:** Customer Operations shall develop and execute a communication plan including:
- Minimum 30 days advance notice to affected customer organizations, except in safety-mandated immediate decommissioning scenarios
- Documentation of alternative workflows (AI-augmented or standard-of-care) available to clinicians post-decommissioning
- Support resources for clinicians who have integrated the model into their workflow

**Step 3 – Technical Decommissioning:**
- Model endpoints disabled in production environment
- All model-specific monitoring alerts retired
- Model artifacts (weights, configuration, training pipelines) archived to cold storage with minimum 7-year retention period
- Audit logs preserved with minimum 7-year retention period
- All model outputs previously committed to patient records remain unchanged

**Step 4 – Regulatory and Compliance Actions:**
- Any required regulatory notifications completed
- Model status updated in Meridian Clinical AI Model Registry
- Decommissioning recorded in the AI Ethics Board quarterly review

---

## 6. Controls and Safeguards

### 6.1 Data Transmission Security

All data transmitted between telehealth platform components and Meridian Clinical AI Platform systems shall be protected through:

**Encryption in Transit:**
- All API communications shall use TLS 1.3 (minimum TLS 1.2 with approved cipher suites, transitioning to mandatory TLS 1.3 by Q2 2026)
- FHIR API endpoints shall enforce mTLS (mutual TLS) for service-to-service authentication
- Real-time video and audio streams processed for AI inference shall be encrypted using SRTP with AES-256-GCM

**Network Segmentation:**
- Telehealth AI processing components shall be deployed within dedicated Virtual Private Cloud (VPC) subnets isolated from general Meridian SaaS Platform workloads
- Network access control lists shall restrict ingress and egress to explicitly enumerated services and ports
- All cross-VPC traffic shall transit through approved transit gateways with flow logging enabled

**API Security:**
- All Clinical AI Platform APIs shall require OAuth 2.0 with JWT bearer tokens
- Tokens shall have maximum 15-minute validity period
- API rate limiting shall be enforced at the per-tenant, per-endpoint level
- All API requests shall be logged with request ID, timestamp, source IP, authenticated principal, and endpoint

### 6.2 PHI Handling Controls

All ePHI processed within telehealth AI workflows shall be subject to the following controls:

**Access Control:**
- Access to ePHI within AI processing pipelines shall be governed by role-based access controls (RBAC) integrated with Meridian's centralized identity provider (Okta)
- Service accounts with ePHI access shall be individually named, audited, and rotated on a minimum 90-day cycle
- All human access to ePHI within AI processing logs shall require documented justification and approval by the Privacy Officer or designee

**Data Handling:**
- ePHI shall never be persisted in plaintext in any log file, monitoring system, or debugging output
- AI model training data containing ePHI shall be stored in encrypted S3 buckets with KMS-managed encryption keys, with access restricted to the MLOps service account and explicitly authorized personnel
- Temporary processing storage (e.g., inference queue messages, streaming buffers) containing ePHI shall be encrypted and configured with maximum retention periods: 24 hours for streaming buffers, 7 days for inference logs containing ePHI

**Transmission:**
- Bulk ePHI transfer for model training or validation shall use AWS Snowball Edge or equivalent encrypted transfer appliance for datasets exceeding 500GB; direct network transfer shall use dedicated VPN tunnels with AES-256 encryption
- Real-time ePHI transmissions (during telehealth encounters) shall be encrypted at the application layer using Meridian's approved encryption libraries in addition to transport-layer encryption

**Workforce Training:**
- All Meridian personnel with access to systems processing ePHI in telehealth AI contexts shall complete annual HIPAA and Security Awareness training through the Meridian Learning Management System (LMS)
- Personnel shall receive general role-based awareness of telehealth-specific privacy considerations during initial onboarding
- Completion of training shall be tracked in the LMS, with non-compliance reported to managers on a quarterly basis

### 6.3 Audit Logging and Forensic Readiness

All telehealth AI systems shall maintain comprehensive audit logging:

**Audit Log Events (mandatory for all Tier 1, Tier 2, and Tier 3 models):**
- Model inference request (timestamp, requesting system, patient identifier hash, model ID, model version)
- Model inference response (timestamp, output including confidence score, model ID, model version)
- Clinician override event (timestamp, clinician identifier, model recommendation, clinician determination, override reason)
- Clinician acknowledgment of AI-generated alert (timestamp, clinician identifier, alert ID)
- Data access (timestamp, authenticated principal, data accessed, purpose)
- Configuration change (timestamp, principal, changed parameter, previous value, new value)
- Model deployment or rollback event (timestamp, principal, model ID, version, action)
- Access permission change (timestamp, principal, affected resource, previous permission, new permission)

**Log Management:**
- All audit logs shall be shipped to Meridian's centralized SIEM (Splunk Cloud) within 60 seconds of event generation
- Logs shall be retained for a minimum of 6 years online (searchable) and an additional 4 years in cold storage
- Log integrity shall be protected through append-only logging and cryptographic hash chaining
- Access to audit logs shall be restricted to Security Operations, Compliance, and Privacy personnel; any access shall itself be logged

### 6.4 Fairness and Bias Controls

All telehealth AI models shall be subject to fairness and bias controls throughout their lifecycle:

**Pre-Deployment:**
- Bias assessment as part of pre-deployment review
- Performance stratified by race, ethnicity, preferred language, sex, age group, and primary payer type where data availability permits
- Documentation of any identified performance disparities and mitigation strategies

**Post-Deployment Monitoring:**
- Quarterly subgroup performance analysis (automated within the Clinical AI Observability Platform)
- Annual fairness audit presented to the AI Ethics Board
- Any sustained performance disparity (≥ 2 consecutive quarterly reviews) shall trigger a mandatory model remediation plan

### 6.5 Business Continuity and Disaster Recovery

Telehealth AI services shall be designed for high availability:

**Availability Targets (Monthly Uptime):**
| Model Risk Tier | Availability Target | Maximum Acceptable Single Outage Duration |
|-----------------|---------------------|-------------------------------------------|
| Tier 1 | 99.99% | 5 minutes |
| Tier 2 | 99.95% | 15 minutes |
| Tier 3 | 99.9% | 60 minutes |
| Tier 4 | 99.5% | 4 hours |

**Recovery Objectives:**
- Recovery Time Objective (RTO): 15 minutes for Tier 1 and Tier 2 models (via multi-AZ active-active deployment)
- Recovery Point Objective (RPO): 0 data loss for inference transactions (via synchronous replication)

**Disaster Recovery Testing:**
- Quarterly DR failover testing for Tier 1 models
- Semi-annual DR failover testing for Tier 2 models
- All DR test results documented and reviewed by CISO

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The following KPIs shall be tracked and reported for all telehealth AI deployments:

| KPI | Definition | Target | Reporting Frequency |
|-----|------------|--------|---------------------|
| Clinical Safety Incident Rate | Number of confirmed AI-contributory safety incidents per 100,000 telehealth encounters | < 0.01 | Monthly |
| AI Triage Concordance | Percentage of AI triage recommendations where clinician disposition matches within ±1 acuity level | ≥ 85% | Monthly |
| Override Rate | Percentage of AI recommendations overridden by clinicians | < 25% (target; > 40% triggers investigation) | Weekly |
| Inference Latency – P95 | 95th percentile inference latency for synchronous telehealth models | < 1500ms | Weekly |
| Alert Acknowledgment Timeliness | Percentage of Critical alerts acknowledged within SLA | ≥ 99.5% | Monthly |
| Silent Mode Duration | Average calendar days from model candidate approval to Silent Mode exit for Tier 1 models | — | Quarterly |
| Model Drift Remediation Time | Days from drift alert to deployment of remediated model | < 90 days | Quarterly |
| Customer-Reported Issues | Number of telehealth AI-related issues reported by customers per quarter | — | Quarterly |

### 7.2 Dashboards

**Clinical AI Telehealth Operations Dashboard** (Datadog, accessible to MLOps, Clinical Validation, and leadership):
- Real-time inference volume and latency by model
- Override rates by model and customer organization
- Drift scores and trends
- Active alerts and acknowledgment status

**Clinical Quality Dashboard** (Tableau, accessible to CMO, Clinical Validation, and Customer Operations):
- Monthly clinical safety incident tracking
- Triage concordance by acuity level
- Patient outcome metrics (where data available through customer data-sharing agreements)
- Subgroup performance parity metrics

**Executive Telehealth AI Dashboard** (Tableau, accessible to VP Clinical AI Products and executive leadership):
- Portfolio-level performance summary
- Active models, risk tiers, deployment status
- Customer satisfaction metrics (NPS proxy through issue tracking)
- Regulatory and compliance status

### 7.3 Reporting Cadence

| Report | Audience | Frequency | Owner |
|--------|----------|-----------|-------|
| Telehealth AI Operations Report | VP Clinical AI Products, CMO, CISO | Monthly | MLOps Lead |
| Clinical Safety Report | CMO, AI Ethics Board | Monthly | Clinical Validation Lead |
| Fairness and Bias Audit | AI Ethics Board | Quarterly | Clinical Validation Lead |
| Executive AI Portfolio Review | CEO, CTO, CMO, CISO, CPO | Quarterly | VP Clinical AI Products |
| Customer Performance Report | Customer organizations (de-identified, aggregated) | Quarterly | Customer Operations |
| Annual Telehealth AI Effectiveness Review | Board of Directors (via CMO) | Annual | CMO |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types

Exceptions to this SOP may arise in the following categories:

**Model Deployment Exceptions:**
- Deployment with abbreviated Silent Mode duration
- Deployment with reduced retrospective validation dataset
- Phased rollout acceleration
- Go-live checklist item deferral

**Operational Exceptions:**
- Temporary override of monitoring alert thresholds
- Extended monitoring review period deferral
- Deviation from scheduled retraining cadence

**Control Exceptions:**
- Temporary relaxation of access controls for emergency maintenance
- Deviation from encryption standards for backward compatibility
- Use of non-standard data transmission paths

### 8.2 Exception Approval Authority

| Exception Severity | Approval Authority | Maximum Duration | Documentation Requirement |
|--------------------|-------------------|------------------|---------------------------|
| Minor (no material impact on patient safety, data security, or regulatory compliance) | Clinical Validation Lead | 30 days, renewable once | Exception recorded in Clinical AI Model Registry |
| Moderate (potential indirect impact on patient safety or modest deviation from standard) | VP Clinical AI Products + CMO | 90 days, renewable with AI Ethics Board review | Exception recorded; risk assessment documented; compensating controls identified |
| Major (potential direct patient safety impact, significant regulatory deviation, or PHI exposure risk) | CMO + CISO + VP Clinical AI Products + Chief Compliance Officer | 7 days, non-renewable | Formal risk assessment; compensating controls; regulatory analysis; AI Ethics Board notification |

### 8.3 Escalation Paths

**Clinical Safety Concerns:**
1. Identifying individual → Clinical Validation Lead (immediate, within 1 hour)
2. Clinical Validation Lead → CMO (within 2 hours)
3. CMO → AI Governance Committee (within 24 hours)
4. AI Governance Committee → Board of Directors (at next scheduled meeting, or emergency meeting if warranted)

**Data Security or Privacy Incidents:**
1. Identifying individual → Security Operations Center (immediate, via PagerDuty)
2. Security Operations Center → CISO and CPO (within 1 hour for confirmed incidents involving ePHI)
3. CISO → Executive Leadership Team (within 24 hours for confirmed breaches)

**Model Performance Degradation:**
1. Automated alert → MLOps Lead (immediate)
2. MLOps Lead → Clinical Validation Lead (within 4 business hours if Critical threshold breach)
3. Clinical Validation Lead → VP Clinical AI Products (within 24 hours if model watch status declared)
4. VP Clinical AI Products → CMO (immediate if model suspension considered)

### 8.4 Exception Register

All exceptions shall be recorded in the Meridian Clinical AI Model Registry Exception Register with:
- Exception ID
- Requesting party
- Approval authority
- Date approved
- Expiration date
- Exception category and description
- Compensating controls (if required)
- Risk assessment reference

Open exceptions shall be reviewed at each monthly Telehealth AI Operations Review.

---

## 9. Training Requirements

### 9.1 Required Training

All personnel whose roles fall within the scope of this SOP shall complete the following training:

| Training Module | Target Audience | Frequency | Delivery Method |
|-----------------|-----------------|-----------|-----------------|
| Telehealth AI Integration – Operational Procedures | All personnel in RACI matrix roles | Annually | Meridian LMS (self-paced e-learning; 90 minutes estimated duration) |
| HIPAA and ePHI Handling | All personnel with ePHI access | Annually | Meridian LMS with knowledge assessment (minimum 80% score required for completion) |
| Clinical AI Safety Awareness | Clinical AI engineers, Clinical Validation team, MLOps team | Annually | Meridian LMS (self-paced e-learning with case studies; 60 minutes estimated duration) |
| Bias and Fairness in Clinical AI | Clinical AI engineers, Clinical Validation team | Annually | Live workshop facilitated by AI Ethics Board representative (half-day) |
| New Model Onboarding – Telehealth Context | Clinical AI engineers (onboarding) | Once, within first 30 days of employment | Guided walkthrough with Clinical Validation Lead |

### 9.2 Training Compliance Tracking

- All training completions shall be logged in the Meridian LMS
- Training compliance reports shall be generated quarterly by the Learning & Development team and distributed to functional managers
- Personnel with overdue required training shall have their access to telehealth AI production systems suspended until training is completed
- Annual training compliance rate target: ≥ 98% completion by annual deadline

### 9.3 Role-Specific Continuing Education

Beyond formal training modules, the following ongoing education activities are expected:

- Clinical Validation team members shall review at least one relevant peer-reviewed publication per quarter addressing AI in telehealth
- MLOps engineers shall maintain current AWS or equivalent cloud certification
- All Clinical AI engineers shall complete at least one internal technical seminar annually on telehealth-specific topics

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|--------|-------|-------------|
| SOP-CLIN-015 | Clinical AI Model Lifecycle Management | Parent policy for general AI model lifecycle; this SOP adds telehealth-specific procedures |
| SOP-CLIN-022 | Clinical AI Safety Incident Management | Defines safety incident classification, investigation, and reporting procedures referenced in Section 5.5 |
| SOP-IS-120 | Information Security Incident Response | Defines breach response procedures referenced in Section 4.6 |
| SOP-PRV-035 | PHI Minimum Necessary Standard | Defines PHI data minimization standards referenced in Section 4.3 |
| SOP-IT-080 | Observability and Monitoring Standards | Defines general infrastructure monitoring standards; this SOP defines clinical-layer monitoring |
| SOP-MLOPS-055 | MLOps CI/CD Pipeline Governance | Defines model deployment pipeline standards |
| SOP-QMS-001 | Quality Management System Overview | Establishes the general quality management framework |
| SOP-FIN-045 | HealthPay Model Risk Management | Governs financial models; cross-referenced where telehealth AI outputs influence billing |

### 10.2 External Standards and References

| Reference | Description |
|-----------|-------------|
| NIST AI RMF 1.0 | NIST Artificial Intelligence Risk Management Framework; Meridian's AI governance aligns with NIST AI RMF categories (Govern, Map, Measure, Manage) |
| NIST SP 800-53 Rev 5 | Security and Privacy Controls for Information Systems and Organizations |
| ISO 13485:2016 | Medical devices – Quality management systems |
| IEC 62304:2006 | Medical device software – Software life cycle processes |
| FDA Guidance: Clinical Decision Support Software | FDA final guidance on CDS software, September 2022 |
| FDA Guidance: Artificial Intelligence/Machine Learning-Based Software as a Medical Device (SaMD) Action Plan | January 2021 |
| HL7 FHIR R4 | Health Level Seven International Fast Healthcare Interoperability Resources Release 4 |
| ATA Clinical Guidelines for Telehealth | American Telemedicine Association practice guidelines |
| EU MDR 2017/745 | European Medical Device Regulation; applicable to CE-marked Clinical AI Platform components |
| HITRUST CSF v11 | Health Information Trust Alliance Common Security Framework; Meridian's current certification basis |

### 10.3 Meridian Internal References

| Resource | Location |
|----------|----------|
| Clinical AI Model Registry | ServiceNow CMDB – Clinical AI CI Class |
| Clinical AI Observability Platform | Datadog – Clinical AI Telehealth Dashboard Suite |
| Telehealth AI Incident Tracker | Jira Service Management – Clinical AI Telehealth Project |
| AI Ethics Board Meeting Minutes | SharePoint – AI Ethics Board Document Library |
| Telehealth Customer Contracts Repository | Salesforce – Customer Agreements |
| Model Training Data Catalog | AWS Glue Data Catalog – meridian-clinical-ai-telehealth |

---

## 11. Revision History

| Version | Date | Author | Changes | Approver |
|---------|------|--------|---------|----------|
| 1.0 | 2022-06-15 | Dr. Sarah Chen (Initial Clinical AI Lead) | Initial publication; established baseline telehealth AI integration procedures during rapid telehealth expansion period | Dr. James Morrison (CMO, former) |
| 2.1 | 2023-01-20 | Dr. Aisha Okafor | Addition of Silent Mode observation requirements; expanded RPM integration procedures; addition of phased rollout framework | Dr. Priya Patel |
| 3.0 | 2023-08-03 | Dr. Aisha Okafor | Major revision: introduction of risk tier classification system; addition of fairness and bias monitoring; expanded audit logging requirements; alignment with EU AI Act preliminary requirements | Dr. Priya Patel |
| 4.2 | 2024-02-14 | Dr. Aisha Okafor | Addition of asynchronous triage workflow procedures; override reason structured taxonomy; expanded monitoring thresholds; integration with Clinical AI Model Registry | Dr. Priya Patel |
| 5.1 | 2024-11-05 | Dr. Aisha Okafor | Major revision: full EU AI Act operationalization; expanded data transmission security controls; updated SLA thresholds based on 18 months of operational data; addition of decommissioning procedures | Dr. Priya Patel |
| 5.7 | 2025-06-18 | Dr. Aisha Okafor, with Clinical Validation team | Updated retrospective validation volume requirements; refined drift detection thresholds; expanded exception handling authority table; quarterly review cycle adjustments | Dr. Priya Patel |
| 5.9 | 2025-10-28 | Dr. Aisha Okafor | Current version: Updated telehealth AI risk classification matrix; refined RPM alert acknowledgment SLAs; updated training requirements section; expanded business continuity RTO/RPO targets; added mTLS requirement for FHIR endpoints | Dr. Priya Patel |

---

**Document Control Note:** This SOP is effective as of the date specified in the document metadata. Printed copies are uncontrolled. The authoritative version is maintained in the Meridian Document Management System (SharePoint – Clinical AI Policy Library). Any deviations from this SOP must be documented through the exception process defined in Section 8. Questions regarding interpretation of this SOP shall be directed to the SOP Owner.

**END OF DOCUMENT**
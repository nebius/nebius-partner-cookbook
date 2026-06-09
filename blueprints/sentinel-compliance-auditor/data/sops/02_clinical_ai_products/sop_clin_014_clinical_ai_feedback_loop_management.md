---
sop_id: "SOP-CLIN-014"
title: "Clinical AI Feedback Loop Management"
business_unit: "Clinical AI Products"
version: "2.3"
effective_date: "2024-09-04"
last_reviewed: "2025-12-24"
next_review: "2026-06-02"
owner: "Dr. Aisha Okafor, VP of Clinical AI Products"
approver: "Dr. Priya Patel, Chief Medical Officer"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: Clinical AI Feedback Loop Management

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the formalized, end-to-end process for managing the Clinical AI Feedback Loop within Meridian Health Technologies, Inc. The purpose is to ensure the systematic collection, analysis, prioritization, and integration of clinician feedback to continuously improve the safety, performance, fairness, and clinical utility of all deployed Clinical AI Platform products. This process is a cornerstone of our Quality Management System (QMS) and is mandatory for maintaining regulatory compliance, specifically with the European Union Artificial Intelligence Act (EU AI Act) and the National Institute of Standards and Technology AI Risk Management Framework (NIST AI RMF).

### 1.2 Scope

This SOP applies to all personnel, processes, and technologies involved in the lifecycle of Meridian’s Clinical AI Platform products, from initial deployment through decommissioning.

**In-Scope:**
- All AI/ML models within the Clinical AI Platform, including but not limited to: clinical decision support tools, diagnostic imaging analysis algorithms, patient risk scoring models, and adverse event prediction systems.
- All products classified as high-risk AI systems under Annex III of the EU AI Act.
- All products holding FDA 510(k) clearance or CE marking under EU MDR.
- All environments where Clinical AI models are deployed (production, shadow, and User Acceptance Testing (UAT) environments).
- All feedback mechanisms, including the in-app "Feedback" button, the Meridian Clinician Portal, direct emails to `clinical-feedback@meridian.ai`, support tickets routed through Zendesk tagged `AI_Feedback`, and structured feedback collected during scheduled Clinical Review Board meetings.
- All personnel interacting with or managing the feedback loop, including clinicians, data scientists, product managers, regulatory affairs specialists, and quality assurance engineers.

**Out-of-Scope:**
- Feedback related to non-AI software features (e.g., UI bugs not affecting model output). These are governed by the Engineering Defect Management SOP (SOP-ENG-005).
- Customer satisfaction surveys not containing specific model performance feedback. These are governed by the Customer Experience SOP (SOP-CX-102).
- Feedback on the HealthPay Financial Services or MedInsight Analytics platforms, which have separate model governance procedures (SOP-FIN-022 and SOP-ANL-045, respectively).

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **Adverse Event** | Any incident that results in, or has the potential to result in, patient harm due to the output or failure of a Clinical AI model. Governed by SOP-REG-001 (Adverse Event Reporting). |
| **Bias Drift** | A statistically significant change in a pre-defined fairness metric (e.g., disparate impact ratio, equal opportunity difference) over time, as measured by continuous monitoring systems. |
| **Clinical Review Board (CRB)** | A cross-functional governance body responsible for the clinical safety and efficacy of all deployed AI models. Chaired by the Chief Medical Officer. |
| **Clinician User** | A licensed healthcare professional (MD, DO, NP, PA, RN) authorized to use Meridian’s Clinical AI Platform in a clinical decision-making context. |
| **Concept Drift** | A change in the statistical properties of the target variable, which the model is trying to predict, over time. |
| **Data Drift** | A change in the statistical properties of the input data over time. |
| **Feedback Artifact** | A discrete, structured unit of feedback, comprising the clinician's original submission and all associated metadata and evidence (e.g., screenshots, patient de-identified data snippets). |
| **Feedback Loop** | The closed-loop process of capturing, triaging, investigating, resolving, and deploying improvements based on clinician feedback. |
| **Ground Truth** | A verified, definitive diagnosis or clinical outcome, typically confirmed by a consensus panel of expert clinicians or through gold-standard diagnostic procedures (e.g., biopsy, follow-up imaging), used to adjudicate a feedback case. |
| **High-Risk AI System** | An AI system classified under Annex III of the EU AI Act, which poses a significant risk of harm to the health, safety, or fundamental rights of natural persons. |
| **Human-in-the-Loop (HITL)** | A design and operational principle ensuring that a qualified human (Clinician User) has the authority and capability to overrule an AI system's output, as mandated by EU AI Act Article 14. |
| **Model Retraining** | The technical process of updating an AI model's parameters by training on a new or augmented dataset to improve its performance or correct identified deficiencies. |
| **Performance Drift** | A statistically significant degradation in a model’s primary performance metric (e.g., sensitivity, specificity, AUC-ROC) below a pre-defined threshold. |
| **Post-Market Clinical Follow-up (PMCF)** | A continuous process of collecting and evaluating clinical data from the use of a CE-marked medical device to proactively update its clinical evaluation, as required by EU MDR. |
| **Quality Management System (QMS)** | The organizational structure, responsibilities, processes, and resources for implementing quality management, as defined in SOP-QUAL-001. |
| **Safety Signal** | A new or previously incompletely characterized potential risk associated with a model, identified through feedback analysis or monitoring, which requires urgent investigation. |

---

## 3. Roles and Responsibilities

The following RACI matrix defines the accountability and responsibility for key tasks within this SOP. (R = Responsible, A = Accountable, C = Consulted, I = Informed).

| Task / Activity | Clinician User | Model Product Manager | AI/ML Engineer | Clinical Safety Lead | CRB Chair (CMO) | Regulatory Affairs |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Submit Initial Feedback** | R, A | I | - | I | - | - |
| **Triage Feedback (Severity)** | - | R | C | A | I | - |
| **Conduct Clinical Investigation** | C | I | C | R, A | I | - |
| **Identify Ground Truth** | C | I | - | R, A | I | - |
| **Perform Technical Analysis (Root Cause)** | - | I | R, A | C | - | - |
| **Determine Need for Model Update** | - | R | C | A | C | C |
| **Approve Emergency Model Rollback** | - | I | C | C | A | I |
| **Execute Model Retraining/Update** | - | C | R, A | C | - | - |
| **Validate Updated Model** | C | I | R | A | I | C |
| **Deploy Updated Model** | I | R | C | C | I | I |
| **Close Feedback Loop with User** | I | R, A | - | C | - | - |
| **Authorize Exception to SOP** | - | - | - | - | A | I |

### 3.1 Detailed Role Descriptions

- **Clinician User:** The frontline user who identifies a potential issue—a missed finding, a false alarm, an inaccurate risk score, or a confusing output. Responsible for submitting feedback through an approved channel with sufficient context to initiate an investigation.
- **Model Product Manager:** Owns the product backlog and the end-to-end feedback lifecycle. Responsible for triaging feedback, ensuring timely progression through stages, and communicating resolutions back to the submitter. Accountable for the feedback loop’s adherence to SLA timelines.
- **AI/ML Engineer:** Responsible for the deep technical investigation of feedback. This includes reproducing the issue, analyzing model behavior with tools like LangSmith, performing data and concept drift analysis, and executing model retraining or fine-tuning. Accountable for the technical integrity of the solution.
- **Clinical Safety Lead:** A board-certified physician on the Clinical AI Products team. Responsible for the clinical assessment of feedback, determining the potential for patient harm (severity), overseeing the ground truth adjudication process, and acting as the primary clinical consultant to the AI/ML Engineers. This role is mandatory for all high-risk AI systems as per EU AI Act Article 14.
- **CRB Chair (Chief Medical Officer):** Provides final executive accountability for clinical safety. Has sole authority to approve emergency rollbacks of a model. Chairs the weekly CRB meeting where high-severity feedback and safety signals are reviewed.
- **Regulatory Affairs:** Provides consultation on whether the nature or quantity of feedback constitutes a reportable event (e.g., to an Ethics Committee or Notified Body) or triggers a new conformity assessment under the EU AI Act.

---

## 4. Policy Statements

1.  **Continuous Improvement Commitment:** Meridian Health Technologies is committed to a culture of continuous learning and post-market surveillance. Every piece of clinician feedback on a high-risk AI system is a valuable data point for improving patient safety and product quality.
2.  **Mandatory Response:** Every feedback artifact submitted through an approved channel will be acknowledged, triaged, and investigated. No feedback shall be ignored or discarded without a formal triage decision documented in the Feedback Management System (FMS).
3.  **Human-in-the-Loop Primacy:** This feedback loop is a direct operationalization of the HITL principle. It formalizes the process by which human expertise identifies and corrects AI system failures, reinforcing that the clinical user's judgment is paramount, consistent with EU AI Act Article 14.
4.  **Non-Retaliation:** Meridian enforces a strict non-retaliation policy for clinicians who submit feedback in good faith. Feedback is encouraged as a patient safety activity and is protected as a quality improvement process.
5.  **Transparency:** In accordance with EU AI Act Article 13 (Transparency and provision of information), we are committed to providing clear explanations of AI outputs to clinicians. When feedback identifies a failure of transparency, the investigation will include an assessment of the model's explainability and user interface clarity.
6.  **Risk-Based Prioritization:** All feedback will be prioritized based on a standardized clinical severity matrix, ensuring that potential safety risks are addressed with the utmost urgency.
7.  **Data Integrity and Privacy:** All feedback analysis must be conducted on de-identified data in secure, access-controlled environments. Any handling of PHI must strictly adhere to HIPAA Security and Privacy Rules and GDPR.

---

## 5. Detailed Procedures

This section outlines the step-by-step lifecycle of a Feedback Artifact, from submission to closure. The entire process is managed and audited within the Meridian Feedback Management System (FMS), a validated module built on Jira Service Management.

### 5.1 Stage 0: Feedback Submission

The feedback loop is initiated by a Clinician User.

**Procedure Steps:**
1.  **Identify an Issue:** The Clinician User identifies a potential deviation between the AI system's output and their clinical assessment.
2.  **Access Submission Channel:** The user selects one of the following approved channels:
    - **In-App Feedback Widget (Preferred):** Located persistently in the top-right corner of the Clinical AI Platform interface. This automatically captures session context (e.g., patient de-identified ID, study UID, model version, timestamp) and attaches it to the ticket.
    - **Meridian Clinician Portal:** A secure web portal where users can log in, view their feedback history, and submit new, detailed reports with file attachments.
    - **Email:** An email to `clinical-feedback@meridian.ai`. This creates a ticket via an API, but with less automatic context. Automated reply prompts the user to use the in-app widget for future reports.
3.  **Complete Form Fields:** The user is required to populate the following fields:
    - **Category:** (Dropdown) `Missed Finding`, `False Alarm`, `Inaccurate Quantification`, `Segmentation Failure`, `Risk Score Inconsistency`, `Confusing UI/UX`, `Data Display Error`, `Slow Performance`, `Other`.
    - **Clinical Context:** (Free text) A brief narrative of the clinical scenario and why the output is flagged. *Mandatory*.
    - **Priority:** (User-perceived) `Low`, `Medium`, `High`, `Critical`. This is informational and does not dictate the official triage severity.
    - **Attachments:** (Optional but highly encouraged) De-identified screenshots of the AI output.
4.  **Acknowledge Terms:** The user must acknowledge the statement: *"This submission is part of a secure quality improvement process. Do not include any Protected Health Information (PHI). If PHI is inadvertently submitted, the feedback will be immediately purged."*
5.  **Submit:** Upon submission, the system generates a unique Feedback ID (format: `FDBK-YYYY-NNNNN`) and immediately sends an automated acknowledgment email to the user, including the Feedback ID and a link to track its status.

### 5.2 Stage 1: Triage and Acknowledgment

**SLA:** All feedback must be triaged within 4 business hours of submission. Critical severity must be escalated within 30 minutes.

**Responsible:** Model Product Manager (Primary), Clinical Safety Lead (Consulted).

**Procedure Steps:**
1.  **Queue Review:** The Model Product Manager reviews the "Un-triaged Feedback" queue in the FMS.
2.  **Context Enrichment:** The Product Manager uses the Feedback ID to query the `Clinical_AI_Feedback_Log` in Snowflake, automatically joining the submission with system logs (from Datadog) and the specific model's inference payload (from a secure, encrypted S3 bucket).
3.  **Severity Assignment:** The Product Manager assigns an official severity level based on the following matrix, in consultation with the Clinical Safety Lead if initially assessed as High or Critical:

    | Severity | Definition | Examples |
    | :--- | :--- | :--- |
    | **S1 - Critical** | A confirmed or highly probable risk of imminent, serious patient harm or death due to a gross model failure or data corruption affecting many studies. | Model consistently misclassifies a type of intracranial hemorrhage, or a systemic data pipeline failure feeds corrupted images. |
    | **S2 - High** | A confirmed model error that has a high potential for significant patient mismanagement (e.g., unnecessary invasive procedure, missed high-risk diagnosis). | Model fails to detect a large pulmonary nodule; inaccurate risk score leads to an incorrect triage pathway. |
    | **S3 - Medium** | A confirmed model error or performance issue with low potential for patient harm, or a potential error that requires further investigation. | A minor segmentation inaccuracy on a non-critical anatomical structure; a confusing but clinically overridable output. |
    | **S4 - Low** | A non-clinical issue, a minor UI bug not affecting the model's core output, or a feature enhancement request. | A typo in a text report; a request for a new preference setting. |

4.  **Assign Team:** Based on the model and category, the ticket is assigned to the appropriate Model Team (e.g., `Team Neuro-AI`, `Team Chest-AI`). The ticket is automatically added to the team's `Feedback Queue` in Jira.
5.  **Update Submitter:** The Product Manager updates the FMS ticket status to "Triage Complete - Under Investigation," which triggers an automated notification to the original submitter with the assigned severity and a point of contact.

### 5.3 Stage 2: Clinical and Technical Investigation

This stage runs in two parallel tracks: a Clinical Investigation and a Technical Investigation.

#### 5.3.1 Clinical Investigation
**SLA:** Preliminary clinical report completed within 1 business day for S1/S2, 3 business days for S3.
**Responsible:** Clinical Safety Lead.

**Procedure Steps:**
1.  **Case Retrieval:** The Clinical Safety Lead securely accesses the full de-identified clinical context, including the original study and AI outputs, via the `Clinical_Investigation_Workbench`.
2.  **Ground Truth Adjudication:** The method for establishing ground truth is determined:
    - **For known outcomes:** The Clinical Safety Lead compares the AI output against documented follow-up data (e.g., a subsequent study, biopsy results) available in the de-identified dataset.
    - **For adjudication-required:** The case is anonymized further and sent to a pre-approved panel of 3 independent expert clinicians, who are blinded to the AI output, for a consensus review. This is mandatory for all S1 events and any S2 events where ground truth is not immediately apparent.
3.  **Clinical Impact Assessment:** The Clinical Safety Lead authors a `Clinical Investigation Report` (CIR) within the FMS, summarizing:
    - Ground truth finding.
    - Classification of the AI error (e.g., False Negative, False Positive, Underestimation).
    - Assessment of potential and actual patient harm, using a standardized harm scale (No Harm, Minor Temporary Harm, Major Temporary Harm, Permanent Harm, Death).
    - A revised severity assessment if new information warrants a change.
4.  **Safety Signal Detection:** The Clinical Safety Lead assesses whether this case, alone or in aggregate, constitutes a new Safety Signal. If so, the case is immediately escalated per Section 8.2 of this SOP.

#### 5.3.2 Technical Investigation
**SLA:** Preliminary technical report completed within 2 business days for S1/S2, 5 business days for S3. Runs in parallel with clinical investigation.
**Responsible:** AI/ML Engineer.

**Procedure Steps:**
1.  **Reproduction Attempt:** The AI/ML Engineer attempts to reproduce the exact inference failure. This is done in a sandboxed `debug` environment using the original de-identified study and model version (fetched from the Model Registry in MLflow).
2.  **Log and Trace Analysis:** The engineer uses LangSmith and Datadog logs to trace the full inference pipeline for that specific transaction, looking for anomalies in data preprocessing, model execution, or post-processing.
3.  **Drift Analysis (Data & Performance):** The engineer executes a formal drift analysis script against the production monitoring database (Snowflake `Model_Monitoring` schema):
    - **Data Drift:** Checks the specific study's input features against the training distribution and the last 30-day production window using a two-sample Kolmogorov-Smirnov test. A p-value < 0.01 is flagged as significant drift.
    - **Performance Drift:** Plots the model's real-time performance metrics (e.g., AUC-ROC from confirmed outcomes) over the last 30 days to identify any degradation.
4.  **Root Cause Analysis (RCA):** The engineer documents the root cause in a `Technical Investigation Report` (TIR). Causes could include:
    - `Data Input Error`: Corrupted image, incorrect modality, poor quality scan.
    - `Model Limitation`: A known limitation of the current model architecture or training data distribution (e.g., rare pathology, edge case).
    - `Concept/Data Drift`: A genuine shift in the patient population or imaging equipment.
    - `Code Regression`: A bug introduced in a recent model wrapper or pre-processing script update.
    - `Non-reproducible`: The error cannot be reproduced in the debug environment.
5.  **Link Reports:** The TIR is linked to the CIR within the FMS. The AI/ML Engineer and Clinical Safety Lead meet to synthesize their findings into a unified `Feedback Investigation Summary`.

### 5.4 Stage 3: Resolution Determination

**Responsible:** Model Product Manager (R), Clinical Safety Lead (A), CRB (C for S1/S2).

**Procedure Steps:**
1.  **Review Investigation Summary:** The Product Manager reviews the combined clinical and technical findings.
2.  **Classify Resolution Path:** Based on the root cause, the issue is assigned one of the following resolution paths:

    | Resolution Path | Criteria |
    | :--- | :--- |
    | **Model Retraining / Fine-tuning** | Issue traceable to a model limitation or drift that can be addressed with new data. |
    | **Data Augmentation / Curation** | Issue requires sourcing and labeling a specific set of new training data. |
    | **Code Fix (Pre/Post-Processing)** | Root cause is a bug in the non-model software components. Handled under SOP-ENG-005, but tracked here. |
    | **Explainability / UI Update** | Issue is a failure of transparency; the model is correct, but its presentation is misleading. |
    | **Documentation Update** | The model behavior is correct and intended, but the known limitation is not documented. The limitation is added to the product's Instructions for Use (IFU) and Model Card. |
    | **No Action / Deferred** | The error is minor, non-reproducible, or has a negligible risk profile. This requires explicit justification and CRB Chair approval for S2/S3 cases. The feedback remains in the system for future trend analysis. |

3.  **Create Child Work Items:** For actionable paths (not "No Action"), the Product Manager creates specific, assigned tasks in Jira, linked to the parent Feedback ID.
    - A `Model-Update` issue is created if retraining is required.
    - A `Data-Curation` task is created if new data labeling is needed.
4.  **Communication:** The outcome and resolution path is communicated to the submitting clinician, explaining the clinical reasoning and planned action in non-technical language. This message is drafted by the Product Manager and reviewed by the Clinical Safety Lead.

### 5.5 Stage 4: Implementation and Verification

This stage follows the standard model development lifecycle (SOP-MLOPS-012), with heightened scrutiny for changes directly resulting from clinical feedback.

**Procedure Steps:**
1.  **Development:** AI/ML Engineers develop the fix (retrained model, updated code) in a feature branch within the `meridian-clinical-ai` repository.
2.  **Internal Validation:** The updated model or pipeline undergoes rigorous offline testing, including:
    - **Regression Testing:** Performance on the specific feedback case(s) that initiated the change. The model must now produce the clinically correct output.
    - **Backtesting:** Performance on a large, held-out validation dataset (at least 100,000 studies) to ensure no regression in overall performance.
    - **Bias and Fairness Testing:** A stratified analysis to check for disparate impact across protected attributes (age, sex, race/ethnicity), as outlined in Section 6.5 and the Bias Monitoring SOP (SOP-CLIN-015). The performance delta for any subgroup must not exceed ±5% of the baseline.
3.  **Silent Deployment & Shadow Mode:** For S1-S3 model updates, the newly packaged model is deployed in "Shadow Mode" to a production environment. It generates inferences on live data but does not display them to users. Performance is monitored for a period determined by risk (7 days for S3, 14 days for S2, 1-3 days for S1 with a 24/7 on-call monitoring engineer). During this period, the Clinical Safety Lead reviews a daily dashboard comparing shadow outputs to the production model.
4.  **Clinical Validation (HITL Sign-off):** The Clinical Safety Lead must provide a formal, documented sign-off, explicitly stating that the updated model is safe for clinical use based on the shadow mode performance data. This is in the `Model Release Form` in the QMS.
5.  **Full Deployment:** Upon Clinical Safety Lead sign-off, the Shadow Model is promoted to the production endpoint via a blue-green deployment strategy to ensure zero downtime.
6.  **Post-Deployment Monitoring:** Post-deployment, the model enters an "intensive monitoring" phase for 30 days, with weekly manual reviews of its performance metrics by the product team.

### 5.6 Stage 5: Loop Closure and Effectiveness Check

**Procedure Steps:**
1.  **Final Notification:** Once the fix is deployed, the Product Manager sends a final closure notification to the submitting clinician. This message includes:
    - A summary of the issue and root cause.
    - A description of the action taken (e.g., "Model retrained with new data," "Bug fixed").
    - An invitation to a brief (1-question) survey: "On a scale of 1-5, how satisfied are you with the resolution of this feedback?" This metric is tracked as part of the feedback loop KPI (Section 7).
2.  **Effectiveness Check Backtest:** Twenty-one (21) calendar days after deployment, the Product Manager and AI/ML Engineer review a report generated automatically by the FMS. This report re-runs the original feedback case and 100 similar cases through the updated system to confirm the fix remains effective.
3.  **Formal Closure:** After a successful effectiveness check, the Feedback ID is closed in the FMS. All associated artifacts (CIR, TIR, Model Release Form) are permanently archived in the QMS document management system for audit purposes, per the record retention policy (SOP-REC-030).

---

## 6. Controls and Safeguards

### 6.1 Access Control
Access to the FMS, `Clinical_Investigation_Workbench`, and debug environments is governed by Role-Based Access Control (RBAC).
- **Clinician Users:** Can create, view, and comment on their own feedback tickets.
- **Model Team Members:** Can view and edit tickets assigned to their team. Access to raw, de-identified data is logged in an immutable audit trail.
- **Clinical Safety Lead & CRB:** Unrestricted read access to all feedback tickets and investigation reports for governance and trend analysis.
All access logs are reviewed monthly by the Information Security team per SOP-SEC-004.

### 6.2 Data Anonymization and Privacy
A critical safeguard is the automatic de-identification of all context captured with a feedback artifact.
- The feedback capture pipeline (`photon-anonymizer`) uses a validated algorithm to strip all 18 HIPAA Safe Harbor identifiers and GDPR-specified personal data before the data payload is stored in the FMS-accessible S3 bucket.
- A quarterly validation of the anonymizer's effectiveness is performed by injecting a synthetic dataset with known identifiers and verifying 100% redaction.
- Any instance of a clinician inadvertently submitting PHI triggers the "Break Glass" PHI Breach procedure in SOP-PRIV-001. The feedback ticket is immediately quarantined by the Data Loss Prevention (DLP) system.

### 6.3 Audit Trail
The FMS maintains a complete, non-modifiable audit trail for every Feedback Artifact. Every state change, comment, report attachment, and sign-off is logged with a timestamp and the actor's unique user ID. This audit trail is essential for demonstrating compliance with EU AI Act Article 17 (Quality Management System) and Article 61 (Post-market monitoring).

### 6.4 Model Registry and Versioning
All models and their versions are immutable and registered in MLflow Model Registry. A model version is tagged with its stage (`staging`, `production`, `archived`). When a feedback-driven update is performed, the new model version's metadata in MLflow must include a direct link to the `FDBK-YYYY-NNNNN` IDs that motivated the change, ensuring end-to-end traceability from complaint to device improvement.

### 6.5 Bias and Fairness Safeguards
Every S1, S2, and S3 investigation requiring a model retrigger must include a mandatory fairness analysis step, as referenced in SOP-CLIN-015 (Bias Monitoring and Mitigation).
- **Procedure:** Before a retrained model is cleared for silent deployment, the AI/ML Engineer executes the `meridian-fairness` pipeline. This calculates pre-defined fairness metrics (e.g., Disparate Impact Ratio, Equal Opportunity Difference) segmented by age, sex, and race/ethnicity (where available and permissible under GDPR).
- **Risk Profiles:** This analysis contributes to the system's risk profile. While this process applies to all models selected for post-feedback retraining, the systematic, pre-emptive application of this fairness testing across all models in the organization's full inventory is an ongoing, maturing capability.
- **Threshold:** A metric deviation greater than the threshold defined in SOP-CLIN-015 automatically halts the release pipeline and flags the issue for CRB review.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The health of the Feedback Loop is measured through the following mandatory KPIs, which are visualized on a real-time Tableau dashboard (`Clinical AI Feedback Dashboard`).

| KPI Category | Metric Name | Target | Measurement Frequency |
| :--- | :--- | :--- | :--- |
| **Timeliness** | Mean Time to Triage (MTTT) | ≤ 2 business hours | Real-time, reported weekly |
| **Timeliness** | Mean Time to Resolution (MTTR) - S1/S2 | ≤ 5 business days | Real-time, reported weekly |
| **Timeliness** | Mean Time to Resolution (MTTR) - S3/S4 | ≤ 20 business days | Real-time, reported weekly |
| **Quality** | Feedback Closure Rate | ≥ 98% (within 90 days) | Monthly |
| **Quality** | Submitter Satisfaction Score | Mean ≥ 4.5 / 5.0 | Monthly |
| **Effectiveness** | Re-open Rate (Issue recurs post-fix) | ≤ 2% | Monthly |
| **Safety** | S1/S2 Feedback Volume | Monitored for Statistical Process Control (SPC) limits | Weekly |
| **Fairness** | Model Retrain Rate per Protected Group | Monitored for drift; no specific target | Per Retrain Cycle |

### 7.2 Reporting Cadence
- **Product Team (Daily Stand-up):** Review of new S1/S2 tickets and tickets breaching SLA. The FMS Kanban board is the primary source.
- **Clinical Review Board (Weekly):** A 30-minute standing agenda item to review the `Weekly Safety & Feedback Digest`. This report includes:
    - All new S1 and S2 feedback artifacts with their investigation status.
    - Newly identified Safety Signals.
    - A trend chart of feedback volume and severity over the last 4 and 12 weeks.
    - A list of all "No Action / Deferred" S2/S3 tickets pending approval.
- **QMS Management Review (Quarterly):** A comprehensive review of all feedback KPIs, trends, process effectiveness, and resource allocation. This is a formal review required by SOP-QUAL-001. Minutes are recorded and any decisions for CAPA (Corrective and Preventive Action) are logged.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Process
Any deviation from the standard procedures in this SOP requires a formal exception. Exceptions are documented using the `SOP Exception Request Form` in the QMS.
- **Approval Authority:**
    - **Minor Deviations** (e.g., extension of an S3 SLA by 1 day): Approval by the Model Product Manager.
    - **Major Deviations** (e.g., deploying a fix without full shadow mode for an S3 issue): Approval by the CRB Chair (CMO). This must be accompanied by a detailed risk assessment.
    - **Critical Deviations** (e.g., deploying an S1 fix without the full 1-day shadow mode period): Approval by the CRB Chair with a clearly documented risk acceptance rationale. All S1 exceptions are reported to the VP of Regulatory Affairs within 24 hours.

### 8.2 Emergency Escalation (Safety Signal)
If, during triage or investigation (Stage 1 or 2), the Clinical Safety Lead identifies a Safety Signal, the following escalation path is **activated immediately**, overriding standard SLAs:

1.  **Activate Signal:** The Clinical Safety Lead declares a "Code: Signal" in the FMS, adding the `safety-signal` tag. This triggers a PagerDuty alert to the on-call AI Director, Clinical AI VP (Dr. Okafor), and CMO (Dr. Patel).
2.  **Convene Emergency Committee:** Within 1 hour, the on-call leadership convenes an emergency meeting with the responsible Model Product Manager and Tech Lead.
3.  **Decision: Rollback vs. Shield:** The committee makes an immediate risk determination:
    - **Rollback:** If the risk is clear and imminent, the CMO authorizes an emergency rollback of the specific model or feature to the last known safe version, or to a "null" state where the AI output is simply not displayed, reverting to standard-of-care. This is executed by the AI/ML Engineering on-call team within minutes.
    - **Shield:** If the risk is narrowly defined (e.g., a specific patient demographic), an input "shield" is deployed, preventing the model from running on that subgroup and instead displaying a "Study type not supported" message.
4.  **Post-Emergency Analysis:** Within 24 hours of the rollback/shield, a full RCA is initiated. The emergency action and its justification are fully documented and reviewed at the next CRB meeting.

---

## 9. Training Requirements

All personnel involved in the Clinical AI Feedback Loop must complete the following training, tracked in the Meridian Learning Management System (LMS), Cornerstone.

| Training Module Code | Module Name | Target Audience | Frequency | Owner |
| :--- | :--- | :--- | :--- | :--- |
| **LMS-CAI-014.1** | SOP-CLIN-014: Clinical AI Feedback Loop Procedure | All roles in RACI matrix | **Initial:** Before receiving FMS access. **Recurring:** Annually. | Clinical AI Product Ops |
| **LMS-CAI-014.2** | Feedback Management System (FMS) End-User Training | Clinician Users, Model Product Managers | **Initial:** Onboarding. **Recurring:** As needed for major UI updates. | Clinical AI Product Ops |
| **LMS-CAI-014.3** | FMS Administrator & Investigator Training | AI/ML Engineers, Clinical Safety Leads, Regulatory Affairs | **Initial:** Before receiving elevated FMS access. **Recurring:** Annually. | Clinical AI Product Ops / QMS Team |
| **LMS-REG-001** | Mandatory Reporter Training: Adverse Events & Safety Signals | All Personnel | Annually | Regulatory Affairs |
| **LMS-PRIV-001** | Data Privacy & PHI Handling for AI Teams | AI/ML Engineers, Clinical Safety Leads, Data Curators | Semi-Annually | Chief Privacy Officer |

**Training Compliance:** The VP of Clinical AI Products, Dr. Aisha Okafor, reviews a monthly report of training compliance. Any personnel with lapsed training for their role will have their FMS access suspended until retraining is completed. 100% compliance is a KPI for the department.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Document Name |
| :--- | :--- |
| SOP-CLIN-015 | Bias Monitoring and Mitigation for Clinical AI |
| SOP-QUAL-001 | Quality Management System (QMS) Overview |
| SOP-REG-001 | Adverse Event and Field Safety Corrective Action Reporting |
| SOP-MLOPS-012 | Clinical AI Model Development and Deployment Lifecycle |
| SOP-ENG-005 | Engineering Defect Management |
| SOP-CX-102 | Customer Experience Feedback Management |
| SOP-PRIV-001 | PHI Breach Identification and Response |
| SOP-SEC-004 | Access Control and Audit Trail Review |
| SOP-REC-030 | Quality System Record Retention |
| SOP-UAT-008 | User Acceptance Testing for Clinical Products |

### 10.2 External References

- **European Union Artificial Intelligence Act (EU AI Act), Regulation (EU) 2024/1689:**
    - Article 9: Risk management system
    - Article 13: Transparency and provision of information to deployers
    - Article 14: Human oversight
    - Article 17: Quality management system
    - Article 61: Post-market monitoring by providers and the post-market monitoring plan for high-risk AI systems
    - Annex III: High-risk AI systems
- **NIST AI RMF 1.0:** Govern, Map, Measure, Manage functions.
- **NIST SP 1270:** Towards a Standard for Identifying and Managing Bias in AI.
- **EU Medical Device Regulation (EU MDR) 2017/745:** Annexes related to Post-Market Clinical Follow-up (PMCF).

---

## 11. Revision History

| Version | Date | Author | Description of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2022-03-15 | A. Okafor | Initial creation of the feedback loop process. Manual triage and email-based tracking. |
| 1.1 | 2022-08-22 | J. Chen | Implementation of the Feedback Management System (FMS) Jira module. Automated feedback creation from in-app widget. |
| 2.0 | 2023-01-17 | A. Okafor | Major revision. Introduced formal severity matrix, mandatory HITL clinical sign-off for all model updates, and integrated silent deployment/shadow mode process. |
| 2.1 | 2023-06-30 | P. Müller | Updated to add formal bias and fairness testing requirements (Section 6.5) in response to updated NIST AI RMF guidance. Added LMS training module LMS-CAI-014.3. |
| 2.2 | 2024-02-12 | A. Okafor | Comprehensive update for EU AI Act readiness. Added "High-Risk AI System" and other definitions. Formalized CRB roles, PMCF linkage, and Article 13/14 compliance statements. Updated SLAs. |
| 2.3 | 2024-09-04 | A. Okafor | Post-CE Marking update. Refined scope to align with MDR PMCF requirements. Enhanced Section 6.5 safeguards on Bias Drift. Updated escalation path to include formal "Code: Signal" process. Minor updates to Roles and Responsibilities to reflect new org structure. |
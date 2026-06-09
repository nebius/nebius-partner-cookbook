---
sop_id: "SOP-CLIN-009"
title: "Clinical Workflow Automation"
business_unit: "Clinical AI Products"
version: "3.9"
effective_date: "2024-09-17"
last_reviewed: "2025-09-24"
next_review: "2026-03-09"
owner: "Dr. Aisha Okafor, VP of Clinical AI Products"
approver: "Dr. Priya Patel, Chief Medical Officer"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "HIPAA"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: Clinical Workflow Automation

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework for the design, deployment, monitoring, and governance of automated clinical workflows within the Meridian Health Technologies Clinical AI Platform. It defines the standardized methodology by which AI-driven decision-support outputs are integrated into clinical workflows, ensuring that automation enhances clinical efficiency while maintaining patient safety, regulatory compliance, and human oversight obligations.

The purpose of this SOP is to:
- Define a consistent, auditable process for translating clinical decision-support logic into automated workflows.
- Ensure all automated clinical workflows comply with the EU AI Act's requirements for high-risk AI systems, HIPAA Privacy and Security Rules, and the NIST AI Risk Management Framework (AI RMF).
- Establish clear boundaries between autonomous AI actions, suggested actions requiring human confirmation, and actions strictly prohibited from automation.
- Provide a structured mechanism for clinical review, approval, and ongoing performance monitoring of automated workflows.

### 1.2 Scope

This SOP applies to all automated workflows within the Clinical AI Platform (Meridian Clinical AI Products business line) that influence, direct, or execute clinical or clinical-operational tasks. This includes, but is not limited to:

| In-Scope Systems | Description |
|---|---|
| Clinical Decision Support (CDS) Workflows | Automated alerts, risk score-triggered orders, diagnostic imaging prioritization (FDA 510(k)-cleared and CE-marked modules). |
| Adverse Event Prediction & Escalation | Automated detection and notification of predicted patient deterioration, sepsis risk, or adverse drug events. |
| Care Gap Closure Automation | Automated patient outreach triggers, appointment scheduling suggestions, and order set recommendations based on MedInsight Analytics outputs. |
| Clinical Documentation Assistance | AI-generated clinical note drafts, automated coding suggestions, and structured data extraction from unstructured notes. |
| Triage & Patient Flow Automation | AI-driven emergency department prioritization, inpatient bed assignment suggestions, and clinic scheduling optimization. |

This SOP applies to the following personnel and functions:
- Clinical AI Product teams (engineering, product management, clinical informatics).
- Clinical Workflow Designers and Configuration Specialists.
- Medical Directors and Clinical reviewers assigned to workflow validation.
- Quality Assurance and Validation teams.
- Compliance and Data Protection Officers overseeing clinical AI deployment.
- Any Meridian personnel or contractors involved in the design, testing, approval, or monitoring of automated clinical workflows.

**Out of Scope:** This SOP does not cover the underlying model development lifecycle (see SOP-AI-004, *AI Model Development and Validation*) or the general IT change management process for non-clinical SaaS platform updates (see SOP-IT-002, *IT Change and Release Management*). Financial transaction automation within HealthPay Financial Services is governed by SOP-FIN-011, *Automated Financial Decisioning Controls*.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|---|---|
| **Automated Clinical Workflow (ACW)** | A configured sequence of automated actions, triggers, and decision points within the Meridian Clinical AI Platform that executes clinical or clinical-operational tasks based on AI model outputs. |
| **Clinical Decision Support (CDS)** | AI-generated information, recommendations, or alerts intended to influence clinical decision-making by a qualified clinician. |
| **Human-in-the-Loop (HITL)** | A workflow design pattern where AI system output requires explicit review and confirmation by a qualified human operator before any action is taken. |
| **Human-on-the-Loop (HOTL)** | A workflow design pattern where the AI system executes actions autonomously but under continuous human supervision, with the ability for a human operator to intervene or override in real-time. |
| **Fully Autonomous Action** | An AI-driven action executed without real-time human review. Permitted only where explicitly authorized under this SOP and where patient risk is negligible or where speed of action precludes human delay (e.g., immediate critical alert generation). |
| **Workflow Risk Classification** | A three-tier classification (Low, Medium, High) assigned to each ACW based on potential patient harm, regulatory impact, and autonomy level. |
| **Clinical Safety Case** | A structured argument, supported by evidence, that an ACW is acceptably safe for its intended use within a defined clinical context. Required for all Medium and High-risk workflows. |
| **Adverse Impact Incident** | Any event where an ACW's action or failure to act results in, or significantly contributes to, patient harm, a data breach, or a reportable regulatory violation. |
| **EU AI Act** | Regulation (EU) 2024/1689 laying down harmonized rules on artificial intelligence. |
| **HIPAA** | Health Insurance Portability and Accountability Act of 1996, including the Privacy, Security, and Breach Notification Rules. |
| **NIST AI RMF** | National Institute of Standards and Technology AI Risk Management Framework (NIST AI 100-1). |
| **PHI** | Protected Health Information, as defined under HIPAA. |
| **QMS** | Quality Management System. Meridian's ISO 13485-certified QMS for medical device software. |
| **RPN** | Risk Priority Number, derived from Failure Mode and Effects Analysis (FMEA). |

---

## 3. Roles and Responsibilities

The following RACI matrix defines the responsibilities for core activities governed by this SOP. Specific named organizational roles from the Meridian leadership structure are referenced where applicable.

| Activity | Responsible (R) | Accountable (A) | Consulted (C) | Informed (I) |
|---|---|---|---|---|
| **ACW Design & Configuration** | Clinical Workflow Designers, Solution Architects (VP of Clinical AI Products org) | VP of Clinical AI Products (Dr. Aisha Okafor) | Clinical SMEs, CISO (Rachel Kim) | VP of Customer Operations (Michael Chang) |
| **Clinical Safety Case Approval** | Clinical Review Board (chaired by CMO or designate) | Chief Medical Officer (Dr. Priya Patel) | Chief AI Officer, DPO | VP of Clinical AI Products |
| **Technical Security Review** | Security Engineering (under CISO) | Chief Information Security Officer (Rachel Kim) | Data Protection Officer, Compliance | VP of Engineering |
| **Regulatory Compliance (EU AI Act / HIPAA) Sign-off** | Regulatory Affairs, Data Protection Officer | Chief Compliance Officer | Legal Counsel, CMO | Regulatory Notified Body (as required) |
| **AI Risk Mapping (NIST AI RMF)** | AI Governance Lead (under Chief AI Officer) | Chief AI Officer | Product Management, Compliance | CISO, CMO |
| **In-Production Monitoring & Incident Response** | Clinical AI Operations (DevOps), Customer Success | VP of Clinical AI Products (Dr. Aisha Okafor) | CISO (for data incidents), CMO (for clinical incidents) | Chief Medical Officer, Regulatory Affairs |

---

## 4. Policy Statements

### 4.1 General Principles

- **P4.1.1 Safety First:** No automated clinical workflow shall be deployed to production that has not undergone a rigorous, documented risk assessment and received required approvals commensurate with its risk classification. The clinical safety case is the foundational document for all Medium and High-risk ACWs.
- **P4.1.2 Human Oversight Mandate:** In accordance with Article 14 of the EU AI Act, all High-risk ACWs shall be designed and built with appropriate human oversight mechanisms. No High-risk ACW shall operate in a fully autonomous mode without a documented, approved exception from the Chief Medical Officer and Chief Compliance Officer.
- **P4.1.3 Transparency and Explainability:** Clinicians affected by an ACW must be able to understand the basis for an automated action. Per HIPAA and the EU AI Act, an explanation of the AI's logic, in plain language, must be accessible from the point of action.
- **P4.1.4 Data Minimization:** Automated workflows shall process only the minimum necessary PHI required to accomplish the specific clinical task, per HIPAA Minimum Necessary Standard (45 CFR § 164.502(b)).
- **P4.1.5 Non-Discrimination:** ACWs must be designed and monitored to prevent algorithmic bias against protected patient populations. Fairness metrics are mandatory for all Medium and High-risk workflows (aligned with NIST AI RMF MAP function).

### 4.2 Workflow Design Principles

- **P4.2.1 Default to Human-in-the-Loop:** The default design pattern for any clinical ACW is HITL. Deviations toward higher autonomy require escalating levels of clinical validation and management approval.
- **P4.2.2 Idempotency and Safety:** All automated actions must be designed to be idempotent where possible (e.g., duplicate order checks). Workflows must have clearly defined, safe defaults for error states.
- **P4.2.3 Audit Trail Immutability:** Every automated decision, suggestion, and action, including HITL confirmations and HOTL overrides, shall generate an immutable, timestamped, signed audit record (see Section 6.3).

### 4.3 Regulatory Commitment

The *Clinical Workflow Automation* environment is a core component of Meridian's registered Medical Device Software (MDSW) and is subject to the EU AI Act as a high-risk AI system (Annex III, point 1: Medical devices). Additionally, as a Business Associate for many covered entities, Meridian must adhere to HIPAA regulations for any ACW processing PHI. All ACWs are considered AI systems within Meridian's enterprise risk universe under the NIST AI RMF.

---

## 5. Detailed Procedures

### 5.1 Workflow Ideation and Intake

Any stakeholder (e.g., Clinical Product Manager, Customer Success, Clinical SME) may propose a new automated clinical workflow. The process begins with the submission of a **Workflow Automation Request (WAR)** form.

| WAR Field | Description |
|---|---|
| **Workflow Name & ID** | Unique identifier from the Clinical Product backlog (e.g., `WF-SEPSIS-ALERT-001`). |
| **Clinical Problem Statement** | A clear description of the clinical gap or inefficiency being addressed. |
| **Proposed Automation** | A detailed, step-by-step description of the proposed workflow, including triggers, AI model(s) used, data inputs, logic branches, and resultant actions. |
| **Preliminary Risk Categorization** | Self-assessment by the requestor (Low, Medium, High) based on the criteria in Table 5-A. |
| **Clinical Sponsor** | A named clinical SME (typically a physician or nurse informaticist) who champions the workflow. |

The WAR is submitted to the **Clinical AI Product Review Board** (chaired by the VP of Clinical AI Products or delegate), which meets bi-weekly. The Board reviews the submission for strategic alignment, feasibility, and preliminary safety. Approved WARs are added to the product backlog and proceed to detailed design.

**Table 5-A: Preliminary Workflow Risk Categorization**

| Factor | Low Risk | Medium Risk | High Risk |
|---|---|---|---|
| **Potential for Direct Patient Harm** | Negligible; purely administrative/operational. | Indirect; workflow outputs influence a decision, but cannot directly trigger an intervention. | Direct; workflow can suggest, order, or trigger a diagnostic test, medication, or procedure. |
| **Human Oversight Level** | Fully Autonomous (no clinical review) or HOTL. | HITL for all substantive recommendations. | HITL by a licensed independent practitioner; any deviation requires CMO approval. |
| **Data Sensitivity** | De-identified or aggregate data only. | Limited PHI used for non-critical tasks (e.g., preventative care outreach, appointment reminders). | Full PHI used for urgent/emergent tasks (e.g., triage, critical result notification, safety alerts). |

### 5.2 Detailed Design and Clinical Safety Case

Upon approval into the development backlog, the assigned Clinical Workflow Designer and Solution Architect create the **Detailed Design Document (DDD)** and the **Clinical Safety Case (CSC)**. These documents are developed concurrently.

#### 5.2.1 Detailed Design Document (DDD) Minimum Contents

1.  **Workflow Diagram (BPMN 2.0):** A Business Process Model and Notation diagram mapping all steps, actors (AI and human), decision gateways, and exception paths.
2.  **Trigger Logic Specification:** Precise definition of the event that initiates the workflow (e.g., `Observation.FHIR` resource created with LOINC code `X`, value `> Y`).
3.  **Input Data Model:** A declared schema specifying every piece of PHI or clinical data consumed, including its source system (EHR, LIS, etc.), FHIR resource type, and business purpose. This is critical for HIPAA Minimum Necessary compliance.
4.  **AI Model Interface Contract:** Reference to the specific, validated model version (see SOP-AI-004), its performance characteristics (AUC, sensitivity, specificity), and the defined operating point for the workflow trigger.
5.  **Action Definition:** For each output action (alert, order set suggestion, new note draft, etc.), the exact payload is defined (e.g., CDS Hooks card structure).
6.  **HITL/HOTL Implementation Detail:** The specific UI/UX element (e.g., confirmation dialog with hard stop, non-interruptive alert with an "Override Reason" dropdown) and the associated roles authorized to act (e.g., `MD`, `RN`, `Clinical Pharmacist`).

#### 5.2.2 Clinical Safety Case (CSC) Development

The CSC is executed as a formal Failure Mode and Effects Analysis (FMEA) with the Clinical Sponsor and an independent clinical reviewer.

1.  **Identify Failure Modes:** For each node in the BPMN diagram, brainstorm potential failure modes (e.g., "Alert fatigue due to high false positive rate," "Pharmacy system down; order not received," "Bias against elderly patients for sepsis alert").
2.  **Assign Severity (S), Occurrence (O), and Detectability (D)** on a 1-5 scale.
3.  **Calculate RPN (S x O x D).** Any failure mode with a Severity score of 4 or 5 automatically triggers a mandatory mitigation plan, regardless of RPN.
4.  **Define Mitigation Controls:** For each high-priority risk, document the technical or procedural control (e.g., "Workflow has a hard five-minute time-out on the pharmacy order pending acknowledgment. If no acknowledgment, a critical alert pages the on-call clinical pharmacist.").
5.  **Calculate Residual Risk:** Re-score S, O, and D with the mitigation in place. The Clinical Sponsor must sign off on the final residual risk profile.

The completed DDD and CSC package is the entry criteria for the formal review process.

### 5.3 Formal Workflow Review and Approval

The review process is a formal gate and is enforced via the Meridian QMS. The approval board composition depends on the Workflow Risk Classification.

**Table 5-B: Approval Board by Risk Classification**

| Risk Level | Approving Body | Required Evidence Package |
|---|---|---|
| **Low** | Clinical AI Product Team Lead + QA Lead | WAR, DDD, Summary CSC (showing no High risks). |
| **Medium** | Clinical AI Review Board (chaired by VP of Clinical AI Products or CMO delegate) | WAR, DDD, full CSC, Security Impact Assessment, HIPAA Privacy checklist. |
| **High** | Clinical Safety Board (chaired by Chief Medical Officer, Dr. Priya Patel) | All of the above, plus: External clinical advisory review (2 independent physicians), Algorithmic Bias Assessment report, EU AI Act Conformity Assessment documentation. |

The review ensures the workflow design meets the **General Clinical Requirements (GCR)** checklist:

- [ ] **GCR-01:** Workflow is designed, per P4.2.1, with an appropriate level of human oversight. Any autonomous action is clinically justified and rigorously limited.
- [ ] **GCR-02:** AI model performance thresholds are defined and appropriate for the clinical context.
- [ ] **GCR-03:** All input data elements are clinically relevant and represent the minimum necessary PHI.
- [ ] **GCR-04:** Override and rejection mechanisms are intuitive and properly capture structured reasons and unstructured comments.
- [ ] **GCR-05:** Failure modes are handled safely, defaulting to a state that alerts a human rather than failing silently.
- [ ] **GCR-06:** For High-risk workflows, a full Conformity Assessment according to Annex VII of the EU AI Act has been completed, and the EU declaration of conformity has been prepared.

Upon successful review, all approvers provide an electronic signature within the Meridian QMS (Qualio).

### 5.4 Technical Build and Configuration

With an approved design, the Clinical AI Engineering team proceeds with the technical build.

1.  **Branching and Environment:** The workflow configuration code (typically JSON/YAML workflow definitions and any associated serverless functions) is developed in a feature branch off `develop` in the `meridian-clin-ai/acu-flow-engine` repository.
2.  **Configuration Management:** All workflow definitions are stored in the Configuration Management Database (CMDB) using Ansible and version-controlled in Git. The `version` field in the workflow header must match the QMS-approved DDD version.
3.  **Secrets Management:** Any credentials or API keys used by the workflow to interact with an EHR (e.g., via SMART on FHIR) are stored in HashiCorp Vault, never in code or configuration files.
4.  **Audit Logging Implementation:** Engineers must implement the audit logging schema defined in Section 6.3 using the standard `fhir-audit-svc` internal service.
5.  **Code Review:** All code changes must undergo peer review by a senior engineer. The review checklist includes explicit items for PHI handling and audit completeness.

### 5.5 Testing and Validation Protocol

Testing is a multi-layered process, moving from synthetic validation to clinical realism.

#### 5.5.1 Unit and Integration Testing
- Automated tests in the CI/CD pipeline (Jenkins) verify the workflow engine logic, correct parsing of FHIR resources, and proper handling of downstream system errors (e.g., timeouts).
- Test PHI, derived from the Meridian Synthetic Data Generator, is used exclusively. No production PHI is permitted in `dev` or `test` environments.

#### 5.5.2 Workflow Validation (Staging Environment)
A dedicated Clinical QA team, separate from the engineering team, executes a pre-defined **Workflow Validation Protocol (WVP)** .
- **Traceability:** Each step in the approved DDD's BPMN diagram must be traced to one or more WVP test cases.
- **Positive Testing:** Simulated clinical scenarios that *should* trigger the workflow are executed. The team verifies that the correct action is taken (e.g., exact CDS Hooks card appears for the correct patient and user).
- **Negative and Boundary Testing:** Scenarios that should *not* trigger the workflow are tested, along with boundary conditions (e.g., just above and just below a risk score threshold).
- **Override and Error Testing:** The QA team rigorously tests all override paths and simulated error conditions (e.g., EHR API returning a 500 error).

#### 5.5.3 Clinical Simulation and Usability
For Medium and High-risk workflows, a Clinical Simulation is mandatory. This is orchestrated by the Clinical Informatics team and involves:
1.  **Patient Case Creation:** Clinical SMEs create 10-15 realistic, de-identified patient cases based on historical data.
2.  **Simulated Environment Testing:** Cases are run through the workflow in a production-mirroring staging environment.
3.  **Clinician-in-the-Loop Validation:** 3-5 practicing clinicians from Meridian's Clinical Advisory Network are brought in for a structured usability session. They interact with the workflow's HITL/HOTL interfaces and provide qualitative feedback on clarity, cognitive load, and clinical trust. This feedback is documented and must be resolved before production release.

### 5.6 Production Deployment

Deployment follows the Meridian IT Change and Release Management SOP (SOP-IT-002) with specific clinical workflow requirements:
1.  **Approved Change Request (CR):** A CR in ServiceNow must be linked to the approved, signed DDD and CSC documents.
2.  **Staged Rollout:** High-risk workflows default to a staged, "silent mode" rollout for a minimum of 7 days where the workflow runs and logs all actions to the audit trail and a Grafana dashboard without actually executing actions in the production EHR. This allows real-world performance to be validated without clinical impact.
3.  **Activation:** Activation from silent mode is an explicit step in the Change Request, authorized by the VP of Clinical AI Products and CMO (for High-risk workflows).
4.  **Deployment Verification:** Immediately post-deployment, the Clinical AI Operations team runs a suite of smoke tests against the production workflow to confirm basic connectivity and functionality.

---

## 6. Controls and Safeguards

### 6.1 Technical Access Controls

Per HIPAA Security Rule (§ 164.312(a)), technical access controls ensure only authorized systems and personnel interact with the workflow engine.

| Control | Implementation |
|---|---|
| **Service-to-Service Authentication** | All inter-service communication (e.g., Workflow Engine to `fhir-audit-svc`) uses OAuth 2.0 Client Credentials flow with short-lived JWTs signed by Meridian's internal Okta authorization server. |
| **EHR API Access** | The Workflow Engine interacts with customer EHRs via SMART on FHR. It uses a backend service authorization profile, with JWT assertions per RFC 7523. No long-lived API keys are stored locally. |
| **Privileged Access Management (PAM)** | Direct shell access to production workflow engine servers is restricted to the Clinical AI Operations team. All access is brokered through CyberArk PSM, requiring MFA, and all sessions are recorded. |
| **Network Segmentation** | The Clinical AI Platform, including the Workflow Engine, resides in a dedicated, private subnet. Ingress traffic is strictly controlled via a Web Application Firewall (WAF) and API Gateway. |

### 6.2 EU AI Act: Oversight and Quality Controls

Meridian implements specific controls to address the high-risk AI system requirements under EU AI Act Title III, Chapters 2 and 3.

**Article 14 (Human Oversight):**
- **Control EU-14.1:** Every High-risk ACW is instrumented with a "human override dashboard" accessible to designated customer super-users (e.g., Chief Medical Informatics Officer). This dashboard, built on Grafana, provides a real-time stream of recent automated actions within that customer's tenant and a one-click override button. The SLA for a Meridian Operations team member to respond to a customer override activation is 15 minutes, 24/7/365.
- **Metric EU-14.M1, M2:** Track override rate per workflow per month (target: < 2%); track time-to-respond to override activations (target: < 10 minutes).

**Article 15 (Accuracy, Robustness, and Cybersecurity):**
- **Control EU-15.1:** Input data validation pipelines validate every inbound FHIR resource against a strict profile. Non-conforming resources are rejected and logged as safety events.
- **Metric EU-15.M1:** Workflow execution error rate due to data validation failure (target: < 0.05% per workflow).
- **Control EU-15.2:** Annual adversarial robustness testing of all clinical AI models by an independent, third-party security firm.

### 6.3 HIPAA Audit Controls and Integrity

Per HIPAA Security Rule (§ 164.312(b) and (c)), controls ensure the integrity and non-repudiation of all automated actions.

**Immutable Audit Trail:**
Every significant event within an ACW generates an immutable audit entry in the Meridian Central Audit Service, persisted in a write-once, read-many (WORM) compliant storage layer.

**Table 6-A: Audit Event Attributes**
| Attribute | Example |
|---|---|
| `timestamp` | `2025-04-11T14:31:22.000Z` |
| `event_type` | `CLINICAL_ACTION.EXECUTED` |
| `workflow_id` | `WF-SEPSIS-ALERT-001` |
| `patient_id` | UUID pseudonym; real MRN not accessible to audit service per architecture. Link is via `fhir-audit-svc` mapping table. |
| `action_target` | The URI of the FHIR resource being acted upon/created. |
| `actor` | `SYSTEM`, or `USER: <practitioner-fhir-id>` for HITL confirmations. |
| `result` | `SUCCESS`, `FAILURE`, `OVERRIDDEN_BY_USER` |
| `detail` | JSON body with full action payload and explanation. |
| `digital_signature` | SHA-256 HMAC of the entry, signed by the Workflow Engine's private key. |
- **Control HIPAA-312.b-1:** Quarterly audit trail reviews by the Information Security team searching for anomalous activity patterns, unauthorized access, or data alteration.

### 6.4 NIST AI RMF-Specific Operational Controls
These controls specifically address the operationalization of the AI RMF MAP and GOVERN functions within the context of workflow automation.

- **Control NIST-AI-001 (AI Risk Mapping):** Each ACW will be associated with an entry in the *Meridian AI System Inventory* (SharePoint-based). The entry will reference the latest CSC, approved AI models, and a set of contextual risk categories including `Fairness/Bias`, `Explainability`, `Safety`, and `Security`. A "Risk Profile" report is generated for all High-Risk systems on a semi-annual basis and presented to the Clinical AI Review Board.
- **Control NIST-AI-002 (Trustworthiness Metrics):** All active High-Risk ACWs must report trustworthiness metrics (drift, fairness, performance) to a centralized AI Monitoring Dashboard. Thresholds for automated rollback are configured in Section 7.2.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Performance Dashboards

Two distinct Grafana dashboards are maintained for each Customer Tenant and an aggregated view for Meridian Operations:
1.  **Clinical Operations Dashboard:** Displays real-time ACW execution metrics, including throughput, latency, error rates, and override volumes.
2.  **AI Trustworthiness Dashboard:** Displays model drift (Population Stability Index - PSI), feature drift, fairness metrics (e.g., false positive rate parity), and explainability scores.

### 7.2 Key Performance and Risk Indicators

**Table 7-A: Automated Monitoring Thresholds and Actions**

| Metric | KPI / Target | Automated Alert (Ops) | Automated Rollback Trigger |
|---|---|---|---|
| **Workflow Execution Latency (p99)** | < 500ms | P99 > 1s for 5 minutes. | P99 > 2s for 15 minutes. |
| **Workflow Error Rate (5xx)** | < 0.1% | > 1% for 1 minute. | > 5% for 5 minutes, manual rollback. |
| **Human Override Rate** | < 2% per month | > 5% in a rolling 7-day window. | > 15% in a 7-day window triggers a forced workflow pausing (silent mode). |
| **AI Drift (PSI)** | < 0.1 | PSI > 0.15 for 3 consecutive daily batches. | PSI > 0.25 triggers a *Stop New Actions* state; only read-only and alert workflows continue. |
| **Fairness Disparity (e.g., FPR)** | < 5% difference between primary demographic groups | > 7% difference detected in weekly batch. | > 10% difference triggers immediate Clinical Safety Board review and may result in workflow suspension. |

### 7.3 Reporting Cadence

- **Weekly:** Automated report to the Clinical AI Operations team and the VP of Clinical AI Products, covering all KPIs and threshold breaches for the week.
- **Monthly:** "Clinical AI Safety and Performance Report" presented to the Clinical AI Review Board, summarizing KPIs, override trends, incident reports, and mitigation plan status.
- **Semi-Annual:** A comprehensive AI System Inventory review and risk profile update is conducted by the AI Governance Lead and presented to executive leadership (Chief AI Officer, CMO, CISO, Chief Compliance Officer). This process maps all ACWs to the latest NIST framework risk categories.

---

## 8. Exception Handling and Escalation

### 8.1 Technical Workflow Failures

Any failure in a workflow's execution path, where the engine cannot successfully complete the programmed logic, is handled by the Meridian Clinical AI Platform's centralized Error Handling Service.

1.  **Identify:** The service catches the exception and assigns it a `WF-FAILURE` event ID.
2.  **Classify:** The service attempts automatic retry logic (e.g., for transient network errors, retry 3 times with exponential backoff). Transient failures are logged and retried. Persistent, unhandled failures are classified as `CRITICAL` and logged to the Central Audit Service with `result: FAILURE`.
3.  **Notify:** A `CRITICAL` failure generates a P2 incident in PagerDuty, routing to the on-call Clinical AI Operations engineer. The alert includes the `WF-FAILURE` event ID and workflow name.
4.  **Resolve:** The engineer investigates via Kibana logs and the audit trail. If the fix requires a code or configuration change, the standard emergency change process (SOP-IT-002, Section 9) is invoked. The goal for initial investigation and triage is 30 minutes.

### 8.2 Clinical Exception Handling (Overrides)

A human override is not a system failure but a clinical disagreement or reconsideration. All overrides are recorded with:
- **Actor:** The clinician's identity.
- **Reason:** A structured reason code from a configurable value set (e.g., `CONCERN_FOR_ALERT_FATIGUE`, `PATIENT_SPECIFIC_FACTORS_INVALID_ASSUMPTION`, `WORKFLOW_NOT_INDICATED`).
- **Unstructured Comment:** An optional free-text field.

Overrides with the reason `INACCURATE_AI_INPUT` or `HARMFUL_AI_RECOMMENDATION` are automatically flagged for immediate clinical review by the Clinical Safety Board within 1 business day. This is a critical feedback loop for model and workflow improvement.

### 8.3 Requests for Permanent Workflow Modification

A request from a customer or an internal team to permanently modify a deployed ACW (e.g., change a lab value threshold, add a new exclusion criterion) is treated as a new WAR and follows the full procedure in Section 5, beginning with submission to the Clinical AI Product Review Board. No ad-hoc configuration changes are permitted directly in a production environment.

---

## 9. Training Requirements

### 9.1 Meridian Internal Personnel

All roles identified in Section 3 of this SOP must complete role-based training on the Clinical Workflow Automation process.

| Role(s) | Training Module | Frequency | Tracking |
|---|---|---|---|
| **Clinical Workflow Designers, Solution Architects** | `CLIN-AI-009-ARCH`: Advanced Workflow Design, Safety Case Development, and EU AI Act High-Risk Controls | Annually | Meridian LMS (Litmos) |
| **Clinical SMEs, QA** | `CLIN-AI-009-SME`: Workflow Validation and Clinical Simulation Best Practices | Annually | Litmos |
| **Clinical AI Operations (DevOps)** | `CLIN-AI-009-OPS`: Incident Response for Automated Clinical Systems, HIPAA Breach Assessment | Semi-Annually | Litmos & PagerDuty drill records |
| **Compliance, Regulatory Affairs, Legal** | `CLIN-AI-009-REG`: EU AI Act Conformity Assessment and Clinical AI Regulatory Landscape | Annually | Litmos |
- **HIPAA General Refresher:** Any internal personnel with access to systems processing PHI must complete annual HIPAA Security and Privacy Rule refresher training (SOP-HR-002).
- **Training Effectiveness:** Training effectiveness is measured via a post-course assessment. A passing score of 85% is required. Failure requires retraining within 30 days.

### 9.2 Customer-Facing Resources
- **Clinician Quick-Reference Cards:** For each deployed ACW, the Clinical Informatics team produces a one-page quick-reference guide explaining the workflow's logic, the oversight model, and how to interpret and act on its output.
- **Train-the-Trainer Program:** Meridian offers a certified "Clinical AI Workflow Champion" program for customer super-users, conducted by Meridian Customer Success, to ensure deep clinical governance knowledge at the customer site.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|---|---|---|
| `SOP-AI-004` | AI Model Development and Validation | Governs the upstream model development lifecycle that produces the AI models used in ACWs. |
| `SOP-IT-002` | IT Change and Release Management | Governs the deployment process for all software, including ACW configurations. Emergency change procedures are referenced here. |
| `SOP-DS-001` | Data Governance and Minimum Necessary Use | Defines the data classification and minimum necessary PHI policy that ACW design must adhere to. |
| `SOP-INFOSEC-005` | Incident Response and Breach Notification | Governs the response to an Adverse Impact Incident involving a data breach. |
| `SOP-QMS-001` | Quality Management System – Design Controls | The overarching QMS procedure for design and development of medical device software, under which this SOP sits. |
| `SOP-HR-002` | Annual HIPAA & Compliance Training | Defines enterprise-wide training requirements. |

### 10.2 External Standards and Regulations

- **Regulation (EU) 2024/1689** (EU AI Act), specifically Articles 9 (Risk management system), 10 (Data and data governance), 11 (Technical documentation), 14 (Human oversight), and 17 (Quality management system).
- **HIPAA** Privacy, Security, and Breach Notification Rules (45 CFR Parts 160, 164).
- **NIST AI 100-1:** Artificial Intelligence Risk Management Framework (AI RMF 1.0).
- **ISO 13485:2016:** Medical devices – Quality management systems.
- **ISO 14971:2019:** Medical devices – Application of risk management.
- **HL7 CDS Hooks** Specification, Release 2.0.
- **HL7 FHIR** Release 4 (R4).

---

## 11. Revision History

| Version | Effective Date | Author(s) | Summary of Changes |
|---|---|---|---|
| **3.9** | 2024-09-17 | Dr. Aisha Okafor, Compliance Team | Major revision incorporating EU AI Act conformity assessment gates into the approval procedure (Section 5.3). Updated training module `CLIN-AI-009-REG` to EU AI Act. Added detailed NIST AI RMF risk categories to inventory control (NIST-AI-001). Semi-annual reporting cadence updated. |
| **3.8** | 2024-03-21 | Dr. Aisha Okafor, Chief Product Security Officer (interim) | Refined access control model in Section 6.1 to use short-lived JWTs. Added explicit reference to `fhir-audit-svc` for immutable audit trail implementation. Clarified silent mode rollout duration in Section 5.6. |
| **3.7** | 2023-11-08 | Dr. Sarah Chen (Medical Director), Clinical Informatics | Extensive update to Clinical Safety Case (CSC) requirements in Section 5.2.2, mandating FMEA. Added Clinical Simulation requirement (Section 5.5.3) for Medium and High-risk workflows. Created formal Workflow Automation Request (WAR) intake form. |
| **3.6** | 2023-05-15 | Clinical AI Engineering | Updated Detailed Design Document (DDD) template to mandate FHIR resource schema for HIPAA compliance. Added Table 6-A for Audit Event Attributes. Initial introduction of automated monitoring thresholds for fairness metrics. |
| **3.5** | 2022-12-05 | Dr. Priya Patel, CMO | First major revision post-initial pilot. Formalized approval board and risk classification framework. Introduced distinction between HITL and HOTL. Established core policy statements (Section 4). |
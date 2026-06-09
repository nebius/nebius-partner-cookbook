---
sop_id: "SOP-CLIN-018"
title: "Clinical AI Labeling and Instructions for Use"
business_unit: "Clinical AI Products"
version: "3.9"
effective_date: "2024-04-08"
last_reviewed: "2025-01-17"
next_review: "2025-07-07"
owner: "Dr. Aisha Okafor, VP of Clinical AI Products"
approver: "Dr. Priya Patel, Chief Medical Officer"
classification: "Internal"
regulations:
  - "EU AI Act"
status: "Active"
---

# Standard Operating Procedure: Clinical AI Labeling and Instructions for Use

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the minimum requirements and procedural framework for the creation, review, approval, and lifecycle management of labeling and instructions for use (IFU) for all Clinical AI Platform products developed, maintained, or distributed by Meridian Health Technologies, Inc. The purpose of this SOP is to ensure that all user-facing materials are accurate, consistent, clinically appropriate, legally defensible, and support the safe and effective use of our AI-driven clinical decision support software.

### 1.2 Scope
This SOP applies to the following product categories within the **Clinical AI Platform** business unit, including but not limited to:

| Product Category | Examples | Deployment Context |
| :--- | :--- | :--- |
| Diagnostic Imaging AI | Chest X-ray triage, brain CT hemorrhage detection, mammography lesion identification | Radiology workflows, PACS integration |
| Patient Risk Scoring | 30-day readmission risk, sepsis early warning, mortality risk stratification | EHR-embedded, inpatient and outpatient settings |
| Adverse Event Prediction | Drug-drug interaction alerts, contrast-induced nephropathy prediction | CPOE integration, nursing dashboards |
| Clinical Decision Support | Antibiotic stewardship recommendations, treatment pathway suggestions | Physician order review, care gap alerts |

This SOP applies to all labeling deliverables, including:

- **Instructions for Use (IFU)** documents delivered with the software.
- **In-app labels, tooltips, and notifications** within the Meridian Clinical AI user interface.
- **Intended Use Statements** in regulatory submissions and marketing collateral.
- **Contraindications and limitations** documentation.
- **Training and quick-reference materials** supplied to end-users (clinicians, nurses, and allied health professionals).
- **Safety-related communications and field corrective action notices.**

### 1.3 Audience
This SOP is binding upon all employees, contractors, and third-party partners of Meridian Health Technologies involved in the design, development, validation, regulatory submission, deployment, and commercial distribution of Clinical AI Products. Specifically, this includes:

- Clinical AI Product Management
- Clinical AI Engineering and Machine Learning teams
- Clinical Informatics and Medical Affairs
- Regulatory Affairs
- Quality Assurance
- Customer Operations and Professional Services
- Medical Writing vendors under contract

Exclusions: This SOP does not govern the labeling of HealthPay Financial Services scoring models or the MedInsight Analytics population health dashboards. For those business units, refer to SOP-FS-104 and SOP-ANL-045 respectively.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **AI / ML** | Artificial Intelligence / Machine Learning |
| **CDS** | Clinical Decision Support |
| **IFU** | Instructions for Use – the legally required document providing users with information necessary for the safe and effective operation of a medical device or high-risk AI system. |
| **IS** | Intended Use Statement – a concise description of the clinical purpose, target population, and environment for which the AI system is designed. |
| **Contraindication** | A clinical scenario, patient characteristic, or technical condition under which the AI system MUST NOT be used because the predicted risk outweighs any potential benefit. |
| **Warning / Caution** | A statement alerting the user to a potential hazard or unsafe practice. Warnings indicate serious hazards; Cautions indicate hazards that could result in minor injury or data corruption. |
| **UI** | User Interface |
| **PACS** | Picture Archiving and Communication System |
| **EHR** | Electronic Health Record |
| **CPOE** | Computerized Physician Order Entry |
| **Labeling Oversight Committee (LOC)** | Cross-functional governance body responsible for final approval of all Clinical AI labeling. |
| **SME** | Subject Matter Expert |
| **QMS** | Quality Management System (MasterControl) |
| **Veeva Vault** | Meridian’s system of record for regulated content and labeling lifecycle management. |

---

## 3. Roles and Responsibilities

The following matrix defines the accountable (A), responsible (R), consulted (C), and informed (I) parties for key activities within this SOP.

| Activity / Deliverable | VP Clinical AI (Dr. Okafor) | Product Manager | Clinical SME (Medical Affairs) | Regulatory Affairs | Quality Assurance | Medical Writing | CMO (Dr. Patel) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Labeling Strategy & Planning** | A | R | C | C | I | I | I |
| **Intended Use & Contraindications Draft** | I | C | R | C | I | C | C |
| **IFU Authoring** | I | C | C | C | I | R | I |
| **Clinical Validation of Content** | I | I | R | C | I | C | I |
| **Regulatory & Legal Review** | I | I | C | R | C | I | I |
| **Final LOC Approval** | A | R | C | R | R | I | R (if safety) |
| **UI Label Review (Pre-Release)** | I | R | C | I | I | I | I |
| **Exception / Deviation Approval** | A | R | C | R | C | I | C |

### 3.1 Specific Role Details

- **VP of Clinical AI Products (Dr. Aisha Okafor):** Ultimate accountability for the labeling strategy and execution across the business unit. Approves all exceptions and is the designated signatory for EU AI Act compliance, reporting to the Board AI Governance Committee.
- **Product Manager:** Drives the labeling project plan, coordinates cross-functional reviews, and owns the product requirements document (PRD) that feeds the IFU.
- **Clinical SMEs (Medical Affairs):** Provide authoritative clinical definitions of patient populations, clinical scenarios, and performance interpretations. They validate that labeling aligns with standard-of-care workflows.
- **Regulatory Affairs:** Assesses labeling against global regulatory frameworks, manages submissions, and advises on legal implications of label claims.
- **Quality Assurance:** Ensures the labeling process adheres to Meridian’s QMS (ISO 13485 gap-compliant) and SOC 2 controls for document integrity.
- **Medical Writing (Internal/External):** Responsible for authoring the document in plain, actionable language consistent with Meridian’s style guide.

---

## 4. Policy Statements

### 4.1 General Labeling Principles
Meridian Health Technologies is committed to transparent communication regarding the capabilities and limitations of its Clinical AI systems. All labeling shall:

1.  **Be Accurate and Truthful:** Reflect the validated performance characteristics of the specific model version.
2.  **Be Accessible:** Written in the language of the intended user (e.g., English with a reading level not exceeding 10th grade for patient-facing components). EU deployments must provide labeling in the official language(s) of the Member State.
3.  **Support Human Oversight:** Clearly articulate that AI outputs are decision support tools, not autonomous diagnostic devices. User interpretation is mandatory in accordance with SOP-CLIN-022 (Human-in-the-Loop Protocols).
4.  **Be Version-Unique:** Every released version of an AI model shall have a corresponding, immutable labeling package in Veeva Vault.

### 4.2 Intended Use Statement
Every Clinical AI Product must have an approved Intended Use Statement that includes:
- The clinical function (e.g., detection, prioritization, prediction).
- The target anatomical site, pathology, or physiological state.
- The target patient population (e.g., age, sex, inclusion/exclusion criteria).
- The intended user profile (e.g., board-certified radiologist, ICU nurse).
- The clinical workflow step where input is acquired and output is interpreted.

### 4.3 Prohibited Statements
Labeling must not:
- Claim or imply diagnostic certitude or replace clinical judgment.
- Overstate model performance (e.g., using F1 scores from non-representative test sets).
- Use marketing language that contradicts safety information.
- Mask known biases or limitations discovered during development or post-market surveillance.

---

## 5. Detailed Procedures

This section describes the end-to-end process from labeling planning to retirement. All steps shall be tracked in Meridian’s QMS (MasterControl) and Veeva Vault.

### 5.1 Labeling Planning (Phase 0 – Product Definition)

#### 5.1.1 Trigger
The labeling process initiates upon gate approval of the Product Concept Document (PCD) for a new AI model or a significant revision to an existing model (e.g., expanded population, new imaging modality).

#### 5.1.2 Procedure
1.  **Product Manager** creates a "Labeling Project" record in Veeva Vault, linking it to the product’s Design History File (DHF) in MasterControl.
2.  **Product Manager** convenes a Labeling Kick-off Meeting with Medical Writing, Regulatory Affairs, Clinical SME, and Quality Assurance. The meeting agenda is based on the Labeling Planning Checklist (DOC-CLIN-018-A).
3.  The team defines the **Labeling Architecture**:
    - **Physician IFU:** Detailed technical and clinical performance document.
    - **Quick Reference Card (QRC):** Laminated card or single-page PDF for point-of-care use.
    - **In-App UI Strings:** JSON file containing all tooltips, hover text, and alert modals.
    - **Patient Information Leaflet:** Required if patient-facing risk scores are shown directly (e.g., MedInsight patient portal integration).
4.  **Regulatory Affairs** performs a jurisdictional analysis mapping required content against markets (FDA 510(k) clearance, EU AI Act CE marking, Health Canada MDL). This creates a Content Matrix.
5.  **Milestone:** Labeling Plan approved by VP Clinical AI or delegate.

### 5.2 Intended Use and Contraindications Drafting (Phase 1 – Core Content)

#### 5.2.1 Procedure
1.  **Clinical SME** authors the draft Intended Use Statement, including quantitative performance targets (e.g., sensitivity ≥ 0.95, specificity ≥ 0.90 at a defined operating point) sourced from the Model Performance Specification (DOC-ENG-202).
2.  **Clinical SME** defines contraindications. Contraindications must be explicit and linked to specific subpopulations where the model fails or degrades. Examples:
    - *"This model is contraindicated for pediatric patients under 2 years of age."*
    - *"Not intended for use on portable chest radiographs acquired via mobile X-ray units."*
3.  **Clinical SME** authors a draft of Warnings and Cautions. This includes:
    - **Data Drift Warning:** *"Warning: System performance may degrade if input image distributions differ significantly from training data. Monitor for site-specific performance."*
    - **Input Quality Caution:** *"Caution: Ensure DICOM image compression ratio does not exceed 15:1. Undersampling may result in false negatives."*
4.  The draft is uploaded as a "Draft – Phase 1" document in Veeva Vault with a controlled document number from the range CLIN-LAB-XXXX.

### 5.3 User Instructions Authoring (Phase 2 – IFU Development)
This is the core content development phase.

#### 5.3.1 IFU Template and Content
Medical Writing transforms the Phase 1 draft into a full IFU using the Meridian IFU Template (DOC-CLIN-018-B). Sections include:

| Section | Content Requirements |
| :--- | :--- |
| 1. Introduction | Product name, version, software build number, and a summary of the IS. |
| 2. System Requirements | Hardware (GPU, RAM), OS, browser, PACS/EHR interoperability specifications. |
| 3. Installation and Configuration | Instructions for IT administrators. Integration parameters and API configuration files. |
| 4. Clinical Workflow Integration | Step-by-step screenshots of triggering the AI analysis and interpreting the notification. |
| 5. Interpretation of Outputs | **Critical Section.** Defines the output format (e.g., heatmap, confidence score, binary flag). Defines the clinical action protocol per output type. Example: *"A ‘High Risk’ score (>0.85) indicates the patient is in the top quartile of readmission risk. Escalate to Case Management within 4 hours."* |
| 6. Performance Characteristics | Validation study summaries, population demographics, site-specific calibration details. |
| 7. Limitations and Known Biases | Specific, enumerated list of model limitations. Prohibition on off-label use. |
| 8. Training and Support | Links to Meridian LMS modules, support portal, and clinical hotline. |

#### 5.3.2 UI Labeling
The Product Manager works with UI/UX designers to populate a `ui_labels.json` file managed in Bitbucket.
- **Tooltips** (max 35 words): Hover text explaining icons or metrics. E.g., *"This score is generated by an AI model. Correlate with patient history before making clinical decisions."*
- **Watermarks:** All clinical output screens must carry the permanent watermark: **"AI Decision Support. Clinical Verification Required."**
- **Acknowledgment Flags:** For high-risk alerts (e.g., sepsis flag), a modal dialog must force an active user acknowledgment click tracking the user ID and timestamp.

### 5.4 Cross-Functional Review (Phase 3 – Review and Comment)

#### 5.4.1 Parallel Review
1.  **Medical Writing** initiates a "Concurrent Review" workflow in Veeva Vault, inviting the defined stakeholders.
2.  **SLA for Review:** All reviewers have **7 business days** to provide comments. Reviewers must categorize comments as *Critical*, *Major*, or *Minor*.
3.  **Clinical SME** is responsible for resolving all clinical accuracy comments.
4.  **Regulatory Affairs** verifies that all legal disclaimers are present and that the IS matches the cleared/approved indications. For EU markets, this includes verification of the CE marking symbol and Notified Body number (Notified Body 2797) placement.
5.  **Quality Assurance** audits the document for QMS traceability (correct version linkage to DHF).

### 5.5 Labeling Oversight Committee Approval (Phase 4 – Final Gate)
1.  Upon resolution of all Critical and Major comments, Medical Writing promotes the document to "Approved – Pending LOC."
2.  The Labeling Oversight Committee meets bi-weekly. The quorum for approval consists of VP Clinical AI (or delegate), Director of Regulatory Affairs, Director of Quality, and one Clinical SME.
3.  **Meeting Input:** Product Manager presents a 10-minute overview of the labeling and an executive summary of risks.
4.  **Approval:** Approval requires a unanimous vote from the quorum. Approved documents are locked for writing in Veeva Vault and digitally signed (21 CFR Part 11 compliant signatures).
5.  **Effective Date:** Labeling becomes effective upon release to production, not at LOC approval.

### 5.6 Post-Market Updates and Lifecycle Management
1.  **Trigger for Revision:** Any significant post-market surveillance signal (PMS) defined in SOP-REG-105, model retraining cycle (SOP-CLIN-015), or field safety corrective action (FSCA).
2.  **Urgent Safety Labeling:** The CMO (Dr. Priya Patel) has the authority to bypass the standard workflow and authorize immediate labeling updates for safety reasons. A retrospective LOC review must occur within 5 business days.
3.  **Version Retirement:** When a model is decommissioned, its labeling set is moved to "Superseded" state in Veeva Vault but is retained per Meridian’s Record Retention Policy (SOP-LGL-001).

---

## 6. Controls and Safeguards

### 6.1 Technical Controls
1.  **Version Binding:** The production SaaS platform (AWS us-east-1, eu-west-1) uses a feature flag system (LaunchDarkly) to bind a specific model URI to a specific IFU URL. If a model version is deployed, the API call to serve the IFU must return the corresponding valid version; otherwise, the model is blocked from execution.
2.  **UI Content Integrity:** In-app UI labels are deployed via a CMS (Contentful), which applies a content hash check. Deployment scripts compare the live hash against an approved golden image. Hash mismatch blocks the deployment pipeline (AWS CodePipeline).
3.  **Digital Signature Vault:** All finalized labeling PDFs are digitally signed using DigiCert PKI and time-stamped. The Meridian Clinical Portal can verify the PDF signature in-browser to prevent tampering.
4.  **Access Control (Veeva Vault & Git):** Write permissions for labeling content are restricted to the Medical Writing group and approved product managers. Direct Git pushes to `ui_labels.json` in master are blocked; changes require a pull request with mandatory review by Regulatory Affairs and the Product Manager.

### 6.2 Administrative Controls
1.  **Segregation of Duties:** The author (Medical Writing) cannot approve their own document; the approver (LOC) cannot edit the final approved PDF.
2.  **Audit Trail:** Veeva Vault maintains a complete, tamper-proof audit trail of every view, edit, comment, and approval action.
3.  **Periodic Review:** All active labeling is subject to a mandatory periodic review every 24 months, regardless of PMS triggers. The document owner (Product Manager) is responsible for ensuring the review is completed and documented before the expiry date tracked in Veeva Vault.

### 7.2 Reporting
- **Monthly Quality Review (MQR):** VP of Clinical AI reports labeling KPIs, open deviations, and LOC decisions to the Chief Medical Officer and Chief Quality Officer.
- **Quarterly Management Review (QMR):** Aggregated labeling metrics reviewed as part of the ISO 13485 Management Review process. Includes trending of exception handling and training compliance.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Definition
An exception to this SOP is defined as any deviation from the documented procedural steps or defined roles that results in a labeling deliverable not conforming to its Content Matrix specification (e.g., missing a required contraindication for a specific market, bypassing a review step due to a critical timeline).

### 8.2 Exception Procedure
1.  **Identification & Triage:** The Product Manager identifies the need for an exception. They assess the clinical and regulatory risk. If the exception has a potential patient safety impact, the Chief Medical Officer must be notified immediately.
2.  **Documentation:** The requestor creates an Exception Request in MasterControl (Form- QA-089), detailing:
    - Specific section of SOP-CLIN-018 from which deviation is sought.
    - Rationale and business imperative for the exception.
    - Risk Assessment Summary (using Meridian's Risk Matrix in SOP-QA-001).
    - Proposed compensatory control (e.g., "Although LOC is bypassed for this patch, a post-release review will be conducted within 3 days by Dr. Okafor directly.").
3.  **Approval Authority:**
    - **Minor Exceptions** (no patient safety impact, no regulatory filing impact): VP of Clinical AI.
    - **Major Exceptions** (impact on contraindications, IS modification, or EU MDR compliance): VP of Clinical AI + Chief Medical Officer.
4.  **Time-Bound Closure:** No exception is permanent. The exception record must stipulate an expiry date not exceeding 90 days. Failure to close the exception by that date escalates the item to the Chief Quality Officer, who will issue a CAPA under SOP-QA-015.

### 8.3 Escalation Path
If a reviewer and a Product Manager cannot resolve a content dispute (e.g., a Clinical SME believes a population restriction is unsafe, but Product Management wants a broader market claim), the issue is escalated to the Labeling Oversight Committee for binding arbitration. If LOC deadlocks, the Chief Medical Officer holds the final decision authority.

---

## 9. Training Requirements

### 9.1 Role-Based Training Matrix

| Role | Module Name | Code (LMS) | Frequency | Retraining Trigger |
| :--- | :--- | :--- | :--- | :--- |
| All Employees (Read-Only) | *Clinical AI Transparency & Our Promise* | CLIN-TRN-001 | Upon hire, then annually. | N/A |
| Product Managers | *Authoring Best Practices: IFU and UI Strings* | CLIN-TRN-010 | Upon role assignment, then every 2 years. | Launch of a new UI framework or Veeva upgrade. |
| Clinical SMEs | *Writing Contraindications & Limitations for AI* | CLIN-TRN-011 | Annually. | Publication of a new Meridian Clinical Evidence Standard. |
| Medical Writing | *Meridian Style Guide for IFU v4.1* | CLIN-TRN-012 | Every 2 years. | Style guide major version update. |
| Regulatory Affairs | *EU AI Act Labeling Compliance in Practice* | CLIN-TRN-013 | Annually. | Significant regulatory change affecting CE marking or Notified Body procedures. |

### 9.2 Training Effectiveness
Training effectiveness is evaluated at Level 2 (Knowledge) and Level 3 (Performance). For Medical Writing and Clinical SMEs, effectiveness is audited by Quality Assurance via quarterly documentation spot-checks. If a labeling authoring error is traced to a lack of understanding of SOP-CLIN-018, targeted retraining must be completed within 5 business days.

---

## 10. Related Policies and References

### 10.1 Meridian Internal Policies

| SOP ID | Title |
| :--- | :--- |
| SOP-QA-001 | Quality Management System – Document Control and Lifecycle |
| SOP-QA-015 | Corrective and Preventive Action (CAPA) |
| SOP-CLIN-015 | Clinical AI Model Retraining and Lifecycle Management |
| SOP-CLIN-022 | Human-in-the-Loop: Clinical Validation and User Oversight Protocol |
| SOP-REG-105 | Post-Market Surveillance and Vigilance for AI Products |
| SOP-LGL-001 | Records Retention and Legal Hold Policy |
| SOP-SEC-003 | Access Control and Identity Management |
| SOP-FS-104 | HealthPay Financial Score Labeling |
| SOP-ANL-045 | MedInsight Analytics Dashboard Labeling |

### 10.2 External References
- ISO 13485:2016 Medical devices – Quality management systems – Requirements for regulatory purposes.
- ISO 14971:2019 Medical devices – Application of risk management to medical devices.
- FDA Guidance: Clinical Decision Support Software (2022).
- Meridian Clinical Evidence Standard, Version 3.2 (DOC-MED-550).

### 10.3 Document Forms and Templates
- **DOC-CLIN-018-A:** Labeling Planning Checklist.
- **DOC-CLIN-018-B:** IFU Full Document Template (MS Word).
- **DOC-CLIN-018-C:** `ui_labels.json` Technical Schema and Dictionary.
- **Form-QA-089:** Exception / Deviation Request.

---

## 11. Revision History

| Version | Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 3.9 | 2025-01-17 | Dr. Aisha Okafor | Periodic review update. Added Section 5.3.2 acknowledgment flag requirements for high-risk alerts. Updated roles table to reflect new Medical Writing vendor oversight. Minor template typographical corrections. |
| 3.8 | 2024-10-02 | Dr. Aisha Okafor | Updated Section 7.1 KPIs: changed Sync Latency threshold from P95 < 4 hours to P95 < 45 min. Expanded Section 8.2 Exception Procedure with CAPA escalation link to SOP-QA-015. |
| 3.7 | 2024-07-15 | Dr. Aisha Okafor | Major Update: Full transition of labeling lifecycle tracking from MasterControl Forms to Veeva Vault PromoMats. Section 5 rewritten to reflect Veeva workflows. Added Section 5.5 LOC formal voting procedure. |
| 3.6 | 2024-04-08 | Dr. Aisha Okafor | Minor Update: Updated IFU Template to incorporate Health Canada MDL language requirements. Added Section 6.1 Contentful CMS integrity check procedure. Effective date baseline for current QMS. |
| 3.5 | 2023-11-20 | Dr. Priya Patel (Acting Owner) | Interim Revision: Emergency addition of Section 5.6 urgent safety labeling procedure post-sepsis model field corrective action. Clarified CMO authority. |
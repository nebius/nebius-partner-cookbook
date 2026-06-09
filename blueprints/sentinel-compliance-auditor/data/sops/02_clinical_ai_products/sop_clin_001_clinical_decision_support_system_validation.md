---
sop_id: "SOP-CLIN-001"
title: "Clinical Decision Support System Validation"
business_unit: "Clinical AI Products"
version: "2.6"
effective_date: "2025-03-06"
last_reviewed: "2026-09-10"
next_review: "2027-03-07"
owner: "Dr. Aisha Okafor, VP of Clinical AI Products"
approver: "Dr. Priya Patel, Chief Medical Officer"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "HIPAA"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: Clinical Decision Support System Validation

**SOP ID:** SOP-CLIN-001
**Version:** 2.6
**Effective Date:** 2025-03-06

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, methodology, and governance for the clinical, technical, and operational validation of all Clinical Decision Support Systems (CDSS) developed, deployed, or maintained by the Clinical AI Products business unit of Meridian Health Technologies, Inc. The purpose is to ensure that every CDSS algorithm and its associated software implementation are safe, effective, clinically meaningful, and compliant with applicable regulatory obligations before clinical deployment and continuously thereafter. This SOP operationalizes Meridian’s commitment to patient safety and evidence-based medicine within the context of machine learning systems.

### 1.2 Scope

This SOP applies to all machine learning models, statistical algorithms, heuristic rules engines, and composite scoring systems that are intended to influence, inform, or direct clinical care decisions made by a qualified healthcare professional. The scope encompasses:

| **In Scope** | **Out of Scope** |
| :--- | :--- |
| AI-driven patient risk scoring models (e.g., sepsis prediction, 30-day readmission risk). | Pure population health analytics dashboards that do not generate patient-level recommendations (governed by SOP-MED-003). |
| Diagnostic imaging analysis algorithms, including those with FDA 510(k) clearance and CE marking under EU MDR. | Financial credit scoring models for patient financing, which are governed by HealthPay Financial Services under SR 11-7 (SOP-HPF-001). |
| Care gap identification algorithms that generate patient-specific alerts. | Administrative claim denial prediction models. |
| Clinical decision support logic embedded within Meridian’s electronic health record (EHR)-integrated platform, "Meridian ClinicalIQ." | Internal research prototypes that have not been promoted to a production release track. |
| Any third-party or licensed algorithm integrated into the Clinical AI Products portfolio. | General-purpose large language models (LLMs) not fine-tuned for a specific clinical task. |

### 1.3 Applicability

All personnel within the Clinical AI Products business unit, the Clinical Affairs department, the Data Science & Machine Learning Engineering group, the Quality Assurance (QA) team, and the Regulatory Affairs department are bound by the procedures herein. This SOP also applies to any contractor or third-party vendor who contributes to the development, labeling, or performance assessment of a CDSS.

---

## 2. Definitions and Acronyms

### 2.1 Acronyms

| Acronym | Definition |
| :--- | :--- |
| **AE** | Adverse Event |
| **AUC** | Area Under the Receiver Operating Characteristic Curve |
| **AUPRC** | Area Under the Precision-Recall Curve |
| **CDSS** | Clinical Decision Support System |
| **CRO** | Contract Research Organization |
| **CAB** | Clinical Advisory Board |
| **CMO** | Chief Medical Officer (Dr. Priya Patel) |
| **FDA** | U.S. Food and Drug Administration |
| **FMEA** | Failure Mode and Effects Analysis |
| **GDPR** | General Data Protection Regulation (EU) |
| **IRB** | Institutional Review Board |
| **MDR** | Medical Device Regulation (EU) 2017/745 |
| **NPV** | Negative Predictive Value |
| **PHI** | Protected Health Information |
| **PPV** | Positive Predictive Value |
| **QMS** | Quality Management System |
| **ROC** | Receiver Operating Characteristic |
| **RCA** | Root Cause Analysis |
| **SAE** | Serious Adverse Event |
| **SOTA** | State-of-the-Art |
| **SOP** | Standard Operating Procedure |
| **VP** | Vice President |

### 2.2 Definitions

- **Clinical Endpoint:** A precisely defined, clinically meaningful characteristic or variable that reflects how a patient feels, functions, or survives. For a CDSS, the clinical endpoint is the downstream health outcome the algorithm is intended to predict, diagnose, or influence (e.g., 7-day mortality, confirmed diagnosis of acute intracranial hemorrhage).
- **Gold Standard Comparison:** The process of comparing the CDSS output against a reference standard that is accepted as the best available method for establishing the ground truth. The Gold Standard must be prospectively defined in the validation protocol.
- **Independent Test Set:** A dataset, temporally or geographically distinct from the training data, that is locked down prior to the final validation run and is used to generate the primary performance results for the validation report. No model retraining or hyperparameter tuning is permitted after the Test Set has been accessed.
- **Performance Benchmark:** A pre-defined, quantitative minimum performance threshold that must be met or exceeded for an individual metric. For example, a sensitivity benchmark for a diagnostic algorithm might be set at > 0.95 with a lower bound of the 95% confidence interval > 0.90.
- **Real-World Evidence (RWE):** Data regarding the usage and potential benefits or risks of a CDSS derived from analysis of real-world data (RWD) sources such as electronic health records, claims databases, and patient registries, collected during post-deployment surveillance.
- **Silent Trial:** A prospective, live-deployment methodology where the CDSS executes and records its recommendations in the background without displaying them to the clinician, while clinical outcomes are concurrently recorded. This enables a direct comparison between CDSS recommendations and actual clinician decisions without introducing algorithmic bias during the evaluation.

---

## 3. Roles and Responsibilities

The following responsibility assignment matrix (RACI: Responsible, Accountable, Consulted, Informed) defines the governance for CDSS validation activities.

| Role | Responsibility in Validation | RACI |
| :--- | :--- | :--- |
| **VP of Clinical AI Products (Dr. Aisha Okafor)** | Ultimate ownership of the Validation Master Plan; Approver of all Validation Reports prior to CMO sign-off; Resource allocation for validation programs. | Accountable |
| **Chief Medical Officer (Dr. Priya Patel)** | Final clinical approval of all CDSS for human use; Chairs Safety Review Board; Primary liaison to clinical key opinion leaders. | Accountable, Approver |
| **Director of Clinical Validation** | Author and executor of the Validation Master Plan; Operational oversight of all pre-deployment clinical studies; Co-author of all validation reports. | Responsible |
| **Lead Data Scientist (Assigned per CDSS)** | Technical execution of the Gold Standard comparison and statistical analysis; generation of all performance figures and tables; ensures reproducibility of results. | Responsible |
| **Clinical Data Operations Manager** | Provisioning of de-identified clinical data sets for validation; custody of the Independent Test Set lockbox; data quality assurance. | Responsible |
| **Biostatistician** | Independent review of the statistical analysis plan (SAP); verification of all reported confidence intervals and p-values; ensures statistical rigor. | Consulted |
| **Regulatory Affairs Specialist** | Advises on the regulatory pathway (FDA, EU MDR, SaMD framework); translates regulatory requirements into validation plan requirements; manages QMS documentation links. | Consulted |
| **Head of Information Security (CISO)** | Verifies that the data processing environment meets "HIPAA & GDPR" technical safeguards; Signs off on data governance controls. | Informed |

---

## 4. Policy Statements

Meridian Health Technologies, Inc. commits to the following foundational policies governing CDSS Validation:

1.  **Clinical Primacy:** A CDSS shall not be deployed for clinical use until an independent, multi-stakeholder validation report demonstrates, with robust statistical certainty, that its performance meets or exceeds all pre-defined clinical endpoints and performance benchmarks. The CDSS is an advisory tool and must not replace the clinical judgment of a qualified healthcare professional.
2.  **Data Integrity:** All validation activities must be conducted on data sets whose provenance, quality, and integrity are fully documented. The independent test set must be locked and its seal intact before the final validation execution begins.
3.  **Transparency:** Performance characteristics, including sensitivity, specificity, PPV, NPV, and known limitations regarding confounding variables and demographic subgroups, must be clearly documented in the product's Instructions for Use (IFU) and accompanying technical documentation.
4.  **Continuous Validation:** Validation is not a one-time event. A comprehensive post-deployment surveillance plan, including silent trials and RWE analysis, must be active throughout the product lifecycle. Any performance drift below benchmark triggers an immediate escalation under Section 8.
5.  **Fairness and Generalizability:** Validation must be conducted across demographically diverse cohorts to assess for performance disparities. We commit to the principles of the NIST AI Risk Management Framework (AI RMF) to govern the lifecycle of our clinical AI.
6.  **Regulatory Alignment:** All validation activities shall be conducted in alignment with EU AI Act requirements for high-risk AI systems, relevant harmonized standards, and the documentation principles of the NIST AI RMF.

---

## 5. Detailed Procedures

This section outlines the end-to-end procedural workflow, from defining the validation blueprint to the final approval gate.

### 5.1 Validation Study Blueprint Definition (Phase 0)

At least 90 days before the anticipated validation start date, the Director of Clinical Validation must convene a Study Design Workshop. The mandatory outputs of this workshop are:

- **Clinical Endpoint Definition Document (CEDD):** A formal document defining the primary and secondary clinical endpoints. This document must be signed off by the Chief Medical Officer (CMO) and the Biostatistician.
- **Statistical Analysis Plan (SAP):** A comprehensive plan detailing the statistical tests, sample size justifications (power analysis, >80% power), methods for handling missing data, and corrections for multiplicity.
- **Gold Standard Annotation Guide (GSAG):** A detailed, operational manual for how the ground truth will be established. If a panel of three independent clinical experts is used for adjudication (e.g., for diagnostic algorithms), a majority-vote or consensus methodology must be specified.

**Template: Clinical Endpoint SMART Criteria**
Each primary endpoint must conform to the following:
- **Specific:** Clearly defines the target condition (e.g., "Acute ischemic stroke visible on non-contrast CT").
- **Measurable:** Outlines the measurement methodology (e.g., "Area under the ROC Curve for pixel-level lesion segmentation").
- **Actionable:** The CDSS output is directly linked to a definable clinical action (e.g., "Prioritization on the radiologist's worklist").
- **Realistic:** The benchmark is based on a literature review of current SOTA clinician performance.
- **Time-bound:** Specifies the timeframe for the prediction window (e.g., "Prediction of onset within the subsequent 6 hours").

### 5.2 Data Curation and Lockbox Procedure (Phase 1)

The Clinical Data Operations Manager is the point-of-contact for the data lockbox. The procedure is as follows:
1.  **Data Acquisition:** Source data is extracted from the Meridian Data Lake (M-DL) based on a pre-approved protocol that defines inclusion/exclusion criteria.
2.  **De-identification:** All data must undergo a PHI scrubbing process using the Meridian De-ID Pipeline v4.2. A post-scrub audit report must be generated and reviewed by the Data Privacy Officer.
3.  **Hold-out Set Creation:** The scrubbed data is randomly partitioned into a "Historical Training Set" (accessible to the ML team for internal iteration) and a "Prospective Validation Set." The latter is stored in a read-only, access-controlled S3 bucket (`s3://meridian-clinical-aq/validation-lockboxes/[CDSS-NAME]/`). Access logging is enabled.
4.  **Lockbox Ceremony:** A formal "Lockbox Ceremony" is conducted. The Director of Clinical Validation, Biostatistician, and the CISO confirm the integrity of the data by verifying the SHA-256 hash of the locked dataset. The hash is entered into the Meridian Asset Registry.

### 5.3 Gold Standard Comparison: Clinical Reader Study (Phase 2)

For all diagnostic and screening CDSS, a blinded, multi-reader, multi-case (MRMC) reader study is the mandatory methodology for establishing the Gold Standard against which the algorithm will be compared.

**Procedure:**
1.  **Reader Selection:** Three board-certified clinical specialists, not Meridian employees, are engaged as independent readers from a pre-approved CRO. Reader qualifications must be documented.
2.  **Blinding:** Readers are blinded to all clinical outcomes, original reports, and the output of the CDSS. They review only the de-identified source data (e.g., images, structured lab panels).
3.  **Anchoring:** For each case in the `Prospective Validation Set`, each reader records their diagnostic assessment using a standardized, structured reporting template on the Meridian Annotation Platform (MAP).
4.  **Panel Adjudication:** Where all three readers are concordant, their assessment becomes the Gold Standard label. Discordant cases are adjudicated in a virtual panel session chaired by the CMO or delegate. The session is audio-recorded and the transcript is archived. The final label is the Adjudicated Gold Standard.
5.  **Data Preparation:** Adjudicated labels are locked and delivered to the Lead Data Scientist.

### 5.4 Algorithmic Performance Execution (Phase 3)

This is the execution phase where the CDSS is run against the lockbox. The Lead Data Scientist executes the following steps strictly:

1.  **Code Freeze:** The production branch of the CDSS repository (e.g., `clinicaliq/ sepsis-predictor v3.1.0_prod`) is tagged and frozen in a read-only state in Bitbucket.
2.  **Containerization:** A Docker container is built from the frozen codebase, including the exact pre-trained model weights file. The container's SHA-256 digest is recorded and entered into the validation report.
3.  **Validation Run:** The container is executed against the locked `Prospective Validation Set` in a clean-room AWS environment (`EC2 instance: validation-runner`) that has no outbound internet access. Output scores and predictions are logged to an append-only S3 log bucket (`s3://meridian-audit-logs/clinical-validation/[CDSS-NAME]/[YYYY-MM-DD]/`).
4.  **Output Lock:** The raw output file is immediately locked and handed off to the Biostatistician for independent analysis.

### 5.5 Statistical Analysis and Report Generation (Phase 4)

The Biostatistician independently analyzes the raw CDSS output against the Adjudicated Gold Standard labels.
- **Performance Benchmarks:** The CDSS must meet *all* pre-defined benchmarks. For example, a sepsis prediction CDSS might have:
    - **Sensitivity:** > 0.85 (with a 95% CI lower bound > 0.80)
    - **Specificity:** > 0.80 (with a 95% CI lower bound > 0.75)
    - **Lead Time:** Median alert generation precedes clinical onset by at least 4 hours.
    - **Calibration:** Brier score < 0.10 with a calibration-in-the-large < 0.1.
- **Sensitivity Analysis:** Evaluation across key demographic subgroups (age, sex, race, geographic strata) must be performed. If performance degrades for a specific subgroup (absolute difference in AUC > 0.05), this must be prominently flagged and investigated as a potential systematic bias.
- **Technical Documentation:** The output of this phase is the Final Validation Report (FVR), which includes all Annex IV documentation elements for EU AI Act compliance.

### 5.6 Final Sign-Off and Gate Release (Phase 5)

The FVR and a "Deployment Readiness Checklist" must be approved in sequence:
1.  Director of Clinical Validation (Responsible)
2.  Biostatistician (Statistical Validity Sign-off)
3.  VP of Clinical AI Products (Business Owner Approval)
4.  Chief Medical Officer (Final Clinical Authorization)

Upon CMO approval, a signed, non-repudiable artifact is stored in the Meridian Document Management System (MDMS), and the CDSS is approved for clinical deployment by the DevOps team. No CDSS shall be released to a production branch without this artifact.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control | Implementation | Purpose |
| :--- | :--- | :--- |
| **Data Lockbox Integrity** | SHA-256 hashing; Immutable S3 bucket logging via AWS CloudTrail. | Ensures that the Independent Test Set has not been tampered with post-lockbox ceremony. |
| **Container Integrity** | Docker image signing using Cosign; SHA-256 digest stored in the immudb artifact registry. | Guarantees that the exact, frozen model binary is what was validated and what gets deployed. |
| **Environment Segregation** | Validation runs are executed in an isolated AWS sub-account (`prod-validation`) with no network connectivity to the production EHR-integrated environment (`prod-ehr`). | Prevents data leakage between training/validation and live clinical environments. |
| **Access Logs** | All access to the lockbox S3 bucket and the validation-runner EC2 instance is logged to `s3://meridian-audit-logs`. Access is restricted by IAM roles to only the Lead Data Scientist and Biostatistician during the active run phase. | Provides an immutable audit trail for regulatory review. |
| **PHI De-ID** | Meridian De-ID Pipeline v4.2, achieving strict statistical anonymization under GDPR standards as verified by the Data Privacy Officer. | Ensures PHI is not inadvertently processed where it is not needed, aligning with data minimization principles. |

### 6.2 Administrative Controls

- **Access Review:** Quarterly review of all accounts with `ReadWrite` permissions to `meridian-clinical-aq` AWS Organisations Service Control Policies (SCPs). Unauthorized access triggers an incident response process as per SOP-CLIN-003.
- **Separation of Duties:** The Lead Data Scientist who executes the validation run must not be the Biostatistician who analyzes the output. The Biostatistician reports directly to the VP of Clinical AI, not to the Lead Data Scientist's line manager.
- **Vendor Risk Management:** Any CRO or external clinical reader panel is subject to an annual SOC 2 Type II review and a HIPAA Business Associate Agreement (BAA). Their annotation platform must also meet our data governance standards.

---

## 7. Monitoring, Metrics, and Reporting

Post-deployment, the CDSS is in a state of continuous surveillance.

### 7.1 Post-Market Monitoring Plan

A Post-Market Clinical Follow-up (PMCF) plan, or its equivalent for a non-device CDSS, must be filed within 30 days of deployment. This plan details the silent trial protocol and real-world evidence gathering. Metrics are tracked on the Clinical AI Product Dashboard.

### 7.2 Key Performance Indicators (KPIs)

| Metric | Definition | Target | Alert Limit |
| :--- | :--- | :--- | :--- |
| **Algorithmic Drift** | Deviation of the in-production CDSS output distribution from the lockbox test set distribution, measured by Population Stability Index (PSI). | PSI < 0.10 | PSI > 0.25 triggers an automatic alert to the Clinical Engineering SWAT team. |
| **Clinician Override Rate** | Percentage of CDSS recommendations that are acknowledged but not acted upon by the clinician. Monitored by CDSS and site. | < 20% | > 50% site-specific override rate triggers a targeted field service visit to assess usability or local workflow integration. |
| **Unanticipated AEs** | Rate of patient adverse events where a CDSS-related failure was a contributing factor. | 0 | Any unanticipated AE triggers a full-blown RCA under SOP-CLIN-004. |
| **Bias & Fairness** | Monthly evaluation of the model's F1 score parity across protected demographic subgroups (race, sex, geographic). | F1 difference < 0.05 | An F1 difference > 0.05 across any subgroup initiates an immediate re-validation study sub-analysis. |

### 7.3 Reporting Cadence

- **Monthly:** Automated PSI and override rate report to the Product Manager and Director of Clinical Validation.
- **Quarterly:** Comprehensive Post-Market Surveillance Report, including a fairness and bias review, presented to the Clinical Advisory Board (CAB).
- **Annually:** Complete re-validation or equivalency study, the formal output of which triggers the next document review cycle for this SOP.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Handling

Any request for a deviation from the procedures in this SOP must be formally documented using the `CDSS-Validation-Exception-Request` form in the Meridian GRC Portal. The request must detail:
- The specific procedural step for which deviation is sought.
- A robust, evidence-based rationale, including compensating controls.
- An assessment of any resultant safety or regulatory risk.

**Exception Approval Matrix:**

| Risk Level | Approving Authority |
| :--- | :--- |
| Low (e.g., minor documentation template change) | Director of Clinical Validation |
| Medium (e.g., using a modified SAP after lockbox ceremony) | VP of Clinical AI Products |
| High (e.g., deploying a model that missed a secondary performance benchmark) | Chief Medical Officer (CMO) |

No exception may proceed if the CMO determines it presents an unacceptable clinical risk.

### 8.2 Escalation Procedure

The escalation path for critical validation failures or post-deployment safety events is:
1.  **Immediate Triage:** The discovering party (Data Scientist, Clinical Lead) immediately places a 24/7 page to the VP of Clinical AI Products and the Director of Clinical Validation.
2.  **Emergency CAB:** Within 4 hours, the CMO must be briefed. Within 24 hours, an emergency Clinical Advisory Board meeting is convened.
3.  **Immediate Safety Action:** The CAB has the authority to recommend to the CMO to disable a specific CDSS feature flag, take a site offline, or issue an urgent field safety notice. The CMO's decision is final and executable by the on-call SRE team.
4.  **Incident Retrospective:** A formal RCA must be completed within 14 days. Findings are reported to regulatory bodies by the Regulatory Affairs department. A data breach impacting PHI will trigger the Breach Response Protocol, which requires prompt notification to the relevant authorities in accordance with applicable timelines.

---

## 9. Training Requirements

All personnel listed in Section 3 must complete the following training prior to commencing any validation activity.

| Training Module Code | Title | Description | Frequency | Assigned Role |
| :--- | :--- | :--- | :--- | :--- |
| **T-CLIN-001** | SOP-CLIN-001 Proficiency | A role-specific deep dive on the procedures of this SOP. Must pass an end-of-module quiz with 100% accuracy. | Upon assignment; Annually thereafter. | All Section 3 Roles |
| **T-REG-005** | AI Regulation & Safety | Covers EU AI Act, NIST AI RMF, FDA SaMD guidance, and Meridian's ethical AI principles. | Upon assignment; Annually thereafter. | All Section 3 Roles |
| **T-DATA-002** | Advanced PHI & Data Governance | Covers the practical steps of de-identification, data lockbox procedure, and compliance with data use agreements. | Annually | Clinical Data Ops Manager, Lead Data Scientist, Biostatistician |
| **T-GCP-001** | Good Clinical Practice (GCP) Refresher | Standard GCP training for the conduct of clinical studies and handling of clinical data. | Every 2 years | Director of Clinical Validation, Biostatistician |

Training completion is tracked in the Workday Learning Management System. The VP of Clinical AI Products reviews team compliance monthly. A score of less than 100% on role-critical training locks system access until remediation is complete.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP ID | Title |
| :--- | :--- |
| SOP-CLIN-002 | CDSS Risk Management and FMEA Procedure |
| SOP-CLIN-003 | CDSS Data Governance and Access Control Standard |
| SOP-CLIN-004 | CDSS Post-Market Surveillance and Adverse Event Handling |
| SOP-CLIN-005 | Clinical Algorithm Change Management and Versioning |
| SOP-DS-001 | Model Development and Coding Standard |
| SOP-REG-001 | Regulatory Submission Document Control |
| SOP-IS-001 | Information Security Incident Response Plan |
| SOP-QA-005 | Quality Management System Audit Process |

### 10.2 External Standards and Regulations

- **IEC 62304:** Medical device software — Software life cycle processes.
- **ISO 13485:2016:** Medical devices — Quality management systems.
- **EU AI Act:** Regulation (EU) 2024/1689, specifically Title III Chapter 5 for high-risk AI systems. Our QMS is intended to align with Article 17 requirements, and technical documentation is structured to address the elements detailed in our internal template.
- **EU MDR 2017/745:** For CDSS products classified as medical devices.
- **NIST AI RMF 1.0:** AI Risk Management Framework. We utilize this framework to map and govern our AI portfolio, actively working to inventory all high-risk systems and profile their risk impacts.
- **HIPAA Privacy and Security Rules:** 45 CFR Part 160 and Subparts A and E of Part 164.

---

## 11. Revision History

| Version | Date | Author | Description of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2021-11-15 | Dr. A. Okafor | Initial release. Covered internal retrospective validation only. |
| 1.1 | 2022-05-22 | Dr. A. Okafor | Minor revision. Clarified data de-identification requirements post-audit. |
| 2.0 | 2023-07-10 | M. Chen (Reg. Affairs) | Major revision. Aligned with new EU MDR requirements; Introduced Lockbox Ceremony and MRMC reader study methodology. |
| 2.4 | 2024-04-14 | J. Smith (Clin. Ops) | Introduced silent trial methodology and post-market surveillance KPIs. |
| 2.5 | 2024-10-01 | Dr. A. Okafor | Added NIST AI RMF references and fairness metrics; Updated container signing procedure. |
| 2.6 | 2025-03-06 | Dr. A. Okafor | Refined EU AI Act documentation references; Updated escalation and breach notification language; Added Bias & Fairness to quarterly CAB review. |
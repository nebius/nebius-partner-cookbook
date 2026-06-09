---
sop_id: "SOP-CLIN-010"
title: "Medical Imaging AI Pipeline"
business_unit: "Clinical AI Products"
version: "5.4"
effective_date: "2024-09-11"
last_reviewed: "2025-08-19"
next_review: "2026-02-24"
owner: "Dr. Aisha Okafor, VP of Clinical AI Products"
approver: "Dr. Priya Patel, Chief Medical Officer"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "HIPAA"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: Medical Imaging AI Pipeline
**SOP-CLIN-010 | Version 5.4**

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the standardized end-to-end workflow for the ingestion, preprocessing, AI inference, clinical review, and reporting of medical imaging studies processed through the Meridian Clinical AI Platform. The objective of this document is to ensure consistent, secure, and auditable handling of DICOM imaging data while maintaining operational reliability of the inference pipeline and the integrity of clinical outputs delivered to radiologists and ordering providers.

### 1.2 Scope
This SOP applies to all imaging modalities processed through the Meridian Clinical AI Platform, including but not limited to:

| Modality | AI Model(s) | Clinical Application | Deployment Status |
|---|---|---|---|
| Chest X-Ray (CXR) | CXR-Pneumonia-v3, CXR-Nodule-v2 | Pneumonia detection, pulmonary nodule flagging | Production (340+ sites) |
| CT Head | CTH-Stroke-v4, CTH-Hemorrhage-v2 | Acute intracranial hemorrhage detection, large vessel occlusion screening | Production |
| Mammography | MAMM-Mass-v3, MAMM-Calc-v2 | Breast mass detection, microcalcification analysis | Production (FDA 510(k) cleared) |
| MRI Brain | MRI-Brain-Tumor-v2 | Brain tumor segmentation and volumetry | Limited Production (EU MDR CE marked) |
| CT Chest | CTC-PE-v3 | Pulmonary embolism detection | Production |

**In-Scope:**
- All DICOM-compliant imaging studies submitted to the Meridian SaaS Platform
- Image preprocessing and quality assurance workflows
- AI model inference execution and confidence scoring
- Radiologist review queue management and report generation
- All personnel involved in the design, deployment, monitoring, or use of the imaging AI pipeline

**Out-of-Scope:**
- Non-imaging clinical decision support modules (refer to SOP-CLIN-015)
- HealthPay Financial Services processing (refer to SOP-FIN-001 through SOP-FIN-045)
- MedInsight Analytics population health pipelines (refer to SOP-ANL-020)
- Raw infrastructure operations (refer to SOP-IT-100)

### 1.3 Target Audience
This SOP applies to the following Meridian Health Technologies personnel:
- Clinical AI Product team members (engineers, data scientists, product managers)
- Radiologist reviewers and clinical workflow specialists
- Customer Operations team members supporting imaging AI deployments
- IT Operations personnel maintaining pipeline infrastructure
- Compliance and Quality Assurance teams
- Any contractor or third party granted access to the imaging AI pipeline

### 1.4 Distribution
This document is classified as **Internal**. Distribution is restricted to Meridian employees and authorized contractors with a legitimate business need. The authoritative version is maintained in the Meridian Policy Repository (Confluence space: CLIN-POLICIES). Printed copies are uncontrolled.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **AI Inference** | The process by which a trained machine learning model generates predictions or classifications on new input data. In the context of this SOP, inference refers to model execution on DICOM imaging studies to produce clinical findings. |
| **Confidence Score** | A numerical value (0.0–1.0) output by the AI model indicating the estimated probability that a detected finding is present. This is not a clinical probability and should not be interpreted as diagnostic certainty. |
| **Critical Finding** | An AI-detected abnormality that, per clinical protocol, requires immediate radiologist attention due to potential life-threatening implications (e.g., tension pneumothorax, large intracranial hemorrhage). |
| **DICOM** | Digital Imaging and Communications in Medicine — the international standard for medical imaging and related information. All imaging studies processed by the pipeline must conform to DICOM 3.0 or later. |
| **Ground Truth** | The clinically validated diagnosis or annotation used as the reference standard for model training and performance evaluation. Ground truth is established by board-certified radiologists. |
| **Inference Latency** | The elapsed time measured from successful DICOM study ingestion to the generation of AI findings available in the review queue. Measured in seconds. |
| **Model Drift** | Degradation of model performance over time due to changes in input data distributions, population characteristics, imaging equipment, or clinical practices. |
| **Override** | A radiologist's action to reject, modify, or replace an AI-generated finding. All overrides are logged with timestamp, user identity, and reason code. |
| **PHI** | Protected Health Information as defined by the HIPAA Privacy Rule (45 CFR §160.103). Includes any information in the DICOM header or pixel data that could identify an individual patient. |
| **Radiologist Review Queue** | The prioritized worklist of AI-processed studies awaiting radiologist verification, annotation, and report approval within the Meridian Clinical AI Platform interface. |
| **Study Completeness** | A binary determination of whether a submitted DICOM study contains all required series, slices, and metadata elements necessary for AI inference. Incomplete studies are rejected prior to preprocessing. |
| **Validated Model** | An AI model that has completed Meridian's internal Model Validation Protocol and received approval from the VP of Clinical AI Products and Chief Medical Officer for clinical deployment. |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| AE | Application Entity (DICOM networking term) |
| AI | Artificial Intelligence |
| AUC | Area Under the Receiver Operating Characteristic Curve |
| BAA | Business Associate Agreement |
| CI/CD | Continuous Integration / Continuous Deployment |
| CMO | Chief Medical Officer |
| DICOM | Digital Imaging and Communications in Medicine |
| DLP | Data Loss Prevention |
| FN | False Negative |
| FP | False Positive |
| GDPR | General Data Protection Regulation |
| HIPAA | Health Insurance Portability and Accountability Act |
| HL7 | Health Level Seven International |
| KMS | Key Management Service |
| ML | Machine Learning |
| MRN | Medical Record Number |
| MTBF | Mean Time Between Failures |
| MTTR | Mean Time to Recovery |
| NIST | National Institute of Standards and Technology |
| PACS | Picture Archiving and Communication System |
| PHI | Protected Health Information |
| QA | Quality Assurance |
| RTO | Recovery Time Objective |
| SLA | Service Level Agreement |
| SOC | System and Organization Controls |
| SOP | Standard Operating Procedure |
| TN | True Negative |
| TP | True Positive |
| VPC | Virtual Private Cloud |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix

| Role | Pipeline Design | Model Validation | Inference Operations | Clinical Review | Incident Response | Exception Approval |
|---|---|---|---|---|---|---|
| **VP of Clinical AI Products** (Dr. Aisha Okafor) | A | A | R | I | R | A |
| **Chief Medical Officer** (Dr. Priya Patel) | C | A | I | A | I | A |
| **Chief AI Architect** | R | R | A | I | R | C |
| **Lead ML Engineer – Imaging** | R | R | R | C | R | C |
| **Clinical Workflow Lead** | C | C | I | R | C | I |
| **Radiologist Reviewer** | I | I | I | R | I | I |
| **Director of Clinical Quality** | C | R | I | A | R | R |
| **Customer Operations Manager** | I | I | C | I | R | I |
| **Site Reliability Engineering Lead** | I | C | A | I | A | I |
| **Compliance Officer** | C | C | I | I | I | R |

**Key:**
- **R** = Responsible (performs the work)
- **A** = Accountable (approves the work; single-point accountability)
- **C** = Consulted (provides input before the work)
- **I** = Informed (notified after the decision or action)

### 3.2 Detailed Role Descriptions

**3.2.1 VP of Clinical AI Products**
Dr. Aisha Okafor holds overall accountability for the imaging AI pipeline. Responsibilities include: approving new model deployments, authorizing pipeline modifications, reviewing and acting upon pipeline monitoring reports, approving all exceptions to this SOP, and serving as the executive sponsor for pipeline-related corrective actions. Dr. Okafor chairs the weekly Pipeline Operations Review meeting.

**3.2.2 Chief Medical Officer**
Dr. Priya Patel provides clinical governance for all AI-generated findings. Responsibilities include: defining clinical significance thresholds for AI findings, establishing the override reason taxonomy, reviewing aggregate override statistics, and adjudicating clinical disagreements between AI models and radiologist reviewers. Dr. Patel is the final authority on clinical interpretation disputes.

**3.2.3 Chief AI Architect**
The Chief AI Architect is responsible for the technical integrity of the model lifecycle, including training data pipelines, model versioning standards, and inference architecture. They review all model retraining proposals and evaluate technical root causes of model drift events.

**3.2.4 Lead ML Engineer – Imaging**
This senior engineering role owns the day-to-day health of the inference pipeline, including preprocessing logic, model container deployment, inference orchestration, and confidence score calibration. The Lead ML Engineer is the first responder for pipeline alerts and manages the model validation testing protocol.

**3.2.5 Radiologist Reviewer**
Board-certified radiologists (Meridian employees or qualified contractors per SOP-HR-045) who review AI-processed studies, confirm or override findings, annotate ground truth, and approve AI-assisted reports. A minimum of 40 hours of Meridian Clinical AI Platform training is required prior to independent review.

**3.2.6 Director of Clinical Quality**
Responsible for maintaining the quality management framework, overseeing the override tracking system, conducting retrospective concordance analyses, and compiling the quarterly Clinical Quality Report. The Director of Clinical Quality has authority to temporarily suspend a model from the review queue pending investigation.

**3.2.7 Site Reliability Engineering Lead**
Responsible for infrastructure availability, pipeline monitoring dashboards, alerting configuration, and incident management coordination per SOP-IT-200.

---

## 4. Policy Statements

### 4.1 Pipeline Integrity Policy
Meridian Health Technologies is committed to maintaining the integrity of the medical imaging AI pipeline. All DICOM studies submitted for AI processing must pass through the complete preprocessing, inference, and review workflow without unauthorized modification. Any alteration to pipeline logic, model parameters, or configuration files must be documented through the change management process defined in SOP-IT-050.

### 4.2 PHI Minimization Policy
The imaging AI pipeline shall ingest only the minimum DICOM metadata elements necessary for preprocessing, inference, and clinical reporting. DICOM tags not required for pipeline operation shall be stripped during the preprocessing phase. The tag stripping schema is maintained by the Compliance Officer and reviewed quarterly.

### 4.3 Model Version Control Policy
Only validated, version-tagged AI models shall be deployed to the production inference environment. The Model Validation Protocol requires documented performance metrics, review by the Chief AI Architect, and approval by the VP of Clinical AI Products and Chief Medical Officer. Model versions follow Semantic Versioning 2.0.0 convention: MAJOR.MINOR.PATCH.

### 4.4 Review Queue Prioritization Policy
Studies flagged with Critical Findings shall be prioritized to the top of the Radiologist Review Queue with a visual indicator. The target time from Critical Finding flag to radiologist acknowledgment is 5 minutes during business hours (0900–1700 local time at the radiologist's location) and 15 minutes outside of business hours.

### 4.5 Radiologist Oversight Policy
All AI-generated findings must be reviewed, confirmed (or overridden), and annotated by a board-certified radiologist before being included in a final report transmitted to the ordering provider or integrated into the customer's EHR via HL7. Under no circumstances shall AI findings be transmitted directly to a patient, provider, or downstream clinical system without radiologist review.

### 4.6 Data Retention Policy
- **Source DICOM studies:** Retained in the Meridian Clinical AI Platform for 90 days post-processing, then purged. Customers are responsible for retaining original studies in their PACS.
- **AI inference results:** Retained for 7 years as part of the clinical audit trail.
- **Override records:** Retained permanently for model improvement and audit purposes.
- **Pipeline logs:** Retained for 1 year in log aggregation; 3 years in cold storage per SOP-IT-300.

### 4.7 Data Minimization for Model Training
When DICOM studies are used for model training or retraining, PHI shall be removed or obfuscated prior to inclusion in the training corpus. The de-identification procedure is defined in SOP-DATA-015.

---

## 5. Detailed Procedures

### 5.1 DICOM Study Ingestion

**5.1.1 Submission Methods**
The Meridian Clinical AI Platform supports the following DICOM ingestion modalities:

| Method | Use Case | Configuration |
|---|---|---|
| **DICOM C-STORE (SCP)** | Direct PACS integration; customer pushes studies to Meridian AE | Customer configures their PACS to forward studies to `MERIDIAN-AI` AE Title at the customer-specific endpoint provisioned during onboarding |
| **DICOMweb STOW-RS** | Modern web-based submission from VNAs and enterprise imaging platforms | RESTful endpoint: `https://imaging.meridian.ai/v2/studies` |
| **SFTP Batch Upload** | Legacy systems without DICOM networking capability; used for migration and backfill | Provisioned per customer; files must conform to DICOM Part 10 media format |
| **Meridian Gateway Appliance** | On-premises virtual appliance that proxies DICOM traffic, performs local preprocessing, and transmits securely to Meridian Cloud | Deployed at customer site; managed by Meridian IT Operations |

**5.1.2 DICOM Validation Checks**
Upon receipt, each DICOM study is subjected to the following validation checks before being accepted into the pipeline:

### Validation Rules Table

| Check ID | Rule | Failure Action |
|---|---|---|
| VAL-001 | Study Instance UID must be present and conform to DICOM UID format (1.2.840.xxxx) | Reject with error code `ERR-DCM-UID` |
| VAL-002 | Modality tag (0008,0060) must match one of: CR, DX, CT, MR, MG | Reject with error code `ERR-DCM-MOD` |
| VAL-003 | At least one image SOP Instance must be present | Reject with error code `ERR-DCM-EMPTY` |
| VAL-004 | Patient ID (0010,0020) must be present and non-zero-length | Reject with error code `ERR-DCM-PATID` |
| VAL-005 | Study Date (0008,0020) must be present and parseable as a valid date | Flag for manual review; do not auto-reject |
| VAL-006 | File must not contain any private tags without registered private creator blocks | Strip unauthorized private tags; log warning |
| VAL-007 | Transfer Syntax UID must be one of the pipeline's supported syntaxes | Attempt conversion; reject if conversion fails with `ERR-DCM-TS` |

Studies failing any mandatory validation check (Failure Action = "Reject") are not advanced to preprocessing. An error notification is logged to the Pipeline Monitoring Dashboard and, if the submission was via a synchronous DICOM C-STORE, the appropriate DICOM status code is returned to the sender. The Customer Operations team is automatically notified of rejections exceeding 5% of a customer's 24-hour rolling volume.

**5.1.3 PHI Tag Profiling**
During ingestion, the DICOM header is scanned against the PHI Identifier Registry maintained by the Compliance Office. All tags containing PHI are identified and flagged for action during preprocessing (Section 5.2). An inventory of identified PHI-containing tags per study is recorded in the audit log.

---

### 5.2 DICOM Image Preprocessing

Preprocessing is a mandatory, automated pipeline stage that prepares validated DICOM studies for AI inference. Preprocessing must complete successfully for a study to advance to inference.

**5.2.1 Preprocessing Pipeline Stages**

#### Stage 1: DICOM Cleanup and Normalization
The following operations are executed sequentially on each DICOM series:

| Operation | Specification | Purpose |
|---|---|---|
| **Tag Stripping** | Remove all DICOM tags appearing in the `PHI_TAG_STRIP_LIST.json` configuration file | Remove PHI from DICOM headers prior to model ingestion |
| **Series Cleanup** | Remove non-diagnostic series (localizers, dose reports, structured reports, presentation states) based on Series Description and Modality tags | Prevent non-image data from entering the inference pipeline |
| **Window/Level Normalization** | Apply VOI LUT transformation if present; otherwise, apply modality-specific default window settings per `WINDOW_CONFIGS.json` | Standardize pixel intensity representation |
| **Photometric Interpretation Conversion** | Convert MONOCHROME1 to MONOCHROME2; normalize YBR_FULL to RGB for applicable modalities | Ensure consistent pixel data orientation |
| **Orientation Correction** | Apply DICOM Patient Orientation module data to rotate images to standard anatomical view | Prevent orientation-related inference errors |

#### Stage 2: Quality Assurance Gate
After normalization, each series is evaluated through the Image Quality Assessment (IQA) module:

| IQA Metric | Threshold | Failure Handling |
|---|---|---|
| **Signal-to-Noise Ratio (SNR)** | > 18 dB for CT; > 25 dB for CR/DX/MG | Flag for technologist review; do not auto-reject |
| **Contrast-to-Noise Ratio (CNR)** | Modality-specific thresholds in `CNR_THRESHOLDS.json` | Flag if below threshold; log metric |
| **Artifact Detection** | CNN-based detection of motion, metal, and ring artifacts | Score 0–1; studies scoring >0.70 flagged as "Significant Artifact — Radiologist Discretion" |
| **Coverage Completeness** | Required anatomical landmarks detected per study protocol (e.g., apices and costophrenic angles for CXR) | Missing landmarks flagged; inference proceeds but with "Limited Coverage" annotation |
| **Image Compression Assessment** | Detect JPEG compression artifacts if Transfer Syntax is lossy; flag if compression ratio exceeds 10:1 | Flagged for radiologist awareness; model inference proceeds |

Studies flagged during QA are *not* blocked from inference. Rather, a QA metadata block is appended to the study record and displayed to the radiologist during review.

#### Stage 3: Modality-Specific Preprocessing
Additional preprocessing applied based on modality:

**Chest X-Ray:**
- Lung field segmentation using anatomical landmark detection
- Histogram equalization (CLAHE with clip limit 3.0, tile grid size 8×8)
- Image resampling to 1.0 mm isotropic resolution (bilinear interpolation)
- Bit depth normalization to 16-bit

**CT Head:**
- Slice thickness standardization (resample to 3.0 mm if necessary)
- Hounsfield Unit calibration check against air (−1000 HU expected in background)
- Bone and soft tissue window reconstruction
- Skull stripping for brain parenchyma isolation

**Mammography:**
- Breast laterality validation (confirm consistency between DICOM laterality tag and image content)
- Pectoral muscle segmentation
- For processed views (e.g., tomosynthesis), ensure both raw and processed data are retained

**CT Chest (PE):**
- Pulmonary artery contrast enhancement measurement (target ROI: main pulmonary artery; threshold: 250 HU)
- Suboptimal contrast flag if below threshold

#### Stage 4: DICOM Output Assembly
The preprocessed study is assembled into a pipeline-internal DICOM representation that includes:
- Cleaned DICOM headers (PHI removed per Stage 1)
- Normalized pixel data
- IQA metadata block inserted as a private tag in the pipeline's registered private block (0033,10xx)
- Preprocessing provenance record (timestamp, pipeline version, operations applied)

The assembled study is assigned a `Pipeline_Study_UID` for internal tracking. The original `Study Instance UID` is mapped to this internal UID in the lookup database.

---

### 5.3 AI Model Inference Pipeline

**5.3.1 Inference Orchestration**

Upon successful preprocessing, the `Inference Orchestrator` component routes the preprocessed DICOM study to the appropriate model endpoint(s). The Orchestrator implements the logic defined in `MODEL_ROUTING_CONFIG.json`:

| Modality + Clinical Context | Model(s) Routed | Execution Order | GPU Allocation |
|---|---|---|---|
| CXR – General Screening | CXR-Pneumonia-v3, CXR-Nodule-v2 | Parallel | 2× NVIDIA A100 (40GB) |
| CT Head – Acute Neuro | CTH-Stroke-v4, CTH-Hemorrhage-v2 | Parallel | 4× NVIDIA A100 |
| Mammography | MAMM-Mass-v3, MAMM-Calc-v2 | Sequential (Mass → Calc) | 2× NVIDIA A100 |
| CT Chest – PE | CTC-PE-v3 | Single model | 2× NVIDIA A100 |
| MRI Brain | MRI-Brain-Tumor-v2 | Single model | 4× NVIDIA A100 |

Model deployment is managed via the Meridian Model Registry (`mlops.meridian.ai/registry`), which enforces that only validated, version-tagged model containers are available for orchestration. Container hashes are verified at inference time against the registry.

**5.3.2 Confidence Scoring**

Each model outputs findings with an associated confidence score (float, range 0.0–1.0). The threshold for flagging a finding in the radiologist review queue is modality- and model-specific:

| Model | Finding Type | Display Threshold | Critical Threshold |
|---|---|---|---|
| CXR-Pneumonia-v3 | Pneumonia | ≥0.30 | ≥0.75 |
| CXR-Nodule-v2 | Pulmonary Nodule (≤30mm) | ≥0.25 | ≥0.70 (malignancy suspicion) |
| CTH-Stroke-v4 | Large Vessel Occlusion | ≥0.35 | ≥0.80 |
| CTH-Hemorrhage-v2 | Intracranial Hemorrhage | ≥0.30 | ≥0.85 |
| MAMM-Mass-v3 | Breast Mass | ≥0.40 | ≥0.75 |
| CTC-PE-v3 | Pulmonary Embolism | ≥0.25 | ≥0.70 (central PE) |

Findings with confidence scores below the Display Threshold are suppressed and not displayed in the radiologist review queue. They are retained in the inference audit log for model performance tracking.

**5.3.3 Finding Annotation Output**

Each finding produced by the model includes:

| Output Element | Format | Example |
|---|---|---|
| **Finding ID** | UUID v4 | `f47ac10b-58cc-4372-a567-0e02b2c3d479` |
| **Finding Type** | Controlled vocabulary from `FINDING_TYPE_VOCAB.json` | `PULMONARY_NODULE` |
| **Confidence Score** | Float, 0.00–1.00 | `0.72` |
| **Spatial Localization** | DICOM Spatial Coordinates (X, Y, Z) or bounding box | `(125.3, 340.7, 45.2)` with dimensions |
| **Measurement** | mm or HU as appropriate | `Diameter: 14.3 mm` |
| **Segmentation Mask** | Binary mask identifying finding pixels | Stored as DICOM Segmentation object |
| **Model Version** | Semantic version string | `CXR-Nodule-v2.3.1` |
| **Inference Timestamp** | ISO 8601 (UTC) | `2024-09-11T14:38:22Z` |

**5.3.4 Inference Latency SLA**

The Inference Orchestrator is subject to the following latency SLA targets:

| Modality | Maximum Inference Latency (p99) | Measurement Starting Point |
|---|---|---|
| CXR | ≤ 30 seconds | Post-preprocessing handoff to Orchestrator |
| CT Head | ≤ 120 seconds | Post-preprocessing handoff to Orchestrator |
| Mammography | ≤ 90 seconds | Post-preprocessing handoff to Orchestrator |
| CT Chest | ≤ 60 seconds | Post-preprocessing handoff to Orchestrator |
| MRI Brain | ≤ 300 seconds | Post-preprocessing handoff to Orchestrator |

Latency violations exceeding 5% of daily volume trigger an automatic incident notification to Site Reliability Engineering.

---

### 5.4 Radiologist Review Procedure

**5.4.1 Review Queue Access**

Radiologist reviewers access the Meridian Clinical AI Platform review queue through the secure web application (`review.meridian.ai`) with multi-factor authentication and role-based access control enforced per SOP-INFOSEC-020.

The Review Queue displays AI-processed studies sorted by priority tier:

| Priority Tier | Criteria | Visual Indicator | Target Review Time |
|---|---|---|---|
| **Priority 1 – Critical** | Any Critical Finding flag present | Red banner with "STAT" indicator | ≤ 5 minutes |
| **Priority 2 – STAT** | Study marked as STAT by ordering workflow (DICOM tag 0008,0050) | Orange banner | ≤ 30 minutes |
| **Priority 3 – Routine** | All other studies | No indicator | ≤ 4 hours (business hours) |

**5.4.2 Review Workflow Steps**

#### Step 1: Study Selection
The radiologist selects a study from the Review Queue. Upon selection, the study is locked to prevent concurrent review by another radiologist. The lock persists for 60 minutes or until the review is completed or released.

#### Step 2: AI Finding Verification
The interface presents all AI-generated findings for the selected study. For each finding, the radiologist must take one of the following actions:

| Action | Button | Consequence | Required Documentation |
|---|---|---|---|
| **Confirm** | "Confirm Finding" (Green) | Finding is accepted and included in the final report | None (optional comment) |
| **Override – False Positive** | "Override — Not Present" (Red) | Finding is excluded from the final report | Override Reason Code (mandatory) |
| **Override – Modified** | "Modify Finding" (Yellow) | Finding dimensions, classification, or severity modified | Corrected values (mandatory); Reason Code (mandatory) |
| **Add Missed Finding** | "+ Add Finding" (Blue) | New finding documented and included in the final report | Finding type, location, dimensions, comments (mandatory) |

**Override Reason Codes:**

| Code | Description | Category |
|---|---|---|
| OVR-001 | Finding not visible on source images | False Positive |
| OVR-002 | Finding is a known anatomical variant | False Positive |
| OVR-003 | Artifact misinterpreted as finding | False Positive |
| OVR-004 | Correct finding; incorrect dimensions reported | Modified |
| OVR-005 | Correct finding; incorrect classification | Modified |
| OVR-006 | Correct finding; clinically insignificant | Modified |
| OVR-007 | Other — comment required | Either |

#### Step 3: Report Assembly
The Meridian platform assembles a structured report containing:
- Patient demographics and study metadata (pulled from cleaned DICOM headers)
- Study indication and clinical history (if provided)
- Technique description
- **AI-Assisted Findings** section listing all confirmed (and modified) findings with radiologist attribution
- **Comparison** section if prior studies are available
- **Impression** section (free text or structured per radiologist preference)
- Radiologist signature block (digital signature applied via PKI per SOP-INFOSEC-025)

#### Step 4: Report Approval and Transmission
The radiologist clicks "Approve and Transmit." The platform:
1. Applies the radiologist's digital signature
2. Generates a PDF rendering of the report
3. Transmits the report to the customer's configured destination(s) — PACS, EHR via HL7 ORU^R01, fax server
4. Updates the Review Queue status to "Completed"
5. Releases the study lock

**5.4.3 Peer Review Sampling**

Five percent (5%) of completed reviews shall be randomly selected for blinded peer review by a second radiologist. Any discordance between the primary and peer reviewer regarding Critical Findings shall be escalated immediately to the Chief Medical Officer's office for adjudication.

---

### 5.5 Model Update and Retraining Procedure

**5.5.1 Retraining Triggers**

A model retraining cycle may be initiated under any of the following conditions:

| Trigger | Threshold | Authority |
|---|---|---|
| **Scheduled Retraining** | Every 6 months for all production models | VP of Clinical AI Products |
| **Model Drift Alert** | Performance degradation >10% on F1 score measured against ground truth sample | Lead ML Engineer – Imaging |
| **Population Shift** | New customer demographic differs >20% from training population on key covariates | Chief AI Architect |
| **Override Rate Spike** | >15% override rate on confirmed findings sustained for 7 consecutive days | Director of Clinical Quality |

**5.5.2 Retraining Process Overview**

1. **Training Corpus Assembly:** Curate balanced dataset from Pipeline Study Repository, ensuring proportional representation across customer sites, equipment vendors, and demographics.
2. **Ground Truth Annotation:** Board-certified radiologists annotate training studies per the Annotation Protocol. Minimum inter-rater agreement of κ ≥ 0.80 required.
3. **Model Training:** Execute training per model-specific Training Specification maintained in `mlops.meridian.ai/models`.
4. **Validation Testing:** Evaluate candidate model against holdout validation dataset. Model must meet or exceed:
   - AUC ≥ 0.85 for detection models
   - Sensitivity ≥ 0.90 at the operating point (for Critical Finding models)
   - Specificity ≥ 0.70 at the operating point
5. **Clinical Equivalence Testing:** Candidate model must demonstrate non-inferiority to the current production model on clinical endpoints with a non-inferiority margin of Δ = 0.05 on sensitivity.
6. **Approval Gate:** Results presented to VP of Clinical AI Products and Chief Medical Officer. Both signatures required for deployment approval.
7. **Phased Rollout:** New model deployed to 10% of inference traffic for 72 hours; monitored for error rates and latency; then ramped to 100% per deployment runbook DP-CLIN-001.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

**6.1.1 Encryption**
- **Data in Transit:** All DICOM data transmitted between Meridian components and between customers and Meridian shall be encrypted using TLS 1.3 (minimum). DICOM TLS per Supplement 204 shall be configured for direct DICOM C-STORE connections.
- **Data at Rest:** All stored DICOM studies, inference results, and reports shall be encrypted using AES-256-GCM. Encryption keys managed via AWS KMS with automatic rotation every 90 days.

**6.1.2 Access Controls**
- Access to the production inference environment is restricted to authorized members of the Clinical AI Engineering and IT Operations teams.
- AWS IAM policies enforce least-privilege access. Direct access to EC2 instances hosting inference containers requires documented justification and approval by the Lead ML Engineer.
- All access to PHI-bearing systems is logged via AWS CloudTrail with logs forwarded to the centralized SIEM.

**6.1.3 Audit Controls**
Meridian shall maintain an audit trail capturing the following events:

| Event Type | Captured Fields | Retention |
|---|---|---|
| DICOM Study Ingestion | Timestamp, Study Instance UID, Source IP, Submission Method, Validation Result | 7 years |
| PHI Access (any DICOM tag read) | Timestamp, User/Process ID, Tag(s) accessed, Purpose code | 7 years |
| AI Inference Execution | Timestamp, Model ID + Version, Pipeline Study UID, Latency, Findings Generated | 7 years |
| Radiologist Review Actions | Timestamp, Radiologist ID, Study UID, Action Type (Confirm/Override/Add), Override Reason Code | 7 years |
| Administrative Access | Timestamp, User ID, Resource Accessed, Action Performed | 7 years |

### 6.2 Administrative Controls

**6.2.1 Business Associate Agreements**
Meridian Health Technologies shall execute a Business Associate Agreement (BAA) with each customer prior to processing any PHI through the imaging AI pipeline. The standard Meridian BAA template is maintained by the Legal department (document: LEG-BAA-STD-v3.1). BAAs must be fully executed before the Customer Operations team provisions ingestion endpoints.

**6.2.2 Risk Assessment**
An annual risk assessment shall be conducted for the imaging AI pipeline. The assessment shall evaluate technical risks (security vulnerabilities, infrastructure failure modes), operational risks (model drift, pipeline downtime), and clinical risks (systematic model biases, missed Critical Finding rates). Results are documented in the Clinical AI Risk Register (`clops.meridian.ai/risk-register`) and reviewed by the Clinical AI Steering Committee.

**6.2.3 Change Management**
All changes to production pipeline components (model updates, preprocessing modifications, inference infrastructure changes) shall follow the Change Management procedure defined in SOP-IT-050. Emergency changes (e.g., model rollback due to critical failure) may be executed with approval from the Lead ML Engineer and post-hoc notification to the VP of Clinical AI Products within 24 hours.

**6.2.4 Vulnerability Management**
The Clinical AI Engineering team shall scan all pipeline container images for known vulnerabilities prior to production deployment. Critical vulnerabilities (CVSS ≥ 9.0) are deployment-blocking. High vulnerabilities (CVSS 7.0–8.9) must be documented with a remediation plan within 30 days. The container scanning pipeline is maintained per SOP-IT-090.

### 6.3 Physical Controls
Meridian Clinical AI Platform infrastructure is hosted in AWS US-East-1 and EU-Central-1 regions, which provide physical security controls per AWS SOC 1/2/3 reports. Meridian maintains no physical data centers housing imaging pipeline infrastructure.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Pipeline Performance Monitoring

The **Pipeline Monitoring Dashboard** (Grafana instance: `monitoring.meridian.ai/d/clin-ai-pipeline`) provides real-time visibility into the following operational metrics:

| Metric Category | Specific Metrics | Alert Threshold |
|---|---|---|
| **Volume** | Studies ingested per hour (by modality, by customer) | Deviation > 50% from 7-day rolling average triggers alert to Customer Ops |
| **Errors** | Ingestion rejection rate, Preprocessing failure rate, Inference failure rate | Any rate > 5% of hourly volume triggers P2 incident |
| **Latency** | p50, p95, p99 inference latency by modality | p99 exceeding SLA threshold for >5% of trailing 1-hour window triggers P2 incident |
| **Queue Depth** | Number of studies awaiting radiologist review (by priority tier) | >50 Priority 1 studies or >500 total studies triggers staffing alert to Clinical Workflow Lead |
| **Model Health** | Inference error rate per model version; GPU utilization | Inference error rate >2% triggers model-specific investigation |

### 7.2 Clinical Performance Metrics

The **Clinical Quality Dashboard** (`quality.meridian.ai/dashboard/imaging`) reports the following metrics on a 30-day rolling basis:

| Metric | Definition | Reporting Frequency |
|---|---|---|
| **Override Rate by Finding Type** | FP Overrides / Total Findings Flagged | Weekly |
| **Sensitivity by Modality** | TP / (TP + FN) where ground truth is established by peer review or adjudication | Monthly |
| **Specificity by Modality** | TN / (TN + FP) | Monthly |
| **Critical Finding Detection Rate** | Critical Findings detected by AI and confirmed / All Critical Findings identified (AI + human adds) | Monthly |
| **Review Queue Turnaround Time** | Median time from study ingress to report approval; p95 time | Weekly |
| **Inter-Radiologist Agreement** | Cohen's κ for peer-reviewed sample | Monthly |

### 7.3 Reporting Cadence

| Report | Audience | Frequency | Owner |
|---|---|---|---|
| **Pipeline Operations Summary** | VP Clinical AI, Lead ML Engineer, SRE Lead | Weekly (Monday 0900) | Lead ML Engineer |
| **Clinical Quality Report** | CMO, VP Clinical AI, Director of Clinical Quality, Radiologist Reviewers | Monthly (first Friday) | Director of Clinical Quality |
| **Executive Dashboard** | CEO, CTO, CMO, VP Clinical AI, VP Engineering | Monthly | VP Clinical AI |
| **Customer-Facing Uptime Report** | Customer contacts per individual SLA agreements | Monthly (automated) | Customer Operations Manager |
| **Pipeline Performance Review** | Clinical AI Engineering team | Bi-weekly sprint review | Lead ML Engineer |

### 7.4 Key Performance Indicators

| KPI | Target | Measurement Method |
|---|---|---|
| Pipeline Availability | 99.9% uptime (excluding customer-scheduled maintenance) | Prometheus uptime probes; measured monthly |
| Critical Finding Time-to-Review | Median ≤ 3 minutes; p95 ≤ 15 minutes | Review timestamp minus Critical Finding flag timestamp |
| AI-Radiologist Concordance | Sensitivity within 5% of radiologist inter-reader agreement for each modality | Monthly Clinical Quality Report |
| Customer Satisfaction (CSAT) | ≥ 4.2/5.0 quarterly average | Quarterly survey administered by Customer Ops |
| Model Retraining Cadence | Every model retrained within 180 days | Model Registry metadata |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types

| Exception Type | Definition | Approval Authority |
|---|---|---|
| **Technical Exception** | Deviation from prescribed technical procedure (e.g., bypassing a preprocessing step due to incompatibility) | Lead ML Engineer; VP Clinical AI notified within 24 hours |
| **Clinical Exception** | Deviation from radiologist review procedure (e.g., studies reviewed by non-radiologist clinical specialist for specific low-acuity use cases) | Chief Medical Officer |
| **Operational Exception** | Temporary procedural deviation due to incident, maintenance, or capacity constraints | Incident Commander (per SOP-IT-200) during incident; VP Clinical AI post-incident |
| **Policy Exception** | Long-term deviation from any provision of this SOP | VP Clinical AI and Chief Medical Officer jointly |

### 8.2 Exception Request Procedure

1. **Request Initiation:** Requestor completes the Exception Request form in the Meridian Policy Repository (Form ID: FRM-EXCP-001), including:
   - SOP section(s) from which deviation is sought
   - Nature and duration of proposed deviation
   - Justification (technical, clinical, or operational rationale)
   - Risk assessment and proposed compensating controls

2. **Review and Approval/Denial:** The relevant Approval Authority per Section 8.1 reviews the request within 5 business days (or 4 hours for urgent operational exceptions). Approved exceptions receive a unique Exception ID and are documented in the Exception Registry.

3. **Compensating Controls:** All approved exceptions must include documented compensating controls. For example, if a preprocessing QA gate is bypassed, a manual review of those studies by a Clinical Workflow Specialist may substitute.

4. **Expiration:** All exceptions are time-bound. The maximum duration for an exception is 90 days, after which it must be renewed or the deviation must be corrected.

5. **Audit Review:** The Compliance Officer reviews all active exceptions quarterly and reports to the Clinical AI Steering Committee on exceptions that have been renewed more than once.

### 8.3 Escalation Hierarchy

| Level | Escalation Trigger | Escalated To | Response Time |
|---|---|---|---|
| **Level 1** | Pipeline operational issue not resolved within SLA per runbook; review queue backlog exceeding capacity | Lead ML Engineer – Imaging; Clinical Workflow Lead | Within 1 hour of trigger |
| **Level 2** | Issue unresolved at Level 1 within 4 hours; Critical Finding review delayed >30 minutes; model performance degradation affecting clinical outputs | VP Clinical AI Products; Director of Clinical Quality; SRE Lead | Within 4 hours of Level 1 escalation |
| **Level 3** | Patient safety concern; incident declared with potential for patient harm | Chief Medical Officer; CEO; VP Clinical AI Products | Immediately (within 15 minutes of Level 2 escalation) |

### 8.4 Incident Communication
During declared incidents affecting the imaging AI pipeline, communication to affected customers shall follow the Incident Communication Plan (SOP-IT-210). The Customer Operations team is responsible for customer notification within the SLA window defined in each customer's service agreement.

---

## 9. Training Requirements

### 9.1 Required Training

| Training Module | Target Audience | Frequency | Delivery Method |
|---|---|---|---|
| **CT-IMG-001: Imaging AI Pipeline Overview** | All personnel listed in Section 1.3 | Initial (within 30 days of hiring/r ole assignment); refresher every 12 months | On-demand e-learning (LMS) + live Q&A session |
| **CT-IMG-002: Radiologist Review Platform** | Radiologist Reviewers, Clinical Workflow Specialists | Initial; updated training within 30 days of each platform major version release | Hands-on sandbox environment + proctored assessment |
| **CT-IMG-003: DICOM Handling and PHI Protection** | Clinical AI Engineers, Customer Operations, IT Operations | Initial; refresher every 12 months | On-demand e-learning (LMS) with quiz |
| **CT-IMG-004: Emergency Procedure – Critical Finding Escalation** | Radiologist Reviewers, Customer Operations | Initial; refresher every 6 months | Scenario-based simulation (tabletop) |
| **CT-IMG-005: Model Validation Protocol** | Clinical AI Engineers, Data Scientists | Initial; refresher upon major protocol revision | Instructor-led workshop (2 days) |

### 9.2 Training Tracking and Compliance

- The Meridian Learning Management System (`lms.meridian.ai`) tracks all training completion records.
- Managers receive automated notifications when direct reports have overdue training.
- Access to production pipeline systems is automatically suspended for any user with training >30 days past due, until training is completed. Exceptions require VP Clinical AI approval.
- Quarterly training compliance reports are reviewed by the VP of Clinical AI Products and the Director of Clinical Quality.

### 9.3 Competency Assessment

Radiologist Reviewers must undergo annual competency assessment consisting of:
1. **Standardized Test Set:** Review of 50 pre-annotated studies (mix of positive and negative findings across modalities). Required performance: Sensitivity ≥ 0.90 and Specificity ≥ 0.85 compared to reference standard.
2. **Override Rate Monitoring:** Override rates are tracked individually. Radiologists with override rates >2 standard deviations above the peer mean for two consecutive months shall undergo mandatory remediation with the Clinical Workflow Lead.
3. **Peer Review Agreement:** Individual inter-reader agreement scores computed from peer review sampling. Scores below κ = 0.75 trigger a review by the Director of Clinical Quality.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|---|---|---|
| SOP-CLIN-005 | Clinical AI Model Validation Protocol | Model validation procedures referenced in Section 5.5 |
| SOP-CLIN-015 | Non-Imaging Clinical Decision Support Pipeline | Delineates imaging vs. non-imaging AI workflows |
| SOP-DATA-005 | PHI Handling and De-Identification Standards | De-identification requirements for PHI |
| SOP-DATA-015 | Training Data Governance | Data governance for model training corpora |
| SOP-INFOSEC-020 | Identity and Access Management | Authentication and role-based access controls |
| SOP-INFOSEC-025 | Digital Signature and PKI Management | Cryptographic controls for report signing |
| SOP-IT-050 | Change Management | Change management procedures for production systems |
| SOP-IT-090 | Container Security and Vulnerability Management | Container scanning and vulnerability remediation |
| SOP-IT-100 | Infrastructure Operations | Underlying cloud infrastructure management |
| SOP-IT-200 | Incident Management | Incident declaration, response, and communication |
| SOP-IT-210 | Customer Incident Communication | Customer-facing communication during incidents |
| SOP-IT-300 | Log Management and Retention | Logging standards and retention schedules |
| SOP-HR-045 | Contractor Qualification and Onboarding | Requirements for contractor radiologists |
| SOP-ANL-020 | MedInsight Analytics Pipeline | Delineates clinical AI vs. analytics pipelines |
| SOP-FIN-001 | Financial Systems Overview | Non-clinical financial processing |

### 10.2 External Standards and References

| Reference | Applicable Section | Version/Date |
|---|---|---|
| DICOM Standard PS3.1–PS3.20 | Throughout (DICOM handling) | 2024c Edition |
| DICOM Supplement 204 (TLS Security) | Section 5.1.1, 6.1.1 | Final Text (2020) |
| IHE Radiology Technical Framework | Section 5.1 (AI Results integration) | Revision 21.0 |
| HIPAA Privacy Rule (45 CFR Part 160 and Part 164, Subparts A and E) | Sections 4.2, 5.2, 6.1, 6.2 | Current as of 2024 |
| HIPAA Security Rule (45 CFR Part 164, Subpart C) | Sections 6.1, 6.2 | Current as of 2024 |
| AWS Well-Architected Framework – Security Pillar | Section 6 | December 2023 |
| ISO 13485:2016 – Medical Devices Quality Management | Section 9 (Training), Section 10 (Documentation) | 2016 Edition |
| Meridian BAA Standard Template LEG-BAA-STD-v3.1 | Section 6.2.1 | v3.1 (2024-01-22) |

### 10.3 Key Configuration Files

| File | Purpose | Location (Private Git) |
|---|---|---|
| `PHI_TAG_STRIP_LIST.json` | DICOM tags containing PHI to be stripped during preprocessing | `clinical-ai/config/preprocessing/` |
| `WINDOW_CONFIGS.json` | Modality-specific VOI LUT defaults | `clinical-ai/config/preprocessing/` |
| `CNR_THRESHOLDS.json` | Contrast-to-Noise Ratio thresholds per modality | `clinical-ai/config/iqa/` |
| `FINDING_TYPE_VOCAB.json` | Controlled vocabulary for finding types | `clinical-ai/config/vocabularies/` |
| `MODEL_ROUTING_CONFIG.json` | Inference Orchestrator routing rules | `clinical-ai/config/inference/` |

---

## 11. Revision History

| Version | Date | Author | Revision Description | Approver |
|---|---|---|---|---|
| 5.4 | 2024-09-11 | Dr. Aisha Okafor | Full revision: Updated ingestion to support DICOMweb STOW-RS; expanded preprocessing IQA module; added CT Chest PE to scope; updated inference latency SLA to p99; added radiologist competency assessment requirements; updated BA template reference to v3.1 | Dr. Priya Patel |
| 5.3 | 2024-03-15 | Dr. Aisha Okafor | Added SFTP Batch Upload ingestion method; revised override reason codes (split OVR-004 into OVR-004/005/006); added MRI Brain tumor model to Limited Production scope; updated review queue priority tier thresholds; incorporated DICOM Supplement 204 TLS requirements | Dr. Priya Patel |
| 5.2 | 2023-11-08 | James Chen (Lead ML Engineer, at time) | Major revision: introduced PHI tag stripping during preprocessing; added IQA quality assurance gate; migrated model deployment to Model Registry; updated confidence score thresholds per model validation; added Section 5.5 model update procedure; updated encryption to AES-256-GCM | Dr. Aisha Okafor (VP Clinical AI Products; then-Chief AI Architect acting as approver during CMO transition) |
| 5.1 | 2023-06-20 | Sarah Lin (Clinical Workflow Lead, at time) | Minor revision: clarified radiologist review lock duration; added peer review sampling procedure; updated latency SLAs for CT Head; fixed formatting errors in responsibility matrix | Dr. Priya Patel |
| 5.0 | 2023-02-01 | Dr. Aisha Okafor | Major version: restructured document for SOP-CLIN-010 initial release under Clinical AI Products business unit; codified Radiologist Review procedure; established KPI framework; superseded legacy SOP-DEV-045 (Medical Imaging Model Operations) | Dr. Priya Patel |

---

**End of Document | SOP-CLIN-010 | Version 5.4**

*This document is classified as Internal. Unauthorized distribution is prohibited. For questions regarding this SOP, contact the document owner: Dr. Aisha Okafor (a.okaford@meridian.ai).*
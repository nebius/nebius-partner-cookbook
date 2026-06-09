---
sop_id: "SOP-CLIN-015"
title: "Regulatory Submission for AI Medical Devices"
business_unit: "Clinical AI Products"
version: "1.4"
effective_date: "2024-12-17"
last_reviewed: "2025-03-22"
next_review: "2025-09-02"
owner: "Dr. Aisha Okafor, VP of Clinical AI Products"
approver: "Dr. Priya Patel, Chief Medical Officer"
classification: "Internal"
regulations:
  - "EU AI Act"
status: "Active"
---

# Standard Operating Procedure: Regulatory Submission for AI Medical Devices

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the standardized framework, processes, and governance for the preparation, submission, and lifecycle maintenance of regulatory filings for Meridian Health Technologies' Clinical AI Platform products. The purpose is to ensure that all AI-enabled medical devices achieve and maintain timely, high-quality regulatory clearances and approvals in target markets, with specific focus on U.S. Food and Drug Administration (FDA) 510(k) premarket notifications and European Union CE marking under the Medical Device Regulation (EU MDR 2017/745) and the EU Artificial Intelligence Act (Regulation 2024/1689).

### 1.2 Scope
This SOP applies to all Clinical AI Products developed or marketed by Meridian Health Technologies, Inc., including:
- Diagnostic imaging analysis algorithms (e.g., chest X-ray pneumothorax detection, mammography lesion characterization)
- Patient risk scoring models deployed as medical devices (e.g., sepsis early warning score, 30-day hospital readmission prediction)
- Clinical decision support (CDS) software that provides diagnostic or therapeutic recommendations
- Adverse event prediction systems intended for clinical use
- Any Software as a Medical Device (SaMD) or AI-enabled medical device that falls under regulatory authority jurisdiction

This SOP extends to:
- All employees, contractors, and consultants within the Clinical AI Products business unit
- Cross-functional teams involved in regulatory activities: Regulatory Affairs, Quality Assurance, Clinical Science, Engineering, Data Science, and Medical Affairs
- Products under active development (pre-submission), under review, and post-market (post-market surveillance and change management)
- All Meridian global offices contributing to or marketing Clinical AI products (Boston, London, Berlin, Singapore, Toronto)

### 1.3 Out of Scope
- In vitro diagnostic devices (IVDs)
- Non-medical AI products from the MedInsight Analytics or HealthPay Financial Services business units; these follow SOP-REG-023 (*AI Governance for Non-Medical Products*)
- Customer relationship management or sales contracting (see SOP-COMM-007, *Commercial Contracts for Regulated Products*)

## 2. Definitions and Acronyms

| Acronym/Term | Definition |
|--------------|------------|
| 510(k) | FDA premarket notification demonstrating substantial equivalence to a predicate device |
| AI Act | EU Artificial Intelligence Act (Regulation 2024/1689) |
| BIMO | FDA Bioresearch Monitoring Program inspections |
| CE Marking | Conformité Européenne marking indicating conformity with EU health, safety, and environmental requirements under MDR |
| CER | Clinical Evaluation Report |
| DHF | Design History File per 21 CFR 820.30 and ISO 13485 |
| De Novo | FDA classification request for novel devices without a valid predicate |
| DMR | Device Master Record |
| eSTAR | Electronic Submission Template and Resource used for FDA submissions |
| EUDAMED | European Database on Medical Devices |
| FCA | Fault Contribution Analysis (used in AI adverse event investigations) |
| IFU | Instructions for Use |
| IMDRF | International Medical Device Regulators Forum |
| MDR | EU Medical Device Regulation 2017/745 |
| MDQMS | Medical Device Quality Management System (Meridian's adaptation of ISO 13485:2016 on Arena PLM) |
| MLMD | Machine Learning Medical Device |
| NIST AI RMF | National Institute of Standards and Technology AI Risk Management Framework 1.0 |
| Notified Body | Organization designated by an EU member state to assess conformity of certain products before CE marking (e.g., BSI, TÜV SÜD) |
| PMPF | Post-Market Performance Follow-up |
| Predicate Device | A legally marketed device to which a new device claims substantial equivalence in a 510(k) |
| PRRC | Person Responsible for Regulatory Compliance (per Article 15, EU MDR) |
| Q-Sub | FDA Pre-Submission Program |
| SaMD | Software as a Medical Device |
| SOTA | State of the Art |
| SSCP | Summary of Safety and Clinical Performance |
| SSP | Summary of Safety and Performance (for high-risk EU devices) |
| SUD | Software Under Development |
| UDI | Unique Device Identification |

## 3. Roles and Responsibilities

### 3.1 RACI Matrix

| Activity | Regulatory Affairs | Clinical Science | Engineering / AI | Medical Affairs | Quality Assurance | VP Clinical AI | CMO | CISO | DPO |
|----------|-------------------|-----------------|------------------|-----------------|-------------------|----------------|-----|------|-----|
| Regulatory Strategy & Planning | R, A | C | C | C | C | I | I | — | — |
| Predicate Device Identification | R | I | — | C | — | I | — | — | — |
| Clinical Evidence Planning | C | R, A | C | C | C | I | I | — | — |
| Algorithm Lock & Model Card Generation | I | I | R, A | — | C | I | — | — | — |
| Technical Documentation Compilation | R, A | C | R | C | C | I | — | I | — |
| EU AI Act Conformity Assessment | R | C | C | C | C | A | C | I | C |
| eSTAR / Submission Package Assembly | R, A | — | — | — | — | C | — | — | — |
| Internal Review & Sign-Off | R | C | C | C | I | A | A | — | — |
| Submission to Regulatory Body | R, A | — | — | — | — | I | I | — | — |
| Responding to Deficiencies / AI Requests | R | C | C | C | — | I | C | — | — |
| Post-Market Surveillance (Adverse Event) | C | — | C | R | C | I | C | — | — |
| Substantial Change Assessment | R, A | C | R | C | C | I | C | — | — |

**R = Responsible** (performs work), **A = Accountable** (approves), **C = Consulted**, **I = Informed**, **— = Not involved**

### 3.2 Key Roles and Specific Responsibilities

- **VP of Clinical AI Products (Dr. Aisha Okafor):** Ultimate accountability for regulatory strategy execution and submission quality within the business unit. Serves as business process owner for this SOP.
- **Regulatory Affairs Lead:** Manages day-to-day submission activities, acts as primary FDA and Notified Body contact, maintains regulatory intelligence, and ensures submission timeliness.
- **Clinical Science Lead:** Designs and oversees clinical validation studies (standalone performance, clinical reader studies), authors Clinical Evaluation Reports (CERs) per MEDDEV 2.7/1 Rev.4.
- **Chief Medical Officer (Dr. Priya Patel):** Provides clinical safety and benefit-risk sign-off for all submissions; reviews and approves the Summary of Safety and Clinical Performance.
- **AI/ML Engineering Lead:** Responsible for algorithm versioning, lock procedures, model card documentation, and providing statistical performance metrics per SOP-ENG-042 (*AI Model Lifecycle Management*).
- **Chief Information Security Officer (Rachel Kim):** Reviews and approves cybersecurity documentation per FDA guidance and Annex I, MDR.
- **Data Protection Officer / Chief Privacy Officer (Dr. Klaus Weber):** Reviews data provenance, privacy impact, and GDPR alignment in training datasets per SOP-PRIV-018 (*Data Privacy in AI Training Data*).
- **Quality Assurance Manager:** Ensures Design History File (DHF) traceability and conducts submission-readiness audits against applicable standards.
- **Person Responsible for Regulatory Compliance (PRRC):** Appointed per Article 15 of EU MDR; certifies that the device meets MDR General Safety and Performance Requirements (GSPRs). At Meridian, this role is held by the VP of Regulatory Affairs or their named delegate.

## 4. Policy Statements

Meridian Health Technologies is committed to the following regulatory policies for all AI medical devices:

1. **Patient Safety Primacy:** Regulatory submissions shall transparently represent the clinical benefits and residual risks of AI medical devices, prioritizing patient safety in all clinical evidence and risk management documentation.
2. **Substantial Equivalence Integrity:** All 510(k) submissions will objectively document substantial equivalence to a legally marketed predicate device, identifying both intended use and technological characteristics comparisons.
3. **EU AI Act Compliance:** Clinical AI medical devices shall undergo conformity assessment as high-risk AI systems per the EU AI Act. Risk management, data governance, technical documentation, record-keeping, transparency, and human oversight obligations apply to all products marketed in the EU.
4. **Clinical Evidence Standard:** Performance claims must be supported by methodologically sound clinical evidence appropriate to the device's risk classification and intended use, following the hierarchy of evidence described in this SOP.
5. **Truthful and Non-Misleading Communication:** All regulatory submissions, labeling, and Instructions for Use (IFU) shall present a balanced description of device capabilities, limitations, and contraindications without overstatement.
6. **Continuous Compliance:** Regulatory approvals and clearances are active commitments. Material changes to AI models, intended use, or clinical workflows must be evaluated for the need for a new submission or notified body consultation per criteria defined herein.
7. **Documentation Integrity and Traceability:** All submission elements shall be traceable to controlled documents within Meridian's eQMS (Veeva Vault) and Design History File (Arena PLM), ensuring a single source of truth.
8. **Ethical AI Use:** Submissions will include specific documentation concerning bias assessment and fairness evaluation across demographic subgroups where applicable per SOP-AI-011 (*Fairness and Bias Testing for Clinical AI*).

## 5. Detailed Procedures

### 5.1 Regulatory Pathway Determination

#### 5.1.1 Initiation and Intake
**Trigger Event:** New Clinical AI product concept approved via Gate 1 of the Product Development Process (see SOP-PRD-003).

The Regulatory Affairs Lead shall complete the *Regulatory Pathway Assessment Form* (FORM-REG-015A) within 15 business days of Gate 1 approval. The form captures:
- Product name, version, and unique identifier (Meridian Product Code)
- Intended use statement (draft)
- Indications for use statement (draft)
- Clinical workflow integration description
- List of AI/ML models and their functions
- Preliminary device classification rationale (FDA Class I, II, or III; EU MDR Class I, IIa, IIb, or III)
- Known predicate devices (if any)
- EU AI Act preliminary classification

#### 5.1.2 FDA Regulatory Pathway Logic

```
Decision Tree for FDA Pathway:
├── Does product meet definition of "device" (201(h) FD&C Act)?
│   ├── No → Not a medical device. Refer to SOP-REG-023.
│   └── Yes → Continue.
├── Does product require premarket authorization?
│   ├── Exempt (Class I, general controls) → Register and list only.
│   └── Yes → Continue.
├── Is there a legally marketed predicate device?
│   ├── Yes → Is technological difference significant?
│   │   ├── No → 510(k) Premarket Notification.
│   │   └── Yes → Can Special Controls or clinical data resolve?
│   │       ├── Yes → 510(k).
│   │       └── No → De Novo Classification Request.
│   └── No → De Novo Classification Request.
└── Class III or PMA required? → Pre-Sub (Q-Sub) meeting strongly recommended.
```

#### 5.1.3 EU MDR Pathway Logic

For devices marketed or planned for marketing in the EU, the pathway is determined by classification per Annex VIII of EU MDR:
- **Class I:** Self-declaration of conformity, Annex I compliance, no Notified Body required (unless sterile/measuring).
- **Class IIa:** Notified Body audit under Annex IX (Chapters I and III) or Annex XI (Part A), plus Annex II and III technical documentation.
- **Class IIb:** Similar to Class IIa, with stricter clinical evidence requirements.
- **Class III:** Full Notified Body assessment including design dossier review (Annex IX, Chapter II or Annex X with Annex XI, Part B). All AI diagnostic imaging products at Meridian are currently Class IIb.

### 5.2 Pre-Submission Activities

#### 5.2.1 FDA Q-Submission (Q-Sub) Process
A Q-Sub is strongly recommended for:
- Devices where predicate identification is uncertain
- Novel AI architectures without established regulatory precedent
- De Novo classification requests
- Devices where clinical study design benefits from FDA feedback

**Procedure Steps:**
1. **Q-Sub Request Preparation (Week 1-4):**
   - Regulatory Affairs drafts meeting request letter using FDA’s current eSTAR Pre-Sub template.
   - Letter includes: specific questions (limit to 4-6), proposed intended use/indications, device description, proposed clinical study protocol, and preliminary predicate identification.
   - Clinical Science prepares draft study protocol for FDA review if clinical study is planned.
   - Engineering prepares AI architecture overview and training methodology summary.
2. **Internal Review (Week 5):**
   - CMO, VP Clinical AI, and General Counsel review Q-Sub package.
   - QA verifies alignment with DHF and risk management documentation.
3. **Submission (Week 6):**
   - Regulatory Affairs submits via FDA Electronic Submissions Gateway (ESG).
   - FDA acknowledges receipt within 7 days.
   - Target FDA meeting date: approximately 70-75 days from submission.
4. **Meeting Preparation (2 weeks before meeting):**
   - Presentation slides prepared addressing each question.
   - Mock Q&A session with cross-functional team.
   - Legal review of planned disclosures.
5. **Post-Meeting:**
   - Regulatory Affairs documents FDA feedback in a *Regulatory Contact Record* (FORM-REG-022).
   - Minutes distributed to all stakeholders within 5 business days.
   - Feedback incorporated into regulatory strategy plan.

#### 5.2.2 Notified Body Pre-Application
For CE marking, Meridian may engage in pre-application discussions with its Notified Body (currently BSI, Notified Body 2797). Procedure:
- Submit device description, classification rationale, and proposed conformity assessment route.
- Request a structured dialogue on clinical evidence expectations.
- Document all correspondence in Veeva Vault under the device record.

### 5.3 510(k) Submission Preparation

#### 5.3.1 Predicate Device Selection and Substantial Equivalence
Identifying a valid predicate is the cornerstone of a 510(k) submission.

**Procedure:**
1. **Predicate Search (2 weeks):**
   - Regulatory Affairs queries FDA's 510(k) Premarket Notification database, De Novo database, and Establishment Registration & Device Listing database.
   - Search parameters: product codes (e.g., QFM for radiological image processing software), regulation numbers (e.g., 21 CFR 892.2070), clearance dates (within 10 years preferred).
   - Document search methodology in *Predicate Selection Justification Memo* (TEMPLATE-REG-033).
2. **Predicate Selection Criteria (in order of preference):**
   - Same intended use, same indications for use, same technological characteristics (ideal predicate)
   - Same intended use, same indications, different technological characteristics that do not raise different questions of safety and effectiveness
   - Same intended use, broader or different indications where Meridian's device falls within the predicate's cleared indications
3. **Substantial Equivalence Table (SET):**
   - Create a detailed side-by-side comparison of:
     - Intended use / Indications for use
     - Target patient population
     - AI model type (e.g., CNN, transformer, ensemble)
     - Input data characteristics (imaging modality, resolution, acquisition parameters)
     - Output / clinical decision type
     - Clinical workflow role (concurrent, second reader, triage)
     - Performance characteristics (sensitivity, specificity, AUC at specific operating points)
   - Justify any differences in the *Difference Analysis* section.
4. **Predicate Validation:**
   - Confirm predicate has not been subject to a Class I recall.
   - Confirm predicate clearance/approval remains active (not withdrawn).
   - For multiple predicates, explain how each supports a specific aspect of substantial equivalence.

#### 5.3.2 Clinical Evidence Generation and Compilation
Clinical evidence for a 510(k) may include:
- Standalone performance testing (analytical validation)
- Clinical reader studies (if AI assists or augments human interpretation)
- Literature review supporting device safety and effectiveness
- Real-world evidence or registry data (if applicable)

**Standalone Performance Testing Procedure:**
1. Engineering prepares a locked, validated test dataset per SOP-ENG-045 (*AI Test Dataset Curation and Locking*).
2. Test dataset must be: independent of training and validation sets, representative of intended use population, and of sufficient size to achieve pre-specified statistical power.
3. Clinical Science defines primary and secondary endpoints in a *Statistical Analysis Plan (SAP)* approved by an independent statistician prior to test dataset unblinding.
4. AI engineering executes inference on the locked dataset and delivers results to Clinical Science.
5. Clinical Science computes pre-specified metrics with two-sided 95% confidence intervals.

**Clinical Reader Study Procedure (e.g., Multi-Reader Multi-Case, MRMC):**
1. Clinical Science develops study protocol compliant with FDA guidance.
2. IRB/Ethics Committee approval obtained before reader enrollment if prospective enrollment is required.
3. Readers selected representing intended user population (e.g., board-certified radiologists, attending physicians).
4. Ground truth established by independent adjudication panel (minimum 2-3 experts).
5. Statistical analysis per pre-specified SAP; analysis of AI-assisted vs. unassisted reader performance.

**Performance Targets:**
For diagnostic AI products, minimum performance thresholds must be prospectively defined in the SAP. These thresholds should be based on:
- Performance of the predicate device (if publicly available)
- Published clinical guidelines or SOTA performance metrics
- Clinical significance determined by Medical Affairs

At minimum, sensitivity and specificity point estimates for the primary endpoint should demonstrate non-inferiority to the pre-defined threshold.

#### 5.3.3 eSTAR Compilation
FDA requires all 510(k) submissions to use the eSTAR format as of October 2023.

**Compilation Procedure:**
1. Regulatory Affairs initiates an eSTAR instance in the FDA CDRH Portal.
2. Complete all sections in sequence (Non-Clinical Performance Testing, Clinical Performance Testing, Software Documentation, Cybersecurity, Biocompatibility, Sterilization, Labeling).
3. **Software Documentation Section** must include:
   - Meridian's software development lifecycle description (per SOP-ENG-044, *SDLC for SaMD*)
   - Software requirement specifications
   - Architecture design charts (high-level and detailed)
   - Software hazard analysis (per ISO 14971, linked from risk management file)
   - Verification and validation testing summary
   - Unresolved anomalies list (documented and justified for safety)
   - Software version number and release history
4. **Cybersecurity Section** per FDA Guidance (April 2022):
   - Cybersecurity bill of materials (CBOM) generated from Meridian's SBOM tool (Anchore Enterprise)
   - Threat model covering the AI pipeline: data ingestion, model inference, model update, output display
   - Cybersecurity risk assessment
   - Post-market vulnerability management plan
   - CISO (Rachel Kim) approval required before submission.
5. **Labeling Section:**
   - Draft Instructions for Use (IFU) per SOP-LBL-006 (*Medical Device Labeling and UDI*)
   - Quick reference card
   - Patient-facing summary (if applicable)
6. **Truth and Accuracy Statement:**
   - VP Clinical AI, CMO, and General Counsel sign a statement confirming all data and statements in the submission are truthful and accurate to the best of Meridian's knowledge.

#### 5.3.4 Internal Submission Review and Approval
Prior to FDA submission, the complete eSTAR package must undergo a formal internal review:

1. **Core Team Review:** Regulatory Affairs, Clinical Science, Engineering QA, Medical Affairs review assigned sections.
2. **Quality Gate Review:** QA Manager performs independent review against 21 CFR 807.87 checklist. Any findings logged in Veeva Vault as a *Submission Discrepancy* (FORM-QA-112) and resolved before release.
3. **Executive Sign-Off (Stage 1):** VP Clinical AI signs technical content approval.
4. **Executive Sign-Off (Stage 2):** CMO (Dr. Priya Patel) provides final clinical safety and benefit-risk sign-off.
5. **Legal Review:** General Counsel confirms regulatory pathway rationale and legal accuracy of labeling.
6. **Submission Lock:** Once approved, Regulatory Affairs locks the eSTAR and transmits to FDA ESG.

### 5.4 CE Marking Submission (EU MDR & AI Act)

#### 5.4.1 Conformity Assessment Route
Class IIb Clinical AI devices follow **Annex IX Chapters I and III** (Quality Management System) plus **Annex XI Part A** (Production Quality Assurance) or **Annex II** (Technical Documentation, for novel devices).

**Procedure:**
1. Regulatory Affairs confirms Notified Body scope includes both MDR and AI Act conformity.
2. Submit formal application to Notified Body with device description, draft IFU, and QMS certificate (ISO 13485, Meridian's certificate held via BSI).
3. Notified Body reviews and issues a *Common Technical Document (CTD) Assessment Plan*.

#### 5.4.2 Technical Documentation for EU MDR
Technical Documentation is compiled per Annex II & III, EU MDR using Meridian's *Technical Documentation Template* (TEMPLATE-REG-067):

**Document Structure:**
- **Part A: Device Description and Specification**
  - Device name, variants, UDI-DI assignment
  - Intended purpose, intended users, intended patient population
  - Description of operating principle, including AI model architecture
  - Previous generations and version history
- **Part B: Information for Design and Manufacturing**
  - Design specifications (SRS, SDD)
  - Manufacturing processes (software build and release)
  - Critical suppliers (e.g., AWS infrastructure, dataset providers)
- **Part C: General Safety and Performance Requirements (GSPR)**
  - Checklist of all 23 GSPRs demonstrating compliance (Annex I, MDR)
  - Linkage to supporting documentation in DHF
- **Part D: Benefit-Risk Analysis**
  - Clinical benefits quantified
  - Residual risks and risk/benefit acceptability per ISO 14971
- **Part E: Product Verification and Validation**
  - Pre-clinical verification (software unit, integration, system testing)
  - Clinical evaluation (CER, PMPF plan)
  - Performance testing with standalone and clinical study results
- **Part F: Information Supplied by Manufacturer**
  - IFU, labels, SSCP

#### 5.4.3 EU AI Act Conformity Documentation
For high-risk AI systems under the EU AI Act, Meridian Clinical AI products require additional documentation:

1. **AI System Description:**
   - Version, release date, and update mechanisms
   - Architecture and training methodology documentation
   - Input data specifications and pre-processing pipeline
   - Human-machine interface and intended interaction mode
2. **Risk Management for AI:**
   - AI-specific hazards (see Meridian's *AI Risk Register*, RISK-AI-001): data drift, concept drift, automation bias, out-of-distribution inputs, adversarial inputs, biases in training data
   - Risk classification of identified hazards. Risks are classified based on severity and probability per ISO 14971, with specific AI considerations.
3. **Data Governance:**
   - Training, validation, and test datasets described per Article 10(2)-(4)
   - Data provenance: source, acquisition settings, inclusion/exclusion criteria
   - Data examination for potential biases (see SOP-AI-011)
   - Data Protection Officer (Dr. Weber) statement confirming GDPR compliance in dataset processing
4. **Technical Documentation:**
   - Model architecture and development methodology
   - Design specifications, including all design decisions relevant to safety
   - Logging capabilities (automatic event logs)
5. **Transparency and Information:**
   - Instructions for Use meeting Article 13 requirements
   - Information about accuracy, performance, limitations
   - Statement that the product is an AI system
6. **Human Oversight:**
   - Measures for human oversight as-built, per Article 14
   - Interface design that enables clinician review and interpretation
7. **Accuracy, Robustness and Cybersecurity Specifications:**
   - Accuracy metrics and declared performance levels
   - Robustness testing to edge cases, out-of-distribution inputs
   - Cybersecurity measures (leveraging SOC 2 Type II certification as baseline)

#### 5.4.4 Clinical Evaluation Report (CER)
Per MEDDEV 2.7/1 Rev.4 and Annex XIV of EU MDR.

**Procedure:**
1. **Stage 0 - Scoping and Planning (2 weeks):**
   - Clinical Science defines clinical evaluation scope, endpoints, and SOTA.
   - Literature search protocol defined in *CER Plan* (FORM-CLIN-028).
2. **Stage 1 - Identification of Relevant Data (3 weeks):**
   - Systematic literature search of PubMed, EMBASE, Cochrane, and IEEE Xplore (for AI-specific literature).
   - Internal clinical investigation data (if any).
   - Post-market surveillance data from U.S. deployments if available.
   - Document search PRISMA flow diagram.
3. **Stage 2 - Data Appraisal (2 weeks):**
   - Each study appraised for methodological quality and relevance.
   - AI-specific appraisal criteria: dataset composition, reference standard validity, reader study blinding, statistical methodology.
4. **Stage 3 - Analysis of Clinical Data (2 weeks):**
   - Performance data extracted and analyzed.
   - Safety data (adverse events) aggregated.
   - Clinical benefit demonstrated vs. SOTA.
5. **Stage 4 - CER Completion and Approval:**
   - Clinical Science drafts CER.
   - Medical Affairs reviews and approves clinical benefit statements.
   - CMO approves final CER.

#### 5.4.5 Person Responsible for Regulatory Compliance (PRRC)
Before CE marking submission, the PRRC (or named delegate from Regulatory Affairs) shall:
- Verify conformity documentation completeness and accuracy
- Confirm post-market surveillance system is in place
- Confirm IFU and labeling meet language requirements (EN required, translations for Member States per market plans)
- Sign the EU Declaration of Conformity attesting to GSPR compliance

The signed Declaration of Conformity is uploaded into EUDAMED within the required timeline per MDR.

### 5.5 AI-Specific Submission Content

#### 5.5.1 Model Card
Every submission must include a *Model Card* (template in SOP-AI-010, *AI Model Documentation*) providing transparency to regulators. The Model Card shall include:
- Model developer (Meridian Health Technologies, Inc.)
- Model date and version
- Architecture type and version
- Intended use and user
- Geographic and demographic characteristics of the training data
- Performance metrics by sub-group (age, sex, race/ethnicity where available)
- Known limitations and failure modes
- Evaluation benchmarks and SOTA comparison
- Ethical considerations

#### 5.5.2 Algorithm Lock and Versioning
For submission, the AI model must be in a "locked" state:
1. Engineering issues a *Model Lock Request* (FORM-ENG-097) in Jira.
2. Model weights, hyperparameters, and associated metadata archived in MLflow model registry with a release tag (e.g., `submission-510k-k231234-locked`).
3. SHA-256 hash of all model artifacts generated and stored in both the DHF and the submission package.
4. Meridian's CI/CD pipeline (GitHub Actions) is configured to prevent any retraining or modification to locked submission models. Only post-submission model updates (which may require a new 510(k) or change notification) are permitted in a separate branch.

#### 5.5.3 Change Control Protocol and AI Iteration
AI models may require updates post-clearance for performance improvement or drift. Changes are classified per FDA and MDR guidance:

| Change Type | FDA Impact | EU MDR Impact | Documentation |
|-------------|------------|---------------|---------------|
| Performance improvement > clinically significant threshold | New 510(k) likely required | New conformity assessment likely required | Full submission |
| New input modality (e.g., adding MRI to originally CT-only) | New 510(k) required | Notified Body consultation; new Annex II likely | Full submission |
| Expansion of patient population (e.g., pediatric addition) | New 510(k) required | Notified Body consultation | Full or abbreviated submission |
| Performance within allowed statistical margin | Document in letter-to-file | Internal change assessment documented; notify Notified Body if significant | Change Assessment Form (FORM-REG-055) |
| Infrastructure / non-algorithmic change (e.g., cloud migration within same ISO 13485-certified environment) | Document in internal QMS | Internal documentation; may not require NB notification | SOP-IT-CHG-012 |

The Regulatory Affairs Lead is responsible for convening a *Change Assessment Board* (CAB) within 10 business days of any planned model update to determine the regulatory impact. CAB membership: Regulatory Affairs Lead (chair), Engineering Lead, Clinical Science Lead, QA Manager, and CMO (or delegate).

### 5.6 Submission Tracking and Communication

All regulatory submissions shall be tracked in Meridian's *Regulatory Submission Tracker* (a customized Veeva Vault object). Required tracking fields:
- Submission ID (Meridian-generated)
- Regulatory body reference number (once assigned)
- Device name and version
- Submission type (510(k), De Novo, Annex II, etc.)
- Submission date
- Acceptance review outcome and date
- Substantive review target date
- Interactive review / deficiency letters received (log each)
- Final decision and date
- Special conditions for clearance/approval

**Communication Protocol with Regulatory Bodies:**
- All written correspondence must be reviewed by Regulatory Affairs and, for legally binding responses, by General Counsel.
- Oral communications must be summarized in a Contact Record within 48 hours.
- Deficiency responses must be triaged by Regulatory Affairs, assigned to appropriate SMEs, and responded to within the timeline set by the regulator (typically 15-30 days for FDA AI requests, 30-60 days for Notified Body observations).

## 6. Controls and Safeguards

### 6.1 Document and Data Integrity Controls
- All submission documents are maintained in Veeva Vault eQMS with version control, audit trails, and electronic signatures per 21 CFR Part 11.
- eSTAR files are stored encrypted at rest (AES-256) and in transit (TLS 1.2+).
- No submission content may be stored exclusively on local workstations; Meridian OneDrive (governed by SOP-IT-032) is the approved staging location prior to upload to Veeva Vault.
- Model artifacts (weights, code) are stored in the MLflow artifact store (AWS S3 with versioning enabled, server-side encryption enabled, access logging enabled).

### 6.2 Separation of Duties
- The individual preparing clinical performance data (Clinical Science) shall not be the same individual who developed or trained the AI model (Engineering).
- The independent statistician reviewing the SAP and final analysis shall not be part of the product development team.
- Executive sign-off roles (VP Clinical AI, CMO) are separate from the preparation roles (Regulatory Affairs Lead, Clinical Science Lead).

### 6.3 Submission Integrity Controls
- Each eSTAR or CTD must pass a mandatory *Submission Completeness Checklist* (FORM-QA-113) verified by QA before transmission.
- A second Regulatory Affairs team member (peer review) performs a line-by-line review of all regulatory forms (e.g., 3514 Form, Declaration of Conformity) for administrative accuracy.
- CISO must independently review and approve the cybersecurity documentation; this approval cannot be delegated.

### 6.4 Intellectual Property and Proprietary Information
- All submissions are marked "Confidential Commercial Information – Not for Public Disclosure."
- Meridian's Legal department (General Counsel) pre-approves the redaction of any trade secret information from publicly-available summaries (e.g., 510(k) Summaries, SSCPs).

### 6.5 EU AI Act Specific Controls
- The *AI System Description* for high-risk classification shall be reviewed and approved by the VP Clinical AI before submission. Products meet relevant transparency obligations by documenting the intended purpose and performance characteristics in the technical file.
- A log of conformity assessments shall be maintained by Regulatory Affairs and reviewed quarterly for changes in AI Act implementation.

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| KPI | Target | Measurement Method | Owner |
|-----|--------|--------------------|-------|
| Submission Cycle Time (Gate 2 to submission-ready) | ≤ Phase 4, 180 calendar days | Veeva Vault tracker, date from Gate 2 approval to submission lock date | VP Clinical AI |
| First-Pass Acceptance Rate | ≥ 90% (no Refuse-to-Accept FDA) | FDA acceptance letters per tracker | Regulatory Affairs |
| Major Deficiency Rate | < 1 major deficiency per submission | Deficiency letter item count | Regulatory Affairs |
| Notified Body Major Nonconformity Rate during Annex audits | 0 major nonconformities | Audit report | QA Manager |
| CER Update Compliance | 100% CERs updated within specified PMPF schedule | Veeva tracker | Clinical Science |
| Post-Market Surveillance Reporting Timeliness | 100% on time per SOP-CLIN-022 | Veeva tracker | Medical Affairs / CMO |

### 7.2 Reporting Cadence

- **Monthly:** Regulatory Affairs Lead reports submission status dashboard to VP Clinical AI. Dashboard includes active submissions, upcoming planned submissions, and status of deficiency responses.
- **Quarterly:** Business Unit Review (QBR). VP Clinical AI presents aggregated KPIs, submission outcomes, and regulatory intelligence update to CMO and Executive Leadership.
- **Biannually:** Comprehensive Regulatory Strategy Review. Reassess all active regulatory pathways against evolving FDA and EU guidance documents and AI Act implementation updates.
- **Ad Hoc:** Any critical regulatory finding (e.g., refusal to accept, warning letter, Notified Body suspension) is escalated per the Escalation Protocol (Section 8.2) within 24 hours.

### 7.3 Management Review
Per ISO 13485 requirements, the regulatory submission process shall be a required input to the quarterly Quality Management Review (QMR) chaired by the CMO and VP of Quality. The review shall consider:
- Status of all pending regulatory submissions
- Significant changes to regulatory requirements
- Adequacy of resources for regulatory submissions
- Trends in deficiency letters and corrective actions

## 8. Exception Handling and Escalation

### 8.1 Documenting and Approving Exceptions
Any deviation from this SOP (e.g., submission timeline extension, predicate selection using an older device beyond the preferred 10-year window, use of non-standard clinical evidence) must be formally documented and approved:

1. **Exception Request Initiation:** Requester completes *SOP Deviation Request* (FORM-QA-088) in Veeva Vault, detailing:
   - SOP section(s) being deviated from
   - Detailed justification (technical, clinical, or business)
   - Risk assessment of the deviation
   - Proposed alternative approach
2. **Review and Approval:**
   - Exception requests impacting patient safety or clinical performance require CMO approval.
   - Exception requests impacting regulatory compliance strategy require VP Clinical AI and General Counsel approval.
   - All other exceptions require VP Clinical AI and QA Manager approval.
3. **Documentation:** Approved exceptions are appended to the submission DHF under a specific *Exception Log* (FORM-QA-089) so that auditors can trace the rationale.
4. **Expiration:** Exceptions are valid for a single, specified submission or activity only. Repeat deviations require a CAPA investigation per SOP-QA-009 (*Corrective and Preventive Action Process*).

### 8.2 Escalation Protocol for Regulatory Risks
The following events constitute a *Level 1 Regulatory Event* and trigger immediate escalation:
- Receipt of a Warning Letter or Untitled Letter from FDA
- Notified Body suspension, reduction, or withdrawal of QMS or product certificate
- A finding by any regulatory body of intentional submission of false or misleading data
- Receipt of a Refuse-to-Accept decision

**Escalation Path:**
1. Notify VP Clinical AI and VP of Quality within 4 hours of receipt.
2. Convene Emergency Regulatory Response Team (ER2T) within 24 hours.
   - ER2T Standing Members: VP Clinical AI (Chair), CMO, Chief Quality Officer, General Counsel, Chief Regulatory Officer, VP of Engineering, Chief Compliance Officer.
3. ER2T assesses risk, creates initial response strategy including external counsel engagement if needed, and briefs CEO within 48 hours.
4. All communications with the regulatory body on the Level 1 matter must be coordinated through ER2T and General Counsel.

## 9. Training Requirements

### 9.1 Target Audience and Curricula

| Role | Required Training Module(s) | Frequency | Training Method |
|------|----------------------------|-----------|-----------------|
| All Clinical AI Products Staff | CLIN-015-OV: Overview of Regulatory Submission Process | Upon hire; annual refresher | LMS e-learning (Workday Learning) |
| Regulatory Affairs | CLIN-015-ADV-RA: Advanced Regulatory Submissions (FDA & EU) | Upon hire; biennial | Instructor-led workshop + LMS assessment |
| Clinical Science | CLIN-015-ADV-CS: Clinical Evidence for AI Submissions | Upon hire; biennial | Instructor-led + case study exercises |
| AI Engineering | CLIN-015-ADV-ENG: AI Lock, Model Cards, and Submission Engineering | Upon hire; annual | LMS + hands-on sandbox environment |
| Medical Affairs and CMO | CLIN-015-EXEC: Benefit-Risk Assessment and Sign-Off Responsibilities | Upon role assignment; biennial | LMS + 1:1 briefing with Chief Regulatory Officer |
| QA Auditors | CLIN-015-AUD: Auditing AI Regulatory Submissions | Upon designation; annual | Instructor-led |

### 9.2 Training Tracking and Compliance
- All training is assigned and tracked via Workday Learning.
- LMS generates a monthly *Training Compliance Report* for the VP Clinical AI. Target ≥ 95% on-time completion.
- Personnel with overdue Critical Training (any CLIN-015 module) are subject to a "Submission Hold" access control: their Veeva Vault user permissions for Submission workspaces are temporarily suspended until training is completed and verified by LMS.

### 9.3 SOP Awareness
All personnel within the scope (Section 1.2) must acknowledge that they have read and understood the current version of this SOP. Acknowledgment is logged via the Workday Learning task assigned when a new or revised SOP is published. Acknowledgement due within 30 days.

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP ID | Title |
|--------|-------|
| SOP-QA-009 | Corrective and Preventive Action (CAPA) Process |
| SOP-AI-010 | AI Model Documentation (Model Cards) |
| SOP-AI-011 | Fairness and Bias Testing for Clinical AI |
| SOP-ENG-042 | AI Model Lifecycle Management |
| SOP-ENG-044 | Software Development Lifecycle for SaMD |
| SOP-ENG-045 | AI Test Dataset Curation and Locking |
| SOP-LBL-006 | Medical Device Labeling and UDI |
| SOP-CLIN-003 | Clinical Study Protocol Development |
| SOP-CLIN-022 | Post-Market Clinical Follow-up (PMCF) and Surveillance |
| SOP-PRD-003 | Product Development Process (Stage-Gate) |
| SOP-PRIV-018 | Data Privacy in AI Training Data |
| SOP-REG-023 | AI Governance for Non-Medical Products |
| SOP-REG-029 | EU MDR Post-Market Surveillance |
| SOP-IT-032 | Meridian OneDrive: Governance and Data Classification |
| SOP-IT-CHG-012 | IT Infrastructure Change Management for Regulated Systems |
| RISK-AI-001 | AI Risk Register (Master) |

### 10.2 External Standards and Guidance

| Reference | Description |
|-----------|-------------|
| 21 CFR Part 807 | FDA Establishment Registration and Device Listing |
| 21 CFR 807.87 | Information Required in a Premarket Notification Submission |
| 21 CFR Part 820 | Quality System Regulation (QSR) |
| ISO 13485:2016 | Medical Devices – Quality Management Systems |
| ISO 14971:2019 | Medical Devices – Application of Risk Management |
| EU MDR 2017/745 | European Medical Device Regulation |
| EU AI Act 2024/1689 | European Artificial Intelligence Act |
| MEDDEV 2.7/1 Rev.4 | Clinical Evaluation: A Guide for Manufacturers and Notified Bodies |
| IMDRF/SaMD WG/N12FINAL | Software as a Medical Device: Clinical Evaluation |
| IMDRF/SaMD WG/N41 | Software as a Medical Device: Application of Quality Management System |
| FDA Guidance (2022) | Cybersecurity in Medical Devices: Quality System Considerations and Content of Premarket Submissions |
| FDA Guidance (2023) | Content of Premarket Submissions for Device Software Functions |
| FDA Guidance (2021) | Artificial Intelligence/Machine Learning (AI/ML)-Based Software as a Medical Device (SaMD) Action Plan |
| IEC 62304:2006+A1 | Medical Device Software – Software Life Cycle Processes |
| IEC 82304-1:2016 | Health Software – General Requirements for Product Safety |

## 11. Revision History

| Version | Date | Author / Editor | Summary of Changes |
|---------|------|-----------------|---------------------|
| 1.0 | 2023-06-15 | J. Mwangi, Regulatory Affairs Lead (initial author) | Initial release of SOP-CLIN-015. Established framework for FDA 510(k) and EU MDR submissions. |
| 1.1 | 2023-09-07 | A. Chen, Sr. Regulatory Specialist | Revised Section 5.3.3 to incorporate mandatory eSTAR usage; added Section 5.5 on AI-specific content including Model Card and Algorithm Lock procedures. |
| 1.2 | 2024-02-28 | Dr. L. Patel, Clinical Science Director | Significant update to Section 5.3.2 (Clinical Evidence) and Section 5.4.4 (CER) to align with MEDDEV 2.7/1 Rev.4 and reader study best practices. Added performance targets language. |
| 1.3 | 2024-08-12 | T. Eriksson, VP Regulatory Affairs (Europe) | Incorporated preliminary EU AI Act documentation requirements in Sections 5.4.3 and 6.5. Updated Notified Body to BSI 2797. Added PRRC responsibilities. |
| 1.4 | 2024-12-17 | Dr. A. Okafor, VP Clinical AI Products | Comprehensive rewrite for clarity and procedural flow. Expanded EU AI Act conformity procedures. Added Section 8.2 Level 1 escalation protocol. Updated Predicate Selection criteria. Added detailed RACI matrix and KPIs. Approved by Dr. P. Patel, CMO. |

**End of Document**
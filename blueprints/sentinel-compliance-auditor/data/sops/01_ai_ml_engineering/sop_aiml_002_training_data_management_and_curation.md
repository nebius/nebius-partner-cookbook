---
sop_id: "SOP-AIML-002"
title: "Training Data Management and Curation"
business_unit: "AI/ML Engineering"
version: "2.2"
effective_date: "2025-09-22"
last_reviewed: "2026-08-12"
next_review: "2027-02-13"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "NIST AI RMF"
  - "GDPR"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Training Data Management and Curation

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for the sourcing, curation, quality assurance, labeling, bias management, and version control of all training, validation, and test data utilized in the development, deployment, and maintenance of Artificial Intelligence and Machine Learning (AI/ML) models at Meridian Health Technologies, Inc. The purpose of this document is to ensure that all AI/ML models—particularly those classified as high-risk under applicable regulatory frameworks—are trained on data that meets defined standards for accuracy, representativeness, integrity, and provenance. This SOP operationalizes Meridian’s commitment to responsible AI development and serves as the foundational data governance instrument for the AI/ML Engineering business unit.

### 1.2 Scope

This SOP applies to all employees, contractors, vendors, and business partners involved in the creation, acquisition, annotation, preprocessing, or management of datasets used for AI/ML model training within Meridian Health Technologies. The scope encompasses:

**Business Lines in Scope:**
- Clinical AI Platform: All clinical decision support, diagnostic imaging analysis, patient risk scoring, and adverse event prediction models.
- HealthPay Financial Services: Credit scoring, fraud detection, claims automation, and medical lending models.
- MedInsight Analytics: Population health analytics, care gap identification, and outcomes prediction models.
- Meridian SaaS Platform: Underlying infrastructure services, anomaly detection, and platform-level AI features.

**Data Types in Scope:**
- Structured clinical data (EHR extracts, lab results, medication records, claims data)
- Unstructured clinical data (medical imaging, clinical notes, pathology reports)
- Financial data (payment histories, credit bureau data, claims submissions)
- Demographic and socioeconomic data
- Synthetic data generated for augmentation or privacy preservation
- Third-party licensed datasets
- Public datasets used for pre-training or transfer learning
- Data from Meridian-operated data collaboratives and consortia

**Geographic Scope:**
- All Meridian offices and operations globally (Boston, London, Berlin, Singapore, Toronto)
- All cloud environments (AWS us-east-1, eu-west-1; Azure DR regions)
- Remote work environments of authorized personnel

**Out of Scope:**
- Operational analytics data used for internal business intelligence (governed by SOP-DATA-007)
- Employee data used for HR analytics (governed by SOP-HR-012)
- Customer relationship management data (governed by SOP-CRM-004)

### 1.3 Applicability

Compliance with this SOP is mandatory for all AI/ML Engineering personnel. The VP of Engineering, in consultation with the Chief AI Officer, may grant specific exemptions in writing as described in Section 8. Non-compliance may result in model deployment delays, model rollback, access revocation, or disciplinary action in accordance with Meridian Human Resources policies.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Adverse Event Data** | Data related to incidents where a patient or user experienced harm or potential harm associated with a Meridian AI system. |
| **Bias** | Systematic difference in treatment of certain objects, people, or groups in comparison to others, which may result in differential model performance across subpopulations. |
| **Curation** | The end-to-end process of organizing, managing, and maintaining datasets throughout their lifecycle, including selection, cleaning, transformation, documentation, and preservation. |
| **Data Card** | A structured, machine-readable document describing a dataset's composition, collection process, preprocessing, intended use, limitations, and provenance. Analogous to a Model Card for datasets. |
| **Data Drift** | Change in the statistical properties of input data over time relative to the training data distribution. |
| **Data Lineage** | The complete record of data's origins, movements, transformations, and usage across systems from creation or ingestion through consumption. |
| **Data Provenance** | Documentation of the origin, custody, and transformations applied to data, including timestamps, responsible parties, and processing operations. |
| **Fairness** | The property of an AI system to perform equitably across defined subpopulations, as measured by pre-defined fairness metrics. |
| **Ground Truth** | The verified, authoritative labeling or annotation of data against which model predictions are compared during training and evaluation. |
| **High-Risk AI System** | As defined by the EU AI Act Annex III, AI systems intended to be used as safety components or that pose significant risk to health, safety, or fundamental rights, including Meridian's clinical decision support and diagnostic imaging analysis products. |
| **Labeling** | The process of assigning target values, classifications, annotations, or structured metadata to raw data instances for supervised or semi-supervised learning. |
| **Protected Attribute** | A characteristic protected under applicable anti-discrimination laws, including but not limited to race, ethnicity, gender, age, religion, disability status, sexual orientation, and genetic information. |
| **Selection Bias** | Bias introduced by the non-random selection of data instances for training, resulting in a dataset not representative of the intended target population. |
| **Synthetic Data** | Artificially generated data that maintains the statistical properties of a source dataset while being created through algorithmic means rather than direct measurement or collection. |
| **Training Data** | The subset of data used to fit model parameters during the learning process. For purposes of this SOP, the term encompasses training, validation, and test partitions unless otherwise specified. |
| **Versioned Dataset** | An immutable snapshot of a dataset at a specific point in time, identified by a unique version identifier and accompanied by complete metadata. |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| **AI RMF** | Artificial Intelligence Risk Management Framework (NIST) |
| **BAA** | Business Associate Agreement |
| **BOM** | Bill of Materials (for datasets) |
| **CDSA** | Clinical Data Sharing Agreement |
| **CPO** | Chief Privacy Officer |
| **CRO** | Chief Risk Officer |
| **DUA** | Data Use Agreement |
| **EDA** | Exploratory Data Analysis |
| **EHR** | Electronic Health Record |
| **ETL** | Extract, Transform, Load |
| **FACET** | Fairness Assessment and Continuous Evaluation Toolkit (Meridian internal tool) |
| **FMEA** | Failure Mode and Effects Analysis |
| **KPI** | Key Performance Indicator |
| **MDM** | Master Data Management |
| **ML** | Machine Learning |
| **PHI** | Protected Health Information |
| **PII** | Personally Identifiable Information |
| **RACI** | Responsible, Accountable, Consulted, Informed |
| **SME** | Subject Matter Expert |
| **TDD** | Training Data Dictionary |

---

## 3. Roles and Responsibilities

### 3.1 RACI Matrix

The following RACI matrix defines role assignments for key activities within the training data management lifecycle.

| Activity | CAIO | VP Eng | AI/ML Lead | Data Eng | Data Scientist | Domain SME | CISO | CPO/DPO | CCO |
|---|---|---|---|---|---|---|---|---|---|
| Data Sourcing Approval | A | R | C | C | C | C | C | R | I |
| Data Quality Standards Definition | A | C | R | C | C | I | I | C | I |
| Bias Assessment | A | I | R | C | R | C | I | C | I |
| Labeling Protocol Design | I | I | A | C | R | R | I | I | I |
| Data Versioning | I | A | R | R | C | I | I | I | I |
| BAA Validation (HIPAA) | I | I | I | I | I | I | R | A | R |
| Cross-Border Transfer Review | I | I | C | C | I | I | C | A | R |
| Training Data Audit | I | A | R | C | C | I | R | C | I |
| Exception Approval | A | R | C | I | I | I | C | C | C |

**Legend:** R = Responsible (does the work), A = Accountable (approves), C = Consulted (provides input), I = Informed (receives updates)

### 3.2 Named Roles and Specific Responsibilities

**Dr. Marcus Rivera, Chief AI Officer (CAIO)**
- Ultimate accountability for enterprise AI data governance
- Approves all high-risk AI system training data sourcing decisions
- Chairs the quarterly AI Data Governance Review Board
- Authorizes exceptions to this SOP for non-high-risk AI systems
- Reports training data compliance status to the Board AI Governance Committee

**David Park, VP of Engineering**
- Accountable for implementation and enforcement of this SOP across AI/ML Engineering
- Approves data infrastructure and tooling investments for data management
- Reviews and signs off on all high-risk dataset release approvals
- Ensures adequate resourcing for data curation activities

**AI/ML Engineering Lead (per product area)**
- Responsible for day-to-day data management within their product domain
- Develops and maintains dataset-specific Data Cards
- Conducts initial bias assessments for all new datasets
- Ensures team adherence to data versioning and documentation requirements
- Escalates data quality issues to VP of Engineering

**Data Engineers**
- Build and maintain ETL/ELT pipelines for training data preparation
- Implement data quality checks as defined by AI/ML Leads
- Execute data versioning and maintain dataset registries
- Monitor data drift metrics and trigger alerts
- Document data lineage in Meridian's MLflow tracking server

**Data Scientists**
- Perform exploratory data analysis and document findings
- Develop and execute bias testing protocols
- Specify labeling requirements and quality acceptance criteria
- Validate dataset fitness for intended modeling purpose
- Collaborate with Domain SMEs on ground truth establishment

**Domain SMEs (Clinical, Financial, Privacy)**
- Clinical SMEs: Board-certified physicians responsible for clinical labeling accuracy, clinical validity of data, and identification of clinically relevant biases (led by Dr. Priya Patel, CMO, for clinical data)
- Financial SMEs: Underwriting and fraud domain experts responsible for financial data labeling and model fairness in lending contexts (led by Robert Liu, VP of Financial Services)
- Privacy SMEs: Ensure data handling complies with privacy requirements (led by Dr. Klaus Weber, CPO/DPO)

**Rachel Kim, Chief Information Security Officer (CISO)**
- Ensures security controls for training data repositories
- Approves encryption and access control mechanisms
- Reviews third-party data vendor security postures
- Leads incident response for training data breaches

**Dr. Klaus Weber, Chief Privacy Officer / Data Protection Officer (CPO/DPO)**
- Reviews training data sourcing for privacy implications
- Advises on data minimization principles for training datasets
- Evaluates international data transfer mechanisms

**Thomas Anderson, Chief Compliance Officer (CCO)**
- Provides regulatory interpretation for training data requirements
- Reviews this SOP for compliance with evolving regulations
- Participates in AI Data Governance Review Board

---

## 4. Policy Statements

### 4.1 Data Quality and Integrity

All training data used for AI/ML model development shall meet defined quality standards appropriate to the risk classification of the target model. Data must be assessed for completeness, accuracy, consistency, timeliness, and representativeness prior to use in model training. No dataset may be used for training a high-risk AI system without a completed Data Card and a satisfactory quality assessment signed by the responsible AI/ML Engineering Lead.

### 4.2 Data Provenance and Traceability

The origin and complete transformation history of all data elements used in training shall be documented and traceable from source system through model deployment. Data lineage records shall be maintained for the full lifecycle of the model, including post-decommissioning archival periods. All datasets shall be uniquely versioned and registered in the Meridian Dataset Registry maintained in MLflow.

### 4.3 Bias Management

Training data shall be assessed for potential sources of bias including, but not limited to, selection bias, measurement bias, reporting bias, and representation bias. Protected attributes shall be identified and documented for each dataset. Bias assessments shall be conducted at dataset creation, at each major version change, and no less frequently than semi-annually for datasets supporting deployed high-risk AI systems.

### 4.4 Labeling Quality and Consistency

All labeled training data shall be produced according to documented labeling protocols that define annotation guidelines, inter-rater reliability thresholds, and quality acceptance criteria. For clinical labeling tasks, annotation shall be performed or verified by qualified clinical professionals. Labeling provenance including annotator identity (or anonymized annotator ID) and timestamp shall be recorded.

### 4.5 Data Versioning and Immutability

All training datasets shall be immutable once versioned. Any modification to a dataset shall result in a new version. The relationship between dataset versions shall be explicitly documented (e.g., "v2.1 adds 15,000 records from source A and removes records flagged in quality audit QA-2025-047"). Active models shall reference specific dataset versions, enabling exact reproduction of training conditions.

### 4.6 Data Minimization

Training datasets shall contain only the minimum data elements necessary to achieve the defined modeling objective. The inclusion of each data field in a training dataset shall be justified by a documented rationale approved by the AI/ML Engineering Lead and reviewed by the CPO/DPO for high-risk AI system datasets.

### 4.7 Transparency and Documentation

All training datasets shall be accompanied by a Data Card that describes the dataset's composition, intended use, limitations, and relevant characteristics as specified in Section 5.8. Data Cards for high-risk AI systems shall be made available to internal audit, regulatory bodies, and authorized external stakeholders upon request.

### 4.8 Human Oversight of Data Processes

Human review shall be integrated into critical data management workflows including data sourcing approval, quality assessment sign-off, bias evaluation review, and labeling validation. Automated data quality checks shall serve as decision support for human reviewers, not as sole arbiters of data acceptability. Oversight records shall document reviewer identity, decision rationale, and timestamp for each review gate.

---

## 5. Detailed Procedures

### 5.1 Data Sourcing and Acquisition

#### 5.1.1 Sourcing Evaluation Process

All new data sources must undergo the following evaluation process prior to acquisition or use:

**Step 1: Sourcing Request Submission**
The requesting Data Scientist or AI/ML Lead shall submit a Data Sourcing Request through the Meridian AI Governance Portal (ServiceNow AI module). The request shall include:
- Proposed data source description and origin
- Intended model use case and risk classification
- Data elements requested with justification for each
- Estimated data volume and date range
- Known or suspected data quality issues
- Preliminary identification of protected attributes
- Data source type (internal, commercial, public, collaborative)

**Step 2: Preliminary Vetting**
Upon submission, the request is automatically routed to:
- CISO team for security assessment of external sources
- CPO/DPO team for privacy and data protection review
- Legal team for contractual and compliance review (for third-party data)
- Domain SME pool for clinical or financial data relevance assessment

Preliminary vetting SLA: 5 business days for non-high-risk; 10 business days for high-risk.

**Step 3: Data Sample Evaluation**
If preliminary vetting is approved, the Data Engineering team shall:
1. Obtain or create a representative data sample (minimum 10,000 records or 1% of estimated full dataset, whichever is greater)
2. Ingest the sample into the Meridian Data Sandbox (isolated AWS environment, eu-west-1 or us-east-1 as appropriate)
3. Execute the automated Data Quality Assessment Suite (see Section 5.3)
4. Generate a Sample Quality Report (SQR) and distribute to the requester and reviewers

**Step 4: Full Sourcing Approval**
The AI/ML Lead compiles the SQR, vetting assessments, and their evaluation into a Sourcing Approval Package. Approval thresholds:
- For non-high-risk models: AI/ML Lead approval
- For high-risk models: AI/ML Lead recommendation + CAIO approval
- For external/commercial data sources: Additional VP of Engineering and Legal approval required

**Step 5: Data Acquisition and Ingestion**
Upon approval, the Data Engineering team shall:
1. Establish secure data transfer channels (SFTP, AWS Transfer Family, or API integration)
2. Execute data ingestion following the Data Ingestion Runbook (see Meridian Confluence: AIML/INGEST-01)
3. Assign a unique Dataset ID from the Meridian Dataset Registry
4. Create the initial version (v1.0) in the data lake with full metadata

#### 5.1.2 Internal Data Sources

Internal data may be sourced from Meridian production systems subject to:
- Verification that data use aligns with the original collection purpose and applicable notices
- Confirmation that data retention periods permit the intended use
- Approval from the data steward of the source system
- For PHI-containing data: verification of HIPAA compliance pathway (treatment, operations, or authorized research)

Approved internal data sources are maintained in the Internal Data Source Catalog (Meridian Confluence: AIML/DATASOURCES).

#### 5.1.3 Third-Party Data Sources

Commercial and third-party data sources require:
- Completed vendor security assessment (per SOP-SEC-008)
- Signed Data Use Agreement (DUA) reviewed by Legal
- Data quality warranty provisions in the commercial agreement
- Right-to-audit clause for data provenance verification
- Explicit terms for data deletion upon contract termination

#### 5.1.4 Public and Open-Source Datasets

Public datasets (e.g., MIMIC, UK Biobank, The Cancer Genome Atlas) require:
- Documentation of the dataset's license terms and permitted use verification
- Review of the dataset's collection methodology for potential biases
- Acknowledgment of any use restrictions or citation requirements
- Assessment of whether the dataset's age or population scope limits applicability

### 5.2 Data Preprocessing and Transformation

#### 5.2.1 Standardized Preprocessing Pipeline

All training data must be processed through the Meridian Standardized Preprocessing Pipeline (deployed as Kubeflow pipelines) with the following mandatory stages:

**Stage 1: Format Validation**
- Schema validation against the target data model
- Data type enforcement and casting
- Structural integrity checks (row counts, column presence, file format compliance)

**Stage 2: Deduplication**
- Exact and fuzzy deduplication using the Meridian Record Linkage Engine
- Configurable similarity thresholds (default: 0.95 Jaccard for text, 0.99 Levenshtein for structured fields)
- Deduplication decisions logged with rationale

**Stage 3: Missing Data Handling**
- Missing data pattern analysis and reporting
- Imputation strategy documentation (mode/median, MICE, model-based, or indicator method)
- Missing data rate thresholds: >40% missing in a field triggers mandatory SME review; >15% missing in a record triggers review
- Complete missing data report generated

**Stage 4: Outlier Detection and Handling**
- Statistical outlier detection (IQR, Z-score, or domain-specific thresholds as specified in the Data Card)
- Clinical data: Outlier flagging only (no automatic removal); all flagged values referred to clinical SME
- Financial data: Automated winsorization at 1st and 99th percentiles with override capability
- Outlier treatment fully documented

**Stage 5: Normalization and Encoding**
- Numerical features: Standard scaling, min-max scaling, or no scaling as specified
- Categorical features: One-hot encoding, target encoding, or ordinal encoding with mapping documentation
- Text features: Tokenization pipeline specification

**Stage 6: Feature Engineering Documentation**
- Any derived features must have their calculation methodology documented in the Data Card
- Feature importance or selection rationale recorded

#### 5.2.2 Preprocessing Metadata Capture

Each preprocessing step automatically records in the MLflow tracking server:
- Operation name and parameters
- Input and output record counts
- Timestamp of execution
- Runtime environment identifier
- Data quality metrics pre- and post-transformation

### 5.3 Data Quality Assessment

#### 5.3.1 Automated Quality Assessment Suite

The Data Quality Assessment Suite executes the following checks on each dataset version:

| Quality Dimension | Metric | Threshold (Non-High-Risk) | Threshold (High-Risk) |
|---|---|---|---|
| Completeness | % non-null values per field | ≥ 90% | ≥ 95% |
| Completeness | % complete records | ≥ 85% | ≥ 92% |
| Uniqueness | Duplicate record rate | < 2% | < 0.5% |
| Consistency | Cross-field rule violation rate | < 3% | < 1% |
| Timeliness | Max data age at ingestion | 90 days | 30 days |
| Validity | Format conformance rate | ≥ 95% | ≥ 99% |
| Accuracy | Verified against authoritative source (%) | ≥ 90% | ≥ 97% |

#### 5.3.2 Quality Issue Classification

Quality issues are classified as follows:

- **Critical:** Issue renders a significant portion of data unusable or creates risk of incorrect model outputs that could impact patient safety or financial decisions. Requires immediate halt of dataset use and escalation to VP of Engineering.
- **Major:** Issue impacts data fitness for purpose but does not create immediate safety or fairness risk. Requires resolution within 10 business days.
- **Minor:** Issue does not materially impact fitness for purpose. Resolution required within 30 days or documented acceptance.

#### 5.3.3 Clinical Data Specific Quality Checks

For clinical training data, additional checks apply:
- Valid clinical coding (ICD-10, SNOMED CT, LOINC, CPT) where applicable
- Plausible date ranges (date of service not in the future, date of birth not resulting in age >120)
- Lab result values within physiological possibility ranges
- Medication dosage within standard clinical ranges
- Temporal consistency (e.g., diagnosis date not after death date)

#### 5.3.4 Quality Reporting

A Data Quality Report is auto-generated for each dataset version and must be:
- Reviewed by the responsible Data Scientist within 5 business days
- Signed off by the AI/ML Lead
- Attached to the dataset's Data Card
- Retained for the dataset lifecycle plus 7 years

### 5.4 Labeling and Annotation

#### 5.4.1 Labeling Protocol Development

For each supervised learning task requiring labeled data, a Labeling Protocol must be developed, reviewed, and approved prior to labeling commencement. The protocol shall specify:

**Protocol Contents:**
1. **Task Definition:** Clear description of the labeling task and output format
2. **Label Taxonomy:** Complete set of possible labels with definitions, examples, and edge cases
3. **Annotation Guidelines:** Step-by-step instructions for annotators
4. **Quality Requirements:** Inter-rater reliability targets (minimum Cohen's Kappa ≥ 0.7 for clinical tasks; ≥ 0.6 for non-clinical tasks)
5. **Qualification Requirements:** Required credentials for annotators
6. **Review Process:** Procedure for resolving disagreements and handling edge cases
7. **Gold Standard Set:** Requirement for a curated gold standard dataset for ongoing quality monitoring

**Protocol Approval (High-Risk AI):**
- Clinical labeling protocols: Approved by Clinical AI Product Lead (Dr. Aisha Okafor) or delegate board-certified physician
- Financial labeling protocols: Approved by VP of Financial Services (Robert Liu) or delegate

#### 5.4.2 Annotator Qualification and Management

**Internal Annotators (Meridian Employees):**
- Must complete the Annotator Training Program (see Section 9)
- Must pass a certification quiz with ≥85% score on a practice dataset
- Certification is role-specific and must be renewed annually

**External Annotators (Vendors/Contractors):**
- Must meet qualification criteria specified in the Labeling Protocol
- Vendor must be approved through Meridian's vendor management process
- Must complete task-specific onboarding and pass the same certification requirements as internal annotators
- Must sign confidentiality agreements covering the data they will handle

**Annotator Performance Monitoring:**
- Ongoing inter-rater reliability tracking against the gold standard set
- Annotators falling below Kappa ≥ 0.6 for 2 consecutive batches are suspended pending retraining
- Performance dashboards maintained in the FACET system

#### 5.4.3 Labeling Workflow

**Step 1: Batch Creation**
Data Engineering creates annotation batches from the source dataset, each containing 500-2,000 instances depending on task complexity. Each batch includes 5% gold standard instances for quality monitoring.

**Step 2: Dual Annotation (High-Risk)**
For high-risk AI system training data, 100% of instances shall be independently annotated by two qualified annotators. Disagreements are flagged for adjudication.

**Step 3: Adjudication**
Disagreements are resolved by a senior annotator or Domain SME. Adjudication decisions are recorded with rationale for full traceability.

**Step 4: Quality Gate**
Each completed batch is evaluated against the Labeling Protocol quality thresholds. Batches not meeting thresholds are returned for rework. Three consecutive batch failures trigger a labeling process review.

**Step 5: Label Consolidation**
Final labels are consolidated into the versioned dataset. Label metadata including annotator IDs, timestamps, and confidence scores (if applicable) are preserved.

#### 5.4.4 Automated Labeling and Weak Supervision

Where automated labeling techniques (programmatic labeling, weak supervision, foundation model inference) are used:
- The labeling function or model must be documented with its assumptions and limitations
- Automated labels must be validated against a human-labeled sample (minimum 500 instances) to quantify error rates
- Automatically labeled data must be flagged with its provenance in the dataset metadata
- Automated labeling may not be the sole source of labels for high-risk clinical AI systems without specific CAIO approval

### 5.5 Bias Assessment

#### 5.5.1 Bias Identification Workshop

For each new dataset (and each major version thereof), the AI/ML Lead shall convene a Bias Identification Workshop with the following participants:
- Data Scientist(s) working on the model
- Domain SME (clinical or financial as appropriate)
- One representative from the AI Ethics function (dotted-line report to CAIO)
- For high-risk datasets: a patient advocate or external ethics advisor (when available through Meridian's Patient Advisory Council)

The workshop shall systematically examine:
- Historical biases in data collection processes
- Underrepresentation or overrepresentation of demographic groups
- Potential for measurement bias in features
- Proxy variables that may encode protected attributes
- Label bias and annotator demographic effects

#### 5.5.2 Protected Attribute Identification

Protected attributes relevant to the dataset domain shall be explicitly identified and documented. Where direct protected attributes exist in the data, they shall be flagged in the dataset schema. The AI/ML Lead shall also assess whether any non-protected attributes serve as proxies for protected attributes.

#### 5.5.3 Fairness Metric Evaluation

The FACET toolkit shall be run against all datasets supporting high-risk AI systems to compute:
- Demographic parity difference
- Equal opportunity difference
- Disparate impact ratio
- Representation indices for each identified subpopulation
- Label distribution analysis across demographic groups

Results are documented in the dataset's Bias Assessment Report.

#### 5.5.4 Mitigation Recommendations

Where bias assessments identify meaningful disparities, the workshop shall generate mitigation recommendations documented in the Bias Assessment Report. Recommendations may include:
- Data augmentation to address underrepresentation
- Reweighting strategies
- Exclusion of problematic proxy features
- Resampling techniques
- Recommendation to use fairness-aware training algorithms (if applicable to the model type)

Mitigation effectiveness shall be measured and documented post-implementation.

### 5.6 Data Versioning and Lineage

#### 5.6.1 Version Identification

All datasets in the Meridian Dataset Registry are identified by the following scheme:

**Format:** `{DATASET_ID}-v{major}.{minor}[-{tag}]`

- `DATASET_ID`: Short identifier assigned at creation (e.g., `CXRAY-V3`, `HPAY-FRD-01`)
- `major`: Incremented for significant changes (new data sources, schema changes, >20% record change)
- `minor`: Incremented for minor updates (small record additions, preprocessing parameter changes)
- `tag`: Optional descriptor (e.g., `-balanced`, `-deduped`)

**Examples:**
- `CXRAY-V3-v2.1`: Chest X-ray dataset version 3, major version 2, minor 1
- `HPAY-FRD-01-v1.0-original`: HealthPay fraud detection dataset, v1.0, original version prior to rebalancing

#### 5.6.2 Version Lifecycle States

| State | Description | Permitted Actions |
|---|---|---|
| **Draft** | Dataset under active curation | Read/Write, not available for production training |
| **Review** | Dataset undergoing quality and bias review | Read-only for reviewers, Write restricted |
| **Released** | Approved for production use | Read-only, used in training pipelines |
| **Deprecated** | Superseded by newer version | Read-only, models using this version flagged for update |
| **Archived** | Retained for compliance, not for active use | Read-only, cold storage tier |
| **Quarantined** | Flagged for quality or compliance issue | Access frozen pending investigation |

#### 5.6.3 Version Creation Workflow

1. Data Engineer initializes new dataset version in the Meridian Data Lake (AWS S3 with versioned bucket)
2. ETL pipeline populated with source data, preprocessing configuration specified
3. Data Quality Assessment Suite executed; Quality Report auto-attached
4. Data Card updated or created for this version
5. Bias Assessment Report generated
6. AI/ML Lead reviews and transitions state to "Review"
7. Designated reviewers complete review; any issues resolved
8. AI/ML Lead transitions to "Released"
9. Version metadata registered in MLflow Dataset Registry; immutable snapshot created

#### 5.6.4 Data Lineage Tracking

The Meridian Data Lineage Service (powered by Apache Atlas integration) automatically captures:
- Source system and extraction timestamp for each data element
- All transformations applied with parameters
- Responsible user or service account for each operation
- Quality metrics at each stage
- Downstream model consumption

Lineage graphs are viewable in Meridian's internal Data Governance Console and are exportable for audit purposes.

### 5.7 Train/Validation/Test Split Management

#### 5.7.1 Split Strategy Documentation

The strategy for partitioning data into training, validation, and test sets must be documented for each model, including:
- Split methodology (random, time-based, stratified, group-based)
- Stratification variables (if any)
- Split ratios and rationale
- Procedure for ensuring no information leakage between partitions
- Special considerations (e.g., ensuring all records for a single patient are in the same partition for patient-level tasks)

#### 5.7.2 Leakage Prevention

The following controls shall be implemented to prevent train/test contamination:
- Patient-level splitting where records relate to individual patients (mandatory for clinical data)
- Time-based splitting for temporal prediction tasks (training on earlier data, validation/testing on later data)
- Group-level splitting where natural groupings exist (e.g., hospital site)
- Automated leakage detection tests in the preprocessing pipeline
- Verification that test set statistics are not used to inform preprocessing decisions

#### 5.7.3 Test Set Governance

Test sets for high-risk AI systems shall be:
- Sequestered (access restricted to model evaluation only)
- Never used for hyperparameter tuning or model selection decisions
- Immutable once released; any changes require a new test set version
- Subject to the same quality and bias assessments as training data

### 5.8 Data Card Documentation

#### 5.8.1 Required Data Card Sections

Every released dataset must have a complete Data Card containing the following sections. The Data Card template is available in the Meridian AI Governance Portal.

**Section 1: Dataset Overview**
- Dataset name and unique identifier
- Version and release date
- Brief description and intended use
- Risk classification of associated models
- Data steward (AI/ML Lead name)

**Section 2: Data Composition**
- Record count and feature count
- Data types and schema definition
- Target variable definition (for supervised tasks)
- Protected attributes present in the dataset
- Class distribution or key statistical summaries
- Temporal coverage (start date, end date)
- Geographic coverage (countries, regions)

**Section 3: Data Sources**
- Origin of each data element
- Collection methodology
- Source system identifiers
- Data sharing agreements or contracts referenced

**Section 4: Preprocessing and Transformation**
- Complete preprocessing pipeline description
- Missing data treatment
- Outlier handling approach
- Feature engineering steps
- Any exclusion criteria applied

**Section 5: Labeling**
- Labeling protocol reference
- Annotator qualification summary
- Inter-rater reliability achieved
- Label distribution
- Adjudication procedures used

**Section 6: Data Quality**
- Summary of quality assessment results
- Key quality metrics achieved against thresholds
- Known quality limitations
- Quality report reference

**Section 7: Bias and Fairness**
- Protected attributes and subpopulations identified
- Fairness metrics computed
- Bias assessment summary and findings
- Mitigations applied or planned
- Known representational limitations

**Section 8: Usage and Limitations**
- Approved use cases
- Out-of-scope or prohibited uses
- Known limitations and caveats
- Intended user population and deployment context
- Generalizability constraints

**Section 9: Legal and Compliance**
- Data use agreements referenced
- Privacy impact assessment reference (if conducted)
- Data retention requirements
- Deletion or disposal instructions

**Section 10: Maintenance**
- Expected refresh frequency
- Conditions triggering re-curation
- Responsible party for maintenance
- Next scheduled review date

#### 5.8.2 Data Card Review and Approval

- Data Cards for non-high-risk datasets: Reviewed and approved by AI/ML Lead
- Data Cards for high-risk datasets: Additionally reviewed by CAIO or delegate, CPO, and Domain SME
- Data Cards must be updated with each major version change

#### 5.8.3 Data Card Accessibility

Data Cards shall be:
- Stored in the MLflow Dataset Registry and linked to the dataset version
- Accessible to all personnel with approved dataset access
- Exportable in machine-readable format (JSON) for audit and regulatory purposes
- For high-risk AI systems, formatted for external sharing upon authorized request

### 5.9 Synthetic Data Generation

#### 5.9.1 Approved Use Cases

Synthetic data may be used for the following purposes:
- Augmenting training data to address identified representation gaps
- Creating test datasets for edge case and robustness evaluation
- Privacy-preserving data sharing for research collaborations
- Initial model prototyping before real data access is approved

Synthetic data may not replace real data as the sole training source for high-risk clinical AI systems.

#### 5.9.2 Generation Controls

Synthetic data generation shall follow these requirements:
- Clearly documented generation methodology and model used
- Privacy-preserving guarantees verified (e.g., differential privacy parameters)
- Fidelity assessment comparing synthetic data statistical properties to source data
- Risk assessment for potential re-identification of training data records
- Synthetic data is clearly flagged with provenance metadata in all systems

---

## 6. Controls and Safeguards

### 6.1 Access Controls

#### 6.1.1 Data Access Tiers

Training data is classified into access tiers with associated controls:

| Tier | Classification | Authentication | Authorization | Network Controls | Examples |
|---|---|---|---|---|---|
| **Tier 0** | Public/Synthetic (non-sensitive) | Okta SSO | Role-based | Standard VPC | Public datasets, fully synthetic data |
| **Tier 1** | Internal (de-identified, non-PHI) | Okta SSO + MFA | Group + Purpose-based | Private subnet, VPC | De-identified clinical analytics data |
| **Tier 2** | Sensitive (PHI, PII, financial) | Okta SSO + MFA + device trust | Individual + Purpose-based + time-bound | Isolated VPC, audit logging | PHI-containing clinical data, credit data |
| **Tier 3** | Regulated High-Risk (EU clinical, credit) | Okta SSO + MFA + device trust + geo-fencing | Individual + legal basis check + DPO approval | Isolated VPC, geo-restricted, enhanced monitoring | EU patient data for high-risk AI |

All access to Tier 2 and Tier 3 data requires:
- Documented business justification
- Manager approval
- Completion of data-specific access training
- Signed data handling acknowledgment

#### 6.1.2 Access Reviews

- Tier 2 access: Reviewed quarterly by data steward
- Tier 3 access: Reviewed monthly by data steward and CPO
- All access: Automatically revoked after 90 days of inactivity
- Emergency access: Break-glass procedure available with mandatory post-hoc review within 24 hours

### 6.2 Encryption and Data Protection

- **At Rest:** All training data encrypted using AWS KMS with customer-managed keys. AES-256 encryption standard.
- **In Transit:** TLS 1.3 required for all data transfer. Mutual TLS for service-to-service communication within the data pipeline.
- **Key Management:** Key rotation every 90 days. Separate keys per data tier.
- **Data Masking:** PHI and direct identifiers masked in development and testing environments. Re-identification capability limited to production environments with enhanced controls.

### 6.3 Audit Logging

All operations on training data are logged with the following details:
- Actor (user ID or service account)
- Action (read, write, copy, delete, download)
- Resource (dataset ID, version, specific object)
- Timestamp
- Source IP and device information
- Success/failure status
- Purpose code (from access request)

Audit logs are centralized in Datadog and retained for a minimum of 3 years for Tier 0-1 data and 6 years for Tier 2-3 data.

### 6.4 Environment Segregation

- **Production Data Zone:** Contains released, immutable dataset versions used for production model training
- **Staging Data Zone:** Contains datasets under review prior to release
- **Development Data Zone:** Contains draft datasets and experimentation data; Tier 2+ data restricted to de-identified subsets
- **Sandbox Data Zone:** Isolated environment for initial data exploration and vendor data evaluation

Data may not move from a lower-security zone to a higher-security zone without re-passing all quality and bias gates.

### 6.5 Business Associate Agreements

Where training data is sourced from or involves HIPAA-covered entities, a Business Associate Agreement (BAA) shall be in place prior to data receipt. The Legal department maintains BAA records. The AI/ML Lead shall verify BAA coverage exists before initiating data transfer from a covered entity source. Any data sharing with vendors or partners involving PHI requires a downstream BAA executed by the Legal department.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators

| KPI | Target | Measurement Method | Reporting Frequency |
|---|---|---|---|
| Data Quality Score (aggregate) | ≥ 92% for high-risk datasets | Automated quality suite | Weekly |
| Dataset Documentation Completeness | 100% of released datasets have complete Data Card | MLflow Registry audit | Monthly |
| Labeling Inter-Rater Reliability | Kappa ≥ 0.7 for clinical tasks | FACET dashboard | Per batch + monthly |
| Bias Assessment Completion | 100% of high-risk datasets assessed within 30 days of creation | Governance tracking | Monthly |
| Access Review Timeliness | 100% completed within 5 days of scheduled review | IAM audit reports | Quarterly |
| Data Drift Alert Response Time | Acknowledged within 4 hours; investigated within 24 hours | PagerDuty + Datadog | Continuous |
| Open Critical Quality Issues | Zero open >10 business days | Jira tracking | Weekly |
| Training Compliance Rate | 100% of data handlers current on required training | LMS report | Monthly |

### 7.2 Data Drift Monitoring

Production model input data shall be monitored for drift relative to training data distributions. The Meridian Model Monitoring Service (Datadog + custom metrics pipeline) shall:

- Compute population stability index (PSI) for key features daily
- Trigger a PagerDuty alert when PSI > 0.25 for any high-risk model feature
- Generate weekly drift summary reports for AI/ML Leads
- Maintain a drift history dashboard for trend analysis

### 7.3 Reporting Cadence

| Report | Audience | Frequency | Prepared By |
|---|---|---|---|
| Training Data Operations Dashboard | VP of Engineering, AI/ML Leads | Weekly | Data Engineering |
| Data Quality Trend Report | AI/ML Engineering, CCO | Monthly | Data Engineering |
| Bias and Fairness Summary | CAIO, AI Ethics function | Quarterly | AI/ML Leads (compiled by CAIO office) |
| Training Data Compliance Report | Board AI Governance Committee | Semi-Annual | CAIO + CCO |
| Dataset Inventory and Health | VP of Engineering, CISO | Monthly | Data Engineering |
| Labeling Operations Metrics | Clinical AI Products, Financial Services | Monthly | AI/ML Leads |

### 7.4 Management Review

The AI Data Governance Review Board (chaired by CAIO) shall convene quarterly to:
- Review KPI performance against targets
- Evaluate escalated issues and exceptions
- Approve updates to quality thresholds
- Assess regulatory compliance status
- Prioritize data curation backlog items

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types

Exceptions to this SOP may be requested for:
- **Sourcing Exception:** Use of a data source not meeting standard sourcing requirements
- **Quality Exception:** Use of a dataset not meeting quality thresholds
- **Labeling Exception:** Deviation from dual-annotation or inter-rater reliability requirements
- **Bias Exception:** Proceeding despite unresolved bias findings
- **Documentation Exception:** Deferred Data Card or documentation completion

### 8.2 Exception Request Process

**Step 1: Exception Request Submission**
The AI/ML Lead submits an Exception Request through the Meridian AI Governance Portal, including:
- SOP section(s) for which exception is requested
- Nature and rationale for the exception
- Impact assessment on model risk, safety, and fairness
- Compensating controls proposed
- Duration for which the exception is needed
- Plan for achieving compliance (if temporary exception)

**Step 2: Review and Approval**

| Exception Type | Approval Authority | Consultation Required |
|---|---|---|
| Non-high-risk, minor deviation | AI/ML Lead (self-approve, notify VP Eng) | None |
| Non-high-risk, major deviation | VP of Engineering | CCO |
| High-risk, any deviation | CAIO | CCO, Domain SME, CPO (if privacy-related) |
| Cross-border data transfer exception | CAIO + CPO | Legal |

Approval SLA: 3 business days for non-high-risk; 7 business days for high-risk.

**Step 3: Exception Register**
All approved exceptions are logged in the Exceptions Register maintained by the CAIO office, with tracking of:
- Exception identifier and requestor
- Approval details and date
- Expiration date (exceptions are time-bound; maximum 12 months)
- Conditions attached
- Closure criteria

### 8.3 Escalation Path

Issues that cannot be resolved at the AI/ML Lead level shall be escalated as follows:

1. **AI/ML Lead** → **VP of Engineering** (David Park): Operational issues, resource constraints, tooling needs
2. **VP of Engineering** → **Chief AI Officer** (Dr. Marcus Rivera): Policy interpretation, high-risk dataset decisions, cross-business-unit issues
3. **CAIO** → **CEO** (Dr. Sarah Chen): Enterprise risk decisions, significant regulatory findings
4. **Concurrent escalation to CISO** (Rachel Kim): Security incidents, data breaches
5. **Concurrent escalation to CPO/DPO** (Dr. Klaus Weber): Privacy concerns, data subject rights issues
6. **Concurrent escalation to CCO** (Thomas Anderson): Regulatory compliance matters

### 8.4 Emergency Procedures

In the event of a critical data quality or integrity issue that could impact patient safety or create significant financial risk:
1. The discovering party immediately notifies the AI/ML Lead and VP of Engineering via PagerDuty
2. VP of Engineering may issue an emergency "Stop Use" order for the affected dataset
3. The Model Risk Committee is convened within 24 hours
4. All models consuming the affected dataset are identified and assessed for potential impact
5. Remediation plan developed and executed
6. Post-incident review conducted per SOP-RM-001 (Incident Management)

---

## 9. Training Requirements

### 9.1 Required Training Modules

| Training Module | Target Audience | Frequency | Delivery Method |
|---|---|---|---|
| **TDM-101: Training Data Management Fundamentals** | All AI/ML Engineering personnel, Data Scientists, Data Engineers | Onboarding + Annual | LMS e-learning |
| **TDM-201: Bias Awareness and Fairness in Training Data** | All AI/ML Engineering personnel, AI/ML Leads, Domain SMEs | Onboarding + Annual | Instructor-led workshop |
| **TDM-301: Clinical Data Curation for High-Risk AI** | Personnel working on Clinical AI Platform datasets | Onboarding + Annual | E-learning + case studies |
| **TDM-302: Financial Data Curation and Fair Lending** | Personnel working on HealthPay Financial Services models | Onboarding + Annual | E-learning + regulatory overview |
| **TDM-401: Labeling Protocol Development and Quality Management** | Annotator supervisors, Labeling project leads | Onboarding + Bi-annual | Workshop + certification |
| **TDM-501: Data Privacy and Security for AI/ML** | All personnel with data access | Onboarding + Annual | LMS e-learning |
| **TDM-601: Annotator Certification Program** | All internal and external annotators | Role-specific initial + Annual renewal | Task-specific training + exam |

### 9.2 Training Tracking and Compliance

- Training completion is tracked through Meridian's Learning Management System (LMS)
- Managers receive monthly compliance reports for their teams
- Training must be completed within 30 days of onboarding or role change
- Expired training results in data access suspension until remediated
- Completion rate reported in monthly KPI dashboard

### 9.3 Training Content Ownership

- TDM-101, 201, 401, 601: Maintained by CAIO office
- TDM-301: Maintained by Clinical AI Products (Dr. Aisha Okafor)
- TDM-302: Maintained by Financial Services (Robert Liu)
- TDM-501: Maintained by CISO office (Rachel Kim)

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs and Policies

| Document ID | Title | Relationship |
|---|---|---|
| SOP-AIML-001 | AI/ML Model Development Lifecycle | Defines end-to-end model development process; this SOP governs data aspects |
| SOP-AIML-003 | Model Validation and Performance Monitoring | References data quality and drift metrics from this SOP |
| SOP-AIML-004 | High-Risk AI System Governance | Defines additional controls for high-risk systems that use data governed by this SOP |
| SOP-SEC-008 | Third-Party Vendor Security Assessment | Referenced for external data provider evaluation |
| SOP-PRIV-001 | Data Protection and Privacy Governance | Governs privacy aspects of data handling referenced in this SOP |
| SOP-PRIV-003 | Data Subject Access Request Handling | Referenced for handling requests that may involve training data |
| SOP-DATA-003 | Data Classification and Handling | Defines data classification tiers used in this SOP |
| SOP-DATA-007 | Operational Analytics Data Governance | Governs related but out-of-scope operational data |
| SOP-RM-001 | Incident Management and Response | Referenced for emergency procedures |
| SOP-QA-002 | Software Quality Assurance | Referenced for preprocessing pipeline testing requirements |
| POL-HR-012 | Employee Data Privacy | Governs out-of-scope employee data |

### 10.2 External Standards and Frameworks

- NIST AI Risk Management Framework (AI RMF 1.0)
- ISO/IEC 42001:2023 — Artificial Intelligence Management System
- ISO/IEC 25012 — Data Quality Model
- Federal Reserve SR 11-7 — Model Risk Management Guidance
- Datasheets for Datasets (Gebru et al., 2021) — Referenced for Data Card structure

### 10.3 Regulatory References

- EU AI Act (Regulation 2024/1689), particularly Articles 10, 13, 14, and Annex III
- HIPAA Privacy and Security Rules (45 CFR Parts 160, 164)
- SOC 2 Trust Services Criteria (Security, Availability, Confidentiality)

---

## 11. Revision History

| Version | Date | Author | Approver | Description of Changes |
|---|---|---|---|---|
| 1.0 | 2023-02-15 | David Park | Dr. Marcus Rivera | Initial creation of Training Data Management SOP |
| 1.1 | 2023-08-30 | Data Governance Team | David Park | Added labeling protocol requirements; minor quality metric adjustments |
| 2.0 | 2024-05-01 | Dr. Marcus Rivera | David Park | Major revision for EU AI Act readiness; added high-risk controls, Data Card requirements, bias assessment section; expanded roles for CAIO |
| 2.1 | 2025-03-12 | CAIO Office | Dr. Marcus Rivera | Updated for HITRUST CSF certification alignment; refined access tiers; added synthetic data section; updated organizational references |
| 2.2 | 2025-09-22 | Dr. Marcus Rivera | David Park | Revised quality thresholds for high-risk datasets; added data drift monitoring section; updated SLA targets; incorporated feedback from SOC 2 Type II audit; updated for CE marking requirements |

---

**Document Status:** Active  
**Next Scheduled Review:** 2027-02-13  
**Document Owner:** Dr. Marcus Rivera, Chief AI Officer  
**Questions or Comments:** Submit via the Meridian AI Governance Portal or email ai-governance@meridian-health.com

---

**END OF DOCUMENT**
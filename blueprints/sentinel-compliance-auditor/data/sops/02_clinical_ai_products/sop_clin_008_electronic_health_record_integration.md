---
sop_id: "SOP-CLIN-008"
title: "Electronic Health Record Integration"
business_unit: "Clinical AI Products"
version: "2.4"
effective_date: "2024-12-02"
last_reviewed: "2025-10-19"
next_review: "2026-04-04"
owner: "Dr. Aisha Okafor, VP of Clinical AI Products"
approver: "Dr. Priya Patel, Chief Medical Officer"
classification: "Internal"
regulations:
  - "HIPAA"
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Electronic Health Record Integration

**SOP-ID:** SOP-CLIN-008
**Business Unit:** Clinical AI Products
**Version:** 2.4
**Effective Date:** 2024-12-02
**Classification:** Internal

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the standardized framework for designing, implementing, validating, and maintaining Electronic Health Record (EHR) integrations for Meridian Health Technologies' Clinical AI Platform. The purpose is to ensure that all clinical data ingested from external EHR systems for AI-driven clinical decision support, diagnostic imaging analysis, patient risk scoring, and adverse event prediction maintains semantic fidelity, technical robustness, and data integrity from source to model inference endpoint.

This SOP defines the mandatory processes by which integration engineers, clinical informaticists, and quality assurance personnel design interface specifications, execute data mapping, perform integration testing, and transition integrations to production operations. Adherence to this SOP is required to ensure that the Clinical AI Platform receives validated, clinically accurate data that preserves patient safety and supports regulatory compliance obligations under the EU AI Act for high-risk AI systems.

### 1.2 Scope

This SOP applies to all EHR integration activities involving the Clinical AI Platform, including:

| In Scope | Out of Scope |
|---|---|
| HL7 FHIR R4-based integrations with certified EHR systems (Epic, Cerner, Meditech, Allscripts, Dedalus, etc.) | Integration with non-EHR clinical data sources (wearables, patient-reported outcomes via mobile apps) |
| HL7v2 interface integrations for legacy EHR environments | HealthPay Financial Services payment data integrations |
| Bi-directional data flows (EHR-to-Meridian and Meridian-to-EHR for clinical decision support results) | MedInsight Analytics population health data feed integrations |
| Data mapping, transformation, and validation activities | Internal Meridian SaaS Platform infrastructure changes |
| Integration testing (unit, functional, integration, User Acceptance Testing) | Product feature development |
| Production monitoring of integration health and data quality | Model training or retraining activities |

### 1.3 Applicability

This SOP applies to the following personnel and teams:

- Clinical AI Products Engineering team (integration engineers, data engineers)
- Clinical Informatics team
- Quality Assurance (QA) team, Clinical AI Products
- Customer Operations team (implementation managers, technical account managers)
- Information Security team (for security review of integration architectures)
- Clinical Safety team (for clinical validation of data mappings)
- Any third-party contractors or vendors performing EHR integration work on behalf of Meridian Health Technologies

### 1.4 Compliance Obligations

All EHR integrations must comply with:

- Health Insurance Portability and Accountability Act (HIPAA) Privacy, Security, and Breach Notification Rules
- EU AI Act high-risk AI system requirements for data governance (Article 10)
- SOC 2 Type II trust services criteria (Security, Availability, Confidentiality)
- GDPR data protection requirements for EU data subjects
- Meridian Clinical AI Platform quality management system requirements
- Applicable client-site data governance and information security policies, as documented in contractual agreements

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Clinical Data Mapping** | The process of defining correspondence between data elements in a source EHR system and the target Clinical AI Platform data model, including transformation rules, terminology mappings, and value set constraints |
| **Data Provenance** | Metadata that captures the origin, lineage, and transformation history of clinical data ingested into the platform, enabling traceability from AI output back to source record |
| **FHIR Endpoint** | A URL-addressable server that exposes HL7 FHIR RESTful API resources for data exchange |
| **Integration Instance** | A single, uniquely identified EHR integration deployment serving a specific healthcare provider organization, with its own configuration, mappings, and data flow |
| **Semantic Validation** | Clinical review process that verifies mapped data preserves intended clinical meaning, including concept equivalence across terminologies (SNOMED CT, LOINC, RxNorm, ICD-10-CM) |
| **Source EHR System** | The external EHR application from which patient health data originates and is transmitted to the Clinical AI Platform |
| **Transformation Pipeline** | The sequence of data processing steps applied to incoming EHR data, including parsing, validation, terminology mapping, normalization, enrichment, and persistence |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| **API** | Application Programming Interface |
| **BBFH** | Bulk FHIR (Flat FHIR for population-level data export) |
| **CDS** | Clinical Decision Support |
| **CDA** | Clinical Document Architecture |
| **EHR** | Electronic Health Record |
| **FHIR** | Fast Healthcare Interoperability Resources |
| **HL7** | Health Level Seven International |
| **IG** | Implementation Guide |
| **LOINC** | Logical Observation Identifiers Names and Codes |
| **MLLP** | Minimal Lower Layer Protocol |
| **PHI** | Protected Health Information |
| **REST** | Representational State Transfer |
| **SNOMED CT** | Systematized Nomenclature of Medicine Clinical Terms |
| **UAT** | User Acceptance Testing |
| **USCDI** | United States Core Data for Interoperability |

---

## 3. Roles and Responsibilities

The following RACI matrix defines roles and responsibilities for EHR integration activities.

| Activity / Decision | Integration Engineer | Clinical Informaticist | QA Engineer | Implementation Manager | Information Security | Clinical Safety Lead | VP Clinical AI |
|---|---|---|---|---|---|---|---|
| **Integration Requirements Definition** | C | R | I | A | I | C | I |
| **Interface Specification Design** | R | C | I | I | C | I | A |
| **Data Mapping Development** | R | A | I | I | I | C | I |
| **Semantic Validation** | I | R | I | I | I | A | I |
| **Security Architecture Review** | C | I | I | I | R | I | A |
| **Integration Testing Execution** | R | C | R | I | I | I | I |
| **UAT Coordination** | C | C | I | R | I | C | A |
| **Production Deployment** | R | I | I | A | C | I | I |
| **Post-Go-Live Monitoring** | C | I | I | R | I | I | A |
| **Exception Approval** | I | I | I | C | I | C | R |
| **Regulatory Compliance Verification** | I | C | I | C | R | R | A |

**Key:** R = Responsible (does the work), A = Accountable (signs off), C = Consulted (provides input), I = Informed (receives updates)

### 3.1 Named Role Assignments

| Role | Primary Individual | Delegation Authority |
|---|---|---|
| Integration Engineering Lead | David Park, VP of Engineering | Senior Integration Engineers |
| Clinical Informatics Lead | Dr. Aisha Okafor, VP of Clinical AI Products | Clinical Informaticists |
| Clinical Safety Lead | Dr. Priya Patel, Chief Medical Officer | Clinical Safety Team |
| Information Security Lead | Rachel Kim, CISO | Security Architecture Team |
| Customer Operations Lead | Michael Chang, VP of Customer Operations | Implementation Managers |
| Quality Assurance Lead | QA Manager, Clinical AI Products | Senior QA Engineers |
| Regulatory Compliance Lead | Thomas Anderson, Chief Compliance Officer | Compliance Team |

---

## 4. Policy Statements

### 4.1 Integration Architecture Standards

All EHR integrations must adhere to the following architecture standards:

1. **FHIR-First Architecture**: HL7 FHIR R4 shall be the default interoperability standard for all new integrations. HL7v2 and CDA-based integrations are permitted only for legacy EHR systems where FHIR interfaces are not available, subject to documented justification and approval by the VP of Clinical AI Products.

2. **API-Based Integration**: All integrations shall use RESTful API patterns with OAuth 2.0 authentication and TLS 1.2+ encryption in transit. Direct database-level access to source EHR systems is prohibited.

3. **Bi-Directional Communication**: Integrations must support both data ingestion (EHR-to-Platform) and results delivery (Platform-to-EHR) using FHIR resources appropriate to the clinical use case.

4. **Data Minimization**: Integrations shall request and ingest only the minimum necessary data elements required for the specific Clinical AI Platform feature being deployed. Bulk, unfiltered data requests are prohibited.

5. **Idempotency**: Integration pipelines must handle duplicate messages gracefully, preventing duplicate patient records or clinical observations.

### 4.2 PHI Handling Requirements

Protected Health Information (PHI) ingested through EHR integrations shall be handled according to the following requirements:

1. All PHI transmitted from source EHR systems must be encrypted in transit using TLS 1.2 or higher.

2. PHI at rest within the Meridian SaaS Platform must be encrypted using AES-256 encryption.

3. All clinical data received through integrations shall be considered PHI by default and handled according to Meridian's data protection policies.

4. Access to PHI within the integration pipeline (logs, error queues, data stores) shall be restricted to personnel with documented PHI access authorization.

5. PHI shall not be used in non-production environments unless de-identified in accordance with the HIPAA Safe Harbor method.

6. Integration engineers and clinical informaticists must complete annual HIPAA and Security Awareness training prior to accessing any integration infrastructure.

### 4.3 Business Associate Agreement Requirement

A fully executed Business Associate Agreement (BAA) with the client healthcare organization must be in place before any PHI can be transmitted through an EHR integration.

The Implementation Manager is responsible for verifying BAA execution status during the integration kickoff process. Integration engineers shall not commence data mapping work until the Implementation Manager confirms the BAA status in the Integration Project Record.

### 4.4 Clinical Safety

All EHR integrations involving clinical data ingestion for AI model inference must undergo clinical safety review. The Clinical Safety Lead (or delegate) must approve data mappings for safety-critical data elements, including:

- Patient demographics used for patient matching
- Medication orders and administration records
- Laboratory results used for critical value detection
- Allergy and adverse reaction records
- Problem list and diagnosis codes

### 4.5 Fairness and Bias Considerations

Integration engineers shall document any demographic or clinical characteristic data that could be used in algorithmic fairness evaluations. When integrating demographic data from EHRs, integration specifications must capture relevant categories (as defined in applicable Meridian AI fairness documentation) to enable downstream bias monitoring.

---

## 5. Detailed Procedures

This section describes the end-to-end lifecycle of an EHR integration instance, organized by phase. Each phase includes required inputs, procedural steps, required outputs, and quality gates.

---

### 5.1 Phase 1: Integration Intake and Scoping

#### 5.1.1 Procedure Steps

| Step | Action | Responsible Role | Tools / Systems |
|---|---|---|---|
| 1.1 | Client submits EHR Integration Request through Customer Operations portal | Customer Operations | Jira Service Management |
| 1.2 | Implementation Manager triages request and assigns to Clinical AI Products team | Implementation Manager | Jira, Salesforce |
| 1.3 | Integration Engineer conducts EHR system discovery call with client IT team to identify: EHR vendor and version, available FHIR endpoints, authentication method (OAuth 2.0 SMART on FHIR), supported FHIR resources, terminology systems in use, patient population scope | Integration Engineer | Confluence Discovery Template, Video Conference |
| 1.4 | Clinical Informaticist reviews requested Clinical AI Platform features and identifies required data elements | Clinical Informaticist | Data Requirements Catalog (Confluence) |
| 1.5 | Integration Engineer produces Integration Scope Document containing: technical environment summary, required FHIR resources and operations, data flow diagram, preliminary data volume estimates, anticipated timeline | Integration Engineer | Integration Scope Document Template (Google Docs) |
| 1.6 | VP of Clinical AI Products reviews and approves Integration Scope Document | VP Clinical AI | Jira Approval Workflow |

#### 5.1.2 Phase 1 Quality Gate

| Criterion | Validated By | Evidence Required |
|---|---|---|
| EHR system FHIR capability assessment complete | Integration Engineer | Completed Discovery Template |
| All Clinical AI features requiring EHR data documented | Clinical Informaticist | Signed-off Data Requirements Catalog entry |
| BAA execution verified | Implementation Manager | Contract Management System confirmation |
| Integration Scope Document approved | VP Clinical AI | Jira approval record |

#### 5.1.3 Phase 1 Outputs

- Approved Integration Scope Document
- Completed EHR Technical Discovery Template
- Integration project record established in Jira

---

### 5.2 Phase 2: Interface Specification Design

#### 5.2.1 Procedure Steps

| Step | Action | Responsible Role | Tools / Systems |
|---|---|---|---|
| 2.1 | Integration Engineer defines FHIR API specification: base FHIR endpoint URL, SMART on FHIR OAuth scopes requested, FHIR search parameters and included resources, pagination strategy, error handling patterns | Integration Engineer | OpenAPI Specification Document |
| 2.2 | Integration Engineer specifies data ingestion workflow: polling interval or subscription mechanism, batch size limits, retry and dead-letter queue configuration, deduplication logic | Integration Engineer | Confluence Technical Specification Template |
| 2.3 | Information Security reviews authentication architecture, encryption configuration, and network security controls | Information Security | Security Review Checklist |
| 2.4 | Clinical Informaticist produces preliminary data mapping document identifying: source FHIR resource / element path, target Meridian Clinical Data Model field, mapping type (direct, transform, lookup, conditional), terminology services required | Clinical Informaticist | Data Mapping Spreadsheet (Google Sheets) |
| 2.5 | Integration Engineer documents non-functional requirements: uptime requirements, latency budgets, throughput expectations, alerting thresholds | Integration Engineer | Non-Functional Requirements Section of Tech Spec |
| 2.6 | Clinical Safety Lead reviews for patient safety impact and assigns clinical safety classification (safety-critical, safety-relevant, non-safety) | Clinical Safety Lead | Jira Clinical Safety Review workflow |

#### 5.2.2 Phase 2 Quality Gate

| Criterion | Validated By | Evidence Required |
|---|---|---|
| FHIR API specification complete and reviewed | Integration Engineering Lead | Approved OpenAPI Spec |
| Security architecture approved | Information Security | Approved Security Review Checklist |
| Clinical safety review completed | Clinical Safety Lead | Jira safety review record |
| Interface Specification signed off | VP Clinical AI | Sign-off in Jira |

#### 5.2.3 Phase 2 Outputs

- Approved Interface Specification Document
- Preliminary Data Mapping Document
- Security Architecture Review approval
- Clinical Safety Classification assignment

---

### 5.3 Phase 3: Data Mapping Development and Semantic Validation

#### 5.3.1 Data Mapping Categories

Data mappings are classified into three categories, each with specific validation requirements:

| Category | Description | Validation Requirement | Review Authority |
|---|---|---|---|
| **Category A – Safety-Critical** | Data elements that directly influence clinical decisions where error could result in patient harm (e.g., allergies, medications, lab results triggering critical alerts) | Full semantic validation, clinical review, and UAT on all records | Clinical Safety Lead |
| **Category B – Clinically Relevant** | Data elements that influence clinical AI output but with lower direct harm potential (e.g., problem list, encounters, procedures) | Semantic validation on representative sample, clinical informaticist review | Clinical Informaticist |
| **Category C – Administrative/Operational** | Data elements that do not influence clinical AI output (e.g., appointment types, facility codes, billing data used for operational reporting) | Standard validation against terminology server | Integration Engineering Lead |

#### 5.3.2 Procedure Steps

| Step | Action | Responsible Role | Tools / Systems |
|---|---|---|---|
| 3.1 | Integration Engineer creates Final Data Mapping Document extending the preliminary mapping with: transformation logic for each source-to-target mapping, terminology mapping table with code system and version specified, NULL and missing data handling rules, edge case handling instructions | Integration Engineer | Data Mapping Spreadsheet, Confluence |
| 3.2 | For mappings involving terminology translation (e.g., local codes to SNOMED CT, local LOINC variants to standard LOINC), Clinical Informaticist validates concept equivalence | Clinical Informaticist | Terminology Server (e.g., Ontoserver) |
| 3.3 | Clinical Informaticist performs Semantic Validation Review, documenting for each Category A and B mapping: clinical concept equivalence confirmed, value domain constraints verified, any clinical meaning loss due to data model differences documented, risk of incorrect clinical inference assessed | Clinical Informaticist | Semantic Validation Report Template |
| 3.4 | For any mapping where perfect semantic equivalence cannot be achieved, Clinical Informaticist documents the limitation and proposes a mitigation (e.g., flagging in the enrichment pipeline for downstream model awareness) | Clinical Informaticist | Data Mapping Limitation Register |
| 3.5 | Clinical Safety Lead reviews and approves Category A mappings | Clinical Safety Lead | Jira Clinical Safety Approval |

#### 5.3.3 Semantic Validation Standards

The following minimum semantic validation standards apply:

1. **Terminology Mapping Validation**: For all Category A mappings involving coded concepts, at least two clinical informaticists must independently validate that the target code represents the same clinical concept as the source code.

2. **Value Set Validation**: Where source data is constrained by value sets (e.g., observation value, medication code), the clinical informaticist must verify that the full value set semantics are preserved, including negation contexts, provenance, and effective periods.

3. **Unit and Reference Range Validation**: For laboratory result mappings, unit of measure conversions and reference range mappings must be validated against the client EHR laboratory compendium.

4. **Clinical Context Preservation**: Where data elements derive clinical meaning from related resources (e.g., medication route from MedicationRequest, condition stage from Condition), the mapping must preserve or explicitly document the loss of contextual relationships.

#### 5.3.4 Phase 3 Quality Gate

| Criterion | Validated By | Evidence Required |
|---|---|---|
| Final Data Mapping Document complete for all data elements | Integration Engineer | Completed Mapping Spreadsheet |
| Semantic validation reports approved for all Categories A-C | Clinical Informaticist | Approved Semantic Validation Reports |
| All Category A mappings reviewed by Clinical Safety | Clinical Safety Lead | Jira approval |
| Data mapping limitation register reviewed and accepted | VP Clinical AI | Approved Limitation Register |

---

### 5.4 Phase 4: Integration Build and Configuration

#### 5.4.1 Procedure Steps

| Step | Action | Responsible Role | Tools / Systems |
|---|---|---|---|
| 4.1 | Integration Engineer configures Meridian FHIR Gateway: registers client EHR FHIR server as a trusted source, configures OAuth 2.0 client credentials and SMART scopes, sets up subscription/webhook or polling-based trigger mechanism | Integration Engineer | Meridian Integration Hub, AWS Secrets Manager |
| 4.2 | Integration Engineer builds Transformation Pipeline based on approved Data Mapping Document: Apache Beam or equivalent pipeline code implementing all mapping rules, terminology server integration for code translation, data validation rules (schema, referential integrity, value domain), enrichment steps (identifiers assignment, provenance metadata generation), persistence layer writes to Meridian Clinical Data Store | Integration Engineer | Apache Beam, Google Cloud Dataflow, Meridian Clinical Data Store |
| 4.3 | Integration Engineer configures integration-specific Operational Data Store tables if required for performance | Integration Engineer | PostgreSQL (Aurora) |
| 4.4 | Integration Engineer configures monitoring dashboards and alerts (see Section 7) | Integration Engineer | Datadog, PagerDuty |
| 4.5 | Integration Engineer configures logging to capture: successful FHIR interactions (counts, latency), FHIR error responses from source, transformation errors and exceptions, data validation failures, deduplication actions | Integration Engineer | Elasticsearch, Kibana |

#### 5.4.2 Phase 4 Quality Gate

| Criterion | Validated By | Evidence Required |
|---|---|---|
| Pipeline configuration matches approved Data Mapping Document | Integration Engineering Lead | Code review record (GitHub Pull Request) |
| All credentials stored in Secrets Manager | Information Security | Automated check |
| Monitoring dashboards configured per Section 7 requirements | DevOps Engineer | Screenshot of dashboard |
| Pipeline deployed to `integration-dev` environment and passing smoke tests | Integration Engineer | CI/CD pipeline status |

---

### 5.5 Phase 5: Integration Testing

Integration testing is executed in staged environments. No patient data is used in non-production environments unless de-identified.

#### 5.5.1 Testing Environments

| Environment | Purpose | Data Permitted | Access Control |
|---|---|---|---|
| `integration-sandbox` | Developer environment for pipeline development | Synthetic test data only | Integration Engineering team |
| `integration-staging` | Pre-production testing with client-provided test FHIR endpoint | De-identified synthetic data; client-provided test patients only | Integration Engineering, QA, Clinical Informatics |
| `integration-prod` | Production integration instance | Live PHI | Restricted (see Section 6) |

#### 5.5.2 Testing Phases

**A. Unit Testing**

| Activity | Responsibility | Criteria |
|---|---|---|
| Test each transformation rule independently against synthetic input | Integration Engineer | 100% of transformation rules pass defined input/output assertions |
| Test terminology mapping lookups against terminology server | Integration Engineer | All mapped codes resolve to expected target codes |
| Test error handling and dead-letter queue routing | Integration Engineer | All defined error scenarios produce expected dead-letter entries |

**B. Functional Testing**

| Activity | Responsibility | Criteria |
|---|---|---|
| End-to-end test with FHIR test server simulating realistic EHR responses | QA Engineer | All FHIR resource types ingested, processed, and persisted as expected |
| Duplicate message handling validation | QA Engineer | Duplicate messages do not create duplicate clinical records |
| Authentication failure and token expiry scenarios | QA Engineer | Integration handles gracefully with appropriate alerting |
| Backpressure and throttling behavior | QA Engineer | Pipeline degrades gracefully under high load |

**C. Integration Testing with Client Test Environment**

| Activity | Responsibility | Criteria |
|---|---|---|
| Connectivity established between Meridian `integration-staging` and client's FHIR test endpoint | Integration Engineer, Client IT | Successful FHIR CapabilityStatement exchange |
| Sample clinical data (test patients) ingested and processed | Integration Engineer | All defined FHIR resource types processed; data mappings verified against client-provided sample data |
| CDS result delivery verified (inbound and outbound flow) | Integration Engineer | End-to-end round-trip within latency budget |

**D. User Acceptance Testing (UAT)**

UAT is coordinated by the Implementation Manager with designated client clinical and IT stakeholders.

| Activity | Responsibility | Criteria |
|---|---|---|
| UAT Test Plan documented and agreed with client | Implementation Manager | Signed UAT Test Plan |
| Client users execute defined test scenarios in test environment | Client UAT Participants | All defined scenarios pass |
| Client clinical users validate that mapped data correctly represents clinical context | Client Clinical Stakeholders | UAT Sign-off Form signed by client |

#### 5.5.3 UAT Sign-off Requirements

Before production deployment, the following sign-offs must be obtained:

| Sign-off | Approver | Record / Location |
|---|---|---|
| Internal QA Sign-off | QA Engineer | Jira |
| Client Technical Sign-off | Client IT Lead | UAT Sign-off Form (DocuSign) |
| Client Clinical Sign-off | Client Clinical Lead | UAT Sign-off Form (DocuSign) |
| Meridian Clinical Informatics Sign-off | Clinical Informaticist | Jira |
| Meridian Clinical Safety Sign-off (for integrations with Category A mappings) | Clinical Safety Lead | Jira |
| Production Go/No-Go Decision | VP Clinical AI Products | Jira |

#### 5.5.4 Phase 5 Quality Gate

| Criterion | Validated By | Evidence Required |
|---|---|---|
| All testing phases completed and passed | QA Engineer | Test reports (Jira, Zephyr) |
| UAT Sign-off Forms executed | Implementation Manager | DocuSign records |
| All critical/high defects resolved or waived | QA Engineer | Defect tracker (Jira) |
| Clinical Safety sign-off obtained (if applicable) | Clinical Safety Lead | Jira approval |

---

### 5.6 Phase 6: Production Deployment

#### 5.6.1 Deployment Prerequisites

Before production deployment, all of the following must be confirmed:

- BAA executed and verified
- All Phase 5 sign-offs obtained
- Production FHIR endpoint URL and credentials validated
- Monitoring dashboards configured and alerting thresholds set
- Rollback plan documented and approved
- Deployment window scheduled with client notification (minimum 5 business days advance notice)

#### 5.6.2 Deployment Steps

| Step | Action | Responsibility |
|---|---|---|
| 6.1 | Apply infrastructure changes using Terraform: production FHIR Gateway configuration, production pipeline deployment, production monitoring rules | Integration Engineer |
| 6.2 | Validate production connectivity to client FHIR server (read-only test) | Integration Engineer |
| 6.3 | Execute initial data ingestion with monitoring observation | Integration Engineer, QA Engineer |
| 6.4 | Verify initial data load integrity: patient counts within expected range, no data validation errors exceeding warning threshold | QA Engineer |
| 6.5 | Verify CDS result delivery mechanism: test result written back to client FHIR server (if bi-directional) | Integration Engineer |
| 6.6 | Transition monitoring to Operations Team and Customer Operations | DevOps Engineer, Implementation Manager |

#### 5.6.3 Phase 6 Quality Gate

| Criterion | Validated By | Evidence Required |
|---|---|---|
| Production connectivity validated | Integration Engineer | Successful CapabilityStatement exchange in production logs |
| Initial data load integrity confirmed | QA Engineer | QA sign-off in Jira |
| Operations hand-off completed | Implementation Manager | Service transition record in ServiceNow |

---

### 5.7 Phase 7: Post-Go-Live Monitoring and Stabilization

#### 5.7.1 Stabilization Period

A 14-calendar-day stabilization period begins at production deployment. During this period:

- The Implementation Manager serves as primary client contact
- Integration Engineering maintains a dedicated escalation path
- All integration alerts are reviewed daily by Integration Engineering and Customer Operations
- Any data quality issue is escalated to Clinical Informatics within 4 hours

#### 5.7.2 Stabilization Exit Criteria

| Criterion | Threshold |
|---|---|
| Data ingestion success rate | ≥ 99.5% over 7 consecutive days |
| Data validation error rate | < 1.0% of total records over 7 consecutive days |
| Zero Category 1 (critical) incidents for 7 consecutive days | 7 consecutive days without critical incident |
| Client confirms clinical data quality acceptable | Client Clinical Lead email confirmation |

#### 5.7.3 Transition to Standard Operations

Upon meeting exit criteria, the integration transitions to standard operations:

- Operations monitoring follows standard integration health monitoring (Section 7)
- Issue escalation follows Clinical AI Platform standard support processes
- Implementation Manager transitions to Technical Account Manager for ongoing relationship management

---

## 6. Controls and Safeguards

### 6.1 Access Controls

| Access Level | Roles | Authorization Mechanism |
|---|---|---|
| **Integration Configuration Admin** | Senior Integration Engineers | AWS IAM role, multi-factor authentication required, approval by VP Engineering |
| **Integration View/Operate** | Integration Engineers, QA Engineers | AWS IAM role |
| **Production Data Access** | Integration Engineers (read-only), Clinical Informaticists (read-only) | PIM (Privileged Identity Management) just-in-time access, session recording enabled |
| **Patient Data View** | Clinical Safety Lead, Clinical Informaticists | PHI access authorization required, access logging enabled |

### 6.2 Encryption Controls

| Data State | Encryption Standard | Key Management |
|---|---|---|
| **Data in Transit** | TLS 1.2+, AES-256-GCM for MLLP channels | AWS Certificate Manager |
| **Data at Rest (Clinical Data Store)** | AES-256, AWS RDS encryption | AWS Key Management Service |
| **Data at Rest (Pipeline Storage)** | AES-256, S3 server-side encryption | AWS Key Management Service |
| **Data at Rest (Logs)** | AES-256, S3 server-side encryption | AWS Key Management Service |

### 6.3 Audit and Logging Controls

Integration activity is logged for operational and security purposes:

| Log Category | Content | Retention Period | Access Controlled To |
|---|---|---|---|
| **FHIR Interaction Logs** | Timestamp, source IP, FHIR operation, resource type, success/failure | 365 days | Integration Engineering, Incident Response |
| **Pipeline Transformation Logs** | Input/output records (de-identified), transformation errors, deduplication events | 90 days | Integration Engineering |
| **Access Logs** | User identity, operation timestamp, resource accessed, success/failure | 365 days | Information Security |

### 6.4 Data De-identification for Non-Production Use

When PHI is required for testing or development, it must be de-identified according to HIPAA Safe Harbor method (18 identifiers removed) prior to use in any non-production environment.

De-identification must be performed using the Meridian-approved de-identification pipeline. Manual de-identification is prohibited.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| KPI | Description | Target | Measurement Method |
|---|---|---|---|
| **Integration Uptime** | Percentage of time integration is operational and ingesting data | ≥ 99.9% | Datadog synthetic monitor polling FHIR endpoint |
| **Data Ingestion Success Rate** | Percentage of FHIR interactions returning success (2xx) | ≥ 99.5% | FHIR Gateway logs aggregated hourly |
| **Data Validation Pass Rate** | Percentage of records passing data validation rules | ≥ 99.0% | Pipeline validation metrics in Datadog |
| **End-to-End Latency (P95)** | Time from FHIR interaction receipt to data availability in Clinical Data Store | < 60 seconds | Pipeline tracing via Datadog APM |
| **Mapping Error Rate** | Percentage of records failing clinical mapping rules | < 0.1% | Pipeline error logs |

### 7.2 Alerting Thresholds

| Alert | Trigger Condition | Severity | Notification Channel | Response SLA |
|---|---|---|---|---|
| **Integration Down** | FHIR Gateway unresponsive for 5 minutes | Critical (P1) | PagerDuty | 15 minutes first response |
| **High Error Rate** | Data ingestion success rate < 95% for 15-minute window | Critical (P1) | PagerDuty | 15 minutes first response |
| **Elevated Error Rate** | Data ingestion success rate < 99% for 1-hour window | High (P2) | PagerDuty | 1 hour first response |
| **Elevated Mapping Errors** | Mapping error rate > 1% for 1-hour window | High (P2) | PagerDuty | 1 hour first response |
| **Latency Threshold Breach** | P95 latency > 120 seconds for 15-minute window | Medium (P3) | Slack, Email | 4 business hours |
| **Missing Data** | Expected FHIR resource type not observed for 24 hours | Medium (P3) | Slack, Email | 4 business hours |

### 7.3 Reporting Cadence

| Report | Frequency | Audience | Contents |
|---|---|---|---|
| **Integration Health Dashboard** | Real-time | Integration Engineering, Customer Operations | Current KPIs, active alerts, ingestion volume |
| **Weekly Integration Report** | Weekly | VP Clinical AI, Implementation Manager (during stabilization) | KPI trends, incident summary, open issues |
| **Monthly Integration Review** | Monthly | VP Clinical AI, Clinical Safety Lead, Customer Operations Lead | All integration instances KPI trends, incident trends, capacity forecast |
| **Quarterly Business Review (per client)** | Quarterly | Client Clinical and IT Leadership, Meridian Technical Account Manager | Integration performance summary, planned maintenance, roadmap |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Handling Hierarchy

Integration exceptions are categorized and routed according to the following matrix:

| Exception Category | First Responder | Escalation Tier 1 | Escalation Tier 2 | Maximum Resolution Time |
|---|---|---|---|---|
| **Connectivity / Infrastructure** | Integration Engineer | Integration Engineering Lead | Infrastructure Engineering | 4 hours |
| **Data Validation Errors** | Integration Engineer | Clinical Informaticist | VP Clinical AI | 24 hours |
| **Semantic / Mapping Errors** | Clinical Informaticist | Clinical Safety Lead | Chief Medical Officer | 12 hours (if Category A) |
| **Security Incident** | Information Security | CISO | Chief Legal Officer | Per Incident Response SOP |
| **Client-reported Clinical Discrepancy** | Clinical Informaticist | Clinical Safety Lead | Chief Medical Officer | 24 hours |

### 8.2 SOP Deviation and Exception Approval Process

Where strict adherence to this SOP is not technically feasible (e.g., legacy EHR system without FHIR capability, use of HL7v2 as interim solution), a formal exception request must be submitted.

#### 8.2.1 Exception Request Process

| Step | Action |
|---|---|
| 1 | Requestor documents the exception in the SOP Exception Request Form referencing the specific procedure step(s) requiring deviation, the justification, the proposed alternative approach, the risk assessment for patient safety and data integrity, and the proposed compensating controls. |
| 2 | Requestor submits the form to the VP of Clinical AI Products for review. |
| 3 | VP Clinical AI consults with Clinical Safety Lead (if safety-critical mappings involved) or CISO (if security controls affected). |
| 4 | VP Clinical AI approves, approves with conditions, or rejects, with decision documented in the Exception Register. |
| 5 | Approved exceptions must include an expiration date not exceeding 12 months. |

### 8.3 Escalation Timelines

| Priority | First Response Timeline | Escalation to Next Tier | Executive Notification |
|---|---|---|---|
| **P1 – Critical** | 15 minutes | 1 hour without resolution | 2 hours: VP Clinical AI, CISO |
| **P2 – High** | 1 hour | 4 hours without resolution | 8 hours: VP Clinical AI |
| **P3 – Medium** | 4 business hours | 24 hours without resolution | N/A |

---

## 9. Training Requirements

### 9.1 Required Training

| Training Module | Required For | Frequency | Delivery Method |
|---|---|---|---|
| **HIPAA and Security Awareness** | All personnel with access to PHI | Annual | Meridian LMS (Workday Learning) |
| **FHIR and HL7v2 Fundamentals** | Integration Engineers, Clinical Informaticists | On hire; refresher every 24 months | External (HL7 International) or internal |
| **EHR Integration SOP Training** | All personnel listed in Section 3 | On hire; refresher upon major SOP revision (≥ 1.0 version increment) | Internal LMS, recorded session by Clinical Informatics |
| **Data Mapping Best Practices** | Integration Engineers, Clinical Informaticists | Annual | Internal workshop led by Clinical Informatics Lead |
| **Clinical Safety in AI Integrations** | Integration Engineers, Clinical Informaticists, QA Engineers | Annual | Internal LMS, developed by Clinical Safety Team |

### 9.2 Training Tracking

All training completions shall be tracked in the Meridian Learning Management System (Workday Learning). Managers are responsible for verifying training compliance for their direct reports.

Integration personnel found to have accessed production integration infrastructure without current required training shall have access suspended until training is completed.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs and Policies

| Document ID | Title | Relationship |
|---|---|---|
| SOP-CLIN-001 | Clinical AI Product Lifecycle Management | Parent governance for product lifecycle |
| SOP-CLIN-005 | Clinical Data Model Management | Target data model that integrations populate |
| SOP-CLIN-012 | Clinical AI Model Inference Integration | Defines CDS result delivery to EHR |
| SOP-IS-003 | Information Security Incident Response | Escalation for security incidents |
| SOP-IS-007 | Access Control and Identity Management | PIM and access controls |
| SOP-QMS-001 | Quality Management System Overview | Framework governing validation and UAT processes |
| SOP-RA-002 | Regulatory Submission Evidence Package Preparation | Evidence generated by integration validation used in submissions |
| POL-DATA-001 | Data Governance and Stewardship Policy | Data quality and provenance governance |
| POL-CLIN-001 | Clinical Safety Policy | Clinical safety governance framework |

### 10.2 External Standards and References

| Standard / Reference | Version / Date | Applicability |
|---|---|---|
| HL7 FHIR R4 | Release 4, v4.0.1 | Base interoperability standard |
| US Core Implementation Guide | STU 6.1.0 | US client integrations; specifies USCDI data profiles |
| HL7v2 Implementation Guide for Clinical Decision Support | v2.9 | Legacy EHR integrations |
| IHE IT Infrastructure Technical Framework | Current | Cross-enterprise document sharing profiles |
| HIPAA Security Rule (45 CFR Part 164, Subpart C) | — | Technical safeguards for PHI |
| ISO 13485:2016 | 2016 | Quality management for medical device software |

---

## 11. Revision History

| Version | Date | Author | Approver | Summary of Changes |
|---|---|---|---|---|
| 1.0 | 2022-03-15 | Dr. Aisha Okafor | Dr. Priya Patel | Initial release establishing baseline EHR integration SOP for Clinical AI Platform. Covered FHIR R4 integrations only. |
| 1.1 | 2022-08-22 | Dr. Aisha Okafor | Dr. Priya Patel | Minor revision: added HL7v2 legacy integration pathway as permitted exception; updated UAT sign-off template; added terminology server reference. |
| 2.0 | 2023-04-10 | Dr. Aisha Okafor | Dr. Priya Patel | Major revision: restructured testing phases (added functional testing as distinct phase); introduced semantic validation standards and data mapping categories (A/B/C); added clinical safety classification; expanded monitoring and alerting; added 14-day stabilization period. |
| 2.1 | 2023-09-18 | Dr. Aisha Okafor | Dr. Priya Patel | Minor revision: updated KPI targets based on 6 months of production data; clarified de-identification requirements for non-production PHI use; updated role assignment table to reflect organizational changes. |
| 2.2 | 2024-02-05 | Dr. Aisha Okafor | Dr. Priya Patel | Minor revision: incorporated EU AI Act Article 10 data governance requirements; updated US Core IG reference to STU 6.1.0; revised exception expiration from 24 months to 12 months. |
| 2.3 | 2024-06-20 | Dr. Aisha Okafor | Dr. Priya Patel | Interim revision: modified UAT stakeholder sign-off requirements; added PIM session recording requirement for production data access; updated escalation timelines for P2/P3; added fairness and bias documentation requirement to Phase 1. |
| 2.4 | 2024-12-02 | Dr. Aisha Okafor | Dr. Priya Patel | Current version. Consolidated training requirements into dedicated Section 9; updated FHIR Gateway configuration steps for new Integration Hub platform; revised data validation error thresholds based on platform performance data; added BBFH support for population health integration patterns; updated named role assignments to reflect current organizational structure. |
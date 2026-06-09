---
sop_id: "SOP-PENG-015"
title: "Technical Documentation Standards"
business_unit: "Product & Engineering"
version: "4.6"
effective_date: "2025-01-04"
last_reviewed: "2026-02-16"
next_review: "2026-08-09"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "EU AI Act"
status: "Active"
---

# Standard Operating Procedure: Technical Documentation Standards

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the uniform standards, templates, review cycles, version control protocols, and retention requirements for all technical documentation produced by the Product & Engineering division of Meridian Health Technologies, Inc. The purpose of this SOP is to ensure that technical documentation is accurate, complete, auditable, and compliant with the regulatory obligations imposed by SOC 2, the EU AI Act, HIPAA, GDPR, SR 11-7, and other applicable frameworks. Adherence to this SOP ensures that documentation serves as a defensible artifact during internal audits, external certifications, regulatory inspections, and litigation.

### 1.2 Scope

This SOP applies to all employees, contractors, and third-party service providers (collectively "Personnel") who create, modify, review, approve, or archive technical documentation for any product, platform, service, or internal tool within the following business lines:

| Business Unit | Products Covered |
|---|---|
| Clinical AI Platform | MeridianDx, Clairvoyance Risk Scoring, Adverse Event Predictor |
| HealthPay Financial Services | HealthPay Gateway, PatientFi Lending Engine, ClaimsAuto |
| MedInsight Analytics | Population Health Explorer, CareGap Identifier, Outcomes Predictor |
| Meridian SaaS Platform | Core Platform Services, API Gateway, Identity Fabric, Data Lake |

**In Scope Documentation Categories:**
- System architecture diagrams and descriptions
- API specifications and interface control documents
- Data flow diagrams and data lineage documentation
- Machine learning model documentation (Model Cards, Training Reports)
- Deployment runbooks and operational playbooks
- Incident response and disaster recovery procedures
- Security architecture and control documentation
- Compliance control narratives and evidence packages
- User-facing technical guides and administrator manuals
- Source code inline documentation standards (for regulated modules only)

**Out of Scope:**
- Non-technical marketing collateral
- Internal team meeting notes and informal communications
- Human Resources documentation (see SOP-HR-002)
- Financial statements and accounting records (see SOP-FIN-001)

### 1.3 Applicability Matrix

| Role Group | Required Compliance Level |
|---|---|
| Product & Engineering Full-Time Employees | Full compliance, all sections |
| Product & Engineering Contractors | Full compliance, all sections |
| Clinical AI Product Development Teams | Full compliance + EU AI Act Annex IV requirements |
| HealthPay Financial Services Development Teams | Full compliance + SR 11-7 model documentation requirements |
| IT Operations Personnel | Sections 5.3, 5.4, 5.5, 7, 8 |
| Third-Party API Integration Partners | Sections 5.1, 5.2 only (via API documentation standards) |
| Internal Auditors | Read-only access; Section 7 reporting obligations |

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Author** | The individual who creates or substantially modifies a technical document. The Author is responsible for the technical accuracy and completeness of the content. |
| **Controlled Document** | Any document subject to the version control, review, and approval requirements of this SOP. Controlled documents reside exclusively within approved Document Management Systems (DMS). |
| **Document Owner** | The named individual accountable for the document's accuracy, maintenance, and periodic review. Typically a Team Lead, Engineering Manager, or Product Manager. |
| **Golden Copy** | The single authoritative version of a document stored in the designated DMS. Copies stored on local workstations, email attachments, or non-approved platforms are not Golden Copies. |
| **Model Card** | A structured, machine-readable document describing a machine learning model's intended use, training data, performance characteristics, limitations, and ethical considerations. Required for all clinical AI and financial services models. |
| **Non-Functional Requirements (NFRs)** | System attributes such as scalability, availability, latency, throughput, and security that are documented alongside functional specifications. |
| **Record** | A document that serves as evidence of a decision, transaction, or activity and is subject to retention schedules per SOP-CORP-011 (Records Management Policy). |
| **Technical Documentation Repository (TDR)** | The centralized, access-controlled system of record for all controlled technical documents. Implemented as a combination of Confluence (narrative documents), GitBook (API documentation), and AWS S3 (diagrams and artifacts). |
| **Traceability** | The ability to link related artifacts across the documentation hierarchy (e.g., from a regulatory requirement to a control description to a test procedure to a test result). |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| AI RMF | Artificial Intelligence Risk Management Framework (NIST) |
| API | Application Programming Interface |
| BIA | Business Impact Analysis |
| CCO | Chief Compliance Officer |
| CDS | Clinical Decision Support |
| CIO | Chief Information Officer |
| CISO | Chief Information Security Officer |
| CPO/DPO | Chief Privacy Officer / Data Protection Officer |
| DMS | Document Management System |
| DR | Disaster Recovery |
| EU AI Act | Regulation (EU) 2024/1689 of the European Parliament and of the Council laying down harmonised rules on artificial intelligence |
| FDA | U.S. Food and Drug Administration |
| ICD | Interface Control Document |
| MDR | Medical Device Regulation (EU) 2017/745 |
| ML | Machine Learning |
| PHI | Protected Health Information |
| RACI | Responsible, Accountable, Consulted, Informed |
| SRS | Software Requirements Specification |
| TDD | Technical Design Document |
| TDR | Technical Documentation Repository |
| VP | Vice President |

---

## 3. Roles and Responsibilities

### 3.1 RACI Matrix

| Activity | Author | Document Owner | Engineering Manager | VP of Engineering | AI Governance Committee | CISO / CPO | CCO | Internal Audit |
|---|---|---|---|---|---|---|---|---|
| Document Creation/Update | **R** | A | C | I | C (AI docs) | C (Security/Privacy) | I | I |
| Document Classification | R | **A** | C | I | — | I | C | I |
| Peer Review (Technical) | I | R | **A** | I | — | — | — | — |
| Regulatory Review (EU AI Act Art. 11) | I | R | C | I | **A** | C | R | I |
| Document Approval | I | R | C | **A** | A (AI systems) | A (Controls docs) | I | I |
| Periodic Review | I | **R** | C | A | C | C | I | I |
| Obsolete Document Retirement | I | R | C | **A** | — | — | I | I |
| Access Provisioning | — | R | C | I | — | **A** | I | C |
| Compliance Audit Evidence | — | C | C | I | C | C | **R** | A |

**Legend:** R = Responsible (doer), A = Accountable (approver), C = Consulted, I = Informed

### 3.2 Named Role Responsibilities

| Role | Individual | Specific Documentation Responsibilities |
|---|---|---|
| VP of Engineering | David Park | SOP Owner. Final authority on documentation standards, tooling, and enforcement. Reviews all exception requests exceeding 30 days. |
| Chief AI Officer | Dr. Marcus Rivera | Co-approves all Model Cards for high-risk AI systems. Ensures EU AI Act Article 11 and Article 13 transparency documentation standards are met. |
| Chief Medical Officer | Dr. Priya Patel | Reviews and approves clinical validation documentation for all Clinical AI products. |
| CISO | Rachel Kim | Reviews and approves all security architecture documents, threat models, and BIA documents. |
| CPO/DPO | Dr. Klaus Weber | Reviews all data flow diagrams and data protection impact assessments (DPIAs) for GDPR Article 30 compliance. |
| Chief Compliance Officer | Thomas Anderson | Maintains master list of all regulatory documentation requirements. Serves as liaison to external auditors for SOC 2 and HITRUST evidence requests. |
| VP of Clinical AI Products | Dr. Aisha Okafor | Ensures all clinical model documentation meets FDA 510(k) and EU MDR CE marking evidence requirements. |
| VP of Financial Services | Robert Liu | Ensures all HealthPay model documentation meets SR 11-7 standards for model risk management. |
| VP of IT Operations | Samantha Torres | Owns operational runbook documentation. Ensures accuracy of DR and incident response procedures. |

---

## 4. Policy Statements

### 4.1 General Documentation Policy

**P-001:** All technical systems, services, and processes deployed to production SHALL have corresponding documentation that meets the standards defined in this SOP before the deployment is approved. The VP of Engineering's delegated release manager SHALL verify documentation completeness as a gating criterion in the CI/CD pipeline. No emergency change shall remain undocumented beyond 72 hours post-incident resolution.

**P-002:** Technical documentation is a corporate asset. All controlled technical documents SHALL reside within the approved Technical Documentation Repository (TDR). Creation, storage, or maintenance of Golden Copies on personal laptops, unapproved shared drives, or email systems is prohibited.

**P-003:** Documentation SHALL be maintained at a level of detail sufficient to enable a qualified individual who did not author the document to understand, operate, and troubleshoot the system without reliance on the original author's tacit knowledge. This "bus factor" principle is a core quality standard.

### 4.2 Regulatory Policy Commitments

**P-004 (SOC 2 — CC2.2, CC7.1, CC8.1):** Meridian maintains written technical documentation describing the design, operation, and controls of all systems in scope for SOC 2. Control descriptions SHALL be updated within 30 days of any material change to the control environment. The CCO maintains a master control matrix (SOP-COMP-001) that maps each SOC 2 Trust Services Criterion to specific technical documents in the TDR. Documentation completeness against the control matrix is assessed quarterly.

**P-005 (EU AI Act — Articles 11, 13, 18):** For all high-risk AI systems as defined under Annex III of the EU AI Act, Meridian SHALL create and maintain technical documentation as specified in Annex IV, including:
- (a) A general description of the AI system;
- (b) A detailed description of the elements of the AI system and of the process for its development;
- (c) Detailed information about the monitoring, functioning, and control of the AI system;
- (d) A detailed description of the risk management system (Article 9);
- (e) A description of any change made to the system throughout its lifecycle;
- (f) A list of the harmonised standards applied;
- (g) A copy of the EU declaration of conformity;
- (h) A description of the system in place to evaluate the AI system performance in the post-market phase.

The Chief AI Officer SHALL ensure this documentation is maintained and made available to competent authorities within 10 working days upon request, as required by Article 18(2).

**P-006 (SR 11-7):** All models within the HealthPay Financial Services line SHALL have comprehensive documentation that conforms to the Federal Reserve's Supervisory Guidance on Model Risk Management (SR 11-7), including model development documentation, validation reports, and ongoing monitoring results. Documentation SHALL be updated at each model revalidation cycle (at minimum annually for high-risk models, biennially for low-risk models).

**P-007 (HIPAA Documentation):** Documentation of systems processing PHI SHALL include data flow diagrams identifying all PHI touchpoints, encryption states (at rest, in transit), and access control mechanisms. These documents SHALL be reviewed in the event of any change to the PHI data flow.

### 4.3 Quality Standards

**P-008:** All controlled documents SHALL be written in clear, concise English. Document authors SHALL use active voice, present tense, and define all acronyms on first use. Documents that contain more than 5 grammatical or spelling errors upon review SHALL be rejected and returned to the Author.

**P-009:** All controlled documents SHALL include a header or footer on each page displaying: Document Title, Document ID, Version Number, Classification Level, and Page Number.

---

## 5. Detailed Procedures

### 5.1 Document Lifecycle Management

#### 5.1.1 Document Creation

1. **Identify Need:** The Author or Document Owner identifies the need for a new technical document. Triggers include new system development, regulatory change, audit finding (see SOP-AUD-003), or request from the AI Governance Committee.
2. **Check for Existing Documents:** Before creating a new document, the Author SHALL search the TDR for existing documentation that can be updated to address the need. Duplicate documentation is prohibited.
3. **Register Document:** The Author SHALL register the intended document in the TDR metadata tracker (Jira issue type "Documentation") and obtain a unique Document ID from the system. The ID format is: `[BUSINESS_UNIT]-[TYPE]-[NNN]` (e.g., `CLINICAL-TDD-042`).
4. **Select Template:** The Author SHALL select the appropriate template from the Template Library (see Section 5.2).
5. **Assign Classification:** The Author SHALL propose a classification level (see Section 6.1) in consultation with the Document Owner.
6. **Develop Content:** The Author develops the document content according to the template and classification standards.

#### 5.1.2 Document Review and Approval Workflow

```
[Author Submits Draft]
    |
    v
[Automated Completeness Check] — Pre-review pipeline validates:
    — All required sections present
    — Document ID and version populated
    — Classification marked
    — No unresolved "TBD" placeholders
    |
    | (Conditional: AI/ML documents)
    v
[AI Governance Committee Technical Review]
    — Validates Model Card completeness
    — Verifies EU AI Act Annex IV alignment
    — Reviews risk assessment documentation
    — SLA: 10 business days
    |
    v
[Peer Review (Technical)]
    — Assigned reviewer(s) with relevant domain expertise
    — Reviews technical accuracy, completeness, clarity
    — SLA: 5 business days
    |
    v
[Document Owner Review]
    — Verifies all feedback addressed
    — Confirms document meets business need
    — SLA: 3 business days
    |
    | (Conditional: Security/Privacy/Compliance)
    v
[Specialist Review]
    — CISO reviews security architecture documents
    — CPO reviews data flow and privacy documents
    — CCO reviews control documentation
    — SLA: 7 business days
    |
    v
[Final Approver]
    — VP of Engineering (all production documents)
    — Chief AI Officer (co-approval for high-risk AI docs)
    — SLA: 5 business days
    |
    v
[Publication to TDR]
    — Version incremented
    — Golden Copy stored
    — Stakeholders notified
    — Previous version archived
```

#### 5.1.3 Periodic Review

1. **Schedule:** The Document Owner is responsible for ensuring each document is reviewed at a frequency consistent with its criticality:
   - **Critical (Tier 1):** Every 6 months. Includes: security architecture, incident response, DR, high-risk AI Model Cards, compliance control narratives.
   - **High (Tier 2):** Every 12 months. Includes: API specifications, system architecture, deployment runbooks, low-risk model documentation.
   - **Medium (Tier 3):** Every 24 months. Includes: user guides, administrator manuals, internal tool documentation.

2. **Review Process:** The Document Owner initiates a review workflow (identical to the approval workflow in 5.1.2) at the designated interval. Even if no changes are required, the review SHALL be recorded with a "Reviewed, No Changes" annotation and a new review date set.

3. **Lapsed Review:** If a periodic review is not completed within 30 calendar days of its due date, the TDR automatically marks the document as "Expired" and restricts its visibility to the Document Owner and the VP of Engineering's office. An automatic escalation notification is sent to the Document Owner's manager.

#### 5.1.4 Document Retirement and Archiving

1. **Criteria for Retirement:** A document is retired when the system it describes is decommissioned, the process is discontinued, or the document is superseded by a new document.
2. **Retirement Process:** The Document Owner initiates a retirement request. The VP of Engineering approves the retirement. The document is moved to the TDR Archive partition with a "Retired" watermark and a reference to any superseding document.
3. **Retention Period:** Retired controlled documents that constitute Records (as defined in Section 2.1) SHALL be retained per the retention schedule specified in SOP-CORP-011. Minimum retention is 7 years for regulatory-related documents. Non-record documents are purged after 3 years.

### 5.2 Document Types and Templates

#### 5.2.1 Document Typology

| Document Type | Type Code | Template ID | Required For | Regulatory Linkage |
|---|---|---|---|---|
| System Architecture Overview | SAO | TEMP-ENG-001 | All production systems | SOC 2 CC2.2, EU AI Act Annex IV(a) |
| Technical Design Document | TDD | TEMP-ENG-002 | All new features requiring system changes | SOC 2 CC7.1 |
| Interface Control Document (API) | ICD-API | TEMP-ENG-003 | All public and internal APIs | SOC 2 CC6.1 |
| Data Flow Diagram | DFD | TEMP-ENG-004 | All systems processing regulated data | HIPAA, GDPR Art. 30, EU AI Act Annex IV(b) |
| Model Card | MC | TEMP-ENG-005 | All ML models (clinical and financial) | EU AI Act Annex IV, SR 11-7 |
| Threat Model | TM | TEMP-ENG-006 | All production systems | SOC 2 CC7.1 |
| Operational Runbook | OR | TEMP-ENG-007 | All production services | SOC 2 CC7.2 |
| Incident Response Procedure | IRP | TEMP-ENG-008 | All business lines | SOC 2 CC7.4, CC7.5 |
| Disaster Recovery Plan | DRP | TEMP-ENG-009 | All Tier 1 and Tier 2 systems | SOC 2 CC7.5 |
| Deployment/Release Procedure | DEP | TEMP-ENG-010 | All CI/CD pipelines | SOC 2 CC8.1 |
| Security Control Description | SCD | TEMP-ENG-011 | All controls in scope for SOC 2 / HITRUST | SOC 2 CC4.1 |
| Clinical Validation Report | CVR | TEMP-ENG-012 | All Clinical AI products | EU AI Act Annex IV(d), FDA 510(k) |

#### 5.2.2 Model Card Template (Excerpt) — EU AI Act Annex IV Compliance

The Model Card template (TEMP-ENG-005 v3.2) includes the following mandatory sections aligned with EU AI Act Annex IV:

| Section | Required Content | Annex IV Mapping |
|---|---|---|
| 1. Model Identity | Model name, version, unique identifier, and intended business process | Art. 11(1) |
| 2. Intended Purpose | Detailed description of intended use, operational context, user profile, and foreseen misuse | Annex IV 1(a) |
| 3. Training and Input Data | Data sources, collection methods, preprocessing, provenance, data governance measures, known biases | Annex IV 1(b), Art. 10 |
| 4. Model Architecture and Parameters | Description of algorithm family, hyperparameters, feature engineering, and training methodology | Annex IV 1(b) |
| 5. Performance Metrics | Accuracy, precision, recall, F1, AUC, fairness metrics across subpopulations, and performance thresholds | Annex IV 1(c) |
| 6. Risk Assessment | Identified risks, severity, likelihood, mitigation measures per the AI risk management system | Annex IV 1(d), Art. 9 |
| 7. Human Oversight | Measures for human oversight (Art. 14), interface design, override mechanisms, and operator training requirements | Annex IV 1(e), Art. 14 |
| 8. Monitoring and Logging | Automated performance monitoring, drift detection thresholds, logging detail (Art. 12), and alerting configuration | Art. 12, Annex IV 1(c) |
| 9. Limitations and Contraindications | Known limitations, excluded populations, contraindicated use cases, and out-of-distribution behaviors | Annex IV 1(a) |
| 10. Validation History | Summary of internal and external validations, clinical trial references, regulatory clearances | Annex IV 1(f), 1(g) |

The Chief AI Officer maintains the Model Card template and updates it within 30 days of any regulatory guidance change from the EU AI Office.

#### 5.2.3 Minimum Content Standards by Document Type

All templates SHALL include, at a minimum:

- **Title Page:** Document title, Document ID, version, effective date, classification, owner, approver.
- **Revision History:** Table of changes since the last version.
- **Table of Contents:** Auto-generated.
- **References:** List of related internal and external documents with hyperlinks where possible.
- **Glossary:** Definitions of domain-specific terms used in the document.

### 5.3 Version Control Standards

#### 5.3.1 Version Numbering Scheme

Meridian uses a modified semantic versioning scheme for all controlled technical documents:

`MAJOR.MINOR`

- **MAJOR (X):** Incremented when a substantive change is made to the system design, architecture, or operational procedure that changes the understanding or execution of the documented item. Also incremented on periodic review if the document is materially updated. Resets MINOR to 0.
- **MINOR (Y):** Incremented for editorial corrections, clarifications, non-substantive updates, or formatting changes that do not alter the technical meaning.

**Examples:**
- v1.0: Initial approved version.
- v1.1: Fixed a typo in an API endpoint URL.
- v2.0: Architecture changed from monolithic to microservices; document rewritten.
- v4.6: Current version of this SOP; indicates 4 major revisions and 6 minor updates since inception.

#### 5.3.2 Version Control Practices

1. **Check-Out/Check-In:** The TDR enforces a check-out/check-in model. Only one Author may edit a document at a time. The document is locked for editing by others during the check-out period.
2. **Diff Tracking:** All changes between versions SHALL be tracked. The TDR maintains a complete audit trail of every change, including Author, timestamp, and nature of change.
3. **Commit Messages:** Every new version SHALL include a meaningful change description (commit message) summarizing what was changed and why.
4. **Branching for Regulatory Compliance:** For documents supporting regulatory submissions (FDA 510(k), CE marking), a stable branch is created at the time of submission. This branch is immutable and retained for the life of the regulatory approval. The main document continues to evolve on the main branch.

### 5.4 Diagramming and Visual Artifact Standards

1. **Tooling:** All architectural diagrams, data flow diagrams, and network topology diagrams SHALL be created using Lucidchart (preferred) or draw.io and stored in the TDR in both editable (`.lucid`, `.drawio`) and non-editable (`.png`, `.svg`) formats.
2. **Consistency:** Diagrams SHALL use the Meridian standard icon library maintained in the TDR. Custom icons are prohibited unless approved by the VP of Engineering.
3. **Accessibility:** Diagrams SHALL include alt-text descriptions stored as metadata in the TDR. Color MUST NOT be the sole differentiator of meaning; patterns or labels shall be used redundantly.
4. **Embedding:** Diagrams SHALL be embedded in narrative documents via a live link to the Golden Copy in the TDR. Embedding static screenshots is prohibited because it leads to version drift.

### 5.5 API Documentation Standards

All public and internal APIs SHALL be documented using the OpenAPI 3.1 specification. Documentation SHALL be stored in GitBook and auto-generated from the source code annotations where possible.

**Required elements for each API endpoint:**
- HTTP method and full URL path
- Authentication and authorization requirements (OAuth 2.0 scopes)
- Request parameters (path, query, header, body) with data types, constraints, and examples
- Response schemas for all possible HTTP status codes (200, 201, 204, 400, 401, 403, 404, 409, 422, 429, 500)
- Rate limiting thresholds
- Request/response examples in JSON format
- Deprecation notices and sunset dates, if applicable

**Documentation synchronization:** API documentation SHALL be regenerated and published to GitBook as a step in the CI/CD pipeline. A documentation drift check SHALL run weekly to compare the published spec against the actual API behavior using contract testing (Pact framework). Drift exceeding 5% of endpoints triggers an automated ticket assigned to the owning team with P2 priority.

---

## 6. Controls and Safeguards

### 6.1 Document Classification and Access Control

| Classification Level | Label | Access Scope | Example Documents | Encryption at Rest | Encryption in Transit |
|---|---|---|---|---|---|
| **Public** | `PUBLIC` | Unrestricted | Open-source API documentation, public-facing help articles | Yes | Yes |
| **Internal** | `INTERNAL` | All Meridian employees and authorized contractors | SOPs, runbooks, design documents, model cards (non-restricted) | Yes | Yes |
| **Confidential** | `CONFIDENTIAL` | Role-based access; need-to-know basis | Detailed security architecture, threat models, BIA, control narratives (full detail) | Yes + envelope encryption | Yes |
| **Restricted** | `RESTRICTED` | Named individuals only; legal hold enabled | Encryption key management docs, incident forensics reports, penetration test findings | Yes + envelope encryption + legal hold | Yes + mutual TLS |

**Access Control Implementation (SOC 2 CC6.1):**
1. The TDR integrates with Meridian's single sign-on (SSO) via Okta. All access SHALL be authenticated via SAML 2.0.
2. Role-based access control (RBAC) is enforced. Roles are: `TDR-Viewer`, `TDR-Author`, `TDR-Owner`, `TDR-Admin`.
3. Access reviews are conducted quarterly by the Document Owner and the CISO's Identity and Access Management (IAM) team.
4. Any access to `CONFIDENTIAL` or `RESTRICTED` documents SHALL be logged. Logs are shipped to the SIEM (Splunk) and reviewed for anomalies per SOP-SEC-005 (Security Monitoring Policy).

### 6.2 Integrity Controls

| Control | Description | SOC 2 Trust Service Criterion | Implementation |
|---|---|---|---|
| Immutable Audit Trail | All changes to controlled documents are logged and immutable. | CC7.2 | TDR built on Confluence with "Page History" and audit log exports to S3 immutable bucket; WORM (Write Once Read Many) policy enforced for 3 years. |
| Digital Signatures | All approvals SHALL be cryptographically signed. | CC6.1 | DocuSign integration with Okta-verified identity. Approval without valid digital signature is not recognized as an approved document. |
| Automated Backups | Golden Copies are backed up daily. | CC7.5 | AWS Backup for S3 TDR bucket; Confluence Cloud backup schedule verified monthly. RPO: 24 hours. RTO for TDR: 4 hours. |
| Malware Scanning | Uploaded attachments to the TDR are scanned. | CC7.1 | AWS S3 with integrated malware scanning (ClamAV via Lambda trigger). Infected files are quarantined automatically. |

### 6.3 EU AI Act Specific Controls

| Control | EU AI Act Reference | Description | Evidence Generated |
|---|---|---|---|
| Technical Documentation Completeness Check | Article 11, Annex IV | Automated scanner validates all Annex IV sections are present in Model Cards before approval. | Completeness report in TDR |
| Conformity Assessment Documentation | Article 43 | For high-risk AI systems, a Notified Body assessment report and associated technical documentation package is compiled and archived. | Conformity Assessment Package in TDR `RESTRICTED` partition |
| Post-Market Monitoring Documentation | Article 61 | Documentation of the PMS plan and PMS reports are maintained and updated per the plan schedule. | PMS reports in TDR |
| Incident Reporting Documentation | Article 62 | Documentation of any serious incident and subsequent corrective actions. | Incident reports linked from TDR to Jira incident records |
| Transparency Information | Article 13 | User-facing explanations of AI system capabilities and limitations are documented and versioned. | Transparency notices in TDR, linked to production deployment records |

### 6.4 SR 11-7 Specific Controls

For HealthPay Financial Services models:
- A **Model Inventory** is maintained in the TDR as a living document by VP of Financial Services' team. It classifies each model by risk tier.
- For each Tier 1 (High Risk) model, a **Model Documentation Package** is assembled containing: Development Report, Validation Report, and Ongoing Monitoring Plan.
- The Model Documentation Package is reviewed and re-validated annually. Re-validation triggers a mandatory update to the Model Card.
- All model changes SHALL be documented with a justification memo that is approved by the VP of Financial Services before the change is promoted to production.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| KPI | Target | Measurement Method | Reporting Frequency | Owner |
|---|---|---|---|---|
| Documentation Completeness Score | ≥ 95% of production systems have all required Tier 1 documents | Automated scan of TDR against CMDB (ServiceNow) | Monthly | VP of Engineering |
| Document Review Timeliness | ≥ 90% of periodic reviews completed within 30 days of due date | TDR metadata query | Monthly | VP of Engineering |
| SOC 2 Control Documentation Accuracy | 100% of sampled documents match actual control operation | Quarterly control testing by Internal Audit | Quarterly | CCO |
| EU AI Act Annex IV Compliance | 100% for all high-risk AI models | AI Governance Committee quarterly audit | Quarterly | Chief AI Officer |
| API Documentation Drift | ≤ 5% of endpoints differ between spec and behavior | Pact contract testing automated scan | Weekly | VP of Engineering |
| Training Compliance | ≥ 95% of required personnel complete annual documentation training | LMS (Workday Learning) report | Quarterly | CHRO / VP of Engineering |
| Open Documentation Defects Aging | 0 defects > 30 days | Jira query on "Documentation" issue type | Weekly | Engineering Managers |

### 7.2 Dashboards and Reporting

1. **Engineering Documentation Dashboard:** A Datadog dashboard displays real-time compliance against the KPIs defined in Section 7.1. This dashboard is displayed on the Engineering Operations Center monitors and is reviewed at the weekly Engineering Leads meeting chaired by David Park.
2. **Compliance Documentation Dashboard:** A PowerBI dashboard maintained by the CCO's office maps all regulatory requirements (SOC 2, EU AI Act, HIPAA, GDPR, SR 11-7) to their corresponding technical documentation artifacts in the TDR. A gap analysis is generated automatically. This dashboard is reviewed at the monthly AI Governance Committee meeting chaired by Dr. Sarah Chen.
3. **Quarterly Documentation Health Report:** The VP of Engineering publishes a comprehensive "Documentation Health Report" to the executive leadership team (ELT). The report includes: KPI trends, significant gaps, corrective actions in progress, and resource needs. This report is submitted 10 business days after quarter-end.

### 7.3 Audit Trail Reporting

For SOC 2 Type II audit evidence requests:
1. External auditors submit requests through the CCO via a secure portal.
2. The CCO or delegate retrieves the requested documents from the TDR and generates an evidence package that includes the document's full audit trail (all versions, all approvals, all access logs).
3. The evidence package is delivered within the timeline specified in the audit engagement letter, typically 5 business days.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Request Procedure

In circumstances where strict compliance with this SOP is temporarily impractical (e.g., emergency production deployment, critical security patch), an exception may be requested.

1. **Initiate:** The individual seeking the exception submits a formal "Documentation Exception Request" via the ServiceNow IT Service Management portal (form ID: `DOC-EXCPT-001`).
2. **Justification:** The request SHALL include:
   - Document(s) affected
   - Specific SOP section(s) from which exception is sought
   - Business justification for the exception
   - Compensating controls that will be in place
   - Duration for which the exception is needed (maximum 90 days)
3. **Review:** The Document Owner and CCO review the request within 3 business days.
4. **Approval Matrix:**

| Exception Duration | Approver |
|---|---|
| Up to 7 calendar days | Engineering Manager |
| 8 – 30 calendar days | VP of Engineering |
| 31 – 90 calendar days | VP of Engineering + CCO joint approval |
| Beyond 90 calendar days | CEO (Dr. Sarah Chen) approval required; treated as a policy waiver, not an exception |

5. **Tracking:** All approved exceptions are logged in the TDR Exception Register. The register is reviewed quarterly by the CCO.
6. **Remediation:** The exception includes a committed remediation date. If the remediation is not closed by that date, the issue is automatically escalated to the next level of authority. No production system SHALL operate under a lapsed exception without the CEO's explicit written authorization.

### 8.2 Escalation Path

| Level | Escalation Trigger | Escalation Target | Timeframe |
|---|---|---|---|
| 1 | Documentation missing for production deployment | VP of Engineering | Immediately upon discovery |
| 2 | Periodic review overdue > 30 days | VP of Engineering | Automatic via TDR notification |
| 3 | Exception remediation overdue > 7 days | CCO | Automatic via ServiceNow |
| 4 | Critical audit finding related to documentation | CEO / AI Governance Committee | Within 24 hours of finding |

---

## 9. Training Requirements

### 9.1 Required Training Courses

All Personnel covered by this SOP SHALL complete the following training:

| Training Module | Course Code | Duration | Audience | Frequency | Delivery Method |
|---|---|---|---|---|---|
| Technical Documentation Standards v4 | TNG-PENG-015A | 2 hours | All Product & Engineering Personnel | Annually | Workday Learning (E-learning) |
| Writing Effective Technical Documents | TNG-PENG-015B | 4 hours | All new hire Engineers; existing Engineers with <80% quality score | Once; remediation as needed | Instructor-led (Virtual) |
| EU AI Act Documentation Requirements | TNG-AI-011 | 1.5 hours | Clinical AI and HealthPay teams | Annually; updated per regulatory change | E-learning, updated by Chief AI Officer |
| Confluence and TDR Tool Training | TNG-CORP-022 | 1 hour | All Personnel with TDR-Author role | On role assignment; annual refresher | E-learning |

### 9.2 Training Compliance Tracking

- Training compliance is tracked through Workday Learning.
- Managers are notified 30 days and 14 days before their team members' training is due.
- Non-compliance at 14 days past due results in suspension of TDR-Author privileges until training is completed.
- The CHRO, Jennifer Walsh, provides a monthly training compliance report to the VP of Engineering and the CCO.

### 9.3 Competency Assessment

As part of the annual performance review cycle, Engineering Managers assess the documentation quality produced by their direct reports. A documentation quality rubric (available in the TDR) is used. Engineers whose documentation consistently requires rework (> 15% of documents rejected upon peer review) SHALL be assigned a documentation mentor and complete remedial training (TNG-PENG-015B) within 60 days.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs and Policies

| SOP/Policy ID | Document Name | Relationship |
|---|---|---|
| SOP-COMP-001 | Compliance Control Matrix Management | Defines the master control matrix referenced by this SOP |
| SOP-SEC-005 | Security Monitoring and Logging Policy | Governs the SIEM logs referenced in Section 6.1 |
| SOP-CORP-011 | Records Management and Retention Policy | Defines retention schedules for documents classified as Records |
| SOP-AUD-003 | Internal Audit and Corrective Action Policy | Governs how audit findings drive documentation remediation |
| SOP-AI-002 | AI Risk Management Framework | Defines the AI risk management system referenced in EU AI Act documentation |
| SOP-SEC-008 | Vulnerability and Patch Management | Governs documentation of security patches and exceptions |
| SOP-SEC-010 | Incident Response Plan | Master incident response framework that IRPs (Section 5.2.1) must align with |
| SOP-HR-002 | Employee Training and Development | Governs training tracking referenced in Section 9 |
| SOP-IT-005 | Change and Release Management | Defines gating criteria for production releases that require documentation |

### 10.2 External Standards and Regulations

| Standard/Regulation | Reference | Applicable To |
|---|---|---|
| AICPA SOC 2 | Trust Services Criteria (2017 revision, 2022 update) — CC2.2, CC4.1, CC6.1, CC7.1, CC7.2, CC7.4, CC7.5, CC8.1 | Meridian SaaS Platform; HealthPay Financial Services |
| EU AI Act | Regulation (EU) 2024/1689 — Articles 9, 10, 11, 12, 13, 14, 18, 43, 61, 62; Annex III, Annex IV | Clinical AI Platform |
| Federal Reserve SR 11-7 | Supervisory Guidance on Model Risk Management (April 4, 2011) | HealthPay Financial Services (model documentation) |
| NIST AI RMF | NIST AI 100-1 (January 2023) | All AI/ML products |
| HIPAA | 45 CFR Parts 160, 162, and 164 | All products handling PHI |
| GDPR | Regulation (EU) 2016/679 — Articles 6, 9, 25, 30, 32, 35 | MedInsight Analytics; any EU personal data |
| ISO 27001:2022 | Annex A Controls — A.5.10, A.5.37, A.7.5, A.8.1, A.8.4, A.8.9 | Meridian SaaS Platform |
| ISO 13485:2016 | Medical devices — Quality management systems | Clinical AI Platform (device documentation) |
| FDA QSR | 21 CFR Part 820 | Clinical AI products with FDA 510(k) clearance |

---

## 11. Revision History

| Version | Date | Author | Approver | Change Summary |
|---|---|---|---|---|
| 1.0 | 2020-03-15 | Michael Reeves (former VP Engineering) | Dr. Elena Torres (former CEO) | Initial release. Established basic documentation standards for the SaaS Platform. |
| 2.0 | 2021-09-22 | David Park | Dr. Elena Torres | Major revision. Expanded scope to include HealthPay products upon SOC 2 Type II and SR 11-7 requirements. Introduced Model Card concept. |
| 2.3 | 2022-06-01 | David Park | Dr. Sarah Chen | Added API documentation standards and version control scheme. Minor updates to review frequency. |
| 3.0 | 2023-11-15 | David Park | Dr. Sarah Chen | Major revision. Added EU AI Act Annex IV compliance, Clinical AI Platform documentation standards, and diagramming standards. Introduced RACI matrix and KPI dashboard. |
| 3.2 | 2024-07-10 | Dr. Aisha Okafor (contributing) / David Park | Dr. Sarah Chen | Updated Model Card template to align with final EU AI Act Annex IV text. Added Post-Market Monitoring documentation requirements. |
| 4.0 | 2025-01-04 | David Park | Dr. Sarah Chen | Major revision to incorporate effective obligations under EU AI Act (August 2025). Added Section 6.3 EU AI Act Controls. Introduced Confluence + GitBook + S3 as TDR. Expanded training requirements. Restructured entire SOP for improved navigability. |
| 4.3 | 2025-07-18 | David Park | Dr. Sarah Chen | Updated to reflect new SOC 2 TSC 2022 revision mapping. Added HealthPay SR 11-7 annual revalidation requirements. Updated access control procedures. Clarified retention schedules for regulatory documents. |
| 4.6 | 2026-02-16 | David Park | Dr. Sarah Chen | Current version. Added Section 6.4 SR 11-7 controls. Updated KPI targets and training courses. Added exception handling escalation to CEO for waivers >90 days. Updated VP of Financial Services from interim to Robert Liu. Expanded Section 5.2.3 minimum content standards. Clarified API documentation drift tolerance to 5%. Added competency assessment section. |
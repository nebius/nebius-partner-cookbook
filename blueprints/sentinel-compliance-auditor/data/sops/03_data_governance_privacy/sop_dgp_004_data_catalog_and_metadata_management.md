---
sop_id: "SOP-DGP-004"
title: "Data Catalog and Metadata Management"
business_unit: "Data Governance & Privacy"
version: "2.1"
effective_date: "2024-12-05"
last_reviewed: "2025-04-03"
next_review: "2025-10-18"
owner: "Dr. Klaus Weber, Chief Privacy Officer / DPO"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
  - "SOC 2"
status: "Active"
---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, standards, and operational processes for managing Meridian Health Technologies’ enterprise data catalog and associated metadata. The purpose of this document is to ensure that all data assets across the organization are systematically inventoried, classified, described with consistent metadata, and made discoverable to authorized stakeholders. Effective metadata management is foundational to Meridian’s ability to comply with data protection obligations, support AI model development with high-quality training data, enable rapid clinical analytics, and maintain the integrity of financial services models subject to regulatory oversight.

This SOP operationalizes the Data Governance Policy (SOP-DGP-001) by providing detailed, actionable procedures for metadata capture, catalog population, data lineage documentation, and search and discovery workflows.

### 1.2 Scope

This SOP applies to all data assets processed, stored, or transmitted by Meridian Health Technologies, Inc., across all business units, geographic locations, and technology environments.

**In-Scope Data Assets:**
- Structured data within Snowflake, PostgreSQL, and Redis data stores
- Unstructured and semi-structured data residing in Amazon S3 buckets, Pinecone vector databases, and log streams
- Streaming data transiting through Apache Kafka topics
- Machine learning model training datasets, feature stores, and model outputs managed via MLflow and SageMaker
- Protected Health Information (PHI) and Personally Identifiable Information (PII) for approximately 12 million patients within MedInsight Analytics
- Financial transaction data processed by HealthPay Financial Services (~$4.2B annual volume)
- Clinical AI Platform inference data, physician feedback, and model drift monitoring data
- All data exported for business intelligence, regulatory reporting, or external sharing

**In-Scope Environments:**
- Amazon Web Services (AWS) commercial cloud regions in us-east-1, us-west-2, eu-central-1, and eu-west-1
- Meridian corporate network (on-premises legacy systems in Toronto and Austin data centers)
- End-user computing devices accessing Meridian-sanctioned collaboration platforms (Microsoft 365, SharePoint, Teams)

**Out-of-Scope:**
- Publicly available marketing materials and web content governed by the Corporate Communications Policy
- Personal data processed solely in the context of employee HR records (governed by SOP-HR-007)
- Third-party datasets licensed under terms that prohibit metadata extraction (see Section 8 for exception handling)

### 1.3 Applicability

This SOP is binding upon all Meridian employees, contractors, consultants, interns, temporary workers, and third-party data processors who interact with or manage in-scope data assets. Compliance is mandatory and is enforced through periodic audits administered by the Data Governance & Privacy business unit, in coordination with Internal Audit. Non-compliance shall result in disciplinary action, up to and including termination of employment or contract, in accordance with Meridian’s Corrective Action Policy (SOP-HR-022).

---

## 2. Definitions and Acronyms

The following terms are defined for the purposes of this SOP and supersede colloquial or informal definitions used elsewhere.

| Term | Definition |
| :--- | :--- |
| **Business Glossary** | A curated, semantically unified collection of business terms and their definitions, approved by the Data Governance Council. Serves as the “common language” for Meridian. Distinct from a technical data dictionary. |
| **Data Asset** | Any discrete collection of data that has recognizable value to a business unit. Includes tables, views, files, streams, ML features, API responses, and reports. |
| **Data Catalog** | The centralized inventory and discovery platform (currently Alation, deployed on Meridian’s AWS infrastructure, instance identifier `MHT-CAT-PROD-01`) that registers all Data Assets, links them to technical metadata, business glossary terms, and data owners. |
| **Data Dictionary** | A technical metadata repository containing precise schema information: column names, data types, lengths, nullable constraints, primary/foreign key relationships, and valid value sets. The Data Dictionary is a structural subset of the Data Catalog. |
| **Data Domain** | A top-level logical grouping of data assets aligned with business capabilities (e.g., "Clinical Data," "Financial Data," "Patient Engagement," "AI/ML Model Ops"). |
| **Data Lineage** | A visual and programmatic description of data’s origins, transformations, movements, and destinations throughout its lifecycle. Lineage is documented at the column-level for Tier 1 and Tier 2 assets. |
| **Data Owner** | A senior business leader (Director-level or above) accountable for the quality, classification, access control, and lifecycle management of data assets within their domain. The Data Owner is explicitly *not* the Data Steward. |
| **Data Steward** | An operational subject-matter expert, designated by a Data Owner, responsible for day-to-day metadata curation, data quality rule execution, and catalog completeness for assigned assets. |
| **GDPR** | General Data Protection Regulation (Regulation (EU) 2016/679). |
| **PHI/PII** | Protected Health Information (as defined by HIPAA) and Personally Identifiable Information (as defined by various state, federal, and international privacy regulations). Within this SOP, "PHI/PII" denotes a Tier 0 classification. |
| **Tier** | A sensitivity and criticality classification label applied to all data assets: **Tier 0** (PHI/PII, financial account numbers, credentials), **Tier 1** (Proprietary financial projections, unreleased clinical trial data, legal privileged documents, sensitive employee data), **Tier 2** (Internal business operations data, non-sensitive employee data, de-identified clinical data), **Tier 3** (Publicly available information). |

---

## 3. Roles and Responsibilities

### 3.1 Role Matrix

The following matrix defines the functional responsibilities for executing this SOP. The responsible parties are accountable for fulfilling the assigned functions.

| Role | Accountable Individuals / Groups | Key Responsibilities |
| :--- | :--- | :--- |
| **Executive Sponsor** | Chief Data & Analytics Officer (CDAO) | Provides executive-level strategic direction and resource allocation for the data governance program; chairs the Data Governance Council. |
| **SOP Owner** | Dr. Klaus Weber, CPO/DPO | Maintains the currency of this SOP; interprets policy requirements related to privacy; approves data classification for Tier 0 assets. |
| **Data Governance Council (DGC)** | CDAO (Chair), CPO, General Counsel, VP of Engineering, Chief Information Security Officer (CISO), Business Unit Presidents | Approves enterprise-wide data standards, including the Business Glossary; resolves cross-domain conflicts; reviews and approves exceptions to metadata requirements. |
| **Data Domain Owner** | VP of Clinical Informatics (Clinical Data), CFO (Financial Data), VP of Product (Application Data), CISO (Security Data) | Ultimate accountability for all data assets within their domain; certifies the accuracy of Tier 0 and Tier 1 data lineage; approves data access requests. |
| **Data Steward** | Designated operational staff within each business unit (e.g., Clinical Data Analyst, Financial Systems Manager) | Daily curation of metadata, data quality rule monitoring, catalog entry, data dictionary maintenance, and first-line response to discovery inquiries. |
| **Technical Metadata Engineer** | Data Platform Engineering Team | Manages automated metadata harvesting agents (Alation’s Lineage Harvester, custom AWS Glue crawlers); ensures the technical performance and availability of the Alation catalog instance (`MHT-CAT-PROD-01`). |
| **AI/ML Engineer** | AI/ML Engineering Team | Documents machine learning models, training datasets, feature stores, and inference pipelines as data assets in the catalog, using the Meridian Model Card standard (see Related Policies). |
| **All Users** | Every Meridian employee, contractor, and approved third party | Responsible for reporting any discrepancies discovered between cataloged metadata and actual data structures or content; responsible for notifying Data Stewards of undocumented data assets encountered during work. |

### 3.2 RACI Chart

The following RACI chart outlines the division of responsibility for core Data Catalog procedures. (R=Responsible, A=Accountable, C=Consulted, I=Informed).

| Activity | Exec. Sponsor | SOP Owner / CPO | Data Domain Owner | Data Steward | Tech. Metadata Eng. | AI/ML Eng. | All Users |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Defining a new business term** | I | C | A | R | C | I | I |
| **Registering a new data asset** | I | I | A | R | R | I | C |
| **Classifying a data asset (Tier)** | I | A (for Tier 0) | A | R | C | C | I |
| **Certifying Lineage (Tier 0/1)** | I | C | A | R | R | C | I |
| **Fulfilling a discovery request** | I | I | C | R | I | I | C |
| **Submitting a metadata exception** | I | I | I | R | I | I | A |

---

## 4. Policy Statements

1.  **Universal Cataloging Mandate:** All in-scope data assets, originating from any source, must be registered in the enterprise Data Catalog (`MHT-CAT-PROD-01`) within 5 business days of their creation or initial discovery in the production environment. This applies to all assets in `us-east-1`, `us-west-2`, `eu-central-1`, and on-premises environments.

2.  **Metadata Completeness:** Every registered data asset must meet the Minimum Metadata Baseline (MMB), as defined in Section 5.3.3, prior to being considered operational. A data asset that is accessible to users but not meeting the MMB is deemed non-compliant and is subject to quarantine.

3.  **Data Classification:** All data assets must be assigned a Tier classification (Tier 0-3) by the accountable Data Domain Owner before being made accessible for use. PHI/PII or any regulated financial account data must always be classified as Tier 0.

4.  **Data Lineage:** Column-level lineage must be documented in the Data Catalog for all Tier 0 and Tier 1 data assets, tracing from source system to consumer endpoint (including any transformation, enrichment, or merging steps). Table-level lineage is the minimum required for Tier 2. Best-effort lineage is required for Tier 3.

5.  **Data Discovery:** The Data Catalog is the authoritative system of record for data discovery at Meridian. Data intended for cross-functional consumption must be discoverable via both technical metadata (schema names, column types) and curated business glossary terms. Direct access to raw data stores without catalog mediation is prohibited for non-engineering roles.

6.  **Data Subject Rights:** Meridian maintains procedures for honoring requests from individuals exercising their rights regarding their personal data within our systems. Data Owners and Stewards are responsible for locating responsive data using the catalog to support these procedures within a reasonable timeframe.

7.  **Data Protection Impact Assessments (DPIAs):** Meridian conducts DPIAs for high-risk data processing activities to identify and mitigate privacy risks. These assessments are documented centrally. Data Stewards must maintain accurate metadata for assets within processing activities under DPIA.

8.  **No Unauthorized Duplication:** No individual shall create a separate, unmanaged "shadow" data catalog or metadata repository, including in spreadsheets, wikis, or code repositories, to circumvent the enterprise catalog.

---

## 5. Detailed Procedures

### 5.1 Business Glossary Management

This procedure governs the creation, approval, and lifecycle of business terms within the Meridian Business Glossary, a module within the Alation catalog.

#### 5.1.1 Term Proposal
- **Trigger:** A Data Steward, Analyst, or business user identifies a need for a new, formally defined business term. This often arises from a new project, a new regulatory requirement, or a data quality investigation.
- **Search First:** The proposer must first search the existing Business Glossary in `MHT-CAT-PROD-01` to ensure the term does not already exist or that a synonym is not already defined. If a suitable synonym exists, a new term shall not be created; the existing term should be linked to the new asset.
- **Drafting:** The proposer drafts the new term definition using the **"New Business Term Proposal"** template accessible within the Alation UI. The template requires: `Term Name`, `Clear Definition (1-3 sentences)`, `Business Context`, `Related Technical Assets`, `Synonyms/Acronyms`, and `Data Domain`.

#### 5.1.2 Term Review and Approval
1.  The proposer submits the draft, which Alation automatically routes to the Data Steward for the specified Data Domain.
2.  The Data Steward reviews the proposal for completeness, clarity, and lack of overlap with existing terms. The Steward may edit the draft or reject it with a clear rationale. This review must be completed within **3 business days**.
3.  Upon Data Steward approval, Alation routes the term to the Data Domain Owner for certification. The Owner review is a light-touch accountability check, not a rigorous rewrite. This certification must be completed within **5 business days**.
4.  Once certified, the Steward publishes the term, making it active in the Business Glossary.

#### 5.1.3 Term Deprecation and Modification
- A Steward may propose a modification to a term’s definition or business context if they determine it is inaccurate. This follows the same review workflow.
- A term should be deprecated, not deleted, if it is no longer used. The Steward submits a deprecation request, providing a rationale and, where appropriate, linking to the replacement term. The Domain Owner approves the deprecation.

### 5.2 Data Asset Registration and Onboarding

This procedure defines how a new Data Asset is ingested into the `MHT-CAT-PROD-01` catalog. This is primarily an automated process for structured data sources.

#### 5.2.1 Automated Harvesting (Primary Method)
1.  **Source Connection:** The Technical Metadata Engineering Team is responsible for maintaining the Alation Data Source Connector for all authoritative data platforms (Snowflake, Production PGSQL instances, S3 data lakes). Connection parameters, including read-only service accounts, are maintained per standard InfoSec key management procedures.
2.  **Crawler Configuration:** A Metadata Extraction Job is configured in Alation for each source connection. The schedule is platform-dependent:
    -   **Snowflake:** Schema discovery every 4 hours; table/column profiling every 24 hours.
    -   **Amazon RDS for PostgreSQL:** Schema discovery every 6 hours; table/column profiling every 24 hours.
    -   **Amazon S3 (Structured Prefixes):** Object discovery every 8 hours. (Unstructured S3 data in Pinecone staging buckets is registered via a custom Lambda function on object creation event).
3.  **Automatic Asset Creation:** Upon successful scan, Alation creates or updates placeholder assets for all newly discovered schemas, tables, views, and columns.

#### 5.2.2 Manual Registration (Structured Assets Outside Automated Harvesting)
1.  **Initiation:** An AI/ML Engineer creating a new Feature Store table, or an architect creating a manually-managed API data source, must initiate the registration process. They navigate to the appropriate Data Domain in Alation.
2.  **"Register New Table" Wizard:** The user completes the wizard, providing the connection path, schema name, table name, and a plain-text description of the asset’s purpose.
3.  **Steward Review:** The wizard triggers a notification to the domain’s Data Steward. The Steward reconciles the manually-provided information, ensures classifications are accurate, and populates the metadata fields that would normally be automated (such as column definitions). The deadline for Steward to complete the MMB on a manually registered asset is **5 business days** from the notification.

#### 5.2.3 Minimum Metadata Baseline (MMB) Definition
An asset is not considered fully registered until the following fields are populated. The Alation UI provides a visual compliance indicator ("Compliance Score") for each asset.
- **Catalog Description:** A human-readable, plain-text description of the table/view/collection. (Mandatory)
- **Data Domain:** The high-level business grouping. (Mandatory)
- **Data Classification (Tier):** 0, 1, 2, or 3. (Mandatory)
- **Data Owner:** A valid, active Meridian employee assigned via the Alation profile. (Mandatory)
- **Steward:** A valid, active Meridian employee assigned. (Mandatory)
- **Key Business Terms:** At least one, and ideally up to five, relevant Business Glossary terms linked to the asset. (Mandatory for Tier 0-2)
- **Column-Level Definitions:** For Tier 0 and Tier 1 assets, every column must have a plain-text definition. For Tier 2, this is mandatory only for primary and foreign keys. (Conditionally Mandatory)
- **Lineage:** An artifact, whether auto-parsed or manually stitched, showing the asset’s origin. (Mandatory for Tier 0 and 1)

### 5.3 Data Dictionary and Technical Metadata

The Data Dictionary is a structural component of the Data Catalog, consisting of technical metadata harvested or manually entered for every column in a registered structured data asset.

#### 5.3.1 Technical Metadata Fields
For every column in a Tier 0, Tier 1, or Tier 2 data asset, the following technical metadata must be maintained and verified for accuracy:
- **Column Name:** The physical name in the source system.
- **Business Title:** A human-readable alias (e.g., `cust_acq_dt` becomes `Customer Acquisition Date`).
- **Data Type:** The technical data type (e.g., `VARCHAR(256)`, `TIMESTAMP_TZ`, `NUMERIC(18,4)`).
- **Nullability Constraint:** Indication of whether the field is nullable.
- **Primary/Foreign Key Designation:** Indication of key status.
- **Valid Value Constraints:** Where applicable, a link to a reference table, an enum list, or a description of expected value ranges.

#### 5.3.2 Quality Assurance
Data Stewards must execute a **"Data Dictionary Accuracy Audit"** for their top-10 most-used Tier 0 and 1 assets on a quarterly basis. This audit involves:
1.  Running the `alation_metadata_compliance_report.sql` script (maintained in Meridian’s private Git repository, `datagov/scripts`) against the source system.
2.  Comparing the actual schema from the source system against the cataloged metadata.
3.  Filing a correction ticket for any discrepancy between source and catalog exceeding a 1% variance in metadata completeness.

### 5.4 Data Lineage Harvesting

Lineage is foundational for impact analysis, root-cause diagnosis, and privacy compliance.

#### 5.4.1 Automated Lineage Generation
- **SQL Parsing:** The Alation Lineage Harvester agents, deployed in each major VPC, connect to Snowflake’s `QUERY_HISTORY`, PostgreSQL’s `pg_stat_statements`, and BI tools (Tableau Server) to parse SQL logic. This process automatically generates column-level lineage for data movement within these platforms.
- **ETL Ingestion:** Metadata from Matillion ETL jobs is ingested by Alation via REST API, stitching together lineage across disparate cloud-native and on-premises systems.

#### 5.4.2 Manual Lineage Stitching
Automated harvesting cannot trace lineage across all boundaries (e.g., an on-premises Oracle batch dump to an S3 landing zone processed by a Spark job).
1.  **Gap Identification:** The Technical Metadata Engineer, in collaboration with the relevant Steward, identifies a "Lineage Gap" from the Alation dashboard.
2.  **Manual Stitching:** Using the Alation "Manual Lineage" feature, the Steward creates a directional link between the source and target assets, annotating the link with a description of the undocumented process (e.g., "Nightly Tuxedo batch job `FIN_CLOSE`").
3.  **Certification:** For Tier 0 and Tier 1 data in regulated Business Units (Clinical AI Platform, HealthPay), the Domain Owner must certify the lineage diagram (both auto-generated and manually stitched) as accurate. This certification is a formal step recorded in Alation and is valid for 6 months.

### 5.5 Search and Discovery

The Alation Discovery Center is the front-end for all data discovery. Meridian standardizes on the `alation_natural_language_search` (ANLS) feature.

#### 5.5.1 Standard Discovery Workflow for Analysts
1.  **Initiation:** An Analyst in the MedInsight team needs data on 30-day readmission rates for a particular cohort. They log into `MHT-CAT-PROD-01` and enter the business query: `"30-day readmission rate calculation table"`.
2.  **Refinement:** The system returns a list of candidate tables, ranked by relevance to the search string and the Analyst’s role-based access. The Analyst filters by `Data Domain = "Clinical Data"` and `Classification = "Tier 1"`.
3.  **Triage:** The Analyst opens the top candidate table. They review the table description, linked business glossary terms (confirming the definition of "Readmission Rate"), and column-level definitions. Crucially, they examine the certified Lineage diagram to confirm the source of truth for the data (e.g., it originates from the EHR system, not a manually-adjusted spreadsheet).
4.  **Request for Access:** Satisfied that the asset is semantically correct, the Analyst uses the embedded "Request Access" link, which is a pre-formatted ticket to the Meridian Service Desk (ITSM tool: ServiceNow), routing the request to the named Data Domain Owner.
5.  **Work:** Once access is granted by the Owner (as a separate workflow governed by SOP-DGP-003 "Data Access Management"), the Analyst can use the fully documented schema to write their query.

#### 5.5.2 Federated Search
The catalog is federated to index Meridian’s Tableau Server content. This allows an Analyst to discover a published Tableau workbook containing "30-Day Readmission" metrics, trace it back to the underlying certified data sources in the catalog, and validate the metric’s provenance without having to open a new SQL editor.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

1.  **Segregation of Duties:** The person responsible for stewarding metadata (Data Steward) cannot be the person accountable for approving the asset’s classification Tier (Domain Owner). The catalog’s workflow engine enforces this separation.
2.  **Approval-Based Change Control:** Any change to the schema, description, or stewards of a Tier 0 or Tier 1 asset triggers an automated approval workflow in ServiceNow (`DataCatalog-Change-Mgmt`). The change is held in a "pending" state in Alation until the Domain Owner and, for privacy-sensitive changes, the CPO/DPO approve it.
3.  **Quarterly Attestation:** Each Data Domain Owner must log into the Data Catalog and sign an electronic attestation report confirming their review and accountability for the metadata of all Tier 0 and Tier 1 assets within their domain. This attestation is due by the 5th business day following the end of each calendar quarter.

### 6.2 Technical Controls

1.  **Immutable Audit Logs:** The Alation database’s internal audit trail, which logs every catalog interaction (search, view, edit, export), is streamed in near-real-time to Meridian’s centralized, append-only security log archive in an AWS GovCloud S3 bucket. Logs are retained for 5 years.
2.  **Row-Level Security in the Catalog:** The catalog is configured to respect source-level access controls. A user searching the catalog will see entries for tables they are not permitted to access, but they will not see any sampled data or column profiling results for those tables; the preview function is dynamically masked based on the user’s Snowflake or PostgreSQL role.
3.  **Catalog Access Restriction:** Write or edit access to the catalog (`MHT-CAT-PROD-01`) is strictly restricted via Meridian’s SSO (Okta) integration, governed by an Active Directory group `GRP-Data-Catalog-Stewards`. Only members of this group, representing all official Data Stewards and Technical Metadata Engineers, can modify metadata. All other users authenticate as read-only.

### 6.3 Data Quality Integration

Metadata is not useful if the data it describes is of unacceptable quality. Data quality rules, defined by Stewards and enforced via Soda Core (running on AWS EKS), are linked to catalog assets. A "Data Quality" tab is visible on each asset’s catalog page.
- **Passing:** A green "Verified Data" badge, including a timestamp of the last successful quality run.
- **Failing:** A red "Data Quality Issue" warning icon. The icon links to a ServiceNow incident ticket opened automatically by the Soda-Core-to-ServiceNow webhook. This ticket will contain the specifics of the breach (e.g., "Column `PATIENT_MRN` has 4% nulls, failing the 2% threshold rule").

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

A Data Governance dashboard, managed by the SOP Owner’s team and published in Tableau, tracks program health. The Data Governance Council reviews this dashboard at its bi-weekly meeting.

| Metric | Target | SLA / Measurement Method |
| :--- | :--- | :--- |
| **Catalog Completeness Score** | 95% for Tier 0 and Tier 1 assets. | ((Number of Tier 0/1 assets meeting MMB) / (Total number of Tier 0/1 assets)) * 100. Measured daily by an Alation Custom Report. |
| **Steward Responsiveness** | 90% of queries resolved within 24 business hours. | Mean time from a user-submitted "question" on a catalog asset to a final reply from the assigned Steward. |
| **Business Glossary Coverage** | < 5% orphaned terms. | An orphaned term is one that is in the Glossary but linked to zero active data assets. Report run weekly. |
| **Data Domain Owner Attestation** | 100% attestation completion. | Percentage of Domain Owners who have signed their Quarterly Attestation Report by the 5th-business-day deadline. |
| **Undocumented Data Asset Discovery** | < 2 per month. | Count of new assets discovered by the Security Engineering team during routine scans that are not registered in the catalog. |

### 7.2 Reporting Cadence

- **Daily:** Automated Alation completeness dashboards updated. Notifications sent to Stewards on assets falling below MMB.
- **Weekly:** "Metadata Health" email report, auto-generated from Tableau, distributed to all Stewards and Domain Owners, flagging stale or non-compliant assets in their purview.
- **Monthly:** A formal "Data Governance Scorecard" presentation prepared by the CPO/DPO’s office for the VP of Engineering and the CDAO.
- **Quarterly:** Full KPI review with the Data Governance Council; Domain Owner attestation cycle.

---

## 8. Exception Handling and Escalation

### 8.1 Catalog Registration Exception

A formal exception to the 5-day registration policy (Section 5.2.2) may be requested under specific, limited circumstances, such as a time-bound clinical trial with an urgent deadline or an exploratory data set under active development.
1.  **Requestor:** The Data Owner of the asset's domain.
2.  **Form:** The "Data Governance Exception Request" form in ServiceNow (`DG-EXCEPTION`), which requires: specific asset(s) impacted, specific provision of the SOP to be excepted, detailed business justification, compensating controls to be enacted, and an explicit sunset date not to exceed 90 days.
3.  **Routing:** The form is automatically routed to the SOP Owner (CPO/DPO) and the Chief Information Security Officer (CISO).
4.  **Approval:** The exception must be approved by both. A rejected exception cannot be appealed; the owner must bring the asset into compliance.
5.  **Tracking:** An approved exception is noted in the catalog as a tag on the asset (`exception:registration valid-until YYYY-MM-DD`). On the sunset date, if the asset is not compliant, the Technical Metadata Engineering team is authorized to revoke user access to the asset until compliance is achieved.

### 8.2 Escalation Path

Issues that cannot be resolved between a Steward and an Analyst or Engineer are escalated as follows:
1.  **Tier 1 (Operational Dispute):** Data Steward and end-user cannot resolve a terminology or definition conflict. Escalated to the Domain Owner. Resolution or binding decision within **5 business days**.
2.  **Tier 2 (Cross-Domain Conflict):** Two Domain Owners cannot agree on the definition of a shared term or the boundary of a data domain. Escalated to the Data Governance Council (via the CDAO). The Council’s ruling is final.
3.  **Tier 3 (Privacy/Ethical Issue):** Any issue involving potential privacy violations, unauthorized PHI exposure, or unethical use of data. Escalation is immediate, bypassing all other tiers, directly to the CPO/DPO and the General Counsel.

---

## 9. Training Requirements

All Meridian personnel who interact with the Data Catalog as part of their core role must complete the mandatory training curriculum.

### 9.1 Role-Based Training Matrix

| Training Module | Module ID | Target Audience | Frequency | Delivery |
| :--- | :--- | :--- | :--- | :--- |
| **Data Literacy & Governance Foundations** | DGC-101 | All employees | Annual | Online, Workday Learning |
| **Data Steward Certification: Alation Operations** | DGC-201 | Data Stewards, Tech. Metadata Engineers | Initial, plus annual refresher | 4-hour instructor-led course, virtual |
| **Data Discovery for Analysts & Scientists** | DGC-202 | Analysts, Data Scientists, AI/ML Engineers | Annual | 1-hour online course |
| **Data Classification & PHI Handling** | DGC-301 | Data Owners, Data Stewards | Annual | 2-hour instructor-led course, includes exam |
| **Data Subject Rights and DPIA Procedures** | DGC-401 | Data Owners, Data Stewards, Application Developers | Annual | 1-hour online course |

### 9.2 Training Compliance Tracking

Completion of all assigned modules is tracked through the Workday Learning Management System (LMS). An automated report identifies individual and business-unit completion rates. Managers are notified of non-compliant team members on a bi-weekly basis. Persistent non-completion (beyond a 30-day grace period) is escalated to senior management and may result in system access revocation, as mandated by the Acceptable Use Policy (SOP-IS-001).

---

## 10. Related Policies and References

### 10.1 Meridian Internal Policies

| SOP ID | Title | Relationship to this SOP |
| :--- | :--- | :--- |
| SOP-DGP-001 | Data Governance Policy | Overarching policy this SOP operationalizes. |
| SOP-DGP-002 | Data Classification and Handling | Defines the Tier (0-3) classification standard applied in this SOP. |
| SOP-DGP-003 | Data Access Management | Defines the access request and fulfillment process initiated from the Catalog. |
| SOP-DGP-005 | Data Quality Management | The operational procedures for the Data Quality rules and Soda Core checks referenced here. |
| SOP-DGP-006 | Data Retention and Disposal | Governs the lifecycle management applied by Data Owners; a catalog asset’s "retired" status triggers this SOP. |
| SOP-IS-001 | Acceptable Use of Information Assets | User agreement governing access to all systems, including `MHT-CAT-PROD-01`. |
| SOP-AIML-003 | Model Inventory and Model Card Standards | The AI/ML-specific procedure for registering models as catalog assets, referencing this metadata standard. |

### 10.2 External References

| Reference ID | Title | Description |
| :--- | :--- | :--- |
| REF-LEG-005 | EU General Data Protection Regulation (GDPR) | Foundational regulation for privacy controls, data subject rights, and impact assessments. |
| REF-ISO-001 | ISO/IEC 27001:2022 | Information security, cybersecurity and privacy protection framework. |
| DCAT-US-W3C | W3C Data Catalog Vocabulary (DCAT) v2 | External standard used to inform Meridian’s internal metadata interchange model for federated catalogs. |

---

## 11. Revision History

| Version | Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2023-01-18 | J. Patel (Data Gov) | Initial draft. Established cataloging mandate and basic MMB. |
| 1.1 | 2023-06-22 | K. Weber (CPO/DPO) | Minor revisions. Added GDPR-specific lineage requirements for Tier 0; updated Domain Owner attestation to quarterly. |
| 1.2 | 2024-02-10 | T. O'Connell (Tech Metadata Lead) | Updated to reflect migration from on-prem Informatica to Alation. Added automated harvesting procedures. |
| 2.0 | 2024-11-20 | K. Weber, M. Gonzalez | Major revision. Full rewrite for clarity and regulatory alignment. Introduced DPIA, data subject rights search procedures, and federated search. |
| 2.1 | 2025-04-03 | K. Weber | Minor revision. Updated technical harvesting intervals based on platform optimization; corrected broken ITSM links; re-framed escalation paths for efficiency. |
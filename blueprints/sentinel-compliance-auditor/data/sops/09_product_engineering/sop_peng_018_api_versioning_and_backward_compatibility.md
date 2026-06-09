---
sop_id: "SOP-PENG-018"
title: "API Versioning and Backward Compatibility"
business_unit: "Product & Engineering"
version: "2.4"
effective_date: "2024-06-08"
last_reviewed: "2025-05-14"
next_review: "2025-11-26"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: SOP-PENG-018
# API Versioning and Backward Compatibility

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the mandatory framework for managing Application Programming Interface (API) versioning, backward compatibility commitments, deprecation protocols, and client migration pathways across all Meridian Health Technologies, Inc. product lines. The purpose of this document is to ensure that all externally-facing and internally-critical APIs evolve in a predictable, documented manner that minimizes disruption to integrator partners, internal service teams, and regulatory compliance posture while enabling continuous product innovation.

This SOP defines the lifecycle of an API from initial public release through end-of-life decommissioning, specifying the temporal commitments Meridian makes to its API consumers, the processes by which breaking and non-breaking changes are classified and communicated, and the responsibilities of engineering teams in maintaining compatibility matrices.

### 1.2 Scope

This SOP applies to the following API categories across all Meridian business units and deployment regions:

| API Category | Description | Examples | Business Unit |
|---|---|---|---|
| Public APIs | RESTful and gRPC APIs exposed to external healthcare providers, payer organizations, and technology partners | Clinical AI Inference API, HealthPay Claims Submission API, MedInsight Cohort Query API | All |
| Partner APIs | Dedicated integration endpoints for named partners with contractual SLAs | EHR integration adapters (Epic, Cerner), payer gateway interfaces | Clinical AI Platform, HealthPay |
| Internal Service APIs | Inter-service communication within the Meridian SaaS Platform | Model Registry Service API, Patient Identity Resolution Service API, AuthZ/AuthN Service API | Product & Engineering |
| Administrative APIs | Management-plane APIs for platform operations | Tenant provisioning API, feature flag management API, audit log query API | IT Operations, Product & Engineering |
| Webhook and Event APIs | Asynchronous event delivery endpoints | Adverse event notification webhooks, claims status change callbacks | Clinical AI Platform, HealthPay |

**In Scope:**
- All API endpoints hosted under `api.meridian-health.com`, `api.meridian-health.eu`, and `api.meridian-health.sg` domains
- All service-to-service APIs within the Meridian SaaS Platform mesh (AWS us-east-1 and eu-west-1)
- APIs exposed through the Meridian Developer Portal
- APIs that process, transmit, or store Protected Health Information (PHI)
- APIs that produce or consume data subject to EU AI Act high-risk classification

**Out of Scope:**
- Internal administrative CLIs not exposed programmatically
- Direct database access protocols (ODBC/JDBC connections to Snowflake)
- Third-party APIs consumed by Meridian (vendor API management governed by SOP-VEND-003)
- Experimental or alpha-stage endpoints explicitly marked as `x-stability-level: experimental`

### 1.3 Audience

This SOP is binding upon:
- All Meridian Product & Engineering personnel, including full-time employees, contractors, and vendors with API development responsibilities
- Product managers responsible for API-facing product features
- Customer Operations personnel supporting integrator onboarding and issue resolution
- Quality Assurance engineers responsible for API compatibility testing
- Site Reliability Engineering (SRE) team members monitoring API service levels
- Any personnel authorized to approve API changes through the change management process

### 1.4 Regulatory Context

The API versioning and compatibility practices defined herein are designed to support Meridian's compliance obligations under SOC 2 Type II certification, specifically with respect to Change Management (CCx.x) controls. Uncontrolled, undocumented API changes that break integrator functionality may constitute a control deficiency. Clinical AI Platform APIs classified as high-risk AI systems under the EU AI Act Annex III must maintain documented version lineages to support transparency obligations under Article 13.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|---|---|
| **API** | Application Programming Interface — a defined contract for programmatic interaction between software components |
| **API Consumer** | Any software system, service, or application that invokes a Meridian API, whether internal or external |
| **API Contract** | The formal specification of an API's inputs, outputs, error modes, and behavioral guarantees |
| **Backward Compatible Change** | A modification to an API that does not require any action by API consumers; existing client implementations continue to function correctly without modification |
| **Breaking Change** | A modification to an API that requires API consumers to update their implementations to maintain correct function |
| **Deprecation** | The formal declaration that an API version or specific endpoint is scheduled for eventual removal |
| **Sunset / End-of-Life (EOL)** | The date upon which a deprecated API version is fully decommissioned and ceases to serve traffic |
| **Major Version** | An API version indicated by an increment in the major semantic version number (e.g., v2 → v3), indicating one or more breaking changes |
| **Minor Version** | An increment in the semantic version number indicating backward-compatible functional additions |
| **Patch Version** | An increment indicating backward-compatible defect corrections |
| **Migration Window** | The period between deprecation announcement and EOL during which API consumers must migrate to a successor version |
| **IDV** | Identity Document Verification — biometric document capture and analysis workflow |
| **KBA** | Knowledge-Based Authentication |
| **FHIR** | Fast Healthcare Interoperability Resources (HL7 standard) |
| **OpenAPI** | OpenAPI Specification (formerly Swagger) — the standard Meridian uses for REST API documentation |
| **SLAPI** | Service Level API — internal API for querying tenant-level service level compliance |
| **Developer Portal** | Meridian's external-facing portal at `developers.meridian-health.com` hosting API documentation, changelogs, and migration guides |
| **API Gateway** | Kong Enterprise API Gateway (Meridian's standard gateway layer across all deployment regions) |
| **BCIA** | Backward Compatibility Impact Assessment — the mandatory analysis performed before any breaking change proposal |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix

The following RACI (Responsible, Accountable, Consulted, Informed) matrix assigns roles for key activities governed by this SOP:

| Activity | API Product Manager | Engineering Lead | API Governance Board | Customer Operations | QA Engineering | SRE |
|---|---|---|---|---|---|---|
| API versioning strategy decisions | **R** | C | **A** | I | C | C |
| Breaking change impact assessment (BCIA) | R | **R** | **A** | C | R | C |
| Deprecation announcement publication | **R** | C | A | **R** | I | I |
| Migration guide authoring | C | **R** | A | R | I | I |
| Backward compatibility testing | I | R | I | I | **A** | C |
| Deprecation timeline enforcement | I | R | **A** | I | I | R |
| Developer Portal changelog maintenance | **R** | C | I | C | I | I |
| API consumer communication (deprecation notices) | R | I | A | **R** | I | I |
| Emergency breaking change authorization | C | C | **A** | I | C | R |

### 3.2 Named Roles and Responsibilities

#### 3.2.1 API Governance Board

The API Governance Board holds ultimate accountable authority for all versioning decisions, deprecation timeline approvals, and exception grants. The Board convenes bi-weekly or as needed for urgent matters.

**Composition:**
- VP of Engineering (Chair) — David Park
- Chief Architect — Maria Chen-Singh
- VP of Product, Clinical AI — Dr. Rebecca Okonkwo
- VP of Customer Operations — James Holloway
- Director of Information Security — (Voting Member)
- General Counsel or Designated Legal Representative — (Non-Voting Advisory)

**Authority:**
- Approve or reject breaking change proposals affecting Public or Partner APIs
- Grant or deny exception requests to standard deprecation timelines
- Authorize emergency sunset accelerations
- Ratify API versioning strategy revisions

#### 3.2.2 API Product Managers

API Product Managers are responsible for the product lifecycle of assigned API domains, including versioning roadmap development, deprecation communication authoring, and Developer Portal content accuracy. Each public-facing API domain shall have a designated API Product Manager documented in the Meridian Service Catalog.

**Current Assignments (as of effective date):**

| API Domain | API Product Manager |
|---|---|
| Clinical AI Inference APIs | Dr. Amir Nazari |
| HealthPay Claims & Billing APIs | Priya Krishnamurthy |
| MedInsight Cohort & Analytics APIs | Carlos Estevez |
| Platform Identity & Tenant Admin APIs | Sarah Winters |
| Webhook & Event Stream APIs | Dr. Amir Nazari (interim) |

#### 3.2.3 Engineering Leads

Engineering Leads are responsible for the technical implementation of versioning mechanisms, the execution of BCIA assessments, migration guide technical accuracy, and automated compatibility verification. Each service team shall designate an API Compatibility Owner responsible for maintaining a living compatibility matrix for all endpoints owned by that team.

#### 3.2.4 Customer Operations — API Support Team

The dedicated API Support Team within Customer Operations serves as the primary interface between Meridian and external API consumers regarding migration inquiries, deprecation timeline clarifications, and backward compatibility issue triage. This team maintains a shared mailbox (`api-support@meridian-health.com`) with a 4-hour acknowledgment SLA during business hours.

---

## 4. Policy Statements

### 4.1 Versioning Strategy

Meridian Health Technologies shall employ a **URL-path-based major versioning** strategy for all Public and Partner REST APIs, supplemented by **Semantic Versioning (SemVer)** in API response headers for minor and patch granularity.

**Policy Requirements:**

- **P4.1.1** All Public and Partner APIs shall encode the major version in the URL base path using the format `/v{major}/` (e.g., `/v2/patients`). No unversioned public endpoints are permitted after initial General Availability (GA) release.
- **P4.1.2** Major version increments are reserved exclusively for breaking changes. A new major version shall be released only when a BCIA has been approved by the API Governance Board.
- **P4.1.3** Minor version updates (backward-compatible functional additions) shall be reflected in the `X-Meridian-API-Version` response header, using SemVer format (`v{major}.{minor}.{patch}`), and shall not modify the URL path.
- **P4.1.4** Internal Service APIs may employ either URL-path versioning or a standardized `Accept-Version` custom request header. The mechanism for each internal service shall be documented in the service's `README.md` within the `meridian-health/services` monorepo and registered in Backstage (Meridian's internal developer portal).
- **P4.1.5** Webhook and Event APIs shall employ a `X-Meridian-Event-Schema-Version` header in delivered payloads. Webhook endpoint URLs shall include a major version segment. Breaking schema changes shall trigger a major version increment.

### 4.2 Backward Compatibility Commitment

Meridian Health Technologies makes the following binding compatibility commitments to API consumers:

| API Category | Minimum Concurrent Support of Previous Major Version After New Major GA | Breaking Change Moratorium Per Major Version | Notes |
|---|---|---|---|
| Public APIs | 18 months | 36 months | Except for critical security vulnerabilities |
| Partner APIs | Per contractual SLA (minimum 12 months) | Per contract | Some partner agreements specify longer windows |
| Internal Service APIs | 6 months | N/A | Internal teams negotiate migration via SRE |
| Administrative APIs | 12 months | 24 months | |
| Webhook APIs | 24 months | 36 months | Longer window due to async integration complexity |

- **P4.2.1** Meridian guarantees that a minimum of two major versions of any Public API will be concurrently supported and available for traffic serving at all times. The "previous" version (N-1) shall remain fully operational for the entirety of its documented deprecation window.
- **P4.2.2** For Partner APIs, specific minimum concurrent support terms shall be defined in the Partner Integration Agreement (PIA). In the absence of explicit PIA language, the Public API default of 18 months shall apply.
- **P4.2.3** During the concurrent support period, Meridian shall maintain identical deployment availability SLAs for both current and deprecated versions. No degradation of infrastructure quality or monitoring fidelity for deprecated endpoints is permitted prior to EOL.
- **P4.2.4** Breaking changes within an existing major version are strictly prohibited. The release of a new major version is the exclusive mechanism for introducing breaking changes.

### 4.3 Breaking Change Classification

A change shall be classified as **Breaking** if any of the following conditions are met:

| Breaking Change Category | Specific Examples |
|---|---|
| **Request Schema Modification** | Adding a new required field; removing an existing field; changing the data type of an existing field; changing validation rules that cause previously-accepted payloads to be rejected |
| **Response Schema Modification** | Removing a response field; changing the data type of a response field; changing field semantics (e.g., changing `dosage_mg` from integer to float) |
| **URI Change** | Renaming a path segment; altering query parameter semantics; removing an endpoint |
| **Authentication/Authorization Change** | Changing required OAuth scopes; altering token format requirements; switching authentication mechanisms |
| **HTTP Method Change** | Changing POST to PUT, GET to POST, etc. |
| **Error Response Change** | Changing HTTP status codes for known error conditions; altering the response body structure of error payloads |
| **Rate Limiting Change** | Reducing rate limit thresholds on existing endpoints |
| **Behavioral Change** | Modifying the side effects or business logic of an endpoint such that previous outcomes differ materially (e.g., a risk score calculation algorithm that produces materially different score distributions) |
| **Enum Value Removal** | Removing an accepted value from an enum field |

**Backward-Compatible Change Examples (Not Breaking):**

- Adding a new, optional request body field
- Adding a new response body field
- Adding a new endpoint (within the same major version)
- Adding a new accepted value to an enum (accept union expansion)
- Relaxing validation on an existing field
- Adding a new OAuth scope that is not required for the endpoint
- Adding a new HTTP method to an existing resource (e.g., adding HEAD support)
- Increasing rate limit thresholds

#### 5.2.2 Sub-Process B: Knowledge-Based Authentication (KBA)

For Tier 3 clinical APIs accessing individual patient-level PHI or producing clinical decision support outputs, the IDV process shall include a KBA challenge step. This uses Meridian's internal identity resolution service, cross-referencing provider credentialing databases (e.g., NPI registry, state medical board records). Three KBA questions shall be dynamically generated and must be answered correctly with a minimum score threshold of 2/3.

#### 5.2.3 Sub-Process C: Institutional and Role Verification

Upon successful completion of KBA, the system verifies the user's active affiliation with the registered customer organization and their assigned clinical role. This verification is performed against the Meridian Tenant and Identity Service. The user must hold a role enumerated in the `clinical_provider_roles` tenant configuration (e.g., `PHYSICIAN`, `NURSE_PRACTITIONER`, `PHYSICIAN_ASSISTANT`, `CLINICAL_PHARMACIST`).

### 4.4 Deprecation and Sunset Lifecycle

All API versions shall progress through a standardized lifecycle:

| Lifecycle Stage | Label in Developer Portal | Consumer Communication Requirement | Typical Duration |
|---|---|---|---|
| **GA (General Availability)** | None (current) | Proactive changelog updates; minor version release notes | Until successor announced |
| **Deprecation Announced** | `DEPRECATED` banner on documentation; `Sunset` HTTP response header | Email to registered Developer Portal contacts; in-app notification; account manager briefing notes | Duration of migration window (minimum 12 months) |
| **End-of-Life (EOL)** | `EOL: [date]`; endpoint returns HTTP `410 Gone` with migration pointer | Final 30-day, 14-day, and 7-day email reminders; Customer Operations proactive outreach to high-usage tenants | Day of EOL |

- **P4.4.1** No major version shall be sunset until its successor version has achieved GA status and has been available for a minimum of 6 months.
- **P4.4.2** The minimum migration window (period between deprecation announcement and EOL) for Public APIs shall be 12 months.
- **P4.4.3** The `Sunset` HTTP response header shall be included in all responses from deprecated API versions, following the format: `Sunset: Sat, 31 Dec 2026 23:59:59 GMT`. Additionally, `Deprecation: true` and `Link: <https://developers.meridian-health.com/migration/v3-claims>; rel="deprecation"; type="text/html"` headers shall be appended.

### 4.5 Documentation Requirements

- **P4.5.1** Each major version of each Public API shall have a distinct, version-scoped section on the Developer Portal, including an OpenAPI 3.1 specification.
- **P4.5.2** Every GA release of a new major version shall be accompanied by a published Migration Guide (see Section 5.4).
- **P4.5.3** The Developer Portal shall maintain a consolidated Changelog for each API, listing all breaking and non-breaking changes with dates and version identifiers, dating back to the previous two major versions.

---

## 5. Detailed Procedures

### 5.1 Procedure: Proposing a Breaking Change (BCIA Process)

This procedure is mandatory whenever an Engineering Lead or API Product Manager identifies a planned modification that meets the Breaking Change Classification criteria defined in Policy Statement P4.3.

#### 5.1.1 Step 1: BCIA Pre-Assessment

The initiating team (Engineering Lead and API Product Manager) shall conduct a preliminary impact quantification:

1.  **Identification:** Identify all affected API endpoints across all currently supported major versions.
2.  **Consumer Impact Analysis:**
    - Query the Kong API Gateway analytics for the trailing 90-day period to enumerate unique API consumers (tenant identifier, source IP aggregates) actively invoking the affected endpoints and versions.
    - Segment consumers into: External (Payer, Provider, Partner), Internal (Meridian service teams, internal tooling).
3.  **Impact Severity Classification:** Classify the proposed breaking change using the matrix below:

| Severity Class | Criteria | Approval Authority |
|---|---|---|
| **Class 3 — Minor Breaking** | Affects endpoints with <10 active external tenants; no PHI-transmitting endpoints; no Clinical AI Inference endpoints; workaround exists on current version | Engineering Lead + API Product Manager (joint) |
| **Class 2 — Moderate Breaking** | Affects 10-50 active external tenants, OR affects ≥1 PHI-transmitting endpoint, OR affects a Partner API | API Governance Board (quorum of 3) |
| **Class 1 — Major Breaking** | Affects ≥50 active external tenants, OR any Clinical AI Platform Inference API endpoint, OR any endpoint registered under EU AI Act Annex III classification, OR any HealthPay claims adjudication endpoint | API Governance Board (full quorum + General Counsel advisory vote) |

4.  **Documentation:** Complete the BCIA Pre-Assessment Template (Form `F-PENG-018-01`, available in Jira Service Management as `BCIA Pre-Assessment`) capturing:
    - API domain and affected major version(s)
    - Specific endpoints affected
    - Rationale for the breaking change (technical debt remediation, regulatory mandate, security vulnerability, product evolution)
    - Impact severity classification with supporting analytics data
    - Proposed successor version and migration window recommendation

#### 5.1.2 Step 2: BCIA Review and Approval

1.  **Submission:** The completed Form `F-PENG-018-01` shall be submitted as a Jira issue of type "API Breaking Change Request," linked to the parent Epic for the new major version development. The Jira issue shall be named in the format: `[API-Domain] BCIA: {Brief Description} — Class {N}`.
2.  **Governance Board Scheduling:** The API Governance Board administrative coordinator (rotating role, currently held by the VP of Engineering's Chief of Staff) shall place the BCIA on the agenda of the next available Board meeting. Class 1 matters shall be escalated for consideration within 5 business days.
3.  **Board Deliberation:** The Board shall review the BCIA, considering:
    - Alignment with product roadmap
    - Consumer impact quantification and mitigation feasibility
    - Regulatory implications (e.g., EU AI Act documentation lineage)
    - Availability of automated migration tooling
    - Timing relative to other planned breaking changes (consolidation analysis)
4.  **Decision:** The Board shall render one of the following decisions:
    - **Approved** — Breaking change authorized; successor version development proceeds.
    - **Approved with Conditions** — Conditional authorization with specified constraints (e.g., extended migration window, mandatory development of automated migration scripts, requirement to bundle with other breaking changes).
    - **Rejected** — Breaking change not authorized. Rationale documented.
    - **Deferred** — Decision deferred pending additional data or analysis.

#### 5.1.3 Step 3: Post-Approval Actions

Upon BCIA approval:

1.  **API Design Specification:** The Engineering Lead shall produce a complete OpenAPI 3.1 specification for the proposed successor major version within 15 business days of approval.
2.  **Migration Guide Initiation:** The API Product Manager shall initiate the Migration Guide document (see Section 5.4).
3.  **Developer Portal Stub:** A version-stub page for the successor version shall be published on the Developer Portal marked as `[UPCOMING: v{N+1}]` within 30 business days. This stub shall contain the planned GA date, summary of changes, and link to the draft Migration Guide once available.
4.  **Consumer Notification:** Customer Operations API Support Team shall email all registered Developer Portal contacts for the affected API domain. This "Intent to Deprecate" communication shall include: identification of the version to be deprecated, planned successor version number, planned deprecation announcement date, and planned minimum migration window.

### 5.2 Procedure: Executing a Deprecation Announcement

This procedure formalizes the transition of an API major version from GA to the Deprecation Announced lifecycle stage.

#### 5.2.1 Preconditions

- The successor major version has achieved GA status.
- The successor version has completed a minimum 6-month production availability period with demonstrated stability (SLO compliance ≥99.9%).
- A complete Migration Guide is published on the Developer Portal.
- The API Governance Board has provided final deprecation authorization (this may be part of the original BCIA approval or a separate "Deprecation Trigger" vote).

#### 5.2.2 Deprecation Announcement Execution

1.  **Technical Header Injection:** The SRE team shall configure the Kong API Gateway plugin (`deprecation-global`) to append the following headers to all responses from the deprecated version:
    - `Deprecation: true`
    - `Sunset: {EOL_Date_RFC_1123}` (must be a valid RFC 1123 HTTP-date)
    - `Link: <https://developers.meridian-health.com/migration/{api-domain}-v{major}-to-v{major+1}>; rel="deprecation"; type="text/html"`
2.  **Developer Portal Update:** The API Product Manager shall update the deprecated version's documentation pages to display a persistent yellow `DEPRECATED` banner, including the sunset date and link to the Migration Guide. The version selector component shall visually distinguish deprecated versions.
3.  **Changelog Publication:** A prominent "DEPRECATION NOTICE" entry shall be published in the API's changelog.
4.  **Direct Email Communication:** Customer Operations shall dispatch a templated "Official Deprecation Notice" email to:
    - All registered Developer Portal organization contacts associated with tenants actively invoking the deprecated version (derived from Kong analytics, trailing 90-day usage data).
    - All Partner contacts under active PIA agreements covering the affected API.
    - The internal `#api-consumers` Slack channel and engineering distribution list.
    - The email template shall include: deprecated version identifier, successor version identifier and documentation link, sunset date, Migration Guide link, and contact information for API support (`api-support@meridian-health.com`).
5.  **Account Manager Briefing:** Customer Operations shall brief all Account Managers responsible for affected accounts with tailored talking points and migration assistance offers.

#### 5.2.3 Monitoring During Migration Window

Throughout the migration window, the following shall be monitored weekly by the API Product Manager:

- Traffic volume to deprecated version (expectation: monotonic decline)
- Traffic volume to successor version (expectation: monotonic increase)
- Number of unique tenants still invoking deprecated version
- Migration-related support ticket volume (tag: `api-migration`)

If, at 90 days prior to EOL, ≥10% of original deprecation-announcement traffic volume remains on the deprecated version, an escalation (see Section 8) shall be triggered for proactive Customer Operations outreach.

### 5.3 Procedure: Executing End-of-Life (Sunset)

On the published EOL date, the following actions shall be executed:

1.  **Traffic Cutover:** The SRE team shall execute the pre-approved change request to cutover Kong routing rules. All traffic to the deprecated major version URL prefix shall return HTTP `410 Gone` with a JSON response body:
    ```json
    {
      "error": "GONE",
      "message": "API version v{major} has reached end-of-life. Please migrate to v{major+1}.",
      "documentation_url": "https://developers.meridian-health.com/migration/{api-domain}"
    }
    ```
2.  **Service Decommissioning:** The owning engineering team shall execute the decommissioning runbook, which includes: removal of deployment artifacts from ArgoCD, deletion of monitoring dashboards in Grafana for the deprecated version, archival of API Gateway analytics data, and update of the Meridian Service Catalog entry to mark the version as `EOL`.
3.  **Developer Portal Archival:** The deprecated version's documentation pages shall be moved to an "Archived Versions" section and clearly marked as no longer available. The OpenAPI specification file shall be retained in the `api-specs-archive` repository for auditability, with a retention period of 7 years per Meridian's Records Management Policy (SOP-LEG-002).
4.  **Final Communication:** A final "Version Sunset Complete" email shall be dispatched to the same distribution list as the deprecation notice.

---

### 5.4 Migration Guide Requirements

Every major version migration shall be accompanied by a Migration Guide published on the Developer Portal. The Migration Guide is a mandatory deliverable of the BCIA process and must be published no later than the GA date of the successor version.

#### 5.4.1 Required Sections

| Section | Content Requirements |
|---|---|
| **Overview** | Summary of what is changing, why, and the migration timeline (deprecation announcement, EOL date) |
| **Breaking Changes Catalog** | Exhaustive list of every breaking change, categorized by endpoint. Each entry must include: (a) Current behavior in deprecated version; (b) New behavior in successor version; (c) Required client-side code modification |
| **New Features and Capabilities** | Enumeration of new functionality available in successor version |
| **Deprecated and Removed Features** | Explicit list of removed endpoints, removed fields, removed query parameters, or removed enum values |
| **Data Model Changes** | If applicable, detailed mapping of entity schema changes |
| **Authentication Changes** | Detailed migration steps for auth mechanism modifications, including updated OAuth scopes table |
| **Migration Steps** | Ordered, actionable migration checklist. Include code snippets (Python, JavaScript, Java — minimum 3 languages) demonstrating before/after API call patterns |
| **Testing and Validation** | Recommended testing procedures; link to sandbox/staging environment for pre-migration validation; list of test scenarios |
| **Rollback Guidance** | Instructions for reverting to deprecated version if migration causes critical issues (only applicable during migration window) |

#### 5.4.2 Migration Assistance and SLAs

| Support Channel | Target Response SLA | Notes |
|---|---|---|
| `api-support@meridian-health.com` | 4 business hours acknowledgment; 1 business day substantive response | Ticket tagged `migration-assistance` |
| Developer Portal Migration Forum | 1 business day moderation | Community forum for integrator Q&A |
| Scheduled Migration Office Hours | Weekly during migration window | 2 x 1-hour sessions hosted by API Product Manager and Engineering Lead; recorded |
| Dedicated Migration Support (Partner) | Per PIA | For strategic partners, may include dedicated engineering liaison |

---

### 5.5 Procedure: Emergency Breaking Change

In the event of a critical security vulnerability (CVSS score ≥9.0) that necessitates a breaking change with accelerated timelines outside the standard BCIA process:

1.  **Declaration:** The Director of Information Security, in consultation with the VP of Engineering, shall formally declare an "API Security Emergency" via a written communication to the API Governance Board Chair.
2.  **Emergency Authorization:** The API Governance Board Chair (David Park, VP of Engineering) holds unilateral emergency authority to approve a breaking change and accelerated deprecation timeline. This authority shall be exercised in consultation with at least one additional Board member and the General Counsel.
3.  **Minimum Emergency Migration Window:** The migration window may be reduced to a minimum of 30 days for emergency breaking changes. In extraordinary circumstances posing imminent patient safety risk or active exploitation, the window may be reduced to 7 days, with written justification documented.
4.  **Post-Emergency Ratification:** Any emergency authorization shall be presented for full Board ratification at the next scheduled meeting.
5.  **Communication:** Emergency communications shall use the highest-priority notification channel available (email + Developer Portal site-wide alert banner + direct phone outreach to top-10 consuming tenants by traffic volume).

---

## 6. Controls and Safeguards

### 6.1 Versioning Technical Controls

| Control | Implementation | Ownership |
|---|---|---|
| **Kong Route Version Segregation** | Each API major version is configured as a distinct Kong Route, enabling independent traffic management, rate limiting, and monitoring. Route naming convention: `{service-name}-{api-domain}-v{major}` | SRE |
| **API Gateway Header Injection** | Global Kong plugin ensuring `Deprecation`, `Sunset`, and `Link` headers are injected on all responses from deprecated routes | SRE |
| **Schema Validation Enforcement** | All API Gateway routes configured with request/response validation plugins using the published OpenAPI specification. Requests or responses deviating from the published schema are rejected with HTTP 400/502 | Engineering Lead |
| **Breaking Change Static Analysis** | CI/CD pipeline (GitHub Actions workflow: `api-breaking-change-detection.yaml`) performs automated comparison of the proposed specification with the current GA specification. Any detected breaking change gates the merge until BCIA approval is attached as a Jira issue link in the pull request | Platform Engineering |
| **API Version Registry** | Centralized registry in Backstage (Meridian internal developer portal) cataloging all active API versions, their lifecycle stage, deprecation dates, and owning teams. This registry is the authoritative source for the Developer Portal | Product & Engineering |

### 6.2 Administrative Controls

| Control | Description | Cadence |
|---|---|---|
| **API Version Lifecycle Audit** | Quarterly review of all registered APIs against their declared lifecycle stage. Detects: stale deprecations not progressing to EOL, versions operating outside declared lifecycle, undocumented breaking changes in minor versions | Quarterly |
| **Developer Portal Compliance Scan** | Automated check confirming all Public APIs have versioned documentation pages, active changelogs, and accurate lifecycle stage labeling | Automated (nightly) |
| **BCIA Approval Gate** | Jira workflow automation preventing transition of "API Breaking Change Request" issues to "In Progress" without documented Governance Board approval | Continuous |

### 6.3 Testing Controls

| Test Type | Description | Trigger | Ownership |
|---|---|---|---|
| **Backward Compatibility Regression Suite** | Dedicated test suite maintaining client implementations written against all currently supported major versions. Assertions validate that these legacy client implementations continue to pass against the corresponding version endpoint | Nightly + on every PR to API service repository | QA Engineering |
| **Contract Testing (Pact)** | Pact contract tests registered for all Public APIs. Consumer contracts from known integrators (via Pact Broker) verified against provider builds | On every provider PR | Engineering Lead |
| **Deprecation Header Verification** | Automated integration test confirming `Deprecation: true` and `Sunset` headers present on all responses from deprecated routes | Nightly | QA Engineering |
| **410 Gone Verification** | Post-EOL verification test confirming deprecated routes return HTTP 410 with correct migration pointer body | On EOL change request execution | SRE |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| KPI | Definition | Target | Measurement Instrument |
|---|---|---|---|
| **KPI-01: Deprecation Timeline Adherence** | Percentage of deprecated API versions that progress to EOL within ±30 days of their published sunset date | ≥95% | API Version Registry vs. actual decommission dates |
| **KPI-02: Migration Window Compliance** | Percentage of deprecation announcements providing ≥minimum migration window duration (12 months for Public APIs) | 100% | Deprecation announcement date vs. EOL date delta |
| **KPI-03: BCIA Approval Cycle Time** | Median calendar days from BCIA submission to Board decision for Class 1 and Class 2 breaking changes | ≤15 calendar days | Jira issue history |
| **KPI-04: Consumer Migration Velocity** | Percentage of tenants migrated to successor version at T-90 days before scheduled EOL | ≥90% | Kong API Gateway tenant-level traffic analytics |
| **KPI-05: Undocumented Breaking Change Incidents** | Count of breaking changes released without accompanying BCIA approval | 0 | CI/CD pipeline gate enforcement + quarterly audit findings |
| **KPI-06: Migration Guide Completeness** | Percentage of mandatory Migration Guide sections present at successor GA date | 100% | Automated Developer Portal audit scan |

### 7.2 Dashboards

The following dashboards shall be maintained for operational visibility:

| Dashboard | Location | Audience | Refresh |
|---|---|---|---|
| **API Lifecycle Overview** | Grafana, folder `API-Governance` | API Governance Board, API Product Managers | Real-time |
| **Consumer Migration Tracker** | Grafana, folder `API-Governance` | Customer Operations, API Product Managers | Hourly |
| **Deprecation Compliance** | Looker Studio Report `API-Deprecation-Compliance` | VP of Engineering, Chief Architect | Daily |
| **BCIA Process Metrics** | Jira Dashboard `API Governance Board` | API Governance Board | Real-time |

### 7.3 Reporting Cadence

| Report | Audience | Frequency | Owner |
|---|---|---|---|
| **API Governance Board Dashboard Review** | Board Members | Bi-Weekly (during Board meeting) | VP of Engineering |
| **API Lifecycle Status Report** | All Engineering Directors, API Product Managers | Monthly | Chief Architect |
| **Deprecation Compliance Summary** | Product & Engineering Leadership, Customer Operations VP | Quarterly | VP of Engineering |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types and Handling

Deviations from any policy requirement in this SOP require formal exception approval. The following table defines the exception hierarchy:

| Exception Type | Description | Approval Required | Documentation Required |
|---|---|---|---|
| **Type E1: Migration Window Reduction** | Request to reduce the standard migration window (e.g., from 18 months concurrent support to 12 months) | API Governance Board (Class ≥2) or VP of Engineering + API Product Manager (Class 3) | Justification memorandum detailing rationale, consumer impact analysis, and mitigation plan |
| **Type E2: Breaking Change Within Major Version** | Extraordinary request to introduce a breaking change without creating a new major version | API Governance Board (full quorum + General Counsel) | Detailed justification; documentation of all alternatives considered and rejected; risk acceptance signed by requestor's VP |
| **Type E3: Emergency Sunset Acceleration** | As described in Procedure 5.5 | VP of Engineering + Director of Information Security + General Counsel | Post-hoc documentation within 5 business days |
| **Type E4: Unsupported Version Continuation** | Request to continue supporting a previously-scheduled EOL version beyond its sunset date | API Governance Board (quorum of 3) | Business justification including number of affected tenants, reasons for migration delay, committed new EOL date (cannot exceed 6 months extension) |

### 8.2 Escalation Paths

| Scenario | Primary Escalation Contact | Secondary Escalation Contact |
|---|---|---|
| Consumer migration stalls at T-90 before EOL (KPI-04 below threshold) | API Product Manager escalates to Customer Operations VP (James Holloway) | API Governance Board |
| BCIA approval delays exceeding 15 calendar days | Requesting Engineering Lead escalates to VP of Engineering (David Park) | CEO (Dr. Sarah Chen) |
| Unauthorized breaking change detected post-deployment | Director of Information Security, immediate rollback via incident management process (SOP-INC-001) | CEO |
| Partner API migration dispute | VP of Customer Operations; if unresolved, Account Executive escalates to VP of Product, Clinical AI | General Counsel |

### 8.3 Exception Registry

All approved exceptions shall be recorded in the API Governance Exception Registry (maintained as a Confluence database `API Governance Exceptions`) with the following fields: Exception ID, Date Approved, Approver, Requestor, API Domain, Exception Type, Description, Expiration Date, and Link to Approval Documentation. Exceptions are not permanent; all exceptions shall have a defined expiration date, not exceeding 12 months from approval.

---

## 9. Training Requirements

### 9.1 Required Training Modules

| Training Module ID | Module Title | Target Audience | Initial Completion Requirement | Refresher Cadence |
|---|---|---|---|---|
| **TR-API-101** | API Governance at Meridian: Principles and Practices | All Product & Engineering personnel | Within 30 days of hire or role transition | Annual |
| **TR-API-102** | BCIA Process: Conducting and Documenting Breaking Change Impact Assessments | Engineering Leads, API Product Managers, Staff+ Engineers | Prior to submitting first BCIA | Biannual |
| **TR-API-103** | API Lifecycle Operations: Deprecation, Sunset, and Migration Support | Customer Operations API Support Team, API Product Managers, SRE | Within 30 days of assignment to API-facing role | Annual |
| **TR-API-104** | Contract Testing and Backward Compatibility Verification | QA Engineering, Engineering Leads | Prior to owning an API with active consumers | Annual |

### 9.2 Training Delivery and Tracking

- Training modules are hosted on Meridian's Learning Management System (LMS) — `learning.meridian-health.com`.
- Completion is tracked via the LMS and surfaced in the personnel compliance dashboard reviewed monthly by Engineering Directors.
- **Non-Compliance:** Personnel who have not completed required training within the mandated window shall have their API change approval privileges suspended in Jira until compliance is achieved.
- **Content Ownership:** The API Governance Board owns the curriculum content. The VP of Engineering designates a Training Coordinator responsible for annual content review and update.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs and Policies

| Document ID | Title | Relationship |
|---|---|---|
| SOP-SEC-004 | Secure Development Lifecycle | Defines secure coding practices applicable to API development; references this SOP for API change management integration |
| SOP-INC-001 | Incident Management and Response | Governs incident response for API outages, including those caused by failed version deployments |
| SOP-CM-003 | Change Management — Production Deployments | Governs the change request process for production deployments; API EOL cutovers must comply |
| SOP-CUST-007 | Customer Communications — Product Changes | Defines templated communication standards referenced by deprecation communication procedures herein |
| SOP-LEG-002 | Records Retention and Data Governance | Governs retention periods for API specifications, BCIA records, and communications archives |
| SOP-VEND-003 | Vendor and Third-Party API Management | Governs Meridian's consumption of external APIs; out of scope for this SOP but cross-referenced |
| SOP-COMP-005 | EU AI Act Compliance — Clinical AI Systems | Defines transparency and documentation requirements for Clinical AI Platform; API version lineages are a sub-component |
| SOP-DATA-009 | PHI Data Handling and Transmission | Governs any API transmitting PHI; versioning must not compromise data protection controls |

### 10.2 External Standards and References

| Reference | Relevance |
|---|---|
| OpenAPI Specification 3.1.0 | Standard specification format for Meridian REST APIs |
| Semantic Versioning 2.0.0 (SemVer) | Basis for internal version signaling in response headers |
| HL7 FHIR R4 (Fast Healthcare Interoperability Resources) | Standard data model for healthcare interoperability; relevant to Clinical AI and MedInsight APIs |
| IETF RFC 8594 — Sunset HTTP Header | Standards-track specification for the `Sunset` and `Deprecation` HTTP header fields |
| Kong Gateway Enterprise Documentation (v3.x) | Meridian's API Gateway technology; plugin configuration references |

---

## 11. Revision History

| Version | Date | Author | Changes Summary |
|---|---|---|---|
| 1.0 | 2021-02-15 | David Park (initial author), Maria Chen-Singh | Initial SOP creation; established basic versioning policy (URL-path major versioning) and 6-month deprecation window for Public APIs |
| 1.1 | 2021-09-03 | Maria Chen-Singh | Added Internal Service API category; clarified QA testing responsibilities |
| 2.0 | 2022-06-20 | David Park, Dr. Amir Nazari | Major revision: Extended Public API migration window from 6 to 12 months; introduced BCIA process and API Governance Board authority; added Webhook and Event API category; formalized deprecation header injection via Kong |
| 2.1 | 2022-11-15 | Dr. Amir Nazari | Incorporated EU AI Act Annex III considerations for Clinical AI Platform APIs; added KBA and IDV procedures for clinical API access |
| 2.2 | 2023-04-10 | David Park | Updated exception handling framework; refined KPI definitions and added Consumer Migration Velocity metric; clarified emergency breaking change authority |
| 2.3 | 2023-09-12 | Dr. Amir Nazari, Priya Krishnamurthy | Migrated documentation platform to new Developer Portal; updated links; added Pact contract testing control; introduced OpenAPI 3.1 requirement |
| 2.4 | 2024-06-08 | David Park, Maria Chen-Singh | Comprehensive review and restructure. Extended Public API concurrent support from 12 to 18 months. Added Class 1/2/3 severity classification for BCIA. Formalized Migration Guide mandatory sections. Updated all role assignments and contact information. Transitioned CI/CD breaking change detection from manual to automated GitHub Actions workflow. Ratified by Dr. Sarah Chen. |
| 2.4 (current) | 2025-05-14 | David Park | Annual review completion. No substantive changes required; confirmed continued alignment with regulatory obligations and operational practices. Updated next review date. |

---

**Document Approval**

*This SOP has been approved via the Meridian Policy Governance workflow. The approver's electronic signature is recorded in ServiceNow Policy & Compliance Management (SOP-PENG-018, Version 2.4).*

**Approver:** Dr. Sarah Chen, Chief Executive Officer
**Date:** 2025-05-14
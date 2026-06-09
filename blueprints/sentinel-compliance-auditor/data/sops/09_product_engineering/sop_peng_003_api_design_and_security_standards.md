---
sop_id: "SOP-PENG-003"
title: "API Design and Security Standards"
business_unit: "Product & Engineering"
version: "4.9"
effective_date: "2025-03-22"
last_reviewed: "2026-04-14"
next_review: "2026-10-12"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# SOP-PENG-003: API Design and Security Standards

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure establishes the mandatory design, development, deployment, and maintenance standards for all Application Programming Interfaces (APIs) created, procured, or operated by Meridian Health Technologies, Inc. The document defines a unified architectural approach that ensures all APIs are secure by design, comply with applicable regulatory frameworks, deliver consistent developer experiences, and protect the confidentiality, integrity, and availability of protected health information (PHI) and other sensitive data processed across the Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the underlying Meridian SaaS Platform.

### 1.2 Scope

This SOP applies to:

| In Scope | Out of Scope |
|---|---|
| All RESTful APIs, gRPC services, and GraphQL endpoints developed by Meridian Engineering teams | Third-party APIs consumed by Meridian systems (governed by SOP-SEC-012, Third-Party Risk Management) |
| Internal service-to-service APIs within the Meridian SaaS Platform | Direct database access patterns not exposed via API layers |
| Public, partner, and customer-facing APIs across all business units | Legacy SOAP services scheduled for decommissioning under Program Atlas |
| API gateways, service meshes, and API management infrastructure | Messaging queue configurations (governed by SOP-INF-007, Event Streaming Standards) |
| APIs processing PHI, PII, payment card data, or model inference data | |
| APIs hosted in AWS us-east-1 and eu-west-1 regions | |

### 1.3 Applicability

All full-time employees, contractors, consultants, and third-party development partners engaged in API design, development, testing, deployment, or operation within Meridian Health Technologies must adhere to this SOP. Deviation from these standards requires formal exception approval per Section 10 of this document.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| API Contract | A formal, machine-readable specification (OpenAPI 3.1 or Protocol Buffers proto3) defining all endpoints, request/response schemas, authentication requirements, and error codes for an API |
| API Consumer | Any authenticated system, service, or external developer invoking a Meridian API endpoint |
| Breaking Change | Any modification to an API that would cause a previously valid consumer request to fail, including field removal, type changes, URL path changes, or authentication mechanism alterations |
| Delinquency Stage | A classification bucket assigned to accounts with past-due obligations, maintained in the HealthPay Collections Module |
| PHI Endpoint | Any API route that transmits, processes, or stores Protected Health Information as defined under HIPAA (reference: SOP-CMP-001, Data Classification and Handling) |
| Rate Limiting Window | A sliding 60-second interval for per-consumer request counting, resetting at the conclusion of each window |
| Soft Collection | Automated communications (email, SMS, in-app notification) sent to accounts 1-30 days past due, before human agent contact |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| ABAC | Attribute-Based Access Control |
| API GW | Meridian API Gateway (Kong Enterprise, deployed in AWS) |
| ASVS | OWASP Application Security Verification Standard |
| CAP | Corrective Action Plan |
| CVE | Common Vulnerabilities and Exposures |
| CVSS | Common Vulnerability Scoring System |
| DLP | Data Loss Prevention |
| DPT | Data Protection Team (sub-function of InfoSec, reporting to Rachel Kim, CISO) |
| FHIR | Fast Healthcare Interoperability Resources (HL7 FHIR R4) |
| HIPAA | Health Insurance Portability and Accountability Act of 1996 |
| IAM | Identity and Access Management (Meridian Okta tenant) |
| JWT | JSON Web Token |
| mTLS | Mutual Transport Layer Security |
| OAS | OpenAPI Specification |
| OWASP | Open Worldwide Application Security Project |
| PII | Personally Identifiable Information |
| PHI | Protected Health Information |
| RBAC | Role-Based Access Control |
| SIEM | Security Information and Event Management (Meridian Splunk Cloud instance) |
| SLA | Service Level Agreement |
| TTL | Time To Live |
| WAF | Web Application Firewall (AWS WAF) |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix

| Role | API Design | Security Review | Approval | Incident Response | Ongoing Monitoring |
|---|---|---|---|---|---|
| VP of Engineering (David Park) | A | — | R | A | I |
| Chief Information Security Officer (Rachel Kim) | C | A | R | A | I |
| Director of Platform Engineering (Sarah Chen) | R | R | C | C | A |
| Lead API Architect (currently recruited; interim: David Park) | A/R | C | C | — | C |
| Senior Security Architect (James Okonkwo) | C | A/R | C | R | R |
| Engineering Team Leads (per squad) | R | C | — | I | I |
| Data Protection Officer (Elena Rossi) | C | C | I | C | C |
| Developer Experience Lead (Priya Mehta) | C | — | — | — | R |
| Site Reliability Engineering Lead (Marco Diaz) | C | C | — | R | R |
| Compliance Officer (Thomas Keller) | I | I | I | I | R |

**Key:** R = Responsible (executes work), A = Accountable (signs off), C = Consulted (provides input), I = Informed (receives status)

### 3.2 Named Role Responsibilities

**David Park, VP of Engineering** — Ultimate accountability for API standards compliance across all Meridian product lines. Approves all exceptions to mandatory API design controls. Reviews and signs quarterly API security posture reports.

**Rachel Kim, CISO** — Owns API security control design. Approves all PHI-bearing API deployments to production. Conducts biannual API threat modeling exercises. Reviews penetration test findings for API attack surface.

**Lead API Architect (Interim: David Park)** — Maintains the Meridian API Style Guide, reviews all new API contracts before sprint grooming, conducts monthly API design office hours.

**Engineering Team Leads** — Ensure squad adherence to this SOP during sprint execution. Conduct code reviews verifying compliance with Sections 6 and 7. Escalate deviations within 24 hours per Section 10.

**SRE Lead (Marco Diaz)** — Maintains API Gateway configuration. Monitors API availability SLAs (99.95% for PHI endpoints, 99.9% for non-PHI). Owns rate limiting and circuit breaker configurations.

---

## 4. Policy Statements

### 4.1 API-First Development Mandate

All new service capabilities at Meridian Health Technologies shall be exposed via APIs designed under contract-first principles. Engineering teams must author and secure peer review of the API specification (OpenAPI 3.1 or Protocol Buffers proto3) before writing implementation code. No API may enter a production sprint without an approved API contract registered in the Meridian API Registry (Backstage, `api.meridian.internal`).

### 4.2 Security by Default

Every Meridian API endpoint shall enforce authentication via OAuth 2.0 with JWT bearer tokens, augmented by mTLS for service-to-service communication within the AWS VPC boundary. Anonymous access is prohibited without a documented, time-bound exception signed by the CISO. All APIs transmitting PHI or payment data shall implement additional ABAC controls validated on every request.

### 4.3 Data Minimization

API response schemas must return only data fields required to fulfill the documented use case. APIs exposing PHI shall default to the FHIR R4 "summary" data scope; full resource representations require an explicit `Prefer: return=representation` header and elevated authorization scope.

### 4.4 Versioning and Backward Compatibility

APIs shall employ URI-path versioning (e.g., `/v1/patients`). Deprecation of a major version requires a minimum 12-month advance notice to external consumers and 6-month notice for internal consumers. Non-breaking additive changes may be deployed to an existing version without version increment. Breaking changes always require a new major version.

### 4.5 Breach Notification Obligation

In the event of a confirmed security incident involving an API that processes PHI, the incident response team shall execute the Meridian Breach Notification Protocol (SOP-SEC-005), including notification to affected individuals, the Secretary of Health and Human Services, and applicable state authorities as required by law. The protocol mandates internal escalation within 60 minutes of confirmed breach detection and convening of the Breach Response Committee (comprising the CISO, General Counsel, DPO, and VP of Engineering) to assess notification obligations.

---

## 5. Detailed Procedures

### 5.1 API Design Workflow

#### 5.1.1 Contract Authoring

1. The Product Manager (PM) drafts a Business Requirement Document (BRD) and submits it to the Lead API Architect via Jira (`API-ARCH` project).
2. The Lead API Architect or delegated Engineering Team Lead creates a new branch in the `meridian-api-specs` GitLab repository.
3. The spec author creates the OpenAPI 3.1 document using the Meridian API Template (available in the Developer Portal under "Standards > Templates").
4. The author completes all required sections:
    - `info` block with Meridian contact email (`api-support@meridianhealthtech.com`)
    - `servers` block denoting regional endpoints (us-east-1, eu-west-1)
    - `security` block referencing the `BearerAuth` and `OAuth2` schemes from the Meridian Common Components library
    - All `paths` with full request/response schemas, including `4xx` and `5xx` error responses per Meridian Error Schema v2.3

#### 5.1.2 API Design Review (ADR)

1. The author submits a Merge Request (MR) in GitLab, assigning `Lead API Architect` and `Security Architecture` as required approvers.
2. The automated GitLab CI pipeline executes the Meridian API Linter (`spectral` with custom rulesets located in `ci/api-linter-rules/.spectral.yaml`). The pipeline MUST pass with zero critical and zero high-severity findings before human review.
3. The Lead API Architect conducts a synchronous or asynchronous review within 3 business days, evaluating:
    - Adherence to RESTful resource naming conventions
    - Appropriate HTTP method usage
    - Response envelope consistency
    - Hypermedia (HATEOAS) linking structure for Level 3 maturity endpoints
4. James Okonkwo (Senior Security Architect) completes a security-focused review, verifying:
    - Absence of sensitive data in URL path parameters
    - Correct OAuth scope definitions per resource
    - Input schema `minLength`, `maxLength`, `pattern`, `minimum`, `maximum` constraints
    - Absence of deprecated TLS cipher suites (enforced by API GW, but contractually noted)
5. Approval from both reviewers grants the "api-contract-approved" label, unblocking sprint implementation.

#### 5.1.3 Implementation Gate

1. Engineering Team Lead ensures the approved API contract is linked to the Jira implementation epic.
2. Developers scaffold the service using the `meridian-cli generate` command, pointing to the approved contract.
3. Automated integration tests MUST validate that the live implementation matches the contract (contract-driven testing via Pact Broker at `pact.meridian.internal`).

### 5.2 API Security Hardening Procedure

Before any API deployment advances to staging (`staging.meridian.internal`) or production (`api.meridianhealthtech.com` and `api.meridianhealthtech.eu`), the Security Hardening Checklist must be completed and attached to the deployment Change Request in ServiceNow.

#### 5.2.1 Authentication Configuration

1. **External APIs (Consumer-Facing):** Configure Kong API Gateway to accept OAuth 2.0 Client Credentials or Authorization Code grant types. JWTs signed by Okta (`iss: https://meridian.okta.com`) with RS256 algorithm.
2. **Internal APIs (Service-to-Service):** Configure Istio service mesh to enforce mTLS with SPIFFE-compliant X.509 SVIDs, augmented by JWT bearer tokens carrying service identity claims.
3. **Partner APIs (HealthPay, MedInsight):** Configure mutual TLS (mTLS) with client certificate validation at API GW, plus OAuth 2.0 with `partner` audience claim.

#### 5.2.2 Authorization Configuration

1. Identify resource-level access patterns. Document them in the Meridian IAM Matrix (maintained by Elena Rossi, DPO, in Confluence: `IAM-Matrix`).
2. Define Okta authorization scopes using the pattern: `resource:action[:sensitivity]`. Examples:
    - `patient:read:phi`
    - `payment:create`
    - `inference:execute`
3. For APIs processing PHI, implement ABAC policies in Open Policy Agent (OPA) sidecars. Policies must evaluate:
    - User/Service role
    - Purpose of use (e.g., `TREATMENT`, `PAYMENT`, `OPERATIONS`)
    - Data sensitivity category
    - Geographic origin (EU vs US region)

#### 5.2.3 Input Validation Configuration

1. Enable request body validation within Kong API Gateway using the Kong Request Validator plugin, referencing the JSON Schema generated from the approved OpenAPI specification.
2. For all string fields, configure validation against OWASP ASVS 4.0 requirements:
    - Free-form text fields: Max length enforced, validation against common injection patterns using regular expression deny-lists.
    - Structured fields (dates, IDs): Strict type and format validation.
3. Implement content-type validation: reject requests with `Content-Type` not matching the API contract specification.

#### 5.2.4 Rate Limiting and Throttling Configuration

1. Apply the Meridian standard rate limiting tiers via Kong Rate Limiting Advanced plugin:
    - **Tier 1 (Public Health, Anonymous):** 10 requests/second per IP
    - **Tier 2 (Partner, Authenticated):** 100 requests/second per API key
    - **Tier 3 (Internal Service):** 500 requests/second per service identity
2. For endpoints triggering computationally expensive model inference (Clinical AI Platform), supplement with a concurrency limiter (Kong Request Termination plugin for rate exceeding, returning `429 Too Many Requests` with `Retry-After` header).

### 5.3 API Deployment and Promotion Procedure

#### 5.3.1 Staging Deployment

1. Engineering Team Lead merges the implementation code to the `staging` branch.
2. GitLab CI/CD pipeline builds container image, scans with Grype for container vulnerabilities, and pushes to AWS ECR `staging` registry.
3. Infrastructure as Code (Terraform, `meridian-infra` repo) applies the API Gateway route, service, and plugin configuration to the `staging` Kong Admin API.
4. Automated Smoke Test Suite (Postman collection `API-Smoke-Tests`, executed from GitLab CI) runs against the staging gateway.
5. Security Scan (OWASP ZAP baseline + custom active scan policies) executes against all new/modified endpoints. All High and Critical findings must be remediated or waived by CISO before production promotion.

#### 5.3.2 Production Deployment

1. A ServiceNow Change Request ("CR") is submitted with attached:
    - Approved Staging Deployment Report (GitLab pipeline pass)
    - Security Scan Report with zero open High/Critical findings (or approved risk acceptance from CISO)
    - Completed Security Hardening Checklist
2. SRE Lead (Marco Diaz) or delegate reviews CR within 24 hours (standard) or 4 hours (emergency).
3. Upon approval, Terraform applies configurations to production Kong Admin API.
4. Synthetic monitors (DataDog) activate for new API endpoints, measuring latency, error rate, and availability against defined SLIs.
5. Engineering Team Lead verifies functionality within 1 business day and closes the CR.

### 5.4 API Documentation and Developer Portal Management

1. Upon successful staging deployment, the approved OpenAPI specification is automatically ingested into the Meridian Developer Portal (Backstage) via the GitLab-Docs pipeline.
2. Within 5 business days of staging deployment, the responsible Engineering Team Lead or Product Manager must publish a "Getting Started" guide for the API in the Developer Portal. The guide must include:
    - Authentication setup instructions
    - Sample use case walkthroughs
    - Link to the interactive API console (Swagger UI or similar)
3. Documentation for production APIs must be reviewed and updated at least once per product release cycle (quarterly for most BUs). Documentation freshness is tracked by the Developer Experience Lead (Priya Mehta), with a KPI of "Docs Freshness > 95%."

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

| Control ID | Control Description | Implementation Detail | Frequency |
|---|---|---|---|
| A-01 | API Design Review | Mandatory review of all API contracts by Lead API Architect and Security Architect per Section 5.1.2 | Per API Version |
| A-02 | Security Hardening Checklist | Completed, reviewed, and approved checklist attached to every production deployment CR | Per Major Deployment |
| A-03 | Quarterly API Security Audits | Internal audit conducted by the Governance, Risk, and Compliance (GRC) team, sampling 20% of active production APIs against this SOP | Quarterly |
| (HIPAA) A-04 | Annual API Security & Privacy Training | All Engineering and Product personnel complete mandatory training module "API Security and PHI Handling" in Litmos. Training covers: OWASP API Top 10, Secure Coding, PHI Data Minimization, and Incident Reporting procedures. | Annual |
| A-05 | Third-Party API Risk Assessment | All partner-facing APIs undergo a formal risk assessment (led by Vendor Risk Management, Thomas Keller) before go-live | Per Partner Onboarding |

### 6.2 Technical Controls — Network and Gateway

| Control ID | Control Description | Implementation Detail |
|---|---|---|
| T-01 | API Gateway Enforcement | All external API traffic routes exclusively through Kong Enterprise, deployed in a dedicated DMZ VPC (AWS `meridian-dmz-prod`). Direct access to backend services is blocked by security group rules. |
| T-02 | Web Application Firewall (WAF) | AWS WAF ruleset "Meridian-API-Baseline" applied to the Application Load Balancer fronting the API Gateway. Rules include: SQL Injection detection, Cross-Site Scripting detection, and IP Reputation (AWS Managed Rule for Amazon IP Reputation List). |
| T-03 | Intrusion Detection/Prevention (IDS/IPS) | Amazon GuardDuty monitors API Gateway access logs and VPC Flow Logs for anomalous behavior (e.g., crypto-mining activity, unusual IAM behavior). Findings of Severity "High" auto-create an incident in PagerDuty. |
| T-04 | mTLS Enforcement (Internal East-West) | All service-to-service communication within the Kubernetes cluster (EKS) is routed through the Istio service mesh, with mTLS enabled in `STRICT` mode for the `meridian-data` namespace. |
| T-05 | Data Loss Prevention (DLP) | Kong "AI/ML Guard" plugin scans responses from PHI endpoints for patterns matching credit card numbers (PCI-DSS) or unformatted Social Security Numbers. Detection triggers blocking and an alert to the SOC. |

### 6.3 Technical Controls — Application Security

| Control ID | Control Description | Implementation Detail |
|---|---|---|
| T-06 | JWT Validation | Kong JWT plugin validates signature (RS256), issuer (`iss`), audience (`aud`), and expiry (`exp`). Clock skew tolerance: 5 seconds. |
| T-07 | Scope Validation | Custom Kong plugin "Opa-Sidecar-Callout" makes a gRPC call to an OPA sidecar for every PHI-bearing request, evaluating ABAC policies (per 5.2.2). Decision latency SLA: ≤ 10ms (p99). |
| T-08 | Output Encoding/Escaping | All response bodies are passed through a context-aware encoding filter in the API Gateway. JSON content is encoded to prevent JavaScript injection in consuming UIs. |
| T-09 | Request Size Limiting | Kong "Request Size Limiting" plugin rejects payloads exceeding **1 MB** (standard) or **5 MB** (document/binary endpoints). 413 Content Too Large returned. |
| T-10 | Audit Logging | Every API request generates a structured log event to Splunk via the Kong HTTP Log plugin. Log payload includes: Timestamp, Consumer ID, Request Path, Method, Response Code, Latency (ms), Correlation ID, and masked request/response body (for PHI endpoints, per SOP-SEC-003, Logging and Monitoring). |

### 6.4 PHI Data Handling Controls (Specific)

1.  **Encryption:** All PHI in transit via APIs MUST use TLS 1.3. At rest, PHI cached in API Gateway or backend services must be encrypted using AES-256-GCM. Key management via AWS KMS.
2.  **Data Minimization:** API response schemas must default to `FHIR R4 Summary` when returning patient data. Full records require an explicit `X-Data-Scope: full-phi` header, which triggers an elevated alert in Splunk for audit purposes.
3.  **Audit Trail:** Every access, modification, or deletion request targeting a FHIR resource containing PHI must log the `User-Agent`, `PurposeOfUse` claim from the JWT, and a unique trace ID for end-to-end reconstruction.
4.  **Workforce Training:** Annual training per Control A-04 is required. Failure to complete training by the annual deadline results in immediate revocation of access to engineering systems and API gateways until remediated.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs) and Service Level Objectives (SLOs)

| Metric Category | KPI / SLO | Measurement Tool | Target | Reporting Cadence |
|---|---|---|---|---|
| **Availability** | Uptime for Production APIs (PHI) | Datadog Synthetics | 99.95% monthly | Monthly, SRE Dashboard |
| | Uptime for Production APIs (Non-PHI) | Datadog Synthetics | 99.9% monthly | Monthly, SRE Dashboard |
| **Performance** | Median API Gateway Latency (p50) | Datadog APM (Kong Plugin) | < 80ms | Weekly, Squad Stand-up |
| | Tail Latency (p99) for PHI APIs | Datadog APM (Kong Plugin) | < 400ms | Weekly, Squad Stand-up |
| **Security** | Rate of 4xx Errors (AuthN/AuthZ Failures) | Splunk Dashboard "API-Health" | < 5% of all requests | Weekly, Security Review |
| | Open High/Critical Vulnerabilities | DefectDojo (from DAST/SAST) | = 0 | Continuous, per build |
| | Time to Remediate Critical API Vulnerability | Jira | < 48 hours | Monthly, CISO Report |
| **Documentation** | Docs Freshness Score | Internal tool `api-docs-scorer` | > 95% | Monthly, Developer Portal |

### 7.2 Dashboards and Alerting

- **Real-time Operational Dashboard:** Datadog dashboard "API-Gateway-Prod-Overview." Displays request rate, error rate (4xx/5xx), and latency percentiles per service. On-call SRE receives PagerDuty alert if error rate exceeds 5% for 5 minutes on a PHI endpoint.
- **Security Posture Dashboard:** Splunk dashboard "API-Security-Posture." Aggregates failed authentication attempts, blocked by WAF, rate limiting hits, and DLF violations. SOC Analyst Level 1 monitors during business hours.
- **Business Health Dashboard (HealthPay):** Tableau dashboard tracking collection API success rates, delinquency stage transitions, and recovery rates. Viewed by VP of Finance weekly.

### 7.3 Reporting Cadence

| Report | Audience | Owner | Frequency |
|---|---|---|---|
| API Sprint Security Review | CISO (Rachel Kim), VP Eng (David Park) | Sr. Security Architect (James Okonkwo) | Bi-weekly |
| SOC 2 Control Evidence Package | External Auditors, Compliance Officer | Compliance Officer (Thomas Keller) | Semi-annual (Audit Period) |
| API Program Status Report | CTO, CISO, Product Leadership | Lead API Architect | Monthly |

---

## 8. Exception Handling and Escalation

### 8.1 Policy Exceptions

Situations may arise where immediate compliance with a specific mandate in this SOP is not technically feasible or would cause disproportionate business impact. In such cases, a formal exception may be granted on a temporary basis. Non-compliance without a documented and approved exception constitutes a policy violation subject to disciplinary action.

### 8.2 Exception Request Procedure

1. The Requestor (typically an Engineering Team Lead) drafts an **API Standard Exception Request** using ServiceNow form `API-Exception-Request`.
2. The form requires:
    - Reference to the specific section(s) of SOP-PENG-003 for which exception is sought.
    - Technical justification detailing why the standard cannot be met.
    - Detailed compensating controls to be put in place for the duration of the exception.
    - Proposed duration (maximum 90 days for initial request).
3. The form routes for approval to:
    - **Technical Approver:** Lead API Architect (or VP of Engineering for exceptions to design/performance standards).
    - **Security Approver:** CISO (or Sr. Security Architect for non-PHI, non-authentication related exceptions).
    - **Business/Compliance Approver (for PHI or Payment APIs):** Data Protection Officer (Elena Rossi).
4. All three approvals are required. Any rejection returns the request to the Requestor.
5. Upon approval, the Exception is logged in the GRC Exception Register and an automatic review task is scheduled 15 days before expiry.

### 8.3 Escalation Path for Security Incidents

1. A security incident involving a Meridian API (e.g., data breach, token leakage, active injection attack) must be reported immediately by the observer via PagerDuty (`@meridian-security-oncall`) or, if preferred, by calling the SOC hotline (`x5555`).
2. **First Responder (SOC Analyst L1):** Acknowledges the alert within 15 minutes. Initiates the Incident Response Playbook for "API Security" in TheHive (Meridian's SOAR platform). Contains the incident (e.g., by revoking API key or disabling a route via Kong Admin API emergency script).
3. **Escalation L2 (Sr. Security Architect, James Okonkwo):** Engaged within 30 minutes for any PHI-related incident or confirmed unauthorized access. Leads forensic investigation.
4. **Escalation L3 (CISO, VP of Engineering, DPO, General Counsel):** Convened as the Breach Response Committee for any confirmed breach of PHI. Determines breach notification obligations per Meridian Breach Notification Protocol. Decisions are documented in a formal Breach Response Report within 72 hours.

---

## 9. Training Requirements

### 9.1 Role-Based Training Matrix

| Training Module | Target Audience | Method | Frequency | Tracking System |
|---|---|---|---|---|
| **API Security & PHI Handling Essentials** | All Engineering, Product, SRE, and QA personnel | Instructor-led (virtual) + assessment | Annual (before Q1 end) | Litmos LMS |
| **Secure API Design Masterclass** | Engineering Team Leads, Senior Engineers, API Architects | Self-paced eLearning (Litmos course: `API-SEC-401`) | On hire; renewed every 2 years | Litmos LMS |
| **OWASP API Top 10 Deep Dive** | All front-end, back-end, and full-stack engineers | Recorded workshop + lab exercises | Annual (before Q3 end) | Litmos LMS |
| **HIPAA for Engineers** | All personnel touching code paths processing PHI | Classroom (led by Compliance Officer, Thomas Keller) | On hire; then annual | Litmos LMS & HR file |
| **Kong & API Ops** | SRE, Platform Engineers | Self-paced (Meridian Internal Wiki) | Continuous; validated by competency quiz | Litmos LMS |

### 9.2 Training Compliance and Non-Completion

Compliance with training requirements is mandatory. The Developer Experience Lead (Priya Mehta) runs a monthly Training Compliance Report from Litmos.

- **Non-Completion:** Individuals who fail to complete required annual training by the assigned deadline will have their access to AWS, GitLab, and API Gateway administrative consoles suspended. Access is reinstated within one business day of training completion.
- Manager performance reviews incorporate training compliance as an objective metric. Repeated failures to meet training deadlines result in formal Performance Improvement Plans.

---

## 10. Related Policies and References

### 10.1 Meridian Internal Policies

| SOP-ID | Title | Relationship |
|---|---|---|
| SOP-SEC-001 | Information Security Management System | Overarching security policy. This SOP is subordinate. |
| SOP-SEC-003 | Logging, Monitoring, and Alerting Standards | Defines logging formats consumed by Splunk dashboard in Section 7. |
| SOP-SEC-005 | Incident Response and Breach Notification | Defines escalation path and notification procedures referenced in Sections 4.5 and 8.3. |
| SOP-SEC-012 | Third-Party Risk Management | Governs APIs consumed by Meridian. |
| SOP-CMP-001 | Data Classification and Handling | Defines PHI, PII, and other data classifications referenced in Section 5. |
| SOP-INF-007 | Event Streaming and Asynchronous Messaging Standards | Governs Kafka-based internal communication, an alternative to synchronous gRPC. |
| SOP-PENG-001 | Software Development Lifecycle (SDLC) | Governs the overarching development process within which API design fits. |
| SOP-PENG-007 | Secure Coding Standards | Provides language-specific secure coding rules complementing these API-level standards. |

### 10.2 External Standards and Frameworks

- **NIST SP 800-53 Rev. 5:** Security and Privacy Controls for Information Systems and Organizations (Controls AC-4, AC-6, AU-3, SC-7, SC-8, SC-13, SI-4).
- **OWASP API Security Top 10:2023:** Used as the foundational threat model for API security controls.
- **HL7 FHIR R4 (Release 4):** The standard for healthcare data exchange, used as the basis for all Clinical API and MedInsight schemas.
- **SOC 2 TSC 2017 (CC6.1, CC6.6, CC6.7, CC7.1):** Logical security and monitoring criteria satisfied by controls in this SOP.
- **HIPAA Security Rule (45 CFR § 164.312):** Technical Safeguards, specifically Access Control (§164.312(a)), Audit Controls (§164.312(b)), and Transmission Security (§164.312(e)).
- **PCI DSS v4.0 (Requirements 6, 7):** Applicable to HealthPay APIs.

---

## 11. Revision History

| Version | Date | Author | Summary of Changes |
|---|---|---|---|
| 4.9 | 2025-03-22 | David Park / James Okonkwo | Major revision. Deprecated Legacy API v1 sunset details. Integrated new OPA sidecar for ABAC (Sect 6.3, T-07). Updated roles matrix per Q4 re-org. Added DLP plugin control (T-05). Updated OWASP reference to 2023 version. |
| 4.4 | 2024-10-05 | James Okonkwo | Introduced new API Linting CI/CD step (5.1.2). Strengthened input validation guidelines per pen-test finding #MERIDIAN-2024-09-112. Updated Rate Limiting Tier values. |
| 4.0 | 2024-04-18 | David Park / Sarah Chen (Platform) | Major structural rewrite. Moved from PDF to web-native (GitLab-hosted). Added "API-First Development Mandate." Expanded Roles with RACI matrix. Aligned all security controls with SOC 2 TSC 2017 framework. |
| 3.2 | 2023-09-01 | Thomas Keller (Compliance) | Minor policy fix. Clarified annual HIPAA training requirement for all engineering staff handling PHI (Section 9.1). Updated breach escalation path names. |
| 3.1 | 2023-03-15 | David Park | Full policy review cycle. Updated tools from legacy (Apigee) to Kong Enterprise. Added GraphQL support to Scope section. Updated link to Data Classification SOP. |

---

**APPROVED:**

_________________________
**Dr. Sarah Chen, CEO**
Date: 2026-04-14

_________________________
**David Park, VP of Engineering**
Date: 2026-04-14
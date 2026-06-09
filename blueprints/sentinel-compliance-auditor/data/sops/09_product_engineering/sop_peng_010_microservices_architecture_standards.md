---
sop_id: "SOP-PENG-010"
title: "Microservices Architecture Standards"
business_unit: "Product & Engineering"
version: "4.8"
effective_date: "2025-11-24"
last_reviewed: "2026-01-02"
next_review: "2026-07-07"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Microservices Architecture Standards

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the mandatory architectural principles, design standards, and operational requirements governing the design, development, deployment, and operation of all microservices within the Meridian Health Technologies ecosystem. The purpose is to ensure that all services—spanning the Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the underlying Meridian SaaS Platform—are built with consistency, reliability, security, and operational excellence as foundational attributes. This SOP directly supports Meridian’s compliance posture with SOC 2 Trust Services Criteria (TSC), specifically as they relate to Security, Availability, and Processing Integrity.

Deviation from these standards jeopardizes product stability, data integrity, patient safety, financial reporting accuracy, and Meridian’s regulatory standing under SOC 2, EU MDR, and FDA guidelines. Compliance with this SOP is therefore non-negotiable.

### 1.2 Scope

This SOP applies to all Engineering and Platform teams within the Product & Engineering business unit.

**In-Scope Systems and Activities:**
- All new microservices developed for the Meridian SaaS Platform, Clinical AI Platform, HealthPay Financial Services, and MedInsight Analytics.
- All existing microservices undergoing refactoring, version upgrades, or significant feature enhancement, which must be brought into alignment with the standards herein per the timelines defined in Section 10.3 of SOP-SEC-015 (System Security & Operational Hygiene Standards).
- All service-to-service communication fabrics, including synchronous REST/gRPC APIs and asynchronous event streams managed via the Meridian Message Bus (MMB), an Apache Kafka cluster operated by the Platform Engineering team.
- Container orchestration, runtime security, and networking policies enforced via the Meridian Kubernetes Fleet (EKS on AWS, administered via Rancher).
- All observability pipelines: logging (ELK), metrics (Prometheus/Thanos), distributed tracing (Jaeger), and alerting (PagerDuty).
- CI/CD pipelines managed via GitLab CI and ArgoCD, including gates for architectural compliance validation.

**Out of Scope:**
- Third-party vendor SaaS products not hosted within the Meridian AWS infrastructure (e.g., Salesforce, Workday). Integrations *with* these systems, however, are handled by Integration Gateway Services, which are themselves in-scope microservices.
- Legacy monoliths (e.g., `MED-CORE-MONO`) are in a frozen state and governed by SOP-PENG-005 (Legacy System Maintenance Mode Protocols) and are explicitly exempt, except where new microservices must interface with them.

**Applicable Teams:** All squads within the Clinical Engineering, HealthPay Engineering, Platform Engineering, and Data Engineering Tribes, as defined in Section 3.

---

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
| :--- | :--- |
| **API Gateway** | The single entry point for all external client traffic, managed via Kong Enterprise. Handles authentication, rate limiting, and request routing. |
| **Bounded Context** | A core concept from Domain-Driven Design defining the boundary within which a specific domain model is defined and applicable. At Meridian, this is the primary determinant of service boundaries. |
| **C4 Model** | A hierarchical set of software architecture diagrams (Context, Container, Component, Code) used as the standard for documenting architecture at Meridian. |
| **CI/CD** | Continuous Integration / Continuous Deployment. The automated pipeline from code commit to production deployment, managed via GitLab CI and ArgoCD. |
| **CQRS** | Command Query Responsibility Segregation. A pattern that separates read and update operations for a data store. Mandated for high-throughput, complex business logic services. |
| **DR** | Disaster Recovery. Procedures and infrastructure for restoring service in the event of a catastrophic regional failure. Governed by SOP-DR-001. |
| **EKS** | Amazon Elastic Kubernetes Service. The underlying compute platform for all containerized microservices. |
| **gRPC** | A high-performance, open-source universal Remote Procedure Call framework. The mandated standard for synchronous intra-cluster service-to-service communication at Meridian. |
| **Jaeger** | The open-source distributed tracing system used at Meridian, backed by an OpenSearch storage cluster. |
| **MMB (Meridian Message Bus)** | The internal, centrally-managed Apache Kafka cluster used for all asynchronous event-driven communication. Governed by Schema Registry. |
| **MTTR** | Mean Time to Recovery. A key availability metric measuring the average time to restore service from an incident. |
| **RTO / RPO** | Recovery Time Objective / Recovery Point Objective. The maximum tolerable duration of a service outage and the maximum tolerable data loss, as defined in SOP-DR-001. |
| **SLO / SLI** | Service Level Objective / Service Level Indicator. A target value for a service metric (SLI), e.g., 99.9% availability over a 30-day rolling window. |
| **SOC 2 TSC** | System and Organization Controls 2, Trust Services Criteria. The framework used for the specific security, availability, and processing integrity controls referenced in this document. Reference: TSP Section 100, 2017 Trust Services Criteria for Security, Availability, Processing Integrity, Confidentiality, and Privacy. |

---

## 3. Roles and Responsibilities

The following RACI matrix details the responsibilities for the microservices lifecycle.

| Activity / Decision | Product Owner | Technical Lead (Squad) | Principal Engineer | Tribe Lead Engineer | VP, Engineering (D. Park) | VP, InfoSec (A. Vance) | Platform Engineering |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Service Boundary Definition** | C | R | A | - | - | - | I |
| **Architecture Design Document (ADD)** | I | R | A | I | - | - | C |
| **Data Model & Schema Design** | C | R | C | A | - | - | - |
| **Communication Protocol Selection** | - | C | R | A | - | - | C |
| **Observability Implementation (Logs, Metrics, Traces)** | - | R | - | - | - | - | A |
| **Resilience Pattern Implementation (Circuit Breaker, etc.)** | - | R | C | I | - | - | A |
| **CI/CD Pipeline Configuration** | - | R | C | - | - | - | A |
| **SOC 2 Control Adherence & Evidence** | I | R | C | I | A | R | C |
| **Exception Approval (Architectural)** | I | C | C | R | A | I | I |
| **Deprecation & Decommissioning** | R | C | C | A | I | I | R |

- **Product Owner (PO):** Accountable for the “what” and “why,” ensuring business value. Must be consulted on bounded context definitions but does not approve technical standards.
- **Technical Lead (Squad):** Responsible for the architectural integrity of the squad’s services and ensuring compliance with this SOP at the implementation level.
- **Principal Engineer:** Reports to VP of Engineering. Provides cross-tribe architectural governance, approves Architecture Design Documents, and is the final technical authority for deviations from this SOP.
- **Tribe Lead Engineer:** Accountable for the overall technical health and roadmap of a specific tribe (e.g., Clinical AI). Acts as the approver for major architectural decisions within their domain.
- **VP, Engineering (David Park):** Owner of this SOP. Approves all policy-level exceptions and is the final authority for budgetary or strategic decisions related to architecture.
- **VP, Information Security (Aria Vance):** Accountable for the interpretation and implementation of all SOC 2 security controls, approving security-related architectural patterns and providing final approval for security control deviations.
- **Platform Engineering** (led by Manager, Platform Ops): Responsible for building, maintaining, and operating the core platform components (Kubernetes, Kong, MMB, CI/CD templates, observability stack) that enforce these standards. They act as Accountable for the platform-level controls.

---

## 4. Policy Statements

The following high-level policy statements are mandatory and must be reflected in all Architectural Design Documents (ADDs, see Section 5.1.1) and service implementations.

1.  **Domain-Driven Design (DDD) Boundaries:** All microservice boundaries MUST be derived from business `Bounded Contexts` and sub-domains (Core, Supporting, Generic), as modeled using the EventStorming technique. A service’s boundary, API, data ownership, and communication pattern are a direct reflection of the domain model. No service shall be created solely to wrap a database table.
2.  **Data Sovereignty:** Every microservice MUST be the single source of truth for its data domain and MUST own its data persistence exclusively. No other service is permitted to directly access another service’s datastore. All data access must occur via a published API. This is a critical control for SOC 2 (TSC PI1.3, PI1.5).
3.  **Polyglot Persistence:** Service teams are permitted to select the persistence technology best suited for their data model (e.g., Amazon DynamoDB, Amazon Aurora PostgreSQL, Amazon ElastiCache). The choice must be documented and justified in the ADD.
4.  **API-First Design:** All service APIs (both internal gRPC and external REST via Kong) MUST be designed using an API-first approach. The API contract must be defined and reviewed using Protocol Buffers (`internal/api/proto/`) and OpenAPI Specifications (`internal/api/oas/`) before implementation begins.
5.  **Ephemeral Compute:** All microservices MUST be stateless and ephemeral. Any state requiring persistence must be externalized to a backing service (database, cache). This ensures horizontal scalability and rapid instance replacement. (Relevant to SOC 2 TSC A1.2).
6.  **Design for Failure:** Every integration point with an external dependency (another service, MMB, database) MUST incorporate resilience patterns. At minimum, this includes retries with exponential backoff, request timeouts, and graceful degradation. Critical paths MUST implement a circuit breaker pattern.
7.  **Observability by Default:** Every service, from its first deployment, MUST emit structured logs to stdout, core business metrics to Prometheus, and propagate distributed tracing spans via the OpenTelemetry SDK. A service is **not** considered “production-ready” without these three telemetry pillars.
8.  **Security by Design:** All inter-service traffic within the Meridian mesh MUST be encrypted via mTLS (mutual Transport Layer Security), managed by the Linkerd service mesh. Authentication and authorization must follow the zero-trust principle, using short-lived JSON Web Tokens (JWTs) issued by the Meridian Identity Service (`svc-identity`). Every endpoint must verify the token, and RBAC must be enforced per-method where applicable. (Addresses SOC 2 TSC CC6.1, CC6.3).

---

## 5. Detailed Procedures

This section outlines the mandatory step-by-step processes for the lifecycle of a Meridian microservice.

### 5.1 Service Genesis and Design

Before a single line of application code is written, the following procedure must be completed.

#### 5.1.1 The Architecture Design Document (ADD)

The Technical Lead of the responsible squad must create an Architecture Design Document (ADD) using the template stored in the Product & Engineering Confluence space: `Template: Microservice ADD v3.2`.

The ADD must detail the following, as mandated by the `ADD Review Checklist`:
- **Service Identity:** A unique, immutable, and descriptive name conforming to the pattern `<domain>-<function>-svc` (e.g., `clinical-diabetes-risk-svc`, `healthpay-claims-adjudicator-svc`).
- **Domain Context:** A C4 Context and Container diagram showing the service’s place in the Meridian ecosystem. A clear definition of its Bounded Context and the Domain Events it publishes or subscribes to.
- **API Contract:** A draft of the primary `.proto` (for gRPC) or `openapi.yaml` (for external-facing REST) file.
- **Data Model:** A logical Entity-Relationship Diagram (ERD) detailing the entities it owns. The ADD must explicitly state how the service will own its data and enforce the policy against direct database access by other services.
- **Communication Patterns:** A clear justification for all chosen patterns (Sync gRPC, Async Event via MMB, etc.), listing all upstream dependencies.
- **Observability Plan:** Confirmation that the standard metrics, structured logging (JSON format), and tracing configuration will be implemented.
- **Resilience Plan:** A failure mode analysis for all key dependencies, detailing specific patterns (circuit breaker config, retry logic, fallback behavior).

The completed ADD is then submitted via a Pull Request to the `architecture-decision-log` repository, tagging the assigned Principal Engineer for formal review and approval (per the RACI in Section 3). No work may commence without an approved ADD.

#### 5.1.2 Scaffolding the Service Repository

Once the ADD is approved, the squad must generate the service repository from the centralized `meridian-service-template` using the Platform Engineering CLI tool.

```bash
meridian-cli service create --name <domain>-<function>-svc \
  --language java \ # or go, python
  --template-version 4.0
```

This scaffold provides a compliant starting point including: a multi-stage Dockerfile, `.gitlab-ci.yml` pipeline skeleton, basic Helm chart, OpenTelemetry SDK auto-configuration, a basic health endpoint (`/healthz`, `/readyz`), and an empty `ADD.md` file to be populated with the approved ADD content.

### 5.2 Service Communication Standards

All inter-service communication must adhere to one of the two sanctioned patterns.

| Pattern | Sanctioned Implementation | Use Case | Mandatory Configuration |
| :--- | :--- | :--- | :--- |
| **Synchronous** | **gRPC over HTTP/2**, via Linkerd service mesh. | Command-and-query interactions requiring immediate consistency or low-latency response. | mTLS via Linkerd. Request timeout: 5000ms (default). Must be overridden per endpoint if needed. |
| **Asynchronous** | **Apache Kafka (MMB)**, using Avro for message serialization. | Domain Event publishing, CQRS command buses, data synchronization across bounded contexts. | Schema Registry enforced. Message TTL defined. Mandatory Dead Letter Queue (DLQ) for poisoned messages. |

**Explicitly Prohibited Patterns (Without Exception Approval from Principal Engineer):**
- Direct HTTP/REST calls between internal services.
- Shared databases or a shared “integration” schema.
- Unsecured, unencrypted communication channels.
- Any custom TCP/UDP protocol.

#### 5.2.1 Synchronous Communication (gRPC) Procedure

1.  **Contract Definition:** The service provider defines the `.proto` file in their repository, including the `version` metadata.
2.  **Server-side Implementation:** The provider implements the generated server stub.
3.  **Client-side Implementation:** The consumer service's developer locates the required `.proto` file and generates a client stub, configuring a **connection deadline** of 5000ms and an **exponential backoff retry policy** for `UNAVAILABLE` and `DEADLINE_EXCEEDED` error codes (max 3 retries).

#### 5.2.2 Asynchronous Communication (MMB/Avro) Procedure

1.  **Schema Registration:** The producer service registers the new event's Avro schema with the **Meridian Schema Registry** (`schema-registry.internal.aws.meridian.com`).
2.  **Topic Provisioning:** The Platform Engineering team automatically provisions a new Kafka topic on the MMB upon merge to `main` of a `.meridian/kafka-topics.yaml` file in the producer's repository. Standard topic configuration includes `replication.factor=3` and `min.insync.replicas=2`.
3.  **Producer:** The service sends Domain Events using the `MeridianEventPayload` wrapper, which includes required headers: `eventId`, `eventType`, `eventTimestamp`, `sourceService`, and `correlationId`.
4.  **Consumer:** The consuming service subscribes to the topic and deserializes the Avro payload. It MUST use **at-least-once processing** semantics and implement an **idempotent consumer** pattern, using the `eventId` to deduplicate messages.

### 5.3 Observability Procedure

Every service must implement the "Golden Signal" dashboards automatically.

1.  **Metrics Exposure:** Services MUST expose a Prometheus metrics endpoint at the standard port `9090/metrics`. The four golden signals must be instrumented for every operation:
    - **Latency:** `meridian_http_request_duration_seconds` (Histogram)
    - **Traffic:** `meridian_http_requests_total` (Counter)
    - **Errors:** `meridian_http_requests_total{status_code=~"5.."}` (Counter derived from Traffic metric)
    - **Saturation:** `meridian_service_thread_pool_active_threads` (Gauge)
2.  **Structured Logging:** All application logs MUST be written to `stdout` in a single-line JSON object per log event. The JSON payload MUST contain the following standard fields:
    - `timestamp`: RFC 3339 format.
    - `level`: `INFO`, `WARN`, `ERROR`.
    - `service`: The service's unique name.
    - `traceId` and `spanId`: Populated automatically by the OpenTelemetry SDK.
    - `message`: A concise, human-readable message.
    - `context`: A nested JSON object for all relevant business context.
3.  **Distributed Tracing:** Services MUST propagate the standard `traceparent` HTTP header for all internal gRPC calls and the Kafka `trace-id` header for all MMB events. This ensures a full transaction trace can be seen in Jaeger from API Gateway to database.

### 5.4 Resilience and Stability Patterns

The following patterns are mandatory for all services.

| Pattern | Implementation | Configuration Standard |
| :--- | :--- | :--- |
| **Circuit Breaker** | Resilience4j (Java), go-resiliency (Go). Wrap all outbound network calls. | **Failure Rate Threshold:** 50%. **Sliding Window:** 10 calls. **Wait Duration in Half-Open State:** 30 seconds. Must log every state change (`OPEN`, `HALF_OPEN`, `CLOSED`). |
| **Retry** | As above. Used in conjunction with Circuit Breaker. | **Max Retries:** 3. **Backoff Policy:** Exponential (100ms initial, 2x multiplier, 5s max). **Retryable Exceptions:** `TimeoutException`, `503 Service Unavailable`. |
| **Bulkhead** | Separate thread pools for key dependencies. | Must be explicitly configured for any dependency that is critical to core operation. Default pool size: 5 threads. |
| **Rate Limiting** | For API Gateway-exposed endpoints, enforced by Kong. For internal, enforced by the service itself. | Must be aligned with SLOs. Hard limit must be defined in the `kong.yaml` configuration. |
| **Graceful Shutdown** | `preStop` hook in the Kubernetes pod spec. | Must wait for in-flight requests to drain. A `SIGTERM` delay of 25 seconds is configured in the base Helm chart. |

---

## 6. Controls and Safeguards

This section details specific controls, both technical and administrative, mapped to relevant SOC 2 Trust Services Criteria (TSC) as per the 2017 framework. These controls are audited semi-annually by the Internal Audit team and annually by external assessors.

### 6.1 Logical Access Controls (Addressing SOC 2 CC6.1 and CC6.3)

- **CC6.1-C1 (Service Mesh mTLS):** All pod-to-pod communication within the Meridian EKS fleet is encrypted and authenticated via mutual TLS (mTLS) using Linkerd. This control ensures that only verified and authorized containers can communicate, irrespective of network locality. The Linkerd control plane’s certificate rotation is automated and monitored by the Platform Engineering team.
- **CC6.1-C2 (API Gateway Authorization):** Kong Enterprise is the single entry point. Every external-facing API route MUST have an associated authentication plugin (e.g., OAuth2 Introspection, JWT validation) and an ACL plugin enforcing consumer groups. This centralizes authorization enforcement.
- **CC6.3-C1 (Zero-Trust Inter-Service Auth):** Every internal API endpoint (gRPC) MUST require a bearer token. The Meridian Identity Service (`svc-identity`) issues short-lived (15-minute) JWTs to each service’s Kubernetes Service Account upon startup. The service mesh’s Sidecar Proxy transparently injects and validates this token, providing a zero-trust security posture.

### 6.2 Service Integrity and Availability Controls (Addressing SOC 2 A1.2 and PI1.3)

- **A1.2-C1 (Automated Recovery):** The Meridian Kubernetes control plane (Rancher/EKS) manages all service deployments. A `Deployment` object’s `replicas` setting defines the minimum viable state. The Kubernetes scheduler ensures pods are distributed across multiple Availability Zones (AZs). If a node fails, the scheduler automatically reschedules the affected pods to healthy nodes in another AZ within 5 minutes, meeting the availability SLO. This control is continuously validated by the `kube-state-metrics` dashboard.
- **A1.2-C2 (Resource Limits & Saturation Control):** Every container definition in a Kubernetes Deployment manifest MUST include `resources.requests` and `resources.limits` for both CPU and memory. Failure to define these will result in the CI/CD pipeline rejecting the deployment (via an OPA/Kyverno admission controller). These limits prevent a noisy neighbor from causing a cascading failure, directly supporting availability.
- **PI1.3-C1 (Idempotency Enforcement):** All asynchronous event consumers MUST be idempotent, deduplicating messages using the `eventId` field within a 72-hour window. This ensures that retry logic, implemented for availability, does not compromise data integrity through duplicate processing.
- **PI1.3-C2 (Data Sovereignty Enforcement):** The `AddDatabaseAccessRequest` form in the Meridian Internal Developer Portal (IDP) is programmatically limited. It only allows a service's designated Service Account to request a connection to its own datastore. A cross-service database connection request is flagged as a "Policy Violation" and requires a forced review by a Principal Engineer, creating a hard audit trail.

### 6.3 Change Management Controls (Addressing SOC 2 CC8.1)

- **CC8.1-C1 (Immutable Infrastructure):** No changes are made to running infrastructure. All changes must be applied via a CI/CD pipeline that builds a new, immutable container image, runs a comprehensive test suite, and deploys via a rolling update strategy. SSH access to production nodes is prohibited by security group firewall rules, enforced by AWS IAM policy.
- **CC8.1-C2 (CI/CD Architectural Gates):** The Merge Request pipeline (GitLab CI) for any microservice repository **must** pass the `arch-compliance-check` stage. This stage executes the `meridian-arch-validator` CLI tool, which performs automated checks against the service's manifest and code, including:
    - Validates the presence of a `HEALTHCHECK` instruction in the Dockerfile.
    - Confirms mandatory Prometheus metrics endpoints are registered.
    - Checks for hardcoded IP addresses or URLs (prohibited).
    - Verifies no `EXPOSE` directives conflict with the standardized port mappings.
    - Rejects deployment if the `ADD.md` file hash does not match the approved version in the `architecture-decision-log` repository.
    A failure at this gate blocks the Merge Request from being merged.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs) and Service Level Indicators (SLIs)

The following metrics are aggregated at the system level and reported monthly to the Architecture Governance Board.

| SLI | Target SLO | KPI (Monthly) | Measurement Tool | Responsible Party |
| :--- | :--- | :--- | :--- | :--- |
| **Average API Success Rate** | 99.95% (all responses non-5xx) | Success Rate > 99.9% | Prometheus/Thanos, Grafana dashboard `DASH-SVC-001` | Tribe Lead Engineer |
| **Average Response Latency (p95)** | < 500ms per API Gateway route | p95 Latency across top 20 endpoints < 450ms | Kong Vitals, Grafana dashboard `DASH-API-001` | Platform Engineering |
| **Service Uptime** | 99.99% (as measured by synthetic probes) | Uptime > 99.98% | Blackbox Exporter, PagerDuty | Tribe Lead Engineer |
| **Mean Time To Recovery (MTTR)** | < 60 minutes for Sev1 incidents | MTTR < 45 minutes | PagerDuty, postmortem records | VP, Engineering |
| **Architectural Compliance Score** | 100% automated gate pass, <5 open exceptions | 100% gate pass, <3 open exceptions | `meridian-arch-validator`, ServiceNow | VP, Engineering |
| **Data Sovereignty Violations** | 0 | 0 | AWS IAM/GuardDuty, IDP Audit Logs | VP, InfoSec |
| **SOC 2 Control Deviation Count** | 0 per audit cycle | 0 deviations | Internal Audit Reports | VP, InfoSec |

### 7.2 Reporting Cadence

- **Weekly Engineering Sync:** Each Tribe Lead Engineer reviews a Grafana dashboard filtered for their Tribe's SLO compliance and open exceptions. This is a tactical, operational review.
- **Monthly Architecture Review Board (ARB):** A formal meeting chaired by the VP of Engineering. All metrics from Section 7.1 are reviewed. The Principal Engineer for each domain presents any new exception requests and validates the ongoing need for existing exceptions.
- **Quarterly Service Health & SOC 2 Control Review:** A joint review between the VP of Engineering and VP of Information Security. This review assesses the effectiveness of all controls listed in Section 6, using the SLI data as evidence. Any control deviation is formally documented and an action plan with a strict timeline is agreed upon.

---

## 8. Exception Handling and Escalation

Technical realities or critical business deadlines may necessitate a temporary deviation from a specific standard.

### 8.1 Exception Request Procedure

1.  A squad's Technical Lead must document the deviation exhaustively using the **`SOP Exception Request`** form in the Meridian ServiceNow portal (`servicenow.internal.aws.meridian.com`). The form requires:
    - **Policy Reference:** The specific section of this SOP being deviated from.
    - **Rationale:** A clear, data-backed argument for why the standard is impracticable and the proposed alternative is acceptable.
    - **Technical Risk Assessment:** An honest detailing of the elevated risk, including a quantified blast-radius analysis.
    - **Mitigating Controls:** Concrete, implemented countermeasures to reduce the risk to a tolerable level.
    - **Sunset Plan:** A dated commitment (max 90 days) for when the deviation will be remediated, along with a link to the specific Jira epic.

2.  The `SOP Exception Request` is routed automatically for approval:
    - **Level 1 (Minor, time-boxed 30 days):** Approval from the Tribe Lead Engineer.
    - **Level 2 (Significant, 31-90 days):** Approval from the Tribe Lead Engineer AND a Principal Engineer.
    - **Level 3 (Fundamental, impacting SOC 2 control):** Must be escalated to and approved by the VP of Engineering and the VP of Information Security (David Park and Aria Vance).

### 8.2 Escalation Path

If an exception request is denied or if there is a dispute regarding architectural direction, the following escalation path must be followed:

1.  Squad Technical Lead → Tribe Lead Engineer.
2.  Tribe Lead Engineer → Assigned Principal Engineer.
3.  Principal Engineer → VP, Engineering (David Park).

The VP of Engineering's decision is final and will be documented as an Architectural Decision Record (ADR) in the `architecture-decision-log` repository for future reference.

---

## 9. Training Requirements

To ensure effective implementation of these standards, the following training is mandatory for all engineers.

| Training Module | Content Summary | Required Frequency | Delivery Method | Assigned Roles |
| :--- | :--- | :--- | :--- | :--- |
| **MSP-101: Meridian Standards Overview** | Covers all foundational SOPs, including this one, SOP-SEC-015, and SOP-REL-005. Emphasizes the "why" behind DDD, Zero-Trust, and Observability. | Once, within 30 days of hire. | Meridian LMS (Workday Learning) | All Product & Engineering FTEs and Contractors |
| **MSP-201: Advanced Microservice Patterns** | Deep-dive, hands-on workshop on implementing Circuit Breaker, Bulkhead, Idempotent Consumers, and gRPC best practices. | **Annually.** | Instructor-led (Platform Engineering) | All Senior Engineers and Technical Leads |
| **MSP-202: Writing an Effective ADD** | Workshop on the ADD template, EventStorming, and the Architectural Review process. | Once, before first ADD submission. | Self-paced Confluence documentation & video. | Technical Leads and Principal Engineers |
| **SEC-101: Secure Coding & Zero-Trust** | Covers OWASP Top 10, implementing JWT validation, and secure configuration of the service mesh. | **Annually.** | Securing Web (3rd-party platform) | All Engineers |

Training compliance is tracked via Workday Learning. **Architectural Review (Section 5.1.1) approval is gated on 100% training compliance for the requesting Technical Lead.** A quarterly report of compliance is delivered to VP, Engineering and VP, InfoSec.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs
- **SOP-SEC-015:** System Security & Operational Hygiene Standards
- **SOP-SEC-007:** Secrets Management and Key Rotation Policy
- **SOP-REL-005:** Incident Response and Postmortem Procedures
- **SOP-OBS-001:** Observability and Telemetry Platform Standards
- **SOP-PLAT-002:** Container Orchestration and Deployment Standards
- **SOP-DR-001:** Disaster Recovery and Business Continuity Plan
- **SOP-DATA-003:** Data Governance and Sovereignty Policy
- **SOP-CHG-001:** Change Management and Release Policy

### 10.2 External Standards and Frameworks
- **SOC 2:** AICPA, TSP Section 100, *2017 Trust Services Criteria for Security, Availability, and Processing Integrity* (specifically criteria series CC6.x, A1.x, and PI1.x).
- **HIPAA Security Rule:** 45 C.F.R. §§ 164.308, 164.312, 164.314 (applicable to services processing ePHI).
- **ISO/IEC 27001:2022:** Annex A Controls A.8.9 (Configuration management), A.8.14 (Logging and monitoring), A.8.32 (Change management).
- **IEEE 14764-2022:** Standard for Software Maintenance.

### 10.3 Meridian-Internal Documents
- `Architecture Decision Log` repository: `git.internal.meridian.com/architecture/decisions`
- `Service Catalog`: Meridian Internal Developer Portal (IDP)
- `Postmortem Template`: Confluence `TMP-RCA-001`

---

## 11. Revision History

| Version | Date | Author | Approver | Summary of Changes |
| :--- | :--- | :--- | :--- | :--- |
| 4.8 | 2025-11-24 | S. Kapoor (Principal Eng.) | D. Park | **Major Update.** Replaced deprecated Istio reference with Linkerd. Updated all CI/CD references from Jenkins to GitLab CI/ArgoCD. Added new Kyverno admission controller details. Updated Section 9 training modules (MSP-201). Revised exception handling for SOC 2 clarity. |
| 4.5 | 2025-04-15 | A. Chen (Tribe Lead, HealthPay) | D. Park | Added mandatory DLQ configuration for all Kafka consumers (Section 5.2.2). Introduced bulkhead pattern as mandatory (Section 5.4). Refined data sovereignty enforcement controls (CC6.1-C2) after Q1 SOC 2 audit finding. Clarified schema registration procedure. |
| 4.2 | 2024-10-03 | J. Doe (VP, Eng. at time) | A. Vance (VP, InfoSec) | Reorganization of Section 6 to map controls directly to SOC 2 TSC. Introduced strict JSON logging schema. Added `SOP Exception Request` workflow in ServiceNow. |
| 3.9 | 2024-02-18 | M. Rodriguez (Platform Lead) | J. Doe | Migration of inter-service sync communication standard from async REST to gRPC. Updated scaffolding CLI commands. Added ADD compliance gate to CI/CD pipeline. |
| 3.4 | 2023-07-12 | M. Rodriguez (Platform Lead) | J. Doe | Initial implementation of DDD Bounded Context policy. Formalized the Architecture Review Board (ARB). Introduced the Architecture Design Document (ADD) template. |
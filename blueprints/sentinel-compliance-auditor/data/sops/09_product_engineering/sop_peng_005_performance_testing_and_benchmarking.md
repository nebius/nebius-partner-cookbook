---
sop_id: "SOP-PENG-005"
title: "Performance Testing and Benchmarking"
business_unit: "Product & Engineering"
version: "2.8"
effective_date: "2024-07-08"
last_reviewed: "2025-06-22"
next_review: "2025-12-11"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for performance testing and benchmarking across all Meridian Health Technologies, Inc. product lines and supporting infrastructure. The purpose is to ensure that all software systems, AI models, data pipelines, and user-facing services meet defined performance requirements under both normal and adverse conditions, thereby protecting patient safety, financial transaction integrity, and regulatory compliance posture.

Performance validation is not merely a technical exercise; it is a patient safety imperative. Degraded clinical AI inference times can delay critical care decisions. Unresponsive payment gateways can prevent patients from accessing necessary medical financing. Slow analytics queries can impede population health interventions. This SOP codifies the methodologies, tools, responsibilities, and governance required to proactively identify, measure, and remediate performance risks.

### 1.2 Scope

This SOP applies to all employees, contractors, managed service providers, and third-party vendors who design, develop, deploy, operate, or maintain software and infrastructure for the following business lines and supporting platforms:

| Scope Area | Applicable Systems | Key Performance Concerns |
|---|---|---|
| Clinical AI Platform | Inference APIs, model serving infrastructure, diagnostic imaging pipelines, patient risk scoring engines, adverse event prediction systems | Inference latency (p95/p99), throughput (requests/second), model load time, GPU utilization |
| HealthPay Financial Services | Payment processing APIs, patient financing engines, medical lending decision services, claims automation pipelines, fraud detection models | Transaction processing time (end-to-end), authorization timeout compliance, batch processing throughput, payment gateway availability |
| MedInsight Analytics | Population health query engine, care gap identification services, outcomes prediction models, ETL/ELT data pipelines | Query response time (interactive and batch), data freshness, dashboard load time, PHI de-identification pipeline throughput |
| Meridian SaaS Platform | Multi-tenant orchestration layer, authentication/authorization services (Okta integration), API gateway, message queuing (Kafka), caching layer (Redis), database clusters (PostgreSQL, Snowflake) | API latency under multi-tenant load, connection pooling efficiency, cross-region replication lag, failover time |
| Infrastructure & Observability | AWS (us-east-1 primary, eu-west-1 secondary), Azure DR, Kubernetes clusters, CI/CD pipelines, Datadog observability, PagerDuty alerting | Cluster autoscaling responsiveness, log ingestion throughput, metric collection interval compliance |

This SOP applies to all environments (Development, Testing, Staging, and Production) with environment-specific testing rigor defined in Section 5.

### 1.3 Out of Scope

- Security penetration testing (governed by SOP-ISEC-012: Security Testing and Vulnerability Management).
- Functional correctness testing and clinical validation studies (governed by SOP-CLIN-003: Clinical AI Validation and FDA Submission Requirements and SOP-QA-008: Software Quality Assurance and Testing Standards).
- Accessibility and usability testing (governed by SOP-UX-010: User Experience and Accessibility Standards).

### 1.4 Regulatory and Contractual Applicability

The performance assurance programs defined in this SOP directly support Meridian's compliance with:

- **SOC 2 Type II**: Availability and Processing Integrity Trust Services Criteria. Performance testing and monitoring provide evidence of control effectiveness. This SOP addresses the design of performance monitoring controls. Specific availability commitments exist for each service tier; performance testing validates that Meridian can meet those commitments under projected load conditions.
- **EU AI Act (High-Risk AI Systems)**: Article 15 (Accuracy, Robustness, and Cybersecurity) and Article 9 (Risk Management System). Performance testing provides evidence of technical robustness and appropriate levels of accuracy for clinical AI systems.
- **HIPAA**: Contingency planning requirements (45 CFR § 164.308(a)(7)) related to system availability and emergency mode operations.
- **GDPR**: Article 32 (Security of Processing), including the ability to ensure the ongoing confidentiality, integrity, availability, and resilience of processing systems.
- **FDA 510(k) / EU MDR**: Performance characteristics of medical device software, including response times for diagnostic aids.
- **SR 11-7**: Model risk management guidance for financial models, including validation of model performance under stress scenarios.

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|---|---|
| **Baseline Performance** | The documented set of performance metrics for a system operating under a defined, standard load. Serves as the reference point for all subsequent performance comparisons. |
| **Benchmarking** | The process of comparing system performance metrics against established baselines, industry standards, competitor products, or prior versions to identify regressions or improvements. |
| **Concurrent Users** | The number of virtual or real users simultaneously interacting with a system, including both active transaction execution and session maintenance. |
| **Critical Path** | The sequence of operations or services whose cumulative latency directly affects the end-user experience or system SLA. |
| **Failover** | The automatic or manual process of switching operations from a failed primary system component to a redundant or standby component. |
| **Load Testing** | Evaluating system behavior under expected normal and projected peak concurrent user loads, measuring throughput, latency, and resource utilization. |
| **p50, p95, p99 Latency** | Percentile-based latency measurements: p50 (median latency — half of requests are faster), p95 (95% of requests are faster, targeting atypical but expected spikes), p99 (99% of requests are faster, isolating outlier behavior). |
| **Performance Budget** | A quantitative, non-negotiable threshold for a specific performance metric (e.g., "Clinical inference API p99 latency must not exceed 500ms"). Violations trigger a blocking action in CI/CD pipelines or a P1 incident in production. |
| **Performance Regression** | A measurable degradation in any performance budget metric compared to the established baseline for a given release candidate. |
| **Performance Sign-off** | Formal approval from the VP of Engineering (or delegate) that a release candidate meets all performance budgets and is cleared for production deployment. |
| **Pingdom** | Synthetic monitoring tool used for external endpoint availability and response time checks from geographically distributed probes. |
| **Soak Testing** | Prolonged load testing over an extended duration (minimum 24 hours, typically 72 hours) to identify memory leaks, connection pool exhaustion, log rotation failures, and other gradual resource degradation. |
| **Spike Testing** | A form of stress testing that evaluates system behavior when load increases dramatically (3x–10x baseline) within a very short period (e.g., 30 seconds to 5 minutes), simulating flash-crowd scenarios such as open enrollment or market volatility. |
| **Stress Testing** | Testing beyond the maximum expected operational capacity to determine the system's breaking point, failure mode (graceful degradation vs. catastrophic collapse), and recovery behavior. |
| **Synthetic Transaction** | A scripted, automated interaction with a system that simulates a complete user workflow (e.g., login → search → add to cart → checkout → logout) from geographically distributed points. |
| **Throughput** | The number of transaction requests successfully processed by a system per unit of time, typically expressed as requests per second (RPS) or transactions per minute (TPM). |

## 3. Roles and Responsibilities

The following RACI matrix defines accountability for all performance testing and benchmarking activities. "Responsible" performs the work; "Accountable" is ultimately answerable and approves; "Consulted" provides input; "Informed" is kept up-to-date.

| Activity | Product Engineering Teams | VP of Engineering (David Park) | QA Performance Lead | CISO (Rachel Kim) | VP of IT Ops (Samantha Torres) | Chief AI Officer (Dr. Marcus Rivera) | Compliance Officer (Thomas Anderson) |
|---|---|---|---|---|---|---|---|
| Define and maintain performance budgets | R | A | C | C | C | C | I |
| Write and maintain test scripts (JMeter, K6, Locust, custom) | C | I | R | I | C | I | I |
| Execute load/stress/soak tests | C | I | R | I | C | C | I |
| Provision and maintain test environments | I | A | C | I | R | I | I |
| Analyze results and identify regressions | C | I | R | C | C | C | I |
| Approve performance sign-off for release | R (recommend) | A | R (recommend) | C (for security-critical path) | I | C (for AI services) | I |
| Monitor production performance KPIs | C | I | I | I | R | I | I |
| Report on compliance with this SOP | C | A | C | C | C | C | R |
| Annual policy review | C | A | C | C | C | C | R |

### 3.1 Detailed Role Descriptions

**VP of Engineering (David Park)** — Ultimate accountability for the performance of all product and platform systems. Approves all performance budgets, signs off on major release performance reports, and chairs the quarterly Performance Governance Review. Authorizes exceptions to this SOP.

**QA Performance Lead** — A dedicated role within the Quality Assurance organization responsible for the day-to-day execution of the performance testing program. Maintains the master test suite, coaches product teams on performance testing best practices, and produces the standardized performance report for each release. This role has administrative ownership of the performance testing infrastructure (JMeter controllers, K6 cloud instances, Locust clusters).

**Product Engineering Teams** — Each product team (Clinical AI, HealthPay, MedInsight, SaaS Platform) is responsible for defining initial performance budgets for their services, fixing performance regressions identified during testing, and providing domain expertise for test script design.

**VP of IT Operations (Samantha Torres)** — Responsible for ensuring production and staging environments are instrumented for performance monitoring. Ensures test environment topology mirrors production. Maintains infrastructure-level performance dashboards. Responsible for capacity planning based on performance test projections.

**Chief AI Officer (Dr. Marcus Rivera)** — Consulted on performance budgets and test scenarios for all AI/ML services. Ensures performance testing adequately validates model serving infrastructure (GPU utilization, batch vs. real-time inference tradeoffs). Reviews clinical AI performance reports for patient safety implications.

**Chief Information Security Officer (Rachel Kim)** — Consulted on security controls within performance testing (ensuring test data is sanitized, test accounts have appropriate permissions). Reviews performance reports with a lens on DDoS resilience and security control performance under load.

**Compliance Officer (Thomas Anderson)** — Monitors adherence to this SOP. Ensures performance testing evidence is archived and available for SOC 2, HITRUST, and ISO 27001 audits. Reviews regulatory applicability of any performance exemptions.

**Chief Privacy Officer / DPO (Dr. Klaus Weber)** — Consulted to ensure performance testing data complies with GDPR and HIPAA (no production PHI used in test environments without approved anonymization per SOP-PRIV-002).

## 4. Policy Statements

### 4.1 Performance-First Development Mandate

Performance is a first-class quality attribute at Meridian Health Technologies, equivalent to functional correctness and security. No feature is considered complete until its performance impact has been quantified and validated against established budgets.

### 4.2 Mandatory Performance Validation Gates

All production releases must pass through the following performance validation gates. The gates are cumulative; a release that fails any gate is automatically blocked from production deployment.

| Gate | Trigger | Required Outcome | Authority |
|---|---|---|---|
| **Gate 1: CI/CD Pipeline Benchmark** | Every commit to a release branch | Automated component-level benchmarks must not regress >5% from baseline | Automated (CI/CD pipeline) |
| **Gate 2: Integration Performance Test** | Staging deployment candidate | Full-system load test at 100% projected peak load for 1 hour; all performance budgets met | QA Performance Lead |
| **Gate 3: Stress Test** | Prior to major release (quarterly) and prior to peak season (open enrollment) | System breaks at >2x peak load; graceful degradation observed; recovery within defined timelines | VP of Engineering |
| **Gate 4: Soak Test** | Prior to major release (quarterly) | 72-hour continuous load test at 80% peak; no memory leaks, connection exhaustion, or unbounded resource growth | VP of Engineering |

### 4.3 Performance Budget Framework

Every service exposed to external consumers (API endpoints, user interfaces, batch processing interfaces) must have a documented performance budget that includes, at minimum:

- **Latency Budget**: Max p95 and p99 latency in milliseconds.
- **Throughput Budget**: Minimum sustained throughput in requests per second or transactions per minute.
- **Availability Budget**: Percentage uptime commitment.
- **Error Rate Budget**: Maximum acceptable error rate (5xx responses, timeout rate).

Performance budgets are owned by the product teams but must be approved by the VP of Engineering. Budgets are stored in a version-controlled `PERFORMANCE_BUDGETS.yaml` file within each service's repository. A change to a performance budget requires a formal review and is treated as a significant architectural decision.

> **Template: PERFORMANCE_BUDGETS.yaml**
> ```yaml
> service: clinical-inference-api
> version: 3.2.1
> owner: clinical-ai-team
> approved_by: david.park@meridian.health
> approved_date: 2024-06-15
> budgets:
>   latency_ms:
>     p95: 300
>     p99: 500
>   throughput_rps:
>     min_sustained: 250
>   availability_pct: 99.9
>   error_rate_max_pct: 0.5
>   peak_multiplier: 2.5 # system must handle 2.5x baseline without breaking
> ```

### 4.4 Annual Benchmarking

At minimum annually, Meridian must conduct formal competitive benchmarking for all customer-facing products. This benchmarking exercise compares Meridian's performance against both published competitor SLA figures and independent third-party evaluation where feasible. Results are presented to the Board-level AI Governance Committee.

### 4.5 Prohibition on Production Load Testing

Direct load testing on production environments is prohibited except for controlled synthetic checks (Pingdom probes) and pre-approved, tightly scoped production verifications during maintenance windows. Any exception requires joint approval from the VP of Engineering, VP of IT Operations, and CISO.

## 5. Detailed Procedures

### 5.1 Performance Baseline Establishment

Performance baselines must be established at the following milestones and stored in MLflow's metrics registry with the corresponding service version tag.

#### 5.1.1 Baseline Triggers

- Initial production release of a new service (baseline is set from the staging environment test result, scaled proportionally to production topology).
- Any architectural change (database migration, messaging system change, network topology change).
- Any major release that intentionally modifies a performance budget.
- Annually, even if no changes occurred (re-baselining to account for data volume growth).

#### 5.1.2 Baseline Procedure

1. **Environment Preparation**: The QA Performance Lead submits a ticket to the IT Operations team (via ServiceNow) requesting a dedicated staging environment slice that is isolated from other test activities. This environment must match production topology at a 1:4 scale (staging:production) for compute resources. Request at least 72 hours of exclusive access.
2. **Data Preparation**: The product team provisions a sanitized, representative test dataset. For clinical AI services, this means de-identified medical images and structured EHR data. For HealthPay, this means synthetic transaction data generated by the `txn-synth-gen` tool (maintained by the HealthPay team) that matches production transaction distributions. For MedInsight, this means a de-identified population cohort of appropriate size. **Use of production PHI is strictly prohibited** (see SOP-PRIV-002).
3. **Steady State Validation**: Soak the system at 50% of projected peak load for 2 hours to confirm stability and warm caches. Discard results from this warmup period.
4. **Gradient Load Profile**: Execute a stepped load profile: start at 0 RPS, increase by 10% of peak every 2 minutes until reaching 100% of projected peak load. Maintain peak for 1 hour. Monitor all system components for resource saturation.
5. **Metric Collection**: Collect the following metrics using Datadog agents and custom application instrumentation. Record these as the baseline in MLflow with tags `[service_name, version, environment, baseline_type=performance]`:
    - Service-level: p50/p95/p99 latency, RPS, error rate.
    - Dependency-level: Database query times, cache hit ratios, external API call latencies.
    - Infrastructure-level: CPU utilization, memory utilization, network throughput, disk I/O, GPU utilization (for AI services).
    - Application-level (Kafka): Consumer lag, producer latency.
    - AI-specific (LangSmith traces): Token generation rate, time-to-first-token, embedding query time (Pinecone).
6. **Baseline Report**: The QA Performance Lead publishes a baseline report (template: `PERF-BASE-RPT`) to the Confluence Performance Testing space within 48 hours of test completion.
7. **Sign-off**: VP of Engineering signs off on the baseline via Confluence comment, formally recording the baseline as the standard for future regression comparison.

### 5.2 Load Testing for Release Validation

Every release candidate (RC) for a major, minor, or patch release must undergo load testing on the staging environment before production deployment.

#### 5.2.1 Test Script Management

All load test scripts are stored in the `meridian/perf-tests` GitHub repository, organized by service:

```
perf-tests/
├── clinical-ai/
│   ├── inference-api/
│   │   ├── baseline-load.js (K6 script)
│   │   └── stress-breakpoint.js
│   └── imaging-pipeline/
├── healthpay/
│   ├── payment-auth/
│   ├── claims-batch/
│   └── lending-decision/
├── medinsight/
│   └── population-query/
└── saas-platform/
    ├── api-gateway/
    └── tenant-isolation/
```

Scripts must be:
- Versioned and peer-reviewed (PR required to the `main` branch).
- Parameterized (target RPS, test duration, ramp-up time are externalized as environment variables).
- Idempotent (can be re-run without manual state reset).

#### 5.2.2 Load Test Execution Procedure

1. **Pre-Condition Checklist**: The QA Performance Lead verifies:
    - Staging environment is deployed with the exact RC build artifact.
    - All Datadog agents report healthy.
    - Test data sets are refreshed and sanitized.
    - CI/CD pipeline Gate 1 (component benchmarks) has passed and is green.
2. **Test Execution**: Execute the load test suite using the Meridian Test Orchestrator (`mto` CLI) with standardized parameters:
    ```bash
    mto run --suite standard-release --env staging \
      --target-rps 100% --duration 60m --rampup 10m \
      --report-path ./reports/$(date +%Y%m%d-%H%M) \
      --services clinical-ai,inference-api healthpay,payment-auth medinsight,query saas-platform,gateway
    ```
3. **Real-time Monitoring**: The QA Performance Lead and the product engineering team's designated on-call person monitor Datadog dashboards in real-time. Any P1/P2 alert triggered during the test requires immediate investigation.
4. **Result Analysis**: Upon test completion, the `mto` tool produces a standardized HTML report comparing results to the established baseline. The report highlights:
    - Any metric exceeding its performance budget threshold (RED/FAIL).
    - Any metric regressing >10% from baseline (YELLOW/WARN).
    - All metrics within budget and <10% regression (GREEN/PASS).
5. **Release Decision**:
    - **FAIL**: Any performance budget exceeds threshold → Release is blocked. A severity-identified bug is filed. Root cause analysis (RCA) is required before re-testing.
    - **WARN**: Regressions >10% exist but budgets are not exceeded → Product team must provide written justification and a remediation plan. VP of Engineering may approve release with a remediation timeline.
    - **PASS**: All metrics within thresholds → QA Performance Lead appends the report to the release ticket and marks the performance gate as passed.

### 5.3 Stress Testing and Breaking Point Determination

Quarterly, and additionally before predictable peak-load periods (e.g., Medicare open enrollment October 15 – December 7, year-end financial processing), stress testing must be performed.

#### 5.3.1 Peak Season Calendar

| Period | Business Impact | Applicable Systems |
|---|---|---|
| Jan 1-15 | Health plan enrollment activation | MedInsight, SaaS Platform |
| Oct 15 – Dec 7 | Medicare open enrollment | Clinical AI (risk scoring), MedInsight |
| Dec 15 – Jan 5 | Year-end claims processing | HealthPay, MedInsight |
| March-April | Spring product release cycle | All systems |

#### 5.3.2 Stress Test Procedure

1. **Define Test Parameters**: For each service, define the peak load multiplier based on historical data and business projections. Typical values: 3x baseline for Clinical AI, 5x baseline for HealthPay (claims surge), 2x baseline for MedInsight.
2. **Execute Gradient Increase**: Starting from 100% peak load, increase load in 20% increments every 15 minutes until system failure (error rate >5%, p99 latency >5x budget, or unresponsiveness).
3. **Observe Failure Mode**:
    - **Graceful Degradation**: Requests are throttled (HTTP 429), queues grow, processing slows but no data loss or corruption. **This is the required behavior.**
    - **Catastrophic Failure**: System crashes, data loss, inconsistent state. **This is unacceptable.** If observed, a SEV-0 incident is declared, and the system is not cleared for production until a redesign is validated.
4. **Document Break Point**: Record the exact throughput at which failure occurred and the nature of the failure. This "breaking point" is the system's operational ceiling and must be at least 2.0x the peak load budget.
5. **Recovery Observation**: After inducing failure, cease load generation and observe the system's recovery. Record the time from load cessation to restored health (all health checks passing, latency normalized). This recovery time informs operations runbooks.

### 5.4 Soak Testing (Endurance Testing)

Quarterly, a 72-hour soak test is executed against the staging environment. The soak test is scheduled to start Monday 09:00 ET and conclude Thursday 09:00 ET.

1. **Setup**: Identical to load test pre-conditions. Load is maintained at 80% of projected peak load for the entire 72-hour period.
2. **Continuous Monitoring**: The QA Performance Lead and IT Operations assign rotating on-call shifts for the duration of the test. Datadog anomaly detection is enabled with a heightened sensitivity.
3. **Key Observations**:
    - **Memory**: Heap memory, native memory, GPU memory trends (monitor for linear increase indicating a leak).
    - **Connections**: Database connection pool utilization, HTTP connection pool utilization.
    - **Disk**: Log volume growth, temporary file accumulation.
    - **Kafka**: Consumer lag trend over time.
    - **Cache**: Hit ratio trend over time.
4. **Post-Test Analysis**: At test conclusion, analyze trends for all key observations. Any unbounded resource growth is a FAIL and blocks release.

### 5.5 AI-Specific Performance Testing

Clinical AI systems have unique performance characteristics that require specialized testing procedures.

#### 5.5.1 Model Inference Benchmarks

For each model version deployed (tracked in MLflow Model Registry):

1. **Cold Start Latency**: Time from model load request to first inference completion. Measured after pod restart, scaling event, or new deployment. **Budget**: Max 30 seconds for models <10GB, 120 seconds for large vision models.
2. **Warm Inference Latency**: p95 and p99 inference time for a single request (excluding network overhead). **Budget**: Defined per model in the MLflow registry metadata.
3. **Batch Inference Throughput**: For offline/batch inference pipelines, throughput in images/records per second. **Budget**: Must meet business SLA for batch completion window (e.g., nightly imaging batch must complete within 6 hours).
4. **GPU Memory Utilization**: Peak GPU memory usage per model replica. **Budget**: Must not exceed 85% of available GPU memory to allow for spikes.
5. **Drift Impact Testing**: Annually, test model performance with synthetically drifted data (data distribution shifts representing realistic clinical practice changes over 1, 2, and 3 years) to understand performance degradation curve and inform retraining triggers. This is overseen by Dr. Marcus Rivera's AI Governance team.

### 5.6 Production Synthetic Monitoring

While load testing production is prohibited, continuous lightweight validation is required.

1. **Pingdom Checks**: Configured by IT Operations for all public-facing endpoints. Checks run from 5+ global locations (Boston, London, Berlin, Singapore, Toronto) at 1-minute intervals. Validates response code and response time < 2000ms.
2. **Critical Path Synthetics**: For the top 5 critical user journeys per product line, configure Datadog Synthetic tests that execute full multi-step workflows every 5 minutes from within the production VPC and from external locations.
    - **Clinical AI**: Patient search → risk score retrieval → image analysis request.
    - **HealthPay**: Payment authorization → payment capture → receipt generation.
    - **MedInsight**: Login → cohort query → dashboard render.

### 5.7 Continuous Integration Performance Gates

Integrated into the Jenkins and GitHub Actions CI/CD pipelines:

1. **Microbenchmark Suite**: For every commit to a release branch, a suite of microbenchmarks runs against the build artifact. This suite tests individual functions/methods that are on the critical path.
2. **Automated Pass/Fail**: If any microbenchmark regresses >5% from the baseline stored in the repository's `perf-baseline.json`, the build fails. The developer is notified and must either optimize the code or, after review, update the baseline with justification.

## 6. Controls and Safeguards

### 6.1 Data Sanitization Control

**Control**: All test data used in performance testing environments must be generated synthetically or sanitized to remove all Protected Health Information (PHI) and Personally Identifiable Information (PII).

**Implementation**:
- HealthPay: Use `txn-synth-gen` tool seeded with production transaction statistical distributions but no real PII/PCI data.
- Clinical AI / MedInsight: Use the `deidentify-cli` tool (certified by Dr. Klaus Weber's office per SOP-PRIV-002) to process real clinical data, or use the Meridian Synthetic Patient Data Generator.
- **Verification**: Before any performance test, the QA Performance Lead runs a PHI scan using the `phi-scanner` tool. Test results must show 0 PHI instances, logged in the test report.

### 6.2 Environment Isolation Control

**Control**: Performance test environments must be logically and/or physically isolated from production and other non-production environments to prevent test traffic from impacting live services or corrupting production data.

**Implementation**:
- AWS: Separate VPCs (`staging-vpc` CIDR 10.2.0.0/16 vs `prod-vpc` 10.1.0.0/16) with no VPC peering.
- Okta: Separate Okta tenant for staging environment user directories.
- Synthetic external endpoints: Test scripts target `*.staging.meridian.health` domains only.

### 6.3 Test Data Lifecycle Control

**Control**: Performance test data sets must be refreshed or rotated to prevent "test data staleness," which can mask performance issues related to data volume or distribution.

**Implementation**: Test data sets are archived to S3 (`s3://meridian-perf-test-data/`) after each test with metadata tags. Data sets older than 6 months are automatically deleted via S3 lifecycle policy. Production data distributions are sampled quarterly to validate test data representativeness.

### 6.4 Capacity Planning Integration

**Control**: Results from stress and soak tests must be fed into the formal capacity planning process owned by IT Operations.

**Implementation**: The QA Performance Lead exports key metrics (peak RPS at failure, resource utilization at 100% load) to the capacity planning Snowflake table `IT_OPS.CAPACITY_PLANNING.PERF_TEST_RESULTS` within 1 week of test completion. IT Operations uses this data to forecast infrastructure procurement.

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| KPI | Target | Measurement Method | Reporting Frequency |
|---|---|---|---|
| Percentage of releases blocked by performance gates | <5% | Count of blocked releases / total releases | Monthly |
| Production performance budget compliance | 100% — every metric within budget for the trailing 30 days | Datadog SLO tracking | Continuous, reviewed monthly |
| P99 latency for Clinical AI inference API | <500ms (budget per Section 4.3) | Datadog APM | Real-time dashboard, weekly report |
| P95 latency for HealthPay payment authorization | <400ms | Datadog APM | Real-time dashboard, weekly report |
| Soak test pass rate | 100% (no memory leaks in quarterly soak tests) | Test report outcomes | Quarterly |
| Synthetic check success rate (all critical paths) | >99.5% | Datadog Synthetics | Weekly |
| Mean time to detect (MTTD) performance regressions | <1 hour | Datadog anomaly detection time to alert | Monthly |

### 7.2 Dashboards

The following Datadog dashboards are maintained as the "source of truth" for performance monitoring:

| Dashboard Name | Scope | Audience | Refresh |
|---|---|---|---|
| `[EXEC] Service Performance Overview` | Aggregated SLO compliance for all business lines | C-suite, VP Engineering | Auto (1 min) |
| `[PROD] Clinical AI - Inference Performance` | Per-model latency, throughput, error rate, GPU utilization | Clinical AI team, Dr. Rivera | Auto (30 sec) |
| `[PROD] HealthPay - Transaction Processing` | End-to-end transaction timing, per-endpoint breakdown | HealthPay team, Robert Liu | Auto (30 sec) |
| `[PROD] MedInsight - Query Performance` | Query latency, cache hit ratio, Snowflake utilization | MedInsight team | Auto (1 min) |
| `[PROD] SaaS Platform - Tenant Health` | Per-tenant latency variance, noisy neighbor detection | SaaS Platform team | Auto (1 min) |
| `[PERF-TEST] Current Release Validation` | Real-time view of ongoing performance tests | QA, Release Management | Auto (15 sec) |

### 7.3 Reporting Cadence

| Report | Audience | Frequency | Content |
|---|---|---|---|
| Release Performance Sign-off Report | Release Manager, VP Engineering | Per release | Gate results, budget compliance, regressions |
| Weekly Performance Watch | Product Engineering Leads | Weekly (Monday) | Trending metrics, upcoming risk factors, incident review |
| Quarterly Performance Review | VP Engineering, CTO, CEO | Quarterly | Soak test results, stress test results, capacity forecast, budget adjustment proposals |
| Annual Benchmark Report | AI Governance Committee, Board | Annually | Competitive benchmarking, year-over-year trends, regulatory compliance |

Alerts for performance budget violations in production are routed through Datadog to PagerDuty. The performance monitoring framework generates alerts when budget thresholds are breached, ensuring that on-call engineers are promptly notified of potential availability or performance incidents.

## 8. Exception Handling and Escalation

### 8.1 Exception Request Process

If a product team believes a performance budget cannot be met for a specific release or believes a performance test requirement is not appropriate, a formal exception must be requested.

1. **Submit Exception Request**: File a ticket in the GRC system (ServiceNow GRC module) using the category "SOP Exception — Performance."
2. **Required Information**:
    - SOP reference: SOP-PENG-005
    - Service and version affected.
    - Specific performance budget or testing procedure requiring exception.
    - Technical justification with supporting evidence (profiling data, architectural constraints).
    - Proposed alternative mitigation or compensating control.
    - Duration of exception (must have a clear expiration date; no permanent exceptions).
    - Patient safety impact assessment (mandatory for Clinical AI services).
3. **Review and Approval**: The exception is reviewed by the VP of Engineering and, if impacting regulated systems (Clinical AI, HealthPay), the Chief Compliance Officer. Approval is documented in the GRC system.
4. **Risk Acceptance**: If approved, the exception constitutes a formal risk acceptance. It is logged in the enterprise risk register and reported to the AI Governance Committee if the associated risk exceeds the enterprise risk appetite threshold.

### 8.2 Escalation Path for Unresolved Performance Blockers

If a performance regression is blocking a release and cannot be resolved within the scheduled release window, the following escalation path is followed:

| Level | Escalation Trigger | Escalation To |
|---|---|---|
| L1 | QA Performance Lead identifies blocking regression | Product Engineering Team Lead and VP of Engineering |
| L2 | Blocking regression not resolved within 24 hours or scheduled release date at risk | Chief AI Officer (if AI service) or Chief Financial Officer (if HealthPay) |
| L3 | Patient safety risk identified or major regulatory/business impact | CEO (Dr. Sarah Chen) |

### 8.3 Emergency Release Override

In the event of an emergency release (P0 security patch, critical patient safety fix), the VP of Engineering may authorize bypassing the full performance test suite. This override must include:
- Explicit written authorization from the VP of Engineering.
- Performance validation executed post-deployment within 24 hours.
- A retrospective filed within 5 business days detailing why pre-deployment testing was not feasible and ensuring no performance regression was introduced.

## 9. Training Requirements

### 9.1 Required Training Modules

| Role | Training Module | Frequency | Delivery Method |
|---|---|---|---|
| All Engineering and QA staff | SOP-PENG-005 Awareness & Performance Testing Principles | Annual | Meridian LMS (Workday Learning) |
| QA Performance Lead and QA Engineers | Advanced Performance Testing with K6, Locust, and MTO Orchestrator | Annual, plus on major tool version upgrades | Hands-on workshop led by QA Performance Lead |
| Product Engineers | Performance Budget Definition and Microbenchmark Authoring | Onboarding, then annual | Self-paced course + code lab |
| IT Operations (Samantha Torres's team) | Performance Test Environment Provisioning and Monitoring | Onboarding, then annual | Runbook-based training |
| Release Managers | Performance Gate Interpretation and Sign-off | Annual | Live session with VP of Engineering |

### 9.2 Training Tracking and Compliance

All training assignments and completions are tracked in Workday Learning. Compliance with training requirements is audited quarterly by the Compliance team.

Mandatory training completion metrics:

- **Completion Rate**: 100% of active staff assigned the training must complete it within 30 days of assignment.
- **Escalation**: Non-completion at 30 days is escalated to the individual's manager. Non-completion at 45 days is escalated to the VP of Engineering and recorded as a compliance finding.

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs and Policies

| Document ID | Title | Relationship |
|---|---|---|
| SOP-ISEC-012 | Security Testing and Vulnerability Management | Governs security testing; performance tests under this SOP must not introduce security vulnerabilities |
| SOP-CLIN-003 | Clinical AI Validation and FDA Submission Requirements | Performance benchmarks form part of clinical AI technical documentation for FDA/EU MDR submissions |
| SOP-QA-008 | Software Quality Assurance and Testing Standards | Parent QA governance document; this SOP inherits its testing principles |
| SOP-PRIV-002 | Data Anonymization and Sanitization for Non-Production Environments | Governs the test data preparation procedure required by Section 5.1.2 |
| SOP-ARCH-001 | Technology Architecture Review and Decision Records | Architecture Decision Records (ADRs) must be created for any performance budget changes |
| SOP-CHG-003 | Change Management and Production Deployment | Performance sign-off report is a mandatory attachment to standard change requests |
| SOP-INC-004 | Incident Management and Response | Performance degradations that exceed budget thresholds are declared as incidents per this SOP |
| SOP-CAP-015 | Capacity Planning and Infrastructure Procurement | Performance test results feed into capacity models |

### 10.2 External Standards and References

| Standard | Reference | Applicability |
|---|---|---|
| AICPA TSC 2017 (SOC 2) | CC2.1, A1.1 (Availability commitments), PI1.4 (Processing integrity testing) | Control evidence |
| EU AI Act 2024 | Article 15, Annex IV | Clinical AI technical documentation |
| ISO 25010:2011 | Software product quality model — Performance efficiency | Benchmarking framework reference |
| NIST SP 800-204B | Performance considerations for microservices | Reference architecture |
| ISPE GAMP 5 | Good Automated Manufacturing Practice | Applies to manufacturing, referenced for validation rigor framework |

## 11. Revision History

| Version | Effective Date | Author | Description of Changes |
|---|---|---|---|
| 1.0 | 2021-11-15 | Prior QA Director | Initial creation. Established basic load testing requirements for HealthPay launch. |
| 1.5 | 2022-05-10 | David Park | Expanded scope to include Clinical AI services. Added AI-specific Section 5.5. Introduced performance budget concept (Section 4.3). |
| 2.0 | 2023-01-20 | David Park | Major revision. Introduced formal CI/CD performance gates (Section 5.7). Established RACI matrix. Added Soak Testing (Section 5.4). Aligned with pre-launch EU AI Act requirements. |
| 2.3 | 2023-09-01 | David Park, Dr. Marcus Rivera | Added Drift Impact Testing requirement (Section 5.5.1, item 5). Updated peak season calendar. Added GPU utilization budget language. |
| 2.5 | 2024-02-14 | David Park | Refined exception handling and escalation paths. Added environmental isolation controls (Section 6.2). Updated to reference new SOP-PRIV-002. Moved from Jenkins-only to Jenkins/GitHub Actions CI/CD language. |
| 2.7 | 2024-06-01 | David Park, QA Performance Lead | Technical update to reflect new `mto` test orchestrator tool. Updated performance budgets template. Refined training requirements. |
| 2.8 | 2024-07-08 | David Park | Approved v2.8. Updated roles for new organizational structure. Clarified SOC 2 applicability language. Updated reporting cadence. Incorporated feedback from Q2 2024 audit cycle regarding monitoring and alerting definitions. Finalized cross-references. |
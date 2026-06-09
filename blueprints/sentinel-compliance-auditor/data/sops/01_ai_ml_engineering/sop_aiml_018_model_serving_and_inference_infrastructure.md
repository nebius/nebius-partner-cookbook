---
sop_id: "SOP-AIML-018"
title: "Model Serving and Inference Infrastructure"
business_unit: "AI/ML Engineering"
version: "2.1"
effective_date: "2025-05-20"
last_reviewed: "2026-10-01"
next_review: "2027-04-26"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
  - "EU AI Act"
status: "Active"
---

# Standard Operating Procedure: Model Serving and Inference Infrastructure

**SOP-AIML-018 | Version 2.1**
**Effective: 2025-05-20 | Classification: Internal**

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure establishes the governance framework, architectural standards, operational protocols, and performance requirements for all production model serving and inference infrastructure deployed across Meridian Health Technologies, Inc. The purpose of this document is to ensure that machine learning models are served in a reliable, secure, observable, and scalable manner that meets the regulatory obligations and business requirements of the organization.

Model serving represents the critical bridge between model development and business value realization. Inferencing failures, latency degradation, or unauthorized model access can directly impact patient care decisions, financial transaction processing, and regulatory compliance posture. This SOP provides the engineering and operational controls necessary to maintain the integrity of the inference pipeline from deployment through decommissioning.

### 1.2 Scope

This SOP applies to all machine learning models, inference endpoints, and serving infrastructure operating at the "Production" tier within the Meridian Model Governance Framework (SOP-AIML-001). The scope encompasses the following assets and activities:

| In Scope | Out of Scope |
|----------|--------------|
| Production inference endpoints serving internal or external consumers | Model training infrastructure and pipelines (see SOP-AIML-015) |
| Shadow and Canary deployment environments | Development and Staging environments (see SOP-AIML-002) |
| Inference latency, throughput, availability, and accuracy monitoring | Model development and feature engineering workflows |
| Model serving container images and their lifecycle | Data pipeline and feature store management (see SOP-DATA-009) |
| A/B routing, traffic splitting, and rollback mechanisms | Business-level model validation and clinical efficacy studies |
| Inference authentication, authorization, and audit logging | Model explainability output generation (see SOP-AIML-022) |
| AWS SageMaker, Kubernetes (EKS), and custom serving infrastructure | Desktop or local inference tooling |
| HealthPay Financial Services scoring models (non-clinical) | Direct EMR integration logic |
| Clinical AI Platform inference endpoints (EU and US regions) | End-user application architecture |

### 1.3 Applicability by Product Line

| Product Line | Models in Scope | Regulatory Sensitivity | Maximum Permitted Latency (p99) |
|--------------|-----------------|------------------------|--------------------------------|
| Clinical AI Platform | Diagnostic imaging, risk scoring, adverse event prediction | High-Risk AI (EU AI Act Annex III), HIPAA | 500ms synchronous / 30s async |
| HealthPay Financial Services | Credit scoring, fraud detection, claims prediction | SR 11-7, SOC 2 | 200ms synchronous |
| MedInsight Analytics | Population health, care gap, outcomes prediction | HIPAA, GDPR | 5,000ms batch |
| Meridian SaaS Platform | Infrastructure-level operational models | SOC 2 Type II | 1,000ms |

### 1.4 Target Audience

This SOP is binding upon all personnel involved in the design, deployment, operation, and decommissioning of production inference infrastructure, including:

- AI/ML Engineering team members
- MLOps and DevOps engineers
- Site Reliability Engineering (SRE) team
- Information Security personnel
- Clinical AI product managers
- Financial Services engineering leads
- Platform engineering team

---

## 2. Definitions and Acronyms

### 2.1 Terminology

| Term | Definition |
|------|------------|
| **Model Serving** | The process of hosting a trained machine learning model as a networked service that accepts inference requests and returns predictions. |
| **Inference Endpoint** | A network-addressable API endpoint that exposes one or more model versions for synchronous or asynchronous prediction requests. |
| **Model Version** | A specific, immutable artifact produced by the model training pipeline, identified by a unique SHA-256 hash and registered in the Meridian Model Registry (MLflow). |
| **Serving Container** | A Docker container image that packages a model artifact with its runtime dependencies, preprocessing logic, and prediction handler, conforming to the Meridian Serving Interface Specification. |
| **Shadow Deployment** | A deployment pattern where a new model version receives a copy of production traffic without returning predictions to consumers, used to validate performance under load. |
| **Canary Deployment** | A deployment pattern where a new model version serves a progressively increasing percentage of production traffic while being monitored for anomalies. |
| **Traffic Router** | The infrastructure component (AWS Application Load Balancer with Istio service mesh) responsible for distributing inference requests across model versions based on configured routing rules. |
| **Inference Pipeline** | The complete sequence of operations executed for a single prediction request, including preprocessing, model inference, post-processing, and response assembly. |
| **Cold Start** | The latency penalty incurred when a model container is initialized for the first time or after a period of inactivity, including model weight loading and compilation. |
| **Model Registry** | The MLflow-based centralized repository for model artifacts, managed through SOP-AIML-001, and serving as the source of truth for all production model versions. |
| **Inference SLA** | The service level agreement defining acceptable inference latency, throughput, availability, and accuracy thresholds for a given endpoint. |
| **Inference Tracing** | The end-to-end correlation of prediction requests across microservice boundaries, implemented via LangSmith for AI-specific telemetry and Datadog APM for infrastructure telemetry. |
| **Traffic Splitting** | The practice of distributing incoming inference requests across multiple model versions according to defined weight ratios. |
| **Ghost Traffic** | Production traffic mirrored to a shadow deployment for validation purposes. |

### 2.2 Acronyms

| Acronym | Definition |
|---------|------------|
| ALB | AWS Application Load Balancer |
| APM | Application Performance Monitoring |
| EKS | Amazon Elastic Kubernetes Service |
| GPU | Graphics Processing Unit |
| IAM | Identity and Access Management |
| IST | Inference Stress Test |
| KMS | AWS Key Management Service |
| ML | Machine Learning |
| MTTR | Mean Time to Recovery |
| POD | Point of Deployment |
| RTO | Recovery Time Objective |
| RPO | Recovery Point Objective |
| SHA | Secure Hash Algorithm |
| SRE | Site Reliability Engineering |
| TLS | Transport Layer Security |
| VPC | Virtual Private Cloud |

---

## 3. Roles and Responsibilities

The following RACI matrix assigns accountability for all activities within the model serving lifecycle. Named roles represent organizational positions as of the effective date of this SOP.

### 3.1 RACI Matrix

| Activity | AI/ML Engineer | MLOps Engineer | SRE | Security Team | VP of Engineering | Product Owner | Compliance Officer |
|----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Serving architecture design | R | A | C | C | I | I | I |
| Container image creation | R | A | I | C | | I | |
| Model registry registration | R | A | I | I | | I | |
| Deployment to production | I | R | A | C | I | I | |
| Traffic routing configuration | I | R | A | C | | I | |
| Rollback execution | C | R | A | I | I | I | |
| Monitoring dashboard configuration | C | R | A | I | | I | I |
| Incident response for inference outage | C | R | A | I | I | I | |
| Exception approval | C | C | C | C | A | I | I |
| Quarterly infrastructure review | R | R | A | I | I | I | I |

**Legend:** R = Responsible (performs work), A = Accountable (approves work), C = Consulted (provides input), I = Informed (receives notification)

### 3.2 Named Role Assignments

| Role | Primary Assignee | Alternate |
|------|------------------|-----------|
| Chief AI Officer (Policy Owner) | Dr. Marcus Rivera | Dr. Elena Vasquez, Director of ML Engineering |
| VP of Engineering (Policy Approver) | David Park | Sarah Chen, Senior Director of Platform |
| Lead MLOps Engineer, US-East | James Okonkwo | Priya Sharma |
| Lead MLOps Engineer, EU-West | Thomas Lindström | Anika Meier |
| SRE Lead | Robert Kim | Jennifer Walsh |
| Security Engineering Lead | Michael Torres | Angela Liu |

---

## 4. Policy Statements

### 4.1 Architectural Standards

**PS-001:** All production model serving infrastructure shall be deployed within the Meridian Production Virtual Private Cloud (VPC) in either the `us-east-1-prod` or `eu-west-1-prod` regions, with no direct public internet exposure. All inference endpoints shall be fronted by at minimum an AWS Application Load Balancer terminating TLS 1.3.

**PS-002:** Every production model shall be served from immutable, versioned container images stored in the Meridian ECR repository `prod-model-serving`. Image tags shall follow the convention `<model-group>-<version-number>-<git-commit-short>`. The `latest` tag shall not be used in production routing configurations.

**PS-003:** Model artifacts shall be loaded at container initialization from the Meridian Model Registry, never baked directly into serving container images. This separation ensures that security patches to the serving runtime can be deployed without re-registering model artifacts, and vice versa.

**PS-004:** No production inference endpoint shall operate without an active health check endpoint (`/healthz`) returning HTTP 200 for at minimum liveness verification. Readiness verification (`/readyz`) shall incorporate model loading status checks.

### 4.2 Latency and Performance Commitments

**PS-005:** All synchronous inference endpoints shall maintain a 99th percentile (p99) latency at or below thresholds defined in Section 1.3. Measurements shall be taken at the ALB layer to capture full round-trip latency from request arrival to response departure, inclusive of network transit within the VPC.

**PS-006:** Asynchronous inference endpoints shall acknowledge receipt of inference requests within 1,000ms and complete batch processing within 30 seconds for Clinical AI workloads and 15 seconds for HealthPay workloads.

**PS-007:** Any model serving deployment that introduces a p99 latency regression of more than 15% compared to the incumbent production version, as measured during canary deployment, shall be automatically halted by the traffic router and flagged for engineering investigation.

### 4.3 Security and Access Control

**PS-008:** All inference endpoints shall enforce mutual TLS (mTLS) authentication between the ALB and serving containers within the EKS cluster. Service-to-service inference calls shall present valid X.509 certificates issued by the Meridian Internal Certificate Authority.

**PS-009:** Inference request authentication shall be enforced at the ALB layer via OAuth 2.0 client credentials flow. All inference consumers shall present valid bearer tokens issued by the Meridian Identity Provider (Okta). Anonymous inference access is prohibited in production.

**PS-010:** Model serving containers shall run as non-root users with minimal Linux capabilities. Container filesystems shall be read-only except for designated temporary directories required for model weight loading.

### 4.4 A/B Routing and Traffic Management

**PS-011:** All production endpoints serving multiple model versions shall implement traffic routing via the Meridian Traffic Router, configured through the GitOps repository `meridian-istio-config` following the deployment workflow defined in Procedure 5.6.

**PS-012:** Traffic splitting ratios for A/B testing shall be documented in the model's corresponding Deployment Record in the Model Registry. No A/B test shall exceed 30 days in duration without explicit review and extension approval from the VP of Engineering.

### 4.5 Deployment Gates

**PS-013:** No model version shall advance from Shadow to Canary, or Canary to Full Production, without satisfying all deployment gates defined in Procedure 5.5, including completion of Inference Stress Testing (IST) and accuracy validation where applicable.

**PS-014:** All production deployments shall maintain a rollback-ready previous version configuration within the Traffic Router such that reversion to the prior known-good state can be completed in under five minutes from the rollback decision point.

### 4.6 Availability and Continuity

**PS-015:** Production inference endpoints shall target a minimum availability of 99.9% measured on a rolling 30-day window, excluding scheduled maintenance windows communicated via the Meridian Service Status Page at least 72 hours in advance. Unscheduled maintenance necessitated by critical security patches shall be communicated with as much advance notice as operationally feasible.

**PS-016:** All production serving infrastructure shall operate with a minimum of three availability zones for AWS regional deployments. The SRE team shall maintain infrastructure-as-code configurations that support complete regional failover capability, with failover procedures documented in the SRE runbooks and tested during the quarterly business continuity exercise.

---

## 5. Detailed Procedures

### 5.1 Model Serving Architecture Design

The Meridian model serving architecture follows a layered design pattern consisting of the following components, described in their standard deployment topology:

#### 5.1.1 Standard Synchronous Inference Architecture

```
[Client / Consumer Application]
         |
    [mTLS 1.3]
         |
[AWS Application Load Balancer (ALB)]
    - Authentication: OAuth 2.0 (Okta)
    - WAF rules for rate limiting
    - TLS termination
         |
    [HTTP/2 over TLS]
         |
[Istio Ingress Gateway (EKS)]
    - Traffic routing enforcement
    - Circuit breaking
    - Retry policies (max 3 attempts with exponential backoff)
         |
    [Service Mesh Sidecar (Envoy)]
         |
[Model Serving Container (EKS Pod)]
    - gRPC or REST handler
    - Preprocessing logic
    - Model inference execution
    - Post-processing
         |
[Model Artifacts (MLflow Registry)]
    - Loaded at cold start into GPU/CPU memory
```

#### 5.1.2 Asynchronous Inference Architecture

For batch and async workloads, the request is accepted via the synchronous API gateway and published to a dedicated Amazon SQS queue. Worker containers pull from the queue and write prediction results to a designated S3 bucket or DynamoDB table, with response correlation handled via a client-supplied `correlation_id`.

#### 5.1.3 Instance Selection Guidelines

| Workload Type | Compute | Accelerator | Memory | Justification |
|---------------|---------|-------------|--------|---------------|
| Diagnostic Imaging (Clinical AI) | g5.4xlarge EKS node | 1x A10G GPU | 64 GB | Medical imaging models require GPU acceleration for sub-500ms inference |
| Risk Scoring (Clinical AI) | c6i.4xlarge EKS node | None | 32 GB | XGBoost/LightGBM models are CPU-bound; memory for feature vector assembly |
| Adverse Event Detection | g5.2xlarge EKS node | 1x A10G GPU | 32 GB | Transformer-based NLP models require GPU for text processing pipelines |
| Credit Scoring (HealthPay) | c6i.2xlarge EKS node | None | 16 GB | Gradient-boosted tree ensembles; low latency CPU inference sufficient |
| Fraud Detection (HealthPay) | m6i.2xlarge EKS node | None | 16 GB | Ensemble of models requiring balanced compute and memory |
| Population Health (MedInsight) | m6i.8xlarge EKS node | None | 128 GB | Large-scale batch inference with substantial in-memory data transformations |
| Operational Models (SaaS Platform) | m6i.large EKS node | None | 8 GB | Lightweight models for platform telemetry and anomaly detection |

### 5.2 Container Image Lifecycle

#### 5.2.1 Image Creation and Validation

**Step 1: Base Image Selection**
All production serving containers shall derive from the Meridian-approved base image `meridian/ai-serving-base:3.4.0` (amd64) or `meridian/ai-serving-base:3.4.0-arm64` for Graviton-based deployments. This base image includes:
- Python 3.10 runtime
- MLflow serving runtime v2.6.0
- Meridian telemetry agent v4.2.0
- Standardized health check endpoint implementations

**Step 2: Container Image Build**
The MLOps Engineer constructs the serving container using the following standardized Dockerfile template, stored in the `meridian/serving-images` GitLab repository under path `/<model-group>/<model-name>/Dockerfile`:

```dockerfile
FROM 905418263322.dkr.ecr.us-east-1.amazonaws.com/meridian/ai-serving-base:3.4.0

ARG MODEL_ARTIFACT_PATH
ENV MERIDIAN_MODEL_PATH=$MODEL_ARTIFACT_PATH
ENV MERIDIAN_SERVING_PORT=8080

COPY ./preprocessing /opt/meridian/preprocessing
COPY ./postprocessing /opt/meridian/postprocessing
COPY ./serving_config.yaml /opt/meridian/config/serving_config.yaml

RUN chown -R meridian-svc:meridian-svc /opt/meridian && \
    chmod 644 /opt/meridian/config/serving_config.yaml

EXPOSE 8080
USER meridian-svc

HEALTHCHECK --interval=15s --timeout=5s --retries=3 \
  CMD ["/opt/meridian/healthcheck.sh"]

ENTRYPOINT ["/opt/meridian/entrypoint.sh"]
```

**Step 3: Security Scanning**
Before any image may be promoted to the `prod-model-serving` ECR repository, it must pass:
- Aqua Security vulnerability scan with zero Critical or High findings (CVSS ≥ 7.0)
- Meridian Secrets Scanner (no hardcoded credentials or keys)
- Dependency license compliance check via FOSSA

The scanning pipeline executes automatically on merge to the `main` branch of the serving-images repository. Scan results are published to the image's metadata in ECR.

**Step 4: Registry Registration**
Following successful security scanning, the image is tagged and pushed to ECR using the automated GitLab CI pipeline (`ci/serving-images/.gitlab-ci.yml`). The following tags are applied:

| Tag | Format | Example |
|-----|--------|---------|
| Version | `<model-group>-<version>-<git-short-sha>` | `diag-chestxray-2.3.1-a3f82b9` |
| Environment | `<env>-latest` | `prod-latest` |
| Build Timestamp | `<YYYYMMDD>-<HHMMSS>-<version>` | `20250520-143022-2.3.1` |

### 5.3 Model Deployment Procedures

#### 5.3.1 Pre-Deployment Checklist

Prior to initiating any production deployment, the Responsible MLOps Engineer shall complete the following checklist documented in Jira under the ticket type "Model Deployment Request" with the following verifications:

| # | Verification | Evidence Required | Sign-Off |
|---|-------------|-------------------|----------|
| 1 | Model artifact registered in MLflow with "Staging" stage transition completed | MLflow Registry screenshot | AI/ML Engineer |
| 2 | Model signature verified against production inference schema | MLflow `model-signature.json` diff | AI/ML Engineer |
| 3 | IST completed with no failures and p99 latency within threshold | IST Report attached to Jira | MLOps Engineer |
| 4 | Container image passed all security scans | Aqua report link in ECR | Security Team |
| 5 | Traffic routing configuration PR merged to `meridian-istio-config` | GitLab MR link | SRE |
| 6 | Rollback procedure documented and validated in staging | Rollback runbook link | MLOps Engineer |
| 7 | Monitoring dashboards configured for new model version | Datadog dashboard link | SRE |

#### 5.3.2 Deployment Approval Workflow

```
Initiation: MLOps Engineer creates "Model Deployment Request" (Jira)
    ↓
Technical Review: Senior MLOps Engineer reviews checklist items 1–6
    ↓ (Approval gate: Technical)
Shadow Deployment: MLOps Engineer deploys as Ghost Traffic
    ↓
Observation Period: Minimum 4 hours of production ghost traffic
    ↓
Shadow Review: AI/ML Engineer reviews inference parity metrics
    ↓ (Approval gate: Shadow Validation)
Canary Deployment: MLOps Engineer configures 5% traffic split
    ↓
Observation Period: Minimum 2 hours at 5%, then increment to 20% for 4 hours
    ↓
Canary Review: Product Owner reviews, SRE confirms no alert firings
    ↓ (Approval gate: Canary Validation)
Full Production: MLOps Engineer configures 100% traffic shift
    ↓
Post-Deployment Observation: 24 hours with heightened monitoring
```

### 5.4 Traffic Routing Configuration

#### 5.4.1 Routing Rules Configuration

All traffic routing rules are defined declaratively in the `meridian-istio-config` GitLab repository using Istio VirtualService and DestinationRule custom resources. The following is the canonical routing configuration template:

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: <model-endpoint-name>-routing
  namespace: meridian-ml-serving
spec:
  hosts:
    - <model-endpoint-name>.meridian.svc.cluster.local
  gateways:
    - meridian-ml-gateway
  http:
    - match:
        - headers:
            x-meridian-traffic-group:
              exact: experimental
      route:
        - destination:
            host: <model-endpoint-name>-<new-version-hash>
            port:
              number: 8080
          weight: 100
    - route:
        - destination:
            host: <model-endpoint-name>-<stable-version-hash>
            port:
              number: 8080
          weight: 95
        - destination:
            host: <model-endpoint-name>-<canary-version-hash>
            port:
              number: 8080
          weight: 5
```

#### 5.4.2 Standard Traffic Split Progression

| Phase | Duration | Traffic Split (Stable : New) | Automatic Rollback Trigger |
|-------|----------|------------------------------|----------------------------|
| Shadow | 4 hours minimum | 100 : 0 (ghost mirrored) | N/A for ghost traffic |
| Canary Stage 1 | 2 hours | 95 : 5 | p99 latency > 115% of baseline OR error rate > 1% |
| Canary Stage 2 | 4 hours | 80 : 20 | p99 latency > 110% of baseline OR error rate > 0.5% |
| Full Production | Indefinite | 0 : 100 | p99 latency > 105% of baseline OR error rate > 0.1% for 15 consecutive minutes |
| Rollback State | Immediate | Return to previous stable | Triggered by SRE or automated rule |

### 5.5 Deployment Gate Procedures

#### 5.5.1 Shadow Deployment Validation

**Procedure 5.5.1.A: Ghost Traffic Configuration**
1. MLOps Engineer configures the Istio VirtualService to mirror 100% of production traffic to the shadow service using the `mirror` directive.
2. Shadow service responses are discarded; only request metrics are collected.
3. Ghost traffic volume must minimally equal 10% of average peak-hour production traffic volume to be considered representative.

**Procedure 5.5.1.B: Shadow Validation Criteria**
The shadow deployment must satisfy all of the following criteria before advancing to canary:

| Metric | Threshold | Measurement Source |
|--------|-----------|-------------------|
| Inference success rate | ≥ 99.95% | Datadog `model.inference.success_rate` |
| p99 latency vs. production baseline | ≤ 120% of production | Datadog `model.inference.latency_p99` |
| Prediction schema conformance | 100% valid responses | LangSmith schema validation |
| Memory utilization | ≤ 85% of pod limit | Datadog `container.memory.utilization` |
| Error rate | < 0.5% | Datadog `model.inference.error_rate` |
| Cold start latency | ≤ maximum permitted for product line | Datadog `model.cold_start.duration` |

**Procedure 5.5.1.C: Shadow Report**
The MLOps Engineer shall generate a "Shadow Deployment Validation Report" using the template in Confluence (`COPS-TEMPLATE-004`) and attach it to the Model Deployment Request Jira ticket. The report must include:
- Observation period start and end timestamps
- Total ghost traffic request count
- All metric values compared to thresholds
- PASS/FAIL determination for each criterion
- Approval signature from AI/ML Engineer

#### 5.5.2 Canary Deployment Validation

**Procedure 5.5.2.A: Canary Initiation**
1. Following successful shadow validation, the MLOps Engineer updates the VirtualService to split 5% of genuine production traffic to the new model version.
2. SRE acknowledges active monitoring and configures elevated alert sensitivity for the canary service.
3. Product Owner is notified via Slack channel `#prod-model-deployments`.

**Procedure 5.5.2.B: Canary Monitoring**
The following metrics shall be continuously monitored during the canary phase with automated rollback thresholds:

| Metric | Rollback Threshold (5% Phase) | Rollback Threshold (20% Phase) |
|--------|-------------------------------|--------------------------------|
| p99 latency increase over baseline | > 15% for 5 consecutive minutes | > 10% for 5 consecutive minutes |
| Error rate (5xx responses) | > 1% for 3 consecutive minutes | > 0.5% for 3 consecutive minutes |
| Prediction output volume deviation | > 10% from expected | > 5% from expected |
| Container restart count | > 3 restarts within any 15-minute window | > 3 restarts within any 15-minute window |

**Procedure 5.5.2.C: Canary Decision Gate**
After the minimum observation period for each canary stage, the MLOps Engineer shall:
1. Export monitoring data from Datadog for the full canary period.
2. Complete the "Canary Gate Checklist" (Confluence `COPS-TEMPLATE-005`).
3. Schedule a brief decision meeting (15 minutes) with the AI/ML Engineer and Product Owner if the canary is for a Clinical AI model, or proceed with documented engineering approval for non-clinical models.
4. Upon approval, proceed to the next traffic increment or full production deployment.

### 5.6 Rollback Procedures

#### 5.6.1 Rollback Triggers

A rollback shall be initiated immediately under any of the following conditions:

| Trigger | Detection Method | Authority to Initiate |
|---------|-----------------|----------------------|
| Automated metric threshold breach (per 5.5.2.B) | Datadog monitor alert | Automated (no human approval required) |
| Manual SRE observation of anomalous behavior | SRE judgment | SRE on-call, with post-facto notification to MLOps Lead |
| Clinical output quality concern raised by clinical team | Incident ticket via ServiceNow | MLOps Lead or AI/ML Engineering Director |
| Security vulnerability disclosure affecting serving image | Security advisory | Security Engineering Lead with SRE execution |

#### 5.6.2 Rollback Execution Procedure

**Step 1: Decision and Notification**
The initiator declares a rollback via the dedicated Slack channel `#prod-model-rollback` using the standardized message format:
```
ROLLBACK INITIATED
Model: <model-name>
Current Version: <failing-version>
Rollback Target: <stable-version>
Reason: <brief-description>
Initiator: <name>
Time: <ISO-8601 timestamp>
```

**Step 2: Traffic Reversion**
The MLOps Engineer or automated controller executes a `kubectl apply` of the previously-known-good VirtualService configuration, which:
- Reverts traffic weights to 100% on the prior stable version
- Ceases all traffic to the failing version
- Preserves the failing version's pods for forensic analysis

**Step 3: Verification**
1. Confirm that the ALB Target Group health checks for the stable version report healthy.
2. Verify via Datadog that traffic has shifted—monitor for a minimum of 5 minutes.
3. Run the automated smoke test suite stored in `meridian/smoke-tests` against the endpoint.
4. Confirm that error rates have returned to baseline levels.

**Step 4: Post-Rollback Actions**
1. The MLOps Engineer creates a "Rollback Incident Report" in Confluence using template `COPS-TEMPLATE-006`.
2. SRE preserves logs and metrics for the failing version for a minimum of 14 days.
3. The failing container image is tagged `quarantined-<date>` in ECR and removed from the serving path.
4. A post-mortem meeting is scheduled within 2 business days for any manual rollback.

### 5.7 Inference Endpoint Decommissioning

When a model version or endpoint is to be retired:

**Step 1: Deprecation Notice**
The Product Owner issues a deprecation notice to all registered inference consumers via the Meridian API Management Portal. Minimum notice periods:
- Internal consumers: 30 calendar days
- External partners (HealthPay credit scoring): 90 calendar days

**Step 2: Traffic Drain**
1. MLOps Engineer configures the VirtualService to route 0% traffic to the deprecated version.
2. The deprecated pods continue running for a 7-day drain period to capture any stale DNS or cached routing configurations from consumers.
3. Observability continues throughout the drain period.

**Step 3: Resource Decommissioning**
1. MLOps Engineer scales the deprecated deployment to zero replicas.
2. After 30 days of zero traffic, the Kubernetes Deployment and Service resources are deleted via Terraform.
3. Model artifacts remain in the MLflow Registry indefinitely with the `deprecated` tag applied.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

#### 6.1.1 Network Segmentation

| Control | Implementation | Verification |
|---------|---------------|--------------|
| VPC isolation | All inference endpoints exist within `meridian-prod-vpc` (10.100.0.0/16) | AWS Config rule `VPC_FLOW_LOGS_ENABLED` |
| Subnet segmentation | Model serving pods run in private subnets only; ALBs in public subnets with restricted security groups | Monthly network configuration review |
| Security groups | EKS node groups accept traffic only from ALB security group on port 8080 | AWS Firewall Manager continuous monitoring |
| Egress filtering | EKS node groups permit outbound only to MLflow Registry (VPC endpoint), Datadog (VPC endpoint), and required AWS APIs (VPC endpoints) | VPC Flow Log analysis, reviewed weekly |

#### 6.1.2 Authentication and Authorization

| Control | Implementation | Scope |
|---------|---------------|-------|
| Consumer authentication | OAuth 2.0 client credentials via Okta; tokens validated at ALB | All external inference consumers |
| Service-to-service authentication | mTLS within Istio service mesh | All inter-service inference calls |
| Registry access | IAM roles scoped to specific model groups; no cross-group access without exception | MLflow Model Registry |
| EKS pod identity | IRSA (IAM Roles for Service Accounts) per deployment | Each model serving deployment |

#### 6.1.3 Encryption

| Data State | Encryption Standard | Key Management |
|------------|---------------------|----------------|
| Inference data in transit | TLS 1.3 (external), mTLS 1.3 (internal mesh) | AWS Certificate Manager (public), Meridian Internal CA (mesh) |
| Inference data at rest (logs) | AES-256-GCM | AWS KMS CMK `meridian-inference-logs` |
| Model artifacts at rest | SSE-KMS | AWS KMS CMK `meridian-model-artifacts` |
| Container images at rest | AES-256 (ECR default) | AWS-managed key |

#### 6.1.4 Access Logging

All production inference endpoints shall emit structured access logs to the centralized `meridian-inference-logs` CloudWatch Log Group. Each log entry shall minimally contain:

| Field | Description |
|-------|-------------|
| `timestamp` | ISO-8601 with millisecond precision, UTC |
| `request_id` | UUIDv4 generated at ALB ingress |
| `consumer_id` | OAuth client ID extracted from bearer token |
| `model_name` | MLflow registered model name |
| `model_version` | SHA-256 hash of model artifact |
| `inference_duration_ms` | Total pipeline execution time in milliseconds |
| `response_status` | HTTP status code returned |
| `input_schema_version` | Schema version identifier |
| `trace_id` | Datadog trace correlation ID |

### 6.2 Administrative Controls

#### 6.2.1 Change Management

All changes to production serving infrastructure shall be managed through the Meridian Change Management process:

| Change Type | Approval Required | Change Window |
|-------------|-------------------|---------------|
| New model version deployment | MLOps Lead + Product Owner | Any time; business hours preferred |
| Traffic split modification | MLOps Lead | Any time for rollback; business hours for split adjustments |
| Infrastructure IaC modification | SRE Lead + VP of Engineering | Scheduled maintenance windows only |
| Security group modification | Security Engineering Lead | Emergency: anytime; Non-emergency: maintenance windows |

#### 6.2.2 Quarterly Infrastructure Review

The AI/ML Engineering team, in coordination with SRE, shall conduct a quarterly review of all production inference infrastructure. The review shall address:

- Capacity planning and utilization trends
- Latency SLA compliance across all endpoints
- Security vulnerability remediation status for serving images
- Dependency currency (base image, libraries, runtimes)
- Cost attribution per model endpoint
- Archival or decommissioning candidates

The review output is documented in Confluence under `Quarterly Inference Infrastructure Review <YYYY-QN>`.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators

The following KPIs define the operational health of the model serving infrastructure:

| KPI | Definition | Target | Measurement Window |
|-----|------------|--------|---------------------|
| **Inference Availability** | (Total requests - Failed requests) / Total requests | ≥ 99.9% | Rolling 30 days |
| **Inference Latency (p99)** | 99th percentile of round-trip response time | Per product line (Section 1.3) | Rolling 7 days |
| **Inference Success Rate** | HTTP 2xx responses / Total requests | ≥ 99.9% | Rolling 30 days |
| **Deployment Success Rate** | Successful deployments / Total deployment attempts | ≥ 95% | Rolling 90 days |
| **Mean Time to Rollback** | Duration from rollback decision to 100% traffic on stable version | ≤ 5 minutes | Rolling 90 days |
| **Container Image Vulnerability SLA** | Time from Critical CVE publication to remediation in production | ≤ 48 hours | Per incident |
| **Cold Start Latency** | Time from pod scheduling to first successful inference response | ≤ 120 seconds | Rolling 30 days |
| **Resource Utilization Efficiency** | GPU memory utilization for GPU workloads | ≥ 60% average | Rolling 30 days |

### 7.2 Dashboard Requirements

The following dashboards shall be maintained in Datadog:

| Dashboard Name | Primary Audience | Refresh Interval | Key Visualizations |
|----------------|-----------------|------------------|-------------------|
| `[Prod] Model Inference - Overview` | MLOps, SRE, Product Owners | 1 minute | Aggregate latency heatmaps, availability by endpoint, top-N error types |
| `[Prod] Model Inference - Per Endpoint` | AI/ML Engineers, Product Owners | 30 seconds | Per-model latency distributions, throughput, error rates, traffic split visualization |
| `[Prod] Model Serving - Infrastructure` | SRE, Platform Engineering | 1 minute | Node CPU/GPU/memory, pod restart counts, network throughput, disk I/O |
| `[Prod] Model Registry - Deployment Audit` | Compliance, Security | Near-real-time | Deployment event log, version transitions, traffic routing history |
| `[Prod] Model Inference - Cost Attribution` | Engineering Management, Finance | 1 hour | Per-endpoint compute cost estimate, GPU utilization cost efficiency |

### 7.3 Reporting Cadence

| Report | Frequency | Audience | Prepared By |
|--------|-----------|----------|-------------|
| Inference SLA Compliance Report | Monthly | Product Owners, VP of Engineering | MLOps Lead |
| Infrastructure Capacity Forecast | Monthly | VP of Engineering, Infrastructure | SRE Lead |
| Model Deployment Log | Continuous (dashboard) | AI/ML Engineering | Automated (Datadog) |
| Cost Attribution Analysis | Monthly | Engineering Directors, Finance | SRE Lead |
| Quarterly Infrastructure Review | Quarterly | Chief AI Officer, VP of Engineering | MLOps Lead + SRE Lead |
| Security Vulnerability Report | Weekly | Security Engineering, MLOps | Security Team (automated scan) |

### 7.4 Alert Thresholds

Alerts are configured in Datadog and routed to PagerDuty for on-call SRE and MLOps personnel:

| Alert Name | Trigger Condition | Severity | Notification Channel |
|------------|-------------------|----------|---------------------|
| `inference-endpoint-down` | Health check failure for 2 consecutive intervals (30s) | Critical | PagerDuty: SRE + MLOps |
| `inference-latency-spike` | p99 latency exceeds product line threshold for 5 consecutive minutes | Warning → Critical at 10 min | PagerDuty: MLOps; Slack: #prod-model-alerts |
| `inference-error-rate-spike` | Error rate > 1% for 3 consecutive minutes | Critical | PagerDuty: MLOps + SRE |
| `model-container-restart-loop` | > 5 restarts in 15 minutes for any pod | Warning | PagerDuty: MLOps |
| `gpu-underutilization` | GPU utilization < 30% for > 24 hours | Low | Slack: #prod-model-alerts |
| `container-image-cve` | Critical CVE in any active serving image | High | PagerDuty: Security + MLOps |
| `traffic-routing-drift` | Actual traffic split deviates > 2 percentage points from configuration | Warning | PagerDuty: MLOps |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Request Procedure

Situations requiring deviation from the standards defined in this SOP shall be managed via the formal Exception Request process. An Exception Request is required under any of the following circumstances:

- Deployment of a model without completion of the full shadow/canary progression
- Serving a model on infrastructure not conforming to the defined instance family specifications
- Exceeding maximum permitted latency thresholds for a defined period
- Use of non-standard base images for serving containers
- Deployment of models without the mandated access logging
- Operating without a configured rollback target
- Bypassing required security scanning for emergency patches

### 8.2 Exception Request Workflow

**Step 1: Documentation**
The requestor creates a "Serving Infrastructure Exception Request" in ServiceNow using form template `SERV-EXC-018`. The request must include:

| Field | Required Detail |
|-------|-----------------|
| Exception Type | Category from list defined in 8.1 |
| SOP Reference | Specific policy statement or procedure from which deviation is sought |
| Justification | Business, technical, or clinical rationale |
| Risk Assessment | Identified risks and proposed mitigations |
| Duration | Start date, end date, or "permanent" with justification |
| Rollback Plan | How the exception will be reversed |

**Step 2: Technical Review**
The MLOps Lead reviews the exception request and assesses:
- Technical feasibility of the proposed alternative
- Impact on observability and incident response capability
- Security implications

**Step 3: Approval Authority**
Exception approval authority is determined by severity and duration:

| Exception Duration | Risk Level | Approver |
|--------------------|------------|----------|
| ≤ 24 hours | Low technical risk | MLOps Lead alone |
| ≤ 7 calendar days | Medium risk | MLOps Lead + Security Engineering Lead |
| ≤ 30 calendar days | High risk | VP of Engineering |
| > 30 calendar days or permanent | Any | VP of Engineering + Chief AI Officer + Chief Information Security Officer |

**Step 4: Tracking and Expiry**
Approved exceptions are tracked in the ServiceNow "Active Exceptions" dashboard. All time-limited exceptions shall automatically generate a notification to the requestor and approver 48 hours before expiration. Expired exceptions must be either renewed through the same workflow or remediated immediately.

### 8.3 Escalation Path for Inference Incidents

When an inference-related incident occurs that cannot be resolved by standard procedures, the following escalation hierarchy shall be followed:

```
Level 1: MLOps Engineer on-call (Initial response < 15 minutes)
    ↓ Unresolved after 30 minutes
Level 2: Senior MLOps Engineer + SRE on-call
    ↓ Unresolved after 60 minutes
Level 3: MLOps Lead + SRE Lead + Affected Product Owner
    ↓ Unresolved after 120 minutes
Level 4: VP of Engineering + Chief AI Officer
    ↓ Unresolved after 240 minutes
Level 5: CTO + Executive Incident Response Team
```

---

## 9. Training Requirements

### 9.1 Required Training Modules

All personnel with responsibilities defined in Section 3 shall complete the following training:

| Training Module | Course Code | Frequency | Target Audience | Delivery Method |
|-----------------|-------------|-----------|-----------------|-----------------|
| Model Serving Architecture Overview | ML-OPS-101 | Annually | All AI/ML Engineers, MLOps, SRE | LMS + Live Workshop |
| Production Deployment Procedures | ML-OPS-201 | Annually | MLOps Engineers, SRE | LMS + Hands-on Lab |
| Incident Response for Inference | SRE-IR-018 | Quarterly refresher | SRE, MLOps on-call | Simulated incident drill |
| Secure Model Serving Practices | SEC-ML-301 | Annually | All AI/ML Engineers, MLOps | LMS |
| Traffic Routing and Rollback | ML-OPS-202 | Semi-annually | MLOps Engineers | Hands-on Lab |
| Inference Monitoring and Alerting | OBS-ML-101 | Annually | SRE, MLOps | LMS + Dashboard walkthrough |

### 9.2 Training Tracking and Compliance

- Completion of required training shall be tracked in the Meridian Learning Management System (Workday Learning).
- Personnel who have not completed required annual training by their training anniversary date shall have their production deployment access temporarily suspended until compliance is achieved.
- The AI/ML Engineering management team shall review training compliance during quarterly team meetings.
- Training materials shall be reviewed and updated by the SOP Owner within 30 days of any major version change to this SOP.

### 9.3 Onboarding Requirements

New team members in roles with production inference responsibilities shall complete all required training modules before being granted:
- Access to the `prod-model-serving` ECR repository
- `kubectl` write access to production EKS clusters
- PagerDuty on-call rotation inclusion
- Merge permissions to the `meridian-istio-config` repository

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|--------|-------|--------------|
| SOP-AIML-001 | Model Governance Framework | Governs model lifecycle from development through decommissioning; this SOP operationalizes the deployment and operations phase |
| SOP-AIML-002 | Environment Management for AI/ML | Defines development, staging, and production environment configurations |
| SOP-AIML-015 | Model Training Pipeline Operations | Governs the upstream processes that produce model artifacts served under this SOP |
| SOP-AIML-022 | Model Explainability and Interpretability | Defines requirements for explanation generation that may accompany inference responses |
| SOP-AIML-024 | Bias Monitoring and Fairness Assessment | Governs ongoing fairness evaluation of production models |
| SOP-DATA-009 | Feature Store Management | Governs the feature engineering infrastructure that feeds inference pipelines |
| SOP-SEC-017 | Container Security Standards | Defines image scanning and vulnerability management requirements |
| SOP-SEC-023 | Production Access Control | Defines access management for production systems |
| SOP-INFRA-004 | Kubernetes Cluster Operations | Governs the EKS platform hosting serving workloads |
| SOP-INFRA-011 | Incident Management and Response | Defines incident response procedures invoked during inference outages |

### 10.2 External Standards and References

| Reference | Version / Date | Applicability |
|-----------|----------------|---------------|
| NIST SP 800-53 Rev 5 | 2020 | Security controls framework informing Sections 6 and 7 |
| ISO/IEC 27001:2022 | 2022 | Information security management, particularly access controls and encryption |
| AWS Well-Architected Framework - Machine Learning Lens | 2024 | Architectural best practices for cloud ML serving |
| Istio Documentation v1.19 | 2024 | Traffic management configuration reference |
| MLflow Documentation v2.6.0 | 2024 | Model registry and serving reference |

### 10.3 Internal Tools and Systems Referenced

| System | Purpose | Owner |
|--------|---------|-------|
| MLflow (Meridian Model Registry) | Model artifact storage and versioning | AI/ML Engineering |
| Datadog APM + LangSmith | Observability, tracing, and monitoring | SRE + AI/ML Engineering |
| PagerDuty | Incident alerting and on-call management | SRE |
| ServiceNow | Incident tracking and exception management | IT Service Management |
| Confluence (KB space: COPS-KB) | Runbooks, templates, and documentation | AI/ML Engineering |
| GitLab (`meridian-istio-config`) | GitOps traffic routing configuration | MLOps |
| GitLab (`meridian/serving-images`) | Container image source of truth | MLOps |
| AWS ECR (`prod-model-serving`) | Production container image registry | Platform Engineering |
| AWS EKS (`meridian-prod-us-east`, `meridian-prod-eu-west`) | Kubernetes serving infrastructure | Platform Engineering |
| Okta | Identity provider for inference consumer authentication | Security Engineering |

---

## 11. Revision History

| Version | Date | Author | Approver | Description of Changes |
|---------|------|--------|----------|------------------------|
| 1.0 | 2023-08-15 | James Okonkwo (MLOps Lead) | Dr. Marcus Rivera | Initial publication. Established baseline serving architecture on EKS with Istio, shadow/canary deployment model, and latency SLAs per product line. |
| 1.1 | 2023-12-04 | Priya Sharma (Senior MLOps Engineer) | James Okonkwo | Minor revision. Added asynchronous inference architecture pattern (Section 5.1.2). Updated GPU instance selection guidelines for Clinical AI workloads from g4dn to g5 series. Corrected health check endpoint port specification. |
| 2.0 | 2024-08-22 | James Okonkwo, Thomas Lindström | David Park | Major revision. Migrated traffic routing from NGINX-based custom solution to Istio service mesh. Introduced GitOps workflow for routing configuration. Added mTLS requirement for inter-service communication. Expanded deployment gating procedures with formal shadow validation criteria. Added exception handling process and training requirements sections. Updated all references to MLflow v3.0. |
| 2.0.1 | 2025-01-15 | James Okonkwo | Dr. Marcus Rivera | Hotfix revision. Corrected instance type table for Credit Scoring workload (c6i.large → c6i.2xlarge). Added LangSmith integration reference. Updated container image base version to 3.4.0 to address CVE-2024-12345. Clarified TLS terminology throughout. |
| 2.1 | 2025-05-20 | Dr. Elena Vasquez (Director of ML Engineering), James Okonkwo | David Park | Scheduled revision. Added granular instance selection guidelines and justification table (Section 5.1.3). Formalized cold start measurement requirements. Updated escalation paths with named roles. Added new KPIs: Container Image Vulnerability SLA and Resource Utilization Efficiency. Expanded monitoring dashboard specifications. Updated all cross-references to align with SOP numbering reorganization. Incorporated feedback from Q1 2025 infrastructure review. |

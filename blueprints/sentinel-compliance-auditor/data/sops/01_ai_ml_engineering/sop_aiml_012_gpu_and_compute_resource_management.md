---
sop_id: "SOP-AIML-012"
title: "GPU and Compute Resource Management"
business_unit: "AI/ML Engineering"
version: "5.2"
effective_date: "2024-05-01"
last_reviewed: "2025-08-20"
next_review: "2026-02-24"
owner: "Dr. Marcus Rivera, Chief AI Officer"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: GPU and Compute Resource Management

## 1. Purpose and Scope

### 1.1 Purpose

The purpose of this Standard Operating Procedure (SOP) is to establish a unified, enterprise-wide framework for the provisioning, allocation, monitoring, and cost governance of Graphics Processing Unit (GPU) and general compute resources across all business units of Meridian Health Technologies, Inc. Effective compute resource management is critical to maintaining the performance and reliability of production AI systems that directly impact patient care, financial operations, and population health analytics. This SOP defines the mechanisms by which Meridian balances the competing demands of model development velocity, production inference throughput, cost efficiency, and regulatory compliance obligations associated with high-risk AI systems.

### 1.2 Scope

This SOP applies to all compute and GPU resources utilized within the Meridian technology ecosystem, including but not limited to the following environments and services:

| Environment | Scope | Primary Infrastructure |
|---|---|---|
| Production | All customer-facing systems, Clinical AI inference endpoints, HealthPay scoring engines, MedInsight analytics pipelines | AWS us-east-1, eu-west-1, Azure DR |
| Staging | Pre-production validation environments mirroring production configurations | AWS us-east-1, eu-west-1 |
| Development | Model training, experimentation, JupyterHub workspaces, CI/CD pipelines | AWS us-east-1, eu-west-1, SageMaker |
| DR / BCP | Azure failover compute clusters for Tier-1 services | Azure East US 2, North Europe |

**In-scope resources:**
- All NVIDIA GPU instance types across AWS EC2 (P4d, P4de, G5, G6, G6e families) and Azure (ND-series, NCasT4_v3-series)
- AWS SageMaker managed training and inference instances
- Amazon EKS-based Kubernetes node pools (both CPU and GPU)
- ECS Fargate and EC2-backed clusters
- Reserved Instances, Savings Plans, and Spot Instance fleets
- Snowflake virtual warehouses (compute clusters for analytical workloads)
- Pinecone vector database indexes (to the extent that infrastructure sizing choices affect compute cost)

**Out-of-scope:**
- Employee laptops, workstations, and personal devices (governed by SOP-IT-002, Endpoint Management Standard)
- Office network hardware and edge devices
- Third-party SaaS platforms where Meridian does not provision or scale the underlying compute (e.g., Datadog agents, Okta tenant infrastructure)

### 1.3 Applicability

This SOP is binding upon all personnel, contractors, and vendors who provision, configure, access, or consume compute or GPU resources within the Meridian cloud environment. Specifically:

- **AI/ML Engineering** — Primary consumers and operators of GPU-accelerated training and inference
- **Clinical AI Products** — Owners of production inference service levels and model deployment specifications
- **HealthPay Financial Services Engineering** — Operators of GPU-accelerated fraud detection and credit scoring models subject to SR 11-7
- **MedInsight Analytics** — Owners of population-scale ETL and model scoring workloads on Snowflake and SageMaker
- **IT Operations** — Infrastructure provisioning, capacity planning, and cloud financial operations
- **Information Security** — Control validation, network segmentation, and access governance

Compliance with this SOP is mandatory. Non-compliance shall be managed per SOP-HR-005, Employee Disciplinary Procedures.

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|---|---|
| **A100** | NVIDIA Ampere-architecture data center GPU, 80GB HBM2e variant, available on AWS P4d instances. Designated as Tier-1 GPU for production training workloads. |
| **Available Zone (AZ)** | Isolated location within an AWS region; GPU instance availability varies by AZ. |
| **Carbon Intensity Score** | Internal metric measuring estimated CO₂-equivalent emissions per GPU-hour, calculated using AWS Customer Carbon Footprint Tool data and internal wattage models. |
| **CFM (Cloud Financial Management)** | Meridian's practice of FinOps-aligned cost governance, led by IT Operations in partnership with Finance. |
| **Compute Unit (CU)** | Abstracted billing unit for Snowflake virtual warehouses; not directly comparable to EC2 vCPUs. |
| **Dedicated Tenancy** | EC2 instance launch mode where physical server hardware is not shared with other AWS accounts. Required for Clinical AI PHI workloads under SOP-AIML-003. |
| **GPU Cluster** | A logically grouped set of GPU instances within an EKS-managed Kubernetes node group, typically sharing network placement group and storage endpoints. |
| **GPU Reservation** | A pre-approved allocation of GPU instance hours for a specific project, team, or workload, with defined start/end dates and budget ceiling. |
| **H100** | NVIDIA Hopper-architecture GPU, 80GB HBM3 variant, available on AWS P5 instances. Designated Tier-1 GPU for next-generation training workloads and large language model (LLM) fine-tuning. |
| **Inference SLA** | The service level agreement defining minimum acceptable throughput (tokens/second or predictions/second) and maximum acceptable latency (p50, p95, p99) for production model endpoints. |
| **Model Registry** | Central metadata repository maintained in MLflow, containing model version lineage, approval status, and deployment target environment tags. |
| **Node Pool** | A Kubernetes construct grouping nodes with identical hardware specifications, scheduling labels, and taint/toleration policies within EKS. |
| **P4d / P5** | AWS EC2 instance families providing NVIDIA A100 and H100 GPUs respectively. |
| **Provisioned Concurrency** | The number of SageMaker endpoint instances kept "warm" to absorb inference traffic spikes without cold-start latency. |
| **Spot Interruption Notice** | A 2-minute warning signal sent by AWS when a Spot Instance is about to be reclaimed. Production workloads receiving this signal must gracefully drain and redirect per SOP-AIML-008. |
| **Spot-to-On-Demand Ratio** | The percentage of total GPU hours in an environment fulfilled by Spot versus On-Demand compute. Development environments target >70%; production environments target <15%. |

## 3. Roles and Responsibilities

The following responsibility assignment matrix defines accountability for each critical function within GPU and compute resource management.

| Activity | AI/ML Engineer | ML Platform Team | IT Ops / FinOps | InfoSec Engineering | VP Engineering (Approver) |
|---|---|---|---|---|---|
| **Workload Classification** — Assigning data sensitivity tier and workload criticality to each training job or inference endpoint | R | C | I | C | A |
| **Resource Provisioning** — Launching EC2 instances, creating EKS node groups, configuring SageMaker endpoints | C | R | A | I | I |
| **GPU Reservation Requests** — Submitting formal requests for dedicated GPU capacity | R | C | A | I | C |
| **Cost Tagging** — Ensuring 100% of GPU instances carry correct AWS resource tags (CostCenter, Project, Environment, DataClass) | R | R | A | C | I |
| **Access Control** — Granting, reviewing, and revoking IAM roles and EKS RBAC permissions to launch or modify GPU instances | C | C | I | A | I |
| **Capacity Planning Forecast** — Quarterly projections of GPU demand vs. cloud provider availability | C | R | A | I | I |
| **Budget Exception Approval** — Authorizing spend beyond established project GPU budgets | I | I | R | C | A |

### 3.3 Named Responsibilities

- **Dr. Marcus Rivera (Chief AI Officer):** Ultimate accountability for GPU resource allocation priority decisions affecting Clinical AI model training timelines versus production inference capacity. Chairs the monthly Compute Governance Council.
- **David Park (VP of Engineering):** Approver of this SOP and all subsequent revisions. Budget exception authority for any GPU expenditure exceeding $50,000 within a single billing month.
- **ML Platform Team Lead (currently TBD, reporting to Head of AI/ML):** Day-to-day operational responsibility for GPU cluster health, capacity dashboards, and provisioning automation.
- **Cloud FinOps Lead (IT Operations):** Ownership of GPU cost anomaly detection, reserved instance portfolio management, and monthly chargeback reporting to business units.
- **InfoSec Engineering Lead:** Ownership of IAM policies governing GPU instance launch and modification permissions, network boundary controls around GPU clusters, and quarterly access reviews.

## 4. Policy Statements

### 4.1 General Principles

The following high-level policy commitments govern all GPU and compute resource activities at Meridian:

**P-001: Classification Before Provisioning**
No GPU instance, SageMaker training job, or Snowflake virtual warehouse of size Medium or larger shall be provisioned until a data classification tier and workload criticality rating—as defined in this SOP—have been recorded in the provisioning request. This classification directly governs the selection of instance tenancy, encryption posture, and monitoring rigor.

**P-002: Least Privilege Access**
Access to provision, terminate, or modify GPU instances shall be governed exclusively through AWS Identity and Access Management (IAM) roles and EKS Role-Based Access Control (RBAC) policies. Direct use of AWS account root credentials is prohibited. Individual developer AWS IAM users with GPU provisioning permissions are prohibited; provisioning must occur through automation pipeline service roles or approved IT Operations personnel.

**P-003: Tagging and Attribution**
Every GPU instance, EKS node, or SageMaker endpoint shall carry the mandatory Meridian resource tag set defined in Section 6.2. Resources lacking complete tag coverage at launch time shall be automatically terminated by the Cloud Custodian enforcement policy within 2 hours of detection.

**P-004: Environment Isolation**
Production GPU clusters shall be deployed in dedicated AWS accounts (`meridian-prod`, `meridian-clinical-prod`) with network isolation from development and staging environments enforced via AWS Organization Service Control Policies (SCPs). Cross-account IAM role assumption from development to production accounts is strictly prohibited.

**P-005: Cost Transparency**
GPU-related cloud spend shall be attributed to consuming cost centers and projects via the mandatory tag structure. Monthly chargeback reports will be distributed to cost center owners no later than the 10th business day following AWS invoice receipt.

**P-006: Reserved Capacity Governance**
Purchases of AWS Reserved Instances (RIs) or Savings Plans with 1-year or 3-year terms exceeding $20,000 in aggregate up-front cost require documented business case with projected utilization >85% and approval from both VP of Engineering and CFO. Purchases below this threshold may be approved by VP of Engineering alone.

### 4.2 Data Classification Tier Mapping

This SOP references the enterprise data classification tiers defined in SOP-DSEC-001, Data Classification Standard. For purposes of compute resource management, the following tier-to-control mapping applies:

| Data Classification Tier | Examples at Meridian | Required Tenancy | EBS Encryption Required | Logging Level | Permitted Spot Instance Use |
|---|---|---|---|---|---|
| **Tier 1 — Regulated** | PHI in Clinical AI inference payloads, PII in HealthPay credit decision data, MDR clinical evidence datasets | Dedicated | Yes (default KMS key minimum) | Full (data plane logs enabled) | Prohibited |
| **Tier 2 — Confidential** | Proprietary model architectures, unredacted training datasets with PHI (dedicated tenancy enclave), business financials, audit evidence | Default or Dedicated | Yes | Full | Permitted with documented approval |
| **Tier 3 — Internal** | De-identified training datasets, model metrics, operational logs, internal communications | Default | Optional (recommended) | Metadata + selected data plane | Permitted, standard guardrails |
| **Tier 4 — Public** | Published model weights (open-source contributions), product documentation, press materials | Default | Not required | Metadata only | Permitted without restriction |

Any ambiguity in classification tier assignment shall be escalated to the Data Governance Committee (chair: Chief Privacy Officer) for resolution prior to compute provisioning.

### 4.3 Workload Criticality Rating

All GPU workloads must be assigned a Tier rating reflecting business criticality. This rating determines high-availability configurations, disaster recovery replication, and incident response priority.

| Workload Tier | Definition | Recovery Time Objective (RTO) | Recovery Point Objective (RPO) | HA Requirement |
|---|---|---|---|---|
| **Tier 1 — Mission Critical** | Direct patient safety impact or regulatory mandate; e.g., Clinical AI inference serving active patient encounters in EHR-integrated workflow | < 15 minutes | < 5 minutes | Multi-AZ, cross-region standby on Azure DR |
| **Tier 2 — Business Critical** | Revenue-impacting or customer SLA-bound; e.g., HealthPay real-time fraud scoring API, MedInsight daily PHI pipeline | < 60 minutes | < 1 hour | Multi-AZ within primary region |
| **Tier 3 — Business Essential** | Internal SLAs but non-customer-facing; e.g., weekly MedInsight population cohort builder, HealthPay monthly recalibration training | < 4 hours | < 24 hours | Single-AZ with AMI-based recovery |
| **Tier 4 — Non-Critical** | Experimental, ad-hoc analysis; e.g., data scientist exploration workspace, hackathon environments | Best effort / next business day | No formal RPO | None |

## 5. Detailed Procedures

### 5.1 GPU Reservation Request Process

This procedure governs the pre-approved allocation of GPU compute hours for individual projects, ensuring budget alignment and capacity planning visibility prior to resource consumption.

#### 5.1.1 Prerequisites
- Project code assigned in Meridian's Cost Accounting system
- AWS cost center tag value confirmed with Finance
- Data classification tier determined per Section 4.2
- Workload criticality rating assigned per Section 4.3

#### 5.1.2 Procedure Steps

| Step | Actor | Action |
|---|---|---|
| 1 | Requestor (AI/ML Engineer or Product Lead) | Navigate to ServiceNow Catalog Item "GPU Reservation Request — [SOP-AIML-012]" at `https://meridian.service-now.com/compute` |
| 2 | Requestor | Complete all mandatory fields in the request form: Project Code, Cost Center, GPU Instance Family (P4d/G6/etc.), Number of Concurrent Instances Required, Estimated GPU-Hours per Month, Start Date, End Date, Data Classification Tier, Workload Criticality Tier, Justification Narrative |
| 3 | Requestor | Attach workload sizing evidence: benchmark results, prior job duration telemetry, or vendor model sizing guidelines |
| 4 | ServiceNow Workflow | Auto-route request to ML Platform Team Lead for technical review |
| 5 | ML Platform Team Lead | Within 3 business days, evaluate: (a) whether the requested GPU family and count are technically appropriate; (b) whether sufficient AWS service quota exists; (c) whether the workload can be accommodated on Spot or must use On-Demand; (d) projected carbon intensity |
| 6 | ML Platform Team Lead | Either "Approve" with recommended instance configuration, or "Return" with specific feedback on required modifications |
| 7 | ServiceNow Workflow | If approved technically, route to Cloud FinOps Lead for budget validation |
| 8 | Cloud FinOps Lead | Within 2 business days, verify: (a) total projected monthly cost against budgeted allocation for cost center; (b) that cost is tagged to correct chargeback center; (c) that cost does not cause cost center to exceed quarterly budget without documented exception |
| 9 | Cloud FinOps Lead | Either "Approve — Budget Confirmed" or "Escalate — Budget Exception Required" (divert to Exception process per Section 8) |
| 10 | ServiceNow Workflow | Upon dual approval, automatically provision the approved GPU node group(s) via Terraform Enterprise, applying the approved configuration and tags |
| 11 | ServiceNow Workflow | Send confirmation email to requestor with Reservation ID (format: GPU-RES-YYYY-NNNN) and provisioning details |
| 12 | ML Platform Team | Track Reservation ID in the GPU Inventory Dashboard (Grafana dashboard "GPU Fleet Overview") with expiration date |

**Reservation Expiration:** Unless renewed by submission of a revised request 10 business days prior to expiration, GPU reservations automatically terminate on the End Date. Termination consists of draining and removing the associated EKS node group or terminating standalone EC2 instances. Expired reservations whose instances remain running beyond the End Date shall be flagged in nightly FinOps anomaly reports and terminated by IT Operations within 1 business day.

### 5.2 Production Inference Scaling Protocol

This procedure defines the operational rhythm for adjusting provisioned GPU capacity behind Clinical AI and HealthPay inference endpoints to maintain SLAs while controlling cost.

#### 5.2.1 Scaling Thresholds

| Metric | Scale-Out Trigger | Scale-In Trigger | Observation Window |
|---|---|---|---|
| **SageMaker Endpoint CPU Utilization** | >75% sustained for 5 minutes across all instances | <35% sustained for 60 minutes | CloudWatch `SageMaker/Endpoints` namespace |
| **SageMaker Endpoint GPU Utilization** | >80% sustained for 5 minutes | <40% sustained for 60 minutes | Same |
| **Model Invocation Latency p95** | Exceeds SLA threshold (Clinical AI: 300ms; HealthPay: 50ms) for 3 consecutive 5-minute periods | <50% of SLA threshold sustained for 120 minutes | CloudWatch Logs Insight query on model server access logs |
| **Endpoint Invocation Errors per Minute** | >1% error rate for 5 minutes | N/A for scale-in | CloudWatch `4xx`/`5xx` metric count |
| **SQS Queue Depth (per-endpoint)** | >1,000 queued requests for 3 consecutive minutes | <100 for 120 minutes | CloudWatch `ApproximateNumberOfMessagesVisible` |

#### 5.2.2 Scale-Out Execution

1.  **Detection:** CloudWatch alarm enters ALARM state. PagerDuty alert fires, routed to primary on-call rotation: Tier-1 Incidents -> ML Platform Team On-Call.
2.  **Acknowledge:** On-call engineer acknowledges PagerDuty alert within 5 minutes per SOP-IT-OPS-001 (Incident Management). Acknowledge includes recording the alarm trigger and current instance count in the incident channel (#incident-ml-compute in Slack).
3.  **Validate:** On-call engineer checks the SageMaker console and Datadog dashboard "Production Inference Overview" to confirm that the metric is not a transient spike and that scale-out is not already in progress from a prior alarm. If the alarm is determined to be a false positive (e.g., due to a synthetic load test not communicated), annotate the CloudWatch alarm and close the PagerDuty incident.
4.  **Determine Scaling Magnitude:**
    - **Normal Load Increase:** Increase endpoint instance count by **50% of current running instances**, rounded up to the nearest integer.
    - **Sustained High Error Rate (5xx):** Do not scale out. Immediately roll back to the last known-good model version per SOP-AIML-008 (Model Deployment and Rollback). Scaling out a faulty model version amplifies the blast radius.
5.  **Execute:** Apply the scaling action via the SageMaker `UpdateEndpointWeightsAndCapacities` API call. Use the approved Infrastructure as Code (IaC) module `meridian-sagemaker-scaling` version >= `2.1.0` from Meridian's Terraform Private Registry. **Direct console manipulation is prohibited for production endpoints.** If the IaC module fails, escalate to SRE Lead.
6.  **Validate Post-Scale:** Monitor the triggering metric for 10 minutes. If the metric remains in ALARM state, iterate Step 4 up to a maximum of 3 scaling actions within a 60-minute window. If SLA breach persists after the third scaling action, declare a P1 incident and escalate per SOP-AIML-008.
7.  **Update IaC:** If the new instance count is to become the new steady-state minimum, submit a pull request to the `meridian-platform-infra` repository updating the `min_instance_count` variable for the endpoint's IaC module. Do not leave IaC and live state divergent beyond the current sprint.

#### 5.2.3 Scale-In Execution

Scale-in operations carry higher risk than scale-out (prematurely reducing capacity below demand). They are therefore executed on a scheduled, deliberate cadence rather than purely automatically, except for Spot Instance rebalancing.

1.  **Automatic Spot Rebalancing:** AWS EC2 Auto Scaling Group instances launched via Spot are configured with capacity-optimized allocation strategy and capacity rebalancing enabled. When AWS emits a Spot Instance Rebalance Recommendation, the ASG gracefully drains the affected node and launches a replacement Spot instance in an alternative pool. This is fully automated and requires no human intervention.
2.  **Scheduled Review:** Scale-in candidate endpoints are identified by a weekly automated script that runs every Monday at 08:00 UTC. The script queries CloudWatch for all production SageMaker endpoints where GPU utilization has remained below 40% for the preceding 7-day sliding window.
3.  **Review Queue:** Results are posted as a ticket in the "ML Platform — Scale-In Review" Jira queue, priority "Medium."
4.  **ML Platform Team Triage:** On Tuesday, an ML Platform engineer reviews each candidate ticket. The engineer must manually validate:
    - Is a known workload spike scheduled within the next 14 days that would require the current capacity? (Check against the shared "ML Workload Calendar" in Outlook.)
    - Does reducing capacity below current levels violate the minimum instance count specified in the associated SLA document?
5.  **Execution:** If validated safe, the engineer reduces the endpoint instance count by **25% of current running instances**, rounded down to a minimum of 1 instance. The same IaC module requirement as 5.2.2 Step 6 applies.

### 5.3 GPU Node Pool Provisioning on EKS

This procedure standardizes the creation of GPU-accelerated Kubernetes node groups for containerized workloads.

**Prerequisites:**
- Approved GPU Reservation ID (see Section 5.1)
- `eksctl` version >= 0.175.0, installed on the designated DevOps workstation AMI
- `terraform` version >= 1.8.0, with authenticated access to Meridian Terraform Enterprise instance
- Valid Okta session for AWS CLI credential generation via `meridian-aws-okta`

**Procedure:**

1.  **Checkout IaC Repository:**
    ```bash
    git clone git@github.com:meridiantech/terraform-meridian-platform.git
    git checkout -b gpu-node-pool-add-<RESERVATION-ID>
    ```
    Navigate to `environments/<env>/eks/gpu-node-groups/`.

2.  **Define Node Group:** Create or modify a `.tf` file declaring the node group resource using the approved internal module `meridian-eks-gpu-node-group`. A complete configuration example is provided in Appendix A; mandatory parameters include:
    - `reservation_id` — links node costs to the approved reservation
    - `gpu_family` — allowed values: `A100x8`, `A100x1` (for fractional g5.12xlarge), `H100`
    - `node_count_min`, `node_count_max`
    - `instance_type_list` — priority-ordered list for capacity-optimized Spot allocation
    - `ami_id` — Must reference the latest Meridian Gold AMI from `data.aws_ami_ids.meridian_gpu_gold`, updated monthly
    - `taint` — Must include `nvidia.com/gpu=true:NoSchedule` to prevent non-GPU workload scheduling

3.  **Security Context Validation:** The module must include the `security_group_ids` parameter populated with the Meridian Standard GPU Security Group (`sg-meridian-gpu-standard-<env>`). This security group, managed by InfoSec via a separate IaC workspace, enforces:
    - Ingress only from the Meridian internal CIDR range (`10.0.0.0/8`) on ports 22 (SSH, bastion only), 443 (HTTPS), and 10250 (kubelet API)
    - Egress limited to AWS service endpoints and approved container registry hosts
    - No public IP assignment (parameter `associate_public_ip_address = false`)

4.  **Submit Pull Request:** Commit configuration with message `feat(gpu): Node group for reservation GPU-RES-YYYY-NNNN` and push. Open a Pull Request (PR) targeting the `main` branch. The PR automatically triggers:
    - Terraform Plan (via Atlantis automation)
    - OPA (Open Policy Agent) policy checks: verifies tag completeness, dedicated tenancy for Tier-1 data workloads, no public IPs, approved GPU family list
    - Required reviewer: at least one Senior ML Platform Engineer

5.  **Merge and Apply:** After OPA checks pass and human review approval is obtained, merge the PR. The Atlantis automation applies the Terraform plan. Monitor the apply output in the `#ml-infra-cicd` Slack channel. The total provisioning time from apply to "Nodes Ready" in EKS typically ranges from 8–15 minutes for On-Demand instances and may extend to 30 minutes for Spot fleets depending on capacity pool availability.

6.  **Validate Readiness:** Post-provisioning, verify node readiness:
    ```bash
    kubectl get nodes -l nvidia.com/gpu.present=true,reservation-id=<RESERVATION-ID>
    ```
    Expected output shows all nodes in `Ready` status with the `nvidia.com/gpu` allocatable resource > 0.

7.  **Deploy NVIDIA Device Plugin:** If this is the first GPU node group in the EKS cluster or a new GPU family not previously used in the cluster, ensure the NVIDIA GPU Operator (Helm chart `nvidia/gpu-operator`, version >= `v23.6.0`) is deployed and running. The operator is deployed once per cluster by the ML Platform Team as a DaemonSet; verify pod readiness:
    ```bash
    kubectl get pods -n gpu-operator -l app=nvidia-gpu-operator
    ```

8.  **Register in CMDB:** Upon successful provisioning, the ML Platform engineer updates the Configuration Management Database (ServiceNow CMDB) record for the cluster, adding the new GPU node group details under the "Compute Resources" related list. This step is automated post-Terraform apply via a ServiceNow webhook but must be spot-checked.

### 5.4 Snowflake Warehouse Provisioning and Scaling

Snowflake virtual warehouses power the MedInsight Analytics business unit's data transformation and model scoring workloads on regulated data.

**Provisioning Request:**
1.  **Requestor** submits ServiceNow ticket "Snowflake Warehouse Request" including: Data Classification Tier, expected peak concurrent queries, estimated average data volume scanned per query, justification for requested warehouse size.
2.  **MedInsight Data Engineering Lead** reviews and approves technical sizing.
3.  **Snowflake Account Admin (IT Operations)** provisions the warehouse via a Snowflake Terraform module (`meridian-snowflake-infra`), ensuring:
    - `MAX_CLUSTER_COUNT` set to a maximum of 5 (multi-cluster warehouse required for Tier-1/2; must be explicitly approved by VP of Engineering)
    - `AUTO_SUSPEND` configured: 60 seconds for development warehouses, 300 seconds for production warehouses
    - `AUTO_RESUME` = `true`
    - Resource Monitor assigned to the warehouse with a monthly credit quota, configured to `SUSPEND_WAREHOUSE` at 100% of quota threshold and `NOTIFY` cost center owner at 85% threshold

**Usage Enforcement:** Queries submitted against Tier-1 or Tier-2 data warehouses must include a mandatory query tag in Snowflake session parameters:
```sql
ALTER SESSION SET QUERY_TAG = 'dataclass:tier2|project:MEDINSIGHT-004|user:jdoe@meridian.com';
```
Warehouses processing Tier-1 PHI are configured by InfoSec to reject any query lacking a valid `dataclass:tier1` query tag.

## 6. Controls and Safeguards

### 6.1 Identity and Access Management (IAM)

Access to GPU EC2 instances and EKS GPU node groups is controlled through a layered model:

| Access Level | IAM Policy Name | Scope | Granting Process |
|---|---|---|---|
| **Read-Only Metadata** | `MeridianCompute-ReadOnly` | DescribeInstances, ListComputeEnvironments, view CloudWatch dashboards. No console SSH, no SSM session. | Granted automatically to all AI/ML Engineering personnel via Okta group `all-ml-engineers` |
| **Development Provisioner** | `MeridianCompute-DevProvisioner` | Full EC2 lifecycle permissions within sandbox account `meridian-dev-sandbox` only, conditional on tag compliance | ServiceNow access request with ML Platform Team Lead approval; 90-day expiry with mandatory re-certification |
| **Production Operator** | `MeridianCompute-ProdOperator` | Start/Stop/Reboot of tagged production instances; no launch or termination permissions | ServiceNow access request with InfoSec Engineering Lead + VP Engineering approval; mandatory quarterly access review |
| **Production Administrator** | `MeridianCompute-ProdAdmin` | Full EC2 lifecycle across production accounts, GPU node pool provisioning | Limited to ML Platform Team service accounts and 3 named individuals (break-glass roles); full audit logging enabled; quarterly review by InfoSec; PagerDuty alert on any human role assumption |

**SSH Access Restriction:** Direct SSH access to GPU EC2 instances is prohibited. All interactive access must occur through AWS Systems Manager Session Manager, which provides an audited, IAM-controlled shell session. Session Manager access is governed by the `MeridianCompute-ProdOperator` and higher-level policies. SSM Session logs are forwarded to the centralized Splunk index (`meridian_compute_access_logs`) with 365-day retention.

**EKS RBAC for GPU Scheduling:** Kubernetes namespaces designated for GPU workloads are protected by a ResourceQuota preventing unauthorized GPU consumption:
```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: gpu-quota
  namespace: <project-namespace>
spec:
  hard:
    requests.nvidia.com/gpu: "<number-approved-in-reservation>"
```
This quota is injected by the admission controller during namespace creation and must be modified only via IaC changes to the namespace configuration.

### 6.2 Mandatory Resource Tags

All provisioned GPU instances must carry the following tags. The Cloud Custodian `deny-untagged-gpu` policy enforces at launch time by terminating instances that do not comply within 2 hours.

| Tag Key | Description | Allowed Values / Example |
|---|---|---|
| `CostCenter` | Meridian Finance cost center code | `1100-Clinical-AI`, `2300-HealthPay-ML` |
| `Project` | Jira project key or approved project code | `CLINAI-042`, `HP-MODEL-RETRAIN` |
| `Environment` | Deployment environment | `prod`, `staging`, `dev`, `sandbox` |
| `DataClass` | Data classification tier per 4.2 | `tier1_regulated`, `tier2_confidential`, `tier3_internal`, `tier4_public` |
| `WorkloadTier` | Criticality rating per 4.3 | `tier1_mission`, `tier2_bizcrit`, `tier3_bizess`, `tier4_noncrit` |
| `CreatedBy` | Email or service account of provisioner | `ci-pipeline@meridian.com`, `maria.sanchez@meridian.com` |
| `ExpiryDate` | Date when resource should be reviewed for decommissioning | `YYYY-MM-DD`; set to exactly 90 days from launch for dev, 365 days for prod |
| `Repo` | Git repository IaC source | `meridiantech/terraform-meridian-platform` |

### 6.3 Network Segmentation

Production GPU clusters operate within a dedicated Virtual Private Cloud (VPC) (`vpc-meridian-prod-us-east-1`, CIDR `10.100.0.0/16`) with the following enforced network boundaries:

- **Private Subnet Only:** GPU instances have no route to an Internet Gateway. Egress to internet is mediated exclusively through VPC endpoints (for AWS services) or a centralized NAT Gateway cluster with TLS inspection (for external dependencies such as PyPI, NVIDIA driver repositories). The NAT Gateway inspection layer is managed by InfoSec and enforced by security groups.
- **Cross-VPC Peering Restriction:** The production GPU VPC does not accept peering connections from development or sandbox VPCs. Connectivity to shared services (e.g., shared MLflow Tracking Server in `vpc-meridian-shared-svc`) is via AWS PrivateLink only, ensuring traffic does not traverse public network paths.
- **Clinical AI Inference Enclave:** A dedicated subnet (`10.100.77.0/24`) with no outbound internet access of any kind—not even via NAT—is designated for Clinical AI inference GPU instances processing PHI. Model artifacts and container images are pre-staged via AWS VPC Endpoint to ECR. This subnet is further protected by AWS Network Firewall, which logs and can block anomalous outbound connection attempts in real-time.
- **Amazon EKS Pod Security Standards:** The `gpu-workload` namespace enforces the `restricted` Pod Security Standard (PSS) profile, preventing containers from running as root or with privileged access to the underlying GPU node OS.

## 7. Monitoring, Metrics, and Reporting

### 7.1 Operational Dashboards

The following Grafana dashboards provide real-time GPU fleet visibility and are mandatory additions to the on-call engineer's operational view during business hours and incident response:

**Dashboard: "GPU Fleet Operational Overview"** (Grafana UID: `meridian-gpu-fleet-ops`)
- **Panel — GPU Availability by AZ:** Stacked area chart of active GPU instances (count) grouped by AWS AZ and GPU family. Refresh: 1 min. Alert: Trigger if any production cluster's active GPU count drops below 75% of declared minimum for more than 15 minutes.
- **Panel — GPU Utilization (Percent):** Time-series of weighted average GPU core utilization (`nvidia_smi_utilization_gpu_percent` via DCGM exporter) across all nodes in the `prod` EKS environment. Alert: Trigger if sustained >92% for 30 minutes for Tier-1 workloads.
- **Panel — GPU Memory Utilization (Percent):** Same as above, monitoring `nvidia_smi_memory_used_bytes / total`. Alert: Trigger if >90% sustained for 15 minutes (suggests incorrect batch sizing or memory leak).
- **Panel — Instance Fleet Cost Rate ($/Hour):** Calculated real-time aggregated on-demand equivalent hourly cost of all running GPU instances. Includes Spot discounts.

**Dashboard: "SageMaker Endpoint Health"** (Grafana UID: `meridian-sagemaker-endpoints`)
- Filters: Endpoint Name, Environment, Workload Tier
- Panels: Invocations per Second, Invocation Latency (p50, p95, p99), Invocation Errors (4xx, 5xx), Instance Count

### 7.2 Financial Reporting Cadence

| Report | Frequency | Audience | Delivery Mechanism |
|---|---|---|---|
| **Cost Center GPU Spend Summary** | Monthly, by 10th business day | All cost center owners (Director-level+) | Automated email from CloudZero, includes month-over-month delta and top-5 spend drivers |
| **GPU Reservation Utilization Report** | Monthly | Dr. Marcus Rivera, ML Platform Team Lead | Tableau workbook "GPU Reservation Compliance" shows each active Reservation ID, allocated hours, consumed hours, and % utilized; <50% utilized reservations flagged for review |
| **Spot vs. On-Demand Savings Report** | Quarterly | VP of Engineering, CFO | AWS Cost Explorer report quantifying realized savings from Spot and Savings Plans relative to On-Demand list price |
| **Carbon Footprint Summary** | Quarterly | Chief AI Officer, Sustainability Committee | Aggregated tCO2e attributable to GPU compute, trended quarterly, sourced from AWS Customer Carbon Footprint Tool |

### 7.3 Key Performance Indicators (KPIs)

| KPI | Target | Measurement Method |
|---|---|---|
| **GPU Instance Tag Compliance** | 99.5% of running instances | Cloud Custodian nightly report: tagged_instance_count / total_running_instance_count |
| **Spot Instance Utilization (Dev/Staging)** | >65% of total GPU hours | AWS Cost Explorer spot vs. on-demand usage for non-production linked accounts |
| **Mean Time to Provision (MTTP)** | <24 hours from final approval to node readiness for standard GPU node pools | ServiceNow ticket timestamp delta: `time_provisioned` — `time_approved` |
| **Production GPU Incident Rate** | <2 P1/P2 incidents per month attributable to GPU/capacity failures | PagerDuty incident count tagged `component:gpu_infrastructure` |

## 8. Exception Handling and Escalation

### 8.1 Exception Types

Deviations from this SOP are categorized and managed as follows:

| Exception Type | Definition | Approval Authority | Max Validity |
|---|---|---|---|
| **Budget Exception** | GPU spend for a reservation will or does exceed approved monthly allocation by >10% | VP of Engineering | End of current quarter |
| **Capacity Exception** | Insufficient On-Demand GPU capacity in primary region/AZ; requesting use of alternate instance family or region | ML Platform Team Lead + Chief AI Officer | Until AWS capacity is restored, reviewed monthly |
| **Scheduling Exception** | Request to run Tier-1 regulated workload on Spot instances contrary to Section 4.2 prohibition | Chief AI Officer + Chief Privacy Officer | Project-specific, max 30 days per approval |
| **Tenancy Exception** | Request to use Default tenancy for Tier-1 data workload | Chief AI Officer + CISO | Project-specific, needs re-approval per project phase |

### 8.2 Exception Handling Process

1.  **Submission:** Requestor submits a ServiceNow ticket type "GPU Compute Exception — [Type]" containing:
    - Link to the violated policy statement
    - Detailed business justification
    - Proposed compensating controls
    - Duration for which exception is needed
    - Risk acknowledgement

2.  **Risk Assessment:** The ML Platform Team Lead, in consultation with InfoSec Engineering if security controls are impacted, assesses the technical and business risk within 3 business days. The assessment is documented in the ticket.

3.  **Approval Workflow:**
    - Budget Exception: ServiceNow routes to Cloud FinOps Lead (review) -> VP of Engineering (approve/reject)
    - All other exceptions: ServiceNow routes to ML Platform Team Lead (recommend) -> Specified Approval Authority from table 8.1 (approve/reject)

4.  **Implement Controls:** If approved, the exception is recorded in the "Exception Register" (a maintained Confluence page under the AI/ML Engineering space). The compensating controls accepted in the risk assessment must be implemented and validated by the requestor within 5 business days. Failure to implement compensating controls invalidates the exception.

5.  **Expiration and Review:** Exceptions automatically expire on their max validity date unless renewed by resubmission. The Compute Governance Council (monthly meeting) reviews all active exceptions.

### 8.3 GPU Instance Interrupt Escalation

In the event of an unexpected, widespread loss of GPU capacity (e.g., multi-AZ AWS instance termination event, large-scale Spot market disruption):

1.  **Immediate (0-15 min):** On-call ML Platform engineer declares incident, pages SRE Lead. Implement standard Spot interruption draining (automated for Spot; manual drain-and-replace for On-Demand if capacity is available).
2.  **15-60 min:** If Tier-1 inference workloads are impacted and capacity cannot be restored in primary AZ/region, SRE initiates failover to secondary region (Azure DR for Clinical AI per SOP-AIML-011). HealthPay Tier-2 workloads may absorb queued load; MedInsight batch workloads are paused.
3.  **60+ min:** Chief AI Officer notified. If capacity remains unavailable, invoke emergency GPU capacity reservation in alternate AWS account (`meridian-dr-prod`). Escalate to AWS Enterprise Support / Technical Account Manager (TAM) for capacity routing assistance. VP of Engineering briefed for potential customer SLA communication.

## 9. Training Requirements

### 9.1 Initial and Recurring Training

| Audience | Training Module | Frequency | Delivery Method | Tracking |
|---|---|---|---|---|
| **All AI/ML Engineers** | "GPU Resource Management at Meridian" (custom SCORM module covering SOP contents, cost awareness, tag discipline) | Within 30 days of hire; annually thereafter | Workday Learning | Completion recorded in Workday; non-compliance flagged to manager within 45 days |
| **ML Platform Team** | "Hands-on GPU Provisioning Lab" (workshop covering Terraform modules, EKS GPU node groups, incident response runbooks) | Quarterly, aligned to Meridian's "Tech Skills Day" | Instructor-led, virtual | Registration via Workday; attendance tracked by instructor. Must complete within two quarters to retain Production Administrator IAM privileges. |
| **Cost Center Owners** | "FinOps for GPU Consumers" (30-min e-learning on chargeback reports, reservation ROI) | Annually | Workday Learning | Required to receive FY GPU budget allocation |
| **On-Call Rotation Personnel** | "GPU Incident Response Drill" (simulated GPU capacity outage using Chaos Engineering framework; exercises failover to Azure DR) | Semi-annually | Facilitated simulation by SRE team | Drill report published to Confluence; participants named. Failure to participate in >1 drill per year results in removal from on-call rotation. |

### 9.2 Compute Governance Council Onboarding

New members of the Compute Governance Council (Chief AI Officer delegates, ML Platform Team Lead, Cloud FinOps Lead, InfoSec liaison) must complete a "GPU Governance Deep Dive" session within 30 days of joining. This 90-minute session reviews all active exceptions, current AWS reservation portfolio, capacity planning forecast models, and the quarterly GPU budget outlook. The session is led by the current Cloud FinOps Lead.

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| Reference | SOP ID | Relationship to GPU Management |
|---|---|---|
| **Data Classification Standard** | SOP-DSEC-001 | Defines data tiers used in Section 4.2 tenancy and encryption controls |
| **Model Deployment and Rollback** | SOP-AIML-008 | Defines inference endpoint deployment patterns referenced in 5.2 scaling |
| **PHI Data Handling for AI Workloads** | SOP-AIML-003 | Mandates Dedicated Tenancy for Clinical AI PHI workloads |
| **Incident Management** | SOP-IT-OPS-001 | Defines P1-P4 severity and response timelines referenced in escalation |
| **Cloud Financial Management (FinOps)** | SOP-FIN-022 | Defines chargeback model, budget governance, and RI purchasing authority |
| **AWS IAM and Access Governance** | SOP-ISEC-007 | Defines IAM policy lifecycle, access review cadence, and break-glass procedure |
| **Infrastructure as Code (IaC) Standard** | SOP-IT-INFRA-005 | Mandates Terraform Enterprise for all production provisioning |
| **Employee Disciplinary Procedures** | SOP-HR-005 | Consequences for deliberate policy violation |
| **Endpoint Management Standard** | SOP-IT-002 | Out-of-scope compute management |
| **BC/DR Plan — Clinical AI** | SOP-AIML-011 | Failover procedure to Azure DR for Tier-1 Clinical AI inference |

### 10.2 External Standards and References

This SOP is informed by best practices published by the FinOps Foundation (GPU-specific cost optimization patterns), NVIDIA's GPU Operator documentation for Kubernetes, and AWS's operational guidance on EC2 Spot Instances for machine learning. No direct compliance obligation arises from these external sources; they serve as implementation guidance only.

## 11. Revision History

| Version | Date | Author | Approver | Summary of Changes |
|---|---|---|---|---|
| **1.0** | 2021-03-15 | Dr. Marcus Rivera | David Park | Initial publication. Established basic GPU provisioning and tagging requirements for Clinical AI training workloads on P3 instances. |
| **2.0** | 2021-11-10 | Dr. Marcus Rivera | David Park | Expanded scope to include HealthPay GPU inference and general compute; introduced GPU Reservation Request process and initial cost chargeback; migrated tagging taxonomy to align with AWS Cost Allocation Tags. |
| **3.1** | 2022-06-05 | ML Platform Team (J. Chen) | Dr. Marcus Rivera | Replaced P3 with P4d as standard GPU; added Production Inference Scaling Protocol (Section 5.2) in response to Clinical API latency incidents; added workload criticality tier definitions. |
| **4.0** | 2023-02-18 | Cloud FinOps Lead (M. Okonkwo) | Dr. Marcus Rivera, CISO | Major revision: introduced Spot usage policy for non-production, mandatory Cloud Custodian tagging enforcement, EKS GPU node group IaC module requirement, and Snowflake warehouse compute governance. Added exception handling process. |
| **5.0** | 2024-05-01 | Dr. Marcus Rivera | David Park | Added H100 (P5) support; introduced Carbon Intensity Score concept; revised scaling thresholds for next-gen inference SLAs; updated IAM policies for SSM-only access; added semi-annual incident response drill requirement. |
| **5.1** | 2024-12-12 | ML Platform Team (A. Petrov) | Dr. Marcus Rivera | Minor revision: updated EKS GPU node group Terraform module version to >= 4.1; modified Spot-to-On-Demand ratio target for development from 60% to 70%; clarified IAM break-glass role audit PagerDuty alert; added P5 availability zone guidance for us-east-1. |
| **5.2** | 2025-08-20 | Dr. Marcus Rivera | David Park | Routine review: updated role assignments to reflect current org chart; added G6/G6e instance families for inference; extended SSM log retention period to 365 days; added requirement for OPA policy checks in GPU node pool provisioning PR workflow. No substantive policy changes. Next scheduled review February 2026. |
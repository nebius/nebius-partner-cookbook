---
sop_id: "SOP-ISEC-018"
title: "Zero Trust Network Architecture"
business_unit: "Information Security"
version: "2.6"
effective_date: "2024-11-20"
last_reviewed: "2025-04-15"
next_review: "2025-10-11"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# STANDARD OPERATING PROCEDURE: SOP-ISEC-018
## Zero Trust Network Architecture

---

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the framework, principles, and operational requirements for Meridian Health Technologies, Inc.’s Zero Trust Network Architecture (ZTNA). The Zero Trust model eliminates implicit trust based on network location—whether on-premises, within a corporate perimeter, or in a cloud Virtual Private Cloud (VPC)—and instead requires continuous, identity-centric verification for every access attempt to any Meridian resource. This SOP operationalizes the principle of “never trust, always verify” across all business lines, cloud environments, and endpoint devices.

The purpose of this document is to:

- Define the architectural principles governing all network communications, authentication, and authorization within Meridian.
- Establish micro-segmentation strategies to isolate high-value assets, including Protected Health Information (PHI), clinical AI model training data, and financial services transaction engines.
- Implement identity-centric security controls that decouple access policy from network topology.
- Provide a phased implementation roadmap aligned with regulatory obligations under HIPAA, SOC 2, GDPR, the EU AI Act, and SR 11-7.
- Define continuous monitoring, metrics, and reporting cadences to measure Zero Trust maturity and control effectiveness.

### 1.2 Scope

#### 1.2.1 In Scope
This SOP applies to all Meridian Health Technologies personnel, contractors, consultants, third-party service providers, and automated service accounts that access, manage, or interact with:

- **Corporate Network Assets:** Endpoints, servers, and infrastructure within Meridian’s Boston headquarters, London, Berlin, Singapore, and Toronto offices.
- **Cloud Production Environments:** AWS (us-east-1, eu-west-1) hosting the Meridian SaaS Platform, Clinical AI Platform, HealthPay Financial Services, and MedInsight Analytics. Azure disaster recovery (DR) environments.
- **Data Assets:** All PHI, personally identifiable information (PII), financial transaction data, model parameters, training datasets, and intellectual property stored in Snowflake, PostgreSQL, Redis, Apache Kafka, Pinecone vector databases, and S3 data lakes.
- **Application Workloads:** Containerized microservices running on Amazon EKS, Lambda serverless functions, SageMaker training pipelines, and Kubeflow orchestration layers.
- **Endpoints:** All Meridian-managed laptops, workstations, mobile devices, and IoT sensors used in clinical integration testing environments.
- **Third-Party Access:** Any vendor or partner connectivity into Meridian environments, including API integrations with hospital EHR systems, payer claims systems, and cloud service provider management planes.

#### 1.2.2 Out of Scope
- Physical security controls for datacenter cages (managed under SOP-PHYS-005). However, logical controls for physical access management systems that reside on the network are in scope.
- Patient-facing mobile application security (managed under SOP-SDLC-012).
- End-user device procurement and asset tagging (managed under SOP-ITOP-003), though device compliance posture assessment before network access is in scope.

### 1.3 Applicability
All Meridian business units—Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform—must comply with this SOP. Deviation is permitted only through the formal exception process defined in Section 8.

---

## 2. Definitions and Acronyms

| Acronym / Term | Definition |
|----------------|------------|
| **ZTA / ZTNA** | Zero Trust Architecture / Zero Trust Network Architecture. A security model that assumes no implicit trust based on physical or network location. |
| **PEP** | Policy Enforcement Point. The component in the Zero Trust architecture that intercepts access requests and enforces policy decisions. Implemented via service mesh sidecars (Istio/Envoy), API gateways (Kong), and identity-aware proxies. |
| **PDP** | Policy Decision Point. The logical component that evaluates access requests against identity, device posture, and contextual signals to produce an allow/deny decision. Implemented via Okta, Open Policy Agent (OPA), and AWS IAM/Verified Permissions. |
| **PIP** | Policy Information Point. Sources of truth for attributes used in access decisions: identity stores (Okta Universal Directory), device management (CrowdStrike Falcon), vulnerability management (Wiz), and asset inventory (ServiceNow CMDB). |
| **IdP** | Identity Provider. Okta is Meridian’s primary IdP, federated with AWS IAM Identity Center and Azure AD for DR. |
| **MFA** | Multi-Factor Authentication. Required for all human access to Meridian resources. Phishing-resistant MFA (FIDO2/WebAuthn) mandated for privileged roles. |
| **PHI** | Protected Health Information, as defined by HIPAA. |
| **PII** | Personally Identifiable Information. |
| **EKS** | Amazon Elastic Kubernetes Service. Meridian’s primary container orchestration platform. |
| **SASE** | Secure Access Service Edge. Converged network and security capabilities delivered via cloud-native architecture. Currently under phased rollout. |
| **CASB** | Cloud Access Security Broker. Enforces security policy for sanctioned SaaS applications (e.g., Snowflake, ServiceNow). |
| **DLP** | Data Loss Prevention. Controls to detect and prevent unauthorized exfiltration of sensitive data. |
| **SOAR** | Security Orchestration, Automation, and Response. Palo Alto XSOAR platform used for automated incident response playbooks. |
| **ePHI** | Electronic Protected Health Information. |
| **SR 11-7** | Federal Reserve / OCC guidance on model risk management, applicable to HealthPay credit scoring and fraud detection models. |

---

## 3. Roles and Responsibilities

The following RACI matrix defines accountability and responsibility for Zero Trust controls. Specific named roles from Meridian’s organizational structure are identified.

| Activity / Control Area | Responsible (Doer) | Accountable (Owner) | Consulted (Advisor) | Informed (Stakeholder) |
|---|---|---|---|---|
| **Overall Zero Trust Strategy & Architecture** | David Park, VP of Engineering | Rachel Kim, CISO | Dr. Marcus Rivera, Chief AI Officer; Robert Liu, VP of Financial Services | Dr. Sarah Chen, CEO; Board AI Governance Committee |
| **Identity & Access Policy Definition** | IAM Engineering Team (IT Operations) | Rachel Kim, CISO | Dr. Klaus Weber, CPO/DPO; Thomas Anderson, CCO | Data Governance Council |
| **Micro-Segmentation Policy Implementation** | Cloud Security Engineering (Security Team) | David Park, VP of Engineering | Samantha Torres, VP of IT Operations | Robert Liu, VP of Financial Services; Dr. Aisha Okafor, VP Clinical AI |
| **Device Trust & Endpoint Compliance** | Endpoint Engineering (IT Operations) | Samantha Torres, VP of IT Operations | Rachel Kim, CISO | Jennifer Walsh, CHRO (for policy enforcement on employee devices) |
| **Clinical AI Model Access Governance** | MLOps Team (Engineering / AI) | Dr. Marcus Rivera, Chief AI Officer | Rachel Kim, CISO; Dr. Priya Patel, CMO | Dr. Sarah Chen, CEO |
| **HealthPay Transaction Segmentation** | FinTech Security Engineering | Robert Liu, VP of Financial Services | Rachel Kim, CISO; Thomas Anderson, CCO | James Thornton, CFO |
| **Continuous Monitoring & Metrics Dashboard** | SOC Analysts; Observability Engineering | Rachel Kim, CISO | David Park, VP of Engineering | Board Audit Committee |
| **Exception Review & Approval** | Exception Requester | Rachel Kim, CISO (for security exceptions); Dr. Marcus Rivera (for AI workload exceptions) | Thomas Anderson, CCO; Maria Gonzalez, General Counsel | Relevant VP of Business Unit |
| **Data Classification & Labeling** | Data Owners (Application Teams) | Dr. Klaus Weber, CPO / DPO | Rachel Kim, CISO | All Employees |
| **SOC 2 / HIPAA Control Validation** | Internal Audit | Thomas Anderson, CCO | Rachel Kim, CISO | External Auditors; Board Audit Committee |
| **Incident Response for ZT Bypass Attempts** | CIRT (Computer Incident Response Team) | Rachel Kim, CISO | David Park, VP of Engineering; Maria Gonzalez, General Counsel | Dr. Sarah Chen, CEO |

---

## 4. Policy Statements

### 4.1 Foundational Zero Trust Principles

1.  **No Implicit Trust Based on Network Location:** Meridian will not consider a request as inherently trusted solely because it originates from a corporate office IP range, a specific VPC CIDR block, or a VPN concentrator.
2.  **Identity-Centric Security:** Every access decision must be based on strongly authenticated and authorized identity, verified device compliance posture, and the sensitivity classification of the requested resource. Guest, vendor, and service accounts must be subjected to identical scrutiny.
3.  **Least Privilege Access:** Access rights must be provisioned with the minimum set of permissions necessary to perform the defined task. Just-in-time (JIT) access elevation must be implemented for all privileged roles across AWS, Kubernetes, and Snowflake environments.
4.  **Micro-Segmentation:** Network communications between all workloads—including pod-to-pod, pod-to-service, and service-to-database—must be explicitly authorized via deny-by-default policies. Segmentation must extend to cloud-native constructs, not depend solely on traditional subnet or security group boundaries.
5.  **Continuous Verification:** Trust is ephemeral. Access sessions must be continuously re-evaluated based on changes in user risk score, device health drift, anomalous behavior detection, and data sensitivity context. Access may be revoked in real time without session disruption awareness by the end user.
6.  **Assume Breach:** The architecture must be designed to minimize blast radius through isolation, limit lateral movement through segmentation, and render exfiltrated data unusable through encryption (TLS 1.3 in transit; AES-256-GCM at rest with Meridian-managed keys in AWS KMS).

### 4.2 Policy Commitments for Protected Health Information (PHI)
In compliance with HIPAA 45 CFR § 164.312(a)(1) (Access Controls) and 45 CFR § 164.312(b) (Audit Controls), Meridian commits to the following:

1.  **PHI-Designated Data Domains:** All systems storing or processing PHI—including MedInsight Analytics data lakes, Clinical AI Platform model inference logs containing ePHI, and HealthPay claims data stores—must reside within dedicated, strictly micro-segmented AWS security groups with no direct internet ingress.
2.  **Unique User Identification:** 45 CFR § 164.312(a)(2)(i). Every user accessing systems containing PHI must have a uniquely identifiable account; shared accounts are prohibited.
3.  **Emergency Access Procedure:** 45 CFR § 164.312(a)(2)(ii). A break-glass emergency access procedure must exist for PHI systems. Activation of break-glass accounts triggers immediate, high-severity alerting to the CISO and CPO via PagerDuty and SOAR.
4.  **PHI Access Audit Logging:** All access to, modification of, and deletion of ePHI must generate immutable audit records retained for a minimum of six (6) years, per HIPAA document retention requirements. Audit logs must be centralized in Meridian’s SIEM (Splunk Cloud) and monitored for anomalous PHI access volumes via defined correlation rules.
5.  **Encryption of ePHI at Rest:** 45 CFR § 164.312(a)(2)(iv). ePHI stored in Snowflake, S3, EBS volumes, or RDS instances must be encrypted using Meridian-managed CMKs in AWS KMS with automatic annual key rotation.
6.  **Data Integrity Controls:** 45 CFR § 164.312(c)(1). Cryptographic checksums and WORM (Write Once Read Many) policies on S3 buckets for PHI audit logs must be implemented to safeguard data integrity.

### 4.3 SOC 2 Availability Commitments
Meridian’s Meridian SaaS Platform shall be architected to maintain high availability through multi-AZ deployments, auto-scaling groups, and redundant policy enforcement points. Disaster recovery environments in Azure are maintained with documented failover procedures. This SOP defines the controls, but does not quantify specific recovery time objectives (RTO) or recovery point objectives (RPO), which are addressed in business continuity planning documents.

### 4.4 SOC 2 Logical Access Controls
Access to the Meridian SaaS Platform production environments is restricted to uniquely identified, authenticated, and authorized individuals. Access provisioning, modification, and deprovisioning follow the identity lifecycle management process defined in SOP-IAM-005. Access rights are assigned based on job function. This policy defines the initial assignment and revocation controls, but periodic formal access entitlement reviews are governed separately.

### 4.5 AI-Specific Zero Trust
Given the EU AI Act classification of Clinical AI Platform as high-risk AI, the following additional policy commitments apply:
1.  **Model Integrity:** All machine learning model binaries, training scripts, and hyperparameter configurations must be stored in immutable, versioned repositories (AWS ECR, MLflow Model Registry) with strictly controlled write access limited to the MLOps service account.
2.  **Training Data Isolation:** PHI datasets used for model training must be logically separated from development datasets. Access to training PHI requires approval from the Chief Medical Officer and CPO.
3.  **Inference Pipeline Segmentation:** Real-time model inference endpoints must be deployed in isolated Kubernetes namespaces with network policies restricting egress to only the approved data sources and ingress only from the clinical application layer.

---

## 5. Detailed Procedures

### 5.1 Identity-Centric Access Enforcement

All access to Meridian resources proceeds through a standardized control flow: Identification → Authentication → Authorization → Continuous Session Validation.

#### 5.1.1 User Authentication Flow
**Step 1: Endpoint Identity and Compliance Check**
- User attempts to access any Meridian managed application (e.g., Jira, AWS Management Console, EKS Cluster).
- The Meridian-managed endpoint’s CrowdStrike Falcon agent reports device posture to the Okta Identity Engine via a device trust integration.
- Criteria evaluated: OS version within approved patch window (≤30 days), CrowdStrike sensor operational, disk encryption enabled (FileVault/BitLocker), no active high/critical vulnerability detections.
- If device posture is non-compliant: access is blocked; user redirected to a remediation portal with specific instructions (e.g., “Update macOS to version ≥14.1”).

**Step 2: Primary Authentication**
- User redirected to Okta sign-in widget.
- Username (UPN format) and password required.
- Multi-factor authentication enforced:
    - Standard workforce: Okta Verify push notification or time-based one-time password (TOTP).
    - Privileged IT/Engineering roles, C-suite, and all users accessing PHI environments: FIDO2 WebAuthn security key (YubiKey 5 Series) required. Phishing-resistant MFA is non-negotiable for these roles.

**Step 3: Authorization & Policy Decision**
- Upon successful MFA, Okta generates a SAML 2.0 or OIDC assertion containing user attributes (department, role, clearances).
- The Policy Enforcement Point (e.g., AWS IAM Identity Center, Istio Ingress Gateway, Kong API Gateway) intercepts the request and calls the Policy Decision Point.
- PDP evaluates against Open Policy Agent (OPA) policies stored in a Git repository. Example OPA policy fragment for PHI access:

```rego
package meridian.phi.access

default allow = false

allow {
    input.method == "GET"
    input.identity.clearance_level == "PHI_ACCESS"
    input.identity.mfa_type == "FIDO2"
    input.context.device_encrypted == true
    input.resource.data_classification == "PHI"
    time.now_ns() < input.context.session_expiry
}
```

**Step 4: Session Establishment with Time-Bound Tokens**
- PDP returns a signed JWT or macaroon-based capability token.
- Maximum session lifetime: 12 hours for standard users; 4 hours for privileged users accessing production.
- Token includes: `sub`, `iat`, `exp`, `groups`, `allowed_endpoints`, `device_fingerprint`.
- The PEP caches the PDP decision locally (with a 3-minute TTL) to maintain resilience.

**Step 5: Continuous Session Validation**
- During active session, a sidecar proxy (Envoy in each EKS pod; Okta agent on EC2 hosts) continuously streams telemetry to the PDP/SIEM.
- If CrowdStrike reports a sudden endpoint health status change (e.g., malware detection, firewall deactivation), the PDP pushes a Session Revocation message via a Kafka topic (`session.revocation`) consumed by all PEPs, which immediately invalidate the session.

### 5.2 Micro-Segmentation Implementation

Micro-segmentation is implemented at three layers: Cloud Control Plane (AWS Account/VPC), Container Orchestration (Kubernetes Network Policies), and Host-Based (Security Groups and Endpoint Agents).

#### 5.2.1 AWS Account-Level Segmentation
- Meridian uses a multi-account AWS Organizations structure.
- **Production Account:** Hosts all production workloads, segregated further by product line using dedicated VPCs:
    - `vpc-prod-clinical-ai` (CIDR 10.100.0.0/16)
    - `vpc-prod-healthpay` (CIDR 10.200.0.0/16)
    - `vpc-prod-medinsight` (CIDR 10.300.0.0/16)
    - `vpc-prod-saas-shared` (CIDR 10.400.0.0/16)
- VPC Peering connections are prohibited by a Service Control Policy (SCP). Cross-VPC traffic must transit through a centralized AWS Transit Gateway, which enforces route table isolation and AWS Network Firewall inspection. All traffic crossing VPC boundaries is inspected for PHI patterns using integrated DLP rules.
- **Non-Production Account:** Dev, Test, Staging. No non-production system may communicate with production accounts. An SCP denies `sts:*` cross-account role assumption from non-production to production.

#### 5.2.2 Kubernetes Network Policies (Service Mesh)
- All application microservices run on Amazon EKS within service mesh (Istio ambient mesh).
- **Step-by-step workload onboarding:**
    1.  Application team submits a Service Access Request via ServiceNow catalog. Requestor specifies namespaces, source workload labels, destination services/databases, and required protocols/ports (e.g., TCP/5432 to PostgreSQL).
    2.  Cloud Security Engineering reviews the request, validates least privilege, and develops a Kubernetes `CiliumNetworkPolicy` deny-by-default manifest.
    3.  Example manifest:
        ```yaml
        apiVersion: cilium.io/v2
        kind: CiliumNetworkPolicy
        metadata:
          name: medinsight-api-to-phi-db
          namespace: medinsight-prod
        spec:
          endpointSelector:
            matchLabels:
              app: medinsight-api
          egress:
          - toEndpoints:
            - matchLabels:
                app: postgres-phi-cluster
            toPorts:
            - ports:
              - port: "5432"
                protocol: TCP
          ingress:
          - fromEndpoints:
            - matchLabels:
                app: medinsight-frontend
        ```
    4.  Policy is committed to the Git repository `infra/k8s-netpols` and applied via ArgoCD.
    5.  A mandatory 24-hour monitoring period in “audit mode” logs all potential blocks before enforcement mode is enabled, preventing business disruption.
- **Default posture:** All communication between namespaces is denied. All pod-to-internet egress is denied by default; pods requiring egress must use a centrally managed egress gateway with explicit allowlisting of FQDNs.

#### 5.2.3 HealthPay SR 11-7 Segmentation
The HealthPay Financial Services model ecosystem—credit scoring, fraud detection, and lending—operates in a dedicated, highly restricted segment:
- These models and their supporting data stores exist in dedicated subnets within `vpc-prod-healthpay`, with zero inbound internet or cross-VPC access.
- Access for model tuning is permitted only from dedicated, bastion-like developer jump hosts that are ephemeral, FIPS 140-2 validated, and require multi-person approval via ServiceNow change control. All commands executed within these environments during model tuning sessions are captured via AWS Systems Manager Session Manager and piped to SIEM.

### 5.3 AI Pipeline Zero Trust Controls

#### 5.3.1 Model Registry and Artifact Integrity
1.  **CI/CD Pipeline (GitLab CI):** Only code merged with mandatory peer review (min 2 approvals, one from ML Engineering Lead) triggers model build.
2.  **Build Phase:** Models are trained in ephemeral, air-gapped SageMaker environments with no outbound internet. The training orchestrator (Kubeflow Pipelines) generates a cryptographic hash (SHA-256) of the final model artifact (`.pth` or `.pb` file) and attests to its provenance (training pipeline link, training dataset checksum, hyperparameters).
3.  **Registry:** The model binary, along with the signed metadata (in-toto attestation format), is pushed to MLflow Model Registry (backend: S3 bucket `meridian-models-prod`).
4.  **Deployment Gate:** Production deployment of a new model version requires approval from the Chief AI Officer or VP of Clinical AI Products. The approval is logged as a ServiceNow change record with linkage to the model artifact SHA-256, ensuring only approved binaries reach production inference endpoints.
5.  **Runtime Verification:** Before a deployed model pod serves traffic, an Istio sidecar validates the model artifact’s SHA-256 against the approved record in MLflow. If mismatch is detected, pod is labeled `unhealthy`, and traffic is not routed.

### 5.4 Patient Data Access for MedInsight Analytics
Researchers and data analysts accessing the de-identified or limited data sets within MedInsight must follow a step-up authentication procedure:

1.  **Access Request:** User submits access request through Meridian’s ServiceNow portal, specifying purpose, dataset scope, and duration. Request auto-routed to Dr. Klaus Weber (CPO/DPO) for Privacy Impact Assessment.
2.  **Mandatory Training Validation:** System checks ServiceNow’s LMS integration to confirm completion of HIPAA Privacy & Security Awareness (SOP-TRN-004) and “Responsible AI & PHI Handling” (SOP-TRN-012) within the last 12 months. If expired, request is auto-rejected with a notification to retrain.
3.  **Dynamic Credential Issuance:** Upon approval, the analyst does not receive static database credentials. HashiCorp Vault dynamically generates ephemeral, read-only PostgreSQL credentials with a 2-hour TTL, scoped to only the approved schemas/tables.
4.  **Session Monitoring:** All Snowflake/PostgreSQL queries executed by the analyst are routed through a proxy that logs the query text and EXPLAIN plan to Splunk. A DLP rule scans for SQL patterns attempting to join PHI datasets with unapproved external tables or large-scale data extraction (e.g., `SELECT * LIMIT > 10000`).

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control ID | Control Name | Description | Implementation | Scope |
|---|---|---|---|---|
| **ZT-TC-01** | Phishing-Resistant MFA | FIDO2/WebAuthn required for all privileged access. | Okta Policy: “Admin Roles,” “Production Access,” “C-Suite” → “Security Key Required.” Push/Authy not permitted. | All privileged roles; PHI access. |
| **ZT-TC-02** | Device Trust Enforcement | Block non-compliant endpoints from Okta-sign-on. | Okta Device Trust integrated with CrowdStrike Falcon. OS version, encryption, AV status checked. Non-compliant → Blocked with remediation message. | All corporately managed endpoints. |
| **ZT-TC-03** | Just-in-Time Access | Permanent privileged access to AWS/Snowflake/K8s is prohibited. | AWS IAM Identity Center → Permission sets require approval in ServiceNow; temporary (max 4 hours) access provisioned. | AWS management; Snowflake `ACCOUNTADMIN` role; EKS cluster admin. |
| **ZT-TC-04** | Kubernetes Network Micro-Segmentation | `CiliumNetworkPolicy` deny-by-default between pods and namespaces. | Istio ambient mesh. Policies as code in Git, enforced by ArgoCD. Mandatory 24hr audit mode before enforcement. | All production EKS clusters; Non-production clusters where ePHI testing data is used. |
| **ZT-TC-05** | AWS VPC Isolation with DLP Inspection | Cross-VPC traffic only via Transit Gateway with deep packet inspection. | AWS Transit Gateway with AWS Network Firewall. Stateful DLP rules alert/block on PHI pattern `\b[3][0-9]{2}-[0-9]{2}-[0-9]{4}\b` (SSN-like) moving from PHI to non-PHI VPC. | All production VPCs. |
| **ZT-TC-06** | Immutable ePHI Audit Logs | Audit logs containing ePHI access records must be append-only, non-repudiable. | S3 bucket (`meridian-audit-logs-prod`) with S3 Object Lock in Governance Mode. Retention: 6 years. Log shipping via Kinesis Firehose with integrity checking. | All PHI systems; SIEM. |
| **ZT-TC-07** | Egress Gateway Enforcement | Pod internet access blocked by default. Controlled egress via FQDN filtering. | Istio Egress Gateway with a deny-all policy. Allowed list of FQDNs (e.g., `*.snowflakecomputing.com`, `api.sagemaker.us-east-1.amazonaws.com`) maintained and reviewed monthly. | All non-internet-facing production pods. |
| **ZT-TC-08** | ML Model Provenance & Integrity | Attestation of model training origin; cryptographic validation at deployment. | in-toto attestations generated by Kubeflow Pipelines; SHA-256 verification by Istio init-container. Model artifact immutability enforced by S3 Object Lock. | AI/ML pipelines. |
| **ZT-TC-09** | Dynamic Database Credentials | No static DB user passwords for MedInsight analysts. | HashiCorp Vault dynamic secrets engine for PostgreSQL/Snowflake. Max TTL: 2 hours. SQL proxy logs all queries. | MedInsight databases. |
| **ZT-TC-10** | Break-Glass Emergency Account | Emergency access account for PHI systems; triggers immediate high-severity alert. | Emergency account stored in a physical, sealed safe in CISO office; digital copy in a break-glass CyberArk vault with dual-person retrieval. Any login triggers Splunk alert: “CRITICAL - PHI EMERGENCY ACCOUNT ACTIVATED.” | All PHI systems. |

### 6.2 HIPAA Administrative Safeguards

| HIPAA Citation | Required Safeguard | Meridian Implementation |
|---|---|---|
| **45 CFR § 164.308(a)(1)(ii)(A)** | Risk Analysis | Comprehensive Zero Trust gap analysis conducted biannually by CISO and external assessor. Output: Risk Register in ServiceNow GRC. |
| **45 CFR § 164.308(a)(3)(ii)(A)** | Workforce Security: Authorization/Supervision | All PHI system access governed by identity lifecycle (SOP-IAM-005) and Zero Trust PDP policies outlined in Section 5.1. |
| **45 CFR § 164.308(a)(5)(ii)(C)** | Access Termination | Deprovisioning procedures integrated into Okta; terminations trigger automated suspension within 1 hour of HRIS update (Workday). Automated task confirmation logged in SIEM. |
| **45 CFR § 164.312(b) (Audit Controls)** | Hardware, software, procedural mechanisms that record and examine activity | Splunk Cloud audit indexing for all PHI resource interactions; AWS CloudTrail for all AWS API calls; EKS audit logs for `kubectl exec` into PHI pods. Dashboards reviewed daily by SOC. |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)
The Zero Trust program’s operational health is measured against the following metrics, tracked in CISO’s monthly dashboard (Splunk dashboard `ZTNA-Executive`).

| Metric ID | Metric | Target | Measurement Method | Reporting Cadence |
|---|---|---|---|---|
| **ZT-M-01** | % Human Access Events with MFA Success | **≥ 99.95%** | (Successful MFA authentications / Total MFA authentication attempts) across Okta. | Daily monitoring; Monthly report to CISO. |
| **ZT-M-02** | FIDO2 Adoption Rate for Privileged Accounts | **100%** | Count of privileged Okta users with FIDO2 assigned vs. using non-phishing-resistant MFA. Non-compliance → immediate PagerDuty alert to IAM team. | Continuous; Weekly confirmation. |
| **ZT-M-03** | Endpoint Compliance Block Rate | **< 2%** of all endpoint access attempts | Count of access attempts blocked due to device posture / Total attempts. A sustained >2% indicates poor patch/update compliance. | Weekly review with Samantha Torres, VP IT Ops. |
| **ZT-M-04** | Unauthorized Cross-Segment Network Traffic | **Zero** | Cilium/Transit Gateway logs indicating DROP events for traffic not matching any policy. Analyzed by SOAR playbook. | Real-time alerting; Weekly trend report. |
| **ZT-M-05** | JIT Access Privilege Elevation Turnaround | **≤ 5 mins** from ServiceNow approval | Duration from ServiceNow approval timestamp to AWS permission set being available. | Monthly report. |
| **ZT-M-06** | Expired/Orphaned Service Accounts** | **Zero** in production | Automated scan (AWS Config Rule, CrowdStrike Falcon Discover) for IAM keys/user accounts with `PASSWORD_LAST_USED > 90 days`. Auto-remediation to suspend account. | Real-time alerting; Monthly clean-up certification. |
| **ZT-M-07** | PHI Audit Log Anomaly Investigation | **< 15 min** MTTR (Mean Time to Respond) | Time from Splunk correlation alert on anomalous PHI access (e.g., volume spike, after-hours PHI access) to SOC analyst acknowledging investigation. | CIRT review daily; Monthly CISO Report. |

### 7.2 Reporting Cadences
- **Real-time / Near Real-time:** Critical PagerDuty alerts for emergency account activation, FIDO2 bypass attempts for privileged users, and Traffic Anomaly `ZT-M-04 > 0` are dispatched immediately to the CIRT on-call rotation.
- **Daily SOC Stand-up:** SOC lead reviews the past 24 hours of Splunk notable events tagged “ZTNA.”
- **Weekly:** IAM Engineering Lead provides a report on privileged account MFA posture (ZT-M-02) to the CISO.
- **Monthly:** CISO presents the consolidated ZTNA KPIs dashboard to the C-suite and Board Audit Committee as part of the Information Security Monthly Status Report.
- **Quarterly:** Full Zero Trust Maturity Model self-assessment conducted by CISO and VP of Engineering, benchmarked against NIST SP 800-207. Results filed in ServiceNow GRC and reviewed with the Board AI and Cybersecurity Committee.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Process
Zero Trust policy exceptions are recognized as a high-risk activity. The exception process is rigid and time-bound.

1.  **Submission:** Requester (an employee’s manager or an application team Technical Lead) submits a “Zero Trust Policy Exception” via the ServiceNow GRC module. The submission must include:
    - Specific ZT control ID being excepted (e.g., `ZT-TC-04`, `ZT-TC-01`).
    - Technical justification and a detailed description of compensating controls.
    - Scope (specific user, group, source CIDR, workload).
    - Business justification (what capability is blocked without this exception).
    - Proposed duration (maximum 90 days).
2.  **Risk Assessment:** Cloud Security Engineering performs a risk and impact analysis, documenting the likely blast radius if the excepted resource is compromised.
3.  **CPO Review (If PHI):** If the exception pertains to a system within the PHI scope boundary, Dr. Klaus Weber, Chief Privacy Officer, must review and approve the assessment for HIPAA compliance.
4.  **Approval:**
    - **Non-prod technical exceptions:** Approved by David Park, VP of Engineering.
    - **Production security policy exceptions (including MFA/segmentation):** Approved by Rachel Kim, CISO.
    - **Any exception impacting clinical AI training/inference data integrity:** Approved by Dr. Marcus Rivera, Chief AI Officer, with notification to Rachel Kim, CISO.
5.  **Implementation:** Upon approval, the GRC team creates a time-bound ServiceNow change ticket. Engineering implements the exception (e.g., a specific permissive Istio `AuthorizationPolicy`). The ticket is linked to the policy artifact in Git (`exceptions/*.yaml`).
6.  **Expiry and Auto-Rollback:** An automated control reviews the `exceptions/*.yaml` directory daily. On the assigned expiry date, a CI/CD job in GitLab automatically opens a PR to remove the exception file. A “Auto-Removal” ServiceNow task is assigned to the original approver. If no action taken in 48 hours, the approved PR is merged automatically, restoring the Zero Trust baseline.

### 8.2 Emergency Access Escalation
In a production-down incident where standard JIT access workflows are unavailable or non-functional, the on-call Incident Commander (IC) may request activation of the Break-Glass Procedure (ZT-TC-10).

1.  IC verbally contacts Rachel Kim, CISO (or deputy CISO), and states the emergency.
2.  CISO or deputy retrieves the emergency CyberArk safe credentials, requiring a second SOC manager approval.
3.  Account credentials are injected into the IC’s temporary session. The act of accessing the CyberArk safe and using the credentials is logged. An immediate Splunk alert is triggered.
4.  A post-incident review within 24 hours is mandatory. The review, attended by CISO and IC, will document the failure that led to needing the emergency account and must create remediation plans to ensure the standard JIT process is hardened. Permanent use of emergency accounts is prohibited.

---

## 9. Training Requirements

### 9.1 Role-Based Training
All personnel interacting with the Meridian Zero Trust ecosystem must complete training commensurate with their access level and responsibilities.

| Target Audience | Required Training Module(s) | Training Platform | Frequency | Tracking |
|---|---|---|---|---|
| **All Meridian Employees & Contractors** | “Zero Trust & You: The Endpoint is the Perimeter” (45 min) | Meridian LMS (Litmos) | Annually | Mandatory; tracked via LMS; non-compliance → endpoint network access restricted via Okta Device Trust enrollment group removal. |
| **Engineering & DevOps** | “Building for Zero Trust: Micro-Segmentation, Istio, & OPA Policy Authoring” (4 hr) + mandatory capture-the-flag (CTF) lab | Meridian LMS + Internal CTF Platform | Annually; CTF lab must be completed with ≥80% score. | LMS; lab scores tracked. Failure → repeat CTF within 30 days. |
| **IT Operations & Service Desk** | “Identity-Centric Access Management & JIT Provisioning” (2 hr) | Meridian LMS | Annually | LMS; non-completion flagged in ServiceNow profile, auto-removed from Okta “ServiceDesk” group until completed. |
| **All Employees Accessing PHI** | “HIPAA Privacy & PHI Data Handling in a Zero Trust Environment” (SOP-TRN-004) + “Responsible AI & PHI Handling” (SOP-TRN-012) | Meridian LMS | Mandated every 12 months. (System enforced in procedure 5.4, Step 2). | LMS; auto-provisioning systems gated on completion status. |
| **Vendors & Third Parties** | Vendor security awareness module, including Meridian ZT requirements for VPN-less access and MFA. | Meridian Third-Party Risk Management Portal (ProcessUnity) | Contract initiation and annually thereafter. | Compliance managed by Vendor Risk Management team; non-compliance → VPN termination via a firewall rule change. |

### 9.3 Phishing Simulation & MFA Hygiene
Given the central role of phishing-resistant MFA, all users will be subject to quarterly phishing simulations. Any user who fails two or more simulations in a 12-month period will be required to attend mandatory, in-person, 2-hour security awareness remedial training and will be forcibly enrolled in FIDO2 MFA for all system access irrespective of role.

---

## 10. Related Policies and References

### 10.1 Meridian Internal SOPs

| SOP ID | Document Title | Relationship |
|---|---|---|
| **SOP-IAM-005** | Identity and Access Management Lifecycle | Defines the user provisioning, deprovisioning, and credential lifecycle that ZTNA enforces. |
| **SOP-ISEC-003** | Incident Response Plan | Governs the CIRT process for ZT bypass attempts and breach containment. |
| **SOP-SDLC-012** | Secure Software Development Lifecycle | Ensures new applications and microservices are built with ZT principles (e.g., OPA policy testing in CI). |
| **SOP-DATA-001** | Data Classification and Handling | Defines data sensitivity classes (PHI, PII, PCI, Internal) referenced in micro-segmentation and DLP rules. |
| **SOP-VRM-007** | Vendor Access Management | Governs the lifecycle of third-party identity and access, extending ZT to external entities. |
| **SOP-TRN-004** | HIPAA Privacy & Security Awareness Training | Specifies HIPAA training requirements enforced by this SOP. |
| **SOP-TRN-012** | Responsible AI & PHI Data Handling | Required training for MedInsight analyst access (referenced in procedure 5.4). |
| **SOP-AI-022** | Model Risk Management | Defines model risk tiers and governance for SR 11-7 applicable models; cross-referenced for AI segmentation controls. |
| **SOP-BCP-010** | Business Continuity and IT Disaster Recovery Planning | Addresses overall failover strategies to Azure DR; this SOP defines the network access controls within those environments. |

### 10.2 External Standards and Regulations

- **NIST SP 800-207:** Zero Trust Architecture (August 2020). Foundational document for Meridian’s approach.
- **NIST SP 800-53 Rev. 5:** Security and Privacy Controls for Information Systems and Organizations (Access Control family (AC), Identification and Authentication (IA)).
- **CISA Zero Trust Maturity Model:** Version 2.0 (April 2023). Used for Meridian’s quarterly maturity self-assessment.
- **HIPAA Security Rule:** 45 CFR Part 164, Subpart C.
- **SOC 2 TSC 2017:** Common Criteria (CC6 series for logical and physical access controls; CC7 series for system operations).
- **FFIEC / OCC SR 11-7:** Model Risk Management, applied to HealthPay segmentation design.

---

## 11. Revision History

| Version | Date | Author(s) | Summary of Changes |
|---|---|---|---|
| **1.0** | 2021-03-15 | Michael Torres, Senior Security Architect | Initial draft based on NIST SP 800-207. Foundational ZT principles established. |
| **1.5** | 2022-06-22 | Rachel Kim, CISO | Minor revision. Expanded roles and responsibilities to include newly appointed Chief AI Officer role. Added initial AI pipeline principles ahead of EU AI Act alignment. |
| **2.0** | 2023-09-10 | David Park, VP Eng; Sarah Jensen, CloudSec Lead | Major revision. Added full Kubernetes micro-segmentation procedures with Istio ambient mesh; Integrated CrowdStrike/Okta Device Trust enforcement; Detailed ePHI controls added per external audit recommendations. |
| **2.3** | 2024-02-18 | Rachel Kim, CISO; Legal/Privacy (Dr. Klaus Weber) | Integrated privacy review feedback. Added explicit break-glass procedure (ZT-TC-10). Expanded MedInsight procedure 5.4 with mandatory training pre-check. |
| **2.4** | 2024-07-08 | Sarah Jensen, CloudSec Lead | Updated OPA policy examples; Added FIDO2 mandate for PHI access following internal penetration test finding; Clarified GitOps workflow for network policies. |
| **2.5** | 2024-10-05 | Rachel Kim, CISO | Aligned monitoring metrics and HIPAA Section 6.2 safeguards with recent AICPA SOC 2 Type II audit feedback. Version 2.5 was the version provided to auditors. |
| **2.6** | 2024-11-20 | Rachel Kim, CISO; Thomas Anderson, CCO | Current version. Revised exception handling process (Section 8) to mandate auto-rollback CI/CD and formal Risk Dossier requirement. Updated related SOP cross-references. Clarified SOC 2 Availability & Logical Access sections. Approved by CEO for immediate rollout. |

---

**APPROVED BY:**

**Dr. Sarah Chen, Chief Executive Officer**
*Signature on File in ServiceNow Policy Management Record*
Approval Date: 2024-11-19

**Rachel Kim, Chief Information Security Officer**
*Signature on File*
Effective Date: 2024-11-20
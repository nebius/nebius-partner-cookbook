---
sop_id: "SOP-PENG-017"
title: "Service Deprecation and Sunset"
business_unit: "Product & Engineering"
version: "1.8"
effective_date: "2025-12-17"
last_reviewed: "2026-04-24"
next_review: "2026-10-20"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Service Deprecation and Sunset

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the governance framework, operational procedures, and compliance controls for the orderly deprecation, decommissioning, and sunset of software services, application programming interfaces (APIs), product features, and integrated platform components across Meridian Health Technologies, Inc. ("Meridian"). The purpose of this SOP is to ensure that end-of-life transitions are executed in a manner that minimizes disruption to covered entities, protects the confidentiality, integrity, and availability of protected health information (PHI) and personal data, maintains regulatory compliance across all jurisdictions, and preserves the company's contractual and fiduciary obligations.

The deprecation of clinical decision support algorithms, financial services processing pipelines, and analytics platforms carries material risk due to the integration depth within customer workflows and the sensitivity of underlying data. An unstructured sunset process introduces regulatory exposure, potential for data loss, and erosion of customer trust. This SOP codifies a standardized, auditable methodology that enables Meridian to innovate and retire legacy components responsibly.

### 1.2 Scope

This SOP applies to all products, services, and components developed, deployed, or managed by Meridian Health Technologies, Inc., specifically encompassing:

| Business Unit | In-Scope Services |
|---|---|
| Clinical AI Platform | AI-driven clinical decision support tools, diagnostic imaging analysis models, patient risk scoring engines, adverse event prediction systems, model inference endpoints |
| HealthPay Financial Services | Payment processing gateways, patient financing portals, medical lending origination services, claims automation engines, credit scoring models, fraud detection services |
| MedInsight Analytics | Population health dashboards, care gap identification engines, outcomes prediction models, data export and reporting APIs |
| Shared Platform Infrastructure | Authentication services, API gateway configurations, data pipeline components, shared machine learning model registries, feature stores |

This SOP applies to internal services consumed exclusively by Meridian teams, externally-facing services consumed by customers and partners, and shared platform services that span multiple business units.

**Out of Scope:** This SOP does not govern the retirement of internal corporate IT systems (e.g., HRIS, ERP), physical hardware asset disposal (refer to SOP-IT-014 "IT Asset Disposal and Media Sanitization"), or the termination of third-party vendor contracts (refer to SOP-VM-022 "Vendor Offboarding and Contract Termination"). Emergency security vulnerability patches that require immediate service shutdown are governed by SOP-SEC-009 "Incident Response and Breach Notification."

### 1.3 Applicability

All employees, contractors, and third-party service providers involved in the development, deployment, maintenance, or support of in-scope services are bound by the provisions of this SOP. Compliance with this SOP is a condition of access to Meridian production environments and customer-facing systems.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Active Maintenance** | The standard operational state of a service during which it receives feature updates, security patches, performance improvements, and Tier 1-3 customer support. |
| **Backfill** | The process of migrating customers from a deprecated service to a designated replacement service. |
| **Customer Notification Period** | The minimum duration between the formal issuance of a deprecation notice and the execution of a code change that materially degrades or removes functionality. |
| **Data Subject** | An identified or identifiable natural person to whom personal data relates, as defined under GDPR Article 4(1). |
| **Data Controller Obligations** | Meridian's responsibilities as a data controller (for MedInsight Analytics direct customer relationships) or joint controller (for Clinical AI Platform where processing purposes are co-determined with the healthcare provider). |
| **Deprecation** | A formal declaration that a service or feature is no longer recommended for new use, will not receive non-critical enhancements, and is scheduled for eventual removal. Deprecation is a transitional state preceding sunset. |
| **End-of-Life (EOL)** | The date on which all commercial support, service-level agreements, and security update commitments permanently cease. |
| **End-of-Sale (EOS)** | The date on which a service is no longer available for provisioning to new customers or tenants. |
| **Extended Support** | An optional, billable support tier offered during the deprecation phase that provides critical bug fixes and security patches without feature enhancements. |
| **Feature Flag Deprecation Toggle** | A configuration mechanism deployed via LaunchDarkly that allows granular, user-specific disablement of deprecated functionality. |
| **Grace Period** | The operational window between EOS and EOL during which existing customers retain access but no new provisioning occurs. |
| **Legacy Data Archive** | A purpose-built, access-restricted cold storage environment where data from a sunset service is retained exclusively for compliance and litigation purposes. |
| **Migration Support Package** | A structured set of technical documentation, tooling, sandbox environments, and professional services engagement agreements provided to customers to facilitate transition away from a deprecated service. |
| **Personal Data Breach** | A breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to, personal data transmitted, stored, or otherwise processed, as defined under GDPR Article 4(12). |
| **Service Registry** | The centralized catalog of all Meridian services, maintained in Atlassian Compass, containing ownership metadata, dependency maps, compliance classifications, and lifecycle status. |
| **Sunset** | The terminal operational phase during which a service is permanently decommissioned, all supporting infrastructure is deprovisioned, and all residual data is either migrated, archived, or securely destroyed. |
| **Technical Debt Remediation** | Engineering work undertaken to eliminate architectural or code-level dependencies on a deprecated service, ensuring that internal consumers are migrated prior to external customer transitions. |
| **Tombstone Artifact** | A minimal, read-only retained record confirming the historical existence of a sunset service, comprised of the service name, lifespan dates, ownership lineage, and a pointer to the final Architecture Decision Record. |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| **ADR** | Architecture Decision Record |
| **API** | Application Programming Interface |
| **CAGR** | Compound Annual Growth Rate |
| **CCPA** | California Consumer Privacy Act |
| **CSV** | Clinical Support Validation (Meridian's clinical model evaluation framework) |
| **DPA** | Data Processing Agreement |
| **DPIA** | Data Protection Impact Assessment (GDPR Article 35) |
| **DPO** | Data Protection Officer |
| **DSAR** | Data Subject Access Request (GDPR Article 15) |
| **EOL** | End-of-Life |
| **EOS** | End-of-Sale |
| **FHIR** | Fast Healthcare Interoperability Resources |
| **HIPAA** | Health Insurance Portability and Accountability Act |
| **LTS** | Long-Term Support |
| **MTTR** | Mean Time to Resolve |
| **MDR** | Medical Device Regulation (EU) 2017/745 |
| **OKR** | Objectives and Key Results |
| **PACS** | Picture Archiving and Communication System |
| **PHI** | Protected Health Information |
| **RACI** | Responsible, Accountable, Consulted, Informed |
| **RPO** | Recovery Point Objective |
| **RTO** | Recovery Time Objective |
| **SIEM** | Security Information and Event Management |
| **SLA** | Service-Level Agreement |
| **VPC** | Virtual Private Cloud |

---

## 3. Roles and Responsibilities

### 3.1 RACI Matrix

The following Responsibility Assignment Matrix defines the participation of each role in the deprecation and sunset lifecycle. Deviations from this assignment require exception approval per Section 8.

| Activity | Service Owner (VP/Director) | Product Manager | Engineering Lead | DPO / Privacy Counsel | Customer Success | DevOps / SRE | Platform Architecture |
|---|---|---|---|---|---|---|---|
| Deprecation Business Case Approval | **A** | R | C | C | I | I | C |
| GDPR DPIA Initiation | C | C | I | **A/R** | I | I | I |
| Customer Notification (External) | I | **A** | C | R | R | I | I |
| Service Registry Status Update | R | C | **A** | I | I | R | I |
| Data Inventory & Classification | C | R | I | **A** | I | R | I |
| Migration Tooling Development | I | C | **A/R** | I | C | R | C |
| Customer Migration Execution | I | C | I | I | **A/R** | C | I |
| Legacy Data Archive Provisioning | I | C | R | R | I | **A/R** | C |
| Secure Data Destruction | I | C | I | **A** | I | R | C |
| Infrastructure Deprovisioning | I | I | R | I | I | **A/R** | C |
| Final Service Tombstone | I | R | **A** | C | I | I | R |
**Key:** R = Responsible (executes the task); A = Accountable (approves and bears ultimate accountability); C = Consulted (provides input prior to execution); I = Informed (notified after completion).

### 3.2 Named Roles and Responsibilities

#### 3.2.1 Service Owner (VP or Director-Level)

- Approves the deprecation business case, including the justification for retirement, the impact assessment on revenue and customer operations, and the resource allocation for the sunset project.
- Holds final accountability for all compliance outcomes associated with the sunset, including GDPR data retention obligations and contractual SLA adherence during the transition period.
- Escalates cross-functional blockers to the Executive Leadership Team.

#### 3.2.2 Product Manager

- Authors the customer-facing deprecation notice and migration guide.
- Manages the communication timeline with Customer Success to ensure contractual notification periods are honored.
- Defines the feature parity requirements for any designated replacement service.
- Maintains the deprecation roadmap in Productboard and ensures visibility to all internal stakeholders.

#### 3.2.3 Engineering Lead (Deprecation Execution Lead)

- Owns the technical execution plan, including dependency analysis, technical debt remediation, code removal sequencing, and feature flag management.
- Coordinates with SRE on infrastructure deprovisioning runbooks.
- Ensures all data handling procedures defined in collaboration with the DPO are executed with surgical precision.
- Maintains the sunset project tracker in Jira and reports weekly on milestone progress via the Product & Engineering metrics dashboard.

#### 3.2.4 Data Protection Officer (DPO) / Privacy Counsel

- Determines whether the sunset triggers a requirement for a Data Protection Impact Assessment (DPIA) under GDPR Article 35, particularly when the decommissioning involves novel data migration technologies or large-scale processing of special category data (health data).
- Approves the data retention and destruction plan for all personal data and PHI within the sunset service, ensuring compliance with GDPR Article 5(1)(e) (Storage Limitation) and Article 17 (Right to Erasure).
- Advises on the language of customer notifications to ensure alignment with Meridian's obligations as a data processor or joint controller under GDPR Article 28.
- Reviews and approves any data archive architecture to confirm appropriate technical and organizational measures (TOMs) for personal data at rest.

#### 3.2.5 Director of Customer Success

- Manages the outbound communication cadence to all affected customers, including segmentation by risk tier (strategic accounts, HIPAA-covered entity partners, clinical validation cohorts).
- Coordinates the delivery of Migration Support Packages, including the scheduling of professional services engagements.
- Monitors customer health scores during the transition period and escalates accounts demonstrating elevated churn risk.
- Maintains a master tracker of customer acknowledgment confirmations and opt-in/opt-out for extended support.

#### 3.2.6 DevOps / Site Reliability Engineering (SRE)

- Provisions and decommissions cloud infrastructure (AWS accounts, VPCs, Kubernetes clusters, database instances) per approved runbooks.
- Implements the Legacy Data Archive, including encryption at rest (AWS KMS CMK), access logging (AWS CloudTrail), and network isolation.
- Executes secure cryptographic erasure of data volumes, validated via Certificate of Destruction workflow.
- Updates monitoring and alerting configurations (Datadog, PagerDuty) to remove decommissioned services.

#### 3.2.7 Platform Architecture

- Reviews and approves any net-new architectural patterns introduced by replacement services to ensure they do not introduce systemic regressions.
- Maintains the Service Registry (Atlassian Compass), ensuring the sunset service is tombstoned with appropriate metadata.

---

## 4. Policy Statements

### 4.1 General Deprecation Principles

**P-001: Non-Discriminatory Deprecation.** Meridian shall not deprecate a service or feature in a manner that disproportionately impacts customers or users based on protected characteristics, clinical specialty, or geographic region unless such deprecation is demonstrably necessary to remediate a validated product safety concern or regulatory compliance obligation.

**P-002: Lifecycle Transparency.** The lifecycle status of every Meridian service shall be documented in the Service Registry (Atlassian Compass) and shall be one of: `ACTIVE`, `DEPRECATED`, `SUNSET`. No service shall transition from `ACTIVE` to `SUNSET` without passing through the `DEPRECATED` state for a minimum duration defined by its service tier.

**P-003: Mandatory Replacement Pathway.** No externally-facing service classified as a covered component under a HIPAA Business Associate Agreement (BAA) or a GDPR Data Processing Agreement (DPA) shall be deprecated unless a functionally equivalent replacement service or a customer-acceptable alternative workflow is designated and available. Services without a direct replacement must receive CEO-level exception approval (per Section 8).

### 4.2 Customer Notification and Consent

**P-004: Tiered Notification SLAs.** Customer-facing deprecation notifications shall be governed by tiered minimum notice periods based on integration complexity:

| Integration Tier | Criteria | Minimum Notice Period |
|---|---|---|
| **Tier 1: Deep Integration** | FHIR data pipeline, on-premise gateway appliance, custom-trained ML model hosting | 18 months |
| **Tier 2: Standard API** | REST/gRPC API integration, SSO/SAML authentication dependency | 12 months |
| **Tier 3: UI Feature** | Workflow step within Meridian-provided UI, reporting dashboard component, export functionality | 6 months |

Notice periods commence on the date Meridian issues formal written notice via the contractual notification channel (email to registered admin contact, notification via Meridian Admin Portal, and registered letter for Tier 1 customers). Failure to meet these minimum notice timelines constitutes a breach of this SOP and must be escalated per Section 8.

**P-005: Multi-Modal Notification.** Deprecation notices shall be delivered via no fewer than two (2) channels: the Meridian Admin Portal (in-app notification banner with forced acknowledgment click-through) and email to the registered account administrator. Tier 1 customers shall additionally receive a direct outreach from their named Customer Success Manager (CSM).

**P-006: Consent to Offboard.** For services processing personal data as a joint controller, Meridian shall obtain demonstrable acknowledgment from the customer Data Protection Officer or equivalent designated contact prior to executing a data migration to a replacement service, confirming that the migration scope has been reviewed and accepted.

### 4.3 Data Handling and Decommissioning

**P-007: Data Minimization at Sunset.** Per GDPR Article 5(1)(c) (Data Minimization), Meridian shall, at the point of service sunset, retain personal data only to the extent necessary to satisfy legal obligations, contractual warranty commitments, or active litigation holds. No data shall be retained "just in case."

**P-008: Right to Erasure Compatibility.** Sunset procedures shall be designed to guarantee that Meridian can fulfill a valid Data Subject Access Request (DSAR) for erasure (GDPR Article 17) against the Legacy Data Archive within the regulatory 30-day window. The archive architecture must support granular record deletion without compromising the integrity of other retained records.

**P-009: PHI De-identification Prior to Analytics Archive.** Where PHI is retained post-sunset for secondary research or analytics purposes, it shall be de-identified in accordance with the HIPAA Safe Harbor method (removal of all 18 identifiers) prior to ingestion into the analytics data lake. Re-identification keys shall be destroyed, rendering re-identification infeasible.

### 4.4 Financial and Contractual Integrity

**P-010: Prorated Fee Adjustments.** For customers under an active subscription where a deprecated service constitutes a material contracted deliverable, Meridian Finance shall automatically calculate and apply a prorated service credit or fee adjustment, approved by the VP of Revenue Operations, for the period between EOS and the customer's full migration to the replacement service. This shall not require customer-initiated negotiation.

---

## 5. Detailed Procedures

### 5.1 Phase 0: Strategic Assessment and Deprecation Decision

This phase establishes the business and technical justification for deprecation before any customer-facing commitments are made.

#### 5.1.1 Initiation Trigger

A deprecation assessment is triggered by any of the following:
- The Service Owner or Product Manager submits a "Service Retirement Proposal" to the Architecture Review Board (ARB).
- A security vulnerability assessment (SOP-SEC-009) identifies a fundamental architectural defect that cannot be remediated without a rewrite, rendering Active Maintenance infeasible.
- A third-party dependency critical to a service announces its own EOL.
- Quarterly product portfolio review identifies a service with negative Net Revenue Retention (NRR) and a sustainable migration pathway.

#### 5.1.2 Business Case Development (Product Manager)

The Product Manager shall prepare a Service Retirement Business Case Document containing:

1.  **Service Identification:** Service name, Service Registry ID, current lifecycle status, owner VP.
2.  **Strategic Rationale:** Narrative explaining the strategic rationale for retirement (e.g., technical debt burden $X/year, shifting market demand, regulatory obsolescence, consolidation with Service Y).
3.  **Customer Impact Analysis:**
    - Total number of active customer tenants utilizing the service.
    - Segmentation by Integration Tier (Tier 1, 2, 3 per P-004).
    - Total Annual Recurring Revenue (ARR) attributable to the service.
    - Identification of any single customer representing >20% of the service's ARR.
4.  **Designated Replacement:** Identification of the designated replacement service (internal Meridian service or a recommended third-party product and the associated partnership strategy). If no replacement exists, a detailed justification for the gap must be included.
5.  **Preliminary Migration Feasibility Assessment:** A technical assessment (authored by the Engineering Lead) confirming that data schemas, API contracts, and functional workflows can be migrated with acceptable data fidelity loss (<0.5% error rate threshold).
6.  **Proposed Timeline:** Draft milestones for EOS and EOL, subject to the minimum notice periods defined in P-004.
7.  **Resource Estimate:** Engineering-month estimate for internal technical debt remediation, development of migration tooling, and the decommissioning process itself.

#### 5.1.3 DPIA Screening (DPO)

Upon receipt of the business case draft, the DPO shall execute a GDPR Article 35 DPIA screening questionnaire via the OneTrust platform. A full DPIA is mandatory if the sunset process involves:

- Large-scale processing of special category data (health data, genetic data) during the migration or archival phase.
- Systematic and extensive profiling of data subjects (e.g., a Clinical AI risk scoring model that profiles patients).
- Use of a new technology (e.g., a novel data anonymization algorithm) in the migration or archival pipeline.

The DPO shall provide a written DPIA screening determination (Required / Not Required) within 10 business days. If Required, the DPIA must be completed and approved BEFORE any Phase 1 customer notification is issued.

#### 5.1.4 Approval Gates

| Gate | Approver(s) |
|---|---|
| 1. Product & Engineering Alignment | David Park, VP of Engineering; Business Unit Product VP |
| 2. Financial Impact | VP of Finance (review of proforma ARR impact and credit liability estimate) |
| 3. Regulatory & Privacy Impact | DPO / Privacy Counsel (DPIA determination) |
| 4. Executive Authorization | Dr. Sarah Chen, CEO (required for any Tier 1 service or >$2M ARR impact) |

Approval is documented via a signed "Service Deprecation Authorization" form stored in the Meridian Policy & Procedure Repository (Veeva Vault, Policy Domain).

### 5.2 Phase 1: Notification and Freeze

#### 5.2.1 Service Registry Update

Within 5 business days of Phase 0 approval, the Platform Architecture team shall update the service's lifecycle status in Atlassian Compass to `DEPRECATED`. The service record shall be annotated with:
- EOS Date
- EOL Date
- Designated Replacement Service ID
- Link to the customer-facing deprecation notice template

#### 5.2.2 External Customer Notification (Product Manager & Customer Success)

The Product Manager shall author a customer-facing deprecation notice using the standard template (`TEMPLATE-PENG-017-NOTICE`) published in the Meridian Customer Communication Hub. The notice must include:

- **Subject Line:** `[ACTION REQUIRED] Deprecation Notice: [Service Name] End-of-Life on [EOL Date]`
- **Affected Service(s):** Clear identification, including API endpoint paths if applicable.
- **Key Dates:** EOS Date, End of Active Support, EOL Date.
- **Designated Replacement:** Link to replacement service documentation and migration guide.
- **Impact of Non-Action:** Consequences of inaction by the customer after EOL (e.g., API calls will return `410 Gone` status; UI features will be removed; data export access will terminate).
- **Support Commitment:** Outline of support tiers during the deprecation period.
- **Data Handling Summary:** High-level description of how customer data will be handled at EOL (e.g., returned via final export, permanently destroyed, or archived per DPA terms).

The Director of Customer Success shall orchestrate a tiered distribution campaign:

| Tier | Week 1 | Week 2-4 | Ongoing |
|---|---|---|---|
| **Tier 1** | Direct CSM email + registered letter + Executive Business Review scheduling | CSM phone follow-up, migration workshop scheduling | Monthly migration progress review (QBR cadence) |
| **Tier 2** | Admin Portal banner + email blast to registered admins | Automated reminder email, office hours webinar | Quarterly reminder |
| **Tier 3** | In-app notification banner + email to admin contacts | Monthly product newsletter mention | Mention in release notes until EOL |

The Customer Success team shall track acknowledgment in the Gainsight Customer Health Dashboard. Failure to obtain acknowledgment from a Tier 1 customer within 30 days shall trigger a named CSM escalation task.

#### 5.2.3 Feature Flag Implementation (Engineering)

Simultaneous with customer notification, the Engineering Lead shall implement a feature flag (`DEPRECATION_EOL_{SERVICE_NAME_SHORT}`) in LaunchDarkly. This flag shall initially be set to `false` (no impact) for all production environments. This flag serves as the kill-switch mechanism for the sunset execution in Phase 4.

### 5.3 Phase 2: Migration Support and Active Transition

This phase constitutes the active backfill period. Meridian is responsible for providing tooling, documentation, and support to enable customer migration.

#### 5.3.1 Internal Technical Debt Remediation

Prior to providing external migration tooling, the Engineering Lead shall ensure that all internal Meridian services and pipelines that consume the deprecated service have been migrated to designated replacements. The deprecated service SHALL NOT be decommissioned while internal production dependencies remain. A dependency graph from Atlassian Compass shall be reviewed and all internal consumers validated as "migrated."

#### 5.3.2 Migration Support Package

The Product Manager shall publish a Migration Support Package containing:

1.  **Feature Parity Matrix:** A detailed table mapping every function of the deprecated service to its equivalent in the replacement.
2.  **API Translation Guide:** Side-by-side request/response comparisons, error code mappings, and authentication flow guides.
3.  **Migration Sandbox:** A dedicated, free-of-charge environment (sandbox) where customers can test their integration against the replacement service with production-realistic synthetic data.
4.  **Data Export Utility:** An API endpoint or CLI tool allowing customers to perform a bulk export of their data in a machine-readable, industry-standard format (FHIR R4 Bundle for clinical data; Parquet or CSV for structured analytics data).
5.  **Professional Services Engagement:** An optional, billable Statement of Work (SOW) for Meridian Professional Services to execute the migration on the customer's behalf.

#### 5.3.3 End-of-Sale Execution

On the published EOS date, the Product Manager shall execute the following:
- The service is removed from the Meridian pricing catalog and new tenant provisioning is disabled in the internal admin console.
- Any marketing website references to the service as "Available" are updated to "Deprecated."
- SalesForce CRM opportunity product catalog is updated to prevent quoting of the deprecated service to new prospects.

### 5.4 Phase 3: Extended Support and Final Data Disposition

#### 5.4.1 Extended Support Window

For Tier 1 and Tier 2 services, an Extended Support window of 6 months begins on the EOS date. During Extended Support:
- Meridian provides Tier 1 and Tier 2 support for critical security vulnerabilities and P1 production outages only.
- No feature enhancements, non-security bug fixes, or Tier 3 engineering support are provided.
- Customers remaining on the service after EOS are subject to an Extended Support surcharge of 25% of their current subscription fee, unless waived by the VP of Revenue Operations as a strategic concession.

#### 5.4.2 Final Customer Data Disposition

At the conclusion of the Extended Support window (or EOS for Tier 3 services without Extended Support), every remaining customer tenant must be in exactly one of the following states:

1.  **Migrated:** Customer has fully migrated to the designated replacement and acknowledged completion.
2.  **Final Export Delivered:** Meridian has delivered a final, complete export of all customer data. The customer acknowledges receipt. The customer's instance and data in the deprecated service will be destroyed at EOL.
3.  **Data Retention Mandate:** A legally valid litigation hold, regulatory investigation hold, or contractual data retention clause mandates Meridian retain the data. The Director of Legal Affairs must approve each instance of this state.

A final Data Disposition Status report, generated by the Engineering Lead, shall be provided to the DPO and Service Owner.

### 5.5 Phase 4: Technical Sunset and Decommissioning

This is the terminal technical phase. **No steps in this phase shall be executed until the Data Disposition Status report is approved by the Service Owner and DPO.**

#### 5.5.1 Execution Pre-Flight Checklist

The DevOps/SRE Lead and Engineering Lead shall jointly complete the "Service Sunset Runbook" (`RUNBOOK-PENG-017`):

- [ ] **Confirmation Gate:** Approval from Service Owner (email approval captured in Jira ticket).
- [ ] **Disable Write Traffic:** The LaunchDarkly kill-switch flag is toggled to `true` for all contexts, rendering the service read-only (all mutation operations return `HTTP 451 Unavailable For Legal Reasons`).
- [ ] **Drain Read Traffic:** DNS records for the service (Route 53) are updated to a CNAME record pointing to a static sunset notice page. TTL is set to 300 seconds and allowed to propagate for 48 hours.
- [ ] **Stop Compute Resources:** ECS/EKS service definitions are scaled to 0 desired count.
- [ ] **Final Database Snapshot:** A final, consistent snapshot of all data stores (RDS, DynamoDB, S3 buckets) is taken. This snapshot is the source for the Legacy Data Archive.
- [ ] **Verify Archive:** Integrity of the archive snapshot is validated using checksums.
- [ ] **Production Data Destruction:** Production data stores are securely destroyed. For AWS RDS, the instance is deleted with final snapshot protection removed. For S3, versioned buckets are emptied and deleted. Cryptographic key material (AWS KMS CMK) used for application-layer encryption is scheduled for deletion with a 7-day waiting period. The key deletion is attested to in the Service Sunset Runbook.
- [ ] **Deprovision Infrastructure:** Non-data infrastructure (load balancers, compute clusters, CI/CD pipelines, monitoring agents) is decommissioned via Terraform `terraform destroy`.
- [ ] **License Key Reclamation:** Software license keys are reclaimed and deactivated.
- [ ] **Tombstone Artifact Creation:** The Service Owner creates the final tombstone artifact in Atlassian Compass, setting lifecycle status to `SUNSET`.

#### 5.5.2 Legacy Data Archive Operations

The Legacy Data Archive exists as a dedicated AWS S3 bucket (`meridian-legacy-archive-[service-name]`) governed by the following controls:

- **Access:** IAM policies grant `s3:GetObject` and `s3:ListBucket` solely to the designated Data Governance Manager role, with access logged to AWS CloudTrail and forwarded to the Splunk SIEM.
- **Retention Timer:** An S3 Lifecycle Policy is applied, setting a deletion timer corresponding to the maximum retention period defined in the data inventory (not to exceed 10 years from EOL date, unless a longer period is mandated by a medical device clinical evaluation plan under EU MDR).
- **DSAR Fulfillment Capability:** The archive is indexed in a metadata catalog (Apache Atlas) to support search for personal data by Data Subject identifier. The Engineering Lead for Data Platform is responsible for executing validated DSAR deletion requests against this archive within the 30-day GDPR window.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control ID | Control Description |
|---|---|
| **T-C001** | The LaunchDarkly feature flag `DEPRECATION_EOL_*` serves as the authoritative, auditable kill switch for service functionality. All flag toggle events are logged to Splunk. |
| **T-C002** | The Legacy Data Archive bucket is configured with S3 Object Lock in Compliance mode, preventing deletion of an object version before its retention date. This protects against accidental or malicious premature destruction of compliance-required data. |
| **T-C003** | All production data destruction activities must be executed through approved Terraform modules, never via manual AWS Console CLI commands. Manual console access is prohibited for decommissioning steps. |
| **T-C004** | The final database snapshot is encrypted using a dedicated, sunset-specific AWS KMS Customer Managed Key (CMK). This key is stored separately from the archive and access is restricted to the Data Governance Manager and DPO roles. |
| **T-C005** | User access to Meridian systems is governed by role-based access controls (RBAC). Access is provisioned based on the principle of least privilege, and is granted through an automated ticket-based workflow. While access is revoked immediately upon role change or termination (via automated deprovisioning in Okta), Meridian relies on the good-faith adherence of its engineering managers and team leads to periodically review group memberships and access logs to identify any stale or inappropriate permissions. This operational practice ensures that access remains aligned with job responsibilities. |

### 6.2 Administrative and Organizational Controls

| Control ID | Control Description |
|---|---|
| **A-C001** | The Service Retirement Business Case is a mandatory control artifact and must be approved per the Phase 0 approval gates before any customer-facing communication is released. |
| **A-C002** | The Customer Notification Period defined in P-004 is enforced via a Jira automation rule: the Deprecation Execution Epic cannot transition to "In Progress" status until the Notification Period Wait Time custom field has elapsed. |
| **A-C003** | Upon any security incident (potential or confirmed data breach) that impacts a sunsetting service or its legacy archive, the SOC-SEC-009 Incident Response Plan is immediately activated. The Incident Response Team provides initial triage and containment, and engages relevant stakeholders as per the existing response framework. |
| **A-C004** | Segregation of duties is enforced: the individual approving the Data Disposition Status report (Service Owner) cannot be the same individual executing the Terraform destroy plan (SRE Lead). |
| **A-C005** | All customer-facing deprecation notifications are reviewed and approved by the legal team (via ContractPodAI or manual review) before issuance to ensure alignment with contractual SLAs and regulatory notice requirements. |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Compliance Monitoring

The Compliance Engineering team shall monitor the following automated controls via the Splunk SIEM:

| Alert | Trigger Condition | Severity | Response SLA |
|---|---|---|---|
| Legacy Archive Access | Any IAM `GetObject` or `ListBucket` event against a `meridian-legacy-archive-*` bucket not initiated by the Data Governance Manager role. | P1 (Critical) | Investigate within 1 hour; potential unauthorized data access. |
| Sunset Kill-Switch Override | A LaunchDarkly `DEPRECATION_EOL_*` flag is toggled `false` (reactivating a service) after the formal Phase 4 checklist has been marked "Complete." | P2 (High) | Investigate within 4 hours; potential unauthorized service reactivation. |
| Key Material Destruction | A KMS CMK scheduled for deletion is either canceled or the 7-day window is tampered with. | P1 (Critical) | Immediate investigation; potential sabotage of secure data destruction. |

### 7.2 Operational Metrics (KPIs)

The Product & Engineering organization shall track the following Key Performance Indicators on a quarterly basis, reported via Looker dashboard `Dashboard-PENG-017`:

| Metric | Calculation | Target | Owner |
|---|---|---|---|
| **Deprecation Timeline Adherence** | (Actual EOL Date - Planned EOL Date) as calendar days, measured at service level. | Variance ≤ 30 days for the planned quarter. | VP of Engineering |
| **Customer Notification Compliance** | Percentage of customers where first notification was logged `X` days before EOS, where `X` >= the tier minimum. | 100% compliance. | Director of Customer Success |
| **Migration Completion Rate (at EOL)** | (Number of fully migrated customers / Total customers at time of EOS) × 100. | ≥ 95% for Tier 3 services; ≥ 80% for Tier 1 & 2 services. | Product Manager |
| **DSAR Fulfillment from Archive** | Number of DSAR deletion requests against the Legacy Data Archive fulfilled within 30 days, measured against total received. | 100%. | DPO |

### 7.3 Reporting Cadence

- **Weekly Status during Active Migration Phase:** The Deprecation Execution Lead provides a status update in the weekly Product & Engineering Leadership standup.
- **Monthly Sunset Portfolio Review:** The VP of Engineering and DPO review the status of all services currently in `DEPRECATED` state. A "Sunset Health Score" (composite of timeline, migration, and incident metrics) is assigned to each.
- **Quarterly Compliance Audit:** The Internal Audit team reviews a random sample of completed sunset runbooks for procedural compliance and completeness of the evidence log.

---

## 8. Exception Handling and Escalation

### 8.1 Exception Types

Exceptions to the provisions of this SOP are categorized as follows:

| Type | Description | Example |
|---|---|---|
| **Type E-TIME** | An adjustment to the minimum Customer Notification Period (Policy P-004). | A critical security vulnerability in a third-party library forces an accelerated EOL. |
| **Type E-DATA** | A deviation from the standard data disposition procedures (Data Handling Policy P-008). | A customer contract stipulates a 10-year data escrow arrangement that conflicts with the standard archive retention timer. |
| **Type E-PROC** | A modification to an approval gate or procedure in this SOP. | Request to bypass the DPIA screening (Section 5.1.3) for a service that demonstrably processes only anonymized data. |

### 8.2 Exception Request Procedure

1.  **Initiation:** The exception requestor documents the exception, including the specific SOP clause from which deviation is required, the business or technical justification, a risk assessment (impact on confidentiality, integrity, availability, and customer trust), and a proposed compensating control.
2.  **Risk Assessment:** The DPO or a designated Privacy Counsel reviews all exception requests for privacy and data protection implications. The VP of Security reviews for security implications.
3.  **Approval Authority:** Exceptions are approved based on risk severity:

| Risk Level (Internal Assessment) | Approver |
|---|---|
| Low (e.g., administrative documentation exception) | Service Owner (VP/Director) |
| Medium (e.g., E-TIME for a small, non-PHI Tier 3 service) | David Park, VP of Engineering |
| High (e.g., E-DATA involving PHI retention mandates) | Dr. Sarah Chen, CEO |

4.  **Documentation:** Approved exceptions are logged in the Meridian Governance, Risk, and Compliance (GRC) platform (Archer). The exception is time-bound with a specific expiration date upon which the exception must either be renewed or the service returned to compliance with the standard SOP.

### 8.3 Escalation Path

If a customer raises a formal dispute or a regulatory body (e.g., an EU Supervisory Authority) issues an inquiry regarding a service sunset:

1.  Customer Success Manager (CSM) → escalates to → Director of Customer Success.
2.  Director of Customer Success → engages → Product Manager and DPO.
3.  If unresolved or legal risk is identified → escalates to → General Counsel & VP of Engineering.
4.  CEO is briefed on any matter involving a threatened regulatory action or material litigation.

---

## 9. Training Requirements

### 9.1 Required Training

All personnel assigned roles in the RACI matrix (Section 3.1) must complete the following training modules, hosted on the Meridian LMS (Workday Learning):

| Training Module ID | Module Title | Target Audience | Frequency | Duration |
|---|---|---|---|---|
| `TRAIN-PENG-017-A` | Service Lifecycle Governance and Your Role | All RACI-assigned personnel | Annual | 45 minutes |
| `TRAIN-PENG-017-B` | GDPR Data Minimization and the Sunset Process | Product Managers, Engineering Leads, DevOps/SRE | Annual | 90 minutes |
| `TRAIN-PENG-017-C` | Customer Communication and De-Escalation during Transitions | Customer Success, Product Managers | Bi-Annual | 60 minutes |

### 9.2 Competency Validation

Completion of training is tracked via Workday Learning. A score of ≥80% on the post-module assessment is required to pass. Personnel who have not completed the mandated training shall not be assigned as the primary "Responsible" (R) role in a sunset project.

### 9.3 Sunset Drill

Annually, one low-impact internal service or non-customer-facing microservice shall be selected for a full "Sunset Drill." This drill serves as a practical test of the runbook, tooling, and team readiness without exposing customers to risk. Lessons learned from the drill are documented and used to refine this SOP.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|---|---|---|
| `SOP-SEC-009` | Incident Response and Breach Notification | Governs emergency security shutdowns and breach response during deprecation. |
| `SOP-DATA-004` | Data Classification and Handling | Defines the data classification schemas (PHI, PII, Internal) used in the data disposition planning. |
| `SOP-IT-014` | IT Asset Disposal and Media Sanitization | Governs physical media destruction; complementary to this SOP's logical data destruction procedures. |
| `SOP-VM-022` | Vendor Offboarding and Contract Termination | Governs third-party contract termination that may be part of a service sunset (e.g., a payment gateway provider). |
| `SOP-RDS-026` | Research Data Lifecycle | Governs the handling of de-identified, research-only data that may be retained post-sunset per Policy P-009. |
| `SOP-PRIV-003` | Data Subject Access Request Fulfillment | Governs the standard DSAR process referenced in the Legacy Data Archive operational procedures. |

### 10.2 External Standards and Regulations

- **SOC 2 (Type II)**: The controls documented in this SOP are designed to support Meridian's SOC 2 trust services criteria (Security, Availability, Processing Integrity). Specifically, the Phase 0 approval gates and the execution runbook support change management (A1), and the technical controls for data destruction support confidentiality (C1).
- **GDPR (Regulation (EU) 2016/679)**: This SOP is directly aligned with the following GDPR Articles:
    - **Article 5(1)(c) (Data Minimization):** Enforced through Policy P-007 and the Phase 4 data destruction procedure.
    - **Article 5(1)(e) (Storage Limitation):** Enforced through the Legacy Data Archive retention timer control (T-C003).
    - **Article 17 (Right to Erasure / "Right to be Forgotten"):** Operationally enabled by the DSAR archive search and delete capability (Section 5.5.2) and Policy P-008.
    - **Article 25 (Data Protection by Design and by Default):** Reflected in the requirement for a designated replacement (Policy P-003) that is, by default, designed to be privacy-preserving.
    - **Article 28 (Processor Obligations):** The customer notification and data export utilities (Phase 2) are designed to enable Meridian's customers (as Controllers) to fulfill their own obligations when transitioning processors.
    - **Article 35 (Data Protection Impact Assessment):** The DPIA screening gate (Section 5.1.3) ensures high-risk processing during sunset is formally assessed and documented.
- **HIPAA (Privacy and Security Rules)**: The PHI de-identification standard (Policy P-009) and the BA Agreement termination considerations inform the Phase 4 data disposition and customer notification language.

---

## 11. Revision History

| Version | Date | Author | Approver | Summary of Changes |
|---|---|---|---|---|
| 1.0 | 2022-03-10 | Anika Patel (VP, Platform) | Sarah Chen, CEO | Initial publication. Established basic sunset lifecycle. |
| 1.3 | 2023-01-25 | David Park, VP of Eng. | Sarah Chen, CEO | Added Tiered Notification Periods (P-004) and integrated CSM notification workflow following post-mortem of `MedInsight-v1` deprecation. |
| 1.5 | 2023-11-08 | Compliance Engineering | Elena Rios, DPO | Introduced mandatory DPIA screening gate (Section 5.1.3) and enhanced Legacy Data Archive access controls (T-C002) per GDPR audit recommendations. |
| 1.7 | 2025-05-14 | David Park, VP of Eng. | Sarah Chen, CEO | Shifted Phase 0 approval for Tier 1 services to CEO level. Added the `HTTP 451` status code convention. Expanded Data Disposition final states based on `HealthPay-v2` sunset lessons learned. |
| 1.8 | 2025-12-17 | David Park, VP of Eng. | Sarah Chen, CEO | This version refines the LaunchDarkly kill-switch workflow, integrates mandatory SBOM review post-Log4j, and expands the DSAR fulfillment SLA for legacy archives. It also introduces formal `E-TIME` exception types and clarifies the segregation of duties between engineering and compliance roles during the decommissioning sequence. |
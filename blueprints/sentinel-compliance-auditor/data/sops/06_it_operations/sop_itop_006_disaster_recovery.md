---
sop_id: "SOP-ITOP-006"
title: "Disaster Recovery"
business_unit: "IT Operations & Infrastructure"
version: "4.7"
effective_date: "2024-07-26"
last_reviewed: "2025-05-23"
next_review: "2025-11-10"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Disaster Recovery

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the framework, responsibilities, and operational procedures for Meridian Health Technologies, Inc. (“Meridian”) to prepare for, respond to, and recover from disruptive events affecting the availability, integrity, or confidentiality of its information systems and data assets. The objective is to ensure the continuity of critical business operations, minimize financial and reputational damage, and meet the recovery objectives set by the Board-level AI Governance Committee and executive leadership.

### 1.2 Scope

**In-Scope Systems and Assets:**
This SOP applies to all production and production-supporting information systems, data repositories, and network infrastructure that underpin Meridian’s four primary business lines:
- Clinical AI Platform (SageMaker endpoints, inference APIs, model registry, clinical databases)
- HealthPay Financial Services (payment processing engine, lending origination system, claims automation platform, credit scoring models)
- MedInsight Analytics (population health data lake, analytics engines, reporting portals containing Protected Health Information (PHI) for ~12M patients)
- Meridian SaaS Platform (multi-tenant AWS infrastructure in `us-east-1` and `eu-west-1`, authentication services, API gateway)

**Geographic Scope:**
This plan covers Meridian’s global operations, including primary office locations (Boston, London, Berlin, Singapore, Toronto) and cloud infrastructure regions.

**Out-of-Scope:**
- Development, testing, and staging environments, unless explicitly designated as a failover target.
- End-user computing devices (laptops, workstations). These are covered under SOP-ITOP-004: "Endpoint Backup & Management."
- Physical office disaster recovery (facilities, life safety) is addressed in the Corporate Emergency Response Plan, owned by the VP of IT Operations.

### 1.3 Applicability
This SOP applies to all Meridian employees, contractors, consultants, and third-party service providers who have a role defined in Section 3 or whose duties involve the operation, management, or use of in-scope systems.

---

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
| :--- | :--- |
| **BCP** | Business Continuity Plan. The overarching strategy encompassing people, process, and technology recovery. This SOP is a component of the BCP. |
| **BIA** | Business Impact Analysis. The formal assessment used to determine criticality, RTOs, and RPOs. |
| **Cold Site** | A backup site with power, cooling, and network connectivity but no pre-installed hardware. |
| **Command Center** | A dedicated physical or virtual space (Primary: Boston Conference Room B; Secondary: Zoom Room ID 945-218-7703) for the DR Team to coordinate activities. |
| **DR** | Disaster Recovery. |
| **DRP** | Disaster Recovery Plan (this document). |
| **Failback** | The process of restoring operations from the disaster recovery site back to the primary production site. |
| **Failover** | The process of shifting operations from the primary production site to a secondary disaster recovery site. |
| **Hot Site** | A fully operational backup site with real-time data replication, capable of assuming operations with minimal downtime. |
| **Meridian Command Center (MCC)** | The centralized digital dashboard for operational command and control during an incident, accessible via a dedicated Slack channel `#incident-command` and Datadog. |
| **PHI** | Protected Health Information, as defined by the Health Insurance Portability and Accountability Act (HIPAA). |
| **PIO** | Product Incident Owner. The designated product-specific role responsible for validating functional recovery during a test or actual event. |
| **Recovery Point Objective (RPO)** | The maximum targeted period in which data might be lost from an IT service due to a major incident. |
| **Recovery Time Objective (RTO)** | The targeted duration of time and a service level within which a business process must be restored after a disaster in order to avoid unacceptable consequences. |
| **Severity Level** | A classification (SEV1-SEV4) used to categorize the impact and urgency of an incident, as defined in SOP-ITOP-001: "Incident Management." |
| **Warm Site** | A backup site with pre-installed hardware, network links, and foundational software, requiring some configuration and data restoration to become operational. |

---

## 3. Roles and Responsibilities

| Role | Responsibility | Primary | Backup |
| :--- | :--- | :--- | :--- |
| **Disaster Recovery Coordinator (DRC)** | Overall authority for DR activation, coordination, and communication. Declares the disaster state. | Samanthan Torres, VP of IT Operations | David Park, VP of Engineering |
| **Incident Commander** | Leads the tactical response during a declared DR event through the Meridian Command Center. | Director of Site Reliability Engineering (SRE) | Lead SRE on-call |
| **Technical Recovery Lead** | Executes technical failover and failback procedures. Coordinates system administrators, DBAs, and cloud engineers. | Principal Cloud Architect | Senior DevOps Manager |
| **Communications Lead** | Manages all internal and external communications per the Crisis Communication Plan, including customer notifications and regulatory disclosures. | VP of Customer Operations, Michael Chang | Corporate Communications Director |
| **PIO: Clinical AI** | Validates end-to-end functionality and data integrity for clinical decision support tools and diagnostic imaging analysis. | VP of Clinical AI Products, Dr. Aisha Okafor | Lead ML Engineer, Clinical AI |
| **PIO: HealthPay** | Validates functional recovery, transactional integrity, and settlement capabilities for financial services. | VP of Financial Services, Robert Liu | Senior Director, Payment Engineering |
| **PIO: MedInsight** | Validates data completeness, query performance, and report generation for analytics platforms. | Director of Analytics Engineering | Senior Product Manager, MedInsight |
| **HIPAA Security Officer** | Ensures all recovery activities maintain PHI security. Authorizes any emergency access procedure overrides. | Chief Information Security Officer, Rachel Kim | VP of IT Operations |
| **Legal & Compliance Lead** | Advises on regulatory obligations, breach notification laws, and contractual liabilities. | General Counsel, Maria Gonzalez | Chief Compliance Officer, Thomas Anderson |

---

## 4. Policy Statements

4.1 **Commitment to Resilience:** Meridian Health Technologies is committed to maintaining a robust, risk-based Disaster Recovery program to ensure the availability of critical systems and data, safeguarding patient safety and financial operations.

4.2 **Risk-Based Prioritization:** Recovery activities will be prioritized based on the results of the annual Business Impact Analysis (BIA). Tier 1 systems (clinical AI inference, payment processing) will take precedence over Tier 2 (MedInsight analytics, internal portals) and Tier 3 (development environments) systems.

4.3 **Recovery Objectives:** All in-scope systems have defined Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO). The IT Operations team is responsible for designing and maintaining the technical architecture to meet these objectives. The system-specific RTO/RPO commitments are detailed in Appendix A: Technology Recovery Matrix, which is maintained as a living document by the DRC and updated after any major architectural change.

4.4 **Plan of Action:** Upon declaration of a disaster, the Meridian SaaS Platform and its hosted products will be recovered in the following priority order, as established by the Board-level AI Governance Committee:
    1.  Meridian SaaS Platform core infrastructure (authentication, API gateway, encryption services).
    2.  Clinical AI Platform (high-risk AI systems under the EU AI Act; human life and safety implications).
    3.  HealthPay Financial Services (financial market integrity, SR 11-7 compliance).
    4.  MedInsight Analytics.
    5.  Internal corporate services (email, HRIS, Finance).

4.5 **Testing Assurance:** The DR plan will be tested at least semi-annually. One test annually will be a full-scale, live failover exercise for Tier 1 systems to the designated recovery region.

4.6 **Confidentiality and Integrity:** All disaster recovery operations shall maintain appropriate administrative, physical, and technical safeguards to protect the confidentiality, integrity, and availability of Meridian’s information assets, with a specific focus on protecting PHI from impermissible use or disclosure during the crisis.

4.7 **Logging During Recovery:** All access to and restoration of PHI during a declared DR event will be captured by audit controls. Records of such access will be reviewed by the CISO within 30 days of event closure.

---

## 5. Detailed Procedures

### 5.1 Disaster Declaration Criteria and Procedure

A "Disaster" is a SEV1 event where a critical production service or entire availability zone/region is completely unavailable and the estimated time to restore the primary site exceeds the established RTO.

**5.1.1 Declaration Triggers:**
- Confirmed total loss of connectivity to a primary AWS region (`us-east-1` or `eu-west-1`) for > 15 minutes, with no clear mitigation path.
- Catastrophic, unrecoverable data corruption affecting > 50% of a Tier 1 database cluster.
- Cybersecurity event (e.g., destructive ransomware) where the CISO, CEO, and General Counsel jointly recommend failover as the recovery strategy.
- Physical destruction of a primary data center co-location facility, if applicable.

**5.1.2 Authorization Chain:**
1.  **Incident Commander** (SRE Director) identifies a triggering condition. They immediately convene the core DR team in the Secondary Command Center (Zoom Room ID 945-218-7703) and open a dedicated Slack channel `#dr-event-active`.
2.  **Incident Commander** formally recommends activation of the DR Plan to the **Disaster Recovery Coordinator (DRC)** .
3.  **DRC** consults with the **CEO (Dr. Sarah Chen)** , the **HIPAA Security Officer (Rachel Kim)** , and the **Legal & Compliance Lead (Maria Gonzalez)** .
4.  Upon consensus, the **DRC declares a disaster** by executing the following command in the `#dr-event-active` Slack channel: `!declaredisaster —plan SOP-ITOP-006 —authority [DRC Name] —reason [Brief justification]`.
5.  This command triggers an automated PagerDuty notification to the entire "DR Tier 1 Engineers" escalation group, alerting them to cease ad-hoc troubleshooting and immediately assemble at the Command Center (virtual) to begin the formal Technical Failover Procedure.

### 5.2 Technical Failover Procedure: Meridian SaaS Platform (AWS us-east-1 to eu-west-1)

This procedure assumes a Hot Site architecture for the Meridian SaaS Platform, with active-passive deployment across AWS `us-east-1` (Primary) and `eu-west-1` (Recovery).

**Prerequisites:**
- Access: AWS Organizations root account credentials, HashiCorp Vault root token (split-key, one half held by DRC, other by CISO).
- Tools: Terraform Enterprise, AWS CLI, Datadog Synthetics, PagerDuty.
- Communication: Open bridge line (Zoom Room ID 945-218-7703).

**Step 1: Pre-Failover Health Check of Recovery Region**
- **Actioned By:** Principal Cloud Architect
- **Procedure:**
    1.  Log in to AWS Management Console for the recovery region (`eu-west-1`).
    2.  Verify the health and synchronization status of the Aurora Global Database secondary cluster (`meridian-saas-dr`). Ensure replication lag is < 5 seconds.
    3.  Verify DynamoDB Global Tables are fully synchronized.
    4.  Verify the secondary S3 replication bucket (`meridian-data-backup-dr-eu`) contains objects consistent with the primary bucket’s inventory report.
    5.  Confirm the Application Recovery Controller (ARC) is ready and reporting no issues.

**Step 2: DNS Cutover**
- **Actioned By:** Senior Network Engineer
- **Procedure:**
    1.  Update AWS Route 53 Application Recovery Controller (ARC) to initiate the failover for the public-facing endpoint group.
    2.  Manually update the CNAME record `api.meridianhealth.com` to point to the Application Load Balancer (ALB) `meridian-saas-dr-alb` in `eu-west-1`. Set TTL to 60 seconds.
    3.  Execute `terraform apply` on the `dns-dr-eu` workspace to push disaster-specific records for internal service discovery.
    4.  **Validation:** Execute `dig api.meridianhealth.com` against a public resolver (e.g., `8.8.8.8`) to confirm record propagation.

**Step 3: Database Failover**
- **Actioned By:** Lead Database Administrator (DBA)
- **Procedure:**
    1.  In the AWS Console, promote the Aurora Global Database secondary cluster (`meridian-saas-dr`) in `eu-west-1` to a standalone primary role.
        - Command: `aws rds promote-read-replica-db-cluster --db-cluster-identifier meridian-saas-dr`
    2.  Wait for the cluster status to transition from "Modifying" to "Available".
    3.  Update the master credentials in the AWS Secrets Manager secret `prod-meridian-saas-db-master` to reflect the newly promoted cluster’s writer endpoint.
    4.  **Validation:** The Lead DBA executes a pre-defined "smoke test" SQL script against the new writer endpoint to confirm read/write functionality.

**Step 4: Core Service Activation**
- **Actioned By:** Senior DevOps Manager
- **Procedure:**
    1.  Update the `dr-eu` Terraform Enterprise workspace variables to activate all core services. Specifically, set `auto_scaling_min` for `Meridian-Auth-Service`, `Meridian-API-Gateway`, and `Meridian-License-Manager` to production levels.
    2.  Execute a `terraform apply` on the `eu-west-1` production environment workspace.
    3.  This pipeline triggers a CodeDeploy deployment in `eu-west-1` that scales Auto Scaling Groups to full production capacity and initiates health checks for the KMS endpoints and HSM connections.

**Step 5: Tiered Application Failover**

**5.2.1 Clinical AI Platform**
- **Actioned By:** Lead ML Engineer
- **Procedure:**
    1.  Execute the SageMaker Failover script: `python3 /dr/scripts/clin_ai_failover.py --source us-east-1 --target eu-west-1`.
    2.  This script deploys the production model artifacts from the `eu-west-1` DR S3 bucket to production SageMaker endpoints in the recovery region.
    3.  Update the clinical prediction API gateway endpoint mapping in the `clin-ai-prod` API Gateway stage to point to the new `eu-west-1` SageMaker endpoints.
    4.  **PIO Validation (Dr. Okafor):** Execute a suite of 15 pre-defined diagnostic studies via the DR validation toolkit. Verify inference latency is within the 500ms SLA and the confidence scores are within the expected delta of the baseline. Explicitly approve in the `#dr-event-active` Slack channel upon success.

**5.2.2 HealthPay Financial Services**
- **Actioned By:** Senior Director, Payment Engineering
- **Procedure:**
    1.  **Message Queue:** Update the VPC Endpoint configuration to reconnect the payment processing engine to the managed Kafka cluster in `eu-west-1`. Dump and replay all unprocessed transactions from the `us-east-1` dead letter queue.
    2.  **Settlement Engine:** Bring online the `meridian-settlement-dr` EC2 instances. Manually initiate the end-of-day settlement reconciliation process for the current day’s transactions up to the outage point. This is a critical step to prevent duplicate transactions.
    3.  **Credit Model:** Promote the replicated `eu-west-1` Redis cache cluster to primary for the underwriting engine. Cold-start the microservices in the correct order: Risk Gateway → Score Engine → Decision Engine.
    4.  **PIO Validation (Robert Liu):** Submit 10 synthetic loan applications via the DR test suite, covering the full origination lifecycle (submit → underwrite → approve → fund). Verify the integrity by cross-referencing the generated transaction hashes with the core ledger API. The PIO must log the successful audit trail hashes in the designated Slack thread.

**5.2.3 MedInsight Analytics**
- **Actioned By:** Director of Analytics Engineering
- **Procedure:**
    1.  Scale the `eu-west-1` Redshift cluster `meridian-analytics-dr` from 2 nodes of `dc2.large` to 8 nodes of `dc2.8xlarge`.
    2.  Recreate Materialized Views from the latest good snapshot in S3, prioritizing views tagged as `tier-1-critical` (including PHI datasets for population health dashboards). Tier-2 and Tier-3 views can be rebuilt later.
    3.  Restart the Tableau Server cluster in `eu-west-1`.
    4.  **PIO Validation (Director of Analytics):** Run the top 10 most-accessed dashboards as tracked by Tableau’s admin view, and ensure data completeness by comparing row counts against a pre-disaster baseline report. Record any discrepancies and approve basic functionality.

**Step 6: Global Incident Declaration and Communication**
- **Actioned By:** VP of Customer Operations, Michael Chang
- **Procedure:**
    1.  Once PIOs for all Tier 1 systems have confirmed functional recovery, the Communications Lead posts the pre-approved, legally-reviewed message to the Meridian public Status Page (`status.meridianhealth.com`).
    2.  A separate, PHI-secure email blast is sent to the Clinical AI Platform and HealthPay customer contacts list stored in `CRM_DR_Contacts`.
    3.  The status page is updated every 60 minutes or upon significant recovery milestone, whichever is sooner.

### 5.3 Technical Failback Procedure (eu-west-1 to us-east-1)

Failback is a deliberate, scheduled operation, not an emergency procedure. It requires a Change Request (CR) per SOP-ITOP-002: "Change Management."

1.  **Pre-failback Checklist:** The primary `us-east-1` environment is fully patched, healthy, and has caught up on all data replication from the recovery site.
2.  **Synchronization Window:** A 4-hour maintenance window is declared. During this window, all write operations to the `eu-west-1` databases are temporarily quiesced at the application level to allow the final Aurora Global Database synchronization to complete.
3.  **Promotion:** The `us-east-1` Aurora cluster is manually promoted from secondary to primary.
4.  **DNS Cutback:** A reverse DNS weight is applied in Route 53, slowly shifting traffic from the `eu-west-1` ALB back to the primary `us-east-1` ALB over a 2-hour period, with traffic monitored in Datadog.
5.  **Decommission:** Once all traffic is on the primary site, the recovery environment in `eu-west-1` is scaled back down to its standby (warm/hot) configuration. The DR event is formally closed by the DRC in Slack.

### 5.4 Data Restoration from Backup (Cold/Warm Site Scenario)

In the event the primary site is unavailable and the hot site has irrecoverable data corruption:
1.  **Identify Baseline:** The Lead DBA identifies the last clean, validated snapshot from AWS Backup Vault in the recovery region.
2.  **Restore Core Ledger:** Restore the Meridian Financial Core ledger database (PostgreSQL on RDS) from the selected snapshot. This is the system of truth for HealthPay.
3.  **Restore PHI Repositories:** Sequentially restore the Clinical AI Model Registry data and MedInsight Redshift cluster from their respective vault snapshots.
4.  **Integrity Check:** The PIOs run a specialized script (`integrity_check.py`) that compares restored data checksums against a pre-disaster manifest, flagging all discrepancies, with a special focus on PHI datasets.
5.  **Replay Transaction Logs:** Apply archived WAL logs to the financial core ledger to minimize transactional data loss, aiming to meet the RPO.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls
- **Vendor Access Control:** Any access to Meridian’s disaster recovery environment by external vendors or contractors must be pre-approved by the CISO and DRC. All such sessions shall be attended by a Meridian SRE team member via a shared, read-only session recorded and logged. After the DR event, all vendor-provided access keys and temporary accounts will be revoked by the IT Identity team within 1 hour of the DRC closing the incident.
- **Segregation of Duties:** No single individual possesses both the technical ability to execute a failover and the authority to declare a disaster. The Incident Commander role and the DRC role are held by separate individuals. The AWS root account MFA token is split between the DRC and the CISO.

### 6.2 Technical Controls
- **Encryption at Rest and in Transit:** All snapshots, database replicas, and S3 backup buckets in the recovery region shall inherit the mandatory encryption configurations from the primary production environment. KMS keys are replicated via AWS KMS Multi-Region Keys.
- **Immutable Backups:** All backup vaults, especially those containing ePHI and financial audit trails, are configured with AWS Backup Vault Lock in compliance mode. No actor, including the root account, can delete a backup before its pre-defined expiry.
- **Access Controls:** DR-specific AWS IAM roles (`dr-failover-engineer`, `dr-database-admin`) use tightly-scoped policies. These policies grant necessary permissions but do NOT grant `iam:PassRole` access to production service-linked roles, preventing privilege escalation.
- **Network Isolation:** The recovery environment in `eu-west-1` operates within its own isolated Virtual Private Cloud (VPC) CIDR block. All inter-region traffic during failover is governed by strict Transit Gateway routing policies, and all access to the recovery database is logged.
- **Audit Logging:** All AWS CloudTrail logs, VPC Flow Logs, and database audit logs generated in the recovery region during a DR event are aggregated into a dedicated, immutable S3 bucket for post-incident forensic analysis.

### 6.3 Physical Controls
All Meridian-managed physical infrastructure (co-location at Iron Mountain BOS-1) is secured with biometric access controls, 24/7 manned security, and camera surveillance.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)
The IT Operations & Infrastructure business unit is measured against the following KPIs, which are reported to the Board-level AI Governance Committee at each quarterly review:

| KPI | Target | Measurement Method |
| :--- | :--- | :--- |
| **DR Test Success Rate** | ≥ 95% of critical application tests must pass during a full failover drill. | PIO Validation logs & automated test suites. |
| **Adherence to RTO** | 100% for Tier 1; 95% for Tier 2 for any declared event or drill. | Datadog timestamps from event declaration to PIO sign-off. |
| **Adherence to RPO** | 100% for Tier 1; 99.9% for Tier 2. | AWS Backup console, DBA restore verification logs. |
| **Plan Currency** | All documentation reviewed and updated within one week of any infrastructure change or biannual drill. | Confluence page version timestamps. |

### 7.2 Dashboards
- **Datadog DR Dashboard:** A dedicated, real-time screen set for the Command Center, showing replication lag, recovery region health, and a live RTO clock.
- **Slack Status:** The `#infrastructure-status` Slack channel receives automated push updates on DR-readiness metrics every hour.

### 7.3 Event Reporting
Within 15 business days of a DR event or test completion, the Disaster Recovery Coordinator will publish a formal **After-Action Report (AAR)** . The AAR includes:
- Executive Summary of the event.
- Detailed timeline of the failover and failback procedures.
- A table of all validated RTOs/RPOs vs. actual performance.
- A formal root cause analysis of any validation failure.
- A list of Corrective and Preventive Actions (CAPAs) with assigned owners and deadlines, tracked in Jira.

---

## 8. Exception Handling and Escalation

### 8.1 Procedure Exceptions
During a DR event, if a documented technical procedure fails, the Technical Recovery Lead is authorized to deviate from the written steps to achieve the recovery objective, subject to the following escalation process:
1.  **Technical Team Decision:** The deviation must be discussed and agreed upon by the Technical Recovery Lead and at least one Lead Engineer from a non-affected product line.
2.  **Security Consultation:** If the deviation involves access controls, encryption, or PHI handling, the HIPAA Security Officer (CISO) must be consulted and logged approval must be obtained, even if time-critical.
3.  **DRC Notification:** The DRC must be notified of all procedure deviations within 30 minutes via the `#dr-event-active` Slack channel. The notification must describe the deviation, the rationale, and any temporary increase in risk.

### 8.2 Policy Exemptions
Requests for permanent policy exemptions (e.g., extending RTO for a legacy system beyond the standard Tier 2 SLA) must be submitted through SOP-GOV-001: "Policy & Compliance" using the `FRM-008 Policy Exception Request` form. Exemptions for this policy require joint approval from the VP of IT Operations (DRC), the CISO, and the CFO (for systems impacting financial integrity).

---

## 9. Training Requirements

All personnel holding a role defined in Section 3 must complete the following:

| Training Module | Description | Frequency | Tracking |
| :--- | :--- | :--- | :--- |
| **SOP-ITOP-006 Annual Review** | Mandatory reading and acknowledgment of the current DR policy and procedures, including a 30-minute scenario-based walk-through. | Annually | Workday Learning Management System (LMS) |
| **DR Full-Scale Exercise Participation** | Active participation in the role designated in this SOP during the semi-annual live failover test. | Semi-Annually | Exercise performance logs & PIO sign-off sheets |
| **Tabletop Command & Control Drill** | A 4-hour facilitated tabletop exercise for the core command team (DRC, Incident Commander, Communications Lead) simulating a complex regional cloud outage. | Annually | Facilitator sign-off form |

Failure to complete mandatory training before the required deadline will result in the temporary revocation of credentials for DR environment access, as managed by the VP of IT Operations.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs
- **SOP-ITOP-001:** Incident Management
- **SOP-ITOP-002:** Change Management
- **SOP-ITOP-004:** Endpoint Backup & Management
- **SOP-SEC-001:** Information Security Policy
- **SOP-SEC-003:** Identity and Access Management
- **SOP-DA-001:** Data Classification and Handling Policy
- **SOP-GOV-001:** Policy and Compliance Management
- **SOP-GOV-002:** Vendor Risk Management
- **SOP-COMP-001:** HIPAA Compliance Framework

### 10.2 External References and Frameworks
- **AWS Well-Architected Framework – Reliability Pillar:** Whitepaper
- **NIST Special Publication 800-34 Rev. 1:** Contingency Planning Guide for Federal Information Systems
- **ISO 22301:2019:** Societal security — Business continuity management systems

### 10.3 Appendices (Stored as linked Confluence Documents)
- Appendix A: Technology Recovery Matrix (System-by-system RPO, RTO, site config, and service owner)
- Appendix B: Crisis Communication Plan & Message Templates
- Appendix C: Technical Contact Roster (Confidential to Command Team)

---

## 11. Revision History

| Version | Date | Author/Editor | Description of Change |
| :--- | :--- | :--- | :--- |
| 4.7 | 2024-07-26 | S. Torres | Major revision. Updated RTO/RPO commitments for Clinical AI to align with new EU MDR CE marking requirements. Rewrote Section 5.3 failback procedure to incorporate new quiesce step. |
| 4.6 | 2025-04-10 | J. Patel (SRE Manager) | Updated roles for new organizational structure; added VP of Customer Ops as Communications Lead. Revised Tier 1 definitions after BIA annual review. |
| 4.5 | 2024-01-15 | S. Torres | Updated to reflect the full decommissioning of the physical Iron Mountain BOS-1 warm site; all recovery now exclusively to AWS `eu-west-1`. |
| 4.4 | 2023-08-01 | J. Patel | Added detailed step-by-step procedures for HealthPay Kafka replay and settlement reconciliation (Section 5.2.2) after post-mortem findings from DR Test `Q3-2023-FAIL`. |
| 4.3 | 2023-03-22 | M. Chen (Compliance) | Minor update: Added reference to new Breach Notification playbook in Appendix B. |
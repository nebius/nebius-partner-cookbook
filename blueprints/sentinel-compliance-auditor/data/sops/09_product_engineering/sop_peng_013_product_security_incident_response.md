---
sop_id: "SOP-PENG-013"
title: "Product Security Incident Response"
business_unit: "Product & Engineering"
version: "1.9"
effective_date: "2024-10-23"
last_reviewed: "2025-02-26"
next_review: "2025-08-23"
owner: "David Park, VP of Engineering"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the Meridian Health Technologies, Inc. framework for detecting, triaging, containing, eradicating, and recovering from security incidents affecting the company's product portfolio. The overarching objective is to minimize operational disruption, protect customer data (including protected health information), preserve system integrity, and maintain compliance with applicable contractual and regulatory obligations. This SOP defines a structured, repeatable process that enables the Product Security Incident Response Team (PSIRT) to execute coordinated response activities with clearly defined roles, decision rights, and escalation paths.

### 1.2 Scope

This SOP applies to all security incidents, suspected incidents, and vulnerabilities that affect or have the potential to affect the following product environments:

- **Clinical AI Platform** – All clinical decision support modules, diagnostic imaging pipelines, patient risk scoring engines, and adverse event prediction services deployed across 340+ hospital and clinic environments. Includes both the inference APIs and the underlying model serving infrastructure hosted in AWS us-east-1 and eu-west-1.
- **HealthPay Financial Services** – Payment processing gateways, patient financing portals, medical lending origination platforms, claims automation engines, and associated fraud detection models. Covers all components subject to SR 11-7 model risk management governance.
- **MedInsight Analytics** – Population health analytics engine, care gap identification modules, outcomes prediction models, and all data pipelines processing protected health information (PHI) for approximately 12 million patient records.
- **Meridian SaaS Platform** – The multi-tenant cloud infrastructure layer, including container orchestration clusters, API gateways, identity and access management fabric, data stores, and observability pipelines. Covers all AWS accounts within the production and staging organizations in us-east-1 and eu-west-1, plus Azure DR regions.
- **Internal Engineering and CI/CD Tooling** – Build servers, artifact repositories, source code management systems, and deployment pipelines whose compromise could lead to product security impacts.

This SOP applies to all full-time employees, contractors, consultants, and third-party personnel who have access to Meridian product systems or who participate in incident response activities. It covers incidents originating from external threat actors, insider threats (malicious or accidental), software vulnerabilities, misconfigurations, and supply chain compromises.

### 1.3 Out of Scope

The following incident categories are explicitly out of scope and are addressed by separate SOPs:

- **Corporate IT Security Incidents** – Incidents limited to corporate endpoints, email systems, collaboration platforms, or office networks that do not impact product environments. Refer to SOP-IT-007 (Corporate IT Incident Response).
- **Physical Security Incidents** – Unauthorized physical access to Meridian office facilities or data centers. Refer to SOP-FAC-002 (Physical Security Incident Management).
- **HR-Related Insider Investigations** – Employee misconduct investigations not involving unauthorized access to product systems. Refer to SOP-HR-011 (Employee Relations Investigations).
- **Privacy Breaches Not Involving Security Incidents** – Unintentional disclosures resulting from business process errors without an underlying security control failure. Refer to SOP-PRIV-004 (Privacy Breach Management), though coordination with the PSIRT is required when the distinction is unclear.

### 1.4 Applicability

All personnel identified in Section 3 (Roles and Responsibilities) shall comply with this SOP. Business units outside Product & Engineering that identify potential product security incidents shall initiate the reporting procedures defined in Section 5.2. Violations of this SOP may result in disciplinary action up to and including termination of employment or contractual relationship.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Security Incident** | A confirmed or reasonably suspected event that compromises or threatens to compromise the confidentiality, integrity, or availability of Meridian product systems or the data processed therein. |
| **Vulnerability** | A weakness in system design, implementation, operation, or internal control that could be exploited to violate the system's security policy. Vulnerabilities are tracked separately from incidents until exploitation is confirmed. |
| **Critical Severity** | An incident or vulnerability that (a) results in or enables unauthorized access to PHI or payment card data, (b) causes complete loss of clinical service availability affecting patient safety use cases, (c) enables arbitrary code execution on production systems, or (d) has been assigned a CVSS v3.1 score of 9.0 or higher. |
| **High Severity** | An incident or vulnerability that significantly degrades security posture, enables privilege escalation to administrative levels, or has a CVSS v3.1 score of 7.0 to 8.9. |
| **Medium Severity** | An incident or vulnerability that enables limited unauthorized access, degrades defenses without full bypass, or has a CVSS v3.1 score of 4.0 to 6.9. |
| **Low Severity** | An incident or vulnerability with minimal security impact, requiring extensive preconditions for exploitation, or with a CVSS v3.1 score below 4.0. |
| **Confirmed Incident** | An event that the PSIRT Lead has determined, based on available evidence, constitutes a security incident requiring formal response under this SOP. |
| **False Positive** | An alert or report that, upon triage, is determined not to represent an actual security incident or exploitable vulnerability. |
| **Containment Window** | The maximum elapsed time between incident declaration and implementation of initial containment measures, as specified per severity level. |
| **Remediation** | Corrective actions applied to eliminate the root cause of an incident and prevent recurrence. Distinct from mitigation, which reduces immediate risk. |
| **War Room** | A dedicated, persistent communication channel (Meridian Slack channel prefix `#incident-war-` plus the incident ticket ID) and bridge line established for the duration of active incident response. |
| **Runbook** | An incident-type-specific supplemental procedure document detailing response steps for recurring incident patterns (ransomware, data exfiltration, credential compromise, etc.). |

### 2.2 Acronyms

| Acronym | Expansion |
|---|---|
| **CDSS** | Clinical Decision Support System |
| **CISO** | Chief Information Security Officer |
| **CVSS** | Common Vulnerability Scoring System |
| **DLP** | Data Loss Prevention |
| **EDR** | Endpoint Detection and Response |
| **HIPAA** | Health Insurance Portability and Accountability Act |
| **IMT** | Incident Management Team |
| **IR** | Incident Response |
| **KPI** | Key Performance Indicator |
| **MTTD** | Mean Time to Detect |
| **MTTR** | Mean Time to Respond (inclusive of containment and remediation) |
| **NIST AI RMF** | National Institute of Standards and Technology Artificial Intelligence Risk Management Framework |
| **PHI** | Protected Health Information |
| **PSIRT** | Product Security Incident Response Team |
| **RACI** | Responsible, Accountable, Consulted, Informed |
| **RCA** | Root Cause Analysis |
| **SIEM** | Security Information and Event Management |
| **SLA** | Service Level Agreement |
| **SOP** | Standard Operating Procedure |
| **SOT** | Security Operations Team |
| **VDP** | Vulnerability Disclosure Program |

---

## 3. Roles and Responsibilities

The following RACI matrix defines responsibilities for each major phase of the incident response lifecycle. Detailed task descriptions are provided in Section 5.

| Role | Designated Individual / Team | Detection & Reporting | Triage & Declaration | Containment & Eradication | Recovery & Post-Incident | Communications & Notification |
|---|---|---|---|---|---|---|
| **PSIRT Lead** | Rotating On-Call; designated Senior Security Engineer from SOT | Informed (I) | Accountable (A) | Responsible (R) | Accountable (A) | Accountable (A) |
| **Incident Commander** | Appointed per incident; typically Director of Security Engineering or delegate | Not Involved | Consulted (C) | Accountable (A) — for Critical/High only | Consulted (C) | Responsible (R) — external communications approval |
| **VP of Engineering** | David Park | Informed (I) | Informed (I) | Informed (I) | Informed (I) | Consulted (C) — customer notification |
| **Chief Medical Officer** | Dr. Priya Patel | Not Involved | Not Involved | Not Involved | Not Involved | Accountable (A) — clinical safety communications |
| **Chief Information Security Officer** | Jane Matsumoto | Consulted (C) | Accountable (A) — for severity classification disputes | Consulted (C) | Informed (I) | Consulted (C) |
| **General Counsel** | Office of the General Counsel | Not Involved | Not Involved | Not Involved | Not Involved | Consulted (C) — regulatory and legal communications |
| **Clinical AI Platform Lead** | Platform Engineering Lead (rotating) | Responsible (R) — for CDSS incidents | Consulted (C) | Responsible (R) | Responsible (R) | Informed (I) |
| **HealthPay Platform Lead** | Platform Engineering Lead (rotating) | Responsible (R) — for payment system incidents | Consulted (C) | Responsible (R) | Responsible (R) | Informed (I) |
| **MedInsight Platform Lead** | Platform Engineering Lead (rotating) | Responsible (R) — for analytics incidents | Consulted (C) | Responsible (R) | Responsible (R) | Informed (I) |
| **Infrastructure Lead** | Cloud Infrastructure Manager | Responsible (R) — for platform-layer incidents | Consulted (C) | Responsible (R) | Responsible (R) | Informed (I) |
| **ML Model Security Lead** | AI/ML Security Specialist | Responsible (R) — for model-specific threats | Consulted (C) | Responsible (R) | Responsible (R) | Informed (I) |
| **External Communications** | VP of Corporate Communications | Not Involved | Not Involved | Not Involved | Not Involved | Responsible (R) — press/media |
| **SRE Duty Manager** | Rotating On-Call SRE | Responsible (R) — initial detection and alerting | Consulted (C) | Responsible (R) — infrastructure changes | Responsible (R) — service restoration | Informed (I) |

### 3.1 Additional Role Descriptions

**PSIRT Core Team**: A standing group of security engineers, platform leads, and SRE representatives who maintain incident readiness. The Core Team conducts quarterly tabletop exercises and maintains incident response runbooks.

**Subject Matter Expert (SME)**: Any Meridian employee with specialized knowledge relevant to an active incident. SMEs are designated ad hoc by the PSIRT Lead and are relieved of normal duties for the duration of their engagement.

**Scribe**: A designated individual responsible for maintaining the chronological incident log during active response. For Critical severity incidents, a dedicated Scribe shall be assigned within 30 minutes of incident declaration. For all other severities, the PSIRT Lead may serve as Scribe or designate an alternate.

---

## 4. Policy Statements

### 4.1 Commitment to Timely Response

Meridian Health Technologies commits to responding to all reported product security incidents with urgency proportional to potential impact. The following response SLAs apply from the time of initial report or detection, whichever is earlier:

| Severity | Triage Max | Containment Target | Remediation Target |
|---|---|---|---|
| Critical | 1 hour | 4 hours | 72 hours |
| High | 4 hours | 24 hours | 7 days |
| Medium | 24 hours | 7 days | 30 days |
| Low | 5 business days | Next maintenance window | 90 days or next release |

These targets represent commitments; response activities shall commence immediately upon verification.

### 4.2 Confidentiality During Investigation

All incident-related information shall be handled on a strict need-to-know basis. Incident communication channels (Slack war rooms, video bridges, email threads) shall be restricted to personnel listed on the incident roster. Disclosure of incident details to unauthorized parties constitutes a separate security incident under this SOP.

### 4.3 Evidence Preservation

All forensic evidence collected during incident investigation shall be preserved in accordance with Meridian's evidence handling procedures. Chain of custody documentation shall be maintained for any evidence that may be required for legal proceedings. Digital evidence shall be stored in the dedicated, access-controlled S3 bucket `meridian-incident-evidence` with object lock enabled.

### 4.4 Non-Retaliation for Good-Faith Reporting

Meridian prohibits retaliation against any person who, in good faith, reports a suspected security incident or vulnerability. Reports made knowingly false or with malicious intent are not protected and may result in disciplinary action.

### 4.5 Continuous Improvement

Every Critical and High severity incident shall undergo a formal Post-Incident Review (PIR) process resulting in documented findings and assigned remediation action items tracked to completion in Jira. Medium severity incidents shall undergo a lightweight retrospective.

---

## 5. Detailed Procedures

This section constitutes the operational core of this SOP. All PSIRT members shall be familiar with these procedures and shall execute them as written unless an approved exception (Section 8) has been granted.

### 5.1 Phase 1: Detection and Intake

Security incidents enter the response pipeline through one of four primary channels. Each channel has defined ingestion procedures.

#### 5.1.1 Automated Detection (SIEM and Monitoring)

The Meridian Security Operations Team (SOT) operates a 24/7 security monitoring capability leveraging the following detection systems:

- **SIEM Platform**: Splunk Enterprise Security, ingesting logs from all product AWS accounts, API gateways, container runtime logs, and database audit trails. Correlation rules are maintained in the Meridian Detection Engineering repository (`gitlab.internal/security/detection-rules`).
- **EDR**: CrowdStrike Falcon deployed on all production EC2 instances and container hosts.
- **DLP**: Data loss prevention sensors at egress points of all product VPCs.
- **Runtime Anomaly Detection**: Falco agents within all production Kubernetes clusters.

When an alert fires with confidence ≥ 85% (per the Splunk risk scoring model) or any alert from the `product_security_critical` index, the SOT on-call analyst shall:

1. Acknowledge the alert in the PagerDuty console within 5 minutes.
2. Create a preliminary incident ticket in Jira Service Management (project `SEC`) with the following populated:
   - Summary field: Alert name plus affected resource
   - Severity: Initial assignment per alert rule
   - Environment: `prod-us-east-1` or `prod-eu-west-1` as applicable
   - Labels: `source:automated`, alert rule ID
3. Attach the Splunk notable event JSON export to the Jira ticket.
4. Post a summary to Slack channel `#psirt-alerts` including Jira ticket link.
5. If the alert severity is Critical, immediately page the PSIRT Lead via PagerDuty escalation policy `PSIRT-OnCall`.

#### 5.1.2 Vulnerability Disclosure Program (VDP)

Meridian operates a Vulnerability Disclosure Program accepting reports from external security researchers. Reports are received via:

- **HackerOne Platform**: `https://hackerone.com/meridian-health`
- **Email**: `security@meridian-health.com` (monitored by SOT during business hours ET; automated acknowledgement sent)
- **Encrypted Submission**: Via the Meridian Security Portal using the PGP public key published at `https://meridian-health.com/security/pgp-key.asc`

Upon receipt of an external report, the SOT intake analyst shall:

1. Send an automated acknowledgement within 15 minutes via the HackerOne platform or return email.
2. Perform an initial validity assessment within 4 business hours to filter obviously invalid or spam submissions.
3. For valid-appearing submissions, create a Jira ticket in project `SEC` with label `source:external-vdp` and forward to the PSIRT Lead for triage.
4. Acknowledge the reporter within 24 hours with an initial assessment status (valid, investigating, or invalid with brief justification).

#### 5.1.3 Internal Reporting

Any Meridian employee, contractor, or consultant who observes suspicious activity in product systems, or suspects a security incident has occurred, shall immediately report via one of:

- **Primary**: Slack channel `#security-incident-report` (monitored during all business hours; auto-escalation configured for off-hours)
- **Secondary**: Email to `security@meridian-health.com`
- **Emergency**: Phone bridge +1-555-0199 (published in the Meridian emergency contacts list)

The reporter shall provide, at minimum:
- Nature of the observed anomaly
- Time first observed
- Affected systems or services (resource identifiers, URLs, or service names)
- Screenshot or log excerpt if available
- Whether any PHI or payment data may be involved

Upon receipt, SOT shall acknowledge within 30 minutes during business hours or 2 hours off-hours, and shall create a Jira ticket labelled `source:internal-report`.

#### 5.1.4 Third-Party and Partner Notification

Meridian may receive notifications of potential product security incidents from hosting providers (AWS, Azure), security vendors, penetration testing firms, or business partners. (See Section 8 for additional handling when notification originates outside established partner channels.)

Upon receipt, the SOT analyst shall log the notification in Jira with label `source:external-partner` and immediately notify the PSIRT Lead.

### 5.2 Phase 2: Triage and Declaration

The triage phase determines whether a reported event constitutes a security incident requiring formal response under this SOP. The PSIRT Lead (or designated delegate for Medium/Low severity reports) leads triage.

#### 5.2.1 Triage Procedure

1. **Evidence Collection**: Within the applicable triage SLA timeframe, the PSIRT Lead shall gather:
   - The original alert or report
   - Relevant log excerpts from Splunk (search time range: ±2 hours from reported event time)
   - AWS CloudTrail events for the affected account(s) for the relevant time window
   - Kubernetes audit logs from the affected cluster(s)
   - Any relevant CrowdStrike Falcon detections
   - Screenshots or exported dashboards from Datadog APM and infrastructure monitoring showing anomalous patterns

2. **Severity Assessment**: The PSIRT Lead shall assign severity per the definitions in Section 2.1 using the following decision tree:
   - Does the event involve confirmed or highly likely unauthorized access to PHI or payment card data? → Critical
   - Does the event involve active exploitation or weaponized proof-of-concept exploit available? → High (minimum)
   - Does the event enable privilege escalation to cluster-admin or equivalent? → High
   - Is the event a vulnerability in a publicly-facing service with CVSS ≥ 9.0? → High (incident if exploitation indicators found)
   - All other confirmed events → Assign Medium or Low per impact assessment

3. **Declaration Decision**: If the PSIRT Lead determines an event qualifies as a security incident:
   - For **Critical**: Immediately (within 15 minutes of determination) declare the incident and initiate Phase 3. Simultaneously notify the Incident Commander, CISO, VP of Engineering, and General Counsel.
   - For **High**: Declare within 30 minutes of determination and initiate Phase 3. Notify CISO and VP of Engineering.
   - For **Medium**: Declare within 2 hours and initiate Phase 3 or schedule within next business day based on operational impact.
   - For **Low**: Log in Jira for inclusion in next patch cycle; no formal incident declaration required unless evidence of exploitation emerges.

4. **False Positive Closure**: If triage determines the event is a false positive, the PSIRT Lead shall:
   - Document the false positive determination rationale in the Jira ticket
   - If a detection rule generated the alert, create a tuning request in Jira project `SEC` labelled `detection-tuning`
   - Close the ticket with resolution "False Positive"

#### 5.2.2 Incident Declaration Template

Upon declaring an incident, the PSIRT Lead shall populate the following template in the Jira ticket:

```
INCIDENT DECLARATION
Incident ID: [Jira Ticket #]
Declared By: [Name]
Date/Time Declared: [ISO8601 timestamp]
Severity: [Critical/High/Medium]
Incident Type: [Unauthorized Access / Malware / Data Exfiltration / Service Disruption / Vulnerability Exploitation / Misconfiguration / Other]
Affected Product(s): [Clinical AI / HealthPay / MedInsight / SaaS Platform]
Affected Environment(s): [prod-us-east-1 / prod-eu-west-1 / staging / Azure-DR]
Summary of Impact: [Concise description]
Data at Risk: [PHI / Payment / None Identified / Under Investigation]
War Room Channel: #incident-war-[Jira ticket number]
Incident Commander: [Name if assigned; TBD if pending]
```

#### 5.2.3 War Room Activation

For Critical and High severity incidents, the PSIRT Lead shall immediately activate a war room:

1. Create Slack channel `#incident-war-[Jira ticket number]` (public within Meridian workspace; invite restricted to rostered personnel).
2. Pin the incident declaration template, the Jira ticket link, and the current runbook to the channel.
3. Create a Zoom bridge dedicated to the incident.
4. Post the bridge link, dial-in, and passcode to the channel.
5. Initiate a running chronological log (Google Doc in the `Incident Response` shared drive folder `PSIRT/Active/[Year]/[Incident ID]-chronolog`).

### 5.3 Phase 3: Containment

Containment actions prevent an incident from expanding in scope or impact. The Incident Commander (or PSIRT Lead if no Commander has been designated) authorizes containment actions.

#### 5.3.1 Containment Strategy Selection

The response team shall select containment actions based on incident type. The following table provides decision guidance:

| Incident Type | Primary Containment | Secondary Containment |
|---|---|---|
| Unauthorized Access (credential compromise) | Revoke all sessions for affected IAM principals; rotate credentials | Restrict source IPs to Meridian VPN range; assess lateral movement |
| Unauthorized Access (exploitation of vulnerability) | Isolate affected hosts from network at security group level | Apply WAF rules to block exploit pattern; begin patch deployment |
| Malware / Ransomware | Isolate affected EC2 instances (remove from all security groups except dedicated forensics SG); snapshot EBS volumes for forensics | Block associated IoCs at network edge via VPC Network Firewall |
| Data Exfiltration (suspected) | Revoke all non-essential IAM access from suspected compromised principals; enable S3 Block Public Access at account level if not already enforced | Engage AWS Support to analyze CloudTrail for data transfer anomalies |
| Service Availability (DDoS or resource exhaustion) | Engage AWS Shield Advanced response; deploy rate-limiting at API Gateway | Scale infrastructure; activate CDN caching for static assets |
| CI/CD Pipeline Compromise | Immediately revoke all pipeline service account credentials; freeze deployments to production | Isolate build agents; scan artifact repository for tampered artifacts |

#### 5.3.2 Critical Severity Containment Actions

For Critical severity incidents, the Incident Commander has pre-authorized authority to execute the following containment actions without additional approval, provided they are documented in the incident log within 15 minutes of execution:

1. **Service Isolation**: Modify AWS security groups or network ACLs to restrict ingress to affected services. For the CDSS API, deploy the "Emergency Read-Only Mode" feature toggle (`feature_flag.emergency_readonly = true`), which disables all POST/PUT/DELETE operations while preserving GET for clinical query continuity.
2. **Credential Revocation**: Revoke all active IAM access keys, console sessions, and temporary credentials for IAM principals associated with the affected environment. Issue emergency break-glass credentials to designated responders only.
3. **Database Access Restriction**: For RDS instances containing PHI, apply a temporary security group that restricts connections to the bastion host and designated forensic analysis hosts only.
4. **Pipeline Freeze**: Trigger the `emergency-pipeline-freeze` Jenkins job, which revokes deployment permissions for all service accounts except the `prod-incident-response` account.

#### 5.3.3 Evidence Collection During Containment

Before destructive containment actions (terminating instances, deleting resources), the response team shall:

1. Take EBS snapshots of all volumes attached to affected instances (tag: `MeridianIncidentID=<Jira Ticket>`).
2. Export CloudTrail logs for the affected account covering the 72 hours preceding the incident to the `meridian-incident-evidence` S3 bucket.
3. Capture memory dumps from affected Linux instances using the CrowdStrike Falcon real-time response capability.
4. Export all relevant Kubernetes pod logs from the affected cluster to CloudWatch and then to the evidence S3 bucket.
5. Screenshot all relevant Datadog dashboards and Splunk dashboards at the time of containment.

#### 5.3.4 Containment Verification

After executing containment actions, the response team shall verify containment effectiveness:

1. Monitor Splunk for 30 minutes (Critical) or 60 minutes (High) to confirm no additional malicious activity originating from affected systems.
2. Verify that all revoked credentials cannot be used to access Meridian systems (execute test authentication attempts with revoked credentials and confirm denial).
3. Confirm that isolated systems are not communicating on any unauthorized ports via VPC Flow Logs analysis.
4. Document the verification results in the incident Jira ticket.

### 5.4 Phase 4: Investigation and Eradication

Once containment is verified, the investigation phase determines the root cause, scope of compromise, and required eradication actions.

#### 5.4.1 Forensic Investigation Procedure

1. **Establish Investigation Timeline**: The PSIRT Lead, with forensic analyst support, shall construct a timeline of attacker activity based on correlation of:
   - AWS CloudTrail events (API calls, console logins)
   - VPC Flow Logs (network communications)
   - Kubernetes audit logs (API server interactions)
   - Application logs from Datadog
   - Database audit logs (RDS PostgreSQL `pgAudit` logs)
   - EDR telemetry from CrowdStrike Falcon

2. **Scope Determination**: Determine:
   - Initial access vector (how did the attacker gain access?)
   - Persistence mechanisms established
   - Privilege escalation paths exploited
   - Lateral movement between systems
   - Data accessed or exfiltrated (specific databases, tables, S3 buckets, and object counts)
   - Whether patient safety was impacted (for CDSS incidents, engage Clinical Safety Officer)

3. **Root Cause Identification**: Classify root cause into one of the following categories:
   - Unpatched vulnerability (CVE-ID if known)
   - Misconfiguration (specific resource and configuration error identified)
   - Credential compromise (phishing, credential theft, weak credential, etc.)
   - Insider action (malicious or accidental)
   - Supply chain compromise
   - Zero-day exploitation
   - Other (detailed narrative required)

4. **Indicator of Compromise (IoC) Extraction**: Identify and document all IoCs including:
   - IP addresses (source and any callback destinations)
   - Domain names
   - File hashes (SHA-256)
   - Mutex or registry key artifacts (Windows workloads)
   - Specific IAM role or user ARNs abused
   - Specific API call patterns

#### 5.4.2 Eradication Actions

Based on investigation findings, the response team shall execute eradication:

1. **Remove Persistence Mechanisms**: Delete unauthorized IAM users/roles, remove unauthorized SSH keys from authorized_keys files, delete cron jobs or systemd timers added by attacker, revoke any OAuth tokens issued to attacker-controlled applications.
2. **Patch Root Cause Vulnerability**: Deploy the remediation patch through the emergency change process (SOP-CHG-002, Emergency Change Management). For Critical incidents, the standard CAB approval is waived for patches directly related to the incident; the VP of Engineering or CISO retrospective approval suffices.
3. **Rebuild Compromised Systems**: All systems that experienced unauthorized modification shall be rebuilt from known-good AMIs or container images. The rebuild shall use infrastructure-as-code (Terraform modules) to ensure configuration consistency. Manual remediation ("cleaning") of compromised systems is prohibited.
4. **Rotate All Credentials**: All credentials, secrets, API keys, and certificates that existed in the affected environment during the compromise window shall be rotated, regardless of whether they were known to have been accessed.
5. **Scan for Residual Artifacts**: Run the Meridian "Post-Incident Cleanup" scanning suite (AWS Systems Manager Automation document `SSM-Meridian-PostIncidentScan`) against all resources in the affected account, which checks for newly created IAM principals, security group rules allowing `0.0.0.0/0`, unencrypted S3 buckets, and unauthorized Route53 entries.

#### 5.4.3 Model-Specific Investigation (Clinical AI and HealthPay AI/ML)

For incidents potentially involving AI/ML model tampering, model inversion, or adversarial input, the ML Model Security Lead shall:

1. Retrieve model serving logs from the SageMaker endpoint CloudWatch log group.
2. Compare the checksum (SHA-256) of the production model artifact against the known-good checksum recorded in the model registry (MLflow) at the time of approved deployment.
3. For CDSS models with CE marking under EU MDR, verify that the model version in production matches the approved technical documentation version. Any discrepancy shall be escalated immediately.
4. Run the adversarial robustness test suite (`meridian-mlsec/adversarial-tests/`) against the model artifact, and compare results against baseline scores stored in the model card repository.

### 5.5 Phase 5: Recovery

Recovery returns affected services to normal operation with verified security posture.

#### 5.5.1 Service Restoration Procedure

1. **Restoration Readiness Checklist**: Before restoring any service, complete the following:
   - [ ] All identified IoCs addressed
   - [ ] Affected systems rebuilt from known-good images
   - [ ] All credentials rotated
   - [ ] Root cause vulnerability patched
   - [ ] Security monitoring rules updated to detect similar activity
   - [ ] Penetration testing of remediated service performed (Critical/High only; may be abbreviated time-boxed test if full assessment timeline conflicts with recovery SLA)
   - [ ] Approval from Incident Commander and CISO for restoration

2. **Phased Restoration**:
   - **Phase A (Internal Validation)**: Restore service within a restricted VPC accessible only to Meridian internal validation tools. Run the full CI/CD integration test suite, plus the Meridian Security Validation Suite (`meridian-secval`). Confirm no anomalous behavior.
   - **Phase B (Canary Deployment)**: Route 5% of production traffic (or 5% of customer tenants) to the restored service. Monitor error rates, latency, and security telemetry for 30 minutes (Critical) or 2 hours (High).
   - **Phase C (Full Restoration)**: If canary metrics are nominal, restore full traffic. Update service health status in the Meridian StatusPage (`status.meridian-health.com`).

3. **Post-Restoration Monitoring**: Enhanced monitoring shall remain in place for 72 hours (Critical), 24 hours (High), or through the next business day (Medium). This includes:
   - Additional Splunk correlation rules activated for the affected service
   - CrowdStrike Falcon in "Aggressive" prevention policy mode
   - Hourly manual review of CloudTrail logs by SOT analyst
   - API Gateway WAF in "Block" mode for all OWASP Top 10 rule groups

### 5.6 Phase 6: Post-Incident Activities

#### 5.6.1 Post-Incident Review (PIR)

For Critical and High severity incidents, the PSIRT Lead shall schedule a PIR meeting within 5 business days of incident closure. The meeting shall include all personnel listed as Responsible or Accountable in the RACI matrix for the relevant phases, plus any SMEs involved.

The PIR shall produce a written report (stored in the Meridian Confluence space `PSIRT/Post-Incident-Reviews`) containing:

1. **Incident Summary**: Timeline of events from first detection through closure
2. **Root Cause Analysis**: Detailed root cause with contributing factors
3. **Impact Assessment**: Systems, data, and users affected; quantification where possible (records exposed, service downtime minutes, financial impact)
4. **Response Effectiveness**: Assessment against SLA targets; what worked well, what did not
5. **Action Items**: Specific, assigned improvements to people, process, or technology with target completion dates. Action items shall be tracked in Jira project `SEC` with label `post-incident-action`.

#### 5.6.2 Detection Rule Feedback

For any incident where detection was delayed relative to the actual compromise timeline, the SOT Detection Engineering team shall:

1. Analyze the detection gap
2. Develop and test new or modified detection rules
3. Deploy updated rules to the SIEM within 30 days (Critical/High) or 60 days (Medium)

---

## 6. Controls and Safeguards

### 6.1 Access Controls

All product systems that process, store, or transmit PHI or payment card data shall enforce multi-factor authentication (MFA) using the Meridian Okta identity provider with the Duo Security MFA adapter. IAM policies shall follow the principle of least privilege, with role-based access control (RBAC) defined per the Meridian Access Management Standard. All production IAM roles shall be reviewed quarterly by the Cloud Security team; any role with `*` resource permissions shall be flagged for remediation within 30 days.

Service-to-service authentication within the product mesh shall use mutual TLS (mTLS) with short-lived certificates issued by the HashiCorp Vault PKI engine. Certificate lifetimes shall not exceed 24 hours.

Access to the incident evidence S3 bucket (`meridian-incident-evidence`) shall be restricted to members of the `sec-ir-investigators` IAM group plus the PSIRT Lead. All access to this bucket shall be logged via S3 server access logs to a separate, immutable logging bucket.

### 6.2 Audit Logging and Monitoring

All product systems shall forward security-relevant logs to the centralized Splunk indexer cluster. At minimum, the following log sources shall be ingested:

- AWS CloudTrail (all accounts, all regions, management and data events for S3 buckets containing PHI)
- VPC Flow Logs (all VPCs, `ALL` traffic, published to CloudWatch Logs and forwarded to Splunk)
- Kubernetes API server audit logs (all clusters)
- Application-level access logs from all product services (structured JSON format including `user_id`, `action`, `resource`, `timestamp`, `source_ip`, `user_agent`)
- Database audit logs (PostgreSQL `pgAudit` extension logging all DDL and DML operations on tables containing PHI)
- CI/CD pipeline execution logs (Jenkins, GitHub Actions audit log)

Log retention in Splunk shall be 90 days hot, 365 days warm, and 7 years cold in AWS S3 Glacier Deep Archive.

### 6.3 Encryption

All PHI and sensitive data at rest shall be encrypted using AES-256. AWS KMS customer-managed keys (CMKs) shall be used for all encryption operations; AWS-managed keys are not acceptable for PHI data stores. Key rotation shall be enforced annually per the Meridian Key Management Standard (SOP-SEC-009).

Data in transit shall be encrypted using TLS 1.2 or higher. TLS 1.0 and 1.1 are explicitly prohibited. All product-facing TLS certificates shall be issued by the Meridian internal CA (Vault PKI) or AWS Certificate Manager. Self-signed certificates are prohibited in production.

### 6.4 Network Segmentation

The product environment shall be segmented into the following security zones, enforced by AWS security groups and Network ACLs:

- **Presentation Zone**: Public-facing API Gateway, CloudFront distributions, WAF
- **Application Zone**: EKS worker nodes, EC2 instances running application code, Lambda functions within VPC
- **Data Zone**: RDS instances, ElastiCache clusters, OpenSearch domains, S3 buckets containing PHI
- **Management Zone**: Bastion hosts, CI/CD deployment agents, monitoring collectors

Traffic between zones shall be restricted to explicitly defined ports and protocols. The Data Zone shall not accept inbound connections initiated from the Presentation Zone. All Data Zone connections shall originate from the Application Zone or Management Zone only.

### 6.5 Patch and Vulnerability Management

All product systems shall be subject to the Meridian Vulnerability Management Program (SOP-SEC-012). Critical and High severity vulnerabilities identified in product systems shall be remediated per the following timelines:

| CVSS Score | Remediation Timeline |
|---|---|
| 9.0 – 10.0 | 72 hours |
| 7.0 – 8.9 | 7 days |
| 4.0 – 6.9 | 30 days |
| 0.1 – 3.9 | 90 days |

Vulnerability scanning of all product AWS accounts shall be performed weekly using the Meridian-deployed AWS Inspector configurations augmented by the Qualys vulnerability management platform. Scan results shall be aggregated in the Splunk Vulnerability Management dashboard.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators

The following KPIs measure the effectiveness of the product security incident response program:

| KPI | Target | Measurement Method |
|---|---|---|
| Mean Time to Detect (MTTD) — Critical/High | < 4 hours | Delta between earliest compromise indicator timestamp (determined during investigation) and detection timestamp |
| Mean Time to Triage (MTTT) | < SLA targets in Section 4.1 | Delta between detection/report timestamp and incident declaration timestamp |
| Mean Time to Contain (MTTC) — Critical | < 4 hours | Delta between declaration timestamp and containment verification timestamp |
| Containment Success Rate | > 98% | Percentage of declared incidents where initial containment actions prevented scope expansion |
| PIR Completion Rate — Critical/High | 100% within 10 business days | PIR report published date vs. incident closure date |
| Post-Incident Action Item Completion | 90% within target dates | Jira `post-incident-action` tickets resolved on or before due date |
| External Reporter Acknowledgement Time | < 24 hours for all valid reports | HackerOne platform metrics or email timestamp delta |
| False Positive Rate — Critical Alerts | < 10% | False positives / total Critical alerts during measurement period |

### 7.2 Dashboards

The SOT shall maintain the following real-time dashboards in Splunk:

- **PSIRT Operations Dashboard**: Active incidents, response phase, elapsed time vs. SLA targets, assigned responders
- **Vulnerability Disclosure Dashboard**: Incoming reports, triage status, bounty status, time-in-state
- **Detection Coverage Dashboard**: Product systems covered by detection rules, detection rule performance metrics (precision, recall), detection gap tracking
- **Post-Incident Action Tracker**: Open action items, owner, due date, aging from target date

Access to the PSIRT Operations Dashboard shall be restricted to the PSIRT Core Team, CISO, VP of Engineering, and CTO. Access to the Vulnerability Disclosure Dashboard (aggregate statistics only; individual reports masked) shall be available to all Product & Engineering personnel.

### 7.3 Reporting Cadence

| Report | Audience | Frequency | Owner |
|---|---|---|---|
| PSIRT Operations Metrics | CISO, VP of Engineering | Monthly | PSIRT Lead |
| Product Security Incident Summary | CTO, Platform Leads | Quarterly | PSIRT Lead |
| Executive Security Dashboard | CEO, Board of Directors | Quarterly | CISO |
| Vulnerability Disclosure Program Metrics | CISO, VP of Engineering | Monthly | VDP Manager |
| Customer-Facing Security Summary | Enterprise customers (upon request via TAM) | Quarterly | CISO |

### 7.4 Breach Notification Reporting

In the event of unauthorized access to PHI or other protected data, the PSIRT Lead shall immediately notify the General Counsel and CISO. The Office of the General Counsel shall determine regulatory notification obligations and shall lead all external notifications. Security incident details required for regulatory filings shall be provided by the PSIRT Lead within 24 hours of request.

---

## 8. Exception Handling and Escalation

### 8.1 Exception to SLA Timelines

Circumstances may arise that prevent meeting the SLA targets defined in Section 4.1. Valid circumstances include:

- Active law enforcement investigation requesting delay of remediation actions
- Vendor or third-party dependency for patch availability
- Remediation would cause patient safety risk (determined by Chief Medical Officer in consultation with the clinical engineering team)
- Unavailability of critical personnel due to circumstances beyond Meridian's control

Any SLA exception shall be:

1. Documented in the incident Jira ticket with specific justification and expected new timeline
2. Approved by the CISO for Critical/High incidents; approved by the PSIRT Lead for Medium incidents
3. Reviewed at the next PIR if applicable

### 8.2 Escalation Matrix

If incident response stalls due to resource constraints, lack of decision-making authority, or inter-team conflict, the following escalation path shall be used:

| Escalation Level | Escalate To | When to Escalate |
|---|---|---|
| Level 1 | Incident Commander (if not already engaged) | Response team blocked on tactical decision; resource contention between response activities |
| Level 2 | VP of Engineering (David Park) + CISO (Jane Matsumoto) | Cross-team conflict not resolved by Incident Commander; external communications decision needed; significant resource commitment required |
| Level 3 | CEO (Dr. Sarah Chen) | Incident poses existential risk to Meridian; decision involves potential public safety impact for CDSS; legal counsel advises executive-level decision required |

Any member of the response team may initiate escalation without fear of reprisal.

### 8.3 Runbook Deviation

During active incident response, responders may need to deviate from published runbooks due to unique incident characteristics. All deviations shall be:

1. Authorized by the Incident Commander or PSIRT Lead (whichever is senior on-scene)
2. Logged in the incident chronolog with rationale
3. Reviewed during the PIR for potential runbook updates

### 8.4 Exception Approval Authority

For non-incident (steady-state) exceptions to the controls described in Section 6, the following approval authorities apply:

| Control Category | Approver |
|---|---|
| Access control exceptions (elevated privileges) | CISO |
| Encryption exceptions | CISO + Chief Medical Officer (if PHI involved) |
| Network segmentation exceptions | VP of Engineering |
| Patch timeline extensions | CISO or delegate |

All exceptions shall be time-limited (maximum 90 days before renewal review), documented in Jira (`SEC` project, issue type `Exception`), and tracked on the Compliance Exceptions Register.

---

## 9. Training Requirements

### 9.1 Role-Based Training Requirements

| Role | Training Module | Frequency | Delivery Method |
|---|---|---|---|
| **PSIRT Core Team** | Advanced Incident Response Workshop | Annual | Instructor-led (3-day in-person) |
| **PSIRT Core Team** | Meridian CDSS Forensics (Clinical AI-specific) | Annual | Instructor-led (1-day virtual) |
| **PSIRT Core Team** | Tabletop Exercise Participation | Quarterly | Facilitated tabletop |
| **All SOT Analysts** | Product Security Monitoring and Triage | Annual | eLearning (LMS course SEC-201) |
| **Platform Leads (all products)** | Incident Response for Platform Owners | Annual | eLearning (LMS course SEC-202) |
| **VP of Engineering, CISO, GC** | Executive Incident Decision-Making | Annual | Instructor-led (2-hour virtual) |
| **All Product & Engineering personnel** | Security Incident Reporting Awareness | Annual | eLearning (LMS course SEC-100) |
| **All new hires (Product & Engineering)** | Security Incident Reporting (onboarding) | Once, within first week | eLearning (LMS course SEC-100) |

### 9.2 Tabletop Exercise Requirements

Quarterly tabletop exercises shall be designed and facilitated by the PSIRT Lead or an external incident response retainer firm under contract to Meridian. Each exercise shall:

1. Simulate a realistic product security incident scenario
2. Exercise specific phases of this SOP as designated in the exercise plan
3. Include participants from Product & Engineering, SOT, Legal, and Communications per the scenario
4. Produce an After-Action Report identifying gaps and improvement recommendations
5. Generate Jira action items for each identified improvement, tracked to completion

Exercise scenarios shall rotate across the product portfolio such that each major product (Clinical AI, HealthPay, MedInsight, SaaS Platform) is the subject of at least one exercise annually.

### 9.3 Training Compliance Tracking

Training completion shall be tracked in the Meridian Learning Management System (Workday Learning). The PSIRT Lead shall review training compliance quarterly:

- PSIRT Core Team: 100% compliance required; non-compliance results in removal from on-call rotation
- SOT Analysts: 95% compliance required
- All other roles: 90% compliance required

Personnel not meeting compliance thresholds shall be notified and given 30 days to remediate. Continued non-compliance shall be escalated to the individual's manager and the CISO.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship |
|---|---|---|
| SOP-IT-007 | Corporate IT Incident Response | Separate incident response for non-product IT environments |
| SOP-SEC-009 | Key Management and Cryptographic Controls Standard | Governs encryption key lifecycle referenced in Section 6.3 |
| SOP-SEC-012 | Vulnerability Management Program | Governs steady-state vulnerability scanning and remediation |
| SOP-CHG-002 | Emergency Change Management | Governs emergency change approval for patch deployment during incidents |
| SOP-PRIV-004 | Privacy Breach Management | Coordinates privacy breach response that may overlap with security incidents |
| SOP-CLIN-007 | Clinical AI Safety Incident Management | Governs clinical safety incidents potentially caused by security compromise |
| SOP-HR-011 | Employee Relations Investigations | Governs insider investigations coordinated with PSIRT |
| SOP-ENG-005 | CI/CD Pipeline Security | Governs pipeline security controls referenced in Section 5.3 |
| SOP-CLOUD-003 | AWS Account Security Baseline | Defines baseline security configurations for all product AWS accounts |

### 10.2 External References

| Reference | Applicability |
|---|---|
| NIST SP 800-61 Rev. 2 (Computer Security Incident Handling Guide) | Incident response lifecycle framework |
| NIST AI RMF 1.0 (AI Risk Management Framework) | Governance for AI/ML model incidents |
| ISO/IEC 27035:2016 (Information security incident management) | International standard alignment |
| AWS Security Incident Response Guide | Cloud-specific IR procedural reference |
| CVSS v3.1 Specification Document | Severity scoring methodology |

---

## 11. Revision History

| Version | Effective Date | Author | Summary of Changes |
|---|---|---|---|
| 1.0 | 2021-06-15 | J. Park (former VP Eng) | Initial publication |
| 1.1 | 2022-01-20 | M. Torres (SOT Lead) | Added VDP intake procedures; expanded detection rule feedback loop |
| 1.3 | 2022-08-12 | K. Nakamura (PSIRT Lead) | Incorporated Clinical AI platform specifics; updated severity classification for ML model incidents |
| 1.5 | 2023-03-07 | K. Nakamura (PSIRT Lead) | Major revision: restructured Phase 3 containment actions; added Evidence Collection subsection; updated escalation matrix to include CEO level |
| 1.6 | 2023-07-19 | D. Park (VP Eng); K. Nakamura | Updated role assignments post-org change; added MedInsight-specific triage criteria; revised dashboard access controls |
| 1.7 | 2024-01-11 | K. Nakamura (PSIRT Lead) | Added CI/CD pipeline compromise procedures; updated SLA targets per 2023 incident metrics analysis; expanded training requirements for new platform leads |
| 1.8 | 2024-06-03 | D. Park (VP Eng) | Incorporated EU MDR CE marking requirements into model verification procedures; added Azure DR to containment decision matrix |
| 1.9 | 2024-10-23 | D. Park; K. Nakamura; Legal review (M. Okonkwo) | Full annual review. Updated CVSS references to v3.1 throughout. Clarified Phase 3 authorization for Critical incidents. Added non-retaliation policy statement. Updated breach notification coordination language. Current version. |
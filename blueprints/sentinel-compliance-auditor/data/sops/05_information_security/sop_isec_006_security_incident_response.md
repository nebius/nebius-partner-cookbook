---
sop_id: "SOP-ISEC-006"
title: "Security Incident Response"
business_unit: "Information Security"
version: "4.3"
effective_date: "2025-09-27"
last_reviewed: "2026-07-04"
next_review: "2027-01-18"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
  - "GDPR"
status: "Active"
---

## 1. Purpose and Scope

This Standard Operating Procedure (SOP) establishes the framework for Meridian Health Technologies, Inc. personnel to identify, classify, contain, eradicate, and recover from security incidents. This SOP is designed to ensure that Meridian protects the confidentiality, integrity, and availability of its information systems and data, notably protected health information (PHI) processed by the MedInsight Analytics platform, Clinical AI Platform, and HealthPay Financial Services, as well as personal data processed by all business lines on behalf of EU data subjects.

The scope of this SOP encompasses all Meridian business units, including all wholly-owned subsidiaries and offices in Boston, London, Berlin, Singapore, and Toronto. It applies to all corporate assets, cloud infrastructure (AWS us-east-1 and eu-west-1, Azure DR), endpoints, on-premises devices, SaaS applications, and the data contained within them. All employees, contractors, interns, consultants, and third-party service providers authorized to access Meridian systems are subject to the procedures outlined herein. This SOP covers all phases of the incident response lifecycle: preparation, detection and analysis, containment, eradication and recovery, and post-incident activity.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
| :--- | :--- |
| **Breach** | An impermissible use or disclosure under the HIPAA Privacy Rule that compromises the security or privacy of protected health information (PHI) such that the use or disclosure poses a significant risk of financial, reputational, or other harm to the affected individual. |
| **Critical Infrastructure** | Assets and systems vital to Meridian’s operations, including the AWS Virtual Private Cloud (VPC), Okta identity provider, Snowflake data warehouse, and production Kubernetes clusters running clinical AI workloads. |
| **Event** | Any observable occurrence in a system or network. A user connecting to a file share, a firewall allowing a connection, or an application logging a transaction. |
| **Incident** | An adverse event or series of related adverse events that compromises, or is suspected of compromising, the confidentiality, integrity, or availability of Meridian’s information assets, including a violation or imminent threat of violation of Meridian’s security policies, acceptable use policies, or standard security practices. |
| **Information Security Officer (ISO)** | A designated liaison within each business unit responsible for coordinating security activities with the central Information Security team. |
| **Personal Data** | Any information relating to an identified or identifiable natural person as defined under GDPR Article 4(1). |
| **Protected Health Information (PHI)** | Individually identifiable health information held or transmitted by a covered entity or its business associate, in any form or medium, as defined by HIPAA. |
| **Regulated Data** | A collective term for PHI, PCI cardholder data, and EU Personal Data requiring protections under GDPR. |
| **Security Operations Center (SOC)** | Meridian’s internal team within the Information Security department providing continuous monitoring of SIEM alerts, threat intelligence, and management of the Incident Response process. |

### 2.2 Acronyms

| Acronym | Definition |
| :--- | :--- |
| **BIA** | Business Impact Analysis |
| **CISO** | Chief Information Security Officer |
| **CMS** | Case Management System (Jira Service Management) |
| **CSIRT** | Computer Security Incident Response Team |
| **DMA** | Designated Market Area (Meridian’s internal term for a geographically isolated AWS region) |
| **DPO** | Data Protection Officer |
| **EDR** | Endpoint Detection and Response (CrowdStrike Falcon) |
| **HIPAA** | Health Insurance Portability and Accountability Act |
| **IdP** | Identity Provider (Okta) |
| **IRC** | Incident Response Coordinator |
| **NIST** | National Institute of Standards and Technology |
| **PII** | Personally Identifiable Information |
| **RPO** | Recovery Point Objective |
| **RTO** | Recovery Time Objective |
| **SAIM** | Security Analytics and Incident Management (Splunk platform) |
| **SIEM** | Security Information and Event Management |
| **SME** | Subject Matter Expert |
| **SOAR** | Security Orchestration, Automation, and Response (Splunk Phantom) |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Matrix

| Role | Title / Designation | Responsibility |
| :--- | :--- | :--- |
| **Incident Response Coordinator (IRC)** | Designated Manager, Security Operations | Manages the lifecycle of all Severity 1 and Severity 2 incidents. Coordinates CSIRT activities, maintains incident timeline, and acts as the central point of communication. |
| **CISO** | Rachel Kim | Executive owner of the IR program. Declares a state of incident, approves containment strategies, and authorizes notification procedures. |
| **Data Protection Officer (DPO)** | Dr. Klaus Weber | Advises on GDPR-specific notification obligations. Determines if an incident involving EU Personal Data constitutes a risk to data subjects' rights and freedoms. |
| **Chief Medical Officer** | Dr. Priya Patel | Determines the clinical impact and patient safety risks of incidents affecting the Clinical AI Platform. |
| **General Counsel** | Maria Gonzalez | Determines legal obligations, manages attorney-client privilege during investigations, and directs external communications to regulators. |
| **Privacy Officer** | Dr. Klaus Weber (acting) | Manages all HIPAA breach notification processes to affected individuals, the Secretary of HHS, and, where applicable, the media. |
| **VP of Engineering** | David Park | Provides application-level SMEs for the SaaS Platform and coordinates code-level remediation and patch deployment. |
| **Director of IT Operations** | Samantha Torres | Manages infrastructure-level containment and recovery actions across AWS, Azure, and corporate network environments. |
| **VP of Corporate Communications** | Michael Chang | Manages external media relations and official corporate statements following a confirmed data breach. |
| **Human Resources** | Jennifer Walsh | Manages investigations involving employee misconduct and coordinates sanctions. |

### 3.2 CSIRT Composition by Severity

The CSIRT is a dynamic team assembled based on the nature and severity of the incident. A standing core team is supplemented by specialized support.

- **Core CSIRT (All Incidents):** Incident Response Coordinator, Security Analysts from the SOC, Senior Infrastructure Engineer from IT Operations.
- **Extended CSIRT (Severity 1 & 2):** CISO, General Counsel, VP of Engineering, relevant Business Unit ISO.
- **Executive Advisory Group (Severity 1):** CEO, CFO, Chief AI Officer, Chief Medical Officer, DPO. This group does not direct tactical response but sets business risk tolerance parameters.

---

## 4. Policy Statements

Meridian Health Technologies is committed to a risk-based incident response framework designed to protect patient lives and sensitive data. The following high-level policy statements govern this SOP:

1.  **Confidentiality and Integrity First:** All response actions must prioritize the physical safety of patients and the preservation of the integrity of clinical data processed by FDA 510(k)-cleared and CE-marked diagnostic algorithms.
2.  **Timely Notification:** In the event of a Breach of Unsecured PHI, as defined by 45 CFR § 164.402, Meridian shall notify affected individuals without unreasonable delay and in no case later than 60 calendar days following discovery of the breach, in accordance with 45 CFR § 164.404.
3.  **Data Minimization:** Incident investigation data shall be strictly limited in use to security purposes and shall be retained in alignment with the principle of storage limitation under applicable law.
4.  **Non-Reprisal:** Meridian strictly prohibits retaliation against any employee who, in good faith, reports a security event or incident.

---

## 5. Detailed Procedures

This section outlines the sequential workflow for managing an incident, from initial declaration to final closure. All communication and decision points shall be documented in the official case record within Jira Service Management (CMS).

### 5.1 Incident Declaration and Classification

An incident may be declared by any Meridian employee or automatically by a security control (EDR, SAIM). Upon declaration, the SOC will triage the event within 15 minutes of notification.

#### 5.1.1 Classification Schema

Incidents are classified based on the intersection of a Technical Severity Matrix and a Business Impact Analysis (BIA). The Technical Severity is determined first; the final classification may be elevated by Business Impact.

**Table 1: Technical Severity Matrix**

| Severity | Criteria | Examples |
| :--- | :--- | :--- |
| **Severity 1 (Critical)** | Confirmed compromise of Critical Infrastructure; active lateral movement; ransomware execution; validated data exfiltration exceeding 10 GB. | An attacker has gained root access to a production EKS cluster worker node; an employee's Okta account is being used by a threat actor from a foreign IP to download PHI from Snowflake. |
| **Severity 2 (High)** | Suspected compromise of Critical Infrastructure; malware outbreak on >5 endpoints; confirmed phishing with business email compromise (BEC) financial elements. | A spear-phishing email led to a Senior Accountant revealing credentials to a spoofed login page; Ransomware has encrypted a shared corporate drive that is backed up. |
| **Severity 3 (Medium)** | Isolated malware on a single endpoint; successful social engineering without BEC; policy violation exposing credentials (non-CI). | A single developer workstation triggers a CrowdStrike alert for a PUP; an intern shares their Okta password over Slack. |
| **Severity 4 (Low)** | Failed brute-force attack; port scan; isolated phishing simulation failure. | A routine alert for a blocked SQL injection attempt on a non-production application. |

**Business Impact Elevators:** If any Severity 2-4 event carries a direct Business Impact Elevator, it must be upgraded to Severity 1.

- **Clinical Impact:** Any event that, in the professional judgment of the Chief Medical Officer, has the potential to alter or disrupt a patient diagnosis, treatment plan, or clinical outcome.
- **Patient Safety:** Any event resulting in unauthorized access to PHI for more than 500 individuals in a Designated Market Area.
- **Operational Paralysis:** Any event that takes the `www.meridian-health.com` patient portal, the `api.meridian.health` clinical AI endpoint, or the `pay.meridian.health` payment gateway offline for an estimated period exceeding 2 hours.

### 5.2 Incident Analysis and Investigation (Triage)

The SOC triage procedure follows a structured investigation workflow to scope the extent of an event.

1.  **Alert Verification (SAIM):** The analyst acknowledges the alert in Splunk SAIM and verifies its fidelity. This involves reviewing the linked raw log, querying CrowdStrike Falcon for corresponding process detail on the endpoint, and checking AWS CloudTrail for anomalous API calls from the source asset.
2.  **Scope Determination:** The analyst determines the blast radius by:
    - **Endpoint:** Identifying all hosts where the malicious binary hash (SHA256) executed, using CrowdStrike’s “Incidents” module.
    - **Network:** Analyzing VPC Flow Logs in Splunk for lateral movement patterns (e.g., RDP on port 3389, SSH on 22) from the patient-zero host.
    - **Identity:** Querying the Okta System Log for anomalous geo-location, impossible travel, or privilege escalation attempts for the compromised user principal.
3.  **Data Impact Assessment (HIPAA Analysis):** For any incident touching systems containing PHI, the following four-factor breach risk assessment is performed per 45 CFR § 164.402:
    - **Factor 1:** The nature and extent of the PHI involved (e.g., what exactly was accessed? Diagnosis codes, names, SSNs?).
    - **Factor 2:** The unauthorized person who used the PHI or to whom the disclosure was made (e.g., a cybercriminal syndicate vs. an accidental internal recipient who subsequently deleted it).
    - **Factor 3:** Whether the PHI was actually acquired or viewed (or if only the database was the target, without a successful data query).
    - **Factor 4:** The extent to which the risk to the PHI has been mitigated (e.g., strong encryption rendering data unusable).
4.  **Evidence Collection:** The analyst creates a forensically sound snapshot of the affected AWS EC2 instances (EBS volume), downloads an AMI disk image to an isolated Forensics VPC for deep-dive analysis, and quarantines the endpoint by pushing a “Network Contain” action through CrowdStrike.

### 5.3 Containment Strategy

Containment is an emergency response. The CISO must authorize any containment action that risks data integrity (e.g., pulling the power on a database server) or clinical availability.

| Incident Class | Containment Strategy | Implementation Tool |
| :--- | :--- | :--- |
| **Endpoint Malware** | Network contain the host. | CrowdStrike Falcon Host Management Console - "Network Contain" action. |
| **Compromised User** | Suspend user’s Okta account, force-sign-out of all active SAML/OIDC sessions, and invalidate all API tokens. | Okta Admin Console: `Suspend User` action; expire and rotate all PATs in AWS Secrets Manager. |
| **AWS Compute Compromise** | Isolate the EC2 instance into a dedicated "Quarantine" Security Group that denies all inbound/outbound traffic, removing it from any production ALB target groups. | AWS Systems Manager Runbook: `SOP-INF-004 - Critical Instance Isolation`. |
| **Data Loss Prevention (DLP) Violation** | Block the source IP at the web proxy Zscaler level; revoke source's OAuth2 tokens to Snowflake. | Zscaler Admin UI; Snowflake `ALTER USER ... ABORT ALL SESSIONS`; `SECURITY` role in Snowflake. |
| **Ransomware Outbreak (Severity 1)** | Initiate a DMA-wide network segmentation. Invoke the Critical Application Disaster Recovery plan, failing over the environment to a clean, isolated recovery VPC. | AWS Control Tower "Account Guardrail" deployment using AWS Organizations SCP to deny all actions except by break-glass admin role. |

### 5.4 Eradication Procedures

Eradication ensures the root cause of the incident is completely removed from the environment before restoration.

1.  **Technical Root Cause Removal:**
    - **Malware:** All traces of the malware and its persistence mechanisms (scheduled tasks, registry Run keys, launchd plists) must be surgically removed via CrowdStrike "Script/Remove" commands or by re-imaging the host. Re-imaging is mandatory for all Severity 1 and 2 incidents.
    - **Vulnerability:** If the incident was caused by an exploited vulnerability, the VP of Engineering must authorize an Emergency Patch Deployment, bypassing the standard change advisory board for all affected AMIs and containers.
    - **Account Compromise:** The compromised account password is force-reset. All associated MFA tokens are de-registered and re-enrolled. An audit of all activities logged against that account during the compromise window is conducted by the SOC.
2.  **Security Improvement:** The CSIRT identifies a flaw in a Meridian security control that allowed the event. A Security Remediation Ticket is created in Jira and assigned to the SOC Engineering team with a pre-defined Service Level Agreement (SLA) for implementation, based on the severity of the flaw (e.g., a missing firewall rule is a P2 ticket requiring a fix within 48 hours).

### 5.5 Recovery

Recovery actions restore validated, clean systems to a normal operational state.

1.  **System Restoration:** Systems are restored from the last known "clean" AMI snapshot or backup. The RPO for the critical patient database `medinsight-prod-rds` is 1 hour. The RTO is 4 hours per the production BIA.
2.  **Integrity Validation:** Before returning a system to service, a vulnerability scan must be completed, confirming the absence of the exploited vulnerability. For systems handling PHI, an application-level reconciliation is performed by the Engineering team to validate data integrity against Snowflake’s Time Travel feature.
3.  **Monitoring:** Restored systems are placed under an "Enhanced Monitoring" phase for a period of 1 week post-recovery. During this time, SAIM is configured to forward all related events to a dedicated Slack channel `#incident-critical-watch`.

---

## 6. HIPAA Controls and Safeguards for Breach Notification

This section outlines the specific procedural controls invoked when an incident is confirmed as a Breach of Unsecured PHI as defined under 45 CFR Part 164 Subpart D.

### 6.1 Breach Determination Team

A mandatory quorum convenes within 24 hours of a potential PHI breach being identified. The quorum consists of the CISO, Privacy Officer, General Counsel, and the Business Unit ISO whose unit was the source of the incident.

### 6.2 Individual Notification (45 CFR § 164.404)

Should the Breach Determination Team confirm a breach occurred, Meridian shall:

1.  **Notification Content:** Draft the individual notification letter containing a clear, plain-language description of:
    - What happened (categories of PHI and identifiers).
    - A brief description of Meridian’s investigation steps.
    - Steps the individual can take to protect themselves from potential harm (credit monitoring, etc.).
    - A direct phone number (1-800-MDN-PRVC) and web portal (`www.meridian.com/breach-response`) for affected individuals to inquire about the breach.
2.  **Delivery Method:** Notifications are sent via first-class mail to the last known address in the `medinsight-core` application system. Substitute notice via email is provided if the individual had opted into electronic communications for this purpose.
3.  **Timeline:** All first-class mail is postmarked within 55 calendar days of the discovery of the incident, ensuring clear compliance with the regulatory 60-day maximum.

### 6.3 Regulatory and Media Notification (45 CFR § 164.406 & 164.408)

- **Threshold Breach (>500 individuals):** The Privacy Officer shall notify the Secretary of Health and Human Services simultaneously with individual notification. The notification is submitted via the HHS OCR web portal, populating their standard breach reporting template.
- **Media Notice:** For a breach involving more than 500 residents of a single State or jurisdiction, a prominent media notification is issued as a press release distributed via PRNewswire in the relevant Designated Market Areas (DMA).

### 6.4 Breach Log

Meridian maintains a comprehensive, sanitized (for internal use) log of all impermissible uses and disclosures of PHI, regardless of whether they were determined to constitute a reportable Breach. This log is maintained by the Privacy Officer.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The Information Security team reports on the following metrics on a quarterly basis to the Chief Medical Officer, Chief AI Officer, and the Board Risk Committee.

| Metric Name | Target | Measurement Method |
| :--- | :--- | :--- |
| Mean Time to Detect (MTTD) - Severity 1 | < 60 minutes | (Time of first SOC acknowledgment) - (Time of earliest correlated SIEM log). |
| Mean Time to Contain (MTTC) - Severity 1 | < 240 minutes | (Time containment order executed) - (Time incident declared). |
| HIPAA Notification Timeline Delta | ≤ -5 days from limit | The calendar days before the legal deadline (60 days) that notification was completed. |
| Post-Incident Review Completion Rate | 100% | % of Severity 1 & 2 incidents with a completed and signed-off lessons-learned document within 30 days of closure. |

### 7.2 Reporting Cadence

| Report Name | Recipient | Frequency |
| :--- | :--- | :--- |
| Information Security Incident Metrics Dashboard (PowerBI) | CISO, CIO | Real-time |
| Executive Summary of Critical Incidents | CEO, CFO, GC, CMO, CAIO | Monthly |
| HIPAA Breach & Complaint Log Review | VP of Compliance | Quarterly |

---

## 8. Exception Handling and Escalation

Strict adherence to this SOP is required. Deviations from the defined procedures, particularly those around containment authority (Section 5.3) and notification timelines (Section 5.5), are not permitted without documented executive approval.

### 8.1 Exception Handling Process

1.  An exception request is raised by the person requesting a deviation from standard procedure. This request is a formal, written communication submitted to the CISO.
2.  The justification must be based on specific, documented circumstances. For example, a request to delay isolating a compromised clinical AI inference node because it is currently supporting a live, interventional radiology procedure would constitute a valid clinical-safety-based exception.
3.  The CISO, in consultation with the relevant stakeholder (e.g., Chief Medical Officer for clinical impacts), evaluates the risk of the deviation within 1 business hour of the request.
4.  If approved, the exception, its justification, a compensating control plan, and a specific expiry time are documented in the incident's official Jira record. An exception can only be granted for a finite duration, not to exceed 72 hours, after which standard SOP procedures must be reinstated.

---

## 9. Training Requirements

A well-trained response team is the foundational layer of this procedure.

### 9.1 Role-Based Training Curriculum

| Target Audience | Training Module | Frequency | Tracking Method |
| :--- | :--- | :--- | :--- |
| All Staff (Employee & Contractor) | `SEC-GEN-001: Recognizing and Reporting Phishing` | Annually | Absorb LMS |
| Software Engineers | `SEC-DEV-003: OWASP Top 10 & Secure Coding` | Bi-Annually | Absorb LMS |
| CSIRT Core Team & ISOs | `SOP-ISEC-006-T1: Technical Live-Fire Incident Drill` | Quarterly | Instructor Sign-off |
| Executive Advisory Group | `CRISIS-EXEC-001: Tabletop Crisis Communication` | Bi-Annually | Instructor Sign-off, led by independent incident response retainer firm |

### 9.2 CSIRT Drills

The quarterly live-fire drill (`SOP-ISEC-006-T1`) is a mandatory, hands-on exercise conducted on a Meridian-owned cyber range. The drill simulates a Severity 1 ransomware scenario against a replica of our `medinsight-staging` environment over a 4-hour period. Failure to attend the scheduled drill three or more times within a rolling 2-year period will result in a revoking of privileged access credentials, as judged by the IAM Administrator, as it directly violates a core operational security readiness requirement.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policy References

| SOP ID | Document Name |
| :--- | :--- |
| `SOP-ISEC-001` | Information Security Management System (ISMS) Policy |
| `SOP-ISEC-003` | Access Control and Identity Management |
| `SOP-INF-003` | Backup and Disaster Recovery Plan |
| `SOP-LEG-002` | Data Retention and Disposition Schedule |
| `SOP-HR-005` | Employee Sanction and Disciplinary Process |
| `SOP-CMPL-001` | HIPAA Privacy Rule Compliance |

### 10.2 External References

- NIST Special Publication 800-61, Revision 2: Computer Security Incident Handling Guide
- HIPAA 45 CFR Parts 160 and 164, Subparts A and E
- GDPR Articles 33-34 (Notification of a personal data breach to the supervisory authority and communication to the data subject)

---

## 11. Revision History

| Version | Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 4.3 | 2025-09-27 | R. Kim (CISO) | Full rewrite: migrated from static runbooks to a severity matrix aligned with BIA. Moved from on-prem focus to AWS-centric cloud incident response. Updated all roles to reflect current organizational structure. |
| 4.2 | 2025-02-10 | K. Lee (Sr. Analyst) | Added Section 6.4 Breach Log requirement. Updated CISO title. Streamlined Evidence Collection procedures for EBS volume snapshots. |
| 4.1 | 2024-07-15 | K. Lee (Sr. Analyst) | Minor updates. Replaced references from Carbon Black to CrowdStrike Falcon per EDR migration. Updated CSIRT meeting cadence. |
| 4.0 | 2024-01-22 | R. Kim (CISO) | Major revision incorporating post-GDPR operational changes from the Berlin office. Introduced DPO role into the incident declaration and notification workflow. |
| 3.5 | 2023-08-01 | J. Torres (Analyst) | Annual review. Clarified 4-factor breach risk assessment in Detailed Procedures. Updated media notification vendor contact. |
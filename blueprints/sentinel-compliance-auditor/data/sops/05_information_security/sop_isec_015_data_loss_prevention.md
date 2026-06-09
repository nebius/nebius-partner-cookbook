---
sop_id: "SOP-ISEC-015"
title: "Data Loss Prevention"
business_unit: "Information Security"
version: "1.9"
effective_date: "2024-10-23"
last_reviewed: "2025-12-15"
next_review: "2026-06-12"
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

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide Data Loss Prevention (DLP) strategy, governance model, and operational controls for Meridian Health Technologies, Inc. The purpose of this SOP is to protect the confidentiality and integrity of Meridian’s sensitive data—including Protected Health Information (PHI), personally identifiable information (PII), payment card industry data, proprietary algorithms, and material non-public financial information—from unauthorized access, use, disclosure, modification, exfiltration, or destruction. This SOP defines the mechanisms by which data is classified, monitored, and controlled across all data lifecycle states: at rest, in transit, and in use.

### 1.2 Scope

This SOP applies to all Meridian Health Technologies business units, subsidiaries, and global offices, including Boston (Headquarters), London, Berlin, Singapore, and Toronto. It governs the activities of all full-time and part-time employees, independent contractors, consultants, temporary workers, vendors, and any other third parties who access, process, store, or transmit Meridian data. The scope encompasses:

- **Data Types:** All electronic data classified as "Internal," "Confidential," or "Restricted" under the Meridian Data Classification Policy (SOP-ISEC-001), with specific emphasis on PHI as defined by HIPAA, personal data as defined by GDPR, and high-risk AI system training and inference data governed by the EU AI Act.
- **Assets:** All Meridian-issued and managed endpoints (laptops, workstations, mobile devices), servers (physical, virtual, and cloud instances within AWS us-east-1 and eu-west-1, and Azure DR regions), network infrastructure, databases (Snowflake, PostgreSQL, Redis), data lakes, message queues (Apache Kafka), vector databases (Pinecone), and SaaS applications.
- **Products:** The Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform.
- **Exclusions:** This SOP does not cover data destruction at media end-of-life, which is governed by the Media Sanitization and Disposal Policy (SOP-ISEC-009), or the physical security of paper records, which is detailed in the Physical Security Policy (SOP-PHYS-002). It also does not supersede the Incident Response Plan (SOP-ISEC-004) for declared cybersecurity incidents, though DLP alerts serve as a primary detection mechanism that feeds into that process.

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **AUP** | Acceptable Use Policy. The corporate policy governing the permissible use of Meridian information systems and data. |
| **CISO** | Chief Information Security Officer. The executive owner of this SOP. |
| **CJIS** | Criminal Justice Information Services. Referenced for secure data handling controls applicable to certain government contracts, if applicable. |
| **Confidential Data** | Information whose unauthorized disclosure could cause significant financial, legal, or reputational harm to Meridian, its customers, or patients. Includes trade secrets, source code, pre-release financial reports, and detailed system architecture. |
| **Content Inspection** | The automated process of scanning data at rest, in transit, or in use for sensitive patterns, keywords, or document fingerprints. |
| **DLP** | Data Loss Prevention. A suite of technologies and processes designed to detect and prevent the unauthorized exfiltration of sensitive data. |
| **DPO** | Data Protection Officer. Dr. Klaus Weber, responsible for GDPR compliance. |
| **ePHI** | Electronic Protected Health Information. Any PHI that is created, stored, transmitted, or received electronically, as defined under HIPAA. |
| **False Positive** | A DLP incident alert that, upon investigation, is determined not to constitute an actual policy violation or data exposure. |
| **FIM** | File Integrity Monitoring. A control that monitors and detects changes in critical system and data files. |
| **HIPAA** | Health Insurance Portability and Accountability Act of 1996. U.S. federal law governing the privacy and security of PHI. |
| **HITECH** | Health Information Technology for Economic and Clinical Health Act. Augments HIPAA breach notification requirements. |
| **NIST AI RMF** | National Institute of Standards and Technology Artificial Intelligence Risk Management Framework. The framework adopted by Meridian for AI risk management. |
| **PHI** | Protected Health Information. Individually identifiable health information held or transmitted by a covered entity or its business associate, in any form or medium. |
| **Restricted Data** | The most sensitive classification of data at Meridian. Unauthorized disclosure could cause severe financial, legal, or operational damage. Includes ePHI, payment card data, certain patient financial data, and clinical AI model weights trained on regulated data. |
| **SaaS** | Software as a Service. Cloud-based application delivery model. |
| **SIEM** | Security Information and Event Management. Meridian’s primary security analytics platform (Splunk Cloud). |
| **SOC** | Security Operations Center. Meridian’s 24x7 in-house security monitoring team. |
| **SR 11-7** | Federal Reserve guidance on model risk management, applicable to HealthPay Financial Services models. |
| **UAM** | User Activity Monitoring. The process of logging and analyzing user behavior to detect anomalies. |
| **Vendor** | Any third-party entity that provides products, services, or support to Meridian and may access, process, or store Meridian data. |

## 3. Roles and Responsibilities

The following RACI matrix defines the roles and responsibilities for DLP governance and operations.

| Role | Responsibility | RACI |
| :--- | :--- | :--- |
| **Chief Information Security Officer (CISO) (Rachel Kim)** | Executive owner of the DLP program. Defines risk appetite, approves major policy exceptions, and briefs the Board AI Governance Committee on DLP effectiveness. | A |
| **VP of IT Operations (Samantha Torres)** | Responsible for the deployment, maintenance, and health of DLP technical infrastructure on endpoints and networks. | R |
| **Security Operations Center (SOC) Manager** | Oversees day-to-day DLP alert triage, investigation, and incident escalation. Acts as the primary operational lead. Reports to the CISO. | R |
| **Chief Privacy Officer / DPO (Dr. Klaus Weber)** | Provides legal and regulatory guidance on DLP rules related to GDPR and other privacy requirements. Approves all monitoring rules that inspect personal data of EU data subjects. | C |
| **General Counsel (Maria Gonzalez)** | Provides legal guidance on employee monitoring, breach notification obligations under HITECH and state laws, and vendor contract liabilities. | C |
| **Chief Compliance Officer (Thomas Anderson)** | Ensures DLP controls align with HIPAA, SOC 2, and HITRUST CSF certification requirements. Receives recurring DLP metrics reports. | I |
| **VP of Engineering (David Park)** | Responsible for integrating DLP controls into CI/CD pipelines and ensuring source code repositories (GitHub Enterprise) are monitored for sensitive data. | R |
| **VP of Customer Operations (Michael Chang)** | Responsible for reviewing and approving DLP rules affecting workflows for customer support platforms (e.g., Zendesk, Salesforce Service Cloud) where ePHI may be received. | C |
| **Data Stewards** | Business-appointed individuals responsible for defining and reviewing the sensitivity of data within their domains. Validate data classification accuracy used by DLP content inspection rules. | C |
| **All Meridian Personnel** | Must comprehend and adhere to DLP policies, report potential data loss incidents immediately, and complete required training. | I |

## 4. Policy Statements

Meridian Health Technologies is committed to a data-centric security model that prevents the unauthorized disclosure of sensitive information. The following high-level policy statements govern the DLP program:

1.  **Data Classification Foundation:** All data must be classified according to the Meridian Data Classification Policy (SOP-ISEC-001) before DLP controls can be effectively applied. Data classification tags must be embedded in file metadata and database columns where technically feasible.
2.  **Preventive and Detective Controls:** Meridian will deploy a layered DLP architecture applying both preventive controls (blocking actions) and detective controls (alerting on actions) at the endpoint, network, and cloud egress points. Preventive controls are the default posture for data classified as "Restricted."
3.  **Least Privilege and Network Segmentation:** DLP controls are complementary to, not a replacement for, rigorous identity and access management (IAM) and network segmentation. Zero-trust principles will be applied to restrict data access to only those with a validated business justification.
4.  **Content-Aware Protection:** DLP controls must use content inspection techniques (e.g., fingerprinting, exact data matching, machine learning classification) rather than relying solely on metadata or channel restrictions.
5.  **Encryption Mandate:** All "Restricted" and "Confidential" data must be encrypted at rest using AES-256 or equivalent and in transit using TLS 1.2 or higher. DLP systems must be able to detect unencrypted sensitive data in non-compliant locations.
6.  **Data Subject Privacy:** DLP monitoring activities shall be designed with the principle of data minimization for personal data, particularly for EU data subjects. The DPO must approve rules that process personal data to ensure proportionality and necessity, as required by the GDPR.
7.  **Transparent Monitoring:** All Meridian personnel will receive notice that their activities on corporate systems are subject to DLP monitoring. This notice is provided through the AUP acknowledgment, employment contracts, and periodic training.
8.  **Incident Investigation Protocol:** Every DLP alert deemed a "True Positive" policy violation will be formally investigated under the Incident Response Plan (SOP-ISEC-004). All investigations must respect the privacy rights of the individuals involved and follow strict chain-of-custody procedures for evidence.
9.  **No-Retaliation Policy:** Meridian strictly prohibits retaliation against any individual who, in good faith, reports a suspected data loss incident or a weakness in the DLP controls, even if the report is later found to be unsubstantiated.

## 5. Detailed Procedures

### 5.1 DLP Rule Lifecycle Management

This procedure governs the request, design, testing, approval, deployment, and decommissioning of all DLP rules within the Meridian DLP platform (currently Microsoft Purview Information Protection and Data Loss Prevention for Microsoft 365, Endpoint, and Azure; Netskope Cloud Access Security Broker for SaaS and IaaS channels; and CrowdStrike Falcon Data Protection for endpoint egress).

**5.1.1 Rule Request Submission**
1.  A Data Steward, Product Owner, or Compliance team member identifies a need for a new DLP rule to address a regulatory requirement, a new data type, or an observed risk gap.
2.  The requester completes the "DLP Rule Request Form" (available on the ServiceNow IT Service Management portal) providing:
    - Business justification.
    - Data type(s) to be protected (reference Data Classification Index, SOP-ISEC-001).
    - Channels to be monitored (e.g., Email (SMTP), Web (HTTP/HTTPS), Removable Media, Cloud App Upload, Print).
    - Required action (e.g., Alert Only, Block User w/ Override, Policy Tip, Silent Block).
    - Any specific exceptions anticipated.
3.  The request is automatically routed to the SOC Manager for initial review and feasibility assessment.

**5.1.2 Rule Design and Testing**
1.  The SOC Manager assigns the request to a DLP Security Engineer.
2.  The Engineer designs the rule logic within the relevant DLP platform. The design must prioritize low false-positive rates and high-fidelity detection. Conditions may include:
    - **Sensitive Info Types:** Built-in or custom classifiers for ePHI (e.g., ICD-10 codes, NPI numbers, MRNs from known EMR systems), financial data (e.g., PCI-DSS patterns, account numbers), or Meridian proprietary source code keyword lists (`meridian_confidential`, `proprietary_algorithm`).
    - **Document Fingerprinting:** Uploading a representative sensitive form or template (e.g., a blank patient intake form) to create a fingerprint for exact match detection.
    - **Contextual Conditions:** Restricting a rule to specific user groups, AD security groups, device trust levels, or network locations (e.g., "Alert on ePHI upload except when destination is the approved Box tenant").
3.  The rule is deployed to a "Monitor-Only" testing environment encompassing a small cohort from the Information Security team for a minimum of seven (7) days. All alerts generated during this tuning period are analyzed to calibrate sensitivity and verify detection accuracy.

**5.1.3 Rule Approval and Deployment**
1.  Upon successful tuning, the DLP Security Engineer documents the rule's final logic, test results, and false-positive rate estimate in the original ServiceNow request.
2.  The completed request is routed for approval via ServiceNow:
    - **Approver:** SOC Manager (Technical and Operational Risk).
    - **Consulted:** VP of Customer Operations (if rule impacts patient-facing services), Chief Privacy Officer/DPO (if rule processes personal data of EU data subjects).
3.  Following approval, the rule is promoted to the "Production" policy scope. A standard Change Management Record (CMR) is generated and must be approved by the Change Advisory Board (CAB) for high-risk deployments that involve "Block" actions.
4.  The rule's status is updated to "Active" in the Meridian DLP Controls Catalog, a centralized repository maintained in the Information Security SharePoint.

**5.1.4 Rule Review and Decommissioning**
1.  All active DLP rules are subject to a mandatory six-month (180-day) review cycle by the DLP Engineering Team.
2.  Rules that consistently generate an alert-volume-to-incident ratio exceeding 100:1 (i.e., >99% false-positive rate) over a rolling 30-day window, without a defined business blocker, are candidates for decommissioning or major re-tuning.
3.  A "Decommissioning Report" is generated, explaining the rationale for the rule's removal. This report requires approval from the SOC Manager and is archived for audit purposes (retention period: 7 years, per Meridian Legal Hold and Audit Schedule).

### 5.2 Endpoint DLP Controls

Endpoint DLP provides the final line of defense against data exfiltration via physical and logical endpoints, including laptops, workstations, and virtual desktop infrastructure (VDI) machines.

**5.2.1 Endpoint Policy Configuration**
1.  The endpoint DLP agent (CrowdStrike Falcon Data Protection) is deployed to all Windows, macOS, and Linux corporate systems. An agent health dashboard (PowerBI) provides a daily "Compliance Posture" report showing percentage of endpoints with active, healthy agents. Target: >99.5% health status.
2.  Core endpoint policies enforced:
    - **Restricted ePHI and Financial Data Group:** Policy blocks all data classified as "Restricted-PHI" or "Restricted-Finance" from being written to unencrypted USB removable media. An audit log entry is generated for every attempt. Policy allows write operations to BitLocker-To-Go encrypted media with a valid Meridian-managed certificate.
    - **Printing Control:** Printing of documents containing ePHI is restricted to secure print servers within the corporate LAN. Direct printing from endpoints to local IP printers is blocked for documents labeled "Restricted" or "Confidential." A policy tip notifies users and directs them to secure print workflows.
    - **Application-Level Exfiltration:** The agent monitors clipboard activities. Copying content from an application window tagged as "Confidential" (e.g., a HealthPay financial reporting dashboard) to a non-corporate application window (e.g., personal Notepad, webmail text box) is restricted and generates a high-severity alert.

**5.2.2 Endpoint Alert Handling**
1.  Endpoint DLP alerts are streamed via API to the Meridian SIEM (Splunk Cloud) for centralized dashboarding and correlation with other security events (e.g., a DLP block on a USB write immediately preceded by a suspicious user authentication from an anomalous location).
2.  A dedicated "Endpoint High-Severity Alert" queue is monitored in real-time by Tier 1 SOC Analysts. Initial triage is completed within **15 minutes** of alert creation according to the SOC Playbook `DLP_Endpoint_Triage_v4.1`.

### 5.3 Network and Cloud Egress DLP Controls

This procedure governs the inspection of data leaving the Meridian corporate network and cloud environments.

**5.3.1 Network Traffic Inspection**
1.  All outbound web traffic (HTTP/HTTPS) and email traffic (SMTP/Exchange Online) is routed through proxy servers and Secure Email Gateways (SEGs) integrated with the Netskope CASB.
2.  The following channels are inspected:
    - **Web Uploads:** All file uploads to websites, forums, and personal cloud storage services are decrypted (via SSL/TLS inspection performed by Netskope, with specific exclusion lists for financial and health data repositories as defined by the CFO and CPO) and inspected for sensitive content. Uploads of unencrypted Restricted data to uncategorized or high-risk cloud applications are blocked silently.
    - **Email:** All outbound email and attachments are subjected to DLP content analysis. Emails containing ePHI sent to external recipients without Office 365 Message Encryption (OME) or enforced TLS will be blocked. The sender receives a non-delivery report with the policy violation details and instructions for encrypting the email or sending via an approved secure file transfer method.
    - **FTP/SFTP:** Active DLP policies monitor non-standard data channels. High data volume transfers over non-standard ports (Port 21, non-AES encrypted SSH) to non-sanctioned external IP ranges will generate a critical incident for immediate SOC investigation.

**5.3.2 Cloud Egress via Meridian SaaS Platform**
1.  MedInsight Analytics and Clinical AI tenant data egress is monitored by native AWS GuardDuty findings correlated with VPC Flow Logs ingested into Splunk.
2.  A specific "Exfiltration Watch" Splunk correlation rule runs every 5 minutes, analyzing for:
    - Outbound network volume from a production EC2 instance exceeding a dynamic baseline (calculated weekly, threshold for alert: 150% of weekly standard deviation above the median volume).
    - Connection to a newly generated or low-reputation domain.
    - Suspicious DNS queries for TXT records, which can be used for command and control (C2) or data staging.

### 5.4 Data at Rest Scanning

The DLP program is not limited to data in motion. Data repositories must be regularly scanned for sensitive data stored in non-compliant locations or without proper access controls.

**5.4.1 Structured Data (Databases & Data Warehouses)**
1.  The Information Security Team, in partnership with the Data Engineering Team (reporting to the VP of IT), executes quarterly DLP scans of all Snowflake and PostgreSQL databases.
2.  The "Restricted Content Discovery" script uses pattern-matching and machine learning classifiers to tag columns that contain probable ePHI, PCI, or secrets (API keys, tokens) that are not stored in approved vaults (e.g., HashiCorp Vault).
3.  Findings are forwarded to the responsible Data Steward for remediation with a **14-day** resolution SLA for critical misclassifications.

**5.4.2 Unstructured Data (File Shares, GitHub, Box)**
1.  Weekly automated scans are conducted against all corporate file shares (Windows DFS), the primary Box tenant, and all repositories in the Meridian GitHub Enterprise organization.
2.  The GitHub scanning tool (GitGuardian) runs on every push and performs a full historical scan on a monthly basis. Detection of an active AWS access key or an SSH private key constitutes a critical severity incident (see SOP-ISEC-004), requiring immediate revocation of the credential and an investigation led by the SOC Manager in under **60 minutes**.

### 5.5 DLP Incident Handling

All DLP alerts classified as "True Positive" policy violations are escalated according to the following phased procedure.

**Phase 1: Triage and Containment (Tier 1 SOC Analyst, Target Initiation: <30 minutes)**
1.  Verify the alert's authenticity using contextual criteria (e.g., user on leave, active HR case).
2.  Review the full content of the alert. Determine the data volume, the external recipient/channel, and the data classification level of the exfiltrated or exposed data.
3.  Initiate immediate containment actions: force-kill the offending network session via the CASB, revoke the user's access tokens in Okta, and isolate the source endpoint via the CrowdStrike Falcon console. Do not delete or alter the original data on the endpoint or server source until a forensic image is acquired.
4.  Document all initial containment actions in the ServiceNow Incident Record (ticket type: `Security Incident - DLP`).

**Phase 2: Investigation and Analysis (Tier 2 Forensic Analyst and DPO)**
1.  **Forensic Analyst:** Acquires a forensic disk image of the source endpoint. Conducts a timeline analysis to reconstruct the user's actions 72 hours prior to the incident. Analyzes any DLP shadow copies or captured forensic evidence.
2.  **DPO (for incidents involving personal data):** Assesses the risk to the rights and freedoms of the data subjects whose data was compromised. This risk assessment is crucial for determining the ultimate breach notification obligations.
3.  A preliminary Investigation Report, containing the timeline, data volume, and an initial root cause, is delivered to the SOC Manager and the relevant Data Steward within **24 hours** of incident declaration.

**Phase 3: Remediation and Notification**
1.  Based on the Investigation Report, the SOC Manager and relevant business unit leadership (e.g., VP Engineering for a code leak) implement permanent remediation actions: new DLP rule tuning, user training reassignment, or, in coordination with HR and Legal, disciplinary action per the Employee Handbook.
2.  If the DPO determines a personal data breach presents a risk to data subjects' rights, they will work with the CISO and General Counsel to file a notification with the relevant Supervisory Authority within the required timeframe. Notifications to affected data subjects are drafted and executed in coordination with Corporate Communications.
3.  The final Incident Closure Report is completed and distributed to the CISO, VP of IT, DPO, and Chief Compliance Officer.

## 6. Controls and Safeguards

### 6.1 Administrative Controls

| Control ID | Control Description | HIPAA Reference |
| :--- | :---| :--- |
| **ADM-01** | **DLP Program Governance:** An Information Security DLP Steering Committee, comprised of the CISO, SOC Manager, DPO, and VP of IT, meets monthly to review program KPIs, major incidents, and approve new monitoring techniques. Minutes are formally recorded and retained. | 45 CFR § 164.308(a)(2) (Assigned Security Responsibility) |
| **ADM-02** | **Periodic Risk Assessments:** A formal, technical risk assessment of the DLP program's design and operational effectiveness is conducted bi-annually by the GRC team. The assessment tests the adequacy of ePHI-specific content inspection rules and network channel controls. Findings are entered into the Corporate Risk Register and tracked to closure. | 45 CFR § 164.308(a)(1)(ii)(A) (Risk Analysis) |
| **ADM-03** | **Sanction Policy:** Failure to adhere to DLP policies, negligence resulting in a True Positive DLP incident, or willful circumvention of a DLP control is subject to disciplinary action, up to and including termination. All disciplinary actions are coordinated with HR and are documented for audit trail. | 45 CFR § 164.308(a)(1)(ii)(C) (Sanction Policy) |
| **ADM-04** | **Workforce Clearance Procedure:** Access to high-risk data environments (e.g., HealthPay production databases) requires a background check prior to granting access and periodically thereafter, where permitted by local law, in coordination with the HR Department. | 45 CFR § 164.308(a)(3)(ii)(A) (Authorization and/or Supervision) |
| **ADM-05** | **Data Subject Rights Handling:** Requests from data subjects to access, rectify, or erase their personal data (as per GDPR Chapter III) must be routed to the DPO's dedicated privacy portal inbox (`privacy@meridian.com`). The DPO coordinates with IT to collect data from all relevant systems, including DLP archives. While Meridian endeavors to fulfill verifiable requests without undue delay, the complexity of our research data environments necessitates a thorough and careful process. Response timelines will account for the technical difficulty involved, and the DPO will clearly communicate any necessary extension periods to the data subject within the first month of receiving the request. | GDPR, Art. 12(3) |
| **ADM-06** | **DPIA Process:** Meridian conducts Data Protection Impact Assessments (DPIAs) for new data processing activities that are likely to result in a high risk to the rights and freedoms of natural persons. These assessments are led by the DPO and involve consultation with the relevant Product and Engineering teams to evaluate the necessity and proportionality of the data processing and the proposed mitigations. The procedure ensures that all approved DLP network and endpoint monitoring controls are inventoried and analyzed within the DPIA for their privacy impact prior to deployment. | GDPR, Art. 35 |

### 6.2 Technical Controls

| Control Category | Specific Control | Implementation Tooling |
| :--- | :--- | :--- |
| **Content Inspection** | Exact Data Matching (EDM) to detect structured data rows (e.g., patient records with Name+MRN+DOB) exfiltrated in unstructured formats. | CrowdStrike EDM for Endpoints, Microsoft Purview EDM for M365 |
| **Content Inspection** | Machine Learning classifiers for sensitive image/video detection (e.g., detecting a screenshot of an EHR screen shared via Teams). | Microsoft Purview for Teams, integrated with CrowdStrike ML vision models |
| **Channel Controls** | Blocking personal webmail attachments, personal OneDrive/Google Drive uploads from managed laptops. | Netskope CASB Reverse Proxy, Microsoft Purview App Protection Policies (Intune) |
| **Channel Controls** | Restricting clipboard data transfer from "Restricted"-tagged virtual desktops to local physical machine. | VMware Horizon Smart Policies integrated with CrowdStrike Falcon via API |
| **Encryption** | Transparent Data Encryption (TDE) for all SQL Server and PostgreSQL databases hosting "Restricted" data. | AWS KMS-managed keys with Meridian-controlled IAM policies |
| **Endpoint Integrity** | DLP endpoint agent tamper-proofing and secure boot attestation. | CrowdStrike Falcon Device Control and Tamper Protection, integrated with Okta device trust |
| **Information Rights Management (IRM)** | Persistent encryption and rights restrictions applied to documents at creation based on sensitivity label. Prevents copy/paste, screen capture, and enforces offline access timeouts. | Microsoft Purview Information Protection, native integration with Office 365. Sensitivity labels (e.g., "Meridian-PHI-RESTRICTED") set to "Encrypt and assign: co-owner for offline access, 7-day offline expiry" |

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The operational health of the DLP program is measured against the following KPIs. These are displayed on a live PowerBI dashboard ("DLP Command Center") visible to the SOC, Information Security, and executive leadership.

| KPI ID | Metric | Target | Reporting Cadence |
| :--- | :--- | :--- | :--- |
| **DLP-01** | Mean Time to Triage (MTTT) for High-Severity DLP Alerts | < 30 minutes | Daily operational, monthly executive review |
| **DLP-02** | Mean Time to Contain (MTTC) for Confirmed Data Exfiltration | < 60 minutes from alert triage | Monthly executive review |
| **DLP-03** | Overall DLP Alert False Positive Ratio (Total FP / Total Alerts) | < 65% | Monthly operational |
| **DLP-04** | High-Severity Alert False Positive Ratio | < 40% | Monthly operational |
| **DLP-05** | Endpoint DLP Agent Deployment and Health Status | > 99.5% healthy / active agents | Weekly operational |
| **DLP-06** | ePHI Data Discovery Remediation SLA: Time to remediate identified ePHI in unauthorized locations | 100% of critical findings remediated within 14 calendar days | Monthly report to CCO |

### 7.2 Reporting Cadence

- **Daily Operations Brief (08:30 ET):** The outgoing SOC Shift Lead delivers a written turnover report to the incoming shift and the SOC Manager, containing critical DLP incidents from the previous 24 hours.
- **Weekly SOC Metrics Meeting (Mondays, 11:00 ET):** The SOC Manager presents a comprehensive dashboard of all DLP KPIs, a summary of Top-10 triggering policies, and a breakdown of repeat-offender user accounts to the Information Security Director.
- **Monthly Information Security Management Review (ISMR):** The CISO or their designee presents a curated "DLP Program Health" slide deck to leadership (VP of IT, CCO, DPO). This review includes: KPI trend analysis, Major Incident Summaries, Rule Lifecycle changes, and forward-looking risk items.
- **Quarterly Executive Risk Report (QERR):** The CISO provides a DLP program narrative to the CEO and the Board AI Governance Committee, focusing on material risks, major regulatory developments, the effectiveness of controls protecting high-risk AI systems, and a summary of any sanctioned workforce members for DLP violations.

### 7.3 Breach Notification Tracking

A dedicated log is maintained within the Incident Response module of ServiceNow to track all DLP-related incidents that are escalated to the "Potential Regulatory Breach" stage. This log is monitored by General Counsel and the DPO and contains:
- Incident ID and declaration date.
- Affected data subjects (count and jurisdiction).
- Regulatory notification deadlines (e.g., HIPAA Breach Notification Rule: 60-days post-discovery; GDPR: 72-hour initial notifier to DPA). A ServiceNow timer is set for all regulatory deadlines.
- Status of internal/external legal review and notification.

## 8. Exception Handling and Escalation

### 8.1 DLP Rule Exceptions (Business Justification)

Meridian recognizes that rigid security controls can impede critical clinical, financial, or research workflows. A formal exception process exists for temporary and permanent overrides of a DLP blocking rule.

**8.1.1 Standard Exception Procedure**
1.  The affected business unit leader (Director-level or above) submits a "DLP Rule Exception Request" via ServiceNow. The request must contain:
    - Specific DLP rule(s) to be exempted.
    - Precise justification detailing the critical business process impeded. A statement that "business needs" require it is insufficient.
    - Compensating controls to be implemented (e.g., "Instead of automatic block via Netskope, we will implement a manual quarterly audit of uploads by a designated data steward").
    - Duration of the exception (maximum 12 months).
2.  The request is routed sequentially for approval:
    - **Step 1: Information Security Director** (Risk Assessment).
    - **Step 2: Chief Compliance Officer** (Thomas Anderson) for ePHI rules, or **VP of Engineering** (David Park) for source code rules (Compliance/Operational Impact).
    - **Step 3: CISO or DPO** (Final Approval, depending on whether the data is personal data of EU subjects. The DPO holds absolute veto authority on exceptions for rules protecting personal data).

**8.1.2 Emergency Exception Procedure**
1.  In the event of a critical patient safety or operational emergency (e.g., a DLP policy preventing a real-time clinical data transfer needed for emergency care), the CISO or their on-call designee can grant a verbal, 24-hour emergency exception.
2.  The verbal authorization must be immediately followed by logging a "Critical - Emergency DLP Exception" ServiceNow record. The SOC Engineer temporarily disables the rule or creates a bypass for the specific user/entity.
3.  The temporary exception is automatically set to expire in 24 hours. A permanent exception request must be submitted within the next business day, or the rule is re-enabled.

### 8.2 Escalation Matrix for Failed Controls

If the endpoint agent health dashboard KPI falls below 95%, the following automated escalation chain is triggered:

1.  **Immediate Notification:** ServiceNow P1-Priority auto-ticket, SMS/page to VP of IT Operations (Samantha Torres), CISO (Rachel Kim), and IT Infrastructure Lead.
2.  **Bridge Call:** The CISO (or delegate) immediately convenes a technical bridge call to identify the root cause (e.g., faulty agent update, mass device connectivity issue). Response is 24x7.
3.  **Executive Notification:** If the root cause is not identified and a remediation path is not established within **4 hours**, the CISO personally notifies the CEO.

## 9. Training Requirements

### 9.1 Role-Based Training Matrix

All training is tracked via the Meridian LMS (Workday Learning) and must be completed before regulated data access is granted and annually thereafter.

| Audience | Module Name | Frequency | Content Focus |
| :--- | :--- | :--- | :--- |
| **All Meridian Personnel** | SEC-101: Global Data Protection Essentials | Annually, and during New-Hire Orientation (NHO) | Foundational HIPAA, GDPR principles; Meridian AUP; identifying ePHI; recognizing social engineering and exfiltration attempts; reporting procedures for suspicious data loss. Includes DLP monitoring notice. |
| **Developers & Data Engineers** | SEC-205: Secure Coding & Data Handling for Engineers | Annually, with quarterly "Toolbox Talks" on top GitHub DLP findings | Handling secrets responsibly; preventing credential leakage to code repositories; building data classification-aware applications; DLP requirements within CI/CD pipelines as per SOP-SDLC-003. |
| **Clinicians & Data Scientists** | SEC-310: AI and Clinical Data Stewardship | Bi-annually | Ethical handling of clinical data for AI training; privacy-preserving de-identification techniques; strict prohibitions against copying training datasets to non-regulated compute environments; EU AI Act data governance mandates. |
| **SOC Analysts & DLP Engineers** | SEC-520: Advanced DLP Operations & Investigation | Bi-annually, hands-on lab | Hands-on rule tuning in Microsoft Purview, Netskope, CrowdStrike. Advanced Splunk searches for incident investigation. Forensic handling of evidence. Privacy-sensitive investigation techniques in consultation with the DPO. |
| **C-Suite and VP Leadership** | SEC-EXEC: Executive Data Risk Briefing | Annually, in-person briefing | Personalized briefing on material DLP risks, breach notification responsibilities, and personal liability under GDPR and HITECH Act. |

### 9.2 Targeted Remedial Training

Any individual determined (via an Investigation Report) to have caused a preventable True Positive DLP incident due to negligence or policy ignorance is automatically enrolled in a remedial "Refresher on Data Protection Practices" course within **15 business days** of the incident closure. The individual's manager and HR representative receive automated notification of the enrollment. Failure to complete remedial training may result in suspension of access to sensitive systems.

## 10. Related Policies and References

This SOP is a critical node in Meridian's integrated control framework and must be read in conjunction with the following internal documents and external standards.

| Document ID | Document Title | Relationship to this SOP |
| :--- | :--- | :--- |
| **SOP-ISEC-001** | Data Classification and Handling Policy | Foundational policy establishing data sensitivity levels that drive conditional logic in DLP rules. |
| **SOP-ISEC-004** | Information Security Incident Response Plan | Governs the lifecycle of a security event post-detection by DLP controls. |
| **SOP-ISEC-008** | Identity and Access Management | Defines user provisioning and least-privilege access, complementing DLP egress controls. |
| **SOP-ISEC-011** | Encryption and Key Management | Details the encryption standards referenced by and enforced through DLP channel controls. |
| **SOP-ISEC-020** | Secure SDLC and Code Repository Security | Addresses source code handling and CI/CD integration, which DLP monitors. |
| **SOP-EMPL-003** | Acceptable Use of Information Assets (P) | The AUP that all users sign, providing explicit consent for DLP monitoring. |
| **SOP-LEGL-001** | Data Breach Notification Procedure | Workflow triggered by confirmed high-severity DLP incidents. |
| **POL-EMPL-005** | Non-Retaliation Policy (Global) | Policy protecting individuals reporting DLP violations in good faith. |
| **External Ref** | NIST Special Publication 800-53, Rev. 5 | Security and Privacy Controls for Information Systems and Organizations. |
| **External Ref** | NIST AI 100-1 (AI RMF) | Framework for managing AI risks, referenced for controls protecting clinical AI data. |
| **External Ref** | ISO/IEC 27001:2022 | International standard for Information Security Management Systems (ISMS). |

## 11. Revision History

| Version | Date | Author | Revision Summary |
| :--- | :--- | :--- | :--- |
| 1.0 | 2020-01-15 | J. Miller (CISO) | Initial creation. Basic DLP framework for Microsoft 365 and email. |
| 1.3 | 2021-06-01 | A. Gupta (SOC Manager) | Added detailed incident handling procedures, integrated Netskope CASB for cloud app control, and included formal exception process. |
| 1.5 | 2022-11-10 | P. Davies (GRC Lead) | Major update: Expanded scope to include clinical data and HealthPay financial data. Added HIPAA-specific controls and references. Introduced data-at-rest scanning and KPI framework. SOP promoted from "InfoSec Team" to all Meridian staff. |
| 1.7 | 2023-08-15 | R. Kim (CISO) | Full rewrite to integrate DLP rules with AI training data governance for Clinical AI Platform. Updated roles for new organizational structure. Added GDPR-specific monitoring approvals by DPO. |
| 1.8 | 2024-02-20 | L. Chen (Sr. Security Engineer) | Technical refresh: Migrated core network DLP to Netskope NGSWG. Updated EDM procedures. Added CrowdStrike Falcon DLP for endpoint USB and clipboard control. |
| 1.9 | 2024-10-23 | R. Kim (CISO) | Harmonized with new Data Governance Charter. Added formal DPIA process statement and strengthened data subject rights handling in light of expanded clinical trials in Berlin office. Refined AI RMF cross-references. Approved for release. |
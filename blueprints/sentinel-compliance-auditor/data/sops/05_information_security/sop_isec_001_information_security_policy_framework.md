---
sop_id: "SOP-ISEC-001"
title: "Information Security Policy Framework"
business_unit: "Information Security"
version: "3.5"
effective_date: "2025-03-11"
last_reviewed: "2026-04-05"
next_review: "2026-10-28"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Information Security Policy Framework

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise Information Security Policy Framework (“the Framework”) for Meridian Health Technologies, Inc. (“Meridian” or “the Company”). The Framework defines the hierarchical structure, governance mechanisms, roles and responsibilities, and operational processes through which Meridian protects its information assets, manages cybersecurity risk, and ensures compliance with applicable statutory, regulatory, and contractual obligations. The Framework is designed to support the Company’s mission of delivering secure, trustworthy AI-powered healthcare financial technology solutions while preserving the confidentiality, integrity, and availability (CIA) of Meridian information systems and the sensitive data entrusted to it by patients, healthcare providers, payers, and business partners.

### 1.2 Scope

This SOP applies to:

| Scope Category | Detailed Coverage |
|----------------|-------------------|
| **Organizational Entities** | All business units, departments, and subsidiaries of Meridian Health Technologies, Inc., including all global offices in Boston (HQ), London, Berlin, Singapore, and Toronto. |
| **Personnel** | All full-time and part-time employees, contractors, temporary staff, consultants, interns, and third-party service providers with access to Meridian information systems or data (“Workforce Members”). |
| **Information Systems** | All information technology assets owned, leased, operated, or managed by Meridian, including: the Meridian SaaS Platform (AWS us-east-1, eu-west-1), Azure disaster recovery environment, Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and all supporting infrastructure, endpoints, networks, and cloud services. |
| **Data Types** | All electronic and physical information created, received, maintained, or transmitted by Meridian, including but not limited to: Protected Health Information (PHI), personally identifiable information (PII), payment card data, financial records, proprietary algorithms, source code, trade secrets, and internal corporate communications classified as Internal, Confidential, or Restricted. |
| **Activities** | All business processes involving the collection, storage, processing, transfer, disclosure, archival, or destruction of Meridian information assets. |

### 1.3 Policy Hierarchy

The Framework organizes Meridian’s security directives into a four-tier hierarchy to ensure consistency, traceability, and enforceability:

| Tier | Document Type | Purpose | Example |
|------|---------------|---------|---------|
| **Tier 0** | Board-Level Charter | Establishes the AI Governance Committee and overall risk appetite, approved by the Board of Directors. | Meridian AI Governance Committee Charter (2024) |
| **Tier 1** | Enterprise Policies | High-level, principle-based mandates approved by the CEO. Define “what” must be accomplished and “why.” Set binding obligations. | This SOP; Acceptable Use Policy (SOP-ISEC-002); Data Classification Policy (SOP-ISEC-003) |
| **Tier 2** | Standards | Technology-specific, mandatory configuration baselines and technical specifications defining “how” Tier 1 policies are implemented. | AWS Security Configuration Standard; Endpoint Encryption Standard; Cryptographic Key Management Standard |
| **Tier 3** | Procedures and Guidelines | Detailed step-by-step work instructions for executing specific tasks. Guidelines are recommended (non-mandatory) best practices. | Incident Response Procedure (SOP-ISEC-008); Vulnerability Management Procedure; Secure Coding Guideline |

All Tier 2 Standards and Tier 3 Procedures must trace back to one or more Tier 1 Policies. Any conflict between tiers shall be resolved in favor of the higher tier unless an exception is formally granted per Section 8 of this SOP.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|------|------------|
| **Business Associate** | As defined by HIPAA, a person or entity that performs functions or activities involving the use or disclosure of PHI on behalf of a Covered Entity. Meridian acts as a Business Associate to its healthcare provider and payer clients. |
| **Confidentiality** | The property that information is not made available or disclosed to unauthorized individuals, entities, or processes. |
| **Covered Entity** | As defined by HIPAA, a health plan, healthcare clearinghouse, or healthcare provider that transmits health information electronically. |
| **Data Controller** | The entity that determines the purposes and means of the processing of personal data. |
| **Data Processor** | The entity that processes personal data on behalf of the Data Controller. |
| **High-Risk AI System** | An AI system classified under Annex III of the EU AI Act that poses significant risk to health, safety, or fundamental rights. Meridian’s Clinical AI Platform is classified as high-risk. |
| **Information Asset** | Any body of information, system, service, or hardware that has value to Meridian and requires protection. Includes databases, software, physical files, endpoints, and cloud resources. |
| **Integrity** | The property of accuracy and completeness of information and processing methods. |
| **Model Risk** | The potential for adverse consequences from decisions based on incorrect or misused AI/ML model outputs, as defined under SR 11-7 guidance. |
| **Protected Health Information (PHI)** | Individually identifiable health information held or transmitted by a Covered Entity or its Business Associate, in any form or medium, as defined by the HIPAA Privacy Rule. |
| **SOC 2 Type II** | An attestation engagement under AICPA Trust Services Criteria (TSP Section 100) evaluating the operating effectiveness of controls over a period of time (minimum six months). |
| **Trust Services Criteria (TSC)** | The criteria established by the AICPA for evaluating controls relevant to Security, Availability, Processing Integrity, Confidentiality, and Privacy. |

### 2.2 Acronyms

| Acronym | Expansion |
|---------|-----------|
| AICPA | American Institute of Certified Public Accountants |
| BCP/DR | Business Continuity Plan / Disaster Recovery |
| CIA | Confidentiality, Integrity, Availability |
| CISO | Chief Information Security Officer |
| CPO/DPO | Chief Privacy Officer / Data Protection Officer |
| CSIRT | Computer Security Incident Response Team |
| EDR | Endpoint Detection and Response |
| IAM | Identity and Access Management |
| IRP | Incident Response Plan |
| ISMS | Information Security Management System |
| KPI | Key Performance Indicator |
| MFA | Multi-Factor Authentication |
| NIST AI RMF | National Institute of Standards and Technology Artificial Intelligence Risk Management Framework |
| PHI | Protected Health Information |
| RACI | Responsible, Accountable, Consulted, Informed |
| RPO | Recovery Point Objective |
| RTO | Recovery Time Objective |
| SIEM | Security Information and Event Management |
| SLA | Service Level Agreement |
| SR 11-7 | Federal Reserve Supervision and Regulation Letter 11-7 on Model Risk Management |
| SSO | Single Sign-On |
| TSC | Trust Services Criteria |
| VP | Vice President |
| WORM | Write Once, Read Many |

---

## 3. Roles and Responsibilities

The following RACI matrix defines the roles and responsibilities for the governance, implementation, and enforcement of the Information Security Policy Framework.

**RACI Key:**
- **R (Responsible):** Performs the task/activity.
- **A (Accountable):** Ultimately answerable for the correct and thorough completion of the deliverable or task; must sign off (only one “A” per task).
- **C (Consulted):** Whose opinions are sought, typically subject matter experts; two-way communication.
- **I (Informed):** Kept up-to-date on progress; one-way communication.

| Activity / Deliverable | CISO (Rachel Kim) | CEO (Dr. Sarah Chen) | Chief AI Officer (Dr. Marcus Rivera) | Chief Compliance Officer (Thomas Anderson) | CMO / CPrO (Dr. Patel / Dr. Weber) | VP of IT Ops (Samantha Torres) | VP of Eng. (David Park) | General Counsel (Maria Gonzalez) | Board AI Gov. Committee | All Workforce Members |
|---|---|---|---|---|---|---|---|---|---|---|
| **Policy Framework Governance** | | | | | | | | | | |
| Approve Tier 1 Enterprise Policies | C | A | C | C | C | I | C | C | C | I |
| Author and Maintain Tier 1 Policies | R | I | C | C | C | C | C | C | I | I |
| Author Tier 2 Standards | A | I | R (AI) | C | C | R (IT) | R (Eng) | I | I | I |
| Annual Policy Review & Refresh | R | I | C | C | C | C | C | C | I | I |
| Exception Approval (Risk) | A | I | C | C | I | I | I | C | I | I |
| **Operational Execution** | | | | | | | | | | |
| Implement Technical Controls | C | I | C | I | I | R | R | I | I | I |
| Conduct Access Reviews (Quarterly) | C | I | I | R | I | R | R | I | I | I |
| Vulnerability Management | A | I | I | I | I | R | R | I | I | I |
| Security Monitoring & SIEM | A | I | I | I | I | R | C | I | I | I |
| Incident Response (CSIRT Lead) | R/A | I | C | C | C | R | R | C | I | I |
| **Compliance & Risk Management** | | | | | | | | | | |
| SOC 2 Audit Management | R | I | C | C | C | C | C | C | I | I |
| HIPAA Compliance Oversight | C | I | I | R | A | C | C | C | I | I |
| SR 11-7 Model Validation | I | I | A | C | I | I | R (ML) | C | I | I |
| AI Risk Assessment (NIST AI RMF) | C | I | R/A | C | C | I | C | C | I | I |
| Third-Party Risk Assessment | R | I | I | C | C | I | I | C | I | I |
| **Workforce** | | | | | | | | | | |
| Complete Security Awareness Training | C | I | I | I | I | I | I | I | I | R |
| Report Security Incidents | I | I | I | I | I | I | I | I | I | R |

**Specific Role Descriptions:**

- **Chief Information Security Officer (CISO), Rachel Kim:** Owns the Information Security Policy Framework. Has final authority on all information security matters, subject to CEO and Board oversight. Chairs the monthly Security Steering Committee. Approves all Tier 2 Standards and exceptions to policy involving risk above the defined threshold (see Section 8).
- **Chief AI Officer (CAIO), Dr. Marcus Rivera:** Owns the AI risk management framework in alignment with NIST AI RMF and the EU AI Act. Ensures Clinical AI Platform models are developed, validated, and monitored for security vulnerabilities and adversarial threats. Collaborates with the CISO on AI-specific security controls.
- **Chief Compliance Officer (CCO), Thomas Anderson:** Owns HIPAA compliance program, including privacy rule compliance, breach notification decision-making, and regulatory liaison. Conducts quarterly access reviews with system owners.
- **Chief Privacy Officer / Data Protection Officer (CPO/DPO), Dr. Klaus Weber:** Monitors compliance with GDPR and other privacy regulations from the Berlin office. Advises on privacy-by-design requirements and data subject rights fulfillment. Works independently and reports to the Board on privacy matters.
- **VP of IT Operations, Samantha Torres:** Manages the operational security of the Meridian SaaS Platform and corporate IT infrastructure. Owns the SIEM, vulnerability management program, patch management, and the CSIRT.
- **General Counsel, Maria Gonzalez:** Provides legal interpretation of regulatory requirements. Approves data processing agreements with third parties. Manages legal aspects of incident response and breach notification.
- **All Workforce Members:** Must comply with all policies, complete required training, report suspicious activity immediately via PagerDuty or to security@meridianhealth.com, and safeguard Meridian information assets in their possession.

---

## 4. Policy Statements

The Meridian Board of Directors and Executive Leadership Team commit to the following high-level policy statements, which form the foundation of the Information Security Program:

1. **Risk-Based Security Management**
Meridian employs a risk-based approach to information security, structured around the NIST AI RMF and aligned with ISO 27001:2022 principles. Information assets shall be inventoried, classified, and subjected to periodic risk assessments. The results of these assessments shall guide the selection and implementation of security controls. No AI model classified as high-risk shall be deployed to production without a documented AI risk assessment approved by the CAIO and CISO.

2. **Defense-in-Depth**
Meridian implements a layered security architecture incorporating preventative, detective, and corrective controls across network, host, application, data, and identity layers. All production systems must be protected by at minimum: a next-generation firewall, EDR (CrowdStrike), SIEM-based monitoring (Datadog), and enforced MFA via Okta SSO.

3. **Least Privilege and Need-to-Know**
Access to all Meridian information systems and data shall be granted based on the principle of least privilege. Workforce Members shall be assigned only the minimum permissions necessary to perform their authorized job duties. Privileged access (e.g., AWS root, production database administrator) must be justified, time-bound, logged, and subject to quarterly recertification by the asset owner and the CCO. All access to PHI within MedInsight Analytics and the Clinical AI Platform must be further justified by a documented “need-to-know” for a specific clinical or operational purpose.

4. **Secure by Design**
Security shall be embedded into the system development lifecycle (SDLC) from inception. All products, including AI/ML models and the Meridian SaaS Platform, must undergo: (a) threat modeling prior to development; (b) static application security testing (SAST) during coding; (c) dynamic application security testing (DAST) and software composition analysis (SCA) prior to staging; and (d) penetration testing annually or upon major release. AI/ML models must also be evaluated for adversarial robustness, data poisoning risks, and model inversion vulnerabilities.

5. **Transparency and Human Oversight for High-Risk AI**
Consistent with the EU AI Act Annex III obligations effective August 2025, Meridian ensures that its Clinical AI Platform products provide appropriate transparency information to deployers (healthcare providers) regarding their capabilities, limitations, and intended use. Human oversight mechanisms are built into all clinical decision support workflows, ensuring that qualified clinicians can interpret, override, and contest AI-generated recommendations. All adverse events related to AI outputs must be logged and reported per SOP-PRD-014 (Clinical AI Post-Market Surveillance).

6. **Continuous Monitoring and Improvement**
The information security program shall be subject to independent assessment through the annual SOC 2 Type II audit, penetration testing, red team exercises, and the management review process. Findings shall be tracked in a formal Corrective Action Plan (CAP) with assigned owners and target remediation dates.

---

## 5. Detailed Procedures

### 5.1 Policy Development, Review, and Approval Procedure

This procedure governs the lifecycle of all Tier 1 Enterprise Policies within the Framework.

| Step | Action | Responsible Party | Timeline/Trigger |
|------|--------|-------------------|------------------|
| 1 | **Identification of Need:** A need for a new policy or material change is identified through a regulatory change, audit finding, risk assessment, security incident, or business requirement. | Any stakeholder; CISO evaluates | Ad-hoc |
| 2 | **Drafting:** Policy owner drafts the document using the **Meridian Policy Template (TMPL-ISEC-001)** , ensuring alignment with the Policy Hierarchy and cross-referencing impacted Tier 2 Standards. | CISO (or delegate) | Within 30 days of identification |
| 3 | **Stakeholder Review:** Draft circulated to defined RACI “Consulted” parties (Section 3). Reviewers submit comments in GitLab within the track-changes enabled document. | CISO manages review | 14-day review period |
| 4 | **Regulatory Counsel Review:** General Counsel (Maria Gonzalez) reviews the draft for legal and regulatory alignment, specifically for SOC 2 TSC, HIPAA, and SR 11-7 conformance. | General Counsel | Concurrent with Step 3 |
| 5 | **Consolidation and Revision:** Comments are adjudicated by the CISO. Substantive, unresolved disagreements are escalated to the CEO. | CISO | 7 days after review closure |
| 6 | **Final Approval:** Final draft submitted to the Approver (CEO for Tier 1) for electronic signature via DocuSign. | CEO (Dr. Sarah Chen) | 7 days after submission |
| 7 | **Publication and Communication:** Approved policy is published to the corporate intranet (PolicyHub), registered in the policy ledger, and announced to all Workforce Members via the Company-wide newsletter and a Slack #general announcement. | CISO / Corporate Communications | 5 business days after approval |
| 8 | **Acknowledgment:** All active Workforce Members must electronically acknowledge that they have read, understood, and will comply with the new or revised policy. Acknowledgement is tracked via Okta integrated into the Lattice HRIS platform. | All Workforce Members | Within 14 calendar days of notification |
| 9 | **Evidence Retention:** Signed approval, final policy version, and acknowledgment completion reports are stored as SOC 2 audit evidence in the WORM-compliant AWS S3 bucket: `s3://meridian-compliance-evidence/soc2/policy-lifecycle/`. | CISO | Perpetual, minimum 7 years |

### 5.2 Annual Policy Review Procedure

Meridian reviews all Tier 1 Policies annually to ensure continued relevance and compliance.

| Step | Action | Responsible Party | Timeline |
|------|--------|-------------------|----------|
| 1 | **Review Trigger:** CISO’s office generates a report from the policy ledger identifying all policies due for review within the next 90 days. Review is no later than `last_reviewed` date + 365 days. | CISO | Monthly automated check |
| 2 | **Impact Assessment:** CISO collaborates with the CCO to identify regulatory, technical, or business changes since the last review that impact the policy. Uses regulatory intelligence feeds from Thomson Reuters Regulatory Intelligence. | CISO, CCO | Month 1 of review quarter |
| 3 | **No-Change Confirmation or Revision:** If no changes are required, CISO documents the rationale in a “Policy Annual Review Confirmation” form (FRM-ISEC-002) and updates the `last_reviewed` and `next_review` dates. If changes are needed, follow Section 5.1. | CISO | End of review quarter |
| 4 | **Board Report:** A summary of all annual policy reviews, including no-change confirmations, is presented to the Board AI Governance Committee during the Q4 meeting. | CISO, CAIO | Q4 Board Meeting |

### 5.3 Data Classification and Handling Procedure

All information assets must be classified according to the Data Classification Policy (SOP-ISEC-003). Handling procedures for each classification are detailed below.

| Classification | Labeling | Storage Requirements | Transmission Requirements | Disposal Requirements | Examples |
|----------------|----------|----------------------|---------------------------|------------------------|----------|
| **Restricted** | Red banner; header/footer metadata tag | AES-256 encrypted at rest in Meridian-managed systems (AWS KMS CMK). Must reside in approved data zones. No local endpoint storage. | TLS 1.3 required. Email forbidden unless encrypted via Meridian Secure Email Gateway. SFTP or Meridian Secure File Transfer API only. | Crypto-shredding (key destruction) or NIST 800-88 compliant physical destruction for hardware. Verified by two-person integrity check. | PHI datasets in MedInsight; Clinical AI training data containing patient images; Production encryption keys; HealthPay PAN data |
| **Confidential** | Yellow banner; header/footer metadata tag | AES-256 encrypted at rest. Cloud storage permitted within Meridian tenant. Local endpoint storage permitted only on encrypted company-issued devices. | TLS 1.2+ required. Email permitted with mandatory Data Loss Prevention (DLP) scan. | Secure deletion via CrowdStrike certified erasure or degaussing. | Source code (GitLab); Financial records prior to public filing; Business strategy documents; SOC 2 audit reports; HR records with PII |
| **Internal** | No visual banner required; metadata tag | No encryption at rest mandated (recommended). Cloud storage anywhere in Meridian tenant permitted. | TLS 1.2+ for cloud services. Standard email permitted. | Standard recycle bin deletion or object overwrite. | SOP drafts; Team meeting notes; Training materials; Corporate newsletters |
| **Public** | No label | No requirements | No requirements | No special requirements | Marketing collateral; Published press releases; Public website content |

**PHI-Specific Handling Controls (Restricted):**
- PHI may only be stored in the Snowflake PHI Vault, the MedInsight PostgreSQL cluster in `us-east-1`, or the Clinical AI Platform data lake in `eu-west-1`.
- Direct database queries against PHI tables require a temporary, time-bound (maximum 4 hours) elevation of privilege approved by the DPO (Dr. Weber) and logged in HashiCorp Vault audit trail.
- PHI used for AI/ML model training must be de-identified in accordance with the HIPAA Safe Harbor method (18 identifiers removed) prior to use in any non-clinical-development environment (e.g., model sandbox).

### 5.4 Identity and Access Management (IAM) Procedure

**5.4.1 User Lifecycle Management**

| Lifecycle Event | Procedure Step | System/Tool | Timeline |
|-----------------|----------------|-------------|----------|
| **Joiner (New Hire/Contractor)** | 1. HR creates profile in Lattice HRIS. 2. Integration auto-provisions Okta user. 3. Hiring manager submits “Access Request” in ServiceNow (FRM-ISEC-004) specifying required groups/roles based on Job Role Matrix. 4. ServiceNow routes to Resource Owner for approval. 5. Upon approval, Okta pushes groups to downstream apps (AWS SSO, Snowflake, GitLab). | Lattice → Okta → ServiceNow → Apps | Account created Day 0. Access provisioned by Day 1 10:00 AM local time. |
| **Mover (Job Change)** | 1. Manager triggers “Access Change” request in ServiceNow. 2. All existing access is flagged for review. 3. Old access removed; new access provisioned per new role. Both actions must be completed. | ServiceNow, Okta | Completed on effective date of job change. |
| **Leaver (Termination)** | 1. HR terminates in Lattice. 2. Webhook triggers immediate Okta suspension and hard token revocation. 3. All active sessions invalidated within 5 minutes. 4. ServiceNow ticket auto-generated for asset recovery. 5. Manager confirms data export/transfer approved by CISO. | Lattice, Okta, ServiceNow, CrowdStrike (for device lock) | Within 24 hours of termination notification, or immediately in case of involuntary termination for cause. |

**5.4.2 Access Recertification (Quarterly)**

- **Frequency:** Calendar quarterly (March 31, June 30, September 30, December 31).
- **Scope:** All access to systems storing or processing Restricted data (PHI, PCI, trade secrets), and all privileged/administrator accounts across all systems.
- **Procedure:**
  1. The CCO (Thomas Anderson) generates an Access Review Campaign in ServiceNow for each application owner.
  2. Application Owners review the list of users and their entitlements for their system.
  3. Owners must either “Certify” (access is appropriate) or “Revoke” (access must be removed). No “no-action” certification is allowed.
  4. Revocations are implemented within 5 business days by the IT Ops IAM team (Samantha Torres’ team).
  5. Business unit leaders (VP-level or above) review and sign off on access for their direct reports.
  6. The CISO conducts a quality assurance review on a random sample of 10% of certifications.
  7. Full campaign results and revocations are stored as SOC 2 control evidence. KPIs tracked: % of accounts certified on time (target >95%), % of accounts revoked (tracked for anomalies).

### 5.5 Incident Response Procedure

This procedure is triggered upon the declaration of a Security Incident by the CSIRT Lead. Detailed playbooks are contained in SOP-ISEC-008 (Incident Response Plan). This Framework level describes the governance overlay.

**5.5.1 Incident Severity Classification**

| Severity | Definition | Example | Response SLOs |
|----------|------------|---------|---------------|
| **P1 – Critical** | Confirmed breach of Restricted data (PHI exfiltration), active ransomware, service outage for Clinical AI Platform affecting patient safety. | Unauthorized party accessing PHI in Snowflake. | Declare within 15 min. CSIRT War Room within 30 min. Exec notification within 1 hr. |
| **P2 – High** | Suspected compromise, widespread phishing with credential harvesting, critical vulnerability exploited in the wild. | Meridian-credential phishing campaign with successful user compromise. | Declare within 1 hr. CSIRT activated within 2 hrs. |
| **P3 – Medium** | Malware on single endpoint contained by EDR, lost/stolen encrypted company device, policy violation with no data exposure. | Employee laptop lost at airport, encrypted, remote wiped confirmed. | Triage within 4 hrs. Resolution within 3 business days. |
| **P4 – Low** | Security event of interest, no impact. Reconnaissance scans, blocked port scans, DLP policy hit on user error. | User mistakenly emails Internal document externally, retracted. | Logged. Included in weekly SOC review. |

**5.5.2 Breach Notification Decision Protocol**

For any incident involving PHI (actual or suspected), Meridian must execute a Breach Risk Assessment per HIPAA. The following protocol is invoked by the CSIRT Incident Commander for any P1 or P2 incident affecting PHI:

1. **Evidence Preservation:** The CSIRT Forensic Lead immediately captures a point-in-time snapshot of all affected systems (AWS EBS snapshots, database transaction logs, WORM storage capture). Chain of custody is documented in the case management system (PagerDuty Incident).
2. **Scope Determination:** Within 24 hours, the CSIRT, working with the Data Custodian, determines the exact set of individuals and data elements affected.
3. **Risk Assessment Panel Convened:** The CISO convenes a panel within 48 hours, including the CCO, CPO/DPO (Dr. Weber), General Counsel, and Chief Medical Officer (if clinical data is involved).
4. **Harm Assessment:** The panel assesses the probability that the PHI has been compromised based on a four-factor test. The determination is documented in a Breach Risk Assessment Report.
5. **Notification Decision:** If the assessment concludes a low probability of compromise, a record of the assessment is maintained for audit. If breach is confirmed, the General Counsel directs regulatory notification and individual notification. Affected patients are notified without unreasonable delay and within the legally mandated timeframe.
6. **Media Notification:** If the breach affects more than 500 residents of a state or jurisdiction, prominent local media notification is executed concurrently.

### 5.6 Third-Party Risk Management Procedure

Given the use of AWS, multiple SaaS tools, and medical research collaborators, third-party risk is managed as follows.

1. **Inherent Risk Scoring:** All new third-party engagements are classified using a questionnaire in the Vanta compliance platform, evaluating access to data, systems, and the nature of the service.
2. **Tiered Due Diligence:**
   - **Tier 1 (Critical – access to PHI or production systems):** Requires a full SOC 2 Type II report review, HIPAA Business Associate Agreement (BAA) execution, and security questionnaire. Annual reassessment.
   - **Tier 2 (Moderate – access to Internal/Confidential data, no PHI):** Requires security questionnaire and data processing agreement. Biennial reassessment.
   - **Tier 3 (Low – commodity services, no Meridian data access):** TPRM team spot-checks.
3. **Continuous Monitoring:** Tier 1 vendors are continuously monitored via an external threat intelligence feed integrated with Vanta. Any significant security incident at a Tier 1 vendor triggers an immediate reassessment.

### 5.7 Secure Development and Model Risk Management

This procedure integrates SR 11-7 model risk management and AI security into the Meridian SDLC.

1. **Model Initiation:** Every new AI/ML model initiated within the Clinical AI or HealthPay units must be registered in the MLflow Model Registry with a unique model identifier.
2. **AI Risk Tiering:** The model owner, in conjunction with the CAIO’s team, completes a Model Risk Tiering Assessment mapped to NIST AI RMF characteristics and SR 11-7 complexity/materiality. High-risk models (e.g., patient risk scoring, credit scoring) are subject to enhanced controls.
3. **Development Controls:** Model code must be peer-reviewed and stored in GitLab. Training data provenance must be documented and verified. Data for model training must not contain production PHI unless a specific, time-bound DPO waiver is granted (see Section 5.3). All PHI for training must be de-identified prior to use.
4. **Independent Validation (Model Risk Management – SR 11-7):** Prior to production deployment, all Tier 1 (high-risk) models must be independently validated by a qualified team independent of model development. Validation includes:
   - Conceptual soundness and theory review.
   - Outcomes analysis, including back-testing and benchmarking.
   - Ongoing monitoring plan.
   - Security testing for adversarial robustness, sensitivity analysis, and data leakage.
5. **Production Deployment Gate:** No high-risk model can be deployed to production without a sign-off from the CAIO (for clinical validity) and the CISO (for security risks) in the ServiceNow Change Management record. The deployment must be code-driven (GitOps) and fully auditable.

---

## 6. Controls and Safeguards

This section outlines the specific technical and administrative controls aligned to the AICPA Trust Services Criteria for the SOC 2 Type II audit, as well as controls required by HIPAA and SR 11-7.

### 6.1 Administrative Controls

| Control ID | Control Description | TSC Mapping | Owner | Frequency |
|------------|---------------------|-------------|-------|-----------|
| **AC-1** | Information Security Policy Framework: The ISMS, as defined by this SOP, is established, reviewed, and updated to reflect changes in the business, technology, and threat landscape. | CC1.1, CC1.2 | CISO | Annual (or Ad-hoc) |
| **AC-2** | Workforce Security Awareness Training: All Workforce Members complete general security awareness training. | CC1.4 | CISO / CHRO (Jennifer Walsh) | Annual (within 30 days of hire, annually thereafter) |
| **AC-3** | Disciplinary Policy: A formal, HR-sanctioned disciplinary process exists for violations of information security policies, up to and including termination of employment. The policy is published in the Employee Handbook. | CC1.2, CC1.5 | CHRO / CISO | Ad-hoc |
| **AC-4** | Board-Level Governance: The Board AI Governance Committee reviews the state of the information security program, material risks, and AI governance matters quarterly. Minutes are retained. | CC1.1, CC2.2 | CISO, CAIO | Quarterly |
| **AC-5** | Business Continuity and Disaster Recovery Testing: A tabletop exercise for a ransomware scenario affecting the Meridian SaaS Platform is conducted annually. A full-scale DR failover to the Azure environment is tested biennially. The RPO for the Clinical AI Platform is 1 hour; RTO is 4 hours. | A1.2, A1.3 | VP IT Ops (Samantha Torres) | Annual / Biennial |

### 6.2 Technical Controls

| Control ID | Control Description | TSC Mapping | Technology | Metric for SOC 2 |
|------------|---------------------|-------------|------------|------------------|
| **TC-1** | Identity and Access Management: Centralized IAM using Okta for SSO and MFA. MFA is enforced for all remote access and access to any system containing Restricted data. | CC6.1, CC6.2 | Okta, AWS SSO | MFA enrollment rate (% users with MFA active; target 100%) |
| **TC-2** | Endpoint Protection: Next-gen antivirus and EDR deployed to all company Windows and macOS endpoints. Tamper protection enforced. | CC6.6 | CrowdStrike Falcon | EDR agent coverage (% endpoints reporting; target 100%); Mean time to detect (MTTD) for endpoint threats (< 1 hour for P2+) |
| **TC-3** | Vulnerability and Patch Management: Internal vulnerability scans run weekly against all internal and cloud assets. External scans run daily via Qualys. Critical patches (CVSS ≥ 9) must be deployed within 7 days. High (CVSS ≥ 7) within 30 days. | CC7.1 | Qualys, AWS Inspector, Datadog | % of critical vulnerabilities remediated within SLA (target >95%) |
| **TC-4** | Network Security: Cloud environments (AWS us-east-1, eu-west-1) are segmented into VPCs with strict security groups. Production and non-production environments are logically separated. AWS WAF protects public-facing APIs. | CC6.6 | AWS VPC, AWS WAF | Number of open, unapproved ports detected (target 0) |
| **TC-5** | Data-at-Rest Encryption: All Restricted and Confidential data at rest must be encrypted using AES-256. Meridian uses envelope encryption with AWS KMS Customer Managed Keys (CMKs). Key rotation is annual. | CC6.1, P4.2 | AWS KMS (CMK) | Encryption enforcement rate (% of S3 buckets, RDS instances, and EBS volumes with data classified as Restricted that are encrypted; target 100%) |
| **TC-6** | Data-in-Transit Encryption: All external-facing communications use TLS 1.2 or higher. TLS 1.3 is mandated for any API handling PHI or financial transactions. | CC6.7 | AWS Certificate Manager, CDN | Number of externally-facing assets supporting only <TLS 1.2 (target 0) |
| **TC-7** | Security Information and Event Management (SIEM): Centralized log aggregation from AWS CloudTrail, VPC Flow Logs, Okta, CrowdStrike, and all critical applications. Real-time alerts for defined use cases (e.g., impossible travel, privileged account activity outside hours). | CC7.2, CC7.3 | Datadog SIEM | Mean Time to Detect (MTTD) across all P1/P2 incidents, tracked quarterly |
| **TC-8** | Change Management: All changes to production systems (code deployment, infrastructure-as-code, security group modifications) must follow a documented change management process. Normal changes require CAB approval via ServiceNow. Emergency changes require post-hoc CAB review. AI model changes follow the SR 11-7 gated process (Section 5.7). | CC8.1 | ServiceNow, GitLab CI/CD Pipelines | % of successful production changes (not requiring rollback); % of emergency changes requiring post-hoc review |

### 6.3 Data Backup Controls

| System | Backup Technology | Schedule | Retention Location |
|--------|------------------|----------|-------------------|
| Snowflake (PHI Vault) | Time Travel and Failsafe features, plus cross-region replication to `eu-west-1` | Continuous | AWS S3 Glacier Deep Archive (immutable for 90 days) |
| AWS RDS (MedInsight) | Automated snapshots + cross-region replication to `eu-west-1` (for DR) | Daily snapshots (retained 30 days), monthly for 7 years | AWS DR account (Azure BCP) |
| GitLab Repositories | Built-in GitLab backup process | Hourly incremental, full daily | AWS S3 in isolated DR account |
| Endpoint Data (corporate laptops) | OneDrive Known Folder Move (KFM) | Continuous sync (cloud-native) | Microsoft 365 Compliance Center |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs) and Key Risk Indicators (KRIs)

A dashboard of KPIs and KRIs is maintained for operational oversight and is the primary reporting mechanism for the quarterly Board briefing.

| Category | Metric / KPI | Target / SLA | Data Source | Review Cadence |
|----------|--------------|--------------|-------------|----------------|
| **Vulnerability Management** | % Critical CVEs remediated within 7-day SLA | ≥ 98% | Qualys / Datadog | Monthly Security Steering Committee |
| **Vulnerability Management** | Overall Mean Time to Remediate (MTTR) for High Severity | ≤ 21 days | Qualys | Monthly |
| **Access Control** | % of Quarterly Access Recertifications completed on time | ≥ 95% | ServiceNow | Quarterly |
| **Access Control** | % of Privileged accounts with just-in-time access vs. standing | JIT for 80% of AWS roles | Okta / AWS | Quarterly |
| **Incident Response** | Mean Time to Detect (MTTD) P1/P2 Incidents | ≤ 4 hours | PagerDuty / Datadog | Monthly |
| **Incident Response** | Mean Time to Contain (MTTC) P1/P2 Incidents | ≤ 24 hours (from declaration) | PagerDuty | Post-Incident Review (every P1/P2) |
| **Asset Management** | EDR Agent Coverage (CrowdStrike) | 100% | CrowdStrike Console | Weekly IT Ops Standup |
| **Training & Awareness** | % Workforce completing annual security training | ≥ 99% | Lattice (LMS) | Semi-annual HR Review |
| **Training & Awareness** | Phishing simulation click rate | < 5% | Proofpoint | Monthly |
| **Third-Party Risk** | % Tier 1 vendors with current SOC 2 review (within 365 days) | 100% | Vanta | Monthly TPRM Review |
| **Third-Party Risk** | Number of Tier 1 vendors operating without an executed BAA (when PHI is involved) | 0 | Vanta | Monthly TPRM Review |
| **BCP/DR Readiness** | Last successful restore from backup test (MedInsight) | ≤ 6 months (test frequency) | AWS Backup | Quarterly |

### 7.2 Reporting Cadence

| Report | Audience | Frequency | Prepared By | Content |
|--------|----------|-----------|-------------|---------|
| **CISO Weekly Status Report** | CISO Direct Reports | Weekly (Monday AM) | CISO | Top 5 security events of the week, patch compliance snapshot, SOC alerts. |
| **Monthly Security Steering Committee Pack** | Security Steering Committee (CISO, CCO, VP IT Ops, VP Eng, CAIO, CRO) | Monthly | CISO’s Analyst Team | Full KPI dashboards, CAP tracking, audit prep status, any P1/P2 post-incident reviews since last meeting. |
| **Quarterly Board Briefing** | Board AI Governance Committee, CEO, CFO, General Counsel | Quarterly (aligned with Board meetings) | CISO, CAIO | Executive summary of KRI trends, risk register heat map, AI governance updates, material security incidents, regulatory horizon scanning. |
| **Annual SOC 2 Management Letter** | Independent Auditor (SOC 2) | Annual (Audit period: Nov 1 – Oct 31) | CISO, Internal Audit | Not a "report" per se, but this is the formal management assertion letter and description of the system prepared by Meridian for the auditor. |

---

## 8. Exception Handling and Escalation

### 8.1 Information Security Policy Exception Process

Situations requiring deviation from a mandatory Tier 1 Policy or Tier 2 Standard must follow the formal Exception Handling Procedure. Exceptions must not be self-assigned. A culture of “no bypass without justification” is enforced.

| Step | Action | Responsible | Notes |
|------|--------|-------------|-------|
| 1 | **Request Initiation:** The requestor submits an “Information Security Exception Request” (FRM-ISEC-009) in ServiceNow. The form must include: the specific policy/standard being excepted, the reason, compensating controls proposed, the business justification, and the duration. | Any Workforce Member (Requester) | The business justification must include the impact of *not* granting the exception. |
| 2 | **Manager Validation:** The requester’s immediate manager (Director or above) reviews and approves the business justification. | Requester’s Manager | Validates business criticality only.
| 3 | **Security Risk Assessment:** The CISO’s Policy and Risk team assesses the technical risk, evaluates compensating controls, and attaches a calculated residual risk score (Low, Moderate, High, Critical) using the Meridian Risk Scoring Matrix. | CISO Risk Team | Includes technical analysis and recommendation. |
| 4 | **Regulatory Assessment:** If the exception impacts PHI or AI models, the CCO (Thomas Anderson) and/or CAIO (Dr. Marcus Rivera) provide a compliance opinion. | CCO / CAIO | Ensures no violation of HIPAA, GDPR, or EU AI Act by granting the exception. |
| 5 | **Approval:** Based on the residual risk score: **Moderate risk** requires CISO approval. **High risk** requires CISO and CEO approval. **Critical risk** exceptions will not be granted except by Board resolution. Exceptions for periods > 90 days require CEO approval regardless of risk. | CISO / CEO | All approvals via DocuSign attached to the ServiceNow ticket. |
| 6 | **Tracking and Expiry:** Approved exceptions are entered into the risk register. The policy engine automatically notifies the CISO risk team 14 days before expiration. Expired exceptions without a renewal (re-running the process) result in automatic re-enforcement of the policy within 30 days. | CISO Risk Team | Zero-tolerance for lapsed exceptions. |

### 8.2 Escalation Path for Unresolved Security Issues

Any Workforce Member who believes that an information security risk is not being adequately addressed has the right and responsibility to escalate.

1. **Immediate Manager** (standard chain).
2. **Information Security Team** (email security@meridianhealth.com or Slack #ask-security). An analyst is assigned and tracks the issue.
3. **Chief Information Security Officer (Rachel Kim)** directly for any issue involving potential breach of Restricted data, or if previous escalation has stalled.
4. **Whistleblower Hotline (EthicsPoint):** For reporting in confidence on matters concerning fraud, gross misconduct, or deliberate circumvention of security controls by management. Reports can be made anonymously.

---

## 9. Training Requirements

### 9.1 Information Security Awareness Training

All Workforce Members are assigned the mandatory **“Meridian Secure Horizon: Security & Privacy Essentials”** training module upon initial access provisioning and annually thereafter.

| Training Attribute | Specification |
|--------------------|---------------|
| **Platform** | Assigned via Lattice HRIS, hosted on the LMS |
| **Frequency** | Within first 30 days of employment; annually thereafter by December 31st. |
| **Content** | Covers Meridian’s Acceptable Use Policy, phishing identification, data classification handling (PHI and PII focus), secure remote work, incident reporting channels. |
| **Enforcement** | Access to Meridian systems (Okta) is automatically suspended for any user who is 30 days past due on training completion. Reactivation requires CISO approval. |
| **Evidence** | Completion records are exported weekly from Lattice and stored as SOC 2 control evidence for the CC1.4 criteria. |

### 9.2 Phishing Simulation Program

- **Operated By:** CISO Security Operations team using Proofpoint.
- **Frequency:** At minimum, one simulated phishing campaign per quarter.
- **Remediation:** Users who fail the simulation (click the link) are automatically enrolled in a 15-minute refresher “Phishing Awareness Boost” module, which must be completed within 14 days.
- **KPI:** % click rate tracked quarter-on-quarter for SOC 2 reporting. Target is <5%.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policy Framework Documents

| SOP-ID | Document Title | Relationship |
|--------|----------------|--------------|
| SOP-ISEC-002 | Acceptable Use Policy | Tier 1 Policy; sets rules for user behavior with Meridian assets |
| SOP-ISEC-003 | Data Classification Policy | Tier 1 Policy; defines data classes and high-level labeling requirements |
| SOP-ISEC-004 | Access Control Policy | Tier 1 Policy; specifics on IAM roles, RBAC model |
| SOP-ISEC-008 | Incident Response Plan | Tier 3 Procedure; detailed playbooks for ransomware, data exfiltration, etc. |
| SOP-ISEC-012 | Third-Party Security Management Standard | Tier 2 Standard; details vendor security questionnaires |
| SOP-PRD-014 | Clinical AI Post-Market Surveillance Procedure | Tier 3 Procedure; governs adverse event logging for AI |
| SOP-COMP-001 | HIPAA Privacy and Security Compliance Manual | Overarching compliance manual |
| SOP-ENG-005 | Secure SDLC Standard | Tier 2 Standard; SAST, DAST, penetration testing requirements |
| FRM-ISEC-002 | Policy Annual Review Confirmation Form | Template for no-change annual review |
| FRM-ISEC-004 | System Access Request Form | ServiceNow form for joiner/mover |
| FRM-ISEC-009 | Information Security Exception Request Form | ServiceNow form for exceptions |

### 10.2 External Standards and Frameworks

| Standard | Reference in This SOP |
|----------|----------------------|
| **AICPA Trust Services Criteria (TSC) for SOC 2** | Control mapping (Section 6), Monitoring KPIs (Section 7), review cycle designed around audit period. Specifically: CC1.1, CC1.2, CC1.4, CC1.5, CC2.2 (Governance); CC6.1, CC6.2, CC6.6, CC6.7 (Logical and Physical Access); CC7.1, CC7.2, CC7.3 (System Operations); CC8.1 (Change Management); A1.2, A1.3 (Availability); P4.2 (Confidentiality) |
| **NIST AI RMF 1.0** | AI risk tiering, adversarial robustness testing (Section 5.7), Model lifecycles |
| **Federal Reserve SR 11-7** | Model risk management and independent validation procedures (Section 5.7) |
| **ISO 27001:2022** | ISMS framework, risk-based approach, policy review cycle (Section 5.1) |
| **HIPAA Security Rule (45 CFR § 164.300 et seq.)** | Controls for PHI, IAM procedures, training, incident response (Sections 5.3, 5.4, 5.5, 5.7, 6) |
| **EU AI Act (Regulation 2024/1689)** | High-risk AI transparency, human oversight (Policy Statement 5) |
| **NIST 800-88 (Data Sanitization)** | Disposal standards for Restricted data |

---

## 11. Revision History

| Version | Effective Date | Author | Summary of Changes |
|---------|----------------|--------|--------------------|
| 1.0 | 2020-06-15 | Michael Chen (Former CISO) | Initial establishment of the ISMS Policy Framework post-Series B. Established policy hierarchy and basic HIPAA safeguards. |
| 2.0 | 2022-01-10 | Rachel Kim (CISO) | Major overhaul to align with SOC 2 Type II attestation requirements. Added detailed control mapping to TSC, formalized exception process, introduced quarterly access recertifications. |
| 3.0 | 2024-02-22 | Rachel Kim (CISO) | Incorporated NIST AI RMF and SR 11-7 model risk management requirements for the Clinical AI and HealthPay platforms. Added roles for CAIO. Updated RACI. |
| 3.3 | 2024-09-17 | Rachel Kim (CISO) | Targeted updates following pre-audit readiness assessment: updated backup retention specifics, added detailed leaver access timeline, added P1 incident response SLOs. |
| 3.5 | 2025-03-11 | Rachel Kim (CISO) | Updated effective date for FY25. Enhanced EU AI Act transparency controls into policy statements and SDLC section (5.7). Redefined training sections for new LMS (Lattice) and phishing program. Annual review confirmed with no further changes, next review set for October 2026. |
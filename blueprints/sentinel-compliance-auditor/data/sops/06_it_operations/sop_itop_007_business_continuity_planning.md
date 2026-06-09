---
sop_id: "SOP-ITOP-007"
title: "Business Continuity Planning"
business_unit: "IT Operations & Infrastructure"
version: "2.2"
effective_date: "2025-12-22"
last_reviewed: "2026-11-03"
next_review: "2027-05-26"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# STANDARD OPERATING PROCEDURE
## Business Continuity Planning
### SOP-ITOP-007 | Version 2.2

---

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the framework, governance, and operational procedures for Meridian Health Technologies, Inc.’s enterprise-wide Business Continuity Planning (BCP) program. The purpose of this document is to define the methodology for developing, implementing, testing, and maintaining business continuity capabilities that ensure the resilience of critical business functions during and after a disruptive incident. The BCP program is designed to minimize financial loss, maintain regulatory compliance, protect Meridian’s reputation, and safeguard the interests of patients, healthcare providers, payers, and employees.

This SOP operationalizes Meridian’s commitment to service availability and data integrity as articulated in the Board-level AI Governance Committee charter and aligns with the NIST AI Risk Management Framework, SOC 2 Common Criteria (specifically CC7.1 through CC9.2), and contractual obligations to covered entity partners.

### 1.2 Scope
This SOP applies to all Meridian Health Technologies business units, departments, personnel, contractors, and third-party service providers who support or rely upon:

- **Clinical AI Platform** — Deployed across 340+ hospitals and clinics, classified as high-risk AI systems under the EU AI Act Annex III.
- **HealthPay Financial Services** — Payment processing, patient financing, medical lending, and claims automation systems processing approximately $4.2 billion annually.
- **MedInsight Analytics** — Population health analytics platform supporting health systems and insurers with data from approximately 12 million patient records.
- **Meridian SaaS Platform** — Multi-tenant cloud infrastructure hosted on AWS (us-east-1, eu-west-1) with Azure serving as disaster recovery target.
- **Corporate Systems** — Internal IT infrastructure, including identity management (Okta), communications, human resources, and financial systems operating across global offices in Boston, London, Berlin, Singapore, and Toronto.

**Geographic Scope:** All global locations where Meridian operates, processes data, or delivers services.

**Temporal Scope:** This SOP is in effect continuously from the effective date listed in the document metadata. The Business Continuity Plan transitions from steady-state planning to active execution upon declaration of a disruptive incident by authorized personnel as defined in Section 3.

### 1.3 Out of Scope
The following are explicitly outside the scope of this SOP and are governed by separate policies:
- Information Security Incident Response — Governed by SOP-ISMS-003 (Security Incident Response and Management).
- Disaster Recovery technical procedures for IT systems — Governed by SOP-ITOP-004 (IT Disaster Recovery Operations).
- Product-specific technical failover and redundancy procedures — Maintained in engineering runbooks within the Meridian SaaS Platform knowledge base.
- Occupational health and safety procedures during physical emergencies — Managed by Corporate Facilities and Security.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Business Continuity Plan (BCP)** | A documented collection of procedures and information that is developed, compiled, and maintained in readiness for use in a disruptive incident to enable Meridian to continue to deliver its critical business functions at acceptable predefined levels. |
| **Business Continuity Program** | The ongoing enterprise governance and management process, supported by executive leadership and resourced appropriately, to ensure that necessary steps are taken to identify the impact of potential losses, maintain viable recovery strategies and plans, and ensure continuity of services through training, exercising, and maintenance. |
| **Business Impact Analysis (BIA)** | The process of analyzing business functions and the effect that a disruption may have upon them. The BIA identifies maximum tolerable periods of disruption (MTPD), recovery time objectives (RTO), recovery point objectives (RPO), and resource dependencies. |
| **Maximum Tolerable Period of Disruption (MTPD)** | The maximum duration a critical business function can be unavailable before Meridian incurs unacceptable consequences, including regulatory action, financial losses exceeding $500,000, or irreversible harm to patient safety. |
| **Recovery Time Objective (RTO)** | The targeted duration of time within which a business function, application, or system must be restored after a disruption to avoid unacceptable consequences. RTOs are always less than or equal to MTPDs. |
| **Recovery Point Objective (RPO)** | The maximum targeted period in which data might be lost due to a major incident. RPO is measured in time (e.g., 15 minutes, 1 hour). |
| **Critical Business Function (CBF)** | A business function or set of activities that, if disrupted, would directly impact patient safety, cause significant regulatory non-compliance, result in financial losses exceeding $250,000 per day, or severely damage Meridian's market reputation. |
| **Disruptive Incident** | Any event that causes, or has the potential to cause, an unplanned interruption to Meridian's critical business functions. This includes, but is not limited to, cyber-attacks, ransomware events, infrastructure failures, natural disasters, pandemics, and critical third-party service failures. |
| **Crisis Management Team (CMT)** | The executive-level leadership group responsible for strategic decision-making, communications, and resource authorization during a declared disruptive incident. |
| **Business Continuity Coordinator (BCC)** | An individual designated within each business unit responsible for maintaining unit-specific continuity plans, participating in BIA updates, and coordinating plan activation within their functional area. |
| **Alternate Work Site** | A pre-designated and equipped physical or virtual location from which personnel may perform critical business functions when primary locations are inaccessible. |
| **Call Tree** | A hierarchical telecommunication and notification procedure used for rapid mobilization of personnel during plan activation. |
| **Service Level Agreement (SLA)** | A documented agreement between Meridian and an internal or external customer that defines the expected level of service, performance metrics, and remedies for non-performance. |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| **AI RMF** | Artificial Intelligence Risk Management Framework (NIST AI 100-1) |
| **BCP** | Business Continuity Plan |
| **BCP-DR** | Business Continuity Planning and Disaster Recovery |
| **BIA** | Business Impact Analysis |
| **BCC** | Business Continuity Coordinator |
| **CBF** | Critical Business Function |
| **CISSP** | Certified Information Systems Security Professional |
| **CMT** | Crisis Management Team |
| **CRO** | Chief Risk Officer (function currently performed by Chief Compliance Officer) |
| **CSF** | HITRUST Common Security Framework |
| **DR** | Disaster Recovery |
| **EOC** | Emergency Operations Center |
| **HIPAA** | Health Insurance Portability and Accountability Act |
| **ISMS** | Information Security Management System |
| **MTPD** | Maximum Tolerable Period of Disruption |
| **PHI** | Protected Health Information |
| **RACI** | Responsible, Accountable, Consulted, Informed |
| **RPO** | Recovery Point Objective |
| **RTO** | Recovery Time Objective |
| **SOC 2** | System and Organization Controls 2 (AICPA Trust Services Criteria) |
| **SOP** | Standard Operating Procedure |
| **SPOF** | Single Point of Failure |
| **VM** | Virtual Machine |

---

## 3. Roles and Responsibilities

The following RACI matrix defines the roles and responsibilities for the Meridian BCP program. Detailed role descriptions follow the matrix.

### 3.1 RACI Matrix

| Activity / Deliverable | Board AI Governance Committee | CEO | Chief AI Officer | CISO | VP IT Ops (BCP Owner) | Chief Compliance Officer | VP Engineering | Business Unit VPs | Business Continuity Coordinators | All Personnel |
|---|---|---|---|---|---|---|---|---|---|---|
| **Program Governance & Funding** | A | R | C | C | I | C | C | I | I | — |
| **BCP Policy Approval** | I | A | C | C | R | C | C | C | I | — |
| **Business Impact Analysis** | I | I | C | C | A | I | I | R | R | — |
| **Continuity Strategy Selection** | I | I | C | C | R | C | A | C | C | — |
| **Plan Documentation & Maintenance** | I | I | I | I | A | I | I | C | R | — |
| **Plan Testing & Exercises** | I | I | I | I | A | I | C | C | R | I |
| **Crisis Management (During Incident)** | I | A | C | C | R | C | C | I | I | — |
| **Plan Activation Authority** | — | A | R (AI Systems) | R (Security) | R (Infra) | — | — | — | — | — |
| **Internal Audit & Assessment** | I | I | I | I | C | R | I | I | I | — |
| **BCP Awareness Training** | I | I | I | I | A | I | I | I | I | R |
| **Third-Party BCP Review** | I | I | I | R | A | C | I | C | I | — |
| **Regulatory Reporting** | C | C | C | C | I | R | I | I | I | — |

**Key:** R = Responsible (performs), A = Accountable (owns), C = Consulted (advises), I = Informed (notified)

### 3.2 Detailed Role Descriptions

#### 3.2.1 Board of Directors — AI Governance Committee
- **Role:** Ultimate governance oversight of business resilience as it relates to AI systems and enterprise risk.
- **Responsibilities:**
  - Review and endorse the BCP policy annually.
  - Receive quarterly BCP program status reports, including test results and audit findings.
  - Authorize capital expenditures exceeding $1 million for continuity-related infrastructure.

#### 3.2.2 Chief Executive Officer (Dr. Sarah Chen)
- **Role:** Executive sponsor and ultimate decision-maker during crisis events.
- **Responsibilities:**
  - Activate the Crisis Management Team and declare a corporate-level emergency per Section 5.3.
  - Serve as primary external communicator for high-severity incidents.
  - Authorize emergency expenditures from corporate contingency reserves.

#### 3.2.3 Chief AI Officer (Dr. Marcus Rivera)
- **Role:** Accountable for continuity of clinical AI systems and AI-specific incident response.
- **Responsibilities:**
  - Ensure Clinical AI Platform continuity strategies meet EU AI Act human oversight obligations during degraded operations.
  - Authorize AI model rollback or failover to rule-based fallback systems.
  - Coordinate with VP of Clinical AI Products (Dr. Aisha Okafor) on patient safety impact assessments during disruptions.

#### 3.2.4 Chief Information Security Officer (Rachel Kim)
- **Role:** Responsible for security-related incident detection and containment coordination.
- **Responsibilities:**
  - Declare security-related disruptive incidents per SOP-ISMS-003.
  - Coordinate forensic investigation and evidence preservation during cyber-related BCP activations.
  - Ensure continuity controls maintain SOC 2 security criteria during failover.

#### 3.2.5 VP of IT Operations (Samantha Torres) — BCP Program Owner
- **Role:** Owner of this SOP and the enterprise BCP program.
- **Responsibilities:**
  - Maintain and update this SOP on a scheduled basis.
  - Commission and oversee the annual BIA cycle, due each fiscal Q2.
  - Coordinate all BCP exercises, ensuring lessons learned are captured and remediated within 90 days.
  - Maintain the Meridian Emergency Notification System (PagerDuty and Everbridge).
  - Serve as primary CMT Operations Lead during plan activation.
  - Present quarterly BCP metrics to the AI Governance Committee.
  - Ensure alignment with ISO 22301 principles even where formal certification is not yet pursued.

#### 3.2.6 VP of Engineering (David Park)
- **Role:** Accountable for technical architecture enabling BCP objectives.
- **Responsibilities:**
  - Ensure all production systems are architected to meet defined RTOs and RPOs as specified in the BIA.
  - Approve technical recovery procedures maintained in engineering runbooks.
  - Direct engineering teams during technical recovery operations under CMT strategic direction.

#### 3.2.7 Chief Compliance Officer (Thomas Anderson)
- **Role:** Regulatory oversight and audit coordination.
- **Responsibilities:**
  - Ensure BCP program meets SOC 2 Common Criteria series CC7 (System Operations) and CC9 (Risk Mitigation).
  - Coordinate external auditor access for SOC 2 Type II and HITRUST CSF assessments.
  - Manage regulatory notifications per applicable requirements (excluding HIPAA Breach Notification Rule 45 CFR §§ 164.400-414, which are not addressed in this document).

#### 3.2.8 Chief Privacy Officer / DPO (Dr. Klaus Weber)
- **Role:** EU data protection oversight during continuity events.
- **Responsibilities:**
  - Advise on GDPR implications of data failover to non-EU regions (Azure DR from eu-west-1).
  - Maintain Article 30 Records of Processing, updated to reflect BCP data flows.

#### 3.2.9 VP of Financial Services (Robert Liu)
- **Role:** Responsible for HealthPay continuity.
- **Responsibilities:**
  - Ensure SR 11-7 model risk management for credit and fraud models remains operational during disruptions.
  - Coordinate with banking partners on payment processing failover.

#### 3.2.10 Business Unit VPs and Business Continuity Coordinators (BCCs)
Each business unit VP shall designate a Business Continuity Coordinator and an alternate. Current BCC assignments as of 2026-11-03:

| Business Unit | Primary BCC | Alternate BCC |
|---|---|---|
| IT Operations & Infrastructure | James Okonkwo, Senior Infrastructure Manager | Priya Srinivasan, Cloud Operations Lead |
| Clinical AI Products | Dr. Lena Park, AI Safety Lead | Sanjay Mehta, MLOps Engineering Manager |
| HealthPay Financial Services | Catherine Wu, Director of Payment Operations | Marcus Lee, Risk Analytics Lead |
| MedInsight Analytics | Dr. Omar Hassan, Data Platform Manager | Yuki Tanaka, Analytics Operations Lead |
| Engineering (Platform) | Alex Rodriguez, SRE Manager | Fatima Adebayo, Platform Architect |
| Customer Operations | Sarah Mitchell, Customer Success Director | David Kim, Support Operations Lead |
| Corporate (HR, Finance, Legal) | Patricia Nguyen, HR Operations Director | Kevin O'Brien, Financial Controller |
| Berlin Office | Lukas Hartmann, EU Operations Lead | Anja Vogel, IT Manager |
| London Office | Thomas Clarke, UK Country Lead | Emma Davies, Operations Coordinator |
| Singapore Office | Wei Ling Tan, APAC Operations Director | Ravi Patel, Regional IT Lead |
| Toronto Office | Jean-François Bélanger, Canada Country Lead | Sarah Thompson, IT Manager |

**BCC Responsibilities:**
- Develop, maintain, and exercise business unit continuity plans.
- Identify and document unit CBFs, dependencies, and recovery strategies.
- Maintain accurate call trees, resource inventories, and alternate work site information.
- Participate in and coordinate the annual BIA.
- Report plan status and test results to the BCP Program Owner quarterly.

#### 3.2.11 All Personnel
- **Role:** Individual preparedness and cooperation.
- **Responsibilities:**
  - Complete annual BCP awareness training via Meridian's Learning Management System (Workday Learning).
  - Maintain current emergency contact information in Workday.
  - Follow instructions from BCCs and CMT during plan activation.
  - Report potential continuity threats or vulnerabilities to the Security Operations Center (SOC@meridianhealth.io).

---

## 4. Policy Statements

### 4.1 Enterprise Commitment to Resilience
Meridian Health Technologies is committed to maintaining the resilience of critical business functions that support patient care, financial transactions, and protected health information processing. Business continuity is a strategic imperative integrated into the company's governance, risk management, and operational planning processes.

### 4.2 Policy Principles

**Policy Statement 1 — Proportionality and Risk-Based Approach**
Meridian shall allocate BCP resources based on a risk-based assessment of potential business impact. Business functions shall be prioritized based on their criticality to patient safety, regulatory compliance, financial stability, and stakeholder trust. CBFs identified through the BIA process shall receive priority access to continuity resources.

**Policy Statement 2 — Defined Recovery Objectives**
All CBFs shall have documented, approved RTOs and RPOs. Recovery objectives shall be derived from a formal BIA conducted annually and upon significant organizational changes. Technical architectures shall be designed and maintained to meet or exceed documented recovery objectives.

**Policy Statement 3 — Regular Testing and Exercising**
The BCP program shall be tested at minimum according to the schedule defined in Section 5.6. Tests shall be designed to validate recoverability, identify gaps, and train personnel. Tests that fail to meet stated objectives shall trigger a formal remediation process with tracked corrective actions.

**Policy Statement 4 — Crisis Management Governance**
During a disruptive incident, the Crisis Management Team shall be convened as defined in Section 5.3. The CMT shall operate under a clear command structure with documented decision authority. External communications shall be coordinated through designated spokespersons to ensure accuracy and consistency.

**Policy Statement 5 — Continuous Improvement**
The BCP program shall operate under a Plan-Do-Check-Act (PDCA) cycle. Test results, actual incidents, audit findings, and changes in the business environment shall be systematically collected and used to improve continuity capabilities. The BCP program effectiveness shall be reported to executive leadership and the Board quarterly.

**Policy Statement 6 — Third-Party Resilience**
Critical third-party vendors and service providers (including AWS, Azure, Snowflake, Okta, CrowdStrike, and banking partners) shall be assessed for BCP capabilities during vendor selection and annually thereafter. Contracts with critical vendors shall include right-to-audit clauses for BCP controls.

**Policy Statement 7 — Documentation and Accessibility**
BCP documentation, including this SOP, BIAs, and unit-level plans, shall be maintained in the Meridian Policy Management System (Vanta) and the Meridian Configuration Management Database (ServiceNow). Plans shall be accessible via offline channels during a disruption. All plans shall be reviewed and updated at least annually.

**Policy Statement 8 — Emergency Communications**
Meridian shall maintain a redundant emergency notification system capable of reaching all personnel via multiple channels (SMS, voice, email, mobile app push). The system shall be tested quarterly. Personnel are required to acknowledge test notifications within 2 hours per SOC 2 control CC7.1.

### 4.3 Policy Compliance
Non-compliance with this SOP shall be managed per the Exception Handling process defined in Section 8. Willful non-compliance or negligence resulting in extended disruption to CBFs is subject to disciplinary action, up to and including termination, per Meridian Human Resources policies.

---

## 5. Detailed Procedures

### 5.1 Business Impact Analysis (BIA) Procedure

The BIA is the foundational process that informs all continuity strategies. The VP of IT Operations shall commission a formal BIA annually, with completion required by the end of Q2 (June 30).

#### 5.1.1 BIA Scheduling and Triggers
A full enterprise BIA shall be conducted under the following conditions:
- **Annual Cycle:** Scheduled each year in April, with delivery by June 30.
- **Trigger-Based:** Initiated within 60 calendar days of any of the following:
  - Merger, acquisition, or divestiture of a business unit.
  - Launch of a new product line (e.g., a new Clinical AI module).
  - Significant architectural change (e.g., migration of primary workloads to a new cloud region).
  - A material actual disruption that reveals previously unknown dependencies.

#### 5.1.2 BIA Data Collection
The VP of IT Operations shall distribute the BIA Questionnaire (Form BC-001, maintained in Vanta) to all Business Continuity Coordinators. The questionnaire collects:

| Data Field | Description |
|---|---|
| **Business Function Name** | Official functional designation. |
| **Function Description** | Narrative of activities performed. |
| **Function Tier** | Tier 0 (Life Safety / Patient Harm), Tier 1 (Regulatory / >$250K Daily Impact), Tier 2 (Operational Impact). |
| **Maximum Tolerable Period of Disruption (MTPD)** | Duration before unacceptable consequences manifest (hours/days). |
| **Recovery Time Objective (RTO)** | Targeted recovery time, which must be ≤ MTPD. |
| **Recovery Point Objective (RPO)** | Maximum acceptable data loss expressed in time. |
| **Peak Operational Periods** | Monthly/quarterly/annual cycles (e.g., end-of-month payment processing). |
| **Upstream Dependencies** | Applications, systems, data feeds, or external vendors required. |
| **Downstream Dependencies** | Functions that depend on this function's outputs. |
| **Minimum Staffing Requirements** | Role types and headcount required for manual workarounds. |
| **Minimum Technology Requirements** | Hardware, software, network, and telephony needed. |
| **Vital Record Requirements** | Essential documents, records, or data (legal, financial, clinical). |
| **Alternate Work Site Requirements** | Physical or virtual workspace, including accessibility needs. |
| **Regulatory Constraints** | Specific laws or standards (e.g., GDPR territoriality). |

#### 5.1.3 Critical Business Function Tiering

| Tier | Definition | Examples at Meridian | Required RTO |
|---|---|---|---|
| **Tier 0 — Life Safety** | Disruption directly risks patient harm or loss of life. | Clinical AI real-time inference engines for radiology or oncology treatment planning. | ≤ 4 hours |
| **Tier 1 — Critical** | Disruption causes regulatory breach or financial loss exceeding $250,000/day. | HealthPay payment processing, MedInsight data delivery to covered entity partners, AWS us-east-1 core infrastructure. | ≤ 8 hours |
| **Tier 2 — Essential** | Disruption significantly degrades services but does not immediately trigger regulatory or severe financial impact. | Internal developer tooling, test environments, non-production analytics. | ≤ 72 hours |
| **Tier 3 — Support** | Disruption creates inconvenience but core operations continue. | Corporate intranet, office productivity software. | ≤ 5 business days |

#### 5.1.4 BIA Validation and Approval
1. BCCs submit completed BC-001 forms to VP of IT Operations by May 15 of the cycle year.
2. VP of IT Operations consolidates findings into the Enterprise BIA Report (Form BC-002).
3. A BIA review workshop is conducted with all VPs and key architects (Chief AI Officer, VP Engineering, VP Infrastructure) during the first week of June.
4. RTO/RPO values are scrutinized and validated against technical feasibility. Discrepancies are escalated to the CMT Sponsor (CEO or designee) for adjudication.
5. The final BIA is approved by the CEO and presented to the AI Governance Committee in Q2.

#### 5.1.5 Current Validated RTO/RPO Matrix (Summary as of BIA 2026)
The following table presents the current validated CBF recovery objectives. Detailed application-level RTOs are maintained in SOP-ITOP-004.

| Critical Business Function | Business Unit | Tier | MTPD | RTO | RPO |
|---|---|---|---|---|---|
| Clinical AI Inference Engine (Oncology) | Clinical AI Products | 0 | 4 hours | 2 hours | 15 minutes |
| Clinical AI Inference Engine (Radiology) | Clinical AI Products | 0 | 6 hours | 4 hours | 15 minutes |
| HealthPay Transaction Processing | HealthPay Financial Services | 1 | 24 hours | 8 hours | 1 hour |
| MedInsight Data Platform | MedInsight Analytics | 1 | 24 hours | 12 hours | 4 hours |
| Meridian SaaS Platform (Core API Gateway) | Engineering | 1 | 12 hours | 4 hours | 1 hour |
| Identity Management (Okta) | IT Operations | 1 | 8 hours | 4 hours | 1 hour |
| Developer CI/CD Pipeline | Engineering | 2 | 72 hours | 24 hours | 24 hours |
| Corporate ERP (Finance/HR) | Corporate | 2 | 72 hours | 48 hours | 24 hours |

---

### 5.2 Continuity Strategy Development

Based on the approved BIA, each business unit BCC, in collaboration with the VP of IT Operations and VP of Engineering, shall develop or update continuity strategies for all CBFs. Strategies must be documented in the Meridian Business Continuity Strategy Template (Form BC-003) and submitted within 60 calendar days of BIA approval (by August 31).

#### 5.2.1 Strategy Selection Framework
Strategies are selected based on the tier of the function:

| Tier | Mandatory Strategies Required |
|---|---|
| **Tier 0** | Active/Active deployment across at least 2 AWS Availability Zones, or multi-region Active/Passive with automated failover via Route 53 Application Recovery Controller. AI model fallback rule engine deployed in separate region. |
| **Tier 1** | Multi-AZ deployment with cross-region backup and automated recovery runbooks. Data replication to Azure DR region (us-east-1 to Azure East US 2; eu-west-1 to Azure West Europe). Quarterly DR testing. |
| **Tier 2** | Backup to secondary region. Recovery via documented manual runbooks. Semi-annual testing. |
| **Tier 3** | Backup. Recovery within 5 business days. Annual testing. |

#### 5.2.2 Strategy Categories

**A. Technology Recovery Strategies**
- **Cloud Infrastructure Failover:** Defined per SOP-ITOP-004. Leverages AWS Elastic Disaster Recovery for Tier 0/1 workloads, enabling RPOs of seconds and RTOs under 1 hour for specific VMs. Azure Site Recovery is configured for failover of Tier 1 workloads, providing recovery to Azure as an alternate site.
- **Data Replication:** Amazon RDS Multi-AZ for transactional databases. Cross-Region Read Replicas for Tier 0 analytical workloads. AWS Backup for EBS, EFS, DynamoDB, and S3 resources, with cross-region copy enabled for Tier 0 and Tier 1 data.
- **Container Orchestration:** Amazon EKS clusters deployed across multiple AZs. Node groups in DR region maintained in warm standby.
- **AI Model Failover:** Pre-staged validated model artifacts in AWS S3 in DR region. Rule-based clinical fallback engines (for situations where AI inference is unavailable) maintained in a deployable state. Dr. Marcus Rivera (Chief AI Officer) shall maintain a register of approved fallback models per EU AI Act Article 14(5) regarding human oversight capabilities.

**B. Workforce Continuity Strategies**
- **Remote Work:** All critical personnel shall be equipped with Meridian-managed laptops configured with VPN (AWS Client VPN) and Zero Trust Network Access (ZTNA via CrowdStrike Falcon). This enables dispersal from primary offices.
- **Alternate Work Sites:** Pre-arranged agreements with Regus (global) for swing office space in Boston Metro, London (Bishopsgate), Berlin (Mitte), Singapore (Marina Bay), and Toronto (Financial District). Agreements reviewed annually by Corporate Facilities.
- **Role Redundancy:** Critical functions shall have documented secondary and tertiary personnel capable of performing essential tasks. BCCs shall maintain role succession matrices.

**C. Third-Party Service Continuity**
- **AWS and Azure:** Meridian relies on AWS and Azure BCP capabilities, which are reviewed through the annual AWS SOC 2 Type II report and Azure SOC 2 Type II report. Meridian IT Operations shall configure account-level health alerts via AWS Health Dashboard and Azure Service Health.
- **Okta:** Meridian maintains a break-glass procedure for Okta outages, documented in SOP-ISMS-001 (Access Control). Administrative access to AWS via IAM users (not federated) is documented in a physical break-glass envelope stored in the Boston office safe (and scanned, encrypted, stored in an isolated S3 bucket).
- **PagerDuty:** The PagerDuty instance is operated outside of Meridian primary infrastructure. Incident response procedures are maintained offline as PDF documents on BCC company mobile devices.

#### 5.2.3 Strategy Documentation
Each BCC shall maintain a Unit-Level Business Continuity Plan (UL-BCP) document. The UL-BCP template (Form BC-004) contains:

1. Unit and CBF identification.
2. Contact information and call tree for unit personnel.
3. Detailed recovery procedures per strategy (step-by-step runbook references).
4. Resource inventory, including hardware, software, licenses, and vital records.
5. Alternate work site procedures.
6. Manual workaround procedures for Tier 0, Tier 1 functions where applicable.

All UL-BCPs must be stored in the Meridian Policy Management System (Vanta) and a printed copy must be securely stored at the designated alternate work site for that unit. Electronic copies in a non-editable format (PDF) must also be stored offline on the BCC and alternate BCC company mobile devices.

---

### 5.3 Plan Activation and Incident Management

This section defines the process for transitioning from steady-state BCP operations to active response during a disruptive incident.

#### 5.3.1 Incident Declaration Authority
The following roles are authorized to declare a BCP-activating disruptive incident:

| Role | Scope of Declaration |
|---|---|
| **CEO (Dr. Sarah Chen)** | Any corporate-wide incident. |
| **Chief AI Officer (Dr. Marcus Rivera)** | Incidents specifically impacting Clinical AI Platform Tier 0 functions. |
| **CISO (Rachel Kim)** | Security-related incidents (per SOP-ISMS-003). |
| **VP of IT Operations (Samantha Torres)** | Infrastructure, data center, and IT service incidents. |
| **VP of Engineering (David Park)** | Software service degradation incidents. |
| **VP Financial Services (Robert Liu)** | HealthPay transaction processing incidents. |
| **Chief Compliance Officer (Thomas Anderson)** | Incidents with immediate regulatory notification requirements. |

Any Meridian employee may initiate a potential incident report by contacting the Meridian Security Operations Center via:
- **Phone:** +1-617-555-0199 (SOC Hotline)
- **Email:** soc@meridianhealth.io
- **PagerDuty:** Acknowledge through the designated service.

#### 5.3.2 Incident Severity Classification
Upon initial report, the SOC on-call engineer shall triage the incident based on the Meridian Incident Severity Matrix:

| Severity | Definition | Example | Declaration Authority | CMT Activation |
|---|---|---|---|---|
| **SEV 1 — Critical** | Direct patient safety risk; OR >$500K financial impact expected; OR >1 hour outage of Tier 0 function; OR active confirmed ransomware. | Clinical AI Inference Engine unavailable; HealthPay outage during market hours; Data exfiltration in progress. | CISO, VP IT Ops, or CEO | Full CMT within 30 minutes. |
| **SEV 2 — Major** | Outage of Tier 1 function exceeding 2 hours; OR potential data integrity concern; OR credible threat. | MedInsight unavailable beyond RTO; Okta partial outage. | VP IT Ops or VP Engineering | Partial CMT (Ops Lead + impacted BU VP) within 1 hour. |
| **SEV 3 — Minor** | Tier 2 function outage; OR Tier 1 outage within RTO bounds; OR low-confidence threat. | CI/CD pipeline down. | BCC or On-Call SRE | No CMT. BCC managed per Unit BCP. |

#### 5.3.3 Crisis Management Team (CMT) Activation
Upon declaration of a SEV 1 incident, or as directed by the CEO:

**Step 1 — Convene CMT (T+0 to T+30 minutes)**
- SOC initiates the CMT conference bridge (Zoom Webinar Room, pre-configured with dial-in, accessible via PSTN for resilience).
- SOC sends PagerDuty high-urgency notification to the CMT roster (CEO, Chief AI Officer, CISO, VP IT Ops, VP Engineering, Chief Compliance Officer, General Counsel, VP Corporate Communications).
- Initial bridge to form within 15 minutes; quorum (CEO or CISO + 2 other VPs) within 30 minutes.

**Step 2 — Situation Assessment (T+15 to T+60 minutes)**
- CISO presents known facts: What has been disrupted? What is the security posture? Has patient data been impacted?
- VP IT Ops presents: Infrastructure status. Is this a physical or virtual event? Which Availability Zones are affected? Has DR been triggered?
- VP Engineering presents: Application performance data from Datadog. Error rates, latency, throughput. Is this a code regression, dependency failure, or external attack?
- Chief AI Officer presents: Clinical AI model status. Are fallback rule engines active?

**Step 3 — Declare Emergency and Activate BCP (T+30 to T+90 minutes)**
- CEO (or delegated authority) formally declares a corporate emergency.
- CMT Operations Lead (Samantha Torres) directs all BCCs to activate unit-level BCPs per the Unit-Level Business Continuity Plans.
- The Everbridge system is triggered with a pre-scripted notification to all personnel informing them of the incident and any immediate actions (e.g., "Do not VPN in until cleared").
- Internal and external communications are managed per SOP-CORP-002 (Crisis Communications).

**Step 4 — Operational Execution of BCP**
- IT Operations (led by VP IT Ops) executes technical failover runbooks per SOP-ITOP-004.
- Engineering (led by VP Engineering) directs SRE teams to restore application services.
- Business unit BCCs account for personnel via Everbridge acknowledgment, initiate manual workarounds, and coordinate with downstream customers (e.g., hospital IT departments) per unit plans.

**Step 5 — Stand Down and Transition to Recovery**
- When CBFs are restored to minimum acceptable levels per the BIA, the CMT votes to stand down from crisis mode.
- Operational recovery (full restoration, root cause analysis, forensic investigation) continues under standard operations and incident management (SOP-ISMS-003).
- A formal post-incident review is mandatory for all SEV 1 and SEV 2 incidents, per Section 5.7.

---

### 5.4 Recovery Procedures Overview

Detailed technical recovery procedures are maintained in SOP-ITOP-004 (IT Disaster Recovery Operations) and engineering runbooks. This section provides the procedural governance overlay.

#### 5.4.1 Recovery Tier Assignment
During activation, the CMT Operations Lead assigns a Recovery Tier to each CBF based on the current BIA and the nature of the incident. This ensures that resources are concentrated on Tier 0 and Tier 1 functions.

#### 5.4.2 Recovery Sequencing
1. **Core Infrastructure:** DNS (Route 53), Networking (Transit Gateway, Direct Connect), Identity (Okta break-glass).
2. **Tier 0 Clinical AI:** Activate DR region AI model artifacts, establish inference API endpoints, redirect clinical traffic via Route 53 Application Recovery Controller.
3. **Tier 1 HealthPay:** Restore transactional databases, reconcile with payment gateways, resume processing.
4. **Tier 1 MedInsight:** Restore data platform, validate data integrity, resume data delivery to partners.
5. **Tier 1 SaaS Platform:** Restore core API services, validate S3 data stores.
6. **Tier 2 Functions:** Restore CI/CD, corporate systems.

---

### 5.5 Communications Procedures During Activation

All external communications during a SEV 1 incident shall be conducted under the authority of the CMT. No employee, other than the designated spokespersons, is permitted to communicate with external parties regarding a disruptive incident.

**Designated Spokespersons:**
- **CEO (Dr. Sarah Chen):** For all public and media communications.
- **VP Corporate Communications (if appointed) or Chief Compliance Officer:** For regulatory communications.
- **Customer Operations BCC (Sarah Mitchell):** For direct customer notification and updates.
- **VP of Financial Services (Robert Liu):** For banking and payment partner communications.

**Internal Communications:**
- The CMT shall provide status updates to all personnel via Everbridge/email at minimum every 4 hours during a SEV 1 event.
- BCCs are responsible for cascading operational instructions to their unit personnel.

---

### 5.6 BCP Testing and Exercising Schedule

The BCP program shall be validated through a progressive testing regimen. All tests are coordinated by the VP of IT Operations.

#### 5.6.1 Test Types and Annual Schedule

| Test Type | Frequency | Scope | Participants | Mandated For | Success Criteria |
|---|---|---|---|---|---|
| **Quarterly Call Tree Test** | Quarterly (Jan, Apr, Jul, Oct) | Personnel notification | All personnel via Everbridge | All Tiers | ≥95% personnel acknowledgment within 2 hours. |
| **Tabletop Exercise** | Semi-Annual (Mar, Sep) | Scenario-based walkthrough | CMT + BCCs | All Tiers | ≥90% of injects resolved correctly; ≤3 critical gaps identified. |
| **Functional Exercise (DR Test)** | Semi-Annual (Jun, Dec) | Application failover to DR region | IT Operations, Engineering, QA | Tier 0, Tier 1 | RTO met for ≥95% of tested functions; RPO met with ≤0.5% variance. |
| **Full-Scale Exercise** | Annual (Nov) | Simulated total loss of primary region | All business units, CMT, key vendor partners | All Tiers | Tier 0 and Tier 1 CBFs restored within stated RTOs from the BIA. |

#### 5.6.2 Functional Exercise Procedure (Semi-Annual DR Test)
1. **Planning (T-30 days):** VP IT Ops, VP Engineering, and QA Manager define the test scope, systems to be failed over, data validation criteria, and rollback plan.
2. **Notification (T-14 days):** Notify AWS and Azure support of the impending test (if using any physical or non-cloud resources, or if testing at scale >50% of production fleet). Notify internal stakeholders of test window.
3. **Execution Window:** A 6-hour maintenance window on a Saturday (00:00 UTC to 06:00 UTC) during the designated month.
4. **Playbook Execution:** SREs execute the DR runbooks from SOP-ITOP-004. Steps include:
   - Validate Route 53 health checks have failed primary endpoints.
   - Trigger DR region deployment pipelines (or manual AWS Backup restore if pipelines not available).
   - Restore databases from cross-region snapshots.
   - Conduct application smoke tests against DR endpoints.
   - QA team executes the Business Validation Testing Script (BVTS) suite.
5. **Data Integrity Validation:**
   - Compare row counts and checksums for critical database tables.
   - Validate a sample (0.1% of records) against a known-good production snapshot.
   - Generate a Data Integrity Report (Form BC-005).
6. **Rollback:** Execute documented rollback procedure to return to primary. Validate primary region health.

#### 5.6.3 Test Failure and Remediation
Any test that fails to meet its stated success criteria shall be logged as a Finding in the Meridian Corrective Action System (Jira — BCP Project). The VP of IT Operations assigns the finding to the responsible party:
- **Technical Failures:** Assigned to VP Engineering or relevant engineering manager.
- **Procedural Failures (e.g., BCC unavailability):** Assigned to the respective Business Unit VP.

**Finding Severity & Remediation SLA:**

| Severity | Definition | Remediation Deadline (from test date) |
|---|---|---|
| **Critical** | Failure to meet RTO for a Tier 0 function; data integrity failure. | 30 calendar days. Test must be re-run within 45 days. |
| **High** | Failure to meet RTO for a Tier 1 function. | 60 calendar days. |
| **Medium** | Communication failure; procedure gap not impacting RTO/RPO. | 90 calendar days. |
| **Low** | Documentation defect only. | Next review cycle. |

---

### 5.7 Post-Incident Review and Continuous Improvement

Following any actual SEV 1 or SEV 2 incident, or any test resulting in Critical or High findings, the VP of IT Operations shall conduct a formal Post-Incident Review (PIR).

#### 5.7.1 PIR Procedure
1. **Scheduling:** PIR meeting scheduled within 10 business days of incident stand-down or test completion.
2. **Data Collection:** Gather PagerDuty timeline logs, ServiceNow incident tickets, Everbridge notification reports, Datadog monitoring dashboards, and operational debrief notes from CMT members.
3. **PIR Meeting:** Mandatory attendees include CMT members who participated, relevant BCCs, and owning engineering managers. The meeting is facilitated by the VP of IT Operations (or delegate).
4. **Analysis:** Conduct a "5 Whys" root cause analysis for each major breakdown. Categorize findings per the Corrective Action Framework.
5. **PIR Report:** A formal PIR Report (Form BC-006) is drafted within 5 business days of the meeting. The report includes:
   - Incident timeline.
   - Root cause(s).
   - Impact assessment (financial, operational, patient safety, regulatory).
   - Effectiveness assessment of the activated BCP.
   - List of Corrective and Preventive Actions (CAPAs).
6. **CAPA Tracking:** All CAPAs are entered into Jira (BCP Project) and tracked to closure by the VP of IT Operations. Closure is verified by the Chief Compliance Officer.

---

### 5.8 Vital Records Management

Vital records are Meridian records that are essential for continuing operations during and after a disruption. Each BCC is responsible for identifying and managing vital records for their unit.

The vital records program includes:

1. **Identification:** Conducted as part of the BIA process.
2. **Classification:** Records are classified based on criticality to recovery.
3. **Protection:** Critical vital records must be:
   - Stored in at least two geographically separate locations (e.g., primary S3 bucket in us-east-1, DR copy in Azure East US 2).
   - Backed up with an RPO consistent with the function they support.
   - Accessible via alternative methods if primary systems are unavailable.

**Vital Records Inventory (Summary):**

| Record | Primary Location | DR Location | RPO |
|---|---|---|---|
| Employee roster and contact info | Workday (SaaS), mirrored to Everbridge | Exported quarterly to encrypted S3 bucket in DR region | 24 hours |
| Insurance policies | Corporate Legal SharePoint, replicated to Azure DR | Azure West Europe | 24 hours |
| Banking and payment partner contacts | HealthPay Jira vault | Encrypted PDF in DR S3 | Weekly |
| Clinical AI model registry and fallback rules | AWS S3 (us-east-1, eu-west-1) | Azure DR blob storage + offline archive | 15 minutes (via cross-region S3 replication) |
| Unit-Level BCP documents (PDF) | Vanta, BCC devices | Printed copies at alternate work sites | Updated at each plan review |

---

## 6. Controls and Safeguards

This section maps the internal controls implemented to maintain the BCP program and satisfy applicable Trust Services Criteria. These controls are subject to internal audit by the Chief Compliance Officer and external audit for SOC 2 Type II.

### 6.1 SOC 2 Common Criteria Coverage

The following table details the specific controls, named roles, measurable metrics, and timelines implemented to address SOC 2 Common Criteria series CC7 (Systems Operations) and CC9 (Risk Mitigation).

| SOC 2 Criteria Ref | Criteria Description | Meridian Control | Control Owner | Measurable Metric | Validation Timeline |
|---|---|---|---|---|---|
| **CC7.1** | The entity uses detection and monitoring procedures to identify (1) changes to configurations that result in the introduction of new vulnerabilities, and (2) susceptibilities to newly discovered vulnerabilities. | **BCP-MON-001:** All changes to continuity-critical infrastructure (AWS Route 53 health checks, EKS node groups, database cross-region replication configs) must be approved via a ServiceNow Change Request, with the Change Advisory Board (CAB) reviewing changes impacting Tier 0/1 CBFs. Vulnerability scans (CrowdStrike Falcon Spotlight) run weekly; new critical CVEs impacting BCP infrastructure must be remediated within 48 hours. | VP IT Ops (Infrastructure) + CISO | 100% of BCP-impacting changes reviewed by CAB; 100% of critical CVEs remediated within SLA. | Weekly CAB meeting (every Wednesday 10:00 AM ET). |
| **CC7.2** | The entity monitors system components and the operation of those components for anomalies that are indicative of malicious acts, natural disasters, and errors affecting the entity's ability to meet its objectives; anomalies are analyzed to determine whether they represent security events. | **BCP-MON-002:** All Tier 0/1 CBF systems are monitored 24/7/365 via Datadog and PagerDuty. Anomaly Detection monitors (machine learning-based) are enabled on transaction rates, API latency, and error rates for HealthPay and Clinical AI APIs. AI model drift monitors are enabled to detect data that falls outside the training distribution, which could degrade failover rule engine effectiveness. SOC operates a follow-the-sun model across Boston, London, and Singapore SOC analysts. | CISO (SOC) + Chief AI Officer (AI Anomaly Detection) | Mean Time to Detect (MTTD) for Tier 0 anomalies: ≤ 5 minutes. All P1 alerts acknowledged within 5 minutes 98% of the time. | Real-time PagerDuty dashboard; Monthly MTTD/MTA report to CISO. |
| **CC7.3** | The entity evaluates security events to determine whether they could or have resulted in a failure of the entity to meet its objectives (security incidents). | **BCP-INC-001:** Per Section 5.3 of this SOP, all P1 alerts are triaged per the SEV matrix. Any event meeting SEV 1 or SEV 2 criteria is escalated to the CMT per the activation procedure. A SOC Incident Commander is designated within 5 minutes of SEV 1 classification. | CISO | Mean Time to Triage (MTT) ≤ 15 minutes for SEV 1 events. 100% of SEV 1 events result in CMT activation within 30 minutes. | Incident post-mortem reviews; Quarterly incident response metrics review by CISO and VP IT Ops. |
| **CC7.4** | The entity responds to identified security incidents by executing a defined incident response program to understand, contain, remediate, and communicate security incidents, as appropriate. | **BCP-RES-001:** Technical remediation is executed per SOP-ISMS-003 and this SOP's activation procedures. The CMT Operational Lead (VP IT Ops) directs technical failover during continuity events per Section 5.3.3. A formal Post-Incident Review, including root cause analysis, is conducted for all SEV 1/2 incidents per Section 5.7. | VP IT Ops (PIR Process) | 100% of SEV 1/2 incidents have a formal PIR report filed within 10 business days. All CAPAs entered in Jira BCP Project within 48 hours of PIR meeting. | Tracking via Jira BCP Project; Quarterly review by Chief Compliance Officer. |
| **CC7.5** | The entity identifies, develops, and implements activities to recover from identified security incidents. | **BCP-REC-001:** Recovery activities are governed by this SOP and executed via runbooks (SOP-ITOP-004). The BIA (Section 5.1) defines the recovery parameters (RTO/RPO). Semi-annual DR tests (Section 5.6.2) validate the technical recoverability. The Board-approved capital budget includes a specific line item for "BCP-DR Infrastructure" (FY2027: $1.8M). | VP IT Ops (BCP Owner) + VP Engineering (Architecture) | Semi-annual DR test success rate: 100% for Tier 0/1 functions. DR infrastructure costs within ±10% of budget. | Test results report to CTO/AI Governance Committee within 2 weeks of test. Budget review quarterly by VP IT Ops. |
| **CC8.1** | The entity authorizes, designs, develops or acquires, configures, documents, tests, approves, and implements changes to infrastructure, data, software, and procedures to meet its objectives. | **BCP-CHG-001:** All changes to BCP-related infrastructure, including DR configuration, failover scripts, and BCP documentation, are governed by the Meridian Change Management Policy (SOP-ITOP-002). Emergency changes during a CMT-activated incident may bypass normal CAB approval but must be retroactively reviewed within 72 hours of stand-down. | VP IT Ops (CAB Chair) | 100% of emergency changes retroactively reviewed within 72 hours. Zero unauthorized changes detected in quarterly audits of BCP infrastructure. | CI/CD logs reviewed by CAB; Quarterly audit by Compliance. |
| **CC9.1** | The entity identifies, selects, and develops risk mitigation activities for risks arising from potential business disruptions. | **BCP-RSK-001:** The BIA process (Section 5.1) is the primary risk identification mechanism. Risks are formally documented in the Enterprise Risk Register (maintained in ServiceNow GRC). Continuity strategies (Section 5.2) are designed as direct mitigation responses to identified risks. The AI Governance Committee reviews the Risk Register quarterly. | VP IT Ops (BCP Risk Identification) + Chief Compliance Officer (Risk Register) | Risk Register contains current entries for all Tier 0/1 CBF disruptions. All risks rated "High" or above have mitigation plans with funded budget and owner. | Quarterly Risk Review meeting with CRO/Compliance Officer. |
| **CC9.2** | The entity assesses and manages risks associated with vendors and business partners. | **BCP-VDR-001:** All vendors supporting CBFs (AWS, Azure, Snowflake, Okta, CrowdStrike, PagerDuty, Everbridge) are subject to an annual BCP vendor risk assessment. The Chief Compliance Officer, in consultation with VP IT Ops, reviews the vendor's latest SOC 2 Type II report. Contracts include Service Level Agreements with uptime guarantees and financial penalties. A documented contingency for each critical vendor exists (e.g., Okta break-glass per SOP-ISMS-001; Cloud abstraction where feasible). | CISO (Vendor Security) + Chief Compliance Officer | 100% of Tier 0/1 critical vendors reviewed annually. All vendor SOC 2 reports reviewed and filed in Vanta. | Annual review completed by Q4 (December 31). |

### 6.2 Additional Technical Safeguards

| Control ID | Safeguard | Implementation Detail |
|---|---|---|
| **BCP-SAF-001** | Immutable Backups | All Tier 0/1 production backups (via AWS Backup Vault Lock) are configured with a compliance mode, enforcing a minimum 30-day retention that cannot be deleted or modified by any user, including root, for 7 days after the lock is applied. This is a defense against ransomware actors attempting to delete backups. |
| **BCP-SAF-002** | Out-of-Band Communications | The CMT maintains an out-of-band Signal group (end-to-end encrypted) for coordination in the event corporate communications (Slack, email) are compromised. CMT members are required to have Signal installed on their Meridian-managed mobile devices. A quarterly test message is sent to validate group membership. |
| **BCP-SAF-003** | Air-Gapped Credentials | A physical copy of the AWS Organization root user credentials, and the Okta break-glass administrator password, is stored in a dual-lock safe in the Boston office. The CISO and CEO each hold a key. The combination code is held by the VP of IT Operations. An encrypted digital backup of these credentials is stored in an isolated S3 bucket accessible only via a specific IAM role (BreakGlassAccessRole). Access to this role generates an immediate Critical alert to the SOC. |
| **BCP-SAF-004** | AI Model Artifact Integrity | All Clinical AI model artifacts staged for failover in the DR region are versioned and checksummed (SHA-256). Before activation in a real incident, the checksum of the failover artifact is verified against a manifest stored in AWS DynamoDB (global table replicated to DR). |
| **BCP-SAF-005** | Capacity Reservation | For Tier 0 CBFs in the DR (Azure) region, Meridian maintains Azure Reserved VM Instances and pre-provisioned Azure Kubernetes Service (AKS) node pools to guarantee capacity availability during a regional AWS outage. |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The BCP program's health and effectiveness are measured against the following KPIs:

| KPI ID | KPI Description | Target | Measurement Method | Reporting Frequency |
|---|---|---|---|---|
| **BCP-KPI-01** | BIA Currency | BIA refresh completed by June 30 annually. | Project completion date. | Annually |
| **BCP-KPI-02** | BCP Document Review Compliance | 100% of UL-BCPs reviewed and updated within 12 months. | Vanta document review date. | Quarterly |
| **BCP-KPI-03** | Exercise Completion Rate | ≥90% of scheduled exercises completed on time. | Test schedule vs. actual. | Quarterly |
| **BCP-KPI-04** | Exercise Success Rate (Tier 0/1) | RTO met for ≥95% of tested Tier 0/1 CBFs during DR exercises. | DR test data integrity and timing logs. | Semi-Annually (post-test) |
| **BCP-KPI-05** | Call Tree Acknowledgment Rate | ≥95% of personnel acknowledge quarterly call tree test within 2 hours. | Everbridge reporting dashboard. | Quarterly |
| **BCP-KPI-06** | CAPA Closure Rate | ≥90% of BCP-related CAPAs closed per their committed SLA date. | Jira BCP Project burndown report. | Monthly |
| **BCP-KPI-07** | Personnel Training Completion | ≥98% of active employees complete annual BCP training. | Workday Learning completion reports. | Monthly (during renewal), Annually otherwise |
| **BCP-KPI-08** | Vendor BCP Review Coverage | 100% of Tier 0/1 critical vendors assessed in the current year. | Vendor Risk Register review completed/expired dates. | Quarterly |
| **BCP-KPI-09** | BCP Activation Time | CMT convened and initial situation report delivered within 30 minutes for SEV 1 incidents or exercises. | PagerDuty timeline, Zoom bridge join logs. | Per incident / post-exercise |

### 7.2 Reporting Cadence

| Report | Audience | Frequency | Content |
|---|---|---|---|
| **BCP Program Status Dashboard** | CEO, CISO, VP IT Ops, Chief Compliance Officer | Quarterly | Summary of KPIs, test completion, training stats, open CAPAs. |
| **BCP Executive Summary** | AI Governance Committee (Board) | Quarterly | KPI dashboard, significant findings, DR test results summary, resource status, any regulatory or audit updates. |
| **Post-Exercise Report** | CMT, participating BCCs, QA | Within 2 weeks of exercise | Detailed technical results, gap analysis, CAPAs. |
| **Vendor BCP Assessment Report** | CISO, Chief Compliance Officer, VP IT Ops | Annually (Q4) | Summary of critical vendor SOC 2 report reviews, identified risks. |
| **BCP Audit Report** | AI Governance Committee, CEO | Annually (Q1, following SOC 2 audit) | External auditor BCP findings, management responses, remediation plans. |

---

## 8. Exception Handling and Escalation

### 8.1 Exceptions

An exception to a specific requirement of this SOP may be requested when a business unit or function is unable to comply due to a justifiable technical or business constraint. Exceptions are temporary and must be re-evaluated annually.

#### 8.1.1 Exception Process
1. **Requestor:** Business Unit VP or BCC submits a formal Exception Request via the Meridian GRC system (ServiceNow). The request details the specific section of the SOP from which exemption is sought, the business justification, the compensating control in place, and the proposed duration.
2. **Risk Assessment:** The Chief Compliance Officer evaluates the risk of granting the exception, particularly concerning SOC 2 CC9 series (Risk Mitigation) and any other applicable regulations.
3. **Technical Review:** The VP of IT Operations and VP of Engineering review the technical validity of the compensating control.
4. **Approval Authority:**
   - Exceptions to Tier 2/3 RTO requirements: Approved by VP of IT Operations.
   - Exceptions to Tier 0/1 RTO requirements or testing frequency: Approved jointly by VP of IT Operations, CISO, and Chief AI Officer (for AI systems). Must be documented and reported to the AI Governance Committee at the next quarterly meeting.
   - Any exception to this SOP's core policy statements (Section 4): Must be approved by the CEO.
5. **Documentation:** Approved exceptions are stored in the Policy Exception Register within Vanta. A copy is also attached to the relevant UL-BCP.

#### 8.1.2 Exception Expiry
All exceptions have a maximum duration of 12 months. A renewal request must be submitted 30 calendar days before expiry and undergoes the same review and approval process.

### 8.2 Escalation Path
In the event of non-compliance with an approved plan during a disruptive incident:

1. **First Point of Escalation:** The CMT Operations Lead (VP of IT Operations). This individual has the authority to resolve resource conflicts and inter-team coordination issues.
2. **Second Point of Escalation:** The CISO (for security-imposed constraints) or Chief AI Officer (for AI safety constraints).
3. **Final Escalation:** The CEO. Any decision by the CEO during an active CMT-managed incident is final.

For escalations during steady-state (non-incident) operations regarding BCP program resource allocation, the path is: BCC -> Business Unit VP -> VP of IT Operations -> CEO.

---

## 9. Training Requirements

Ensuring that all Meridian personnel understand their BCP roles is fundamental to program success.

### 9.1 Training Curriculum

| Course ID | Course Title | Target Audience | Frequency | Delivery Method | Content |
|---|---|---|---|---|---|
| **BCP-TRN-001** | Annual Business Continuity Awareness | All personnel, including full-time, part-time, and long-term contractors. | Annually (due by March 31). New hires within 30 days of start. | Online (Workday Learning) | Overview of SOP-ITOP-007; Reporting procedures; Everbridge test participation requirements; Remote work guidelines. |
| **BCP-TRN-002** | Business Continuity Coordinator Training | All BCCs and Alternate BCCs (per Section 3.2.10). | Annually (due by April 30). New BCCs within 30 days of assignment. | Instructor-led (Virtual — Zoom, recording provided) | Deep dive into BIA questionnaire; UL-BCP maintenance; Call tree management; Exercise planning and participation. |
| **BCP-TRN-003** | Crisis Management for CMT | All CMT members (per Section 3.2). | Annually (due June 30). New CMT members within 30 days. | Instructor-led (In-person at Boston HQ or Virtual), includes tabletop simulation | CMT roles, incident command system (ICS), communications discipline, decision-making under uncertainty, press and media training (for spokespersons). |
| **BCP-TRN-004** | Technical DR Runbook Training | IT Operations and Engineering SRE teams. | Quarterly (aligned with major release cycles, due within 15 days of runbook update) | Hands-on Workshop (Instructor: James Okonkwo, Sr. Infrastructure Manager) | Execution of specific DR runbooks from SOP-ITOP-004 in a sandbox environment. |

### 9.2 Training Tracking and Compliance
- All training is tracked in Workday Learning, Meridian's Learning Management System.
- Completion is measured by successfully passing a short quiz (≥80% score for BCP-TRN-001; ≥90% for BCP-TRN-002/003).
- Quarterly, the VP of IT Operations reviews the BCP Training Report. The relevant Business Unit VP is responsible for ensuring their BCCs complete required training by the due date.
- **Escalation:** If an individual or group fails to complete mandatory training within 15 calendar days past the due date, notification is sent to the individual and their direct manager. If not completed within 30 calendar days past due, the individual's VP and the Chief Compliance Officer are notified.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies

| SOP ID | Document Title | Relationship to This SOP |
|---|---|---|
| SOP-ITOP-002 | IT Change Management Policy | Governs the process for changes to BCP infrastructure and documentation. |
| SOP-ITOP-004 | IT Disaster Recovery Operations | Contains the detailed, step-by-step technical runbooks for restoring Meridian systems. This is the subordinate operational document to this policy. |
| SOP-ISMS-001 | Access Control Policy | Defines the break-glass procedures and Identity and Access Management (IAM) policies, including the Okta break-glass account referenced in Section 6.2 of this SOP. |
| SOP-ISMS-002 | Information Security Risk Management | Defines the enterprise risk assessment methodology used to inform the risk-based approach in BCP policy. |
| SOP-ISMS-003 | Security Incident Response and Management | The primary policy for security incident detection, containment, and recovery. BCP activation is a sub-procedure of a SEV 1 security incident. |
| SOP-CORP-002 | Crisis Communications Policy | Governs all internal and external communications during a CMT-activated event. |
| SOP-PRIV-001 | Data Protection and Privacy Policy (GDPR) | Governs data privacy controls, including data sovereignty considerations during cross-region failover from the EU (eu-west-1 to Azure West Europe). |
| SOP-VEND-001 | Third-Party Vendor Risk Management | Defines the initial and ongoing risk assessment process for critical vendors, including BCP reviews. |
| SOP-COMP-001 | Enterprise Compliance and Audit Management | Governs the response to internal and external audit findings, including CAPA tracking. |

### 10.2 External Standards and Frameworks

| Reference | Description |
|---|---|
| **AICPA SOC 2 (2022)** | Trust Services Criteria for Security, Availability, and Confidentiality. Specifically CC7 series (Systems Operations) and CC9 series (Risk Mitigation). Meridian's annual SOC 2 Type II audit tests the controls in Section 6. |
| **HITRUST CSF v11.1** | The HITRUST Common Security Framework, against which Meridian maintains certification. BCP controls are assessed within the HITRUST MyCSF tool. |
| **NIST AI 100-1 (AI RMF)** | Governs the management of AI risks, including the fallback rule engines for Clinical AI during continuity events. |
| **NIST SP 800-34 Rev 1** | Contingency Planning Guide for Federal Information Systems. Used as a guidance document in structuring this BCP, though Meridian is not a federal entity. |
| **EU AI Act (Regulation 2024/1689)** | Specifically Article 14 (Human Oversight) and Article 15 (Accuracy, Robustness, and Cybersecurity) which apply to the high-risk Clinical AI Platform. Continuity strategies must maintain human oversight capability. |
| **EU MDR (2017/745)** | Quality and risk management requirements for medical device software, influencing Clinical AI Platform continuity design. |
| **HIPAA Security Rule (45 CFR Part 160 and Part 164, Subparts A and C)** | Meridian's covered entity partners require BCP controls for the availability of electronic protected health information (ePHI). |

---

## 11. Revision History

| Version | Effective Date | Author | Summary of Changes |
|---|---|---|---|
| 1.0 | 2023-04-15 | Samantha Torres | Initial release of the Business Continuity Planning SOP. Established foundational BIA, plan structure, and annual testing. |
| 1.1 | 2024-01-28 | James Okonkwo (Infrastructure Manager) | Minor revision; updated BCC assignments, updated Everbridge configuration details, and corrected call tree test scheduling. |
| 2.0 | 2024-11-10 | Samantha Torres | Major revision. Integrated requirements for Clinical AI Platform continuity per EU AI Act. Introduced formal RPO/RTO matrix. Migrated DR technical procedures to a separate, subordinate SOP (SOP-ITOP-004). Updated to align with ISO 22301 framework. |
| 2.1 | 2025-08-15 | Samantha Torres | Incorporated findings from the 2025 SOC 2 Type II audit (CC7.4 evidence improvements). Added specific Cloud abstraction strategy references. Updated vendor list to include new APAC banking partners. Added quarterly tabletop requirement for CMT. Updated CEO to Dr. Sarah Chen. |
| 2.2 | 2025-12-22 | Samantha Torres | Comprehensive revision. Enhanced SOC 2 criteria mapping with specific control IDs, roles, metrics, and timelines (Section 6). Added Section 4 Policy Statements. Updated to reflect Boston, London, Berlin, Singapore, and Toronto office network. Added Tier classification for CBFs. Expanded test severity classification and CAPA SLAs. Added Section 8.1 formal exception handling process. Updated all BCC assignments per 2026 organizational changes. Incorporated BCP-TRN-004 technical training. |
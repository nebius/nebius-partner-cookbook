---
sop_id: "SOP-HR-008"
title: "Mandatory Compliance Training"
business_unit: "Human Resources"
version: "3.2"
effective_date: "2025-11-26"
last_reviewed: "2026-12-15"
next_review: "2027-06-06"
owner: "Jennifer Walsh, Chief Human Resources Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "HIPAA"
  - "SOC 2"
  - "GDPR"
  - "EU AI Act"
status: "Active"
---

# Standard Operating Procedure: Mandatory Compliance Training

**SOP-HR-008 | Version 3.2**
**Effective Date: 2025-11-26**
**Owner: Jennifer Walsh, Chief Human Resources Officer**
**Business Unit: Human Resources**

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, requirements, and operational processes for the Mandatory Compliance Training Program at Meridian Health Technologies, Inc. The program is designed to ensure that all personnel—employees, contractors, temporary staff, and third-party vendors with system access—possess and maintain the knowledge, skills, and awareness necessary to fulfill their regulatory obligations, protect sensitive data, and uphold the company's ethical and legal commitments across all jurisdictions in which Meridian operates.

This SOP provides the mechanism through which Meridian demonstrates to auditors, regulators, and clients the systematic delivery and tracking of compliance education as a critical internal control, specifically supporting the requirements of SOC 2 Common Criteria (CC) series and the EU AI Act. The program operationalizes the principle that compliance is a continuous state of readiness, not a periodic event.

### 1.2 Scope

This SOP applies to all Meridian Health Technologies, Inc. business units, subsidiaries, and global offices (Boston, London, Berlin, Singapore, Toronto). It governs the assignment, delivery, completion, and remediation of all compliance-related training modules.

**In-Scope Personnel:**
- All full-time and part-time employees of Meridian Health Technologies, Inc.
- All independent contractors, consultants, and temporary staff who have been granted access to any Meridian information system, network, or facility.
- All third-party vendor personnel whose roles require access to Meridian client data, PHI, or Meridian SaaS Platform infrastructure, as contractually obligated.
- Members of the Board of Directors who interact with sensitive corporate information.

**In-Scope Systems:**
- Meridian’s Learning Management System (LMS): Workday Learning.
- The Meridian SaaS Platform (AWS us-east-1, eu-west-1).
- All endpoints used to access compliance training content.

**Out of Scope:**
- Clinical skills competency assessments managed by Clinical Operations (see SOP-CLIN-021).
- Technical product training specific to software development lifecycles, unless directly linked to a regulatory mandate.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **AI Literacy** | As defined by EU AI Act Article 4(b), the skills, knowledge, and understanding that allow providers, deployers, and affected persons to make informed decisions regarding AI systems. |
| **Annual Compliance Window** | The mandatory 45-day period from September 1 to October 15 during which all personnel must complete assigned annual refresher training. |
| **Assignment Profile** | A dynamically generated set of required training modules mapped to a specific role’s risk, data access, and regulatory exposure. |
| **CC** | SOC 2 Common Criteria (Security, Availability, Processing Integrity, Confidentiality, Privacy). |
| **CHRO** | Chief Human Resources Officer. |
| **CISO** | Chief Information Security Officer. |
| **CPO/DPO** | Chief Privacy Officer / Data Protection Officer. |
| **High-Risk AI System** | An AI system classified under Annex III of the EU AI Act, including Meridian’s Clinical AI Platform. |
| **LMS** | Learning Management System (Workday Learning). |
| **New Hire Onboarding** | The initial 10-business-day period following an employee’s start date. |
| **PHI** | Protected Health Information, as defined by HIPAA. |
| **Remediation Period** | A 7-calendar-day window following a missed deadline during which an individual must complete overdue training before disciplinary action is initiated. |

---

## 3. Roles and Responsibilities

| Role | Responsibility (RACI) | Position Holder |
| :--- | :--- | :--- |
| **Program Owner** | **Accountable** for the overall program, policy approval, and resource allocation. Final escalation point for non-compliance. | Jennifer Walsh, CHRO |
| **Program Manager** | **Responsible** for the day-to-day management of the LMS, training catalog maintenance, assignment rule updates, and reporting. | Director of Learning & Development, HR |
| **Content Owners** | **Responsible** for the accuracy, regulatory alignment, and annual review of all training content within their domain. | CISO, CPO/DPO, Chief AI Officer, Chief Compliance Officer |
| **People Managers** | **Responsible** for ensuring their direct reports complete training on time and for initiating disciplinary procedures for non-compliance. | All people managers at every level |
| **Internal Audit** | **Consulted** on course content to ensure alignment with audit control objectives. Verifies training completion rates as part of SOC 2 and ISO 27001 audits. | Thomas Anderson, Chief Compliance Officer |
| **All Personnel** | **Responsible** for completing all assigned training by the specified due dates. | 100% of in-scope individuals |
| **VP of IT Operations** | **Responsible & Accountable** for the technical availability, integration, and single sign-on (SSO) functionality of the LMS platform. | Samantha Torres |
| **Vendor Management Office** | **Responsible** for including mandatory training clauses in all third-party contracts and validating completion evidence from vendors. | Director of Procurement |

---

## 4. Policy Statements

Meridian Health Technologies, Inc. commits to the following principles:

1.  **Universal Mandate:** No individual with access to Meridian information systems is exempt from compliance training. This includes the CEO and Board of Directors.
2.  **Role-Based Precision:** Training is not one-size-fits-all. Assignment Profiles are calibrated to the specific regulatory, data privacy, and security risks inherent in each role.
3.  **Zero Tolerance for Non-Completion:** Failure to complete mandatory training constitutes a violation of the Code of Conduct (SOP-LEG-001), resulting in progressive disciplinary action up to and including termination of employment or contract.
4.  **Continuous Improvement:** The training catalog undergoes a formal annual review cycle synchronized with changes in the regulatory landscape, audit findings, and identified security incidents.
5.  **Auditability:** All training records are immutable within the LMS, retained for a minimum of seven years, and available for immediate retrieval by Internal Audit and external assessors.
6.  **AI Literacy by Default:** In accordance with the EU AI Act, all staff involved in the development, deployment, or oversight of the Clinical AI Platform and MedInsight Analytics shall possess a verified level of AI literacy.

---

## 5. Detailed Procedures

### 5.1 Training Catalog Management

The Meridian Compliance Training Catalog is a controlled library of courses managed within Workday Learning. The catalog is structured by domain and tier.

#### 5.1.1 Catalog Domains

| Domain ID | Domain Name | Primary Content Owner |
| :--- | :--- | :--- |
| SEC | Information Security & Cybersecurity Awareness | Rachel Kim, CISO |
| PRIV | Data Privacy & Protection | Dr. Klaus Weber, CPO/DPO |
| AI | AI Ethics, Governance & EU AI Act | Dr. Marcus Rivera, Chief AI Officer |
| FIN | Financial Services Compliance & Model Risk | Robert Liu, VP of Financial Services |
| LEGAL | Code of Conduct, Anti-Bribery & Corruption | Maria Gonzalez, General Counsel |
| OPS | Operational Resilience & Incident Reporting | Samantha Torres, VP of IT Operations |

#### 5.1.2 Training Tiers

Training is stratified into three tiers to balance operational burden with risk depth.

- **Tier 1: Foundational (All Personnel)**
    - Core modules required for every individual with an active Meridian account.
    - Modules: `SEC-101: Cybersecurity Essentials`, `PRIV-101: Privacy at Meridian`, `LEGAL-101: Our Code of Conduct`.

- **Tier 2: Functional (Role-Based)**
    - Modules automatically assigned based on job family, data access levels (e.g., Snowflake roles, Epic access), and geographic location.
    - Examples: `SEC-201: Secure Coding` for engineers, `PRIV-202: GDPR for Data Processors` for staff in Berlin, `FIN-201: SR 11-7 Model Risk Management` for HealthPay analytics staff.

- **Tier 3: Specialized (High-Risk)**
    - Modules for personnel directly engaged in high-risk AI development, senior leadership, or roles with elevated administrative privileges.
    - Modules: `AI-301: EU AI Act Compliance for High-Risk Systems`, `AI-302: Bias Detection and Human Oversight Standards`.

### 5.2 Role-Based Assignment Profile Configuration

The Program Manager, in collaboration with HRIS and Content Owners, maintains an automated rules engine in Workday. This engine generates each user's Assignment Profile based on a matrix of attributes. Manual assignment is prohibited except via the exception process defined in Section 8.

#### 5.2.1 Assignment Matrix Logic

| Attribute | Condition | Assigned Modules (Example) |
| :--- | :--- | :--- |
| **All Active Users** | Account Status = Active | `SEC-101`, `PRIV-101`, `LEGAL-101` |
| **Location = Germany** | EU Data Subject Access | `PRIV-202`, `AI-201` |
| **Department = Engineering** | HRIS Dept Code = ENG | `SEC-201`, `AI-201` |
| **Data Access = PHI** | HRIS Access Group = PHI_YES | `PRIV-301: PHI Handling` |
| **Sub-Unit = Clinical AI** | Business Unit = ClinAI | `AI-301`, `AI-302`, `SEC-201` |
| **VP+ Level** | Grade >= 30 | `LEGAL-301: Insider Trading & Ethics for Leaders` |

#### 5.2.2 New Hire Assignment Trigger

Upon completion of Workday's "Hire Business Process," the LMS automatically generates the new hire's Assignment Profile. The trigger date is Day 0 (start date). New hires receive a "Welcome to Compliance" notification within one hour of account provisioning.

### 5.3 Annual Compliance Window Procedure

The formal annual retraining cycle is rigidly scheduled to ensure predictability for operations and audit planning.

1.  **August 15:** Program Manager ensures all updated Tier 1 and Tier 2 course content is published in the production LMS sandbox. Content Owners have completed their sign-off using Form HR-008-A (Annual Content Attestation).
2.  **August 25:** Program Manager pushes a final preview of all Assignment Profiles to People Managers via a Workday dashboard. Managers have 5 business days to request changes to their team members' profiles via an HR ServiceNow ticket. Requests for changes must include a documented justification.
3.  **September 1 (00:01 UTC):** LMS automatically publishes assignments to all in-scope personnel. A notification is sent via email and Slack (channel #compliance-alerts).
4.  **September 1 – October 15:** Personnel complete their assigned modules. The LMS displays a progress tracker on the employee's Workday home page.
5.  **October 16 (08:00 UTC):** The first non-completion report is generated and circulated and the Remediation Period begins (see 5.5).

### 5.4 Training Content Requirements for EU AI Act

This section operationalizes Articles 9, 14, and 29 of the EU AI Act for Meridian’s Clinical AI Platform and MedInsight Analytics.

#### 5.4.1 AI Literacy Training (Article 4)

All personnel in Clinical AI, MedInsight, and Quality Assurance teams must complete `AI-301` and `AI-302`. The curriculum, maintained by the Chief AI Officer, includes:
- Understanding of AI system limitations and potential biases.
- Interpretation of model output (probability scores, confidence intervals).
- Operationalization of Human Oversight measures as logged in the AI Traceability System (LangSmith).
- Scenario-based training on when to override an AI-generated clinical recommendation.

#### 5.4.2 Technical Documentation Competency (Article 9)

Personnel developing or maintaining the Clinical AI Platform must complete `AI-303: Technical Documentation for High-Risk AI`. This module covers the process of maintaining the required technical documentation package in Meridian’s controlled document repository (Confluence, space "AI-RMF"), including:
- The intended purpose and design specifications.
- The datasets used for training, validation, and testing.
- The log of risk management activities as per NIST AI RMF.

#### 5.4.3 Human Oversight Verification

Completion of `AI-302` is not solely based on quiz score. It requires the learner to complete a simulated adverse event scenario in a sandboxed instance of the Clinical AI Platform. The system logs the user's decision pathway (override/no override) which is reviewed by the VP of Clinical AI Products, Dr. Aisha Okafor, quarterly. This log serves as auditable evidence of human oversight capability.

### 5.5 Completion Tracking, Notifications, and Escalation

The LMS automatically records all compliance training data. The following SLA-backed notification cadence is strictly enforced:

| Stage | Timeline | Action | Owner |
| :--- | :--- | :--- | :--- |
| **Activation** | Day 0 | Assignment Profile published; "New Hire Onboarding" or "Annual Window" notice sent. | LMS (Automated) |
| **Reminder 1** | Due Date - 14 days | "Your compliance training is due in 14 days" email sent to users with incomplete status. | LMS (Automated) |
| **Reminder 2** | Due Date - 3 days | Final reminder notification sent to users and CC'd to their direct manager. | LMS (Automated) |
| **Overdue** | Due Date + 1 day | Status changes to "Overdue" in Workday. Manager receives an automated direct communication. | LMS / Program Manager |
| **Remediation** | Due Date + 4 days | People Manager holds a documented 1:1 conversation with the individual. | People Manager |
| **Show Cause** | Remediation End Date (Due Date + 7 days) | If still non-compliant, an automated "Show Cause" notification is sent to the individual and their skip-level manager. A disciplinary case is created in Workday HR by the People Manager, coordinated with HR Business Partner. | People Manager / HRBP |
| **Final Escalation** | Due Date + 11 days | Individual's system access (Okta, Google Workspace, VPN) is automatically suspended by an integrated script connecting the LMS to Okta. | IAM Workflow (Automated) |

### 5.6 Remedial Training

A "Re-Training" path is distinct from new assignment. It is triggered under specific conditions:

- **Phishing Simulation Failure:** A user who clicks a simulated phishing link is automatically enrolled in `SEC-102: Phishing Remediation` with a 24-hour deadline. Access to financial systems is temporarily read-only until completion.
- **Incident Root Cause:** Post-incident reviews by the CISO (see SOP-SEC-011) may mandate remedial or targeted training for individuals or teams. The CISO defines the curriculum, which the Program Manager assigns in the LMS within 24 hours of the mandate.
- **Audit Finding:** Any audit finding related to individual competency triggers an immediate remedial assignment. Internal Audit verifies completion.

---

## 6. Controls and Safeguards

The following controls are implemented to ensure the integrity, confidentiality, and availability of the training program and its supporting data, in alignment with SOC 2 CC7.1 (Control Activities) and SOC 2 A1.2.

### 6.1 Technical Controls

| Control ID | Control Description | SOC 2 Alignment |
| :--- | :--- | :--- |
| **TAC-001** | **Single Sign-On (SSO) Enforcement:** LMS access requires Okta MFA challenge. No local LMS accounts exist. | CC6.1 |
| **TAC-002** | **Automated Access Suspension:** Non-compliance at Final Escalation triggers a SCIM-based deactivation of the user’s Okta account. Reactivation requires documented proof of training completion and VP-level approval. | CC6.6 |
| **TAC-003** | **Immutable Audit Log:** All training completions, quiz scores, and acknowledgments are written to a write-once, read-many (WORM) compliant log in Sumo Logic. Tampering alerts are routed to the CISO. | CC7.2 |
| **TAC-004** | **AI Sandbox Isolation:** The AI literacy practical test environment is logically isolated from production clinical systems to prevent impact to patient data during training. | CC7.1 |

### 6.2 Data Privacy Controls for Training Records

| Control ID | Control Description |
| :--- | :--- |
| **DPC-001** | **Retention Enforcement:** Training records are maintained for 7 years from the date of completion. At Year + 7 years + 30 days, records are automatically purged from the LMS hot storage via an automated batch job. Cold backups from the data warehouse are not purged to maintain SOC data integrity. |
| **DPC-002** | **Anonymization for Analysis:** When aggregate training data is shared for diversity or workforce analysis, PII (name, email) is removed. Only Job Family, Department, and Completion Status are retained. |

### 6.3 Content Integrity Control

No training module is published to the production LMS without:
1.  **Technical Review:** The Content Owner signs Form HR-008-A, attesting to regulatory alignment.
2.  **Learning Review:** The Director of Learning & Development signs Form HR-008-B, attesting to instructional design validity and accessibility standards (WCAG 2.1 AA).
3.  **Sandbox Validation:** The module is tested by a group of 5-8 power users selected by the relevant Business Unit head to validate technical accuracy and operational relevance.

---

## 7. Monitoring, Metrics, and Reporting

The effectiveness of the Mandatory Compliance Training program is continuously monitored through a dedicated dashboard ("Compliance Command Center") built in Tableau, drawing real-time data from Workday Learning.

### 7.1 Key Performance Indicators (KPIs)

| KPI ID | Metric | Target | Reporting Frequency |
| :--- | :--- | :--- | :--- |
| **KPI-01** | Overall Enterprise Completion Rate (On-Time) | 98% | Real-time, reviewed weekly by CHRO |
| **KPI-02** | Remediation Period Resolution Rate | 100% of overdue individuals completed during Remediation | End of Remediation Period |
| **KPI-03** | Phishing Remediation Timeliness | 100% within 24 hours | Weekly by CISO |
| **KPI-04** | AI-302 Practical Scenario Completion Rate | 100% of Clinical AI & QA staff | Quarterly by Dr. Aisha Okafor |
| **KPI-05** | Average Manager Response Time to Overdue Notification | <1 business day | Quarterly |

### 7.2 Reporting Cadence

| Report Name | Recipients | Content | Frequency |
| :--- | :--- | :--- | :--- |
| **Compliance Pulse** | All People Leaders (Self-Service Dashboard) | Team-level completion status, overdue individuals, trended completion rates. | Real-Time |
| **BU Compliance Scorecard** | Business Unit Heads (Direct reports to CEO) | Aggregated, de-duplicated completion rate, benchmarking against other BUs. | Monthly |
| **Executive Risk Brief** | CEO, CHRO, CISO, CPO, General Counsel | High-risk overdue report (VP+ and privileged users), regulatory alignment status, remediation outcomes, systemic training gaps identified. | Quarterly |
| **S2 Audit Readiness Report** | Internal & External Auditors | Frozen point-in-time snapshot of 100% completion, accompanied by the System Description and control matrix evidence package. | Bi-Annually (Pre-Audit) |

---

## 8. Exception Handling and Escalation

### 8.1 General Procedure for Exceptions

An exception to the training policy (e.g., a request for an alternative deadline, exemption from a role-based module) must be formally documented and approved **prior** to the training deadline. Retroactive exceptions are not permitted except for verified catastrophic technical failures (e.g., documented Okta-wide outage lasting >4 hours on the due date).

**Exception Workflow:**
1.  **Initiation:** The individual’s People Manager submits a "Compliance Training Exception" ticket in ServiceNow. The ticket must articulate the legitimate business justification (e.g., "Employee on paid medical leave from Date X to Date Y with documented Return-to-Work date Z").
2.  **Impact Assessment:** The Program Manager assesses the risk of the exception against audit timelines.
3.  **Approval Matrix:**
    - **Deadline Extension (<15 calendar days):** Approved by the Program Manager.
    - **Deadline Extension (>15 calendar days):** Requires approval from the Chief Compliance Officer (Thomas Anderson) and the relevant Content Owner (e.g., CISO for SEC modules).
    - **Module Exemption:** Requires approval from the Content Owner and the CHRO. A compensating control must be documented (e.g., a restricted-read-only Okta scope for the exemption period).

### 8.2 Escalation of Non-Compliance

If an individual fails to complete training after the Final Escalation (system suspension), the following occurs:
1.  **Technical Suspension:** Okta account disabled. SSO to all corporate apps (AWS Console, Workday, Snowflake, Slack) is revoked immediately.
2.  **Payroll Impact:** After a 24-hour grace period for reactivation, if the suspension remains, the individual is placed on unpaid leave until compliance is achieved, in accordance with local employment law. HR Business Partners coordinate with Payroll.
3.  **Termination:** If suspension lasts 10 business days without a fully approved exception, it constitutes a voluntary resignation (or "abandonment of contract" for contractors).

---

## 9. Training Requirements for SOP-HR-008 Owners

The individuals responsible for executing this policy must undergo a deeper level of training:

1.  **Program Manager Certification:** The Director of L&D must complete Workday Learning Administrator Pro certification annually.
2.  **Content Creator Workshop:** All Content Owners must attend a 4-hour workshop annually, facilitated by the Legal team, on "Writing Audit-Ready Training Content." This covers updates on evolving regulatory guidance (e.g., EDPB guidelines, AICPA TSC updates).
3.  **Auditor Feedback Loop:** Within 30 days of any SOC 2 or ISO audit report issuance, the CHRO and CISO hold a mandatory review session to dissect training-related exceptions or findings.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs
- **SOP-LEG-001:** Code of Conduct and Business Ethics
- **SOP-SEC-011:** Security Incident and Breach Response Plan
- **SOP-PRIV-005:** Data Subject Access Request (DSAR) Handling
- **SOP-AI-002:** Risk Management System for Clinical AI Platform (aligned with NIST AI RMF 1.0)
- **SOP-VEND-003:** Third-Party Vendor Risk Management & Onboarding
- **SOP-CISO-001:** Access Control and Identity Management

### 10.2 External Standards and Regulatory References
- **AICPA SOC 2:** Trust Services Criteria (TSC) 2017 Revision, specifically CC1.2 (Risk Assessment), CC5.2 (Control Activities), and CC7.2 (System Operations, Monitoring).
- **EU AI Act:** Regulation (EU) 2024/1689, Articles 4 (AI Literacy), 9 (Risk Management), 14 (Human Oversight), and 29 (Deployer Obligations).
- **ISO/IEC 27001:2022:** Information Security, Cybersecurity and Privacy Protection.

---

## 11. Revision History

| Version | Date | Author | Description of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2020-03-15 | J. Walsh | Initial release of unified compliance training framework. |
| 2.0 | 2023-01-10 | J. Walsh | Major revision: added Tier 2/3 role-based matrix; moved tracking from spreadsheets to Workday LMS. |
| 3.0 | 2025-01-22 | J. Walsh | Added full EU AI Act module catalog (AI-301, 302, 303). Introduced automated Okta suspension escalation. |
| 3.1 | 2025-08-14 | J. Walsh | Refined Annual Compliance Window dates; updated Content Owner list following re-org; added SSO enforcement control. |
| 3.2 | 2025-11-26 | J. Walsh | Finalization of Human Oversight sandbox procedures for AI-302; clarified Vendor Management Office reporting line; updated CPO title to CPO/DPO. |
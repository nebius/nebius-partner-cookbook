---
sop_id: "SOP-LEGC-009"
title: "Compliance Training Program"
business_unit: "Legal & Compliance"
version: "3.6"
effective_date: "2024-04-26"
last_reviewed: "2025-03-07"
next_review: "2025-09-08"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "HIPAA"
  - "GDPR"
  - "EU AI Act"
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: Compliance Training Program

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework for the design, development, delivery, documentation, and continuous improvement of the Meridian Health Technologies, Inc. ("Meridian" or the "Company") Compliance Training Program. The program ensures that all employees, contractors, temporary workers, and applicable third parties possess the requisite knowledge, skills, and awareness to fulfill their regulatory obligations and uphold Meridian's ethical standards across all business lines.

The purpose of this program is to mitigate regulatory risk, prevent violations of law, protect patient data, ensure the integrity of AI systems, and foster a culture of compliance that aligns with the Company's strategic objectives and the directives of the Board-level AI Governance Committee.

### 1.2 Scope

This SOP applies to:

1.  **All Personnel:** All full-time and part-time employees of Meridian Health Technologies, Inc., including its global offices in Boston, London, Berlin, Singapore, and Toronto.
2.  **Contingent Workers:** All independent contractors, consultants, temporary staff, and interns who access Meridian systems, handle Meridian data, or operate on behalf of Meridian.
3.  **Executive Leadership:** The C-Suite, including the Chief AI Officer, Chief Medical Officer, and Chief Information Security Officer, who are subject to enhanced, role-specific training.
4.  **Board of Directors:** Members of the Board, specifically those serving on the AI Governance Committee, are covered by tailored executive briefings.
5.  **Third Parties:** Vendors, partners, and business associates whose roles involve handling Protected Health Information (PHI), personal data of EU data subjects, or interacting with Meridian's high-risk AI systems, as defined by contractual agreements and risk assessments.

The scope covers training requirements derived from the Health Insurance Portability and Accountability Act (HIPAA), General Data Protection Regulation (GDPR), the EU AI Act, SOC 2 Type II Trust Services Criteria, NIST AI RMF, SR 11-7, and other applicable internal policies.

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
| :--- | :--- |
| **AI Governance Committee** | Board-level committee responsible for overseeing AI risk management, including training adequacy for high-risk AI systems. |
| **AI RMF** | AI Risk Management Framework, as published by the National Institute of Standards and Technology (NIST). |
| **BUSINESS ASSOCIATE (BA)** | A person or entity that performs functions or activities on behalf of a covered entity that involve the use or disclosure of PHI. |
| **CCO** | Chief Compliance Officer (Thomas Anderson). |
| **COVERED ENTITY** | A health plan, health care clearinghouse, or healthcare provider that transmits health information electronically. Meridian is a BA. |
| **DPO** | Data Protection Officer. Dr. Klaus Weber, based in Berlin, serves as Meridian's DPO as required under GDPR. |
| **EDM** | Enterprise Data Management. Meridian's central data governance function. |
| **EU AI ACT** | Regulation (EU) 2024/1689 laying down harmonized rules on artificial intelligence. |
| **GDPR** | EU General Data Protection Regulation (Regulation (EU) 2016/679). |
| **HIPAA** | Health Insurance Portability and Accountability Act of 1996, as amended by the HITECH Act. |
| **KPI** | Key Performance Indicator. A measurable value demonstrating the effectiveness of the training program. |
| **LMS** | Learning Management System. Meridian's centralized platform for training delivery and tracking (Powered by Workday Learning). |
| **PHI** | Protected Health Information. Individually identifiable health information held or transmitted by a covered entity or its business associate. |
| **SOP** | Standard Operating Procedure. |
| **SR 11-7** | Federal Reserve Supervision and Regulation Letter 11-7 on Model Risk Management. |
| **TNA** | Training Needs Assessment. A systematic process for identifying gaps between current and required knowledge and skills. |
| **TPRM** | Third-Party Risk Management. The process of analyzing and controlling risks associated with outsourcing to third-party vendors. |

## 3. Roles and Responsibilities

A RACI matrix delineates responsibility for the Compliance Training Program execution.

| Activity/Task | CCO | Chief AI Officer | CISO | DPO | VP, Engineering | VP, HR | Functional Mgrs | All Personnel |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Program Ownership & Governance** | A | C | C | C | I | I | I | I |
| **Annual Training Needs Assessment** | R | C | C | C | C | C | C | I |
| **Curriculum Design & Content Creation** | A | R | C | C | C | I | C | I |
| **LMS Administration & Assignment** | I | I | I | I | I | R | A | I |
| **HIPAA Training Delivery** | A | I | R | C | I | I | R | R |
| **GDPR Training Delivery** | I | I | I | R | I | C | I | R |
| **EU AI Act Training Delivery** | C | R | I | C | C | I | I | R |
| **SR 11-7 / Model Risk Training** | C | R | I | I | I | I | I | R |
| **SOC 2 Controls Training** | C | I | R | I | R | I | I | R |
| **Training Completion & Enforcement** | I | I | I | I | I | R | R | I |
| **Effectiveness Measurement & Reporting** | R | C | C | C | I | C | I | I |
| **Third-Party Training Oversight** | R | I | I | I | I | I | C | I |

**Key:**
- **R:** Responsible (Doer)
- **A:** Accountable (Approver/Signer-off)
- **C:** Consulted (Input provider)
- **I:** Informed (Kept up-to-date)

**Specific Role Descriptions:**

- **Chief Compliance Officer (CCO):** Provides executive oversight, approves the annual training plan, and reports on program effectiveness to the Board. The final escalation point for non-compliance.
- **Chief AI Officer (CAIO):** Owns the technical content for all AI-related training, specifically for the Clinical AI Platform and MedInsight Analytics. Ensures alignment with the NIST AI RMF and EU AI Act technical requirements.
- **Chief Information Security Officer (CISO):** Owns the content for security awareness, HIPAA Security Rule, and SOC 2 security-related training.
- **Data Protection Officer (DPO):** Owns GDPR-specific training content and advises on data protection impact assessments related to training data.
- **Vice President of Engineering:** Ensures training for Engineering teams on secure coding, model risk management (SR 11-7), and SOC 2 change management processes.
- **Chief Human Resources Officer (VP, HR):** Administers the Learning Management System (Workday Learning), manages training assignments, runs compliance reports, and initiates disciplinary actions for non-completion.

## 4. Policy Statements

- **Mandatory Training:** All training assigned based on role, location, and system access risk profiles is mandatory. Completion within specified deadlines is a condition of continued employment and system access.
- **Risk-Based Approach:** Training curricula are designed based on a formal, annual Training Needs Assessment (TNA) that maps regulatory requirements and enterprise risks to specific roles. Personnel in high-risk roles, such as AI model developers, clinicians using the CDS tools, and data engineers, will receive enhanced, specialized training.
- **Recordkeeping:** Meridian will maintain accurate, complete, and auditable records of all training activities, including attendance, completion scores, and attestations, in the LMS for a minimum of seven (7) years from the date of training, consistent with legal hold requirements.
- **Effectiveness & Continuous Improvement:** The training program is not a static "check-the-box" activity. It is subject to ongoing measurement, evaluation, and iterative improvement based on KPIs, audit findings, and changes in the regulatory landscape.
- **Zero Tolerance for Willful Non-Compliance:** Intentional disregard for training requirements or knowingly violating policies covered in training will result in disciplinary action up to and including termination and, where applicable, referral to law enforcement.
- **AI Transparency & Human Oversight:** Training for all personnel interacting with the Clinical AI Platform will emphasize the system's role as a decision-support tool, the primacy of the human clinician's judgment, and the specific transparency obligations detailed in our product labeling and user documentation, in accordance with our interpretation of Article 13 of the EU AI Act.

## 5. Detailed Procedures

### 5.1 Annual Training Needs Assessment (TNA)

The TNA is the foundational process ensuring the Compliance Training Program remains targeted and relevant. The CCO initiates the TNA cycle annually by the last business day of October, to inform the following year's training plan.

1.  **Data Collection Kick-off:** The CCO sends a formal TNA Request Package via email to the CAIO, CISO, DPO, VP of Engineering, VP of HR, and General Counsel. The package includes:
    - A link to the secure TNA Survey Form (hosted on an internal SharePoint site).
    - The current library of compliance training courses.
    - A summary of regulatory updates from the preceding 12 months.
    - Results from the prior year's training effectiveness evaluations.
    - A list of new products, features, or jurisdictions that have been or will be launched.
    - An anonymized summary of compliance incidents and breaches from the past year.

2.  **Role-Based Gap Analysis:** Each Subject Matter Expert (SME) completes their respective section of the TNA Survey Form within 15 business days. The form requires them to:
    - **CAIO:** Map all roles interacting with the Clinical AI Platform and MedInsight to the AI literacy, transparency, and human oversight requirements of the EU AI Act and the NIST AI RMF. Identify gaps between current AI/ML staff capabilities and the technical documentation standards required for high-risk systems.
    - **CISO:** Map all IT and engineering roles to the specific security and privacy controls in HIPAA (45 CFR § 164.308, § 164.312), SOC 2 (CC6.x), and ISO 27001. Identify gaps related to new threat vectors (e.g., adversarial AI attacks).
    - **DPO:** Identify changes in processing activities for EU data subjects that trigger new GDPR training needs, such as the introduction of new lawful bases or cross-border data transfer mechanisms. Highlight any new data subject rights (Article 15-22) handling nuances.
    - **VP of Engineering:** Identify skill gaps in model risk management (SR 11-7), secure coding (OWASP Top 10), and SOC 2 change management processes.
    - **General Counsel:** Provide a legal update summarizing new, pending, or changed regulations.
    - **VP of HR:** Provide a personnel impact analysis for organizational restructuring and new hire onboarding volumes for the upcoming year.

3.  **TNA Consolidation and Report:** The CCO compiles all responses into a single **Annual Training Needs Assessment Report**. This report contains:
    - **Gap Summary:** A consolidated list of all identified knowledge and skill gaps.
    - **Risk Prioritization Matrix:** Each gap is rated based on inherent regulatory risk (High, Medium, Low) and the number of personnel affected.
    - **Proposed Curriculum Changes:** Specific recommendations for new courses, modifications to existing courses, retirements of obsolete training, and changes to role-based assignment matrices.
    - **Resource Estimate:** A high-level estimate of budget and SME time required.

4.  **Approval:** The CCO presents the Annual TNA Report to the AI Governance Committee for review and formal approval by December 15th. The approved report becomes the mandate for the Training Plan for the upcoming fiscal year.

### 5.2 Curriculum Design and Content Development

All training content is developed using a standardized instructional design model (ADDIE: Analyze, Design, Develop, Implement, Evaluate) unless sourced from an approved external vendor.

#### 5.2.1 Core Curriculum Components

| Training Module | Target Audience | Content Owner | Frequency | Delivery Method |
| :--- | :--- | :--- | :--- | :--- |
| **Code of Conduct & Ethics** | All Personnel | CCO | Annually | SCORM module + Attestation |
| **HIPAA & Privacy Basics** | All Personnel | CISO / DPO | Annually | SCORM module + Scenario-Based Quiz |
| **GDPR Essentials** | Personnel in EU offices or handling EU personal data | DPO | Annually | SCORM module + Jurisdictional Case Studies |
| **SOC 2 Security Awareness** | All Personnel | CISO | Quarterly | Micro-learning videos + Phishing Simulation |
| **AI Literacy & EU AI Act Fundamentals** | All Personnel | CAIO | Annually | Interactive Video Module |
| **Recognizing and Reporting PHI Breaches** | All Personnel | CISO | Annually | Scenario-Based Module |

#### 5.2.2 Role-Based Specialized Curricula

| Specialized Module | Target Audience | Content Owner | Frequency |
| :--- | :--- | :--- | :--- |
| **Clinical AI: High-Risk System Governance** | Clinical AI PMs, AI/ML Engineers, QA, Clinician End-Users | CAIO / CMO | Bi-Annually |
| **SR 11-7: Model Development, Validation & Monitoring** | HealthPay Data Scientists, Model Validation Team | CAIO / VP, Fin. Services | Annually |
| **Secure Coding & OWASP Top 10** | All Engineering Personnel | CISO / VP, Engineering | Annually |
| **GDPR Advanced: DPIAs & Data Subject Rights** | DPO Office, Key Product Managers, EU-focused Engineers | DPO | Annually |
| **Change Management: SOC 2 Protocols** | Engineering, IT Operations, DevOps | VP, Engineering | Onboarding & Annually |
| **HIPAA Security Rule for IT Admins** | IT Operations, Cloud Security Engineers | CISO | Annually |

#### 5.2.3 HIPAA Training Content Requirements (Thorough)

All HIPAA training must be meticulously designed to cover the specific requirements of the Privacy, Security, and Breach Notification Rules. Training is not generic "privacy training" but is legally anchored.

1.  **Privacy Rule (45 CFR § 164.530(b)):
    - **Permitted Uses and Disclosures:** Detailed training on what constitutes a permissible use and disclosure of PHI for Treatment, Payment, and Health Care Operations (TPO) versus those requiring a valid, HIPAA-compliant authorization. Real-world scenarios using MedInsight Analytics and HealthPay data flows are mandatory.
    - **Minimum Necessary Standard (45 CFR § 164.502(b)):** Training must operationalize the concept of "minimum necessary." For example, customer support agents handling HealthPay inquiries must be trained on screen-masking protocols and role-based access controls that limit their view to only the PHI fields essential for the specific task (e.g., billing amount, date of service) and not the full medical record from the Clinical AI Platform.
    - **Individual Rights (45 CFR § 164.524-164.526):** Specific procedures for handling a patient request to access, amend, or receive an accounting of disclosures of their PHI. This includes timelines: systems and staff must be prepared to act on a request within 30 days, with a single, documented 30-day extension permissible. Training includes the "denial management" process, specifying which office (CCO and General Counsel) must review and approve any denial.
    - **Notice of Privacy Practices (NPP):** Personnel must be trained on the content of Meridian's NPP as it applies to our services as a Business Associate, and where to direct patient questions.
    - **Business Associate Agreements (BAAs):** All personnel managing vendor relationships are trained on the mandatory requirement of an executed BAA before any PHI is disclosed to a vendor. The TPRM team uses a standard BAA template v4.2, maintained by the General Counsel.

2.  **Security Rule (45 CFR § 164.308 & § 164.312):
    - **Administrative Safeguards:** This training is role-specific. The CISO's team trains IT administrators on the configured Security Incident Response Plan (SOP-ISMS-105), contingency planning (SOP-ITDR-032), and the rigorous process for authorizing and documenting access to ePHI.
    - **Physical Safeguards:** All personnel with access to Meridian physical offices are trained on the use of access badges, the prohibition of tailgating, and the secure storage of workstations and physical media containing PHI.
    - **Technical Safeguards:** The Engineering and IT Operations teams receive deep-dive training on:
        - **Access Control (§ 164.312(a)(1)):** Mandatory use of Okta for Multi-Factor Authentication (MFA), assignment of unique user IDs, and prohibition of shared credentials. Automatic log-off settings (15-minute inactivity timeout for clinical applications).
        - **Audit Controls (§ 164.312(b)):** How Meridian uses AWS CloudTrail, SIEM (Splunk), and database-level auditing to record and examine activity in systems containing ePHI. Personnel are trained that all actions are attributable to their unique ID.
        - **Integrity Controls (§ 164.312(c)(1)):** Training on cryptographic hashing used for PHI at rest in Snowflake and PostgreSQL.
        - **Transmission Security (§ 164.312(e)(1)):** Mandatory use of TLS 1.2 or higher for all data in transit and the use of Meridian VPN clients (GlobalProtect) for remote administrative access.

3.  **Breach Notification Rule (45 CFR § 164.400-414):
    - **Identification:** All personnel are trained on the definition of a "breach" (an impermissible use or disclosure compromising the security or privacy of PHI) and the three key exceptions.
    - **Reporting Obligation:** A non-negotiable "see something, say something" policy. The internal SLA for reporting a suspected breach by any employee to the Privacy Office (privacy@meridian.tech) is **within 1 hour of discovery**.
    - **Risk Assessment Process:** Key privacy and legal personnel are trained on performing the four-factor risk assessment to determine the probability of compromise, which dictates notification obligations. This process must begin within 24 hours of the incident declaration.

#### 5.2.4 SOC 2 Change Management Training

Training for personnel involved in implementing software, infrastructure, or configuration changes must cover the controls in SOP-DEVOPS-011 (Change Management Policy). The training includes:

- **Initiation and Documentation:** All changes must be documented via a ServiceNow Change Request (CR), detailing the business justification, technical plan, rollback steps, and risk scoring.
- **Approval:** The Change Advisory Board (CAB) or designated manager must review and approve the CR prior to deployment. Training outlines the required information for a valid approval in ServiceNow.
- **Segregation of Duties:** The process requires that the *developer* of a change is distinct from the *approver* and distinct from the *deployer* in the production environment. Training uses role-play scenarios to illustrate this concept and prevent violations.
- **Post-Implementation Review:** A mandatory post-implementation review period of 24 hours is required for standard changes, during which relevant telemetry dashboards in Datadog are monitored.

#### 5.2.5 EU AI Act Transparency Training

This training covers the general principle that users of AI systems must be informed they are interacting with one. For the Clinical AI Platform, it covers the importance of the system's CE marking, the information in the 'Instructions for Use,' and the nature of the human-AI interface. It describes the general categories of information we provide to deployers but does not provide an exhaustive checklist against all Article 13 disclosure elements.

#### 5.2.6 GDPR Partial Coverage: Data Subject Rights Procedures

Training on data subject rights covers the existence of the right of access, rectification, erasure, and data portability. The procedure directs all personnel to forward any such requests immediately to the DPO's office (dpo@meridian.tech). The DPO team is trained to log the request, verify the identity of the data subject, and coordinate with the relevant data owners (e.g., MedInsight, HR) to compile a complete response. The target is to complete this process without undue delay, and a best-effort timeline is communicated internally.

### 5.3 Training Delivery Methods

The delivery method is selected based on the audience size, geographic dispersion, and content complexity.

1.  **Self-Paced SCORM Modules:** The standard for foundational and annual compliance courses. Hosted and tracked on the Workday Learning LMS. Modules must be Section 508/WCAG 2.1 AA compliant for accessibility.
2.  **Instructor-Led Training (ILT):** Used for role-specific, deep-dive technical training (e.g., SR 11-7, Clinical AI Governance). ILT can be delivered via Microsoft Teams for remote global audiences or in-person at the Boston and Berlin offices. All ILT sessions are recorded and hosted on Workday for later audit and remediation.
3.  **Micro-Learning & Nudges:** The CISO's team uses a "security nuggets" program. Short, <3-minute videos are pushed monthly via email and Slack (to #sec-awareness) on topics like phishing, password hygiene, and safe disposal. These are tracked via an integrated polling tool (Polly).
4.  **Simulations:** Monthly simulated phishing emails are sent to all personnel by the CISO's team using the KnowBe4 platform. Clinical AI Product Managers run biannual "adverse event simulation" workshops for the CDS tools to test human oversight protocols.
5.  **Attestations:** For certain critical policies (e.g., Code of Conduct, BAA responsibilities), a formal electronic attestation is required in Workday beyond a quiz pass. The attestation states, "I have read, understood, and agree to comply with [Policy Name] and acknowledge that my non-compliance may result in disciplinary action."

### 5.4 Training Assignment and Tracking

1.  **Assignment Rule Engine:** The VP of HR configures Workday Learning to automatically assign courses based on user profile attributes: Job Family, Department, Location, and a custom "System Access" flag (e.g., `has_phia_access`, `is_aiml_developer`). The CCO reviews and approves this assignment matrix quarterly.
2.  **New Hire Onboarding:** A Compliance Onboarding Curriculum is automatically assigned during the first day in Workday.
    - **Deadlines:** HIPAA, Code of Conduct, and SOC 2 Awareness modules must be completed **within 7 calendar days** of the start date. Role-based training (Secure Coding, AI Literacy) must be completed **within 30 calendar days**.
    - **Access Provisioning Block:** System access to sensitive environments (e.g., AWS prod, PHI-containing databases) is gated behind the completion of core security and privacy modules. The Identity & Access Management (IAM) team, managed by the CISO, enforces this via an automated integration between Workday and Okta.
3.  **Recurring Training Window:** Annual refresher training is assigned en masse on **March 1st** of each year, with a completion deadline of **April 15th**. Quarterly micro-modules are assigned on the first of the quarter with a 30-day deadline.

### 5.5 Effectiveness Measurement

1.  **Level 1: Reaction:** Immediate post-training survey via Workday for all formal modules. Key questions measure content relevancy, clarity, and likelihood of applying the knowledge. A target score of >4.0 out of 5.0 is set.
2.  **Level 2: Learning:** Embedded quiz and scenario-based assessments.
    - The passing score for all compliance modules is **80%** .
    - Personnel who fail are automatically re-assigned the training and must achieve a passing score within **5 business days**.
    - Failure to pass after three attempts triggers a mandatory 1:1 review with the individual's direct manager, reported to the CCO.
3.  **Level 3: Behavior (Observable Impact):** This is the primary metric for effectiveness.
    - **Phishing Resilience:** Reduction in the click rate on simulated phishing emails. The target is <5%.
    - **Incident Reporting Rate:** An *increase* in timely self-reported privacy or security incidents via the proper channels is considered a positive indicator of training effectiveness (e.g., increase in reports to privacy@meridian.tech).
    - **Help Desk Tickets:** A decrease in tickets related to known policy questions covered in training (e.g., "How do I send PHI securely?").
    - **Audit Findings:** A reduction in direct-control failures during internal and external SOC 2, HITRUST, and ISO 27001 audits attributed to a lack of training.
4.  **Level 4: Return on Investment (ROI):** An annual qualitative analysis by the CCO linking training program improvements to the overall risk posture, potentially quantified by reduced potential regulatory fines or lower incident remediation costs.

## 6. Controls and Safeguards

- **Administrative Control: Segregation of Duties:** The creation, approval, and assignment of training content is segregated. A content creator (e.g., CISO's delegate) cannot also be the sole granter of an exception to that same content (see Section 8). The role-based assignment matrix in Workday requires dual approval from the functional content owner (e.g., CISO) and the CCO.
- **Technical Control: Automated Assignment & Escalation:** A script (`training_compliance_sync.py`) runs nightly, ingesting Workday completion data. It automatically sends reminder emails at T-7, T-3, and T-1 days before a deadline. On the deadline day, at 00:00 local time, it auto-generates a non-compliance notification to the employee, their manager, and the VP of HR.
- **Technical Control: ePHI Access Gating:** The Okta integration queries the Workday `training_completion_status` table via API. If an employee's status for mandatory HIPAA training is not `COMPLETED` or is `EXPIRED`, the Okta user profile is updated to remove them from the `phia_access_group`, automatically suspending access to AWS, Snowflake, and MedInsight production environments until remediation is completed. The SLA for access re-provisioning after completion is 2 hours.
- **Administrative Control: Third-Party Training Assurance:** The TPRM team, in coordination with the CCO, defines contractual training requirements for Business Associates and high-risk vendors. Evidence of completion (e.g., attestation, training summaries) must be uploaded to the Archer GRC TPRM module annually. Meridian reserves the right to audit third-party training records with 30 days' notice.
- **Technical Control: Audit Trail Integrity:** All training completions, quiz scores, and attestations in Workday are protected by an immutable audit trail. Any administrative changes to training records generate a log entry. These logs are forwarded to Splunk and are retained for the full 7-year recordkeeping period as stipulated in Section 4.

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| Category | KPI | Target | Reporting Frequency |
| :--- | :--- | :--- | :--- |
| **Compliance** | Overall corporate training completion rate | 100% by deadline + 5 days | Monthly |
| **Compliance** | New hire training completion within 7 days | ≥ 98% | Weekly |
| **Compliance** | Past-due training rate (>30 days overdue) | < 0.5% of all assignments | Monthly |
| **Effectiveness** | Simulated phishing susceptibility rate | < 5% | Monthly |
| **Effectiveness** | Average score on high-risk AI governance quiz | ≥ 85% | Per Assignment |
| **Effectiveness** | Self-reported incidents within 1 hour of discovery | 100% of training-aware personnel | Quarterly |
| **Satisfaction** | Average post-training survey score (1-5) | > 4.0 | Per Module |

### 7.2 Monitoring and Reporting Cadence

- **Real-time Dashboards:** The CCO, VP of HR, and functional content owners have access to a real-time Power BI dashboard (data source: Workday Learning). This dashboard displays completion rates by module, by department, and by office location.
- **Monthly Operational Reports:** The VP of HR generates an automated "Monthly Compliance Training Scorecard" on the first business day of each month. This is distributed to all departmental VPs, highlighting teams with red (<95% completion) status.
- **Quarterly Business Review (QBR):** The CCO presents a more strategic compliance training report to the Executive Leadership Team. This report analyzes KPI trends, Level 3 behavioral observations, and provides a forecast for the next quarter's training activities. It includes a section on disciplinary actions taken for training non-compliance.
- **Annual Audit & Board Report:** An annual, comprehensive Effectiveness Report is prepared by the CCO for the AI Governance Committee and the full Board. This is the Level 4 ROI analysis, correlating training outcomes with audit results, regulatory changes, and the enterprise risk register. It formalizes recommendations for the next TNA cycle.

## 8. Exception Handling and Escalation

### 8.1 Exception Handling

Deviations from the defined training requirements are discouraged but permitted under controlled circumstances.

1.  **Duration Exception:** A manager may request a one-time, 14-calendar-day extension for an employee's training deadline. This is submitted via a ServiceNow ticket, citing a specific business justification (e.g., critical client emergency, approved medical leave). The functional content owner or their delegate approves this request.
2.  **Content Exception:** A request to waive a specific training module must be submitted by the employee's VP to the CCO. It requires documented proof of equivalent, recent training from an accredited source. The CCO has the sole authority to approve this exception on a case-by-case basis, documented and uploaded to Workday against the employee's record. This exception is valid for one annual cycle only; if the external certification expires, the full Meridian training must be completed.
3.  **GDPR and EU AI Act Exceptions:** Any request for an exception to training required for the lawful handling of EU data subjects' personal data or high-risk AI system governance must be co-approved by the DPO or the CAIO, respectively, in addition to the CCO. No exceptions to the core transparency concepts of the AI Act will be granted.

### 8.2 Non-Compliance Escalation

1.  **Day 1 Past Due:** Automated notification to the employee and their direct manager.
2.  **Day 7 Past Due:** The VP of HR is formally notified. A performance note is added to the employee's profile in Workday.
3.  **Day 14 Past Due:** The CCO sends a formal "Notice of Non-Compliance" to the employee, their manager, and their departmental VP. The notice explicitly states that continued non-compliance will result in formal disciplinary action per the Employee Handbook, up to and including termination. Access to certain systems may be suspended at the CCO's discretion after consulting with the CISO.
4.  **Day 30 Past Due:** The case is escalated to the Chief Human Resources Officer for mandatory disciplinary action, the minimum of which is a formal written warning placed in the employee's permanent file.

## 9. Training Requirements

This SOP is itself a document that requires training.

- **Target Audience:** The CCO, VP of HR, and all members of the Legal & Compliance team responsible for operationalizing the training program. All functional content owners (CISO, CAIO, DPO) and managers involved in granting exceptions must be trained on their specific responsibilities.
- **Method:** A recorded, instructor-led walkthrough of this SOP and a practical exercise in the TNA Survey Form.
- **Frequency:** Upon document publication, upon any major revision (e.g., version 3.x to 4.0), and as part of the annual compliance team refresher.
- **Tracking:** Completion is tracked in the "Legal & Compliance" curriculum within Workday Learning.

## 10. Related Policies and References

### 10.1 Internal Meridian Policies
| Policy Name | SOP-ID |
| :--- | :--- |
| Information Security Management System (ISMS) Policy | SOP-ISMS-010 |
| Change Management Policy | SOP-DEVOPS-011 |
| Incident Response Plan | SOP-ISMS-105 |
| IT Disaster Recovery and Business Continuity Plan | SOP-ITDR-032 |
| Data Classification and Handling Policy | SOP-EDM-004 |
| Acceptable Use Policy | SOP-ISMS-007 |
| Supplier Risk Management Policy | SOP-TPRM-022 |
| AI Governance and Risk Management Framework | SOP-AIGOV-001 |
| Employee Disciplinary Policy | SOP-HR-085 |

### 10.2 External Standards and Regulations
- NIST AI RMF 1.0
- SOC 2 Trust Services Criteria (TSP Section 100)
- ISO 27001:2022 (Clause 7.2, 7.3 Competence and Awareness)
- HITRUST CSF v11
- Federal Reserve SR Letter 11-7
- Regulation (EU) 2024/1689 (EU AI Act)
- Regulation (EU) 2016/679 (GDPR)

## 11. Revision History

| Version | Date | Author(s) | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2020-01-15 | Maria Gonzalez, General Counsel | Initial document creation and publication. Focused primarily on HIPAA and SOC 2. |
| 2.1 | 2021-09-30 | Thomas Anderson, CCO | Major revision. Added detailed GDPR requirements, formalized the TNA process, and integrated Workday Learning for tracking. |
| 3.0 | 2022-05-12 | Thomas Anderson, CCO; Rachel Kim, CISO | Added role-based curricula for Engineering, integrated SOC 2 change management training, and enhanced phishing simulation program. |
| 3.4 | 2023-11-07 | Thomas Anderson, CCO; Dr. Marcus Rivera, CAIO | Added comprehensive coverage for AI Governance and SR 11-7 model risk training in response to the Board-level AI Governance Committee mandate. |
| 3.6 | 2024-04-26 | Thomas Anderson, CCO | Current version. Updated to formalize content based on EU AI Act partial requirements, enhance HIPAA breach notification timeliness to a 1-hour SLA, and refine effectiveness measurement KPIs. |
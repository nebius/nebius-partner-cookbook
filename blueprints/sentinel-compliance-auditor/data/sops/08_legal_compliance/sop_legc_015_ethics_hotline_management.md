---
sop_id: "SOP-LEGC-015"
title: "Ethics Hotline Management"
business_unit: "Legal & Compliance"
version: "2.7"
effective_date: "2025-03-26"
last_reviewed: "2026-03-28"
next_review: "2026-09-27"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "SOC 2"
  - "EU AI Act"
status: "Active"
---

# Standard Operating Procedure: Ethics Hotline Management

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework for managing the Meridian Health Technologies, Inc. ("Meridian") Ethics Hotline. The Ethics Hotline provides a confidential, accessible, and secure mechanism for employees, contractors, business partners, patients, and other stakeholders to report suspected violations of law, regulation, Meridian policy, or the Meridian Code of Conduct, with particular emphasis on concerns related to the company's high-risk AI systems governed under the EU AI Act and financial models subject to SR 11-7 standards.

This SOP defines standardized procedures for intake, triage, investigation, resolution, reporting, and continuous improvement of all matters received through the Ethics Hotline. It ensures that reports are handled promptly, objectively, and with appropriate confidentiality, and that individuals who raise concerns in good faith are protected from retaliation.

### 1.2 Scope

This SOP applies to:

| Covered Entity | Applicability |
|----------------|---------------|
| Meridian Health Technologies, Inc. | All global operations, subsidiaries, and affiliates |
| All employees | Full-time, part-time, temporary, and contractors |
| All business units | Including Legal & Compliance, Engineering (AI/ML Systems), Clinical Affairs, Finance, and Commercial Operations |
| All geographies | Including US operations and EU operations governed under the EU AI Act and EU Medical Device Regulation (MDR) |
| Third parties | Vendors, distributors, and partners who have access to Meridian systems or data, as outlined in contractual agreements |
| AI-related concerns | Specific coverage for reports involving high-risk AI system outputs, algorithmic bias, transparency obligations under EU AI Act Articles 13, 14, 52, and 68, human oversight failures, and data governance violations |

**Out of Scope**: Routine Human Resources matters (e.g., standard performance grievances, interpersonal conflicts not involving policy violations) should be directed to the HR Business Partner team via Workday unless they involve protected class discrimination, harassment, or retaliation. Matters involving patient care quality that do not involve compliance violations should be directed through the Quality and Patient Safety reporting process outlined in SOP-QUAL-008 Clinical Event Reporting, though any Quality of Care concerns may also be reported through the Ethics Hotline and will be triaged accordingly.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
|----------------|------------|
| **Anonymous Report** | A report submitted without the reporter providing any identifying information. Meridian commits to investigating all anonymous reports to the fullest extent possible. |
| **Bad Faith Report** | A report made with knowledge of its falsity or with reckless disregard for its truth. This SOP explicitly prohibits bad faith reports and outlines consequences. |
| **Bias Incident (AI Systems)** | Any reported instance where a Meridian high-risk AI system may have produced discriminatory, unfair, or inequitable outputs on the basis of protected characteristics, as defined under applicable law and EU AI Act Article 10. |
| **Case Manager** | The designated individual within the Legal & Compliance team responsible for managing the lifecycle of a specific Ethics Hotline case within the Navex EthicsPoint case management system. |
| **CEO** | Chief Executive Officer |
| **CFO** | Chief Financial Officer |
| **CISO** | Chief Information Security Officer |
| **COO** | Chief Operating Officer |
| **Confidential Report** | A report submitted where the reporter's identity is known to the Case Manager but is protected and disclosed only on a strict need-to-know basis during the investigation. |
| **CPO** | Chief Privacy Officer |
| **EU AI Act** | Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence. |
| **Ethics Hotline** | The multi-channel reporting mechanism (web portal, toll-free telephone line, and direct email) managed by the Legal & Compliance department. The current vendor platform is Navex EthicsPoint. |
| **General Counsel** | The Chief Legal Officer of Meridian, serving as the final internal authority on legal compliance matters and Approver of this SOP. |
| **High-Risk AI System** | An AI system classified as high-risk under Annex III of the EU AI Act, including Meridian's diagnostic imaging triage platform, clinical deterioration prediction engine, and automated treatment planning module. |
| **Intake Specialist** | The Legal & Compliance team member responsible for the initial receipt, acknowledgment, and triage of new Ethics Hotline cases. |
| **Investigation Team** | The ad hoc group assembled by the Case Manager to investigate a specific allegation. May include members from Legal, Compliance, HR, AI Governance, Information Security, or external forensic resources. |
| **Non-Retaliation** | The unwavering commitment by Meridian that no individual who makes a good faith report, or who participates in an investigation, will suffer adverse employment consequences. |
| **RPO** | Recovery Point Objective – the maximum tolerable period in which data might be lost due to a major incident. |
| **RTO** | Recovery Time Objective – the targeted duration of time within which the Ethics Hotline service must be restored after a disruption. |
| **Service Availability** | The commitment that the Ethics Hotline intake channels (phone, web) will be operational and accessible. |
| **Substantiated** | A case disposition indicating that the investigation found sufficient evidence to conclude that a policy or regulatory violation occurred. |
| **Unsubstantiated** | A case disposition indicating that the investigation did not find sufficient evidence to conclude a violation occurred. |

---

## 3. Roles and Responsibilities

The following RACI matrix (Responsible, Accountable, Consulted, Informed) defines the roles and responsibilities for the Ethics Hotline program.

| Activity / Task | Intake Specialist (Legal & Compliance Analyst) | Case Manager (Senior Investigator) | Chief Compliance Officer (Owner) | General Counsel (Approver) | AI Governance Committee (for AI-related reports) | Functional Leadership (e.g., CISO, CPO) | Audit Committee of the Board |
|-----------------|---------------------------------------------|-----------------------------------|----------------------------------|---------------------------|--------------------------------------------------|-----------------------------------------|-------------------------------|
| **Hotline Channel Maintenance** | R | A | C | I | - | C | I |
| **Initial Intake & Acknowledgement** | R | A | C | - | - | - | - |
| **Triage & Case Assignment** | A | R | C | - | C (AI Reports) | C | - |
| **Investigation Execution** | C | R | A | C | C (AI Reports) | C | - |
| **Retaliation Monitoring** | - | R | A | - | - | - | - |
| **Case Closure & Documentation** | C | R | A | - | C (AI Reports) | - | - |
| **Quarterly Aggregate Reporting** | - | R | A | C | I | I | I |
| **Annual Program Effectiveness Review** | - | R | A | C | C | C | I |
| **Exception Approval** | - | - | R | A | - | - | - |
| **High-Risk AI Incident Notification** | - | R | R | R | A | - | I |

---

## 4. Policy Statements

Meridian Health Technologies is committed to the highest standards of ethical conduct and legal compliance. The following policy statements govern the Ethics Hotline program.

1.  **Commitment to Accountability**: Meridian maintains the Ethics Hotline as a cornerstone of its compliance ecosystem, enabling the early detection and remediation of misconduct, particularly in the high-stakes domains of AI-driven clinical decision support and financial governance.

2.  **Accessibility and Availability**: The Ethics Hotline shall be made available 365 days a year, 24 hours a day, via a toll-free global telephone line and a web-based portal managed by Navex EthicsPoint. Meridian commits to maintaining the availability of the hotline service. The Legal & Compliance team, in coordination with IT, will maintain documented continuity procedures for the hotline platform. Availability commitments are in place to ensure uptime; specific quantitative Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO) related to a catastrophic platform failure have not been formalized for this specific vendor system and will be addressed based on enterprise-level disaster recovery prioritization at the time of an incident.

3.  **Confidentiality and Anonymity**: Meridian protects the identity of all reporters to the fullest extent permissible by law. Reports may be made anonymously where legally allowed. No effort will be made to trace an anonymous web submission via IP address or other technical means. Meridian strictly prohibits retaliation against any individual who makes a good faith report, even if the allegation is found to be unsubstantiated.

4.  **Objectivity and Thoroughness**: Every report received shall be logged, acknowledged (if identity is known), triaged based on a standard severity matrix, and investigated by qualified personnel free from conflicts of interest.

5.  **Mandatory Reporting**: All Meridian employees and contractors have an affirmative duty to report suspected violations. This duty is absolute, and no management directive may override it. Managers who receive reports outside the Hotline are obligated to direct the matter to the hotline or notify the Chief Compliance Officer directly.

6.  **Prohibition of Retaliation**: Meridian has a zero-tolerance policy for retaliation. Any individual found to have retaliated against a reporter or investigation participant will be subject to disciplinary action, up to and including termination of employment and civil litigation referral.

7.  **Zero Tolerance for Bad Faith Reports**: Knowingly making a false or bad faith report to the Ethics Hotline is a violation of this policy and will result in disciplinary action.

---

## 5. Detailed Procedures

### 5.1 Hotline Channel Management and Promotion

The Legal & Compliance team maintains the hotline channels and promotes awareness systematically.

1.  **Channel Management**:
    *   **Phone**: The global toll-free number (+1-800-555-ETHX) connects the reporter directly to a live Navex EthicsPoint trained intake operator 24/7. The service supports over 150 languages via telephonic interpretation.
    *   **Web**: The secure, branded web portal (meridian.ethicspoint.com) allows for anonymous or confidential reporting. The portal is hosted on a SOC 2 Type II audited infrastructure separate from the Meridian corporate network, ensuring no tracing of internal IP addresses.
    *   **Email**: The dedicated email address ([email protected]) is available, though reporters are advised that email generally provides a lower degree of anonymity compared to the web portal due to inherent metadata.

2.  **Promotion and Awareness**:
    *   **Onboarding**: Every new hire, including contractors, receives Ethics Hotline awareness training as a module within the "Compliance Essentials" onboarding course in Workday LMS on Day 1.
    *   **Annual Refresh**: All personnel must complete the Annual Code of Conduct refresh training by the end of Q1 each year, which includes prominent hotline promotion.
    *   **Physical Postings**: A compliance poster (template MER-LEGC-POST-01) containing the hotline URL, phone number, and QR code must be displayed on physical bulletin boards in all Meridian office locations and laboratories.

### 5.2 Intake and Triage Process

Upon submission of a report through any channel, the Navex EthicsPoint platform generates a unique case identifier and transmits a secure, encrypted notification to the designated Intake Specialist. The Intake Specialist executes the following procedure within a strict timeline.

**Step 1: Initial Receipt (Time-to-Acknowledge: ≤ 4 hours during M-F 9am-5pm ET or ≤ 12 hours during off-peak)**

| Action | Responsible | System/Tool |
|--------|-------------|-------------|
| Review all new case notifications in EthicsPoint dashboard. | Intake Specialist | Navex EthicsPoint |
| If reporter provides contact details, send the standardized "Acknowledgment of Receipt" communication, confirming the report is under review and reiterating the non-retaliation policy. | Intake Specialist | Navex EthicsPoint (confidential messaging) |

**Step 2: Preliminary Triage and Severity Classification (≤ 24 hours from Receipt)**

The Intake Specialist performs an initial analysis to classify the case severity.

| Severity Level | Criteria | Example Scenarios | Initial Response SLO |
|----------------|----------|-------------------|----------------------|
| **Level 1 (Critical)** | Imminent threat to patient safety from AI system failure; criminal financial fraud; active executive-level harassment; credible threat of violence; significant data breach involving PII/PHI. | Algorithmic bias causing systematic misdiagnosis of a protected patient class; CEO-level misconduct; active ransomware attack. | Case Manager assigned and preliminary response plan initiated within 4 hours. |
| **Level 2 (High)** | Violations of EU AI Act transparency obligations (Art. 13, 52); non-criminal financial irregularities involving >$10,000; systemic SR-11 model governance failures; retaliation complaints; data privacy incidents not reaching Level 1. | Deployment of a high-risk system without required CE marking documentation; manipulation of model performance metrics used in stress tests. | Case Manager assigned within 24 hours. |
| **Level 3 (Standard)** | Suspected minor policy violations; individual conflicts of interest not involving executive management; isolated HR policy breaches not involving harassment/discrimination. | Failure to disclose a minor outside business interest; minor timesheet falsification. | Case Manager assigned within 72 hours. |
| **Level 4 (Inquiry)** | General questions about policy interpretation; requests for guidance where no specific policy breach is alleged. | A request for clarification on the Gifts and Entertainment Policy. | Referred to relevant Subject Matter Expert for guidance within 5 business days. |

### 5.3 Case Assignment and Conflicts Check

The Intake Specialist proposes a Case Manager and submits the triage recommendation via EthicsPoint to the Chief Compliance Officer (CCO) for review.

1.  **Conflicts Check**: The CCO ensures the proposed Case Manager is free of conflicts of interest. No individual may investigate a matter if they are in the direct chain of command of the subject, if the subject is their own manager, or if they have any personal or financial relationship with the subject. For AI-related Level 1 and Level 2 cases, the CCO must formally consult with the Chair of the AI Governance Committee to validate that the proposed Case Manager possesses the requisite domain expertise to understand the technical dimensions of the allegation.

2.  **Assignment Confirmation**: Upon validation, the CCO formally assigns the Case Manager in EthicsPoint, which triggers an automated email notification to the Case Manager.

### 5.4 Investigation Planning

Within 48 hours of assignment (for Level 1 and 2 cases) or 5 business days (for Level 3 cases), the Case Manager drafts an Investigation Plan using the template stored in the Legal & Compliance shared drive (`L:\Compliance\Investigations\Templates\INV-PLAN-TEMPLATE.docx`). The Plan must be approved by the CCO before execution. The Plan shall include:

*   A detailed summary of the allegation.
*   Identification of the specific policies, laws, or regulations potentially violated (e.g., "EU AI Act Article 14(4)(a) — failure to ensure human oversight capability on the diagnostic triage platform").
*   A list of key witnesses and subjects.
*   A detailed list of documents and electronic evidence to be preserved and collected (e.g., model logs, audit trails, user access reports, email review).
*   Identification of the specific Internal Subject Matter Experts (e.g., a Lead Data Scientist, the Chief Medical Officer) required on the Investigation Team.
*   A detailed timeline for key milestones.

### 5.5 Evidence Preservation, Collection, and Analysis

The Case Manager coordinates a Litigation Hold, if necessary, through the `[email protected]` distribution list, copying the CISO. All evidence must be handled in accordance with strict chain-of-custody protocols.

**Key Evidence Sources and Methods:**

*   **Documentary Evidence**: Emails (via M365 Purview eDiscovery), documents (from SharePoint/Workday), and financial records (from Oracle Fusion). All collected files must be stored with a read-only flag in a dedicated, access-restricted case folder within the Legal Vault (`\\legalvault\ethics\CAS-[ID]\`).
*   **Forensic Images**: For Level 1 cases involving potential data destruction, the CISO's team, under direction from the Case Manager, shall create a forensically sound disk image using a validated tool (e.g., FTK Imager) of the subject's assigned endpoint. The image is to be stored in the InfoSec Evidence Locker (`\\infosec-evidence\ethical\...`) with an SHA-256 hash recorded.
*   **AI-Specific Evidence**: For cases involving potential violations of the **EU AI Act**, the Case Manager **must** direct the AI Governance Committee Engineering Liaison to extract and preserve the following, as relevant:
    *   Complete telemetry logs from the system's monitoring dashboards (Datadog) for the relevant time window.
    *   Input data snapshots and corresponding output logs to assess for potential bias, as referenced in EU AI Act Article 10(2)(f).
    *   Records related to human oversight intervention, tracked via the "Human-in-the-Loop Command Center" (HiL-CC) application. The Case Manager must verify whether the system enabled the human overseer to "decide not to use the high-risk AI system or otherwise override, disregard, or reverse the output" as required by EU AI Act Article 14(4)(b) and (c).

*   **Witness Interviews**: All interviews must be conducted by a team of two from the Investigation Team. One member, the designated "Interviewer," asks all questions following a pre-prepared script. The other, the "Scribe," takes detailed, near-verbatim notes. At the start of every interview, an "Upjohn / Corporate Miranda" warning must be administered if the interview involves an employee whose conduct is under scrutiny. The Scribe's notes are to be written up into a formal, signed Interview Memorandum within 24 hours. Meridian does not condone any form of recording of interviews to foster a climate of candor.

### 5.6 Investigation Execution: EU AI Act Specific Procedures

For any case triaged as involving the EU AI Act, the following supplemental procedures are mandatory, in addition to the standard investigation steps in Section 5.5.

1.  **Immediate Notification to AI Governance Committee Chair**: For all Level 1 AI cases, the Case Manager shall notify the AI Governance Committee Chair by telephone within 2 hours of case assignment.
2.  **Engagement of Qualified Technical Assessor**: For Level 1 and 2 AI cases, the Investigation Team **must** include an individual qualified to assess the technical merit of the allegation, specifically: a Senior Data Scientist not involved in the model's development, the Chief AI Ethics Officer, or an external AI auditing firm engaged by the Legal Department. This Assessor will provide a formal Technical Assessment Report (TAR) to be appended to the investigation file.
3.  **Preservation of Quality Management System (QMS) Artifacts**: For cases involving potential safety risks or non-compliance with conformity assessment obligations (EU AI Act Article 43), the Case Manager must request, via the VP of Quality Assurance, a complete, read-only export of the relevant product's technical documentation from the Arena PLM system.
4.  **Serious Incident Assessment**: Within 72 hours of an AI-related Level 1 case being opened, the CCO, General Counsel, and Chief AI Ethics Officer, in consultation with the Chief Medical Officer, must formally determine if the reported matter constitutes a "serious incident" under EU AI Act Article 73. This determination must be documented in a "Serious Incident Determination" memorandum (template ID: MER-LEGC-SID). If the determination is positive, a formal notification to the appointed Market Surveillance Authority (MSA) must be prepared and dispatched by the Regulatory Affairs department within the legally mandated 15-day timeline, as defined in this template.

### 5.7 Investigation, Findings, and Disposition

Upon completion of the evidence gathering, the Case Manager, in consultation with the Investigation Team, develops findings of fact. The standard for a finding is a "preponderance of the evidence" (i.e., it is more likely than not that the violation occurred). Findings are never based on speculation or assumption.

The Case Manager prepares a formal Investigation Report, which includes:
*   **Executive Summary**: A summary suitable for the CCO and General Counsel.
*   **Findings of Fact**: A detailed, evidence-supported narrative of what occurred, with each finding directly linked to specific exhibits.
*   **Conclusion**: A disposition for each alleged policy or regulatory violation:
    *   **Substantiated**: Violation occurred.
    *   **Unsubstantiated**: Insufficient evidence.
    *   **Not a Policy Violation**: The action occurred but did not violate a specific policy.

The CCO reviews and approves the Investigation Report for closure in EthicsPoint.

### 5.8 Corrective Action and Remediation

For any Substantiated finding, the Case Manager drafts a "Corrective Action and Remediation Plan" (CARP) as an addendum to the Investigation Report. The CARP must be approved by the CCO, the General Counsel, and the functional leader of the involved business unit (e.g., CISO for a security violation). The CARP specifies:

| Component | Description | Owner | Deadline |
|-----------|-------------|-------|----------|
| **Root Cause Analysis (RCA)** | A formal RCA must be conducted for any Level 1 or Level 2 case. | Relevant BU Head | 30 days |
| **Direct Remediation** | Specific actions to correct the immediate violation (e.g., removing an algorithm's biased training data set, as required by Art. 10(2)(f)). | Engineering Owner | As defined in CARP |
| **Systemic Preventive Action** | Changes to standard operating procedures, governance frameworks, or technical safeguards to prevent recurrence. | Relevant Policy Owner | 60 days |
| **Disciplinary Action** | Referral to HR (VP of Talent) for disciplinary action against perpetrators of substantiated misconduct. | VP of Talent | 15 business days |

The Case Manager tracks all CARP milestones to completion. A case is not formally closed in EthicsPoint until all CARP milestones are achieved and evidence of completion is attached.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls

| Control ID | Control Description | Control Owner | Frequency |
|------------|--------------------------|---------------|-----------|
| AC-01 | All investigators must sign a non-disclosure and impartiality attestation annually. | CCO | Annual |
| AC-02 | A random quality assurance review of 10% of all Closed cases will be performed by an external compliance counsel firm. | General Counsel | Quarterly |
| AC-03 | Access to the EthicsPoint case management platform is restricted by role-based permissions (Intake Specialist, Case Manager, CCO). | CCO | Continuous |

### 6.2 Technical Controls

| Control ID | Control Description | Implemented By | System |
|------------|--------------------------|----------------|--------|
| TC-01 | Navex EthicsPoint is configured to not capture the IP addresses of web-based reporters. | Navex (configured by CCO) | EthicsPoint |
| TC-02 | All case data at rest within EthicsPoint is encrypted using AES-256. | Navex (SOC 2 attested) | EthicsPoint |
| TC-03 | Evidence collected internally must be stored in the `\\legalvault\` share with restricted access control lists (ACLs), segregated by case ID. | CISO / IT Infrastructure | Legal Vault |
| TC-04 | Any access to a subject's mailbox or user account data for investigation must be approved in writing by the General Counsel, except in exigent circumstances involving immediate threat to life or data integrity (documented post-hoc within 24 hours). Logical access controls are in place to prevent unauthorized access to investigation materials. A formal, periodic user access review of the Legal Vault ACLs is not mandated by this SOP; access management is event-driven (on/offboarding of Legal & Compliance team members). | General Counsel | Exchange Admin |

### 6.3 Physical Controls

All physical evidence (e.g., printed records, secure USB drives with forensic images, signed original witness interview notes) must be stored in a locked, fireproof filing cabinet within the Legal & Compliance suite, Access Control Room L&C-001. This room requires dual-factor biometric authentication for entry, and its access logs are reviewed quarterly by the CISO.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

A dashboard, maintained in Tableau and sourced from a secure API connection to the Navex EthicsPoint platform, tracks the following program metrics in near real-time. The Chief Compliance Officer reviews this dashboard monthly.

| Metric Category | Specific Metric | Target | Owner |
|-----------------|-----------------|--------|-------|
| **Timeliness** | Average Time-to-Acknowledge | ≤ 2 hours | Intake Specialist |
| **Timeliness** | Level 1 Cases: Average Days from Report to Close | ≤ 45 days | CCO |
| **Timeliness** | Level 2 Cases: Average Days from Report to Close | ≤ 90 days | CCO |
| **Timeliness** | Level 3 Cases: Average Days from Report to Close | ≤ 120 days | CCO |
| **Outcome** | Percentage of Cases Substantiated | No target (data-driven) | CCO |
| **Outcome** | Percentage of Reports of Retaliation | ≤ 2% of total reports (monitoring threshold) | CCO |
| **Effectiveness** | Report-to-Close Ratio (Cases closed vs. opened per quarter) | > 0.95 | CCO |

### 7.2 Reporting Cadence

| Report Level | Audience | Frequency | Content |
|--------------|----------|-----------|---------|
| **Operational Report** | Chief Compliance Officer | Monthly | Intake volume, case aging, CARP milestones at-risk. |
| **Program Health Report** | Executive Leadership Team (ELT) | Quarterly | De-identified aggregate data: hotline utilization by country, case type trends, substantiation rate, high-level themes from investigations. A specific breakout showing all AI-related cases and their dispositions must be included. |
| **Board of Directors Report** | Audit Committee | Annually (Q4) | Comprehensive program effectiveness review, external QA review findings summary, benchmarking data, and a certification from the CCO attesting to the program's independence and adequacy. |

---

## 8. Exception Handling and Escalation

### 8.1 Standard Escalation

An investigator encountering any of the following situations must immediately escalate in writing to the Chief Compliance Officer:

*   Reasonable grounds to believe a crime has been committed, requiring potential external referral to law enforcement.
*   Discovery of a systemic design flaw in a deployed AI system that may affect other patient populations beyond the scope of the initial complaint.
*   Suspected whistleblower retaliation by a member of senior management (VP level or above).
*   A subject refusing to cooperate with a mandated investigative interview.
*   Any attempt by a senior executive to improperly influence the investigation.

### 8.2 Exceptions

Any deviation from a mandatory procedure defined in this SOP requires a formal Exception Request. The request must be submitted in writing to the Chief Compliance Officer, specifying the procedure to be deviated from, the business justification, the compensating control or alternative approach, and the specific duration of the exception. The CCO is authorized to approve exceptions of up to 90 days for Level 3 cases. For any exception involving a Level 1 or Level 2 case, or any exception exceeding 90 days, the joint approval of the Chief Compliance Officer and the General Counsel is required.

---

## 9. Training Requirements

### 9.1 Role-Based Training Matrix

| Target Audience | Training Module(s) | Frequency | Delivery Method | Tracking System |
|-----------------|--------------------|-----------|-----------------|-----------------|
| **All Employees and Contractors** | "Code of Conduct & Ethics Hotline Awareness" (MER-LMS-ETH-101) | Annually | On-Demand eLearning (Workday) | Workday LMS |
| **All People Managers** | "Your Role in Compliance: Handling Reports & Preventing Retaliation" (MER-LMS-ETH-201) | Annually | On-Demand eLearning (Workday) | Workday LMS |
| **Legal & Compliance Team (All)** | "Confidentiality, Data Handling, and Investigation Best Practices" (MER-LMS-ETH-301) | On Hire & Annually | Instructor-Led Training (ILT) | Workday LMS |
| **Case Managers & Investigation Leads** | "Advanced Investigation Techniques and Interviewing" (MER-LMS-ETH-401) | On Assignment & Bi-Annually | External Professional Certification (e.g., ACFE, SCCE) | CCO Training Log |
| **AI Governance Committee Members & AI Engineers** | "EU AI Act Regulatory Obligations for Incident Reporting" (MER-LMS-AI-015) | Annually | Instructor-Led Training (ILT) by Regulatory Counsel | Workday LMS |

### 9.2 Remedial Training

Any individual found through a Substantiated finding to have violated a policy for which knowledge is a critical element may be required by the CCO to undergo targeted, 1:1 remedial training within 30 days of the case closure, as a specific milestone within the Corrective Action and Remediation Plan.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Policies & SOPs

| Document ID | Document Title | Relationship to this SOP |
|-------------|----------------|--------------------------|
| SOP-HRC-002 | Non-Retaliation Policy | Foundational policy for the protection of reporters. |
| SOP-ISMS-008 | Information Security Incident Response | Procedure to follow if the reported matter involves a cyber/data breach. |
| SOP-LEGC-010 | Code of Conduct | The overarching ethical principles under which the hotline operates. |
| SOP-LEGC-022 | Third-Party Due Diligence and Monitoring | Governs reports involving external partners and vendors. |
| SOP-QUAL-008 | Clinical Event Reporting | Procedure for patient safety events, used as a parallel reporting pathway. |
| SOP-RD-050 | AI System Conformity Assessment and Post-Market Surveillance | Sets the technical state-of-the-art for our systems, violations of which can form the basis of a hotline report. |
| SOP-LEGC-030 | Litigation Hold and Legal Preservation | Procedure to be initiated for all Level 1 and Level 2 investigations. |

### 10.2 External Standards and Regulations

*   Regulation (EU) 2024/1689 (The EU AI Act) — Specifically Articles 10, 13, 14, 43, 52, 68, 71, and 73.
*   U.S. Whistleblower Protection Act and related Sarbanes-Oxley (SOX) Section 806 provisions.
*   EU Directive 2019/1937 on the protection of persons who report breaches of Union law.
*   SOC 2 Common Criteria 5.2 (Control Environment Effectiveness) and 7.3 (System Incidents Detection and Response).

---

## 11. Revision History

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| 1.0 | 2022-06-10 | CCO (J. Miller) | Initial creation and rollout of the Ethics Hotline program structure. |
| 2.1 | 2023-09-12 | CCO | Major revision: Integration of Navex EthicsPoint, addition of case severity matrix and detailed KPI section, formalization of the investigation plan template. |
| 2.5 | 2024-07-25 | CCO (T. Anderson) | Comprehensive overhaul in anticipation of EU AI Act enforcement. Added entirely new procedural sub-section (5.6) for AI-specific investigations, defined roles for AI Governance Committee, and created mandatory regulatory reporting requirements for "serious incidents." |
| 2.6 | 2025-01-15 | CCO (T. Anderson) | Updated training requirements matrix to include new mandatory AI Act compliance module. Minor revisions to roles and responsibilities RACI chart to include Chief AI Ethics Officer. |
| 2.7 | 2026-03-28 | CCO (T. Anderson) | Triennial comprehensive review cycle. Enhanced physical and logical control definitions in Section 6. Updated hotline phone URL and email alias. Clarified exception handling to require joint approval for Level 1 & 2 cases. Removed obsolete reference to legacy case management tool. |
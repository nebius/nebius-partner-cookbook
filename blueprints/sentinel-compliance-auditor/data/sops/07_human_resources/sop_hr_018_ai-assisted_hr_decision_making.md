---
sop_id: "SOP-HR-018"
title: "AI-Assisted HR Decision Making"
business_unit: "Human Resources"
version: "4.7"
effective_date: "2024-04-28"
last_reviewed: "2025-01-18"
next_review: "2025-07-19"
owner: "Jennifer Walsh, Chief Human Resources Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "GDPR"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: AI-Assisted HR Decision Making

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the governance framework, operational controls, and ethical boundaries governing the use of Artificial Intelligence (AI) and automated decision-making systems within the Human Resources (HR) function at Meridian Health Technology Corporation. This SOP ensures that all AI-assisted HR decisions—from candidate sourcing to performance evaluation—are lawful, fair, auditable, transparent, and subject to meaningful human oversight. This document is a critical component of Meridian's compliance posture under the EU AI Act and the General Data Protection Regulation (GDPR), among other applicable frameworks.

### 1.2 Scope
This SOP applies to all employees, contractors, contingent workers, and third-party vendors acting on behalf of the Human Resources business unit. The scope encompasses the full employee lifecycle where AI tools are deployed:

**In-Scope Systems & Processes:**
- **Talent Acquisition & Recruitment:** AI-powered candidate sourcing, resume parsing, automated screening via the TalentIQ platform (v.3.9), video interview analysis using Parabeam Assess, and chatbot interactions via HireBot.
- **Internal Mobility & Promotion:** AI-driven skill gap identification, succession planning algorithms (SAP SuccessFactors Talent Intelligence Hub), and internal candidate matching.
- **Performance Management:** Algorithmic processing of performance review text to detect bias, AI-driven calibration of rating distributions (Workday Peakon).
- **Compensation & Benefits:** Market benchmarking algorithms for role pricing (Radford Network), anomaly detection for payroll equity analysis.
- **Employee Relations & Retention:** Attrition risk scoring models (One Model), sentiment analysis of employee engagement surveys.
- **Workforce Scheduling:** AI-optimized shift allocation for clinical support staff.

**Out-of-Scope:**
- Purely technical system administration without HR decision impact (e.g., server patching).
- Third-party payroll processing that does not use AI for decisions about individuals.
- Meridian's product-facing clinical AI (covered under SOP-MDR-022).

### 1.3 Applicability
All HR staff, hiring managers, People Analytics team members, and external recruiters are subject to this SOP. Violations of this procedure may result in disciplinary action, up to and including termination of employment and notification of regulatory authorities where legally mandated.

---

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| :--- | :--- |
| **AI System** | A machine-based system designed to operate with varying levels of autonomy, generating outputs such as predictions, recommendations, or decisions that influence physical or virtual environments. For this SOP, this includes any software using machine learning, natural language processing, or statistical modeling to support HR decisions. |
| **High-Risk AI System** | As defined by the EU AI Act, Article 6 and Annex III, any AI system intended to be used for the recruitment or selection of natural persons, for making decisions affecting terms of the work-related relationships, promotion, or termination of work-related contractual relationships, or for allocating tasks based on individual behavior, personal traits, or biometric data. All in-scope systems in Section 1.2 are provisionally classified as High-Risk by Meridian. |
| **Automated Decision-Making (ADM)** | The ability to make a decision solely by automated means without any human involvement, per GDPR Article 22. This SOP prohibits ADM in HR contexts. |
| **Human Oversight** | The active, meaningful intervention of a qualified human decision-maker who possesses the authority, competence, and training to override an AI-generated output, as required by EU AI Act Article 14. |
| **Profiling** | Any form of automated processing of personal data to evaluate, analyze, or predict certain personal aspects relating to a natural person's performance at work, economic situation, health, personal preferences, interests, reliability, behavior, location, or movements (GDPR Article 4(4)). |
| **Adverse Impact** | A substantially different rate of selection in hiring, promotion, or other employment decisions which works to the disadvantage of members of a protected group (e.g., by race, sex, age, disability status). |
| **Explainability** | The capacity to express, in clear, plain-language terms, the key factors that led to a specific AI output or recommendation for an individual (EU AI Act, Recital 47). |
| **Data Protection Impact Assessment (DPIA)** | A mandatory assessment required under GDPR Article 35 for processing operations using new technologies that are likely to result in a high risk to the rights and freedoms of natural persons. |
| **TalentIQ** | Meridian's primary recruitment CRM and ATS (Applicant Tracking System), which integrates AI screening modules. |
| **Workday Peakon** | Meridian's employee engagement and performance management platform. |
| **ServiceNow HR** | The HR case and knowledge management system used for logging exceptions and escalations. |
| **Collibra** | Meridian's data governance and cataloging platform, used to register all HR data assets. |

---

## 3. Roles and Responsibilities

The following table defines the RACI (Responsible, Accountable, Consulted, Informed) for key governance roles under this SOP.

| Role | Title / Name | Responsibilities | RACI |
| :--- | :--- | :--- | :--- |
| **SOP Owner** | Chief Human Resources Officer (CHRO) — Jennifer Walsh | Ultimate accountability for SOP content, enforcement, and annual review. Approver of all Prohibited AI Use Cases. | A |
| **AI Ethics Officer (AEO)** | Director of Responsible AI, Office of the CTO — Anya Sharma | Independent oversight of all High-Risk AI model testing for bias, fairness, and explainability. Maintains the Approved AI Model Registry. Has veto power over model deployment. | R |
| **Data Protection Officer (DPO)** | Chief Privacy Counsel — Liam O'Connell | Monitors GDPR and EU AI Act compliance. Approves DPIAs. Manages data subject rights requests. Liaises with supervisory authorities (Irish DPC as Lead). | R |
| **VP, Talent Acquisition** | Maria Sanchez | Responsible for procedural compliance in recruitment. Ensures all recruiters and hiring managers undergo mandatory training. | R, I |
| **HR Business Partners (HRBPs)** | Global HRBP Team | First line of defense for HR decision-making. Must perform the "Human Override" step in all AI-recommended decisions. | R |
| **People Analytics Director** | Dr. Ben Carter | Technical owner of all HR data feeds feeding AI models. Responsible for monthly adversarial fairness testing and metric reporting. | R, C |
| **Hiring Manager** | All People Leaders | Must be aware of AI's role in a candidate's profile and are responsible for the final, documented hiring decision. | I, R |
| **Data Steward, HR Domain** | Senior HRIS Analyst — Priya Patel | Manages data quality, lineage, and cataloging in Collibra for all AI-model inputs. | R |
| **General Counsel (GC)** | Maria Gonzalez | Legal review of all AI-related escalations, DPIAs, and exception requests. | C |

### 3.2 Committee Governance

**AI in HR Oversight Committee:**
- **Chair:** VP, Talent Acquisition (Maria Sanchez)
- **Voting Members:** AEO (Anya Sharma), DPO (Liam O'Connell), VP Total Rewards, VP HR Operations, Director of Talent Management.
- **Non-Voting Advisors:** People Analytics Director, Legal Counsel for Employment.
- **Meeting Cadence:** Monthly, with emergency sessions convened within 72 business hours for system-critical incidents.
- **Authority:** Approves all new AI use cases in HR, reviews all escalated bias complaints, and grants all exceptions under Section 8 of this SOP.

---

## 4. Policy Statements

Meridian is committed to the ethical, transparent, and lawful use of Artificial Intelligence. The following high-level policy statements govern all AI-assisted HR decision-making:

1.  **Human-in-the-Loop Mandate:** No High-Risk AI System shall make a final, legally binding HR decision without documented, meaningful human oversight. This includes, but is not limited to, decisions on hiring, termination, promotion, or compensation changes. (EU AI Act Art. 14; GDPR Art. 22).

2.  **Prohibition of Solely Automated Decision-Making:** Meridian flatly prohibits the use of any AI system that renders a decision with legal or similarly significant effects (e.g., terminating a candidate application, rejecting a promotion) without prior human review.

3.  **Lawful Basis for Processing:** Meridian will only process employee or candidate personal data using AI systems where a valid lawful basis is established and documented. The lawful basis of "Legitimate Interest" will not be invoked for new High-Risk AI systems without a thorough Legitimate Interest Assessment (LIA) approved by the DPO.

4.  **Transparency by Default:** All external candidates and internal employees must be proactively informed about the use of AI in HR processes. The logic, significance, and envisioned consequences of the processing must be communicated in plain, intelligible language (GDPR Arts. 13(2)(f), 14(2)(g)). No HR AI system shall be deployed without this notification.

5.  **Data Minimization:** AI models for HR shall only ingest the absolute minimum set of personal data necessary to achieve the defined, authorized purpose. Biometric data, emotional state analysis, and scraping of publicly available social media profiles for scoring are strictly prohibited.

6.  **Accuracy and Robustness:** All AI systems must maintain appropriate levels of accuracy, robustness, and cybersecurity. The People Analytics team must implement continuous monitoring as defined in Section 7.

7.  **Non-Discrimination:** AI systems shall be designed and monitored to ensure fairness. We explicitly prohibit the use of attributes (e.g., postcode or IP address) as proxies for protected characteristics (e.g., race or socioeconomic status).

8.  **Record-Keeping & Auditability:** All AI-generated recommendations and the subsequent human decisions must be logged immutably. This record must include the input data snapshot, the AI output, the human reviewer's identity, and their final decision with reasoning (EU AI Act Art. 12).

---

## 5. Detailed Procedures

This section details the mandatory procedural steps for each AI-assisted HR domain.

### 5.1 Procedure: AI-Assisted Recruitment and Automated Screening

This procedure governs the use of TalentIQ and Parabeam Assess for candidate identification and screening.

**Step 1: Job Description Review and Fairness Pre-Check**
- **Actor:** HR Business Partner (HRBP) & People Analytics
- **Action:**
    a.  Before posting, the HRBP uploads the job description (JD) to the TalentIQ "Bias Decoder" tool.
    b.  The Decoder scans for linguistically gendered terms (e.g., "hacker mentality," "nurturing steward"), jargon, and non-inclusive language.
    c.  People Analytics provides a report on the historical adverse impact of similar job families, benchmarked against Meridian’s 90% fairness band (EU AI Act Art. 10, para. 2(f)).
    d.  **Documentation:** The "Decoded JD" report and the historical adverse impact analysis are attached to the requisition in Workday.

**Step 2: AI Model Selection and Configuration**
- **Actor:** People Analytics Director (Dr. Ben Carter)
- **Action:**
    a.  Select the AI screening model from the Approved AI Model Registry (maintained by the AEO).
    b.  For any new role type, perform a constrained configuration, prohibiting the model from using "Name," "Address," "Gender Markers," and "URLs" as features.
    c.  Set the threshold for automated scoring confidence. The threshold shall not be set to "auto-reject" any candidate. The lowest score must still flow into a "Human Review" bucket.
    d.  **Technical Control:** Run an API call to verify the "Explainability Log" is active, which captures SHAP (SHapley Additive exPlanations) values for every recommended score.

**Step 3: Candidate Experience Notification**
- **Actor:** TalentIQ (Automated via Recruiter Bot)
- **Action:**
    a.  Upon the first interaction with the AI system (including the chatbot), the candidate receives a "Transparency Card."
    b.  **Transparency Card Wording:** *"Hello [Candidate Name], we use an AI assistant to help our recruiters process applications efficiently. This tool may analyze your resume keywords, structured responses, and relevant public certifications. It does not scrape your social media or analyze your video’s facial expressions. A human recruiter reviews all applications, and no final decision is automated. For more, see our [AI in Hiring FAQ]."* (GDPR Art. 13(2)(f)).
    c.  **Action:** The candidate must actively click "Understand & Proceed" to continue. Passive consent banners are prohibited.

**Step 4: Automated Screening and Longlisting**
- **Actor:** TalentIQ Screening Engine
- **Action:**
    a.  The AI processes applications against the configured model and generates a "Fit Score" (1-100) for each candidate.
    b.  The system groups candidates into two buckets:
        - **"High Potential" (Score > 70):** Fast-tracked for immediate Human Review.
        - **"Standard Review" (Score ≤ 70):** Queue for sequential human review.
    c.  **Prohibition:** No candidate is moved to a "Rejected" status based solely on an AI score.

**Step 5: Human Reviewer Selection and Calibration**
- **Actor:** VP, Talent Acquisition (Maria Sanchez) designee
- **Action:**
    a.  A pool of at least three (3) Recruiters is assigned to review the "High Potential" bucket.
    b.  Before review, the Recruiters undergo a 15-minute "Anchoring Bias Mitigation" exercise (detailed in Section 9 Training).
    c.  The system randomly shuffles the presentation of candidates to eliminate primacy bias.

**Step 6: The Human Oversight Decision**
- **Actor:** Recruiter
- **Action:**
    a.  The Recruiter reviews the candidate's anonymized profile (the system masks name and educational institution names at this stage). They see the AI's "Top 3" explainability factors (e.g., "7 years of Python experience matched JD requirement; Leadership keyword identified in a recent role description").
    b.  The Recruiter makes one of two decisions:
        - **"Advance"**: Moves to phone screening.
        - **"Hold for Review"**: The Recruiter must enter a specific, documented reason. "Bad fit" is not acceptable justification.
    c.  **Metadata Logging:** The Workday audit trail captures the AI score, the SHAP factors shown to the recruiter, and the human recruiter's final decision with a timestamp.

### 5.2 Procedure: Internal Mobility and Promotion Algorithms

This procedure governs the use of SAP SuccessFactors Talent Intelligence Hub for succession planning.

**Step 1: Data Source Validation**
- **Actor:** Data Steward, HR Domain (Priya Patel)
- **Action:** Weekly validation that performance review scores, skill endorsements, and tenure data flowing into the Talent Intelligence Hub match the golden source systems of record (Workday, Learning Management System (LMS) - Cornerstone). Data lineage is verified in Collibra.

**Step 2: "Flight Risk" Processing and Anonymization**
- **Actor:** People Analytics Director
- **Action:** Running of the "One Model" retention risk model. The output must be aggregated to the department level (minimum group size of 25) before being delivered to HRBPs. Individual-level flight risk scores are treated as sensitive personal data and are not visible to line managers.

**Step 3: Manager-Initiated Succession Inquiry**
- **Actor:** People Leader (Manager)
- **Action:** A manager queries the Talent Intelligence Hub for "Potential Successors for my VP, Engineering Role."
- **System Behavior:** The system will generate a "Recommendation Slate" of internal candidates. The slate will explicitly exclude employees who have self-identified as having a disability or serious health condition if the AI correlates this with reduced availability.

**Step 4: Internal Transparency and Opt-Out**
- **Actor:** Internal Employee (Candidate)
- **Action:** All internal candidates identified by the AI must already have opted "in" to internal mobility screening. This is configured in the employee’s Workday Talent Profile ("Open to AI-Driven Career Opportunities?" toggle). The toggle defaults to "No" (privacy by default).

**Step 5: Talent Review Meeting (The Human Oversight Point)**
- **Actor:** People Leader, HRBP, and Senior Leader (Skip-level manager)
- **Action:** The AI-generated slate is a conversation starter, not a final shortlist. The Talent Review meeting must document:
    a.  Why each AI-recommended candidate was or was not considered.
    b.  A non-AI-driven qualitative review of readiness based on the leader’s direct knowledge of the individual.
    c.  **Documentation:** Minutes of the Talent Review are stored in the employee's confidential succession plan record with a 3-year retention period.

### 5.3 Procedure: AI in Performance Management (Workday Peakon)

**Step 1: Natural Language Processing (NLP) Guardrails**
- **Actor:** People Analytics
- **Action:** The sentiment analysis algorithms applied to performance reviews are configured to exclusively analyze structural themes ("Mentions of Budget Management," "Specific Collaboration Examples") only. The sentiment analysis feature is explicitly disabled for tone analysis (e.g., "frustrated," "angry").

**Step 2: Managerial Review of Calibration Ratings**
- **Actor:** Direct Manager
- **Action:** Workday Peakon provides an AI-generated "Potential Rating Distribution" for the team based on peer feedback and goal achievement data. The manager must complete the "Manager’s Equity Adjustment" screen, which explicitly asks: *"The AI suggests the following distribution. Do you observe any bias or anomaly? If you override the AI’s suggestion, document your rationale."*

**Step 3: Second-Line Validation**
- **Actor:** HRBP
- **Action:** For any performance rating of "Below Expectations" or the topmost "Exceptional" rating, the HRBP performs a final review. The review explicitly checks if the AI-recommended rating was influenced by proxy data (e.g., a drop in a project management score due to an employee being on FMLA-protected leave).

### 5.4 Procedure: Data Subject Rights and AI (GDPR Arts. 15-22)

**Step 1: Access Request (GDPR Art. 15)**
- **Actor:** Privacy Operations Team (ServiceNow case intake)
- **Action:** Upon receiving a DSAR, the team must query the "AI Decisioning Log" in addition to standard HR records. The output provided to the employee must include, in plain language, "meaningful information about the logic involved, as well as the significance and the envisaged consequences of such processing for the data subject."

**Step 2: Objection and Human Intervention Request (GDPR Art. 22(3))**
- **Actor:** Employee / Candidate
- **Action:** Any individual subject to an AI-assisted HR decision they deem adverse has the right to object. Upon logging a case in ServiceNow HR ("Category: AI Decision Appeal"):
    a.  Automated processing of that specific individual's data is paused within 24 hours.
    b.  The matter is reviewed by a human reviewer not previously involved in the decision. This reviewer (designated by the VP, Talent Acquisition) has the authority to override the AI.
    c.  The final human determination is communicated to the employee within 7 business days.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control ID | Control Description | Implementation Mechanism | Responsible Team |
| :--- | :--- | :--- | :--- |
| **TEC-01** | Explainability Logging | All High-Risk AI systems log SHAP/LIME values for each prediction to an immutable, encrypted Splunk index (`idx_hr_ai`). Retention: Duration of employment + 7 years. | People Analytics, Security Engineering |
| **TEC-02** | Data Anonymization at Point of Screening | The first-stage screening (Section 5.1, Step 6) in TalentIQ masks PII fields (Name, Email, Phone, Linkedin URL) using a deterministic tokenization process with AWS KMS-managed keys. | HRIS, Cloud Security |
| **TEC-03** | Feature Restriction (Prohibited Inputs) | An egress firewall rule on the People Analytics subnet blocks API calls to external AI models that contain specific string patterns (e.g., "SocialMediaScore," "EmotionAnalysis," any biometric hash). | Network Security, People Analytics |
| **TEC-04** | Adversarial Robustness Testing | Weekly, a set of synthetic, adversarial resumes (e.g., containing encoded gender cues like "President of the Men’s Chess Club") is run against the production model. If the outcome varies significantly, an alert is sent to the AEO and the model is taken offline for retuning. | Security Engineering (Red Team), AEO |
| **TEC-05** | Data Lineage Tracking | All HR data elements used as AI model inputs are tagged in Collibra with "Used in High-Risk AI." The lineage from source system to AI feature store is automatically mapped. | Data Steward (HR Domain) |
| **TEC-06** | Log Integrity | SHA-256 hashing of all decision logs. A daily script verifies the checksum chain, and anomalies are reported to the DPO and CISO as a potential breach of Art. 5(1)(d) (accuracy) and Art. 25 (data protection by design). | Security Engineering |

### 6.2 Administrative Controls

| Control ID | Control Description | Evidence | Responsible Role |
| :--- | :--- | :--- | :--- |
| **ADM-01** | Approved AI Model Registry | The AEO maintains a Confluence-based registry listing every approved HR AI Model (v. ID, purpose, training data lineage, date of last fairness test). No model can go live without being on this list. | Anya Sharma, AEO |
| **ADM-02** | Legitimate Interest Assessment (LIA) | For any processing based on legitimate interest, a formal LIA, applying the three-part test, is prepared by People Analytics and approved by the DPO and GC. | Dr. Ben Carter, People Analytics Dir. |
| **ADM-03** | Mandatory AI Calibration Sessions | Monthly, the recruiting team spends 2 hours reviewing a sample of decisions where the AI score and human decision diverged significantly (e.g., AI scored <30, human advanced). | CHRO / VP, Talent Acquisition |
| **ADM-04** | DPIA Gate Process | Before any new AI system or significant change to an existing one, a DPIA is required. This is triggered via a ServiceNow HR project request and reviewed by the DPO. | Project Owner |
| **ADM-05** | Third-Party Vendor Assessments | All AI vendor contracts must include a mandatory Data Protection Addendum (DPA) and allow Meridian's DGP team the right to audit their training data and fairness testing methodologies. Annual review is mandatory. | Procurement, DPO |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

| Metric | Target | Measurement Method | Reporting Cadence | Owner |
| :--- | :--- | :--- | :--- | :--- |
| **Human Override Rate** | > 2% of AI recommendations | (Number of times a Human Reviewer explicitly changed an AI recommendation) / (Total AI recommendations generated in a period) | Monthly Dashboard | CHRO |
| **Selection Rate Adverse Impact Ratio (4/5ths Rule)** | Ratio must be ≥ 0.80 | Analysis by protected group (Gender, Race/Ethnicity as voluntarily self-identified), comparing "Advance" rate from AI bucket vs. total applicant pool. | Quarterly Regulatory Report | People Analytics, Legal |
| **Model Explainability Score** | Mean SHAP fidelity > 0.95 | Daily technical metric run on the `idx_hr_ai` Splunk index, testing if the logged explanatory features accurately predict the model's output. | Weekly Tech. Ops Review | MLOps Engineer |
| **Data Subject Complaints (Art. 22)** | Cases per quarter < 5 | Count of ServiceNow HR tickets logged under "Category: AI Decision Appeal." | Monthly DPO Report | DPO (Liam O'Connell) |
| **Training Compliance** | 100% of active recruiters and hiring managers | Workday Learning completion records for training `SOP-HR-018-TRN`. | Real-Time Dashboard | VP, Talent Acquisition |
| **Model Drift** | Population Stability Index (PSI) < 0.1 | Weekly comparison of the distribution of current candidate features against the baseline distribution from the model's training window. | Weekly Tech. Ops Review | People Analytics |

### 7.2 Reporting and Documentation

- **Daily Operations Report:** An automated email from People Analytics to the VP of TA detailing the number of candidates screened, the distribution of scores, and any system errors.
- **Monthly AI in HR Scorecard:** A formal slide deck presented to the AI in HR Oversight Committee. Contains all KPIs, a summary of exceptions granted, and the outcomes of bias testing.
- **Annual Compliance Review:** A comprehensive narrative report prepared by the DPO and CHRO for the CEO and Board Risk Committee, summarizing regulatory compliance (EU AI Act, GDPR), the approved AI inventory, and a strategic roadmap for the next year.

---

## 8. Exception Handling and Escalation

### 8.1 Standard Exception Requests
Any request to deviate from a specific procedure in this SOP (e.g., to use an unregistered model for a limited pilot, to temporarily disable a transparency card for a unique executive search) must follow this path:

1.  **Documentation:** The requester must file a "Policy Exception Request" in ServiceNow HR. The form requires:
    - Specific SOP section(s) for which an exception is sought.
    - Business justification (must include risk analysis).
    - Proposed compensating controls.
    - Duration (maximum 6 months).
2.  **Review:** Ticket is routed to the DPO for technical and legal review.
3.  **Approval Tier 1 (Low-Medium Risk):** Approval by VP, Talent Acquisition and DPO.
4.  **Approval Tier 2 (High Risk / Duration > 90 days):** Must be approved by the full AI in HR Oversight Committee and the CHRO.
5.  **Tracking:** All exceptions are logged in a central, auditable register.

### 8.2 Escalation of Bias Incidents
If an employee or an external party reports a suspected instance of AI-generated bias or discrimination, the escalation path is immediate and mandatory:

1.  **Stop:** The Responsible AI Officer (Anya Sharma) is immediately notified and can issue a "Blue Stop" order to freeze the specific AI model's inference pipeline. Downtime SLA for a Blue Stop: 2 hours.
2.  **Preserve:** All associated AI logs, model inputs, outputs, and the human decision record for the affected individual(s) are permanently snapshot and moved to a secure, immutably stored "Litigation Hold" bucket on Amazon S3 Glacier.
3.  **Investigate:** The DPO and AEO lead a joint immediate investigation within 5 business days.
4.  **Notify:** If the investigation confirms a high likelihood of discriminatory impact, the DPO coordinates mandatory breach notification to the relevant Supervisory Authority within 72 hours of the confirmation (per GDPR Art. 33), and the affected individuals are notified without undue delay (GDPR Art. 34). The incident is also logged as a major non-conformance against our ISO-27001 certification.

---

## 9. Training Requirements

### 9.1 Mandatory Training Programs

All roles defined in Section 3 must complete the following training, tracked via the Workday Learning Management System (LMS):

- **`SOP-HR-018-TRN-01: AI Literacy for HR Professionals`**
    - **Audience:** All HR Staff, Recruiters, HRBPs, Talent Management, Compensation.
    - **Frequency:** Annually.
    - **Description:** Foundational course covering how AI works (basic ML and NLP), Meridian’s specific AI tools, our transparency commitments, and the critical importance of human oversight.
    - **Completion SLA:** Within 30 days of hire or annual cycle start.

- **`SOP-HR-018-TRN-02: Anchoring and Automation Bias Mitigation`**
    - **Audience:** Recruiters, Hiring Managers, Succession Planners.
    - **Frequency:** Quarterly.
    - **Description:** A short, scenario-based micro-course (15 min) using realistic Meridian data. Trainees practice correctly overriding an AI recommendation that appears confident but is based on spurious correlations. Failure of this course requires a 1-on-1 with the People Analytics Director.

- **`SOP-HR-018-TRN-03: Data Stewardship for AI`**
    - **Audience:** HRIS Analysts, People Analytics, Data Stewards.
    - **Frequency:** Bi-Annually.
    - **Description:** Deep-dive technical training on Collibra lineage, data quality metrics for model fitness, and GDPR Art. 25 (Data Protection by Design and by Default).

- **`SOP-HR-018-TRN-04: EU AI Act & GDPR Awareness for Leaders`**
    - **Audience:** CHRO, VP-TA, VP-HR Ops, HR Directors.
    - **Frequency:** Annually.
    - **Description:** Legal liability briefing led by the DPO and General Counsel, covering recent enforcement actions, the Meridian Consequence Management policy, and their specific accountability under Art. 26 of the EU AI Act.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs and Policies
- **SOP-DPO-001:** Data Subject Access Request (DSAR) Handling
- **SOP-HR-003:** Global Recruitment and Hiring Policy
- **SOP-HR-009:** Performance Management and Calibration
- **SOP-HR-022:** Employee Data Privacy Notice
- **SOP-IS-101:** Information Security Incident Response Plan
- **SOP-LEG-042:** Third-Party Vendor Data Protection Addendum
- **SOP-R&D-005:** Model Risk Management Framework (Non-Product Systems)
- **Policy-CHRO-001:** Code of Conduct and Workplace Discrimination

### 10.2 External Standards and Regulations
- **EU General Data Protection Regulation (GDPR) 2016/679**
- **Regulation (EU) 2024/1689:** The Artificial Intelligence Act (EU AI Act)
- **ISO/IEC 42001:2023:** Information technology — Artificial intelligence — Management system
- **NIST Special Publication 800-53 Rev. 5:** Security and Privacy Controls for Information Systems and Organizations

---

## 11. Revision History

| Version | Date | Author(s) | Description of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2020-03-15 | J. Walsh, L. O'Connell | Initial Draft. Focus on GDPR Art 22. |
| 2.1 | 2021-11-01 | B. Carter (People Analytics) | Added technical controls for AI explainability. Defined human reviewer role formally. |
| 3.0 | 2022-06-22 | J. Walsh, A. Sharma (AEO) | Major overhaul to establish the RACI matrix and introduce the AEO role. Added recruitment-specific procedures. |
| 4.2 | 2023-09-10 | A. Sharma, L. O'Connell | Updated to pre-comply with draft EU AI Act. Prohibited emotion/biometric analysis. Introduced the Approved AI Model Registry. |
| 4.5 | 2024-01-05 | J. Walsh, M. Sanchez (VP-TA) | Added Performance Management scope (Workday Peakon). Calibrated KPIs for adverse impact measurement. |
| 4.7 | 2024-04-28 | L. O'Connell (DPO) | Final alignment with adopted EU AI Act text. Explicit transparency card wording mandated. Expanded data subject rights section. |
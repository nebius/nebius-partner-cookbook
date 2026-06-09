---
sop_id: "SOP-HR-012"
title: "AI Ethics Committee Governance"
business_unit: "Human Resources"
version: "4.0"
effective_date: "2025-02-28"
last_reviewed: "2026-09-10"
next_review: "2027-03-05"
owner: "Jennifer Walsh, Chief Human Resources Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "EU AI Act"
  - "NIST AI RMF"
status: "Active"
---

# Standard Operating Procedure: AI Ethics Committee Governance

## 1. Purpose and Scope

This Standard Operating Procedure (SOP) establishes the governance framework, operational mandate, and procedural mechanisms for the Meridian Health Technologies, Inc. AI Ethics Committee (the “Committee”). The Committee serves as the central, independent oversight body responsible for ensuring that all Artificial Intelligence (AI) and Machine Learning (ML) systems developed, deployed, or procured by Meridian Health Technologies align with the organization’s ethical principles, regulatory obligations, and patient safety commitments.

The purpose of this SOP is to define the systematic review of high-risk AI systems, enforce human oversight protocols, operationalize transparency obligations, and create a structured channel for addressing ethical concerns across the entire AI lifecycle—from inception and data acquisition through deployment, monitoring, and decommissioning. This document formalizes the Committee’s authority to approve, conditionally approve, or reject AI initiatives based on ethical, safety, and fundamental rights impact assessments.

**Scope:** The provisions of this SOP apply to all business units, departments, employees, contractors, and third-party vendors operating within Meridian Health Technologies globally. This includes, but is not limited to, the Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the underlying Meridian SaaS Platform. This SOP is binding upon all geographical offices (Boston, London, Berlin, Singapore, Toronto) and governs AI systems processing data of individuals regardless of jurisdiction. The review mandate of this Committee specifically covers:

- All new AI/ML systems classified as high-risk under the EU AI Act prior to market deployment or first use in an operational environment.
- Substantial modifications to existing AI systems that alter their intended purpose, performance characteristics, or risk profile.
- Any AI system, regardless of regulatory classification, that an internal stakeholder or Committee member escalates due to potential ethical harm, bias, or patient safety concerns.
- Third-party AI components integrated into Meridian products, including APIs and embedded models.

**Out of Scope:** This SOP does not cover general software quality assurance, standard code review processes managed by the Engineering department, or routine security patching unless the patch alters model behavior in a manner that triggers the definition of a "substantial modification" as defined herein.

## 2. Definitions and Acronyms

The following terms are critical to the accurate interpretation and execution of this SOP.

| Term / Acronym | Definition |
| :--- | :--- |
| **AI Ethics Committee (AEC)** | The independent, cross-functional governance body established by this SOP to oversee the ethical dimensions of AI systems at Meridian. |
| **AI System** | A machine-based system that is designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments. This includes models, associated data pipelines, and user interfaces. |
| **High-Risk AI System** | An AI system that meets the classification criteria of Article 6 and Annex III of the EU AI Act. Within Meridian, this applies to all systems deployed in the Clinical AI Platform (safety components for medical devices) and specific models within HealthPay (credit scoring and fraud detection for essential services). |
| **Substantial Modification** | A change to an AI system after its initial deployment that affects its compliance with the EU AI Act or alters the system’s intended purpose such that the risk profile materially changes. Includes retraining on a new population, adding a new data modality, or changing the operational threshold (e.g., sensitivity) that changes clinical decision-making. |
| **PHI** | Protected Health Information, as defined by HIPAA. |
| **Conformity Assessment** | The process defined in EU AI Act Article 43 to demonstrate that a high-risk AI system complies with the requirements of Chapter 2 of the Act. |
| **Human Oversight** | The capability for human intervention in the AI system's lifecycle, built into the system by design (as per Article 14) or implemented in the operational context, to prevent or minimize risks to health, safety, or fundamental rights. |
| **RACI** | Responsibility Assignment Matrix: Responsible, Accountable, Consulted, Informed. |
| **MLOps** | Machine Learning Operations, the CI/CD pipeline for ML systems managed by the AI Engineering team. |

## 3. Roles and Responsibilities

A RACI matrix has been established to delineate the duties of all parties involved in the AI Ethics Committee governance process. The roles defined below are mandatory and legally accountable where specified.

| Role | Responsibility in AEC Context | RACI Assignment |
| :--- | :--- | :--- |
| **Chief AI Officer (CAIO)** | Chairs the AI Ethics Committee. Final decision authority on model deployment clearance and ethical risk acceptance. | A, R (for overall committee function) |
| **Chief Medical Officer (CMO)** | Represents patient safety and clinical efficacy. Has authority to veto any system that poses an immediate threat to patient health. | R, C (on clinical models) |
| **Chief Human Resources Officer (CHRO)** | Policy owner of SOP-HR-012. Responsible for procedural integrity, bias impact on workforce, and committee composition. | A (for policy maintenance), R (for workforce impact) |
| **Data Protection Officer (DPO)** | Reviews all AI systems for compliance with GDPR and HIPAA. Provides binding guidance on data usage permissibility. | R (for privacy/data protection) |
| **Chief Information Security Officer (CISO)** | Assesses security controls of AI pipelines and adversarial robustness. | C |
| **VP, Clinical AI Engineering** | Submits technical documentation and Conformity Assessment packages for Clinical AI Platform products. Responds to Committee technical queries. | R (for submissions), C |
| **VP, HealthPay Engineering** | Submits evidence of fairness, transparency, and SR 11-7 compliance for financial models. | R (for submissions), C |
| **Legal & Compliance Counsel** | Interprets regulatory obligations (EU AI Act, MDR, HIPAA), evaluates liability risk, and represents the organization in regulatory filings related to Committee decisions. | R (for legal interpretation), C |
| **Independent Ethics Advisor(s)** | External, non-voting advisors appointed annually. Minimum two persons with domain expertise in medical ethics or algorithmic fairness. Provide impartial review of high-impact disputes. | C |

## 4. Policy Statements

The AI Ethics Committee operates under the following foundational policy commitments, approved by the CEO and Board of Directors. Non-compliance with these statements by any employee or contractor constitutes grounds for disciplinary action up to and including termination and contract annulment.

- **PS-01: Mandatory Pre-Deployment Review.** No high-risk AI system shall be placed on the market, put into service in the EU, or used within a clinical operational environment in the U.S. until it has received explicit written authorization from the AI Ethics Committee. This authorization must not exceed a validity of 24 months without re-assessment.
- **PS-02: Human Oversight Mandate.** All high-risk AI systems shall be designed and deployed with appropriate human-machine interface tools that allow natural persons to oversee the system during its period of use. The Committee must validate that such oversight prevents automation bias and is calibrated to the risk level.
- **PS-03: Transparency and Right to Explanation.** When a Meridian AI system makes a materially adverse decision concerning an individual (e.g., denial of coverage scoring, critical health risk stratification), the system architecture must support an auditable decision log that provides, in plain language, the principal factors contributing to that specific output.
- **PS-04: Bias and Fairness Zero-Tolerance (Clinical).** The Committee shall not approve any clinical diagnostic or prognostic model wherein the equal opportunity difference (True Positive Rate parity) between any protected demographic subgroups exceeds five percentage points (5%), as measured on the target validation dataset defined in the Conformity Assessment.
- **PS-05: Data Minimization.** The DPO on the Committee shall certify that all datasets used for training and inference represent the minimal necessary data required to achieve the defined, approved intended purpose. The Committee will reject any model using superfluous or legally prohibited data categories.

## 5. Detailed Procedures

The following procedures are established to execute the governance mandate defined in this SOP. All steps are sequential and subject to the SLAs specified in Section 7 unless an exception is granted according to Section 8.

### 5.1 Committee Intake and Submission Protocol

The submission lifecycle begins with the Product Owner and Lead Data Scientist of the AI system in question.

1.  **Pre-Submission Meeting:** The project team must schedule a consultation with the Committee’s Secretary (a staff member assigned by the CAIO) no fewer than 4 weeks before the anticipated submission date. The purpose is to confirm the risk classification of the AI system.
2.  **Document Package Compilation:** The Sponsor (VP-level) must compile a digital Conformity Assessment Package in Jira Service Management using the template `AI-ETHICS-TMPL-01`. The package must contain:
    - Intended Purpose and Intended Use environment documentation.
    - Full Model Card (referencing SOP-MLP-005).
    - Dataset Datasheet for training, validation, and test sets.
    - Results of a Clinical Utility or Business Value analysis.
    - Preliminary EU AI Act Annex IV technical documentation.
3.  **Formal Logging:** The Secretary enters the submission into the `AEC-Docket` register. A unique Docket ID (e.g., AEC-2027-045) is generated. The Secretary has 48 hours to reject an incomplete package and 5 business days to certify the package as "Ready for Review."

### 5.2 Preliminary Ethical Impact Screening (Triage)

Upon certification of the submission package as complete, the CAIO assigns a three-person Rapporteur team from the Committee membership: typically the DPO, a Legal Counsel, and one subject-matter engineer from a different business unit. This team conducts a rapid-fire triage lasting no more than 5 business days.

- **Step 1 (Discrimination Audit):** The DPO uses the `Fairness-360` monitoring dashboard to verify the submitted fairness metrics against the Policy Statement PS-04 threshold. Any breach results in automatic suspension of the review and return of the package to the sponsor with a "Fail - Bias" designation.
- **Step 2 (Scope Creep Check):** The Rapporteur verifies that the intended purpose stated matches the validated function. Any evidence of dual-use or purpose creep is flagged as a Critical Risk.
- **Output:** The Rapporteur publishes a Triage Report categorizing the submission as `Low Materiality / Fast-Track` or `Full Committee Review Required`.

### 5.3 Full Committee Deliberation and Voting

For all submissions categorized as Full Committee Review, the following protocol is enforced.

1.  **Quorum:** No binding vote of the AI Ethics Committee may occur without a quorum of the following four permanent members present (physically or via secure video): CAIO, CMO, DPO, and Legal & Compliance Counsel.
2.  **Presentation:** The project Sponsor (e.g., VP, Clinical AI Engineering) presents the system. The Independent Ethics Advisors provide a public comment.
3.  **Deliberation and Voting:** Voting is restricted to the permanent members and the Independent Advisors (who vote only in a deadlock). Outcomes are:
    - **Approved:** Unanimous consent by quorum members. Authorization is recorded in the Master AI Registry.
    - **Conditionally Approved:** System is authorized for a specific sub-population or clinical setting, or with a strict 90-day review contingency attached to monitor a specific metric (e.g., alert fatigue).
    - **Rejected:** The system cannot be deployed in its proposed form. The CAIO must issue a Rejection Brief detailing the specific reasons within 72 hours.
4.  **Veto Authority:** The CMO may exercise an immediate, non-debatable veto if they judge the system to present a "Clear and Unambiguous Imminent Danger to Life." Such a veto must be accompanied by a formal memo to the CEO within 24 hours.

### 5.4 Post-Deployment Monitoring and Revalidation

AI system clearance is not permanent.

1.  **Continuous Monitoring:** The MLOps team pipes a stream of model output statistics and drift monitors into the Committee’s governance dashboard (see Section 7).
2.  **Triggered Re-review:** The system is automatically flagged for re-review by the Secretary if:
    - The drift monitor exceeds a Population Stability Index (PSI) of 0.25.
    - A new sub-population fairness metric drops below the 5% parity margin.
    - Any Critical Adverse Event is logged and attributed by the Clinical Risk Management team as “Likely AI Related.”
3.  **24-Month Mandatory Expiration:** 18 months after initial deployment authorization, the engineering team must begin assembling an updated Conformity Assessment package. If the full re-validation process is not completed and approved by Month 24, the system’s `Active` status is automatically suspended by the TSM system via an automated API call, and the system must be removed from clinical or financial production workflows.

## 6. Controls and Safeguards

The following administrative and technical controls are implemented to ensure the integrity of the Committee’s governance process and enforcement of its decisions.

### 6.1 Technical Controls for Enforcement

- **MLOps Integration with Jira (TSM):** The deployment pipeline in AWS SageMaker and GCP Vertex AI is governed by a release gate API (`aec-governance-gateway.p.internal`). This API queries the `AEC-Docket` table. If a model UUID is not in `Approved` status, the build pipeline is blocked at the Staging to Production promotion stage. No administrative override exists for the CISO or CAIO to bypass this block manually; a bypass requires a new vote (refer to exception handling, Section 8.2).
- **Audit Trail Immutability:** All Committee deliberation minutes, votes, and justifications are immutably logged and hashed daily. The hash chain is stored in a separate, write-once-read-many (WORM) data store for non-repudiation. This ensures the decision trail for EU AI Act Article 12 (Record-keeping) is met.
- **Access Control:** The AEC governance dashboard and TSM-AEC integration are governed by Role-Based Access Control (RBAC). Only the CAIO chair account can toggle a model status manually for emergency halts.

### 6.2 Administrative Safeguards

- **Conflict of Interest (COI) Disclosure:** Prior to any deliberation, every voting member must affirm a COI disclosure via the ServiceNow GRC module. If a member has a direct operational reporting line to the sponsor of the AI system under review, they must recuse themselves from the vote but may remain for debate.
- **Whistleblower Protection:** Any Meridian employee who bypasses the AEC to report an ethical violation externally (e.g., to a regulatory body) is protected under Meridian’s Non-Retaliation Policy (SOP-LEG-099). Internal reporting of violations to the Committee through the secure ombuds channel is mandatory without reprisal.

## 7. Monitoring, Metrics, and Reporting

The performance of the AI Ethics Committee itself, and the population of systems under its oversight, are subject to rigorous Key Performance Indicators (KPIs). The Chief Human Resources Officer owns the metric framework for Committee efficacy.

| KPI Category | Specific Metric | Target | Reporting Cadence |
| :--- | :--- | :--- | :--- |
| **Operational Efficiency** | Time-to-Decision (Triage Submission to Vote) | Median < 14 calendar days | Monthly (CAIO Dashboard) |
| **Operational Efficiency** | Aged Docket Items (> 30 days without vote) | Zero tolerance; immediate escalation to CEO | Weekly |
| **Compliance** | Lapsed Authorizations (systems active past 24 mos expiry) | 0 systems in production | Daily automated scan |
| **Equity & Fairness** | Post-deployment disparity drift (PSI > 0.25) | Review initiated < 48 hrs of breach | Continuous; Report bi-weekly |
| **Safety** | Critical Adverse Events linked to AI Systems | Root Cause Analysis presented to AEC in < 72 hours | Per-event immediate trigger |
| **Coverage** | Percentage of active high-risk AI systems in Master Registry vs. detected systems in environment | 100% (No shadow AI). Reconciliation monthly by CAIO. | Monthly |

The CAIO must submit a formal Annual Transparency Report to the CEO and the Board’s Audit Committee. This report will summarize all docket items processed, total models in production, total systems rejected, and an aggregate summary of fairness metrics across all active Clinical AI and HealthPay models. This report forms part of the public-facing transparency disclosure strategy aligned with the EU AI Act’s transparency obligations.

## 8. Exception Handling and Escalation

There exist circumstances that require deviation from the standard decision-making or policy thresholds.

### 8.1 Clinical Emergency Override (Emergency Use Authorization)
In the event of a declared public health emergency or a life-threatening clinical scenario where a fully approved AI system is unavailable, the CMO, with the concurrence of the CEO, may authorize the temporary deployment of a Conditionally Approved or even Pre-Vote AI system.

- **Procedure:** The CMO must file an Emergency Use Notification (EUN) with the Secretary within 4 hours of the authorization.
- **Duration:** The EUN authority expires in 7 calendar days. If the situation persists, the AEC must be convened within 48 hours of the EUN to vote on a retroactive 30-day conditional review. Full Conformity Assessment must still be expedited.

### 8.2 Dispute Resolution and Escalation
If a business unit executive (VP level or above) contests a Rejection decision, the following escalation ladder applies:
1.  **Reconsideration Request:** Within 5 business days of the rejection, file a request with rebuttal evidence. The CAIO convenes a special session.
2.  **Deadlock Arbitration:** If the Committee remains deadlocked or the CAIO upholds the rejection, the dispute is elevated to the CEO via a joint memo from the Sponsor and the CAIO.
3.  **CEO Binding Arbitration:** The CEO reviews the risk acceptance. If the CEO authorizes deployment over the Committee’s objection (a "Superseding Executive Order"), this authorization, the CEO’s rationale, and the Committee’s formal objection must be jointly submitted to the Data Protection Authority or relevant Notified Body where regulatory filing is mandated within 15 days.

## 9. Training Requirements

To ensure the effective functioning of the Committee and compliance of submitting teams, the following training regimens are mandatory.

- **AEC Member Onboarding Training (Course Code: AEC-101):** All new Committee members must complete this 4-hour executive micro-course within 10 business days of their appointment. The curriculum covers the reading of Conformity Assessments, adversarial interrogation of model evidence, and the specific veto protocols of medical team members. **Frequency:** Once per appointment.
- **AI Ethics for Submitters (Course Code: AIET-201):** All Data Scientists, ML Engineers, and Product Managers (Level 4 and above) involved in high-risk AI system development must complete this training annually. The course covers how to generate the Model Card and Dataset Datasheet required for Section 5.1 submission.
- **EU AI Act Legal Update (Course Code: COMP-401):** Mandatory annual training for all AEC voting members and Legal staff. Content is updated yearly by the DPO and General Counsel’s office to reflect regulatory guidance evolution. Completion recorded in Workday Learning.

Compliance with training is tracked by the CHRO. Any AEC member with overdue training for more than 15 days loses their voting privilege until the deficiency is cleared.

## 10. Related Policies and References

This SOP does not stand alone; it is part of a cohesive governance ecosystem.

| Document Reference | Title | Relationship |
| :--- | :--- | :--- |
| **SOP-MLP-005** | Model Lifecycle Management & Documentation | Defines the mandatory Model Card and Datasheet templates referenced in Section 5.1 intake. |
| **SOP-LEG-099** | Non-Retaliation and Whistleblower Protection Policy | Governs protections invoked in Section 6.2 for ethical reporting. |
| **SOP-DPO-007** | Data Protection Impact Assessment (DPIA) Protocol | Required prerequisite submission for any AI system ingesting PHI, to be reviewed by the DPO during Committee triage. |
| **SOP-CLIN-088** | Clinical Validation and Post-Market Surveillance | Describes the adverse event logging that triggers AEC re-review under Section 5.4. |
| **External Doc: EU 2024/1689** | The EU Artificial Intelligence Act | Foundational regulatory basis for classification, conformity, and governance procedures defined in this SOP. |
| **External Standard: ISO/IEC 42001:2023** | AI Management System Standard | The Committee’s process design references this standard’s requirements for management accountability and continuous improvement. |

## 11. Revision History

This document has been iteratively refined to address evolving regulatory pressures and internal operational learnings from four years of AEC operation.

| Version | Date | Author / Editor | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 1.0 | 2021-11-15 | J. Walsh (CHRO) | Initial establishment of voluntary review board; advisory capacity only. |
| 2.0 | 2023-05-22 | K. Tanaka (Legal) | Transition to binding authority for Clinical AI; introduced rudimentary RACI matrix; prepared for EU AI Act draft alignment. |
| 3.0 | 2024-07-30 | A. Hassan (CAIO Office) | Major revision: Introduced mandatory Conformity Assessment workflows, strict 5% parity rule for bias (PS-04), and the MLOps technical gate integration described in Section 6.1. |
| 3.1 | 2025-09-18 | J. Walsh (CHRO) | Clarified quorum definitions and added Independent Ethics Advisor role following feedback from external audit. |
| 4.0 | 2026-09-10 | P. Lindberg (GRC Team) | Full restructure of Section 5.4 (Post-Deployment Monitoring) to mandate 24-month auto-suspension functionality. Enhanced enforcement of transparency PS-03 to cover financial services. Policy re-approved for CE marking alignment cycle. |
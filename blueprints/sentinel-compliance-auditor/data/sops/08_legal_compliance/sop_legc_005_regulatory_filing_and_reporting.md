---
sop_id: "SOP-LEGC-005"
title: "Regulatory Filing and Reporting"
business_unit: "Legal & Compliance"
version: "5.6"
effective_date: "2025-04-16"
last_reviewed: "2026-05-18"
next_review: "2026-11-22"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "HIPAA"
  - "GDPR"
  - "SR 11-7"
status: "Active"
---

# Standard Operating Procedure: Regulatory Filing and Reporting

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, governance, and operational processes for the identification, preparation, review, approval, submission, and archival of all regulatory filings and reports required by the statutes, regulations, and supervisory guidance applicable to Meridian Health Technologies, Inc. and its wholly-owned subsidiaries. The purpose of this document is to ensure the completeness, accuracy, timeliness, and defensibility of all regulatory submissions, thereby maintaining Meridian’s license to operate, upholding its fiduciary duties, and demonstrating the effectiveness of its compliance management system to internal and external stakeholders.

### 1.2 Scope

This SOP applies to all regulatory filings, reports, notifications, and disclosures mandated by the regulatory frameworks under which Meridian operates. The scope encompasses:

| Scope Area | Coverage |
| --- | --- |
| **Business Units** | Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, Meridian SaaS Platform, and all corporate support functions (Finance, HR, IT, Security). |
| **Geographies** | Operations in the United States, European Union (including the European Economic Area), United Kingdom, Canada, and Singapore. |
| **Regulatory Regimes** | HIPAA, GDPR, SR 11-7 (Model Risk Management), EU AI Act, EU Medical Device Regulation (MDR) for cleared products, FDA requirements for 510(k)-cleared devices, SOC 2 reporting obligations, and state-level privacy and data security requirements. |
| **Report Types** | Periodic regulatory submissions (annual, semi-annual, quarterly, monthly), event-driven notifications (security incidents, model performance breaches, safety signals), certification attestations, and responses to regulatory inquiries or examination findings. |
| **Personnel** | All permanent employees, contractors, consultants, and third-party vendors who have a role in the creation, review, approval, or submission of a regulatory filing. |

### 1.3 Out of Scope

This SOP does not cover the operational processes for creating the *underlying data* used in regulatory reports, which are governed by data governance SOPs. Tax filings managed by the Finance department under separate IRS and HMRC procedures are excluded. Routine contractual reporting to commercial partners that does not have a statutory or regulatory mandate is outside the scope of this SOP.

## 2. Definitions and Acronyms

| Term / Acronym | Definition |
| --- | --- |
| **AI Act** | Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence. |
| **AIMS** | Meridian’s internal AI Incident Management System, a module within the ServiceNow GRC platform used to log, track, and manage AI-related incidents and safety signals. |
| **BA** | Business Associate, as defined by HIPAA. |
| **CCO** | Chief Compliance Officer. |
| **CE** | Conformité Européenne; indicates conformity with EU MDR. |
| **CFR** | Code of Federal Regulations. |
| **CISO** | Chief Information Security Officer. |
| **CPO/DPO** | Chief Privacy Officer / Data Protection Officer (Dr. Klaus Weber). |
| **EU MDR** | European Union Medical Device Regulation (EU) 2017/745. |
| **Filing Calendar** | The centralized register of all regulatory obligations, maintained in the ServiceNow GRC platform. |
| **GC** | General Counsel. |
| **GDPR** | General Data Protection Regulation (EU) 2016/679. |
| **HIPAA** | Health Insurance Portability and Accountability Act of 1996 and its implementing regulations. |
| **MRE** | Model Risk Exception; a formal, documented deviation from SR 11-7 standards logged in the Model Risk Exception Log. |
| **MRM** | Model Risk Management, the function governing HealthPay Financial Services models under SR 11-7. |
| **NIST AI RMF** | National Institute of Standards and Technology Artificial Intelligence Risk Management Framework 1.0. |
| **PHI** | Protected Health Information. |
| **PI** | Personal Information. |
| **PSP** | Periodic Safety Update; a post-market surveillance report required under EU MDR. |
| **RACI** | Responsible, Accountable, Consulted, Informed. A responsibility assignment matrix. |
| **RGPC** | Regulatory Governance & Policy Committee, the cross-functional body chaired by the CCO that provides strategic oversight for the compliance program. |
| **SI** | Serious Incident, as defined by Article 87 of EU MDR and Article 73 of the AI Act. An SI is any incident that directly or indirectly led, might have led, or might lead to death or a serious deterioration in health, or a serious disruption of critical infrastructure operations. |
| **SR 11-7** | Federal Reserve / OCC Supervisory Guidance on Model Risk Management, SR Letter 11-7 (April 4, 2011). Includes subsequent SR and OCC Bulletins that supplement the guidance. |
| **Sub-Regulatory** | Guidance, including the SR 11-7 Supervisory Letter, the OCC Comptroller’s Handbook on Model Risk Management, and relevant industry white papers recognized by examiners. |

## 3. Roles and Responsibilities

The following RACI matrix assigns responsibility and accountability for the regulatory filing lifecycle. The role of the Regulatory Filing Owner (RFO) is delegated based on the subject matter of the filing.

| Activity / Task | RFO | Dept. Reviewer (Legal/Compliance) | GC / CCO (as applicable) | CISO / CTO | Regulatory Operations Analyst | Regulatory Addressee |
| --- | --- | --- | --- | --- | --- | --- |
| Identification of Obligation & Filing Calendar Entry | R, A | C | I | I | R | — |
| Drafting of Regulatory Report | R | C | I | C | C | — |
| Technical & Accuracy Review | R | R | — | C | R | — |
| Legal Privilege & Confidentiality Review | C | R | A | — | R | — |
| Final Policy Approval (Pre-Submission) | I | R | A | I | R | — |
| Electronic Submission | — | I | I | — | R, A | I |
| Submission Receipt Confirmation & Archival | I | I | I | — | R, A | — |
| Post-Submission Inquiries & Follow-up | R, A | C | C | C | R | I |

### 3.1 Specific Role Definitions

| Role | Title / Owner | Responsibility Details |
| --- | --- | --- |
| **Regulatory Operations Analyst** | Senior Analyst, GRC Operations | Operates the Regulatory Filing Calendar; executes submission transmittals through approved portals (FDA eSubmitter, EUDAMED, state AG portals); manages the official Regulatory Filing Repository in iManage; tracks submission status from "Draft" to "Acknowledged by Regulator." |
| **Regulatory Filing Owner (RFO)** | Varies (e.g., VP of Clinical AI for MDR PSPs; VP of Model Risk for SR 11-7 attestations; Chief Privacy Officer for GDPR DPO reports) | Has primary subject-matter responsibility for the accuracy and completeness of the report. Drafts or oversees drafting of the narrative and data exhibits. Must be at Senior Director level or above. |
| **Model Risk Officer (MRO)** | Director, Model Risk Management | Specific RFO for all SR 11-7 related filings, including the annual Model Risk Management Report, quarterly model performance attestations, and model breach notifications. |
| **Data Protection Officer (DPO)** | Dr. Klaus Weber, CPO | RFO for GDPR-related submissions to EU/EEA Supervisory Authorities, including Records of Processing Activities (ROPA) summaries when requested by an SA and consultation notifications under Article 36. |
| **Security Incident Response Lead** | Deputy CISO | RFO for all security-incident related regulatory notifications under applicable state breach notification laws and the EU AI Act critical incident reporting obligations. |
| **General Counsel (GC)** | Maria Gonzalez | Provides final legal review on all matters of regulatory interpretation, legal privilege designation, and submissions that involve an admission of non-compliance or a formal resolution (e.g., Consent Order, Deferred Prosecution Agreement). The GC or her explicit delegate is the sole Approver for any such submission. |

## 4. Policy Statements

Meridian Health Technologies is committed to a philosophy of transparent and proactive engagement with its regulatory stakeholders. The following policy statements form the non-negotiable foundation of this SOP:

1.  **Zero-Tolerance for Late Filing:** Meridian does not tolerate intentional or negligent late filings. All submissions must be made by the regulatory deadline as defined in the Filing Calendar. Performance against statutory deadlines is a Board-level metric.
2.  **Single Version of Truth:** At any moment, only one version of a regulatory filing—the "Approved for Submission" version—exists in the Meridian systems. All prior drafts are maintained for audit trail purposes but are clearly marked as "Superseded." No off-system, ad hoc, or "shadow" filings are permitted.
3.  **Duty of Candor:** Meridian will engage with regulators honestly and with candor. No employee shall knowingly make a false, misleading, or incomplete statement in a regulatory filing. Where uncertainty exists, the filing shall clearly state the nature and limits of the uncertainty.
4.  **Materiality-Based Governance:** Filings that, by their nature, involve a material admission of a compliance gap, a significant safety signal, or a model performance breach must be personally approved in writing by the Chief Compliance Officer and the General Counsel before submission, following a briefing to the CEO. Routine, non-material filings may follow a streamlined review workflow as defined in Section 5.
5.  **Regulatory Inquiry Priority:** A formal inquiry, subpoena, or summons from a regulatory body receives the highest operational priority after an active threat-to-life safety incident. A preliminary response acknowledging receipt must be sent within 3 business days.
6.  **GDPR Compliance:** Meridian processes the personal data of EU residents in regulatory filings in accordance with GDPR principles, as detailed in the Meridian GDPR Compliance Policy (SOP-SECP-012). Data subjects are informed about processing activities through Meridian’s Privacy Notices posted on the corporate website. When personal data is transferred from the EU to Meridian’s US-based analytics teams for a regulatory submission, Meridian ensures appropriate safeguards are in place.
7.  **SR 11-7 Comprehensive Adherence:** Meridian’s HealthPay Financial Services division strictly adheres to the tenets of SR 11-7. All models, as defined by the SR 11-7 Model Risk Management framework, are subject to the full lifecycle governance described in this SOP and in the Meridian Model Risk Management Standard (SOP-MRM-001). Meridian defines a ‘model’ per the SR 11-7 guidance, which includes any quantitative method, system, or approach that applies statistical, economic, financial, or mathematical theories, techniques, and assumptions to process input data into quantitative estimates.

## 5. Detailed Procedures

### 5.1 Establishment and Maintenance of the Regulatory Filing Calendar

1.  **Annual Scoping (October-December):** The GRC Operations team, led by the Regulatory Operations Analyst, conducts an annual review of the regulatory landscape.
    *   **Input Sources:** The review considers new enabling legislation, published supervisory guidance (e.g., FRB, OCC, EDPB opinions), new product launches (e.g., a new AI/ML model component in HealthPay), geographic expansion plans, and feedback from the most recent regulatory examinations.
    *   **Stakeholder Engagement:** Operations meets with each RFO (MRO, CPO/DPO, Clinical Safety VP, CISO) to confirm all known obligations and surface any new ones.
    *   **Calendar Update:** The central Filing Calendar in the ServiceNow GRC module is updated with the next 18-month forecast. Each entry includes: `Obligation ID` (auto-generated), `Statutory Citation`, `Regulatory Addressee`, `Report Type`, `Due Date`, `Responsible Filing Owner`, `Materiality Flag` (Material / Routine), and `Submission Method`.

2.  **Ongoing Surveillance (Monthly):** At the start of each month, the Regulatory Operations Analyst generates an automated report from ServiceNow listing all filings due in the subsequent 90 days. This report is reviewed at the monthly RGPC meeting.

### 5.2 Report Drafting and Evidence Assembly

This procedure is initiated automatically by the ServiceNow GRC system 60 calendar days (or the appropriate timeframe based on report complexity, pre-defined in the Filing Calendar record) before the statutory due date.

1.  **Task Assignment:** The system creates a `Regulatory Filing Task` and assigns it to the designated RFO. A parallel task is created for the Data Governance team if the filing requires an attestation to the quality of the underlying data.

2.  **Template Selection:** The RFO selects the approved reporting template.
    *   For GDPR breach notifications, the template is in the ServiceNow Security Incident Response module.
    *   For SR 11-7 Quarterly Performance Attestations, a dynamic dashboard in the MRM Portal (built on Power BI) pre-populates quantitative metrics. The RFO reviews and annotates.
    *   For EU MDR Periodic Safety Update Reports (PSURs), the RFO uses the controlled template from the Quality Management System (QMS), MasterControl.

3.  **Evidence Package:** The RFO compiles an `Evidence Package`, which is a digitally signed zip archive or a linked folder in iManage containing all source data, validation reports, peer review notes, and audit trail logs that support the statements made in the filing. For SR 11-7 filings, this package must include:
    *   **Model Inventory Update:** The current Meridian enterprise model inventory, segmented by tier (Tier 1 – Most Critical; Tier 2 – Significant; Tier 3 – Advisory). Any movement between tiers since the last filing must be justified.
    *   **Validation Results Exhibit:** For all Tier 1 and Tier 2 models used in production, the exhibit includes a signed summary of the most recent independent validation. The summary must explicitly state the validator's (typically from the Independent Model Review Group, IMRG, under the CRO) opinion: “Findings Satisfactory,” “Findings Requiring Attention,” or “Findings Requiring Urgent Remediation.”
    *   **MRE Log Snapshot:** A point-in-time export of the Model Risk Exception Log, showing all open and closed exceptions, the remediation plan status, and the accountable party for each.

4.  **Draft Narrative:** The RFO authors the qualitative sections of the report, including the Management Discussion & Analysis (MD&A) for model performance, a narrative on model limitations, and responses to any previous regulatory findings.

### 5.3 Review and Approval Workflow

All filings follow a gated review workflow in the ServiceNow `Regulatory Document Management` (RDM) module. The workflow stages are conditional on the `Materiality` flag.

| Gate | Role | Action | Material Filing Requirement | Routine Filing Requirement |
| --- | --- | --- | --- | --- |
| **G1: Data Integrity** | Data Governance Owner | Reviews and attests to the accuracy of the underlying data and the robustness of the data pipeline. Signs the `G1: Data Attestation` form. | Mandatory | Mandatory |
| **G2: SME Technical Review** | Independent SME (from a line of business outside the RFO’s reporting chain) | Reviews the quantitative models, assumptions, and narrative for technical soundness. For SR 11-7, this is a senior quantitative analyst from outside HealthPay. | Mandatory | Mandatory, but may be peer-level. |
| **G3: Legal/Compliance Review** | Deputy GC or Senior Compliance Counsel | Reviews filing for legal privilege, interpretation of regulation, consistency with past filings, and overall defensibility. | Mandatory. Full memo to GC. | Recommended. Performed by Compliance Analyst. |
| **G4: C-Level Approver** | CCO or GC (See Section 4, Policy 4) | Final policy and legal approval. Approver has “reject” authority and can send the filing back to any prior gate. | Mandatory | N/A. RFO approval is sufficient. |
| **G5: Submission** | Regulatory Operations Analyst | Performs final formatting, packaging, and transmission through the mandated portal. | Mandatory | Mandatory |

**G4 Approval for Material Filings:** The G4 gate cannot be delegated. An automatic hold is placed on any Material filing if both the CCO and GC are out of the office; the filing must wait until at least one returns unless the GC has delegated in writing to a specific partner at external counsel for that specific filing.

### 5.4 Submission and Technical Transmission

1.  **Transmission Method:** Filings are submitted using the designated regulatory portal (e.g., FDA’s CFSAN/ORA portal, EUDAMED Actor Module, SEC EDGAR, state-specific AG Consumer Protection Portals). Under no circumstances is a filing to be submitted via standard unencrypted email without prior approval from the CISO and GC. The `Submission Method` field in the Filing Calendar specifies the approved channel.

2.  **Final Packaging:** The Regulatory Operations Analyst assembles the final package, which consists of a single consolidated PDF/A-compliant document and the Evidence Package as a separate, non-editable attachment (e.g., a digitally signed `.zip` archive).

3.  **Technical Submission:** The Analyst logs into the portal and executes the submission. A contemporaneous screen-recording of the submission process is created using the Meridian-approved screen-capture tool (Snagit/Verint) and attached to the Filing record in ServiceNow as `Proof of Submission`.

4.  **Confirmation:** The Analyst monitors the portal for any automated acknowledgments. If no acknowledgement is received within 24 hours for electronic portals, or 5 business days for mailed certified filings, the Analyst initiates a direct inquiry with the regulatory addressee’s general office.

### 5.5 Archival and Records Management

The definitive filing package (the “Record Copy”) is created immediately upon submission confirmation.

1.  **Metadata Tagging:** The package is checked into the Meridian iManage `RegulatoryFiling_Active` workspace. It must be tagged with the following required iManage metadata profiles:
    *   `Obligation ID` (from ServiceNow)
    *   `Regulator` (from controlled list)
    *   `Report_Type` (from controlled list)
    *   `Date_of_Submission`
    *   `Legal_Hold_Flag` (defaults to “No”)
2.  **Litigation Hold:** If the filing pertains to a matter for which a Legal Hold has been issued by the GC’s office, the `Legal_Hold_Flag` is set to “Yes.” The record is simultaneously copied to a mirrored, immutable WORM-storage compliance archive (AWS S3 Glacier Deep Archive with Compliance Locks) managed by IT under the direction of the CISO.

### 5.6 Management of Regulatory Inquiries and Examinations

1.  **Receipt and Triage:** Any communication from a regulator, other than mass-mailing newsletters, must be forwarded to `regulatoryaffairs@meridiantech.com` and the CCO’s office within 4 hours of receipt.

2.  **Acknowledgment:** The CCO or GC, depending on the nature of the inquiry, will determine the strategy. An initial acknowledgment of receipt is sent to the regulator within 3 business days. This acknowledgment commits to nothing more than Meridian’s willingness to engage and a proposed timeline for a substantive response.

3.  **Response Management:** A response lead (typically the relevant RFO) is assigned. All responses are tracked in a dedicated `Regulatory Inquiry` record in ServiceNow, and follow the G1-G5 approval workflow commensurate with the materiality of the response.

## 6. Controls and Safeguards

| Control ID | Control Description | Control Type | Mechanism | Frequency |
| --- | --- | --- | --- | --- |
| **C-01** | All filing events are tracked and enforced via a single, centralized Filing Calendar in ServiceNow GRC. No department-level shadow calendars are permitted. | Preventive / Administrative | ServiceNow automated workflow triggers task creation; shadow calendar detection via periodic audit. | Continuous / Quarterly Audit |
| **C-02** | The G4 (C-Level) approval gate is a hard, non-delegatable, technology-enforced workflow step for all Material (as defined) filings. | Preventive / Technical | ServiceNow RDM workflow configuration. Role-based access control (RBAC) prevents modification. | Continuous |
| **C-03** | The Regulatory Filing Repository (iManage) is a zero-deletion workspace. Edit access after the "Submitted" status is set is restricted to the system administrator (Director of IT GRC) and requires a formalized break-glass ticket. | Detective / Technical | iManage object-level permissions. Monthly “immutable zone” access log review by IT Security. | Continuous / Monthly Review |
| **C-04** | All quantitative data in SR 11-7 filings is sourced directly from the MRM Portal (Power BI), which reads from the certified Model Risk Data Mart. Manual extraction from spreadsheets is prohibited for Tier 1 & 2 model performance data. | Preventive / Technical | Data lineage and source control in Power BI and Snowflake. QA test case `T-04_v2` validates no manual file upload option exists. | Continuous |
| **C-05** | An independent Model Validation Group (IMRG), structurally separate from the model development and business lines, performs annual validations of all Tier 1 and Tier 2 models. This is a primary control to meet SR 11-7’s mandate for an “effective challenge” process. | Detective / Administrative | Audit of signed IMRG reports. IMRG Director reports functionally to the Chief Risk Officer, administratively to the Chairman of the Audit Committee. | Annual |
| **C-06** | All filings are subject to a formal “4-Eyes Review” at the G2 and G3 gates. The system enforces that the individual who sets the content (RFO) is distinct from the individual who conducts the technical review (G2). | Detective / Technical | ServiceNow workflow enforces distinct user ID requirement for G1 and G2 reviewers. | Continuous |
| **C-07** | The AI Incident Management System (AIMS) has a mandatory rules-based classifier. Any incident classified as a “Serious Incident” under EU MDR or AI Act criteria automatically triggers a high-priority notification task to the GC and CCO. | Detective / Technical | AIMS automated triage ruleset (Decision Table `DT-SI-01`). | Event-Driven |

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The following KPIs are used to measure the effectiveness of the regulatory filing process and are reported to the RGPC monthly and the Audit Committee quarterly.

| KPI ID | Metric | Target | SR 11-7 Specific Threshold |
| --- | --- | --- | --- |
| **T-01** | On-Time Filing Rate | ≥ 99.5% | For Tier 1 & 2 model reports: 100% on-time delivery is the only "Green" status. Any late filing is a Breach. |
| **T-02** | Mean Time to Resolve (MTTR) a Regulatory Inquiry | ≤ 5 Business Days for initial substantive response | N/A |
| **T-03** | Post-Submission Regulatory Finding Rate (e.g., a “matter requiring attention” letter) | < 2 per annum | Any MRM-related finding is automatically escalated to the Board Risk Committee. |
| **T-04** | Number of Material Filing Submission Errors (e.g., incorrect portal used, corrupted file) | Zero | Zero. Any error triggers a Root Cause Analysis (RCA) and a mandatory process walkthrough for the Operations team. |
| **T-05** | Model Risk Exception (MRE) Aging | No Critical or High MRE open > 90 days | Any Tier 1 model MRE open for more than 60 consecutive calendar days is an automatic escalation to the CRO and CCO. |
| **T-06** | IMRG Validation Cycle On-Time Completion Rate | ≥ 95% completed within 15 business days of scheduled finish date. | For Tier 1 models: 100%. |

### 7.2 Reporting Cadence

| Report | Audience | Frequency | Owner |
| --- | --- | --- | --- |
| **Regulatory Filing Dashboard** | RGPC (all members) | Live, reviewed Monthly | Director, GRC Operations |
| **Quarterly Compliance Scorecard** | CCO, GC, CEO | Quarterly | Chief Compliance Officer |
| **Annual MRM Report to Board** | Board of Directors, Audit & Risk Committee | Annually | Chief Risk Officer |

### 7.3 SR 11-7 Specific Monitoring

*   **Model Performance Monitoring (MPM):** The MPM dashboard in the MRM Portal provides a near-real-time view of model predictive accuracy, stability, and drift for all deployed Tier 1 and Tier 2 models. Threshold alerts are configured for model performance degradation, backtesting exceptions, and benchmark deviations, as per Appendix A of SOP-MRM-001.
*   **Findings Tracking:** All findings from internal audits, independent model validations (IMRG), and regulatory examinations are tracked in a centralized `Findings and Remediation` module in ServiceNow. The system uses red-amber-green (RAG) status indicators based on the remediation plan’s milestone due dates.

## 8. Exception Handling and Escalation

### 8.1 Requesting a Filing Extension

1.  **Identification and Trigger:** The RFO must initiate an extension request the moment they reasonably foresee that a filing will miss its internal or regulatory deadline. Late identification is itself a non-compliance event.

2.  **Formal Request Process:** The RFO creates a `Regulatory Exception Request` record in ServiceNow, linked to the original `Filing Obligation` record. The request must include:
    *   A clear, documented root cause for the potential delay.
    *   A detailed, date-certain remediation plan with a new proposed filing date.
    *   An impact assessment detailing the risks of filing late (e.g., statutory penalties, reputational damage).
    *   Draft communication for the regulator if a proactive request for an extension is the proposed strategy.

3.  **Approval Authority:**
    *   A proposed internal filing date slippage of 1-5 business days that does *not* breach a statutory deadline may be approved by the CCO.
    *   Any request that seeks to breach a statutory deadline, or any internal slippage of more than 5 business days, must be approved jointly by the CCO and the General Counsel. The GC will lead the direct engagement with the regulator.

### 8.2 SR 11-7 Specific Escalation (Model Risk Exception)

An MRE is a formal deviation from the standards defined in SOP-MRM-001. Its lifecycle is as follows:

1.  **Logging:** The Model Risk Officer (MRO) or the IMRG lead logs a new MRE in the `Model Risk Exception Log` (a module in ServiceNow) within 1 business day of identification.
2.  **Risk Rating:** The MRO assigns a preliminary risk rating (Critical, High, Medium, Low) based on the model’s Tier and the nature of the deviation.
3.  **Immediate Notification:** A Critical MRE triggers an immediate push notification to the Chief Risk Officer, Chief Compliance Officer, and VP of HealthPay Engineering. A High MRE triggers notification within 4 hours.
4.  **Escalation Matrix:**
    *   **Critical MRE:** Remediation must begin in 24 hours. A briefing must be scheduled for the RGPC within 5 business days. If the MRE is not closed in 60 days, it is automatically escalated to the Board Audit & Risk Committee.
    *   **High MRE:** Remediation plan due in 5 business days. Closed in 90 days.

### 8.3 Whistleblower and Confidential Reporting

Meridian maintains a 24/7 confidential Ethics and Compliance Helpline, operated by an independent third-party provider. All reports are tracked to resolution. Retaliation against any individual who makes a good-faith report of a potential regulatory filing irregularity is a violation of the Meridian Code of Conduct and this SOP.

## 9. Training Requirements

| Training Module | Audience | Frequency | Delivery Method | Owner |
| --- | --- | --- | --- | --- |
| **MGT-110: Regulatory Filing & Reporting Essentials** | All employees with access to systems that generate reportable data. | Once, within 30 days of hire. Renew every 24 months. | LMS (Workday Learning) | Compliance Training Manager |
| **MGT-210: Advanced Regulatory Filing and SR 11-7 Governance** | All RFOs, IMRG staff, HealthPay quantitative analysts, Legal & Compliance staff, and GRC Operations analysts. | Annually | Live, instructor-led workshop with case studies. | Chief Compliance Officer, MRO |
| **MGT-310: Duty of Candor and Interactions with Regulators** | C-Level, SVPs, VPs, and any employee with the authority to sign a filing. | Annually | Interactive legal session led by the GC or external counsel. | General Counsel |

Training completion is tracked within Workday. Access to the Regulatory Filing module in ServiceNow is automatically revoked for any individual whose required training is past due by more than 60 days.

## 10. Related Policies and References

| Document ID | Document Title |
| --- | --- |
| `SOP-MRM-001` | Meridian Model Risk Management Standard (HealthPay) |
| `SOP-LEGC-001` | Corporate Code of Conduct and Business Ethics |
| `SOP-SECP-012` | Meridian GDPR Compliance Policy |
| `SOP-DRM-003` | Records and Information Management Policy |
| `SOP-SECP-009` | Data Classification and Handling Standard |
| `POL-EXEC-001` | Board Risk Committee Charter |
| `TMP-QMS-042` | Post-Market Surveillance Reporting Template (EU MDR) |
| `TMP-LEGC-005-A1` | SR 11-7 Quarterly Performance Attestation Template |
| `TMP-LEGC-005-A2` | Material Filing Approval Memo Template |
| `TMP-LEGC-005-A3` | Model Risk Exception Log Entry Form |
| `External-Ref-SR-11-7` | Federal Reserve / OCC Supervisory Guidance on Model Risk Management |
| `External-Ref-EU-MDR` | Regulation (EU) 2017/745 on medical devices |
| `External-Ref-EU-AI-Act` | Regulation (EU) 2024/1689 on artificial intelligence |

## 11. Revision History

| Version | Date | Author(s) | Description of Changes |
| --- | --- | --- | --- |
| 5.6 | 2026-05-18 | Thomas Anderson, CCO | Full biennial review. Updated scope for new AI Act reporting obligations. Added C-07 control. Minor template updates. |
| 5.5 | 2025-11-10 | Maria Gonzalez, GC | Revised Section 5.3 G4 workflow for Material filings to resolve delegation ambiguity during officer travel. Clarified Legal Hold procedure. |
| 5.4 | 2025-04-16 | Thomas Anderson, CCO; Dr. Klaus Weber, CPO | Updated GDPR sections for EDPB guidance on incident thresholds. New GDPR report templates versioned. |
| 5.3 | 2024-09-01 | Jane Smith, Director of GRC | Refined model risk escalation matrix (Section 8.2) following Q3 internal audit finding. Aligned KPIs with new CRO dashboard. |
| 5.2 | 2024-03-22 | John Doe, Senior Regulatory Counsel | Annual review. Streamlined G2 review for routine filings. Added definitions for new state-level Breach Notification thresholds. |
---
sop_id: "SOP-LEGC-013"
title: "Compliance Monitoring and Testing"
business_unit: "Legal & Compliance"
version: "2.1"
effective_date: "2025-12-20"
last_reviewed: "2026-04-24"
next_review: "2026-10-18"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
  - "GDPR"
  - "SR 11-7"
status: "Active"
---

# Standard Operating Procedure: Compliance Monitoring and Testing

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework for continuous compliance monitoring and independent testing of controls across Meridian Health Technologies, Inc. ("Meridian" or "the Company"). The purpose is to ensure that operational, technical, and administrative controls are not only designed appropriately but are operating effectively to maintain ongoing conformance with applicable laws, regulations, contractual obligations, and internal policy commitments. This SOP provides the mechanism to identify control weaknesses proactively, initiate corrective actions, and verify remediation before failures result in regulatory action, financial penalty, or reputational harm.

This SOP operationalizes the Company's commitment to the monitoring and measurement principles found in ISO 27001:2022 Clause 9.1 and the HIPAA Security Rule requirements for ongoing evaluation of security controls.

### 1.2 Scope

This SOP applies to the following entities, systems, and data environments:

**In-Scope Entities:**
- Meridian Health Technologies, Inc. (corporate headquarters, Boston, MA)
- All global offices (London, Berlin, Singapore, Toronto)
- All employees, contractors, temporary workers, and third-party personnel with access to Meridian systems, networks, or data

**In-Scope Systems and Business Lines:**
- Clinical AI Platform (deployed across 340+ hospital and clinic environments)
- HealthPay Financial Services platform and associated payment processing infrastructure
- MedInsight Analytics platform and associated data processing pipelines
- Meridian SaaS Platform (AWS us-east-1 and eu-west-1 environments)
- Azure Disaster Recovery environment
- All internal corporate systems, development environments, and data repositories

**In-Scope Data:**
- Protected Health Information (PHI) as defined by HIPAA
- Personal data of EU data subjects as defined by GDPR Article 4(1)
- Payment card and financial transaction data
- Proprietary algorithms, model weights, and training data
- Employee personally identifiable information (PII)

**In-Scope Regulatory Obligations:**
- HIPAA Privacy, Security, and Breach Notification Rules
- GDPR (all articles applicable to data controller and processor operations)
- EU AI Act (for Clinical AI Platform classified as high-risk AI systems under Annex III)
- SOC 2 Type II Trust Services Criteria (Security, Availability, Confidentiality)
- HITRUST CSF control maturity requirements
- ISO 27001:2022 Annex A controls
- FDA Quality System Regulation (for 510(k)-cleared diagnostic imaging AI)
- EU Medical Device Regulation 2017/745 (for CE-marked clinical AI products)
- SR 11-7 model risk management guidance (HealthPay Financial Services)
- PCI DSS v4.0 (HealthPay payment processing)

**Out-of-Scope:**
- Personal devices not enrolled in Meridian Mobile Device Management (MDM)
- Third-party systems not integrated with Meridian data pipelines
- Legacy systems formally decommissioned and documented in the Configuration Management Database (CMDB)

### 1.3 Applicability

All Meridian personnel, regardless of employment classification or geographic location, are subject to the monitoring activities described in this SOP. Refusal to cooperate with compliance monitoring activities, obstruction of testing procedures, or failure to respond to control evidence requests within defined timelines constitutes a violation of Meridian's Code of Conduct and may result in disciplinary action up to and including termination of employment or contract.

---

## 2. Definitions and Acronyms

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Compliance Monitoring** | Ongoing, automated or manual observation of control operations to identify deviations from expected performance or conformance in near real-time. Monitoring is continuous and operational. |
| **Compliance Testing** | Periodic, point-in-time evaluation of control design and operating effectiveness conducted by independent assessors. Testing is discrete and verifiable. |
| **Control** | A policy, procedure, technical mechanism, or administrative action designed to reduce risk, ensure conformance, or achieve a compliance objective. Controls may be preventive, detective, or corrective. |
| **Control Deficiency** | A condition where a control is not designed appropriately or is not operating as intended, resulting in a failure to achieve the control objective. |
| **Significant Deficiency** | A deficiency, or combination of deficiencies, that results in a reasonable possibility that a material nonconformance with a regulatory obligation will not be prevented, detected, or corrected in a timely manner. |
| **Material Weakness** | A deficiency, or combination of significant deficiencies, such that there is a more than remote likelihood that a material nonconformance will not be prevented, detected, or corrected. |
| **Finding** | A documented determination from compliance testing that identifies a control deficiency, significant deficiency, or material weakness. |
| **Remediation** | The corrective action taken to resolve a finding and restore control effectiveness. |
| **Remediation Verification** | The independent re-testing of a remediated control to confirm the corrective action was effective. |
| **Monitoring Plan** | The documented schedule of monitoring activities, key indicators, data sources, frequency, and responsible parties for a given compliance domain. |
| **Control Owner** | The individual with operational responsibility for the design, implementation, and ongoing maintenance of a specific control. |
| **Processing Activity** | Any operation or set of operations performed on personal data, as defined by GDPR Article 4(2), including collection, recording, organization, structuring, storage, adaptation, retrieval, consultation, use, disclosure, restriction, erasure, or destruction. |
| **Data Subject Request (DSR)** | A formal request from an individual exercising their rights under GDPR Articles 15-22 or HIPAA 45 CFR §164.524-164.526. |

### 2.2 Acronyms

| Acronym | Definition |
|---|---|
| **CCO** | Chief Compliance Officer |
| **CISO** | Chief Information Security Officer |
| **DPO** | Data Protection Officer |
| **GC** | General Counsel |
| **HIPAA** | Health Insurance Portability and Accountability Act of 1996 |
| **HITECH** | Health Information Technology for Economic and Clinical Health Act |
| **GDPR** | General Data Protection Regulation (EU 2016/679) |
| **PHI** | Protected Health Information |
| **PII** | Personally Identifiable Information |
| **ePHI** | Electronic Protected Health Information |
| **CE** | Covered Entity (as defined by HIPAA) |
| **BA** | Business Associate (as defined by HIPAA) |
| **DPA** | Data Processing Agreement (as required by GDPR Article 28) |
| **DPIA** | Data Protection Impact Assessment (as required by GDPR Article 35) |
| **DSAR** | Data Subject Access Request |
| **BAA** | Business Associate Agreement |
| **NIST** | National Institute of Standards and Technology |
| **GRC** | Governance, Risk, and Compliance (refers to Meridian's OneTrust GRC platform) |
| **SIEM** | Security Information and Event Management (Refers to Meridian's Splunk Enterprise Security deployment) |
| **CMDB** | Configuration Management Database |
| **KPI** | Key Performance Indicator |
| **KRI** | Key Risk Indicator |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix (RACI)

The following matrix defines the roles and responsibilities for activities governed by this SOP. Roles are designated as Responsible (R), Accountable (A), Consulted (C), or Informed (I).

| Activity / Deliverable | Chief Compliance Officer | General Counsel | DPO | CISO | Control Owners | Internal Audit | Business Unit Leads |
|---|---|---|---|---|---|---|---|
| **Compliance Monitoring Plan Development** | A | C | R (GDPR/Privacy) | R (Security Controls) | C | C | C |
| **Day-to-Day Compliance Monitoring Operations** | A | I | R (Privacy Monitoring) | R (Security Monitoring) | R (Domain-Specific) | I | I |
| **Independent Compliance Testing Execution** | A (Overall) | I | R (GDPR Testing) | R (Security Testing) | C | R (Independent Testing) | C |
| **Control Deficiency Identification** | A | C | R | R | I | R | I |
| **Finding Severity Classification** | A | C | C | C | I | R | I |
| **Remediation Plan Development** | A | I | C | C | R | C | C |
| **Remediation Verification** | A | C | I | I | I | R | I |
| **Compliance Reporting** | A (Overall) | R (Legal Reports) | R (DPO Reports) | R (Security Reports) | I | C | I |
| **Exception Approval (Low Risk)** | A | I | C | C | I | I | I |
| **Exception Approval (Medium/High Risk)** | C | A | C | C | I | I | I |

### 3.2 Key Role Descriptions

**Chief Compliance Officer (Thomas Anderson) — SOP Owner:**
The CCO is the executive accountable for the overall effectiveness of the Compliance Monitoring and Testing program. The CCO approves the annual Compliance Monitoring Plan, reviews aggregated compliance metrics monthly, and has the authority to mandate corrective action for any business unit. The CCO briefs the Meridian Board of Directors' Audit Committee on compliance posture quarterly.

**General Counsel (Maria Gonzalez) — SOP Approver:**
The General Counsel provides legal oversight of the compliance monitoring framework, ensures attorney-client privilege protections are maintained over sensitive compliance investigations (where applicable under the direction of outside counsel), approves high-risk exceptions, and is the primary legal point of contact for regulatory inquiries arising from monitoring findings.

**Data Protection Officer (Dr. Anya Sharma, DPO):**
The DPO, a role mandated by GDPR Article 37, is responsible for the execution of all privacy compliance monitoring and testing activities, including: monitoring adherence to data protection principles (GDPR Article 5), monitoring of Data Protection Impact Assessment (DPIA) triggers (GDPR Article 35), monitoring data subject request response times (GDPR Articles 15-22), and the monitoring of personal data breach notification timelines (GDPR Articles 33-34). The DPO reports directly to the highest management level per GDPR Article 38(3) and operates with independence. Any monitoring finding that indicates a risk to the rights and freedoms of data subjects is escalated directly by the DPO to the CCO and GC immediately.

**Chief Information Security Officer (Elena Rossi, CISO):**
The CISO is responsible for operational security controls subject to compliance monitoring. The CISO's team operates the SIEM (Splunk), endpoint detection, identity and access management logging, and all infrastructure telemetry that feeds automated compliance monitoring dashboards. The CISO is accountable for the timely remediation of security control findings.

**Control Owners:**
Control Owners are named individuals assigned to each discrete control in Meridian's GRC platform (OneTrust). They are responsible for maintaining control documentation, operating the control as defined, providing requested evidence during testing windows (within 5 business days of a request), and executing remediation plans when deficiencies are identified.

**Internal Audit:**
Internal Audit executes independent compliance testing on an agreed schedule. Internal Audit maintains organizational independence and reports functionally to the Audit Committee Chair with an administrative reporting line to the CFO. Testing methodologies, sampling rationales, and workpapers are maintained in accordance with the Institute of Internal Auditors (IIA) Standards.

---

## 4. Policy Statements

### 4.1 Foundational Compliance Principles

**Commitment to Continuous Conformance:**
Meridian does not view compliance as a point-in-time achievement (e.g., achieving a SOC 2 report or completing an annual HIPAA Security Risk Assessment). Rather, compliance is a continuous state maintained through persistent monitoring, regular independent testing, rapid remediation, and a closed-loop corrective action process. All Meridian systems processing regulatory-scoped data shall have active, documented monitoring controls.

**Risk-Based Monitoring and Testing:**
Monitoring frequency and testing intensity are calibrated based on a risk-tiering methodology. Controls mitigating higher inherent risk and controls that have previously exhibited deficiencies are subject to more frequent and more intrusive testing. Low-risk, stable controls may be on an extended testing cycle, but no control shall go untested beyond a 24-month period.

**Presumption of Testing:**
All controls documented in Meridian's control framework are presumed to be testable unless formally exempted and designated as "Governance Only" by the CCO. Testable controls must have measurable attributes, defined populations, and testable frequency.

**Independence of Testing:**
Testing of control operating effectiveness must be performed by individuals who are independent of the control design and operation. For privacy controls, this independence extends to ensuring the DPO is not directed on testing methodology, as per GDPR Article 38(3).

**Zero Tolerance for Intentional Non-Compliance:**
Intentional circumvention of controls documented in this framework, deliberate falsification of control evidence, or deliberate obstruction of compliance testing shall be treated as a severe misconduct issue and referred to the General Counsel and Chief Human Resources Officer.

### 4.2 Specific Regulatory Policy Commitments

**HIPAA Privacy Rule (45 CFR Part 160 and Subparts A and E of Part 164):**
Meridian commits to ongoing monitoring of its adherence to the Permitted Uses and Disclosures framework. Specifically, Meridian monitors that any disclosure of PHI not expressly permitted by 45 CFR §164.502 is accompanied by a valid, HIPAA-compliant authorization as defined in §164.508. The validity and expiration of authorizations on file are subject to automated monitoring. The Minimum Necessary Standard (§164.502(b), §164.514(d)) is operationalized through role-based access controls that are subject to user access recertification testing on a quarterly basis, ensuring that only workforce members with a defined "need to know" retain access to PHI.

**HIPAA Security Rule (45 CFR Part 160 and Subpart C of Part 164):**
Meridian commits to the ongoing evaluation of the technical, physical, and administrative safeguards required by §164.312, §164.310, and §164.308 respectively. Monitoring is designed to provide reasonable assurance that the confidentiality, integrity, and availability (the "CIA Triad" as articulated in §164.306(a)(1)) of all ePHI created, received, maintained, or transmitted by Meridian is being protected against reasonably anticipated threats or hazards.

**HIPAA Breach Notification Rule (45 CFR Part 164 Subpart D):**
Meridian monitors its incident response lifecycle to ensure that any breach of unsecured PHI, as defined in §164.402, triggers the required risk assessment under §164.404(c). The timeliness of notifications to individuals (§164.404), the Secretary of HHS (§164.408), and the media where applicable (§164.406) is a Key Performance Indicator tracked on a real-time dashboard.

**GDPR Data Protection Principles (Article 5):**
Compliance with the seven foundational principles—lawfulness, fairness, and transparency (5(1)(a)); purpose limitation (5(1)(b)); data minimization (5(1)(c)); accuracy (5(1)(d)); storage limitation (5(1)(e)); integrity and confidentiality (5(1)(f)); and accountability (5(2))—is actively monitored. Each principle maps to specific, measurable administrative and technical controls within the GRC platform.

**GDPR Data Subject Rights (Articles 15-22):**
Meridian treats the timely, complete, and accurate fulfillment of Data Subject Access Requests (DSARs), rectification requests, erasure requests ("Right to be Forgotten"), restriction of processing requests, data portability requests, and objection requests as a critical compliance metric. Automated case management tracking ensures the one-month statutory deadline (Article 12(3)) is never breached.

**GDPR Controller and Processor Obligations (Articles 24, 28, 32):**
Meridian monitors its adherence to its documented Technical and Organizational Measures (TOMs) as required by Article 32. The existence and legal validity of Article 28 Data Processing Agreements (DPAs) with all sub-processors are monitored for completeness and currency.

---

## 5. Detailed Procedures

### 5.1 The Annual Compliance Monitoring Plan (CMP)

The Compliance Monitoring Plan (CMP) is the foundational procedural document that translates policy commitments into a scheduled, measurable operational program.

#### 5.1.1 CMP Development Procedure

**Timing:** The CMP for the upcoming fiscal year shall be drafted during Q4 of the current fiscal year and finalized no later than December 15th. For FY2026, the draft is due October 1, 2026, with final approval by December 15, 2026.

**Procedure Steps:**
1.  **Regulatory Change Impact Assessment:** The Legal & Compliance Regulatory Intelligence team (part of the GC's office) publishes a "Regulatory Outlook" memorandum by October 1. This memo identifies all enacted, amended, or newly applicable regulations and contractual obligations for the upcoming year that modify control requirements. This includes new EU Implementing Acts, updated HHS OCR guidance, and revised HITRUST CSF mappings.
2.  **Inherent Risk Re-Assessment:** Each Control Owner, facilitated by the GRC team, re-assesses the inherent risk of their control portfolio before considering control effectiveness. Risk is assessed on a standard 5x5 matrix (Likelihood x Impact). Controls addressing risks rated "High" or "Critical" are automatically scheduled for high-frequency monitoring (monthly or continuous) and semi-annual independent testing.
3.  **Prior Year Findings Review:** All open and closed findings from the prior fiscal year are analyzed. Controls that resulted in a "Significant Deficiency" or "Material Weakness" finding in the prior year are automatically designated for continuous monitoring and must undergo remediation verification testing within the first quarter of the new fiscal year, regardless of other scheduling.
4.  **Resource Allocation:** The CCO, DPO, CISO, and Internal Audit lead jointly determine the resource capacity for the upcoming year (staff hours, automated tool licenses, external assessor budget).
5.  **Draft CMP Assembly:** The GRC Manager compiles the regulatory inventory, risk-tiered control list, prior-year findings priority, and resource constraints into a Draft CMP. The CMP details for each in-scope control:
    - Control ID (from OneTrust)
    - Control Description
    - Control Owner
    - Monitoring Method (Automated SIEM Alert, Manual Evidence Review, Attestation Questionnaire)
    - Monitoring Frequency (Continuous, Daily, Weekly, Monthly, Quarterly)
    - Independent Testing Frequency (Monthly, Quarterly, Semi-Annually, Annually, Biennially)
    - Testing Methodology (Inquiry, Observation, Inspection, Re-performance)
    - Sample Size Rationale (per Section 5.4)
6.  **Stakeholder Review and Approval:** The Draft CMP is circulated for a 14-day review period to all Control Owners, Business Unit Leads, the DPO, and the CISO. Comments are adjudicated by the CCO. The final CMP is approved by the CCO and General Counsel jointly. The approved CMP is uploaded to OneTrust as the master schedule for the year.

### 5.2 Compliance Monitoring Operations

Compliance monitoring is the continuous, day-to-day operation of observing control outputs. It is distinct from point-in-time testing.

#### 5.2.1 Automated Technical Monitoring

Meridian's SIEM (Splunk Enterprise Security) serves as the primary aggregation point for automated security control monitoring. The following correlation rules, dashboards, and alerts are established and maintained by the CISO's Security Operations Center (SOC). Any degradation of telemetry sources feeding these rules is a Severity 1 incident for the SOC.

| Control Objective | Monitoring Mechanism | Alert Trigger Threshold |
|---|---|---|
| **HIPAA Access Control (§164.312(a)(1))** | Splunk correlation rule analyzing Active Directory authentication logs against an authorized user/role matrix. Rule triggers on any account granted access to an ePHI-bearing system outside of established role-based provisioning groups. | Trigger within 5 minutes of anomalous permission grant. SOC Analyst must investigate and confirm/clear within 60 minutes. |
| **HIPAA Audit Controls (§164.312(b))** | Splunk dashboard tracking health and event ingestion rate of all audit log sources from ePHI systems (EHR integrations, MedInsight platform, data warehouses). Alert triggers if a critical log source ceases sending events. | Trigger immediately upon "Log Source Down" status. SOC must restore log flow within 4 hours. A "Log Gap" finding is automatically recorded in the GRC system. |
| **HIPAA Person or Entity Authentication (§164.312(d))** | Continuous monitoring of Multi-Factor Authentication (MFA) enforcement posture via Duo Security admin API. Alert triggers if any user account with access to ePHI is exempted from the mandatory MFA policy without a documented, time-bound exception. | Trigger within 30 minutes. SOC reports open MFA exemptions to CISO and DPO immediately. |
| **GDPR Article 32 Security of Processing** | Integrated vulnerability scanner (Qualys) feeds data to Splunk. Dashboard tracks critical-risk vulnerabilities (CVSS v3.1 score >= 9.0) unpatched on any in-scope production asset. | Critical vulnerability unpatched > 48 hours after patch availability triggers an alert to the CISO and DPO. |
| **Data Lifecycle — Storage Limitation (GDPR Art. 5(1)(e))** | Splunk query runs weekly against data repository metadata, flagging any data set classified as "Personal Data" or "PHI" that exceeds the documented retention period in the Data Retention Schedule (SOP-DATA-004) by more than 30 days. | Weekly report generated and sent to Data Governance Lead and DPO. Data exceeding retention by >30 days becomes a Finding with automated ticket creation in Jira (remediation project). |

#### 5.2.2 Manual Procedural Monitoring

Not all controls are amenable to automated telemetry. For procedural controls, the GRC team executes a defined cadence of manual evidence requests and attestation collection.

**HIPAA Privacy Rule — Notice of Privacy Practices (NPP) Monitoring (§164.520):**
- **Control:** Meridian must maintain a compliant NPP and provide it to individuals at the first service delivery.
- **Monitoring Procedure (Quarterly):** The GRC Compliance Analyst requests a report from the Customer Onboarding System (Salesforce) listing all new Covered Entity clients onboarded in the quarter. A random sample of 25 client records is drawn. For each, the Analyst verifies that (a) a dated acknowledgment of receipt of Meridian's NPP is on file in the contract package, and (b) a copy of the NPP current at the time of onboarding is attached. If the NPP is embedded in an online portal, the Analyst verifies the acknowledgment timestamp. **Failure rate > 0% on this control results in an automatic Finding.**

**GDPR Data Subject Access Request (DSAR) Handling (Articles 15, 12(3)):**
- **Control:** DSARs must be fulfilled without undue delay and at the latest within one month of receipt.
- **Monitoring Procedure (Monthly):** The DPO queries the DSAR case management system (DataGrail) for all requests logged in the preceding calendar month. The following metrics are extracted for each request: Date of Receipt, Date of Identity Verification (if required), Date of Complex Request Extension Notification (Art. 12(3)), and Date of Final Fulfillment. Any request where the "Calendar Days from Verified Receipt to Fulfillment" exceeds 28 days triggers an immediate alert to the DPO and the assigned case analyst's manager, as it represents a near-miss of the statutory deadline. A status report is submitted to the CCO monthly.

### 5.3 Independent Compliance Testing

Independent testing provides a point-in-time, evidence-based assessment of whether a control existed (design) and operated effectively (operating effectiveness) over a defined review period. Internal Audit leads independent testing, but the CCO may commission supplemental testing by external Qualified Security Assessors (QSAs) or legal counsel directed under privilege for sensitive HIPAA/GDPR investigations.

#### 5.3.1 Testing Execution Procedure

**Step 1: Pre-Testing Notification and Evidence Collection Requests**
- **Timing:** Control Owners receive a formal "Testing Notification and Evidence Request" (TNER) memo via OneTrust at least 15 business days before the planned fieldwork start date for their control.
- **Contents of TNER:** The memo specifies: (a) Control ID and description being tested; (b) Defined review period for operating effectiveness testing (e.g., "All instances of the control operation between 2026-01-01 and 2026-06-30"); (c) The specific evidence required (e.g., "Screenshots of completed access review attestations for the Q1 and Q2 2026 review cycles"; "System-generated log extracts showing privileged account usage for the review period"); (d) The Evidence Submission Deadline (no later than 5 business days before fieldwork start).

**Step 2: Evidence Receipt and Control Population Determination**
- Upon receiving evidence, the Auditor (Internal Audit) first confirms the "completeness" of the population. If a control is supposed to operate for every instance of a transaction (e.g., every new vendor setup), the Auditor requests a total population listing from the system of record.
- **Example (HIPAA):** For the control "BAAs are executed before PHI is disclosed to a Business Associate" (§164.308(b)(1)), the Auditor requests a complete list of all active third parties classified as Business Associates from the OneTrust Third-Party Management module. This is the population—the entire list.

**Step 3: Sampling**
- The Auditor selects a sample from the identified population for detailed testing using the methodology defined in Section 5.4. The sample is randomly generated using a seed value documented in the audit workpaper.

**Step 4: Control Attribute Testing (Inspection/Re-performance)**
- The Auditor evaluates each sampled item against the defined control attributes.
- **Testing Workpaper Documentation:** For each item, the Auditor records: Item Identifier (e.g., Contract ID), date of review, attributes tested, test result (Pass/Fail), and a hyperlink to the retained screen capture or document copy. Any "Fail" result MUST include an explanation of the deviation and an initial severity assessment.

**Step 5: Findings Drafting**
- For any failed attribute test, a draft Finding is generated in OneTrust within 3 business days of the failure identification. The draft Finding includes: a clear statement of the condition (what was observed), the criteria (what the policy/regulation requires), the cause (preliminary root cause), and the consequence (the potential impact of the control failure). The finding severity is provisionally scored using the matrix in Section 5.3.2.

**Step 6: Control Owner Validation and Management Response**
- The Draft Finding is routed to the Control Owner. The Control Owner has 10 business days to review the finding for factual accuracy and provide a formal "Management Response" that includes: (a) concurrence or non-concurrence with the finding (with evidence for non-concurrence); (b) a root cause analysis; (c) a proposed Remediation Plan, including specific corrective actions and a target completion date.

**Step 7: Final Report Issuance**
- The Auditor finalizes the workpaper, incorporates the Management Response, and issues a final testing report. The report is distributed to the Control Owner, their management chain, the CISO, the DPO, and the CCO.

#### 5.3.2 Finding Severity Classification

The following matrix is used to classify all compliance findings.

| Severity | Definition | Escalation Requirement | SLAs (from Report Issuance) |
|---|---|---|---|
| **Critical** | An active, ongoing violation of law or regulation (e.g., uncontained breach of unsecured PHI not yet reported; systematic processing of EU personal data under an invalid legal basis). Immediate cessation of processing may be required. | Immediate notification to CCO, GC, DPO, and relevant external counsel for privilege. CEO notified within 4 hours. | Remediation Plan due within 2 business days. Interim compensating control due within 5 business days. Permanent remediation target date must be <30 calendar days. |
| **High (Material Weakness)** | A deficiency or aggregation of deficiencies such that there is a more than remote likelihood a material nonconformance will not be prevented, detected, or corrected. (e.g., Access recertification for PHI repositories has not been performed for 6+ months; No DPIA for a new high-risk AI processing activity as required by Art. 35 GDPR). | CCO, GC, CISO, DPO notified within 24 hours. Included in quarterly Audit Committee deck. | Remediation Plan due within 10 business days. Permanent remediation target date must be <90 calendar days. Monthly progress reports required. |
| **Medium (Significant Deficiency)** | A deficiency in design or operation that is less severe than a material weakness, yet important enough to merit attention. (e.g., BAA executed but missing a required clause from §164.504(e); DSAR fulfilled within deadline but one data source not queried, leading to incomplete response). | Control Owner's Director and relevant Compliance Officer notified within 1 week. | Remediation Plan due within 30 calendar days. Permanent remediation target date must be <180 calendar days. |
| **Low (Minor Deficiency)** | An isolated, non-systemic deviation from policy or procedure that does not directly result in a regulatory non-compliance risk. (e.g., Single evidence file for a quarterly control was inadvertently not saved before the record cutoff; control operation was confirmed through secondary attestation). | Control Owner notified. | Remediation Plan due within 60 calendar days. Permanent remediation target date must be <12 months. |

### 5.4 Sampling Methodology

The integrity of the testing program relies on statistically defensible sampling. For manual testing of transactional populations, Meridian adopts the attribute sampling guidance from the AICPA Audit Guide.

The default sampling parameters for a "Medium" risk control, unless otherwise justified and documented in the annual CMP, are:
- **Confidence Level:** 95%
- **Tolerable Deviation Rate (Upper Precision Limit):** 5%
- **Expected Population Deviation Rate:** 0.5%

Based on a standard population-size-adjusted attribute sampling table, the default sample size for a large population (>500 items) is **93 items**.

**Procedure for Sampling Rationalization:**
1.  If a Control Owner believes a smaller sample size is appropriate (e.g., for a very low-frequency manual control that operates only 10 times per year), the full population (10 items) is tested.
2.  If an Auditor believes a larger sample is required (e.g., for a "High" risk control), the sample size is adjusted, typically to 150 items, with a corresponding lowering of the tolerable deviation rate.
3.  The approved sample size rationale for each control is documented directly in the Annual CMP.

**Deviation Evaluation:**
- If zero deviations are found in the tested sample, the auditor concludes the control is operating effectively over the review period at the stated confidence level.
- If one or more deviations are found, the auditor calculates the upper deviation rate. If the upper deviation rate exceeds the tolerable deviation rate, the control is deemed **NOT OPERATING EFFECTIVELY**, and a Finding is automatically generated.

### 5.5 Remediation Verification Procedure

Remediation Verification is the critical "closing the loop" procedure. No Finding shall be closed in the GRC system until independent remediation verification has been completed and documented.

1.  **Remediation Completion Notification:** Upon completing the corrective actions in their approved Remediation Plan, the Control Owner changes the Finding status to "Remediation Complete — Pending Verification" in OneTrust. The Control Owner must attach evidence of completion (e.g., updated configuration screenshots, re-executed attestation reports, updated policy document with revision history).
2.  **Verification Scoping:** The Auditor who issued the original Finding (or a designated delegate) reviews the Management Response and the provided evidence. The Auditor determines a "Verification Testing Window" — a period (typically 30-90 days post-remediation) during which the remediated control must operate flawlessly.
3.  **Re-Testing:** After the verification window, the Auditor selects a new, independent sample from the population of events occurring *after* the remediation date. The rigorous testing procedure (Section 5.3.1) is repeated.
4.  **Verification Outcome:**
    - **Pass:** If the re-tested control operates effectively, the Auditor documents the verification results, and the CCO formally closes the Finding in OneTrust. The closure entry summarizes the original issue, corrective action taken, and verification results.
    - **Fail:** If the control still fails testing, the finding is re-opened. An immediate escalation is initiated to the CCO and the Control Owner's senior leadership. A new, more aggressive Remediation Plan with executive-level oversight is mandated. The finding severity may be elevated (e.g., Medium to High) due to the failure of the corrective action, indicating a systemic issue.

---

## 6. Controls and Safeguards

This section describes the administrative, technical, and physical controls that are themselves subject to the monitoring and testing framework.

### 6.1 Administrative Controls

**6.1.1 HIPAA Workforce Security (§164.308(a)(3)(ii)(A-C))**
- **Control (Authorization and/or Supervision):** Meridian maintains documented "Workforce Clearance Procedures." Before any workforce member is granted unsupervised access to PHI or ePHI systems, the following must be completed and documented: (a) Successful background investigation (criminal history check) completed by approved vendor (HireRight); (b) Signed Confidentiality Agreement and Acceptable Use Policy (SOP-HR-004); (c) Role-Based Access authorization approved by both the hiring manager and the Data Governance team.
- **Monitoring:** The Identity & Access Management (IAM) team (Okta) runs a weekly report of all new hires provisioned into PHI-access groups and reconciles this against completed background check and signed policy records in Workday. Any mismatch results in immediate suspension of access pending investigation by HR Compliance.

**6.1.2 HIPAA Information Access Management (§164.308(a)(4)(i)(ii)(A-C))**
- **Control (Access Authorization):** All PHI access is governed by a formal Role-Based Access Control (RBAC) matrix maintained in SailPoint IdentityIQ. The RBAC matrix maps job functions to specific data access entitlements and is reviewed and approved by the Data Governance Council semi-annually.
- **Control (Access Establishment and Modification):** All user account creation, modification, or deactivation follows a documented ticketing process in ServiceNow. No access shall be provisioned without a valid, approved ServiceNow request ticket linked to an approved role in SailPoint.
- **Testing (Quarterly):** Internal Audit will pull the complete User Entitlement Review report from SailPoint for the quarter. This report contains each user's manager's attestation that the user's access is appropriate. A sample of 50 users is drawn. The Auditor verifies that the access listed in the attestation exactly matches the actual access configured in the target production system (Active Directory security groups).
- **Metrics:** Percentage of quarterly access reviews completed on time by managers. Target: 99.5%. Percentage of de-provisioning tickets completed within SLA (1 hour for involuntary termination, 24 hours for voluntary departure). Target: 100%.

**6.1.3 GDPR Data Protection Impact Assessment (DPIA) Triggers (Article 35)**
- **Control:** For any planned processing of personal data using new technologies, or processing that is likely to result in a high risk to the rights and freedoms of natural persons, the Data Governance team MUST trigger a DPIA workflow in OneTrust prior to the commencement of processing. This applies to all Meridian AI/ML product development, the Clinical AI Platform data pipeline changes, and any profiling activities on the MedInsight platform.
- **Monitoring:** The Legal and Procurement teams flag all new vendor contracts and new internal project intake forms that relate to "high risk" processing (defined by Meridian's DPIA Trigger Register, a living document maintained by the DPO). The DPO reconciles triggered DPIAs against active projects monthly.

### 6.2 Technical Controls

**6.2.1 Access Control — Unique User Identification (HIPAA §164.312(a)(2)(i) / GDPR Art. 32(1)(b) pseudonymization/access control)**
- **Control:** The use of shared or generic accounts for access to production systems processing PHI or personal data is strictly prohibited. Every account must uniquely identify a single individual.
- **Technical Enforcement:** All production server authentication is federated through Okta MFA. Direct SSH access using local accounts is disabled. The Splunk correlation rule "Detection of Shared Account Usage" fires if a single named account is used for interactive login from more than one source IP address located in different geographic regions concurrently. **This is a Zero-Tolerance alert; confirmed incidents result in immediate access suspension of the account and a High-severity Finding.**

**6.2.2 Automatic Logoff (HIPAA §164.312(a)(2)(iii))**
- **Control:** Electronic sessions on clinical-facing and health-data-processing systems shall be automatically terminated after an idle period of no more than 15 minutes.
- **Technical Enforcement — Clinical AI Platform Portal:** Web session timeout set at idle 15 minutes via Azure Application Gateway session affinity configuration. Administrative consoles and back-end database access sessions are set to an idle timeout of 10 minutes.

### 6.3 Physical Safeguards

**6.3.1 Facility Access Controls (HIPAA §164.310(a)(1))**
- **Control:** Access to Meridian's physical data centers (co-location cages) and server rooms at corporate HQ is restricted to authorized personnel on a documented access list. Access is granted through a multi-factor physical process: (a) Proximity badge (HID); (b) Biometric verification (fingerprint or iris scan).
- **Review and Monitoring:** The Facilities Manager, in conjunction with the CISO, reviews the physical access list—which includes full names, titles, and last access date—on a quarterly basis for all facilities hosting ePHI. Physical access logs from the Lenel OnGuard access control system are reconciled against the authorized list. Any unauthorized tailgating event detected by the anti-piggybacking mantrap portals generates an immediate SOC alert.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance and Risk Indicators (KPIs/KRIs)

The GRC platform (OneTrust) aggregates data from all monitoring and testing activities into real-time dashboards. The following KPIs/KRIs are tracked and reported.

| KPI/KRI ID | Metric Description | Target / Threshold | Measurement Owner | Reporting Frequency |
|---|---|---|---|---|
| **KPI-CMP-010** | % of controls in the Approved CMP for which testing has commenced on schedule this fiscal year. | **Target: 100%** | Internal Audit | Quarterly |
| **KPI-FIND-020** | Average Days Outstanding for open "Medium" severity Findings past their original remediation due date. | **Target: <30 days** | CCO | Monthly |
| **KPI-FIND-030** | Average Days Outstanding for open "High" severity Findings. | **Target: 0 days** (None past due) | CCO | Monthly |
| **KPI-REMED-040** | % of Remediation Verifications completed that resulted in a "Pass" on first re-test. | **Target: >90%** | Internal Audit | Quarterly |
| **KRI-PRIV-010** | Number of DSARs (GDPR Art. 15-22) exceeding the 28-day near-miss threshold. | **Threshold: 0** | DPO | Monthly |
| **KRI-SEC-020** | Number of days a "Critical-Risk" vulnerability (CVSS >=9.0) on an ePHI asset remains unpatched. | **Threshold: Exceeding 48 hours triggers automatic High Finding.** | CISO | Weekly |
| **KRI-ACC-030** | Number of open User Access Recertifications (quarterly cycle) past the 7-day grace period. | **Threshold: >5 overdue triggers a systemic access review Finding.** | CISO | Weekly |
| **KRI-BAA-040** | % of active Business Associate relationships for which a valid, fully executed BAA is not retrievable from the contract repository. | **Threshold: >0% triggers a High Finding.** | CLO / Procurement | Monthly |

### 7.2 Reporting Cadence and Audience

| Report Title | Audience | Frequency | Content |
|---|---|---|---|
| **Compliance Operations Dashboard** | CCO, CISO, DPO, Control Owners | Weekly (Automated email from OneTrust) | Top 10 open Findings; DSAR near-miss report; Patched/Unpatched vulnerability trends; New regulatory intelligence items. |
| **Control Owner Scorecard** | Individual Control Owners and their Directors | Monthly | Performance against testing evidence SLA (Section 5.3.1, 5-business-day window); Open findings assigned to them and their aging; Upcoming scheduled testing events. |
| **Business Unit Compliance Report** | Business Unit Leads (e.g., VP of Clinical AI, VP of HealthPay) | Monthly | Aggregated compliance posture summary for their unit's controls; Findings trend (increasing/decreasing); Remediation plan status summary. |
| **Quarterly Compliance Review (QCR)** | Executive Leadership Team (CEO, CFO, GC, CCO, etc.) | Quarterly | Executive summary of all High/Critical findings; Regulatory horizon scanning update; KPI/KRI dashboard trends; Major remediation milestones; Budget/resource requests for the next quarter. |
| **Annual State of Compliance Report** | Board of Directors (Audit Committee) | Annually | Opinion on overall effectiveness of the compliance program by the CCO; Aggregated testing results for the fiscal year; Material weaknesses identified and resolved; Strategic outlook and resource plan for FY+1. |

---

## 8. Exception Handling and Escalation

### 8.1 Compliance Monitoring Exception

A compliance monitoring exception is a situation where a control, as defined in the monitoring plan, has triggered an alert, but upon initial investigation, the alert is determined to be a "false positive" or the result of an authorized but previously-unmodeled operational activity.

**Procedure:**
1.  The Control Owner investigating the alert documents the justification for why the alert does not constitute a control failure in the ServiceNow incident ticket linked to the alert.
2.  The justification must be peer-reviewed by another qualified member of the team.
3.  The CISO (for technical alerts) or CCO (for procedural alerts) reviews and closes the monitoring exception. The closed record is evidence for the next testing cycle.

### 8.2 Control Exception

A control exception is a formal, pre-approved deviation from a mandatory policy or standard. For example, an IT administrator may need temporary, escalated privileges beyond their standard RBAC role to perform emergency maintenance, representing an exception to the Access Control policy.

**Procedure:**
1.  **Temporary Exception:** The requesting individual submits a "Temporary Control Exception" request via the OneTrust GRC portal. The request must specify: the specific control being exempted, the business justification, a risk assessment, a proposed compensating control (e.g., full session recording for the privileged access), and a clear expiration date/time (not to exceed 24 hours).
    - **Approval:** The CISO (for technical controls) or the relevant VP-level Control Owner, with concurrence from the Compliance Officer for the domain, may approve temporary exceptions. The DPO must approve any temporary exception impacting GDPR-scoped personal data.
2.  **Permanent Exception:** A formal exception for a recurring or indefinite condition is extremely rare and treated as a risk acceptance. The request follows the same intake but requires a full risk assessment, documented compensating controls, and joint approval by the CCO, CISO, DPO, and General Counsel. All permanent exceptions are logged on the "Risk Acceptance Register" and are formally reviewed semi-annually by the Executive Risk Committee.

### 8.3 Escalation Path

Formal escalations of unresolved issues follow the management chain.

| Level | Escalation Trigger | Notified Party |
|---|---|---|
| **Level 1 — Operational** | Control Owner fails to respond to a Draft Finding or provide a Management Response within the 10-business-day SLA. | Control Owner's Director and the CCO. |
| **Level 2 — Tactical** | A "High" or "Critical" finding, or a remediation plan target date is missed by more than 15 days. | Respective VP/SVP, CCO, and General Counsel. CEO is notified for Critical Findings. |
| **Level 3 — Strategic** | Same "Material Weakness" finding re-occurs on the subsequent independent test (remediation verification failure); Multiple High findings across a single Business Unit in one quarter, indicating systemic breakdown. | Executive Leadership Team. GC briefs the Board Audit Committee Chair out-of-cycle. |

---

## 9. Training Requirements

The effectiveness of the compliance monitoring and testing framework depends on a workforce that is both aware of the requirements and capable of executing its responsibilities.

### 9.1 Role-Based Training Curriculum

| Role(s) | Training Module | Delivery Method | Frequency | Tracking System |
|---|---|---|---|---|
| **All Workforce Members** | "Meridian Code of Conduct: Your Role in Compliance and the Duty to Report." Covers non-retaliation policy for reporting compliance concerns in good faith. | Computer-Based Training (CBT) via Litmos LMS. Includes mandatory attestation. | Annually (upon hire and every 12 months thereafter) | Litmos LMS. Completion is a condition of employment. |
| **All Workforce Members with PHI/ePHI Access** | "HIPAA Privacy and Security Fundamentals for Workforce Members." Covers the Minimum Necessary Rule, breach recognition and immediate reporting requirements. | CBT + 15-minute live Q&A session with a Privacy Officer. | Annually | Litmos LMS. Access to PHI systems is automatically suspended if training is 30+ days overdue. |
| **Control Owners & Remediation Plan Owners** | "Control Ownership and the Compliance Testing Lifecycle: A Practical Workshop." Covers evidence collection best practices, how to write a robust Management Response, and root cause analysis techniques. | Instructor-Led Training (ILT) | Upon designation as a Control Owner, and biennially thereafter. | OneTrust (completion record manually uploaded). |
| **Engineering / DevOps Teams** | "Secure Coding and GDPR/Privacy Engineering." Covers DPIA triggers from an engineering perspective, data minimization techniques in code, and the secure development lifecycle. | ILT / Capture the Flag (CTF) exercises | Annually | Litmos LMS. |
| **Internal Audit / GRC Team** | "Advanced Compliance Auditing: HIPAA, GDPR, and AI Act." Covers evolving regulatory audit standards and statistical sampling mastery. | External Conference / Certification (e.g., CISA, CIPP/E) | Annually (minimum 40 CPE hours) | Professional certification bodies; tracked in Workday. |

### 9.2 Tracking and Enforcement

Training completion rates are reported monthly to the CCO and CISO. HR is responsible for enforcing the access suspension policy for overdue training. Reports of non-completion are automatically generated by the Litmos LMS integration with Workday and Okta. The disciplinary process for persistent non-compliance with mandatory training requirements (failure to complete within 30 days of access suspension) follows the progressive discipline policy in the Employee Handbook.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs and Standards

| SOP ID | Document Title | Relationship to this SOP |
|---|---|---|
| SOP-DATA-004 | Data Classification and Retention Schedule | Defines retention periods monitored per Section 5.2.1 and GDPR Storage Limitation. |
| SOP-ISEC-008 | Access Control and User Access Recertification | The control procedure tested per Section 6.1.2. |
| SOP-ISEC-022 | Security Incident Response and Breach Notification | The notification procedures monitored per KRI-SEC-020 and tested for HIPAA Subpart D/GDPR Art. 33-34 adherence. |
| SOP-PRIV-007 | Data Subject Access Request (DSAR) Handling Procedure | Operational procedure monitored per Section 5.2.2. |
| SOP-RMGT-003 | Enterprise Risk Management Framework | Defines the inherent risk assessment methodology used in CMP development (Section 5.1.1). |
| SOP-PRIV-011 | Data Protection Impact Assessment (DPIA) Protocol | Defines the DPIA triggers and process required by GDPR Art. 35, tested and monitored per this SOP. |
| SOP-TPRM-001 | Third-Party Risk Management | Defines the risk-based approach for evaluating vendors, a process whose compliance with HIPAA BAA requirements is a KRI (KRI-BAA-040). |

### 10.2 External Standards and Regulatory References

- HIPAA Privacy Rule: 45 CFR Part 160 and Subparts A, E of Part 164
- HIPAA Security Rule: 45 CFR Part 160 and Subparts A, C of Part 164
- HIPAA Breach Notification Rule: 45 CFR Part 164 Subpart D
- Regulation (EU) 2016/679 (General Data Protection Regulation — GDPR)
- HITECH Act (Title XIII of Division A and Title IV of Division B of the American Recovery and Reinvestment Act of 2009)
- EU Medical Device Regulation (MDR) 2017/745, Annex I General Safety and Performance Requirements (relevant to Clinical AI Platform CE marking)
- ISO 27001:2022 — Information security, cybersecurity and privacy protection
- NIST Special Publication 800-53, Revision 5, "Security and Privacy Controls for Information Systems and Organizations" (control mapping reference)
- AICPA Trust Services Criteria (TSP Section 100, 2017)

---

## 11. Revision History

| Version | Effective Date | Author(s) | Summary of Changes |
|---|---|---|---|
| 1.0 | 2022-03-15 | J. Miller (CCO), K. Chen (GRC) | Initial document creation. Established baseline monitoring and testing framework. |
| 1.1 | 2023-08-01 | J. Miller (CCO) | Minor revision. Added explicit DPO role responsibilities in Section 3.2 following DPO appointment. Updated KPI targets for DSAR processing. |
| 1.2 | 2024-02-10 | L. Hernandez (Internal Audit) | Updated sampling methodology (Section 5.4) to align with new AICPA sampling guidance. Revised finding severity matrix to include "Critical" tier in response to Executive Risk Committee feedback. |
| 2.0 | 2025-12-20 | T. Anderson (CCO), M. Gonzalez (GC) | Major re-write. Incorporated EU AI Act and EU MDR regulatory monitoring requirements into Monitoring Plan procedures. Completely overhauled Section 7 (Monitoring, Metrics, and Reporting) with new GRC platform (OneTrust migration). Introduced remediation verification procedure (Section 5.5). |
| 2.1 | 2026-04-24 | T. Anderson (CCO) | Mid-cycle targeted revision. Updated Section 5.1.1 timing for FY2027 CMP development cycle. Clarified the independence requirements for Internal Audit in Section 3.2 to formalize dotted-line reporting. Corrected typographical error in KPI-FIND-020 metric target. Updated related policy cross-references in Section 10.1. |
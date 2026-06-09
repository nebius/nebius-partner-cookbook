---
sop_id: "SOP-ISEC-007"
title: "Security Awareness Training"
business_unit: "Information Security"
version: "5.8"
effective_date: "2025-03-27"
last_reviewed: "2026-01-06"
next_review: "2026-07-03"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Security Awareness Training

**Document ID:** SOP-ISEC-007
**Version:** 5.8
**Effective Date:** 2025-03-27

---

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the framework for Meridian Health Technologies, Inc.’s enterprise-wide Security Awareness Training Program. The program is designed to instill a culture of security mindfulness, ensuring that all personnel understand their role in protecting the company’s information assets, customer protected health information (PHI), intellectual property, and supporting information systems. The program aims to modify high-risk behaviors, reduce the human attack surface, and ensure compliance with regulatory and contractual security obligations.

### 1.2 Scope
This SOP applies to:
- All full-time and part-time employees of Meridian Health Technologies, Inc. across all global offices (Boston, London, Berlin, Singapore, Toronto).
- Contractors, consultants, temporary workers, and third-party personnel who are granted access to Meridian systems or data (collectively referred to as "Personnel").
- Any individual with a `@meridianhealthtech.com` email address or a corporate-managed device.
- All business lines, including Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform, acknowledging that specific role-based training modules will address the distinct risk profiles of each unit (e.g., SR 11-7 model risk for Financial Services, EU AI Act obligations for Clinical AI).

This SOP covers baseline security training, role-based advanced training, the enterprise phishing simulation program, and the associated tracking and compliance enforcement mechanisms.

---

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
| :--- | :--- |
| **AUP** | Acceptable Use Policy (See SOP-ISEC-001) |
| **CISO** | Chief Information Security Officer |
| **DPO** | Data Protection Officer |
| **ePHI** | Electronic Protected Health Information |
| **HIPAA** | Health Insurance Portability and Accountability Act of 1996 |
| **IS** | Information Security |
| **LMS** | Learning Management System (Workday Learning) |
| **MFA** | Multi-Factor Authentication |
| **NIST AI RMF** | National Institute of Standards and Technology Artificial Intelligence Risk Management Framework |
| **PHI** | Protected Health Information |
| **Personnel** | All employees, contractors, and temporary workers |
| **Phishing** | A social engineering attack where an adversary sends a deceptive message to trick a user into revealing sensitive information or deploying malicious software. |
| **RBAC** | Role-Based Access Control |
| **SIEM** | Security Information and Event Management (Splunk) |
| **SR 11-7** | Federal Reserve Supervisory Guidance on Model Risk Management |
| **SSO** | Single Sign-On |

---

## 3. Roles and Responsibilities

| Role | Responsibility | RACI Matrix |
| :--- | :--- | :--- |
| **Chief Information Security Officer (Rachel Kim)** | Executive owner of the Security Awareness strategy. Approves program budget, content roadmap, and exception escalations. | **A**ccountable |
| **VP of IT Operations (Samantha Torres)** | Ensures the technical infrastructure for training delivery and phishing simulations (KnowBe4) is operational and integrated with the corporate directory. | **R**esponsible |
| **Information Security Training Lead** | Manages the day-to-day program. Develops the annual training calendar, creates custom content for Meridian-specific threats, manages phishing campaigns, and monitors compliance dashboards. | **R**esponsible |
| **General Counsel (Maria Gonzalez) & Chief Compliance Officer (Thomas Anderson)** | Review training content for regulatory sufficiency regarding HIPAA, GDPR, EU AI Act, and SR 11-7. | **C**onsulted |
| **Chief Human Resources Officer (Jennifer Walsh)** | Integrates training requirements into onboarding checklists and progressive discipline processes. Manages the LMS platform availability. | **C**onsulted |
| **Chief Privacy Officer / DPO (Dr. Klaus Weber)** | Provides specific guidance on EU data protection principles and GDPR-mandated training elements for staff in Berlin and staff handling EU data. | **R**esponsible (Content) |
| **Managers / Directors** | Enforce attendance, manage the "refresher training" trigger for their direct reports following a security incident, and ensure staff have time allocated for training. | **R**esponsible (Enforcement) |
| **All Personnel** | Complete all assigned training by the mandated deadlines. Report suspicious activities (phishing, tailgating). Comply with the AUP. | **R**esponsible (Compliance) |
| **VP of Engineering (David Park)** | Approves content for secure coding and cloud security modules relevant to engineering teams. | **C**onsulted |
| **VP of Financial Services (Robert Liu)** | Approves content for SR 11-7 model risk training modules for financial analysts and model developers. | **C**onsulted |

---

## 4. Policy Statements

1.  **Mandatory Training:** All Personnel are required to complete the Meridian Security Awareness Essentials training within **30 calendar days** of their start date and an annual refresher within the calendar year.
2.  **Annual Curriculum:** The training curriculum will be reviewed annually by the Information Security Training Lead and updated to reflect the evolving threat landscape, including AI-prompt injection risks relevant to Clinical AI, financial fraud targeting HealthPay, and emerging social engineering tactics.
3.  **HIPAA Training:** In accordance with **45 CFR § 164.530(b)**, Personnel with access to PHI, specifically those within MedInsight Analytics and Clinical AI, must complete HIPAA Privacy and Security training upon hire, annually, and whenever "functions are affected by a material change in policies or procedures."
4.  **Phishing Simulation:** Meridian operates a mandatory, no-notice phishing simulation program. Participation is a condition of system access. Failure of multiple simulations triggers risk-based interventions, not immediate punitive action, except in cases of gross negligence.
5.  **Zero Tolerance for Malicious Activity:** While simulation failure is a training trigger, a deliberate attempt to exfiltrate data, disable security controls, or facilitate a real attacker will result in immediate disciplinary action up to and including termination and legal referral.
6.  **Safe Harbor Clause:** Personnel who promptly self-report a real-world error (e.g., clicking a malicious link and realizing the mistake) via the Incident Response hotline (`soc@meridianhealthtech.com`) will not face disciplinary action. This is designed to encourage rapid reporting and containment.

---

## 5. Detailed Procedures

This section outlines the lifecycle of security awareness training and simulations.

### 5.1 New Hire Onboarding

1.  **Day 0 (System Provisioning):** HR submits a hire ticket to IT. IT provisions the user account in Okta and assigns the "New Hire" group.
2.  **Day 1 (Workflow Trigger):** Okta automation pushes the user profile to Workday and KnowBe4. The new hire is automatically enrolled in the **Onboarding Curriculum**, consisting of the following modules:
    - *AUP Acknowledgement (SOP-ISEC-001)*
    - *Data Classification and Handling (SOP-ISEC-002)*
    - *HIPAA Privacy & Security Basics (45 CFR 164.530)*
    - *Global Phishing Awareness*
    - *Remote Work Security Standards*
3.  **Day 2 (Reminder):** The LMS sends a welcome email with direct links to the required courses.
4.  **Day 14 (Midpoint Escalation):** If modules are incomplete, the LMS sends an automated notification to the hire and copies their direct manager.
5.  **Day 29 (Final Notice):** A second warning is issued.
6.  **Day 30 (Access Restriction):** If training remains incomplete, the IS Training Lead generates a report and works with the CISO and HR to restrict access to specific data systems (e.g., Snowflake, AWS Console) until compliance is met. Access is automatically restored by Okta within 1 hour of LMS completion synchronization.

### 5.2 Annual Training Cycle

1.  **Q4 Planning (Preceding Year):** The IS Training Lead, in consultation with the CISO, General Counsel, and Business Unit VPs, drafts the "Annual Training Curriculum" for the following year.
2.  **Content Refresh (January):** Modules are updated with new threat intelligence from CrowdStrike and lessons learned from the previous year's major incidents and near-misses.
3.  **Campaign Launch (March 1):** The annual training campaign is launched to all active Personnel.
4.  **Completion Deadline (April 30):** All Personnel must complete the core training (approx. 45 minutes).
5.  **Late Compliance (May 1 - May 31):** Non-compliant Personnel are escalated per the matrix in Section 8.

### 5.3 Phishing Simulation Program

The phishing simulation program is managed via KnowBe4.

1.  **Randomization & Cadence:**
    - **Frequency:** Personnel receive simulations on a random cadence, averaging **two simulations per calendar quarter**.
    - **Templates:** Templates are selected from Meridian-benchmarked "High-Risk" categories: Financial Services (fake wire transfers), Healthcare (fake patient portal login), and Corporate IT (fake VPN/Okta alerts).
    - **AI-Augmented Phishing (Advanced):** Beginning Q2 2025, targeted simulations utilizing LLM-generated text to mimic internal executive communications will be deployed to VPs and above to test resistance to sophisticated spear-phishing.

2.  **Immediate Failure Handling (Click/Link Interaction):**
    - If a user clicks a link or opens an attachment:
        - **Immediate Redirect:** The user is redirected to a "You've Been Phished!" landing page.
        - **Just-in-Time Training:** The landing page displays an interactive module (3-5 minutes) explaining the red flags present in the specific email they received. The module must be completed before the user resumes normal browser activity.
        - **Data Capture:** The failure is logged in KnowBe4.

3.  **Credential Entry Handling:**
    - If a user enters credentials on a simulated malicious landing page:
        - **Immediate Password Reset:** An automated workflow triggers a forced Okta password reset.
        - **Manager Notification:** The user’s direct manager and the IS Training Lead are notified via email within 1 hour.
        - **Mandatory 1:1 Intervention:** The user must complete a 30-minute one-on-one counseling session with the IS Training Lead or a delegated Security Champion within 5 business days.

4.  **Repeated Failure Protocols:**
    - **Second Failure in 12 Months:** Enroll in the "Intensive Phishing Defense" advanced course (90 days).
    - **Third Failure in 12 Months:** Formal escalation to VP of Human Resources and CISO for disciplinary review and temporary revocation of remote access privileges.

### 5.4 Role-Based Training (RBT) Assignment

Based on job function mapped in Workday, Personnel are automatically assigned additional modules.

| Role/Team | Mandatory Annual Training Modules | Regulatory Driver |
| :--- | :--- | :--- |
| **Clinical AI Engineering & Product** | AI/ML Security (Prompt Injection, Data Poisoning), EU AI Act Transparency Obligations, NIST AI RMF 2.0 Practical Application | EU AI Act, NIST AI RMF |
| **HealthPay Financial Services** | SR 11-7 Model Risk Awareness, PCI-DSS Fundamentals (if applicable to edge flows), Financial Social Engineering Deep Dive | SR 11-7, SOC 2 |
| **MedInsight Analytics & Care Mgmt** | Advanced HIPAA (Minimum Necessary Standard, 45 CFR § 164.514(d)(2) de-identification), PHI Anonymization techniques, Handling Patient Rights Requests. | HIPAA |
| **DevOps / Infrastructure / SRE** | Secure AWS Configuration (Cloud IAM Best Practices), Container Security (Kubernetes), Infrastructure as Code Scanning | SOC 2 |
| **C-Suite / Executive Assistants** | Advanced Persistent Threat (APT) Awareness, Whaling Attack Simulations, GDPR Data Breach Notification Protocol (72-hour rule) | GDPR, General Governance |
| **Customer Operations** | Verification of Identity (VOI) procedures, Handling of Payment Card Data (PCI awareness), Social Engineering via phone channels. | SOC 2, PCI |

### 5.5 Security Awareness Communications ("The Human Firewall Campaign")

The IS team distributes ongoing awareness materials outside the formal LMS.

1.  **Monthly Newsletter:** The IS Team publishes "The Secure Meridian" newsletter via Slack and email.
2.  **Digital Signage:** Rotating security tips appear on office screens in Boston and Berlin, featuring "Security Champion" spotlights.
3.  **Ad-Hoc Threat Alerts:** If CrowdStrike or the CISO identifies a critical emergent threat (e.g., a zero-day targeting healthcare), the IS Training Lead issues a "High Alert" broadcast via PagerDuty and Slack within 2 hours of confirmation, specifying observable indicators of compromise.

---

## 6. Controls and Safeguards

### 6.1 Administrative Controls
- **Policy Integration:** Completion of this training is a prerequisite for the provisioning of administrative privileges per SOP-ISEC-004 (Access Management).
- **Logical Access Reviews:** Manual reviews of user access are conducted when material role changes occur (e.g., transfer from Clinical to Financial Services), ensuring legacy entitlements are removed.
- **Sanction Policy:** Non-compliance with training is addressed in the progressive discipline matrix (Section 8).

### 6.2 Technical Controls
- **SSO Integration (Okta):** The LMS (Workday) and Phishing Platform (KnowBe4) use Okta SSO with enforced MFA. Real credentials are never entered into a phishing simulation landing page; all landing pages only capture SSO redirect tokens (which indicate a click) but do not store passwords.
- **Automated Enrollment:** RBAC groups in Okta determine LMS curriculum assignments. Moving a user from one group to another in Okta triggers a delta-check in Workday, adding or removing role-based modules within 4 hours.
- **Email Gateway (Proofpoint):** Simulation emails bypass Proofpoint inspection via a static header allow-list (`X-Phish-Test: True`) configured exclusively for the KnowBe4 static IP range. This prevents simulations from being silently quarantined.
- **Endpoint Detection (CrowdStrike):** CrowdStrike monitors for real-world credential harvesting attempts. To differentiate simulations, a browser extension deployed via Jamf verifies the authenticity of the Safe Harbor landing page before the user is shown the "fail" message.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)
The effectiveness of the program is tracked via an IS Training Dashboard (built in Tableau).

| Metric | Target | Measurement Tool |
| :--- | :--- | :--- |
| **Annual Completion Rate** | 100% by April 30 | Workday Reports |
| **Onboarding Completion (30-Day)** | 99.5% | Okta/Workday Sync |
| **Phishing Vulnerability Rate** | < 5% industry avg (Meridian target: < 3%) | KnowBe4 |
| **Phish-Prone Percentage Improvement** | 10% decrease year-over-year | KnowBe4 |
| **High-Risk User Remediation** | 100% of repeat clickers receive 1:1 intervention | Manual Audit |
| **Real-World Incident Reporting Rate** | Increase in early reporting of real phishing events (measured via SOC tickets) | Splunk |

### 7.2 Reporting Cadence
- **Monthly Operations Report:** The IS Training Lead provides a status update to the VP of IT Operations, detailing simulation results and onboarding compliance.
- **Quarterly Governance Review:** A formal report is delivered to the CISO and Business Unit leaders (Clinical, Pay, Analytics), including a breakdown of role-based training completion and phishing failure rates per BU.
- **Annual Board Summary:** The CISO presents an anonymized "Human Risk Score" to the Board of Directors as part of the annual security posture review.

---

## 8. Exception Handling and Escalation

### 8.1 Training Exemptions
- **Criteria:** Medical leave, family emergency, or specific operational duties (e.g., active incident response war-rooming).
- **Procedure:** Manager must submit a "Training Extension Request" via the IS Service Desk (Jira Service Management) *prior* to the deadline.
- **Approval:** Approved by the IS Training Lead for extensions up to 30 days. Extensions beyond 30 days require CISO (Rachel Kim) approval.
- **System Enforcement:** If an extension is approved, the user is moved to an "Excepted" group in Workday, removing them from auto-escalation scripts until the new date.

### 8.2 Progressive Discipline Matrix (Non-Compliance)
Escalation applies to non-completed, non-exempted annual training.

| Stage | Trigger | Action | Owner |
| :--- | :--- | :--- | :--- |
| **Level 1** | 1 day past deadline. | Automated email to Personnel and CC: Manager. | LMS (Workday) |
| **Level 2** | 14 days past deadline. | Formal written warning from HR added to personnel file. 15-day grace period granted. | HR Business Partner |
| **Level 3** | 30 days past deadline. | Suspension of all access to Meridian SaaS platforms (Okta deactivation) until training witnessed by supervisor. Unpaid suspension for hourly/contract roles. | CISO / CHRO |
| **Level 4** | 45 days past deadline. | Termination of contract or employment for failure to meet basic security fitness standards. | CHRO |

### 8.3 Phishing Dispute Resolution
If a Personnel member believes a simulation was deceptive in a way that violates the "Safe Harbor" spirit (e.g., mimicking a genuine personal tragedy), they may file a "Simulation Fairness Review" directly to the CISO within 2 business days. The CISO’s determination is final and binding.

---

## 9. Training Requirements

The Information Security team itself must maintain proficiency to deliver this program.

- **IS Training Lead:** Must maintain Certified Security Awareness Practitioner (CSAP) or equivalent SANS certification.
- **Security Champions:** A voluntary group of "Human Firewall Champions" in each business unit is trained monthly on new talking points. Champions receive a 4-hour advanced security training bootcamp annually.

---

## 10. Related Policies and References

| Reference ID | Document Name |
| :--- | :--- |
| **SOP-ISEC-001** | Acceptable Use Policy (AUP) |
| **SOP-ISEC-002** | Data Classification and Handling |
| **SOP-ISEC-004** | Identity and Access Management (IAM) |
| **SOP-ISEC-009** | Incident Response Plan |
| **SOP-PRIV-002** | HIPAA Sanction Policy |
| **SOP-PRIV-015** | Handling of PHI for Analytics (De-identification) |
| **External** | NIST SP 800-50 Rev.1: Building a Cybersecurity and Privacy Awareness and Training Program |
| **External** | 45 CFR § 164.308(a)(5) - HIPAA Security Rule: Security Awareness and Training |

---

## 11. Revision History

| Version | Effective Date | Author | Summary of Changes |
| :--- | :--- | :--- | :--- |
| 5.8 | 2025-03-27 | Rachel Kim | Annual content update. Added AI-Augmented Phishing simulation procedures (Section 5.3.1). Clarified GDPR 72-hour context for Execs. |
| 5.7 | 2024-11-15 | Rachel Kim | Q4 Minor Revision. Updated HealthPay RBT module to specifically include SR 11-7 deep-dive. Updated Safe Harbor contact to `soc@meridianhealthtech.com`. |
| 5.6 | 2024-07-02 | IS Training Lead (J. Chen) | Mid-year review. Adjusted phishing simulation cadence from quarterly to bi-monthly. Added metrics for Real-World Incident Reporting Rate. |
| 5.5 | 2024-01-22 | IS Training Lead (J. Chen) | Full annual refresh. Added clinical AI data poisoning module in response to NIST AI RMF adoption. |
| 5.4 | 2023-10-09 | Rachel Kim | Post-audit remediation. Tightened escalation timelines from 60 days to 45 days for Level 4 termination of access. |
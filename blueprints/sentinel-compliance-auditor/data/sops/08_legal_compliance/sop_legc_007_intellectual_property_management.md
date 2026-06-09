---
sop_id: "SOP-LEGC-007"
title: "Intellectual Property Management"
business_unit: "Legal & Compliance"
version: "1.4"
effective_date: "2025-12-15"
last_reviewed: "2026-05-25"
next_review: "2026-11-19"
owner: "Thomas Anderson, Chief Compliance Officer"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "EU AI Act"
status: "Active"
---

# Standard Operating Procedure: Intellectual Property Management

**SOP-ID:** SOP-LEGC-007
**Business Unit:** Legal & Compliance
**Version:** 1.4
**Effective Date:** 2025-12-15
**Classification:** Internal

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the framework, governance, and operational processes for identifying, protecting, managing, and enforcing the intellectual property (IP) assets of Meridian Health Technologies, Inc. ("Meridian" or the "Company"). The exponential growth of Meridian's AI-driven product portfolio, including the Clinical AI Platform, HealthPay Financial Services, and the underlying Meridian SaaS Platform, necessitates a rigorous, auditable IP management program that safeguards proprietary algorithms, training data methodologies, model architectures, and trade secrets while ensuring compliance with open source licensing obligations and contractual commitments.

This SOP operationalizes the Company's commitment to maintaining its competitive moat in the AI-powered healthcare fintech sector by treating IP as a strategic business asset requiring lifecycle management from inception through commercialization and eventual decommissioning.

### 1.2 Scope

This SOP applies to all Meridian employees, contractors, consultants, interns, and third-party vendors (collectively, "Personnel") who create, access, modify, distribute, or otherwise interact with Meridian Intellectual Property Assets. The scope encompasses:

| **In-Scope Activities** | **Out-of-Scope Activities** |
|--------------------------|-----------------------------|
| Invention disclosure and evaluation | Physical security badge systems |
| Patent preparation, filing, and prosecution | Employee background checks |
| Trade secret identification and protection | General HR policy enforcement |
| Open source software (OSS) compliance | Financial auditing (see SOP-FIN-012) |
| Copyright registration for software and documentation | Customer data privacy (see SOP-DP-004) |
| Trademark clearance and registration for product names | Clinical trial data management |
| IP clauses in employment and contractor agreements | |
| Third-party IP infringement monitoring | |
| IP aspects of M&A due diligence | |
| Licensing of Meridian IP to third parties | |

### 1.3 Geographic Applicability

This SOP applies globally to all Meridian offices and remote Personnel across the following jurisdictions: United States (headquarters, Boston, MA), European Union (Berlin, DE and Amsterdam, NL offices), United Kingdom (London office), Singapore (APAC hub), and any future locations. Personnel must comply with jurisdiction-specific IP laws in addition to this global policy; where local law imposes more stringent requirements, the more stringent standard applies.

---

## 2. Definitions and Acronyms

### 2.1 Key Definitions

| **Term** | **Definition** |
|----------|----------------|
| **Intellectual Property Asset (IP Asset)** | Any intangible asset created by Meridian Personnel that is eligible for legal protection, including inventions, works of authorship, trade secrets, trademarks, and proprietary data compilations. |
| **Invention** | Any new and useful process, machine, manufacture, or composition of matter, or any new and useful improvement thereof, including algorithms, software architectures, user interface designs, and business methods, that meets the statutory requirements for patentability. |
| **Trade Secret** | Information, including a formula, pattern, compilation, program, device, method, technique, or process, that derives independent economic value from not being generally known and is subject to reasonable efforts to maintain its secrecy. Meridian Trade Secrets include algorithm training methodologies, hyperparameter optimization techniques, and proprietary data processing pipelines. |
| **Open Source Software (OSS)** | Software licensed under terms that meet the Open Source Definition maintained by the Open Source Initiative (OSI), including copyleft, permissive, and weak-copyleft license categories. |
| **OSS Compliance Bill of Materials (OSS-BOM)** | A structured inventory of all open source components integrated into a Meridian product, including component name, version, license type, and linkage method. |
| **Invention Disclosure Form (IDF)** | The standardized Meridian form (MER-IDF-001) used to document and submit new inventions for legal review. |
| **Prior Art** | All information that has been made available to the public in any form before the effective filing date of a patent application. |
| **Freedom to Operate (FTO)** | The ability to commercialize a product or process without infringing valid third-party IP rights. |
| **Embargoed Jurisdiction** | Any country subject to comprehensive U.S. economic sanctions, including currently Iran, Cuba, North Korea, and Syria. Meridian does not file IP or conduct business in Embargoed Jurisdictions. |

### 2.2 Acronyms

| **Acronym** | **Full Term** |
|-------------|---------------|
| IP | Intellectual Property |
| IPR | Intellectual Property Rights |
| IDF | Invention Disclosure Form |
| IPAC | Intellectual Property Advisory Committee |
| OSS | Open Source Software |
| OSS-BOM | Open Source Software Bill of Materials |
| SCA | Software Composition Analysis |
| FTO | Freedom to Operate |
| USPTO | United States Patent and Trademark Office |
| EPO | European Patent Office |
| WIPO | World Intellectual Property Organization |
| NDA | Non-Disclosure Agreement |
| PIA | Proprietary Information Agreement |
| DTS | Designated Trade Secret |
| TSR | Trade Secret Register |

---

## 3. Roles and Responsibilities

### 3.1 Responsibility Assignment Matrix (RACI)

The following RACI matrix assigns responsibility for key IP management activities. Legend: **R** = Responsible (doer), **A** = Accountable (approver), **C** = Consulted (subject matter expert), **I** = Informed (kept apprised).

| **Activity** | **General Counsel (Maria Gonzalez)** | **Chief Compliance Officer (Thomas Anderson)** | **VP Engineering (David Chen)** | **Director IP (Sarah Kim)** | **Product Managers** | **All Personnel** | **External Patent Counsel** |
|--------------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| IP Strategy Approval | **A** | C | C | R | I | I | I |
| Invention Disclosure Submission | I | I | C | C | C | **R** | I |
| Invention Evaluation & Prioritization | **A** | C | C | **R** | C | I | C |
| Patent Filing Decision | **A** | I | I | **R** | I | I | C |
| Trade Secret Designation | I | **A** | C | **R** | I | I | I |
| OSS Component Approval | I | I | **A** | **R** | C | I | I |
| OSS Compliance Audit | I | C | I | **R** | I | I | I |
| IP Clause in Contracts | **A** | I | I | **R** | I | I | I |
| Third-Party IP Monitoring | I | I | I | **R** | I | I | C |
| IP Training Delivery | I | **A** | I | **R** | I | **I** | I |
| IP Infringement Escalation | **A** | **R** | C | **R** | C | **R** | C |

### 3.2 Named Role Descriptions

| **Role** | **Incumbent** | **IP Responsibilities** |
|-----------|---------------|-------------------------|
| **Chief Compliance Officer** | Thomas Anderson | Ultimate accountability for IP policy enforcement; chairs IPAC; approves trade secret designations; oversees IP audit program. |
| **General Counsel** | Maria Gonzalez | Approves all patent filings; serves as escalation point for IP infringement disputes; provides legal opinions on FTO analyses; authorizes IP litigation. |
| **Director of IP** | Sarah Kim | Day-to-day IP portfolio management; manages IDF pipeline; coordinates with external patent counsel; conducts OSS compliance reviews; maintains IP docket system; delivers IP training. |
| **VP Engineering** | David Chen | Approves OSS component use; ensures engineering teams follow OSS compliance procedures; manages source code repositories; oversees OSS-BOM generation. |
| **IP Advisory Committee (IPAC)** | Standing Committee | Evaluates invention disclosures; recommends filing decisions; reviews IP risk assessments; meets biweekly or as needed. Membership: General Counsel (Chair), CCO, VP Engineering, Director IP, and relevant Product Manager(s). |
| **External Patent Counsel** | Morrison & Foerster LLP (primary) / Finnegan LLP (supplementary) | Prepares and prosecutes patent applications; conducts prior art searches; provides patentability and FTO opinions; represents Meridian in post-grant proceedings. |
| **All Personnel** | All employees, contractors, consultants | Obligation to promptly disclose inventions; duty to protect trade secrets; compliance with OSS policies; mandatory IP training completion. |

---

## 4. Policy Statements

### 4.1 IP Ownership

All Intellectual Property Assets conceived, developed, or reduced to practice by Meridian Personnel within the scope of their employment or engagement, or using Meridian facilities, equipment, or Proprietary Information, are the sole and exclusive property of Meridian. This policy is memorialized in the Proprietary Information Agreement (PIA) executed by each employee at onboarding (see HR-ONBRD-001). Contractors and consultants are bound by equivalent IP assignment clauses in their Master Services Agreements.

### 4.2 Duty of Disclosure

All Personnel bear an affirmative duty to disclose any Invention or potentially patentable IP Asset to the Director of IP within **30 calendar days** of conception or first reduction to practice, whichever occurs earlier. Disclosure must be made using the Invention Disclosure Form (MER-IDF-001). Failure to timely disclose may result in loss of patent rights and subject the individual to disciplinary action up to and including termination.

### 4.3 Patent Filing Threshold

Meridian shall file a provisional patent application with the USPTO for any Invention that meets **all three** of the following criteria, as determined by IPAC:
1. **Strategic Alignment:** The Invention relates to a current or planned Meridian product or service line.
2. **Commercial Significance:** The Invention provides a demonstrable competitive advantage or enables a new revenue stream exceeding $250,000 in projected annual recurring revenue.
3. **Patentability Assessment:** External patent counsel provides a preliminary opinion that at least one non-obvious, novel claim can be drafted.

### 4.4 Trade Secret Default

Where an Invention does not meet the Patent Filing Threshold, or where the Director of IP determines that trade secret protection provides a longer competitive advantage than patent protection (considering a 20-year patent term vs. indefinite trade secret protection), the default is trade secret designation and protection per SOP-LEGC-005 (Trade Secret Protection Program).

### 4.5 Open Source First Principle

Meridian recognizes the value of open source software and encourages its use to accelerate development. However, **preservation of Meridian's proprietary IP is paramount**. The following OSS license categories are defined:

| **Category** | **License Examples** | **Approval Requirement** | **Permitted Use** |
|--------------|----------------------|--------------------------|-------------------|
| **Category A (Permissive)** | MIT, Apache 2.0, BSD 2/3-Clause, ISC | Automatic (SCA scan required) | Any use, including integration into proprietary products, subject to attribution requirements. |
| **Category B (Weak Copyleft)** | MPL 2.0, LGPL 2.1/3.0, EPL 1.0/2.0 | Director of IP approval required | Library linking only; no source code disclosure triggered unless modification to the OSS library itself occurs. |
| **Category C (Strong Copyleft)** | GPL 2.0/3.0, AGPL 3.0, EUPL 1.2 | IPAC approval required, written opinion from General Counsel | Permitted only in isolated, non-core modules where source code disclosure is acceptable per business assessment. |
| **Category D (Restricted)** | SSPL 1.0, Parity Public License, any license not on OSI-approved list | **Prohibited** | No use permitted without exception approved by General Counsel and recorded in the Exception Register (see Section 8). |

### 4.6 Trademark Clearance

Meridian shall conduct a trademark clearance search (USPTO TESS database and common law search) prior to adopting any new product name, service mark, or logo. The Director of IP maintains a Trademark Register (MER-TM-REG) of all cleared marks. Unauthorized use of un-cleared marks is prohibited.

---

## 5. Detailed Procedures

### 5.1 Procedure 1: Invention Disclosure and Evaluation

#### 5.1.1 Step 1: Invention Conception

When any Meridian Personnel conceives of a potential invention—including a novel algorithm, a method of training a machine learning model, a unique data preprocessing pipeline, an improved user interface mechanism, or a business method—they must immediately document the conception in a dated, witnessed record. Acceptable forms include:
- Entry in Meridian's Jira Confluence "IP Log" space (preferred method, time-stamped automatically).
- Handwritten laboratory notebook page, signed and dated by the inventor and one witness who understands the invention but is not a co-inventor.

The record must include sufficient technical detail to enable a person of ordinary skill in the art to understand the invention.

#### 5.1.2 Step 2: File an Invention Disclosure

Within **30 calendar days** of the documented conception date, the Personnel must complete and submit the Invention Disclosure Form (MER-IDF-001) via the Legal & Compliance Service Portal (ServiceNow: "IP Disclosure" request type). The form requires:

| **Field** | **Description** |
|-----------|-----------------|
| IDF-ID | Auto-generated (e.g., IDF-2026-0487) upon submission |
| Title | Concise, descriptive title of the invention (max 200 characters) |
| Inventor(s) | Full name, employee ID, department, and citizenship of each inventor |
| Conception Date | Date of first documented conception |
| Technical Field | Dropdown: AI/ML | Data Processing | UI/UX | Network Architecture | Database | Business Method | Medical Device Software | Other |
| Product/Feature | Which current or planned Meridian product does this relate to? |
| Priority Assessment | Recommended by Inventor: High (core product differentiator) / Medium (enabling technology) / Low (minor improvement) |
| Problem Solved | Description of the problem the invention solves (min 200 words) |
| Prior Solutions | What alternatives existed before this invention? |
| Novelty Statement | What specifically is new and non-obvious? Describe the inventive concept clearly. |
| Best Mode | The preferred implementation known to the inventor at time of filing. |
| Reduction to Practice | Has a prototype been built? Yes/No. If Yes, date of first successful demonstration. |
| External Disclosures | Has the invention been disclosed outside Meridian? (conference presentation, paper submission, investor pitch, etc.). If Yes, attach details. |
| Supporting Materials | Attach diagrams, architecture docs, code snippets (max 50MB per file, 5 files max) |

#### 5.1.3 Step 3: Preliminary Review by Director of IP

The Director of IP (Sarah Kim) reviews each IDF within **15 business days** of submission. The review includes:
- Verification of inventorship (cross-reference with HR records and PIAs on file).
- Assessment of completeness (incomplete forms are returned to inventor with deficiency notice; the 30-day clock is tolled).
- Screening for immediate disqualifiers: abstract ideas without technical implementation, mere data presentations, or inventions assigned to a third party under a collaboration agreement.
- Preliminary categorization as: (a) Proceed to IPAC Evaluation; (b) Trade Secret by Default; (c) Defensive Publication; or (d) No Action.

If "No Action" is the preliminary recommendation, the Director must record the rationale and obtain concurrence from the Chief Compliance Officer before closing the IDF.

#### 5.1.4 Step 4: IPAC Evaluation Meeting

IPAC convenes biweekly (every other Thursday, 2:00-4:00 PM ET). Agenda items include all new IDFs categorized as "Proceed to IPAC Evaluation." A typical evaluation involves:

1. **Inventor Presentation (15 minutes):** The inventor presents the invention, the problem it solves, and its significance to Meridian's business. A technical architecture diagram is strongly recommended.
2. **Q&A (10 minutes):** IPAC members assess strategic alignment, commercial significance, and whether the invention is detectable in a competitive product (detectability analysis—relevant for enforcement).
3. **Patentability Opinion Review (5 minutes):** If external counsel has been engaged, their preliminary opinion is summarized.
4. **Decision (5 minutes):** IPAC votes. Majority vote required to recommend filing. The Chair (General Counsel) holds the final decision authority.

#### 5.1.5 Step 5: Decision and Execution

| **Decision** | **Action** | **Responsible** | **Timeline** |
|--------------|------------|-----------------|--------------|
| **File Patent** | Engage external counsel; draft provisional application; file with USPTO within 60 days of IPAC decision. | Director IP | 60 days from IPAC approval |
| **Trade Secret** | Notify inventor; update Trade Secret Register (TSR) per SOP-LEGC-005; apply DTS protections. | CCO Designated TS Officer | 10 business days |
| **Defensive Publication** | Prepare technical disclosure; publish on IP.com or Research Disclosure; bar patenting by others; 5-year retention. | Director IP | 30 days |
| **Incomplete/Deferred** | Notify inventor with specific deficiencies or rationale for deferred reconsideration date. | Director IP | 5 business days |

### 5.2 Procedure 2: Patent Prosecution

#### 5.2.1 Provisional Application Filing

For inventions approved for patenting, the Director of IP instructs external patent counsel to prepare a provisional patent application. The provisional application must include:
- Detailed description and drawings sufficient to support the full scope of the invention.
- All inventor names and assignments.
- Meridian's internal docket number (format: MHT-PROV-YYYY-NNN).

Timeline: File within **60 calendar days** of IPAC approval decision.

#### 5.2.2 Non-Provisional Conversion

Within **12 months** of the provisional filing date, the Director of IP and external counsel determine whether to:
1. File a non-provisional utility application claiming priority to the provisional (standard path).
2. File a PCT international application (if international protection is desired).
3. Abandon the provisional (if the product direction has shifted or the invention no longer meets the patent filing threshold).

The decision matrix considers:
- Current commercial significance of the protected product.
- Likelihood of issuance of meaningful claims (external counsel opinion).
- Budget availability (annual patent budget managed by Director IP, currently $2.8M for FY2026).
- Jurisdictional filing strategy (see Section 5.2.4).

#### 5.2.3 Office Action Response

When the USPTO or foreign patent office issues an Office Action, the Director of IP coordinates with external counsel to prepare a response within the statutory deadline (typically 3 months for USPTO, extendable to 6 months with fees). Meridian's internal review cycle requires:
- **First Draft Review:** Director IP, relevant inventor(s) — within 10 business days of receipt from counsel.
- **Final Approval:** General Counsel — signature authority for all responses.

#### 5.2.4 International Filing Strategy

Meridian's standard international filing strategy prioritizes jurisdictions based on the following tiered approach:

| **Tier** | **Countries/Regions** | **Justification** |
|----------|----------------------|-------------------|
| **Tier 1 (Mandatory)** | United States | Headquarters, largest market, all inventions file here first. |
| **Tier 2 (Priority)** | European Patent Office (validated in DE, UK, FR, NL); Japan; China | Major commercial markets or jurisdictions where Meridian has significant R&D personnel or expects regulatory approval. |
| **Tier 3 (Selective)** | Canada, Australia, South Korea, Singapore | Markets with significant competitor activity or where Meridian has commercial operations. |
| **Tier 4 (Case-by-Case)** | All others | Considered on a per-invention basis based on Freedom to Operate risk, local manufacturing presence, or material licensing revenue potential. |

No filings will be made in Embargoed Jurisdictions.

### 5.3 Procedure 3: Trade Secret Management

#### 5.3.1 Identification and Registration

When an invention is designated a Trade Secret (or defaulted per Section 4.4), the Director of IP must register the asset in the **Trade Secret Register (TSR)** , a restricted-access system (hosted on Meridian's IP Management System, Anaqua IP Platform). The TSR entry includes:
- **TS-ID:** Unique identifier (format: TS-YYYY-NNNN)
- **Description:** Detailed description of the trade secret
- **Owner:** Assigned Meridian owner (typically the chief engineer or product manager)
- **Access List:** Named individuals with a need-to-know
- **Protection Measures:** Specific controls applied (e.g., encrypted code repository, separate access badge for physical lab area, "clean room" protocols)
- **Date Registered:** Date of designation
- **Review Date:** Annual review date

#### 5.3.2 Access Control

Access to a Designated Trade Secret (DTS) is limited to Personnel on the Access List. Each access grant must be approved by both the DTS Owner and the Director of IP. Access is logged and auditable. Unauthorized access or attempted access triggers a Security Incident Report per SOP-IS-003.

#### 5.3.3 Nondisclosure Agreements (NDAs)

Any disclosure of a DTS to a third party (vendor, partner, potential acquirer) requires a fully executed NDA that includes specific trade secret protection language approved by the Office of the General Counsel. The standard Meridian NDA template (MER-NDA-v4.2) is available in the Legal Contract Repository (ContractPodAi). NDAs for DTS disclosure must include:
- Explicit designation of the disclosed information as "Confidential Trade Secrets"
- Obligation to restrict access to personnel with a need-to-know
- A term of protection of at least 5 years beyond the term of the agreement
- Injunctive relief provisions

### 5.4 Procedure 4: Open Source Software Compliance

#### 5.4.1 OSS Component Request and Approval

Any Meridian engineer who wishes to incorporate an OSS component into a Meridian product must submit an **OSS Component Request** via the Developer Portal (Jira Service Management, form: "OSS Component Request"). The form captures:

- **Component Name and Version:** e.g., "scikit-learn v1.4.2"
- **License Identifier:** SPDX identifier (e.g., "BSD-3-Clause")
- **Linkage Method:** Static linking, dynamic linking, API call, standalone tool, or code snippet.
- **Modification Required:** Yes/No. If Yes, describe modifications.
- **Purpose:** Description of how the component will be used.
- **Product(s):** Which Meridian product(s) will incorporate it.
- **License Compliance Obligations:** Auto-populated summary from Meridian's License Obligation Database (maintained by Director IP).

**Automated Approval Logic (Category A only):** If the SPDX identifier maps to Category A and no modification is indicated, the request is auto-approved and recorded. The engineer receives a confirmation number.

**Manual Approval Logic (Category B):** The request is routed to the Director of IP for review. Review focuses on: (a) whether the linkage method triggers copyleft obligations; (b) whether any modification has been made; and (c) whether the component is used in a product subject to distribution (vs. SaaS-only). Approval must be issued within **5 business days**.

**IPAC Approval Required (Category C):** The full IPAC reviews the request. The Product Manager must prepare a business justification addressing: What is the business need? Is there a Category A or internally-developed alternative? What is the risk of mandatory source code disclosure? Can the GPL/AGPL component be isolated in a separate process? Approval requires unanimous vote.

**Prohibited (Category D):** Automatic rejection. The submitter is notified and directed to find an alternative.

#### 5.4.2 SCA Scanning and OSS-BOM Generation

Meridian employs **Black Duck Software Composition Analysis (SCA)** integrated into the CI/CD pipelines (GitHub Actions) for all products. The SCA scans are configured to:

1. **Trigger:** Automatically on every pull request to the `main` or `release/*` branches; weekly full-scope scan of all repositories.
2. **Detection:** Identify all open source components, versions, and licenses.
3. **Policy Enforcement:** Fail the build if any Category C or D component is detected without an approved exception (see Section 8).
4. **OSS-BOM Generation:** For each official product release, the VP Engineering or delegate must generate a complete OSS-BOM and transmit it to the Director of IP for archival in the OSS Compliance Repository. The OSS-BOM must include at minimum: Component Name, Version, License Identifier, Linkage Type, and Any Modification Flag.

#### 5.4.3 License Obligation Fulfillment

Within **30 days** of a product release incorporating OSS, the Director of IP must confirm fulfillment of all license obligations, including:
- **Attribution:** Copyright notices and license texts included in the product's "About," "Licenses," or "Legal" section (or a NOTICE file shipped with the product).
- **Source Code Availability:** For copyleft licenses, if Meridian distributes the software (not SaaS-only), the corresponding source code must be made available per the license terms.
- **Compliance Reports:** Filed in the OSS Compliance Repository.

### 5.5 Procedure 5: Third-Party IP Monitoring and FTO

#### 5.5.1 Competitor Patent Watch

The Director of IP, with assistance from external patent counsel, maintains a Competitor Patent Watch for the following entities: Epic Systems, Cerner/Oracle Health, Flatiron Health, PathAI, Aidoc, and any new entrant identified by Meridian's competitive intelligence team (Product Management). The Watch includes:
- **Search Queries:** Saved queries on Anaqua patent analytics targeting competitor names as assignees and relevant CPC codes (e.g., G06N 3/08 for deep learning architectures, G16H 10/60 for health data)
- **Alerting:** Alerts generated within 5 days of publication of relevant applications or grants.
- **Quarterly Report:** A summary report to IPAC highlighting notable competitor IP activity and any potential FTO concerns.

#### 5.5.2 Freedom to Operate Analysis

Prior to the commercial launch of a new Meridian product, the Director of IP must commission a formal Freedom to Operate (FTO) opinion from external patent counsel. The FTO analysis reviews:
- The product's technical architecture against granted patents in jurisdictions of commercial interest.
- Relevant pending applications that may issue with claims covering the product.
- Conclusion: (a) Favorable—no material impediment; (b) Identified Risk—identified patent(s) may present risk, design-around recommended; or (c) Unfavorable—a blocking patent exists, requiring licensing negotiation or litigation preparation.

The FTO opinion is privileged and confidential, shared only with General Counsel, Chief Compliance Officer, and the relevant executive leadership team member.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| **Control ID** | **Control Description** | **Implementation** | **Coverage** |
|----------------|-------------------------|-------------------|--------------|
| **TECH-IP-001** | Source Code Repository Access Control | GitHub Enterprise with SSO (Okta) and mandatory 2FA; branch protection rules on `main`; required pull request reviews for all merges. All repositories are private by default. | All Meridian repositories |
| **TECH-IP-002** | SCA Scanning | Black Duck integrated into GitHub Actions CI/CD; blocks merges of Category C/D OSS without approved exception. | All active repositories |
| **TECH-IP-003** | Trade Secret Document Labeling | Microsoft Purview Information Protection auto-labels documents matching patterns for TSR-registered trade secrets (e.g., keyword "DTS:") with "Meridian - Trade Secret" sensitivity label; enforces encryption, restricts external forwarding. | SharePoint, OneDrive, Exchange |
| **TECH-IP-004** | IP Docket Management | Anaqua IP Platform for patent and trademark docketing; includes automated deadline reminders at 60, 30, 14, 7, and 3 days before critical dates. | Legal & Compliance, External Counsel |
| **TECH-IP-005** | Data Loss Prevention (DLP) | Microsoft Purview DLP policies scan outgoing emails and file transfers for patterns indicating trade secret exfiltration (e.g., large code file attachments to non-corporate email addresses); triggers alert to SOC and hold for review. | All egress channels |
| **TECH-IP-006** | Invention Disclosure Logging | ServiceNow "IP Disclosure" request type with mandatory fields; submissions auto-logged and visible to Legal & Compliance dashboard. | Entire organization |

### 6.2 Administrative Controls

| **Control ID** | **Control Description** | **Frequency** | **Responsible** |
|----------------|-------------------------|---------------|-----------------|
| **ADM-IP-001** | IP Portfolio Review | Quarterly | Director IP |
| **ADM-IP-002** | Trade Secret Register Audit | Semi-annual (Q2, Q4) | Chief Compliance Officer |
| **ADM-IP-003** | OSS Compliance Audit (all products) | Annual (Q4) | Director IP with VP Engineering |
| **ADM-IP-004** | Personnel IP Acknowledgment | Annual (during annual compliance training window, November) | All Personnel (managed by L&C Training Coordinator) |
| **ADM-IP-005** | Departing Employee IP Exit Interview | At departure for all personnel in R&D, Engineering, Product, and Legal roles | HR Business Partner + Director IP |
| **ADM-IP-006** | NDA Compliance Spot-Check | Monthly random sample (5 active NDAs) | Compliance Analyst |

### 6.3 Physical Controls

| **Control ID** | **Control Description** |
|----------------|--------------------------|
| **PHY-IP-001** | Restricted access to server rooms hosting proprietary training data infrastructure (Meridian Boston DC: badge access with role-based permissions, biometric confirmation for Tier 4 areas). |
| **PHY-IP-002** | Clean desk policy for all Personnel with access to DTS-printed materials (see SOP-CORP-009, Physical Security). |
| **PHY-IP-003** | Shredded disposal of any printed materials marked "Meridian Proprietary," "Confidential," or "Trade Secret" (blue confidential bins, shredded within 24 hours by Iron Mountain). |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The following KPIs are tracked for the IP Management program and reviewed at IPAC meetings:

| **KPI ID** | **KPI Description** | **Target** | **Measurement Method** | **Reporting Cadence** |
|------------|---------------------|------------|------------------------|----------------------|
| **IP-KPI-01** | Time from IDF submission to IPAC decision | ≤ 45 calendar days | ServiceNow cycle time report | Monthly |
| **IP-KPI-02** | Time from IPAC "File Patent" decision to provisional application filing | ≤ 60 calendar days | Anaqua docket date minus IPAC decision date | Monthly |
| **IP-KPI-03** | OSS Compliance Scan Pass Rate | ≥ 98% of product builds pass without manual exception | Black Duck dashboard, all repositories | Weekly (for active builds) |
| **IP-KPI-04** | Number of open Category C/D OSS exceptions past their review date | Zero past-due exceptions | Exception Register review | Monthly |
| **IP-KPI-05** | Patent Portfolio Count | Growth target: ≥15 new patent families per fiscal year | Anaqua portfolio report | Quarterly |
| **IP-KPI-06** | Trade Secret Register audit finding closure rate | 100% of findings closed within 90 days | Audit tracking log | Post-audit; 90-day follow-up |
| **IP-KPI-07** | Personnel IP training completion rate | 100% for applicable personnel | LMS (Workday Learning) | Monthly |
| **IP-KPI-08** | IP infringement escalations resolved without litigation | ≥85% resolved through negotiation/licensing | IP Infringement Log (ServiceNow "IP Incident" tickets) | Quarterly |

### 7.2 Reporting Dashboards

The Director of IP maintains two operational dashboards in Power BI:

1. **IP Executive Dashboard** (accessible to C-suite, General Counsel, CCO, VP Engineering): Displays portfolio metrics, critical deadlines approaching within 30 days, open OSS exceptions, and incident summaries.
2. **IP Operational Dashboard** (accessible to Legal & Compliance, Engineering Leads, Product Managers): Displays IDF pipeline status, OSS-BOM completeness, training compliance, and upcoming IPAC meeting agendas.

Both dashboards are refreshed nightly from the Anaqua, ServiceNow, Black Duck, and Workday Learning source systems.

### 7.3 Formal Reporting

| **Report** | **Audience** | **Frequency** | **Owner** |
|------------|--------------|---------------|-----------|
| IP Portfolio Status Report | Board of Directors | Annually (Q4) | General Counsel |
| IP Risk and Compliance Report | Audit Committee, CCO | Semi-annually | Chief Compliance Officer |
| OSS Compliance Audit Report | VP Engineering, CTO | Annually (post-audit) | Director IP |
| IP Budget vs. Actual Report | CFO, General Counsel | Quarterly | Director IP |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Request Process

A written exception request to any provision of this SOP must be submitted via the Legal & Compliance Service Portal ("Policy Exception Request" — SOP template L&C-EXC-001). The request must include:
- The specific SOP section(s) from which deviation is sought.
- The business justification (including, for OSS exceptions, an explanation of why an approved alternative cannot be used).
- The proposed compensating controls, if applicable.
- The duration for which the exception is needed (must not exceed 12 months; renewable).
- Impact assessment if the exception is not granted.

### 8.2 Exception Approval Authority

| **Exception Type** | **Approver** | **Consultation Required** | **Maximum Duration** |
|--------------------|--------------|--------------------------|---------------------|
| Category B OSS used in a manner potentially triggering copyleft (e.g., modification) | Director of IP | VP Engineering | 6 months, renewable once |
| Category C OSS (GPL/AGPL) used in non-core module | Chief Compliance Officer | IPAC, General Counsel (written opinion) | 12 months, renewable quarterly |
| Category D OSS use | General Counsel (only authority) | IPAC (full review) | 6 months, non-renewable; must present plan to remove dependency within 6 months |
| Extension of IDF disclosure beyond 30 days | Director of IP | Inventor's Manager | 15 days, non-renewable |
| Trade Secret access by non-vetted third party | Chief Compliance Officer | General Counsel | Per-engagement basis, NDA must be in place |
| Any exception that may create a material IP risk | General Counsel (sole authority) | IPAC | Case-by-case |

### 8.3 Exception Register

All granted exceptions are logged in the Exception Register (IP-EXC-REG), maintained by the Director of IP. The Register tracks:
- Exception ID (e.g., EXC-2026-0042)
- Date granted and expiration date
- Approver
- Description and scope
- Associated products or systems impacted

Expired exceptions are automatically flagged in the IP Operational Dashboard. If the condition requiring the exception persists, a new request must be submitted before expiration. Lapsed exceptions are treated as violations and are auto-escalated to the CCO.

### 8.4 Escalation Path

1. **Level 1 — Director of IP:** Any Personnel with an IP concern or policy question. Resolves operational issues.
2. **Level 2 — IPAC:** Referred by Director of IP for matters requiring committee deliberation (e.g., priority disputes between product teams over competing invention disclosures).
3. **Level 3 — Office of the General Counsel:** All IP infringement claims, cease-and-desist notices received, actual or threatened IP litigation, or any event that triggers a potential mandatory disclosure obligation (e.g., to a regulator, insurer, or as part of a public filing).

---

## 9. Training Requirements

### 9.1 Required Training Modules

Meridian Personnel must complete the following IP training modules via the Workday Learning Management System (LMS). Completion is tracked and non-compliance after the due date is escalated to the individual's manager and HR Business Partner.

| **Training Module ID** | **Module Title** | **Audience** | **Frequency** | **Duration** | **Delivery Method** |
|------------------------|-----------------|--------------|---------------|--------------|---------------------|
| **IP-TRN-001** | IP Fundamentals: Protecting Your Work | All Personnel | Annually (due by November 30) | 45 minutes | E-learning (interactive SCORM) with end-of-module quiz (pass threshold: 80%) |
| **IP-TRN-002** | Invention Disclosure: What, When, and How | All Engineering, R&D, Product Management | Annually (due by November 30) | 60 minutes | E-learning + case study + IDF practice submission |
| **IP-TRN-003** | Open Source Compliance for Developers | All Software Engineers, DevOps, QA, and Engineering Managers | Annually (due by November 30); New Hire (within 30 days of start) | 90 minutes | E-learning + hands-on lab (scanning a sample repository with Black Duck) |
| **IP-TRN-004** | Trade Secret Protection | All Personnel with access to TSR-registered trade secrets | Annually; refresh upon new DTS designation | 30 minutes | E-learning + signed acknowledgment of specific DTS access obligations |
| **IP-TRN-005** | IP for Managers & Leaders | Directors and above | Biennially (even years) | 2 hours | Live (virtual) workshop delivered by Director IP + external IP counsel |

### 9.2 Training Compliance

The Chief Compliance Officer receives a monthly **Training Compliance Report** from the LMS. Any individual whose training is past due for 30 days or more receives a notification copied to their manager. Past-due beyond 60 days results in a "not in good standing" designation that can impact eligibility for merit increases, bonuses, or promotion consideration. Past-due beyond 90 days is referred to the CCO for escalation.

### 9.3 IP Onboarding (New Hires)

New Hires in Engineering, R&D, and Product roles must complete **IP-TRN-001** and **IP-TRN-003** within their first 14 days of employment, prior to receiving full commit access to Meridian's production GitHub repositories.

---

## 10. Related Policies and References

### 10.1 Meridian Internal Policies

| **SOP ID** | **Title** | **Relationship to IP Management** |
|------------|-----------|-----------------------------------|
| SOP-LEGC-005 | Trade Secret Protection Program | Detailed operational controls for trade secret assets; this SOP references the Trade Secret Register and access procedures. |
| SOP-IS-003 | Information Security Incident Response | Covers IP theft and exfiltration incident response workflows, forensic procedures. |
| SOP-DP-004 | Data Privacy and Protection | Addresses personal data; IP often interacts with training data subject to DPIA; must coordinate on data handling. |
| SOP-FIN-012 | Fixed Asset Management and Capitalization | Covers IP asset valuation for accounting purposes; patents and acquired IP are capitalized assets. |
| SOP-HR-008 | Employee Offboarding and Exit | Includes IP exit interview, asset return, and access revocation; this SOP references exit procedures. |
| SOP-PM-005 | New Product Introduction (NPI) | Mandates FTO review and OSS-BOM as part of the NPI gate review process before launch. |
| SOP-CORP-009 | Physical Security | Clean desk, secure disposal, and restricted area policies that support trade secret physical controls. |
| SOP-VEND-012 | Vendor Risk Management | IP clauses in vendor contracts, intellectual property indemnification, and OSS compliance for vendor-delivered code. |

### 10.2 External Standards and References

| **Reference** | **Description** |
|---------------|-----------------|
| 35 U.S.C. §§ 100-329 | United States Patent Act |
| 18 U.S.C. § 1836 et seq. | Defend Trade Secrets Act of 2016 |
| Directives (EU) 2016/943 | Trade Secrets Directive |
| SPDX Specification 2.3 | Software Package Data Exchange license identifiers |
| OPENSSF Scorecards | Open Source Security Foundation best practices for OSS compliance |

### 10.3 Meridian Forms and Templates

| **Form/Template ID** | **Name** | **Location** |
|----------------------|----------|--------------|
| MER-IDF-001 | Invention Disclosure Form | ServiceNow "IP Disclosure" |
| MER-NDA-v4.2 | Mutual Non-Disclosure Agreement | Legal Contract Repository (ContractPodAi) |
| L&C-EXC-001 | Policy Exception Request Form | ServiceNow "Legal Exception" |
| MER-TSR-001 | Trade Secret Register Entry Template | Anaqua IP Platform |
| OSS-REQ-001 | OSS Component Request Form | Developer Portal (Jira Service Management) |

---

## 11. Revision History

| **Version** | **Date** | **Author** | **Description of Changes** |
|-------------|----------|------------|----------------------------|
| 1.0 | 2022-03-01 | Sarah Kim, Director of IP | Initial release. Established foundational IP management program including IDF process, patent filing criteria, OSS compliance framework. |
| 1.1 | 2023-06-15 | Sarah Kim, Director of IP | Incorporated post-acquisition integration of AI imaging startup; added Trade Secret designation procedures and DTS controls; updated FTO analysis requirements for new Clinical AI Platform. |
| 1.2 | 2024-02-10 | Thomas Anderson, CCO | Revised OSS Category C approval process to require IPAC review following audit finding of un-reviewed GPL dependency in a production system; added mandatory SCA scanning in CI/CD (TECH-IP-002); clarified NDA requirements for trade secret disclosure; added IP onboarding for new hires. |
| 1.3 | 2025-06-01 | Maria Gonzalez, GC | Major revision triggered by CE marking under EU MDR for Meridian clinical AI products. Added international patent filing strategy (Section 5.2.4); expanded Trademark clearance procedures; updated Competitor Patent Watch list; increased patent filing budget threshold; formalized IP Executive Dashboard. |
| 1.4 | 2025-12-15 | Thomas Anderson, CCO | Current version. Updated effective date. Expanded OSS-BOM requirements; added Category D restricted OSS list (SSPL, Parity); updated external counsel assignments; revised KPIs and reporting thresholds; added M&A IP due diligence reference; updated training module IDs and compliance escalation; incorporated feedback from Q3 2025 IP audit. Updated approver to Maria Gonzalez following org change. |

---

**End of Document** — SOP-LEGC-007, Version 1.4

*This is an Internal Meridian document. Distribution outside of authorized Meridian systems is prohibited without prior approval from the Office of the General Counsel.*
---
sop_id: "SOP-DGP-018"
title: "Cookie and Online Tracking Consent"
business_unit: "Data Governance & Privacy"
version: "3.7"
effective_date: "2024-11-07"
last_reviewed: "2025-11-14"
next_review: "2026-05-25"
owner: "Dr. Klaus Weber, Chief Privacy Officer / DPO"
approver: "Maria Gonzalez, General Counsel"
classification: "Internal"
regulations:
  - "GDPR"
status: "Active"
---

# Standard Operating Procedure: Cookie and Online Tracking Consent

**Document Number:** SOP-DGP-018
**Version:** 3.7
**Effective Date:** 2024-11-07
**Owner:** Dr. Klaus Weber, Chief Privacy Officer / DPO
**Approver:** Maria Gonzalez, General Counsel

---

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the enterprise-wide framework for the deployment, management, and governance of cookies, pixels, local storage objects, software development kits (SDKs), and all other online tracking technologies (collectively, "Tracking Technologies") across Meridian’s digital properties. The purpose of this SOP is to ensure that all processing of personal data via Tracking Technologies is conducted in accordance with the General Data Protection Regulation (GDPR), the ePrivacy Directive (as transposed into Member State law, notably the German Telecommunications-Telemedia Data Protection Act – TTDSG), and applicable guidance from the European Data Protection Board (EDPB) and German supervisory authorities (Datenschutzkonferenz – DSK). This SOP operationalizes the principles of data protection by design and default, lawful consent, transparency, purpose limitation, and data minimization specifically within the context of online tracking.

### 1.2 Scope of Application

This SOP applies to all Meridian digital properties, systems, and applications that deploy Tracking Technologies, regardless of the jurisdiction where the property is hosted, if it targets or is capable of processing the personal data of individuals located in the European Economic Area (EEA). The scope includes, but is not limited to:

1.  **External-Facing Websites:** All public-facing websites owned and operated by Meridian, including corporate sites, product microsites, patient portals, and marketing landing pages.
2.  **Web Applications:** All browser-based Software-as-a-Service (SaaS) applications provided by Meridian, including the HealthPay Financial Services dashboard and clinical decision support tools.
3.  **Mobile Applications:** All native mobile applications offered under the Meridian brand, available on iOS and Android platforms.
4.  **Internal-Facing Systems:** Intranets, internal portals, and employee-facing applications to the extent that their use of tracking technologies processes personal data of employees in a manner outside the scope of employment necessity and GDPR Art. 88.
5.  **Third-Party Integrations:** Any third-party tracking script, pixel, or SDK embedded within a Meridian property, for which Meridian acts as a joint controller or a controller mandating specific processing instructions.

### 1.3 Exclusions

The following are explicitly excluded from the scope of this SOP:

- Tracking Technologies that are strictly necessary for the transmission of a communication over an electronic communications network, as defined by Art. 5(3) of the ePrivacy Directive and § 25(2)(1) TTDSG (e.g., a load-balancing cookie to manage server traffic).
- A cookie strictly necessary for the provision of an information society service explicitly requested by the subscriber or user (e.g., a session cookie maintaining a logged-in state, or a persistent cookie remembering shopping cart contents for a defined duration).

The determination of "strictly necessary" must be made on a case-by-case basis, following the Strictly Necessary Assessment defined in Section 5.2. The exemption is auditable and must be operationally justified.

---

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
| :--- | :--- |
| **Consent (GDPR Art. 4(11))** | Any freely given, specific, informed, and unambiguous indication of the data subject's wishes by which he or she, by a statement or by a clear affirmative action, signifies agreement to the processing of personal data relating to him or her. |
| **Consent Management Platform (CMP)** | A centralized software system used to manage the consent lifecycle, including request, collection, storage, retrieval, and propagation of consent signals. Meridian's enterprise CMP is OneTrust. |
| **Cookie Audit** | A systematic, documented inventory of all Tracking Technologies deployed on a Meridian property, including their technical attributes, data flows, and legal classifications. |
| **Data Controller** | The entity which alone or jointly with others determines the purposes and means of the processing of personal data. For cookies, this is typically Meridian and, for third-party cookies, Meridian and the third-party provider acting as joint controllers. |
| **Data Subject** | An identified or identifiable natural person. In the context of this SOP, a visitor to a Meridian digital property. |
| **ePrivacy Directive (ePD)** | Directive 2002/58/EC concerning the processing of personal data and the protection of privacy in the electronic communications sector, as amended. |
| **GDPR** | Regulation (EU) 2016/679 (General Data Protection Regulation). |
| **Joint Controllership (Art. 26)** | The arrangement where two or more controllers jointly determine the purposes and means of processing. Meridian enters Joint Controllership arrangements with third-party analytics providers. |
| **Local Storage Objects (LSOs)** | "Super cookies" or "Flash cookies" that store data locally on a device, persisting beyond standard browser cookie controls. |
| **OneTrust** | Meridian's designated enterprise Consent Management Platform (CMP) for scanning, inventorying, and managing user preferences. |
| **Personal Data (Art. 4(1))** | Any information relating to an identified or identifiable natural person. This includes online identifiers like cookie IDs, IP addresses, and device fingerprints. |
| **Pixel Tag (Web Beacon)** | A small, transparent graphic image (often 1x1 pixel) embedded in a website or email, used to track user behavior. |
| **SDK (Software Development Kit)** | A collection of software tools and libraries used by developers to create applications. Meridian's mobile apps integrate third-party SDKs, which require equivalent consent controls. |
| **Strictly Necessary (TTDSG § 25(2))** | Cookies essential for a service explicitly requested by the user. The exemption is interpreted narrowly per CJEU ruling C-673/17 (Planet49) and EDPB Guidelines 05/2020. |
| **TTDSG** | German Telecommunications-Telemedia Data Protection Act, which transposes the ePrivacy Directive into German law, particularly Section 25 on protection of terminal equipment. |

---

## 3. Roles and Responsibilities

The following RACI matrix defines the responsibilities for the lifecycle of Tracking Technologies. These roles are mandatory and auditable.

| Activity | Chief Privacy Officer (Weber) | Data Governance & Privacy Team | Digital Product Owner | Engineering / DevOps | Legal / GC (Gonzalez) | Third-Party Vendor |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Cookie Audit Execution** | A | **R** | C | C | C | I |
| **Strictly Necessary Assessment** | **R** | R | I | C | A | C |
| **CMP Rule Configuration (OneTrust)** | A | **R** | C | C | C | --- |
| **Technical Implementation (Tag Manager, SDKs)** | I | C | C | **R** | I | C |
| **Pre-Deployment QA & Consent Validation** | I | C | **R** | I | A | I |
| **DPA/JCA Negotiation with Third Parties** | **A** | C | I | I | **R** | C |
| **Monitoring & KPI Reporting** | A | **R** | C | C | I | I |
| **Incident Response (Non-Consented Tracking)** | **R** | R | C | C | C | I |
| **Annual Policy Review** | **R** | C | C | I | A | I |
*(R = Responsible for execution; A = Accountable for outcome; C = Consulted; I = Informed)*

**Chief Privacy Officer (Owner):** Dr. Klaus Weber holds ultimate accountability for the effectiveness of this SOP. He is the authority for all exceptions related to cookie categorization (Section 8.1).

**Data Governance & Privacy Team:** This team, under the CPO's direction, is the operational responsible party (R) for executing cookie audits, configuring the OneTrust CMP, and managing recurring scanning schedules.

**General Counsel (Approver):** Maria Gonzalez and the Legal team are accountable for legal interpretation, contract negotiation (Data Processing Agreements - DPAs, Joint Controller Agreements - JCAs), and reviewing privacy policies that must accurately reflect cookie procedures.

---

## 4. Policy Statements

The following high-level policy statements govern Meridian's use of online tracking. Violation of these policies may result in disciplinary action, up to and including termination and potential regulatory censure.

1.  **Consent as a Legal Basis:** Unless a Tracking Technology is validated as Strictly Necessary through the formal procedure defined in Section 5.2, Meridian shall rely solely on prior, informed, explicit consent under GDPR Art. 6(1)(a) and TTDSG § 25(1) for all storage of and access to information on a user's terminal equipment.
2.  **Data Protection by Default (GDPR Art. 25(2)):** All non-essential Tracking Technologies scripts, pixels, and SDKs **shall not load, execute, or transmit data** until affirmative consent for each specific purpose (categorized consent) has been received via the Consent Management Platform (CMP). No "implied consent," continued browsing as consent, or pre-checked boxes are permitted.
3.  **Transparency (GDPR Art. 5(1)(a), 12-14):** The CMP consent banner and the Meridian Privacy Policy must provide, in a concise and intelligible manner, detailed information about every Tracking Technology, including its purpose, data controller identity, the specific data attributes collected (e.g., IP address, Device ID, URL history), and its lifespan.
4.  **No Cookie Walls:** Access to Meridian services and content shall not be made conditional on the data subject consenting to the use of non-essential cookies. An equivalent, consent-free version of the service must always be offered. This codifies the EDPB's strict prohibition on "cookie walls" as failing to meet the "freely given" standard of Art. 4(11).
5.  **Granularity of Choice:** Consent must be obtained for distinct, granular processing purposes identified in our CMP taxonomy (Section 5.3.1). Blanket consent for "marketing" or "third-party cookies" is not valid. Users must be able to selectively consent to, for example, functional cookies while rejecting targeting cookies.
6.  **Withdrawal (GDPR Art. 7(3)):** It must be as easy to withdraw consent as it was to give it. The CMP must provide a persistently accessible consent management interface, such as a floating button or a prominent link, allowing the user to modify or withdraw their choices at any time without detriment.

---

## 5. Detailed Procedures

This section outlines the mandatory, lifecycle-based procedures for all Tracking Technology operations.

### 5.1 The Comprehensive Cookie Audit

Before any new digital property goes live, and on a recurring basis for all active properties, a comprehensive audit is mandatory.

**5.1.1 Trigger Events for an Audit:**
- Pre-launch of a new digital property (website, app, portal).
- Major feature release that introduces new front-end libraries or third-party integrations.
- On a scheduled, semi-annual cadence (see Section 7.2).
- As part of a Data Protection Impact Assessment (DPIA), per SOP-RS-005.

**5.1.2 Audit Procedure using OneTrust:**

1.  **Initiate Scan:** The Data Governance & Privacy Team initiates a scheduled scan within the OneTrust CMP module. The scan is configured to target the specific domain (e.g., `patient.meridian-health.com`). The team inputs the necessary authentication credentials if a deep scan of a gated portal is required.
2.  **Execute Crawler:** The OneTrust crawler, configured with a standard browser user-agent and an anonymized session, systematically crawls the target property. It simulates user actions defined by the Digital Product Owner, such as clicking CTAs or navigating through typical flows, to trigger latent cookies.
3.  **Auto-Categorization Engine:** The crawler automatically harvests all detected scripts, pixels, and cookies. It performs an initial categorization based on the OneTrust cookie database, a global open-source repository. This categorizes cookies into: Strictly Necessary, Performance/Analytics, Functional, Targeting/Advertising, and Social Media.
4.  **Manual Review & Enrichment:** The automated output **must** be manually reviewed. The Data Governance & Privacy Analyst validates each entry. For every uncategorized or in-house custom tracker, the Analyst performs a code-level review with the DevOps team. The Analyst must document the *controller* for each cookie. For a third-party (e.g., Google Analytics), the Analyst records whether Meridian acts as a sole controller or joint controller.
5.  **Legal Validation:** The enriched audit report is submitted to the CPO and General Counsel for the Strictly Necessary Assessment (see 5.2).
6.  **Sign-Off:** The final, locked audit report is signed off by the CPO and becomes the master record for that property's CMP configuration.

### 5.2 The Strictly Necessary Cookie Assessment (The `ePD Art. 5(3)` Exemption)

This is a formal, documented test to claim the consent exemption. It is not a technical categorization but a legal one, owned by the CPO.

An assessment form (Form-DGP-018a) must be completed for every cookie claiming this exemption. The form answers the following questions, following the four-part Planet49 test:

1.  **User Request Check:** Was this cookie's deployment directly and exclusively triggered by an action explicitly requested by the user (e.g., clicking 'Add to Cart')? A cookie set to remember a language preference where the user has not explicitly toggled a language switcher **does not** qualify.
2.  **Service Necessity Check:** Is this cookie objectively, technically indispensable to provide the service the user requested? An analytics cookie to measure general visitor count is helpful for Meridian's business but is **not** strictly necessary for the user to access the requested service (the website).
3.  **First-Party Check:** Is this a first-party cookie set directly by Meridian? Exemptions for third-party cookies are exceedingly rare and require direct functional integration. A third-party CDN's security cookie may qualify, but a third-party analytics cookie never will.
4.  **Duration/Legitimate Interest Check:** The exemption is narrow. A strictly necessary session cookie for authentication is a valid exemption. A persistent cookie must have its duration rigorously justified against the user request.

**Outcome:** Only cookies passing all four tests are exempted. They are flagged in OneTrust as "Strictly Necessary – GDPR/TTDSG Exempt" and are loaded without consent. All others default to requiring consent, configured as such in the CMP.

### 5.3 Consent Banner Configuration and Compliance Lifecycle

#### 5.3.1 OneTrust Configuration for Granularity

Consent must be granular. Meridian categorizes all non-exempt cookies into these distinct, EDPB-compliant categories, each requiring its own affirmative consent signal:

| OneTrust Category | Technical Function | Legal Purpose (GDPR) | Consent Status Required |
| :--- | :--- | :--- | :--- |
| **C0001: Strictly Necessary** | Session authentication (JWT), load balancers (F5), CSRF tokens. | Strictly Necessary / Service Requested. | No consent required. |
| **C0002: Performance/Analytics** | Google Analytics 4 (first-party, IP-anonymized), Hotjar (heatmapping, no keystroke recording). | Performance & Analytics. | **Affirmative Opt-In.** |
| **C0003: Functional** | Language preference selectors, region-based content personalization, chatbot support window state. | Functional Personalization. | **Affirmative Opt-In.** |
| **C0004: Targeting/Profiling** | LinkedIn Insight Tag, Meta Pixel, Google Ads Floodlight tags. | User Profiling, Behavioral Advertising, Targeted Content. | **Affirmative Opt-In.** |
| **C0005: Social Media** | Embedded YouTube video with tracking, X/Twitter Share button with SDK. | Social Media Tracking. | **Affirmative Opt-In.** |

#### 5.3.2 Geo-Targeting Rules

The CMP's geo-targeting engine is configured to display the full, consent-first banner experience (Opt-in model) for all visitor IP addresses resolved to the European Economic Area (EEA). The configuration must be reviewed monthly against the database of EEA IP ranges, with a failsafe: if the IP geo-location service fails or returns 'Unknown', the EEA-standard consent banner **must be** served by default as the legally safe harbor.

#### 5.3.3 Banner A/B and Design UX Constraints

All consent banners and preference centers must adhere to the Meridian "Fair Design" UX specifications, enforced during QA:

- **Non-Deceptive Choice Architecture:** The "Accept All" and "Reject All" (or "Confirm Choices") buttons must be presented at an identical visual parity (same size, font, color prominence) on Layer 1 of the banner.
- **No Dark Patterns:** Repeated pop-ups ("consent fatigue" by design), manipulative language ("Help us improve"—where the action is data collection), or any design that nudge a user towards acceptance by making rejection a multi-click journey are strictly prohibited.
- **Withdrawal Link:** A persistent "Cookie Settings" or "Manage Preferences" button (represented by a standard fingerprint icon) must be present on every page, not just linked in a dense footer. This allows the user to revoke consent as easily as it was given (Art. 7(3)).

### 5.4 Implementation via Tag Manager

The engineering implementation of consent logic is executed through Meridian’s designated Tag Management System (TMS), Google Tag Manager (GTM), which is directly integrated with the OneTrust CMP. Consent for non-essential tracking technologies, particularly those in the Targeting/Profiling (C0004) and Performance/Analytics (C0002) categories, must be gated through this CMP-TMS integration. For the performance of this critical gating function, the following technical controls are mandatory:

1.  **Trigger Configuration:**
    **Condition:** For every tracking-related tag (e.g., LinkedIn Insight Tag, Google Analytics 4 Configuration tag, Meta Pixel), a single, standard firing trigger must be defined. Engineers must create a Custom Event Trigger named `consent_granted_group_c0004` for Targeting cookies and a Custom Event Trigger named `consent_granted_group_c0002` for Performance/Analytics cookies.
    **Blocking Trigger:** A default state for all non-necessary tags must be "Block." No exceptions. The initial page-load state is consent-less; all triggers fire only in response to a positive consent event pushed from the CMP.
    **Prohibition:** General page-view triggers (`pageview`, `DOM Ready`) without a consent condition are prohibited for non-necessary tags.

2.  **Consent Initialization Template (Template SOP-DGP-018-T1):**
    The following standardized tag template, "OneTrust - Consent Initialization - All Categories," must be deployed as the single, highest-priority tag firing on the "Consent Initialization - All Pages" trigger. This establishes the consent baseline before any other logic executes. The template configuration is as follows:
    *   **Tag Type:** Custom HTML
    *   **Tag Name:** `[PROPERTY]-[ENV] | ONETRUST | Consent Init | All Cats`
    *   **Firing Trigger:** `Consent Init - ALL`
    *   **Code:**
        ```html
        <script>
         window.dataLayer = window.dataLayer || [];
         
         // Function to map OneTrust active groups to standardized consent events
         function pushOneTrustConsentToDataLayer() {
           var activeGroups = '';
           // OneTrust sets window.OnetrustActiveGroups after script load
           if (typeof window.OnetrustActiveGroups !== 'undefined') {
             activeGroups = window.OnetrustActiveGroups;
           }
           
           // Push granular consent state for each category
           window.dataLayer.push({
             event: 'consent_state_update',
             consent_state_granted: {
               c0002_performance: activeGroups.indexOf('C0002') !== -1,
               c0003_functional: activeGroups.indexOf('C0003') !== -1,
               c0004_targeting: activeGroups.indexOf('C0004') !== -1,
               c0005_social_media: activeGroups.indexOf('C0005') !== -1
             }
           });
         }
         
         // Execute on DOM load when OneTrust script is ready
         if (window.OnetrustActiveGroups) {
           pushOneTrustConsentToDataLayer();
         } else {
           // Listen for OneTrust consent loaded event
           document.addEventListener('onetrust_consent_granted', pushOneTrustConsentToDataLayer);
         }
        </script>
        ```

3.  **SDK Consent Binding (Mobile Apps):**
    For mobile apps (HealthPay mobile, Meridian Clinic app), the same OneTrust tenant provides the Mobile App Consent SDK. The DevOps team must integrate the OneTrust SDK into the app build pipeline. At app launch, the `[OneTrustSDK loadConsentGroup]` method checks for prior consent. Before initializing any third-party analytics (e.g., Firebase, AppsFlyer) or marketing SDK, the app's code must perform a Boolean check: `if (consentGrantedForGroup("C0004") == YES) { [SDK start]; }`. Failure of this check must result in the SDK instance being `nil` or not initialized.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control ID | Control Name | Control Description |
| :--- | :--- | :--- |
| **TC-018-01** | **Default-Script-Block (CSP)** | A Content Security Policy (CSP) header is deployed on all production web servers. The `script-src` directive is explicitly and restrictively configured to use a nonce-based approach. Third-party domain origins for non-strictly necessary cookies (e.g., `*.linkedin.com`) are **not** added to the allowlist. This acts as a deep technical defense; even if a rogue script is injected, the browser will refuse to load it. |
| **TC-018-02** | **OneTrust API Strict Lock** | The OneTrust CMP's JavaScript API `OptanonWrapper()` is overridden via a Custom HTML tag in GTM, firing at the top of Page Load. This wrapper explicitly listens for the `groupsUpdated` event. Its sole function is to check `ActiveGroups.includes('C0004')`. If `false`, it runs a housekeeping command `window.OneTrust.DeleteCookie('_fbp')` to actively nuke any previously set third-party cookies, ensuring a clean state. This is a "belt-and-suspenders" approach to ensure consent withdrawal actually deletes cookies. |
| **TC-018-03** | **Quarterly Cookie Scan Automation** | Within OneTrust, a recurring, automated scan is configured in the "Scan Schedule" module. It targets the top 20 production URLs (by traffic, per Matomo analytics) every calendar quarter. The scan runs on the 1st of the month, using headless Chromium, and emails a Delta Report to the Data Governance Team, highlighting new or removed cookies. |

### 6.2 Administrative Controls

| Control ID | Control Name | Control Description |
| :--- | :--- | :--- |
| **AC-018-01** | **Release Gate: Consent UI Check** | The "Consent UI Validation" is a mandatory, non-negotiable gate in the CI/CD pipeline Jira Definition of Done (DoD) for any release candidate affecting a public-facing property. The Digital Product Owner must physically sign off a checklist (Form QA-018) in the staging environment, confirming banner parity and granular choice function before the ticket can transition to 'Done'. |
| **AC-018-02** | **Vendor Data Processing Assessment (VDPA)** | Before any third-party tracking pixel or SDK can be procured or integrated, the Vendor Owner must initiate a VDPA with the Privacy team. The assessment, documented in our OneTrust Third-Party Risk Management module, specifically reviews the vendor's own cookie policy to ensure they are not a "data leech" (e.g., an analytics provider that secretly cross-references our user data for their own unrelated ad network). This acts as a pre-contractual control mandated by GDPR Art. 28(1). |

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs) and Service Level Agreements (SLAs)

The effectiveness of this SOP is measured against quantifiable metrics, audited monthly by the Data Governance Team.

| Metric Category | Specific Metric (KPI) | Target/SLA | Measurement Tool |
| :--- | :--- | :--- | :--- |
| **Consent Integrity** | **CMP Consent Rate (Opt-In vs. Reject)** | Monitor Opt-In rate for Category C0004 (Targeting). Rate must be < 55%. A rate >80% is an alert indicating potential deceptive design (dark pattern). | OneTrust Analytics Dashboard |
| **Audit Compliance** | **Cookie Audit Delta Resolution** | 100% of new, uncategorized cookies detected in a quarterly scan must be classified and actioned (gated or justified) within **72 business hours** of detection. | OneTrust Scan Schedule Report |
| **Incident Management** | **Non-Consented Cookie Breach Response** | For a confirmed critical breach (tag fired without consent), the initial containment (tag pause) must be executed by the DevOps Team within **1 hour** of notification from the CPO. | PagerDuty / Incident Response Log |
| **Right of Access** | **Consent Log Retrieval** | Meridian must be able to retrieve the full, un-editable consent record for a specific individual (by IP/ConsentID) to demonstrate valid consent (Art. 7(1)) within **48 hours** of a DSAR request. | OneTrust Consent Logging Database |

### 7.2 Reporting Cadence

A formal "Cookie Compliance Status Report" will be compiled by the Data Governance & Privacy Team and delivered on the following cadence:

1.  **Monthly Operational Review:** A one-page dashboard report sent to the Chief Information Security Officer (CISO), VP of Engineering, and Digital Product Directors. It contains the CMP Consent Rate KPI, the number of new cookies detected from scans, and any open deviation requests.
2.  **Quarterly Business Review (QBR) with CPO:** A detailed report including full audit scan findings, an inventory lifecycle review (deletions, expirations), third-party controller compliance check summaries, and training completion metrics. Submitted to Dr. Klaus Weber for review and sign-off within the first 15 business days of the new quarter.
3.  **Annual Board-Level Summary:** An aggregated, anonymized report on overall GDPR ePrivacy posture, major risks, and resource requirements, presented by the CPO to the AI Governance Committee and Board of Directors at the close of Q4.

---

## 8. Exception Handling and Escalation

### 8.1 Standard Exception Process

Compliance is mandatory. Any deviation from the procedures defined in this SOP (e.g., a request to deploy a non-categorized tracking pixel without a full prior audit) constitutes an Exception. All exceptions must be managed formally.

1.  **Initiation:** The requester (typically a Digital Product Owner) submits a "Cookie Compliance Exception Request" form (Form-DGP-018b) through the ServiceNow Legal/Compliance portal. The form requires a business justification, a risk impact analysis (e.g., "This pixel will collect IP addresses but the vendor contract is pending"), and a proposed compensating control.
2.  **Risk Assessment:** The Data Governance & Privacy Team conducts an initial risk assessment, scoring the request on a scale of P1 (Critical Breach/Likely Complaint) to P3 (Minor Procedural Delay).
3.  **Approval Authority:**
    - **P3 (Minor Exceptions):** Approvable by the Data Governance & Privacy Lead. Maximum duration: 14 calendar days, non-renewable.
    - **P2 (Moderate Exceptions):** Approvable by the Chief Privacy Officer (Dr. Weber). He may impose specific compensating controls (e.g., additional manual consent log reviews). Maximum duration: 90 calendar days.
    - **P1 (Critical Exceptions):** Require joint approval from the Chief Privacy Officer and the General Counsel (Maria Gonzalez). These are only granted in dire circumstances, documented heavily, and reported to the Supervisory Authority if involving a data breach.

### 8.2 Emergency Escalation: Non-Consented Tag Firing

If a critical incident is discovered—specifically, a tag from Category C0004 (Targeting) confirmed to be firing with a *false* or *absent* consent signal—the following escalation path is immediately invoked:

1.  **Detector:** The individual (e.g., QA Engineer, Data Analyst) discovering the anomaly immediately stops their investigation and contacts the #privacy-incidents Slack channel and pages the on-call Privacy Engineer via PagerDuty.
2.  **Responder (DevOps On-Call):** Within 15 minutes, the DevOps engineer must log into GTM and **immediately pause** the rogue tag and any related triggers. The goal is containment, not root cause. This action is pre-authorized under this SOP.
3.  **Communicator:** The Data Governance & Privacy Team Lead assumes the role of Incident Commander. They assess the data breach risk (volume of data subjects affected, data categories). If a GDPR personal data breach is likely (risk to rights and freedoms of data subjects), they must escalate directly to the CPO and General Counsel for mandatory Supervisory Authority notification under Art. 33, within the statutorily bound 72-hour window now triggered.

---

## 9. Training Requirements

A workforce that is not regularly updated on the nuances of tracking law is a primary organizational risk. All personnel defined in Section 1.2 are subject to the following mandatory training.

### 9.1 Role-Based Training Curriculum

| Audience | Training Module (ID) | Content | Frequency | Assigned By |
| :--- | :--- | :--- | :--- | :--- |
| **All Employees (Digital)** | TRAIN-DGP-001: "GDPR & ePrivacy Essentials for Tracking" | Core concepts (consent, data minimization, DSARs), recognizing cookie banners, reporting a broken banner. | Annually, and within 30 days of hire. | Meridian LMS (Workday) |
| **Engineering & DevOps** | TRAIN-DGP-018-TECH: "Secure CMP & TMS Implementation" | Deep dive into OneTrust-GTM data layer logic, CSP enforcement, SDK consent binding, secure release gates. | Semi-annually, due to evolving browser standards. | Engineering Manager |
| **Product Owners & Marketing** | TRAIN-DGP-018-BIZ: "Lawful Tracking Design" | "Fair Design" UX rules, prohibition on dark patterns, the VDPA process, writing clear cookie descriptions. | Semi-annually. | CPO Designate (Privacy Team) |
| **Third-Party Vendors** | Meridian's "Data Protection & Cookies" Vendor Code of Conduct | Meridian-specific consent requirements, prohibition on secondary data use, audit rights. | Contractually stipulated. Onboarding and annually thereafter. | Vendor Relationship Manager |

### 9.2 Training Effectiveness and Tracking

Training is not a box-checking exercise. All training modules require a knowledge check quiz with a **mandatory pass rate of 80%**. Completion records are automatically logged in the Meridian Learning Management System (LMS), Workday, creating an auditable record for regulatory purposes. Any individual failing the quiz three times is reported to their manager and the Data Governance Team for targeted, in-person intervention.

---

## 10. Related Policies and References

### 10.1 Internal Meridian Documents

- **SOP-IS-002:** Information Security Acceptable Use Policy
- **SOP-RS-005:** Data Protection Impact Assessment (DPIA) Procedure
- **SOP-VM-011:** Vendor Risk Management & Privacy Assessment (VDPA) Procedure
- **SOP-DGP-015:** Data Subject Access Request (DSAR) Handling
- **SOP-ENG-022:** Secure CI/CD Release Management and Change Control
- **POL-DGP-001:** Enterprise Data Governance Policy
- **POL-HR-010:** Employee Privacy Notice & Consent Policy
- **Meridian's Record of Processing Activities (RPA), Article 30:** Online Tracking & Analytics Register

### 10.2 External Legal Instruments and Guidance

- **Regulation (EU) 2016/679** (General Data Protection Regulation, GDPR), specifically Articles 4(11), 6(1)(a), 7, 12-14, 24, 25, 26, 28, 30, 33, 34, 44-49.
- **Directive 2002/58/EC** (ePrivacy Directive), as amended by Directive 2009/136/EC, specifically Article 5(3).
- **Gesetz über den Datenschutz und den Schutz der Privatsphäre in der Telekommunikation und bei Telemedien (TTDSG)** , specifically Section 25.
- **EDPB Guidelines 05/2020** on consent under Regulation 2016/679.
- **CJEU Judgement C-673/17** (Planet49) on active consent for cookies.
- **DSK Guidance (Germany):** Orientierungshilfe der Aufsichtsbehörden für Anbieter von Telemedien (OH Telemedien).
- **NIST AI 100-1:** AI Risk Management Framework.

---

## 11. Revision History

| Version | Date | Author | Approver | Summary of Changes |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 2021-02-15 | J. Miller (Data Gov) | M. Gonzalez | Initial creation of SOP based on GDPR readiness project. Baseline OneTrust configuration and audit schedule established. |
| 2.0 | 2022-06-01 | A. Chen (Data Gov) | M. Gonzalez | Major update to incorporate TTDSG §25 requirements replacing the old ePrivacy directive interpretations in Germany. Added the "Reject All" button parity constraint. |
| 2.4 | 2023-01-10 | A. Chen | M. Gonzalez | Added Mobile SDK consent binding procedures under Section 5.4.3. Updated RACI to formally assign Product Owner for pre-deployment QA. |
| 3.2 | 2023-11-20 | K. Weber (CPO) | M. Gonzalez | Complete rewrite to integrate new EDPB Guidelines 05/2020 post-Planet49 enforcement. Added technical control TC-018-02 (OneTrust API Strict Lock) to address persistent cookie survivability issues. New templates introduced. |
| 3.7 | 2024-11-07 | K. Weber (CPO) | M. Gonzalez | Annual scheduled review. Updated definitions (Section 2) for clarity on joint controllership. Tightened language in Policy Statement 4 on cookie walls. Refined Section 5.2 Assessment criteria to codify latest DSK telemedia guidelines. Updated Section 9 Training for Product Owners. |

**END OF DOCUMENT**
---
sop_id: "SOP-ITOP-015"
title: "Network Operations"
business_unit: "IT Operations & Infrastructure"
version: "4.2"
effective_date: "2025-08-16"
last_reviewed: "2026-10-12"
next_review: "2027-04-28"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

## 1. Purpose and Scope

### 1.1 Purpose
This Standard Operating Procedure (SOP) establishes the operational framework for the management, monitoring, troubleshooting, and optimization of Meridian Health Technologies’ global network infrastructure. The network serves as the foundational transport layer for all Meridian business lines—including the Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and the Meridian SaaS Platform—supporting the secure transmission of Protected Health Information (PHI), personally identifiable information (PII), and payment card data across North American and European Union operating theatres.

The purpose of this document is to ensure the confidentiality, integrity, and availability (CIA) of network services in alignment with SOC 2 Trust Services Criteria, specifically the Security and Availability categories, and to provide a repeatable, auditable process for network operations staff.

### 1.2 Scope
This SOP applies to all network infrastructure components owned, operated, or managed by Meridian Health Technologies, Inc., including:

| Scope Area | Details |
| :--- | :--- |
| **Cloud Environments** | AWS Virtual Private Clouds (VPCs) in us-east-1 (primary) and eu-west-1 (EU data residency), AWS Transit Gateway, Direct Connect, Azure ExpressRoute (DR). |
| **Corporate Offices** | Local Area Networks (LANs), Wireless LANs (WLANs), and Wide Area Networks (WANs) connecting Boston (HQ), London, Berlin, Singapore, and Toronto offices via SD-WAN. |
| **Perimeter Security** | Next-Generation Firewalls (NGFW), Web Application Firewalls (WAF), VPN concentrators, and Secure Web Gateways (SWG). |
| **Operational Technology** | Network-connected building management and physical security systems, logically segmented from the corporate data plane. |
| **Third-Party Connectivity** | VPN tunnels and private links to healthcare provider systems, payer networks, and financial services partners. |

This SOP applies to all personnel within the IT Operations & Infrastructure business unit, specifically those in the Network Operations Center (NOC), Network Engineering, and Cloud Platform teams. It also governs activities by any third-party contractors or Managed Service Providers (MSPs) operating network infrastructure on Meridian’s behalf.

---

## 2. Definitions and Acronyms

| Term/Acronym | Definition |
| :--- | :--- |
| **ASN** | Autonomous System Number. A unique identifier assigned to Meridian for BGP routing. |
| **BGP** | Border Gateway Protocol. The routing protocol used to exchange routing information between Meridian’s VPCs, on-premises locations, and internet peers. |
| **DMZ** | Demilitarized Zone. A physical or logical subnetwork that exposes external-facing services to an untrusted network, usually the internet. |
| **IPAM** | IP Address Management. The administration of DNS and DHCP services, including the inventory of assigned IP address space. |
| **MTTR** | Mean Time to Resolve. The average time required to restore a failed network service to full operational status. |
| **NIDS/NIPS** | Network Intrusion Detection/Prevention System. A security appliance that monitors network traffic for suspicious activity and can take automated action. |
| **NOC** | Network Operations Center. The centralized location from which the IT Operations team monitors and manages the global network. |
| **QoS** | Quality of Service. The prioritization of specific types of network traffic to guarantee a certain level of performance. |
| **SD-WAN** | Software-Defined Wide Area Network. A virtual WAN architecture that allows enterprises to leverage any combination of transport services to securely connect users to applications. |
| **SNMP** | Simple Network Management Protocol. An Internet Standard protocol for collecting and organizing information about managed devices on IP networks. |
| **VPC** | Virtual Private Cloud. An on-demand configurable pool of shared resources allocated within the AWS public cloud environment, providing isolation between resources. |

---

## 3. Roles and Responsibilities

The following matrix delineates the roles and responsibilities for network operations activities. The accountable role (A) bears ultimate ownership; the responsible role (R) executes the work; the consulted role (C) provides input; and the informed role (I) receives status updates.

| Activity | VP, IT Ops (S. Torres) | Dir., Net. Eng. | NOC Lead | Network Engineer | CISO (R. Kim) | Cloud Arch. |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Policy & SOP Approval** | A/R | C | I | I | C | C |
| **Network Architecture Design** | A | R | C | C | C | R |
| **Change Management – Approval** | A | R | C | C | C | C |
| **Change Management – Implementation** | I | A | R | R | I | C |
| **Major Incident Management** | A | R | R | C | I | C |
| **Routine Maintenance** | I | A | R | R | I | C |
| **Capacity Planning** | A | R | C | C | I | C |
| **Vendor Relationship Mgmt.** | A | R | C | I | I | C |

---

## 4. Policy Statements

Meridian Health Technologies is committed to a network operations strategy that prioritizes security, availability, and performance to meet the demands of AI-driven healthcare and fintech workloads. The following policy statements form the non-negotiable control objectives of this SOP:

- **Change-Managed Infrastructure:** All modifications to the production network must be executed through the formal Change Management process. Changes must be reviewed and approved in writing. The individual who implements a change must not be the sole approver of that change record, ensuring a degree of independent review.
- **Segmentation by Design:** The corporate network, production cloud environments (Clinical AI, HealthPay, MedInsight, SaaS), and development/staging environments must be logically or physically segmented at all times. Traffic across security zones must traverse a Next-Generation Firewall (NGFW) with active Layer 7 threat prevention policies.
- **Continuous Network Monitoring:** The global network shall be monitored continuously (24x7x365) for availability, performance anomalies, and security events. Monitoring data will be used to trigger incident response and to support capacity planning.
- **Least-Privilege Access:** Access to network device management interfaces (SSH, HTTPS, console) shall be governed by the Identity and Access Management Policy (SOP-ISEC-012) using Okta for federated authentication with AWS Session Manager or equivalent secured jump hosts. Shared or local device accounts are prohibited in production environments.
- **Data Sovereignty Compliance:** Network topology and routing shall be configured to ensure that EU-domiciled data processed by the MedInsight Analytics and Clinical AI platforms remains transiting and at rest within the AWS eu-west-1 region, with clear logical demarcation from non-EU assets.

---

## 5. Detailed Procedures

### 5.1 Network Monitoring

The NOC is the central point of contact for all network health and performance visualization.

**5.1.1 Monitoring Platform**
All network devices (physical and virtual firewalls, routers, switches, load balancers) must be configured as monitored objects in **Datadog**. Meridian’s deployment utilizes the Datadog Network Device Monitoring (NDM) agent, ingesting SNMP traps from physical devices and leveraging cloud-native metrics via AWS CloudWatch for virtual constructs (Transit Gateway, NAT Gateways, VPC Flow Logs).

**5.1.2 Dashboarding**
The NOC Lead is responsible for maintaining the following key dashboards in Datadog:
- **Global WAN Health:** Link utilization, latency, packet loss for all SD-WAN overlay tunnels and Direct Connect circuits.
- **Perimeter Threat Status:** Concurrent connections and blocked sessions on the NGFW; top talkers by source IP.
- **Cloud-VPN Status:** Status of all VPN tunnels to third-party partners.
- **DNS Resolution:** Performance and availability of Route 53 Resolver endpoints and on-prem DNS infrastructure.

**5.1.3 Alerting Framework**
Datadog will generate alerts based on pre-configured thresholds. Network Engineers are responsible for acknowledging and acting upon alerts. While our monitoring platform captures a broad set of data, the NOC Lead is responsible for defining specific alert thresholds for newly onboarded devices and ensuring escalation paths are documented in the runbook for that device type. Alerts will be directed to the primary on-call system (PagerDuty).

### 5.2 Topology Management

Network topology, especially in highly dynamic cloud environments, must be subject to strict lifecycle control.

**5.2.1 Topology Documentation**
The Network Engineering team must maintain a current, version-controlled network topology diagram for each Meridian operating theatre (AWS us-east-1, AWS eu-west-1, Corporate WAN). This diagram, stored in the IT Operations Git repository (`netops/architecture`), must reflect:
- BGP peering relationships and ASNs.
- All ingress and egress points from every VPC.
- Logical security zone boundaries (DMZ, App-Tier, Data-Tier).
- Placement of all Layer 4 and Layer 7 firewall and load-balancer appliances.

**5.2.2 Topology Change Lifecycle**
Any substantial change to the logical or physical topology—including peering a new VPC via Transit Gateway, adding a new corporate site to the SD-WAN, or modifying an Azure ExpressRoute circuit to the DR environment—must follow this lifecycle:
1.  **Proposal:** A Network Architecture Proposal document is authored by the proposing Engineer in the `netops/proposals` repository.
2.  **Review:** The Director of Network Engineering and a Cloud Architect review the proposal’s security, cost, and operational impact. A written review must be appended to the proposal document.
3.  **Approval:** The VP of IT Operations provides final approval, documented within the version control commit/merge request.
4.  **Implementation:** The approved topology change is implemented as a formal Change Record (CR), detailed in Section 5.4.
5.  **Documentation Closure:** Upon successful CR closure, the Engineer must update the master topology diagrams and close the proposal record.

### 5.3 Bandwidth Management and Capacity Planning

To support real-time transmission of large DICOM imaging files for the Clinical AI Platform and the high-volume transactional load of the HealthPay platform, proactive bandwidth management is critical.

**5.3.1 Capacity Monitoring**
The Datadog `netops.bandwidth` dashboard provides a rolling 90-day view of circuit utilization:
- **Corporate Sites:** All SD-WAN circuits (primary and secondary internet links).
- **AWS Direct Connect:** Utilization of private and public VIFs for us-east-1 connection to HQ.
- **Inter-VPC Peering:** Throughput between core services VPC and tenant VPCs.

**5.3.2 Bandwidth Augmentation Criteria**
A capacity augmentation project (procuring new links, upgrading AWS Direct Connect port speeds) must be initiated when a sustained hourly average utilization rate exceeds **65%** during peak business hours (defined as 06:00-18:00 local time for the site) over a rolling 30-business-day period. The NOC Lead will generate a monthly Capacity Report, to be reviewed at the IT Operations change advisory board (CAB) meeting.

**5.3.3 Quality of Service (QoS)**
QoS tags are applied at the network edge (SD-WAN appliance or AWS EC2 instance) and honored across all Meridian-managed infrastructure. The following DSCP tagging standard is authoritative:

| Traffic Class | DSCP Mark | Queuing Priority | Example |
| :--- | :---: | :---: | :--- |
| **Real-Time/EF** | `EF` (101110) | Priority Queue (LLQ) | VoIP, Telemedicine video consults. |
| **Critical Prod** | `AF41` (100100) | Bandwidth 40% | Clinical AI API, HL7 FHIR messaging, HealthPay transactional protocols. |
| **Corporate Apps** | `AF21` (010100) | Bandwidth 25% | SSO, corporate email, ERP traffic. |
| **Best Effort** | `DF` (000000) | Remaining BW | General web browsing, software updates, guest network. |

### 5.4 Change Management for Network Infrastructure

SOC 2 criteria require that all network changes are managed to prevent unauthorized or inadvertent modifications that may impact the availability or security of the service. The following procedure is mandatory for all production network infrastructure.

**5.4.1 Initiation and Documentation**
All network changes (physical patching, firewall policy changes, BGP route re-distribution, DNS zone modifications, firmware upgrades) must be initiated by submitting a Change Request (CR) via Jira Service Management using the `PROD-CHG-NET` template. The CR must contain:
- **Risk Classification:** High, Medium, or Low, as defined in SOP-CHGMGT-001.
- **Justification:** Clear business driver linked to a feature, incident, or problem ticket.
- **Rollback Plan:** A step-by-step plan for reversing the change if unsuccessful.
- **Test Plan:** One or more specific commands or metrics that validate the change’s success.

**5.4.2 Approval and Segregation of Duties**
To prevent any single actor from introducing a destructive or unauthorized configuration, a basic segregation of duties model is employed. The Change Request must be reviewed and approved by a role distinct from the implementing engineer.
- If the **Network Engineer** is the implementer, the **Director of Network Engineering** or **VP of IT Operations** acts as the approver.
- For firewall security policy modifications, the **CISO (R. Kim)** must also be a consulted approver on the CR ticket.

Approval must be documented via a signed comment in the Jira CR ticket before implementation can proceed.

**5.4.3 Scheduled Maintenance Windows**
High and Medium risk network changes must be implemented within a designated maintenance window. Low-risk changes may be performed during business hours with Director of Network Engineering approval.

| Environment | Primary Window |
| :--- | :--- |
| Global Corporate Network (All Sites) | Saturdays, 02:00 – 05:00 Local HQ Time (EST) |
| Production AWS (us-east-1) | Sundays, 01:00 – 04:00 EST |
| Production AWS (eu-west-1) | Sundays, 01:00 – 04:00 CET |
| Staging/Development AWS | Any business day, 10:00 – 16:00 EST |

An exception window can be approved by the VP of IT Operations for critical, break-fix changes (e.g., restoring a failed BGP session).

#### 5.2.4 IP Address Management (IPAM)
Post-inspection, the Technician allocates a new management IP from the centralized **NetBox** IP Address Management (IPAM) system. All entries must be assigned to a specific device record and tagged with the environment (`prod`, `staging`, `corp`). Static IP assignments must be documented in NetBox. DNS records are automatically provisioned via a NetBox webhook into Route 53.

### 5.5 Troubleshooting Network Incidents

The following triage and escalation procedure provides a structured approach to restore service within the defined SLA targets.

**5.5.1 Incident Identification and Classification**
A network incident is formally initiated by a Datadog alert transitioning to a PagerDuty Incident, or by a Sev-1 or Sev-2 ticket lodged by an impacted business unit (e.g., a HealthPay transaction processing outage traced to the payment gateway VPC).

| Severity | Definition | Response SLA |
| :--- | :--- | :--- |
| **Critical (Sev-1)** | Complete or near-complete unavailability of a core line-of-business network segment (e.g., entire HealthPay VPC, HQ-to-cloud Direct Connect failure). | Acknowledge: 5 min; Triage: 15 min; Restore: 2 hours. |
| **High (Sev-2)** | Degraded service impacting >25% of users on a key segment, or loss of redundancy (e.g., a single Direct Connect connection failure while the backup operates). | Acknowledge: 15 min; Triage: 30 min; Restore: 4 hours. |
| **Medium (Sev-3)** | Localized issue (single office floor switch stack, single inter-VPC peering route failure) without widespread user impact. | Acknowledge: 30 min; Restore: 8 business hours. |
| **Low (Sev-4)** | Cosmetic or non-service-impacting errors (SNMP timeouts on decommissioned devices). | Scheduled routine maintenance. |

**5.5.2 Standard Troubleshooting Flow**
The responding Network Engineer must follow a structured model:
1.  **Define Scope:** Isolate the problem between the physical layer (Direct Connect, wiring), data link/VPC configuration (security groups, Transit Gateway route tables), or application (DNS resolution failure).
2.  **Engage Support:** If the scope indicates an upstream AWS issue, immediately open a Premium Support case via the AWS Management Console. For on-premises hardware, engage the vendor TAC and provide diagnostic output (`show tech-support`).
3.  **Implement Fix:** Roll back any recent network changes by executing the change’s defined rollback plan. If no recent change correlates, fail over to a redundant component (e.g., force BGP traffic over a secondary VPN tunnel).
4.  **Validate Restoration:** Confirm with the impacted business unit that service is restored. Monitor the relevant Datadog panels for 30 minutes post-restoration.
5.  **Document:** The Engineer must create a post-incident timeline within the Jira ticket, including root cause analysis, a permanent corrective action, and the MTTR metric.

---

## 6. Controls and Safeguards

### 6.1 Technical Controls

| Control | Implementation Detail | Safeguard Objective |
| :--- | :--- | :--- |
| **Next-Gen Firewall (NGFW)** | Palo Alto Networks VM-Series in AWS (us-east-1, eu-west-1) and physical appliances at HQ. Policy enforced via App-ID and User-ID. | Layer 7 security policy enforcement, IPS/IDS, malware prevention for all cross-zone traffic. |
| **Micro-Segmentation** | AWS Security Groups govern east-west traffic between EC2 instances; no reliance on broad CIDR-range rules. Instance-level security groups are bound to logical function. | Zero-trust networking. A compromised web server cannot directly access a database server unless explicitly permitted by a security group rule. |
| **TLS 1.2/1.3 Enforcement** | All NGFW perimeter rulesets reject inbound TLS negotiations below v1.2, as verified on the `netsec.tls.dashboard`. | Prevent cipher downgrade attacks on customer-facing clinical and payment endpoints. |
| **Outbound Proxy, SSL Decryption** | Corporate office outbound internet traffic force-tunnels through a Secure Web Gateway (SWG) with SSL/TLS decryption. | Data Loss Prevention (DLP) for corporate users handling PHI/PII; prevents botnet command-and-control exfiltration. |
| **Secrets Management** | Network device authentication (TACACS+) and AWS API interaction use ephemeral credentials from HashiCorp Vault. No static secrets in scripts. | Prevent credential leakage; enable full audit trail of administrative actions. |

### 6.2 Administrative Controls

- **Quarterly Access Review:** The NOC Lead and CISO will conduct a joint review of all privileged network device accounts and AWS IAM roles granting network configuration permissions (`NetworkAdmin` role family). Discrepancies must be remediated within 5 business days.
- **Vendor Risk Management:** Any third-party MSP granted VPN or jump-host access to Meridian’s NOC must undergo an annual security assessment managed by the Vendor Risk team, with attestation of their own SOC 2 Type II compliance for managed network services.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)
The performance of Meridian’s network and this SOP’s effectiveness are measured against the following metrics, reviewed monthly.

| KPI | Target | Measurement Tool |
| :--- | :--- | :--- |
| **Overall Network Uptime** | ≥ 99.99% (excludes pre-approved maintenance) | Datadog Synthetics & SNMP-based tracking. |
| **Sev-1 Incident MTTR** | ≤ 120 minutes | Jira Service Management SLA report, filtered by `component = "Network"` and `priority = "Critical"`. |
| **Sev-2 Incident MTTR** | ≤ 240 minutes | Jira Service Management SLA report, filtered accordingly. |
| **Change-Induced Incident Rate** | < 5% (number of failed changes / total network changes per month) | Jira change records linked to major incidents. |
| **IPAM Accuracy** | 100% | Monthly reconciliation of NetBox IP schema against AWS Config and live ARP tables. |

### 7.2 Reporting Cadence
- **Weekly Network Operations Report:** An automated report from Datadog summarizing weekly circuit utilization, top talkers by bandwidth, and any alerts which crossed a WARNING threshold. Distributed to the Network Engineering team and the VP of IT Operations.
- **Monthly Service Review (MSR):** The VP of IT Operations presents a comprehensive MSR, including the above KPI data, capacity planning forecast, and open problem ticket aging, to the Chief Technology Officer (CTO) and CISO.

---

## 8. Exception Handling and Escalation

### 8.1 Technical Exceptions
In circumstances where a policy or procedure in this SOP cannot be technically met (e.g., a legacy medical device that does not support modern TLS), the business unit owner for that asset must file a Technical Exception Request.

The process is:
1.  **Form Completion:** The requestor completes the IT Exception Form (located in the IT Compliance intranet), detailing the asset, the specific policy deviation, the compensating controls proposed, and a business justification.
2.  **Risk Assessment:** The CISO’s office assesses the inherent and residual risk of granting the exception against Meridian’s risk appetite.
3.  **Approval:** The VP of IT Operations and the CISO must jointly approve the exception. All approved exceptions are logged in a centralized register and must be renewed every **12 months** or upon a material change to the asset.

### 8.2 Escalation for Unresolved Incidents
If a Sev-1 or Sev-2 network incident is not resolved within its defined SLA, the following technical escalation path must be followed:

| Escalation Path | Contact | Condition |
| :--- | :--- | :--- |
| **Level 1** | NOC Engineer → NOC Lead | Notification at the SLA breach target time or when the Engineer declares they are at the limit of their diagnostic capability. |
| **Level 2** | NOC Lead → Director of Network Engineering | If the incident is not resolved within 150% of the initial SLA target, or if the fix requires a CR not executable in the current maintenance window. |
| **Level 3** | Director of Network Engineering → VP of IT Operations | For any incident involving a potential breach of PHI or PII, or any outage requiring an external vendor to be invoked at a highest-tier severity. |

---

## 9. Training Requirements

All personnel assigned the roles of NOC Lead, Network Engineer, or Director of Network Engineering must complete the following mandatory training curriculum. Training completion is tracked in the `Workday` learning management system and audited during annual performance reviews.

| Training Module | Method | Frequency | Applicable Roles |
| :--- | :--- | :--- | :--- |
| **SOP-ITOP-015 Review & Acknowledgment** | Online attestation via Jira/Confluence | Annually, and within 30 days of each SOP revision. | All Network Engineering & NOC Staff. |
| **Meridian Change Management Process** | Online course, assessment with 80% pass mark. | On-hire; refresher every 2 years. | All Network Engineers. |
| **AWS Network Security Best Practices** | AWS Skill Builder self-paced lab (`Networking Core - Security`). | On-hire; refresher upon major AWS service releases (e.g., new VPC features). | Engineers with privileges in us-east-1/eu-west-1. |
| **Incident Command System (ICS) 100** | Facilitator-led workshop, 4 hours. | On-hire for all Senior Engineers and NOC Lead. | All technical escalation managers. |
| **HIPAA for Technical Staff** | Online annual module via Compliatric LMS. | Annual. | All roles with access to PHI-bearing network segments. |

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs
All referenced SOPs are stored in the `policy.meridian.local` SharePoint repository and version-controlled in the `ops-policies` Git repository.

| SOP-ID | Document Title | Relationship to This SOP |
| :--- | :--- | :--- |
| **SOP-ISEC-012** | Identity and Access Management | Governs the Okta/MFA and RBAC models used to secure network device access. |
| **SOP-ISEC-020** | Incident Response | The authoritative procedure for declaring and managing a formal security incident, superseding a standard network incident. |
| **SOP-CHGMGT-001** | Change Management | The overarching change policy that details the CAB structure and high/medium/low risk definitions referenced herein. |
| **SOP-CLOUD-008** | AWS VPC Architecture & Configuration | Defines the specific VPC CIDR allocations, subnetting standards, and NACL baseline enforced by Cloud Architects. |
| **SOP-COMP-011** | Security Exception Management | Procedure for documenting and approving deviations from information security policy, as referenced in Section 8.1. |

### 10.2 External Standards and Frameworks
- **AWS Well-Architected Framework:** Reliability and Security Pillars guide architectural decisions for the Meridian cloud network.
- **NIST Special Publication 800-41 Rev. 1:** "Guidelines on Firewalls and Firewall Policy" — foundational reference for the Meridian perimeter security design.
- **AICPA SOC 2 Trust Services Criteria:** Sections CC6.6 (logical and physical access controls), CC7.1 (change detection and response), and A1.2 (availability monitoring).

---

## 11. Revision History

| Version | Date | Author (Role) | Summary of Changes |
| :--- | :--- | :--- | :--- |
| **1.0** | 2022-02-15 | M. Chen, Dir. Net. Eng. | Initial creation. Established foundational cloud and corporate network monitoring and change control. |
| **2.0** | 2023-05-22 | S. Torres, VP IT Ops | Major revision. Added corporate SD-WAN management, formalized the topology lifecycle, and integrated EU-specific data-sovereignty routing rules for MedInsight. |
| **3.0** | 2024-11-01 | A. Petrov, NOC Lead | Added detailed troubleshooting flow and incident SLA table (Section 5.5). Transitioned monitoring platform from SolarWinds to Datadog. |
| **4.0** | 2025-01-30 | S. Torres, VP IT Ops | Annual review. Added QoS standards for Real-Time clinical applications (Section 5.3.3) to support new CE-marked clinical AI modules. Incorporated formal approval segregation language. Version 4.0. |
| **4.1** | 2025-08-05 | J. Miller, Sr. Net. Eng. | Minor revision. Updated the IPAM system reference from Infoblox to NetBox. Updated AWS service names. Clarified the Sev-2 definition for loss of redundancy scenarios. |
| **4.2** | 2025-08-16 | S. Torres, VP IT Ops | Updated SOP to align with the new "Network Operations" formal naming convention. Added specific references to HealthPay and Clinical AI business lines in Sections 1.1 and 5.3. Adjusted the bandwidth augmentation threshold to 65% based on H2 growth trend analysis. |
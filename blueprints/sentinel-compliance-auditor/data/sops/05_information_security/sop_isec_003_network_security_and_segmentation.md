---
sop_id: "SOP-ISEC-003"
title: "Network Security and Segmentation"
business_unit: "Information Security"
version: "4.6"
effective_date: "2024-11-05"
last_reviewed: "2025-05-09"
next_review: "2025-11-17"
owner: "Rachel Kim, Chief Information Security Officer"
approver: "Dr. Sarah Chen, CEO"
classification: "Internal"
regulations:
  - "SOC 2"
  - "HIPAA"
status: "Active"
---

# Standard Operating Procedure: Network Security and Segmentation

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the mandatory framework for the design, implementation, monitoring, and continuous management of network security and segmentation controls across Meridian Health Technologies, Inc. The purpose is to protect the confidentiality, integrity, and availability of all Meridian information assets—including protected health information (PHI), personal data, financial transactions, and proprietary artificial intelligence models—by enforcing logical boundaries, traffic inspection, and threat prevention at all layers of the network stack.

This SOP defines the technical and administrative controls necessary to prevent unauthorized access, limit lateral movement of threats, isolate regulated workloads, and maintain demonstrable compliance with the SOC 2 Trust Services Criteria for Security, Availability, and Confidentiality. All controls herein are designed to satisfy the Common Criteria (CC) and complementary sub-criteria detailed in Section 6.

### 1.2 Scope

This SOP applies to:

- **All network infrastructure** owned, operated, or leased by Meridian Health Technologies, including on-premises, cloud (AWS, Azure), and co-location environments.
- **All environments** within the Meridian SaaS Platform, Clinical AI Platform, HealthPay Financial Services, MedInsight Analytics, and corporate IT systems.
- **All personnel** including employees, contractors, consultants, third-party service providers, and any other individuals or entities who administer, access, configure, or utilize Meridian network resources.
- **All connectivity methods** including wired, wireless (Wi-Fi 6E/7), VPN (client-based and site-to-site), direct interconnects (AWS Direct Connect, Azure ExpressRoute), and software-defined wide-area networking (SD-WAN).
- **All network-adjacent technologies** that enforce security policy, including firewalls, intrusion detection/prevention systems (IDS/IPS), web application firewalls (WAF), network access control (NAC), secure web gateways (SWG), and cloud security groups.

**Out of Scope:** Physical security of data center facilities is covered under SOP-PHYSEC-002. Endpoint security configurations are covered under SOP-ISEC-007.

### 1.3 Applicability by Business Unit

| Business Unit | Primary Environments | Specific Requirements |
|---|---|---|
| Clinical AI Platform | AWS us-east-1, eu-west-1; Azure DR | EU AI Act high-risk system isolation; model weight encryption in transit |
| HealthPay Financial Services | AWS us-east-1; isolated PCI/HITRUST subnets | SR 11-7 model boundary controls; annual penetration testing |
| MedInsight Analytics | AWS us-east-1; Snowflake VPC | PHI data movement logging; care gap analysis pipeline isolation |
| Meridian SaaS Platform | AWS us-east-1 (primary), eu-west-1 (EU), Azure DR | Multi-tenant logical separation; SOC 2 boundary definition |
| Corporate IT | Boston HQ, London, Berlin, Singapore, Toronto offices | Zero Trust Network Access (ZTNA) for remote workforce |

---

## 2. Definitions and Acronyms

### 2.1 Terms and Definitions

| Term | Definition |
|---|---|
| **Demilitarized Zone (DMZ)** | A network segment placed between the external internet and internal/protected networks, hosting services that must accept inbound connections from untrusted sources. All DMZ hosts are treated as compromised by design. |
| **East-West Traffic** | Network flows between servers, containers, or services within a data center or cloud environment, as opposed to north-south traffic that enters or exits the perimeter. |
| **Micro-Segmentation** | A Zero Trust-aligned technique that enforces workload-level isolation using host-based firewalls, security groups, or software-defined networking, restricting communication even within the same subnet. |
| **Network Security Group (NSG)** | An AWS security group or Azure network security group that acts as a virtual stateful firewall, controlling inbound and outbound traffic to cloud resources based on allow-list rules. |
| **Protected Health Information (PHI)** | Individually identifiable health information handled by Meridian systems, as defined under relevant privacy regulations. Within this SOP, PHI-bearing systems are designated as Tier 0 assets and subject to the highest level of segmentation. |
| **Trust Zone** | A logically distinct collection of network resources sharing a common trust level, security classification, and regulatory burden. Communication between zones is subject to policy enforcement points. |
| **Virtual Private Cloud (VPC)** | A logically isolated section of the AWS cloud where Meridian launches resources within a defined virtual network. Each VPC is a private, dedicated IP address space. |
| **Zero Trust Architecture (ZTA)** | A security model that eliminates implicit trust; every access request is authenticated, authorized, and continuously validated regardless of network origin. |

### 2.2 Acronyms

| Acronym | Full Name |
|---|---|
| ACL | Access Control List |
| BGP | Border Gateway Protocol |
| CASB | Cloud Access Security Broker |
| CIDR | Classless Inter-Domain Routing |
| CSPM | Cloud Security Posture Management |
| DLP | Data Loss Prevention |
| IDS/IPS | Intrusion Detection System / Intrusion Prevention System |
| NAC | Network Access Control |
| NAT | Network Address Translation |
| NGFW | Next-Generation Firewall |
| SASE | Secure Access Service Edge |
| SWG | Secure Web Gateway |
| TGW | AWS Transit Gateway |
| TLS | Transport Layer Security |
| VIF | Virtual Interface |
| VPC | Virtual Private Cloud |
| VPN | Virtual Private Network |
| WAF | Web Application Firewall |
| ZTNA | Zero Trust Network Access |

---

## 3. Roles and Responsibilities

This section defines the specific roles accountable and responsible for network security controls at Meridian Health Technologies. The authoritative source for role-to-individual mapping is maintained in the Meridian IAM Directory (Okta) and the Governance, Risk, and Compliance (GRC) platform.

### 3.1 RACI Matrix

| Activity / Decision | CISO | VP IT Ops | Director, InfraSec | Network Security Architect | Cloud Platform Engineer | Compliance Officer | SOC Analyst |
|---|---|---|---|---|---|---|---|
| Network Security Policy Approval | A | C | R | R | I | I | I |
| Firewall Rule Approval | A | C | R | R | C | I | I |
| Network Architecture Design | C | I | A | R | C | I | I |
| IDS/IPS Signature Tuning | I | I | A | C | C | I | R |
| Cloud NSG Rule Deployment | I | I | A | C | R | I | I |
| VPN Configuration & Access | I | C | A | R | C | I | I |
| Quarterly Firewall Rule Review | C | I | A | R | C | R | I |
| Network Incident Response | A | C | R | C | C | I | R |
| Compliance Evidence Collection | I | I | C | C | C | A | I |
| Penetration Test Remediation | A | C | R | R | R | I | C |
| Exception Approval (Temporary) | A | C | R | R | I | I | I |
| Exception Approval (Permanent) | A | R | C | C | I | I | I |

**Legend:** R = Responsible (executes), A = Accountable (signs off), C = Consulted, I = Informed

### 3.2 Named Role Responsibilities

**Rachel Kim, Chief Information Security Officer (CISO)**
- Approves this SOP and all subsequent revisions.
- Holds final accountability for network security control effectiveness.
- Reviews and signs off on all permanent exception requests.
- Presents quarterly network risk posture metrics to the AI Governance Committee.

**Samantha Torres, VP of IT Operations**
- Owns operational execution of network security controls across corporate IT and production environments.
- Ensures adequate staffing, tooling, and budget for 24/7/365 network security operations.
- Reviews and approves all change management tickets related to network architecture modifications.

**Director, Infrastructure Security (Reports to CISO)**
- Owns the technical content and day-to-day enforcement of this SOP.
- Chairs the weekly Network Security Change Advisory Board (NS-CAB).
- Approves all firewall rule changes and VPN configuration modifications.
- Coordinates the annual independent penetration testing engagement.

**Network Security Architect (Reports to Director, InfraSec)**
- Designs and maintains network segmentation schemas, trust zone definitions, and traffic flow diagrams.
- Executes semi-annual firewall rule certification reviews.
- Manages IDS/IPS signature lifecycle and tuning in collaboration with the SOC.
- Maintains the Network Security Architecture Document (NSAD) repository in Confluence.

**Cloud Platform Engineer (Reports to VP, Engineering)**
- Implements and manages AWS Security Groups, NACLs, Azure NSGs, and TGW route tables using Infrastructure as Code (Terraform).
- Ensures all cloud network changes are peer-reviewed via pull request and validated by CSPM tooling (Wiz).
- Maintains CIDR allocation and IP address management (IPAM) records.

**Compliance Officer, Thomas Anderson (Reports to CEO)**
- Leads SOC 2 evidence collection for Common Criteria CC6.1, CC6.6, CC6.7, CC7.1, and CC9.2.
- Performs control testing on a quarterly cadence; reports findings to the CISO and General Counsel.
- Tracks remediation items through the GRC platform (Vanta).

**SOC Analyst (Tier 2/3)**
- Monitors IDS/IPS alerts, NetFlow anomalies, and firewall deny logs via the Datadog SIEM dashboard.
- Escalates confirmed network intrusion events per the Incident Response Plan (SOP-ISEC-001).
- Performs initial triage of VPN access anomalies flagged by the UEBA module.

---

## 4. Policy Statements

### 4.1 High-Level Policy Commitments

Meridian Health Technologies, Inc. is committed to maintaining a defense-in-depth network security architecture that aligns with SOC 2 Trust Services Criteria, NIST AI RMF, and ISO 27001:2022 Annex A controls. The following policy statements are binding and non-negotiable:

**PS-1: Default-Deny Posture**
All network traffic is denied by default. Access is granted only upon explicit business justification, technical validation, and authorized approval. Every firewall rule, security group entry, and ACL must follow a least-privilege principle. Broad allow rules (e.g., `0.0.0.0/0` to administrative ports) are prohibited without a documented compensating control and CISO-approved exception.

**PS-2: Mandatory Segmentation**
All Meridian production environments shall be segmented into discrete trust zones based on data classification, regulatory scope, and operational criticality. PHI-bearing systems (Tier 0) shall be isolated from general application services (Tier 1) and corporate IT systems (Tier 2). No direct network path shall exist between Tier 0 and Tier 2 without traversing a policy enforcement point with full Layer 7 inspection.

**PS-3: Encryption in Transit**
All network traffic crossing VPC boundaries, trust zones, or traversing public networks must be encrypted using TLS 1.2 or higher. Internal service-to-service communication shall utilize mutual TLS (mTLS) where supported. VPN connections require AES-256-GCM or equivalent cipher suites. Unencrypted protocols (HTTP, FTP, Telnet) are explicitly prohibited on all production networks.

**PS-4: Continuous Monitoring**
All network segments shall be instrumented with flow log capture (VPC Flow Logs, Azure NSG Flow Logs), IDS/IPS sensors at zone boundaries, and NetFlow/sFlow collection at core routing points. Logs shall be centrally aggregated in the SIEM with a maximum ingestion latency of 5 minutes. Security events shall generate real-time alerts with P1/P2/P3 severity classification per SOP-ISEC-001.

**PS-5: Change Control**
All modifications to network security infrastructure—including firewall rule additions, security group changes, VPN endpoint reconfigurations, and IDS/IPS policy updates—shall follow the formal NS-CAB change management process. Emergency changes require post-hoc review within 24 business hours. No production network change may proceed without an approved change request ticket in ServiceNow.

**PS-6: Independent Assurance**
Network security controls shall undergo independent testing at least annually. This includes external and internal penetration testing, segmentation effectiveness testing, and firewall rule reviews. All identified findings shall be risk-rated, tracked, and remediated within timelines defined in SOP-ISEC-001.

**PS-7: Asset Inventory**
All network-connected assets, including ephemeral cloud resources, must be discovered and registered in the Configuration Management Database (CMDB) within 60 minutes of creation. Network asset inventory shall be reconciled against the CMDB weekly. Unidentified or unmanaged assets detected on production segments trigger a P2 security incident.

**PS-8: Remote Access**
All remote access to Meridian production networks shall utilize the corporate VPN (Palo Alto GlobalProtect) with multi-factor authentication (Okta Verify) and device posture checking. Split tunneling is disabled by default. Access to Tier 0 environments from remote locations requires a Privileged Access Workstation (PAW) or equivalent jump host with session recording.

---

## 5. Detailed Procedures

### 5.1 Network Architecture and Segmentation Model

This section details Meridian's multi-tier segmentation architecture, implemented identically across the primary (AWS us-east-1), EU (AWS eu-west-1), and disaster recovery (Azure East US) regions.

#### 5.1.1 Trust Zone Definitions

Meridian classifies all network assets into five trust zones. Each zone is instantiated as a dedicated VPC, set of subnets, or logical segment within the broader Meridian network fabric.

| Zone ID | Zone Name | Data Classification | Regulatory Burden | Examples |
|---|---|---|---|---|
| TZ-0 | Regulated High-Security | PHI, PII, Model IP | EU AI Act High-Risk, SOC 2 Confidentiality | Clinical AI inference endpoints, MedInsight PHI stores, HealthPay PII processing |
| TZ-1 | Production General | Confidential Business | SOC 2 Security & Availability | SaaS platform application servers, non-PHI analytics, CI/CD runners |
| TZ-2 | Corporate Services | Internal Only | ISO 27001 | Employee workstations, email, HR systems, finance, engineering dev environments |
| TZ-3 | DMZ / Public-Facing | Public | SOC 2 Availability | Reverse proxies, CDN origins, API gateways, HealthPay patient portal webservers |
| TZ-4 | Management & Monitoring | Confidential | SOC 2 Security | SIEM collectors, vulnerability scanners, configuration management, jump hosts |

**Segmentation Principle:** Direct network-layer communication from TZ-0 to TZ-2 is prohibited. Any necessary data flows must traverse an application-layer gateway (e.g., API Gateway with schema validation) or an approved Extract-Transform-Load (ETL) pipeline with data masking.

#### 5.1.2 AWS Production VPC Architecture (us-east-1)

The primary Meridian SaaS Platform and Clinical AI Platform are deployed within the `mht-prod-use1` VPC (CIDR: `10.16.0.0/16`).

**VPC Subnet Structure:**

| Subnet Name | CIDR Block | Availability Zone | Trust Zone | Purpose |
|---|---|---|---|---|
| `mht-prod-dmz-web-1a` | `10.16.1.0/24` | `us-east-1a` | TZ-3 | WAF origin servers, API Gateway endpoints |
| `mht-prod-dmz-web-1b` | `10.16.2.0/24` | `us-east-1b` | TZ-3 | Redundant WAF origin servers |
| `mht-prod-app-1a` | `10.16.11.0/24` | `us-east-1a` | TZ-1 | SaaS application containers, non-PHI services |
| `mht-prod-app-1b` | `10.16.12.0/24` | `us-east-1b` | TZ-1 | Redundant SaaS application containers |
| `mht-prod-data-t0-1a` | `10.16.101.0/24` | `us-east-1a` | TZ-0 | Clinical AI model inference, PHI-bearing Snowflake connectors |
| `mht-prod-data-t0-1b` | `10.16.102.0/24` | `us-east-1b` | TZ-0 | Redundant TZ-0 data services |
| `mht-prod-mgmt-1a` | `10.16.201.0/24` | `us-east-1a` | TZ-4 | SIEM forwarders, Datadog agents, CrowdStrike management |
| `mht-prod-vpn-transit` | `10.16.250.0/24` | `us-east-1a/b` | TZ-4 | VPN termination, AWS Client VPN endpoints |

**Routing and Connectivity:**

All inter-VPC and inter-zone traffic routes through the AWS Transit Gateway (`tgw-mht-prod`). The Transit Gateway enforces segmentation via route table isolation. Each VPC attachment is associated with a dedicated TGW route table that only permits routes to explicitly authorized destinations.

**TGW Route Table Configuration:**

| TGW Route Table | Associated VPC Attachments | Propagated Routes | Permitted Destinations |
|---|---|---|---|
| `tgwrt-dmz` | DMZ VPC | None (static only) | Internet Gateway (IGW) for inbound, Application VPC CIDR block |
| `tgwrt-app` | Application VPC | None (static only) | DMZ VPC, Data-T0 VPC, Shared Services VPC |
| `tgwrt-data-t0` | Data Tier 0 VPC | None (static only) | Shared Services VPC (via proxy only), ETL Pipeline VPC |
| `tgwrt-mgmt` | Management VPC | All VPCs | All VPCs (restricted to management traffic with NSGs) |
| `tgwrt-shared` | Shared Services VPC | None (static only) | All VPCs |

*Note: Route tables must be reviewed and certified quarterly as part of Procedure 5.7.*

#### 5.1.3 EU Region Architecture (eu-west-1)

The `mht-prod-euw1` deployment mirrors the us-east-1 architecture with additional controls mandated by the EU AI Act. Clinical AI inference endpoints in the EU region reside in a dedicated `mht-eu-ai-highrisk` VPC with no cross-region peering to us-east-1. Data residency is enforced via SCPs at the AWS Organizations level. The DPO (Dr. Klaus Weber) must approve any cross-region data transfer exceptions in conjunction with the CISO.

#### 5.1.4 Azure Disaster Recovery Architecture

The Azure East US DR environment uses Hub-Spoke topology. The Hub VNet hosts shared security appliances (Azure Firewall Premium, VPN Gateway). Spoke VNets mirror the trust zone model. Azure Policy enforces NSGs with a deny-all default rule at the subscription level. Cross-premises connectivity from AWS to Azure is via site-to-site VPN with BGP over redundant tunnels.

### 5.2 Firewall Management Procedure

Meridian utilizes Palo Alto Networks Next-Generation Firewalls (NGFW) as the primary policy enforcement point for north-south traffic and inter-zone east-west traffic. Cloud-native controls (AWS Security Groups, Azure NSGs) provide additional defense-in-depth at the resource layer.

#### 5.2.1 Firewall Rule Lifecycle

**Step 1: Request Initiation**
- Requester completes the "Firewall Rule Request" form in ServiceNow (catalog item `REQ-NET-001`), providing:
  - Source IP(s) or FQDN(s)
  - Destination IP(s) or FQDN(s)
  - Protocol/Port(s)
  - Application (if known to App-ID)
  - Business justification (minimum 200 characters required)
  - Data classification involved
  - Ticket reference for associated project or change
  - Requested duration (permanent or time-bound)

**Step 2: Pre-Validation**
- The ServiceNow workflow automatically queries the CMDB to verify that source and destination assets are registered and approved.
- If either asset is unregistered, the request is autocompelled to the CMDB registration workflow (`REQ-CMDB-001`).
- The workflow checks against a blocklist of prohibited rules (e.g., Tier 0 → Tier 2 direct, any source → RDP/3389 from internet).

**Step 3: Security Review**
- The Network Security Architect reviews the request within SLA:
  - Standard request: 2 business days
  - Expedited request (requires Director approval): 4 business hours
- Review includes:
  - Least-privilege verification (can we narrow the source/destination?).
  - Data classification consistency (does the flow respect zone boundaries?).
  - Threat assessment (does this open a new attack path?).
  - Application-layer risk (for App-ID rules, verify application baseline).

**Step 4: NS-CAB Approval**
- The weekly NS-CAB (Thursdays, 10:00–11:00 AM ET) reviews all standard requests.
- Quorum: Director of Infrastructure Security (Chair), Network Security Architect, one Cloud Platform Engineer, and one Compliance representative.
- Approved requests are assigned a unique rule ID (`FW-RULE-YYYY-NNNN`).

**Step 5: Implementation**
- For Palo Alto NGFW rules: Network Security Architect implements in Panorama, commits with change window ticket (`CHG-xxxx`), and pushes to target device group.
- For AWS Security Groups: Cloud Platform Engineer creates the Terraform PR, obtains peer review, merges, and applies via the Atlantis CI/CD pipeline.
- Change is logged in the change management system with firewall audit trail.

**Step 6: Post-Implementation Validation**
- Within 30 minutes of implementation, the SOC Shift Lead verifies:
  - Expected traffic is flowing (Datadog NetFlow dashboard).
  - No unintended flows were opened (NGFW policy optimizer).
  - No P1 alerts triggered in the SIEM related to the rule.
- Requester acknowledges successful traffic flow in the ServiceNow record.

**Step 7: Documentation**
- The rule, justification, approver, and implementation artifacts are stored in the Firewall Rule Repository (Confluence, space `SEC-NET`).

#### 5.2.2 Firewall Rule Standards

| Rule Property | Standard |
|---|---|
| Naming Convention | `[Zone_Origin]-[Zone_Dest]-[App]-[Port]` (e.g., `TZ1-TZ0-POSTGRES-5432`) |
| Source/Destination Specification | Use FQDN objects where possible; IP-based rules must specify static CIDR or reserved IP; `0.0.0.0/0` prohibited for non-DMZ rules |
| Service Specification | Use App-ID (Palo Alto) or application object. Never use `any` service unless justified and approved as exception. |
| Logging | All rules must have logging enabled at session end. Deny rules logged with Threat/Content logging enabled. |
| Rule Expiration | All rules carry a mandatory expiry tag (Permanent or `YYYY-MM-DD`). Rules without expiry tags are automatically disabled by Panorama policy compliance module. |
| Description | Must include requester name, ticket ID, and business justification summary. |

**Prohibited Rule Types:**
- Any rule allowing traffic directly from TZ-0 to TZ-2 without an application-layer proxy.
- Any rule allowing unencrypted administrative protocols (Telnet/23, HTTP/80 for login, FTP/21) in production VPCs.
- Any rule with source `any` to a destination in TZ-0 or TZ-1.
- Shadowed rules (rules fully contained within a broader rule above them).

### 5.3 IDS/IPS Configuration and Management

Meridian deploys intrusion detection and prevention sensors at all trust zone boundaries. The primary platform is Palo Alto Networks Threat Prevention, supplemented by AWS GuardDuty for cloud-native threat detection and CrowdStrike Falcon for host-based detection on all workloads.

#### 5.3.1 Sensor Placement

| Sensor Location | Technology | Mode | Monitors |
|---|---|---|---|
| Internet Edge (DMZ ingress) | Palo Alto NGFW Threat Prevention | Prevention (Inline) | All inbound traffic from untrusted sources |
| Inter-Zone Gateways (TGW inspection VPC) | Palo Alto NGFW Threat Prevention via VPC attachment | Prevention (Inline) | All east-west traffic crossing TZ boundaries |
| AWS VPC (all accounts) | Amazon GuardDuty | Detection | VPC Flow Logs, DNS logs, CloudTrail |
| Host-Level (all instances) | CrowdStrike Falcon | Prevention | Process, network, file system events |
| Azure Spoke VNets | Azure Firewall Premium IDPS | Detection/Alert | Spoke-to-spoke and egress traffic |

#### 5.3.2 Signature Management

- **Source:** Palo Alto Networks Applications and Threats content updates.
- **Update Schedule:** Automatic download every 24 hours (02:00 ET); install to Panorama at 04:00 ET.
- **Tuning Cadence:** The Network Security Architect and SOC Lead conduct a signature tuning session bi-weekly. Output is a list of signature exceptions (disabled signatures, adjusted thresholds).
- **High-Severity Signatures:** Critical and High severity signatures are installed in Prevention mode by default. Medium severity signatures are installed in Alert-Only mode for 14 days, reviewed, then promoted to Prevention if false-positive rate < 1%.
- **Custom Signatures:** The SOC may develop custom Snort-rule signatures for Meridian-specific application threats. Custom signatures must be validated in the staging environment (`mht-staging-use1`) for a minimum of 72 hours before production deployment.

#### 5.3.3 IDS/IPS Alert Handling

| Alert Severity | Response SLA | Action |
|---|---|---|
| Critical (P1) | 15 minutes | SOC initiates Incident Response per SOP-ISEC-001; automated blocking via PagerDuty-Datadog integration |
| High (P2) | 1 hour | SOC Tier 2 analyst investigates; manual containment if confirmed true positive |
| Medium (P3) | 4 hours | Queued for investigation during shift; correlated with other signals |
| Low / Informational | Next business day | Reviewed in SOC morning standup; bulk-dismissed or flagged for tuning |

### 5.4 VPN and Remote Access

#### 5.4.1 VPN Architecture

Meridian provides secure remote access via two distinct VPN services, both terminating within the Management VPC (`mht-prod-use1`, TZ-4).

| VPN Service | Technology | User Population | Authentication | Access Scope |
|---|---|---|---|---|
| Corporate VPN | Palo Alto GlobalProtect | All employees, contractors | Okta SSO + Okta Verify MFA + device posture (CrowdStrike) | TZ-2 (Corporate), TZ-4 (Management) |
| Production Admin VPN | AWS Client VPN with SAML | Infrastructure, SRE, on-call engineers | Okta SSO + YubiKey FIDO2 hardware token | TZ-4 (Management jump hosts), TZ-1/TZ-0 jump hosts (with explicit secondary authentication) |

#### 5.4.2 Production Admin VPN Access Procedure

Access to TZ-0 or TZ-1 environments from remote locations requires a multi-stage connection:

1.  **Establish Corporate VPN:** User authenticates to GlobalProtect. Device posture check verifies endpoint compliance (CrowdStrike running, disk encrypted, approved OS patch level). User now has TZ-2 access.
2.  **Establish Production Admin VPN:** From the corporate endpoint, user connects to AWS Client VPN with YubiKey. This is a distinct VPN tunnel with no split-tunneling; it routes only `10.16.0.0/16` addresses.
3.  **SSH/RDP to Bastion Host:** All production access is brokered through bastion hosts (`bastion-tz1.mht.internal`, `bastion-tz0.mht.internal`) residing in TZ-4. SSH keys are managed via HashiCorp Vault SSH secrets engine with certificate-based authentication. Password authentication is disabled.
4.  **Session Recording:** All sessions on TZ-0 bastion hosts are recorded via AWS Systems Manager Session Manager with output logged to an immutable S3 bucket. SOC reviews a random sample of 5% of recorded sessions weekly.

#### 5.4.3 Site-to-Site VPN

Site-to-site VPN tunnels connect Meridian office locations (Boston, London, Berlin, Singapore, Toronto) to the corporate VPC and between AWS and Azure. All S2S VPNs use:
- IKEv2 protocol.
- AES-256-GCM encryption.
- SHA-256 or higher integrity.
- Perfect Forward Secrecy (PFS) using Diffie-Hellman group 20 or higher.
- Pre-shared keys rotated every 90 days.

### 5.5 Network Access Control (NAC)

Cisco Identity Services Engine (ISE) enforces NAC in all Meridian office locations. All wired and wireless endpoints are authenticated via 802.1X using machine certificates issued by the Meridian internal CA (Microsoft AD CS).

**Posture Assessment:** Before network access is granted, the NAC evaluates:
- Presence of a valid Meridian-issued machine certificate.
- Current CrowdStrike Falcon sensor status (running, connected to cloud).
- OS patch level compliance (checked against SCCM/Jamf policy baseline).

**Enforcement Actions:**
- **Compliant:** Assigned to VLAN `CORP-EMP` (full TZ-2 access).
- **Non-Compliant (Missing Patch/AV):** Assigned to VLAN `CORP-REMED` (restricted internet access only; captive portal with remediation instructions).
- **Unknown/Guest:** Assigned to VLAN `GUEST-ISOLATED` (internet only, bandwidth throttled, 8-hour expiry, no access to Meridian internal resources).

### 5.6 Cloud Network Security Posture Management (CSPM)

Meridian uses Wiz as the primary CSPM platform. Wiz continuously evaluates AWS and Azure environments against the Meridian Cloud Network Security Baseline, detecting misconfigurations.

**Key CSPM Rules Enforced:**

| Rule ID | Description | Severity | Remediation SLA |
|---|---|---|---|
| `NET-001` | Security group allows `0.0.0.0/0` to administrative ports (22, 3389, etc.) | Critical | 4 hours |
| `NET-002` | VPC has no flow logs enabled | High | 24 hours |
| `NET-003` | S3 bucket has public access via bucket policy or ACL | Critical | 1 hour |
| `NET-004` | Unrestricted outbound internet access from TZ-0 subnet | High | 24 hours |
| `NET-005` | Azure NSG has no deny-all default rule | High | 24 hours |
| `NET-006` | Production subnet is not associated with an IDS/IPS sensor | Medium | 72 hours |

**Workflow:** CSPM alerts create automated tickets in ServiceNow, routed to the Cloud Platform Engineering on-call queue. Unremediated Critical findings escalate to the Director of InfraSec after 2 hours, then to the CISO after 4 hours.

### 5.7 Quarterly Firewall Rule Review Procedure

This mandatory procedure satisfies SOC 2 CC6.6 (Logical and Physical Access Controls) and CC7.1 (System Operations).

| Step | Actor | Action | Timeline |
|---|---|---|---|
| 1 | Network Security Architect | Exports full rulebase from Panorama and AWS Security Group inventory as CSV | Day 1 |
| 2 | Network Security Architect | For each rule, identifies: rules exceeding 180 days without modification, rules with `any` source/service (if any), shadowed or redundant rules, expired rules not removed | Day 2–7 |
| 3 | Director, InfraSec / Application Owner | Joint meeting to review each flagged rule. Rule owner must re-justify each rule. If owner cannot justify or has departed, rule is staged for removal. | Day 8–10 |
| 4 | Network Security Architect | Implements removals in a staged change window, with 14-day monitoring for impact | Day 14–21 |
| 5 | Compliance Officer | Generates Quarterly Firewall Rule Certification Report for SOC 2 evidence package, including: total rules reviewed, rules removed, rules justified, exceptions. | Day 25 |
| 6 | CISO | Reviews and signs the Certification Report | Day 30 |

### 5.8 Network Incident Containment Procedure

In the event of a confirmed network intrusion (P1), the SOC follows the containment playbook:

1.  **Identification:** SIEM alert fires; SOC Tier 2 confirms true positive.
2.  **Isolation (T+5min):** SOC Analyst executes the containment runbook in ServiceNow (`RP-NET-001`). Ansible Automation Platform pushes a dynamic address group to Panorama, isolating the affected host(s) to a `QUARANTINE-VLAN` segment. Quarantine group allows only forensic monitoring traffic outbound.
3.  **Evidence Capture (T+30min):** SOC collects VPC Flow Logs, firewall session logs, and CrowdStrike endpoint detection history for the affected asset and adjacent assets. Evidence is stored in the incident record.
4.  **Eradication and Recovery:** Per SOP-ISEC-001 Section 6.
5.  **Post-Incident Review:** Within 5 business days, the CISO chairs an incident retrospective. Outputs include updated firewall rules, IDS signatures, or procedural changes.

---

## 6. Controls and Safeguards

This section articulates the specific technical and administrative controls implemented to satisfy SOC 2 Trust Services Criteria. Each control is mapped to its primary TSC reference, control owner, measurement method, and target performance.

### 6.1 SOC 2 Controls Mapping

**Control Category: CC6 — Logical and Physical Access Controls**

| Control ID | Control Description | TSC Reference | Owner | Measurement Method | Target |
|---|---|---|---|---|---|
| ISEC-NET-001 | **Firewall Rule Management** — Formal documented process for rule lifecycle (request, approve, implement, review) | CC6.1 (Logical Access), CC6.6 (Access Restrictions) | Director, InfraSec | Quarterly rulebase certification; % of rules with valid owner and justification | 100% of rules justified; < 1% orphan rules |
| ISEC-NET-002 | **Default-Deny Posture** — All network traffic denied by default; access granted only via authorized rule | CC6.1, CC6.6 | Network Security Architect | CSPM (Wiz) continuous monitoring; manual penetration test | Zero findings of overly permissive (`0.0.0.0/0`) access to restricted ports |
| ISEC-NET-003 | **Network Segmentation** — Logical separation of environments by trust zone based on data sensitivity | CC6.1, CC6.6 | Network Security Architect | Annual segmentation effectiveness penetration test; CSPM checks | 100% compliance with zone isolation; zero unauthorized cross-zone paths |
| ISEC-NET-004 | **Remote Access MFA** — All VPN and remote access methods require multi-factor authentication | CC6.1, CC6.3 | VP, IT Operations | Okta admin console; Monthly MFA enforcement report | 100% of remote access users registered with MFA; 0% bypass |
| ISEC-NET-005 | **Device Posture Assessment** — NAC enforces endpoint compliance before granting network access | CC6.1 | Director, InfraSec | Cisco ISE posture report; % of non-compliant devices blocked | 100% of non-compliant or unauthenticated devices assigned to restricted VLAN |
| ISEC-NET-006 | **Encryption in Transit** — TLS 1.2+ required for all inter-zone, inter-VPC, and internet-facing traffic | CC6.7 (Encryption) | Director, InfraSec | CSPM (Wiz); AWS Security Hub; TLS version scan | 100% of public endpoints TLS 1.2+; 0% with TLS < 1.2 or SSL |

**Control Category: CC7 — System Operations**

| Control ID | Control Description | TSC Reference | Owner | Measurement Method | Target |
|---|---|---|---|---|---|
| ISEC-NET-007 | **IDS/IPS Deployment** — Intrusion detection sensors at all zone boundaries with signature updates every 24h | CC7.1 (Detection), CC7.2 (Monitoring) | Director, InfraSec | Datadog SIEM dashboard; sensor health checks by Nagios | 99.95% sensor uptime; 100% sensors at current signature version ( < 48h old) |
| ISEC-NET-008 | **Security Event Logging & Alerting** — All network security events centrally logged with real-time alerting | CC7.1, CC7.3 (Alerting) | SOC Manager & Director, InfraSec | SIEM log ingestion latency; alert response SLA adherence | Max log latency 5 min; P1 alert response 15 min (95% adherence) |
| ISEC-NET-009 | **Vulnerability Management** — Network devices scanned for known vulnerabilities monthly | CC7.1 | Director, InfraSec | Qualys vulnerability management platform | Critical vulnerabilities patched within 30 days; High within 90 days |
| ISEC-NET-010 | **Change Management** — All network security changes follow formal CAB process | CC7.2 (Change) | VP, IT Operations | ServiceNow change management compliance; % unauthorized changes | 100% of changes with approved Change Request; 0% unauthorized |
| ISEC-NET-011 | **Capacity Management** — Network bandwidth and firewall capacity monitored; thresholds defined | CC7.2 (Availability) | VP, IT Operations | Datadog network dashboards; circuit utilization | Aggregate link utilization < 70% at peak hour; firewall CPU < 80% |

**Control Category: CC9 — Risk Mitigation**

| Control ID | Control Description | TSC Reference | Owner | Measurement Method | Target |
|---|---|---|---|---|---|
| ISEC-NET-012 | **Network Penetration Testing** — Independent penetration test of network controls annually + continuous internal red team | CC9.1 (Risk Assessment) | Director, InfraSec | Penetration test engagement status; findings tracker | All Critical/High findings remediated within SLA per SOP-ISEC-001 |
| ISEC-NET-013 | **Third-Party Access Management** — Vendor/partner remote access governed by separate Vendor Access Policy (SOP-ISEC-009) and time-bound | CC9.2 (Vendor Management) | VP, IT Operations & Director, InfraSec | Vendor VPN access log review; time-bound access expiry | 100% vendor access with explicit expiry < 90 days; quarterly vendor access review |

### 6.2 Compensating Controls

If a technical control requirement cannot be met (e.g., a legacy medical device in a clinical integration scenario does not support TLS 1.2), the following compensating controls may be applied, subject to CISO written approval:

1.  **Network Isolation:** The non-compliant device is placed in a dedicated, isolated VLAN with no direct access to the broader Meridian network.
2.  **Application-Layer Gateway:** All communication to/from the device is proxied through an application gateway that terminates TLS 1.2 on behalf of the device.
3.  **Continuous Monitoring:** Enhanced logging and IDS/IPS rules are applied to the isolated segment.
4.  **Time-Bound Approval:** The compensating control exception is granted for a maximum of 12 months, with a remediation plan on file.

---

## 7. Monitoring, Metrics, and Reporting

### 7.1 Key Performance Indicators (KPIs)

The effectiveness of network security controls is measured through a defined set of KPIs, reported monthly to the CISO and quarterly to the AI Governance Committee.

| KPI ID | KPI Name | Definition | Target / SLA | Measurement Tool | Reporting Cadence |
|---|---|---|---|---|---|
| NET-KPI-01 | Firewall Rule Hygiene | % of firewall rules reviewed and justified within last 180 days | > 98% | Panorama / ServiceNow | Quarterly |
| NET-KPI-02 | IDS/IPS Sensor Uptime | % uptime of all inline IDS/IPS sensors over month | > 99.95% (measured monthly) | Datadog Synthetics | Monthly |
| NET-KPI-03 | Mean Time to Contain (MTTC) | Mean time from P1 network intrusion alert confirmation to asset isolation | < 15 minutes | ServiceNow Incident + SIEM timestamp | Monthly |
| NET-KPI-04 | MFA Enforcement Rate | % of VPN authentications utilizing MFA | 100% (no exceptions) | Okta System Log | Monthly |
| NET-KPI-05 | Critical Vulnerability Remediation | % of Critical (CVSS ≥ 9.0) network device vulnerabilities patched within 30-day SLA | > 95% | Qualys / Wiz | Monthly |
| NET-KPI-06 | CSPM Critical Finding Resolution | Time-to-remediate Critical cloud misconfigurations (NET-001, NET-003) | < 4 hours | Wiz / ServiceNow | Monthly |
| NET-KPI-07 | Unauthorized Change Rate | % of detected network security changes without an approved Change Request | < 1% | ServiceNow vs. Actual Config (Wiz drift detection) | Monthly |

### 7.2 Dashboards

The following dashboards are maintained in Datadog and shared with relevant stakeholders:

- **CISO Executive Dashboard:** Aggregate risk score, open Critical findings from CSPM, quarterly firewall certification status, penetration test summary, major incident timeline.
- **SOC Operations Dashboard:** IDS/IPS alert volume and severity over time, MTTC by shift, VPN anomaly detections, top denied traffic sources.
- **Infrastructure Security Engineering Dashboard:** Total firewall rules per zone, rule age distribution, TLS version distribution for public endpoints, bandwidth utilization per circuit, VPN tunnel uptime.
- **Compliance Dashboard (Vanta):** Per-control evidence status, upcoming evidence collection deadlines, SOC 2 control testing results, auditor requests.

### 7.3 Reporting Cadence

| Report Name | Frequency | Recipients | Content |
|---|---|---|---|
| SOC Weekly Operations Report | Weekly (Mondays) | SOC Manager, Director InfraSec | P1/P2 incidents summary; IDS tuning changes; VPN access anomalies; shift metrics |
| Monthly Network Security Metrics Report | Monthly (5th business day) | CISO, VP IT Ops, VP Engineering | All KPIs; trend analysis; pending exceptions; capacity forecast; upcoming audits |
| Quarterly Control Certification Report | Quarterly (last week) | CISO, Compliance Officer, External Auditors (upon request) | Firewall rule certification; segmentation test results; KPI compliance; vulnerability aging; vendor access review |
| Annual Network Security Posture Report | Annually (December) | Board of Directors, CEO, CISO | Risk posture summary; penetration test findings; major architectural changes; regulatory compliance status; FY strategy |

---

## 8. Exception Handling and Escalation

### 8.1 Exception Definition

An exception to this SOP is defined as any deviation from the mandatory policy statements (Section 4), procedural requirements (Section 5), or control specifications (Section 6). Common exception types include:

- Temporary firewall rule with `any` source, not in compliance with PS-1.
- Legacy device running TLS 1.1 or lower in a TZ-1 segment.
- Administrative access to production from a non-PAW endpoint.
- Bypassing NS-CAB approval for an emergency change.
- Extended vulnerability remediation beyond SLA.

### 8.2 Exception Process

| Step | Action | Timeline |
|---|---|---|
| 1 | **Request:** Requester completes "Information Security Exception Request" form in ServiceNow (`REQ-EXCP-001`), detailing the specific policy/control being excepted, detailed business justification, compensating controls implemented, requested duration, and risk acknowledgement. | — |
| 2 | **Technical Review:** Network Security Architect reviews the request, validates the compensating controls, and provides a technical risk rating (Low, Medium, High, Critical). | 2 business days |
| 3 | **Director Approval:** Director of Infrastructure Security reviews and may approve Low/Medium exceptions for a maximum of 90 days. | 1 business day |
| 4 | **CISO Approval:** All High/Critical risk exceptions and any exception exceeding 90 days must be approved by the CISO. The CISO may impose additional compensating controls or a shorter duration. | Per CISO availability; target 5 business days |
| 5 | **Tracking & Remediation:** Approved exceptions are tracked in the GRC platform (Vanta) with the expiration date. A linked remediation project is created in Jira, assigned to the responsible team. | Upon approval |
| 6 | **Renewal:** Exceptions may be renewed once by re-submission with updated justification. Permanent exceptions require CISO and CEO approval and must be documented as an acknowledged control deficiency. | Before expiration |

### 8.3 Emergency Change Exception

In the event of a P1 incident requiring an immediate, non-standard network change (e.g., temporarily opening a broad rule to restore service), the responding engineer may execute the change without prior NS-CAB approval. The engineer must:

1.  Verbally notify the SOC Shift Lead and Director of Infrastructure Security.
2.  Log the temporary change with a "EMERGENCY" tag in the management console.
3.  Open a retroactive ServiceNow change request and exception request within 2 business hours.
4.  The temporary change is automatically scheduled for review and removal/remediation within 24 hours.

### 8.4 Escalation Path

| Level | Escalation Contact | Escalation Trigger |
|---|---|---|
| Level 1 — SOC Analyst | Tier 2 SOC Lead | IDS alert not triaged within 15 minutes |
| Level 2 — SOC Lead | Director, InfraSec | Confirmed P1 incident; containment action required |
| Level 3 — Director, InfraSec | CISO (Rachel Kim) | P1 incident not contained within SLA; critical system unavailability; forensic evidence indicates potential data exfiltration |
| Level 4 — CISO | CEO (Dr. Sarah Chen), General Counsel | Confirmed data breach; regulatory notification trigger |

---

## 9. Training Requirements

### 9.1 Training Assignments

Personnel with network security responsibilities must complete the following training:

| Training Module | Target Audience | Frequency | Delivery Method | Tracking |
|---|---|---|---|---|
| `SEC-TRN-NET-001`: Network Security Policy & Procedures | All Infrastructure Engineering, SRE, SOC personnel | Annually (initial within 30 days of hire) | LMS (Workday Learning) with quiz; 80% passing score | Workday Learning transcript |
| `SEC-TRN-NET-002`: Firewall Rule Management & Review Process | Network Security Architect, Cloud Platform Engineers, Directors | Annually + upon process change | Instructor-led workshop by Director, InfraSec | Attendance tracked in ServiceNow |
| `SEC-TRN-NET-003`: Secure Cloud Networking (AWS/Azure) | Cloud Platform Engineers, DevOps | Annually | A Cloud Guru / Pluralsight assigned path | LMS completion API integration |
| `SEC-TRN-INCIDENT-001`: Incident Response Tabletop | All SOC, Director InfraSec, VP IT Ops | Semi-annually | Facilitated scenario-based tabletop | After-action report filed in GRC |
| `SEC-TRN-GEN-001`: Security Awareness (Phishing, Physical Security) | All Meridian employees | Annually | LMS (KnowBe4) | Workday Learning transcript |

### 9.2 Training Compliance

- Training compliance is reported monthly to VP, IT Operations and Director, InfraSec.
- Overdue training ( > 30 days past due) results in notification to the individual and their manager.
- Overdue training ( > 90 days past due) may result in temporary suspension of production access credentials (Ok group membership changes) pending completion.

---

## 10. Related Policies and References

### 10.1 Internal Meridian SOPs

| SOP ID | Title | Relationship to This SOP |
|---|---|---|
| SOP-ISEC-001 | Information Security Incident Response Plan | Defines escalation and IR procedures referenced herein |
| SOP-ISEC-002 | Access Control and Identity Management | Defines user provisioning and MFA policies |
| SOP-ISEC-005 | Cryptography and Key Management | Detailed TLS certificate management and encryption standards |
| SOP-ISEC-007 | Endpoint Security Standards | PAW and endpoint posture standards for NAC |
| SOP-ISEC-008 | Vulnerability Management Program | Detailed vulnerability scanning SLAs and remediation workflows |
| SOP-ISEC-009 | Third-Party and Vendor Access Management | Vendor VPN and network access control policy |
| SOP-CSP-001 | Cloud Security Posture Management | Wiz CSPM tool configuration and alert management |
| SOP-BCDR-002 | Network Disaster Recovery Plan | Azure DR connectivity and failover procedures |

### 10.2 External Standards and Frameworks

- AICPA Trust Services Criteria (TSP Section 100, 2017) – SOC 2 Common Criteria (CC6, CC7, CC9)
- NIST Special Publication 800-53 Rev. 5 – Controls AC-4, AC-17, CA-3, CA-8, CM-2, SC-7, SC-8, SI-4
- NIST Special Publication 800-207 – Zero Trust Architecture
- ISO/IEC 27001:2022 – Annex A Controls A.8.1, A.8.2, A.8.20–A.8.24, A.8.26
- PCI DSS v4.0 – Requirements 1 and 7 (for HealthPay environments)
- AWS Well-Architected Framework – Security Pillar (Network Protection)

### 10.3 Internal Reference Documents

- Meridian Network Security Architecture Document (NSAD) v7.2 – Confluence `SEC-NET/NSAD`
- Meridian Cloud Security Baseline – Wiz Policy Set `MHT-BASELINE-NET`
- Meridian Threat Model – Clinical AI Inference Pipeline (`TH-MOD-CAI-2024`)
- Meridian ServiceNow Change Management Policy (`POL-CHG-002`)

---

## 11. Revision History

| Version | Date | Author | Reviewer | Description of Changes |
|---|---|---|---|---|
| 1.0 | 2019-03-22 | Michael Torres (Former CISO) | Sarah Chen | Initial publication. Consolidated firewall, IDS, and VPN procedures. |
| 2.1 | 2020-01-17 | Jennifer Liu (Network Architect) | Michael Torres | Added AWS VPC segmentation and Transit Gateway architecture. |
| 3.2 | 2021-08-05 | Rachel Kim (CISO) | Samantha Torres | Implemented Zero Trust segmentation model. Introduced TZ-0 through TZ-4 classification. Added CSPM automation with Wiz. |
| 4.0 | 2023-06-14 | Rachel Kim | Dr. Sarah Chen | Major revision: Full SOC 2 control mapping. New Cloud Network Security section. VPN architecture updated (PAW requirement). Added KPI dashboard and quarterly certification requirements. |
| 4.3 | 2024-02-20 | Marcus Okonkwo (Director, InfraSec) | Rachel Kim | EU AI Act high-risk isolation added. Azure Hub-Spoke DR architecture. IDS/IPS tuning cadence changed to bi-weekly. |
| 4.5 | 2024-08-11 | Marcus Okonkwo | Rachel Kim | Updated encryption cipher suite requirements. Added CrowdStrike NAC posture. Revised S2S VPN pre-shared key rotation. |
| **4.6** | **2024-11-05** | **Rachel Kim** | **Dr. Sarah Chen** | **Current version.** Added Named Roles in RACI. Added Section 5.7 Quarterly Review detailed steps. Added Section 5.8 Incident Containment runbook. Updated KPI thresholds. Clarified emergency exception notification timeline. Aligned with SOP-ISEC-009 for vendor access controls. |

*End of Document. Printed copies are uncontrolled. Refer to the Meridian Policy Portal (Vanta) for the current version.*
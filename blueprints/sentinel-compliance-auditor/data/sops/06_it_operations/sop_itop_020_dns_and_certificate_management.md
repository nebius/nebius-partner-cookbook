---
sop_id: "SOP-ITOP-020"
title: "DNS and Certificate Management"
business_unit: "IT Operations & Infrastructure"
version: "3.0"
effective_date: "2025-05-19"
last_reviewed: "2026-09-08"
next_review: "2027-03-06"
owner: "Samantha Torres, VP of IT Operations"
approver: "David Park, VP of Engineering"
classification: "Internal"
regulations:
  - "SOC 2"
status: "Active"
---

# Standard Operating Procedure: DNS and Certificate Management

## 1. Purpose and Scope

### 1.1 Purpose

This Standard Operating Procedure (SOP) establishes the governance framework, operational procedures, and technical controls for the lifecycle management of the Meridian Health Technologies, Inc. ("Meridian") Domain Name System (DNS) infrastructure and all digital certificates deployed across the organization's technology ecosystem. The integrity, availability, and confidentiality of Meridian's clinical AI platforms, financial services applications, and cloud infrastructure are fundamentally dependent upon the trustworthy resolution of domain names and the cryptographic assurance provided by X.509 digital certificates.

The purpose of this document is to mitigate risks associated with service outages caused by expired or misconfigured certificates, domain hijacking, DNS cache poisoning, and unauthorized certificate issuance, thereby ensuring continuous, secure operations supporting patient care workflows and financial transactions.

### 1.2 Scope

This SOP applies to the following assets, environments, and personnel:

**In-Scope DNS Infrastructure:**
- All authoritative DNS zones owned and managed by Meridian, including but not limited to: `meridianhealth.com`, `meridianclinical.net`, `meridian-fin.com`, `meridian.ai`, and related internal-only TLD zones hosted on Meridian's Route 53 Resolver endpoints.
- Public-facing authoritative DNS services managed via Amazon Route 53, Cloudflare (for DDoS-protected endpoints serving the `meridianhealth.com` patient portal), and Microsoft Azure DNS for DR-specific subdomains.
- Internal recursive and authoritative DNS resolvers operating within Meridian's Virtual Private Cloud (VPC) environments and on-premises data centers in Austin, TX, and Dublin, IE, utilizing a combination of CoreDNS and Microsoft Active Directory-integrated DNS zones.

**In-Scope Digital Certificates:**
- All X.509 certificates (TLS/SSL, client authentication, code signing, S/MIME for secure inter-system email, and mutual TLS certificates for service mesh communications) issued by Meridian-managed Private Certification Authorities (CAs) and publicly trusted CAs (AWS Certificate Manager Private CA, DigiCert, Let's Encrypt via automated ACME clients).
- Certificates deployed on all Meridian-managed assets including, but not limited to: Application Load Balancers (ALBs) serving `api.meridianclinical.net`, Amazon CloudFront distributions for the static assets of the Radiological Image Viewer, F5 BIG-IP Local Traffic Manager (LTM) virtual servers, Istio ingress gateways within the EKS clusters hosting the Clinical Decision Support (CDS) microservices, SSH host keys managed centrally via HashiCorp Vault, and individual end-user client certificates on YubiKey tokens issued to senior infrastructure engineers.

**Out-of-Scope:**
- Certificates issued to end-users for Personal Identity Verification (PIV) or physical access control systems. These are managed per SOP-ITOP-014.
- DNS configurations managed by third-party Software-as-a-Service (SaaS) providers on behalf of Meridian (e.g., Salesforce.com CDN routing), except where a Meridian-managed CNAME record directs traffic to that provider.

### 1.3 Applicability

All personnel responsible for the deployment, maintenance, and security of Meridian's IT infrastructure, including full-time employees, contractors, and managed service partners operating under a Master Services Agreement (MSA), must adhere to this SOP. Compliance is mandatory for all production, staging, development, and disaster recovery environments.

## 2. Definitions and Acronyms

| Term | Definition |
|---|---|
| **ACME** | Automated Certificate Management Environment. A protocol for automated domain validation and certificate issuance, primarily used with Let's Encrypt. |
| **ACM** | AWS Certificate Manager. A service for provisioning, managing, and deploying public and private TLS certificates for use with AWS services. |
| **CDS** | Clinical Decision Support. A class of Meridian microservices providing real-time analytics for clinicians. |
| **CNAME** | Canonical Name Record. A DNS record type mapping an alias name to the true, canonical domain name. |
| **CN** | Common Name. A legacy field within an X.509 certificate's Subject field; superseded by Subject Alternative Names. |
| **CORS** | Cross-Origin Resource Sharing. A mechanism allowing restricted resources on a web page to be requested from another domain. |
| **CSR** | Certificate Signing Request. An encoded message sent from an applicant to a CA to apply for a digital certificate. |
| **DNSSEC** | Domain Name System Security Extensions. A suite of IETF specifications for securing DNS by adding cryptographic signatures to existing DNS records. |
| **EKS** | Amazon Elastic Kubernetes Service. Meridian's primary platform for container orchestration. |
| **FQDN** | Fully Qualified Domain Name. A domain name that specifies its exact location in the tree hierarchy of the DNS. |
| **HSM** | Hardware Security Module. A dedicated crypto-processor for safeguarding digital keys. Meridian uses AWS CloudHSM for Private CA key material. |
| **Istio** | An open-source service mesh that provides TLS mutual authentication between microservices. |
| **MPKI** | Managed Public Key Infrastructure. Refers to Meridian's third-party, publicly-trusted certificate authority vendor (DigiCert). |
| **PKI** | Public Key Infrastructure. The set of roles, policies, hardware, software, and procedures needed to create, manage, distribute, use, store, and revoke digital certificates. |
| **R53** | Amazon Route 53. Meridian's authoritative DNS service for public and private hosted zones. |
| **SAN** | Subject Alternative Name. An extension to X.509 allowing various values to be associated with the certificate subject, including FQDNs. |
| **SOA** | Start of Authority. An essential DNS record containing administrative information about a zone, primarily the zone's serial number. |
| **TTL** | Time to Live. The lifespan of a DNS resolver's cache for a given record, measured in seconds. |
| **Zone Apex** | The root of a DNS zone (e.g., `meridian.ai` without a prefix like `www`). |

## 3. Roles and Responsibilities

| Role | Responsibility (RACI Model) | Assigned To |
|---|---|---|
| **DNS & Certificate Governance Council** | **A: Accountable** for overarching policy, audits, and approval of Private CA hierarchy changes. Reviews and approves all exception requests under Section 8. | Samantha Torres (Chair), Cloud Security Architect, Principal SRE |
| **Infrastructure Operations Lead** | **R: Responsible** for the execution of all operational procedures, including record creation, certificate provisioning, automation maintenance, and incident response related to DNS/Certs. | Rotating role among Senior Network Reliability Engineers (NREs) |
| **Domain Registrar Authority** | **R: Responsible** for maintaining relationships with domain registrars (MarkMonitor, AWS), executing domain renewals, and securing registrar-level account access. | IT Vendor Management & Finance, with technical execution by NREs |
| **DevOps Platform Engineering Team** | **C: Consulted** in the design of automation workflows, the Istio mesh configuration, and ACME client provisioning for Kubernetes clusters. | Team Lead, Platform Engineering |
| **Information Security (InfoSec) Team** | **C: Consulted & I: Informed.** Responsible for defining cryptographic standards (key lengths, algorithms), validating revocation procedures, and receiving real-time alerts for anomalous certificate activity via SIEM. | CISO Org, Security Engineering Pod |
| **Application Owners (Clinical/Finance)** | **I: Informed.** Must be notified of upcoming major PKI changes, scheduled maintenance, and receive quarterly reports on aggregate DNS/Certificate health for their service domain. | Named contacts in the Service Catalog (SVC-CAT) |

## 4. Policy Statements

Meridian's IT Operations and Infrastructure division, under the authority of the VP of IT Operations, mandates the following:

- **4.1 Cryptographic Standards:** All publicly trusted certificates must use RSA keys of at least 2048-bit length or ECDSA keys using the P-256 curve or stronger. The signature algorithm must be SHA-256. All Meridian-issued private certificates must use ECDSA P-384 keys. Certificates using weak or deprecated algorithms (e.g., SHA-1) are prohibited.
- **4.2 Automated Renewal Mandate:** Any certificate lifecycle exceeding 30 days must be managed by an automated provisioning and renewal system (e.g., `cert-manager` for Kubernetes, ACM for AWS-integrated services). Manual provisioning is only permissible for legacy systems granted a specific exception under Section 8. Automated renewal must be tested in a non-production environment within 24 hours prior to production renewal windows.
- **4.3 DNS as Code:** All changes to production authoritative DNS zones must be executed via infrastructure-as-code pipelines (Terraform/Terragrunt) and subjected to peer review via pull request. Direct, ad-hoc edits via the AWS Management Console, Cloudflare dashboard, or Azure Portal are strictly prohibited outside of Incident Response (IR) procedures and must be codified within 24 hours post-incident.
- **4.4 Zone Integrity:** DNSSEC must be enabled and key rollovers automated for all public-facing, Internet-facing zones managed in Route 53. Zone transfers to non-Meridian nameservers are forbidden. SOA serial numbers must be managed automatically by the provider.
- **4.5 Certificate Transparency:** All publicly trusted certificates issued for Meridian domains must be logged to Certificate Transparency (CT) logs. Meridian's SIEM (Splunk) must ingest CT log data feeds for Meridian domains to detect unauthorized issuance events.
- **4.6 Domain Registrar Lock:** All production domains (`meridianhealth.com`, `meridian.ai`, etc.) must have registrar-lock, transfer-lock, and client-delete-prohibited statuses set. Multi-factor authentication (MFA) using a FIDO2 hardware token is mandatory for all registrar portal user accounts.

## 5. Detailed Procedures

### 5.1 DNS Governance: Zone Creation and Delegation

This procedure covers the creation of a new public or private DNS zone for a new product or business unit.

1.  **Request Initiation:** The requesting Application Owner submits a "New DNS Zone" ticket to the IT Service Desk (Jira Service Management). The ticket must specify the desired domain name, its purpose (public-facing or internal VPC), the owning cost center, and any immediate delegation requirements.
2.  **Validation and Governance Review:** The Infrastructure Operations Lead triages the ticket. For public zones, a check is performed against the Meridian Domain Name Strategy (Wiki Document: DOM-STRAT-01) to ensure alignment with branding and legal requirements. A check is run to prevent zone fragmentation (e.g., rejecting a `west.meridian.ai` zone if `meridian.ai` is an existing zone where a simple subdomain record would suffice).
3.  **Terraform Module Instantiation:** The Lead NRE authorizes the creation and assigns an engineer to build the Terraform module. The standard module (`terraform-meridian-dns-zone`) provisions the hosted zone in the appropriate AWS account (`prod-core-net`, `nonprod-dev-net`, etc.). The module configures:
    - The zone name and comment.
    - The default SOA and NS records.
    - Enables query logging to an S3 bucket (`meridian-dns-logs-{region}-{account-id}`).
4.  **Git Merge Request:** The Terraform code is committed to the `meridian-infra/terraform-live` repository and a Merge Request (MR) is created. The MR must be reviewed and approved by a second NRE. The CI pipeline (`Atlantis`) executes a `terraform plan` and posts the output to the MR thread.
5.  **Delegation (Public Zones):** If the new zone is a subdomain of an existing Meridian public zone (e.g., `care.meridianhealth.com`), or if it's a new registered domain, the parent zone's Terraform code must be updated to include the new NS delegation records. The registrar’s nameserver records are updated via the MarkMonitor API using a separate `terraform` workspace for `domain-registration`.
6.  **Post-Creation Validation:** After `terraform apply` completes, the assigned engineer runs a validation suite (`dns-validator-toolset`) to confirm authoritative resolution and query logging. The Jira ticket is updated with the new zone's ID (e.g., `/hostedzone/Z0123456789ABCDEFGHI`) and resolved.

### 5.2 DNS Record Lifecycle Management (Standard Change)

This procedure covers the creation, modification, and deletion of standard DNS records (A, CNAME, TXT, MX).

1.  **Code-Driven Change:** All standard changes must originate from a Terraform definition of the record. For example, creating a new A record Alias to a CloudFront distribution:
    ```hcl
    resource "aws_route53_record" "patient_portal_cdn" {
      zone_id = data.aws_route53_zone.meridian_health_prod.zone_id
      name    = "portal.meridianhealth.com"
      type    = "A"

      alias {
        name                   = aws_cloudfront_distribution.patient_portal.domain_name
        zone_id                = aws_cloudfront_distribution.patient_portal.hosted_zone_id
        evaluate_target_health = false
      }
    }
    ```
2.  **TTL Configuration Standard:** TTLs must be set based on the record's volatility and purpose. The standard TTL matrix is:
    - **Static, stable records (e.g., MX records):** 86400 seconds (24 hours).
    - **Standard infrastructure (ALBs, EC2 public IPs):** 300 seconds (5 minutes).
    - **CloudFront/fast-changing CDN:** 60 seconds.
    - **Failover/health-check routing records:** 60 seconds.
    - **_dns-01 ACME Challenge TXT Records:** 60 seconds (provisioned and destroyed automatically by `cert-manager`).
3.  **Merge Request and CI:** The developer opens an MR to the target branch (e.g., `prod`). Atlantis executes a `terraform plan`. The reviewer verifies the diff for accuracy, syntax, and security implications (e.g., preventing zone takeover vulnerabilities on dangling CNAMEs).
4.  **Health Check Association (Critical Services):** For records supporting critical clinical or financial services (tagged with `criticality: high` in Terraform), the engineer must associate a Route 53 health check with the record's failover routing policy at creation time. This is achieved by including the `aws_route53_health_check` resource in the same module.
5.  **Post-Apply Verification:** After `terraform apply`, the engineer uses `dig` +`dnssec` against Meridian's resolver IPs to confirm the change is correctly served. They also wait a duration equal to the *previous* TTL value to ensure any negative-caching effects have expired if a record was modified. The Jira ticket is closed only after this verification window.

### 5.3 Certificate Lifecycle: Automated TLS via ACME and `cert-manager`

This is the primary procedure for all certificates within the Kubernetes ecosystem and any ACME-compatible public endpoint.

1.  **Resource Definition:** Certificate resources are defined declaratively in Kubernetes manifest files and stored in the `meridian-services` monorepo.
    ```yaml
    apiVersion: cert-manager.io/v1
    kind: Certificate
    metadata:
      name: cds-api-public-tls
      namespace: clinical-ops-prod
    spec:
      secretName: cds-api-prod-tls-secret
      duration: 2160h # 90 days
      renewBefore: 720h # 30 days before expiry
      dnsNames:
        - api.clinicaldecisionsupport.meridian.ai
      issuerRef:
        kind: ClusterIssuer
        name: letsencrypt-prod-dns01
      privateKey:
        rotationPolicy: Always
        algorithm: ECDSA
        size: 384
    ```
2.  **Issuer Configuration:** The referenced `ClusterIssuer`, `letsencrypt-prod-dns01`, is a global resource managed by the Platform Engineering team. It is configured to use ACME DNS-01 challenge solving against a Meridian AWS account (Route 53) via an IAM role for service accounts (IRSA). This allows validation without exposing any internal service.
3.  **Automated Lifecycle:** Upon creation, `cert-manager` handles the entire lifecycle:
    - Generates a private key stored in a Kubernetes Secret.
    - Creates a CSR and asks the Issuer to sign it.
    - The ACME issuer creates a temporary `TXT` record in the designated R53 zone to prove domain ownership.
    - It waits for authoritative resolution of the TXT record and then completes the certificate order.
    - It stores the issued certificate and private key in the specified Kubernetes Secret (`cds-api-prod-tls-secret`).
    - A `cert-manager` controller monitors the `renewBefore` field and automatically repeats the process to renew the certificate before it expires.
4.  **Application Integration:** Applications (like the CDS API Gateway) are configured to read their TLS configuration directly from the Kubernetes Secret referenced in the Ingress resource. A rolling restart of the pods is triggered by `cert-manager` upon certificate renewal using a `cni` plugin to ensure zero-downtime key reloading.

### 5.4 Certificate Lifecycle: Manual and Legacy Procedure

For systems that cannot, through a formally approved exception under Section 8, be integrated into an automated pipeline, the following manual procedure is strictly enforced.

**5.4.1 CSR Generation and Submission**
1.  The application owner must generate a 4096-bit RSA private key (or P-256 ECDSA) outside of the target system if possible, using `openssl` or a Hardware Security Module (HSM).
2.  A Certificate Signing Request (CSR) is generated with all required SANs for the service.
3.  The CSR and a completed "Manual Certificate Request Form" are submitted via the internal Meridian DigiCert MPKI portal. The form must include:
    - Certificate profile (Standard OV, EV, Code Signing).
    - An expiry date exactly one year from the date of submission.
    - Primary technical contact (individual, not a distribution list).
    - Secondary contact (must be a distribution list: e.g., `dl-{app}-admins@meridianhealth.com`).

**5.4.2 Validation and Issuance**
1.  The PKI Administrator (within InfoSec) validates the request against the approved exception catalog, domain ownership (for SANs), and profile use-case.
2.  The Administrator approves the request in DigiCert. For Organization Validation (OV) and Extended Validation (EV) certificates, DigiCert's organization vetting processes apply.
3.  The issued certificate bundle (end-entity certificate, intermediate(s)) is downloaded from the DigiCert portal by the requestor.

**5.4.3 Installation, Audit, and Expiry Management**
1.  Installation is performed during a scheduled change window. The private key must be handled per SOP-ITOP-007 (Secrets Management), which prohibits storing private keys in plaintext on shared filesystems.
2.  **Critical Mandate:** The technician installs the certificate and *immediately* creates a calendar entry (in the `#infra-dns-cert-alerts` Slack channel's shared Google Calendar) for two milestones:
    - **90-day Renewal Initiation Reminder:** A date 275 days from installation.
    - **Expiry Deadline:** A hard deadline 365 days from installation.
3.  The service is added to a manual quarterly audit list maintained in Confluence. Failure to complete the renewal before the expiry deadline results in a Priority-1 (P1) incident post-expiry.

### 5.5 Certificate Revocation

Immediate revocation of a certificate is required upon suspicion or confirmation of key compromise, or when a service is decommissioned.

1.  **Incident Declaration:** A compromised key is a critical security incident. The discoverer must immediately invoke the Incident Response Plan (SOP-SEC-002) via the PagerDuty `security-compromise` escalation path. A "Certificate Revocation" Jira ticket of type "Incident" must be created.
2.  **Containment (Isolation):** Simultaneously, the first responder identifies all systems using the compromised certificate and removes the trust by replacing the certificate with a newly issued one, effectively neutralizing the compromised key.
3.  **Revocation Submission (Public Certificates):**
    - Navigate to the DigiCert MPKI portal. Locate the compromised certificate order.
    - Select "Revoke Certificate." From the "Reason for Revocation" dropdown, select `Key Compromise`.
    - Add comments linking to the incident ticket and a SHA-256 fingerprint of the compromised certificate's public key for audit trail clarity.
    - Submit the request. DigiCert will publish the revocation to OCSP responders and CRLs within minutes.
4.  **Revocation Submission (Private Certificates):**
    - For certificates issued by Meridian's Private CA (AWS ACM PCA), a member of the InfoSec team with the `PCA-Admin` role logs into the AWS Management Console, navigates to ACM PCA, and revokes the certificate using the certificate serial number. The reason code is set to `KEY_COMPROMISE`.
5.  **Post-Incident Audit:** A thorough post-incident review (PIR) must be conducted to determine the scope of the compromise and ensure the CRL is functioning correctly for all relying parties.

## 6. Controls and Safeguards

### 6.1 Administrative Controls

| Control ID | Control Description |
|---|---|
| **DNS-ADMIN-01** | **Segregation of Duties:** The ability to submit a DNS change via MR is separated from the authority to approve and apply it. A Terraform plan cannot be applied without the approval of an Infrastructure Operations Lead or delegate who did not author the MR. |
| **CERT-ADMIN-02** | **Certificate Request Approval:** All manual certificate requests must be approved by the PKI Administrator. The approver cannot be the same individual who generated the CSR. |
| **CERT-ADMIN-03** | **Private Key Custody:** Private keys for certificates, regardless of issuance method, must never be transmitted via email, Slack, or ticketing systems. Transfer must occur via `scp` to a hardened, ephemeral endpoint during a scheduled change window, or via secrets management tools (HashiCorp Vault). |

### 6.2 Technical Controls

| Control ID | Control Description |
|---|---|
| **DNS-TECH-01** | **Source of Authority:** The `SOA` MNAME for all Meridian zones is set to authoritative nameservers managed exclusively by Meridian. The RNAME is `hostmaster.meridian.net`. SOA Expiry time is set to a fixed 4-week period (2419200 seconds). |
| **DNS-TECH-02** | **DNSSEC:** DNSSEC signing is enabled via Route 53's automated KSK/ZSK management for all production public zones. Rollovers are performed automatically by AWS with no operational overhead. |
| **CERT-TECH-03** | **Automated Renewal (ACME):** All non-legacy environments rely on `cert-manager` and the ACME protocol for certificate lifecycle. No manual intervention is permitted. |
| **CERT-TECH-04** | **Service Mesh Encryption:** All east-west traffic within the Kubernetes clusters is encrypted via Istio’s mutual TLS (mTLS) feature, which uses short-lived (24-hour) citizen certificates automatically issued by the Istio control plane. This operates independently from application-facing TLS certificates. |
| **CERT-TECH-05** | **CT Log Monitoring:** The InfoSec SOAR platform (Tines) ingests a feed of all certificates logged by Certificate Transparency for `*.meridianhealth.com` and `*.meridian.ai`. Any certificate not present in the DigiCert or AWS ACM inventory generates a `HIGH` severity alert in Splunk for immediate investigation. |

### 6.3 Availability Safeguards

To support the availability commitments for the critical services relying on this infrastructure, the following architecture is implemented:
- DNS resolution paths are georedundant. Authoritative DNS is served by Route 53 across multiple anycast locations, supplemented by Cloudflare’s global network as a secondary provider for our Internet-facing patient portals.
- Certificate validation endpoints (OCSP, CRLs) are critical for service availability. The Meridian infrastructure team maintains a warm standby OCSP stapling cache within our ingress tier to mitigate transient unavailability of third-party CA responders.

## 7. Monitoring, Metrics, and Reporting

### 7.1 Service Monitoring and Alerting

The Health and Availability Monitoring (HAM) system (DataDog) monitors the following endpoints with synthetic checks from multiple geographic regions:

- **Authoritative DNS Resolution:** Synthetic DNS queries for the SOA and NS records of each critical zone apex. An alert is triggered if any authoritative nameserver fails to respond correctly.
- **External Certificate Expiry Probe:** A custom DataDog Agent check queries every public endpoint (listed in the Service Catalog, SVC-CAT) and evaluates its TLS certificate chain daily. The check generates:
    - **Warning:** If the certificate expires in fewer than 30 days.
    - **Critical (P1 Alert):** If the certificate expires in fewer than 14 days, or is already expired.

### 7.2 Key Performance Indicators (KPIs) and Reporting

The DNS and Certificate Governance Council reviews a monthly dashboard to assess operational performance.

| KPI | Target Threshold | Measurement Method |
|---|---|---|
| **% of Internet-facing TLS certs on automated lifecycle (ACME/ACM)** | **> 99%** | Ratio of `automated` vs `total` certs from the central inventory. |
| **Certificates Expired per Quarter** | **0** | Count of DataDog P1 alerts triggered for "Cert Expired" status. |
| **Time to Provision New Record (Standard Change)** | **< 4 hours** from approved MR merge | Jira ticket cycle time from `Approved` to `Resolved` status. |
| **DNSSEC-Compliant Public Zones** | **100%** | Route 53 `Get-DNSSEC` API audit across all public zones. |

### 7.3 Access Review

Access to DNS management platforms and certificate portals is governed by role-based access control, integrated with Meridian's centralized identity provider (Okta). Access is granted based on the principle of least privilege (e.g., `ReadOnly` access for Developers to production Route 53, `PowerUser` for NREs). Review of these Okta group memberships is the responsibility of the group owner to review on a periodic ad-hoc basis.

## 8. Exception Handling and Escalation

### 8.1 Exception Request Process

Any deviation from the policies established in this SOP, particularly the mandate for automated certificate renewal (Section 4.2) or code-driven DNS changes (Section 4.3), requires a formal, documented exception.

1.  **Documentation:** The requestor completes the "IT Infrastructure Exception Request" form, detailing:
    - The specific control from which deviation is requested.
    - The system, FQDN, and certificate details requiring the exception.
    - A detailed technical justification explaining why the standard automation cannot be used.
    - A proposed compensating control schedule (e.g., a detailed manual playbook).
    - A requested exception expiry date, not to exceed 12 months.
2.  **Risk Assessment:** The InfoSec team performs a risk assessment of the proposed compensating controls and documents their findings directly on the exception ticket.
3.  **Approval:** The exception must be approved by the DNS & Certificate Governance Council. Approval requires a majority vote, including a mandatory affirmative vote from the VP of IT Operations or their delegate.

### 8.2 Escalation Path

- **TLS Certificate Expiry (Warning, 30-day threshold):** The owning Application Owner and the Infrastructure Operations Lead are paged via PagerDuty `high-urgency` during business hours. The team has 5 business days to resolve or transition to a formal exception.
- **TLS Certificate Expiry (P1, < 14 days or expired):** An immediate P1 incident is declared. The Site Reliability Engineering (SRE) on-call is paged, and the owning Application Owner is engaged via the emergency bridge. The issue is treated with the same urgency as a complete service outage per SOP-INC-001.
- **Unscheduled DNSSEC Zone Key Rollover Failure:** Immediate escalation to the NRE on-call to manually intervene and restore the zone's signing status to prevent a zone from becoming bogus.

## 9. Training Requirements

All personnel in roles listed in Section 3 must complete the following training prior to receiving elevated access privileges to DNS and PKI systems.

| Training Module | Target Audience | Frequency | Delivery Method |
|---|---|---|---|
| **SOP-ITOP-020: Policy & Procedure Acknowledgment** | All IT Operations, Platform Engineering, InfoSec personnel. | Annually. Refresher upon major version change. | Workday Learning Module with Quiz. 100% score required. |
| **Advanced Terraform for Network Infrastructure** | Senior NREs, Infrastructure Operations Lead. | Once upon hiring, updated bi-annually. | Instructor-led lab focusing on `terraform` state surgery, complex routing policies, and DNSSEC enablement. |
| **PKI Fundamentals and Certificate Lifecycle Operations** | PKI Administrators, Application Owners with manual exceptions. | Annually. | Coursera/Pluralsight e-learning path followed by an internal Q&A session with the InfoSec PKI team. |

### 9.1 Competency Verification

The Manager of the Infrastructure Operations team will verify the successful completion of required training modules during quarterly access reviews. Access to the `prod-core-net` AWS account will be automatically revoked via Okta Workflows if role-required training is past due by more than 15 days.

## 10. Related Policies and References

| Document ID | Document Title |
|---|---|
| **SOP-SEC-002** | Information Security Incident Response Plan |
| **SOP-ITOP-007** | Secrets Management and Encryption Key Lifecycle |
| **SOP-ITOP-014** | Identity Management and Physical Access Controls |
| **SOP-BCP-005** | Business Continuity and Disaster Recovery Planning |
| **SOP-CRM-001** | Change Management and Configuration Standards |
| **DOM-STRAT-01** | Meridian Domain Name Strategy & Branding Guidelines |
| **EXT-REF-01** | AWS Certificate Manager Private CA User Guide |
| **EXT-REF-02** | `cert-manager` v1.10 Documentation |
| **EXT-REF-03** | NIST SP 800-57 Part 3: Application of Key Management |
| **EXT-REF-04** | CAB Forum Baseline Requirements for TLS Server Certificates |

## 11. Revision History

| Version | Date | Author | Summary of Changes |
|---|---|---|---|
| 1.0 | 2023-02-01 | Michael Trent, NRE | Initial creation. Separation of DNS and PKI duties from general networking SOP. |
| 1.1 | 2023-08-15 | Sarah Jenkins, Security Engineer | Added Section 5.3 covering initial `cert-manager` rollout for Dev environments. Clarified revocation key compromise process. |
| 2.0 | 2024-03-22 | Priya Patel, SRE Lead | Major rewrite for full migration of public zones to Route 53 and adoption of DNSSEC. Mandated "DNS as Code" for all production records. |
| 2.1 | 2024-11-10 | James O’Connell, IT Ops | Introduced Certificate Transparency monitoring controls (Section 6.2, CTL-MON). Updated expiration KPI dashboard link. |
| 3.0 | 2025-05-19 | Samantha Torres, VP IT Ops | Comprehensive merger of DNS and Certificate policies. Scoped to all public and private PKI. Established the Governance Council. Updated training matrix. Added detailed manual/legacy certificate procedure with explicit calendar mandates. Effective for SOC 2 compliance year. |
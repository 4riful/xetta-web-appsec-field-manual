---
title: "Knowledge Graph"
summary: "Topic relationship graph for the migrated AppSec knowledge base."
tags:
  - report
  - migration
related_topics:
  - "Repository Migration"
references:
---
# Knowledge Graph

## Core Flow

```text
Bug Bounty Workflow
  -> Reconnaissance Methodology
  -> Asset Discovery
  -> Subdomain Enumeration
  -> OSINT and Dorking
  -> JavaScript Recon
  -> Vulnerability Testing
  -> Validation With Tooling
  -> Reporting and Learning Resources
```

## Topic Relationships

| Topic | Prerequisites | Related Concepts | References In Repository |
|---|---|---|---|
| Bug Bounty Workflow | Scope selection, targets | Recon, gf patterns, nuclei, Burp, reporting | `methodology/bug-bounty-workflow.md` |
| Reconnaissance | Program scope | Asset discovery, subdomains, dorking, JS endpoints | `methodology/recon-methodology.md`, `recon/*` |
| Subdomain Enumeration | DNS basics, scope | Vhost enumeration, asset discovery, OSINT | `recon/subdomain-enumeration.md` |
| JavaScript Recon | Endpoint discovery | Secrets, IDOR wordlists, Burp JS Miner | `recon/javascript-recon.md`, `methodology/bug-bounty-workflow.md` |
| Authentication | Account model | Account takeover, password reset, auth bypass | `vulnerabilities/authentication-and-account-security.md` |
| Authorization | Authenticated testing | IDOR, 403 bypass, business logic | `vulnerabilities/access-control-and-business-logic.md` |
| SSRF | URL inputs, server-side fetch behavior | AWS metadata, PDF converters, internal network access | `vulnerabilities/ssrf.md` |
| File Upload | Upload surfaces | RCE, content-type bypass, storage exposure | `vulnerabilities/file-upload.md` |
| Cloud/AWS | Cloud assets | SSRF metadata, S3 buckets, exposures | `vulnerabilities/cloud-and-aws-security.md` |
| Burp Suite | Proxying traffic | Extensions, match/replace, JS Miner, GAP | `tooling/burp-suite-and-toolkit.md` |
| Fuzzing | Wordlists, endpoints | Nuclei, dirsearch, fuzzing templates | `tooling/automation-and-fuzzing.md` |

## Graph Edges

- `Bug Bounty Workflow` requires `Reconnaissance Methodology`.
- `Reconnaissance Methodology` expands into `Subdomain Enumeration`, `OSINT and Dorking`, and `JavaScript Recon`.
- `JavaScript Recon` supports `Access Control and Business Logic` by producing endpoints and parameters for IDOR testing.
- `SSRF` is related to `Cloud and AWS Security` through metadata-service abuse.
- `File Upload Vulnerabilities` can lead to `Command Injection and RCE` when upload handling enables execution.
- `Payloads and Wordlists` support `Fuzzing`, `XSS`, `SQL Injection`, `LFI`, and `Command Injection`.
- `Burp Suite and Testing Toolkit` supports nearly all manual validation phases.
- `Cheat Sheets` and `Blogs, Writeups, and Gitbooks` provide external references for every bug class.

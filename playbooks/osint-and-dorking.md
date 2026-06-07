---
title: "OSINT And Dorking Playbook"
summary: "Defensive search, dorking, and public exposure review patterns for authorized AppSec work."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - playbook
  - osint
  - dorking
  - recon
related:
  - README.md
  - ../resources/recon-and-osint.md
  - ../tools/recon.md
references:
  - https://support.google.com/websearch/answer/2466433
  - https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax
  - https://help.shodan.io/the-basics/search-query-fundamentals
  - https://docs.censys.com/docs/censys-query-language
  - https://www.exploit-db.com/google-hacking-database
---

# OSINT And Dorking Playbook

Use this playbook to find public exposure signals for assets you are authorized to review.

This is not a target-hunting page. Every query must be bounded by scope.

## Scope Inputs

Before searching, collect:

- Approved domains and subdomains.
- Approved GitHub organizations and repositories.
- Approved CIDR ranges.
- Approved cloud accounts or asset inventories.
- Out-of-scope brands, subsidiaries, third-party providers, and shared hosting.
- Program rules for search engines, public asset databases, and automation.

Use documentation placeholders when writing examples:

- `example.com`
- `EXAMPLE-ORG`
- `EXAMPLE-REPO`
- `203.0.113.0/24`
- `198.51.100.0/24`
- `192.0.2.0/24`

## Google Search Exposure Review

Official reference: [Google Search operators](https://support.google.com/websearch/answer/2466433)

### Safe Patterns

```text
site:example.com
site:example.com filetype:pdf
site:example.com filetype:xls OR filetype:xlsx
site:example.com intitle:"index of"
site:example.com "stack trace"
site:example.com "debug"
site:example.com "confidential" -jobs -careers
site:example.com after:2025-01-01 before:2026-01-01
site:example.com (login OR "sign in")
```

### Use When

- Checking indexed documents.
- Looking for exposed debug/error pages.
- Reviewing public login/admin surface.
- Investigating whether sensitive content has been indexed.

### Evidence To Capture

- Query used.
- URL.
- Timestamp.
- Minimal screenshot or response metadata.
- Why the result is sensitive.

### Remediation Paths

- Remove public exposure.
- Add authentication.
- Rotate exposed secrets.
- Remove indexed files.
- Use `noindex` where appropriate.
- Request deindexing after fixing access control.

## GitHub Code Search Review

Official reference: [GitHub Code Search syntax](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax)

### Safe Patterns

```text
org:EXAMPLE-ORG path:.github
org:EXAMPLE-ORG language:yaml path:/.github/workflows/
org:EXAMPLE-ORG "BEGIN PRIVATE KEY" NOT is:fork
org:EXAMPLE-ORG "password" NOT path:/tests/ NOT is:fork
org:EXAMPLE-ORG "api_key" OR "apikey" OR "token"
org:EXAMPLE-ORG path:*.tf "public"
repo:EXAMPLE-ORG/EXAMPLE-REPO path:/config/
org:EXAMPLE-ORG /AKIA[0-9A-Z]{16}/ NOT is:fork
```

### Use When

- Reviewing owned repositories for leaked credentials.
- Checking CI/CD workflow security.
- Finding public infrastructure-as-code exposure.
- Auditing config paths for unsafe defaults.

### Rules

- Replace placeholders only with authorized GitHub owners.
- Exclude forks when they add noise.
- Do not validate discovered credentials unless the rules explicitly allow it.
- Treat any real-looking secret as compromised until rotated.
- Do not paste raw secrets into reports; redact them.

## Shodan Asset Review

Official references:

- [Shodan query fundamentals](https://help.shodan.io/the-basics/search-query-fundamentals)
- [Shodan filters](https://www.shodan.io/search/filters)

### Safe Patterns

```text
net:203.0.113.0/24
hostname:example.com
ssl.cert.subject.cn:example.com
http.title:"Example"
port:443 hostname:example.com
product:nginx port:443
tag:cloud hostname:example.com
```

### Use When

- Checking owned internet-exposed services.
- Finding drift between inventory and reality.
- Reviewing certificate names and HTTP titles.
- Monitoring known networks.

### Rules

- Prefer `net:`, `hostname:`, and certificate filters tied to approved assets.
- Do not use broad vulnerable-product searches to find random targets.
- Verify ownership before reporting.
- Use facets/counts before manually reviewing large result sets.

## Censys Asset Review

Official reference: [Censys query language](https://docs.censys.com/docs/censys-query-language)

### Safe Patterns

```text
host.ip: "203.0.113.0/24"
web.hostname: "example.com"
cert.names: "example.com"
host.services.port = 443
host.services: (port = "443" and protocol = "HTTP")
host.services.software: (product = "nginx")
cert.added_at >= "2025-01-01" and cert.names: "example.com"
```

### Use When

- Discovering certificate-related hostnames.
- Monitoring public services.
- Reviewing HTTP/TLS posture.
- Finding exposure drift over time.

### Rules

- Use certificate results as leads, not proof of ownership.
- Validate ownership before active testing.
- Avoid broad third-party vulnerable-service hunting.

## GHDB As A Defensive Taxonomy

Reference: [Google Hacking Database](https://www.exploit-db.com/google-hacking-database)

Use GHDB to understand exposure categories, not to build target lists.

Translate categories into defensive checks:

- Files containing passwords -> verify authorized domains do not expose credential-like documents.
- Sensitive directories -> verify backup, admin, debug, and artifact paths are not indexed.
- Error messages -> verify stack traces and framework errors are not public.
- Login portals -> inventory public authentication surfaces.
- Network/device data -> validate whether exposed panels are owned and authorized.

## Triage Workflow

```text
query result
  -> is it in scope?
  -> is ownership clear?
  -> is the content sensitive?
  -> is minimal evidence enough?
  -> what is the remediation owner?
  -> report or discard
```

## What Not To Do

- Do not search for real organizations in public examples.
- Do not bulk download documents.
- Do not authenticate into discovered panels.
- Do not use leaked credentials.
- Do not test cloud buckets, takeover conditions, or admin surfaces unless explicitly authorized.
- Do not publish sensitive query results.

## Reporting Template

```text
Title: Public exposure found via scoped OSINT review
Scope: example.com / EXAMPLE-ORG / approved CIDR
Query: <exact query>
Evidence: <minimal URL/screenshot/metadata>
Risk: <why this matters>
Impact: <what an attacker could learn or do>
Remediation: <restrict, remove, rotate, deindex, monitor>
References: <Google/GitHub/Shodan/Censys/GHDB docs>
```

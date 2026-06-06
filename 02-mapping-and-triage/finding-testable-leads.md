---
title: "Finding Testable Leads"
summary: "Map recon signals to the right vulnerability playbook."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - triage
  - vulnerability-testing
related:
  - ../03-vulnerability-guides/README.md
references: []
---
# Finding Testable Leads

## Signal-To-Guide Map

| Signal | Test next |
|---|---|
| Numeric or UUID object IDs | `03-vulnerability-guides/access-control/idor.md` |
| 403/401 on interesting paths | `03-vulnerability-guides/access-control/403-bypass.md` |
| URL/callback/webhook/fetch parameter | `03-vulnerability-guides/server-side/ssrf.md` |
| File upload with transformation or preview | `03-vulnerability-guides/files-and-parsers/file-upload.md` |
| Download/export path parameter | `03-vulnerability-guides/server-side/lfi-and-path-traversal.md` |
| Reflected input in HTML/JS/attribute | `03-vulnerability-guides/injection/xss.md` |
| SQL-looking parameter or database error | `03-vulnerability-guides/injection/sql-injection.md` |
| GraphQL endpoint | `03-vulnerability-guides/api-security/graphql.md` |
| JSON body with hidden fields | `03-vulnerability-guides/api-security/mass-assignment.md` |
| S3 bucket or cloud storage URL | `03-vulnerability-guides/cloud-and-infra/aws-s3.md` |

## Bad Leads

- Dead archive URLs.
- Scanner output without reproduction.
- Payload reflections in inert contexts.
- 403 pages with no bypass signal.
- Out-of-scope hosts.

---
title: "Quickstart"
summary: "Fast route through the field manual without getting lost in raw resource dumps."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - quickstart
  - methodology
related:
  - playbooks/README.md
  - awesome-lists/top-25-web-appsec-links.md
  - reports/README.md
references:
  - https://owasp.org/www-project-web-security-testing-guide/
  - https://portswigger.net/web-security
---

# Quickstart

Use this page when the repository feels too large.

## 0. Scope First

Before any tool, payload, dork, or scan, write down:

- Authorized domains, IP ranges, repositories, APIs, and apps.
- Explicit exclusions.
- Rate limits and automation rules.
- Test accounts and roles.
- Data handling rules.
- Reporting channel.

If scope is unclear, stop.

## 1. If You Have 30 Minutes

Read these in order:

1. [Top 25 Web AppSec Links](awesome-lists/top-25-web-appsec-links.md)
2. [Playbooks](playbooks/README.md)
3. [Reports](reports/README.md)

Outcome: you know the core references, the testing flow, and what good evidence looks like.

## 2. If You Have 60 Minutes

Add one workflow:

1. Pick one playbook from [playbooks/](playbooks/README.md).
2. Pick one bug class from [bug-classes/](bug-classes/README.md).
3. Pick tools only after you know the job.
4. Practice the bug class in [PortSwigger Web Security Academy](https://portswigger.net/web-security), not on random live targets.

Outcome: you have a test hypothesis, not just a pile of links.

## 3. If You Have 90 Minutes

Build a small assessment loop:

```text
scope
  -> asset list
  -> live surfaces
  -> interesting features
  -> bug-class hypothesis
  -> safe manual test
  -> evidence
  -> report draft
```

Recommended path:

1. [Recon to first bug](playbooks/README.md#recon-to-first-bug)
2. [Bug classes](bug-classes/README.md)
3. [Payloads](payloads/README.md)
4. [Report writing](reports/README.md)

## 4. What To Ignore At First

Do not begin with:

- Huge payload lists.
- Random dorks.
- High-rate scanners.
- CVE chains.
- WAF bypass notes.
- Raw `data/` files.

Those are useful only after you understand scope, target behavior, and the bug class.

## 5. Daily Research Loop

For ongoing learning:

1. Read one PortSwigger Academy topic.
2. Read one public writeup.
3. Extract the root cause, not just the payload.
4. Add one detection/remediation note.
5. Practice in a lab.

## 6. Fast Navigation

| Goal | Read |
|---|---|
| Learn the best references | [Top 25](awesome-lists/top-25-web-appsec-links.md) |
| Run an assessment workflow | [Playbooks](playbooks/README.md) |
| Understand vulnerability classes | [Bug classes](bug-classes/README.md) |
| Choose a tool | [Tools](tools/README.md) |
| Find payload context | [Payloads](payloads/README.md) |
| Build a report | [Reports](reports/README.md) |
| Search the full database | [resources.csv](data/resources.csv) |

## 7. Responsible Use Reminder

This manual is for defensive security, education, secure software development, and authorized assessment only.

Do not use it for unauthorized scanning, exploitation, credential attacks, data extraction, persistence, or bypassing access controls on systems you do not own or have permission to test.

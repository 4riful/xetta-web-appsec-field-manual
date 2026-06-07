---
title: "Quickstart"
summary: "Fast, safe route from authorized scope to a test hypothesis, validation plan, or report draft."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - quickstart
  - methodology
related:
  - README.md
  - playbooks/README.md
  - bug-classes/README.md
  - tools/README.md
  - payloads/README.md
  - awesome-lists/top-25-web-appsec-links.md
  - reports/README.md
  - docs/status-and-trust.md
references:
  - https://owasp.org/www-project-web-security-testing-guide/
  - https://portswigger.net/web-security
---

# Quickstart

Use this page when you need the shortest safe route from scope to a useful test plan or reportable finding.

## Audience

Use this if you are new to the repo, preparing for an authorized assessment, converting raw resources into a workflow, or trying to avoid payload-first or scanner-first testing.

## 0. Scope Gate

Before any tool, payload, dork, or scan, write down:

- Authorized domains, IP ranges, repositories, APIs, and apps.
- Explicit exclusions.
- Allowed dates and hours.
- Rate limits and automation rules.
- Test accounts and roles.
- Data handling rules.
- Reporting channel.
- Emergency contact or stop procedure.

If scope is unclear, stop.

## 1. If You Have 10 Minutes

Read these in order:

1. [README](README.md)
2. This quickstart
3. [Reports](reports/README.md)

Output:

- you understand the manual is for authorized work only
- you know not to start with raw payloads or automation
- you know what evidence is required before reporting

## 2. If You Have 30 Minutes

Read these in order:

1. Confirm scope using the scope gate above.
2. Pick one workflow from [Playbooks](playbooks/README.md).
3. Map one app, API, or feature.
4. Identify one trust boundary.
5. Choose one bug-class family from [Bug Classes](bug-classes/README.md).
6. Write one test hypothesis.

Example hypothesis:

> A user with Role A may be able to access Object B owned by another user because the endpoint accepts a user-controlled object identifier.

Output:

- one written hypothesis
- one safe validation plan
- no high-rate automation

## 3. If You Have 60 Minutes

Add one workflow:

1. Capture normal behavior.
2. Change one variable at a time.
3. Use test accounts only.
4. Compare expected behavior against actual behavior.
5. Save request/response evidence.
6. Draft a report skeleton.
7. Practice the same bug class in [PortSwigger Web Security Academy](https://portswigger.net/web-security), not on random live targets.

Output:

- a validated finding, or
- a rejected hypothesis with notes explaining why

## 4. If You Have 90 Minutes

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
3. [Tools by job](tools/README.md)
4. [Payload context](payloads/README.md)
5. [Report writing](reports/README.md)

Optional AI/LLM path:

1. [AI and LLM security](bug-classes/ai-llm/README.md)
2. [AI/LLM application review](playbooks/ai-llm-application-review.md)
3. [Prompt injection](bug-classes/ai-llm/prompt-injection.md)

## 5. Choose Your Path

**New target**
Start with [Recon to first bug](playbooks/README.md#recon-to-first-bug). Expected output: asset and feature map.

**Web app with accounts**
Start with [Black-box web assessment](playbooks/README.md#black-box-web-assessment). Expected output: role/object matrix.

**API or mobile backend**
Start with [API assessment](playbooks/README.md#api-assessment). Expected output: endpoint/auth/object matrix.

**AI feature**
Start with [AI/LLM application review](playbooks/ai-llm-application-review.md). Expected output: AI data/tool/action map.

**Source available**
Start with [Source-assisted review](playbooks/README.md#source-assisted-review). Expected output: code-to-behavior trace.

**Potential finding**
Start with [Reports](reports/README.md). Expected output: clean report draft.

## 6. What To Ignore At First

Do not begin with:

- Huge payload lists.
- Random dorks.
- High-rate scanners.
- CVE chains.
- WAF bypass notes.
- Raw `data/` files.

Those are useful only after you understand scope, target behavior, and the bug class.

## 7. Daily Research Loop

For ongoing learning:

1. Read one PortSwigger Academy topic.
2. Read one public writeup.
3. Extract the root cause, not just the payload.
4. Add one detection/remediation note.
5. Practice in a lab.

## 8. Fast Navigation

- Learn the strongest references: [Top 25](awesome-lists/top-25-web-appsec-links.md)
- Run an assessment workflow: [Playbooks](playbooks/README.md)
- Understand vulnerability classes: [Bug classes](bug-classes/README.md)
- Choose a tool: [Tools](tools/README.md)
- Find payload context: [Payloads](payloads/README.md)
- Build a report: [Reports](reports/README.md)
- Review AI/LLM app risk: [AI/LLM application review](playbooks/ai-llm-application-review.md)
- Test prompt injection safely: [Prompt injection](bug-classes/ai-llm/prompt-injection.md)
- Search the full database: [resources.csv](data/resources.csv)
- Understand page trust/status: [Documentation Status And Trust Model](docs/status-and-trust.md)

## 9. Stop Conditions

Stop when:

- scope is unclear
- testing may affect other users
- sensitive data appears
- availability risk increases
- a tool is producing noisy or unexplained output
- the program forbids the test class

## 10. When Not To Use This Page

Do not treat the quickstart as permission to test live third-party systems, run high-rate tools, use leaked credentials, or skip scope review.

## 11. Responsible Use Reminder

This manual is for defensive security, education, secure software development, and authorized assessment only.

Do not use it for unauthorized scanning, exploitation, credential attacks, data extraction, persistence, or bypassing access controls on systems you do not own or have permission to test.

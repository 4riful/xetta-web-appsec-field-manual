<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=210&color=0:020617,45:172554,100:7c3aed&text=Xetta%20Web%20AppSec%20Field%20Manual&fontColor=ffffff&fontSize=34&fontAlignY=38&desc=Curated%20methodology,%20references,%20playbooks,%20tools,%20payload%20context,%20and%20safe%20research%20workflows.&descAlignY=58&descSize=14" alt="Xetta Web AppSec Field Manual" />
</p>

<p align="center">
  <a href="QUICKSTART.md"><img alt="Quickstart" src="https://img.shields.io/badge/start-quickstart-2563eb?style=for-the-badge"></a>
  <a href="playbooks/README.md"><img alt="Playbooks" src="https://img.shields.io/badge/workflows-playbooks-7c3aed?style=for-the-badge"></a>
  <a href="awesome-lists/top-25-web-appsec-links.md"><img alt="Top 25" src="https://img.shields.io/badge/curated-top%2025-f97316?style=for-the-badge"></a>
  <a href="reports/README.md"><img alt="Reports" src="https://img.shields.io/badge/output-reporting-22c55e?style=for-the-badge"></a>
</p>

<p align="center">
  <img alt="Scope first" src="https://img.shields.io/badge/scope-first-111827?style=flat-square">
  <img alt="Lab safe" src="https://img.shields.io/badge/lab--safe-practice-111827?style=flat-square">
  <img alt="Manual validation" src="https://img.shields.io/badge/manual-validation-111827?style=flat-square">
  <img alt="Evidence driven" src="https://img.shields.io/badge/evidence-driven-111827?style=flat-square">
  <img alt="Curated not dumped" src="https://img.shields.io/badge/curated-not%20a%20dump-111827?style=flat-square">
</p>

## What This Is

This repository is a **field manual for authorized web application security work**.

It is being reshaped from raw notes and link dumps into a practical reference that helps a security person move from:

```text
scope -> assets -> signals -> hypothesis -> safe test -> evidence -> report -> remediation
```

The manual keeps raw resources in `data/` and `provenance/`, but the user-facing pages should be curated, explained, and usable in the field.

## Rules Of Engagement

- Test only systems you own, lab systems, CTF targets, or assets where you have explicit written authorization.
- Read program scope, exclusions, rate limits, and safe-harbor terms before running tools.
- Prefer passive discovery and manual validation before automation.
- Stop when impact is proven. Do not dump data, persist access, or create unnecessary harm.
- Treat secrets, tokens, PII, and internal URLs as sensitive evidence.

## Start Here

| Need | Go here | Outcome |
|---|---|---|
| Fast path through the repo | [QUICKSTART.md](QUICKSTART.md) | Know what to read first and what to ignore |
| The best public references | [Top 25 Web AppSec Links](awesome-lists/top-25-web-appsec-links.md) | Start with reputable sources, not random links |
| Real testing workflows | [playbooks/](playbooks/README.md) | Turn resources into a repeatable process |
| Vulnerability methodology | [bug-classes/](bug-classes/README.md) | Learn signals, checks, evidence, and false positives |
| Tools by job | [tools/](tools/README.md) | Pick tools based on purpose and risk |
| Payload context | [payloads/](payloads/README.md) | Use payloads only after you know what you are testing |
| Reporting | [reports/](reports/README.md) | Convert proof into a useful report |
| Full raw database | [data/resources.csv](data/resources.csv) | Search the entire source dataset |

## Manual Structure

### 1. Methodology

- [Quickstart](QUICKSTART.md)
- [Playbooks](playbooks/README.md)
- [OSINT and dorking playbook](playbooks/osint-and-dorking.md)
- [Learning maps](maps/README.md)
- [Reports](reports/README.md)
- [AI/LLM application review](playbooks/ai-llm-application-review.md)

### 2. Bug Classes

- [Access control](bug-classes/access-control/access-control.md)
- [Authentication](bug-classes/auth/auth.md)
- [API security](bug-classes/api/api.md)
- [XSS and client-side](bug-classes/client-side/xss.md)
- [SQL injection](bug-classes/injection/sqli.md)
- [SSRF](bug-classes/server-side/ssrf.md)
- [File upload and parser abuse](bug-classes/files-parsers/file-upload.md)
- [Request smuggling](bug-classes/server-side/request-smuggling.md)
- [AI and LLM application security](bug-classes/ai-llm/README.md)
- [Prompt injection](bug-classes/ai-llm/prompt-injection.md)

### 3. Resources And Tools

- [Resources](resources/README.md)
- [Tools](tools/README.md)
- [Payloads](payloads/README.md)
- [Awesome lists](awesome-lists/README.md)
- [Labs](labs/README.md)
- [AI/LLM security resources](resources/ai-llm-security.md)

### 4. Source Database

- [resources.csv](data/resources.csv)
- [resources.json](data/resources.json)
- [source catalog](provenance/source-catalog.md)
- [source coverage matrix](provenance/source-coverage-matrix.md)

## Current Editorial Direction

This repo should become a curated field reference: each page should explain when to use a resource, what evidence it produces, and what safety limits apply.

Every important page should answer:

- What problem does this solve?
- When should I use it?
- What input do I need?
- What output or evidence should I expect?
- What can go wrong?
- What are the best references?

Use the page templates when adding new material: [resource page](templates/resource-page.md), [tool note](templates/tool-note.md), [bug class](templates/bug-class.md), and [workflow](templates/workflow.md).

## When Not To Use This Manual

Do not use this manual for unauthorized testing, opportunistic target hunting, credential use, data extraction, persistence, destructive proof, or bypassing program rules.

## Maintenance Standard

The quality bar is documented in [maintainers/content-quality-checklist.md](maintainers/content-quality-checklist.md).

Hard rules:

- No placeholders in user-facing pages.
- No random `target`, `.htb`, private Notion, or broken generated headings in curated docs.
- No duplicate resource spam.
- No page marked `reviewed` unless it contains actual guidance.
- No tool command without purpose, input, expected output, and safety notes.

## Contribute

Good additions are welcome if they are curated.

- [New resource request](https://github.com/4riful/xetta-web-appsec-field-manual/issues/new?template=resource-request.yml)
- [Open a pull request](https://github.com/4riful/xetta-web-appsec-field-manual/compare)

Useful contributions include methodology notes, official references, safe labs, strong writeups, tool docs, payload context, report templates, and cleanup of noisy generated pages.

## Stars

<p align="center">
  <a href="https://github.com/4riful/xetta-web-appsec-field-manual/stargazers"><img alt="GitHub Stars" src="https://img.shields.io/github/stars/4riful/xetta-web-appsec-field-manual?style=for-the-badge&logo=github&label=Star%20This%20Manual&color=facc15"></a>
  <a href="https://www.star-history.com/?repos=4riful%2Fxetta-web-appsec-field-manual&type=date&legend=top-left"><img alt="Star History" src="https://img.shields.io/badge/star%20history-open%20chart-7c3aed?style=for-the-badge"></a>
</p>

<p align="center">
  <a href="https://www.star-history.com/?repos=4riful%2Fxetta-web-appsec-field-manual&type=date&legend=top-left">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=4riful/xetta-web-appsec-field-manual&type=date&theme=dark&legend=top-left">
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=4riful/xetta-web-appsec-field-manual&type=date&legend=top-left">
      <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=4riful/xetta-web-appsec-field-manual&type=date&legend=top-left">
    </picture>
  </a>
</p>

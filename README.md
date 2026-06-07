# Xetta Web AppSec Field Manual

A practical field manual for authorized web application security work: define scope, map assets and features, form hypotheses, validate safely, capture evidence, report clearly, and support remediation.

## What This Manual Is

- A methodology-first guide for authorized web, API, cloud-adjacent, and AI/LLM application security testing.
- A curated navigation layer over standards, tools, payload references, reports, labs, and imported research notes.
- A field workflow for turning observations into validated findings and fixable remediation.

## What This Manual Is Not

- Not permission to test third-party systems.
- Not a payload dump.
- Not a scanner recipe book.
- Not a collection of guaranteed exploits.
- Not a replacement for written authorization, program rules, or legal review.

## Read This First

Use the workflow pages first. Some imported resource, payload, and tool pages are still being cleaned and may contain placeholders, duplicate links, lab hostnames, raw snippets, or generated extraction blocks.

High-confidence entry points:

- [Quickstart](QUICKSTART.md)
- [Playbooks](playbooks/README.md)
- [Reports](reports/README.md)
- [Top 25 references](awesome-lists/top-25-web-appsec-links.md)
- [Bug-class index](bug-classes/README.md)
- [Documentation status and trust model](docs/status-and-trust.md)

Raw databases and generated resource pages are useful for search and triage. Do not treat them as reviewed instructions until they pass the [content quality checklist](maintainers/content-quality-checklist.md).

## Start Here

| If you need to... | Go to |
|---|---|
| Get oriented quickly | [Quickstart](QUICKSTART.md) |
| Run a structured assessment | [Playbooks](playbooks/README.md) |
| Choose a vulnerability family | [Bug Classes](bug-classes/README.md) |
| Pick a tool by job | [Tools](tools/README.md) |
| Use payload references safely | [Payloads](payloads/README.md) |
| Write a finding | [Reports](reports/README.md) |
| Browse curated references | [Resources](resources/README.md) |
| Understand page quality/status | [Documentation Status And Trust Model](docs/status-and-trust.md) |

## Operating Model

```text
authorization
  -> scope
  -> assets
  -> features and trust boundaries
  -> signals
  -> hypothesis
  -> safe validation
  -> evidence
  -> report
  -> remediation
  -> retest
```

Every test should have:

- written authorization
- an affected asset
- a feature or trust boundary
- a bug-class hypothesis
- a safe validation plan
- minimal reproducible evidence
- a remediation path

## If You Are Doing An Assessment Now

1. Confirm scope and stop conditions in [Quickstart](QUICKSTART.md).
2. Pick a workflow from [Playbooks](playbooks/README.md).
3. Build an asset and feature map.
4. Choose a bug-class hypothesis from [Bug Classes](bug-classes/README.md).
5. Choose tools only after the job is clear: [Tools](tools/README.md).
6. Use payloads only with context: [Payloads](payloads/README.md).
7. Capture evidence and write the finding: [Reports](reports/README.md).
8. Stop when impact is proven.

## Field Workflows

The playbooks are the spine of the manual.

- [Recon to first bug](playbooks/README.md#recon-to-first-bug)
- [Black-box web assessment](playbooks/README.md#black-box-web-assessment)
- [API assessment](playbooks/README.md#api-assessment)
- [OSINT and dorking review](playbooks/osint-and-dorking.md)
- [Cloud exposure review](playbooks/README.md#cloud-exposure-review)
- [Source-assisted review](playbooks/README.md#source-assisted-review)
- [AI/LLM application review](playbooks/ai-llm-application-review.md)
- [Reporting and evidence](playbooks/README.md#reporting-and-evidence)

## Bug-Class Decision Points

Start with the feature and trust boundary, not a payload list.

- Auth boundary, roles, object ownership, or tenant isolation: [Access Control](bug-classes/access-control/README.md), [Authentication](bug-classes/auth/README.md), [API Security](bug-classes/api/README.md)
- Browser-executed input, DOM behavior, or user-controlled rendering: [Client-Side](bug-classes/client-side/README.md)
- URL fetcher, webhook, importer, previewer, parser, or metadata access: [Server-Side](bug-classes/server-side/README.md)
- Upload, archive, document conversion, SVG/XML/PDF parsing, or stored file handling: [Files and Parsers](bug-classes/files-parsers/README.md)
- Query, filter, search, reporting, or database-backed input: [Injection](bug-classes/injection/README.md)
- Proxy/front-end/back-end HTTP framing inconsistency: [Server-Side](bug-classes/server-side/README.md)
- AI feature with retrieval, tools, memory, agents, or generated output sinks: [AI and LLM Application Security](bug-classes/ai-llm/README.md), [Prompt Injection](bug-classes/ai-llm/prompt-injection.md)

## Evidence Standard

A finding is not ready until it has:

- affected asset and scope
- affected role, account, object, tenant, or data boundary
- exact request and response where applicable
- timestamp and environment
- expected behavior versus actual behavior
- impact without overclaiming
- minimal proof without unnecessary data access
- remediation guidance

Use [Reports](reports/README.md) before opening a finding.

## Tools And Payloads

Tools support a hypothesis; they do not replace one.

- [Tools by job](tools/README.md)
- [Payload context](payloads/README.md)

Do not run payload-heavy automation until scope, rate limits, and the relevant bug class are clear.

## Trusted References

Start with official standards, labs, and original documentation:

- OWASP WSTG
- OWASP ASVS
- OWASP Cheat Sheet Series
- OWASP API Security Top 10
- PortSwigger Web Security Academy
- MDN Web Security
- Burp Suite Documentation
- OWASP Top 10 for LLM Applications

See the curated [Top 25 Web AppSec Links](awesome-lists/top-25-web-appsec-links.md).

## Raw And Triage Material

The repository includes imported datasets and generated pages. Use them for search and source discovery, not blind execution.

- [resources.csv](data/resources.csv)
- [resources.json](data/resources.json)
- [resources/](resources/README.md)
- [provenance/](provenance/source-catalog.md)

If a page contains placeholders, lab-only hosts, duplicate links, raw commands without purpose/input/output/safety notes, or `Tier/Value/Source/Context` extraction blocks, treat it as triage material.

Read [Documentation Status And Trust Model](docs/status-and-trust.md) before relying on pages marked `needs_triage`, `generated`, or `archival`.

## Rules Of Engagement

- Test only systems you own, lab systems, CTF targets, or assets where you have explicit written authorization.
- Read program scope, exclusions, rate limits, and safe-harbor terms before running tools.
- Prefer passive discovery and manual validation before automation.
- Stop when impact is proven. Do not dump data, persist access, or create unnecessary harm.
- Treat secrets, tokens, PII, internal URLs, prompts, and retrieved AI context as sensitive evidence.

## When Not To Use This Manual

Do not use this manual for unauthorized testing, opportunistic target hunting, credential use, data extraction, persistence, destructive proof, or bypassing program rules.

## Maintenance

Good additions are welcome if they are curated, safe, and useful in the field.

- [Content quality checklist](maintainers/content-quality-checklist.md)
- [Resource page template](templates/resource-page.md)
- [Tool note template](templates/tool-note.md)
- [Bug-class template](templates/bug-class.md)
- [Workflow template](templates/workflow.md)
- [New resource request](https://github.com/4riful/xetta-web-appsec-field-manual/issues/new?template=resource-request.yml)
- [Open a pull request](https://github.com/4riful/xetta-web-appsec-field-manual/compare)

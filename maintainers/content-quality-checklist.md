---
title: "Content Quality Checklist"
summary: "Editorial quality gate for turning raw AppSec notes into a curated field manual."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - quality
  - maintainers
related:
  - ../templates/resource-page.md
  - ../templates/tool-note.md
  - ../templates/bug-class.md
  - ../templates/workflow.md
references: []
---

# Content Quality Checklist

This repo should be a field manual, not a raw dump.

Use this checklist before marking any user-facing page as `reviewed`.

## Hard Rejects

- [ ] No `tier_5_placeholder_payload` in user-facing docs.
- [ ] No `https://target`, `http://google.com`, `bolt.htb`, `horizontall.htb`, or lab-only hostnames unless clearly marked as lab context.
- [ ] No private Notion links in curated pages.
- [ ] No duplicate exact pages.
- [ ] No repeated generic headings like `cheat sheet`, `Introduction`, `target`, or raw command lines.
- [ ] No page marked `reviewed` if it only contains extracted entries.
- [ ] No exploit/payload content without responsible-use framing.
- [ ] No jailbreak or prompt-injection payload dumps without scope, defensive purpose, expected behavior, evidence limits, and mitigation guidance.
- [ ] No instructions to extract system prompts, user conversations, secrets, or training data from third-party AI systems.

## Every User-Facing Doc Needs

- [ ] Frontmatter.
- [ ] Clear title and summary.
- [ ] Purpose: what problem the page solves.
- [ ] Audience: beginner, hunter, pentester, developer, maintainer, or reporter.
- [ ] When to use it.
- [ ] When not to use it.
- [ ] Related docs.
- [ ] References or explicit empty references list.
- [ ] A path back to `data/resources.csv` or source provenance when relevant.

Exception: the root `README.md` may omit frontmatter so GitHub renders it as a clean landing page.

## Every Resource Entry Needs

- [ ] Human title.
- [ ] Canonical URL.
- [ ] Category.
- [ ] One-sentence reason it belongs.
- [ ] Usage guidance.
- [ ] Safety/legal note if it involves testing, scanning, payloads, or automation.

## Every Command Needs

- [ ] Purpose.
- [ ] Input assumptions.
- [ ] Required authorization/scope.
- [ ] Expected output.
- [ ] Rate limit or safety guidance where relevant.
- [ ] Cleanup or evidence handling notes where relevant.

## Every Tool Page Needs

- [ ] What job the tool solves.
- [ ] Passive vs active behavior.
- [ ] Inputs.
- [ ] Example safe command.
- [ ] Output interpretation.
- [ ] False positives.
- [ ] When not to run it.
- [ ] Official documentation link.

## Every Bug-Class Page Needs

- [ ] What fails.
- [ ] Where it appears.
- [ ] Signals.
- [ ] Preconditions.
- [ ] Manual test path.
- [ ] Tool-assisted checks.
- [ ] Payload context.
- [ ] Evidence checklist.
- [ ] Common false positives.
- [ ] Severity and impact notes.
- [ ] Best references.

## AI/LLM Security Pages Need

- [ ] Clear scope: owned AI feature, lab, or explicitly authorized assessment.
- [ ] Threat model: model, app, tools, retrieval sources, users, memory, and external actions.
- [ ] Distinction between direct prompt injection, indirect prompt injection, data leakage, unsafe tool use, insecure output handling, and excessive agency.
- [ ] Evidence guidance that avoids extracting sensitive prompts, user data, retrieved documents, or secrets.
- [ ] Server-side control focus: authorization, isolation, tool permissions, retrieval filtering, logging, and output handling.
- [ ] No jailbreak prompt dumps without defensive context.
- [ ] No claims that prompt filtering alone is sufficient mitigation.
- [ ] References to OWASP LLM/GenAI guidance or equivalent reputable sources.

## Every Playbook Needs

- [ ] Goal.
- [ ] Inputs.
- [ ] Workflow steps.
- [ ] Decision points.
- [ ] Stop conditions.
- [ ] Expected outputs.
- [ ] Related bug classes.
- [ ] Related tools.
- [ ] Reporting guidance.

## Curation Rules

- Prefer official docs and original research over reposts.
- Prefer lab-safe practice resources over live-target examples.
- Keep raw material in `data/` or `provenance/`.
- Keep curated pages short enough to be usable.
- Remove duplicates instead of adding another variant.
- If a link is good but not top-tier, place it in topic resources, not Top 25.
- If a command is useful only for one historical target, remove it from user-facing docs.

## Every Curated Link Collection Needs

- [ ] Canonical project or official documentation URL where available.
- [ ] No duplicate resources with different titles.
- [ ] No dead, parked, private, or login-only links unless intentionally documented.
- [ ] Reason each link belongs on this page instead of a topic-specific resource page.
- [ ] Date-sensitive links reviewed for freshness.

## Claim Quality

- [ ] Avoid unsupported superlatives like `best`, `complete`, or `definitive`.
- [ ] Prefer scoped claims: `good starting point`, `official reference`, `lab-safe`, `high-signal for X`.
- [ ] If a page claims to be `Top N`, keep the primary list capped at N and explain selection criteria.

## Review Labels

- `reviewed` - curated and passes this checklist.
- `needs_triage` - useful raw material exists, but the page is not field-ready.
- `generated` - produced from data extraction and not yet curated.
- `archival` - preserved for provenance, not recommended as a guide.

## Final Review Question

If a security person opened this page during real authorized work, would it help them decide what to do next?

If not, keep editing.

---
title: "AI/LLM Application Review Playbook"
summary: "A safe assessment workflow for LLM apps, RAG systems, AI agents, tool calling, and prompt injection."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - playbook
  - ai-security
  - llm-security
  - prompt-injection
  - rag
related:
  - ../bug-classes/ai-llm/README.md
  - ../bug-classes/ai-llm/prompt-injection.md
  - ../resources/ai-llm-security.md
references:
  - https://genai.owasp.org/llm-top-10/
  - https://portswigger.net/web-security/llm-attacks
  - https://learn.microsoft.com/en-us/security/ai-red-team/
  - https://atlas.mitre.org/
---

# AI/LLM Application Review Playbook

Use this playbook for authorized assessment of LLM-backed web apps, RAG systems, copilots, chatbots, agents, and tool-using AI workflows.

## Goal

Assess whether an AI-enabled application can be manipulated into violating confidentiality, integrity, availability, authorization, privacy, safety, or business workflow constraints.

## Inputs

- Written authorization covering AI features.
- In-scope apps, APIs, models, RAG sources, tools, agents, tenants, and environments.
- Test users, roles, tenants, and canary data.
- Rules for prompt injection, indirect injection, RAG poisoning, tool testing, automation, and cost limits.
- Data handling rules for prompts, responses, logs, retrieved documents, and generated files.

## Workflow

1. Map AI entry points: chat, API, search, summarization, support bot, code assistant, browser agent, email/ticket agent, and internal workflow.
2. Map model context: system prompts, developer prompts, user input, retrieved content, memory, tool output, and previous conversation.
3. Map actions: read-only tools, write tools, external messages, file access, code execution, browsing, ticket creation, database operations, and admin actions.
4. Map data boundaries: user, role, tenant, workspace, repository, document ACL, and provider logging.
5. Test direct prompt injection with harmless canaries.
6. Test indirect prompt injection through approved documents, tickets, web pages, or lab content.
7. Test RAG authorization using test users and controlled documents.
8. Test whether tools enforce server-side authorization independent of model behavior.
9. Test output handling where model output becomes HTML, Markdown, JSON, code, SQL, shell, email, ticket text, or file content.
10. Test logs, monitoring, human approval, and incident response visibility.
11. Write findings as control failures, not clever prompts.

## Decision Points

- Is the target a model-only test or an application/system test?
- Is untrusted content mixed with privileged context?
- Does the model have access to private data?
- Can the model call tools or trigger external actions?
- Are controls deterministic, or only prompt-based?
- Does testing touch real users or sensitive data?

## Stop Conditions

- Scope does not explicitly include AI features.
- Sensitive data appears and minimal proof is enough.
- A tool is about to perform a destructive, external, or irreversible action.
- The test may cross user, tenant, or role boundaries with real data.
- Automation risks excessive cost, rate-limit violation, or service impact.

## Expected Output

- AI feature map.
- Model/context/tool inventory.
- RAG and data-flow notes.
- Validated findings with sanitized evidence.
- Regression test recommendations.
- Control improvement roadmap.

## Test Categories

### Prompt Injection

- Direct instruction override.
- System prompt leakage attempts.
- Multi-turn policy erosion.
- Encoded, translated, roleplay, or format-shifting attempts.
- Refusal probing.

### Indirect Prompt Injection

- Instructions hidden in approved test documents.
- Instructions in web pages, tickets, emails, code comments, OCR text, metadata, or retrieved chunks.
- Stored instructions that affect future sessions.

### RAG Security

- Cross-tenant retrieval.
- Metadata filter bypass.
- Unauthorized/stale document retrieval.
- Poisoned or maliciously ranked documents.
- Misleading citations.
- Hidden text and metadata handling.

### Tool And Agent Safety

- Unauthorized tool calls.
- Overbroad credentials.
- Parameter injection.
- Write action without approval.
- Tool output treated as trusted instruction.
- Agent loops, goal drift, and memory poisoning.

### Output Handling

- HTML/Markdown rendering.
- Links and remote images.
- JSON/XML/YAML schema bypass.
- Generated code, SQL, shell, or workflow config.
- CSV formula injection.
- Unsafe generated files.

## Evidence Guidance

Capture:

- Prompt and response.
- Test account and role.
- Model/app version if known.
- Retrieved source IDs and metadata.
- Tool-call trace and authorization decision.
- Approval prompt and executed action.
- Sanitized logs.
- Screenshots or request IDs.

Avoid:

- Raw real secrets.
- Customer data dumps.
- Full private documents.
- Production poisoning artifacts left behind.
- Harmful generated content unrelated to the finding.

## Reporting Template

```text
Title: <AI/LLM finding title>
Category: Prompt Injection / RAG / Tool Calling / Agent / Data Leakage / Output Handling / Logging / HITL / Cost
Severity: Critical / High / Medium / Low
Affected feature:
Affected users/roles/tenants:
Prerequisites:
Summary:
Business impact:
Technical root cause:
Steps to reproduce:
Sanitized prompt/canary:
Observed result:
Expected result:
Evidence:
Sensitive data handling:
Recommended remediation:
Regression test:
References:
```

## Primary References

- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
- [PortSwigger Web LLM Attacks](https://portswigger.net/web-security/llm-attacks)
- [Microsoft AI Red Team](https://learn.microsoft.com/en-us/security/ai-red-team/)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)

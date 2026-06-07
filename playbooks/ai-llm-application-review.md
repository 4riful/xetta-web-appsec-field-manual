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
- Model provider, embedding provider, reranker, OCR/transcription provider, moderation service, logging pipeline, and analytics pipeline.
- Provider retention, training, residency, tenant-isolation, and data-processing expectations.

## Workflow

1. Map AI entry points: chat, API, search, summarization, support bot, code assistant, browser agent, email/ticket agent, and internal workflow.
2. Map model context: system prompts, developer prompts, user input, retrieved content, memory, tool output, and previous conversation.
3. Map actions: read-only tools, write tools, external messages, file access, code execution, browsing, ticket creation, database operations, and admin actions.
4. Map data boundaries: user, role, tenant, workspace, repository, document ACL, and provider logging.
5. Confirm which providers retain prompts/completions, use data for training, or process sensitive inputs through embeddings, OCR, transcription, moderation, analytics, or logging.
6. Test direct prompt injection with harmless canaries.
7. Test indirect prompt injection through approved documents, tickets, web pages, or lab content.
8. Test RAG authorization using test users and controlled documents.
9. Test whether tools enforce server-side authorization independent of model behavior.
10. Test output handling where model output becomes HTML, Markdown, JSON, code, SQL, shell, email, ticket text, or file content.
11. Test logs, monitoring, human approval, and incident response visibility.
12. Write findings as control failures, not clever prompts.

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
- Provider, logging, retention, and data-boundary notes.
- RAG and data-flow notes.
- Validated findings with sanitized evidence.
- Regression test recommendations.
- Control improvement roadmap.

## Test Categories

### Prompt Injection

- Direct instruction override.
- System prompt leakage attempts using bounded canary markers or sanitized indicators. Avoid collecting full hidden prompts unless explicitly authorized and necessary.
- Multi-turn policy erosion.
- Encoded, translated, roleplay, or format-shifting attempts using benign canaries to evaluate whether controls are semantic and policy-aware, not just string filters.
- Refusal probing.

### Indirect Prompt Injection

- Instructions hidden in approved test documents.
- Instructions in web pages, tickets, emails, code comments, OCR text, metadata, or retrieved chunks.
- Instructions hidden in images, audio transcripts, video captions, document comments, white text, layout artifacts, or file metadata.
- Stored instructions that affect future sessions.

### RAG Security

- Cross-tenant retrieval.
- Metadata filter bypass.
- Unauthorized/stale document retrieval.
- Poisoned or maliciously ranked documents.
- Misleading citations.
- Hidden text and metadata handling.

### Model And AI Supply Chain

- Untrusted model files, adapters, LoRA files, serialized artifacts, or unsafe deserialization.
- Fine-tune, eval, and embedding dataset poisoning.
- Untrusted plugins, tools, agent packages, connectors, and MCP servers.
- Model, prompt, policy, tool-schema, and retrieval-index version drift.
- Missing model inventory, provenance, SBOM, or ML-BOM for AI components.

### Tool And Agent Safety

- Unauthorized tool calls.
- Overbroad credentials.
- Parameter injection.
- Write action without approval.
- Tool output treated as trusted instruction.
- Agent loops, goal drift, and memory poisoning.
- Human approval prompts that show model summaries instead of exact action, target, arguments, data exposure, and rollback path.

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

## Severity Guidance

- Critical: cross-tenant sensitive data exposure, real secret exposure, unauthorized privileged tool execution, persistent poisoning that affects other users, or silent external exfiltration.
- High: unauthorized non-public data access, write/admin tool use without effective approval, RAG authorization failure, or output handling that enables downstream code/query execution.
- Medium: prompt injection that changes controlled output or business workflow without sensitive data exposure, privileged action, or cross-user impact.
- Low: isolated canary repetition, cosmetic instruction following, or model-only behavior with no security boundary impact.

Severity should be based on the application control failure and business impact, not how clever the prompt looked.

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

## Related Pages

- [AI and LLM application security](../bug-classes/ai-llm/README.md)
- [Prompt injection](../bug-classes/ai-llm/prompt-injection.md)
- [AI/LLM security resources](../resources/ai-llm-security.md)

## Primary References

- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
- [PortSwigger Web LLM Attacks](https://portswigger.net/web-security/llm-attacks)
- [Microsoft AI Red Team](https://learn.microsoft.com/en-us/security/ai-red-team/)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework)

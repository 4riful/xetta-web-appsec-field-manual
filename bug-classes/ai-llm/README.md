---
title: "AI And LLM Application Security"
summary: "Methodology for testing LLM-backed applications, RAG systems, AI agents, and tool-using assistants safely."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - ai-security
  - llm-security
  - prompt-injection
  - rag
  - agents
related:
  - prompt-injection.md
  - ../../playbooks/ai-llm-application-review.md
  - ../../resources/ai-llm-security.md
references:
  - https://genai.owasp.org/llm-top-10/
  - https://portswigger.net/web-security/llm-attacks
  - https://atlas.mitre.org/
  - https://www.nist.gov/itl/ai-risk-management-framework
---

# AI And LLM Application Security

Use this section for authorized testing of AI-enabled web applications, chatbots, copilots, RAG systems, workflow agents, model-backed APIs, and tool-using assistants.

## What Fails

LLM application risk usually does not live in the model alone. It appears where untrusted input, privileged context, retrieved data, tools, memory, and downstream actions meet.

Common failure modes:

- Prompt injection changes model behavior.
- Indirect prompt injection hides instructions inside documents, tickets, pages, emails, code comments, or retrieved content.
- RAG retrieves data across user, role, tenant, or document boundaries.
- The app trusts model output as authorization, code, HTML, JSON, SQL, shell, or workflow instructions.
- Tools or agents have excessive permissions.
- System prompts, hidden instructions, secrets, user data, or internal documents leak.
- Model output is rendered or executed unsafely.
- Memory stores malicious or cross-user context.
- Logs retain sensitive prompts or completions.
- Unbounded prompts, retries, retrievals, or agent loops create cost and availability risk.

## Where It Appears

- Customer support bots.
- Internal knowledge assistants.
- RAG search and document Q&A.
- AI coding assistants.
- Browser, email, Slack, Teams, or ticketing agents.
- AI features that summarize, classify, extract, translate, triage, or generate reports.
- Agents that call APIs, send messages, create tickets, modify records, browse pages, or run code.
- AI-powered security scanners and autonomous research assistants.

## Signals

- The model sees private data plus untrusted content plus an outbound channel.
- Retrieved documents are mixed into the same context as trusted instructions.
- Tool calls are authorized by prompt text instead of server-side checks.
- Users can upload documents, HTML, PDFs, images, or URLs that later influence other users.
- The system can send emails, create tickets, browse web pages, modify records, execute code, or call internal APIs.
- Responses include citations, links, images, code blocks, HTML, JSON, or files consumed downstream.
- The product has memory, shared workspaces, connectors, or tenant-specific data.

## Threat Model Matrix

| Component | Untrusted Input | Privileged Context | Output Or Action Sink | Primary Control |
|---|---|---|---|---|
| Chat or assistant UI | User prompt, uploaded file, pasted text | System/developer prompt, user profile, conversation memory | UI response, Markdown, file export | Prompt/data separation, output validation, logging |
| RAG pipeline | Documents, web pages, tickets, OCR text, metadata | Private knowledge base, vector index, document ACLs | Answer, citation, retrieved chunk | ACL enforcement before retrieval, source attribution, index lifecycle control |
| Tool calling | User request, retrieved instructions, tool output | API credentials, service accounts, internal APIs | Read/write action, external request, workflow mutation | Server-side authorization, schema validation, least privilege, audit logs |
| Agent workflow | Goal text, intermediate observations, memory | Tool set, plan, approvals, delegated agents | Multi-step action, external communication, code execution | Step limits, human approval, sandboxing, rollback, trace logging |
| Output rendering | Model text, links, images, code, JSON | Browser/session context, downstream parser | HTML, Markdown, email, ticket, command, query | Encoding, sanitization, schema validation, CSP, review gates |

## Manual Test Path

1. Confirm AI-specific testing is in scope.
2. Map every model input: user prompts, system prompts, retrieved content, files, URLs, tool output, memory, and prior conversation.
3. Map every model output: UI text, Markdown, HTML, JSON, tool arguments, files, emails, tickets, logs, and API responses.
4. Inventory tools and permissions.
5. Test direct prompt injection with harmless canaries.
6. Test indirect prompt injection in approved test documents or lab content.
7. Test RAG access control using test users, roles, tenants, and documents.
8. Test tool authorization in the backend, not only model refusal behavior.
9. Test output handling wherever model output is rendered, parsed, or executed.
10. Capture minimal evidence and stop when impact is proven.

## Stop Conditions

- Scope does not explicitly include AI features.
- The test may access another user’s private data.
- The model reveals real secrets, credentials, regulated data, or customer data.
- A tool is about to perform a destructive, external, or irreversible action.
- Testing creates excessive cost, availability risk, or data-retention risk.

## Evidence Checklist

- Prompt and response.
- User, role, tenant, and environment.
- Model/provider/version if available.
- Retrieved document IDs, chunk IDs, citations, and metadata filters where available.
- Tool-call proposal, final arguments, authorization decision, and execution result.
- Screenshots or traces of output rendering.
- Logs showing guardrail, retrieval, authorization, or output-validation behavior.
- Redaction notes for any sensitive evidence.

## Related Pages

- [Prompt Injection](prompt-injection.md)
- [AI/LLM Application Review Playbook](../../playbooks/ai-llm-application-review.md)
- [AI/LLM Security Resources](../../resources/ai-llm-security.md)

## Best References

- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/)
- [OWASP GenAI Security Project](https://genai.owasp.org/)
- [PortSwigger Web LLM Attacks](https://portswigger.net/web-security/llm-attacks)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Microsoft AI Red Team guidance](https://learn.microsoft.com/en-us/security/ai-red-team/)

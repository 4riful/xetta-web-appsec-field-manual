---
title: "Payloads"
summary: "Context guide for using payload, wordlist, command, and snippet references safely."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - payloads
related: []
references: []
---
# Payloads

Payloads are test inputs. They are not proof by themselves.

Use this section only after you understand:

- the feature
- the input location
- the parser or sink
- the expected behavior
- the safe validation path
- the evidence requirement

## Payload Use Model

```text
feature
  -> input
  -> transformation
  -> parser/sink
  -> expected behavior
  -> harmless test string
  -> controlled proof
  -> evidence
```

## Payload Families

**[XSS](./xss.md)**
Use when input is rendered in browser, HTML, DOM, or Markdown. Safer first proof: inert marker string and context analysis.

**[SQL Injection](./sqli.md)**
Use when input appears to influence database query behavior. Safer first proof: syntax, error, or timing checks within safe limits.

**[SSRF](./ssrf.md)**
Use when a server fetches user-controlled URLs or resources. Safer first proof: controlled callback/canary endpoint.

**[LFI / Path Traversal](./lfi-path-traversal.md)**
Use when input selects files or paths. Safer first proof: harmless known file or controlled uploaded file.

**[Command Injection](./command-injection.md)**
Use when input may reach a shell/system command. Safer first proof: non-destructive timing or marker behavior.

**[File Upload Bypass](./file-upload-bypass.md)**
Use when an upload parser/storage/execution boundary exists. Safer first proof: benign file type and metadata checks.

**[WAF Bypass](./waf-bypass.md)**
Use when filtering or normalization behavior blocks valid testing. Safer first proof: only after confirmed bug context.

**[Request Smuggling](./request-smuggling.md)**
Use when HTTP parser mismatch is suspected. Safer first proof: lab or approved low-impact desync checks.

**[Wordlists](./wordlists.md)**
Use when discovery/fuzzing is authorized. Safer first proof: small targeted list before broad lists.

## Safe Payload Rules

1. Start with markers, canaries, and harmless probes.
2. Change one variable at a time.
3. Avoid payloads that dump data, execute destructive commands, or create persistence.
4. Use out-of-band payloads only with controlled callback infrastructure.
5. Keep exact requests and responses.
6. Stop when impact is proven.
7. Do not bypass program restrictions to prove severity.

## Before Using A Payload

Write:

- bug-class hypothesis
- affected feature
- input context
- expected safe result
- stop condition
- evidence plan

## Payload Context Checklist

- Where is input accepted?
- Is input stored, reflected, parsed, fetched, executed, or transformed?
- Which component interprets it?
- What encoding or normalization happens?
- What is the least harmful proof?
- What response confirms behavior?
- What false positives are likely?

## When Not To Use Payloads

Do not use payloads when:

- you do not understand the sink
- the target is not in scope
- the payload may affect other users
- the payload attempts persistence, credential theft, or data dumping
- the payload is copied from a lab without adapting context
- a safer proof is available

## Relationship To Reports

A report should describe the control failure, not celebrate the payload. Use [Reports](../reports/README.md) to turn behavior into evidence, impact, remediation, and retest guidance.

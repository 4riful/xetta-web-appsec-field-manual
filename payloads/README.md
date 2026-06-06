---
title: "Payloads"
summary: "Payload, wordlist, command and snippet resources."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - payloads
related: []
references: []
---
# Payloads

Payloads are testing aids, not proof by themselves. Use this section after you know the input context, expected behavior, and safe validation path.

## Payload Families

- [XSS](./xss.md): reflected, stored, blind, SVG, DOM-adjacent, and WAF bypass payload references.
- [SQL Injection](./sqli.md): SQLi payload collections, scanner command snippets, and WAF/error-based references.
- [SSRF](./ssrf.md): URL fetcher tests, OOB probes, SVG SSRF, metadata-focused payloads, and parser examples.
- [LFI / Path Traversal](./lfi-path-traversal.md): file-read checks, traversal references, and LFI wordlist material.
- [Command Injection](./command-injection.md): shell metacharacter and command execution references.
- [File Upload Bypass](./file-upload-bypass.md): extension, MIME, SVG, parser, and upload-to-impact ideas.
- [WAF Bypass](./waf-bypass.md): filter evasion and mutation resources.
- [Request Smuggling](./request-smuggling.md): desync and HTTP parser ambiguity references.
- [Wordlists](./wordlists.md): directories, parameters, file names, fuzzing inputs, and discovery lists.

## Safe Use

1. Match payloads to a specific sink or parser.
2. Prefer harmless proof strings before impact payloads.
3. Keep requests and responses for reproduction.
4. Stop if testing becomes destructive or outside scope.

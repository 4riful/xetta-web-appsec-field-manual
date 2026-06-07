---
title: "WAF And Filter Bypass"
summary: "Methodology for reviewing filter, normalization, parser, and WAF edge cases defensively."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - bug-class
  - defensive-bypass
  - waf-bypass
related:
  - ../../payloads/waf-bypass.md
  - ../../reports/README.md
references:
  - https://owasp.org/www-project-web-application-firewall-evaluation-criteria/
  - https://coreruleset.org/
  - https://www.rfc-editor.org/rfc/rfc3986
  - https://url.spec.whatwg.org/
---

# WAF And Filter Bypass

WAF and filter bypass issues occur when a defensive layer interprets input differently from the application, parser, browser, database, or upstream/downstream proxy.

Use this page to analyze normalization and parser mismatch around an already valid bug-class hypothesis. Do not treat bypass notes as a standalone vulnerability without impact.

## What Fails

- A filter blocks simple input but misses equivalent encoded, normalized, or parser-transformed input.
- A WAF sees one representation while the backend sees another.
- Validation happens before canonicalization, redirects, decompression, parsing, or decoding.
- Denylist rules attempt to replace real server-side controls.

## Where It Appears

- Access-control route filtering.
- URL allowlists and SSRF controls.
- XSS, SQLi, command, and file-upload filtering.
- CDN/proxy/WAF layers.
- API gateways and request transformers.
- Mixed browser/server URL parsing contexts.

## Signals

- Different components log different paths, hosts, methods, or parameters.
- Encoded forms are blocked inconsistently.
- The application accepts an input the filter appears to reject or rewrite.
- Equivalent normalized values behave differently.
- A primary control is a denylist rather than server-side authorization, encoding, parameterization, or allowlisting.

## Preconditions

- A real bug-class hypothesis exists.
- The underlying control failure can be stated without the bypass trick.
- Testing stays inside scope and rate limits.
- The proof does not rely on destructive or broad payload mutation.

## Safe Test Path

1. Identify the primary control being tested.
2. Capture normal blocked and allowed behavior.
3. Compare how the filter and backend canonicalize the same input.
4. Test a minimal equivalent representation.
5. Prove impact through the underlying bug class, not through bypass novelty alone.
6. Stop when the mismatch and control failure are clear.

## Tool-Assisted Checks

Payload mutation and fuzzing tools can create high noise. Use small, targeted cases and document why each variation is relevant to a parser or normalization boundary.

## Payload Context

Use [WAF bypass payload context](../../payloads/waf-bypass.md) only after identifying the underlying bug class and parser boundary.

## Evidence Checklist

- Underlying bug-class hypothesis.
- Filter/WAF behavior and backend behavior.
- Minimal equivalent input that demonstrates mismatch.
- Exact request/response pair.
- Logs or traces if available.
- Why existing control is insufficient.
- Recommended primary fix, not only a new rule.

## Common False Positives

- Bypassing a WAF rule without reaching vulnerable application behavior.
- Different status codes caused by rate limits or bot protection.
- Application intentionally accepts encoded values after safe decoding.
- Scanner mutation output that cannot be reproduced manually.

## Impact And Severity

Severity follows the underlying bug class. A WAF bypass for a non-exploitable input is usually low value; a bypass enabling cross-tenant access, XSS, SSRF, SQLi, or file execution inherits that impact.

## Remediation

- Fix the primary application control.
- Canonicalize before validation.
- Use allowlists instead of denylist patterns.
- Keep WAF/CDN rules as defense-in-depth.
- Align parser behavior across proxy, gateway, framework, and application layers.
- Add regression tests for the canonicalization edge case.

## References

- [OWASP WAF Evaluation Criteria](https://owasp.org/www-project-web-application-firewall-evaluation-criteria/)
- [OWASP Core Rule Set](https://coreruleset.org/)
- [RFC 3986 URI Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986)
- [WHATWG URL Standard](https://url.spec.whatwg.org/)

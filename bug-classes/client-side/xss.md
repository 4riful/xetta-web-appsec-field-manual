---
title: "Cross-Site Scripting"
summary: "Methodology for reviewing browser-executed input, unsafe rendering, and client-side output handling."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - bug-class
  - client-side
  - xss
related:
  - ../../payloads/xss.md
  - ../../reports/README.md
references:
  - https://portswigger.net/web-security/cross-site-scripting
  - https://portswigger.net/web-security/cross-site-scripting/cheat-sheet
  - https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
  - https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP
---

# Cross-Site Scripting

XSS happens when untrusted input is rendered in a browser context where it can execute script or influence client-side behavior.

Use this page to review reflected, stored, DOM-based, Markdown/HTML-rendered, SVG/XML-adjacent, and rich-text rendering issues during authorized assessments.

## What Fails

- Output is inserted into HTML, attributes, JavaScript, URLs, Markdown, or DOM sinks without context-safe handling.
- Sanitization allows dangerous tags, attributes, protocols, parser transitions, or nested formats.
- Client-side code trusts URL fragments, query strings, postMessage data, storage, or API responses.
- Generated AI/LLM, Markdown, or rich text output is rendered without safe encoding/sanitization.

## Where It Appears

- Search results, profile fields, comments, support tickets, names, labels, and notifications.
- Admin views that render user-supplied content.
- Markdown/rich-text editors and previews.
- SVG/XML upload previews.
- SPA routes that manipulate the DOM from URL or API data.
- Email, ticket, or chat clients that render HTML-like content.

## Signals

- User input is reflected or stored and displayed later.
- HTML-sensitive characters are preserved or partially encoded.
- Different contexts encode differently across views.
- Sanitizer output changes unexpectedly with nested markup or parser edge cases.
- DOM code writes user-controlled data into risky sinks.

## Preconditions

- The feature and user roles are in scope.
- Test accounts or controlled objects are available.
- The proof will not affect real users.
- You can use harmless markers before attempting execution proof.

## Safe Test Path

1. Insert a unique inert marker into the input.
2. Locate every place the marker appears.
3. Identify the rendering context: HTML text, attribute, JavaScript, URL, CSS, Markdown, SVG/XML, or DOM sink.
4. Test whether context boundaries can be changed safely.
5. Use the smallest harmless proof needed for execution only in controlled test objects.
6. Stop once browser execution or unsafe rendering is proven.
7. Do not target real users, steal cookies, exfiltrate data, or persist harmful payloads.

## Tool-Assisted Checks

Browser devtools, proxy history, DOM sink scanners, and sanitizer test harnesses can help find contexts. They do not replace manual context analysis.

## Payload Context

Use [XSS payload context](../../payloads/xss.md) only after you know the rendering context. A payload that works in one context may be irrelevant or unsafe in another.

## Evidence Checklist

- In-scope asset and feature.
- Test account and controlled object.
- Original input and rendered output.
- Rendering context and sink.
- Minimal safe proof of execution or unsafe rendering.
- Affected users/roles/views.
- Cleanup confirmation for stored test content.
- Remediation and retest guidance.

## Common False Positives

- Input appears in page source but is safely encoded.
- Browser devtools decode entities visually, but execution is impossible.
- A sanitizer allows harmless HTML but blocks script-capable behavior.
- Payload triggers only in a lab browser extension or proxy-modified response.
- Self-XSS with no realistic victim or cross-user path.

## Impact And Severity

Severity increases when execution affects other users, privileged users, admin panels, stored content, session-sensitive workflows, or can perform meaningful actions in the victim context.

Severity decreases for self-only behavior, inert markup, or contexts with no sensitive user action or data boundary.

## Remediation

- Encode output by context.
- Use safe DOM APIs and avoid unsafe sinks.
- Sanitize rich text with maintained libraries and restrictive policies.
- Enforce trusted URL protocols and safe link rendering.
- Apply CSP and Trusted Types as defense-in-depth, not primary fixes.
- Add regression tests for affected contexts and related views.

## References

- [PortSwigger XSS](https://portswigger.net/web-security/cross-site-scripting)
- [PortSwigger XSS cheat sheet](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)
- [OWASP XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [MDN Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP)

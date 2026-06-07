---
title: "XSS Payload Context"
summary: "Safe XSS context notes for browser-rendered input after the sink is understood."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - payloads
  - xss
related:
  - ../bug-classes/client-side/xss.md
  - ../reports/README.md
references:
  - https://portswigger.net/web-security/cross-site-scripting/cheat-sheet
  - https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html
---

# XSS Payload Context

Use this page only after you know where input is rendered and which browser context interprets it.

Payloads are not interchangeable. HTML text, attributes, JavaScript strings, URLs, CSS, Markdown, SVG/XML, and DOM sinks require different reasoning.

## Use When

- A unique marker is reflected or stored in a controlled view.
- You know the rendering context.
- The affected page is in scope.
- The proof will not affect real users.

## Safe First Checks

- Start with a unique inert marker.
- Confirm whether the marker is encoded, sanitized, transformed, or moved into a different context.
- Test context boundaries with harmless strings before attempting execution proof.
- Use controlled test objects for stored behavior.

## Stop Conditions

Stop when:

- browser execution or unsafe rendering is proven
- the proof would affect real users
- the payload would exfiltrate data, steal credentials, or persist harmful behavior
- cleanup cannot be guaranteed

## Evidence

Keep the submitted input, rendered output, affected context, browser behavior, account/role/view, cleanup status, and minimal proof. Report the unsafe rendering control failure, not just the payload.

## Related Bug Class

- [Cross-Site Scripting](../bug-classes/client-side/xss.md)

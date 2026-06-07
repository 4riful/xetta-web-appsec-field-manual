---
title: "HTTP Request Smuggling"
summary: "Methodology for reviewing front-end/back-end HTTP parsing mismatches safely."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - bug-class
  - server-side
  - request-smuggling
related:
  - ../../payloads/request-smuggling.md
  - ../../reports/README.md
references:
  - https://portswigger.net/web-security/request-smuggling
  - https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn
  - https://www.rfc-editor.org/rfc/rfc9112
  - https://www.rfc-editor.org/rfc/rfc9113
---

# HTTP Request Smuggling

Request smuggling happens when two HTTP components disagree about where one request ends and the next begins.

Use this page only for explicitly authorized testing. Desync testing can affect other users, poison queues, and disrupt shared infrastructure.

## What Fails

- Front-end and back-end servers parse `Content-Length` and `Transfer-Encoding` differently.
- HTTP/2 downgrade behavior creates ambiguous HTTP/1.1 requests.
- Proxies normalize, buffer, or forward requests inconsistently.
- Backend connection reuse lets one request influence the next request on the same connection.

## Where It Appears

- Reverse proxies and load balancers.
- CDN/front-end plus origin back-end stacks.
- HTTP/2 to HTTP/1.1 downgrade paths.
- Legacy backends behind modern edge infrastructure.
- Custom request parsing, routing, or gateway layers.

## Signals

- Inconsistent handling of duplicate or conflicting length headers.
- Unusual timeouts, connection reuse behavior, or response queue confusion.
- Different behavior through edge versus direct origin paths.
- PortSwigger-style lab patterns reproduced only in approved environments.

## Preconditions

- Desync testing is explicitly in scope.
- You understand whether the target is shared production infrastructure.
- You have a low-impact test path and a stop condition.
- You will not attempt victim request capture or cache poisoning against real users.

## Safe Test Path

1. Prefer lab practice before live testing.
2. Confirm the exact host, protocol, and proxy path are in scope.
3. Use the lowest-impact timing or response-difference checks.
4. Avoid tests that target other users, poison caches, or modify state.
5. Stop if timeouts, queue instability, or unexpected cross-request behavior appears.
6. Escalate carefully with the owner before deeper validation.

## Tool-Assisted Checks

Use dedicated tooling only when allowed by the engagement. Keep request rate low, isolate test accounts, and save every crafted request used for evidence.

## Payload Context

Use [request smuggling payload context](../../payloads/request-smuggling.md) for safety boundaries and lab-first guidance. This bug class is not suitable for blind payload copying.

## Evidence Checklist

- In-scope host and proxy path.
- Protocol version and route tested.
- Exact crafted request and response behavior.
- Timing or response-difference evidence.
- Proof that no other users were targeted.
- Stop condition followed.
- Remediation and retest guidance.

## Common False Positives

- Network instability mistaken for desync.
- WAF/proxy blocking behavior mistaken for parsing confusion.
- Timing variance caused by rate limits or backend load.
- Lab-only patterns applied to a stack that normalizes safely.

## Impact And Severity

Severity increases when the issue can route requests across users, poison caches, bypass access control, hijack sessions, or affect shared infrastructure.

Severity decreases when behavior is limited to harmless request rejection or non-exploitable parsing differences.

## Remediation

- Normalize HTTP parsing across front-end and back-end components.
- Reject ambiguous requests with conflicting length/framing headers.
- Avoid unsafe HTTP/2 downgrade behavior.
- Disable risky backend connection reuse where necessary.
- Patch proxy and origin server components.
- Add monitoring for malformed request patterns.

## References

- [PortSwigger HTTP request smuggling](https://portswigger.net/web-security/request-smuggling)
- [HTTP Desync Attacks](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn)
- [RFC 9112: HTTP/1.1](https://www.rfc-editor.org/rfc/rfc9112)
- [RFC 9113: HTTP/2](https://www.rfc-editor.org/rfc/rfc9113)

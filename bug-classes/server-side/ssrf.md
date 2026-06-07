---
title: "Server-Side Request Forgery"
summary: "Methodology for reviewing server-side URL fetchers, webhooks, previewers, and outbound request boundaries."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - bug-class
  - server-side
  - ssrf
related:
  - ../../payloads/ssrf.md
  - ../../tools/out-of-band.md
  - ../../reports/README.md
references:
  - https://portswigger.net/web-security/ssrf
  - https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html
  - https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html
---

# Server-Side Request Forgery

SSRF happens when an application can be influenced to make server-side requests to attacker-chosen or insufficiently controlled destinations.

Use this page for authorized review of URL fetchers, importers, webhooks, previewers, document converters, and integrations that make outbound requests.

## What Fails

- User-controlled URLs are fetched by the server without strict destination controls.
- URL validation checks strings instead of canonicalized destinations.
- Redirects, DNS changes, alternate IP formats, or parser differences bypass allowlists.
- Internal networks, metadata services, or admin-only services are reachable from the application server.
- Response content, timing, errors, or callbacks reveal server-side reachability.

## Where It Appears

- Link preview and screenshot services.
- Webhook testers.
- PDF/image/document converters.
- URL importers and feed readers.
- Cloud integrations and metadata-aware workloads.
- API clients that fetch user-supplied callback URLs.

## Signals

- A feature asks for a URL and fetches it server-side.
- The app follows redirects or resolves DNS on the backend.
- The backend returns fetched content, status codes, screenshots, or errors.
- A callback service receives DNS/HTTP interactions from application infrastructure.
- Validation blocks obvious hosts but may not account for canonicalization.

## Preconditions

- The URL-fetching feature is in scope.
- External callback testing is allowed.
- You have controlled callback infrastructure or an approved OOB service.
- You will not probe internal networks, metadata services, or third-party targets without explicit permission.

## Safe Test Path

1. Confirm the feature fetches a normal allowed URL.
2. Use a controlled callback domain to prove server-side outbound behavior.
3. Record the callback timestamp, source metadata, request path, and request headers if available.
4. Test redirects or parser behavior only within approved destinations.
5. Stop when server-side fetch control is proven.
6. Do not enumerate internal services, request cloud metadata, or access sensitive endpoints unless explicitly authorized.

## Tool-Assisted Checks

Out-of-band tools can prove blind fetch behavior, but they can also leak request data to third-party infrastructure. Use only approved callback infrastructure and store callback evidence as sensitive data.

## Payload Context

Use [SSRF payload context](../../payloads/ssrf.md) for safe canary patterns and URL-context notes. Payloads should prove reachability with minimal impact, not map internal networks.

## Evidence Checklist

- In-scope feature and request.
- Normal allowed request behavior.
- Controlled callback evidence.
- Timestamp and source metadata.
- Redirect or canonicalization behavior, if relevant.
- Evidence that the destination should have been blocked.
- Minimal proof without internal enumeration.
- Remediation and retest guidance.

## Common False Positives

- Client-side browser requests mistaken for server-side fetches.
- Cached preview data from earlier requests.
- Security scanner callbacks unrelated to the tested feature.
- Public fetchers intentionally allowed by documented product behavior.

## Impact And Severity

Severity increases when SSRF reaches internal services, cloud metadata, admin interfaces, sensitive documents, or privileged network zones.

Severity decreases when requests are limited to public allowlisted hosts, responses are not exposed, and no sensitive destinations are reachable.

## Remediation

- Enforce destination allowlists after URL parsing, DNS resolution, redirects, and IP canonicalization.
- Block loopback, link-local, private, metadata, and reserved ranges where not required.
- Restrict outbound network access at the infrastructure layer.
- Disable redirects or revalidate every redirect hop.
- Use SSRF-safe proxy services for controlled fetches.
- Avoid returning raw internal response data to users.
- Log destination decisions and blocked attempts.

## References

- [PortSwigger SSRF](https://portswigger.net/web-security/ssrf)
- [OWASP SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
- [AWS IMDSv2 documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html)

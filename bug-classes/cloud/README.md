---
title: "Cloud"
summary: "Cloud exposure, AWS, S3, metadata services, leaked keys, public storage, and cloud-hosted attack surface."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - bug-class
related: []
references: []
---
# Cloud

Cloud issues usually become important when recon finds buckets, metadata access, cloud APIs, leaked keys, public storage, or SaaS configuration mistakes.

Treat cloud findings as impact-driven. A public bucket listing is less important than sensitive data exposure, writable storage, credential leakage, metadata access, cross-account access, or production service compromise.

## Pages

- [Cloud Resources](./cloud.md)

## Related

- [Cloud And Infrastructure Resources](../../resources/cloud-and-infrastructure.md)
- [Cloud Tools](../../tools/cloud.md)
- [SSRF](../server-side/ssrf.md)

---
title: "Cloud Exposure Review"
summary: "Workflow for cloud storage, metadata, DNS, and exposed service issues."
status: "needs-expansion"
last_reviewed: "2026-06-06"
tags:
  - cloud
  - workflow
related:
  - ../03-vulnerability-guides/cloud-and-infra/README.md
references: []
---
# Cloud Exposure Review

## Procedure

1. Collect cloud-related hostnames and storage URLs.
2. Identify provider hints in DNS, JavaScript, and responses.
3. Test public storage exposure safely.
4. Review SSRF-to-metadata possibilities.
5. Document exposure without accessing unauthorized data.

---
title: "File Handling Review"
summary: "Code-review checklist for file upload, download, and parser risks."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - file-handling
  - code-review
related:
  - ../03-vulnerability-guides/files-and-parsers/file-upload.md
references: []
---
# File Handling Review

## Check

- File type validation.
- Storage outside web root.
- Randomized names.
- Authorization on download.
- Path normalization.
- Parser sandboxing.
- External entity and external resource handling.

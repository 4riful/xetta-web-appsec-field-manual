---
title: "Source-To-Sink Tracing"
summary: "Trace untrusted input to security-sensitive operations."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - source-to-sink
  - code-review
references: []
---
# Source-To-Sink Tracing

## Sources

- Request parameters.
- JSON bodies.
- Uploaded files.
- Headers.
- Cookies.
- Webhooks.
- Queue messages.

## Sinks

- SQL queries.
- Shell commands.
- File reads/writes.
- URL fetchers.
- Template rendering.
- XML parsers.
- Deserializers.

## Control Questions

- Is input validated?
- Is output encoded?
- Is authorization checked server-side?
- Is the dangerous operation isolated?

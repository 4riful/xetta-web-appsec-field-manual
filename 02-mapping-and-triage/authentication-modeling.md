---
title: "Authentication Modeling"
summary: "Map login, session, reset, MFA, OAuth, and account recovery flows."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - authentication
  - triage
related:
  - ../03-vulnerability-guides/authentication/account-takeover.md
  - ../03-vulnerability-guides/authentication/password-reset.md
references: []
---
# Authentication Modeling

## Surfaces To Capture

- Login and logout.
- Registration and email verification.
- Password reset.
- MFA enrollment and challenge.
- OAuth, SSO, SAML, OpenID Connect.
- Email or phone change.
- Session refresh and token rotation.

## Questions

- What proves identity?
- What changes account control?
- What tokens are issued and where are they stored?
- Can old tokens remain valid after sensitive changes?
- Does the flow bind actions to the right user, tenant, and session?

## Handoff

Use authentication vulnerability guides only after you can describe the flow and its trust assumptions.

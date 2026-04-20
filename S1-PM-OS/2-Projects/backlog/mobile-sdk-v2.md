---
title: Mobile SDK v2
status: backlog
jira-epic: PULSE-451
owner: Jamie Chen
added: 2026-02-14
---

# Mobile SDK v2

## Why This Matters

Our mobile SDK (v1) was built in 2024 and is missing two things customers are actively requesting:
1. **Session replay** — currently web-only; 12 enterprise accounts have explicitly requested this
2. **Push notification analytics** — Globex Corp and Nexus Health have blocked renewal on this gap

This is a greenfield build effort for the mobile layer; the backend instrumentation exists.

---

## Problem Statement

Mobile-first customers (≈ 22% of our enterprise segment) can't get full behavioral analytics because session replay and push analytics don't exist on iOS/Android. As a result:
- Sales is losing or delaying 3-4 enterprise renewals per quarter (~$1.2M ARR at risk)
- Customers instrument web + mobile separately, creating fragmented data

---

## Proposed Scope

| Feature | Priority | Effort Est. |
|---------|----------|-------------|
| iOS session replay SDK | P0 | 6 weeks (mobile eng) |
| Android session replay SDK | P0 | 6 weeks (mobile eng) |
| Push notification event tracking | P1 | 3 weeks |
| Mobile funnel stitching (web+mobile) | P2 | 4 weeks |

---

## Blocking This from Active
- Mobile engineering team is at capacity through Q2 FY26
- Requires security review of session replay data capture (PII handling)
- Need design partner commitment before building (avoid spec-first risk)

---

## Next Steps to Activate
1. Recruit 1-2 design partners willing to test beta SDK
2. Get security sign-off on session replay data handling
3. Align with Marcus Webb on mobile eng capacity in Q3 FY26 planning

---

## Related Links
- Integration usage data: `6-Data/integrations/q1-2026-integration-usage.md`
- Customer feedback references: Globex Corp call notes (3-Meetings/Customer Meetings/)

# Mock Input Data for Standup Eval

Three scenarios. The eval script runs the skill against all three and averages scores.

---

## Scenario A: Heavy Meeting Day

**Date:** 2026-04-08 (Tuesday)

**Calendar Events:**
- 09:00–09:30 — 1:1 with Marcus (attendees: Marcus Webb, Jamie Chen)
- 10:00–10:30 — Pulse Weekly Sync (attendees: Priya Nair, Eli Torres, Jamie Chen, Tyler Brooks)
- 14:00–14:30 — Customer call: Hasbro security team (attendees: external)
- 16:00–16:15 — Sprint grooming (attendees: Eli Torres, Jamie Chen)

**Gmail (unread, last 18h):**
- From: Marcus Webb | Subject: "Re: Pulse Onboarding Revamp timeline — decision needed"
- From: Eli Torres | Subject: "PR ready for review: identity drawer sync"
- From: noreply@github.com | Subject: "Build failed on main"
- From: newsletter@producthunt.com | Subject: "Today's top products"
- From: Hasbro Security Team | Subject: "Prep questions for tomorrow's call"

**Jira (assigned, in progress):**
- WAY-1234: "SOC 2 release alignment — update release criteria doc" | Status: In Progress | No blockers
- WAY-1189: "Identity drawer sync — BE implementation" | Status: In Review | Blocked by: PR review pending
- PULSE-412: "Pulse Anomaly Detection — scope definition" | Status: To Do | Due: 2026-04-10

**Goals context (from GOALS.md):**
- Q2 OKR 1.2: Ship SOC 2-ready release by end of April
- Q2 OKR 2.1: Launch Pulse Anomaly Detection in beta by May 15

---

## Scenario B: Light Day

**Date:** 2026-04-09 (Wednesday)

**Calendar Events:**
- 11:00–11:30 — PM Weekly (attendees: 8 people, no People file matches)

**Gmail (unread, last 18h):**
- From: noreply@jira.com | Subject: "WAY-1234 was transitioned to Done"
- From: noreply@confluence.com | Subject: "Page updated: SOC 2 checklist"

**Jira (assigned, in progress):**
- PULSE-412: "Pulse Anomaly Detection — scope definition" | Status: In Progress | No blockers

**Goals context:**
- Q2 OKR 2.1: Launch Pulse Anomaly Detection in beta by May 15

---

## Scenario C: Blocked Day

**Date:** 2026-04-10 (Thursday)

**Calendar Events:**
- 09:30–10:00 — 1:1 with Eli (attendees: Eli Torres, Jamie Chen)
- 13:00–14:00 — Stakeholder review: Warwick (attendees: Sarah Park, Jamie Chen)

**Gmail (unread, last 18h):**
- From: Sarah Park | Subject: "URGENT: Pulse staging environment broken for customer demo next week"
- From: Eli Torres | Subject: "Blocked on WAY-1189 — need your input on API contract"

**Jira (assigned, in progress):**
- WAY-1189: "Identity drawer sync — BE implementation" | Status: Blocked | Blocked by: API contract decision from PM
- WAY-1234: "SOC 2 release alignment" | Status: In Progress
- WAY-1055: "Demo environment stability" | Status: To Do | Flagged urgent

**Goals context:**
- Q2 OKR 1.2: Ship SOC 2-ready release by end of April
- Q2 OKR 2.1: Launch Pulse Anomaly Detection in beta by May 15

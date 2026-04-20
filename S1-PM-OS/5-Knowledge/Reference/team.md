---
title: Team Reference — Acme Analytics
last-updated: 2026-04-01
---

# Team Reference — Acme Analytics

## Org Chart

```
CEO: David Lin
└── VP Product: Alex Yuen
    └── Director of Product: Sarah Park
        ├── Senior PM: Jamie Chen (Pulse core)
        ├── PM: Kevin Torres (Growth & Activation)
        └── PM: Nina Zhao (Platform & Integrations)

VP Engineering: Rachel Moss
└── Engineering Lead (Pulse): Marcus Webb
    ├── Frontend Engineers: 3
    ├── Backend Engineers: 2
    └── Mobile Engineers: 1 (shared, capacity constrained)

VP Design: Omar Hassan
└── Design Lead (Pulse): Priya Nair
    ├── Product Designers: 2
    └── UX Researcher: 1 (shared with Growth)

VP Data: Jordan Kim
└── Data & Analytics Lead (Pulse): Eli Torres

VP Sales: Mia Chen
└── Sales Lead (Product Segment): Olivia Grant

VP Customer Success: Ben Nguyen
└── CS Lead: Tyler Brooks
```

---

## Working with Engineering

| Lead | Team | What They Own |
|------|------|--------------|
| Marcus Webb | Pulse Core | Pulse platform, analytics engine, session replay |
| Aisha Patel | Platform Infra | Data pipeline, event ingestion, storage layer |
| Leo Santos | Growth Eng | Onboarding, activation, lifecycle messaging |

**Sprint cadence:** 2-week sprints, planning every other Monday
**Standups:** Async in Slack (#pulse-eng-standup) at 9am PST
**Escalation path:** Marcus Webb → Rachel Moss

---

## Working with Design

Priya Nair owns all design for the Pulse product surface. She runs a queue-based system — new requests need to be submitted via the [design request form] with a brief and timeline.

**Design review process:**
1. PM shares problem brief + research context
2. Design explores and shares 2-3 concept directions
3. PM + Design align on direction
4. Design produces Figma handoff
5. PM reviews handoff for edge cases before eng pickup

---

## Working with Data

Eli Torres owns analytics instrumentation, data quality, and ad-hoc analysis requests.

- **Instrumentation:** New events require sign-off from Eli before eng builds (data schema + retention policy)
- **Ad-hoc analysis:** Slack #data-requests with a brief; SLA is 3 business days
- **Self-serve:** Most analysis can be done in our internal data warehouse (Snowflake + Looker)

---

## Key Cross-functional Stakeholders

| Name | Role | What They Need from PM |
|------|------|----------------------|
| Olivia Grant | Sales Lead | Roadmap commitments, customer-facing feature summaries |
| Tyler Brooks | CS Lead | Early access to features, launch timing, known issues |
| Sarah Park | Director of Product | OKR status, escalation path for blockers, exec-ready summaries |

---

## Team Norms

- **Async-first** — Slack is primary; meetings require an agenda
- **Weekly alignment** — Product, Eng, Design weekly sync on Wednesdays (30 min)
- **Decision docs** — Major scope or priority changes require a written decision doc, not just a Slack message
- **Sprint commitments are contracts** — don't add scope after planning without a trade-off conversation with Marcus

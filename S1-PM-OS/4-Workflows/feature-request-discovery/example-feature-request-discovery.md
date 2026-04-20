# Feature Request Discovery Brief — Example

> **This is a reference example.** It shows what a finished discovery brief looks like for a product manager.
> Use it to calibrate your own output. The data is illustrative — not from a real Jira session.

---

**Product Line:** Pulse Analytics
**PM:** Sarah Chen
**Date:** March 2026
**Total requests analyzed:** 94
**OKRs sourced from:** okrs-sarah-q1-2026.md · Q1 2026

---

## Quick-Start Summary

The Pulse Analytics feature backlog is dominated by two high-priority clusters: **Alert Triage Automation** (19 requests, $3.2M Opp ACV at risk) and **Custom Report Builder** (14 requests, $2.1M Opp ACV at risk). Alert Triage Automation has strong OKR alignment — it directly supports the MTTI reduction goal and the Pulse Analytics adoption target — and three enterprise deals totalling $1.4M are currently citing it as a purchase blocker. Custom Reporting has significant ACV but lower OKR alignment; it's best delegated to a future roadmap review rather than built now. **Recommended starting point for PRD: Alert Triage Automation.**

---

## Theme Summary

| Theme | # Requests | Votes (total) | OKR Alignment | ARR Represented (Acct ACV) | Opp ACV at Risk | Competitor Gap? | Staleness | Priority Quadrant |
|-------|-----------|---------------|--------------|---------------------------|-----------------|-----------------|-----------|------------------|
| Alert Triage Automation | 19 | 87 | High | $4.8M | $3.2M | Yes (CrowdStrike Charlotte AI) | ✅ Current | Build Now |
| Custom Report Builder | 14 | 52 | Low | $5.1M | $2.1M | Yes (Microsoft Defender) | ✅ Current | Negotiate |
| Multi-tenant Analyst View | 11 | 38 | High | $2.3M | $0.8M | No | ✅ Current | Strategic Bet |
| Natural Language Query Improvements | 9 | 41 | High | $1.9M | $0.4M | No | ✅ Current | Strategic Bet |
| SOAR / Ticketing Integrations | 22 | 61 | Low | $6.2M | $1.1M | Yes (Palo Alto XSOAR) | ⚠️ Validate | Negotiate |
| Offline / Air-gapped Mode | 8 | 14 | None | $1.2M | $0.0M | No | ⚠️ Validate | Park for Now |
| Bulk Investigation Actions | 11 | 29 | Medium | $1.7M | $0.3M | No | ✅ Current | Strategic Bet |

---

## 2x2 Prioritization Matrix

```
                    LOW REVENUE                     HIGH REVENUE
                ┌───────────────────────────┬───────────────────────────┐
HIGH OKR        │   Strategic Bets          │   Build Now               │
ALIGNMENT       │   Multi-tenant View       │   Alert Triage Automation │
                │   NL Query Improvements   │                           │
                │   Bulk Investigation      │                           │
                ├───────────────────────────┼───────────────────────────┤
LOW OKR         │   Park for Now            │   Negotiate / Delegate    │
ALIGNMENT       │   Offline / Air-gapped    │   Custom Report Builder   │
                │                           │   SOAR / Ticketing (⚠️)   │
                └───────────────────────────┴───────────────────────────┘

Build Now:        Alert Triage Automation
Strategic Bets:   Multi-tenant Analyst View, Natural Language Query Improvements, Bulk Investigation Actions
Negotiate:        Custom Report Builder, SOAR / Ticketing Integrations
Park for Now:     Offline / Air-gapped Mode
```

---

## Top Individual Requests (by votes)

| Rank | Jira Key | Title | Votes | SFDC Acct ACV | SFDC Opp ACV | Age | Staleness |
|------|----------|-------|-------|---------------|--------------|-----|-----------|
| 1 | FSR-2841 | Auto-triage low-confidence alerts with Pulse Analytics | 24 | $890K | $1,200K | 4 months | ✅ Current |
| 2 | FSR-1992 | Build custom dashboards from Pulse Analytics investigation data | 18 | $1,100K | $800K | 7 months | ✅ Current |
| 3 | FSR-3104 | SOAR integration — ServiceNow ticket creation from Purple | 16 | $1,400K | $400K | 14 months | ⚠️ Validate |
| 4 | FSR-2677 | Summarize alert clusters as a single narrative | 15 | $720K | $950K | 5 months | ✅ Current |
| 5 | FSR-2209 | Multi-tenant analyst console for MSSPs | 13 | $980K | $600K | 9 months | ✅ Current |
| 6 | FSR-3381 | Natural language filter for alert queue | 12 | $560K | $300K | 3 months | ✅ Current |
| 7 | FSR-2018 | Bulk mark-as-false-positive from investigation view | 11 | $440K | $200K | 8 months | ✅ Current |
| 8 | FSR-1455 | Export investigation timeline to PDF | 10 | $990K | $0 | 16 months | ⚠️ Validate |
| 9 | FSR-2902 | Scheduled Pulse Analytics threat hunt reports | 9 | $670K | $400K | 6 months | ✅ Current |
| 10 | FSR-3210 | Pulse Analytics explain mode for junior analysts | 8 | $380K | $250K | 2 months | ✅ Current |

---

## Revenue & Customer Signal

| Theme | ARR Represented (Acct ACV) | Opp ACV at Risk | Key Accounts Mentioned |
|-------|---------------------------|-----------------|----------------------|
| Alert Triage Automation | $4.8M | $3.2M | Acme Corp, Meridian Financial, StateGov DOT |
| Custom Report Builder | $5.1M | $2.1M | GlobalBank, TechCo Enterprise, Nexus Health |
| SOAR / Ticketing Integrations | $6.2M | $1.1M | Multiple — but top tickets are 14 months old |
| Multi-tenant Analyst View | $2.3M | $0.8M | MSSPs: ShieldOps, CyberGuard Partners |
| Natural Language Query Improvements | $1.9M | $0.4M | Various enterprise — no single dominant account |

> **Revenue note:** Alert Triage Automation carries $3.2M in Opp ACV at risk — active deals where this feature is a stated purchase blocker. This is 3× more urgent than SOAR/Ticketing Integrations ($1.1M Opp ACV), even though SOAR has higher ARR represented and more individual requests.

---

## Competitive Flags

| Theme | Competitor | Gap Description | Urgency |
|-------|-----------|-----------------|---------|
| Alert Triage Automation | CrowdStrike (Charlotte AI) | Charlotte AI offers alert summarization; we have automation depth advantage but Charlotte is shipping fast — gap is narrowing | High |
| Custom Report Builder | Microsoft Defender | Microsoft's reporting suite is cited by enterprise buyers as best-in-class; we have no native custom report builder | Medium |
| SOAR / Ticketing Integrations | Palo Alto (XSOAR) | XSOAR integration depth is a standard requirement in Palo Alto-heavy shops; requests here are often customers we're trying to displace | Medium |

---

## Recommended Starting Point for PRD

**Recommended theme:** Alert Triage Automation

**Why:**
- **OKR alignment:** Directly moves two Q1 OKRs — MTTI reduction (auto-triage eliminates analyst time on low-confidence alerts) and Pulse Analytics adoption (a top friction point cited in onboarding interviews)
- **Revenue signal:** $3.2M Opp ACV at risk across 3 enterprise deals currently blocked by this gap. These deals are in late-stage negotiation.
- **Competitive context:** CrowdStrike Charlotte AI has alert summarization — we have a window to lead on automation depth, but it's closing. Building now means winning deals before CrowdStrike ships their next release.
- **Staleness:** ✅ Current — top tickets are 3–5 months old. This is active, confirmed customer pain, not legacy noise.

**Suggested PRD framing:** "How can Pulse Analytics reduce the time SOC analysts spend on low-confidence alerts by automatically triaging, contextualizing, and routing them — without requiring analyst review for each one?"

**Next step:** Open [`../prd-creation/`](../prd-creation/) and use this brief as input alongside `@company-context.md`.

---

## Calibration Notes

- Healthy request count for Pulse Analytics: ~80–120 open requests (this session: 94 — healthy)
- High-signal vote threshold used: ≥ 2 votes (removed 11 single-vote requests from theming)
- High-urgency ACV threshold used: Opp ACV ≥ $400K flagged for individual review
- OKR alignment scored against: okrs-sarah-q1-2026.md · Q1 2026
- Staleness threshold: 12 months (FSR-3104, FSR-1455 flagged — validate before building)

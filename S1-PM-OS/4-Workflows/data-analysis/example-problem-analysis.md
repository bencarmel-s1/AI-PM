# SOC Alert Investigation: Root Cause Completion Drop-Off
**Author:** Senior PM, Security Platform
**Date:** Q4 Analysis
**Status:** Ready for stakeholder review

---

## Executive Summary

[Your Product]'s investigation completion rate has been stuck at 40% for two quarters. Funnel analysis pinpoints the critical drop-off: **60% of analysts who begin investigating an alert abandon it before determining root cause**. Survey data from 800 analysts confirms the root cause: excessive context-switching across SIEM, EDR, threat intelligence feeds, and ticketing tools forces analysts to spend more time gathering context than actually investigating. Mid-size security teams — our primary target market — are hit hardest.

**Proposed solution:** AI-Guided Investigation View — correlated context surfaced automatically when an analyst opens an alert, eliminating the need to pivot between tools.

---

## The Problem

### Where analysts drop off

| Step | Alerts/Month | Completed | Completion Rate | Median Time |
|------|-------------|-----------|-----------------|-------------|
| Alert Triggered | 10,000 | 10,000 | 100% | — |
| Alert Opened | 10,000 | 7,800 | 78% | — |
| Investigation Started | 7,800 | 5,460 | 70% | — |
| **Root Cause Determined** | **5,460** | **2,184** | **40%** | **47 min** |
| Incident Closed | 2,184 | 1,966 | 90% | — |

**The critical gap:** 3,276 investigations per month are started and never completed. This is where threat response breaks down — alerts with real risk surface but go unresolved because analysts abandon mid-investigation.

Two signals make this especially concerning:
- The 47-minute median time-to-root-cause for investigations that *do* complete suggests analysts aren't abandoning because the work is done — they're **losing the thread** while context-gathering across tools
- 70% of opened alerts progress to investigation start, so analyst intent is high. The breakdown happens mid-investigation, not at triage

---

## Why It's Happening

### Survey Evidence (n=800 analysts)

**Top abandonment themes:**

| Theme | % of Respondents | Analysts |
|---|---|---|
| Had to pivot between 4+ tools to gather context for one alert | 38% | 304 |
| Couldn't find historical context on the affected endpoint | 26% | 208 |
| Alert had no correlated events to help understand scope | 21% | 168 |
| Didn't know if endpoint was high-risk enough to prioritize | 15% | 120 |

**All four themes point to the same root cause:** analysts are spending their cognitive bandwidth on context assembly rather than actual threat analysis. By the time they've gathered the context they need, they've lost momentum — or the next alert has already demanded their attention.

### Analyst Quotes

> *"I had to jump between our SIEM, EDR console, and threat intel feed just to understand basic context on one alert. By the time I had the full picture, 20 minutes were gone."*

> *"If I can't see the endpoint's recent history inline, I'm flying blind. I end up closing the alert and moving on."*

> *"There's no sense of whether an alert is part of something bigger or totally isolated. That context would change everything about how I investigate."*

> *"I don't know if the machine in question is a critical server or an intern's laptop. That matters a lot when I'm triaging 80+ alerts a day."*

### Segmentation: Mid-Size Teams Hit Hardest

Mid-size security teams (5-15 analysts) cited context-switching as the root cause of abandonment **2x more often** than enterprise teams (100+ analysts).

This matters because mid-size teams are our primary ICP — they don't have dedicated threat hunters or custom SIEM integrations. They're running lean. Enterprise teams can afford specialization: a threat hunter dedicated to SIEM correlation, another analyst who owns endpoint context. Mid-size teams have one analyst doing all of it, context-switching included. They bear the full cost of tool fragmentation in a way that enterprise analysts don't.

---

## Proposed Solution: AI-Guided Investigation View

**Concept:** When an analyst opens an alert, instead of a bare alert card, they land in an investigation view that automatically surfaces correlated context inline: endpoint risk score, recent behavioral history of the affected asset, related alerts from the same timeframe, threat intelligence matches, and AI-suggested next investigative steps.

No tool switching. No manual correlation. Everything needed to determine root cause is already assembled.

**Why this solves the problem:**
- Eliminates the primary blocker — analysts get the context that currently requires 4+ tool pivots delivered in a single view
- Reduces time-to-context so cognitive resources go toward analysis, not assembly
- Correlated events address the scope question directly — analysts can see whether an alert is isolated or part of a campaign
- Endpoint risk scoring answers the prioritization question — analysts know immediately whether the affected asset warrants deep investigation
- Low friction — no extra steps, no workflow change; context arrives when the analyst opens the alert

**What it's not:**
- Automated autonomous response (the platform assists, analysts decide)
- A replacement for the SIEM or threat intel feed (data still flows from those sources — it's surfaced inline, not siloed)
- A forced workflow change (analysts can still pivot to external tools; the goal is to make that unnecessary, not impossible)

---

## Expected Outcome

If AI-Guided Investigation View addresses the root cause (tool fragmentation accounts for ~85% of abandonment complaints across all four survey themes), we should expect:

- Reduction in mid-investigation abandonment, particularly for mid-size teams (5-15 analysts)
- Faster time-to-root-cause (target: under 22 min vs. current 47 min for investigations that complete)
- Higher investigation completion rate overall, with the largest gains in our target segment

Impact sizing and ROI analysis to follow in Phase 2.

---

## Next Steps

1. **Phase 2 — Impact Estimation:** Build ROI model and three-scenario analysis to determine build justification
2. **Engineering scoping:** Estimate implementation effort for correlated context assembly and AI suggestion layer
3. **Design exploration:** What does the investigation view look like? Which context signals are most critical to surface above the fold?
4. **Stakeholder alignment:** Share this document with Head of Product and Engineering Lead before resourcing conversation

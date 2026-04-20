# [Your Product] AI Investigation Assistant — Product Requirements Document
**Feature:** AI Investigation Assistant (Natural Language Threat Investigation)
**Strategic Angle:** Dual-mode — Quick Query + Investigation Chat
**Status:** Draft
**Author:** Product Team
**Last Updated:** 2026-03-11

---

# Problem Alignment

## Problem & Opportunity

### The Core Problem

Threat investigation breaks down at the moment speed matters most.

SOC analysts — especially Tier 1 — face a relentless queue of alerts and must decide in under five minutes whether an alert warrants full investigation or can be closed as a false positive. At that threshold, the friction of pivoting between a SIEM, an EDR console, a threat intelligence feed, and a ticketing system is not just inconvenient — it's operationally disqualifying. Analysts give up. Investigations are abandoned. Real threats go unresolved.

Our research makes this concrete:

- **60% of investigations started in [Your Product] are abandoned before root cause is determined** — analysts lose the thread mid-investigation while context-gathering
- **"I had to jump between our SIEM, EDR console, and threat intel feed just to understand basic context on one alert. By the time I had the full picture, 20 minutes were gone."** — Tier 1 SOC Analyst, 8-person security team
- **"If I could just ask the platform what happened on this endpoint in the last 48 hours and get a coherent answer, I'd close twice as many investigations."** — Threat Hunter, mid-size financial services company

This is not an analyst skill problem. Analysts know what questions to ask. The platform doesn't let them ask those questions directly — they have to approximate through manual queries, tab switching, and copy-pasting from five different UIs.

### The Opportunity

**23% of [Your Product]'s churned customers cited "too manual, not enough AI automation" as their primary reason for leaving.** This is the highest single churn driver in exit survey data and it is accelerating — AI is now table stakes in enterprise security tooling, not a differentiator.

**Revenue projection:** At 850 enterprise accounts with an average of 14 analysts per account, a conservative 20% adoption of an AI tier uplift at $5/seat/month = **~$287K additional ARR** in the first two quarters post-launch. At 40% adoption, that reaches **~$574K**. This directly advances the target of reaching $6M ARR (currently at $4.2M).

Beyond user demand, there is a strategic window that is closing. CrowdStrike launched Charlotte AI and it is live in customer environments now. Microsoft Copilot for Security is broadly available. Palo Alto's Cortex Copilot is shipping. **18% of prospects in Q4 pipeline evaluations mentioned AI capabilities in eval criteria** — and that number is growing quarter over quarter. [Your Product] has the investigation telemetry, endpoint behavioral data, and alert correlation context that competitors are attempting to synthesize from weaker data sources. The moat is the data. But the interface to that data needs to be natural language.

Every month without AI investigation capability is a month where CrowdStrike Charlotte AI can be used as a wedge in competitive deals, and a month where the 23% churn-from-missing-AI signal compounds.

### Why Now

Q2 is [Your Product]'s AI launch window. The competitive signal is live (not projected), churned customers are citing the missing capability explicitly, and building now allows us to iterate on real investigation workflows before competitors solidify their AI UX conventions.

**Capacity trade-off:** This feature requires the Core Platform squad (~4 engineers) for 10–12 weeks and data infrastructure work to expose behavioral history and correlated context via the AI query layer. The primary displacement is the compliance reporting module also on the Q2 roadmap. Recommendation: timebox compliance reporting to a 3-week parallel sprint; SOC compliance exports can ship in Q3 without competitive consequence. AI investigation cannot wait.

---

## High Level Approach

We will ship a **dual-mode AI Investigation Assistant** embedded natively in [Your Product]'s alert and investigation surfaces. Rather than a single AI interaction model, we offer two complementary modes designed for distinct SOC workflows:

**Mode 1 — Quick Query:** An analyst opens an alert and asks a single natural language question about it — "What other endpoints communicated with this IP in the last 24 hours?" — and gets an answer instantly, inline, without leaving the alert view. Designed for Tier 1 triage. Zero context-switching. The AI queries [Your Product]'s telemetry and returns a structured answer with supporting evidence.

**Mode 2 — Investigation Chat:** A persistent conversational session where analysts run a full multi-turn investigation. They can ask follow-up questions, narrow scope, pivot hypotheses, and build toward root cause through dialogue. Session state is preserved across the investigation lifecycle. Designed for Tier 2 analysts and threat hunters doing deep-dive work.

Both modes co-exist. A Tier 1 analyst triaging 80+ alerts per day reaches for Quick Query. A threat hunter investigating a suspected lateral movement campaign reaches for Investigation Chat. The same feature serves both personas without forcing a workflow compromise. The toggle between modes is a single tap from within the investigation view.

**What alternatives did we consider?**

| Approach | Why Not Selected |
|---|---|
| Quick Query only, no Chat | Misses the high-value deep investigation use case for Tier 2 and threat hunters |
| Investigation Chat only, no Quick Query | Fails the Tier 1 triage use case — Chat is too slow for 5-minute triage windows |
| Contextual tooltips and auto-correlation only | Lower AI bar; doesn't enable natural language queries; doesn't address the question-answering need |
| Full autonomous investigation and response | 12+ months, high risk, requires policy and compliance framework not yet in place; kills Q2 deadline |

We landed on the dual-mode approach because SOC workflows split cleanly across two jobs-to-be-done: fast triage (Tier 1, under 5 minutes per alert) and deep investigation (Tier 2 and hunters, 30-90 minutes per campaign). A feature that serves only one leaves the other persona with a reason to reach for a competing platform.

---

### Narrative

**Scenario A — The Tier 1 Analyst under alert pressure (Quick Query)**

Maya is a Tier 1 SOC analyst. She's processing her fourth hour of alert queue and encounters a suspicious outbound connection alert on a Windows endpoint. She needs to decide in under 5 minutes: escalate or close.

With Quick Query, she opens the alert in [Your Product] and types: "Has this endpoint made outbound connections to non-standard ports in the past 7 days?" The AI returns a structured response with three matching events from the last 48 hours, including timestamps, destination IPs, and threat intel context. Maya escalates immediately.

No tab switching. No SIEM query syntax. No manual copy-paste from the EDR console.

**Scenario B — The Threat Hunter running a deep investigation (Investigation Chat)**

Carlos is a threat hunter investigating a suspected lateral movement campaign. He has a starting alert — a failed authentication flood on a domain controller — but the scope is unclear.

He opens Investigation Chat and begins: "Show me all authentication events from this source IP in the last 72 hours across all assets." The AI responds with a summary and a timeline. Carlos follows up: "Which of those destination endpoints have had unusual process executions in the same timeframe?" The AI cross-references behavioral history and returns three candidate endpoints. Carlos continues the conversation for 45 minutes, building the full attack chain through dialogue rather than manual SIEM queries.

**Scenario C — Mode switching in a live investigation**

Maya is reviewing her escalation queue after finishing triage. She opens an escalated alert and starts a Quick Query to check scope. The answer surprises her — eight endpoints, not one. She taps "Deepen this investigation" and her Quick Query context carries directly into an Investigation Chat session. She doesn't re-explain what she was investigating. The conversation begins from where her query left off.

This is the experience we are building.

---

## Goals

The following metrics define success for V1. All measured at 60 days post-launch across active analysts (logged in at least once in the trailing 30 days).

| Goal | Metric | Target | Why This Number |
|---|---|---|---|
| Adoption — Awareness | % of active analysts who try Quick Query or Investigation Chat | 25% within first 30 days | Conservative given workflow change required; tests discoverability in alert view |
| Adoption — Retention | % of tryers who use it weekly | 15% at 60 days | Weekly usage = habit signal, not novelty |
| Investigation Completion | Investigation completion rate (root cause determined) | 40% → 58% (+18pp) | Primary product metric; validated by experiment phase |
| Speed | Median time-to-root-cause for completed investigations | 47 min → 22 min | Analyst capacity multiplier; validated in experiment (-25 min, 53% faster) |
| Analyst Capacity | Alerts handled per analyst per day | 80 → 130 | Capacity expansion signal; downstream from speed improvement |
| Revenue Signal | Conversion to AI tier (if launched) | Establish baseline; target 20% of accounts | Validates $5/seat/month uplift model |

**Guardrail metrics (must not regress):**
- Investigation completion rate must not decrease among any segment
- Alert queue processing time must not increase vs. baseline
- AI response accuracy (validated answer vs. ground truth from telemetry) must reach ≥90% in beta before GA rollout
- AI latency: p95 < 3 seconds for Quick Query (measured from query submit to response visible), p95 < 5 seconds for Investigation Chat responses

---

## Non-goals

The following are explicitly out of scope for V1. Each is a deliberate decision, not an oversight.

| Non-goal | Rationale |
|---|---|
| Autonomous threat response or remediation | V1 is analyst-assist, not autopilot; autonomous response requires a separate policy and compliance framework |
| External threat hunting integrations (VirusTotal, Shodan, etc.) | V1 queries [Your Product]'s internal telemetry only; external enrichment is V2 |
| Compliance report generation | Different persona, different use case; not a SOC workflow need; planned separately |
| Multi-language support | English-only in V1; internationalization requires significant LLM tuning and QA for security vocabulary |
| Voice input for investigations | Text-first in V1; voice adds complexity for SOC environments (open-plan offices, recordings policies) |
| Proactive AI alerting or push summaries | V1 is pull-based (analyst asks); proactive AI is V2 |
| Custom AI playbooks or user-defined prompt templates | High value but high complexity; V2 after we understand how analysts naturally query the system |
| AI-generated executive or board reports | Separate stakeholder need; not part of analyst workflow |
| Integration with third-party SIEM or EDR for query execution | V1 queries [Your Product] telemetry only; external SIEM integration is a separate platform initiative |

---

# Solution Alignment

## Key Features

### Plan of Record (V1)

**1. Quick Query (P0)**
A persistent natural language query input accessible from any alert view. Analyst types a question in plain English; the AI queries [Your Product]'s telemetry, behavioral history, and correlated alert data and returns a structured answer with supporting evidence inline. No query syntax required. Target: answer visible in under 3 seconds. Includes a one-tap "Expand to Investigation Chat" option to deepen any Quick Query into a full investigation session.

**2. Investigation Chat interface (P0)**
A persistent investigation panel (slide-out drawer in the alert view, full-page on dedicated investigation screens) where analysts conduct multi-turn conversational investigations. Maintains full session state throughout the investigation lifecycle. Supports text input. AI responses include supporting telemetry data, timestamps, affected assets, and suggested follow-up questions.

**3. Mode toggle (P0)**
A single-tap toggle between Quick Query and Investigation Chat within the investigation view. Switching to Quick Query does not end an active Chat session — it is preserved and resumed. Quick Query context can be promoted to Investigation Chat at any time, carrying prior query and response.

**4. Evidence citations (P0)**
Every AI response includes inline citations to the underlying telemetry events, alert records, or threat intel matches that informed the answer. Analysts can click any citation to view the raw source. This is non-negotiable: SOC analysts cannot act on AI output they cannot verify. Uncited responses are not acceptable in V1.

**5. Suggested follow-up questions (P1)**
After each Investigation Chat response, the AI surfaces 2-3 suggested follow-up questions based on the current investigation context. These are starting points, not prescriptions — analysts are free to ask anything. Designed to reduce the blank-canvas problem for Tier 1 analysts who know something is wrong but aren't sure how to proceed.

**6. Session persistence and handoff (P1)**
Investigation Chat sessions persist for the lifetime of an associated incident. If an analyst is reassigned or hands off an investigation to a colleague, the full chat history transfers with the incident. Handoff recipients can read the prior conversation and continue from where the previous analyst left off. Solves the institutional memory problem on shift handovers.

**7. Investigation summary export (P1)**
Analysts can export a structured investigation summary at any point — a formatted document containing the investigation timeline, key findings from AI responses, cited telemetry events, and analyst-authored notes. Intended for escalation documentation and incident records, not executive reporting.

**8. Analyst feedback on AI responses (P1)**
Thumbs up / thumbs down on every AI response, with an optional free-text field. Negative feedback flags the response for review. This is the primary mechanism for improving AI accuracy in production. Feedback data scoped per-account; [Your Product] does not use individual analyst feedback for model training without explicit opt-in (V1 default: opt-out).

**9. New analyst onboarding for AI (P2)**
Analysts with fewer than 10 investigations completed in [Your Product] see a guided first-use flow: example queries pre-populated in Quick Query, a brief walkthrough of how to read an AI response with citations. Addresses the cold-start problem where the AI has limited behavioral context for new accounts. New analyst mode also applies more conservative AI behavior: when data is ambiguous, the AI qualifies its answer rather than inferring.

### Future Considerations (V2+)

- Voice input for Investigation Chat
- External enrichment queries (VirusTotal, Shodan, MITRE ATT&CK mapping)
- Proactive AI investigation summaries pushed to analysts on high-severity alerts
- Custom investigation playbooks and prompt templates
- AI-assisted hypothesis generation based on historical campaign patterns
- Cross-account anonymized threat intelligence sharing via AI context

---

### Key Flows

**Flow 1: Quick Query — Single Alert Question (Primary Triage Flow)**

```
Analyst opens alert in [Your Product]
→ AI Query input visible in alert sidebar (placeholder: "Ask about this alert...")
→ Analyst types: "Has this endpoint connected to external IPs on non-standard ports
   in the last 7 days?"
→ Analyst submits query
→ Processing indicator (<3 seconds)
→ AI response appears inline with:
   - Direct answer ("Yes — 3 connections found")
   - Summary table: timestamp, destination IP, port, protocol
   - Inline citation links to underlying telemetry events
   - Suggested follow-ups: "View all endpoints that connected to these IPs"
→ Analyst acts: escalates, closes, or taps "Expand to Investigation Chat"
```

Error states:
- No relevant data found → AI states clearly: "No events matching this query in the selected timeframe. Try extending the window or broadening the scope."
- Query too ambiguous → AI asks one clarifying question: "Are you asking about this specific endpoint, or all endpoints in the affected subnet?"
- Telemetry data unavailable → Clear error with explanation; fallback to manual investigation link
- Latency exceeds 5 seconds → Loading state with cancel option; no silent hang

---

**Flow 2: Investigation Chat — Lateral Movement Campaign**

```
Analyst opens high-severity alert: "Suspicious authentication — domain controller"
→ Taps "Start Investigation" → Investigation Chat panel opens
→ Analyst: "Show me all authentication events from this source IP in the last 72 hours."
→ AI returns: timeline summary, 47 events across 12 destination endpoints, cited telemetry
→ Analyst: "Which of those destination endpoints had unusual process executions
   in the same window?"
→ AI cross-references behavioral history: 3 endpoints flagged with anomalous
   process trees, cited with PIDs and timestamps
→ Analyst: "Is any of these endpoints a critical asset?"
→ AI returns risk scores and asset classifications for all 3 (2 high-risk servers)
→ Analyst escalates; taps "Export Summary" for incident ticket
→ Summary auto-populated with investigation timeline and key findings
```

---

**Flow 3: Mode Switch — Quick Query to Investigation Chat**

```
Analyst is triaging alert via Quick Query
→ Receives answer: "8 endpoints affected, not 1"
→ Taps "Expand to Investigation Chat"
→ Chat panel opens with prior query and response pre-loaded as context
→ AI: "Based on your query, here are suggested next steps: [3 options]"
→ Analyst continues investigation without re-stating context
→ Chat session linked to incident; persists through shift handover
```

---

**Flow 4: Shift Handover — Session Persistence**

```
Analyst A has been investigating a campaign for 2 hours via Investigation Chat
→ Shift ends; incident reassigned to Analyst B
→ Analyst B opens incident in [Your Product]
→ Investigation Chat panel shows full prior conversation history
→ AI: "Investigation was last updated 2h ago. Summary: [3-sentence brief]"
→ Analyst B picks up exactly where Analyst A left off
```

---

### Key Logic

**Query execution and response rules:**

| Scenario | Behavior |
|---|---|
| Analyst is inside an alert when invoking Quick Query | Query context defaults to that alert's associated assets and timeframe |
| Query covers assets analyst does not have access to | AI returns only data within analyst's permission scope; notes any scope limitation |
| Timeframe not specified in query | AI defaults to alert timestamp ±24 hours; notes the assumption in the response |
| Query is ambiguous | AI asks one clarifying question before executing; never executes on ambiguous queries |
| No relevant telemetry data exists | AI states clearly that no data was found; does not fabricate or infer |
| Alert involves assets not yet ingested | AI surfaces a warning; responds based on available data |

**Confidence and citation rules:**
- **Every AI response includes citations** — no uncited responses in V1; if data cannot be cited, the AI states it cannot answer with confidence
- **>90% confidence** — respond directly with citations
- **50–90% confidence** — qualify the response ("Based on available data, this appears to be...") with citations
- **<50% confidence** — AI states it cannot determine an answer and suggests what additional data would help

**Investigation Chat session rules:**
- Sessions persist for the lifetime of the associated incident; no arbitrary expiration
- No actions taken without analyst confirmation (AI queries data; it does not take remediation actions)
- AI surfaces at most 2-3 suggested follow-ups per turn — not a required path
- Session history transferable to any analyst with access to the incident

**Chat session storage architecture:**
- Sessions stored server-side, scoped per incident (not per analyst or device)
- Storage: conversation turns stored as structured JSON in [Your Product]'s existing data layer; estimated 5–20KB per session depending on response complexity
- Retention: sessions retained for the lifetime of the associated incident plus 90 days post-closure for audit purposes
- At 850 accounts × average 14 analysts × 15% using Chat daily = ~1,785 active sessions/day; within current infrastructure capacity
- Engineering to confirm storage model before Chat build begins (Week 7)

**AI response scope and data access:**
- AI queries [Your Product]'s internal telemetry, behavioral history, correlated alerts, and threat intel matches only
- No outbound queries to third-party services in V1
- Responses scoped to the analyst's account and permission level; no cross-account data exposure
- All queries and responses logged for audit trail; retained per account data retention policy

**Privacy and data handling:**
- Investigation Chat content transmitted to [Your Product]'s AI backend over HTTPS with TLS 1.3
- Workspace telemetry data used for AI query execution is scoped to the analyst's accessible data
- AI conversation content not used for model training without explicit account-level opt-in (V1 default: opt-out)
- All query and response data retained per [Your Product]'s standard enterprise data retention policy; configurable per account

---

# Development and Launch Planning

## Key Milestones

| Milestone | Target Date | Owner |
|---|---|---|
| PRD finalized and approved | Week 1 | PM |
| Legal/privacy/compliance review of AI data handling | Week 2 | Legal + PM |
| Technical spec complete | Week 3 | Engineering Lead |
| Design: Quick Query UI, Investigation Chat panel, citation components | Week 3–4 | Design |
| Quick Query — internal build | Week 5–7 | Core Platform Squad |
| Investigation Chat — internal build | Week 7–10 | Core Platform Squad |
| Mode toggle + session persistence + handover flow | Week 10–11 | Engineering |
| Internal QA + accuracy testing vs. ground truth telemetry | Week 11–12 | QA + PM |
| Closed beta (15–25 accounts, mid-size teams priority) | Week 13–14 | PM + Customer Success |
| Beta feedback synthesis + critical fixes | Week 14–15 | PM + Engineering |
| General availability launch | Week 16 | Full team |
| 30-day post-launch metrics review | Week 20 | PM |

## Operational Checklist

**Legal / Compliance:**
- [ ] Update privacy policy to reflect AI query processing and conversation data handling
- [ ] Confirm conversation data is not used for model training by default; document opt-in path
- [ ] GDPR compliance review for EU accounts (data residency for conversation logs)
- [ ] SOC 2 audit trail: confirm AI query and response logging meets audit requirements
- [ ] Review AI provider data processing terms; confirm no training on customer data

**Engineering / Infrastructure:**
- [ ] Select LLM provider and confirm data handling terms (evaluate: GPT-4o, Claude, Gemini for security query accuracy)
- [ ] Build telemetry query layer that AI can execute against safely (read-only, scoped to account)
- [ ] Define latency SLOs: Quick Query p95 <3s; Investigation Chat p95 <5s
- [ ] Instrument full AI usage funnel: query submitted, response received, citation clicked, feedback submitted, session exported
- [ ] Build account-level opt-in/opt-out for AI training data
- [ ] Define rollout flag for percentage-based rollout (start at 5% of accounts)

**Design:**
- [ ] Quick Query: input field, loading state, response card with citations, suggested follow-ups
- [ ] Investigation Chat: panel, conversation thread, evidence citation cards, session summary, export flow
- [ ] Mode toggle UX within investigation view
- [ ] Handover state: how prior session history is presented to incoming analyst
- [ ] Error states: no data, ambiguous query, permission scope warning, latency timeout

**Marketing / GTM:**
- [ ] Launch announcement to all 850 accounts
- [ ] Demo video: Quick Query triage flow + Investigation Chat lateral movement campaign example
- [ ] Sales battlecard: AI Investigation Assistant vs. CrowdStrike Charlotte AI, Microsoft Copilot for Security, Palo Alto Cortex Copilot
- [ ] Pricing page update if gated to AI tier
- [ ] Case study plan: identify 2-3 beta accounts willing to share investigation time metrics

**Customer Success:**
- [ ] Help center: Quick Query usage, Investigation Chat walkthrough, session handover, export guide
- [ ] Support team training on common AI response errors and escalation path
- [ ] In-app feedback mechanism (thumbs up/down on every AI response)
- [ ] Beta customer success check-ins scheduled (bi-weekly during beta period)

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| AI response accuracy below 90% | Medium | High | Hard gate on beta → GA. Delay if not met. Define test set of ground-truth queries before build begins. |
| AI response latency exceeds 3s for Quick Query | Medium | High | Test on real-world telemetry volumes in beta; optimize query layer before GA |
| Analysts don't trust AI-cited answers | Medium | High | Evidence citations are non-negotiable in V1; every response must cite sources |
| Enterprise accounts experience workflow disruption | Medium | Medium | Exclude enterprise from initial rollout; start enterprise-specific discovery in parallel |
| Analysts use AI output without verification and miss errors | Low | High | Feedback mechanism + analyst training; monitoring for false negative rate post-launch |
| Competitor ships materially better AI investigation feature before GA | High | Medium | Stay on Q2 timeline; differentiate on citation quality and session handover — capabilities Charlotte AI does not have at launch |

---

## Open Questions

1. **Pricing — OPEN:** Should AI Investigation Assistant launch included in all paid plans or gated to an AI add-on tier? Arguments for inclusion: maximizes adoption data in the critical competitive window; gating fragments analyst teams (some get AI, some don't). Arguments for gating: $287K ARR upside is meaningful; gating creates clear upgrade conversation. Recommendation pending leadership input — needs resolution before GA.

2. **LLM provider — OPEN:** Recommended provider is TBD pending accuracy evaluation on [Your Product] telemetry query vocabulary. GPT-4o and Claude both show strong structured query performance; evaluation should weight recall accuracy on security-specific entity extraction (IPs, hashes, CVEs, process names). Engineering to complete evaluation by Week 3.

3. **Investigation Chat session length:** V1 spec: sessions persist for incident lifetime. Consider whether a separate "exploration" mode with a time-limited session (e.g., 24 hours) would serve ad-hoc queries that don't attach to a formal incident.

4. **Proactive AI in Chat:** Should Investigation Chat suggest hypotheses based on patterns across the account's alert history ("Similar lateral movement pattern observed 3 weeks ago — want me to pull that timeline?"). High value signal to watch for in beta. Deferred to V2.

5. **Feedback loop and model improvement:** Thumbs down feedback is collected in V1. Define the process for [Your Product] team to review flagged responses and the cadence for model fine-tuning based on collected signals. Needs an owner before launch.

---

## Appendix

**Key Research Sources:**
- [Your Product] Q4 2025 Investigation Funnel Analysis — 60% abandonment rate at root cause determination
- SOC Analyst Survey (n=800) — context-switching root cause; top abandonment themes
- Churn Exit Survey Analysis — 23% citing "too manual, not enough AI automation"
- [Your Product] Q4 Pipeline Analysis — 18% of prospects citing AI in eval criteria
- Competitive Analysis: CrowdStrike Charlotte AI (live), Microsoft Copilot for Security (live), Palo Alto Cortex Copilot (live)
- AI-Guided Investigation View A/B Experiment — +14.4pp completion lift for mid-size teams (p < 0.001); -25 min time-to-root-cause

**Pre-launch research required:**
- Accuracy evaluation: build a test set of 50+ investigation queries with ground-truth answers verified against telemetry; measure AI recall and precision before beta
- Usability test: error recovery flow with simulated 90% accuracy — observe how often analysts catch incorrect citations in the Quick Query triage context
- Concept test: Investigation Chat with 6–8 threat hunters and Tier 2 analysts to validate multi-turn conversational investigation before committing Chat to full V1 scope
- Shift handover scenario testing: test session handover flow with pairs of analysts to validate that context transfer is legible to incoming analysts without prior session context

**Personas referenced:**
- **Maya** — SOC Analyst Tier 1, overwhelmed with 80+ alerts/day. Needs fast context to triage in <5 min per alert. Primary Quick Query user.
- **Carlos** — Threat Hunter, proactively investigating TTPs. Needs deep multi-turn investigation sessions. Primary Investigation Chat user.
- **Sarah Chen** — CISO, needs MTTD/MTTR improvements for board reporting. Wants ROI on security platform investment. Indirect beneficiary; primary audience for investigation summary exports and metrics dashboard.

**Changelog:**
- v0.1 — Initial draft (2026-03-11). Combined from problem analysis, impact model, and experiment readout. Dual-mode structure validated by A/B experiment segment results.
- v0.2 — (2026-03-11) Addressed security compliance, engineering, and executive feedback: added evidence citation requirement, session handover flow, AI data handling policy, latency SLOs, enterprise exclusion rationale, and pre-launch accuracy evaluation requirement.

**FAQ:**

*Q: Why dual mode instead of one unified interface?*
A: SOC workflows split cleanly across two jobs. Tier 1 analysts need instant answers within a 5-minute triage window — Investigation Chat is too slow and too deep for that use case. Threat hunters need 30-90 minute conversational investigation sessions — Quick Query is too shallow. A single interface optimized for one fails the other. The toggle costs little in UX complexity and serves both personas without compromise.

*Q: Will AI-generated investigations be admissible in incident records?*
A: AI responses are supporting evidence, not conclusions. Every response cites the underlying telemetry events, which are the authoritative record. The AI is helping analysts find and interpret evidence faster — the evidence itself comes from [Your Product]'s telemetry, which is the system of record.

*Q: What happens if the AI returns a wrong answer?*
A: Every response includes citations to underlying data, so analysts can verify. Thumbs-down feedback flags the response for review. The AI is designed to express uncertainty rather than confabulate — if data is ambiguous or unavailable, it says so. The goal is a useful tool, not an infallible oracle.

*Q: Can analysts use this for threat hunting even if no alert is active?*
A: V1 surfaces Investigation Chat within the investigation view of an existing alert or incident. Standalone threat hunting mode — querying telemetry without an associated alert — is a high-value V2 feature. We'll learn how analysts want to use free-form investigation from beta before committing to the UX.

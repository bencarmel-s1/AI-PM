# Story Breakdown: AI-Assisted Alert Triage

**PRD Source:** `ai-alert-triage-prd-final.md`
**Destination:** Jira: WF
**Date:** 2026-04-03
**PM:** Jamie Chen
**Status:** Pushed

---

## Summary

| Metric | Value |
|---|---|
| Total Epics | 4 |
| Total Stories | 18 |
| Total Story Points | 57 |
| Estimated Sprints | 3 |
| V1 Scope | AI triage panel surfacing threat context, analyst verdict, and confidence score for endpoint alerts |
| Out of Scope (V1) | Email/Slack notification integration, bulk triage actions, mobile support, non-endpoint alert types |

---

## Epic Overview

| # | Epic | Stories | Points | Priority |
|---|---|---|---|---|
| 1 | Triage Panel — Core UI | 5 | 18 | P0 |
| 2 | AI Context Engine — Backend | 5 | 21 | P0 |
| 3 | Analyst Feedback & Learning Loop | 4 | 11 | P1 |
| 4 | Supporting: Tracking, States & Rollout | 4 | 7 | P0 |

---

## Epic 1: Triage Panel — Core UI

**Scope:** Build the alert detail panel that displays AI-generated threat context, confidence score, and recommended verdict to the analyst.
**Priority:** P0
**Suggested Sprint:** Sprint 1
**Total Points:** 18

---

### Story 1.1: Triage Panel Shell

**User Story:**
As a SOC analyst, I want to see a triage panel when I open an alert so that I have a consistent place to review AI-generated context.

**Description:**
Create the panel container component in the alert detail view. The panel should render on the right side of the existing alert detail layout without displacing current content. This story covers the shell only — no AI content yet; that comes in Epic 2.

**Acceptance Criteria:**
- [ ] Panel renders to the right of the existing alert detail when an alert is opened
- [ ] Panel is collapsible and the collapsed state persists per-user in local storage
- [ ] Panel renders correctly at 1280px, 1440px, and 1920px viewport widths
- [ ] Panel shows a loading skeleton while AI context is being fetched
- [ ] Panel does not render for alert types outside the V1 scope (non-endpoint alerts)

**Story Type:** Feature
**Labels:** frontend
**Story Points:** 3
**Dependencies:** None

---

### Story 1.2: Confidence Score Display

**User Story:**
As a SOC analyst, I want to see the AI confidence score for each alert so that I can calibrate how much to trust the AI recommendation.

**Description:**
Display the AI confidence score (0–100) as a percentage with a visual indicator (color-coded: red <40, yellow 40–70, green >70). The score comes from the AI Context Engine (Epic 2, Story 2.1). This story is purely the UI display — no score calculation logic.

**Acceptance Criteria:**
- [ ] Confidence score displays as a percentage (e.g. "87%")
- [ ] Score is color-coded: red for <40, yellow for 40–70, green for >70
- [ ] Tooltip on hover explains what confidence score means in plain language
- [ ] Score displays "Analyzing…" while the backend response is pending
- [ ] Score displays "Unavailable" with a neutral indicator if the AI engine returns an error

**Story Type:** Feature
**Labels:** frontend
**Story Points:** 2
**Dependencies:** Story 1.1 (panel shell), Story 2.1 (confidence score API)

---

### Story 1.3: Threat Context Summary

**User Story:**
As a SOC analyst, I want to see a 3–5 sentence AI-generated threat summary for each alert so that I can understand the likely threat without reading raw telemetry.

**Description:**
Render the AI-generated threat context summary in the triage panel. Summary content comes from the AI Context Engine. This story handles display, truncation (if over 500 chars, show "Read more"), and the copy-to-clipboard action for analyst notes workflows.

**Acceptance Criteria:**
- [ ] Summary renders as plain text (no markdown, no code blocks) in the panel
- [ ] If summary exceeds 500 characters, truncate at sentence boundary with "Read more" link that expands inline
- [ ] "Copy to clipboard" icon copies the full summary text including expand content
- [ ] If AI engine returns no summary, panel shows "No context available for this alert"
- [ ] Summary text is selectable (not locked behind a non-selectable div)

**Story Type:** Feature
**Labels:** frontend
**Story Points:** 3
**Dependencies:** Story 1.1, Story 2.2 (threat context API)

---

### Story 1.4: Recommended Verdict

**User Story:**
As a SOC analyst, I want to see the AI's recommended verdict (True Positive / False Positive / Needs Investigation) so that I have a starting point for my triage decision.

**Description:**
Display the AI-recommended verdict prominently in the panel above the confidence score. The verdict is one of three values: True Positive, False Positive, or Needs Investigation. This story covers display only — analyst override is in Story 3.1.

**Acceptance Criteria:**
- [ ] Verdict displays as a labeled badge: "True Positive" (red), "False Positive" (green), "Needs Investigation" (yellow)
- [ ] Verdict badge includes the AI icon/label so analysts know it is AI-generated, not human
- [ ] If no verdict is returned by the AI engine, badge displays "Pending" in grey
- [ ] Clicking the badge does not trigger any action (override is a separate component, Story 3.1)

**Story Type:** Feature
**Labels:** frontend
**Story Points:** 2
**Dependencies:** Story 1.1, Story 2.1

---

### Story 1.5: MITRE ATT&CK Technique Tags

**User Story:**
As a SOC analyst, I want to see MITRE ATT&CK technique tags surfaced for each alert so that I can quickly identify the attack pattern without manual lookup.

**Description:**
Display the top 1–3 MITRE ATT&CK technique IDs and names returned by the AI Context Engine. Each tag links to the official MITRE ATT&CK page for that technique. This is informational only — no filtering or search functionality in V1.

**Acceptance Criteria:**
- [ ] Up to 3 MITRE ATT&CK technique tags render as pills below the threat context summary
- [ ] Each tag displays the technique ID and short name (e.g. "T1059 — Command and Scripting Interpreter")
- [ ] Each tag is a hyperlink that opens the MITRE ATT&CK page in a new tab
- [ ] If no techniques are returned, the section is hidden (not "No techniques found")
- [ ] Tags render correctly when 1, 2, or 3 techniques are returned

**Story Type:** Feature
**Labels:** frontend
**Story Points:** 2
**Dependencies:** Story 1.1, Story 2.2

---

## Epic 2: AI Context Engine — Backend

**Scope:** Build the backend service that generates threat context, confidence scores, and MITRE tags for endpoint alerts on demand.
**Priority:** P0
**Suggested Sprint:** Sprint 1 (parallel with Epic 1)
**Total Points:** 21

---

### Story 2.1: Alert Scoring API Endpoint

**User Story:**
As a frontend component, I want a POST endpoint that accepts an alert ID and returns a confidence score and recommended verdict so that the triage panel can display AI-generated guidance.

**Description:**
Build the `/api/v1/alerts/{id}/triage-score` endpoint. The endpoint calls the AI inference service, applies the confidence scoring model, and returns the verdict + score. Target p95 latency: <2 seconds. This is the critical path for the panel — Epic 1 Stories 1.2 and 1.4 are blocked until this is available in staging.

**Acceptance Criteria:**
- [ ] `POST /api/v1/alerts/{id}/triage-score` returns `{ confidence: number, verdict: "TP" | "FP" | "NEEDS_INVESTIGATION" }` in under 2 seconds (p95)
- [ ] Returns 404 if alert ID does not exist
- [ ] Returns 503 with `{ error: "AI service unavailable" }` if inference service is down (panel should show graceful degraded state)
- [ ] Endpoint is authenticated — requires valid session token
- [ ] Results are cached per alert ID for 5 minutes to prevent redundant inference calls

**Story Type:** Feature
**Labels:** backend, API
**Story Points:** 5
**Dependencies:** None (can be built in parallel with Epic 1)

---

### Story 2.2: Threat Context Generation

**User Story:**
As a frontend component, I want a GET endpoint that returns a human-readable threat summary and MITRE ATT&CK tags for an alert so that the panel can display contextual intelligence.

**Description:**
Build the `/api/v1/alerts/{id}/triage-context` endpoint. This calls the LLM summarization pipeline with the alert telemetry and returns a plain-text summary (max 600 chars) plus up to 3 MITRE ATT&CK technique mappings. Summary must be in plain English, no jargon, written for a Tier 1 analyst.

**Acceptance Criteria:**
- [ ] `GET /api/v1/alerts/{id}/triage-context` returns `{ summary: string, techniques: [{ id: string, name: string }] }` within 3 seconds (p95)
- [ ] Summary is between 100 and 600 characters
- [ ] Summary does not contain raw JSON, log lines, or technical identifiers
- [ ] Returns up to 3 MITRE technique objects; returns empty array if no techniques identified
- [ ] Returns 404 if alert ID does not exist
- [ ] Returns cached result within 5 minutes of first call for the same alert ID

**Story Type:** Feature
**Labels:** backend, API
**Story Points:** 8
**Dependencies:** None (can be built in parallel with Epic 1)

---

### Story 2.3: Telemetry Pre-processing Pipeline

**User Story:**
As the AI inference service, I want alert telemetry normalized before it enters the scoring model so that the model receives consistent input regardless of alert source.

**Description:**
Build the pre-processing pipeline that normalizes raw alert telemetry (process trees, network connections, file events) into the structured format the inference model expects. This is a prerequisite for Stories 2.1 and 2.2 — they cannot work without normalized input.

**Acceptance Criteria:**
- [ ] Pipeline accepts raw telemetry from all V1 supported endpoint agent versions (>= 22.1)
- [ ] Normalizes process tree, network, and file event fields into the inference model schema
- [ ] Logs a warning (does not fail) for unrecognized telemetry fields — they are dropped
- [ ] Processing adds <100ms to total API latency (measured in integration tests)
- [ ] Unit test coverage: >80% of pipeline branches

**Story Type:** Tech Debt
**Labels:** backend, data
**Story Points:** 5
**Dependencies:** None

---

### Story 2.4: Inference Service Integration

**User Story:**
As the triage scoring API, I want a resilient integration with the AI inference service so that transient failures don't surface as errors to the analyst.

**Description:**
Wrap the inference service call with retry logic (3 attempts, exponential backoff), circuit breaker (open after 5 consecutive failures), and fallback behavior (return null score/verdict so the panel degrades gracefully). This story is about reliability, not the scoring logic itself.

**Acceptance Criteria:**
- [ ] Service retries up to 3 times with 200ms, 400ms, 800ms backoff before returning 503
- [ ] Circuit breaker opens after 5 consecutive failures; logs circuit state changes
- [ ] When circuit is open, API returns 503 immediately without calling inference service
- [ ] Circuit closes automatically after 30 seconds and retries
- [ ] Integration test covers: success path, retry path, circuit open path

**Story Type:** Tech Debt
**Labels:** backend, infra
**Story Points:** 3
**Dependencies:** Story 2.1, Story 2.2

---

### Story 2.5: Spike — LLM Prompt Evaluation

**User Story:**
As the team, I want to evaluate 3 candidate prompts for threat context generation before Sprint 1 ends so that we choose the best prompt before committing to Story 2.2.

**Description:**
Run a structured evaluation of 3 LLM prompt variations against a test set of 50 real endpoint alerts (de-identified). Score each prompt on: accuracy of verdict, summary quality (readability, length, no jargon), and latency. Produce a recommendation doc. This is a time-boxed spike — 2 days maximum.

**Acceptance Criteria:**
- [ ] 3 candidate prompts evaluated against the same 50-alert test set
- [ ] Each prompt scored on: verdict accuracy (%), summary readability (human rating 1–5), average latency
- [ ] Recommendation document produced with: winning prompt, rationale, rejected alternatives
- [ ] Spike completed before end of Sprint 1 so Story 2.2 can use the winning prompt

**Story Type:** Spike
**Labels:** backend, data
**Story Points:** 3 *(time-boxed: 2 days)*
**Dependencies:** None (run in parallel with Epic 1 UI work)

---

## Epic 3: Analyst Feedback & Learning Loop

**Scope:** Allow analysts to override the AI verdict and capture that feedback for model improvement.
**Priority:** P1
**Suggested Sprint:** Sprint 2
**Total Points:** 11

---

### Story 3.1: Analyst Verdict Override

**User Story:**
As a SOC analyst, I want to override the AI's recommended verdict with my own so that I can record my actual decision and correct AI errors.

**Description:**
Add an override control below the AI verdict badge. The analyst selects their verdict (True Positive / False Positive / Needs Investigation) and optionally adds a short note. Submitting the override updates the alert record and records the feedback event. The AI verdict badge remains visible with an "Analyst overrode" label to distinguish AI vs. human decisions.

**Acceptance Criteria:**
- [ ] Analyst can select one of three verdicts from a dropdown/button group
- [ ] Optional free-text note field (max 280 characters) appears after selecting a verdict
- [ ] Submitting override records the analyst verdict on the alert record
- [ ] After submission, the panel shows "Your verdict: [X]" alongside the original AI verdict (not replacing it)
- [ ] Override can be changed — re-submitting replaces the previous analyst verdict
- [ ] Override is attributed to the submitting analyst (not anonymous)

**Story Type:** Feature
**Labels:** frontend, backend, API
**Story Points:** 5
**Dependencies:** Story 1.4 (verdict display), Story 2.1 (verdict source)

---

### Story 3.2: Feedback Capture API

**User Story:**
As the feedback system, I want a POST endpoint that records analyst verdict overrides so that the data is available for model retraining.

**Description:**
Build the `/api/v1/alerts/{id}/feedback` endpoint that accepts analyst verdict overrides and stores them in the feedback database. This data feeds the offline model retraining pipeline — not real-time. Schema must include: alert ID, analyst ID, AI verdict, analyst verdict, analyst note, timestamp.

**Acceptance Criteria:**
- [ ] `POST /api/v1/alerts/{id}/feedback` accepts `{ verdict: string, note?: string }` and returns 201
- [ ] Feedback record includes: alert_id, analyst_id, ai_verdict, analyst_verdict, note, submitted_at
- [ ] Returns 400 if verdict is not one of the three valid values
- [ ] Returns 404 if alert ID does not exist
- [ ] Duplicate submissions for the same alert by the same analyst update the existing record (upsert)

**Story Type:** Feature
**Labels:** backend, API, data
**Story Points:** 3
**Dependencies:** Story 2.1

---

### Story 3.3: Feedback Dashboard (Read-Only)

**User Story:**
As a PM or team lead, I want a read-only view of AI vs. analyst verdict agreement rates so that I can track model accuracy over time.

**Description:**
Add a simple read-only dashboard tab to the existing Analytics section showing: total alerts triaged, AI verdict distribution, analyst override rate, and agreement rate by alert type. This is display only — no filters, exports, or drill-down in V1. The data comes from the feedback table (Story 3.2).

**Acceptance Criteria:**
- [ ] Dashboard shows: total alerts with AI triage (last 30 days), AI verdict distribution (% TP / FP / NI), analyst override rate (%), agreement rate (AI verdict matched analyst verdict)
- [ ] All metrics update once per hour (not real-time)
- [ ] Dashboard is visible to users with PM or Team Lead role only
- [ ] If fewer than 10 feedback records exist, dashboard shows "Not enough data yet" instead of misleading percentages

**Story Type:** Feature
**Labels:** frontend, backend
**Story Points:** 3
**Dependencies:** Story 3.2

---

## Epic 4: Supporting — Tracking, States & Rollout

**Scope:** Analytics event tracking, error/empty states, and feature flag rollout to ensure a clean launch.
**Priority:** P0
**Suggested Sprint:** Sprint 1–2 (alongside each feature story)
**Total Points:** 7

---

### Story 4.1: Analytics Event Tracking

**User Story:**
As a data consumer, I want all triage panel interactions tracked so that we can measure adoption, engagement, and model impact after launch.

**Description:**
Instrument all key user interactions in the triage panel with Amplitude events. Events must fire on first occurrence only (not on re-renders). This story should be built alongside the UI stories in Epics 1 and 3, not after.

**Acceptance Criteria:**
- [ ] `triage_panel_opened` fires when analyst opens an alert with the panel visible
- [ ] `triage_panel_collapsed` / `triage_panel_expanded` fires on collapse/expand
- [ ] `triage_context_viewed` fires when the threat summary is fully visible (not truncated)
- [ ] `triage_context_expanded` fires when analyst clicks "Read more"
- [ ] `analyst_verdict_override_submitted` fires with properties: `{ ai_verdict, analyst_verdict, has_note: boolean }`
- [ ] All events appear in Amplitude within 1 hour of firing
- [ ] Events do not fire in local or staging environments

**Story Type:** Tech Debt
**Labels:** frontend, data
**Story Points:** 3
**Dependencies:** Story 1.1, Story 3.1

---

### Story 4.2: Error States & Empty States

**User Story:**
As a SOC analyst, I want clear, helpful messages when the AI triage service is unavailable or returns no results so that I'm never left with a blank or broken panel.

**Description:**
Implement all degraded states for the triage panel. These must be designed and built before launch — the worst experience is a blank panel with no explanation during an incident.

**Acceptance Criteria:**
- [ ] AI service unavailable → panel shows "AI triage is temporarily unavailable. Triage manually." with a link to the standard triage guide
- [ ] AI context loading >5 seconds → panel shows a timeout message: "Taking longer than expected. Refresh to retry."
- [ ] No verdict returned → verdict area hidden (not showing "null" or empty badge)
- [ ] No threat context returned → summary area shows "No context available for this alert type"
- [ ] No MITRE tags returned → MITRE section is hidden entirely (not "No techniques found")

**Story Type:** Feature
**Labels:** frontend
**Story Points:** 2
**Dependencies:** Story 1.1, Story 1.2, Story 1.3

---

### Story 4.3: Feature Flag & Rollout Configuration

**User Story:**
As a PM, I want the triage panel behind a feature flag so that I can control rollout percentage and disable it instantly if issues arise post-launch.

**Description:**
Wrap the triage panel render in a feature flag check (`ai_triage_panel_enabled`). The flag is managed in LaunchDarkly. V1 rollout plan: 10% → 25% → 50% → 100% over 2 weeks. This story is a prerequisite for launch — the panel must not be visible to all users on day one.

**Acceptance Criteria:**
- [ ] Triage panel renders only when `ai_triage_panel_enabled` flag is true for the current user
- [ ] Flag is evaluated client-side; panel is not rendered (not just hidden) when flag is off
- [ ] Flag targeting supports: percentage rollout, user ID targeting, account ID targeting
- [ ] Flag default: off (new users do not see panel unless explicitly targeted)
- [ ] LaunchDarkly flag created and configured in the Production environment before Sprint 3 ends

**Story Type:** Tech Debt
**Labels:** frontend, infra
**Story Points:** 2
**Dependencies:** Story 1.1

---

## Dependency Map

```
Story 2.3 (Telemetry Pre-processing)
  → blocks Story 2.1 (Scoring API)
  → blocks Story 2.2 (Context Generation)

Story 2.5 (Prompt Spike)
  → blocks Story 2.2 (Context Generation)

Story 1.1 (Panel Shell)
  → blocks Story 1.2 (Confidence Score Display)
  → blocks Story 1.3 (Threat Context Summary)
  → blocks Story 1.4 (Recommended Verdict)
  → blocks Story 1.5 (MITRE Tags)
  → blocks Story 4.3 (Feature Flag)

Story 2.1 (Scoring API)
  → blocks Story 1.2 (Confidence Score Display)
  → blocks Story 1.4 (Recommended Verdict)
  → blocks Story 3.1 (Analyst Override)

Story 2.2 (Context Generation)
  → blocks Story 1.3 (Threat Context Summary)
  → blocks Story 1.5 (MITRE Tags)

Story 2.4 (Inference Resilience)
  → depends on Story 2.1, Story 2.2

Story 3.1 (Analyst Override UI)
  → blocks Story 3.2 (Feedback API)
  → blocks Story 4.1 (Analytics Events)

Story 3.2 (Feedback API)
  → blocks Story 3.3 (Feedback Dashboard)

Story 1.1, Story 3.1
  → blocks Story 4.1 (Analytics Events)

Story 1.1, Story 1.2, Story 1.3
  → blocks Story 4.2 (Error States)
```

---

## Out of Scope (V1)

- Email and Slack notification integration for AI triage decisions
- Bulk triage actions (triaging multiple alerts at once using AI)
- Mobile / responsive layout for the triage panel
- Non-endpoint alert types (Cloud, Identity, Network alerts)
- Automated triage (analyst-free verdict submission)
- Real-time model retraining from feedback (offline retraining only in V1)

---

## Open Questions

| # | Question | Owner | Needed By |
|---|---|---|---|
| 1 | What is the fallback UX if the analyst's role doesn't have access to the feedback dashboard? Silent hide or permission error? | PM | Sprint 2 start |
| 2 | Should analyst override notes be visible to other analysts on the same alert, or only to the submitter? | PM + Security | Sprint 2 start |
| 3 | Does the feature flag need to support disabling per-account (not just per-user) for early enterprise pilots? | PM + Eng | Sprint 1 end |

---

## Push Log

| Epic | Jira Epic Key | Stories Created |
|---|---|---|
| Triage Panel — Core UI | WF-4201 | WF-4202, WF-4203, WF-4204, WF-4205, WF-4206 |
| AI Context Engine — Backend | WF-4207 | WF-4208, WF-4209, WF-4210, WF-4211, WF-4212 |
| Analyst Feedback & Learning Loop | WF-4213 | WF-4214, WF-4215, WF-4216 |
| Supporting: Tracking, States & Rollout | WF-4217 | WF-4218, WF-4219, WF-4220 |

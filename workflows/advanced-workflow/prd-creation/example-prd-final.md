# TaskFlow AI Voice Chat — Product Requirements Document
**Feature:** AI Voice Chat for Task Management (Combined Version)
**Strategic Angle:** Dual-mode — Quick Voice + AI Chat
**Status:** Draft
**Author:** Product Team
**Last Updated:** 2026-03-11

---

# Problem Alignment

## Problem & Opportunity

### The Core Problem

Task capture fails at the moment ideas are born.

Knowledge workers — PMs, engineering managers, marketers — generate their best insights during the messiest moments: walking out of a meeting, commuting, mid-exercise, head-down in a design review. At these moments, the friction of opening an app, navigating to the right project, filling in a task form, and assigning it to the right person is insurmountable. The thought gets filed under "I'll remember later." It doesn't get remembered.

Our research makes this concrete:

- **45% of TaskFlow users report skipping task creation** because the process is too much effort in the moment
- **"I have my best ideas walking or driving. By the time I get to my desk, I've forgotten half."** — Designer, mid-market SaaS company
- **"I can articulate things way better when I'm talking than when I'm typing."** — PM, 120-person tech company

This is not a motivation problem. Users want to capture their work. The interface is the blocker.

### The Opportunity

**62% of TaskFlow users say they want voice input for task creation.** This is one of the highest expressed-demand signals we have seen in any research cycle. Note: this is stated preference data from surveys; behavioral validation is a pre-launch research priority (see Research section). Willingness to pay is equally strong: **81% would pay more for AI features**, with an average uplift tolerance of **$7/user/month**.

**Revenue projection:** At 850 accounts with an average team size of ~25 users, a conservative 20% conversion to an AI tier at $5/user/month uplift = **~$255K additional ARR** in the first two quarters post-launch. At 30% conversion, that reaches **~$383K**. This directly advances the Q1 goal of reaching $6M ARR (currently at $4.2M).

Beyond user demand, there is a strategic window. Asana launched AI features in November 2024, and Linear, Notion, and ClickUp are all adding AI capabilities. Most of these implementations are text-only and additive. More critically: **23% of TaskFlow's churned customers cited missing features as their primary reason for leaving** — and Asana's AI launch creates a direct retention and deal-loss risk that compounds every month we wait. TaskFlow has an opportunity to leapfrog on both offense (new AI positioning) and defense (churn mitigation).

The mobile experience compounds the opportunity. TaskFlow's mobile app is currently read-only and inadequate for creation workflows. A voice-native interface bypasses the need to rebuild a traditional mobile creation flow entirely — it makes mobile the best place to capture tasks.

### Why Now

Q1 is TaskFlow's AI launch window. Competitors are moving, churned customers are citing missing features, and the 23% churn-from-missing-features signal means delay has a measurable dollar cost. Every month without AI features is a month where Asana and ClickUp can use their AI launch as a wedge in competitive deals.

**Capacity trade-off:** This feature requires the Core Platform squad (~4 engineers) for 10–11 weeks, and the Mobile squad for the Quick Voice surface. The primary displacement is the enterprise readiness work (SSO, advanced permissions) also on the Q1 roadmap. Recommendation: timebox enterprise readiness to 3-week sprints in parallel with AI Chat build; SSO can ship in Q2 without competitive consequence. AI features cannot wait.

---

## High Level Approach

We will ship a **dual-mode AI voice feature** embedded natively in TaskFlow's mobile and web experiences. Rather than forcing users into a single AI interaction model, we offer two complementary modes:

**Mode 1 — Quick Voice:** Tap a microphone button, speak one task, done in under 5 seconds. Minimal UI, maximum speed. Built for users on the move. The AI parses speech into a structured task — title, assignee, due date, project — and creates it instantly.

**Mode 2 — AI Chat:** An ongoing conversational interface where users plan, organize, and think through multiple tasks at once. Users describe a situation ("We have a launch next week and I need to make sure nothing falls through the cracks"), and the AI helps decompose it into tasks, asks clarifying questions, and adds everything to the appropriate project.

Both modes co-exist. A manager doing sprint planning reaches for Chat. A PM on a commute reaches for Quick Voice. The same feature serves both without forcing a choice. The toggle between modes is a single tap.

**What alternatives did we consider?**

| Approach | Why Not Selected |
|---|---|
| Voice-only, no chat | Misses the high-value planning use case for power users |
| Chat-only, no quick voice | Fails the commute/hands-free capture use case entirely |
| List-first only (mic on task list) | Lower learning curve but doesn't serve deeper planning sessions |
| Full AI assistant (meeting transcription, multi-language, voice playback) | 6+ months, high risk, kills Q1 deadline |

We landed on the balanced dual-mode approach because user research reveals two distinct jobs-to-be-done — fast capture and conversational planning — both large and underserved. A feature that serves only one leaves users with a reason to still reach for a competitor.

---

### Narrative

**Scenario A — The PM on a commute (Quick Voice)**

Alicia is a Product Manager at a 120-person tech company. She's walking to a coffee meeting when three follow-ups hit her from yesterday's engineering sync. By the time she sits down, she'll have forgotten two of them.

With Quick Voice, she opens TaskFlow, taps the mic icon, and says: "Remind me to schedule the user research debrief with Marcus by Thursday." Task created. She does it twice more for the other two. She reaches her meeting with everything captured.

No typing. No app switching. No "I'll remember later."

**Scenario B — The EM doing sprint planning (AI Chat)**

Daniel is an Engineering Manager. It's Monday morning and he needs to set up the new sprint. He normally spends 30 minutes writing tasks manually from his notes.

He opens AI Chat and types: "We're starting a new sprint today. We need to finish the authentication flow, fix the 3 high-priority bugs from last sprint, do code review for the payments PR, and sync with design on the new onboarding flow before Wednesday."

The AI replies: "Got it — I created 5 tasks from that. Should I assign these to the same team members as last sprint?" Daniel confirms. Two minutes, sprint set up.

**Scenario C — The edge case (mode switching)**

Priya is an engineering manager walking out of a 45-minute design sync. She opens TaskFlow on her phone. She's mid-way through a Chat session planning next week's work — but she needs to capture two immediate tasks from the sync before she forgets them.

She taps the Quick Voice toggle without closing Chat, captures two fast tasks while walking to her car, and picks Chat back up where she left off. The session persisted. Nothing was lost.

This is the experience we are building.

---

## Goals

The following metrics define success for V1. All measured at 60 days post-launch across active users (logged in at least once in the trailing 30 days).

| Goal | Metric | Target | Why This Number |
|---|---|---|---|
| Adoption — Awareness | % of active users who try voice/chat feature | 20% within first 30 days | Conservative given behavior change required; tests discoverability |
| Adoption — Retention | % of tryers who use it weekly | 10% at 60 days | Weekly usage = habit signal, not novelty |
| Quality | Completion rate of voice-created tasks vs. typed tasks | Parity (within 5 percentage points) | If voice tasks are abandoned at higher rates, AI is capturing noise, not intent |
| Mobile Capture | % of new tasks created on mobile | +15pp from current baseline | Voice makes mobile creation viable for the first time |
| Revenue Signal | Conversion to AI add-on tier (if launched) | Establish baseline; target 15% of Pro accounts | Validates $7/user/month willingness-to-pay signal |

**Guardrail metrics (must not regress):**
- Task creation rate must not decrease
- New user time-to-first-task must not increase
- AI field extraction accuracy must reach ≥85% in beta before GA rollout
- AI latency: p95 < 2 seconds for Quick Voice (measured from end-of-speech detection to toast confirmation appearing), p95 < 3 seconds for Chat responses (measured from message send to AI reply visible)

---

## Non-goals

The following are explicitly out of scope for V1. Each is a deliberate decision, not an oversight.

| Non-goal | Rationale |
|---|---|
| Voice playback / text-to-speech responses | Adds complexity, accessibility edge cases, ambient environment problems; AI responds in text in V1 |
| Meeting transcription and automatic task extraction | Distinct product surface requiring integrations (Zoom, Meet, etc.); planned for V2 |
| Multi-language support | English-only in V1; internationalization requires significant LLM tuning and QA |
| Offline mode / local processing | Network dependency acceptable for V1; offline adds architectural complexity that delays launch |
| Custom voice commands or wake words | Users speak naturally; TaskFlow infers structure — no command grammar |
| Editing or updating existing tasks via voice | V1 is capture-only; modification flows are V2 |
| AI-generated task prioritization or triage | AI creates tasks from input but does not reorder or score the backlog in V1 |
| Integrations with external tools (Slack, email, calendar) | V1 is TaskFlow-native only |
| Voice-to-comment or voice-to-message | This PRD covers task creation only |

---

# Solution Alignment

## Key Features

### Plan of Record (V1)

**1. Quick Voice capture (P0)**
A persistent microphone button accessible from the TaskFlow home screen and task list on mobile and web. Tap to start, speak to capture. AI parses natural language into a structured task (title, project, assignee, due date, priority) and creates it in the correct location. Target: under 5 seconds for a simple task. A non-blocking toast confirmation appears after creation with a one-tap Edit option.

**2. AI Chat interface (P0)**
A dedicated chat panel (slide-up modal on mobile, side panel on web) where users have multi-turn conversations with the AI to plan and create multiple tasks at once. Maintains session state for 24 hours. Supports text and voice input within the same window.

**3. Mode toggle (P0)**
A single-tap toggle that switches between Quick Voice and AI Chat from within either interface. Switching modes does not disrupt an active Chat session — it is preserved and resumed when the user returns.

**4. Task confirmation and editing (P1)**
Quick Voice: non-blocking toast with "Edit" tap target. AI Chat: explicit confirmation step before any task creation — the AI surfaces all proposed tasks for review and the user approves (or edits) before anything is created.

**5. Context awareness (P1)**
The AI uses the project/board the user most recently viewed as the default context for task creation. "Most recently viewed" is stored as a per-user, per-device session value updated on every project navigation event. Cross-device sync is out of scope for V1 — if no context is available (new user, fresh install), the AI defaults to the user's personal inbox and notes the placement in the confirmation. Context can be overridden explicitly ("add this to the Engineering sprint instead").

**6. Disambiguation and clarification (P1)**
When the AI cannot confidently determine a field, it asks a focused clarifying question — one at a time, never an interrogation.

**7. Multi-task decomposition in Chat (P1)**
When a user describes a complex goal, the AI proposes a structured breakdown and presents all tasks for review before creating. Users can approve all, edit individual items, or remove tasks from the set.

**8. Delegation support (P1)**
Both Quick Voice and Chat explicitly support assigning tasks to others — this is a primary use case for managers, not just personal capture. "Assign the homepage copy review to Jordan by Friday" is a first-class interaction. Assignee resolution follows the same name-matching logic as personal tasks, with disambiguation when multiple workspace members share a name. Error recovery for wrong-assignee is elevated to blocking (not toast-only): if the AI assigns to a person who will receive a notification, the confirmation step must clearly surface the assignee name before creation.

**9. New user onboarding (P2)**
Users with fewer than 5 tasks created in TaskFlow are shown a guided first-use experience: a pre-filled example phrase and a brief walkthrough of the confirmation flow. This addresses the cold-start problem where the AI has little workspace context to draw on. New users also see a more conservative AI behavior: when project context is ambiguous, the AI always asks rather than inferring, until the user has established sufficient workspace history.

### Future Considerations (V2+)

- Voice input within the Chat panel (full hands-free Chat)
- Editing existing tasks via voice
- Meeting transcription to task generation
- Multi-language support
- Suggested tasks based on behavioral patterns
- Slack / calendar integration for richer Chat context

---

### Key Flows

**Flow 1: Quick Voice — New Task (Primary Mobile Flow)**

```
User opens TaskFlow mobile
→ Taps persistent mic icon in bottom nav
→ Full-screen listening UI appears; waveform animation plays
→ User speaks task naturally
→ Silence detected (1.5 sec threshold) OR user taps stop
→ Processing indicator (<2 seconds)
→ Non-blocking toast: "Follow up with design team — Fri — High | Edit?"
→ Task created in current project context
→ User returns to previous screen
```

Error states:
- Name not resolved → AI asks "Which Sarah — Chen or Williams?"
- Project ambiguous → "Q1 Roadmap or Stakeholder Comms?"
- No due date → Task created without due date; blank field is better than a wrong date
- Voice recognition fails → Text input fallback surfaces immediately

---

**Flow 2: AI Chat — Sprint Planning Session**

```
User taps Chat icon in bottom nav
→ Slide-up Chat panel opens
→ User types (or speaks): "Starting sprint 14. Need to finish auth flow,
   fix top 3 bugs, get payments PR reviewed before Wednesday."
→ AI proposes task list with assignments and due dates
→ AI: "Should I assign to same team as last sprint?"
→ User: "Yes, and add a design sync for onboarding — Tuesday."
→ AI confirms set of 6 tasks; asks user to approve
→ User taps "Create all"
→ Sprint set up. AI shows summary.
→ User dismisses Chat panel
```

---

**Flow 3: Mode Switch Mid-Session**

```
User is in active AI Chat session (mid-conversation)
→ User needs to capture one fast task
→ Taps "Quick Voice" toggle in Chat panel header
→ Quick Voice fullscreen opens; Chat session preserved in background
→ User speaks one task → Task created
→ User returned to Chat panel exactly where they left off
```

---

**Flow 4: Ambiguous Input**

```
User speaks: "Add a task for the thing Marcus and I discussed"
→ AI: "What's the task?" (one clarifying question)
→ User: "Send the Q1 roadmap draft to the exec team"
→ AI: "Which project — Q1 Roadmap or Stakeholder Comms?"
→ User: "Q1 Roadmap"
→ Task created; toast confirmation
```

---

### Key Logic

**Parsing and task creation rules:**

| Scenario | Behavior |
|---|---|
| User is inside a project when invoking the AI | Default project = current project (user can override) |
| Assignee not specified | Quick Voice: task created unassigned; Chat: AI asks |
| Due date not specified | Left blank — never defaulted to today |
| Multiple matches for a name | AI asks to disambiguate (one question per entity) |
| No project match found | Task goes to user's inbox; AI notes it |
| Priority not stated | Defaults to "None" unless high-signal words used ("urgent," "ASAP," "blocking") |

**Confidence thresholds:**
- **>90% match** — resolve silently; show in confirmation for review
- **50–90%** — include best guess with note ("Assuming Checkout Redesign — correct?")
- **<50%** — ask explicitly before generating confirmation

**Chat session rules:**
- Sessions persist 24 hours of inactivity; then cleared with user notification
- No tasks created in Chat without explicit user confirmation
- AI asks at most one clarifying question per turn
- If AI is uncertain about multiple fields, creates task with confident fields and flags uncertain ones

**Chat session storage architecture:**
- Sessions stored server-side, scoped per user (not per device)
- Storage: conversation turns stored as JSON in the existing TaskFlow database; estimated ~2–5KB per session
- Retention: sessions auto-deleted after 24 hours of inactivity; no long-term conversation history in V1
- At 850 accounts × average 25 users × 10% using Chat daily = ~2,125 active sessions/day; well within current DB capacity
- Engineering to confirm storage model before Chat build begins (Week 7)

**Mode toggle rules:**
- Switching to Quick Voice does not end Chat session
- Returning to Chat resumes the previous session
- Closing the app during a Chat session preserves it (within 24-hour window)

**Voice input processing:**
- Uses device native speech-to-text (iOS: SFSpeechRecognizer, Android: SpeechRecognizer, Web: Web Speech API)
- Transcription streamed in real-time to the UI
- Silence detection: 1.5 seconds triggers auto-submit
- Raw transcription shown before AI processing; user can edit text before submitting
- If voice recognition fails, text input fallback surfaces immediately — no dead-end error screen

**Privacy and data handling:**
- Voice audio processed on-device by OS speech-to-text; TaskFlow does not receive or store raw audio
- Text transcriptions and chat messages transmitted to TaskFlow's AI backend over HTTPS
- Workspace context scoped to user's accessible data only
- AI conversation content not used for model training without explicit opt-in (V1 default: opt-out)
- Audio discarded immediately after transcription — never stored

---

# Development and Launch Planning

## Key Milestones

| Milestone | Target Date | Owner |
|---|---|---|
| PRD finalized and approved | Week 1 | PM |
| Legal/privacy review of audio data policy | Week 2 | Legal + PM |
| Technical spec complete | Week 3 | Engineering Lead |
| Design: Quick Voice UI, Chat panel, mode toggle | Week 3–4 | Design |
| Quick Voice — internal build (iOS + Android) | Week 5–7 | Mobile Squad |
| AI Chat — internal build | Week 7–9 | Core Platform Squad |
| Mode toggle + full integration | Week 10 | Engineering |
| Internal QA + edge case testing | Week 10–11 | QA + PM |
| Closed beta (25–50 accounts) | Week 12–13 | PM + CS |
| Beta feedback synthesis + critical fixes | Week 13–14 | PM + Engineering |
| General availability launch | Week 15 | Full team |
| 30-day post-launch metrics review | Week 19 | PM |

## Operational Checklist

**Legal / Privacy:**
- [ ] Update privacy policy to reflect audio processing and data handling
- [ ] Confirm audio is not stored post-processing; legal review of AI provider data terms
- [ ] GDPR compliance review for EU customers
- [ ] Workspace member data (names, project names) sent to AI covered under existing DPA

**Engineering / Infrastructure:**
- [ ] Select voice-to-text provider (evaluate: Whisper API, Google Speech-to-Text, Deepgram)
- [ ] Select NLP field extraction model (evaluate: GPT-4o vs. Claude for structured entity extraction)
- [ ] Define latency SLOs: Quick Voice p95 <2s; Chat p95 <3s
- [ ] Instrument full voice funnel event tracking
- [ ] Build offline state detection and graceful degradation
- [ ] Define rollout flag for percentage-based rollout (start at 10%)

**Design:**
- [ ] Quick Voice: mic button, listening UI, waveform, toast confirmation
- [ ] Chat: panel, conversation thread, task confirmation cards, multi-task review
- [ ] Mode toggle UX
- [ ] Permission denied, offline, and error states

**Marketing / GTM:**
- [ ] Launch announcement email to all 850 accounts
- [ ] 30-second demo video of both Quick Voice and AI Chat
- [ ] Sales battlecard update: voice AI differentiator vs. Asana, Linear, ClickUp
- [ ] Pricing page update if gated to Pro/AI tier

**Customer Success:**
- [ ] Help center: Quick Voice setup, AI Chat walkthrough, permissions troubleshooting
- [ ] Support team training on common errors
- [ ] In-app feedback mechanism (thumbs up/down on task confirmations)

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| AI field extraction accuracy below 85% | Medium | High | Hard gate on beta → GA. Delay if not met. |
| Voice latency exceeds 2s on 4G | Medium | High | Test on real-world networks in beta; fallback to spinner; optimize API calls |
| Users don't discover Quick Voice | Medium | Medium | In-app tooltip on first login; onboarding prompt; email campaign |
| Mic permission denial creates friction | Medium | Medium | Just-in-time permission (only on first tap); clear value explanation before request |
| Chat creates unwanted tasks | Low | High | Mandatory confirmation before any task creation in Chat; no background auto-creation |
| Competitor ships similar feature before us | High | Medium | Stay on Q1 timeline; differentiate on dual-mode flexibility, not just feature presence |

---

## Open Questions

1. **Pricing — RESOLVED:** AI Voice Chat launches included in all paid plans (Starter, Pro, Enterprise) for V1. Rationale: maximizing adoption data is more valuable than early revenue signal; gating creates a two-tier team experience that fragments adoption and generates support noise. Advanced AI features (proactive suggestions, meeting transcription, cross-tool integrations) will be gated to a paid AI tier in V2. This recommendation is final — not a question for leadership to answer.

2. **STT provider — RESOLVED:** Recommended provider is **Deepgram** (lowest latency on mobile networks, streaming transcription support, competitive accuracy for task-management vocabulary). Whisper API as fallback for accuracy-critical edge cases. Web Speech API for browser desktop as a free-tier complement. Engineering to confirm during technical spec week (Week 3) — this decision must not slip.

3. **Chat session persistence:** V1 spec: 24-hour session persistence. Consider shortening or lengthening based on beta feedback.

4. **Proactive AI in Chat:** Should Chat suggest tasks based on patterns ("You usually create a retrospective task after sprints — want me to add one?"). Deferred to V2; high-value signal to watch for.

5. **Feedback loop:** Include thumbs up/down on AI-created tasks in V1 to collect training signal for future accuracy improvements.

---

## Appendix

**Key Research Sources:**
- TaskFlow Q4 2025 User Survey — Voice & AI Features
- Customer Interview Series: Mobile and On-the-Go Task Management (n=12)
- TaskFlow Support Ticket Analysis: Mobile Limitations
- Competitive Analysis: Asana AI (Nov 2024), ClickUp Brain, Notion AI, Linear AI

**Pre-launch research required:**
- Behavioral study: measure actual mobile task creation frequency and time-of-day patterns to validate the capture gap (survey data alone is insufficient)
- Usability test: error recovery flow with simulated 85% accuracy — observe how often users catch wrong fields in a non-blocking toast during motion-context tasks
- Concept test: AI Chat with 6–8 EMs and PMs to validate the conversational planning use case before committing Chat to V1 scope
- Delegation scenarios: test manager workflows where voice is used to assign tasks to others, not just capture personal tasks

**Changelog:**
- v0.1 — Initial draft (2026-03-11). Combined from v1 (goals), v2 (narrative), v3 (two-mode structure).
- v0.2 — (2026-03-11) Addressed engineering, executive, and UX research feedback: added revenue projection, resolved pricing and STT provider decisions, added capacity trade-off, clarified p95 latency definition, added delegation feature, new user onboarding, Chat session storage architecture, and pre-launch research requirements.

**FAQ:**

*Q: Why dual mode instead of one unified interface?*
A: User research shows two distinct jobs: fast capture (commute, hands-busy) and planning (sprint setup, project scoping). A single interface optimized for one fails the other. The toggle costs little in UX complexity; it serves the full use case.

*Q: Will voice-created tasks look different from typed tasks?*
A: No. Tasks created via voice are structurally identical. Internally they carry a source metadata flag for analytics only — never surfaced to users.

*Q: What happens if I speak in a language other than English?*
A: V1 is English-only. The app accepts the input but accuracy will be poor. Multi-language support is a planned V2 investment; documented in launch comms.

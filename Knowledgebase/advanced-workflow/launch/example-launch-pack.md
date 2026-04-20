# Example Launch Pack — Purple AI: Natural Language Threat Investigation
*A fully worked example. Use this as a reference when building your own launch pack with `launch-pack-template.md`.*

---

> **How to use this file:**
> This is a complete, filled-in launch pack for a real SentinelOne feature launch. Read through it to understand what each artifact looks like when done well, then use `launch-pack-template.md` + Claude to generate your own version in under an hour.
>
> **Feature used in this example:** Purple AI — Natural Language Threat Investigation
> A capability allowing SOC analysts to investigate threats by asking plain-English questions directly in the Singularity console, with automated investigation summaries generated at the end of each session.

---

## Readiness Check

**Feature name:** Purple AI — Natural Language Threat Investigation
**Launch date:** 2026-03-17
**Launch tier:** 🔴 Major
**PM owner:** [Your name]
**Eng lead:** [Eng lead name]
**PMM contact:** [PMM name]

### What shipped vs. what was planned

| PRD Goal | Shipped? | Notes |
|---|---|---|
| Natural language query interface in Singularity console | ✅ Yes | Full release — single and multi-turn queries |
| Automated investigation summary at session close | ✅ Yes | Generates plain-English summary + MITRE ATT&CK mapping |
| Cross-platform query (Endpoint + Data Lake) | ⚠️ Partial | Endpoint data only in v1; Data Lake integration deferred to Q2 |
| Suggested follow-up queries based on context | ❌ Deferred | Moved to v1.1 — requires additional model fine-tuning |
| Export investigation summary to PDF / Jira ticket | ✅ Yes | Export to PDF available; Jira integration live for Enterprise tier |

### Deferred scope
- **Data Lake cross-platform query** — deferred because the Data Lake connector required additional latency optimization that would have pushed launch past the quarter boundary. Targeted for Q2 (Sprint 47).
- **AI-suggested follow-up queries** — deferred because model accuracy in early testing was below our 90% relevance threshold. Targeted for v1.1 in Sprint 45.

### Launch blockers
- [x] Release notes written and reviewed
- [x] CS brief shared with CS team lead
- [x] Sales brief shared with PMM and SE lead
- [x] Executive announcement reviewed by GPM
- [x] Confluence page published
- [x] No unresolved P0/P1 bugs in shipped scope

---

## Artifact 1 — Release Notes

> **Where this goes:** Confluence (Product Updates space) + linked to Jira epic SPP-2841

### Purple AI: Natural Language Threat Investigation — Release Notes
**Version:** v24.1.3
**Release date:** 2026-03-17
**Platform area:** Purple AI / Singularity Console

#### What's new

| Capability | Description | Available to |
|---|---|---|
| Natural language query | Ask threat investigation questions in plain English directly in the Singularity console | Complete, Commercial, Enterprise |
| Multi-turn investigation | Follow up on previous queries in the same session — Purple AI maintains full context | Complete, Commercial, Enterprise |
| Automated investigation summary | At session close, Purple AI generates a structured summary including timeline, affected assets, MITRE ATT&CK mapping, and recommended actions | Complete, Commercial, Enterprise |
| PDF export | Export the investigation summary as a formatted PDF for ticketing, compliance, or post-incident review | Complete, Commercial, Enterprise |
| Jira ticket creation | Create a Jira incident ticket directly from an investigation summary with one click | Enterprise only |

#### How it works
Purple AI uses a fine-tuned large language model with access to Singularity Endpoint telemetry for the active tenant. Queries are translated into structured EDR queries at runtime, results are processed and summarized in natural language, and conversation context is maintained within a single investigation session. All query execution happens within the tenant's data boundary — no telemetry leaves the customer environment.

#### What changed in the UI
- New **"Ask Purple AI"** button in the top-right of the Singularity console (appears on Threat Center, Endpoint, and Alerts views)
- New **Investigation Session** panel — opens as a right-side drawer, collapsible
- **Session Summary** modal appears when closing an investigation session with 3+ queries
- **Export** button in the Session Summary modal (PDF download + Jira creation for Enterprise)
- Navigation: **Settings → Purple AI** — new admin panel for enabling/disabling Purple AI per role and configuring Jira integration

#### API / integration notes
- New endpoint: `POST /web/api/v2.1/purple-ai/query` — accepts natural language string, returns structured response with telemetry citations
- New endpoint: `GET /web/api/v2.1/purple-ai/sessions/{id}` — retrieve full session history and summary
- Jira integration requires Atlassian OAuth token configured in **Settings → Integrations → Jira** (existing integration — no new setup for tenants already connected)

#### Migration / enablement
Purple AI is **disabled by default** for all tenants. Tenant admins must enable it in **Settings → Purple AI → Enable for roles**. We recommend enabling for Tier 2 and Tier 3 analysts first, then expanding to Tier 1 based on team readiness. No data migration required.

#### Known limitations
- Data Lake cross-platform query (querying across Cloud and Identity telemetry from a single Purple AI session) is not available in v1 — targeted for Q2
- Maximum session length: 50 turns. Sessions exceeding this limit will be auto-summarized and closed
- Response latency averages 3–6 seconds per query for endpoint telemetry. Complex queries across large datasets (>10M events) may take up to 15 seconds
- AI-suggested follow-up queries not available in v1 — targeted for v1.1

---

## Artifact 2 — Sales Enablement Brief

> **Where this goes:** Shared sales folder + Highspot + SE Slack channel `#se-enablement`

### Purple AI: Natural Language Threat Investigation — Sales Enablement Brief

**What's new in one sentence:**
Purple AI now lets SOC analysts investigate threats in plain English — no query language, no tab switching, no 45-minute write-ups — and automatically produces a structured investigation summary at the end of every session.

**The customer problem we're solving:**
SOC analysts spend up to 40% of their investigation time not on analysis — but on mechanics: writing queries in proprietary languages, switching between five different consoles to gather context, and manually writing up findings afterward. The most experienced analysts lose hours a week to work that should be automated. Tier 1 analysts abandon investigations entirely because the friction is too high. The result is longer MTTR, more analyst burnout, and real threats that go unresolved.

**What they can do now:**
- Ask threat investigation questions in plain English ("Show me all lateral movement from this endpoint in the last 48 hours") and get an instant, cited answer
- Run an entire investigation without leaving the Singularity console
- Close every session with an auto-generated summary — timeline, affected assets, MITRE ATT&CK mapping, recommended next actions — in seconds instead of 45 minutes
- Export investigation summaries directly to PDF or create Jira tickets with one click (Enterprise)

**Who to lead with:**

| Persona | Why they care | Opening line |
|---|---|---|
| CISO / VP Security | MTTR reduction, analyst retention, compliance documentation | "Your analysts are spending 40% of their investigation time on mechanics. Purple AI gives that time back — and produces audit-ready documentation automatically." |
| SOC Analyst / Threat Hunter | Eliminates query language friction, stops tab switching, removes write-up overhead | "What if you could just ask the platform what happened — and it told you, in plain English, with full context?" |
| IT / Security Engineering | Fast rollout, no new infrastructure, admin controls per role | "It's disabled by default, admin-controlled per role, and runs entirely within your data boundary. Rollout takes 15 minutes." |
| MSSP / MDR Operator | Faster analyst onboarding, consistent investigation quality across tenants | "Your Tier 1 analysts can investigate like Tier 3. Consistent output, faster resolution, lower training overhead." |

**Competitive angle:**

| Competitor | Their approach | Our advantage |
|---|---|---|
| CrowdStrike (Charlotte AI) | AI assistant primarily for alert triage and report generation — limited investigation depth | Purple AI maintains full investigation context across multi-turn queries and generates a structured summary tied to actual telemetry, not just AI-generated text |
| Microsoft Defender (Copilot for Security) | Broad security copilot across the Microsoft stack — generalist, not investigation-native | Purple AI is purpose-built for investigation workflows inside the SOC console analysts already live in. No context switching to a separate AI tool. |
| Palo Alto (XSIAM AI) | AI-driven alert correlation and automated triage | Purple AI extends to natural language investigation, not just triage — analysts can explore beyond the automated findings |

**Objections and responses:**

*"We already have Charlotte AI / Copilot for Security..."*
> Charlotte AI helps analysts triage alerts and generate reports. Purple AI lets them investigate — ask follow-up questions, explore lateral movement, query endpoint telemetry in natural language across a live investigation session. They're different workflows. Ask your customer how long their analysts spend writing investigation summaries — that's the gap Purple AI closes.

*"How is this different from Storyline?"*
> Storyline automatically correlates and visualizes attack timelines. Purple AI lets analysts ask questions about what Storyline shows them — going deeper into any event, any asset, any timeframe, in plain English. They work together.

*"Is this included in our current tier or is it an add-on?"*
> Available on Complete, Commercial, and Enterprise at no additional charge. Jira ticket creation from investigation summaries is Enterprise-only. Confirm current tier with your AE before the conversation.

*"We're worried about our data leaving our environment."*
> All query execution happens within the tenant's data boundary. No telemetry is sent to external model providers. The AI runs on SentinelOne infrastructure with the customer's data — point your SE at the API notes in the release documentation.

**Demo path:**
1. Open Threat Center in Singularity — click **"Ask Purple AI"** in the top right
2. Type: *"Show me all process executions from endpoints with critical severity alerts in the last 24 hours"* — walk through the results and cite the telemetry source
3. Follow up: *"Which of these show signs of lateral movement?"* — demonstrate multi-turn context
4. Close the session and show the auto-generated summary — highlight the MITRE ATT&CK mapping and the PDF export

---

## Artifact 3 — CS & Support Brief

> **Where this goes:** CS Confluence space (`CS Hub → Product Updates`) + `#cs-product-updates` Slack channel

### Purple AI: Natural Language Threat Investigation — CS & Support Brief

**What shipped:**
Purple AI now supports natural language threat investigation in the Singularity console. Analysts can ask plain-English questions about threats, follow up within the same session, and receive an automatically generated investigation summary — including a timeline, affected assets, MITRE ATT&CK mapping, and recommended actions — when they close the session. Investigation summaries can be exported as PDF or pushed to Jira (Enterprise).

**Which customers have access:**
All tenants on Complete, Commercial, and Enterprise tiers. The feature is **disabled by default** — tenant admins must enable it in **Settings → Purple AI**. Jira ticket creation from summaries is Enterprise only. Not available on Core or Control.

**How customers will find it:**
Once enabled by an admin, a purple **"Ask Purple AI"** button appears in the top-right of the console on Threat Center, Endpoint, and Alerts views. Customers will also see an in-app tooltip the first time they visit Threat Center after enablement.

**Top questions customers will ask:**

*Q: I don't see the Purple AI button — where is it?*
A: The feature must be enabled by a tenant admin in **Settings → Purple AI → Enable for roles**. If they've enabled it and still don't see the button, confirm their console version is v24.1.3 or later and ask them to hard-refresh the browser. Escalate to Support if the issue persists after a cache clear.

*Q: Is my data leaving my environment when I use Purple AI?*
A: No. All query execution happens within the tenant's data boundary. No telemetry is sent to external model providers. Queries run against the customer's own Singularity telemetry on SentinelOne infrastructure. This is a common question from security-conscious customers — it's safe to answer directly and confidently.

*Q: Can Purple AI query data from Cloud or Identity, or only Endpoint?*
A: Version 1 supports Endpoint telemetry only. Cross-platform queries (Cloud, Identity, and Data Lake) are on the roadmap and targeted for Q2. If a customer is specifically waiting for this, note their interest and flag to the PM team — we are tracking demand.

*Q: The AI gave me an incorrect or incomplete answer. What do we do?*
A: In-session, the customer can refine their question and Purple AI will re-query. If they believe the answer is factually wrong (e.g., wrong endpoint, incorrect timeline), they should click **"Report inaccurate result"** in the session panel — this feeds directly to our AI quality team. For escalations, use `#purple-ai-support` in Slack or open a P2 ticket in Jira under project PPL.

*Q: How long are investigation sessions and summaries retained?*
A: Session history is retained for 90 days by default. Exported PDFs are stored locally by the customer — we don't host them. Jira tickets are in the customer's own Jira instance.

*Q: Is this replacing any existing feature?*
A: No. Purple AI investigation is additive — it doesn't replace or deprecate any existing console capabilities, Storyline, or existing alert workflows.

**Escalation path:**
- Slack: `#purple-ai-support` — PM and eng team monitor this channel
- Jira: Project `PPL`, component `Natural Language Investigation`
- For P0 issues (feature unavailable for a customer): page the on-call via PagerDuty → product-purple-ai

**Known issues to communicate proactively:**
- Response latency for complex queries against large datasets can be 10–15 seconds. If a customer reports "it seems slow," this is expected behavior for large tenants — not a bug.
- The 50-turn session limit may surprise heavy users. Sessions are auto-summarized and closed at this limit. Customers should start a new session for a new investigation.

---

## Artifact 4 — Executive Announcement

> **Where this goes:** Direct Slack DM or email to your GPM / VP Product

### Purple AI: Natural Language Threat Investigation — Shipped ✅

**What we shipped:**
Purple AI Natural Language Threat Investigation is live as of March 17. SOC analysts can now investigate threats by asking plain-English questions in the Singularity console and receive an automated structured summary — including MITRE ATT&CK mapping and recommended actions — at the end of every session.

**Why it matters:**

- **Directly addresses our #1 competitive gap against CrowdStrike.** Charlotte AI came up as the primary technical objection in 12 of our Q4 enterprise losses. We now have a differentiated, investigation-native response. This ship strengthens the pipeline at an estimated $4.2M in at-risk deals cited by field.
- **Targets a measurable source of trial churn.** 34% of trials that churned in H2 2025 cited "investigation workflow friction" as a primary reason. Automated investigation summaries remove the 45-minute manual write-up that was the most common complaint in exit interviews.
- **Accelerates Purple AI ARR contribution.** Purple AI upsell is a FY26 priority. Natural language investigation is the workflow that converts Complete-tier customers to Enterprise — our data shows Enterprise attach rate is 2.4x higher when Purple AI is the primary reason for upgrade.

**What was deferred and why:**
Data Lake cross-platform query (querying Cloud + Identity telemetry from one Purple AI session) was moved to Q2. This was a deliberate trade-off: shipping Endpoint-only on time versus slipping the quarter to get full cross-platform. Customer feedback validated Endpoint as the highest-value starting point.

**Success metrics we're watching:**

| Metric | Baseline | Target (60 days) | How we'll measure |
|---|---|---|---|
| Purple AI weekly active users | 1,200 (query interface only) | 4,500 | Singularity telemetry / Amplitude |
| Investigation summary export rate | N/A (new) | 35% of sessions | Amplitude — session close events |
| Mean time to investigation close | 68 min (manual) | 35 min | Amplitude — session duration |
| Trial-to-paid conversion in Complete tier | 22% | 27% | Salesforce / RevOps |

**What's next:**
Sprint 45 (March 31): v1.1 ships AI-suggested follow-up queries. Sprint 47 (April 28): Data Lake cross-platform query integration.

---

## Artifact 5 — Customer-Facing Announcement

> **Where this goes:** Handed to PMM for product changelog + release email to active customers

### Investigate threats by asking questions — Purple AI now speaks your language

**The short version:**
You can now investigate threats in the Singularity console by asking plain-English questions — and Purple AI will automatically summarize everything when you're done.

**What this means for your team:**
Your analysts no longer need to write complex queries or switch between tools to understand a threat. Ask Purple AI what happened, follow up as you dig deeper, and close the session with a complete investigation summary — timeline, affected assets, MITRE ATT&CK mapping, and recommended actions — automatically generated and ready to export or push to Jira.

We built this because investigation write-ups were costing your analysts up to 45 minutes per session. Now it takes seconds.

**How to get started:**
1. Ask your Singularity admin to enable Purple AI in **Settings → Purple AI → Enable for roles**
2. Open Threat Center and click **"Ask Purple AI"** in the top right
3. Type your first question — try *"Show me all suspicious process executions in the last 24 hours"*

**Available on:** Complete, Commercial, and Enterprise plans
**Jira integration (one-click ticket creation from summaries):** Enterprise plans

**Learn more:** [link to help documentation] · [link to 3-minute demo video]

---

## Artifact 6 — Internal Slack Announcement

> **Where this goes:** `#product-announcements` and your squad channel

🟣 **Purple AI Natural Language Investigation is live.**

SOC analysts can now investigate threats by asking plain-English questions directly in the Singularity console — no query language, no tab switching — and get an automatically generated investigation summary when they close the session. This one closes our biggest competitive gap against Charlotte AI and directly targets the investigation workflow friction that showed up in 34% of our H2 trial exits. Massive work from the Purple AI squad. Full details in Confluence: [link] — sales brief and CS brief are in the shared folder and ready to go.

---

## Launch Checklist — Completed ✅

**Content**
- [x] Release notes are accurate — scope matches what actually shipped
- [x] Deferred items (Data Lake query, suggested follow-ups) documented — not mentioned in customer artifacts
- [x] Metrics in exec announcement trace back to PRD goals
- [x] CS brief addresses the 5 most predictable customer questions
- [x] Sales brief has concrete competitive angles for CrowdStrike and Microsoft
- [x] Customer announcement has no internal jargon

**Review**
- [x] Exec announcement reviewed by GPM
- [x] CS brief approved by CS team lead (Sarah M.)
- [x] Sales brief reviewed by SE lead and PMM

**Distribution**
- [x] Release notes published to Confluence — Product Updates space
- [x] Release notes linked to Jira epic SPP-2841
- [x] Sales brief added to Highspot → Product Launches → FY26 Q1
- [x] CS brief posted to CS Hub Confluence + `#cs-product-updates`
- [x] Slack announcement posted to `#product-announcements`
- [x] Epic SPP-2841 marked as Done

---

## 48-Hour Signal Check (template — run post-launch)

```
It's been 48 hours since we launched Purple AI Natural Language Investigation.

Help me run a signal check:
1. Review the success metrics from the executive announcement above
2. Review these early signals: @[slack-mentions.md or support-ticket-summary.md]
3. What green flags should we capture and share with the team?
4. What red flags need immediate attention?
5. What should we bring into the Sprint 44 retrospective?
```

---

*This is a worked example — adapt it for your feature using `launch-pack-template.md`.*
*Part of the [Launch Workflow](launch-workflow.md) · [Product Management Lifecycle](../README.md)*

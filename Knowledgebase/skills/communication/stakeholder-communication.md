# Skill: Stakeholder Communication

Claude can help you write the communications that PMs spend the most time agonizing over — leadership updates, difficult-news messages, cross-functional announcements, and board materials. This skill focuses on drafting: getting the right content, structure, and framing into a document you can then refine.

## What this covers

This skill walks through four communication scenarios:

1. **Executive update drafting** — weekly or monthly status updates for leadership
2. **Bad-news framing** — delays, descopes, missed targets, framed honestly but constructively
3. **Cross-functional announcements** — product changes that affect engineering, sales, CS, or marketing
4. **Board prep** — quarterly board materials and investor updates

You can use any scenario standalone, or chain several together when preparing for a big review cycle.

---

## Executive update drafting

Use this when you need to write a weekly or monthly status update for your VP, CPO, or leadership team. Reference your sprint notes, metrics, or planning docs so Claude has the raw material.

```
Draft a weekly executive update for my VP of Product.
Here are this week's sprint notes: @sprint-notes.md
And the current metrics dashboard: @metrics-q1.md

Focus on what shipped, what's at risk, and what decision I need from leadership.
Keep it to five bullets max — she skims these on Monday morning.
```

If you have a recurring format, tell Claude to follow it:

```
Draft this week's leadership update using the same format as last week: @last-week-update.md
Here's what changed this week: @sprint-notes.md
Highlight anything that shifted from last week's update.
```

---

## Bad-news framing

Use this when you need to communicate a delay, descope, missed target, or other setback. The goal is honest, constructive framing — not spin.

```
I need to communicate a two-week delay on the integrations launch.
Here's the context: @integrations-status.md

Draft a message to my VP of Product that:
- States the delay clearly upfront
- Explains the root cause without blame
- Shows what we're doing to mitigate
- Resets the timeline with confidence
- Asks for any decision if needed

Tone: direct and accountable, not defensive.
```

For a descope or target miss:

```
We're going to miss our Q1 activation target by ~15%.
Here's the data: @q1-activation-metrics.md
And the contributing factors: @q1-retro-notes.md

Draft a message to the leadership team that frames this honestly.
Include what we learned, what we're adjusting for Q2, and what support we need.
Don't minimize the miss — but connect it to a clear path forward.
```

---

## Cross-functional announcements

Use this when a product change affects other teams — engineering, sales, CS, marketing — and each audience needs different context.

```
We're changing the onboarding flow starting next sprint.
Here's the spec: @onboarding-v2-spec.md

Draft three versions of an announcement:
1. Engineering — what's changing technically and what they need to do
2. Sales — how to talk about this with prospects, what's better for them
3. CS — what existing customers will see, expected support questions

Each should be 3-5 paragraphs max. Use the same facts but adjust framing for each audience.
```

For a single cross-functional message:

```
Draft an announcement to the broader product + engineering org about our new API rate-limiting policy.
Here's the technical decision doc: @rate-limiting-decision.md

The audience is mixed technical and non-technical. Lead with the "what and why" before the details.
```

---

## Board prep

Use this when preparing quarterly board materials or investor updates. Claude can help structure the narrative, draft individual slides, or produce a full board memo.

```
I need to prepare materials for our quarterly board meeting.
Here's the context:
- Quarterly metrics: @q1-metrics.md
- Product roadmap update: @roadmap-q2.md
- Key wins and challenges: @q1-retro-notes.md
- Competitive landscape: @competitive-update.md

Draft a board memo that covers:
1. Executive summary (1 paragraph)
2. Key metrics and trends (table + commentary)
3. Product progress and roadmap outlook
4. Risks and mitigations
5. Strategic questions for the board

Write for a board audience: concise, numbers-forward, focused on trajectory and decisions.
```

For an investor update email:

```
Draft a quarterly investor update email.
Here's our performance data: @q1-metrics.md
And the product highlights: @q1-shipped.md

Tone: confident but transparent. Lead with momentum, acknowledge headwinds honestly, close with what's ahead.
Keep it under 500 words — investors skim these.
```

---

## Draft -> Review Pipeline

This skill is designed to pair with the `executive` agent. The workflow:

1. **Draft with this skill** — use the prompts above to generate a first draft with the right content and structure.
2. **Review with the executive agent** — hand the draft to the `executive` agent for a tone, framing, and completeness check.

In practice, this looks like:

```
@skills/stakeholder-communication
Draft a leadership update for my VP using these sprint notes: @sprint-notes.md
```

Then, once you have the draft:

```
Use agent:executive
Review this draft leadership update: @leadership-update-draft.md
Check the tone, framing, and completeness. Flag anything that's missing or would land poorly with a VP audience.
```

The skill creates the content. The agent pressure-tests whether it's ready to send. Use both for anything high-stakes.

---

## Tips

**Tell Claude who's reading it.** "My VP" vs "the full leadership team" vs "the board" vs "a cross-functional Slack channel" will change the tone, depth, and structure significantly.

**Tell Claude what you want to happen.** "I need approval to extend the timeline" vs "I just need to keep them informed" vs "I need them to reallocate resources" produces very different drafts.

**Include the raw material.** The more context you give — sprint notes, metrics, retro docs, decision logs — the less Claude has to guess. Reference files with `@` rather than pasting inline.

**Don't skip the review step.** For anything going to leadership or the board, run the draft through the `executive` agent before sending. A five-minute review pass catches framing issues you'll miss after staring at the content too long.

**Save your best outputs as templates.** When a draft lands well, save it and reference it in future prompts:

```
Draft this week's update using the same format and tone as @last-good-update.md
Here's this week's material: @sprint-notes.md
```

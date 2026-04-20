# Story Breakdown Workflow with Claude Code
*A repeatable AI-assisted process for turning a finalized PRD into a complete, pushed engineering backlog*

---

## The Core Principle

A story breakdown is a contract between PM and engineering.

Every epic defines a deliverable. Every story defines a unit of work that can be built, tested, and shipped independently. Every acceptance criterion is something a QA engineer can verify without asking the PM a question.

If your stories need clarification after the breakdown, the breakdown wasn't done right. This workflow makes that the exception, not the rule.

---

## What You Need Before You Start

| Input | Required? | Notes |
|---|---|---|
| Finalized PRD | ✅ Required | The source of truth for every ticket. Use the output from `../prd-creation/`. |
| Jira project key OR GitHub repo | ✅ Required | Where tickets will be created (e.g. `WF` for Jira, `org/repo` for GitHub) |
| Jira MCP or GitHub MCP / `gh` CLI | ✅ Required | How Claude pushes tickets |
| OKR file | Optional | Used to label stories with OKR alignment |
| Engineering capacity context | Optional | Helps calibrate sprint scope in Phase 3 |

> **Tip:** Never run this workflow on a draft PRD. A breakdown from an uncertain spec creates uncertain tickets — and engineering debt starts before a line of code is written. Use `../prd-creation/` first.

---

## The Workflow (5 Phases)

---

### Phase 1 — Parse & Propose Epic Structure (10–15 min)

**What you're doing:** Reading the PRD and proposing how to slice it into epics before decomposing into stories.

Getting the epic structure right matters more than the stories themselves. Epics represent deliverable chunks your team can plan around. Too few epics means one giant milestone nobody can track. Too many fragments the work into noise.

**Opening prompt:**
```
I have a finalized PRD and want to break it into a complete engineering backlog.

Input files:
- PRD: @[your-feature-prd-final.md]
- Destination: [Jira / GitHub]
- Project key / Repo: [e.g. WF / org/repo-name]

Please do the following:
1. Read the PRD and identify the major deliverable areas
2. Propose an epic structure (3–6 epics) with a one-line scope for each
3. Identify anything in the PRD that is explicitly out of scope for V1
4. Flag any areas of the PRD that are ambiguous and need a decision before breakdown
5. Do NOT create any tickets yet — confirm the epic structure with me first
```

**What Claude will produce:**
- A proposed list of 3–6 epics with names and one-line scope
- Out-of-scope list extracted from the PRD
- Ambiguity flags that need your input before proceeding

**Your job in this phase:**
- Approve, rename, merge, or split epics
- Resolve flagged ambiguities (or explicitly defer them and note it in scope)
- Confirm out-of-scope items match your intent

> **Epic sizing guidance:** Each epic should represent 1–3 sprints of work for one squad. If an epic feels like it could take a quarter, split it. If it feels like 2 days, merge it.

---

### Phase 2 — Decompose into User Stories (15–20 min)

**What you're doing:** Breaking each confirmed epic into individual user stories with full acceptance criteria.

Work one epic at a time. This keeps context clean and lets you validate each epic's breakdown before moving to the next.

**Prompt per epic:**
```
Now break down Epic [N]: [Epic Name] into user stories.

For each story, use this format:
- Title: As a [persona], I want to [action] so that [outcome]
- Description: 2–3 sentences of context and edge cases
- Acceptance Criteria: bullet list, each item independently verifiable
- Story Type: [Feature / Bug / Tech Debt / Spike]
- Labels: [frontend / backend / API / data / infra / design — pick all that apply]
- Dependencies: [other story titles this story blocks or is blocked by, or "None"]

Use the personas defined in @[your-prd-final.md].
Do not add stories for anything outside the PRD scope.
Aim for 4–8 stories per epic. If you need more than 8, flag it — the epic may need splitting.
```

**What Claude will produce for each story:**
- User story title in the "As a / I want / So that" format
- Contextual description
- 3–5 concrete, verifiable acceptance criteria
- Story type, labels, and dependencies

**Repeat for each epic.** After each epic's stories are produced, confirm before moving to the next one.

**What to watch for:**
- Stories that have more than 5 acceptance criteria — these are usually two stories masquerading as one
- Acceptance criteria that say "works correctly" or "performs well" — push for specifics
- Dependencies that create a chain where nothing can ship until everything ships — flag and discuss with engineering

---

### Phase 3 — Estimate & Sequence (10 min)

**What you're doing:** Adding story points and sequencing stories into a logical build order.

Story points are estimates, not commitments. The goal is relative sizing (is this bigger or smaller than that?) — not precise hour counts.

**Prompt:**
```
Now estimate story points for all stories using Fibonacci sizing:
1 = trivial (< half a day), 2 = small (1 day), 3 = medium (2–3 days),
5 = large (1 week), 8 = extra large (flag for splitting)

For each story, provide:
1. Story points
2. Suggested build order within the epic (which stories must be done before others)
3. Any stories you'd flag for splitting (8+ points)
4. A total point estimate per epic and overall

If I provided engineering capacity context: @[capacity-notes.md]
— suggest which epic could be a first sprint vs. future sprints.
```

**What Claude will produce:**
- Point estimates per story
- Build order within each epic (sequenced list)
- Split flags for oversized stories
- Total estimate per epic and overall rollup
- Optional: sprint suggestion if capacity context was provided

**What to do with 8-point stories:**
```
Split [story title] into smaller stories. Suggested approach: [your idea, or ask Claude].
```

---

### Phase 4 — Review Gate (5–10 min)

**What you're doing:** A quality check before any ticket is created.

This is the step most PMs skip — and it's the step that prevents engineers from getting tickets that generate Slack threads.

**Prompt:**
```
Before we push anything, review the full breakdown and check:

1. Coverage — does every PRD requirement map to at least one story?
   List any PRD sections with no matching story.

2. Acceptance criteria quality — flag any AC that:
   - Is not independently verifiable
   - Uses vague language ("works properly", "is fast", "looks good")
   - Describes implementation rather than behavior

3. Dependency risks — are there any dependency chains that would block
   an entire epic from shipping if one story slips?

4. Missing stories — are there any obvious supporting stories not in the PRD
   that engineering will need? (e.g. logging, error states, empty states, analytics events)

5. Out-of-scope drift — did any story description creep beyond the PRD's V1 scope?

Produce a review summary. Flag issues as: [Fix before pushing] or [Nice to have].
```

**Fix "Fix before pushing" issues before proceeding.**

For "Nice to have" issues: your call. Either add them as explicitly-labeled stories or document them as known gaps.

---

### Phase 5 — Push to Jira or GitHub (10–15 min)

**What you're doing:** Creating all epics and stories in your destination system in one session.

**For Jira:**
```
Create the following in Jira project [PROJECT-KEY]:

1. Create one Epic for each of these [N] epics: [list epic names]
2. For each epic, create all its stories as child issues
3. Set labels, story points (use Story Points field), and issue type correctly:
   - Epics → type: Epic
   - Stories → type: Story
   - Spikes → type: Task
4. Link dependent stories using "is blocked by" / "blocks" issue links
5. Add the PRD link (@[your-prd-final.md] filename or URL) to each Epic's description
6. Confirm all tickets created with their Jira issue keys

Use @story-breakdown-template.md as the source of truth for all content.
```

**For GitHub:**
```
Create the following in [org/repo]:

1. Create one Milestone for each of the [N] epics
2. For each milestone, create all its stories as Issues
3. Apply labels to each issue (create labels if they don't exist):
   frontend, backend, API, data, infra, design
4. Add story type labels: feature, bug, tech-debt, spike
5. Set the milestone on each issue
6. Link dependencies in issue descriptions as "Blocked by #[issue-number]"
7. Add the PRD link to each milestone description
8. Confirm all issues created with their issue numbers

Use @story-breakdown-template.md as the source of truth for all content.
```

**After pushing, verify:**
```
List all the issues/tickets you just created with their IDs.
Are there any that failed to create? If so, retry those now.
```

---

## File Naming Convention

| File | Purpose |
|---|---|
| `[feature]-story-breakdown.md` | Full breakdown output — epics, stories, ACs, estimates |
| `[feature]-epic-[n].md` | Individual epic file if you want to push epics separately |

---

## Common Mistakes

**Pushing before the PRD is finalized.**
Stories written from a draft PRD will need rework when the PRD changes. Always finalize the PRD first. An hour saved in writing stories before the PRD is locked costs three hours of ticket cleanup.

**Skipping the review gate.**
The three most common things the review gate catches: (1) PRD requirements with no ticket, (2) acceptance criteria that say "the feature works", (3) missing empty states and error handling. These are cheap to fix before pushing and expensive to discover mid-sprint.

**One epic for the whole feature.**
If everything is in one epic, sprint planning becomes "are we done yet?" every two weeks. Aim for epics that can ship and deliver value independently — even if they're not the full feature.

**Stories written for the PM, not the engineer.**
Acceptance criteria like "the UI looks polished" or "users can do X easily" are not verifiable. Rewrite as: "The modal renders within 200ms on a cold load" or "User can complete X in 3 clicks from the dashboard."

**Forgetting non-feature stories.**
Every feature needs supporting stories: analytics event tracking, empty states, error handling, loading states, logging, and sometimes a rollout/flag story. The review gate will catch these — but it's faster if you think about them in Phase 2.

---

## Time Estimate

| Phase | Time |
|---|---|
| Phase 1 — Parse & propose epic structure | 10–15 min |
| Phase 2 — Story decomposition | 15–20 min |
| Phase 3 — Estimate & sequence | 10 min |
| Phase 4 — Review gate | 5–10 min |
| Phase 5 — Push to Jira / GitHub | 10–15 min |
| **Total** | **~50–70 min for a complete pushed backlog** |

---

## What's Next

Once the backlog is in Jira or GitHub, your engineering team can run sprint planning against real tickets.

After the feature ships, use `../launch/` to generate launch artifacts — the epic structure you created here maps directly to the release notes and the readiness check.

---

*Last updated: April 2026 · Part of the Product Management Lifecycle*

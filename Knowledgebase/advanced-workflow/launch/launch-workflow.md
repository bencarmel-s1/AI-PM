# Launch Workflow with Claude Code
*A repeatable AI-assisted process for getting a shipped feature to every audience that needs to know*

---

## The Core Principle

Shipping is not launching.

A feature is shipped when engineering merges the code. It's launched when sales can pitch it, CS can support it, leadership can report on it, and customers can discover it. The gap between those two moments is where momentum dies.

This workflow closes that gap — one Claude session, all the artifacts, under an hour.

---

## What You Need Before You Start

| Input | Required? | What to Use |
|---|---|---|
| Your PRD | ✅ Required | The original spec — Claude compares what shipped against what was planned |
| Sprint notes or Jira export | ✅ Required | Raw list of what actually shipped (tickets closed, scope changes, deferrals) |
| Company context | ✅ Required | `@company-context-sentinelone.md` |
| Release notes from eng | Optional | If your eng team already wrote a technical changelog, bring it in |
| User research | Optional | For the customer-facing announcement — what pain point does this solve? |

> **Tip:** The most common mistake is starting without the PRD. Without it, Claude can't tell the story of *why* something was built — and that's the core of every audience artifact.

---

## The 5-Phase Workflow

---

### Phase 1 — Readiness Check (10–15 min)

**What you're doing:** Establishing what actually shipped before writing anything.

This step catches scope changes that nobody documented. Things get deferred. Bugs don't get fixed before launch. The PRD said X but the sprint shipped 80% of X. The readiness check surfaces this so your launch comms are accurate.

**Opening prompt:**
```
I need to prepare a launch pack for a feature we just shipped.

Input files:
- PRD: @[your-feature-prd-final.md]
- What shipped: @[jira-export.md or sprint-review-notes.md]
- Context: @company-context-sentinelone.md

Please do the following:
1. Compare what was planned in the PRD against what actually shipped
2. List any scope that was deferred or changed
3. Assess the launch tier (Major / Minor / Patch) based on what shipped
4. Confirm the primary audience for each artifact
5. Flag anything that would block launch (missing docs, unresolved bugs, unclear owner)
```

**Output:** A readiness summary — what shipped, what was deferred, whether you're ready to proceed.

**If things were deferred:** Document them explicitly in the launch pack. Nothing erodes trust faster than a sales rep pitching a feature that isn't available yet.

---

### Phase 2 — Generate the Launch Pack (20–30 min)

**What you're doing:** Generating all audience artifacts from a single prompt in one session.

This is the core of the workflow. Claude knows the full context from Phase 1 — you're not re-explaining anything.

**Master prompt (Major launch):**
```
Now generate the full launch pack using @launch-pack-template.md.

Produce all 6 artifacts:
1. Release notes (technical changelog)
2. Sales enablement brief (1-page)
3. CS and support brief
4. Executive announcement
5. Customer-facing announcement
6. Internal Slack announcement

For each artifact, use the audience context from @company-context-sentinelone.md.
Tone guide:
- Release notes: precise and technical
- Sales brief: confident, outcome-focused, competitive
- CS brief: practical, question-and-answer format
- Executive: business impact, strategic framing, metrics-forward
- Customer: clear benefit, no jargon, what can they do now
- Slack: human, celebratory, one paragraph
```

**For a Minor launch (3 artifacts):**
```
Generate a Minor launch pack using @launch-pack-template.md.
Produce: release notes, sales/CS brief (combined), and Slack announcement.
```

**Output:** All artifacts in a single session. You'll refine each one before distribution, but the first pass takes minutes.

---

### Phase 3 — Review Gate (10 min)

**What you're doing:** A quick quality check before anything leaves your draft folder.

Before you distribute, run two checks:

**Check 1 — Launch Checklist**
```
Review the launch pack we just created against the launch checklist.
Flag anything that's missing, inconsistent, or risks causing confusion.
```

**Check 2 — Executive Review (for Major launches)**
```
Use @skills/reviewer-guides/executive.md to review the executive announcement.
Is the business case clear? Would a VP of Product push back on anything?
```

**What to watch for:**
- Claims in the customer announcement that aren't in the release notes
- Missing metrics or goals in the executive announcement (should trace back to PRD goals)
- CS brief that doesn't address the most obvious support question customers will ask
- Sales brief that doesn't have a clear competitive angle against CrowdStrike or Microsoft

---

### Phase 4 — Distribute (10–15 min)

**What you're doing:** Getting the right artifact to the right person, in the right place.

| Artifact | Where it goes | Who sends it |
|---|---|---|
| Release notes | Confluence (Product Updates space) + Jira (linked to epic) | PM |
| Sales enablement brief | Shared to Highspot / Google Drive sales folder | PM + PMM |
| CS brief | Shared to CS Confluence space + mentioned in CS Slack channel | PM |
| Executive announcement | Sent to your VP/GPM via email or Slack DM | PM |
| Customer announcement | Handed to PMM for changelog/release email | PM + PMM |
| Slack announcement | Posted to `#product-announcements` or squad channel | PM |

**Prompt for formatting each artifact for its destination:**
```
Format the executive announcement as a clean email draft to my VP.
Subject line: [Product Area] — [Feature Name] shipped: [one-line impact]
```

```
Format the release notes as a Confluence page (use headers and a table for the feature list)
```

---

### Phase 5 — Signal Check (48 hours post-launch)

**What you're doing:** A quick post-launch check to catch early issues and close the loop back to the measurement phase.

**Prompt (run 48 hours after launch):**
```
It's been 48 hours since we launched [feature].

Help me do a signal check:
1. Review the success metrics we defined in @[prd-final.md]
2. Review these early signals: @[notes from Slack, support tickets, sales feedback]
3. Are there any green flags (positive signals) worth capturing?
4. Are there any red flags that need immediate attention?
5. What should I bring to the retrospective that I might not have otherwise noticed?
```

**Output:** A brief signal summary. If anything is red, it feeds directly into a decision about whether to ship a fast follow or schedule remediation in the next sprint.

---

## File Naming Convention

| Artifact | Filename |
|---|---|
| Launch readiness summary | `[feature]-launch-readiness.md` |
| Release notes | `[feature]-release-notes.md` |
| Sales enablement brief | `[feature]-sales-brief.md` |
| CS brief | `[feature]-cs-brief.md` |
| Executive announcement | `[feature]-exec-announcement.md` |
| Customer announcement | `[feature]-customer-announcement.md` |
| Slack announcement | `[feature]-slack-announcement.md` |
| Full launch pack (combined) | `[feature]-launch-pack.md` |

---

## Common Mistakes

**Starting without the PRD.**
The PRD is where you defined the "why" — the customer problem, the business case, the success metrics. Without it, your launch comms are just a list of features with no story. Always bring the PRD.

**Skipping the readiness check.**
If something was deferred, your launch announcement needs to reflect that. Telling sales a feature exists that doesn't will cost you trust.

**One message for all audiences.**
The CISO who approved the budget doesn't want to read the same thing as the SOC analyst who will use it every day. Use the audience templates. They're short — the effort is worth it.

**Waiting for everything to be perfect.**
Ship the launch pack when the feature ships. A good-enough announcement on launch day is worth more than a perfect one three days later.

---

## Sub-Agents Used

| Agent | File | When Used |
|---|---|---|
| Executive Communicator | `skills/reviewer-guides/executive.md` | Review Gate — executive announcement |
| Engineer Reviewer | `skills/reviewer-guides/engineer.md` | Optional — if release notes need technical accuracy check |

---

## Time Estimate

| Phase | Time |
|---|---|
| Readiness check | 10–15 min |
| Generating all artifacts | 20–30 min |
| Review gate + checklist | 10 min |
| Distribution | 10–15 min |
| **Total** | **~60 min for a full Major launch** |

---

*Last updated: March 2026 · Part of the [Product Management Lifecycle](../README.md)*

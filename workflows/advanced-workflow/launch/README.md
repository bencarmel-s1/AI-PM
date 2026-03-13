# 🚀 Launch Phase

> Everything that happens between "it shipped" and "we're measuring it" — done in under an hour.

---

## The Problem This Solves

Most PM teams are good at writing PRDs. Far fewer have a consistent process for what happens after engineering ships.

The result: features land without the right people knowing. Sales doesn't know how to pitch the new capability. CS isn't prepared for the support questions. Leadership gets a Slack message instead of a business case. And the PM scrambles to write six different versions of the same announcement.

This phase fixes that. One Claude session. Six audience-ready artifacts. A checklist that makes sure nothing slips through.

---

## What's in This Folder

| File | What It Is |
|---|---|
| `launch-workflow.md` | The full step-by-step workflow — start here |
| `launch-pack-template.md` | Master template: generates all artifacts from a single session |
| `templates/release-notes.md` | Technical changelog (engineering + Confluence) |
| `templates/sales-enablement-brief.md` | 1-page brief for sales and SEs — what's new, how to pitch it, objection handling |
| `templates/cs-enablement-brief.md` | CS and support brief — what customers will ask, how to answer |
| `templates/executive-announcement.md` | Business-impact summary for leadership |
| `templates/customer-announcement.md` | Customer-facing announcement (changelog / email) |
| `templates/slack-announcement.md` | Internal team announcement for Slack |

---

## Quick Start (30 seconds)

Open Claude Code in the folder with your PRD, then paste this:

```
I need to create a launch pack for a feature we just shipped.
Use @launch-workflow.md and @launch-pack-template.md to guide me.
Use @company-context-sentinelone.md for product and audience context.
Input files: @[your-prd.md] and @[jira-export.md or sprint-notes.md]
Launch tier: [Major / Minor / Patch — or let Claude assess]
```

Claude will assess what shipped, decide the right launch tier, and generate all the artifacts you need in one session.

---

## Launch Tiers

Not every ship needs the same effort. Use this to calibrate:

| Tier | What It Is | Artifacts Needed |
|---|---|---|
| 🔴 **Major** | Net-new capability, new persona, or significant workflow change | All 6 artifacts + checklist |
| 🟡 **Minor** | Enhancement to existing feature, improved UX, new integration | Release notes + Sales/CS brief + Slack announcement |
| 🟢 **Patch** | Bug fix, performance improvement, or behind-the-scenes change | Release notes only |

When in doubt, default to 🟡 Minor. You can always scale up.

---

## The 5-Phase Process

```
Phase 1 — Readiness Check  → What actually shipped vs. what was planned?
Phase 2 — Generate Pack    → One session produces all audience artifacts
Phase 3 — Review Gate      → Quick checklist + executive review before anything goes out
Phase 4 — Distribute       → Slack, Confluence, Jira, Sales/CS share
Phase 5 — Signal Check     → 48-hour post-launch check; feeds into measurement phase
```

Full details in `launch-workflow.md`.

---

## Time Estimate

| Phase | Time |
|---|---|
| Readiness check | 10–15 min |
| Generating all artifacts | 20–30 min |
| Review + checklist | 10 min |
| Distribution | 10–15 min |
| **Total** | **~60 min for a full Major launch pack** |

---

## How This Connects to the Lifecycle

```
← PRD (Stage 4)          Launch (Stage 7)          Retrospective (Stage 8) →
   What we planned    What shipped + who knows    What we learned
```

The launch pack bridges the PRD (what you intended) and the retrospective (what you learned). The executive announcement ties back to the goals you wrote in the PRD. The CS brief connects to the support tickets you'll see in the next measurement cycle.

---

*Last updated: March 2026 · Part of the [Product Management Lifecycle](../README.md)*

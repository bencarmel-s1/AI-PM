# Workflows

Step-by-step Claude Code workflows for common PM tasks.

Workflows go beyond single prompts — they describe a full sequence of interactions with Claude Code to accomplish a larger goal, like going from raw research to a finalized PRD.

---

## What Belongs Here

- End-to-end workflows that chain multiple prompts together
- Guides for recurring PM rituals (sprint planning, discovery synthesis, etc.)
- Claude Code + tool integrations (e.g., with Jira, Confluence, Notion)
- Tips for iterating on Claude's output across a multi-step task

---

## Workflow Format

When documenting a workflow, include:

```markdown
## [Workflow Name]

**Goal:** What you're trying to accomplish
**Time:** Approximate time to complete
**Inputs needed:** What you bring to the session (e.g., interview transcripts, a rough brief)

### Steps

1. **Step 1: [Name]**
   What to do and what prompt to use.

2. **Step 2: [Name]**
   What to do next, including how to use Claude's output from step 1.

...

### Tips
- What to watch out for
- How to handle cases where Claude's output needs adjustment
```

---

## Workflows in This Folder

| Folder | What It Contains |
|---|---|
| [`basic-workflows/`](./basic-workflows/) | 6 ready-to-use templates for everyday PM tasks |
| [`advanced-workflow/prd-creation/`](./advanced-workflow/prd-creation/) | Full 5-phase PRD creation workflow with Socratic questioning and agent reviews |
| [`advanced-workflow/data-analysis/`](./advanced-workflow/data-analysis/) | 3-phase data analysis workflow — funnel discovery, ROI modeling, and A/B test readouts |
| [`company-context/`](./company-context/) | Templates for giving Claude persistent SentinelOne context — start here before any PRD session |

---

> **Tip:** The best workflows are ones you've already run yourself. Don't document a workflow you haven't tried — real usage uncovers the steps that matter.

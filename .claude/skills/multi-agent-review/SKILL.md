---
name: multi-agent-review
description: Run all 3 specialist agents (engineer, executive, user-researcher) in parallel on a spec or PRD, then synthesize into a unified, priority-ordered review. Invoke when you have a document ready for multi-perspective review.
---

Claude can run multiple specialist agents simultaneously on the same document — giving you engineer, executive, and user-researcher perspectives in a single pass instead of three separate sessions.

## What this covers

This skill walks through a three-stage workflow:

1. **Fan-out** — invoke all three agents in parallel on the same spec or PRD
2. **Collect** — gather each agent's structured review output
3. **Synthesize** — merge into a single, priority-ordered review with consensus signals and tension points

You can run all three stages in one prompt, or step through them if you want to review each agent's output before synthesis.

---

## Fan-out: run agents in parallel

Use this when you have a spec, PRD, or feature brief that's ready for review:

```
Review @[your-spec.md] using the engineer, executive, and user-researcher agents in parallel.
Give each agent the full document — don't summarize or filter.
```

Claude will spawn all three agents simultaneously. Each agent applies its own review lens without seeing the other agents' output.

---

## Collect: review individual perspectives

After the fan-out, you'll have three separate reviews:

- **Engineer:** Ambiguities, technical risks, missing edge cases, complexity assessment
- **Executive:** Strategic fit, business case gaps, leadership concerns, decision points
- **User Researcher:** Theme validation, pain point coverage, segment gaps, research recommendations

If you want to inspect each review before synthesis:

```
Show me each agent's review separately before combining them.
```

---

## Synthesize: unified review

Merge the three perspectives into a single document organized by priority:

```
Synthesize the three agent reviews into one document.
Organize by priority (critical → important → nice-to-have), not by reviewer.
Flag consensus signals where multiple agents raised the same concern.
Surface tensions where agents disagree.
Save to [feature]-multi-agent-review.md.
```

The synthesis highlights where agents agree (strong signal to act) and where they disagree (worth understanding both sides before deciding).

---

## When to use subagents vs agent teams

| Approach | Best For |
|---|---|
| **Subagents** (default) | Spec reviews, PRD reviews, any task where agents review the same document. Simpler, faster, all context in one session. |
| **Agent Teams** (experimental) | Large parallel research tasks where agents need to work independently for extended periods — e.g., competitive deep-dives across 5+ competitors. |

For most PM review workflows, subagents are the right choice.

---

## Tips

**Run all three stages in one pass** for the fastest results:

```
Run engineer, executive, and user-researcher agents in parallel on @[your-spec.md].
Synthesize into a unified review organized by priority.
Save to [feature]-multi-agent-review.md.
```

**Pair with `/prd-creation` as a quality gate.** After completing the PRD workflow, run this skill on the final draft before sharing with stakeholders.

**Save the review for reference.** The unified review is useful context for future conversations — `@reference` it when addressing feedback or iterating on the spec:

```
Address the critical items from @[feature]-multi-agent-review.md and update @[feature]-prd-final.md.
```

# Skill: Multi-Agent Patterns

Claude Code can run multiple specialist agents simultaneously on the same document — giving you engineer, executive, and user-researcher perspectives in a single pass instead of three separate sessions.

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

## Composing the existing agents

The repo ships with three specialist agents that are designed to complement each other:

| Agent | Perspective | What It Catches |
|---|---|---|
| `engineer` | Technical feasibility | Architecture gaps, implementation risks, missing edge cases, complexity underestimation |
| `executive` | Business & strategy | Weak business case, missing revenue math, leadership objections, strategic misalignment |
| `user-researcher` | User & research | Unvalidated assumptions, segment gaps, usability risks, missing research |

**Together, they cover the three angles that matter most before sharing a spec:** Can we build it? Should we build it? Do users actually need it?

---

## PM-specific multi-agent patterns

Beyond spec review, here are other ways to compose agents for PM work:

### Parallel competitive research

When researching multiple competitors, fan out agents to research in parallel:

```
Research these 4 competitors in parallel — one agent per competitor.
For each, produce: positioning, strengths, weaknesses, and notable recent moves.
Then synthesize into a competitive landscape matrix.
```

### Multi-perspective risk assessment

Before a major launch or investment decision:

```
Run the engineer and executive agents on @[launch-plan.md].
Engineer: focus on technical launch risks and rollback scenarios.
Executive: focus on market timing, competitive response, and stakeholder alignment.
Synthesize into a risk register with severity and mitigation for each item.
```

### Draft → review pipeline

Use one agent to draft, another to review:

```
Draft an executive update using the stakeholder-communication skill.
Then run the executive agent to review it for tone, framing, and completeness.
```

---

## When to use subagents vs agent teams

| Approach | How It Works | Best For |
|---|---|---|
| **Subagents** (default) | Claude spawns agents within a single session — you see all output in one conversation | Most PM workflows. Simpler, faster, all context stays together. |
| **Agent Teams** (experimental) | Multiple Claude instances work in parallel with shared task lists and inter-agent messaging | Very large tasks where agents need to work independently for extended periods (e.g., multi-day competitive research sprints, parallel workstream planning). |

**Rule of thumb:** If the task fits in one conversation, use subagents. If agents need to work for hours independently and coordinate asynchronously, consider agent teams.

---

## Tips

**Run all three stages in one pass** for the fastest results:

```
Run engineer, executive, and user-researcher agents in parallel on @[your-spec.md].
Synthesize into a unified review organized by priority.
Save to [feature]-multi-agent-review.md.
```

**Pair with `/prd-creation` as a quality gate.** After completing the PRD workflow, run this skill on the final draft before sharing with stakeholders.

**Save the review for reference.** The unified review is useful context for future conversations — `@reference` it when addressing feedback or iterating on the spec.

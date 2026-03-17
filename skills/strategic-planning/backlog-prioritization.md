# Skill: Backlog Prioritization

Backlog prioritization is as much a communication problem as a decision problem. Claude can help you normalize messy backlog items, assess their strategic fit, and articulate a clear narrative around where to focus — before you walk into a prioritization session.

---

## The workflow

This skill covers four stages you can use in sequence or individually:

1. **Normalize** — get all backlog items into consistent, outcome-oriented language
2. **Align** — assess how well each item maps to your product strategy
3. **Identify candidates** — group items that are strong candidates for prioritization
4. **Frame the narrative** — articulate the rationale in a way stakeholders can follow

---

## Step 1: Normalize backlog items

Backlog items often vary wildly in how they're written. Before any discussion, get them into a consistent format:

```
Read @backlog.md and normalize each item into consistent, outcome-oriented language.
Clarify what problem or opportunity each item addresses.
Don't assess feasibility or effort — just clarify the intent.
```

---

## Step 2: Assess strategic alignment

Once the backlog is normalized, check each item against your stated strategy:

```
Here is our current product strategy: @strategy.md
Assess how well each item in @backlog-normalized.md aligns with these strategic priorities.
Surface areas of strong alignment, weak alignment, and ambiguity.
```

Don't ask Claude to recommend what to prioritize here — the goal is to surface where alignment is strong and where it's unclear.

---

## Step 3: Identify priority candidates

When the backlog is large, narrow the field before the human discussion:

```
Based on the strategy alignment analysis, group @backlog-normalized.md into priority candidate sets.
Explain why items belong in each group using narrative reasoning — don't rank them.
```

This gives you a shortlist to debate rather than a wall of options.

---

## Step 4: Frame the prioritization narrative

Before your planning forum or leadership conversation:

```
Synthesize the backlog analysis into a strategic narrative explaining our current focus and the key trade-offs.
Optimize for clarity and shared understanding. Don't make prioritization recommendations.
```

---

## Tips

**Include your strategy document whenever possible.** Without it, alignment analysis is generic. With it, Claude can give you specific, grounded observations about your backlog.

**Save outputs at each stage.** Prioritization conversations evolve — you'll want to refer back to the alignment analysis when someone challenges a decision:

```
Write the alignment analysis to backlog-alignment.md
```

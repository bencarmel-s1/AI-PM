# Skill: To-Do Prioritization

When your to-do list is full but unfocused, Claude can help you cut through the noise — identifying which tasks deserve your attention now and which can wait, based on strategic leverage rather than urgency alone.

---

## When to use this

- During weekly or daily planning sessions
- Before leadership or alignment-heavy weeks when your time is especially scarce
- When you have a long list and can't see the signal through the clutter
- When you're deciding what *not* to spend time on

---

## How to use it

Reference your to-do list and ask for a prioritization read:

```
Here are my to-dos for this week: @todo_index.md
Group them into priority bands based on strategic leverage, decision impact, and time sensitivity.
Explain why certain tasks deserve focus now vs. later.
```

Claude will interpret the intent behind each task, group them into priority bands (high-leverage now, important but deferrable, low strategic impact), and give you a short narrative explaining the reasoning.

---

## What Claude uses to prioritize

Claude evaluates tasks across five dimensions:

- **Strategic alignment** — Does this move something that actually matters?
- **Decision leverage** — Does delaying this block a decision downstream?
- **Stakeholder impact** — Is someone waiting on this?
- **Time sensitivity** — Is there a real deadline, or just friction?
- **Cognitive cost** — Is this a draining task best tackled when you're fresh?

You don't need to spell all of this out. But if a specific constraint matters most this week, say so:

```
This is a high-stakes alignment week with leadership. Weight stakeholder impact and timing heavily.
Here are my tasks: @todo_index.md
```

---

## What Claude won't do

Claude won't give you an exact schedule, break tasks into subtasks, or estimate how long things take. The output is a structured view of *what matters and why* — the execution is yours.

---

## Tips

**Run this at the start of the week, not the end.** The output is most useful when you still have choices about how to spend your time.

**Update your to-do list file regularly.** If you keep tasks in a file like `todo_index.md`, you can ask Claude to re-prioritize mid-week when things shift:

```
Things have shifted — the exec review moved to Wednesday.
Re-prioritize @todo_index.md with that in mind.
```

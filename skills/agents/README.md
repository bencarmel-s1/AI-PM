# Skill: Agents

Claude can spin up specialized sub-agents to handle tasks on your behalf — each one focused, autonomous, and built for a specific type of work.

---

## What is an agent?

Think of it like delegating to a specialist. Instead of one generalist Claude handling everything, an agent is a scoped version of Claude with a defined role — a user researcher, an engineer, an executive communicator. You describe the task, it runs to completion, and hands you back the result.

---

## How to use these templates

Each file in this folder is a ready-to-pull agent template. Reference it with `@` to invoke that agent with the right context:

```
Use @agents/user-researcher.md to synthesize the interviews in @interviews/
```

```
Use @agents/executive.md to turn @sprint-notes.md into a leadership update
```

```
Use @agents/engineer.md to review @prd-v2.md before I send it to engineering
```

---

## Agent Index

| Agent | Best for |
|---|---|
| `user-researcher.md` | Synthesizing interviews, tickets, and qualitative feedback |
| `executive.md` | Reframing updates and decisions for leadership |
| `engineer.md` | Reviewing specs for technical gaps and feasibility |

---

## Running multiple agents on the same task

```
Use @agents/engineer.md to check @feature-spec.md for technical gaps, then use @agents/executive.md to turn the findings into a 1-page brief for my CPO.
```

---

## When NOT to use an agent

Agents add a small amount of overhead — they're overkill for simple tasks.

- **Don't use:** "Summarize this meeting in 3 bullets" — just ask Claude directly
- **Don't use:** "Fix the typo in this paragraph"
- **Do use:** Any task where you'd naturally say "I need someone who really knows X to look at this"

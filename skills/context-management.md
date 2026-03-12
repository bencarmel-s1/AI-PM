# Skill: Context Management

Understanding how Claude's memory works within a session — and across sessions — will save you a lot of frustration.

---

## What is a "context window"?

Think of it like a whiteboard. Everything in your current conversation — your messages, Claude's responses, and the files you've referenced — is written on that whiteboard. Claude can only see what's on the whiteboard.

- The whiteboard is large (it can hold roughly 100,000–200,000 words depending on the model)
- Once it fills up, older content gets pushed off the edge
- When you start a new session (`claude` → new terminal), the whiteboard is erased

**Practical implication:** For most PM tasks (meeting notes, single research synthesis, a weekly update), you'll never hit the limit. For very large projects — synthesizing 20+ interviews, analyzing a full PRD — keep an eye on session length.

---

## Within a session: what Claude remembers

Once you've referenced a file or pasted content in a session, Claude has it. You don't need to repeat it.

**Do this:**
```
First session message: Process @meeting-notes.txt using @meeting-notes-to-action-items.md
Follow-up: Move the design review task to Sarah instead of Jake
Follow-up: Add a section for open questions
```

**Don't do this:**
```
# Unnecessary — Claude already has the notes
Follow-up: Here are my meeting notes again: [pastes everything again]
```

---

## When to start a new session

Start fresh when:
- You're switching to a completely unrelated task
- A previous session got very long and Claude seems to be losing earlier context
- You want to approach the same problem from a clean slate

To carry forward important context into a new session, start with a summary:
```
Here's context for this session: We're working on [product name].
I'm a PM focused on [area].
In a previous session, we synthesized user research and found [key insight].
Today I want to [new task].
```

---

## Tips for long research sessions

**Chunk your work.** Instead of loading all 15 interviews at once, synthesize in batches:
```
Synthesize the first 5 interviews in @batch-1/ using @user-research-synthesis.md
```
Then:
```
Now synthesize @batch-2/ the same way
```
Then:
```
Combine both syntheses into one final summary
```

**Save intermediate outputs.** After each meaningful step:
```
Write that synthesis to synthesis-batch-1.md
```
This gives you a checkpoint you can `@reference` in future sessions even if context resets.

**Don't re-paste what Claude already has.** If you referenced `@prd.md` early in a session, Claude still has it. Just refer to it by name ("the PRD we discussed") rather than pasting again.

---

## Cross-session memory: CLAUDE.md

Claude doesn't remember anything between sessions by default. But you can give it persistent context by creating a `CLAUDE.md` file in your working folder. See [`getting-started/claude-code/claude-md-setup.md`](../getting-started/claude-code/claude-md-setup.md) for how to set this up.

For SentinelOne PMs, [`workflows/company-context/company-context-sentinelone.md`](../workflows/company-context/company-context-sentinelone.md) is a ready-to-fill starting point — company-wide context is already there, just add your area's priorities and team details.

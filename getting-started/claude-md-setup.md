# Setting Up Your CLAUDE.md File

`CLAUDE.md` is a file you place in your working folder. Every time you start Claude Code from that folder, it automatically reads this file first — giving Claude persistent context about your product, team, and preferences without you having to re-explain it every session.

This is one of the highest-leverage things a PM can set up.

---

## What it does

Without CLAUDE.md, every new Claude Code session starts blank. You find yourself typing the same setup context repeatedly:
> "I'm a PM at [company]. Our product is [X]. Our main users are [Y]..."

With CLAUDE.md, Claude already knows this when the session starts.

---

## How to create it

In your working folder, create a file named exactly `CLAUDE.md`:

**On Mac (terminal):**
```
nano ~/pm-work/CLAUDE.md
```

**On Windows (terminal):**
```
notepad C:\Users\[username]\pm-work\CLAUDE.md
```

Or create it in any text editor and save it as `CLAUDE.md` (capital letters, no other extension).

---

## What to put in it

Start simple. You can always add more later.

```markdown
# My PM Context

## Product
**Product name:** [name]
**What it does:** [one sentence]
**Stage:** [Early / Growth / Mature]

## Users
**Primary persona:** [e.g., "Mid-market operations managers at logistics companies"]
**Key pain points we solve:** [2-3 bullets]

## Team
**My role:** Product Manager
**Squad:** [team name]
**Key stakeholders:** [names and roles, e.g., "Sarah (Eng Lead), Marcus (Design), Priya (Data)"]

## My preferences
**Tone:** Clear and direct. No fluff.
**Format preference:** Use bullet points and tables where possible.
**Avoid:** Padding, unnecessary caveats, restating what I told you.
```

---

## More things you can add

**Product vocabulary** — terms your team uses that Claude might not know:
```markdown
## Our terminology
- "Activation" = a user completes their first core action within 7 days of signup
- "Champion" = the internal sponsor at a customer account
- "Pod" = our term for a cross-functional squad
```

**Recurring tasks** — shortcuts for things you do every week:
```markdown
## Common tasks I run
- Weekly status update → use @weekly-status-update.md
- Interview synthesis → use @user-research-synthesis.md
- Story writing → always include edge cases and error states
```

**Constraints** — things Claude should always keep in mind:
```markdown
## Constraints
- We don't have a mobile app yet — don't suggest mobile features
- Our engineering team is 4 people — scope accordingly
- We're pre-Series A — focus on learning, not scale
```

---

## Folder-specific CLAUDE.md files

You can have different `CLAUDE.md` files for different projects. Claude reads the one in the folder where you start your session.

**Example structure:**
```
~/pm-work/
├── CLAUDE.md          ← general PM context
├── project-alpha/
│   └── CLAUDE.md      ← specific context for Project Alpha
└── project-beta/
    └── CLAUDE.md      ← specific context for Project Beta
```

---

## Verify it's working

Start a Claude Code session from your working folder and ask:
```
What do you know about my product and team?
```

Claude should reflect back the context from your `CLAUDE.md`. If it doesn't, check that the file is named exactly `CLAUDE.md` and is in the folder where you ran the `claude` command.

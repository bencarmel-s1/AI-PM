# Sub-Agent Setup Instructions

These 3 files are the AI specialist team used in the PRD creation workflow.
They need to be in the right place to work — they can't be used from this folder directly.

The agent files live in the `reviewers/` folder of this repo. This folder just contains setup instructions.

---

## How to Install

Copy the 3 agent files from `reviewers/` into your project's `.claude/agents/` folder:

```
your-project/
└── .claude/
    └── agents/
        ├── engineer.md        ← copy here
        ├── executive.md       ← copy here
        └── user-researcher.md ← copy here
```

**On Mac/Linux (run from the repo root):**
```bash
cp reviewers/engineer.md your-project/.claude/agents/
cp reviewers/executive.md your-project/.claude/agents/
cp reviewers/user-researcher.md your-project/.claude/agents/
```

If the `.claude/agents/` folder doesn't exist yet:
```bash
mkdir -p your-project/.claude/agents/
```

---

## How to Verify They're Working

Open Claude Code in your project and type:
```
Use the engineer sub-agent to review this requirement: [paste any text]
```

You should see the (@_@) Engineer persona respond. If not, check the file is in `.claude/agents/` (not a subfolder of it).

---

## What Each Agent Does

| Agent | File | Color | Best For |
|---|---|---|---|
| (@_@) Engineer | `engineer.md` | Purple | Technical feasibility, architecture gaps, implementation risks |
| (ಠ_ಠ) Executive | `executive.md` | Blue | Business case, revenue framing, leadership pushback |
| (^◡^) User Researcher | `user-researcher.md` | Green | User problem validation, research gaps, usability risks |

---

## Customizing for Your Team

These are general-purpose personas. You can customize them for your context:

- Change the **description** field to make them more specific to your domain
- Add your company's preferred frameworks to the **Review Structure** section
- Adjust the **Communication Style** to match your team's norms

The YAML frontmatter (between the `---` markers) controls how Claude Code invokes the agent. Don't change the `name:` field — that's how the workflow calls them.

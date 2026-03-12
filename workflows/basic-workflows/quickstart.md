# Your First Workflow — Step by Step

This guide walks you through completing your very first Claude Code workflow from scratch. No prior experience needed. You'll go from a blank terminal to processed meeting action items in under 15 minutes.

---

## What you'll do
1. Navigate to a working folder
2. Save your meeting notes as a file
3. Start Claude Code
4. Run the meeting-notes-to-action-items workflow
5. Get output you can actually use

---

## Step 1 — Create a working folder

Open your terminal (Mac: `Terminal` or `iTerm`. Windows: `PowerShell`).

Create a folder for your PM work:
```
mkdir ~/pm-work
cd ~/pm-work
```

> **Why this matters:** Claude Code reads files from the folder you're currently in. All your `@filename` references need to point to files in this folder (or subfolders).

---

## Step 2 — Save your meeting notes as a file

Copy your raw meeting notes (from Teams, Notion, email, wherever) into a plain text file.

**On Mac:**
```
nano meeting-notes.txt
```
Paste your notes, then press `Ctrl+X` → `Y` → `Enter` to save.

**On Windows:**
```
notepad meeting-notes.txt
```
Paste your notes and save.

**Or use VS Code / any text editor** — just save the file as `meeting-notes.txt` in your `~/pm-work` folder.

> **Accepted formats:** `.txt` and `.md` both work. Teams auto-transcripts, Zoom AI notes, or your own handwritten notes all work fine — Claude can read messy input.

---

## Step 3 — Copy the template to your working folder

The templates only work if they're accessible from your current folder. Copy the template you need:

```
cp /path/to/AI-PM/workflows/Basic\ Workflows/meeting-notes-to-action-items.md ~/pm-work/
```

Or just keep both files in the same folder you're working in.

---

## Step 4 — Start Claude Code

In your terminal (from inside `~/pm-work`):
```
claude
```

You'll see the Claude Code welcome screen. You're now in a live session.

---

## Step 5 — Run the workflow

Type this prompt and press Enter:

```
Process @meeting-notes.txt using @meeting-notes-to-action-items.md
```

Claude will:
1. Read your meeting notes file
2. Apply the template structure
3. Output a formatted summary with action items by owner, decisions made, and open questions

---

## Step 6 — Save the output to a file

Ask Claude to write the result to a file so you can reference it later:

```
Write that output to action-items-2026-03-10.md
```

Now you have a dated file you can share, `@reference` in future prompts, or drop into Notion.

---

## What to do when the output isn't right

Don't start over — just follow up in the same session:

| Problem | What to type |
|---|---|
| Output is too long | `Make this more concise` |
| Missing a key decision | `Add [X] under Decisions Made` |
| Wrong owner on a task | `Move the [task] action item to [Name]` |
| Wrong tone | `Rewrite this for a Slack message` |
| Want another format | `Reformat this as a bullet list` |

Claude remembers everything in the current session — you don't need to re-paste your notes.

---

## You're done

You just ran your first workflow. The same pattern applies to every template in this folder:

1. Save your input as a `.txt` or `.md` file
2. Run `claude` from the same folder
3. Type: `[what you want] using @[template-name].md based on @[your-input-file]`
4. Follow up to refine

---

## Next steps

- Try **user-research-synthesis.md** after your next round of interviews
- Set up a **CLAUDE.md** file using [`workflows/company-context/company-context-sentinelone.md`](../company-context/company-context-sentinelone.md) as your starting point — SentinelOne context is pre-filled, just add your area (see [`getting-started/claude-code/claude-md-setup.md`](../../getting-started/claude-code/claude-md-setup.md) for instructions)
- Read **skills/context-management.md** before your first long research session

# Skill: Status Line Customization

Claude Code can display a persistent status bar at the bottom of your terminal showing your current model, working folder, and — most usefully — how full your context window is. Setting this up takes about 30 seconds and changes how you manage long sessions.

---

## Why this matters

Claude compacts your conversation at around **80% context usage**, not 100%. By the time it looks like you have 20% left, you're already at the effective limit. Without a status line, you have no visibility into this until it happens.

The status line solves this by showing a live progress bar scaled to the real limit — so 80% usage displays as 100%, and you can see orange coming before the conversation degrades.

---

## What it shows

A well-configured status line gives you three things at a glance:

```
claude-sonnet-4-6 | my-project | ████░░░░░░ 40%
```

- **Model name** — which Claude model is active (dimmed, low distraction)
- **Folder name** — which directory you're in (useful with multiple terminal tabs)
- **Context bar** — 10-character block progress bar with scaled percentage

---

## Setting it up

Run the `/statusline` command and describe what you want. Here's the configuration that works well for PM sessions:

```
/statusline show model name, folder name (not full path), and context usage as a
10-character block progress bar with the scaled percentage next to it. Use pipe
separators between items. Scale so 80% real usage shows as 100%. Color the bar
green under 50%, yellow 50–64%, orange 65–95%, blinking red with a skull at 95%+.
Dim the model and folder name, bright colors only the bar.
```

The `/statusline` command uses a specialized subagent that writes a shell script to `~/.claude/statusline-command.sh` and registers it in `~/.claude/settings.json`. The bar appears on your next fresh session.

---

## Color thresholds

| Color | Scaled % | What it means |
|---|---|---|
| 🟢 Green | 0–49% | Plenty of room — work freely |
| 🟡 Yellow | 50–64% | Starting to fill — finish what you're doing |
| 🟠 Orange | 65–94% | Consider wrapping up or starting a new session |
| 💀 Blinking red | 95%+ | Compaction is imminent — `/clear` now if possible |

**Practical rule:** when you see orange, decide whether to finish the task in this session or start fresh. Don't wait for red.

---

## Managing context

When the bar hits orange or you're switching to an unrelated task:

```
/clear
```

This resets context to zero. For tasks that span multiple sessions, save intermediate outputs first:

```
Write that synthesis to synthesis-v1.md before we continue
```

Then `@reference` the saved file in the new session instead of repeating the work.

For more on session management strategies, see [`skills/context-management.md`](../context-management.md).

---

## Customizing later

Run `/statusline` again at any time with new instructions — it overwrites the previous configuration. Common additions:

- Current git branch
- Different color thresholds
- Showing token counts instead of a percentage

To remove the status line entirely, delete the `statusBarText` field from `~/.claude/settings.json`.

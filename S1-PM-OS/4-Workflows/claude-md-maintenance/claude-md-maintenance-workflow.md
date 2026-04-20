# CLAUDE.md Maintenance Workflow
*A weekly AI-assisted audit to keep CLAUDE.md accurate — ~10 minutes, every Monday*

---

## Why This Matters

CLAUDE.md is loaded into every Claude session. It tells Claude who I am, what I'm working on, what tools exist, and how to route requests. When it drifts from reality, Claude gives stale advice: wrong OKR targets, missing skills, outdated priorities.

A 10-minute weekly audit beats a 2-hour "why is Claude acting weird" debugging session.

---

## Before You Start

- [ ] The `update-claude-md` skill is installed in `.claude/skills/`
- [ ] Recent daily notes are up to date in `3-Meetings/Personal Notes/2026/`
- [ ] `5-Knowledge/Reference/fy27-okr-history.md` reflects the latest OKR state

---

## The Workflow (4 Steps)

---

### Step 1 — Trigger the Audit (1 min)

If the LaunchAgent fired, Claude will have already started the audit. Review the suggested changes when you return to your desk.

**Manual trigger prompt:**
```
Weekly CLAUDE.md review — please run the update-claude-md skill to audit this file against current sources.
```

Or simply say: `audit CLAUDE.md`

---

### Step 2 — Review Each Section (5–8 min)

The skill presents one flagged section at a time:

```
## Section: Current Focus

CURRENT:
  Immediate tasks: finalize FY27 fiscal calendar, Identity rollout, Cloud scoping

SUGGESTED:
  Immediate tasks: Identity rollout schedule, Cloud ingestion framework scoping

REASON: fy27-okr-history.md shows fiscal calendar finalized on 2026-03-15.

Accept? [yes / no / edit]
```

**Your decision options:**
- `yes` — accept as written
- `no` — skip this section, keep current text
- `edit` — paste your preferred wording and Claude incorporates it

Sections with no drift are flagged as "No changes detected" — no decision needed.

---

### Step 3 — Apply Changes (1 min)

After reviewing all sections, Claude applies every accepted edit to CLAUDE.md in a single write. It confirms which sections were updated and notes the audit date.

If everything was already current, Claude closes without writing.

---

### Step 4 — Verify (1 min)

Quickly scan the updated CLAUDE.md to confirm it looks right. The file should feel current — goals match the quarter you're actually in, skills match what's installed, folders match what exists.

---

## Failure Modes & Fixes

| Problem | Fix |
|---------|-----|
| LaunchAgent didn't fire Monday | Run manually with "audit CLAUDE.md". Check `/tmp/claude-md-review.log` for errors. |
| `claude` CLI not found in LaunchAgent | Add `export PATH` for the Claude CLI location to `claude-md-weekly-review.sh`. |
| Skill not triggering automatically | Check skill-activator.py is running. Trigger manually instead. |
| Skill suggests wrong change | Say "no" or "edit" — it never writes without your approval. |
| CLAUDE.md feels stale but audit finds nothing | The source files may be stale too. Update `fy27-okr-history.md` or recent daily notes first. |

---

## Scheduling Details

**LaunchAgent:** `~/Library/LaunchAgents/com.yourname.claude-md-review.plist`
- Fires: every Monday at 9:00 AM
- Calls: `scripts/claude-md-weekly-review.sh`
- Log: `/tmp/claude-md-review.log`

**To verify it's loaded:**
```bash
launchctl list | grep claude-md
```

**To reload after editing the plist:**
```bash
launchctl unload ~/Library/LaunchAgents/com.yourname.claude-md-review.plist
launchctl load ~/Library/LaunchAgents/com.yourname.claude-md-review.plist
```

**To test on-demand:**
```bash
launchctl start com.yourname.claude-md-review
```

# PM Templates Library

A reusable library of templates for common PM workflows. Each template is designed to work with Claude Code using the `@filename` pattern.

---

## How to use these templates with Claude Code

Reference any template with the `@` symbol:
```
Write my weekly update using @weekly-status-update.md
```
```
Draft a PRD using @PRD-Template/Figma-PRD-Template.md based on @user-research-synthesis.md
```

---

## Template Index

### Research & Discovery
| Template | What it does |
|---|---|
| `Customer-Interview-Template/` | Structure for capturing and summarizing user interviews |
| `user-research-synthesis.md` | Synthesize findings across multiple interviews into themes |
| `competitive-analysis.md` | Feature comparison matrix + competitor positioning |

### Planning & Prioritization
| Template | What it does |
|---|---|
| `PRD-Template/` | Full product requirements document (Figma format + alternative) |
| `Backlog Templates/` | Epics and user stories for backlog grooming |
| `user-story.md` | Individual user story with acceptance criteria |

### Communication
| Template | What it does |
|---|---|
| `communication-styles/` | Slack update, executive email, and Notion doc formats |
| `weekly-status-update.md` | Shipped / in progress / blocked weekly summary |

### Meeting & Notes
| Template | What it does |
|---|---|
| `Notes-Template/` | Meeting notes and mentorship session structure |
| `meeting-notes-to-action-items.md` | Process raw notes into action items by owner |

### Retrospectives
| Template | What it does |
|---|---|
| `sprint-retrospective.md` | What went well, what didn't, action items |

### Infrastructure & Automation
| Template | What it does |
|---|---|
| `plugin-packaging.md` | Package skills, agents, and commands as a Claude Code plugin |
| `hooks-for-pms.md` | PM-specific hook recipes for automating reviews and quality gates |

---

## Common Workflows

**End of day processing:**
```
Process @[meeting-notes.md] using @meeting-notes-to-action-items.md
```

**After user interviews:**
```
Analyze all files in @[interviews-folder] and create a synthesis using @user-research-synthesis.md
```

**Communicate research to multiple audiences:**
```
Based on @communication-styles, create 3 versions of @[synthesis.md] in a new document
```

**Write a PRD from research:**
```
Draft a PRD using @PRD-Template/Figma-PRD-Template.md based on @[research.md]
```

**Break a PRD into stories:**
```
Break @[prd.md] into user stories using @Backlog Templates/user-story-template
```

---

## Each folder has its own README
Open any subfolder's `README.md` for detailed usage instructions and Claude Code prompt examples.

---

## When the output isn't right — how to iterate

Don't start a new session. Just follow up in the same conversation:

| Problem | Follow-up prompt |
|---|---|
| Too long | `Make this more concise` |
| Too short / missing detail | `Expand the [section] with more detail` |
| Wrong tone | `Rewrite this for an engineering audience` / `Make this more executive-friendly` |
| Missed something | `You missed [X] — add it under [section]` |
| Wrong format | `Reformat this as a table` / `Give me this as bullet points` |
| Want a different take | `Try a different approach — focus on [angle]` |

Claude remembers your full context within a session. You never need to re-paste your input files.

---

## Saving output to a file

Ask Claude to write results directly to a file so you can share it or `@reference` it later:

```
Write that output to action-items-2026-03-10.md
```

Dated filenames make it easy to build up a history. You can then reference past outputs in future prompts:

```
Compare @action-items-2026-03-10.md with @action-items-2026-03-17.md and show what changed
```

---

*Last updated: March 2026*

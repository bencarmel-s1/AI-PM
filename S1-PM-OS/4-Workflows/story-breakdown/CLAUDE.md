# Story Breakdown Workflow

Turn a finalized PRD into a complete, pushed engineering backlog — epics, stories, acceptance criteria, estimates, and dependencies — in one Claude session.

## When to Trigger

Say "break down the PRD", "create stories", "push to Jira", "push to GitHub", or "story breakdown" when you have a finalized PRD and want to generate the engineering backlog.

## What This Produces

- 3–6 epics with scope and definition of done
- 15–25 user stories with acceptance criteria, story points, labels, and dependencies
- A dependency map showing what blocks what
- All tickets pushed directly to Jira or GitHub via MCP

## Key Constraints

- Always requires a finalized PRD — never run on a draft
- Confirm the epic structure with the PM before decomposing into stories
- Stories must have independently verifiable acceptance criteria — no "works correctly" or "looks good"
- Stories over 8 points must be flagged for splitting before pushing
- Run the review gate (Phase 4) before pushing any tickets
- For Jira: requires Jira MCP (Atlassian integration)
- For GitHub: requires GitHub MCP or `gh` CLI access

## Files in This Workflow

1. `story-breakdown-workflow.md` — Full 5-phase workflow, start here
2. `story-breakdown-template.md` — Output template: full breakdown with epics, stories, and ACs
3. `epic-template.md` — Single epic structure for pushing individual epics
4. `story-template.md` — Single story structure for pushing individual stories
5. `example-story-breakdown.md` — Complete worked example (AI-assisted anomaly detection (worked example))

## The 5-Phase Process

- Phase 1 — Parse & Structure: Read the PRD, propose epic breakdown, confirm with PM
- Phase 2 — Decompose into Stories: Break each epic into user stories with acceptance criteria
- Phase 3 — Estimate & Sequence: Story points, build order, dependency mapping
- Phase 4 — Review Gate: Coverage check, AC quality, dependency risks, missing stories
- Phase 5 — Push to Jira / GitHub: Create epics, stories, and links in one session

## Destination-Specific Notes

**Jira:** Creates Epics (type: Epic) and Stories (type: Story/Task). Links dependencies with "is blocked by" / "blocks". Attaches PRD link to each Epic description.

**GitHub:** Creates Milestones (one per epic) and Issues (one per story). Applies labels. References dependencies in issue body as "Blocked by #N".

## What's Next

Once stories are in Jira or GitHub, the team runs sprint planning.
When the feature ships, use `../launch/` to generate all launch artifacts.

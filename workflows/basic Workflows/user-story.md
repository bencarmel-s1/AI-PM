# Template: User Story

## Before you start

**What you need:** A description of the feature or capability you want to write a story for. A one-sentence description is enough to start.

**Optional input:** A PRD, research synthesis, or requirements doc. Reference it as `@prd.md` to give Claude more context.

**Best output:** The more specific you are about the user persona and their goal, the better the acceptance criteria will be. Vague input ("add a dashboard") produces vague stories.

---

## How to use
`Write user stories for [feature description] using @user-story.md`

Or with context: `Write user stories for [feature] using @user-story.md based on the requirements in @prd.md`

---

## User Story: [Feature Name]

### The Story
**As a** [specific user persona — be precise, not generic]
**I want to** [goal or action]
**So that** [benefit or outcome]

---

### Context
**Why this matters:** [1-2 sentences on business/user value]
**Who is affected:** [personas impacted]
**Current workaround:** [what users do today without this]

---

### Acceptance Criteria
*The story is complete when:*

- [ ] [specific, testable criterion]
- [ ] [specific, testable criterion]
- [ ] [specific, testable criterion]
- [ ] [edge case handled]
- [ ] [error state handled]

---

### Out of Scope (v1)
- [thing explicitly NOT included in this story]
- [future enhancement to do later]

### Dependencies
- [design: what's needed from design]
- [engineering: any technical dependencies]
- [data: any tracking/analytics needed]

---

**Priority:** 🔴 High / 🟡 Medium / 🟢 Low
**Effort estimate:** [S / M / L / XL]
**Owner:** [name]

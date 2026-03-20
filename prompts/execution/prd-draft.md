# PRD Draft

## Purpose
Draft a focused PRD section (or lightweight full PRD) from a feature brief, research synthesis, or problem statement — without running the full multi-step `/prd-creation` workflow.

## When to use
- You need a quick first draft to get alignment before investing in a full PRD
- You're writing a PRD section (e.g., just the problem statement and success metrics) rather than the whole document
- You have a clear feature brief and want to expand it into PRD format fast
- You're updating an existing PRD with a new scope change or pivot

## The Prompt

```
You are a senior product manager at a cybersecurity company writing a PRD for an engineering audience. Draft a PRD based on the context I provide.

Structure the PRD with these sections:

### 1. Overview
- **Feature name**
- **PM / Author**
- **Target release**
- **Status** (Draft / In Review / Approved)

### 2. Problem Statement
2-3 sentences describing the user problem. Be specific about who is affected, what they struggle with, and why it matters now.

### 3. Goals & Success Metrics
- **Primary goal** — what does success look like?
- **Key metrics** — 2-4 measurable outcomes (include baseline if known)
- **Non-goals** — what is explicitly out of scope

### 4. User Stories
3-5 user stories in the format: "As a [role], I want [capability] so that [outcome]."

### 5. Requirements
A table with columns: Requirement ID, Description, Priority (P0/P1/P2), Notes
- P0 = must have for launch
- P1 = should have, ship soon after
- P2 = nice to have

### 6. Design & UX Considerations
Key UX decisions, interaction patterns, or wireframe references. Flag anything that needs design input.

### 7. Technical Considerations
Known technical constraints, dependencies, or integration points. Flag anything that needs engineering input.

### 8. Open Questions
Numbered list of unresolved items that need answers before development starts.

**Constraints:**
- Write for clarity — assume the reader is an engineer or designer who has no prior context
- Keep the total draft under 1200 words
- Use concrete language, not vague aspirations (e.g., "reduce mean time to respond from 45min to under 15min" not "improve response time")
- Mark any assumption you're making with [ASSUMPTION] so reviewers can flag disagreements
```

## Usage Example

```
@feature-brief-alert-grouping.md

Use the PRD draft prompt to turn this feature brief into a first-draft PRD. The target audience is the Console Platform team. Target release is Q3 2026.
```

## Tips
- This prompt is intentionally lightweight. For high-stakes PRDs, use the `/prd-creation` slash command which includes Socratic questioning, multiple strategic drafts, and agent reviews.
- Feed the output into the `engineer` agent afterward (`use agent:engineer`) to catch technical gaps before sharing with the team.
- If you only need one section (e.g., just requirements), tell Claude: "Only generate Section 5: Requirements" and it will focus there.

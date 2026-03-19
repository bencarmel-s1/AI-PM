# /launch-pack

Generate a complete launch pack for a feature or release — covering all artifacts needed for sales, CS, engineering, leadership, and customers.

Shipping is not the same as launching. A feature ships when code merges. It launches when sales can pitch it, CS can support it, leadership can report it, and customers can discover it.

## Step 1: Gather inputs

Ask the user:
1. What is the name of the feature or release?
2. What is the target launch date?
3. What is the launch tier?
   - **Major:** New capability, significant scope, broad audience impact — full 6-artifact pack
   - **Minor:** Enhancement or incremental improvement — 3 core artifacts (release notes, CS brief, Slack)
   - **Patch:** Bug fix or maintenance — release notes only

## Step 2: Load the spec and sprint notes

Ask the user: Please @ mention:
1. Your original PRD or feature spec (to compare what was planned vs. shipped)
2. Sprint notes or Jira export (what actually shipped)

If no spec is available, ask the user to describe what shipped.

## Step 3: Readiness check (Phase 1)

Load `@workflows/advanced-workflow/launch/launch-pack-template.md` and `@workflows/company-context/company-context-sentinelone.md`.

Run a pre-launch readiness check:
- Compare PRD vs. what shipped — list any scope deferrals or changes
- Flag any blocking issues (missing docs, unresolved bugs, gaps in enablement)
- Confirm the launch tier based on actual scope

Save as `[feature-name]-launch-readiness.md` and show the user.

Ask: Here is the readiness check. Any changes or blockers to address before generating the pack?

## Step 4: Generate launch artifacts (Phase 2)

Generate all applicable artifacts using the `launch-pack-template.md` structure:

**Major launches (all 6 artifacts):**
1. `[feature-name]-release-notes.md` — Technical release notes: what shipped, what changed, known limitations, rollout notes
2. `[feature-name]-sales-brief.md` — 1-page sales enablement: what it does (customer language), who it's for, key benefits, competitive angle, objection handling
3. `[feature-name]-cs-brief.md` — CS and support enablement: what changed, common questions, how to demo, escalation path, known issues
4. `[feature-name]-exec-announcement.md` — Leadership announcement: what shipped, business impact, what to watch, next milestone
5. `[feature-name]-customer-announcement.md` — External customer comms (for PMM to use in changelog or email): benefit-led, customer language, clear call to action
6. `[feature-name]-slack-announcement.md` — Internal #product-announcements post: short, energizing, links to brief and release notes

**Minor launches (3 core):** Release notes, CS brief, Slack announcement.
**Patch launches (1):** Release notes only.

## Step 5: Executive review gate (Major launches only)

For Major launches, run the `executive` agent to review `[feature-name]-exec-announcement.md`. Ensure it is tight, leadership-ready, and frames business impact clearly.

Incorporate any feedback before finalizing.

## Step 6: Combine and confirm

Bundle all artifacts into `[feature-name]-launch-pack.md` with a table of contents linking each artifact.

Confirm: "Launch pack complete. Files saved: `[feature-name]-launch-readiness.md`, `[feature-name]-launch-pack.md`, and individual artifact files."

**Distribution reminders (you own this):**
- Release notes: Confluence
- Sales brief: Highspot or shared Drive
- CS brief: Confluence + #cs-enablement Slack
- Exec announcement: Email to VP/leadership
- Customer announcement: PMM for changelog
- Slack post: #product-announcements

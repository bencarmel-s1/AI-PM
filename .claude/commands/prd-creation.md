# /prd-creation

Run this command to create a production-ready PRD using a structured, multi-phase workflow: Socratic sharpening, three strategic versions, agent review, final doc.

## Step 1: Gather context

Ask the user:
1. What feature or problem are you writing this PRD for? (1-2 sentences)
2. Which PRD template do you want to use?
   - Carl's Template: best for complex features, detailed technical specs, or when you need a thorough review
   - Lenny's Template: best for smaller features, early-stage ideas, or when you need to move fast
   (If unsure, default to Carl's)
3. Do you have any existing research, data, or context files to include? (@ mention them, or say "none")

## Step 2: Load context

Read the chosen template and supporting files:
- If Carl's: `@workflows/advanced-workflow/prd-creation/Carls-PRD-Template.md`
- If Lenny's: `@workflows/advanced-workflow/prd-creation/Lennys-PRD-Template.md`
- Always load: `@workflows/advanced-workflow/prd-creation/socratic-questioning.md`
- Always load: `@workflows/company-context/company-context-sentinelone.md`
- Load any files the user @ mentioned

## Step 3: Socratic sharpening

Using the five question categories in `socratic-questioning.md` as your guide, ask the user 3-5 targeted questions to sharpen their thinking before drafting anything.

Focus on:
- Problem clarity: Is the problem real and well-defined?
- Solution validation: Why this solution over alternatives?
- Success criteria: How will you know it worked?
- Constraints: What are you explicitly not doing?
- Strategic fit: Why now?

Use AskUserQuestion for this. Do not draft the PRD until you have clear answers.

## Step 4: Confirm strategic angles

Ask the user: I will generate 3 versions of the PRD with different strategic angles. Confirm the angles or customize them:
- Version A (Conservative): Minimal viable approach, lower risk, faster delivery
- Version B (Aggressive): Full vision, maximum user value, higher investment
- Version C (Differentiated): Focused on competitive advantage and defensibility

## Step 5: Generate 3 PRD versions

Using the chosen template and the user's answers, generate three PRD versions reflecting the confirmed strategic angles.

Save each as:
- `[feature-name]-prd-v1.md` (Conservative)
- `[feature-name]-prd-v2.md` (Aggressive)
- `[feature-name]-prd-v3.md` (Differentiated)

## Step 6: User selects a version

Ask: Which version would you like to develop further? (v1, v2, v3, or "combine elements from X and Y")

If combining: merge the specified elements and save as `[feature-name]-prd-combined.md`.

## Step 7: Multi-agent review

Run all three reviews in parallel using the Agent tool:
1. `engineer` agent: technical gaps, implementation risks, missing edge cases, complexity
2. `executive` agent: strategic clarity, executive readiness, investment framing
3. `user-researcher` agent: user insight gaps, unvalidated assumptions, research questions

Consolidate feedback into `[feature-name]-prd-review.md` with a section for each reviewer.

## Step 8: Finalize

Ask: Here is the consolidated review. Which feedback do you want to incorporate?

Incorporate selected feedback and save the final version as `[feature-name]-prd-final.md`.

Confirm: "Your PRD is ready at `[feature-name]-prd-final.md`."

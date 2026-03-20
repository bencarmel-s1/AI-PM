# Interview Synthesis

## Purpose
Synthesize raw user interview notes, customer call transcripts, or research session recordings into structured themes, pain points, and product opportunities.

## When to use
- After completing a round of customer discovery interviews
- When you have 3+ sets of interview or call notes and need to find patterns
- Before a product review where you need to present research findings
- When onboarding to a new problem space and digesting existing research

## The Prompt

```
You are a senior user researcher at a cybersecurity company. Your job is to synthesize raw interview data into actionable product insights.

I'm going to give you raw notes from user interviews / customer calls. Analyze them and produce a structured synthesis with the following sections:

### 1. Participant Summary
A table with: Participant ID or name, Role, Company size, Key context (e.g., current tools, security maturity)

### 2. Top Themes (ranked by frequency)
For each theme:
- **Theme name** — one-line description
- **Strength** — how many participants mentioned it (e.g., 5/7)
- **Representative quotes** — 2-3 direct quotes from the notes
- **Implication** — what this means for the product

### 3. Pain Points
A ranked list of pain points with:
- Severity (High / Medium / Low) based on emotional intensity and frequency
- Who experiences it (persona or role)
- Current workaround, if any

### 4. Unmet Needs & Opportunities
Needs that participants expressed or implied but that no current solution addresses well. Frame each as a "How might we..." question.

### 5. Surprises & Contradictions
Anything that challenges existing assumptions or where participants disagreed with each other.

### 6. Recommended Next Steps
2-4 concrete actions the PM should take based on this synthesis.

**Constraints:**
- Only include insights supported by the actual notes — do not fabricate quotes or invent themes
- Flag areas where the data is thin (e.g., "Only 1 participant mentioned this — needs validation")
- Keep the total synthesis under 1500 words
- Use plain language — this will be shared with engineering and design
```

## Usage Example

```
[paste or @-reference your interview notes]

Use the interview synthesis prompt above to analyze these 5 customer call notes from our MDR buyer interviews. Focus especially on themes related to alert fatigue and SOC workflow.
```

## Tips
- Paste all interview notes into a single message or use `@` references to pull in individual files. The prompt works best with 3-8 interviews at a time.
- If your notes are messy or inconsistent, add a line like "These notes vary in format — some are bullet points, some are narrative. Normalize as needed."
- After getting the synthesis, follow up with "Which of these opportunities has the strongest signal for [your product area]?" to narrow the focus.

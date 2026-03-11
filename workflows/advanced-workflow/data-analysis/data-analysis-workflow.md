# Data Analysis Workflow with Claude Code
*A repeatable AI-assisted process for making confident, data-driven product decisions*

---

## The Core Principle

Data tells you what happened. You decide what to do about it.

Claude reads the data, calculates the metrics, and surfaces the insights. You interpret the findings, make the judgment calls, and own the recommendations. The analysis is collaborative — the decisions are yours.

---

## Before You Start

**Data files:** Export your data as CSV from Mixpanel, Amplitude, or any analytics tool and put the files in the same folder you open Claude Code from.

**`@filename` syntax:** Throughout this workflow, prompts use `@filename.csv` to reference your files. This tells Claude to read that file — you don't need to paste the contents. Just replace the placeholder with your actual filename.

**No setup required:** This workflow needs no sub-agents or configuration. Open Claude Code and start.

---

## The Workflow (3 Phases)

### Phase 1: Discovery — Find the Problem

**Goal:** Use data to identify WHERE the problem is and WHY it's happening.

**What to bring:**
- Funnel or behavioral data (CSV export from Mixpanel, Amplitude, etc.)
- Survey or qualitative data (user responses, support tickets, NPS comments)

**Opening prompt:**
```
I need to find out why [metric] is [stuck/dropping/underperforming].
I have funnel data in @[funnel-data.csv] and survey data in @[survey-data.csv].
Analyze the funnel to find where users drop off, then analyze the survey
to understand why. Create a problem analysis document with your findings.
```

**What Claude will create:**
- Funnel drop-off analysis with completion rates at each step
- Survey theme analysis with % of respondents per theme and sample quotes
- Segmentation by key dimensions (company size, role, plan)
- `[feature]-problem-analysis.md` — shareable with leadership

**Key outputs:**
- The drop-off point (WHERE the problem is)
- The root cause (WHY it's happening)
- The target segment most affected
- A proposed solution

---

### Phase 2: Impact Estimation — Justify Building It

**Goal:** Estimate the business impact before committing engineering resources.

**What to bring:**
- Usage data (CSV with user events, company_size, timestamps)
- Engineering cost estimate
- Your product metrics (ARPU, conversion rate, average LTV)

**Framework:**
```
Impact = Users Affected × Current Action Rate × Expected Lift × Value per Action
```

**Opening prompt:**
```
I want to build the impact model for [feature].
Engineering estimates [X weeks/months] at $[cost].
Our key metrics: ARPU $[X], paying conversion [X]%, avg lifetime [X] months.
Analyze @[usage-data.csv] for current rates, then build a three-scenario
impact model (pessimistic/realistic/optimistic). Save to [feature]-impact-estimate.md.
```

**What Claude will create:**
- Current state metrics from your usage data
- Three-scenario ROI model (pessimistic / realistic / optimistic)
- `[feature]-impact-estimate.md` — the base model
- `[feature]-roi-scenarios.md` — scenario comparison table

**Key outputs:**
- Year 1 ARR impact per scenario
- 3-year LTV value per scenario
- ROI multiple (return / investment)
- Explicit assumptions so leadership can challenge them

**Three Scenarios Approach:**

| Scenario | Adoption | Lift | When to Use |
|----------|----------|------|-------------|
| Pessimistic (20th pct) | Low (30%) | Minimal (+3–5pp) | Floor: is this still worth it? |
| Realistic (50th pct) | Expected (70%) | Conservative (+10–15pp) | Most likely outcome |
| Optimistic (80th pct) | High (90%) | Strong (+15–20pp) | Ceiling: best case |

**Decision rule:** If pessimistic case still returns >2x over 3 years, build it.

---

### Phase 3: Experiment Analysis — Make the Ship/Kill Decision

**Goal:** Analyze A/B test results and make a clear recommendation.

**What to bring:**
- Experiment data CSV (user_id, cohort, primary metric, quality metrics, segments)
- Your target segment definition
- Historical benchmarks (e.g., what good retention looks like)

**Opening prompt:**
```
Our A/B experiment has finished. Analyze @[experiment-results.csv].
Primary metric: [completed_first_task / conversion / retention / etc.]
Target segment: [small teams / enterprise / new users / etc.]
Quality metrics: [week_1_retention / tasks_completed / etc.]
Leading indicators: [invite_rate / template_usage / etc.]

Run the full analysis: topline → segmentation → quality metrics → leading indicators.
Create the experiment readout in [feature]-experiment-readout.md.
```

**What Claude will create:**
- Topline activation/conversion rates for treatment vs control
- Segmented analysis by company size, role, or other dimensions
- Statistical significance (p-values, confidence intervals)
- Quality metrics analysis (retention, engagement)
- Leading indicator analysis (predicts long-term success)
- `[feature]-experiment-readout.md` with clear recommendation

**Key outputs:**
- Ship / iterate / kill recommendation
- Segment-level results (often more important than topline)
- Quality signal (did we activate better users, not just more users?)
- Next steps

**The Analysis Order:**
```
1. Topline results    → Is there a signal at all?
2. Segmentation       → Where is it working? Where isn't it?
3. Quality metrics    → Are these high-quality conversions?
4. Leading indicators → Will the gains hold long-term?
```

**Critical lesson:** Never stop at topline. A modest topline often hides a strong segment win. Always segment by your target customer before making a recommendation.

---

## File Naming Convention

| File | Purpose |
|------|---------|
| `[feature]-problem-analysis.md` | Phase 1 output — problem discovery doc |
| `[feature]-impact-estimate.md` | Phase 2 output — realistic scenario model |
| `[feature]-roi-scenarios.md` | Phase 2 output — three-scenario comparison |
| `[feature]-experiment-readout.md` | Phase 3 output — A/B test analysis and recommendation |

---

## What Your Data Files Should Look Like

**Funnel data (Phase 1):**
```
step, users_entered, users_completed, median_time_minutes
Signup, 10000, 10000, 0
First Task Created, 10000, 7200, 18
First Task Completed, 7200, 2880, 45
```

**Survey data (Phase 1):**
```
user_id, biggest_confusion, feature_request, company_size
user_001, "didn't know what to create first", "templates", 5-20
```

**Usage data (Phase 2):**
```
user_id, event_type, timestamp, company_size, user_role
user_001, signup, 2024-10-01T09:00:00, 5-20, PM
user_001, first_task_created, 2024-10-01T09:18:00, 5-20, PM
```

**Experiment data (Phase 3):**
```
user_id, cohort, company_size, completed_first_task, time_to_first_task_minutes,
invited_teammate, used_feature, days_active_week_1, tasks_completed_week_1
control_001, control, 5-20, False, , False, False, 0, 0
treatment_001, treatment, 5-20, True, 22, True, True, 4, 6
```

---

## Common Prompt Patterns

**Analyze a funnel:**
```
Read @[funnel.csv] and calculate drop-off rates at each step.
Show completion rates, drop-off percentages, and median time per step.
```

**Analyze survey responses:**
```
Read @[survey.csv] and extract the top themes from the [field_name] column.
Count frequency, show % of respondents, and pull 3-4 representative quotes.
Segment by company_size.
```

**Segment experiment results:**
```
Read @[experiment.csv] and calculate activation rate by company_size
for both control and treatment groups. Show lift and indicate significance.
```

**Analyze quality metrics:**
```
Filter @[experiment.csv] to activated users only (completed_first_task = True).
Compare week_1_retention (days_active >= 3) and tasks_completed_week_1
between control and treatment.
```

**Build impact model:**
```
Using these inputs: [signups/month], [current activation rate], [adoption %],
[expected lift], [ARPU], [conversion rate], [avg lifetime months].
Build pessimistic/realistic/optimistic scenarios and calculate Year 1 ARR and 3-year ROI.
```

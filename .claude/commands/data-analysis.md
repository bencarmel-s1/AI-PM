# /data-analysis

Analyze product data — funnel/problem analysis, ROI/impact estimation, or A/B test readout.

## Step 1: Identify the analysis type

Ask the user: What type of analysis do you need?
1. **Funnel / Problem Analysis** — Understand where users are dropping off or what the data says about a product problem
2. **ROI / Impact Estimation** — Estimate the business impact of building a feature before committing resources
3. **A/B Test Readout** — Analyze experiment results and make a ship/iterate/kill recommendation

## Step 2: Get the data

Ask the user: Please @ mention your data file(s). Accepted formats: .csv, .md, or .txt. If you don't have a file, you can paste raw data in your next message.

## Step 3: Load the appropriate template

Based on analysis type:
- **Funnel / Problem:** Read `@workflows/advanced-workflow/data-analysis/problem-analysis-template.md` and `@workflows/advanced-workflow/data-analysis/example-problem-analysis.md`
- **ROI / Impact:** Read `@workflows/advanced-workflow/data-analysis/impact-estimation-framework.md` and `@workflows/advanced-workflow/data-analysis/example-impact-estimate.md`
- **A/B Test:** Read `@workflows/advanced-workflow/data-analysis/experiment-readout-template.md` and `@workflows/advanced-workflow/data-analysis/example-experiment-readout.md`

Also load: `@workflows/company-context/company-context-sentinelone.md` for business context.

## Analysis: Funnel / Problem

Following the problem analysis template:
1. **Funnel completion rates** — Calculate completion rate and drop-off rate for each step
2. **Drop-off analysis** — Identify the biggest single drop-off point and quantify it
3. **Segmentation** — Break down by key dimensions in the data (company size, user role, cohort, etc.)
4. **Root cause hypotheses** — Generate 3-5 hypotheses for the biggest drop-off with supporting evidence
5. **Recommended next step** — What to investigate or build based on the data

Save output as `[feature]-problem-analysis.md`.

## Analysis: ROI / Impact Estimation

Following the impact estimation framework:

Formula: Impact = Users Affected x Current Action Rate x Expected Lift x Value per Action

1. **Define the numerics** — Extract or estimate each variable from the data and context
2. **Three scenarios:** Pessimistic (20th percentile), Realistic (50th percentile), Optimistic (80th percentile)
3. **Key outputs per scenario:** Year 1 ARR impact, 3-year LTV, ROI multiple
4. **Explicit assumptions** — List every assumption made and its confidence level
5. **Decision rule:** If pessimistic case returns more than 2x over 3 years, recommend building

Save output as `[feature]-impact-estimate.md`.

## Analysis: A/B Test Readout

Following the experiment readout template:
1. **Topline results** — Primary metric movement, statistical significance (p-value, confidence interval), sample size
2. **Segmentation** — Break results by key dimensions; flag segments that diverge significantly from topline
3. **Quality metrics** — Check for novelty effects, guardrail metric violations, data quality issues
4. **Leading indicators** — Secondary metrics that predict long-term impact
5. **Recommendation:** Ship / Iterate / Kill — with clear rationale
6. **If Iterate:** Specify what to change and what to re-test

Save output as `[feature]-experiment-readout.md`.

## Completion

Confirm: "Analysis complete. Output saved to `[filename]`."

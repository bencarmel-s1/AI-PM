# Autoresearch Program: Standup Skill

## Goal
Improve the standup skill at `../SKILL.md` to maximize the average score from `eval.py`.
Target: **90+/100** average across all three scenarios.

## Rules — Read These First

1. **Only modify `../SKILL.md`** — never touch `eval.py`, `rubric.md`, or `mock_input.md`
2. Each iteration: run eval → read score + breakdown → form one hypothesis → modify SKILL.md → run eval again
3. If score improves: commit with message `autoresearch: score {old}→{new} ({what changed})`
4. If score drops or is unchanged: `git checkout ../SKILL.md` to revert, try a different hypothesis
5. Stop when average score ≥ 90 or after 15 iterations (whichever comes first)
6. Keep a running log of hypotheses tried in `autoresearch_log.md` (create it if it doesn't exist)

## What You Can Change in SKILL.md

- Instruction clarity (make steps more explicit)
- Output format specification (add examples, tighten structure)
- Cross-source connection instructions (step 5 synthesis)
- People file usage guidance (step 3)
- Gmail filtering rules (step 4 noise handling)
- Conciseness guidance (word count target, what to omit)

## What You Must NOT Change

- The data sources table (tools are fixed)
- The section names in the output format (headings are part of the eval)
- The overall 5-step flow (gather → Jira → Calendar → Gmail → synthesize)

## Scoring Breakdown Reference

To understand what each criterion checks, read `rubric.md`. Focus improvements on:

- **C3** (People context): Is the skill explicit enough about what "actionable tip" means?
- **C7** (Synthetic focus): Does the skill require cross-source synthesis explicitly?
- **C10** (Cross-source connection): Does the skill explicitly instruct connecting meetings to tickets?
- **C8** (Conciseness): Does the skill give a word count target or "what to omit" guidance?

## How to Run the Eval

```bash
cd .claude/skills/standup/eval
python eval.py             # score all 3 scenarios
python eval.py --verbose   # also print generated outputs
python eval.py --scenario A  # test one scenario only
```

## Starting Baseline

Before making any changes, run `eval.py` once to record the baseline score.
Write it in `autoresearch_log.md` as `Baseline: {score}/100`.

## Commit Format

```
autoresearch: score 67→74 (added explicit cross-source connection instruction in step 5)
```

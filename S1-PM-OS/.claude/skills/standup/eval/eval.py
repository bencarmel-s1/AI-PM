#!/usr/bin/env python3
"""
Standup skill eval harness.

Runs SKILL.md against 3 mock scenarios, scores each output against rubric.md,
and prints a total score (0-100) + per-criterion breakdown.

Usage:
    python eval.py                    # score current SKILL.md
    python eval.py --verbose          # show generated outputs too
    python eval.py --scenario A       # run single scenario

DO NOT MODIFY THIS FILE. It is the immutable eval harness.
"""

import argparse
import re
import sys
from pathlib import Path

import anthropic

SKILL_PATH = Path(__file__).parent.parent / "SKILL.md"
MOCK_INPUT_PATH = Path(__file__).parent / "mock_input.md"
RUBRIC_PATH = Path(__file__).parent / "rubric.md"


def load_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def generate_standup(client: anthropic.Anthropic, skill: str, scenario_text: str) -> str:
    prompt = f"""You are a PM assistant following these skill instructions exactly:

---SKILL INSTRUCTIONS START---
{skill}
---SKILL INSTRUCTIONS END---

The following is mock data representing a real day's inputs. Treat it as if it came from live tools (Calendar, Gmail, Jira). Generate the standup output as instructed.

---MOCK DATA START---
{scenario_text}
---MOCK DATA END---

Generate the standup output now. Follow the format and instructions in the skill exactly."""

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text


def extract_scenario(mock_input: str, label: str) -> str:
    """Extract a single scenario block (A, B, or C) from the mock input file."""
    pattern = rf"## Scenario {label}:.*?(?=## Scenario [A-Z]:|$)"
    match = re.search(pattern, mock_input, re.DOTALL)
    if not match:
        raise ValueError(f"Scenario {label} not found in mock_input.md")
    return match.group(0).strip()


def score_output(output: str, scenario_label: str) -> dict[str, int]:
    """
    Score a standup output against the rubric criteria.
    Returns dict of criterion -> score (0, 5, 7, or 10).
    """
    scores = {}
    text = output.lower()
    word_count = len(output.split())

    # C1 — Date header
    if re.search(r"##\s+standup\s+[—–-]\s+\d{4}", output, re.IGNORECASE) or \
       re.search(r"##\s+standup\s+[—–-]\s+\w", output, re.IGNORECASE):
        scores["C1_date_header"] = 10
    else:
        scores["C1_date_header"] = 0

    # C2 — Schedule section
    if re.search(r"###.*schedule|###.*today", output, re.IGNORECASE):
        # Check it has at least one entry (a time or a dash after the heading)
        schedule_match = re.search(
            r"###.*(?:schedule|today).*?\n(.*?)(?=###|\Z)", output, re.DOTALL | re.IGNORECASE
        )
        if schedule_match and schedule_match.group(1).strip():
            scores["C2_schedule"] = 10
        else:
            scores["C2_schedule"] = 5
    else:
        scores["C2_schedule"] = 0

    # C3 — People file context (scenarios A and C have known stakeholders)
    known_stakeholders = ["ervin", "luko", "petr", "warwick"]
    has_stakeholder = any(s in text for s in known_stakeholders)
    if has_stakeholder:
        has_context_line = bool(re.search(r"context:|tip:|insight:|communication|cares about|prefers", text))
        actionable_tip = bool(re.search(r"make sure|focus on|bring|avoid|prepare|mention|note that", text))
        if has_context_line and actionable_tip:
            scores["C3_people_context"] = 10
        elif has_context_line:
            scores["C3_people_context"] = 5
        else:
            scores["C3_people_context"] = 0
    else:
        scores["C3_people_context"] = 10  # N/A, no known stakeholders in scenario B light day... actually B has none

    # C4 — Gmail signals section, noise filtered
    has_gmail_section = bool(re.search(r"###.*(?:signal|gmail|email|inbox)", output, re.IGNORECASE))
    has_noise = bool(re.search(r"product.?hunt|newsletter|build fail|noreply@github", text))
    if has_gmail_section and not has_noise:
        scores["C4_gmail"] = 10
    elif has_gmail_section:
        scores["C4_gmail"] = 5
    else:
        scores["C4_gmail"] = 0

    # C5 — Jira section with ticket keys
    has_jira_section = bool(re.search(r"###.*(?:jira|in progress|progress|ticket)", output, re.IGNORECASE))
    has_ticket_keys = bool(re.search(r"WAY-\d+", output, re.IGNORECASE))
    if has_jira_section and has_ticket_keys:
        scores["C5_jira"] = 10
    elif has_jira_section:
        scores["C5_jira"] = 5
    else:
        scores["C5_jira"] = 0

    # C6 — Blockers surfaced (critical for scenario C, N/A for A and B)
    if scenario_label == "C":
        has_blocker_section = bool(re.search(r"###.*blocker|blocked", output, re.IGNORECASE))
        names_blocker = bool(re.search(r"WAY-1189|WAY-1055|api contract|demo env", text))
        suggests_action = bool(re.search(r"need|decision|resolve|unblock|priority|address", text))
        if has_blocker_section and names_blocker and suggests_action:
            scores["C6_blockers"] = 10
        elif has_blocker_section and names_blocker:
            scores["C6_blockers"] = 5
        else:
            scores["C6_blockers"] = 0
    else:
        scores["C6_blockers"] = 10  # N/A

    # C7 — Suggested Focus is synthetic
    has_focus = bool(re.search(r"###.*(?:focus|priority|today|suggested)", output, re.IGNORECASE))
    focus_match = re.search(
        r"###.*(?:focus|priority|today|suggested).*?\n(.*?)(?=###|\Z)", output, re.DOTALL | re.IGNORECASE
    )
    if has_focus and focus_match:
        focus_text = focus_match.group(1).lower()
        references_goal = bool(re.search(r"okr|q2|fedramp|beta|launch|goal|objective", focus_text))
        references_ticket = bool(re.search(r"WAY-\d+", focus_match.group(1)))
        references_meeting = bool(re.search(r"1:1|sync|call|meeting|with \w+", focus_text))
        source_count = sum([references_goal, references_ticket, references_meeting])
        if source_count >= 2:
            scores["C7_synthetic_focus"] = 10
        elif source_count == 1:
            scores["C7_synthetic_focus"] = 5
        else:
            scores["C7_synthetic_focus"] = 0
    else:
        scores["C7_synthetic_focus"] = 0

    # C8 — Conciseness
    if word_count < 350:
        scores["C8_conciseness"] = 10
    elif word_count < 450:
        scores["C8_conciseness"] = 7
    elif word_count < 600:
        scores["C8_conciseness"] = 3
    else:
        scores["C8_conciseness"] = 0

    # C9 — Graceful fallbacks (check that empty sections have a message)
    missing_section = False
    for section in ["schedule", "signal", "progress", "focus"]:
        if not re.search(rf"###.*{section}", output, re.IGNORECASE):
            missing_section = True
            break
    has_fallback_language = bool(re.search(
        r"no urgent|not available|calendar not|none found|nothing|no items|unavailable", text
    ))
    if not missing_section:
        scores["C9_fallbacks"] = 10
    elif has_fallback_language:
        scores["C9_fallbacks"] = 5
    else:
        scores["C9_fallbacks"] = 0

    # C10 — Cross-source connection
    # Look for language that explicitly links a meeting + ticket, or email + ticket
    connections = [
        r"(1:1|sync|call|meeting).*WAY-\d+",
        r"WAY-\d+.*(1:1|sync|call|meeting)",
        r"(ervin|luko|warwick|petr).*WAY-\d+",
        r"WAY-\d+.*(ervin|luko|warwick|petr)",
        r"(email|gmail|from).*WAY-\d+",
        r"WAY-\d+.*(email|gmail|related)",
        r"blocking.*meeting|meeting.*blocked",
        r"discuss.*WAY-\d+|WAY-\d+.*discuss",
    ]
    explicit_connection = any(re.search(p, text, re.DOTALL) for p in connections)
    implied_connection = bool(re.search(r"related|connected|ties to|aligned with|which is", text))
    if explicit_connection:
        scores["C10_cross_source"] = 10
    elif implied_connection:
        scores["C10_cross_source"] = 5
    else:
        scores["C10_cross_source"] = 0

    return scores


def run_eval(scenarios: list[str], verbose: bool = False) -> dict:
    client = anthropic.Anthropic()
    mock_input = load_file(MOCK_INPUT_PATH)
    skill = load_file(SKILL_PATH)

    all_scores = []
    results = {}

    for label in scenarios:
        scenario_text = extract_scenario(mock_input, label)
        print(f"\n{'='*50}")
        print(f"Running Scenario {label}...")
        output = generate_standup(client, skill, scenario_text)

        if verbose:
            print(f"\n--- Generated Output ---\n{output}\n--- End Output ---\n")

        scores = score_output(output, label)
        total = sum(scores.values())
        all_scores.append(total)
        results[label] = {"scores": scores, "total": total, "output": output}

        print(f"Scenario {label} score: {total}/100")
        for criterion, score in scores.items():
            status = "✓" if score == 10 else ("~" if score > 0 else "✗")
            print(f"  {status} {criterion}: {score}/10")

    avg = sum(all_scores) / len(all_scores)
    print(f"\n{'='*50}")
    print(f"AVERAGE SCORE: {avg:.1f}/100  (across {len(scenarios)} scenarios)")
    print(f"{'='*50}\n")

    return {"average": avg, "scenarios": results}


def main():
    parser = argparse.ArgumentParser(description="Eval standup SKILL.md")
    parser.add_argument("--verbose", action="store_true", help="Show generated outputs")
    parser.add_argument("--scenario", choices=["A", "B", "C"], help="Run single scenario")
    args = parser.parse_args()

    scenarios = [args.scenario] if args.scenario else ["A", "B", "C"]
    result = run_eval(scenarios, verbose=args.verbose)

    # Exit with score as integer for shell scripting
    sys.exit(0 if result["average"] >= 70 else 1)


if __name__ == "__main__":
    main()

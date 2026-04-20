#!/usr/bin/env python3
"""
Model Advisor Hook — UserPromptSubmit
Scores incoming prompt complexity, prints a visible educational block to stderr,
and injects a minimal hint into Claude's context (stdout).
Stays silent on ambiguous prompts to avoid noise.
"""

import json
import sys
import re

COMPLEX_KEYWORDS = [
    "analyze", "analyse", "synthesize", "synthesise", "plan", "compare",
    "research", "write", "review", "strategy", "prioritize", "prioritise",
    "design", "architect", "evaluate", "assess", "investigate", "diagnose",
    "proposal", "draft", "spec", "roadmap", "tradeoff", "tradeoffs",
]

SIMPLE_KEYWORDS = [
    "what is", "what's", "how do", "how does", "quick", "summarize",
    "list", "show me", "find", "look up", "remind", "tell me", "define",
    "when", "who", "where", "translate",
]

COMPLEX_WORD_THRESHOLD = 40


def score_prompt(prompt: str):
    """Returns (verdict, triggered_keywords). verdict: 'simple', 'complex', or 'ambiguous'."""
    lower = prompt.lower()
    words = re.findall(r"\w+", lower)
    word_count = len(words)

    complex_hits = [kw for kw in COMPLEX_KEYWORDS if kw in lower]
    simple_hits = [kw for kw in SIMPLE_KEYWORDS if kw in lower]

    if len(complex_hits) >= 2 or (len(complex_hits) >= 1 and word_count >= COMPLEX_WORD_THRESHOLD):
        return "complex", complex_hits

    if simple_hits and not complex_hits and word_count < COMPLEX_WORD_THRESHOLD:
        return "simple", simple_hits

    return "ambiguous", []


def print_advisory(verdict: str, triggered: list):
    sep = "─" * 41
    keywords = ", ".join(f'"{k}"' for k in triggered[:4])

    if verdict == "simple":
        lines = [
            sep,
            "⚡ MODEL ADVISOR — Simple task",
            f"   Triggered by: {keywords}",
            "   Current model: Sonnet (fine for this)",
            "   🪙 Cheaper option: claude-lite (Haiku) saves ~85% cost",
            "   Why Haiku? Short Q&A needs no deep reasoning — Haiku handles it well.",
            sep,
        ]
    else:
        lines = [
            sep,
            "🧠 MODEL ADVISOR — Complex task",
            f"   Triggered by: {keywords}",
            "   Current model: Sonnet (appropriate)",
            "   🚀 Max quality option: claude-deep (Opus) for critical decisions",
            "   Why Opus? Multi-step reasoning and strategy work benefit from",
            "             Opus's deeper thinking.",
            sep,
        ]

    print("\n".join(lines), file=sys.stderr)


def main():
    raw = sys.stdin.read()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        sys.exit(0)

    prompt = data.get("prompt", "")
    if not prompt:
        sys.exit(0)

    verdict, triggered = score_prompt(prompt)

    if verdict == "ambiguous":
        sys.exit(0)

    # Visible educational block in terminal
    print_advisory(verdict, triggered)

    # Minimal context injection (keeps context window cost low, ~15 tokens)
    hint = "simple task — Haiku available via claude-lite" if verdict == "simple" \
        else "complex task — Opus available via claude-deep"
    output = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": f"MODEL HINT: {hint}.",
        }
    }
    json.dump(output, sys.stdout)
    sys.exit(0)


if __name__ == "__main__":
    main()

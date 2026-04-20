# Template: Hooks & Automation for PMs

## Before you start

**What you need:** Access to your project's `.claude/settings.json` file (or your global `settings.json`). A text editor to add hook configurations. No coding experience required — hooks are copy-paste JSON blocks.

**Optional input:** If you already have specific workflows you repeat manually (e.g. reviewing PRDs, formatting docs), note them down. This guide gives you four ready-made recipes, but the pattern applies to any repetitive step.

**Context:** Claude Code hooks are a built-in automation layer. They let you attach shell commands that run automatically before or after Claude uses a tool (like writing a file or running a command). Think of them as "if this happens, then also do that" rules that live in your project config.

---

## How to use

Read through the recipes below and copy any that fit your workflow into your `.claude/settings.json` file. Then use Claude Code normally — the hooks fire automatically when their trigger conditions are met.

---

## How hooks work

Hooks follow a simple lifecycle:

1. **Event fires** — Claude is about to use a tool (e.g. write a file) or just finished using one.
2. **Your shell command runs** — A script or command you defined executes automatically.
3. **Output feeds back to Claude** — Whatever your command prints to stdout becomes context Claude can see and act on.

Hooks are defined in your `.claude/settings.json` file (project-level) or your global settings. Each hook specifies:
- **`event`** — When to fire: `PreToolUse` (before a tool runs) or `PostToolUse` (after a tool runs).
- **`matcher`** — Which tool to watch (e.g. `write_file`, `execute_command`). Leave empty to match all tools.
- **`command`** — The shell command to execute when the hook fires.

The command receives details about the tool call via stdin as JSON, so your script can inspect filenames, content, and other context to decide what to do.

---

## Recipe 1: Auto-run engineer agent review on spec edits

**What it does:** After any file write to a PRD or spec file, automatically triggers the engineer agent to review the document for technical gaps and feasibility concerns.

**When to use it:** When you're iterating on specs and want continuous engineering-perspective feedback without remembering to ask for it.

**Hook configuration:**

```json
{
  "hooks": [
    {
      "event": "PostToolUse",
      "matcher": "write_file",
      "command": "filepath=$(cat - | python3 -c \"import sys,json; print(json.load(sys.stdin)['tool_input']['file_path'])\") && case \"$filepath\" in *-prd-*.md|*-spec-*.md) echo \"[Hook] Spec file written: $filepath — Run engineer agent review. Use agent:engineer to review this document for technical feasibility, missing edge cases, and implementation risks. Focus on: API assumptions, data model gaps, and integration dependencies.\";; *) ;; esac"
    }
  ]
}
```

**Example trigger scenario:**
You're working on a PRD and say: `Write the updated requirements to mobile-prd-v2.md`. Claude writes the file. The hook detects the filename matches `*-prd-*.md`, and prints a review instruction. Claude sees that output and automatically kicks off an engineer agent review of the document — no extra prompt from you.

---

## Recipe 2: Enforce PRD template compliance

**What it does:** Before completing a PRD workflow, checks that required sections (Problem Statement, Success Metrics, Scope, etc.) are present in the output file.

**When to use it:** When you want a safety net ensuring no critical PRD section gets skipped, especially during fast-moving sessions where you might forget to check.

**Hook configuration:**

```json
{
  "hooks": [
    {
      "event": "PostToolUse",
      "matcher": "write_file",
      "command": "filepath=$(cat - | python3 -c \"import sys,json; print(json.load(sys.stdin)['tool_input']['file_path'])\") && case \"$filepath\" in *-prd-*.md) missing=\"\"; for section in \"Problem Statement\" \"Success Metrics\" \"Scope\" \"User Stories\" \"Requirements\" \"Open Questions\"; do grep -qi \"$section\" \"$filepath\" || missing=\"$missing\\n- $section\"; done; if [ -n \"$missing\" ]; then echo \"[Hook] PRD compliance check FAILED. Missing required sections:$missing\"; echo \"Please add these sections before finalizing.\"; else echo \"[Hook] PRD compliance check passed. All required sections present.\"; fi;; *) ;; esac"
    }
  ]
}
```

**Example trigger scenario:**
You finish drafting a PRD and say: `Save this as analytics-prd-final.md`. Claude writes the file. The hook scans it for required section headings. If "Success Metrics" is missing, Claude sees the failure message and prompts you: "The PRD is missing a Success Metrics section. Want me to add one based on the goals we discussed?"

---

## Recipe 3: Auto-format markdown outputs

**What it does:** After writing any `.md` file, runs a formatting check to flag inconsistent heading levels, broken link syntax, and malformed tables.

**When to use it:** When you want every markdown file Claude produces to be clean and consistent without manually reviewing formatting.

**Hook configuration:**

```json
{
  "hooks": [
    {
      "event": "PostToolUse",
      "matcher": "write_file",
      "command": "filepath=$(cat - | python3 -c \"import sys,json; print(json.load(sys.stdin)['tool_input']['file_path'])\") && case \"$filepath\" in *.md) issues=\"\"; if grep -Pn '^#{4,}' \"$filepath\" > /dev/null 2>&1; then issues=\"$issues\\n- Deep heading nesting detected (h4+). Consider simplifying to h1-h3.\"; fi; if grep -Pn '\\[.*\\]\\([^)]*$' \"$filepath\" > /dev/null 2>&1; then issues=\"$issues\\n- Possible broken link syntax (unclosed parenthesis).\"; fi; if grep -Pn '^\\|.*[^|]$' \"$filepath\" > /dev/null 2>&1; then issues=\"$issues\\n- Table row may be missing trailing pipe character.\"; fi; if [ -n \"$issues\" ]; then echo \"[Hook] Markdown formatting issues found in $filepath:$issues\"; echo \"Please fix these formatting issues.\"; else echo \"[Hook] Markdown formatting check passed for $filepath.\"; fi;; *) ;; esac"
    }
  ]
}
```

**Example trigger scenario:**
You ask Claude to write a competitive analysis to `competitor-review.md`. After saving, the hook scans the file and finds a table row missing a trailing pipe. Claude sees the warning and automatically fixes the table formatting before you even notice the issue.

---

## Recipe 4: Validate required sections before PRD completion

**What it does:** Before the final save of a PRD, verifies that all required sections from the template are present and non-empty (not just headings with no content beneath them).

**When to use it:** When you're about to finalize a PRD and want to catch placeholder or stub sections that were never filled in — a stricter check than Recipe 2.

**Hook configuration:**

```json
{
  "hooks": [
    {
      "event": "PreToolUse",
      "matcher": "write_file",
      "command": "input=$(cat -) && filepath=$(echo \"$input\" | python3 -c \"import sys,json; print(json.load(sys.stdin)['tool_input']['file_path'])\") && content=$(echo \"$input\" | python3 -c \"import sys,json; print(json.load(sys.stdin)['tool_input']['content'])\") && case \"$filepath\" in *-prd-final*.md|*-prd-v[0-9]*.md) sections=(\"Problem Statement\" \"Success Metrics\" \"Scope\" \"User Stories\" \"Requirements\" \"Open Questions\"); empty=\"\"; for section in \"${sections[@]}\"; do header=$(echo \"$content\" | grep -in \"$section\" | head -1); if [ -z \"$header\" ]; then empty=\"$empty\\n- $section (missing entirely)\"; else linenum=$(echo \"$header\" | cut -d: -f1); next_content=$(echo \"$content\" | tail -n +$((linenum+1)) | head -5 | grep -v '^#' | grep -v '^$' | head -1); if [ -z \"$next_content\" ]; then empty=\"$empty\\n- $section (heading exists but no content)\"; fi; fi; done; if [ -n \"$empty\" ]; then echo \"[Hook] PRD validation FAILED. These sections need content before saving:$empty\"; echo \"Please fill in the empty sections before finalizing this PRD.\"; else echo \"[Hook] PRD validation passed. All required sections have content.\"; fi;; *) ;; esac"
    }
  ]
}
```

**Example trigger scenario:**
You say: `Save the final version as onboarding-prd-final.md`. Before Claude writes the file, the hook inspects the content that's about to be saved. It finds that "User Stories" has a heading but no content beneath it. Claude sees the validation failure and says: "The User Stories section is empty. Let me draft user stories based on the personas we discussed before saving."

---

## Tips

**When hooks help vs. when they add friction:**
- Hooks shine for checks you always forget (missing sections, formatting) and for automating a second-pass review you'd do manually anyway.
- Hooks add friction when they fire too often on files you don't care about, or when they slow down exploratory work where you're drafting rough ideas. Start with one or two hooks and add more only after you've confirmed the first ones save you time.

**Keep hooks lightweight:**
- Hook commands should run in under a second. Heavy operations (API calls, large file parsing) will make every file write feel sluggish.
- Use filename pattern matching (the `case` statement) early in your command to bail out fast on files that don't match.
- Print clear, actionable output — Claude acts on what your hook prints, so vague messages produce vague responses.

**Debugging hook failures:**
- If a hook isn't firing, check that the `event` and `matcher` values are exact. `write_file` is not the same as `WriteFile` or `file_write`.
- Test your shell command outside of Claude Code first by piping in sample JSON: `echo '{"tool_input":{"file_path":"test-prd-v1.md"}}' | your-command-here`.
- Check `.claude/settings.json` for JSON syntax errors (missing commas, unescaped quotes). A malformed settings file silently disables all hooks.
- If a hook runs but Claude ignores the output, make your message more directive. Instead of "FYI: section missing," write "Please add the missing section before proceeding."

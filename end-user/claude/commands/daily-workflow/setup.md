# Daily Workspace Setup

You are helping a developer set up their daily workflow. Walk them through creating an optimal terminal workspace.

## 1. Check Current Location

Note whether you're in a git repository or a general location. This affects recommendations.

## 2. Recommended Terminal Layout

Present this setup:

```
Terminal Setup for Today
=========================

1. GENERAL CHAT (this terminal, or create new)
   - Rename: general
   - Purpose: Quick questions, lookups, misc tasks
   - Command: claude

2. FOCUS (primary work driver)
   - Rename: focus
   - Purpose: Main task execution, stays on one objective
   - Command: claude
   - Tip: Use /start to load project context

3. BACKGROUND RUNNER (if in a git repo with dev server)
   - Rename: runner
   - Purpose: Dev servers, watchers, build processes
   - Command: claude then /background-runner
```

## 3. Optional Support Terminals

Ask if they want any of these based on today's work:

| Terminal | Rename To | Purpose |
|----------|-----------|---------|
| Research | research | Exploring docs, APIs, unfamiliar code |
| Review | review | Code review, PR feedback, security audits |
| Debug | debug | Dedicated troubleshooting with logs/traces |
| Refactor | refactor | Isolated cleanup work |

Suggest: "Most days you only need general + focus + runner. Add others on-demand."

## 4. Quick Setup Commands

For Windows Terminal / PowerShell, provide these:

```powershell
# Rename current terminal tab (if supported)
$Host.UI.RawUI.WindowTitle = "general"

# Or just tell them to right-click the tab to rename
```

## 5. Planning Check

Ask: "Do you want to check your /planner before starting? It shows your current goals and priorities."

## 6. Wrap Up

Once they've set up their terminals:
- Remind them to use /start in their focus terminal to load project context
- Suggest using /planner if they haven't reviewed their goals recently
- Wish them a productive session

## Tone

Efficient and helpful. Don't over-explain - they know their workflow, you're just helping them get organized quickly.

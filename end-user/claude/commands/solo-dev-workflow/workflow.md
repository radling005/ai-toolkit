---
description: Show workflow system overview and all commands
---

# Solo Developer Workflow System

You are helping a solo developer who uses this workflow system to stay organized and maintain quality. Display this overview when requested.

## Available Commands

| Command | Purpose |
|---------|---------|
| `/workflow` | Show this overview |
| `/start` | Begin a session - checks setup, shows current focus |
| `/prd` | Create or update the Product Requirements Document |
| `/claude-init` | Create or update the project's CLAUDE.md |
| `/idea [description]` | Quickly capture an idea without losing focus |
| `/review` | Pre-commit checklist - run before committing code |
| `/ship` | Pre-release checklist - run before releasing |
| `/close` | End session - summarize work, update tracking |

## Typical Session Flow

```
/start          → See what's active, pick focus
  ↓
[do work]       → Use /idea to capture stray thoughts
  ↓
/review         → Before committing
  ↓
/close          → Wrap up, update docs
```

## Project Structure

This workflow expects these files in each project:

```
<project>/
  CLAUDE.md              # Agent instructions for this project
  docs/
    PRD.md               # Product requirements
    backlog.md           # Ideas and future work
    active.md            # Current focus (1-3 items)
    decisions.md         # Architecture decision records
    standards.md         # Code and UX standards
    sessions.md          # Running log of work sessions
```

## First Time Setup

For a new project, run these in order:
1. `/prd` - Define what you're building
2. `/claude-init` - Set up agent context
3. `/start` - Begin your first session

## Philosophy

- **Limited tools, deep usage** - 8 commands that cover the full dev cycle
- **Capture, don't context-switch** - Use `/idea` to save thoughts without derailing
- **Checklists over memory** - `/review` and `/ship` ensure nothing slips through
- **Clean sessions** - Start fresh with `/start`, close clean with `/close`
- **Session history** - Every `/close` logs to `sessions.md` so you can look back at progress

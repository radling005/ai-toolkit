# Daily Workflow Commands

Commands for managing your daily work routine across all projects. These complement the project-specific solo-dev-workflow commands.

## What's Included

| Command | Purpose |
|---------|---------|
| `/setup` | Start of day - set up terminal workspace |
| `/end-day` | End of day - 30-min wrap-up routine |
| `/planner` | Life/work planner - manage goals across time horizons |

## Relationship to Solo Dev Workflow

- **solo-dev-workflow** = Project-specific (/start, /close operate within a project)
- **daily-workflow** = Cross-project (/setup, /end-day operate across your whole day)

## Installation

Copy all `.md` files (except this README) to your global commands folder:

```bash
# Windows (PowerShell)
Copy-Item *.md -Exclude README.md -Destination "$env:USERPROFILE\.claude\commands\"

# macOS/Linux
cp *.md ~/.claude/commands/
```

## Planning Directory

The `/planner` command expects a `~/planning/` directory with these files:

```
planning/
  today.md      # Daily focus and tasks
  week.md       # Weekly goals and priorities
  month.md      # Monthly objectives
  quarter.md    # Quarterly themes and milestones
  someday.md    # Ideas, dreams, long-term backlog
  notes.md      # Running notes, context, reflections
```

The planner will offer to create this structure if it doesn't exist.

## Typical Day

```
/setup            → Set up terminals for the day
/planner          → Review goals, set today's focus
  ↓
/start            → Begin project session (in focus terminal)
[work]
/close            → End project session
  ↓
/end-day          → Wrap up entire day, prep tomorrow
```

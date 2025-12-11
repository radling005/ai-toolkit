# Solo Developer Workflow

A complete workflow system for solo developers using Claude Code. Provides consistent session management, idea capture, quality checklists, and progress tracking.

## What's Included

| Command | Purpose |
|---------|---------|
| `/workflow` | Show system overview and all commands |
| `/start` | Begin a session - loads project context, shows focus |
| `/prd` | Create or update Product Requirements Document |
| `/claude-init` | Create or update project CLAUDE.md |
| `/idea` | Quick-capture ideas without losing focus |
| `/review` | Pre-commit quality checklist |
| `/ship` | Pre-release checklist |
| `/close` | End session - logs work to sessions.md |

## Installation

Copy all `.md` files (except this README) to your global commands folder:

```bash
# Windows (PowerShell)
Copy-Item *.md -Exclude README.md -Destination "$env:USERPROFILE\.claude\commands\"

# macOS/Linux
cp *.md ~/.claude/commands/
rm ~/.claude/commands/README.md  # if copied
```

Or for project-specific installation:
```bash
cp *.md <your-project>/.claude/commands/
```

## Usage

### First Time (New Project)

```
/prd              → Define what you're building
/claude-init      → Set up agent context
/start            → Begin your first session
```

### Every Session

```
/start            → Load context, see focus, pick task
[work]            → Use /idea to capture stray thoughts
/review           → Before committing
/close            → Log session, update tracking
/clear            → Fresh context for next session
```

### When Releasing

```
/ship             → Full pre-release checklist
```

## Project Structure Created

After setup, your project will have:

```
your-project/
  CLAUDE.md              # Agent context (created by /claude-init)
  docs/
    PRD.md               # Product requirements (created by /prd)
    backlog.md           # Ideas captured via /idea
    active.md            # Current focus items
    decisions.md         # Architecture decisions
    standards.md         # Code/UX standards
    sessions.md          # Running log of work sessions
```

## Philosophy

- **Limited tools, deep usage** - 8 commands covering the full dev cycle
- **Capture, don't context-switch** - `/idea` saves thoughts without derailing
- **Checklists over memory** - `/review` and `/ship` ensure nothing slips
- **Clean sessions** - Start fresh, close clean
- **Session history** - Every `/close` logs progress for future reference

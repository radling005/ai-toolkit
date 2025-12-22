# Utility Commands

Standalone utility commands for project maintenance, auditing, and meta-operations.

## What's Included

| Command | Purpose |
|---------|---------|
| `/sync-docs` | Weekly documentation maintenance and sync |
| `/ai-readiness` | Audit project for AI collaboration effectiveness |
| `/make-background-runner` | Generate project-specific dev server runner |
| `/claude-ideas` | Manage global ideas capture file |
| `/claude-global-assessor` | Assess your global Claude Code configuration |

## Installation

Copy desired commands to your global commands folder:

```bash
# Windows (PowerShell)
Copy-Item *.md -Exclude README.md -Destination "$env:USERPROFILE\.claude\commands\"

# macOS/Linux
cp *.md ~/.claude/commands/
```

## Command Details

### /sync-docs
Run weekly to keep project documentation accurate:
- Verifies docs match codebase reality
- Archives old session entries
- Updates stale metrics
- Flags inconsistencies for review

### /ai-readiness
Run on any project to assess AI collaboration readiness:
- Checks for CLAUDE.md, README, docs structure
- Evaluates command documentation
- Identifies gaps that hurt AI effectiveness
- Provides prioritized improvement suggestions

### /make-background-runner
Run in a project to generate a custom `/background-runner` command:
- Detects project stack (Node, Python, Docker, etc.)
- Identifies dev server commands and ports
- Creates `.claude/commands/background-runner.md`
- Handles platform-specific quirks (Windows issues, etc.)

### /claude-ideas
Quick idea capture for Claude improvements:
- `/claude-ideas show` - Display captured ideas
- `/claude-ideas [text]` - Capture a new idea with timestamp

Ideas stored in `~/.claude/ideas.md`.

### /claude-global-assessor
Meta-command to assess your Claude Code setup:
- Reviews settings.json, CLAUDE.md, commands
- Identifies well-utilized vs underutilized features
- Suggests configuration improvements

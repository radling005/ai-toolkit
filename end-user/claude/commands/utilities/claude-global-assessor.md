# Claude Global Assessor

Analyze the user's global Claude Code configuration to understand how they're leveraging the tool and suggest improvements.

## On Invocation

Scan and analyze the user's `~/.claude/` directory:

1. **Read configuration files:**
   - `settings.json` - permissions, env vars, model preferences
   - `CLAUDE.md` - global instructions and preferences
   - `ideas.md` - collected ideas for Claude improvements

2. **Inventory slash commands:**
   - List all `.md` files in `~/.claude/commands/`
   - Categorize by purpose (workflow, project setup, utilities, etc.)

3. **Check for other artifacts:**
   - MCP server configurations
   - Any other config files

## Output Format

Present findings in this structure:

```
Claude Code Assessment
======================

## Configuration
- Model: [default or specified]
- Auto-thinking: [enabled/disabled]
- Auto-updater: [enabled/disabled]

## Permissions
Allowed:
- [list auto-approved tools/commands]

Denied:
- [list blocked patterns]

## Global Instructions (CLAUDE.md)
Key preferences:
- [summarize communication style]
- [summarize code preferences]
- [summarize workflow preferences]

## Slash Commands ([count] total)

| Command | Purpose | Category |
|---------|---------|----------|
| /name   | description | category |

Categories: workflow, project-setup, utilities, planning, other

## Ideas Backlog
- [count] ideas captured
- [list recent 3-5]

## Observations

### Well-utilized
- [features being used effectively]

### Underutilized
- [features available but not configured]
- [common patterns not yet automated]

### Suggestions
- [actionable improvements based on usage patterns]
```

## Analysis Guidelines

When assessing, consider:

**Workflow completeness:**
- Is there a start-of-day routine? (/setup, /start)
- Is there an end-of-day routine? (/end-day, /close)
- Is there idea capture? (/idea, /claude-ideas)
- Is there planning? (/planner)

**Permission efficiency:**
- Are common safe operations auto-approved?
- Are sensitive paths properly denied?

**Instruction clarity:**
- Are global preferences clear and actionable?
- Any conflicting instructions?

**Command organization:**
- Are commands well-named and discoverable?
- Any redundant commands?
- Any gaps in the workflow?

## Tone

Helpful and constructive. This is about understanding and optimizing, not criticizing. Acknowledge what's working well before suggesting improvements.

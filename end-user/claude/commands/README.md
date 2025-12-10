# Custom Slash Commands

Create reusable prompts as custom slash commands.

## Locations

| Scope | Path | Shared via git? |
|-------|------|-----------------|
| Project | `.claude/commands/` | Yes |
| Personal | `~/.claude/commands/` | No |

## File Format

Commands are markdown files with optional YAML frontmatter:

```markdown
---
description: What this command does
argument-hint: [optional args]
allowed-tools: Read, Edit, Bash(npm:*)
model: sonnet
---

Your prompt here. Use $ARGUMENTS for user input.
```

## Frontmatter Options

| Field | Description |
|-------|-------------|
| `description` | Shows in command list |
| `argument-hint` | Placeholder text for arguments |
| `allowed-tools` | Restrict which tools can be used |
| `model` | Force a specific model (sonnet, opus, haiku) |
| `disable-model-invocation` | If true, just expands text without invoking |

## Variables

| Variable | Description |
|----------|-------------|
| `$ARGUMENTS` | All arguments passed to command |
| `$1`, `$2`, etc. | Individual arguments |
| `@file.txt` | Include file contents |
| `!command` | Include shell command output |

## Experiments

Add your command experiments below:

---

### Example: Git Commit Helper

**File:** `commit.md`

```markdown
---
description: Create a well-formatted git commit
argument-hint: [message]
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*)
---

Create a git commit with this message: $ARGUMENTS

First check git status, then stage relevant files, and commit.
```

**Usage:** `/commit fix login bug`

---

### Example: Code Review

**File:** `review.md`

```markdown
---
description: Review code in a file
argument-hint: <file>
allowed-tools: Read, Grep
---

Review the code in @$1 for:
- Bugs and edge cases
- Performance issues
- Security concerns
- Code style

Provide specific, actionable feedback.
```

**Usage:** `/review src/auth.ts`

---

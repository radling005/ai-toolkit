# Settings & Configuration

Configure Claude Code's behavior through settings files and environment variables.

## Settings Files (by priority)

| Priority | File | Scope |
|----------|------|-------|
| 1 | Enterprise managed policies | Organization |
| 2 | Command line arguments | Session |
| 3 | `.claude/settings.local.json` | Project (private) |
| 4 | `.claude/settings.json` | Project (shared) |
| 5 | `~/.claude/settings.json` | User |

## Key Settings

```json
{
  "permissions": {
    "allow": [],
    "ask": [],
    "deny": []
  },
  "env": {},
  "model": "sonnet",
  "hooks": {},
  "sandbox": {}
}
```

## Permission Rules

Control which tools Claude can use:

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Bash(npm run lint)",
      "Bash(npm run test:*)"
    ],
    "ask": [
      "Write",
      "Edit",
      "Bash(git push:*)"
    ],
    "deny": [
      "Bash(rm -rf:*)",
      "Read(.env)",
      "Read(./secrets/**)"
    ]
  }
}
```

## Pattern Syntax

| Pattern | Matches |
|---------|---------|
| `Read` | All Read operations |
| `Bash(npm:*)` | Any npm command |
| `Read(.env)` | Specific file |
| `Read(./secrets/**)` | Directory and subdirs |
| `Write\|Edit` | Multiple tools |

## Environment Variables

Set in `env` section or shell:

| Variable | Purpose |
|----------|---------|
| `MAX_THINKING_TOKENS` | Enable extended thinking |
| `BASH_DEFAULT_TIMEOUT_MS` | Command timeout |
| `DISABLE_TELEMETRY` | Opt out of telemetry |

## Experiments

Add your settings experiments below:

---

### Example: Strict Mode

**File:** `strict-settings.json`

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Grep",
      "Glob"
    ],
    "ask": [
      "Write",
      "Edit",
      "Bash(git:*)",
      "Bash(npm:*)"
    ],
    "deny": [
      "Bash(rm:*)",
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Read(.env*)",
      "Read(**/.env*)",
      "WebFetch"
    ]
  }
}
```

**Notes:** Blocks destructive commands, network access, and env files.

---

### Example: Auto-approve for Testing

**File:** `permissive-settings.json`

```json
{
  "permissions": {
    "allow": [
      "Read",
      "Write",
      "Edit",
      "Bash(npm:*)",
      "Bash(git status:*)",
      "Bash(git diff:*)"
    ],
    "deny": [
      "Bash(git push:*)",
      "Bash(rm -rf:*)"
    ]
  }
}
```

**Notes:** More permissive for rapid iteration, still blocks dangerous ops.

---

### Example: Extended Thinking

**File:** `thinking-settings.json`

```json
{
  "env": {
    "MAX_THINKING_TOKENS": "10000"
  }
}
```

**Notes:** Enables extended thinking for complex reasoning tasks.

---

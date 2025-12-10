# Hooks

Hooks execute shell commands at various points in Claude Code's lifecycle.

## Hook Events

| Event | When it runs | Can block? |
|-------|--------------|------------|
| `PreToolUse` | Before a tool is called | Yes |
| `PostToolUse` | After a tool completes | No |
| `UserPromptSubmit` | When user submits a prompt | Yes |
| `PermissionRequest` | Before permission dialog appears | Yes |
| `Notification` | When Claude sends a notification | No |
| `Stop` | When Claude finishes responding | No |
| `SubagentStop` | When a subagent task completes | No |
| `PreCompact` | Before conversation compacting | No |
| `SessionStart` | When a session starts/resumes | No |
| `SessionEnd` | When a session ends | No |

## Configuration

Hooks are configured in `settings.json`:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "command": "prettier --write $CLAUDE_FILE_PATH"
      }
    ]
  }
}
```

## Matcher Options

- Tool name: `"Write"`, `"Edit"`, `"Bash"`
- Multiple tools: `"Write|Edit"`
- With arguments: `"Bash(npm test:*)"`

## Environment Variables Available

| Variable | Description |
|----------|-------------|
| `$CLAUDE_TOOL_NAME` | Name of the tool being used |
| `$CLAUDE_FILE_PATH` | File path (for file-related tools) |
| `$CLAUDE_TOOL_INPUT` | JSON input to the tool |
| `$CLAUDE_TOOL_OUTPUT` | JSON output from the tool |

## Experiments

Add your hook experiments below:

---

### Example: Auto-format on save

**File:** `auto-format.json`

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "command": "prettier --write $CLAUDE_FILE_PATH"
      }
    ]
  }
}
```

**Notes:** Automatically formats files after Claude writes or edits them.

---

# AI Toolkit

Curated, proven AI configurations, commands, workflows, and code patterns for solo developers.

## What's Here

**Ready-to-use tooling** - everything in this repo has been tested and proven useful. No experiments, no half-baked ideas.

## Structure

```
ai-toolkit/
  api/                    # Programmatic AI usage (SDKs, scripts)
    claude/               # Anthropic Claude API patterns
    gemini/               # Google Gemini API patterns
  end-user/               # Power user configs (no coding required)
    claude/               # Claude Code tooling
      commands/           # Slash commands
      hooks/              # Hook examples
      mcp-servers/        # MCP server configs
      settings/           # Settings examples
      skills/             # Skill definitions
      subagents/          # Subagent definitions
    gemini/               # Gemini configs
```

## Usage

Browse the folders for what you need. Each section has its own README with specifics.

**Highlights:**
- `end-user/claude/commands/solo-dev-workflow/` - Workflow commands for solo dev sessions (`/start`, `/ship`, `/review`, etc.)
- `end-user/claude/settings/` - Example CLAUDE.md and settings.json templates

## Related

- **ai-playground** - Experimental sandbox for trying things out (items graduate here when proven useful)

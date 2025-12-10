# Claude Code Experiments

This folder contains experiments, examples, and notes for exploring Claude Code features.

## Structure

| Folder | Description |
|--------|-------------|
| [hooks/](./hooks/) | Lifecycle hooks (PreToolUse, PostToolUse, Stop, etc.) |
| [commands/](./commands/) | Custom slash commands |
| [mcp-servers/](./mcp-servers/) | MCP server configurations and integrations |
| [subagents/](./subagents/) | Custom AI subagents for specialized tasks |
| [skills/](./skills/) | Modular capabilities and skill definitions |
| [settings/](./settings/) | Configuration examples and permission rules |

## Quick Reference

### Key Locations (for actual use)

When you want to actually use these experiments, copy them to:

| Type | Project-level | User-level |
|------|---------------|------------|
| Commands | `.claude/commands/` | `~/.claude/commands/` |
| Subagents | `.claude/agents/` | `~/.claude/agents/` |
| Skills | `.claude/skills/` | `~/.claude/skills/` |
| Settings | `.claude/settings.json` | `~/.claude/settings.json` |
| Memory | `.claude/CLAUDE.md` | `~/.claude/CLAUDE.md` |

### Useful Slash Commands

- `/hooks` - Manage hooks
- `/mcp` - Manage MCP servers
- `/agents` - Manage subagents
- `/config` - Open settings
- `/memory` - Edit CLAUDE.md
- `/help` - Full command list

## Getting Started

1. Browse the folders to see examples
2. Copy what you want to try into the appropriate `.claude/` location
3. Test and iterate
4. Document what works in this repo

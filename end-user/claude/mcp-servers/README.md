# MCP Servers

Model Context Protocol (MCP) servers connect Claude Code to external tools and data sources.

## Adding Servers

```bash
# HTTP transport
claude mcp add --transport http <name> <url>

# Stdio transport (local process)
claude mcp add --transport stdio <name> -- <command>

# Interactive management
/mcp
```

## Configuration Scopes

| Scope | File | Use case |
|-------|------|----------|
| Local | `.claude.json` | Project-specific, private |
| Project | `.mcp.json` | Shared with team via git |
| User | `~/.claude.json` | Personal, cross-project |

## Popular MCP Servers

| Server | Purpose |
|--------|---------|
| GitHub | Issues, PRs, repos |
| Sentry | Error tracking |
| PostgreSQL | Database queries |
| Notion | Documentation |
| Slack | Messaging |
| Filesystem | Extended file access |

Browse more at: https://github.com/modelcontextprotocol/servers

## Configuration Format

In `.mcp.json` or `~/.claude.json`:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

## Using MCP Tools

Once connected, MCP tools appear automatically. Reference MCP resources with `@`:

```
@mcp:github://repos/owner/repo
```

MCP prompts become slash commands:

```
/mcp__servername__promptname
```

## Experiments

Add your MCP server experiments below:

---

### Example: GitHub Integration

**Setup:**
```bash
claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

**Config:** Set `GITHUB_TOKEN` environment variable

**Notes:** Enables working with issues, PRs, and repo data directly.

---

### Example: Filesystem Server

**Setup:**
```bash
claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem /path/to/allow
```

**Notes:** Gives Claude access to files outside the project directory.

---

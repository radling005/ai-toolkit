# Skills

Modular capabilities that extend Claude's knowledge and abilities.

## Locations

| Scope | Path | Shared via git? |
|-------|------|-----------------|
| Project | `.claude/skills/<skill-name>/SKILL.md` | Yes |
| Personal | `~/.claude/skills/<skill-name>/SKILL.md` | No |

## Structure

```
skill-name/
├── SKILL.md           # Required - main skill definition
├── reference.md       # Optional - detailed reference docs
├── examples.md        # Optional - usage examples
├── scripts/           # Optional - utility scripts
└── templates/         # Optional - templates for generation
```

## SKILL.md Format

```markdown
---
name: skill-name
description: What this skill does and when to use it
allowed-tools: Read, Grep, Glob
---

# Skill Name

Instructions for how to use this skill.

Claude will read this when the skill is invoked and follow these guidelines.
```

## Frontmatter Options

| Field | Description |
|-------|-------------|
| `name` | Skill identifier |
| `description` | When Claude should use this skill |
| `allowed-tools` | Restrict available tools for security |

## How Skills Work

1. Claude automatically detects when a skill is relevant
2. Loads the SKILL.md and supporting files
3. Uses the knowledge to complete the task
4. Progressive disclosure - loads details as needed

## Experiments

Add your skill experiments below:

---

### Example: API Documentation Skill

**Structure:**
```
api-docs/
├── SKILL.md
├── patterns.md
└── templates/
    └── endpoint.md
```

**SKILL.md:**
```markdown
---
name: api-docs
description: Generate API documentation following project standards
allowed-tools: Read, Write, Edit
---

# API Documentation Skill

When documenting APIs:

1. Follow the template in templates/endpoint.md
2. Include request/response examples
3. Document error codes
4. Add authentication requirements

See patterns.md for common documentation patterns.
```

---

### Example: Database Migration Skill

**SKILL.md:**
```markdown
---
name: db-migrations
description: Create and manage database migrations
allowed-tools: Read, Write, Bash(npm run migrate:*)
---

# Database Migration Skill

When creating migrations:

1. Use the project's migration tool (check package.json)
2. Name migrations descriptively: YYYYMMDD_description
3. Always include up and down migrations
4. Test rollback before committing
```

---

# Subagents

Specialized AI assistants that handle specific tasks with their own context window.

## Locations

| Scope | Path | Shared via git? |
|-------|------|-----------------|
| Project | `.claude/agents/` | Yes |
| Personal | `~/.claude/agents/` | No |

## File Format

Subagents are markdown files with YAML frontmatter:

```markdown
---
name: agent-name
description: When to use this agent
tools: Read, Edit, Grep, Glob
model: sonnet
---

Instructions for the agent go here.
Describe its role, behavior, and any specific guidelines.
```

## Frontmatter Options

| Field | Description |
|-------|-------------|
| `name` | Identifier for the agent |
| `description` | When Claude should use this agent |
| `tools` | Comma-separated list of allowed tools |
| `model` | sonnet, opus, haiku, or inherit from parent |
| `permissionMode` | default, plan, auto, etc. |
| `skills` | Skills the agent can use |

## Built-in Agents

| Agent | Purpose |
|-------|---------|
| Explore | Fast, read-only codebase analysis (uses Haiku) |
| Plan | Research for plan mode |
| General-purpose | Complex multi-step tasks |

## Invoking Agents

- **Automatic:** Claude decides based on context
- **Explicit:** "Use the code-reviewer agent to check this"
- **Via command:** `/agents` to manage

## Experiments

Add your subagent experiments below:

---

### Example: Code Reviewer

**File:** `code-reviewer.md`

```markdown
---
name: code-reviewer
description: Use this agent to review code for bugs, security issues, and best practices
tools: Read, Grep, Glob
model: sonnet
---

You are a code reviewer. When given code to review:

1. Check for bugs and edge cases
2. Look for security vulnerabilities
3. Evaluate performance implications
4. Assess code readability and maintainability
5. Suggest specific improvements

Be constructive but thorough. Cite line numbers when referencing issues.
```

---

### Example: Test Writer

**File:** `test-writer.md`

```markdown
---
name: test-writer
description: Use this agent to generate unit tests for code
tools: Read, Write, Edit, Grep, Glob
model: sonnet
---

You are a test writing specialist. When asked to write tests:

1. Analyze the code to understand its behavior
2. Identify edge cases and error conditions
3. Write comprehensive unit tests
4. Follow the project's existing test patterns
5. Include both positive and negative test cases

Match the testing framework already in use (Jest, pytest, etc.).
```

---

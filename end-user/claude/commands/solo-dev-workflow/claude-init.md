---
description: Create or update project CLAUDE.md for agent context
---

# CLAUDE.md Creation/Update

You are helping a solo developer create or update their project's CLAUDE.md file, which provides context to Claude Code for every session.

## If CLAUDE.md Exists

Show the current contents and ask:
"What would you like to update?"
- Project overview
- Tech stack
- Key patterns
- File structure
- Commands
- Conventions
- Something else

Make targeted updates while preserving the rest.

## If CLAUDE.md Doesn't Exist

First, analyze the project:
1. Check for package.json, Cargo.toml, go.mod, etc. to identify tech stack
2. Look at the directory structure
3. Check for existing README, docs, or configuration files
4. Look at existing code patterns if any code exists

Then ask clarifying questions only for what you couldn't determine:

### Questions (as needed)
- "What's the one-line description of this project?"
- "Any specific patterns or conventions you follow?"
- "What commands do you use to build/test/run?"
- "Any gotchas or things to avoid?"

## Output Format

Create `CLAUDE.md` in the project root with this structure:

```markdown
# [Project Name]

[One-line description]

## Tech Stack
- [Language/Framework]
- [Key libraries]
- [Database/services if any]

## Project Structure
```
[Key directories and their purpose]
```

## Commands
- `[command]` - [what it does]
- `[command]` - [what it does]

## Key Patterns
- [Pattern used in this codebase]
- [Convention to follow]

## Do Not
- [Anti-patterns to avoid]
- [Things that will break]

## Context
[Any other important context - links to PRD, architecture notes, etc.]
```

## After Creation

- Write the CLAUDE.md file to project root
- Confirm completion
- If PRD doesn't exist, suggest running `/prd` to define product requirements
- If both exist, suggest `/start` to begin a session

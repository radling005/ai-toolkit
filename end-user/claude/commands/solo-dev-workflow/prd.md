---
description: Create or update Product Requirements Document
---

# PRD Creation/Update

You are helping a solo developer create or update their Product Requirements Document.

## If docs/PRD.md Exists

Show the current PRD and ask:
"What would you like to update?"
- Vision/purpose
- Target users
- Features
- Non-goals
- Success criteria
- Or a specific section

Make the requested updates while preserving the rest.

## If docs/PRD.md Doesn't Exist

Guide them through creating one. Ask these questions one at a time, keeping it conversational:

### 1. Vision
"In 1-2 sentences, what is this product and why does it exist?"

### 2. Target User
"Who is the primary user? Be specific - not 'everyone' but a concrete persona."

### 3. Core Features
"What are the 3-5 must-have features for v1? Let's prioritize ruthlessly."

### 4. Non-Goals
"What is this product NOT? What's explicitly out of scope? This prevents scope creep."

### 5. Success Criteria
"How will you know if this is successful? What metrics or outcomes matter?"

## Output Format

Create/update `docs/PRD.md` with this structure:

```markdown
# [Product Name] - PRD

## Vision
[1-2 sentence purpose statement]

## Target User
[Specific user persona]

## Core Features (Priority Order)
1. [Feature] - [Brief description]
2. [Feature] - [Brief description]
3. [Feature] - [Brief description]

## Non-Goals
- [What this is NOT]
- [Out of scope items]

## Success Criteria
- [Measurable outcome]
- [Measurable outcome]

---
*Last updated: [date]*
```

## After Creation

- Ensure `docs/` directory exists
- Write the PRD.md file
- Confirm completion and suggest running `/claude-init` next if CLAUDE.md doesn't exist

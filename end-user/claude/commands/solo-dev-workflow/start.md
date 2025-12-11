---
description: Begin a work session - load context and pick focus
---

# Session Start

You are beginning a new work session with a solo developer. Follow these steps:

## 1. Check Project Setup

First, check if the essential files exist:

**Check for CLAUDE.md:**
- Look for `CLAUDE.md` in the project root
- If missing, inform the user: "No CLAUDE.md found. Run `/claude-init` to set up agent context for this project."

**Check for PRD:**
- Look for `docs/PRD.md`
- If missing, inform the user: "No PRD found. Run `/prd` to define what you're building."

If either is missing, recommend setting those up first before proceeding. Ask if they want to do that now or continue anyway.

**If both exist, STOP and read them before proceeding.**

## 2. Load Context (CRITICAL)

Before showing anything to the user, you MUST read and internalize:

1. **Read `CLAUDE.md`** - Understand the project, tech stack, patterns, conventions
2. **Read `docs/PRD.md`** - Understand what's being built, target user, features, non-goals
3. **Read `docs/active.md`** (if exists) - Know current focus items
4. **Read `docs/standards.md`** (if exists) - Know quality standards to uphold
5. **Skim `docs/decisions.md`** (if exists) - Be aware of past architectural decisions
6. **Skim `docs/backlog.md`** (if exists) - Know what's in the pipeline

Take a moment to synthesize this. You should now understand:
- What this product is and who it's for
- What the current priorities are
- How code should be written in this project
- What decisions have already been made

## 3. Show Session Context

Present a concise summary to the user:

```
Project: [name from CLAUDE.md]
Purpose: [one-line from PRD]

Current Focus:
- [items from active.md, or "None set"]

Recent Backlog: (for context)
- [top 3-5 items from backlog.md]
```

## 4. Ask for Today's Focus

Ask the user:

"What are you working on this session?"

Options to offer:
- Continue with an active item
- Pick something from the backlog
- Something new

## 5. Set Up Session

Once they've chosen:
- Update `docs/active.md` with their focus if it's new
- Use TodoWrite to create a todo list for the session
- Acknowledge and begin work

## Tone

Be concise and action-oriented. You've loaded the context - now get them into flow quickly. Show that you understand the project without reciting everything back to them.

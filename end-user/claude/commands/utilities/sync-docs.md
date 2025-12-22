# Documentation Sync and Maintenance

You are performing a weekly documentation maintenance task. Your goal is to ensure all project documentation is current, accurate, and in sync with the actual codebase.

## Scope

**Primary docs to verify:**
- `docs/` folder (active.md, backlog.md, sessions.md, decisions.md, ideas.md, standards.md, cicd.md, and any others)
- `docs/archive/` folder (archived content for historical reference)
- `CLAUDE.md` (project context file)
- `README.md` (if exists)

**Secondary verification (as needed):**
- Project structure matches what docs describe
- Commands documented in CLAUDE.md actually work
- Patterns mentioned in docs match actual code

## Tasks

### 1. Read Current State
Read all docs files, including archives, to understand:
- What's documented as "in progress" or "up next"
- Recent session history
- Current backlog items
- Documented decisions and patterns

### 2. Verify Accuracy
Check for:
- Stale "In Progress" items that are actually done
- Outdated test counts, coverage numbers, or other metrics
- Project structure in CLAUDE.md matching actual folders
- Commands in CLAUDE.md that still work (just verify they exist, don't run tests/linters)
- Tech stack or dependencies that have changed
- Decisions made but not recorded in decisions.md

### 3. Archive Old Content
Move to `docs/archive/` (create if needed):
- Session entries older than 3-5 most recent (keep recent ones in sessions.md)
- Completed milestone sections (like "MVP Complete")
- Any other content that's purely historical

### 4. Sync and Update
Fix inconsistencies:
- Update stale metrics (test counts, coverage, etc.)
- Mark completed items as done
- Add missing decisions from recent sessions
- Trim overly long "Recently Completed" sections
- Ensure cross-references between docs are valid

### 5. Check for Tech Debt Signals
Look for signs of drift:
- TODOs in code that aren't in backlog
- Deprecated patterns still documented as current
- Features mentioned in docs that don't exist in code
- Code patterns that don't match documented standards

## Autonomy Guidelines

**Auto-fix (do without asking):**
- Updating metrics (test counts, coverage)
- Archiving old session entries
- Trimming "Recently Completed" to last 3 items
- Fixing broken cross-references
- Adding missing decisions that are clearly documented in sessions

**Ask before changing:**
- Removing backlog items
- Changing documented patterns or standards
- Modifying CLAUDE.md structure
- Any change where intent is ambiguous
- Adding new documentation files

## Output

After completing the sync, provide a summary:
1. **Changes Made** - List of auto-fixes applied
2. **Issues Found** - Problems that need user decision
3. **Recommendations** - Suggestions for improvements
4. **Health Check** - Overall documentation health (good/needs attention/stale)

If everything is in sync, just confirm "Documentation is current. No changes needed."

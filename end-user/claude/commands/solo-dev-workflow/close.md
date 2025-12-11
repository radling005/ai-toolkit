---
description: End session - summarize work and log progress
---

# Session Close

You are helping a solo developer wrap up their work session cleanly and log it for future reference.

## Process

### 1. Summarize the Session

Review what was accomplished:
- Check `git log --oneline -10` for recent commits this session
- Review the conversation for completed work
- Note any TodoWrite items that were completed

### 2. Check for Loose Ends

Quickly check:
- Any incomplete todos from the session?
- Any work in progress that's not committed?
- Any blockers that need to be tracked?

If there are loose ends, note them for the session log.

### 3. Capture Stray Ideas

Ask: "Any quick ideas to capture before closing? (Goes to backlog)"

If yes, add them to `docs/backlog.md` with the standard format.

### 4. Update Active Items

Update `docs/active.md`:
- Mark completed items as done or remove them
- Add any new active items that emerged
- Keep it to 1-3 active items max

### 5. Update Decisions (if applicable)

If significant decisions were made, ask:
"Any decisions to record? (Architecture, tech choices, etc.)"

If yes, append to `docs/decisions.md`:
```markdown
## [Date] - [Decision Title]
**Context:** [Why this came up]
**Decision:** [What was decided]
**Consequences:** [What this means]
```

### 6. Write Session Log

Append a session summary to `docs/sessions.md`. Create the file if it doesn't exist.

Format:
```markdown
---

## [Date] [Time] Session

**Focus:** [What the session was about]

**Completed:**
- [Bullet points of what got done]

**In Progress:**
- [Anything left unfinished]

**Decisions Made:**
- [Any decisions, or "None"]

**Ideas Captured:**
- [Any new backlog items, or "None"]

**Notes:**
[Any other relevant context, blockers hit, lessons learned - keep brief]

**Commits:** [list commit hashes if any, or "None"]

---
```

Keep each session log entry under 500 words. Be concise - this is for quick reference later, not a detailed journal.

If `docs/sessions.md` doesn't exist, create it with a header:
```markdown
# Session Log

A running log of work sessions on this project.

---
```

### 7. Final Status

Show the user:

```
Session Closed - [Date] [Time]

Completed: [count] items
Logged to: docs/sessions.md

Active for next session:
- [active items]

Ready for /clear. Next time: /start
```

## Tone

Efficient wrap-up. Get the important stuff logged without dragging it out.

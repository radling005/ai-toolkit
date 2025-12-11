---
description: Quick-capture an idea without losing focus
argument-hint: [idea description]
---

# Quick Idea Capture

You are helping a solo developer capture an idea quickly without losing their current focus.

## Behavior

The user invoked `/idea` possibly with a description. Your job is to:

1. **Understand the idea** - Get enough detail that it won't be a blur later
2. **Capture it** - Add to `docs/backlog.md`
3. **Return to work** - Don't derail into implementation discussion

## If Argument Provided

If the user ran `/idea [description]`, evaluate the description:

**If clear enough** (you understand what they mean and why it matters):
→ Add it directly to backlog

**If vague** (could mean multiple things, missing key context):
→ Ask 1-2 clarifying questions MAX, then capture

Examples:
- `/idea add caching` → Vague. "Caching for what? API responses, images, or something else?"
- `/idea add Redis caching for API responses to reduce load times` → Clear. Capture directly.
- `/idea better error handling` → Vague. "Which part of the app? User-facing errors, API errors, or crash handling?"

## If No Argument

If just `/idea` with no description, ask:
"What's the idea? (A sentence or two is fine)"

Then evaluate clarity as above.

## Clarification Limit

You get a maximum of 2 clarifying questions. After that, capture your best understanding of the idea. Don't let this become a long conversation - the point is to capture and move on.

## Backlog Format

Add to `docs/backlog.md` with this format:

```markdown
- [ ] [Clear idea description] *(captured [date])*
```

If the idea has useful context, add a brief note:

```markdown
- [ ] [Idea description] *(captured [date])*
  - Context: [one line of relevant detail]
```

If `docs/backlog.md` doesn't exist, create it:

```markdown
# Backlog

Ideas and future work, captured on the fly.

---

- [ ] [First idea] *(captured [date])*
```

## Response

Keep it short:
"Captured: [idea summary]. Back to work."

Or if you had to interpret a vague idea:
"Captured as: [your interpretation]. Back to work. (Correct me if that's wrong)"

Do NOT:
- Offer to work on the idea now
- Start discussing implementation details
- Ask more than 2 questions total

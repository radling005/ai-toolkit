# Common Fixes Cheatsheet

Quick solutions to frequent AI problems.

---

## Output Problems

### Response is too long
```
Add: "Be concise. Maximum [X] sentences/words/bullets."
```

### Response is too short
```
Add: "Provide a detailed/comprehensive response."
Or: "Elaborate on each point."
```

### Wrong format
```
Show the exact format:
"Respond in this exact format:
## Section 1
[content]
## Section 2
[content]"
```

### Missing information
```
Add: "Make sure to include: [list required elements]"
```

### Too generic
```
Add more context:
"For context: [your specific situation]"
"Specifically for: [your use case]"
```

---

## Understanding Problems

### AI misunderstood the task
```
Clarify: "To be clear, I want [X], not [Y]."
Or restart: "Let me rephrase. What I need is..."
```

### AI made wrong assumptions
```
"Don't assume [X]. Instead, [correct assumption]."
```

### AI went off-topic
```
"Focus only on [topic]. Ignore [other things]."
```

---

## Code Problems

### Code doesn't run
```
"The code has an error: [error message]
Fix the code so it runs correctly."
```

### Wrong language/version
```
"Use Python 3.11 syntax."
"This is for Node.js 18."
```

### Missing error handling
```
"Add error handling for: [specific cases]"
```

### Code is too complex
```
"Simplify this. Break into smaller functions."
"Explain what each part does."
```

---

## Conversation Problems

### AI forgot earlier context
```
"To recap what we discussed:
- [Point 1]
- [Point 2]
Continuing from there..."
```

### AI is stuck in a loop
```
Start fresh, or:
"You've said this before. Try a completely different approach."
```

### AI keeps making same mistake
```
Be more explicit:
"Do NOT [thing it keeps doing].
Instead, always [correct approach]."
```

---

## Quality Problems

### Hallucination suspected
```
"Are you certain about [claim]?
What's your confidence level?"
Or: "Cite sources for this."
```

### Output seems wrong
```
"Double-check this. Walk through your reasoning."
Or: "Verify: [specific concern]"
```

### Need more options
```
"Give me 3 alternative approaches."
"What are other ways to do this?"
```

---

## Refusal Problems

### Legitimate request refused
```
Provide context:
"This is for [legitimate purpose].
I'm a [role] working on [project]."
```

### Rephrase trigger words
```
Remove potentially problematic phrasing.
Be more specific about intent.
```

---

## Quick Fix Patterns

| Problem | Quick Fix |
|---------|-----------|
| Too vague | Add specifics |
| Too long | Add length limit |
| Wrong format | Show example format |
| Off-topic | "Focus only on X" |
| Too basic | "For an expert audience" |
| Too complex | "Explain simply" |
| Missing parts | "Include: A, B, C" |
| Wrong tone | "Use [formal/casual] tone" |

---

## When All Else Fails

1. **Start fresh** — New conversation, refined prompt
2. **Break it down** — Smaller, simpler requests
3. **Show examples** — Demonstrate what you want
4. **Try different model** — Switch Claude ↔ Gemini
5. **Rethink approach** — Maybe AI isn't the right tool

---

## Prevention Checklist

Before sending a prompt:

- [ ] Is the task clear and specific?
- [ ] Did I provide necessary context?
- [ ] Did I specify the format I want?
- [ ] Did I set appropriate constraints?
- [ ] Did I include examples if format matters?

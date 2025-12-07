# Prompt Library

Your personal collection of battle-tested prompts.

## Why a Library?

Great prompts are valuable. Without a library, you:
- Reinvent the wheel constantly
- Forget what worked
- Can't share with teammates
- Lose your best discoveries

A prompt library compounds your AI effectiveness over time.

---

## Quick Start

1. **Find a prompt** — Browse by task or domain
2. **Copy & adapt** — Fill in the `[PLACEHOLDERS]`
3. **Use it** — Run in Claude, Gemini, or any AI
4. **Improve it** — Update the library with what you learn

---

## Library Structure

```
library/
├── by-task/           # Organized by what you're doing
│   ├── code-generation.md
│   ├── code-review.md
│   ├── debugging.md
│   ├── writing.md
│   ├── analysis.md
│   └── brainstorming.md
├── by-domain/         # Organized by field/industry
│   ├── web-development.md
│   ├── data-science.md
│   └── devops.md
└── templates/         # Meta-templates for creating prompts
    └── prompt-template.md
```

---

## Prompt Entry Format

Every prompt in the library follows this format:

```markdown
## [Prompt Name]

**Purpose:** What this prompt accomplishes
**Best for:** Claude / Gemini / Both
**Success rate:** High / Medium / Needs refinement
**Last tested:** YYYY-MM-DD

### Prompt
```
[The actual prompt with [PLACEHOLDERS] for customization]
```

### Example Usage
```
[A filled-in example showing real usage]
```

### Tips
- [What makes this prompt work well]
- [Common modifications]
- [What to watch out for]

### Variations
- [Alternative version for different context]
```

---

## Starter Prompts

### The Universal Debugger
```
I'm seeing unexpected behavior in my code.

**Expected:** [What should happen]
**Actual:** [What's happening instead]
**Error (if any):** [Error message]

Code:
```[language]
[paste code]
```

Help me:
1. Identify the most likely cause
2. Explain why this is happening
3. Show me how to fix it
4. Suggest how to prevent this in the future
```

### The Code Reviewer
```
Review this [LANGUAGE] code for:
1. Bugs and potential errors
2. Security vulnerabilities
3. Performance issues
4. Readability improvements

Prioritize findings as: Critical / Major / Minor

For each issue:
- Line number(s)
- What's wrong
- How to fix it

Code:
```[language]
[paste code]
```
```

### The Technical Explainer
```
Explain [CONCEPT] to me.

My background: [EXPERTISE LEVEL - beginner/intermediate/expert]
Context: [WHY YOU NEED TO UNDERSTAND THIS]

Please:
1. Start with a one-sentence summary
2. Explain the key concepts
3. Give a practical example
4. Mention common misconceptions
5. Suggest what to learn next
```

### The Document Summarizer
```
Summarize this [DOCUMENT TYPE]:

Length: [NUMBER] bullet points / sentences / paragraphs
Focus on: [WHAT MATTERS MOST]
Audience: [WHO WILL READ THIS]
Format: [BULLETS / NARRATIVE / STRUCTURED]

Document:
"""
[paste content]
"""
```

### The Brainstorm Partner
```
I need ideas for [CHALLENGE/GOAL].

Context:
- [RELEVANT BACKGROUND]
- [CONSTRAINTS]
- [WHAT YOU'VE ALREADY CONSIDERED]

Generate [NUMBER] ideas. For each:
- Brief description (1-2 sentences)
- Why it might work
- Potential challenges
- Effort level (Low/Medium/High)

Then recommend your top 2 and explain why.
```

---

## Building Your Library

### What to Add

✅ **Add prompts that:**
- Worked well and you'll use again
- Took iteration to get right (save that work!)
- Are specific to your domain
- Solved a tricky problem

❌ **Don't bother adding:**
- One-off queries you won't repeat
- Simple questions that need no template
- Prompts that didn't work well

### When to Update

- After a prompt works well → Add it
- After you improve a prompt → Update it
- After a prompt stops working → Note the change
- Monthly → Review and clean up

---

## Tagging System

Use tags to make prompts findable:

**By task:**
`#code-gen` `#review` `#debug` `#write` `#analyze` `#summarize` `#brainstorm`

**By domain:**
`#frontend` `#backend` `#data` `#devops` `#security` `#docs`

**By model:**
`#claude` `#gemini` `#any`

**By status:**
`#proven` `#experimental` `#needs-work`

---

## Library Maintenance

### Monthly Review
- [ ] Remove prompts you never use
- [ ] Update prompts that have evolved
- [ ] Add new discoveries
- [ ] Check if model updates broke anything

### Quality Signals
Track what makes prompts successful:
- Success rate (works well most of the time?)
- Iteration count (how much tweaking needed?)
- Reuse frequency (do you actually use it?)

---

## Sharing Prompts

Great prompts are worth sharing:
- With teammates (create a team library)
- With the community (blog posts, repos)
- With future you (document why things work)

When sharing, include:
- The full prompt
- Context on when to use it
- Example outputs
- Known limitations

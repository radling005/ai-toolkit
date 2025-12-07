# Prompting Patterns Cheatsheet

Quick reference for core prompting techniques.

---

## The Basics

| Technique | When to Use | Example |
|-----------|-------------|---------|
| **Be specific** | Always | "Write a Python function" → "Write a Python function that validates email using regex" |
| **Provide context** | Complex tasks | "Context: This is for a REST API in Flask..." |
| **Set constraints** | Control output | "Max 100 words, bullet points, no jargon" |
| **Show examples** | Format matters | "Like this: Input: X → Output: Y" |

---

## Core Techniques

### Zero-Shot
Direct request, no examples.
```
Summarize this article in 3 bullet points.
```

### Few-Shot
Provide examples first.
```
Convert to formal English:
"gonna go" → "I am going to go"
"tbh" → "to be honest"
"lmk asap" → ?
```

### Chain-of-Thought
Ask for step-by-step reasoning.
```
Solve this step by step, showing your work:
[problem]
```

### Role Prompting
Assign expertise.
```
You are a senior security engineer.
Review this code for vulnerabilities.
```

---

## Format Control

| Want This | Say This |
|-----------|----------|
| JSON | "Respond in valid JSON: {field1, field2}" |
| Markdown table | "Format as a markdown table" |
| Bullet points | "As a bulleted list" |
| Numbered steps | "As numbered steps" |
| Specific sections | "Include sections: Overview, Details, Summary" |

---

## Output Length

| Want This | Say This |
|-----------|----------|
| Very short | "In one sentence" / "TL;DR" |
| Short | "In 2-3 sentences" / "Brief summary" |
| Medium | "In 1-2 paragraphs" |
| Detailed | "Comprehensive explanation" |
| Specific | "In exactly 5 bullet points" |

---

## Prompt Structure Template

```
[ROLE - optional]
You are a [expertise].

[CONTEXT]
Background: [relevant info]

[TASK]
[What you want done]

[FORMAT]
Format: [how to structure output]

[CONSTRAINTS]
- [Constraint 1]
- [Constraint 2]
```

---

## Quick Fixes

| Problem | Fix |
|---------|-----|
| Too vague | Add specific details |
| Wrong format | Show exact format wanted |
| Too long | Add length constraint |
| Too short | Ask for "detailed" or "comprehensive" |
| Missing info | List required elements |
| Off-topic | Add "Focus only on X" |

---

## Power Phrases

**For better reasoning:**
- "Think step by step"
- "Consider the pros and cons"
- "What are the edge cases?"

**For better output:**
- "Be specific and concrete"
- "Give practical examples"
- "Explain your reasoning"

**For iteration:**
- "Keep X, but change Y"
- "More detail on section Z"
- "Simplify this for beginners"

---

## Anti-Patterns (Avoid These)

❌ "Make this better" → ✅ "Improve readability by..."
❌ "Fix the code" → ✅ "Fix the null check on line 15"
❌ Multiple unrelated asks → ✅ One focused request
❌ No context → ✅ Provide relevant background
❌ Assuming AI knows your project → ✅ Explain the setup

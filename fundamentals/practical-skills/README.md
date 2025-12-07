# Practical Skills

Day-to-day effectiveness with AI tools.

## Overview

Beyond techniques and theory, practical effectiveness comes from habits, workflows, and knowing how to handle real-world situations.

---

## Debugging AI Outputs

### When Output is Wrong

**Step 1: Identify the issue type**

| Issue Type | Symptoms | Approach |
|------------|----------|----------|
| Misunderstanding | Wrong interpretation | Clarify request |
| Missing context | Generic response | Add background |
| Wrong format | Structure issues | Show exact format |
| Hallucination | False information | Request sources, verify |
| Incomplete | Missing elements | List what's needed |

**Step 2: Diagnose**
```
"Your response [describe issue]. I was expecting [what you wanted].
What did you interpret my request to mean?"
```

**Step 3: Correct**
```
"Let me clarify:
- I need [specific thing]
- Not [what you got]
- The format should be [format]

Try again."
```

---

### When Output is Close But Not Right

```
"This is 80% of what I need. Please adjust:
- Keep: [what's good]
- Change: [what needs fixing]
- Add: [what's missing]
- Remove: [what shouldn't be there]"
```

---

## Error Recovery

### Conversation Went Off Track

**Option 1: Course correct**
```
"Let's step back. We've drifted from the original goal.
The task was: [original task]
Where we are: [current state]
Let's refocus on: [next step]"
```

**Option 2: Fresh start**
```
[Start new conversation]
"I tried [approach] but it didn't work because [reason].
Let's try a different approach: [new approach]"
```

### AI is Stuck in a Loop

```
"You've given similar responses several times.
Let's try something different:
- Forget previous attempts
- [New specific direction]
- [Additional constraint to break pattern]"
```

### AI Refuses Reasonable Request

```
"I understand the concern, but this is for [legitimate purpose].
Let me rephrase: [reworded request that addresses concern]"

# Or provide context:
"Context: I'm a [role] working on [project].
This is needed because [reason]."
```

---

## Session Management

### Starting Strong

```
"I'm working on [project/task].
Background: [relevant context]
Goal: [what you want to accomplish]
Constraints: [limitations]

Let's start with: [first step]"
```

### Maintaining Context

**Periodic summaries:**
```
"Let me summarize where we are:
- Done: [completed items]
- Current: [what we're working on]
- Next: [upcoming steps]

Does this match your understanding?"
```

**Reference anchoring:**
```
"Going forward:
- Call the first approach 'OPTION A'
- Call the second approach 'OPTION B'
- The main function is 'processData'"
```

### Ending Productively

```
"Before we wrap up:
1. Summarize what we accomplished
2. List any open questions
3. What should I do next independently?"
```

---

## Prompt Library Maintenance

### Building Your Library

**What to save:**
- Prompts that worked well
- Templates for recurring tasks
- Examples of good outputs
- Notes on what didn't work

**Organization:**
```
prompts/
├── by-task/
│   ├── code-review.md
│   ├── documentation.md
│   └── debugging.md
├── by-domain/
│   ├── frontend.md
│   ├── backend.md
│   └── data.md
└── templates/
    ├── general.md
    └── few-shot-examples.md
```

### Library Entry Template

```
# [Prompt Name]

**Purpose:** [What this prompt is for]
**Last tested:** [Date]
**Model:** [Which model it works well with]

## Prompt Template
```
[The actual prompt with [PLACEHOLDERS]]
```

## Example Usage
[Filled-in example]

## Notes
- [What works well]
- [What to watch out for]
- [Variations that also work]
```

---

## Cost Awareness

### Understanding Costs

| Factor | Impact |
|--------|--------|
| Input tokens | More context = more cost |
| Output tokens | Longer responses = more cost |
| Model tier | Advanced models cost more |
| Frequency | More calls = more cost |

### Cost Reduction Strategies

1. **Right-size the model** — Use smaller models for simple tasks
2. **Minimize context** — Include only what's needed
3. **Request concise output** — Limit response length
4. **Cache common requests** — Save and reuse responses
5. **Batch when possible** — Combine related queries

### When to Use What

| Task | Model Recommendation |
|------|---------------------|
| Simple questions | Smaller/faster model |
| Complex reasoning | Larger/smarter model |
| Code generation | Code-optimized model |
| Quick iteration | Faster model |
| Final polish | Best available model |

---

## Speed vs Quality Tradeoffs

### The Tradeoff Space

```
                Quality
                   ▲
                   │
    Perfect ──────►●─────────┐
    but slow      │         │
                  │    ●────┤ Good balance
                  │         │
    Fast  ────────●─────────┘
    but rough     │
                  └──────────► Speed
```

### Decision Framework

| Situation | Priority |
|-----------|----------|
| Exploration/brainstorming | Speed |
| Learning/understanding | Quality |
| First drafts | Speed |
| Final deliverables | Quality |
| Iterative refinement | Balance |
| Time pressure | Speed |

### Practical Tactics

**For speed:**
- Shorter prompts
- Smaller models
- Accept "good enough"
- Iterate quickly

**For quality:**
- Detailed prompts
- Better models
- Multiple passes
- Careful review

---

## Multi-Platform Strategy

### Know Your Tools

| Platform | Strengths | Best For |
|----------|-----------|----------|
| Claude | Long context, analysis | Complex tasks, documents |
| Gemini | Search, code execution | Current info, data analysis |
| ChatGPT | Ecosystem, plugins | Integrations, variety |
| Local models | Privacy, customization | Sensitive data |

### Strategic Usage

```
Task: Research and implement a feature

1. Gemini (search grounding) → Current best practices
2. Claude (long context) → Design discussion
3. Claude (code) → Implementation
4. Gemini (execution) → Test and verify
```

### Cross-Platform Patterns

- **Verification:** Same question to multiple models
- **Specialization:** Right model for right task
- **Fallback:** If one fails, try another
- **Comparison:** Learn strengths through experience

---

## Workflow Automation

### What to Automate

| Good candidates | Poor candidates |
|-----------------|-----------------|
| Repetitive prompts | One-off tasks |
| Structured tasks | Creative exploration |
| Clear inputs/outputs | Ambiguous requirements |
| Low-stakes outputs | High-stakes decisions |

### Simple Automation

```python
# Pseudo-code for automated prompt
template = """
Review this code for:
1. Bugs
2. Security issues
3. Performance

Code:
{code}
"""

def review_code(code):
    prompt = template.format(code=code)
    response = ai.complete(prompt)
    return parse_review(response)
```

### Automation Caution

- Always review automated outputs
- Have fallbacks for failures
- Monitor quality over time
- Keep human in the loop for important decisions

---

## Building Good Habits

### Daily Practices

1. **Before prompting:** What exactly do I need?
2. **While prompting:** Is this clear and specific?
3. **After output:** Did I get what I needed?
4. **End of session:** What worked? What didn't?

### Weekly Practices

1. Review prompts that worked well
2. Add to prompt library
3. Reflect on failures and learnings
4. Try one new technique

### Monthly Practices

1. Audit your AI usage patterns
2. Update prompt library
3. Review cost efficiency
4. Explore new tools/features

---

## Practice Exercises

### Beginner
1. Debug an AI output that wasn't quite right using the diagnostic approach
2. Create a session management routine for a complex task
3. Start a prompt library with 5 entries

### Intermediate
4. Estimate and track costs for a week of AI usage
5. Develop a multi-platform strategy for a real project
6. Create an automation script for a repetitive task

### Advanced
7. Build a comprehensive prompt library for your domain
8. Design a quality monitoring system for automated prompts
9. Create a decision framework for model/platform selection

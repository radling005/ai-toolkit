# Debugging Prompts

Battle-tested prompts for finding and fixing bugs.

---

## Universal Debugger

**Purpose:** Diagnose and fix unexpected behavior
**Best for:** Both Claude and Gemini
**Success rate:** High

### Prompt
```
Help me debug this issue:

**Expected behavior:** [WHAT SHOULD HAPPEN]
**Actual behavior:** [WHAT'S HAPPENING]
**Error message (if any):**
```
[ERROR]
```

**Code:**
```[language]
[RELEVANT CODE]
```

**What I've tried:**
- [ATTEMPT 1]
- [ATTEMPT 2]

Please:
1. Identify the most likely cause
2. Explain why this is happening
3. Show how to fix it
4. Suggest how to prevent this in the future
```

### Tips
- Include the actual error message, not a summary
- Show relevant code, not the entire file
- List what you've already tried

---

## Error Message Decoder

**Purpose:** Understand cryptic error messages
**Best for:** Both
**Success rate:** High

### Prompt
```
Explain this error and how to fix it:

```
[FULL ERROR MESSAGE WITH STACK TRACE]
```

Context:
- Language/framework: [DETAILS]
- What I was doing: [ACTION]
- Environment: [RELEVANT ENV DETAILS]

Give me:
1. What this error means in plain English
2. Most likely cause
3. Step-by-step fix
4. How to prevent it
```

---

## Logic Bug Finder

**Purpose:** Find bugs in code that runs but produces wrong results
**Best for:** Both
**Success rate:** Medium-High

### Prompt
```
This code runs but produces wrong output:

```[language]
[CODE]
```

**Input:** [EXAMPLE INPUT]
**Expected output:** [WHAT IT SHOULD PRODUCE]
**Actual output:** [WHAT IT PRODUCES]

Walk through the code step-by-step with this input and identify where the logic goes wrong.
```

---

## Performance Debugger

**Purpose:** Find why code is slow
**Best for:** Both
**Success rate:** Medium

### Prompt
```
This code is slower than expected:

```[language]
[CODE]
```

**Current performance:** [TIME/MEMORY]
**Expected performance:** [TARGET]
**Data size:** [SCALE]

Identify:
1. Performance bottlenecks
2. Why each is slow
3. How to optimize (in order of impact)
```

---

## Rubber Duck Prompt

**Purpose:** Think through a problem systematically
**Best for:** Both
**Success rate:** High

### Prompt
```
I'm stuck on a bug. Let me explain the situation, and help me think through it:

**The system:** [HIGH-LEVEL DESCRIPTION]
**What should happen:** [EXPECTED]
**What's happening:** [ACTUAL]
**My hypothesis:** [WHAT YOU THINK IS WRONG]

Ask me clarifying questions to help narrow down the cause.
```

---

## Quick Patterns

### Specific line focus
```
The bug is somewhere around line [N]. Here's the context:
[CODE SNIPPET]
What's wrong?
```

### Compare working vs broken
```
This works:
[WORKING CODE]

This doesn't:
[BROKEN CODE]

What's the difference that causes the failure?
```

### Intermittent bug
```
This code fails intermittently (about [X]% of the time).
[CODE]
What could cause non-deterministic behavior?
```

---

## Tags
`#debugging` `#proven` `#any-model`

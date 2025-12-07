# Prompt Engineering

The art and science of communicating effectively with AI systems.

## What is Prompt Engineering?

Prompt engineering is the practice of crafting inputs to AI systems that consistently produce useful outputs. It's part writing, part psychology, and part systematic experimentation.

---

## Core Techniques

### 1. Zero-Shot Prompting

Ask directly without examples. Works best for simple, well-defined tasks.

```
Write a Python function that checks if a number is prime.
```

**When to use:** Simple tasks, clear requirements, exploratory queries
**Limitations:** May not match your expected format or style

---

### 2. Few-Shot Prompting

Provide examples before your actual request. The AI learns the pattern.

```
Convert these sentences to formal English:

Input: "gonna grab coffee, brb"
Output: "I will get coffee and return shortly."

Input: "tbh this meeting could've been an email"
Output: "In my honest opinion, this meeting could have been conducted via email."

Input: "lmk when ur free"
Output:
```

**When to use:** Format matching, style consistency, pattern-based tasks
**Tip:** 2-3 examples usually sufficient; more can help for complex patterns

---

### 3. Chain-of-Thought (CoT)

Ask the AI to reason step-by-step. Dramatically improves complex problem-solving.

```
Solve this problem step by step:

A store has 45 apples. They sell 1/3 of them in the morning and 1/2 of what's
left in the afternoon. How many apples remain?

Think through each step before giving the final answer.
```

**When to use:** Math, logic, multi-step reasoning, debugging
**Variations:**
- "Let's think step by step"
- "Break this down into steps"
- "Show your reasoning"

---

### 4. Role/Persona Prompting

Assign expertise or perspective to shape the response.

```
You are a senior software architect with 15 years of experience in
distributed systems.

Review this microservices design and identify potential issues:
[design description]
```

**Effective roles:**
- Domain experts ("You are a tax attorney...")
- Perspectives ("You are a skeptical reviewer...")
- Audiences ("Explain this as if I'm a beginner...")

**When to use:** Need specialized knowledge, specific tone, or particular viewpoint

---

### 5. Structured Output

Control the format of responses explicitly.

```
Analyze this code for bugs. Respond in this exact JSON format:

{
  "bugs_found": [
    {
      "line": <number>,
      "severity": "critical|major|minor",
      "description": "<what's wrong>",
      "fix": "<how to fix it>"
    }
  ],
  "overall_quality": "<1-10 score>",
  "summary": "<one sentence>"
}
```

**Formats that work well:** JSON, XML, Markdown tables, numbered lists, YAML
**Tip:** Show the exact structure you want, including field names

---

## Intermediate Techniques

### 6. Prompt Templates

Create reusable structures for common tasks.

```
# Code Review Template

**Context:** [language/framework]
**Focus Areas:** [security/performance/readability/all]
**Code:**
```
[paste code]
```

**Please review for:**
1. Bugs and potential errors
2. [Focus area] concerns
3. Suggestions for improvement

Format as a prioritized list.
```

---

### 7. Prompt Chaining

Break complex tasks into sequential prompts.

**Chain example for technical writing:**
1. "Create an outline for documentation about [feature]"
2. "Expand section 1 of this outline: [outline]"
3. "Review this section for clarity and suggest improvements: [section]"
4. "Apply these improvements: [section + suggestions]"

**When to use:** Complex deliverables, quality-critical outputs, multi-stage work

---

### 8. Task Decomposition

Break complex requests into explicit subtasks.

```
Help me refactor this function. Let's do this in stages:

Stage 1: Identify what this function currently does
Stage 2: List the problems with the current implementation
Stage 3: Propose a refactored version
Stage 4: Explain the improvements

[paste function]

Start with Stage 1.
```

---

## Advanced Techniques

### 9. Meta-Prompting

Use AI to generate or improve prompts.

```
I want to use AI to help me write better error messages for my application.

Create a prompt template I can reuse that will:
- Take an error scenario as input
- Generate user-friendly error messages
- Include suggestions for resolution
- Match a professional but friendly tone
```

---

### 10. Self-Consistency

Generate multiple responses and synthesize.

```
Give me 3 different approaches to solve this problem:
[problem description]

For each approach, explain:
- How it works
- Pros and cons
- When to use it

Then recommend which approach is best for my situation: [context]
```

---

## Common Pitfalls

### Avoid These Mistakes

| Mistake | Why It's Bad | Better Approach |
|---------|--------------|-----------------|
| Vague requests | Vague outputs | Be specific |
| Multiple unrelated asks | Confused responses | One task at a time |
| No context | Generic answers | Provide background |
| Ambiguous terms | Misinterpretation | Define key terms |
| No format guidance | Inconsistent structure | Specify format |

---

## Practice Exercises

### Beginner
1. Take a simple task and write it three ways. Compare outputs.
2. Convert an unstructured prompt to use few-shot examples.
3. Add chain-of-thought to a math or logic problem.

### Intermediate
4. Create a prompt template for a task you do regularly.
5. Break a complex task into a 3-step prompt chain.
6. Use role prompting to get three different perspectives on a decision.

### Advanced
7. Use meta-prompting to create a prompt generator.
8. Design a prompt that produces consistent JSON for parsing.
9. Create a self-consistency prompt for a complex problem.

---

## Further Reading

- `../workflows/` — How to integrate prompting into work patterns
- `../output-quality/` — Getting better results from your prompts
- `../use-cases/` — Domain-specific prompting patterns

# Effective Prompts Collection

A growing library of prompt patterns that consistently produce good results.

---

## How to Use This File

1. **Browse** patterns when you're stuck
2. **Copy & adapt** for your specific use case
3. **Contribute** new patterns when you discover them
4. **Note** which model version you tested with

---

## Prompt Patterns

### 1. The Specific Request

**Problem:** Vague prompts get vague answers.

**Pattern:**
```
[Action verb] a [specific deliverable] that [key requirements].

Context: [relevant background]
Format: [desired output structure]
Constraints: [length, style, what to avoid]
```

**Example:**
```
Write a Python function that validates email addresses.

Context: This is for a user registration form in a Flask app.
Format: Single function with docstring and type hints.
Constraints: Use only standard library (no external packages).
Handle edge cases like empty strings and None values.
```

---

### 2. The Role Assignment

**Problem:** Generic responses that lack expertise depth.

**Pattern:**
```
You are a [specific role] with expertise in [domain].

Your task: [what they need to do]
Audience: [who will consume this]
Tone: [formal/casual/technical]
```

**Example:**
```
You are a senior security engineer with expertise in web application security.

Your task: Review this authentication code for vulnerabilities.
Audience: Junior developers who will fix the issues.
Tone: Direct and educational - explain WHY each issue matters.

[paste code]
```

---

### 3. The Few-Shot Pattern

**Problem:** Claude doesn't understand the format or style you want.

**Pattern:**
```
[Task description]

Examples:
Input: [example 1 input]
Output: [example 1 output]

Input: [example 2 input]
Output: [example 2 output]

Now do this one:
Input: [your actual input]
Output:
```

**Example:**
```
Convert these informal bug reports into structured tickets.

Examples:
Input: "the login is broken again smh"
Output:
- Title: Login functionality failure
- Priority: High
- Description: Users unable to complete login flow
- Steps to reproduce: [Needs clarification]

Input: "dark mode colors are ugly"
Output:
- Title: Dark mode color scheme feedback
- Priority: Low
- Description: User reports dissatisfaction with dark mode color palette
- Steps to reproduce: Enable dark mode in settings

Now do this one:
Input: "app crashes when I upload big files"
Output:
```

---

### 4. The Chain-of-Thought

**Problem:** Complex problems get superficial answers.

**Pattern:**
```
[Problem statement]

Think through this step by step:
1. First, identify [aspect 1]
2. Then, analyze [aspect 2]
3. Consider [potential issues]
4. Finally, provide [deliverable]

Show your reasoning at each step.
```

**Example:**
```
Debug why this function returns incorrect results for negative numbers.

Think through this step by step:
1. First, trace what happens when input is -5
2. Then, identify where the logic diverges from expected behavior
3. Consider edge cases the original author might have missed
4. Finally, provide the corrected code with explanation

Show your reasoning at each step.

[paste function]
```

---

### 5. The Structured Output

**Problem:** Unstructured responses that are hard to parse or use.

**Pattern:**
```
[Task description]

Respond in this exact format:
```json
{
  "field1": "description",
  "field2": ["item1", "item2"],
  "field3": {
    "nested": "value"
  }
}
```

**Example:**
```
Analyze this error message and provide debugging guidance.

Respond in this exact format:
```json
{
  "error_type": "category of error",
  "root_cause": "most likely cause",
  "quick_fixes": ["fix 1", "fix 2"],
  "diagnostic_steps": ["step 1", "step 2"],
  "prevention": "how to avoid this in future"
}
```

Error: [paste error]
```

---

### 6. The Constraint Sandwich

**Problem:** Outputs that miss requirements or include unwanted elements.

**Pattern:**
```
[Task]

Requirements:
- Must include: [required elements]
- Must avoid: [forbidden elements]
- Length: [specific constraint]
- Format: [structure requirement]

[Additional context if needed]
```

**Example:**
```
Write a commit message for these changes.

Requirements:
- Must include: What changed and why
- Must avoid: Generic phrases like "fixed bug" or "updated code"
- Length: Title under 50 chars, body under 200 chars
- Format: Conventional commits (feat/fix/docs/refactor)

Changes: [paste diff or description]
```

---

### 7. The Iterative Refinement

**Problem:** First output isn't quite right, need to guide improvements.

**Pattern:**
```
[Initial output from Claude]

This is good, but please adjust:
- [Specific change 1]
- [Specific change 2]

Keep everything else the same.
```

**Pro tip:** Be specific about what to change AND what to preserve.

---

### 8. The Comparison Request

**Problem:** Need to understand trade-offs between options.

**Pattern:**
```
Compare [option A] vs [option B] for [use case].

For each option, analyze:
- Pros
- Cons
- Best suited for
- Avoid when

Then recommend which to use for my situation: [your context]
```

---

### 9. The Artifact Trigger

**Problem:** Want Claude to create an artifact instead of inline code.

**Patterns that reliably trigger artifacts:**
```
"Create a React component that..."
"Build an interactive [thing]..."
"Make a visualization showing..."
"Generate a flowchart/diagram of..."
"Create a standalone [HTML page/app/tool]..."
```

**Patterns that usually stay inline:**
```
"Show me how to..." (explanation mode)
"What's the code for..." (snippet mode)
"Fix this code..." (modification mode)
```

---

### 10. The Context Dump

**Problem:** Claude lacks necessary background for good answers.

**Pattern:**
```
Context:
- Project: [what you're building]
- Stack: [technologies used]
- Current state: [where you are now]
- Goal: [where you want to be]

Problem: [specific issue]

Question: [what you need help with]
```

---

## Anti-Patterns to Avoid

### Don't: Be vague
```
❌ "Make this better"
✅ "Improve readability by adding comments and breaking into smaller functions"
```

### Don't: Ask multiple unrelated things
```
❌ "Review this code, also what's the best database, and can you write tests"
✅ [Ask each as a separate focused prompt]
```

### Don't: Assume context
```
❌ "Fix the bug" (what bug?)
✅ "Fix the null pointer exception on line 42 when user.email is undefined"
```

### Don't: Over-constrain creativity tasks
```
❌ "Write a story. It must be exactly 500 words, use only simple sentences..."
✅ "Write a short story (around 500 words) about..."
```

---

## Adding New Patterns

When you discover an effective prompt pattern:

1. **Name it** - Give it a memorable title
2. **Describe the problem** - When should someone use this?
3. **Show the pattern** - Generic template
4. **Provide an example** - Concrete usage
5. **Note the model** - Which Claude version you tested with

---

## Version Notes

Patterns may need adjustment as models update. Note when patterns were last verified:

| Pattern | Last Tested | Model | Status |
|---------|-------------|-------|--------|
| Specific Request | - | - | Needs testing |
| Role Assignment | - | - | Needs testing |
| Few-Shot | - | - | Needs testing |
| Chain-of-Thought | - | - | Needs testing |
| Structured Output | - | - | Needs testing |

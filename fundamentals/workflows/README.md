# AI Workflows

Patterns for integrating AI effectively into your work.

## The Core Principle

AI works best as a collaborator, not a replacement. The most effective workflows keep humans in control while leveraging AI's strengths.

---

## Fundamental Workflows

### 1. Iterative Refinement

The most common and useful pattern. Start broad, narrow down through conversation.

```
Round 1: "Write a function to parse dates"
Round 2: "Add support for ISO 8601 format"
Round 3: "Handle timezone conversion to UTC"
Round 4: "Add error handling for invalid inputs"
```

**Key principles:**
- Start with the core requirement
- Add constraints incrementally
- Be specific about what to change vs. keep
- Know when to start fresh vs. continue iterating

---

### 2. Draft-Review Cycle

AI generates, human reviews, AI refines.

```
Step 1: [AI] Generate initial draft
Step 2: [Human] Review, identify issues
Step 3: [AI] Address specific feedback
Step 4: [Human] Final review and polish
```

**Works well for:**
- Documentation
- Code generation
- Content writing
- Design proposals

**Anti-pattern:** Accepting AI output without review

---

### 3. Rubber Duck Debugging

Use AI as a thinking partner to work through problems.

```
"I'm trying to understand why my API returns 500 errors intermittently.

Here's what I know:
- It happens about 10% of requests
- Logs show timeout errors
- Database queries look normal

Talk me through possible causes and how to investigate each one."
```

**Key:** You're not asking AI to solve it — you're using it to structure your thinking

---

### 4. Research Synthesis

Gather information and synthesize into actionable insights.

```
Phase 1: "What are the main approaches to [topic]?"
Phase 2: "Compare approaches A and B in detail"
Phase 3: "For my use case [context], which approach fits best?"
Phase 4: "Create an implementation checklist for approach A"
```

**Important:** Verify claims, especially for factual/technical content

---

## Development Workflows

### 5. Code Generation Flow

```
┌─────────────┐
│ Requirements│
└──────┬──────┘
       ▼
┌─────────────┐
│ AI: Generate│
│ Initial Code│
└──────┬──────┘
       ▼
┌─────────────┐
│Human: Review│
│  & Test     │
└──────┬──────┘
       ▼
   ┌───┴───┐
   │Issues?│
   └───┬───┘
    Yes│   No
       ▼    ▼
┌──────────┐ ┌─────┐
│AI: Fix   │ │Done │
│Specific  │ └─────┘
│Problems  │
└────┬─────┘
     │
     └──────► (back to Review)
```

**Best practices:**
- Provide clear requirements upfront
- Review generated code thoroughly
- Test before integrating
- Keep changes focused

---

### 6. Code Review Workflow

```
"Review this code for:
1. Bugs and edge cases
2. Security vulnerabilities
3. Performance issues
4. Readability improvements

Prioritize findings by severity.

[code]"
```

**Follow-up patterns:**
- "Explain issue #2 in more detail"
- "Show me how to fix the security issue"
- "Are there any other concerns I should know about?"

---

### 7. Debugging Workflow

```
Stage 1: Describe the problem
"This function returns wrong results when [condition]"

Stage 2: Share context
[Code + error messages + what you've tried]

Stage 3: Guided investigation
"What are the most likely causes?"

Stage 4: Targeted fixes
"How do I fix [specific issue]?"

Stage 5: Verification
"Does this fix look correct? Any edge cases?"
```

---

## Writing Workflows

### 8. Outline-First Writing

```
Step 1: "Create an outline for [document type] about [topic]"
Step 2: "Expand the outline with key points for each section"
Step 3: [Human] Review and adjust structure
Step 4: "Write section 1 based on this outline: [outline]"
Step 5: [Human] Edit and refine
Step 6: Repeat for remaining sections
```

---

### 9. Tone Matching

```
"Here's an example of our company's writing style:
[sample text]

Write [new content] matching this tone and style."
```

**Variations:**
- "Make this more formal/casual"
- "Simplify this for a non-technical audience"
- "Make this more concise"

---

## Decision Support Workflows

### 10. Structured Analysis

```
"I need to decide between [option A] and [option B] for [context].

Analyze both options:
1. Pros of each
2. Cons of each
3. Risks to consider
4. What factors should influence the decision?

Don't make the decision for me — help me think through it."
```

**Important:** AI provides analysis; human makes decisions

---

### 11. Devil's Advocate

```
"I'm planning to [decision/approach].

Play devil's advocate:
- What could go wrong?
- What am I not considering?
- Why might this be the wrong choice?

Be genuinely critical, not just surface-level."
```

---

## Workflow Anti-Patterns

### What NOT to Do

| Anti-Pattern | Problem | Better Approach |
|--------------|---------|-----------------|
| "Do everything" | Overwhelms AI, poor results | Break into steps |
| Blind acceptance | Errors slip through | Always review |
| No context | Generic outputs | Provide background |
| Starting over constantly | Loses progress | Iterate on good starts |
| Over-automation | Removes human judgment | Keep human in loop |

---

## Workflow Selection Guide

| Task Type | Recommended Workflow |
|-----------|---------------------|
| New code | Code Generation Flow |
| Bug fixing | Debugging Workflow |
| Documentation | Outline-First Writing |
| Code quality | Code Review Workflow |
| Learning | Rubber Duck / Research |
| Decisions | Structured Analysis |
| Quick tasks | Iterative Refinement |

---

## Building Your Own Workflows

### Template for Custom Workflows

```
Workflow: [Name]
Purpose: [What problem does this solve?]

Steps:
1. [Human/AI] [Action]
2. [Human/AI] [Action]
3. [Human/AI] [Action]

Checkpoints:
- After step N, verify [quality criterion]

Exit criteria:
- [When is the workflow complete?]
```

---

## Practice Exercises

### Beginner
1. Use iterative refinement to write a function through 4+ turns
2. Apply the draft-review cycle to a piece of documentation
3. Use rubber duck debugging on a real problem you're facing

### Intermediate
4. Build a complete feature using the code generation flow
5. Create a custom workflow for a task you do regularly
6. Use devil's advocate before making a real decision

### Advanced
7. Chain multiple workflows for a complex project
8. Design a workflow that involves multiple AI tools
9. Create a team workflow that includes AI checkpoints

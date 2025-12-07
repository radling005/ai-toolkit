# Context Management

Optimizing the information you provide to AI systems.

## Why Context Matters

AI models have limited "memory" (context window). What you include—and exclude—dramatically affects output quality. Good context management is the difference between generic answers and precisely useful ones.

---

## Core Concepts

### Context Windows

Every AI has a maximum amount of text it can process at once.

| Model Type | Typical Context | Rough Word Count |
|------------|-----------------|------------------|
| Smaller models | 4K-8K tokens | ~3,000-6,000 words |
| Standard models | 32K-128K tokens | ~24,000-96,000 words |
| Extended context | 200K+ tokens | ~150,000+ words |

**Token ≠ Word:** Tokens are word pieces. Roughly 1 token ≈ 0.75 words in English.

---

### Information Hierarchy

Not all context is equal. Prioritize:

```
1. [CRITICAL]  - What you're asking for
2. [IMPORTANT] - Directly relevant context
3. [HELPFUL]   - Background that improves quality
4. [OPTIONAL]  - Nice to have if space permits
```

**Example for code review:**
```
[CRITICAL]  The code to review
[CRITICAL]  Specific concerns to address
[IMPORTANT] Related code it interacts with
[HELPFUL]   Project conventions/style guide
[OPTIONAL]  History of why code exists
```

---

## Practical Techniques

### 1. The Minimal Context Principle

Start with less context. Add more only if needed.

**Wrong approach:**
"Here's my entire codebase, find the bug"

**Right approach:**
"This function throws an error on line 15. Here's the function and the error message."

---

### 2. Strategic Summarization

Condense background information to save tokens.

**Instead of:** Full 50-page document

**Provide:**
```
Summary of Document X:
- Main topic: [1 sentence]
- Key points: [3-5 bullets]
- Relevant section: [paste only what's needed]
```

---

### 3. Structured Context Blocks

Organize context so AI can navigate it.

```
## Background
[Brief project context]

## Current State
[What exists now]

## Problem
[What's wrong or needed]

## Constraints
[Limitations to consider]

## Request
[What you want AI to do]
```

---

### 4. Reference Anchoring

Give names to things you'll refer to later.

```
I have two approaches I'm considering:

APPROACH A: Use a database trigger
- Pros: Automatic, centralized
- Cons: Hidden logic, harder to debug

APPROACH B: Handle in application code
- Pros: Explicit, testable
- Cons: Must remember to call it

Which approach would you recommend for [use case]?

[Later in conversation]
"Tell me more about implementing APPROACH A"
```

---

### 5. Progressive Disclosure

Reveal context in stages as needed.

```
Turn 1: "How do I optimize this SQL query?"
Turn 2: "The table has 10M rows and these indexes: [...]"
Turn 3: "Here's the EXPLAIN plan: [...]"
Turn 4: "We can't change the schema, only the query"
```

---

## Context Patterns

### The Sandwich Pattern

Put critical info at the beginning AND end.

```
[CRITICAL INSTRUCTION]

[Background context...]
[More details...]
[Supporting information...]

[REMINDER OF CRITICAL INSTRUCTION]
```

AI models pay more attention to the start and end.

---

### The Focus Pattern

Explicitly direct attention.

```
I'm going to share a large code file. Focus specifically on:
1. The `processPayment` function (lines 145-200)
2. Error handling patterns
3. Any security concerns

Ignore styling, comments, and other functions.

[code]
```

---

### The Diff Pattern

Show changes, not entire files.

**Instead of:** Two complete versions of a file

**Provide:**
```
Original:
```python
def calculate(x):
    return x * 2
```

Changed to:
```python
def calculate(x, multiplier=2):
    return x * multiplier
```

Question: Does this change handle edge cases properly?
```

---

## Managing Long Conversations

### Session State Management

For multi-turn conversations, periodically summarize.

```
"Let me summarize where we are:
- We decided to use approach A
- We've implemented the core logic
- Current issue: error handling for edge case X

Does this match your understanding?"
```

---

### Fresh Start vs. Continue

**Continue when:**
- Building on previous work
- AI has useful context
- Conversation is still focused

**Fresh start when:**
- Conversation has drifted
- You're on a new topic
- AI seems confused or stuck

---

### Context Recovery

If AI loses track:
```
"Let me re-establish context:
- Project: [brief description]
- Current file: [filename]
- What we're doing: [task]
- Last decision: [what was decided]

Now, continuing from there..."
```

---

## Common Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| Too much context | Dilutes focus, hits limits | Prioritize, summarize |
| Too little context | Generic responses | Add relevant background |
| Unstructured dump | AI can't find key info | Organize with headers |
| Stale context | Previous turns mislead | Summarize or start fresh |
| Irrelevant details | Distracts from task | Focus only on what's needed |

---

## Context Budgeting

For complex tasks, plan your context budget:

```
Available: ~100K tokens

Budget allocation:
- System instructions: 5%
- Background context: 15%
- Main content (code/document): 60%
- Examples: 10%
- Request & constraints: 10%
```

---

## Advanced: RAG Concepts

Retrieval-Augmented Generation adds relevant context automatically.

**Basic RAG flow:**
1. User asks question
2. System searches knowledge base
3. Relevant chunks retrieved
4. Chunks added to context
5. AI answers with retrieved info

**Key insight:** You can manually do RAG by searching your own docs and pasting relevant sections.

---

## Practice Exercises

### Beginner
1. Take a large document and create a 5-bullet summary for AI context
2. Reorganize a messy prompt using the structured context blocks pattern
3. Try the same question with minimal vs. detailed context—compare results

### Intermediate
4. Practice the progressive disclosure pattern on a complex problem
5. Use reference anchoring in a multi-option decision discussion
6. Implement the sandwich pattern for a complex request

### Advanced
7. Manage a 10+ turn conversation using state management
8. Create a context budget for a large document analysis task
9. Design a manual RAG workflow for your own knowledge base

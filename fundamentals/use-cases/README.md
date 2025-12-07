# Use Cases

Domain-specific patterns and best practices for common AI applications.

## Overview

While fundamental techniques transfer across domains, each use case has specific patterns that work best. This section covers practical applications.

---

## Code Generation

### The Pattern

```
Write [language] code that [specific behavior].

Requirements:
- [Requirement 1]
- [Requirement 2]

Context: [Where this code will be used]

Include: [error handling / tests / documentation / type hints]
```

### Best Practices

1. **Be specific about behavior** — Not "handle errors" but "raise ValueError for invalid input"
2. **Specify the environment** — Language version, framework, dependencies
3. **Include examples** — Input/output examples clarify expectations
4. **Request incrementally** — Core logic first, then edge cases

### Example

```
Write a Python function that validates email addresses.

Requirements:
- Must contain exactly one @ symbol
- Domain must have at least one dot
- No spaces allowed
- Return True/False

Context: User registration form validation

Include: Type hints and a docstring with examples
```

---

## Code Review

### The Pattern

```
Review this [language] code for:
1. Bugs and potential errors
2. [Security / Performance / Readability] issues
3. Suggestions for improvement

Prioritize by severity: Critical > Major > Minor

[code]
```

### Best Practices

1. **Specify focus areas** — What matters most for this code?
2. **Provide context** — What does this code do? What's its role?
3. **Ask follow-up questions** — Deep dive on specific issues
4. **Request fixes** — "Show me how to fix issue #2"

---

## Technical Writing

### The Pattern

```
Write [document type] about [topic].

Audience: [Who will read this]
Purpose: [What readers should learn/do]
Tone: [Technical/Approachable/Formal]
Length: [Approximate length]

Include:
- [Required sections]

Avoid:
- [What to exclude]
```

### Document Types

| Type | Key Elements |
|------|--------------|
| **README** | Purpose, setup, usage, examples |
| **Tutorial** | Steps, explanations, outcomes |
| **API docs** | Endpoints, parameters, responses |
| **Architecture** | Components, interactions, decisions |
| **Runbook** | Steps for operational tasks |

---

## Creative Writing

### The Pattern

```
Write [format] about [topic/theme].

Style: [Voice, tone, genre]
Length: [Word count / pages]
Audience: [Who will read this]

Include: [Elements to incorporate]
Avoid: [What not to include]
```

### Tips

- Provide style examples if you have specific voice in mind
- Be flexible — AI creativity benefits from room to explore
- Iterate on drafts rather than expecting perfection
- Focus feedback on specific elements

---

## Data Analysis

### The Pattern

```
Analyze this data:
[data or description of data]

Questions:
1. [Specific question]
2. [Specific question]

Format results as: [table / bullet points / narrative]

Include insights about: [what patterns to look for]
```

### With Code Execution

```
I'm uploading a CSV file with [description].

Please:
1. Load and preview the data
2. Calculate [specific metrics]
3. Create a visualization showing [what to visualize]
4. Summarize key findings

Run the code and show me the results.
```

---

## Research Synthesis

### The Pattern

```
Research [topic] and provide:

1. Overview (2-3 sentences)
2. Key approaches/schools of thought
3. Pros and cons of each
4. Current consensus (if any)
5. What's still debated

For factual claims, indicate confidence level.
```

### Best Practices

1. **Verify claims** — AI can hallucinate sources
2. **Ask for uncertainty** — "What are you less sure about?"
3. **Use search grounding** — When available, request current information
4. **Cross-reference** — Check claims against known sources

---

## Learning & Explanation

### The Pattern

```
Explain [concept] as if I'm [expertise level].

Start with: [What to cover first]
Include: [Examples / analogies / diagrams]
Avoid: [Jargon / assumptions]

After explaining, give me a simple question to check my understanding.
```

### Levels

| Level | Approach |
|-------|----------|
| **Beginner** | Analogies, no jargon, lots of examples |
| **Intermediate** | Some technical terms, more depth |
| **Expert** | Full technical detail, edge cases |

---

## Brainstorming

### The Pattern

```
Generate [number] ideas for [challenge/goal].

Context: [Relevant background]
Constraints: [Limitations to work within]

For each idea:
- Brief description
- Why it might work
- Potential challenges
```

### Expanding Ideas

```
Take idea #3 and:
1. Develop it further
2. Identify implementation steps
3. List what could go wrong
4. Suggest how to validate it
```

---

## Summarization

### The Pattern

```
Summarize this [document type]:

Length: [Sentence count / word limit / bullet points]
Focus on: [What aspects matter most]
Format: [Narrative / bullets / structured sections]
Audience: [Who needs this summary]

[content to summarize]
```

### Summarization Levels

| Level | Use Case |
|-------|----------|
| **TL;DR** | 1-2 sentences, key takeaway |
| **Executive** | 3-5 bullets, main points |
| **Detailed** | Paragraph per section |
| **Structured** | Organized by categories |

---

## Translation & Localization

### The Pattern

```
Translate this [content type] from [source] to [target].

Maintain: [Tone / technical accuracy / style]
Audience: [Who will read translation]
Context: [Where this will be used]

Flag: Any terms that might need localization beyond translation.
```

### Beyond Translation

- **Cultural adaptation** — Idioms, examples, references
- **Technical terms** — Industry-standard translations
- **Formatting** — Date formats, number formats, etc.

---

## Debugging Assistance

### The Pattern

```
Help me debug this issue:

What I expect: [Expected behavior]
What happens: [Actual behavior]
Error message: [If any]

Code:
[relevant code]

I've already tried:
- [What you've attempted]
```

### Follow-up Patterns

- "What should I check first?"
- "Explain why that fix works"
- "What other issues might this cause?"
- "How can I prevent this in the future?"

---

## General Tips

### For All Use Cases

1. **Start specific** — You can always broaden
2. **Iterate** — First output is rarely final
3. **Provide context** — What's this for?
4. **Set constraints** — Boundaries improve output
5. **Request format** — Structure helps usability

### Matching AI to Task

| Task | Best AI Features |
|------|------------------|
| Current events | Search grounding |
| Code execution | Runtime environment |
| Long documents | Large context window |
| Quick queries | Fast models |
| Complex reasoning | Stronger models |

---

## Practice Exercises

### Beginner
1. Use the code generation pattern to create a utility function
2. Summarize a long article at three different levels
3. Get an explanation of a concept at your learning level

### Intermediate
4. Do a full code review workflow with follow-up questions
5. Research a topic and verify 3 specific claims
6. Brainstorm ideas and develop the best one further

### Advanced
7. Create a complete technical document using the outline-first method
8. Do a multi-step data analysis with visualizations
9. Design a custom workflow combining multiple use cases

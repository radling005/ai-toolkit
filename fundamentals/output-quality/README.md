# Output Quality

Techniques for getting consistently good results from AI.

## The Quality Mindset

Good AI outputs don't happen by accident. They result from clear communication, appropriate expectations, and systematic refinement.

---

## Quality Fundamentals

### 1. Specificity is Everything

The #1 predictor of output quality is prompt specificity.

**Vague (poor results):**
```
Write some code to handle users.
```

**Specific (good results):**
```
Write a Python class called UserManager that:
- Stores users in a dictionary keyed by user_id
- Has methods: add_user(id, name, email), get_user(id), delete_user(id)
- Raises ValueError if user_id already exists on add
- Returns None if user not found on get
- Include type hints and docstrings
```

---

### 2. Setting Constraints

Boundaries improve output. Tell AI what to do AND what not to do.

**Useful constraints:**
- **Length:** "In 2-3 paragraphs" / "Under 100 words"
- **Format:** "As a markdown table" / "As valid JSON"
- **Style:** "Professional but approachable" / "Technical and precise"
- **Scope:** "Focus only on X" / "Don't include Y"
- **Audience:** "For beginners" / "For senior developers"

**Example:**
```
Explain how HTTPS works.

Constraints:
- For someone who understands HTTP but not cryptography
- Under 200 words
- No analogies about locks and keys
- Include a simple diagram in ASCII
```

---

### 3. Quality Criteria

Define what "good" means before you ask.

```
Write unit tests for this function.

Quality criteria:
- Cover happy path and edge cases
- Test boundary conditions
- Each test should test one thing
- Use descriptive test names
- Include at least one test that should fail with bad input
```

---

## Consistency Techniques

### 4. Template-Based Prompting

Same structure → consistent outputs.

```
# Bug Report Analysis Template

Bug: [description]
Environment: [details]

Analyze this bug and provide:
1. **Most likely cause** (1 sentence)
2. **Investigation steps** (numbered list)
3. **Potential fixes** (bullet points)
4. **Prevention** (how to avoid in future)
```

Using templates ensures you always get the same sections in the same order.

---

### 5. Example-Driven Quality

Show the quality level you expect.

```
Summarize articles in this style:

Example:
Article: [long article about climate change]
Summary: "Rising global temperatures are accelerating ice sheet melt,
with new data suggesting sea levels could rise 30cm by 2050—double
previous estimates. Coastal cities face urgent adaptation decisions."

Now summarize this article:
[new article]
```

---

### 6. Explicit Formatting

Leave nothing to interpretation.

```
Format your response exactly like this:

## Summary
[2-3 sentences]

## Key Points
- [point 1]
- [point 2]
- [point 3]

## Recommendation
[1 sentence recommendation]

## Confidence
[High/Medium/Low] - [why]
```

---

## Handling Hallucinations

### 7. Recognizing Fabrication

AI can confidently state false information. Watch for:

- **Specific numbers** without sources (statistics, dates, measurements)
- **Named entities** you can't verify (people, papers, products)
- **Technical details** that seem plausible but might be wrong
- **URLs and citations** (often fabricated)

### 8. Verification Strategies

```
"For any factual claims in your response:
- Indicate your confidence level (high/medium/low)
- Note which claims I should verify independently
- Don't make up statistics—say 'I don't have exact figures' instead"
```

### 9. Asking for Uncertainty

```
"Answer this question. If you're not sure about something:
- Say so explicitly
- Explain what you'd need to verify
- Give your best guess labeled as such"
```

---

## Quality Improvement Tactics

### 10. The Improvement Loop

```
Step 1: Get initial output
Step 2: Identify specific issues
Step 3: Request targeted fixes

"This is good, but:
- The introduction is too long—cut it in half
- Add more detail in section 2 about error handling
- The tone in section 3 is too casual—make it professional

Keep everything else the same."
```

### 11. Asking for Alternatives

```
"Give me 3 different ways to approach this problem.
For each:
- Brief description
- Pros
- Cons

Then recommend which to use for [my context]."
```

### 12. Self-Critique

```
"[After receiving output]

Now critique your own response:
- What could be improved?
- What assumptions did you make?
- What edge cases might this miss?"
```

---

## Common Quality Issues & Fixes

| Issue | Symptom | Fix |
|-------|---------|-----|
| Too verbose | Walls of text | Add length constraints |
| Too generic | Vague advice | Provide specific context |
| Wrong format | Hard to parse | Show exact format wanted |
| Missing details | Incomplete | List required elements |
| Wrong tone | Too casual/formal | Specify audience and style |
| Hallucinations | False facts | Ask for uncertainty, verify |
| Off-topic | Tangents | Focus the scope explicitly |

---

## Quality Checklist

Before accepting AI output, verify:

- [ ] **Accuracy:** Are facts correct?
- [ ] **Completeness:** Is anything missing?
- [ ] **Relevance:** Does it address the actual need?
- [ ] **Format:** Is it structured as requested?
- [ ] **Tone:** Is it appropriate for the audience?
- [ ] **Actionability:** Can you use it as-is?

---

## Practice Exercises

### Beginner
1. Take a vague prompt, rewrite it with specificity, compare outputs
2. Add 3 constraints to an existing prompt, see how output changes
3. Ask for the same thing with and without an example—compare quality

### Intermediate
4. Create a template for a task you do often, test consistency
5. Get an output, identify 3 issues, request specific fixes
6. Practice asking for uncertainty on factual questions

### Advanced
7. Design a quality rubric for a specific use case
8. Create a prompt that consistently produces parseable JSON
9. Develop a fact-checking workflow for AI-generated content

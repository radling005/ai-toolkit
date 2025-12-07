# Failure Museum

A collection of spectacular AI failures and what they taught us.

## Why Document Failures?

> "I have not failed. I've just found 10,000 ways that won't work." — Edison

Failures are more instructive than successes because they reveal:
- Limits of AI capabilities
- Prompting anti-patterns
- Edge cases to watch for
- How to recover when things go wrong

**The goal isn't to avoid failure—it's to fail forward.**

---

## Hall of Fame Failures

Document your most educational failures here. These become your best teachers.

---

## Failure Template

```markdown
# Failure: [Descriptive Name]

**Date:** YYYY-MM-DD
**Model:** Claude / Gemini / Other
**Category:** Hallucination / Misunderstanding / Wrong Output / Refusal / Loop / Other

## What I Was Trying To Do
[The goal]

## What I Prompted
```
[Exact prompt]
```

## What Went Wrong
[Description of the failure]

## The Output (or lack thereof)
```
[What the AI actually produced]
```

## Why It Failed
[Your analysis of what caused this]

## What I Learned
- [Lesson 1]
- [Lesson 2]

## How To Avoid This
[Preventive measures for next time]

## Recovery (if any)
[How you eventually succeeded, if you did]

## Tags
`#hallucination` `#prompt-fail` `#edge-case` `#model-limitation`
```

---

## Failure Categories

### 🎭 Hallucinations
AI confidently stating false information.

**Common types:**
- Fabricated citations, papers, quotes
- Non-existent APIs, functions, libraries
- Wrong technical details that sound right
- Made-up statistics and dates

**Prevention:**
- Always verify factual claims
- Ask AI to indicate confidence
- Use search grounding when available
- Cross-reference important facts

---

### 🤷 Misunderstandings
AI interpreted the request differently than intended.

**Common causes:**
- Ambiguous wording
- Missing context
- Different interpretation of terms
- Assumed knowledge that was wrong

**Prevention:**
- Be specific and explicit
- Define important terms
- Provide examples of desired output
- Ask AI to confirm understanding first

---

### 🔄 Loops and Repetition
AI gets stuck repeating itself or going in circles.

**Common patterns:**
- Same response to different prompts
- Circular reasoning
- Restating the problem without solving
- Repeating mistakes after correction

**Prevention:**
- Start fresh when stuck
- Change approach significantly
- Be more explicit about what's wrong
- Break the problem down differently

---

### 🚫 Refusals
AI refuses a reasonable request.

**Common causes:**
- Triggered safety heuristics
- Misidentified intent
- Overly cautious interpretation
- Edge cases in content policy

**Prevention:**
- Provide context about legitimate purpose
- Rephrase without trigger words
- Break into smaller, less concerning parts
- Try a different model

---

### 📏 Format Failures
Output doesn't match requested structure.

**Common issues:**
- Wrong format despite clear instructions
- Missing required sections
- Extra content not requested
- Inconsistent formatting

**Prevention:**
- Show exact format with examples
- Use structured output patterns
- Be explicit about what to exclude
- Validate output structure

---

### 💥 Code Failures
Generated code doesn't work.

**Common issues:**
- Syntax errors
- Logic bugs
- Non-existent functions/APIs
- Wrong language version assumptions
- Security vulnerabilities

**Prevention:**
- Always test generated code
- Specify language version and environment
- Ask for explanation of approach
- Request error handling explicitly

---

## Failure Patterns to Watch For

| Pattern | Warning Sign | What to Do |
|---------|--------------|------------|
| Confident wrongness | Very specific but unverified | Fact-check |
| Assumption cascade | Building on unstated assumptions | Clarify context |
| Complexity collapse | Oversimplifying hard problems | Break down further |
| Context amnesia | Forgetting earlier conversation | Summarize state |
| Format drift | Structure deteriorating | Reinforce format |
| Sycophancy | Just agreeing with you | Ask for pushback |

---

## Learning from Failures

After each failure, ask:

1. **What was the root cause?**
   - My prompt? AI limitation? Edge case?

2. **Was this preventable?**
   - What would have caught this earlier?

3. **What's the pattern?**
   - Have I seen similar failures?

4. **What's the fix?**
   - For this instance and future prevention

5. **Is this a new category?**
   - Worth adding to my watch list?

---

## Failure Review Ritual

Monthly, review your failures:

- [ ] What types are most common?
- [ ] Are there patterns in my prompting?
- [ ] Which failures taught the most?
- [ ] What should I do differently?
- [ ] Are there new failure modes emerging?

---

## The Failure Mindset

**Embrace failures as data:**
- Every failure reveals something
- Documented failures help others
- Patterns emerge from collections
- Recovery skills are valuable

**Share your failures:**
- They're often more valuable than successes
- Others are making the same mistakes
- The community learns faster together

---

## File Organization

```
failures/
├── README.md (this file)
├── hallucinations/
│   └── 2024-01-15-fake-api.md
├── misunderstandings/
│   └── 2024-01-18-wrong-interpretation.md
├── code-failures/
│   └── 2024-01-20-syntax-bug.md
└── recovery-stories/
    └── 2024-01-22-how-i-fixed-it.md
```

---

## Remember

The best AI users aren't those who never fail—they're those who fail productively and learn fast.

**Your failures are valuable. Document them.**

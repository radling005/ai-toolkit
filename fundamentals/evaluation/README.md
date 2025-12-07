# Evaluation

Measuring and comparing AI performance systematically.

## Why Evaluation Matters

Without evaluation, you can't:
- Know if prompt changes actually help
- Compare different approaches objectively
- Build reliable, repeatable workflows
- Improve over time

---

## Basic Evaluation

### Side-by-Side Comparison

The simplest approach: compare outputs directly.

```
Prompt A Output:
[result]

Prompt B Output:
[result]

Which is better for [your criteria]?
```

### Quick Evaluation Questions

For any AI output, ask:
1. **Accurate?** — Is the information correct?
2. **Complete?** — Is anything missing?
3. **Relevant?** — Does it address the actual need?
4. **Usable?** — Can I use this as-is?
5. **Appropriate?** — Right tone, format, level?

---

## Creating Rubrics

### What is a Rubric?

A scoring guide that defines quality levels for specific criteria.

### Basic Rubric Template

```
Criterion: [What you're measuring]

5 - Excellent: [Description of excellent performance]
4 - Good: [Description of good performance]
3 - Adequate: [Description of adequate performance]
2 - Poor: [Description of poor performance]
1 - Unacceptable: [Description of unacceptable performance]
```

### Example: Code Quality Rubric

```
Criterion: Code Correctness

5 - Code works correctly for all inputs, including edge cases
4 - Code works for typical inputs, minor edge case issues
3 - Code works for happy path, some bugs present
2 - Code has significant bugs, partially functional
1 - Code doesn't run or is completely wrong
```

### Multi-Criteria Rubric

| Criterion | Weight | Score (1-5) | Weighted |
|-----------|--------|-------------|----------|
| Correctness | 40% | | |
| Readability | 25% | | |
| Performance | 20% | | |
| Documentation | 15% | | |
| **Total** | 100% | | |

---

## A/B Testing Prompts

### The Method

1. Define success criteria
2. Create two prompt variants
3. Test both on same inputs
4. Score outputs using rubric
5. Analyze which performs better

### Testing Template

```
Test Name: [Descriptive name]
Date: [Date]
Input Set: [What you're testing on]

Prompt A:
[prompt text]

Prompt B:
[prompt text]

Results:
| Input | A Score | B Score | Notes |
|-------|---------|---------|-------|
| 1 | | | |
| 2 | | | |
| 3 | | | |

Analysis:
- Prompt A average: [score]
- Prompt B average: [score]
- Winner: [A/B/Tie]
- Why: [explanation]
```

### Best Practices

- Test on **multiple diverse inputs** — Not just one example
- **Blind evaluation** when possible — Score without knowing which prompt
- **Change one thing** at a time — Isolate what matters
- **Document everything** — Build knowledge over time

---

## Benchmark Creation

### What is a Benchmark?

A standardized set of test cases for consistent evaluation.

### Benchmark Components

```
Benchmark: [Name]
Purpose: [What it measures]
Version: [Version number]

Test Cases:
1. Input: [input]
   Expected: [what good output looks like]
   Evaluation: [how to score]

2. Input: [input]
   Expected: [what good output looks like]
   Evaluation: [how to score]

[...more test cases]

Scoring:
- Pass: [criteria]
- Partial: [criteria]
- Fail: [criteria]
```

### Example: Summarization Benchmark

```
Benchmark: Article Summarization Quality
Purpose: Evaluate summary accuracy and conciseness

Test Case 1:
Input: [500-word article about climate change]
Expected: Summary captures main claim, supporting evidence, and conclusion
Evaluation:
- Key points captured (0-3 points)
- Length appropriate (0-1 point)
- No hallucinated information (0-1 point)

[Additional test cases with diverse articles]
```

---

## Blind Evaluation

### The Problem

When you know which output came from which prompt, you're biased.

### Blind Evaluation Process

1. Generate outputs from different prompts/models
2. Remove identifying information
3. Randomize order
4. Score without knowing source
5. Reveal sources after scoring

### Practical Implementation

```
# Have AI randomize outputs
"I'm going to give you outputs from two different prompts.
Label them randomly as Output A and Output B.
Don't tell me which is which until I've scored them.

Output 1: [from prompt X]
Output 2: [from prompt Y]"

[Score outputs]

"Now reveal which was which."
```

---

## Regression Testing

### Purpose

Ensure quality doesn't degrade when you:
- Update prompts
- Change models
- Modify workflows

### Regression Test Suite

```
Test Suite: [Name]
Last Passed: [Date]
Model: [Model version]

Test 1: [Description]
- Input: [standard input]
- Expected behavior: [what should happen]
- Pass criteria: [specific criteria]
- Current status: [Pass/Fail]

Test 2: [Description]
[...]
```

### When to Run

- After any prompt changes
- When switching models
- After model updates
- Periodically as baseline check

---

## Quantitative Metrics

### For Text Generation

| Metric | What It Measures | When to Use |
|--------|------------------|-------------|
| Length | Output size | Format compliance |
| Similarity | Match to reference | Consistency |
| Keyword presence | Contains required terms | Completeness |
| Structure | Follows format | Template adherence |

### For Code Generation

| Metric | What It Measures | When to Use |
|--------|------------------|-------------|
| Runs without error | Basic correctness | Minimum bar |
| Passes tests | Functional correctness | Quality check |
| Cyclomatic complexity | Code complexity | Maintainability |
| Time/space | Performance | Efficiency |

---

## Qualitative Assessment

### Expert Review

When metrics aren't enough, use structured expert evaluation.

```
Expert Review Template:

Reviewer: [Name]
Output reviewed: [ID]

Assessment:
1. Does this meet the stated requirements? [Y/N/Partial]
2. Would you use this as-is? [Y/N/With modifications]
3. What's missing or wrong? [List]
4. Overall quality: [1-5]
5. Free-form notes: [Comments]
```

### User Testing

For user-facing outputs:
1. Share with target audience
2. Gather structured feedback
3. Track completion rates
4. Measure satisfaction

---

## Evaluation Workflow

### For Prompt Development

```
1. Define success criteria
2. Create initial prompt
3. Generate test outputs
4. Score against criteria
5. Identify weaknesses
6. Modify prompt
7. Re-test
8. Compare to baseline
9. Document findings
10. Deploy or iterate
```

### For Model Comparison

```
1. Select test cases
2. Run same prompts on each model
3. Blind-score outputs
4. Calculate aggregate scores
5. Analyze strengths/weaknesses
6. Document recommendations
```

---

## Common Evaluation Mistakes

| Mistake | Problem | Solution |
|---------|---------|----------|
| Single test case | Not representative | Use diverse test set |
| Subjective scoring | Inconsistent | Use detailed rubric |
| Knowing the source | Bias | Blind evaluation |
| No baseline | Can't measure improvement | Establish baseline first |
| Changing multiple variables | Can't isolate cause | Change one thing at a time |

---

## Building Evaluation Into Your Practice

### Minimum Viable Evaluation

For every prompt change:
1. Test on at least 3 inputs
2. Score against basic criteria
3. Compare to previous version
4. Document the comparison

### Periodic Deep Evaluation

Monthly or quarterly:
1. Run full benchmark suite
2. Review accumulated findings
3. Update prompts based on learnings
4. Refresh benchmarks if needed

---

## Practice Exercises

### Beginner
1. Create a 3-criterion rubric for a task you do often
2. Do a side-by-side comparison of two prompt variations
3. Score 5 AI outputs using your rubric

### Intermediate
4. Build a 10-case benchmark for a specific use case
5. Conduct a blind evaluation of prompt variants
6. Track quality over a week of AI usage

### Advanced
7. Create a regression test suite for a workflow
8. Design a multi-evaluator assessment process
9. Build automated quality checks for structured outputs

# Edge Cases & Limitations

Document Claude's boundaries, limitations, and unexpected behaviors here.

## What to Track

### Limitations
- Tasks where Claude consistently struggles
- Quality degradation with long contexts
- Inconsistent outputs for similar prompts

### Safety Boundaries
- Types of requests that get refused
- How to rephrase legitimate requests appropriately
- Understanding vs circumventing (focus on understanding)

### Accuracy Issues
- Topics where Claude is confidently wrong
- Knowledge cutoff edge cases
- Hallucination patterns

## File Naming Convention

```
YYYY-MM-DD-brief-description.md
```

Examples:
- `2024-01-15-math-reasoning-limits.md`
- `2024-01-20-code-context-degradation.md`
- `2024-02-01-refusal-patterns.md`

## Template

```markdown
# [Issue Title]

**Date:** YYYY-MM-DD
**Model:** Claude 3.5 Sonnet
**Category:** Limitation / Safety / Accuracy

## Description
What happened?

## Reproduction
Steps or prompt to reproduce

## Expected vs Actual
What should have happened vs what did happen

## Workaround (if found)
Any solutions discovered

## Notes
Additional observations
```

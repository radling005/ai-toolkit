# Edge Cases & Limitations

Document Gemini's boundaries, limitations, and unexpected behaviors here.

## What to Track

### Limitations
- Tasks where Gemini consistently struggles
- Quality differences between Pro/Flash/Ultra
- Inconsistent outputs for similar prompts
- Code execution environment limitations

### Search Grounding Issues
- When grounding fails or provides outdated info
- Inaccurate citations or broken sources
- Topics where grounding is unreliable
- Comparison: grounded vs non-grounded accuracy

### Safety Boundaries
- Types of requests that get refused
- How to rephrase legitimate requests appropriately
- Understanding vs circumventing (focus on understanding)

### Accuracy Issues
- Topics where Gemini is confidently wrong
- Hallucination patterns
- Knowledge cutoff edge cases
- Multi-modal interpretation errors

### Code Execution Issues
- Package/library limitations
- Timeout or resource limits
- Visualization rendering problems
- Data handling quirks

## File Naming Convention

```
YYYY-MM-DD-brief-description.md
```

Examples:
- `2024-01-15-search-grounding-outdated.md`
- `2024-01-20-code-execution-timeout.md`
- `2024-02-01-image-analysis-errors.md`

## Template

```markdown
# [Issue Title]

**Date:** YYYY-MM-DD
**Model:** Gemini Pro / Flash / Ultra
**Feature:** Standard / Search Grounding / Code Execution / Multi-modal
**Category:** Limitation / Grounding / Safety / Accuracy / Execution

## Description
What happened?

## Reproduction
Steps or prompt to reproduce

## Expected vs Actual
What should have happened vs what did happen

## Workaround (if found)
Any solutions discovered

## Comparison (optional)
Did Claude or other models handle this better?

## Notes
Additional observations
```

## Common Issues to Document

### Search Grounding
- [ ] Outdated information despite grounding
- [ ] Missing or broken source links
- [ ] Contradictory sources handled poorly
- [ ] Grounding not triggering when expected

### Code Execution
- [ ] Import errors for common packages
- [ ] Memory/timeout limits hit
- [ ] Visualization not rendering
- [ ] File upload processing issues

### Multi-modal
- [ ] Image misinterpretation
- [ ] Text extraction errors from images
- [ ] Chart/graph reading mistakes
- [ ] Document structure confusion

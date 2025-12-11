---
description: Pre-commit code review checklist
---

# Pre-Commit Review

You are helping a solo developer review their code before committing. Run through this checklist systematically.

## Process

1. First, run `git diff --staged` and `git diff` to see what's being committed
2. If nothing is staged, ask if they want to review unstaged changes
3. Go through the checklist below
4. Summarize findings at the end

## Checklist

### Code Quality
- [ ] **No debug code** - console.logs, print statements, commented-out code removed?
- [ ] **Naming** - Variables/functions clearly named? No abbreviations that obscure meaning?
- [ ] **Complexity** - Any functions doing too much? Should anything be broken up?
- [ ] **Duplication** - Any copy-paste code that should be extracted?

### Correctness
- [ ] **Edge cases** - Null checks, empty arrays, boundary conditions handled?
- [ ] **Error handling** - Failures handled gracefully? User-facing errors helpful?
- [ ] **Types** - If typed language, are types accurate and helpful?

### Security (OWASP awareness)
- [ ] **Input validation** - User input sanitized before use?
- [ ] **No secrets** - API keys, passwords, tokens not hardcoded?
- [ ] **SQL/injection** - Parameterized queries used? No string concatenation for queries?
- [ ] **XSS** - User content escaped before rendering in UI?

### Mobile-Specific (if applicable)
- [ ] **Performance** - No unnecessary re-renders? Heavy operations off main thread?
- [ ] **Offline** - Graceful handling if network unavailable?
- [ ] **Memory** - No obvious leaks? Large objects cleaned up?

### Tests
- [ ] **Coverage** - New functionality has tests?
- [ ] **Tests pass** - Run the test suite, all green?

## Output

Provide a summary:

```
Review Summary:
- [x] Code quality: [pass/issues found]
- [x] Correctness: [pass/issues found]
- [x] Security: [pass/issues found]
- [x] Tests: [pass/issues found]

[If issues found, list them with specific file:line references]

Verdict: [Ready to commit / Needs attention]
```

## If Issues Found

Offer to help fix them, but let the user decide. Don't automatically start making changes.

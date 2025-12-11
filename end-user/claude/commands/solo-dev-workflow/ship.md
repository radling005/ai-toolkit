---
description: Pre-release checklist before shipping
---

# Pre-Release Checklist

You are helping a solo developer prepare for a release. This is a more thorough check than `/review`.

## Process

Go through each section, checking and reporting status.

## Checklist

### 1. Code Complete
- [ ] All features for this release implemented?
- [ ] Check `docs/active.md` - are active items done?
- [ ] No TODO/FIXME comments for critical items?

### 2. Tests
- [ ] All tests passing? (run the test suite)
- [ ] New features have test coverage?
- [ ] Manual testing of critical paths done?

### 3. CI/CD
- [ ] CI pipeline passing?
- [ ] Build succeeds in production mode?
- [ ] No new warnings in build output?

### 4. UX Review
- [ ] Loading states present where needed?
- [ ] Error states handled gracefully?
- [ ] Empty states designed (no data scenarios)?
- [ ] Accessibility basics (contrast, labels, tap targets)?

### 5. Performance
- [ ] App size reasonable? No accidental large assets?
- [ ] Startup time acceptable?
- [ ] No obvious jank or slow screens?

### 6. Security
- [ ] No hardcoded secrets?
- [ ] API keys in secure config, not in code?
- [ ] Sensitive data not logged?
- [ ] HTTPS enforced for all network calls?

### 7. Documentation
- [ ] README up to date?
- [ ] CHANGELOG updated for this release?
- [ ] Version number bumped appropriately?

### 8. Release Prep
- [ ] Git tag created?
- [ ] Release notes drafted?
- [ ] Rollback plan if something goes wrong?

## Output

Provide a release readiness report:

```
Release Readiness: [Project Name] v[X.X.X]

[x] Code Complete
[x] Tests Passing
[ ] CI/CD - [issue if any]
[x] UX Review
[x] Performance
[x] Security
[ ] Documentation - [issue if any]
[ ] Release Prep - [issue if any]

Blockers:
- [List any blockers]

Recommendations:
- [Any suggestions]

Status: [Ready to ship / Needs work]
```

## If Not Ready

Help them work through blockers one by one if they want. Prioritize by risk.

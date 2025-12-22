# Project AI-Readiness Audit

You are a project assessor specializing in optimizing codebases for effective AI agent collaboration. Your goal is to evaluate this project's structure, documentation, and conventions to maximize AI contribution efficiency.

## Phase 1: Discovery

Scan and read the following (if they exist):
- CLAUDE.md / .claude/ directory
- README.md
- /docs folder contents
- Config files (package.json, pyproject.toml, Cargo.toml, etc.)
- Sample source files to detect patterns
- .gitignore, .env.example, docker-compose.yml

## Phase 2: Evaluate Against Checklist

Assess each category:

### Environment & Setup
- [ ] Dev environment setup steps documented
- [ ] Required tools/versions specified
- [ ] Environment variables documented (.env.example or similar)
- [ ] Database/service setup instructions

### Commands & Workflows
- [ ] Build command documented
- [ ] Test command documented (unit, integration, e2e)
- [ ] Lint/format commands documented
- [ ] Deploy process documented
- [ ] Common dev workflows explained

### Code Conventions
- [ ] File/folder structure explained
- [ ] Naming conventions defined
- [ ] Code patterns and idioms documented
- [ ] Error handling approach specified
- [ ] Key architectural decisions recorded

### Project Context
- [ ] Project purpose/goal clearly stated
- [ ] Tech stack listed with versions
- [ ] Key dependencies and their purposes explained
- [ ] "Do not" rules or anti-patterns listed

### AI-Specific Guidance
- [ ] CLAUDE.md exists and is comprehensive
- [ ] Slash commands for common workflows
- [ ] Clear instructions an AI can follow without guessing

## Phase 3: Identify Issues

Flag these problems:
- **Gaps**: Missing information AI would need
- **Contradictions**: Conflicting info across files
- **Outdated content**: Stale docs, dead links, deprecated patterns
- **Noise**: Excessive detail that adds confusion without value
- **Ambiguity**: Vague instructions open to interpretation

## Phase 4: Output Report

Structure your findings as:

```
## Summary
One paragraph overall assessment.

## Scores
- Environment & Setup: [Good/Partial/Missing]
- Commands & Workflows: [Good/Partial/Missing]
- Code Conventions: [Good/Partial/Missing]
- Project Context: [Good/Partial/Missing]
- AI-Specific Guidance: [Good/Partial/Missing]

## High Priority Gaps
Items that would significantly improve AI effectiveness.

## Medium Priority Improvements
Nice-to-have additions.

## Cleanup Recommendations
Outdated, redundant, or confusing content to remove/update.

## Suggested Actions
Concrete next steps, ordered by impact.
```

Be specific. Don't say "add more documentation" - say exactly what's missing and where it should go.

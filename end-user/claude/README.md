# Claude End-User Experiments

A structured learning lab for developing AI prompting skills and understanding Claude's capabilities.

## Folder Structure

```
claude/
├── prompts/           # Prompt engineering experiments
│   ├── coding/        # Code generation & debugging
│   ├── writing/       # Creative & technical writing
│   ├── analysis/      # Data interpretation, reasoning
│   └── multi-turn/    # Complex conversation chains
├── artifacts/         # Claude Artifacts experiments
│   ├── react-components/   # UI component generation
│   ├── visualizations/     # Charts, diagrams, SVGs
│   └── documents/          # Formatted docs, reports
├── edge-cases/        # Limitations & boundary testing
└── templates/         # Reusable prompt templates
```

---

## Learning Tracks

### Track 1: Prompt Engineering Fundamentals

Master the core techniques that improve AI output quality.

| Technique | Description | Try This |
|-----------|-------------|----------|
| **Zero-shot** | Direct task with no examples | Ask Claude to write a function with just the requirements |
| **Few-shot** | Provide examples before the task | Give 2-3 example inputs/outputs, then your actual request |
| **Chain-of-thought** | Ask Claude to reason step-by-step | Add "Think through this step by step" to complex problems |
| **Role prompting** | Assign a persona or expertise | "You are a senior security engineer reviewing this code..." |
| **Structured output** | Request specific formats | "Respond in JSON with fields: title, summary, tags" |

**Exercise:** Take a single task and try all 5 techniques. Document which produces the best result and why.

---

### Track 2: Claude-Specific Features

#### Artifacts
Claude can create interactive artifacts (code, documents, visualizations). Experiment with:

- [ ] Triggering React component generation
- [ ] Creating SVG graphics and diagrams
- [ ] Generating Mermaid flowcharts
- [ ] Building interactive HTML demos
- [ ] Iterating on artifacts across multiple turns

**Key question:** What phrasing reliably triggers artifact creation vs inline code?

#### Projects & Knowledge
- [ ] How does Claude use uploaded project files?
- [ ] What file formats work best for knowledge retrieval?
- [ ] How to structure documents for optimal context usage?

#### Extended Thinking
- [ ] Compare outputs with thinking enabled vs disabled
- [ ] Which problem types benefit most from extended thinking?
- [ ] How does thinking depth affect code quality?

---

### Track 3: Capability Deep Dives

#### Coding (`prompts/coding/`)
- Code generation from natural language
- Debugging and error explanation
- Code review and refactoring suggestions
- Test case generation
- Documentation writing

#### Writing (`prompts/writing/`)
- Technical documentation
- Creative writing with style constraints
- Summarization at different lengths
- Tone adaptation (formal, casual, persuasive)
- Translation and localization

#### Analysis (`prompts/analysis/`)
- Data interpretation from tables/CSVs
- Logical reasoning problems
- Pros/cons analysis
- Research synthesis
- Decision frameworks

#### Multi-turn Conversations (`prompts/multi-turn/`)
- Context retention over long conversations
- Iterative refinement workflows
- Complex multi-step tasks
- Maintaining consistency across turns

---

### Track 4: Edge Cases & Limitations

Document these in the `edge-cases/` folder:

#### Known Limitations
- Where does Claude struggle?
- What types of tasks produce inconsistent results?
- How does output quality degrade with context length?

#### Safety Boundaries
- Understanding refusal patterns
- What triggers safety responses?
- How to rephrase legitimate requests that get refused

#### Accuracy Testing
- Fact-checking Claude's claims
- Testing knowledge cutoff boundaries
- Identifying confident-but-wrong responses

---

## Experiment Template

Use this format when documenting experiments (see `templates/experiment-template.md`):

```markdown
## Experiment: [Descriptive Name]

**Date:** YYYY-MM-DD
**Model:** Claude 3.5 Sonnet / Claude 3 Opus / etc.
**Feature:** Artifacts / Extended Thinking / Standard

### Goal
What are you trying to learn or test?

### Hypothesis
What do you expect to happen?

### Prompt
\`\`\`
[Your exact prompt here]
\`\`\`

### Response Summary
[Key points from Claude's response]

### Observations
- What worked well?
- What surprised you?
- What failed or was unexpected?

### Lessons Learned
- Key takeaways for future prompting
- Techniques to repeat or avoid
```

---

## Skill-Building Exercises

### Beginner
1. **Prompt Comparison** — Same task, 3 different phrasings. Which works best?
2. **Format Control** — Get Claude to output valid JSON, XML, and Markdown tables
3. **Artifact Triggers** — Find 5 reliable ways to trigger artifact creation

### Intermediate
4. **Iterative Refinement** — Start with a bad output, improve it in 5+ turns
5. **Token Efficiency** — Achieve the same output with progressively shorter prompts
6. **System Prompt Lab** — Test how custom instructions change behavior

### Advanced
7. **Multi-step Workflows** — Chain 3+ prompts for a complex deliverable
8. **Failure Recovery** — Intentionally break things, document recovery strategies
9. **Model Comparison** — Same prompt to Claude vs Gemini, analyze differences

---

## Best Practices

### Do
- Save exact prompts, not paraphrases
- Note the specific model version used
- Record both successes AND failures
- Date everything (models change over time)
- Build a personal library of effective patterns

### Don't
- Assume what worked once will always work
- Ignore unexpected behaviors
- Skip documenting failures (they teach the most)
- Forget that model updates change behavior

---

## Quick Reference: Effective Prompting Patterns

See `templates/effective-prompts.md` for a growing collection of proven patterns.

### The Basics That Always Help
1. **Be specific** — Vague prompts get vague answers
2. **Provide context** — What's this for? Who's the audience?
3. **Show examples** — Demonstrate the format/style you want
4. **Set constraints** — Length, format, tone, what to avoid
5. **Ask for reasoning** — "Explain your approach" improves quality

---

## Contributing to Your Learning

After each session:
1. Did you learn something new? Write it down.
2. Did something fail? Document why.
3. Did you find a great prompt? Save it to templates.
4. Can you explain what you learned to someone else?

The goal is **deliberate practice** — not just using AI, but understanding it deeply.

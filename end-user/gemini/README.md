# Gemini End-User Experiments

A structured learning lab for developing AI prompting skills and understanding Gemini's capabilities.

## Folder Structure

```
gemini/
├── prompts/           # Prompt engineering experiments
│   ├── coding/        # Code generation & debugging
│   ├── writing/       # Creative & technical writing
│   ├── analysis/      # Data interpretation, reasoning
│   └── multi-turn/    # Complex conversation chains
├── artifacts/         # Gemini output experiments
│   ├── code-execution/     # Live code running results
│   ├── visualizations/     # Charts, images, diagrams
│   └── documents/          # Formatted docs, exports
├── edge-cases/        # Limitations & boundary testing
└── templates/         # Reusable prompt templates
```

---

## Learning Tracks

### Track 1: Prompt Engineering Fundamentals

Master the core techniques that improve AI output quality.

| Technique | Description | Try This |
|-----------|-------------|----------|
| **Zero-shot** | Direct task with no examples | Ask Gemini to write a function with just the requirements |
| **Few-shot** | Provide examples before the task | Give 2-3 example inputs/outputs, then your actual request |
| **Chain-of-thought** | Ask Gemini to reason step-by-step | Add "Think through this step by step" to complex problems |
| **Role prompting** | Assign a persona or expertise | "You are a data scientist analyzing this dataset..." |
| **Structured output** | Request specific formats | "Respond in JSON with fields: title, summary, tags" |

**Exercise:** Take a single task and try all 5 techniques. Document which produces the best result and why.

---

### Track 2: Gemini-Specific Features

#### Google Search Grounding
Gemini can ground responses in real-time search results:

- [ ] When does Gemini decide to search vs use training data?
- [ ] How to explicitly request search-grounded answers
- [ ] Comparing grounded vs non-grounded responses for accuracy
- [ ] Understanding source citations and verification

**Key question:** What phrasing reliably triggers search grounding?

#### Code Execution (Gemini Advanced)
Gemini can run Python code and return results:

- [ ] Triggering code execution vs code display
- [ ] Data analysis with uploaded files
- [ ] Visualization generation (matplotlib, seaborn)
- [ ] Iterating on code with live feedback
- [ ] Limitations of the execution environment

#### Gems (Custom AI Personas)
Create specialized versions of Gemini:

- [ ] Designing effective Gem instructions
- [ ] When to use a Gem vs custom prompt
- [ ] Comparing Gem consistency vs ad-hoc role prompts
- [ ] Building Gems for specific workflows

#### Multi-Modal Capabilities
- [ ] Image understanding and analysis
- [ ] Comparing image interpretation accuracy
- [ ] Document/PDF analysis
- [ ] Audio and video understanding (where available)

#### Google Workspace Integration
- [ ] Using Gemini with Gmail, Docs, Sheets
- [ ] @mentions and context pulling
- [ ] Workflow automation experiments

---

### Track 3: Capability Deep Dives

#### Coding (`prompts/coding/`)
- Code generation from natural language
- Debugging and error explanation
- Code review and refactoring suggestions
- Test case generation
- Multi-language support comparison

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
- Research synthesis with search grounding
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
- Where does Gemini struggle?
- What types of tasks produce inconsistent results?
- How does output quality vary across model versions (Pro vs Flash)?

#### Safety Boundaries
- Understanding refusal patterns
- What triggers safety responses?
- How to rephrase legitimate requests that get refused

#### Accuracy Testing
- Fact-checking Gemini's claims
- Testing search grounding accuracy
- Identifying hallucination patterns
- Comparing with/without grounding

---

## Gemini Model Variants

Understanding when to use each:

| Model | Best For | Trade-offs |
|-------|----------|------------|
| **Gemini Pro** | Balanced performance, most tasks | Good all-rounder |
| **Gemini Flash** | Speed, simple tasks, high volume | Less capable on complex reasoning |
| **Gemini Ultra** | Most complex tasks, nuanced reasoning | Slower, higher resource usage |

**Exercise:** Run the same complex prompt on each variant, document differences.

---

## Experiment Template

Use this format when documenting experiments (see `templates/experiment-template.md`):

```markdown
## Experiment: [Descriptive Name]

**Date:** YYYY-MM-DD
**Model:** Gemini Pro / Flash / Ultra
**Feature:** Standard / Code Execution / Search Grounding / Gems

### Goal
What are you trying to learn or test?

### Hypothesis
What do you expect to happen?

### Prompt
\`\`\`
[Your exact prompt here]
\`\`\`

### Response Summary
[Key points from Gemini's response]

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
2. **Format Control** — Get Gemini to output valid JSON, XML, and Markdown tables
3. **Search Grounding** — Find 5 reliable ways to trigger grounded responses

### Intermediate
4. **Iterative Refinement** — Start with a bad output, improve it in 5+ turns
5. **Code Execution Lab** — Upload data, generate analysis, iterate on visualizations
6. **Gem Creation** — Build a specialized Gem for a recurring workflow

### Advanced
7. **Multi-step Workflows** — Chain prompts for a complex deliverable
8. **Model Comparison** — Same prompt to Gemini vs Claude, analyze differences
9. **Grounding Verification** — Fact-check grounded responses for accuracy

---

## Best Practices

### Do
- Save exact prompts, not paraphrases
- Note the specific model version used
- Record both successes AND failures
- Date everything (models change over time)
- Verify search-grounded claims independently
- Build a personal library of effective patterns

### Don't
- Assume what worked once will always work
- Ignore unexpected behaviors
- Skip documenting failures (they teach the most)
- Trust grounded responses without verification
- Forget that model updates change behavior

---

## Quick Reference: Effective Prompting Patterns

See `templates/effective-prompts.md` for a growing collection of proven patterns.

### The Basics That Always Help
1. **Be specific** — Vague prompts get vague answers
2. **Provide context** — What's this for? Who's the audience?
3. **Show examples** — Demonstrate the format/style you want
4. **Set constraints** — Length, format, tone, what to avoid
5. **Request sources** — "Cite your sources" for factual claims

---

## Gemini vs Claude: Key Differences to Explore

| Aspect | Gemini | Claude |
|--------|--------|--------|
| **Search** | Native Google Search grounding | No built-in search |
| **Code Execution** | Can run Python code | Cannot execute code |
| **Multi-modal** | Strong image/video support | Image understanding |
| **Ecosystem** | Google Workspace integration | Artifacts system |
| **Customization** | Gems | Projects |

**Exercise:** Document which tool works better for specific use cases.

---

## Contributing to Your Learning

After each session:
1. Did you learn something new? Write it down.
2. Did something fail? Document why.
3. Did you find a great prompt? Save it to templates.
4. Can you explain what you learned to someone else?

The goal is **deliberate practice** — not just using AI, but understanding it deeply.

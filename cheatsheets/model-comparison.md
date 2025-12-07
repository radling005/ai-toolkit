# Model Comparison Cheatsheet

When to use Claude vs Gemini.

---

## Quick Decision Guide

| Task | Recommended | Why |
|------|-------------|-----|
| Long document analysis | Claude | Larger context, strong comprehension |
| Current events / facts | Gemini | Search grounding |
| Code generation | Both | Test and compare |
| Data analysis + visualization | Gemini | Code execution |
| Creative writing | Claude | Strong creative capabilities |
| Multi-modal (images) | Both | Test for your use case |
| Quick simple tasks | Gemini Flash | Speed |
| Complex reasoning | Claude / Gemini Ultra | Strongest models |

---

## Feature Comparison

| Feature | Claude | Gemini |
|---------|--------|--------|
| **Search grounding** | ❌ | ✅ |
| **Code execution** | ❌ | ✅ |
| **Artifacts** | ✅ | ❌ |
| **Large context** | ✅ (200K) | ✅ (1M+) |
| **Projects** | ✅ | Via Gems |
| **Custom personas** | Via Projects | ✅ Gems |
| **Image understanding** | ✅ | ✅ |
| **Image generation** | ❌ | ✅ |

---

## Model Tiers

### Claude
| Model | Best For | Speed |
|-------|----------|-------|
| Haiku | Simple tasks, high volume | ⚡⚡⚡ Fast |
| Sonnet | Balanced performance | ⚡⚡ Medium |
| Opus | Complex reasoning | ⚡ Slower |

### Gemini
| Model | Best For | Speed |
|-------|----------|-------|
| Flash | Simple tasks, speed | ⚡⚡⚡ Fast |
| Pro | Balanced performance | ⚡⚡ Medium |
| Ultra | Complex reasoning | ⚡ Slower |

---

## Use Claude When...

✅ Analyzing long documents
✅ Complex multi-step reasoning
✅ Creative writing projects
✅ Code that needs explanation
✅ Building with Artifacts (React, HTML)
✅ Nuanced analysis tasks

---

## Use Gemini When...

✅ Need current information (search)
✅ Data analysis with actual code execution
✅ Want visualizations generated
✅ Fact-checking with citations
✅ Speed is critical (Flash)
✅ Google Workspace integration

---

## Both Work Well For...

- General coding tasks
- Documentation writing
- Brainstorming
- Summarization
- Learning and explanations
- Basic analysis

**When in doubt:** Test both. Add to your comparisons lab.

---

## Cost Considerations

| Factor | Impact |
|--------|--------|
| Input tokens | More context = more cost |
| Output tokens | Longer responses = more cost |
| Model tier | Opus/Ultra > Sonnet/Pro > Haiku/Flash |
| API vs Web | API typically cheaper per token |

**Cost optimization:**
- Use smaller models for simple tasks
- Limit output length when possible
- Batch similar requests
- Cache common queries

---

## Switching Between Models

**What to adjust:**
- Claude uses `messages` format
- Gemini may need search grounding prompts
- Feature-specific syntax differs

**What stays the same:**
- Core prompting techniques
- Output format requests
- Most prompt patterns

---

## Build Your Own Guide

After testing, fill in:

**For [task type], I prefer [model] because:**
-
-

**[Model] consistently beats [other] at:**
-
-

**Surprising findings:**
-

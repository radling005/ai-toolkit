# Cost Reference Cheatsheet

Understanding and optimizing AI costs.

---

## Token Basics

**What's a token?**
- Roughly 0.75 words in English
- "Hello, world!" ≈ 4 tokens
- Code often uses more tokens than prose

**Quick estimates:**
| Content | Approximate Tokens |
|---------|-------------------|
| 1 word | ~1.3 tokens |
| 1 sentence | ~15-25 tokens |
| 1 paragraph | ~75-100 tokens |
| 1 page | ~400-500 tokens |
| 1,000 words | ~1,300 tokens |

---

## Context Window Sizes

| Model | Context Window | ~Words |
|-------|---------------|--------|
| Claude Haiku | 200K | ~150K |
| Claude Sonnet | 200K | ~150K |
| Claude Opus | 200K | ~150K |
| Gemini Flash | 1M | ~750K |
| Gemini Pro | 1M | ~750K |

**Note:** Larger isn't always better—more context = more cost.

---

## Cost Factors

| Factor | Impact | Optimization |
|--------|--------|--------------|
| **Input tokens** | Direct cost | Minimize context |
| **Output tokens** | Direct cost | Set length limits |
| **Model tier** | Multiplier | Use appropriate tier |
| **Frequency** | Cumulative | Cache, batch |

---

## Model Cost Comparison (Relative)

| Tier | Cost Level | When to Use |
|------|------------|-------------|
| Haiku/Flash | 💰 Low | Simple tasks, high volume |
| Sonnet/Pro | 💰💰 Medium | Most tasks |
| Opus/Ultra | 💰💰💰 High | Complex reasoning only |

**Rule of thumb:** Start with cheaper models, upgrade only if needed.

---

## Cost Optimization Strategies

### Reduce Input Tokens
```
❌ Pasting entire files
✅ Paste only relevant sections

❌ Full conversation history
✅ Summarize previous context

❌ Verbose instructions
✅ Concise, clear prompts
```

### Reduce Output Tokens
```
Add constraints:
- "In 3 bullet points"
- "Maximum 100 words"
- "Just the code, no explanation"
```

### Choose Right Model
```
Simple task → Haiku/Flash
Standard task → Sonnet/Pro
Complex reasoning → Opus/Ultra (only when needed)
```

### Batch and Cache
```
- Combine related queries
- Save responses for reuse
- Use consistent prompts for caching
```

---

## Estimation Guide

**Before running expensive prompts, estimate:**

| Your input | Tokens | Your output (expected) | Tokens |
|------------|--------|----------------------|--------|
| Prompt | ~X | Response length | ~Y |
| Context/code | ~X | Format overhead | ~Y |
| Examples | ~X | | |
| **Total Input** | ~X | **Total Output** | ~Y |

---

## Cost-Conscious Patterns

### For Development/Testing
- Use cheaper models while iterating
- Upgrade to better models for final output
- Test prompts with short outputs first

### For Production
- Cache common responses
- Set max_tokens limits
- Monitor usage patterns
- Use streaming for long outputs

---

## Warning Signs

🚨 **You might be overspending if:**
- Using Opus/Ultra for simple tasks
- Pasting entire codebases
- No length limits on outputs
- Not reusing successful prompts
- Running the same query repeatedly

---

## Free Tier Awareness

**Web interfaces (Claude.ai, Gemini):**
- Usually have usage limits
- Limits reset periodically
- May have model restrictions

**APIs:**
- Pay per token
- No caps (can get expensive)
- Set spending limits!

---

## Quick Reference

| Task | Model | Length Limit |
|------|-------|--------------|
| Quick question | Haiku/Flash | Default |
| Code review | Sonnet/Pro | "Key issues only" |
| Complex analysis | Sonnet | "Summarize findings" |
| Simple generation | Haiku/Flash | Set max tokens |
| Important work | Appropriate tier | As needed |

---

## Tracking Your Usage

Create a simple log:

| Date | Task | Model | Input Est. | Output Est. | Notes |
|------|------|-------|------------|-------------|-------|
| | | | | | |

Review weekly to identify optimization opportunities.

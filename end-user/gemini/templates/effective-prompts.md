# Effective Prompts Collection

A growing library of prompt patterns that consistently produce good results with Gemini.

---

## How to Use This File

1. **Browse** patterns when you're stuck
2. **Copy & adapt** for your specific use case
3. **Contribute** new patterns when you discover them
4. **Note** which model version you tested with

---

## Gemini-Specific Patterns

### 1. Search Grounding Trigger

**Problem:** Need up-to-date or factual information, not training data.

**Pattern:**
```
Search for current information about [topic].

Based on your search results:
1. [Specific question 1]
2. [Specific question 2]

Cite your sources for each claim.
```

**Example:**
```
Search for current information about Python 3.12 new features.

Based on your search results:
1. What are the top 5 new features?
2. Which ones improve performance?

Cite your sources for each claim.
```

**Variations that trigger grounding:**
- "What's the latest on..."
- "Search and tell me about..."
- "Find current information about..."
- "What do recent sources say about..."

---

### 2. Code Execution Request

**Problem:** Need Gemini to actually run code, not just show it.

**Pattern:**
```
Write and run Python code that [task].

Show me:
1. The code
2. The output when executed
3. Any visualizations generated
```

**Example:**
```
Write and run Python code that analyzes this data and creates a bar chart.

Data:
Product A: 150 sales
Product B: 230 sales
Product C: 180 sales

Show me:
1. The code
2. The output when executed
3. The bar chart visualization
```

**Tips:**
- Explicitly say "run" or "execute"
- Request to see the output
- Works best with data analysis and visualization tasks

---

### 3. The Specific Request

**Problem:** Vague prompts get vague answers.

**Pattern:**
```
[Action verb] a [specific deliverable] that [key requirements].

Context: [relevant background]
Format: [desired output structure]
Constraints: [length, style, what to avoid]
```

**Example:**
```
Write a Python function that validates email addresses.

Context: This is for a user registration form in a Flask app.
Format: Single function with docstring and type hints.
Constraints: Use only standard library (no external packages).
Handle edge cases like empty strings and None values.
```

---

### 4. The Role Assignment

**Problem:** Generic responses that lack expertise depth.

**Pattern:**
```
You are a [specific role] with expertise in [domain].

Your task: [what they need to do]
Audience: [who will consume this]
Tone: [formal/casual/technical]
```

**Example:**
```
You are a senior data analyst with expertise in e-commerce metrics.

Your task: Analyze this sales data and identify trends.
Audience: Marketing team with basic data literacy.
Tone: Clear and actionable, avoid jargon.

[paste data]
```

---

### 5. The Few-Shot Pattern

**Problem:** Gemini doesn't understand the format or style you want.

**Pattern:**
```
[Task description]

Examples:
Input: [example 1 input]
Output: [example 1 output]

Input: [example 2 input]
Output: [example 2 output]

Now do this one:
Input: [your actual input]
Output:
```

**Example:**
```
Convert these informal bug reports into structured tickets.

Examples:
Input: "the login is broken again smh"
Output:
- Title: Login functionality failure
- Priority: High
- Description: Users unable to complete login flow
- Steps to reproduce: [Needs clarification]

Input: "dark mode colors are ugly"
Output:
- Title: Dark mode color scheme feedback
- Priority: Low
- Description: User reports dissatisfaction with dark mode palette
- Steps to reproduce: Enable dark mode in settings

Now do this one:
Input: "app crashes when I upload big files"
Output:
```

---

### 6. The Chain-of-Thought

**Problem:** Complex problems get superficial answers.

**Pattern:**
```
[Problem statement]

Think through this step by step:
1. First, identify [aspect 1]
2. Then, analyze [aspect 2]
3. Consider [potential issues]
4. Finally, provide [deliverable]

Show your reasoning at each step.
```

**Example:**
```
Debug why this function returns incorrect results for negative numbers.

Think through this step by step:
1. First, trace what happens when input is -5
2. Then, identify where the logic diverges from expected behavior
3. Consider edge cases the original author might have missed
4. Finally, provide the corrected code with explanation

Show your reasoning at each step.

[paste function]
```

---

### 7. Multi-Modal Analysis

**Problem:** Need Gemini to analyze images, documents, or other media.

**Pattern:**
```
[Upload image/document]

Analyze this [image/document] and:
1. [Specific analysis request]
2. [Specific extraction request]
3. [Specific question]

Format your response as: [desired structure]
```

**Example:**
```
[Upload screenshot of dashboard]

Analyze this dashboard screenshot and:
1. List all the metrics shown
2. Identify any data anomalies or concerning trends
3. What questions should I ask the data team based on this?

Format your response as a bulleted list grouped by category.
```

---

### 8. The Structured Output

**Problem:** Unstructured responses that are hard to parse or use.

**Pattern:**
```
[Task description]

Respond in this exact format:
```json
{
  "field1": "description",
  "field2": ["item1", "item2"],
  "field3": {
    "nested": "value"
  }
}
```

**Example:**
```
Analyze this error message and provide debugging guidance.

Respond in this exact format:
```json
{
  "error_type": "category of error",
  "root_cause": "most likely cause",
  "quick_fixes": ["fix 1", "fix 2"],
  "diagnostic_steps": ["step 1", "step 2"],
  "prevention": "how to avoid this in future"
}
```

Error: [paste error]
```

---

### 9. Gem Instruction Pattern

**Problem:** Creating effective custom Gems.

**Pattern for Gem Instructions:**
```
You are [role/persona] specialized in [domain].

Your communication style:
- [Style trait 1]
- [Style trait 2]
- [Style trait 3]

When responding:
- Always [behavior 1]
- Never [behavior 2]
- Format outputs as [preferred format]

Your expertise includes:
- [Skill 1]
- [Skill 2]
- [Skill 3]
```

**Example Gem Instructions:**
```
You are a Code Review Assistant specialized in Python best practices.

Your communication style:
- Direct and constructive
- Focus on "why" not just "what"
- Use code examples to illustrate points

When responding:
- Always categorize issues (critical, suggestion, nitpick)
- Never just say "this is wrong" without explaining why
- Format outputs as markdown with code blocks

Your expertise includes:
- PEP 8 style guidelines
- Python performance optimization
- Security best practices
- Testing patterns
```

---

### 10. The Verification Request

**Problem:** Need to fact-check or verify Gemini's claims.

**Pattern:**
```
[Make initial request]

Then:
1. Rate your confidence in each claim (high/medium/low)
2. For medium/low confidence, note what would need verification
3. Cite sources where available
```

---

## Anti-Patterns to Avoid

### Don't: Be vague
```
❌ "Make this better"
✅ "Improve readability by adding comments and breaking into smaller functions"
```

### Don't: Ask multiple unrelated things
```
❌ "Review this code, also what's the best database, and can you write tests"
✅ [Ask each as a separate focused prompt]
```

### Don't: Assume grounding is always active
```
❌ "What's the current stock price?" (may use training data)
✅ "Search for the current stock price of AAPL and cite your source"
```

### Don't: Trust grounded responses blindly
```
❌ Accept all "searched" facts without verification
✅ Verify key claims, especially for important decisions
```

---

## Adding New Patterns

When you discover an effective prompt pattern:

1. **Name it** - Give it a memorable title
2. **Describe the problem** - When should someone use this?
3. **Show the pattern** - Generic template
4. **Provide an example** - Concrete usage
5. **Note the model** - Which Gemini version you tested with
6. **Note Gemini-specific behavior** - Search grounding, code execution, etc.

---

## Version Notes

Patterns may need adjustment as models update. Note when patterns were last verified:

| Pattern | Last Tested | Model | Status |
|---------|-------------|-------|--------|
| Search Grounding | - | - | Needs testing |
| Code Execution | - | - | Needs testing |
| Specific Request | - | - | Needs testing |
| Role Assignment | - | - | Needs testing |
| Few-Shot | - | - | Needs testing |
| Chain-of-Thought | - | - | Needs testing |
| Multi-Modal | - | - | Needs testing |
| Structured Output | - | - | Needs testing |
| Gem Instructions | - | - | Needs testing |
| Verification | - | - | Needs testing |

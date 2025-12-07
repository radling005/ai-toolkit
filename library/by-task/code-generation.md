# Code Generation Prompts

Battle-tested prompts for generating code.

---

## Function Generator

**Purpose:** Generate a function from requirements
**Best for:** Both Claude and Gemini
**Success rate:** High

### Prompt
```
Write a [LANGUAGE] function that [DESCRIPTION].

Requirements:
- [REQUIREMENT 1]
- [REQUIREMENT 2]
- [REQUIREMENT 3]

Include:
- Type hints/annotations
- Docstring with examples
- Error handling for [EDGE CASES]

Context: [WHERE THIS WILL BE USED]
```

### Example Usage
```
Write a Python function that calculates the Fibonacci sequence.

Requirements:
- Takes an integer n and returns the nth Fibonacci number
- Handle negative numbers by raising ValueError
- Optimize for repeated calls (memoization)

Include:
- Type hints
- Docstring with examples
- Error handling for non-integer input

Context: Educational tool for teaching recursion
```

### Tips
- Be specific about error handling needs
- Mention performance requirements if relevant
- Specify the exact return type

---

## API Endpoint Generator

**Purpose:** Generate REST API endpoint code
**Best for:** Both
**Success rate:** High

### Prompt
```
Create a [FRAMEWORK] API endpoint for [RESOURCE].

Endpoint: [METHOD] [PATH]
Purpose: [WHAT IT DOES]

Request:
- Body/params: [EXPECTED INPUT]
- Validation: [RULES]

Response:
- Success: [FORMAT]
- Errors: [ERROR CASES]

Include: [AUTHENTICATION / LOGGING / ETC]
```

---

## Test Generator

**Purpose:** Generate unit tests for existing code
**Best for:** Both
**Success rate:** High

### Prompt
```
Write unit tests for this [LANGUAGE] code:

```[language]
[CODE TO TEST]
```

Test framework: [PYTEST / JEST / ETC]

Cover:
- Happy path cases
- Edge cases: [SPECIFIC EDGES]
- Error cases: [EXPECTED ERRORS]

Style: [ONE ASSERTION PER TEST / DESCRIPTIVE NAMES / ETC]
```

---

## Class/Module Generator

**Purpose:** Generate a complete class or module
**Best for:** Both
**Success rate:** Medium-High

### Prompt
```
Create a [LANGUAGE] class for [PURPOSE].

Class name: [NAME]

Properties:
- [PROPERTY 1]: [TYPE] - [DESCRIPTION]
- [PROPERTY 2]: [TYPE] - [DESCRIPTION]

Methods:
- [METHOD 1]: [DESCRIPTION]
- [METHOD 2]: [DESCRIPTION]

Include:
- Constructor with validation
- String representation
- [OTHER REQUIREMENTS]

Usage context: [HOW IT WILL BE USED]
```

---

## Quick Patterns

### One-liner request
```
Write a [LANGUAGE] one-liner that [TASK].
```

### With specific style
```
Write this in [FUNCTIONAL / OOP / PROCEDURAL] style.
Following [PEP8 / AIRBNB / GOOGLE] style guide.
```

### With dependencies
```
Use [LIBRARY] for [PURPOSE].
Assume [DEPENDENCY] is already imported.
```

---

## Tags
`#code-gen` `#proven` `#any-model`

# Ideas for Claude

Manage quick idea capture for later review.

## Arguments
- `$ARGUMENTS` - Either "show" to display ideas, or the idea text to store

## Instructions

The ideas file is located at: `~/.claude/ideas.md`

**If the argument is "show" (case-insensitive):**
- Read and display the contents of the ideas file
- If the file doesn't exist or is empty, say "No ideas collected yet"

**Otherwise (storing a new idea):**
- Append the idea to the ideas file with a timestamp
- Format: `- [YYYY-MM-DD HH:MM] <idea text>`
- Create the file if it doesn't exist
- Confirm the idea was saved

Keep responses brief.

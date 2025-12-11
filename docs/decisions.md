# Decisions

Architecture and technical decisions for this project.

---

## 2025-12-10 - Split into Two Repos (ai-toolkit + ai-playground)

**Context:** The original ai-playground repo was mixing proven, reusable tooling with experimental half-baked ideas. Made it hard to find and trust things.

**Decision:** Split into two repositories:
- **ai-toolkit** - Curated, proven AI configs, commands, workflows, and code patterns
- **ai-playground** - Experimental sandbox for trying things out

**Consequences:**
- Clear separation between "ready to use" and "still experimenting"
- Higher quality bar for ai-toolkit (only proven stuff)
- Items graduate from ai-playground to ai-toolkit when proven useful
- Two repos to maintain, but each with a clear purpose

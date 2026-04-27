---
name: 1-pointer-story-implementation
description: "Implements 1-pointer JIRA stories with discovery, planning, and implementation phases"
argument-hint: "[JIRA-ID]"
disable-model-invocation: true
model: opus
effort: high
allowed-tools:
  - Read
  - Glob
  - Grep
  - Bash
  - Agent
  - Edit
  - Write
  - mcp__bahmni_atlassian__*
---

## Context

You are implementing the requirement $JIRA_ID in the current repository.
This is a **1-pointer story** - expect minimal, focused changes only.

**First, read the shared base configuration:** `${CLAUDE_PLUGIN_ROOT}/shared/config/story-implementation-base.md`

### Phases for This Command
1. Validation - Git checks, JIRA fetch, prerequisites
2. Discovery - Analyze requirements, plan approach
3. Implementation - Code, test, complete

---

## Prerequisites

See shared prerequisites in `${CLAUDE_PLUGIN_ROOT}/shared/config/story-implementation-base.md`.

---

## Templates Used

| Template | Purpose |
|----------|---------|
| `${CLAUDE_PLUGIN_ROOT}/shared/templates/discovery-and-plan.md` | Discovery and planning document |
| `${CLAUDE_PLUGIN_ROOT}/shared/templates/implementation-summary.md` | Implementation summary with PR description |

---

## Files Created

See shared files in `${CLAUDE_PLUGIN_ROOT}/shared/config/story-implementation-base.md`.

No additional files for 1-pointer stories.

---

## 1-Pointer Configuration

| Setting | Value |
|---------|-------|
| Story Points | 1 |
| Refactoring | ❌ NOT allowed |
| Smart Checkpoint | ❌ Disabled |
| Work Breakdown | Optional (for trivial changes, skip) |

---

## 1-Pointer Specific Rules

### Scope Verdict (MANDATORY)

Binary verdict only:
- ✅ **Confirmed 1-pointer** - work is minimal and focused
- ❌ **NOT a 1-pointer** - work exceeds minimal scope (explain why)

**If NOT a 1-pointer:** Use `AskUserQuestion` (Override / Cancel for 2-pointer / Cancel to split).

### Implementation Approach

**For trivial changes** (typo fix, config flag, simple guard clause):
- Propose a single, direct approach
- State: "This is a trivial change with one obvious implementation path"

**For non-trivial changes** (logic changes, new functionality, multi-file):
- Present 2-3 approaches if multiple viable options exist
- Include: technical approach, files to modify, pros/cons, complexity/risk

### Strict Constraints (1-Pointer Specific)

In addition to base constraints:
- ❌ Do NOT refactor unrelated code
- ❌ Do NOT rename files, variables, or APIs unless required by AC
- ❌ Do NOT "clean up" nearby code opportunistically

### Scope Monitoring

- Track files modified during implementation
- **If changes feel like they're expanding beyond minimal scope:** Pause and use `AskUserQuestion` (Continue / Stop and review)

### No Acceptance Criteria

If ticket has no AC: **Stop with error** (stricter than 2-pointer which marks BLOCKED)

---

## Workflow

### Phase 1: Validation
Follow shared validation steps from base config, then:
- Check story points = 1 (warn if different)
- Display summary: JIRA ID, summary, story points, AC count, branch, CLAUDE.md status

### Phase 2: Discovery
Follow shared codebase assessment from base config, then:
1. Determine implementation approach (trivial vs non-trivial)
2. Provide scope verdict (binary)
3. List clarifying questions
4. Save to `$JIRA_ID_discovery_and_plan.md` using template

**Use AskUserQuestion:** "Proceed to implementation" | "Cancel"

### Phase 3: Implementation

**Execute implementation using Task tool with model: sonnet:**

Launch a sonnet agent to perform the implementation based on the approved discovery plan. The agent should receive:
- The discovery document (`$JIRA_ID_discovery_and_plan.md`)
- JIRA acceptance criteria
- CLAUDE.md guidelines (if present)
- 1-pointer strict constraints (no refactoring, no scope creep)

The sonnet agent will:
1. Apply 1-pointer strict constraints (no refactoring)
2. Monitor for scope creep
3. Run validation checks
4. Save to `$JIRA_ID_implementation_summary.md` using template

**On completion:** Display READY FOR PR, suggest `/submit-pr $JIRA_ID`

**Use AskUserQuestion:** "Done" | "Request changes"

---

## Error Handling

See shared error handling in `${CLAUDE_PLUGIN_ROOT}/shared/config/story-implementation-base.md`.

Additional 1-pointer specific errors:

| Error | Action |
|-------|--------|
| No AC defined | Stop with error (not BLOCKED) |
| Story points ≠ 1 | Warn, use AskUserQuestion to confirm |
| Scope creep detected | Pause and review with user |

---

## Guidelines

See shared guidelines in `${CLAUDE_PLUGIN_ROOT}/shared/config/story-implementation-base.md`.

Additional 1-pointer specific guidelines:
- **Minimal scope**: Flag immediately if changes expand beyond minimal scope
- **No opportunistic changes**: Implement only what's in the acceptance criteria
- **No refactoring**: Document improvement opportunities in Follow-up Items, don't implement
- **Quick turnaround**: 1-pointers should be fast and focused

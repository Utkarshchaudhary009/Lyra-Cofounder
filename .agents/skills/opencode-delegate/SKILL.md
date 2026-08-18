---
name: opencode-delegate
description: "Delegate background development subtasks (large-scale refactoring, multi-file code generation, isolated UI testing, iterative search/research) to OpenCode CLI asynchronously."
---

# OpenCode CLI Subtask Delegation

## Overview

This skill enables Antigravity to offload intensive, multi-file, or background development subtasks to the **OpenCode CLI** runner. By delegating heavy subtasks to `opencode`, Antigravity keeps the primary conversation thread responsive, fast, and focused on high-level orchestration and user interaction.

---

## Delegation Criteria (When to Delegate)

You **MUST** delegate a subtask to OpenCode CLI whenever the task or orchestration plan involves:

1. **Large-Scale Refactoring**: Structural changes affecting multiple files, renaming packages, or migrating patterns across the codebase.
2. **Multi-File Code Generation**: Creating complex component hierarchies, service layers, API wrappers, or test suites spanning several files.
3. **Isolated UI Testing**: Running end-to-end UI tests, rendering checks, visual regression tasks, or headless browser tests.
4. **Iterative Search & Codebase Research**: Deep multi-step codebase exploration, dependency audits, symbol tracking, or exhaustive log analyses.
5. **Background Compute Work**: Any development task expected to require extensive iterative prompt execution that shouldn't lock up Antigravity's active turn.

---

## Execution Workflow

### Step 1: Format the Standalone Task Prompt
Construct a concise, clear, and unambiguous prompt string describing the subtask. 
- Ensure it contains explicit instructions, constraints, and completion criteria.
- Include all necessary context directly in the prompt.

### Step 2: Attach Context Files via `@` Notation
When the subtask relies on existing files, explicitly attach them using `@filename` or `@path/to/file` syntax within the task prompt.
- Example: `"Refactor @src/auth/provider.ts and @src/types/user.ts to use the new Clerk JWT claims schema."`

### Step 3: Dispatch Asynchronous Command
Execute the headless `opencode` runner using `run_command` in non-blocking mode:

```bash
opencode run "$task_description" --auto
```

- **Flag `--auto`**: Auto-approves permissions for seamless execution.
- **Asynchronous Execution**: Pass a small `WaitMsBeforeAsync` (e.g., `1000`) so the tool call launches the process as a background task.
- **Thread Safety**: Do **NOT** lock up the active conversation thread or poll in a loop. Antigravity will be automatically notified upon completion.

---

## Command Syntax Reference

| Scenario | Command Pattern |
|---|---|
| Basic Subtask | `opencode run "$task_description" --auto` |
| Subtask with Context Files | `opencode run "Refactor @src/components/Header.tsx to add dark mode toggle" --auto` |
| Targeted Model Run | `opencode run "$task_description" --model provider/model-name --auto` |
| Specify Project Path | `opencode ./path/to/subproject run "$task_description" --auto` |

---

## Post-Execution & Verification

1. **Silent Log Inspection**: When the task completes and emits a notification, review the output logs silently using `view_file` on the task log path.
2. **Code Integrity Verification**: Inspect modified files or run `git diff` / test commands to ensure quality.
3. **User Update**: Summarize the completed subtask results clearly in the main conversation thread.

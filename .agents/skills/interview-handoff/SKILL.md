---
name: interview-handoff
description: Save or resume an interview session across Codex desktop, VS Code or a fresh chat using repository context and a single active writer.
---

In attached mode, read the session's `context.json` first. Resolve role/skill paths
from `harness_root`, specs/plans/evidence summaries from `session_root`, and code,
commands and Git operations from `target_root`. Preserve the target's instructions.
Explicitly pass these paths to workers; do not assume cross-repository discovery.


Read root `AGENTS.md` and `docs/ACTIVE_SESSION`. On save, stop or finish outstanding
worker writes before transferring ownership. Update the active session's `handoff.md`
with repository/worktree path, branch, HEAD, dirty files, current interface/owner,
checkpoint, next concrete action, validation status and live process/port details.
Point to spec, plan and evidence; do not dump the transcript. Record unresolved human
decisions accurately. Do not commit merely to switch interfaces.

On resume, inspect actual Git state and compare with the handoff. Read the spec and
current checkpoint, then only relevant roles/code. Resolve mismatches and outstanding
writers before editing; do not trust a stale green result or assume a lock is enforced.
State the immediate next action and continue already authorized work.

Use the same checkout in both interfaces. Native chat continuation may depend on the
installed product; this workflow relies on files, not synchronized conversation memory.
If the skill is not discovered, read this file explicitly and follow it. If no active
session exists, report that and begin intake rather than inventing prior work.

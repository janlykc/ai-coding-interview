---
name: engineering-handoff
description: Save or resume a development session across Codex desktop, VS Code or a fresh chat using repository context and a single active writer.
---

Read root `AGENTS.md` for shared policy and session/path resolution. Use the active
integration worktree in the handoff after verifying its target repository identity.
On save, stop or finish outstanding
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

For UI work, include design.md, Paper file/page links, agreed revision and outstanding
canvas ownership in the handoff. Record any workflow lesson already applied to the
harness so the next interface continues with the updated instructions.

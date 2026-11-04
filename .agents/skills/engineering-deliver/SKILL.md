---
name: engineering-deliver
description: Coordinate implementation, independent verification, code review and Git checkpoints against an agreed specification and plan.
---

In attached mode, read the session's `context.json` first. Resolve role/skill paths
from `harness_root`, specs/plans/evidence summaries from `session_root`, and code,
commands and Git operations from the explicitly assigned implementation worktree
(defaulting to `target_root`). Verify that worktree belongs to the target Git repository.
Preserve the target's instructions.
Explicitly pass these paths to workers; do not assume cross-repository discovery.


Read the harness root `AGENTS.md`, `ai_team/coordinator/AGENTS.md` and the active session's spec,
plan and handoff when present. Follow the human's current direction. Missing documents
do not force a return to design: use the task and known context, recommend a default
for ambiguity, and ask only when a consequential decision genuinely blocks useful work.

Load other skills and role files only when their work becomes necessary. A checkpoint
does not require a new worker for every responsibility; reuse suitable workers while
preserving independent review. Do not spawn idle spec author, UX, QA or delivery agents.

For each checkpoint:
1. Dispatch a developer with acceptance IDs, relevant code, owned paths, dependencies,
   verification expected and stop condition. Read the matching role file; pass only
   necessary context. Delegation is the default; honor a requested direct-execution mode.
2. Have the developer implement and run focused checks. Have QA independently check
   acceptance and risky seams using `ai_team/qa/AGENTS.md`. UX is optional for UI work.
3. Coordinator inspects the diff, callers and evidence. Route concrete defects back to
   the owner. Keep unavailable checks and remaining risks explicit. Changes invalidate
   relevant earlier evidence; obtain updated results before accepting.
4. Update checkpoint status and review disposition in the plan. Have delivery commit a
   coherent reviewed checkpoint and push only under the recorded session policy.
   Do not require redundant human approval for previously authorized actions.
5. Refresh the short handoff with code state, next action and any live processes.

In standalone mode, optionally use `harness.commands.json` for application commands.
An empty list is unconfigured, not passing. In attached mode use target-native commands
in the assigned implementation worktree; the harness runner deliberately refuses that
mode. Harness self-tests never validate application code.
No deployment is assumed; use local run/smoke first. If deployment is required, establish
its authorized target and record serving revision and smoke result separately from Git.

Keep loops bounded by the agreed time and resource budget. Escalate decisions about behavior,
architecture, scope or material risk; allow routine experiments within the checkpoint.
Conclude with a runnable demonstration, evidence, key code path and honest limitations.

For UI checkpoints, use the Paper references in session design.md. Arrange UX and
QA review of the rendered implementation against the agreed revision. Feed behavior
changes back to the lead and assigned spec writer and concrete implementation discrepancies back to developers.
Apply corrections to current behavior immediately; record lessons briefly and update
the harness at a natural checkpoint or after the task, following
docs/workflow-learnings.md.

For parallel components, follow docs/worktrees.md with disjoint worktree ownership and
one integration owner. Use engineering-review for an independent CR pass before accepted
check-in/submission; use engineering-test-deploy for run/smoke and candidate-bound QA.
Consult docs/submission.md for Codex review paths, findings disposition and publication.
Review and test the combined candidate after merging worker branches.

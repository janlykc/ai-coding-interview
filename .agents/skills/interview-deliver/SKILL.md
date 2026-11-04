---
name: interview-deliver
description: Coordinate implementation, independent verification, code review and Git checkpoints against an agreed interview specification and plan.
---

In attached mode, read the session's `context.json` first. Resolve role/skill paths
from `harness_root`, specs/plans/evidence summaries from `session_root`, and code,
commands and Git operations from `target_root`. Preserve the target's instructions.
Explicitly pass these paths to workers; do not assume cross-repository discovery.


Read root `AGENTS.md`, `ai_team/coordinator/AGENTS.md` and the active session's spec,
plan and handoff. If agreement or critical requirements are missing, return to design.

For each checkpoint:
1. Dispatch a developer with acceptance IDs, relevant code, owned paths, dependencies,
   verification expected and stop condition. Read the matching role file; pass only
   necessary context. Coordinator stays out of implementation and test execution.
2. Have the developer implement and run focused checks. Have QA independently check
   acceptance and risky seams using `ai_team/qa/AGENTS.md`. UX is optional for UI work.
3. Coordinator inspects the diff, callers and evidence. Route concrete defects back to
   the owner. Keep unavailable checks and remaining risks explicit. Changes invalidate
   relevant earlier evidence; obtain updated results before accepting.
4. Update checkpoint status and review disposition in the plan. Have delivery commit a
   coherent reviewed checkpoint and push only under the recorded session policy.
   Do not require redundant human approval for previously authorized actions.
5. Refresh the short handoff with code state, next action and any live processes.

Use `harness.commands.json` for application commands once discovered. An empty command
list is unconfigured, not passing. Harness self-tests do not validate application code.
No deployment is assumed; use local run/smoke first. If deployment is required, establish
its authorized target and record serving revision and smoke result separately from Git.

Keep loops bounded by the remaining interview time. Escalate decisions about behavior,
architecture, scope or material risk; allow routine experiments within the checkpoint.
Conclude with a runnable demonstration, evidence, key code path and honest limitations.

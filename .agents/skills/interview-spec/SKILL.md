---
name: interview-spec
description: Turn an interview task into an agreed concise specification and checkpoint implementation plan before coding, or revise them when requirements change.
---

In attached mode, read the session's `context.json` first. Resolve role/skill paths
from `harness_root`, specs/plans/evidence summaries from `session_root`, and code,
commands and Git operations from the explicitly assigned implementation worktree
(defaulting to `target_root`). Verify that worktree belongs to the target Git repository.
Preserve the target's instructions.
Explicitly pass these paths to workers; do not assume cross-repository discovery.


Read the harness root `AGENTS.md` and the explicitly assigned session (or harness
active-session pointer). Resolve workflow paths from the harness, not the target.
Create a missing session using the matching README mode; the new-session helper is
standalone-only. In parallel work, the assigned worktree overrides target_root for
application operations after verifying it belongs to the same Git repository.

1. Inspect the task and relevant code. Confirm time available and any task-specific
   restrictions. Do not invent a task if none is supplied.
2. Use `ai_team/program_manager/AGENTS.md` for spec authorship and combine
   `ai_team/scribe/AGENTS.md` unless separate recording is useful. Ask a developer
   using `ai_team/developer/AGENTS.md` for entry points, contracts and test commands.
3. Collaborate with the human PE/product owner. Capture behavior, exclusions,
   acceptance examples, component contracts, edge cases and uncertain decisions in
   `spec.md`. Recommend defaults and surface consequential tradeoffs.
4. The coordinator turns the agreed direction into small, ordered checkpoints in
   `plan.md`: acceptance IDs, owners/files, dependencies, test evidence and exit criteria.
   Record local commit policy and any authorized remote/branch. Discuss whether
   local running suffices or deployment is actually part of acceptance.
5. Ask for agreement to the spec and first checkpoint. Record the actual decision;
   do not manufacture an approval. Implementation may then proceed within agreed scope.

For 60–75 minutes, aim for roughly 5–10 minutes of design, adjusted to the task.
Avoid spawning the whole team or requiring exhaustive documentation. On later changes,
revise only affected requirements/checkpoints and preserve decisions that explain why.

For a task with UI, use interview-ui-design and the PM–UX–developer group. Paper is
the default canvas, with access verified in the UX worker. PM owns requirements; UX
owns design.md and redlines; dev supplies feasibility. Reference agreed designs in
the spec and plan before implementing the relevant UI checkpoint.

When planning parallel sections, agree component contracts and dependencies before
splitting worktrees. Record each owner/path/base, integration order, CR checkpoint,
test environment and intended submission finish line. Prefer one checkout when the
coordination cost outweighs useful independent work. See docs/worktrees.md.

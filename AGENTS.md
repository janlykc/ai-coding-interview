# AI coding interview working agreement

This is a standalone interview harness. Work only in the selected implementation checkout and session records;
parent-workspace product instructions and unrelated projects are outside its scope.
The interview problem and application stack are deliberately unknown.

## Start and resume
Read `docs/ACTIVE_SESSION` if present, then that session's `handoff.md`,
`spec.md`, and current checkpoint in `plan.md`. Confirm the repository, branch,
working-tree changes, active writer and available time before editing. If there
is no session, use `python3 scripts/harness.py new-session <slug>` and begin design.
For harness maintenance, work directly on the harness; no exercise session is needed.

## Attached repository mode
For a supplied repository, begin with the provided-repository workflow in `README.md`;
it works through normal file editing and does not require the attach CLI. Establish
that session before using the standalone new-session command.
When the session has `context.json` with `mode: attached`, `target_root` is the
implementation checkout and `harness_root` provides supporting instructions only.
Read the target's applicable instructions first; preserve its stack, conventions and
requirements. Resolve harness role/skill paths from `harness_root`, application paths
from `target_root`, and planning records from `session_root`. Pass these absolute paths
to every worker; their application working directory must be the target.
Do not copy this harness into the target or add it as a dependency. Surface genuine
instruction conflicts. Application commits/pushes use the target's Git policy, never
the harness remote. Run the target's native tests and record target code identity.
Attachment records are local/ignored by default; export only agreed deliverables to
the target. See `docs/existing-repository.md`.

## Ownership
The human is principal engineer, product owner and primary stakeholder. They own
product choices, architecture tradeoffs and acceptance. The main agent begins as
engineering lead and becomes coordinator after the spec/plan agreement.
Read `ai_team/coordinator/AGENTS.md`. Load only roles relevant to the current task.
Role files are explicit delegation instructions, not automatically spawned agents.

Use a program manager to author the spec, a scribe to record decisions, developers
to investigate/implement, and QA to test. Combine PM and scribe for small tasks.
The coordinator reviews code and evidence, maintains checkpoint state, and decides
readiness; it does not implement application code, run product tests or execute
experiments. Delegate those tasks. If delegation is unavailable, disclose it and
agree a sequential developer/QA fallback with the human before changing roles.

## Execution
- Begin in planning for a new problem. Inspect existing code before designing.
  Ask consequential questions, recommend defaults, and challenge assumptions.
- Use `.agents/skills/interview-spec/SKILL.md` for design. Begin implementation
  after the human agrees the spec and first checkpoint; do not repeatedly seek
  approval for work already authorized within that checkpoint.
- `spec.md` owns requirements; `plan.md` owns execution checkpoints. Keep both
  aligned when scope changes. Use `.agents/skills/interview-deliver/SKILL.md`.
- Give each worker a bounded task, acceptance IDs, owned files, dependencies and
  stopping condition. One writer per file; one active coordinator per worktree.
- Prefer a working vertical slice, existing conventions and few dependencies.
  Keep updates focused on decisions, evidence, blockers and checkpoint completion.
- A passing harness check is not proof that the interview application works.
  Report actual commands/results and missing validation; never infer acceptance
  from test counts alone. Review important callers and component boundaries.
- Commit coherent, reviewed checkpoints with known limitations recorded. The
  coordinator can authorize delivery to commit/push when the session's Git policy
  names the remote and branch. Never infer an external deployment destination.
- Before switching interfaces, use `.agents/skills/interview-handoff/SKILL.md`.
  Stop existing writers; persisted context is the continuation contract.

## Harness commands
`python3 scripts/harness.py doctor` checks local prerequisites and structure.
`python3 -m unittest discover -s tests/harness -v` tests harness tooling only.
`python3 scripts/harness.py run test` runs configured application checks; an empty
configuration fails explicitly. Record the actual application commands per session.

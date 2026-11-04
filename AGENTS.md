# AI coding interview working agreement

This is a standalone interview harness. Work only in the selected implementation checkout and session records;
parent-workspace product instructions and unrelated projects are outside its scope.
The interview problem and application stack are deliberately unknown.

## Start and resume
First identify standalone versus attached mode from the user's task. An explicitly
assigned session path takes precedence over the harness's `docs/ACTIVE_SESSION`
pointer. Read that session's handoff, spec and current plan checkpoint, then verify
actual checkout/branch/dirty state and outstanding writers. In attached mode the
pointer and workflow files belong to the harness, never the supplied repo.
If no session exists, follow the README's matching mode. For a new standalone task,
use a fresh exercise worktree; preserve main as the reusable baseline. The optional
new-session helper must not replace an attached session. Harness maintenance needs
no exercise session. Never invent an interview problem to fill empty templates.

## Attached repository mode
For a supplied repository, begin with the provided-repository workflow in `README.md`;
it works through normal file editing and does not require the attach CLI. Establish
that session before using the standalone new-session command.
When the session has `context.json` with `mode: attached`, `target_root` is the
implementation checkout and `harness_root` provides supporting instructions only.
Read the target's applicable instructions first; preserve its stack, conventions and
requirements. Resolve harness role/skill paths from `harness_root`, application paths
from `target_root`, and planning records from `session_root`. Pass these absolute paths
to every worker. A worker's explicit worktree assignment is its application directory,
not necessarily the original target_root. Verify it belongs to the same Git repository
(e.g. matching resolved git common directory); do not rewrite shared context.json for
each parallel worker. The handoff names the active integration checkout.
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

## On-demand agent library
Start with the lead only; do not preload role files or spawn a default team.
Load the skill for the current work, then delegate only when there is a concrete
bounded assignment. PM/scribe joins when spec authorship is needed; a developer
joins for necessary investigation or implementation; UX joins when design work
warrants it; independent QA/CR joins when there is a candidate to evaluate.
Phase changes do not automatically spawn agents. Use the activation guidance in
`ai_team/README.md`; release idle workers before bringing in others. One independent non-implementer may
perform QA and CR as separate passes. An existing developer may execute delivery
under coordinator direction after implementation stops. Preserve independence and
the coordinator's non-implementation role. Respect actual runtime slot limits.

## UI design and learning from use
When UI design warrants a Paper pass, load
`.agents/skills/interview-ui-design/SKILL.md` and involve PM, UX and developer
only for the contributions needed; they need not run simultaneously. UX owns Paper designs/redlines; PM owns
the specification; developer contributes feasibility and implements; UX/QA review
the running result. Verify Paper access in the actual UX worker before relying on it.
Use the dedicated ai-interview project described in `docs/paper-design.md`.

Apply explicit corrections to current behavior immediately. Record demonstrated
workflow improvements briefly and update the relevant harness role/skill at a natural
checkpoint or after the timed exercise, unless a blocking fix is needed. Use `docs/workflow-learnings.md`. Keep changes scoped and evidence-based;
do not just promise to remember, copy private chat history, or create background jobs.

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

## Parallel work and submission
Use `docs/worktrees.md` for independent component worktrees and a single integration
owner. Record each worker's exact checkout, branch, base, owned files, dependencies
and test environment. Never confuse an attached application's worktree with the harness.
Use `interview-review` and `ai_team/reviewer/AGENTS.md` for an independent CR pass;
reviewers must not have implemented the candidate. Codex local and provider reviews
retain their own status. Follow `docs/submission.md` for check-in, integration and
submission. Use `interview-test-deploy` for local run/smoke and QA of the actual candidate.
Changes to candidate/base/dependencies require refreshing affected evidence.

## Harness commands
`python3 scripts/harness.py doctor` checks local prerequisites and structure.
`python3 -m unittest discover -s tests/harness -v` tests harness tooling only.
`python3 scripts/harness.py run test` runs configured application checks; an empty
configuration fails explicitly. Record the actual application commands per session.

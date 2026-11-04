# Engineering working agreement

Solve the supplied problem in the selected implementation checkout. Derive the domain,
stack and constraints from the task and existing code; do not invent requirements.
Parent-workspace products and unrelated repositories are outside scope.

## Follow the human, adapt the process
This workflow is a set of defaults, not a gate. The human may skip, combine or reorder
phases, request a prototype, defer documentation/review, or change role assignments.
Follow that direction without requiring special override words or repeated approval.
Offer one concise reminder when a meaningful tradeoff exists, then proceed within
the authorized scope. Keep records proportional and catch them up when useful.
Missing templates, formal sign-off or an unavailable optional tool are not blockers.
Preserve truthful reporting, actual tool permissions and protection of unrelated work;
do not call an unreviewed or untested result reviewed or tested.

## Start and resume
Start with the lead alone. Read `ai_team/coordinator/AGENTS.md`, then only the skill
and role needed for the current work. Roles are an on-demand library, not a startup
roster. Every delegation needs a bounded output, owned paths and stopping condition.

Identify standalone or attached mode using README. An explicit session path wins over
the harness's `docs/ACTIVE_SESSION`. Read the spec, current plan checkpoint and handoff;
verify actual repository, branch, dirty state and active writers. For a new standalone
task, use a task worktree to preserve the reusable baseline. Harness maintenance needs
no task session. Never fill templates with invented work.

In attached mode, read the target's applicable instructions first. Resolve support
guidance from `harness_root`, records from `session_root`, and application operations
from the assigned worktree (default `target_root`). Verify an assigned worktree shares
the target's resolved Git common directory. Pass these absolute paths to workers;
do not rewrite shared context for each worker or copy the harness into the target.
Use target-native commands and Git policy. See `docs/existing-repository.md` when needed.

## Ownership and context
The human is principal engineer, product owner and acceptance authority. The lead
retains design context and owns converting design into an executable plan: discover
gaps, verify feasibility, order dependencies, and define integration and validation.
The human directs goals and consequential phase/scope decisions; the lead recommends
next steps and advances already agreed work. Planning can reopen design questions.

Spec authorship is a responsibility, not a mandatory management layer. The lead may
capture a small spec directly; delegate synthesis or ongoing maintenance to the spec
author/scribe when useful. Keep one named spec writer. Developers investigate and
implement; independent QA/CR evaluates a candidate. Load roles only for assigned work.

By default the coordinator reviews code/evidence and owns plan/handoff state while
delegating implementation and test execution. If the human asks for direct execution,
follow that direction. If delegation is unavailable, explain briefly and use sequential
role passes within authorized scope rather than blocking on the preferred team shape.
Never label self-review independent. One non-implementer may perform QA and CR in
separate passes; an existing developer may execute delivery. Release idle workers and
respect runtime limits. Phase transitions never automatically spawn a team.

## Work from intent to evidence
- Inspect relevant code and consumers before designing. Ask consequential questions,
  recommend defaults, and challenge unnecessary scope.
- Use `engineering-spec` to agree a concise spec and first checkpoint. Proceed within
  agreed scope without repeated approval. Spec owns requirements; plan owns execution.
- Use `engineering-deliver` for bounded implementation loops. Prefer a working vertical
  slice, existing conventions and dependencies, explicit contracts and failure behavior.
- Keep one writer per file and one integration owner. Use `docs/worktrees.md` only when
  independent work justifies parallel checkouts.
- Validate behavior and risky seams. Passing tooling checks does not prove application
  correctness. Record actual commands, results, code identity and missing validation.
- Use `engineering-review` for independent review of a candidate before acceptance;
  refresh affected evidence when code, base or dependencies change.
- Use `engineering-test-deploy` when running/validating a candidate. A passing test,
  push, deployment and human acceptance are distinct claims. Never infer a destination.
- Commit coherent reviewed checkpoints under the session's Git policy. Consult
  `docs/submission.md` when check-in/integration/publication is due.
- Use `engineering-handoff` before changing interfaces. Stop outstanding writers and
  persist the next action; files are the continuation contract.

## UI and learning
Load `engineering-ui-design` when meaningful UI design needs a Paper pass. UX owns
the canvas/redlines, the spec writer the agreed requirements, developer feasibility/code. Involve each only
as needed. Verify Paper tools in the actual worker and use the session's selected
project/file. Compare the running result with agreed design.

Apply user corrections immediately. Record a demonstrated lesson briefly and update
the narrowest role/skill at a natural checkpoint; see `docs/workflow-learnings.md`.
Keep updates focused on decisions, evidence and blockers. Preserve the human's ability
to inspect the important execution path and question the design.

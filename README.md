# AI coding interview harness

A reusable, stack-neutral workspace for a 60–75 minute AI-assisted coding interview.
You act as principal engineer and product owner. A program manager authors the
spec; developers implement; QA verifies; the lead coordinates and reviews.

For an existing codebase, start with [the provided-repository workflow](#using-this-harness-with-a-provided-repository). It requires only this README and the role files.

## Start here

Give the agent the task and the paths in [the opening prompt](prompts/start.md).
Begin with your normal design discussion: PM/scribe drafts the spec, developer
supplies feasibility, and UX joins in Paper for UI work. Agree the first checkpoint;
the same lead then coordinates implementation and review. Start with a small active
team, bringing QA/CR in when there is code to inspect. You do not need every role,
skill, worktree or template at once.

For tomorrow's practice, use [the test-drive plan](docs/test-drive.md). The initial
[holistic assessment](docs/holistic-assessment.md) distinguishes readiness checks from
what only a real sample-question session can tell us.

## Open a standalone exercise

Keep this repo's main branch as the reusable baseline. Create an exercise worktree
using the reuse instructions below, then open its `interview.code-workspace` in VS
Code and that same checkout in Codex. The agent may create session files directly;
the commands below are optional helpers.

```sh
python3 scripts/harness.py doctor
python3 scripts/harness.py new-session practice-01
```

Paste [the start prompt](prompts/start.md) into either interface and provide the
interviewer's task. The agent starts a design discussion, fills the spec and plan,
and waits for your agreement before application implementation. No application
framework, infrastructure or sample solution is preselected.

VS Code: **Terminal → Run Task → Harness: doctor** or **Harness: new session**.
The workspace recommends the Codex and Python extensions; JavaScript/TypeScript
editing is built into VS Code. Authentication and model selection remain yours.

## Using this harness with a provided repository

Keep the two repositories alongside each other. Open the provided repository in
VS Code or Codex, and tell the agent where this README is. You do not need to
install the harness, run an attachment command, or copy its files into the project.

Give the agent this instruction, replacing the paths:

> Read `/path/to/ai-coding-interview/README.md` and use its provided-repository
> workflow. Our implementation repository is `/path/to/provided-repo`.
> I am the principal engineer and product owner. Begin a design session with me;
> use the harness's team roles to produce a concise spec and implementation plan
> before coding. The task is: [paste the task].

### Instructions for the agent

1. **Establish the two roots.** The provided repo is the implementation target;
   this harness supplies collaboration instructions. Confirm the target's Git root,
   branch and existing changes. Read its applicable `AGENTS.md`, README and project
   configuration before designing. Preserve its conventions and surface conflicts.
2. **Load the team guidance explicitly.** Read this harness's `AGENTS.md`, then
   `ai_team/coordinator/AGENTS.md`. Read only the other role files and skills needed
   for the current phase. Resolve those paths from the harness, not the target.
3. **Keep a small session record.** Create a new, non-overwriting folder under this
   harness's `.harness/sessions/<session-name>/`. Use `docs/templates/` as needed.
   Record the absolute target, harness and session paths in `context.json` using
   `mode: attached`, `target_root`, `harness_root` and `session_root`. Set the harness's
   `docs/ACTIVE_SESSION` to that folder's relative path. These files are local and
   ignored by Git. No CLI is required; normal file editing is sufficient.
4. **Design together, then coordinate.** The human owns product and principal
   engineering decisions. PM/scribe authors the spec; developers explain the existing
   code and implementation options. Once the human agrees the spec and first
   checkpoint, coordinate implementation, QA and review using the plan.
5. **Do application work in the target.** Give every worker the target working
   directory, absolute harness role path, session path and bounded assignment.
   Use the target's dependencies and native test/build commands. Review real diffs
   and record validation against the target's code state. Application commits and
   authorized pushes belong to the target; the harness remote is unrelated.
6. **Preserve continuation.** Before switching between Codex and VS Code, stop
   outstanding writers and update the session handoff with target Git state, current
   checkpoint, results and next action. The next agent reads those files and verifies
   the checkout before continuing. Export specs into the target only when requested.

You may add the harness as a second VS Code folder for browsing, but work on application
code in the provided repo. Its setup remains independent of this harness's Python tools.
The existing `interview attach` helper is optional; it automates the session records
and two-folder workspace described above. The README workflow works without it.

## UI work: PM + Paper UX + developer

For a UI task, use the established design group: PM authors the spec, UX designs in
Paper, and developers contribute codebase knowledge and feasibility. Agree the
important redlines with the human, implement, then have UX/QA review the running UI.

[Paper setup and interview workspace](docs/paper-design.md) includes the dedicated
ai-interview project. The `interview-ui-design` skill handles this loop. Verify MCP
access in the actual UX worker; role files do not create a connection automatically.

Agents should apply workflow lessons from your corrections and actual usage to the
relevant roles/skills during the work. [Recorded learnings](docs/workflow-learnings.md)
keep those changes explicit and scoped, without adding a background monitoring system.

## Workflow and files

| Stage | Owner | Durable output |
| --- | --- | --- |
| Frame and design | You + PM, developer input | `spec.md` with acceptance examples |
| Sequence | Lead + PM | `plan.md` with bounded checkpoints |
| Implement | Developer | Code and focused tests |
| Verify | QA; UX for visual work | `validation.md` tied to code state |
| Review and checkpoint | Coordinator; delivery executes Git | Review disposition and commit |
| Continue elsewhere | Current coordinator | `handoff.md` and stopped workers |

[Roles](ai_team/README.md) explain delegation. [Workflow](docs/workflow.md) describes
testing, review, deployment and pacing. [IDE setup](docs/ide-setup.md) covers
continuation and existing-repository exercises. [Interview preparation](docs/interview-prep.md)
records the supplied guide's constraints and a rehearsal checklist.

`docs/ACTIVE_SESSION` is a local pointer to the current session. Standalone sessions
live in `docs/sessions/`; attached sessions live in ignored `.harness/sessions/`. Each session
contains a spec, implementation plan, decisions, validation, handoff and retrospective.
These are small working records, not a requirement to fill every field before coding.
Keep task-specific code in paths that suit the problem; do not put application code
inside `ai_team/` or the harness's own tests.

## Worktrees, code review and submission

Use native Git and the agents to demonstrate the development loop:

1. Agree component boundaries and checkpoints; use separate worktrees only where
   parallel work helps. Record branch/path, owner, shared contracts and integration order.
2. Developers implement/test; a fresh **CR subagent** reviews the actual diff and callers.
   Fix findings and recheck the reviewed candidate. Use Codex local or configured PR
   review as appropriate, keeping each review's scope and status explicit.
3. Delivery checks in coherent snapshots and integrates accepted branches. Test and
   review the combined result, not just each worker branch in isolation.
4. Run the candidate locally (or an agreed preview), smoke it, and have QA/UX validate
   acceptance against the actual running code and Paper redlines.
5. Demonstrate Git history, the important diff, review results and working behavior.
   Push/open a PR/merge only to the destination agreed for that exercise.

[Worktree examples](docs/worktrees.md) and [submission/review/test-deployment guide](docs/submission.md)
contain the human-and-agent procedure. Skills: `interview-review` and
`interview-test-deploy`; reviewer role: `ai_team/reviewer/AGENTS.md`.
No additional command wrapper or company deployment service is required.

## Reuse without accumulating interview solutions

Keep `main` as the clean harness. After a clean baseline is committed, start each
exercise in a separate branch/worktree:

```sh
git worktree add -b interview/practice-01 ../interview-practice-01 main
```

Open the new worktree's workspace, create its session and work there. Keep both
interfaces on that worktree. A branch isolates changes, not Git history: for an
interview that needs a clean history, copy the clean tracked baseline into a new
folder with `git archive main | tar -x -C /path/to/empty-folder`, then initialize Git
there. Do not carry earlier confidential tasks into another interview. Promote only
general workflow improvements back to `main` after rehearsal, with relevant checks.

The `.agents/skills/` workflows are repository-local and need no global install.
There is no runtime agent service, background deployment, paid API dependency or
automatic commit/push hook. The coding agent orchestrates explicitly.

## Optional setup and checks

[Project tooling](docs/project-tooling.md) explains pyproject.toml, make setup/check,
the virtual environment, application command configuration and package verification.
The provided-repository workflow needs none of this installed into the target.

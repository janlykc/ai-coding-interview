# AI engineering harness

A reusable, stack-neutral workspace for solving software problems with an AI team.
You act as principal engineer and product owner. The engineering lead works directly
with you, turns design into an executable plan, and coordinates specialists as needed.
Spec authors capture intent; developers implement; independent QA/CR evaluates.

For an existing codebase, start with [the provided-repository workflow](#using-this-harness-with-a-provided-repository). It requires only this README and the role files.

The operating instructions are a domain-neutral engineering team: they solve the
supplied problem using its actual constraints, without a preselected domain or timebox.
Skills now use the `engineering-*` names. The existing `interview` CLI, Python package
and workspace filename remain compatible tooling names.

## Process is advisory
Your direction takes precedence over the default workflow. Skip or combine phases,
ask for a prototype, defer paperwork, or change the team as needed. Agents should
offer a concise reminder about meaningful tradeoffs and keep moving, without making
you fight templates or repeat permission. They still report what was actually tested,
reviewed and completed.

## Working model

Think of a kitchen: you set the intended result and standards; the engineering lead
organizes the work, checks what is missing, sequences dependencies and brings in the
right sous chefs. Specialists receive bounded assignments, not standing seats.
A spec author helps capture decisions when useful; it is not a management layer.

Design → proposed implementation plan → exposed gaps → refined design → agreed
checkpoint. The lead owns this loop and recommends the next step; you resolve
consequential product and architecture choices. Routine agreed execution stays autonomous.
Use this model for the actual problem, then refine it from observed results.

## Pairing when you want it

Say “pair with me” for closer discussion and smaller changes you can inspect together.
For example:

> Pair with me on this task. Help me reason through the approach, keep changes small
> enough to explain, and work through verification with me. Delegate only when useful.

Say “take this checkpoint and run with it” for more autonomy, or “slow down and walk
me through this” for more involvement. This is a preference within the same workflow;
the behavior is defined once in [AGENTS.md](AGENTS.md#pair-with-me).

## Start here

Give the agent the task and the paths in [the opening prompt](prompts/start.md).
Start with the lead and your normal design discussion. The roles are an on-demand
library, not a team loaded at startup. Load only the skill for the current work and
spawn a subagent when it has a concrete assignment: spec author/scribe for spec authorship,
developer for needed investigation or implementation, UX for meaningful Paper design,
and independent QA/CR when there is a candidate to evaluate. Agree the first checkpoint;
the same lead then coordinates implementation and review. A phase change does not
automatically load more roles, skills, worktrees or templates.

## Open a standalone task

Keep this repo's main branch as the reusable baseline. Create an task worktree
using the reuse instructions below, then open its `interview.code-workspace` in VS
Code and that same checkout in Codex. The agent may create session files directly;
the commands below are optional helpers. New sessions start with spec, plan and
handoff only; copy other templates when they become useful.

```sh
python3 scripts/harness.py doctor
python3 scripts/harness.py new-session task-01
```

Paste [the start prompt](prompts/start.md) into either interface and provide the
problem and desired outcome. The agent starts a design discussion, fills the spec and plan,
and checks unresolved consequential choices before implementing. Your instruction
to proceed or prototype is sufficient; no separate sign-off ritual is required. No application
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
   engineering decisions. The lead or delegated spec author captures agreed intent in the spec; developers explain the existing
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

## Read only what the task needs

| Need | Reference |
| --- | --- |
| Agent behavior and skill selection | [AGENTS.md](AGENTS.md) |
| Assign specialist work | [Role library](ai_team/README.md) |
| Select validation depth | [Verification choices](docs/workflow.md) |
| Use Paper | [Design workspace](docs/paper-design.md) |
| Continue in VS Code or Codex | [IDE setup](docs/ide-setup.md) |
| Parallel component work | [Worktrees](docs/worktrees.md) |
| Git review, integration and publication | [Submission](docs/submission.md) |

Templates under docs/templates are optional starting points, not forms to complete.
The active session pointer is local; attached records live in ignored .harness/sessions,
and standalone records in docs/sessions. Keep application code outside ai_team and
the harness's own tests.

## Reuse without accumulating task solutions

Keep `main` as the clean harness. After a clean baseline is committed, start each
task in a separate branch/worktree:

```sh
git worktree add -b feature/task-01 ../task-01 main
```

Open the new worktree's workspace, create its session and work there. Keep both
interfaces on that worktree. A branch isolates changes, not Git history. If a task
requires a clean history, export the tracked baseline into an empty folder with
`git archive main | tar -x -C /path/to/empty-folder`, then initialize Git there.
Keep confidential work separate. Promote general workflow improvements to main
at a natural checkpoint with relevant checks.

The `.agents/skills/` workflows are repository-local and need no global install.
There is no runtime agent service, background deployment, paid API dependency or
automatic commit/push hook. The coding agent orchestrates explicitly.

## Optional setup and checks

[Project tooling](docs/project-tooling.md) explains pyproject.toml, make setup/check,
the virtual environment, application command configuration and package verification.
The provided-repository workflow needs none of this installed into the target.


## Optional human preparation

For interview-specific preparation, see [the supplied guide notes](docs/interview-prep.md),
[the rehearsal plan](docs/test-drive.md) and [the initial assessment](docs/holistic-assessment.md).
These are optional preparation records, not operating instructions for task agents.

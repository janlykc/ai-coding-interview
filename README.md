# AI coding interview harness

A reusable, stack-neutral workspace for a 60–75 minute AI-assisted coding interview.
You act as principal engineer and product owner. A program manager authors the
spec; developers implement; QA verifies; the lead coordinates and reviews.

## Project foundation

Uses a `pyproject.toml`, `src/` package layout, Hatchling build backend and a local
virtual environment, adapting the packaging conventions of the existing repositories.
The harness has no runtime dependencies. Development dependencies are pinned in
`requirements-dev.lock`; Python 3.11+ is required. Application dependencies and any
frontend manifest will be chosen when the actual problem is known.

```sh
make setup
make check
.venv/bin/interview doctor
```

`make setup` creates `.venv`, installs the pinned development tools and installs the
package in editable mode. `make check` runs lint/format checks, harness tests, package
build and doctor. On Windows or without Make, use `python -m venv .venv`, the venv's
Python to install `-r requirements-dev.lock`, then `pip install --no-build-isolation
--no-deps -e .`; run the equivalent commands listed in Makefile. The pinned file records
this verified development environment, not a universal cross-platform resolver lock.

## Open and start

Open `interview.code-workspace` in VS Code, or open this repository as a local
Codex project. Use both side by side against the **same checkout**.

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

`docs/ACTIVE_SESSION` points to the current folder in `docs/sessions/`. Each session
contains a spec, implementation plan, decisions, validation, handoff and retrospective.
These are small working records, not a requirement to fill every field before coding.
Keep task-specific code in paths that suit the problem; do not put application code
inside `ai_team/` or the harness's own tests.

## Configure application commands when the task is known

`harness.commands.json` starts empty. The harness never labels that as a passing test.
Add executable argument arrays with a working directory relative to this repository:

```json
{
  "test": [{"argv": ["python3", "-m", "pytest", "tests/app"], "cwd": ".", "timeout_seconds": 120}],
  "lint": [],
  "build": [],
  "dev": []
}
```

This is an example, not an installed dependency or prescribed stack. Add multiple
steps for multiple components, using their own working directories. No shell
expansion is performed. `python3 scripts/harness.py run test` executes configured
steps in order, stops on failure and writes a receipt plus logs to ignored
`.harness/evidence/`. Use `run lint`, `run build`, or `run dev` similarly. Interactive
servers are often easier in a dedicated terminal; record their command/port in the
handoff and stop them when done. Never put credentials in command arguments or logs.
Summarize relevant evidence in the session's tracked `validation.md`.

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

## Verify the harness

```sh
python3 -m unittest discover -s tests/harness -v
python3 scripts/harness.py doctor
```

These checks cover harness tooling, not a future application. See
[setup verification](docs/setup-verification.md) for the actual setup results and
remaining interactive rehearsal steps.

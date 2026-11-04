# Setup verification

Date: 2026-11-03. Environment: macOS, Python 3.12.6.

Completed:

- Read the supplied interview guide and adapted general project conventions from
  existing repositories without importing product code or internal dependencies.
- Installed the project and development tools in the local `.venv`.
- `make check`: Ruff lint/format passed, 11 harness tests passed, source distribution
  and wheel built, doctor passed with application commands explicitly unconfigured.
- Three repository-local skills passed the Skill Creator structural validator.
- Confirmed VS Code is installed and `openai.chatgpt` is among its installed extensions.

The harness tests cover session isolation/non-overwrite, invalid paths, absent configuration,
failed or missing executables, timeout handling, candidate evidence and stopping on failure.
They do not test AI behavior or certify an application that has not been assigned.

Remaining manual rehearsal: sign-in, skill discovery, model/subagent availability,
actual interface switching with a running exercise, and screen sharing. The application
stack, commands, deployment target and acceptance examples intentionally await the task.

Clean-copy verification passed in a separate temporary checkout and fresh virtual
environment: `make setup`, `make check`, installed `interview new-session smoke-check`,
`interview status`, and rejection of an unconfigured application test with exit code 2.
This caught a missing editable-build dependency during setup; it was added to the
project and pinned tool list before the successful clean run. `pip check` also passed.
Workspace/task JSON and local Markdown links were checked.

Delivery: the initial baseline is committed to this repository. Consult Git history and
`git status --short --branch` for the current commit and remote tracking state. No live
interview session or application is bundled into the reusable baseline.

## Attached repository mode

Added an `attach` command with local session context, a two-folder workspace and
an explicit start/resume prompt. Its tests verify preservation of target files/Git
status, non-overwrite, invalid target rejection, prevention of running support-repo
checks as application checks, and switching back to standalone mode. The full suite
now contains 14 tests. No real interviewer repository has been attached or modified.

# Setup verification

Historical construction/verification record, not current operating instructions.
Current behavior is defined by root AGENTS.md and the relevant role/skill.
Results below describe the versions checked at the time.

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

## Paper UX workflow

On 2026-11-03, the configured local Paper MCP responded to guide/resource reads,
created the separate ai-interview project and blank design workspace, and returned
its three pages. No application screens or redlines have been approved. Added the
engineering-ui-design skill and explicit PM/UX/developer ownership, plus scoped
in-session maintenance of learned working agreements. Actual worker/IDE tool access
still needs verification in that worker/interface; a dependency declaration alone
does not establish that access.

## Submission and worktree workflow

Added independent reviewer instructions, engineering-review and engineering-test-deploy
skills, native Git worktree/integration guidance, review/submission templates and a
README walkthrough. Reference inspection used the installed esse-release source at
b4422849b889548116b87083e1b9d0bdd7431eb0 and esse-test-deploy source at
d3d3eea350bb7c9cf93f28c6d9d00af5cd426df8, plus the existing backend reviewer rubric.
Adapted principles only: independent current-candidate review, one execution owner,
dependency order, precise evidence and distinct source/delivery/acceptance milestones.
Internal release authority, cloud tooling, provider fallback rules and credentials
were not imported into the interview workflow.

Verification on 2026-11-03:

- Disposable Git rehearsal: committed baseline, two distinct worker branches/worktrees,
  dependency-order integration, successful combined behavior assertion, preservation
  of unrelated dirty work, and non-forced removal of integrated worker worktrees.
- `make check`: lint/format, 14 harness tests, package build and doctor passed.
- All six skills passed structural validation; local documentation links were checked.
- `codex review --help` verified the documented local scope flags with CLI 0.144.6.
  No live CLI/provider review or remote test deployment was performed in this exercise.

Independent CR receipt: review_submission_workflow, separate from the implementer,
reviewed the tracked changes from f127302d50647eb40e0fd0edf21b36c4b78073cc and the
new reviewer role, skills, worktree/submission guides and templates. Verdict: No findings.
The reviewed tracked-diff SHA-256 was
115a959ca47e778648e8a1661fc5f3038d3fe544844512aee8effc19d25cb6e1.
The reviewer inspected instructions and ran diff checks; it did not independently run
the Git rehearsal, provider review or deployment. This verification-note addition is
subsequent documentation, not part of that frozen review. No finding required repair.

## Holistic review before the first sample-question rehearsal

On 2026-11-03 a full repository pass and separate reviewer identified attached-mode
resume/command/worktree contradictions, an environment-sensitive command example,
stale counts and coordination overhead risks. See holistic-assessment.md for findings,
corrections and what remains unproven. Four regression tests increased the suite from
14 to 18; lint/format, package build, doctor and six skill validators pass. No real
interview sample, application deployment or live interface switch was performed here.

## Domain-neutral operating instructions

On 2026-11-03, renamed the six skills from interview-* to engineering-* and updated
their callers, generated attachment prompts and doctor checks. Existing CLI/package
and workspace filenames remain compatible. Agent roles, prompts and session templates
now use the supplied task's domain, deadline and acceptance criteria.

Historical Paper setup links (optional, not the default destination for new tasks):
[ai-interview project](https://app.paper.design/files/01M6JEANFRPD81YDVKY8JPPDRJ),
[AI Interview — Design Workspace](https://app.paper.design/file/01M6JEAS1E91BYY4E52V3V08Z5).
Select the working project/file per session and verify access before use.

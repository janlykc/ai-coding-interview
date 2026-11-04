# Working on a provided repository

Use two separate checkouts: the provided repository is the application; this repository
is a support toolkit. The harness is not a runtime library, submodule or dependency
of the application. No copying of role files into the supplied repo is required.

## Start

Clone the supplied URL using its access instructions. Clone this harness alongside it
if it is not already available. From the harness, after `make setup`:

```sh
.venv/bin/interview attach /absolute/path/to/provided-repo --session interview-01
```

This verifies the target is a separate Git/worktree root, creates local planning
records, captures its initial branch/HEAD, and prints two paths:

- `interview.code-workspace`: opens the implementation and support folders in VS Code.
- `start.md`: an explicit bootstrap/continuation prompt for the coding agent.

Open that workspace. Start Codex on the **implementation** folder (or select that
local project in the desktop app) and paste `start.md`. The prompt identifies the
target, harness and session by absolute path. Attachment does not edit the target,
checkout a branch, install packages, change its remote or execute its code.

## How agents operate

The target's applicable AGENTS.md, project documentation, manifests and test setup
remain authoritative for that codebase. The harness supplies your collaboration
workflow. The human remains PE/product owner; PM authors the spec; developers inspect
and implement; QA validates; the coordinator reviews and orchestrates checkpoints.

Every worker receives target root, harness role path, session path, checkpoint and
owned files. Code and test commands run in the target. Specs, plans, decisions and
validation summaries live in the support session. If the interviewer requires docs
in their repo, agree the destination and export the relevant deliverables there.

Use the target's dependency manager and environment. Do not install this harness's
pyproject dependencies into the target or replace its configuration. Discover its
baseline tests before changing code. In attached mode the harness `run` command
refuses application execution to prevent accidentally testing the support package;
use native target commands and record their exact working directory, code state and
outcome in validation.md. Harness `make check` still checks only the toolkit.

Application commits belong to the target's branch. Confirm its remote and push policy
in the session plan; never send the supplied code to the harness remote. A remote URL
existing in the provided clone is not by itself permission to push there.

## Continue in either interface

The generated start prompt works for both initial intake and continuation. Before a
switch, save the session handoff and stop workers; the next agent checks target Git
state, current checkpoint and remaining decisions. `interview status` from the harness
shows the attachment and target Git state. One controller writes a target at a time.

Attachment records and generated workspace paths are in ignored `.harness/sessions/`;
the active-session pointer is also ignored. They persist on this machine but do not
travel with a push of the harness. To move machines, deliberately transfer authorized
session records, rebind their absolute paths, and confirm the target checkout/revision.
Do not rely on an automatic chat or folder sync.

An attachment points to a local path, not a permanent repository identity. If the target
folder is replaced or its branch changes, compare its actual Git state with context.json
and the latest handoff before resuming. To use a different target, create a new attachment
with a new session name; existing sessions are never overwritten. `new-session` switches
back to standalone mode. No session is created until an actual target is supplied.

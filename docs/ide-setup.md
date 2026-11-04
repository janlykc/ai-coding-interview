# VS Code and Codex continuation

## Same checkout, two interfaces

Open `interview.code-workspace` in VS Code. Add/open the same absolute repository
path in the Codex desktop app as a local project. This chat can edit those files too
when given that path; it must explicitly read that repository's AGENTS.md first.
A separate Codex worktree is a different checkout: open its path in VS Code as well.
Keep docs, relevant code, diff and a terminal visible while narrating decisions.

Run `make setup` before selecting the repository virtual environment. The workspace
default is `.venv/bin/python` on macOS/Linux; on Windows select `.venv\Scripts\python.exe`
using Python: Select Interpreter. The debug configuration runs the harness doctor;
add application launch configurations once the actual entry point is known.

VS Code already has the Codex extension installed on the setup machine. Other machines
can install the workspace recommendation `openai.chatgpt` and sign in. Choose the
available reasoning level appropriate for coordination/review in the UI; no model ID
is pinned by this harness. Check tool availability before relying on subagents.

The IDE can provide open-file/selection context and display edits. Working from the
Codex app against the same files also updates what VS Code sees. This harness does
not automate the VS Code UI or install an IDE control server.

## Switch the active controller

1. Ask the current agent to use `engineering-handoff` to save context and stop workers.
2. Confirm the outgoing agent is idle; save open editor buffers.
3. Open the same checkout in the other interface. Fill the harness, session and
   implementation paths in `prompts/resume.md`; attached-mode session files are in
   the support harness, not the supplied repo.
4. Verify branch, HEAD, dirty files and next checkpoint, then name the new writer
   in the handoff. Resume only after resolving mismatched or unsaved state.

The active-writer entry is a coordination convention, not an enforced process lock.
Native conversation availability across app/IDE versions is not assumed or tested by
this repository. File-based continuation works even in a fresh chat. If skill discovery
fails, explicitly ask the agent to read `.agents/skills/<name>/SKILL.md`.

## If given an existing repository

Start with the [README workflow](../README.md#using-this-harness-with-a-provided-repository);
no command is required. The optional `attach` command
creates a two-folder workspace and explicit bootstrap prompt without editing the target.
Open a Codex chat on the implementation checkout, and paste the generated prompt so it
can explicitly read the support harness. Cross-repository instructions/skills are not
automatically inherited. If access to the support directory is unavailable, grant that
folder through the host's normal access controls or supply the relevant instructions
explicitly; do not silently proceed without the agreed context.

## Sources checked during setup, 2026-11-03

Codex reads root and applicable nested instructions; arbitrary sibling role files must
be explicitly provided. See [AGENTS.md discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
Repo-local skills live under `.agents/skills/` and can be invoked explicitly; see
[skills documentation](https://learn.chatgpt.com/docs/build-skills).
For opening and using Codex beside source and diffs, see the
[IDE extension documentation](https://learn.chatgpt.com/docs/codex/ide).

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

1. Ask the current agent to use `interview-handoff` to save context and stop workers.
2. Confirm the outgoing agent is idle; save open editor buffers.
3. Open the same checkout in the other interface. Use `prompts/resume.md`.
4. Verify branch, HEAD, dirty files and next checkpoint, then name the new writer
   in the handoff. Resume only after resolving mismatched or unsaved state.

The active-writer entry is a coordination convention, not an enforced process lock.
Native conversation availability across app/IDE versions is not assumed or tested by
this repository. File-based continuation works even in a fresh chat. If skill discovery
fails, explicitly ask the agent to read `.agents/skills/<name>/SKILL.md`.

## If given an existing repository

Preserve its instructions, manifests and Git history. Open it separately and inspect
before changing it. With task permission, copy `ai_team/`, relevant skills and session
templates into non-conflicting paths; merge the concise harness working agreement into
its existing AGENTS.md rather than replacing it. Resolve collisions deliberately.
Alternatively keep the harness as a reference folder and explicitly pass absolute role
and session paths. Skills in this harness are not automatically discovered from a different
Git root. Record the target checkout and command locations in the handoff; use the target's
native commands if the harness runner is not installed there.

## Sources checked during setup, 2026-11-03

Codex reads root and applicable nested instructions; arbitrary sibling role files must
be explicitly provided. See [AGENTS.md discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
Repo-local skills live under `.agents/skills/` and can be invoked explicitly; see
[skills documentation](https://learn.chatgpt.com/docs/build-skills).
For opening and using Codex beside source and diffs, see the
[IDE extension documentation](https://learn.chatgpt.com/docs/codex/ide).

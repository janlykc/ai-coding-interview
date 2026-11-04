---
name: engineering-ui-design
description: Design application UI in Paper MCP with spec writer and developer collaboration, agree redlines, and review the implemented interface against them.
---

Read the active session, `ai_team/ux/AGENTS.md`, and `docs/paper-design.md` from the
harness. In attached mode resolve harness guidance from `harness_root`, application
code from the assigned implementation worktree (default `target_root`), and planning
records from `session_root` in context.json. Verify worktree repository identity.

## Connect and establish ownership

Check that the UX worker can call the available Paper MCP tools. Server names vary;
this machine currently exposes `papaer`. Read its current `paper-mcp-instructions`
guide before other Paper tools. If absent, disclose the missing connection; the role
file and dependency declaration do not install a server or guarantee worker access.
Use the current host's tools to discover the connection; never invent an endpoint.

Resolve the session-selected project with list_resources. Reuse its recorded file
if it exists; otherwise create a distinctly named task file in the selected project.
If no destination is selected, agree one before mutating a canvas.
Create the project if absent and supported. Open the intended file, inspect basic
info and selection, and record file/page references in session `design.md`.
If tools only support the current canvas, have the user open/create the intended
design file and verify it before editing. Keep one UX writer per artboard.

## Specification–UX–developer design loop

These are contributions, not a required simultaneous roster. The spec writer may
be the lead or a delegated author; do not spawn a spec writer just for this loop. Use the existing spec
as spec writer input; request spec writer or developer involvement only for unresolved requirements,
feasibility or implementation work. Do not spawn extra workers merely to run this skill.

1. The spec writer supplies acceptance IDs, behavior, constraints and open decisions. Developer
   inspects existing components, styling conventions and data/API contracts. UX
   proposes the journey and a short design brief; do not invent requirements.
2. Follow Paper's current guide for typography checks, existing tokens, brief before
   visual mutations, incremental creation and screenshot review. Use explicit file/page
   IDs. Keep exploration separate from agreed redlines; do not mark a page approved
   merely because it is named "Agreed redlines".
3. Review with spec writer and developer before broad implementation. Human resolves material
   tradeoffs. The spec writer updates acceptance criteria; UX records agreed screens, states,
   interactions and revision in design.md; coordinator maps them to checkpoints.
   Bound iterations to the time available; do not require polished mockups for every state.
4. Supply exact structure/styles/assets through available Paper export/inspection tools
   such as get_jsx and get_computed_styles. For JSX export omit Paper node IDs. Adapt to
   the target stack rather than introducing a framework to match an export.
5. Developer implements; UX and QA inspect the real rendered application. Record
   differences against the selected design and acceptance IDs. Screenshots validate
   appearance; they do not prove functionality or replace exact design values.
   Refresh relevant evidence when code or agreed design changes.

Finish with Paper's finish_working_on_nodes. Report design readiness, implementation
readiness and human acceptance separately. On handoff include Paper links, latest
agreed revision, unresolved decisions and who owns outstanding canvas/code edits.

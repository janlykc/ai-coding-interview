# Paper design workspace

For UI work, Paper is the default design environment. PM, UX and developer work
through a short design loop before implementation; UX remains involved in review.

## Ready on this machine

On 2026-11-03 the configured `papaer` MCP server at `http://127.0.0.1:29979/mcp`
responded successfully. The following interview-only workspace was created:

- [ai-interview project](https://app.paper.design/files/01M6JEANFRPD81YDVKY8JPPDRJ)
- [AI Interview — Design Workspace](https://app.paper.design/file/01M6JEAS1E91BYY4E52V3V08Z5)
- Pages: Exploration, Agreed redlines, Implementation review.

The pages are empty staging areas, not an approved design. No task has been invented.
For a new exercise, create a separate file inside the project or clone the empty
workspace. Verify actual contents before reusing it; it may have changed since setup.
These account-specific links do not grant another user access.

Paper is already configured in this machine's Codex user settings. The UI skill declares
that dependency; it does not install Paper, start its desktop server, authenticate, or
force subagent inheritance. Keep Paper running and verify the tools in the actual UX
worker and whichever interface you use. On another machine, configure Paper through
its supported MCP setup and inspect the endpoint it provides rather than assuming this
local address works. No credentials belong in the repository.

## Minimal design record

The UX owner creates `design.md` in the active session only when UI work is relevant:

- Paper file/page links and selected artboards (machine IDs may be recorded for tools).
- Acceptance IDs, critical user journey and existing component/style constraints.
- Agreed states/interactions, relevant responsive and accessibility behavior.
- Human decision, design revision/checkpoint and unresolved questions.
- Exact exports/style references for implementation and observed review discrepancies.

PM owns requirements in spec.md; UX owns design.md and the canvas; coordinator owns
plan.md; developer owns code. Keep the records linked rather than copying the same
spec into each file. A Paper page title never constitutes human acceptance.

Before code handoff, PM checks behavior and developer checks feasibility. After code
handoff, UX/QA review the running interface. Use screenshots for visual review and
Paper inspection/export tools for implementation values. The live Paper guide controls
tool-specific details, so the harness does not carry a copied manual that can go stale.

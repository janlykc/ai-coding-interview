# Paper design workspace

For UI work, Paper is the default design environment. PM, UX and developer work
through a short design loop before implementation; UX remains involved in review.

## Select and verify the workspace

Use the project/file recorded in the active session. If none is selected, agree the
destination before creating or editing designs. Verify actual contents and access;
do not assume another task's canvas or a parent agent's connection is appropriate.

The UI skill declares a Paper dependency; it does not install a server, authenticate
or guarantee worker access. Discover the available MCP connection and read its live
guide. Verify tools in the actual UX worker and active interface. No credentials
belong in the repository. Historical local setup is recorded in setup-verification.md.

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

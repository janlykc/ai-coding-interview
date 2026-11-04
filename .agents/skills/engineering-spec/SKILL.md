---
name: engineering-spec
description: Turn a development task into an agreed concise specification and checkpoint implementation plan before coding, or revise them when requirements change.
---

Read root `AGENTS.md` for shared policy and session/path resolution. Use the
README's matching setup only if session records are needed and none exist.

1. Inspect the task and relevant code. Confirm time available and any task-specific
   restrictions. Do not invent a task if none is supplied.
2. Keep a small spec with the lead or delegate synthesis/maintenance using
   `ai_team/spec_author/AGENTS.md` when it adds value. Combine the scribe responsibility.
   Record one spec writer; load the role only when delegating, not at startup. Ask a developer using
   `ai_team/developer/AGENTS.md` only when investigation or feasibility input is
   needed; do not spawn one solely because design has begun.
3. Collaborate with the human PE/product owner. Capture behavior, exclusions,
   acceptance examples, component contracts, edge cases and uncertain decisions in
   `spec.md`. Recommend defaults and surface consequential tradeoffs.
4. The engineering lead converts design into a proposed implementation plan, testing
   its completeness against existing code: missing behavior, unclear contracts,
   dependencies, feasibility, integration points and failure paths. Surface consequential
   gaps to the human; revise the spec with agreed answers before dispatching dependent
   work. This is an iterative design–plan loop, not a one-way document handoff.
   Write small ordered checkpoints in `plan.md`: acceptance IDs, owners/files,
   dependencies, integration points, test evidence and exit criteria.
   Record local commit policy and any authorized remote/branch. Discuss whether
   local running suffices or deployment is actually part of acceptance.
5. Confirm consequential unresolved choices when needed. An instruction to implement,
   prototype or proceed is direction to act; do not demand separate formal sign-off.
   If the human prefers to explore in code, capture only useful assumptions and refine
   the spec/plan from results. Record actual decisions without inventing agreement.

Size design effort to uncertainty, risk and the actual deadline; do not assume a fixed timebox.
Avoid spawning the whole team or requiring exhaustive documentation. On later changes,
revise only affected requirements/checkpoints and preserve decisions that explain why.

For material UI design, use engineering-ui-design and reference the agreed design.
For parallel sections, use docs/worktrees.md after identifying independent boundaries.

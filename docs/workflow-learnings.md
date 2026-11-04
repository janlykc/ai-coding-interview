# Working agreements learned from use

These are scoped to this engineering harness. Source: the user's development retrospective
and corrections in this conversation, including the explicit Paper workflow on 2026-11-03.
They are qualitative working preferences, not measured claims of superiority.

| Observed preference or correction | Harness behavior |
| --- | --- |
| Human supplies requirements and questions, then reviews redlines | PM/scribe authors the spec; human keeps product and PE decisions |
| PM, Paper UX and developers iterate together | UI design uses Paper, with feasibility input before implementation and UX review after |
| Roles are a library, not a startup team (2026-11-03) | Start with the lead only; load the current skill and delegate concrete work on demand; phase changes do not spawn a roster |
| Same lead retains useful context | Design lead becomes checkpoint coordinator |
| Autonomous experiments are useful; decision-critical findings need visibility | Bounded execution with concise decision/evidence updates |
| Fast delivery still needs confidence in lower layers | Inspect component seams and meaningful evidence; QA complements human acceptance |
| README should explain how to use another repository | Existing-repo mode is readable and usable without a custom command |
| Skills should improve from actual usage | Promote a demonstrated lesson into the relevant role/skill during the session |

## How agents maintain these agreements

When the human corrects a workflow or a repeated outcome demonstrates a useful change,
apply the correction to current behavior immediately. Record the lesson briefly;
update the narrowest harness role/skill at a natural checkpoint or after the task unless a blocking fix is needed. Do not derail implementation to maintain
the harness or merely promise to remember. Report the update and validate affected
links/skill metadata or tooling.
Preserve user edits, existing authorization and task scope.

Use relevant conversations and session retrospectives already available to the task.
If further history is needed, inspect targeted chats rather than sweeping all local
conversations or copying private transcripts into this portable repository. Separate
explicit preferences from hypotheses; try uncertain improvements in a bounded trial first.
Remove superseded advice instead of accumulating contradictory rules. Do not turn a
one-off task constraint into a universal rule, add new bureaucracy, or change global
machine settings as a side effect. This is an in-session practice, not a background
monitor or a claim that every conversation is automatically observed.

Submission/worktree refinement (2026-11-03): preserve the useful release habits—one
owner per mutation, independent review of the current candidate, dependency-order
integration, and QA of the actual running code—using native Git and lightweight
session records. Do not transplant company-specific admission or cloud infrastructure.

## Domain-neutral engineering review — 2026-11-03

User correction: the operating team solves a real problem, with domain and deadline
supplied by that task. Interview preparation belongs in human-facing notes. Roles
remain an on-demand library; skill names now use engineering-*.

Sources inspected in the local Esse workspace (inspiration, not runtime dependencies):

| Source | Portable lesson applied |
| --- | --- |
| esse-ai/AGENTS.md and ai_team/engineering/planning_agent/agents.md | Inspect existing capabilities; keep deterministic logic first, external adapters explicit, and model cost bounded |
| esse-core/AGENTS.md and docs/agents/shared/contract_reviewer.md | Trace producers/consumers, missing/null/empty semantics, reconstructed models and historical data |
| esse-core/docs/agents/shared/python_testing.md | Test at the lowest useful layer with fake external adapters; preserve meaningful regression/seam coverage |
| esse-web-app/AGENTS.md and esse-core/docs/agents/shared/frontend_reviewer.md | Respect existing UI conventions; inspect state invalidation, optimistic rollback and service contracts |
| ai_team/reviewer/backend/AGENTS.md | Independent, findings-first review of concrete behavior; no invented stylistic blockers |
| esse-deployment/agents/ci-release-shared/AGENTS.md, agents/test-deployment-operator/AGENTS.md and installed esse-release/SKILL.md | One executor, candidate-bound evidence, bounded recovery, verify destination rather than submission alone |

The resulting instructions are self-contained. They assume no household domain,
company repository layout, cloud provider, credential set or special release authority.

## Lead-owned planning and specialist kitchen — 2026-11-03

The human sets direction, asks design questions and resolves consequential tradeoffs.
The engineering lead owns converting design into an executable plan: identify missing
behavior/contracts, check feasibility, order dependencies, define integration and
validation, and bring unresolved design decisions back to the human. Planning can
expose gaps and reopen design; it is not merely scheduling an already-complete spec.

Use specialists like sous chefs with bounded assignments. Spec authorship is optional
delegation, not a management layer: the lead may capture a small spec directly.
The former program_manager role is now spec_author; it records agreed intent while
the lead retains technical decomposition and phase recommendations. Keep one spec
writer, on-demand context, independent evaluation and autonomous agreed execution.

Evaluate this working model through real tasks and bounded trials. Keep what reduces
rework and improves clarity; revise what adds coordination without useful output.

## Advisory workflow — 2026-11-03

User correction: the process may remind, but must not become something the human
has to fight. Roles, phase order and documentation are adaptable defaults. Follow
requests to prototype, skip/combine phases, defer paperwork/review or work directly;
give a concise reminder for a meaningful tradeoff without repeated approval gates.
Stay honest about missing evidence and respect actual permissions and unrelated work.

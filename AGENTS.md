# Engineering working agreement

Solve the supplied problem in the selected checkout. Derive domain, stack and constraints
from the task and existing code; unrelated workspace products are outside scope.

## Advisory defaults
The human is principal engineer, product owner and acceptance authority. Follow their
direction to skip/reorder phases, prototype, defer records/review or change roles.
Offer one concise reminder for a meaningful tradeoff, then proceed within authorized
scope; missing templates or formal sign-off are not blockers. Preserve actual tool
permissions, unrelated work and truthful reporting of what was tested or reviewed.

## Pair with me
When the human requests close pairing, keep the same workflow but shorten the feedback
loop. Discuss the approach and consequential choices together, explain the next small
change, and make its code and verification easy to inspect. Suggest test cases and
invite the human to interpret results with you; do not turn this into a quiz or require
approval for every edit. Use existing direction to continue routine work.

Delegate only when it helps without losing shared understanding; keep assignments
small enough to follow. Match explanation depth to the human and avoid running several
checkpoints ahead. Requests such as “walk me through this” or “take this checkpoint and
run with it” adjust involvement naturally, without special commands or a separate mode.
Preserve the current preference and its scope in an existing handoff when switching
interfaces; a temporary autonomous checkpoint does not silently end ongoing pairing.

## Context and ownership
Start with the lead alone: read `ai_team/coordinator/AGENTS.md`. Load other roles and
skills only for concrete work; see `ai_team/README.md` for assignments. Delegate
implementation by default; honor direct-execution requests or use sequential roles
when delegation is unavailable. Never label self-review independent.

For setup, use the matching README mode. An explicit session path wins over the
harness's `docs/ACTIVE_SESSION`. Read available spec, current checkpoint and handoff;
verify actual repository, branch, dirty state and active writers. Harness maintenance
needs no task session. Do not invent work to fill templates.

In attached mode, read the target's applicable instructions first. Resolve guidance
from `harness_root`, records from `session_root`, and application operations from the
assigned worktree (default `target_root`). Verify that worktree shares the target's
resolved Git common directory. Pass absolute paths to workers; do not rewrite shared
context per worker or copy the harness into the target. Use target-native commands
and Git policy. See `docs/existing-repository.md` for optional tooling and relocation.

## Select the needed workflow
- `engineering-spec`: design and lead-owned planning, including gaps and dependencies.
- `engineering-deliver`: implementation checkpoints and validation.
- `engineering-ui-design`: Paper design when useful, with access checked in the UX worker.
- `engineering-review`: independent candidate review.
- `engineering-test-deploy`: run/smoke/QA of the actual candidate.
- `engineering-handoff`: transfer context and writer ownership between interfaces.

Use `docs/worktrees.md` when independent work justifies parallel checkouts, and
`docs/submission.md` for Git integration/publication. Skills are procedures, not
mandatory phases. Record source/review/test/deployment/acceptance separately; changing
code or dependencies invalidates affected evidence. Harness checks do not test the app.

Apply corrections immediately. At a natural checkpoint, replace superseded guidance
in its owning role/skill rather than adding another copy. Keep only useful evidence
and decisions; `docs/workflow-learnings.md` records why the defaults evolved.

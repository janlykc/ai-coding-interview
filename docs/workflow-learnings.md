# Why these defaults exist

Qualitative lessons from the user's Esse retrospective and corrections on 2026-11-03.
These explain the current instructions; they are not a second policy manual or measured
claims that the workflow is faster.

| Learning | Where it belongs |
| --- | --- |
| Direct human/lead discussion; optional spec author, not program management | Coordinator and spec-author roles |
| Planning exposes design gaps as well as ordering work | engineering-spec |
| Specialists are on demand; process should remind, not restrict | Root AGENTS.md |
| Paper design needs feasibility input and running-result review | engineering-ui-design |
| Exact candidate and component seams matter more than test counts | Reviewer/QA roles and review/test-deploy skills |
| Another repository must work without installing a custom CLI | README provided-repository setup |
| Repeated rules drift and waste context | Shared policy in root, judgment in roles, procedures in skills |
| Empty records create ceremony | New sessions create spec/plan/handoff; other templates are on demand |

The DRY pass merged the separate scribe into spec_author and retained historical
construction records as provenance only. Update the owning instruction at a natural
checkpoint when evidence or human direction changes it; replace superseded wording.
Use targeted available context, not broad private-chat collection or background monitoring.
Judge future changes by useful output, rework and coordination cost.

## Esse source provenance

Inspected local sources are inspiration, not runtime dependencies:

| Source | Portable lesson applied |
| --- | --- |
| esse-ai/AGENTS.md and ai_team/engineering/planning_agent/agents.md | Inspect existing capabilities; keep deterministic logic first, external adapters explicit, and model cost bounded |
| esse-core/AGENTS.md and docs/agents/shared/contract_reviewer.md | Trace producers/consumers, missing/null/empty semantics, reconstructed models and historical data |
| esse-core/docs/agents/shared/python_testing.md | Test at the lowest useful layer with fake external adapters; preserve meaningful regression/seam coverage |
| esse-web-app/AGENTS.md and esse-core/docs/agents/shared/frontend_reviewer.md | Respect existing UI conventions; inspect state invalidation, optimistic rollback and service contracts |
| ai_team/reviewer/backend/AGENTS.md | Independent, findings-first review of concrete behavior; no invented stylistic blockers |
| esse-deployment/agents/ci-release-shared/AGENTS.md, agents/test-deployment-operator/AGENTS.md and installed esse-release/SKILL.md | One executor, candidate-bound evidence, bounded recovery, verify destination rather than submission alone |


The portable team assumes no household domain, company layout, cloud provider,
credentials or special release authority.

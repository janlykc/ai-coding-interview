# Specialist library

Root `AGENTS.md` owns shared policy. Roles add specialist judgment; skills own
procedures. Neither a role folder nor a phase transition launches an agent.

| Role | Use when | Responsibility |
| --- | --- | --- |
| [Lead/coordinator](coordinator/AGENTS.md) | Main agent | Design-to-plan, gap discovery, sequencing and review |
| [Spec author / scribe](spec_author/AGENTS.md) | Synthesis or records need delegation | Agreed intent and decisions; the lead can do this directly |
| [Developer](developer/AGENTS.md) | Investigation or implementation | Existing code, bounded changes and focused tests |
| [Reviewer](reviewer/AGENTS.md) | Candidate needs independent CR | Concrete correctness/compatibility findings |
| [QA](qa/AGENTS.md) | Behavior needs independent validation | Acceptance checks and evidence |
| [UX](ux/AGENTS.md) | Material UI design | Paper redlines and rendered-result review |
| [Delivery](delivery/AGENTS.md) | Git or environment execution | Commit, integration, run and authorized deployment |

Use stronger reasoning for ambiguity/review and lighter workers for bounded execution
where supported and within budget. Respect actual slot limits; retire idle workers
with a handoff. One non-implementer may handle QA and CR in separate passes; an existing
developer may execute delivery. These responsibilities do not require separate processes.

## Assignment contract

Pass the relevant role path, harness/session/implementation paths, bounded task,
necessary context, owned files, dependencies, expected evidence and stopping condition.
Do not copy the entire conversation or library. Workers return changed paths, behavior,
actual checks, limitations and next action. Stop stale assignments when scope changes.

Keep one writer per file. The lead owns plan/handoff, the assigned spec writer owns
requirements/decisions, and QA owns validation when delegated. Others propose changes
to those owners. Templates are optional aids; create records when they become useful.

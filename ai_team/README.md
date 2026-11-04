# Team

The user is principal engineer, product owner and acceptance authority.
Role files are prompts to explicitly read/pass to a worker; naming a folder does
not register or launch a native agent. Keep the worker's working directory at the
selected repository root and pass the role path in its assignment.

| Role | Read when | Ownership |
| --- | --- | --- |
| [Coordinator](coordinator/AGENTS.md) | Main agent throughout | Technical direction, review, plan state, checkpoint decisions |
| [Specification author](spec_author/AGENTS.md) | Delegated synthesis or spec maintenance | Records agreed intent and acceptance examples; no phase authority |
| [Scribe](scribe/AGENTS.md) | Decisions need recording | Concise decision log; may be combined with spec author |
| [Developer](developer/AGENTS.md) | Investigation or implementation | Python/frontend and existing code; component-specific assignment |
| [Reviewer](reviewer/AGENTS.md) | Code ready for review | Independent CR and findings, separate from implementation |
| [QA](qa/AGENTS.md) | Verification | Independent behavior checks and evidence |
| [UX](ux/AGENTS.md) | UI is material | Paper design/redlines and visual/accessibility review |
| [Delivery](delivery/AGENTS.md) | Commit, push or environment work | Git execution, local run, optional deployment |

Start with the lead only. This is a library, not a startup roster: do not load every
role into context. Delegate spec authorship only when useful; bring in a developer for concrete
investigation or implementation, and QA/CR when a candidate needs evaluation.
Create backend/frontend workers only when the boundaries support independent work.
The coordinator should use the strongest reasoning setting available within the
user's budget. Smaller implementation tasks may use faster workers where supported;
these are preferences, not hard-coded model IDs or promises about host controls.

## On-demand activation and context budget

Roles need not be simultaneous or separate processes. Check the host's actual slot
limit; with four total slots, keep the coordinator plus at most three active workers.

- Design: load engineering-spec. The lead can capture a small spec; delegate to
  spec author/scribe when synthesis or ongoing maintenance warrants it. Ask a developer only when code investigation or feasibility needs it.
  Load engineering-ui-design and involve UX when meaningful UI design is needed.
- Build: load engineering-deliver and delegate the next implementation checkpoint.
  Add more developers only for useful independent work.
- Verify: load engineering-review or engineering-test-deploy when a candidate is ready.
  An independent non-implementer may handle QA and CR in separate passes.
- Deliver: consult submission guidance when a Git checkpoint or release is due.
  Reuse an available developer for delivery execution; this is not independent approval.

These are activation triggers, not teams to spawn at phase entry. Before delegation,
identify the needed output and pass only the relevant role, skill sections and task
context. Skill availability does not require loading every skill body.

Use supported stop/follow-up mechanisms and preserve handoffs before retiring a worker.
Do not keep completed agents occupying slots solely to match the organization chart.
Load root guidance, the assigned role and the current checkpoint; consult other skills
only as needed. In a short task, spec.md, plan.md and handoff.md are the initial working
records. Add validation/review/design records when those phases begin; unused templates
are not forms that must be filled. Do not transcribe dialogue into multiple files.

## Assignment contract

Pass: role path; session path; checkpoint and acceptance IDs; relevant code/context;
owned files; input/output contract; forbidden overlap; validation expected; stop condition.
Workers return: changed files, behavior, evidence, open risks and recommended next action.
Do not copy the whole chat or every role/skill into every worker. Stop stale assignments
when scope changes. Name one spec writer (lead or delegated spec author); coordinator
owns plan and handoff writes;
QA owns validation writes. Others propose edits to those owners.

If the runtime cannot spawn agents, say so. Ask the human to allow sequential role
passes, or have them open the required worker manually. Do not claim independence
for a review performed by the implementation agent itself.

For substantial UI design, spec author, Paper UX and developer collaborate as needed,
without requiring three simultaneous workers. See
[Paper setup](../docs/paper-design.md) and [workflow learnings](../docs/workflow-learnings.md).

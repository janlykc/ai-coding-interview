# Team

The user is principal engineer, product owner and acceptance authority.
Role files are prompts to explicitly read/pass to a worker; naming a folder does
not register or launch a native agent. Keep the worker's working directory at the
selected repository root and pass the role path in its assignment.

| Role | Read when | Ownership |
| --- | --- | --- |
| [Coordinator](coordinator/AGENTS.md) | Main agent throughout | Technical direction, review, plan state, checkpoint decisions |
| [Program manager](program_manager/AGENTS.md) | Design or scope changes | Spec and acceptance criteria |
| [Scribe](scribe/AGENTS.md) | Decisions need recording | Concise decision log; may be combined with PM |
| [Developer](developer/AGENTS.md) | Investigation or implementation | Python/frontend and existing code; component-specific assignment |
| [Reviewer](reviewer/AGENTS.md) | Code ready for review | Independent CR and findings, separate from implementation |
| [QA](qa/AGENTS.md) | Verification | Independent behavior checks and evidence |
| [UX](ux/AGENTS.md) | UI is material | Paper design/redlines and visual/accessibility review |
| [Delivery](delivery/AGENTS.md) | Commit, push or environment work | Git execution, local run, optional deployment |

Start with coordinator, PM/scribe and one developer; add QA at a useful checkpoint.
Create backend/frontend workers only when the boundaries support independent work.
The coordinator should use the strongest reasoning setting available within the
user's budget. Smaller implementation tasks may use faster workers where supported;
these are preferences, not hard-coded model IDs or promises about host controls.

## Phase schedule and context budget

Roles need not be simultaneous or separate processes. Check the host's actual slot
limit; with four total slots, keep the coordinator plus at most three active workers.

- Design: coordinator + PM/scribe + developer; add UX for a UI task.
- Build: coordinator + the needed developers; PM/UX remain available for questions
  but need not occupy running slots after the design handoff.
- Verify: stop/release idle workers and bring in an independent QA/CR worker. The same
  non-implementer may perform those two responsibilities in distinct passes.
- Deliver: reuse an available implementation worker as delivery operator under the
  coordinator's decision. This is execution, not independent approval.

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
when scope changes. PM owns spec writes; coordinator owns plan and handoff writes;
QA owns validation writes. Others propose edits to those owners.

If the runtime cannot spawn agents, say so. Ask the human to allow sequential role
passes, or have them open the required worker manually. Do not claim independence
for a review performed by the implementation agent itself.

For UI tasks, PM + Paper UX + developer is the default design group. See
[Paper setup](../docs/paper-design.md) and [workflow learnings](../docs/workflow-learnings.md).

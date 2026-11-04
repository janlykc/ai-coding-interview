# Solving a development problem

## Design and agreement

Begin with the lead only. Load phase skills and role instructions on demand, and
delegate only concrete work. The roles below describe ownership, not a starting
roster; design, implementation, testing and release do not each require a new team.

The human owns product direction and principal engineering judgment. The lead or delegated spec writer
captures agreed intent while developers explain existing code and feasible options.
A high-level problem may need several components; choose the smallest useful set
and document inputs/outputs, failure behavior and dependencies before parallel work.
An algorithm or debugging task may need only one function and a few examples.

Allocate effort to uncertainty and risk within the actual deadline. Keep design short
when behavior is clear; spend more when contracts or decisions are unresolved.
Communicate decisions and evidence to the stakeholder.

The lead converts design into a proposed implementation plan and checks for gaps:
behavior, contracts, feasibility, dependency order, integration and verification.
Resolve consequential gaps with the human, update the design, and revise the plan.
The spec author records agreed answers; the lead owns decomposition and sequencing.

Agree the spec and first checkpoint, then let the coordinator orchestrate within scope.
The same lead keeps context across design and delivery. The assigned spec writer (lead or delegated author) keeps the spec current;
coordinator keeps execution current. Use a separate scribe only when it helps.

## Checkpoints

Prefer a runnable vertical slice before parallel component expansion. Each checkpoint
names acceptance IDs, files/owner, dependencies, verification and a concrete exit.
Status: planned → in_progress → in_review → accepted, or blocked/rework.
Accepted means the specified exit is supported by evidence, with limitations visible.
A commit can preserve an intentionally partial slice; it does not imply feature completion.

Developers execute; coordinator reads diffs, interfaces/callers and evidence. QA
independently challenges the result. Escalate material requirement changes to the human.
Use focused updates, not a continuous transcript of routine experiments.

## Testing, validation and deployment

| Layer | Purpose | Typical evidence |
| --- | --- | --- |
| Baseline | Separate existing failures from new ones | Exact command, result, code state |
| Unit/behavior | Verify algorithm and boundary behavior | Focused tests tied to acceptance IDs |
| Contract/integration | Verify component seams | Real request/response or adapter test |
| Local end-to-end | Verify the critical user journey | Running service/CLI/browser walkthrough |
| UI | Verify interaction, states and accessibility | Browser/manual actions and observations |
| Review | Evaluate correctness and maintainability | Diff/caller review, concrete findings |
| Deployment, if required | Verify the serving candidate | Revision, URL, smoke and rollback |

Choose layers appropriate to the task. Tests should reveal incorrect behavior, not mirror
the implementation. For a bug, preserve the reproducer as a regression check where useful.
Model evaluations need a stable sample and failure analysis; use precision/recall/F1 only
when the task warrants them. Do not optimize an aggregate metric at the expense of a
critical acceptance case. A higher-reasoning QA agent supplements evidence, not human
product judgment or actual execution.

Capture code identity before testing and note changes during verification. If the candidate
changes, rerun affected checks. Build success, test success, review acceptance, human
acceptance, push success and deployment success are distinct claims.

Default to local execution. Agree any external deployment target and authorization
when the task is known. Avoid building a CI platform merely to demonstrate a small feature.
If CI is required, use the same documented commands locally and in CI and inspect results.

## Git and improvement

The coordinator decides meaningful commit boundaries after review. Delivery stages
explicit paths and records the commit. The plan records whether pushes are authorized
and to which remote/branch. Missing remote information does not block local development.

After a meaningful delivery or retrospective, write a short retrospective: what helped, what wasted time, what
remained hard to explain, and one adjustment to try next. Track time to first working
slice, rework after QA, waiting/coordination time, and optional token usage if the tool
actually reports it. Improve the harness based on observations rather than adding a rule
for every hypothetical failure. Keep task solutions separate from reusable improvements.

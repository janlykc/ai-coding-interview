# Verification choices

Planning and execution procedures live in the engineering-spec and engineering-deliver
skills. Use this reference only when choosing validation depth.

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

## Learn from the result

After a meaningful delivery, use the retrospective template if useful: what helped,
what wasted time, what remained hard to explain, and one adjustment to try. Observe
time to first working slice, rework and coordination cost; report token counts only
if the tools expose them. Replace ineffective guidance rather than accumulating rules.

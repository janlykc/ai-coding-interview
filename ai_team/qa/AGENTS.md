# QA and validation

Derive checks from the agreed spec and its acceptance examples. Inspect what changed,
then independently exercise the behavior; do not merely repeat the developer's summary.
Use available test tools and local runtime. Never claim to have run a tool you lack.

Own `validation.md`. Record acceptance ID, code state (commit or dirty diff identity),
command/action, expected and observed behavior, outcome and evidence location. Separate
pass, fail, blocked and not-run. Count skipped tests as skipped. Keep pre-existing failures
visible. If code changes after validation, identify and rerun affected checks.

Choose checks by risk: unit behavior and boundaries, component/API contracts, then a
critical end-to-end path where feasible. For UI, use actual browser/manual interaction,
keyboard and representative viewport checks; report screenshots only if captured.
For model/data tasks, use a fixed labeled sample, baseline and error analysis; include
precision/recall/F1 only when appropriate. Aggregate improvements do not excuse lost
critical cases. Report concrete reproduction steps and severity. The human retains
product acceptance; coordinator decides checkpoint readiness from evidence.

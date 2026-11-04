---
name: engineering-debug
description: Investigate failing tests, incorrect behavior or performance regressions in existing code; work from a reproducer and hypothesis to a focused fix and verification. Supports code-comment and pseudocode discussion before implementation.
---

Read root AGENTS.md for scope, pairing preferences and editor-discussion behavior.
Use the target's native tools. A bug does not require a full specification, new role
or session ceremony; use existing code, tests and the human's current direction.

1. Establish expected versus observed behavior. Read the relevant code and recent
   changes, preserve the human's edits, and reproduce the failure at the smallest useful
   boundary. Separate pre-existing failures from this issue. If reproduction is blocked,
   report the missing evidence rather than claiming a diagnosis.
2. Trace the actual data/state transition. Treat comments, pseudocode and AI explanations
   as hypotheses to check, not proof of runtime behavior. State the leading explanation
   and a discriminating check; use a counterexample when competing explanations matter.
   For performance, measure the relevant workload and identify repeated work before
   changing algorithms.
3. In close pairing, discuss the causal path and useful edge cases beside the code.
   If the human is still sketching, stay in discussion; propose a concrete next edit
   without replacing their sketch. If they asked to fix or implement, proceed within
   that direction without another sign-off.
4. Make the smallest coherent fix that addresses the cause and preserves contracts.
   Do not delete failing tests, weaken assertions or introduce unrelated rewrites to
   get green. Update tests only when their expected behavior is demonstrably wrong
   or the requirement changed, explaining why.
5. Rerun the reproducer and relevant nearby/contract checks. Preserve a useful regression
   case where appropriate. Explain cause, change, actual evidence and remaining limits;
   a passing example alone does not establish correctness or performance.

If a hypothesis fails, use the result to revise it; do not repeat the same fix blindly.
Stop and surface the specific unresolved choice or evidence gap when further retries
have no basis. Use engineering-spec only if a genuine design/requirement gap needs it,
and engineering-review/test-deploy when their work is useful. Keep the human able to
follow the reasoning; do not turn debugging into a scripted quiz.

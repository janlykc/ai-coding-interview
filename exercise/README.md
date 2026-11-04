# Reconstructed build-system trial

This is an original synthetic fixture inspired by the three phase titles and the
user's written NeetCode report. It is not NeetCode's starter code, tests or solution.

Task: fix dependency ordering, implement a deterministic event-driven build scheduler,
then check large DAG behavior. Each task has a unique string name, positive integer
duration and zero or more existing dependencies. The graph may be empty. Reject
cycles and nonpositive worker counts with ValueError. Inputs are already validated
for task IDs, duration and dependency existence. Do not mutate the input graph.

schedule(graph, workers) returns {name: (start, finish)}. Every task appears once,
runs without interruption for its duration, starts no earlier than its prerequisites
finish, and total concurrent tasks never exceeds workers. Start ready work whenever
capacity is free; when several tasks are ready, choose lexicographically by name.
Process all completions at the same timestamp before choosing new work.
This asks for a valid deterministic schedule, not a globally optimal makespan.

Run: python3 -m unittest discover -s exercise -v

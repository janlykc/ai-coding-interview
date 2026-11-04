import sys, random, time
from pathlib import Path
sys.path.insert(0, str(Path(sys.argv[1]) / "exercise"))
from graph import Graph, Task
from scheduler import schedule

def reference(tasks, workers):
    result, completed, running = {}, set(), {}
    t = 0
    while len(completed) < len(tasks):
        for name in list(running):
            if running[name] == t:
                completed.add(name)
                del running[name]
        ready = sorted(name for name, task in tasks.items()
                       if name not in result and set(task.deps) <= completed)
        for name in ready[:workers - len(running)]:
            finish = t + tasks[name].duration
            result[name] = (t, finish)
            running[name] = finish
        if not running and len(completed) != len(tasks):
            raise ValueError("cycle")
        t += 1
    return result

rng = random.Random(20261104)
for case in range(300):
    names = [f"t{i:02d}" for i in range(rng.randrange(0, 13))]
    rng.shuffle(names)
    tasks = {name: Task(rng.randrange(1, 7), tuple(p for p in names[:i]
                                                if rng.random() < .25))
             for i, name in enumerate(names)}
    workers = rng.randrange(1, 6)
    graph = Graph(tasks)
    expected = reference(tasks, workers)
    actual = schedule(graph, workers)
    assert actual == expected, (case, tasks, workers, actual, expected)
    assert graph.tasks == tasks
    assert schedule(graph, workers) == actual
print("300 seeded random DAGs match independent time-step reference; repeated calls preserve input.")
for size in (1000, 10000):
    names = [f"n{i:05d}" for i in range(size)]
    tasks = {name: Task(1, (names[i-1],) if i else ())
             for i, name in enumerate(names)}
    start = time.perf_counter()
    result = schedule(Graph(tasks), 8)
    assert result[names[-1]] == (size-1, size)
    print(f"Chain {size}: correct, {time.perf_counter()-start:.4f}s (single local observation).")
tasks = {f"w{i:05d}": Task(1) for i in range(10000)}
result = schedule(Graph(tasks), 8)
assert max(end for start, end in result.values()) == 1250
print("10,000-task independent set: valid lexical batches with 8 workers.")

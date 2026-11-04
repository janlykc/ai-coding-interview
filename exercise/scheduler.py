from heapq import heapify, heappop, heappush


def schedule(graph, workers):
    if workers <= 0:
        raise ValueError("workers must be positive")

    dependents, remaining = graph.adjacency()
    ready = [name for name, count in remaining.items() if count == 0]
    heapify(ready)
    running = []
    result = {}
    now = 0

    while ready or running:
        while ready and len(running) < workers:
            name = heappop(ready)
            finish = now + graph.tasks[name].duration
            result[name] = (now, finish)
            heappush(running, (finish, name))

        now = running[0][0]
        # Completion, not dispatch, releases dependents. Batch ties before
        # choosing new work so lexical priority includes every newly ready task.
        while running and running[0][0] == now:
            _, name = heappop(running)
            for child in dependents[name]:
                remaining[child] -= 1
                if remaining[child] == 0:
                    heappush(ready, child)

    if len(result) != len(graph.tasks):
        raise ValueError("dependency cycle")
    return result

# Existing unrelated note: future caller will format timestamps; keep scheduling numeric.

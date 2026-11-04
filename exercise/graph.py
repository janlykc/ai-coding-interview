from collections import deque
from dataclasses import dataclass

@dataclass(frozen=True)
class Task:
    duration: int
    deps: tuple[str, ...] = ()

class Graph:
    def __init__(self, tasks: dict[str, Task]):
        self.tasks = dict(tasks)

    def adjacency(self):
        dependents = {name: [] for name in self.tasks}
        indegree = {name: 0 for name in self.tasks}
        for name, task in self.tasks.items():
            for dependency in task.deps:
                # A prerequisite points to its consumers; count each consumer's prerequisites.
                dependents[dependency].append(name)
                indegree[name] += 1
        return dependents, indegree

    def topological(self):
        dependents, indegree = self.adjacency()
        ready = deque(sorted(name for name, count in indegree.items() if count == 0))
        order = []
        while ready:
            name = ready.popleft()
            order.append(name)
            for child in dependents[name]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    ready.append(child)
        if len(order) != len(self.tasks):
            raise ValueError("dependency cycle")
        return order

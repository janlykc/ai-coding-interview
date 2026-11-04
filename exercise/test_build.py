import unittest
from graph import Graph, Task
from scheduler import schedule

class GraphTests(unittest.TestCase):
    def test_dependency_precedes_consumer(self):
        self.assertEqual(Graph({"compile": Task(2, ("fetch",)), "fetch": Task(3)}).topological(),
                         ["fetch", "compile"])
    def test_cycle(self):
        with self.assertRaises(ValueError):
            Graph({"a": Task(1, ("b",)), "b": Task(1, ("a",))}).topological()
    def test_empty(self):
        self.assertEqual(Graph({}).topological(), [])

class ScheduleTests(unittest.TestCase):
    def test_chain(self):
        self.assertEqual(schedule(Graph({"b": Task(2, ("a",)), "a": Task(3)}), 2),
                         {"a": (0, 3), "b": (3, 5)})
    def test_empty(self):
        self.assertEqual(schedule(Graph({}), 2), {})
    def test_workers(self):
        for workers in (0, -1):
            with self.subTest(workers=workers), self.assertRaises(ValueError):
                schedule(Graph({}), workers)
    def test_cycle(self):
        with self.assertRaises(ValueError):
            schedule(Graph({"a": Task(1, ("a",))}), 1)
    def test_completion_not_dispatch(self):
        tasks = {"a": Task(10), "b": Task(1), "c": Task(1, ("a", "b"))}
        self.assertEqual(schedule(Graph(tasks), 2)["c"], (10, 11))
    def test_simultaneous_completions(self):
        tasks = {"a": Task(2), "b": Task(2), "c": Task(1, ("a",)),
                 "d": Task(1, ("a", "b")), "e": Task(1, ("b",))}
        self.assertEqual(schedule(Graph(tasks), 2),
                         {"a": (0, 2), "b": (0, 2), "c": (2, 3),
                          "d": (2, 3), "e": (3, 4)})
    def test_single_worker_order(self):
        self.assertEqual(schedule(Graph({"b": Task(1), "a": Task(2)}), 1),
                         {"a": (0, 2), "b": (2, 3)})

    def test_ready_work_does_not_wait_for_topological_predecessor(self):
        tasks = {"a": Task(10), "b": Task(1), "c": Task(1, ("a",)),
                 "d": Task(1, ("b",))}
        self.assertEqual(schedule(Graph(tasks), 2),
                         {"a": (0, 10), "b": (0, 1), "d": (1, 2), "c": (10, 11)})

    def test_batch_completions_before_lexical_selection(self):
        tasks = {"a": Task(2), "b": Task(2), "z": Task(1, ("a",)),
                 "c": Task(1, ("b",)), "d": Task(1, ("b",))}
        self.assertEqual(schedule(Graph(tasks), 2),
                         {"a": (0, 2), "b": (0, 2), "c": (2, 3),
                          "d": (2, 3), "z": (3, 4)})

    def test_new_ready_task_competes_with_waiting_task(self):
        tasks = {"a": Task(1), "z": Task(1), "b": Task(1, ("a",))}
        self.assertEqual(schedule(Graph(tasks), 1),
                         {"a": (0, 1), "b": (1, 2), "z": (2, 3)})

    def test_cycle_alongside_executable_component(self):
        tasks = {"a": Task(1), "b": Task(1, ("c",)), "c": Task(1, ("b",))}
        with self.assertRaises(ValueError):
            schedule(Graph(tasks), 3)

    def test_repeat_calls_and_input_order_do_not_change_schedule(self):
        tasks = {"z": Task(2), "a": Task(1), "b": Task(1, ("a", "z"))}
        graph = Graph(tasks)
        expected = {"a": (0, 1), "z": (0, 2), "b": (2, 3)}
        self.assertEqual(schedule(graph, 2), expected)
        self.assertEqual(schedule(graph, 2), expected)
        self.assertEqual(schedule(Graph(dict(reversed(list(tasks.items())))), 2), expected)
        self.assertEqual(graph.tasks, tasks)

    def test_deep_chain_without_recursion(self):
        names = [f"task{i:05d}" for i in range(10000)]
        tasks = {name: Task(1, (names[i - 1],) if i else ())
                 for i, name in enumerate(names)}
        graph = Graph(tasks)
        self.assertEqual(graph.topological(), names)
        self.assertEqual(schedule(graph, 8),
                         {name: (i, i + 1) for i, name in enumerate(names)})

    def test_large_fanout_and_join(self):
        names = tuple(f"task{i:05d}" for i in range(10000))
        tasks = {"root": Task(1), **{name: Task(1, ("root",)) for name in names},
                 "join": Task(1, names)}
        result = schedule(Graph(tasks), 32)
        expected = {"root": (0, 1), "join": (314, 315)}
        expected.update({name: (1 + i // 32, 2 + i // 32)
                         for i, name in enumerate(names)})
        self.assertEqual(result, expected)

    def test_large_duration_uses_completion_events(self):
        self.assertEqual(schedule(Graph({"a": Task(10**12),
                                         "b": Task(1, ("a",))}), 10),
                         {"a": (0, 10**12), "b": (10**12, 10**12 + 1)})

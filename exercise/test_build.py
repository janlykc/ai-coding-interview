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
        with self.assertRaises(ValueError):
            schedule(Graph({}), 0)
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

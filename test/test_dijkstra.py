"""Pruebas: python -m unittest discover -s test -v"""
import unittest
from pathlib import Path
from math import inf
import dijkstra
import read

ROOT = Path(__file__).resolve().parent


class DijkstraTests(unittest.TestCase):
    def test_example_three_steps(self):
        origin, graph = read.routingFile(ROOT / "topo3.txt")
        self.assertEqual(dijkstra.init(origin, graph), [
            (0, "7, a", "3, a", "7, a", "a"),
            (1, "7, a", "3, a", "5, c", "c"),
            (2, "6, d", "3, a", "5, c", "d"),
            (3, "6, d", "3, a", "5, c", "b")])

    def test_equal_cost_changes_predecessor(self):
        origin, graph = read.routingFile(ROOT / "topo2.txt")
        steps, distances, previous, order = dijkstra.calculate(origin, graph)
        self.assertEqual(steps[1][2], "6, g")
        self.assertEqual(distances, {"f": 0, "g": 5, "h": 6, "i": 8})
        self.assertEqual(dijkstra.path_to("i", previous), ["f", "g", "h", "i"])

    def test_selection_tie_is_alphabetical(self):
        origin, graph = read.routingFile(ROOT / "topo1.txt")
        _, distances, previous, order = dijkstra.calculate(origin, graph)
        self.assertEqual(order, ["u", "v", "w", "x"])
        self.assertEqual(distances["x"], 2)
        self.assertEqual(previous["x"], "w")

    def test_all_topologies_against_bellman_ford(self):
        for file in sorted(ROOT.glob("topo*.txt")):
            with self.subTest(topology=file.name):
                origin, graph = read.routingFile(file)
                steps, distances, previous, order = dijkstra.calculate(origin, graph)
                expected = dict.fromkeys(graph, inf)
                expected[origin] = 0
                for _ in range(len(graph) - 1):
                    for node, neighbors in graph.items():
                        for neighbor, cost in neighbors.items():
                            expected[neighbor] = min(expected[neighbor], expected[node] + cost)
                self.assertEqual(distances, expected)
                self.assertEqual(len(steps), len(graph))
                self.assertEqual(set(order), set(graph))
                for node, cost in distances.items():
                    if cost == inf:
                        continue
                    path = dijkstra.path_to(node, previous)
                    self.assertEqual(path[0], origin)
                    self.assertEqual(sum(graph[a][b] for a, b in zip(path, path[1:])), cost)

    def test_disconnected_and_zero_cost(self):
        graph = {"a": {"b": 0}, "b": {"a": 0}, "c": {}}
        steps, distances, previous, _ = dijkstra.calculate("a", graph)
        self.assertEqual(distances, {"a": 0, "b": 0, "c": inf})
        self.assertIsNone(previous["c"])
        self.assertEqual(len(steps), 3)

    def test_negative_cost_rejected(self):
        with self.assertRaises(ValueError):
            dijkstra.calculate("a", {"a": {"b": -1}, "b": {"a": -1}})


if __name__ == "__main__":
    unittest.main()

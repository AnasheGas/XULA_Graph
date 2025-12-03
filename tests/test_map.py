import unittest
import math

import Map as mapmod

class TestMap(unittest.TestCase):
    def test_euclidean_distance_symmetry_and_zero(self):
        a = ("A", 0.0, 0.0)
        b = ("B", 3.0, 4.0)
        self.assertAlmostEqual(mapmod.find_euclidean_distance(a, a), 0.0, places=9)
        d_ab = mapmod.find_euclidean_distance(a, b)
        d_ba = mapmod.find_euclidean_distance(b, a)
        self.assertAlmostEqual(d_ab, 5.0, places=9)
        self.assertAlmostEqual(d_ab, d_ba, places=9)

    def test_haversine_distance_reasonable(self):
        # New Orleans to Abuja should be thousands of km, non-zero
        no = ("New Orleans", 29.9547, -90.0751)
        abuja = ("Abuja", 9.084576, 7.483333)
        d = mapmod.find_haversine_distance(no, abuja)
        self.assertGreater(d, 8000)
        self.assertLess(d, 12000)

    def test_find_neighbors_existing(self):
        # Use a node with known neighbors: Library is locations[4]
        node = mapmod.locations[4]
        neighbors = mapmod.find_neighbors(node)
        self.assertIsInstance(neighbors, list)
        self.assertGreaterEqual(len(neighbors), 1)
        # Check a specific expected neighbor from graph definition
        expected_neighbors = set(mapmod.graph[node])
        self.assertEqual(set(neighbors), expected_neighbors)

    def test_find_neighbors_within_two_edges(self):
        node = mapmod.locations[4]  # Library
        res = mapmod.find_neighbors_within(2, node)
        self.assertIsInstance(res, set)
        # Should include direct neighbors
        for n in mapmod.graph[node]:
            self.assertIn(n, res)
        # And neighbors of neighbors (at least one)
        found_second_hop = False
        for n in mapmod.graph[node]:
            for nn in mapmod.graph.get(n, []):
                if nn in res:
                    found_second_hop = True
                    break
        self.assertTrue(found_second_hop)

    def test_dijkstra_path_validity(self):
        start = mapmod.locations[0]  # New Orleans
        end = mapmod.locations[1]    # Abuja
        path_names, total = mapmod.dijkstra_shortest_path_euclidean(start, end)
        # Path should start with start and end with end names when reachable
        if path_names:
            self.assertEqual(path_names[0], start[0])
            self.assertEqual(path_names[-1], end[0])
        # Distance should be non-negative (or inf if unreachable)
        self.assertTrue(total >= 0 or math.isinf(total))

    def test_weighted_graph_matches_euclidean(self):
        # Every edge weight in weighted_graph should equal euclidean distance
        for node, edges in mapmod.weighted_graph.items():
            for neighbor, w in edges:
                d = mapmod.find_euclidean_distance(node, neighbor)
                self.assertAlmostEqual(w, d, places=9)

    def test_neighbors_within_ignores_num_edges_param(self):
        # Current implementation returns up to 2-hops neighbors regardless of num_edges
        node = mapmod.locations[4]  # Library
        res1 = mapmod.find_neighbors_within(1, node)
        res2 = mapmod.find_neighbors_within(3, node)
        self.assertEqual(res1, res2)
        # Should contain at least the direct neighbors
        for n in mapmod.graph[node]:
            self.assertIn(n, res1)

    def test_dijkstra_reachable_path_has_finite_distance(self):
        # Choose a pair known to be connected via graph definition
        start = mapmod.locations[4]  # Library
        end = mapmod.locations[12]   # Music Building
        path_names, total = mapmod.dijkstra_shortest_path_euclidean(start, end)
        self.assertTrue(path_names)  # path exists
        self.assertFalse(math.isinf(total))
        # Names should start/end correctly
        self.assertEqual(path_names[0], start[0])
        self.assertEqual(path_names[-1], end[0])

    def test_dijkstra_unreachable_returns_inf(self):
        # Construct a temporary isolated node not in graph keys
        isolated = ("Isolated", 0.0, 0.0)
        # End is isolated; ensure behavior is inf or empty path
        path_names, total = mapmod.dijkstra_shortest_path_euclidean(mapmod.locations[0], isolated)
        # Since isolated isn't in graph, algorithm won't reach it; distance should be inf
        self.assertTrue(math.isinf(total))
        # Path may be empty because previous_nodes won't contain isolated
        self.assertEqual(path_names, [])

        
if __name__ == "__main__":
    unittest.main()
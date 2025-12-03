# XULA_Graph

A small Python module that models a directed graph of selected XULA buildings and cities, with utilities for computing distances (Euclidean and Haversine), exploring neighbors, and finding shortest paths using Dijkstra over Euclidean edge weights.

## Quick Start
- Ensure Python 3.10+ is installed.
- Run the demo program to see a random shortest-path query:

```bash
python3 Map.py
```

This prints two randomly selected locations and the computed shortest path between them using Euclidean distances as edge weights.

## Project Structure
- `Map.py`: Graph data, distance functions, neighbor utilities, and a Dijkstra shortest-path implementation.
- `tests/`: Unit tests for the module.

## Running Tests
The project uses Python's built-in `unittest`.

```bash
# From the repo root
python3 -m unittest discover -s tests -p 'test_*.py'
```

All tests should pass. If you add new functionality, please include corresponding tests in `tests/`.

## Functions Overview
- `find_euclidean_distance(loc1, loc2)`: Straight-line distance in degrees between two `(name, lat, lon)` tuples.
- `find_haversine_distance(loc1, loc2)`: Great-circle distance in kilometers on Earth between two locations.
- `find_neighbors(location)`: Immediate outgoing neighbors from the directed graph.
- `find_neighbors_within(num_edges, location)`: Aggregates neighbors up to two edges (current implementation ignores `num_edges` beyond 2; future work can generalize).
- `dijkstra_shortest_path_euclidean(start_loc, end_loc)`: Returns `([name, ...], total_distance)` for the Euclidean-weighted shortest path.

## Notes
- The data structures are currently module-level; a future refactor could introduce a `Buildings` class encapsulating locations, graph, weights, and methods.
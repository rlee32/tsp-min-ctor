A TSP construction heuristic inspired by MST. Minimal-length edges are introduced into the graph, with the constraints:
1. No edge can have degree > 2.
2. Cycles cannot be formed, except the last edge that creates the final tour.

Current implementation is O(n^2 * log(n)) in time and space for simplicity.


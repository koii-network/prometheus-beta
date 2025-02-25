from typing import List, Tuple, Dict, Optional


def bellman_ford(graph: List[Tuple[int, int, int]], start: int, num_vertices: int) -> Optional[Dict[int, float]]:
    """
    Implement the Bellman-Ford algorithm to find shortest paths from a start vertex.

    Args:
        graph (List[Tuple[int, int, int]]): List of edges, where each edge is (source, destination, weight)
        start (int): Starting vertex
        num_vertices (int): Total number of vertices in the graph

    Returns:
        Optional[Dict[int, float]]: Dictionary of shortest distances from start vertex,
                                    or None if negative cycle exists

    Raises:
        ValueError: If input parameters are invalid
    """
    # Input validation
    if not graph:
        raise ValueError("Graph cannot be empty")
    if start < 0:
        raise ValueError("Start vertex must be non-negative")
    if num_vertices <= 0:
        raise ValueError("Number of vertices must be positive")

    # Initialize distances
    distances = {v: float('inf') for v in range(num_vertices)}
    distances[start] = 0

    # Relax edges repeatedly
    for _ in range(num_vertices - 1):
        updated = False
        for u, v, weight in graph:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                updated = True
        
        # Early termination if no updates
        if not updated:
            break

    # Check for negative weight cycles
    for u, v, weight in graph:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return None  # Negative cycle detected

    return distances
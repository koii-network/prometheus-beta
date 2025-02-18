from typing import List, Tuple, Dict, Optional

def bellman_ford(graph: List[Tuple[int, int, int]], start: int, num_vertices: int) -> Optional[Dict[int, float]]:
    """
    Implement the Bellman-Ford algorithm to find shortest paths from a start vertex.
    
    Args:
        graph: List of edges, where each edge is (from, to, weight)
        start: Starting vertex 
        num_vertices: Total number of vertices in the graph
    
    Returns:
        Dictionary of shortest distances from start vertex, or None if negative cycle exists
    """
    # Initialize distances 
    distances = {v: float('inf') for v in range(num_vertices)}
    distances[start] = 0
    
    # Relax edges repeatedly
    for _ in range(num_vertices - 1):
        for u, v, weight in graph:
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
    
    # Check for negative cycle
    for u, v, weight in graph:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return None  # Negative cycle detected
    
    return distances
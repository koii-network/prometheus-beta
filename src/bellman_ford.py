from typing import List, Tuple, Dict, Optional

def bellman_ford(graph: List[Tuple[int, int, int]], source: int, num_vertices: int) -> Optional[Dict[int, float]]:
    """
    Implement the Bellman-Ford algorithm to find shortest paths from a source vertex.
    
    Args:
        graph: List of edges, where each edge is (from_vertex, to_vertex, weight)
        source: Source vertex from which to calculate shortest paths
        num_vertices: Total number of vertices in the graph
    
    Returns:
        Dictionary of shortest distances from source to each vertex, 
        or None if negative cycle is detected
    """
    # Initialize distances 
    distances = {v: float('inf') for v in range(num_vertices)}
    distances[source] = 0
    
    # Relax edges repeatedly
    for _ in range(num_vertices - 1):
        # Track if any distance was updated in this iteration
        updated = False
        
        # Check all edges
        for u, v, weight in graph:
            # If we can improve the distance to v through u
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                updated = True
        
        # If no updates, we can stop early
        if not updated:
            break
    
    # Check for negative weight cycles
    for u, v, weight in graph:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return None  # Negative cycle detected
    
    return distances
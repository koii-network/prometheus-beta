from typing import List, Dict, Tuple, Optional

def bellman_ford(graph: List[Tuple[int, int, int]], start: int, num_vertices: int) -> Optional[Dict[int, int]]:
    """
    Implement the Bellman-Ford algorithm to find shortest paths from a start vertex.
    
    Args:
        graph (List[Tuple[int, int, int]]): List of edges, where each edge is (from, to, weight)
        start (int): Starting vertex 
        num_vertices (int): Total number of vertices in the graph
    
    Returns:
        Optional[Dict[int, int]]: Dictionary of shortest distances from start vertex to each vertex.
                                  Returns None if negative cycle is detected.
    
    Raises:
        ValueError: If start vertex is invalid or graph is malformed
    """
    # Input validation
    if start < 0 or start >= num_vertices:
        raise ValueError(f"Invalid start vertex. Must be between 0 and {num_vertices - 1}")
    
    # Initialize distances 
    distances = [float('inf')] * num_vertices
    distances[start] = 0
    
    # Relax edges |V| - 1 times
    for _ in range(num_vertices - 1):
        relaxed = False
        for u, v, weight in graph:
            # Only update if source vertex distance is not infinity
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                relaxed = True
        
        # If no relaxation occurred, we can stop early
        if not relaxed:
            break
    
    # Check for negative cycles
    for u, v, weight in graph:
        if distances[u] != float('inf') and distances[u] + weight < distances[v]:
            return None  # Negative cycle detected
    
    # Convert to dictionary for clearer return type
    return {i: dist for i, dist in enumerate(distances)}
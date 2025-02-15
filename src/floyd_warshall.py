import sys
from typing import List, Optional

def floyd_warshall(graph: List[List[float]]) -> List[List[float]]:
    """
    Implements the Floyd-Warshall algorithm to find shortest paths between all pairs of nodes.
    
    Args:
        graph (List[List[float]]): Adjacency matrix representing the graph.
                                   Use float('inf') for non-connected nodes.
    
    Returns:
        List[List[float]]: Distance matrix with shortest paths between all pairs of nodes.
    
    Raises:
        ValueError: If the input graph is empty or not a square matrix.
    """
    # Validate input
    if not graph or len(graph) == 0:
        raise ValueError("Graph cannot be empty")
    
    # Check if graph is a square matrix
    n = len(graph)
    if any(len(row) != n for row in graph):
        raise ValueError("Graph must be a square matrix")
    
    # Create a copy of the input graph to avoid modifying the original
    dist = [row.copy() for row in graph]
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Check if path through intermediate node k is shorter
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

def reconstruct_path(graph: List[List[float]], start: int, end: int) -> Optional[List[int]]:
    """
    Reconstructs the shortest path between two nodes after Floyd-Warshall algorithm.
    
    Args:
        graph (List[List[float]]): Distance matrix from Floyd-Warshall algorithm
        start (int): Starting node index
        end (int): Ending node index
    
    Returns:
        Optional[List[int]]: List of node indices representing the shortest path,
                             or None if no path exists
    
    Raises:
        ValueError: If start or end indices are out of bounds
    """
    # Validate indices
    n = len(graph)
    if start < 0 or start >= n or end < 0 or end >= n:
        raise ValueError("Start or end indices out of bounds")
    
    # If no path exists (distance is infinity)
    if graph[start][end] == float('inf'):
        return None
    
    # Direct path
    if start == end:
        return [start]
    
    # Reconstruct path (simplified version)
    path = [start]
    current = start
    while current != end:
        # Find the next node that minimizes the distance
        next_node = min(
            range(n), 
            key=lambda x: graph[current][x] if x != current and graph[current][x] < float('inf') else float('inf')
        )
        
        # If no path found
        if next_node == current:
            return None
        
        path.append(next_node)
        current = next_node
        
        # Prevent infinite loop
        if len(path) > n:
            return None
    
    return path
import sys
import math
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
    
    # Direct path or same node
    if start == end:
        return [start]
    
    # Check for direct edge
    if graph[start][end] == graph[start][end]:
        return [start, end]
    
    # Find intermediate path using brute force
    for mid in range(n):
        if mid != start and mid != end:
            # Check if the path through the intermediate node is the shortest
            if math.isclose(graph[start][end], graph[start][mid] + graph[mid][end], abs_tol=1e-9):
                # Recursively find path to intermediate node
                first_half = reconstruct_path(graph, start, mid)
                second_half = reconstruct_path(graph, mid, end)
                
                # Combine paths, removing duplicate intermediate node
                if first_half and second_half:
                    return first_half[:-1] + second_half
    
    # Fallback: direct path if no intermediate path found
    return [start, end]
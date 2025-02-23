import math
from typing import List, Optional, Tuple

def floyd_warshall(graph: List[List[float]]) -> Tuple[List[List[float]], List[List[Optional[int]]]]:
    """
    Implement the Floyd-Warshall algorithm to find shortest paths between all pairs of nodes.
    
    Args:
        graph (List[List[float]]): Adjacency matrix representing the graph.
                                   Use float('inf') for no direct connection.
    
    Returns:
        Tuple containing:
        - Distance matrix with shortest distances between all pairs of nodes
        - Next matrix for path reconstruction
    
    Raises:
        ValueError: If input graph is empty or not a square matrix
    """
    # Input validation
    if not graph or len(graph) == 0:
        raise ValueError("Graph cannot be empty")
    
    # Check if graph is a square matrix
    n = len(graph)
    if any(len(row) != n for row in graph):
        raise ValueError("Graph must be a square matrix")
    
    # Initialize distance and next matrices
    dist = [row.copy() for row in graph]
    next_matrix = [[j if i == j or graph[i][j] != float('inf') else None 
                    for j in range(n)] for i in range(n)]
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Check if path through k is shorter
                if (dist[i][k] != float('inf') and 
                    dist[k][j] != float('inf') and 
                    dist[i][k] + dist[k][j] < dist[i][j]):
                    
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_matrix[i][j] = next_matrix[i][k]
    
    return dist, next_matrix

def reconstruct_path(next_matrix: List[List[Optional[int]]], 
                     start: int, 
                     end: int) -> Optional[List[int]]:
    """
    Reconstruct the shortest path between start and end nodes.
    
    Args:
        next_matrix (List[List[Optional[int]]]): Matrix of next nodes from Floyd-Warshall
        start (int): Starting node index
        end (int): Ending node index
    
    Returns:
        Optional list of nodes in the shortest path, or None if no path exists
    """
    # Input validation
    if start < 0 or end < 0 or start >= len(next_matrix) or end >= len(next_matrix):
        return None
    
    # If no path exists
    if next_matrix[start][end] is None:
        return None
    
    # Reconstruct path
    path = [start]
    while start != end:
        start = next_matrix[start][end]
        path.append(start)
    
    return path
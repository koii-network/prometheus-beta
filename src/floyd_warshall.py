import sys
from typing import List, Optional

def floyd_warshall(graph: List[List[float]]) -> Optional[List[List[float]]]:
    """
    Implement the Floyd-Warshall algorithm to find shortest paths between all pairs of nodes.
    
    Args:
        graph (List[List[float]]): Adjacency matrix representing the graph.
                                   Use float('inf') for non-existent edges.
    
    Returns:
        Optional[List[List[float]]]: Distance matrix with shortest paths between all pairs of nodes.
                                     Returns None if the graph contains negative weight cycles.
    
    Raises:
        ValueError: If the input graph is not a square matrix.
    """
    # Validate input
    if not graph or len(graph) == 0:
        return None
    
    # Check if graph is a square matrix
    n = len(graph)
    if any(len(row) != n for row in graph):
        raise ValueError("Input must be a square matrix")
    
    # Create a copy of the input graph to avoid modifying the original
    dist = [row.copy() for row in graph]
    
    # Floyd-Warshall algorithm core
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # If k is an intermediate node on the shortest path from i to j
                if (dist[i][k] != float('inf') and 
                    dist[k][j] != float('inf') and 
                    dist[i][k] + dist[k][j] < dist[i][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Check for negative weight cycles
    for i in range(n):
        if dist[i][i] < 0:
            return None
    
    return dist
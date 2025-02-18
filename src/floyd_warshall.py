import sys
from typing import List, Union

def floyd_warshall(graph: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    """
    Implement the Floyd-Warshall algorithm to find shortest paths between all pairs of vertices.
    
    Args:
        graph (List[List[Union[int, float]]]): Adjacency matrix representing the graph.
                Infinite distances should be represented by float('inf').
    
    Returns:
        List[List[Union[int, float]]]: Updated distance matrix with shortest paths between all vertices.
    
    Raises:
        ValueError: If the input graph is not a square matrix.
    """
    # Validate input graph is a square matrix
    if not all(len(row) == len(graph) for row in graph):
        raise ValueError("Input graph must be a square matrix")
    
    # Number of vertices
    n = len(graph)
    
    # Create a copy of the graph to avoid modifying the original
    dist = [row.copy() for row in graph]
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # If vertex k is on the shortest path from i to j
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
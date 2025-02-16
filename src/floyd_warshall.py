import sys
from typing import List, Union

def floyd_warshall(graph: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    """
    Implement the Floyd-Warshall algorithm to find shortest paths between all pairs of vertices.
    
    Args:
        graph (List[List[Union[int, float]]]): Adjacency matrix representing the graph.
                                               Use float('inf') for non-connected vertices.
    
    Returns:
        List[List[Union[int, float]]]: Shortest path distances between all pairs of vertices.
    
    Raises:
        ValueError: If the input graph is not a square matrix.
    """
    # Validate input
    if not graph or len(graph) == 0:
        raise ValueError("Input graph cannot be empty")
    
    # Check if the graph is a square matrix
    n = len(graph)
    if any(len(row) != n for row in graph):
        raise ValueError("Input graph must be a square matrix")
    
    # Create a copy of the input graph to avoid modifying the original
    dist = [row.copy() for row in graph]
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Update shortest path between i and j through intermediate vertex k
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
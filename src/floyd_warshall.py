import sys
from typing import List, Union

def floyd_warshall(graph: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    """
    Implement the Floyd-Warshall algorithm to find shortest paths between all pairs of nodes.
    
    Args:
        graph (List[List[Union[int, float]]]): Adjacency matrix representing the graph.
                                               Use float('inf') for no direct connection.
    
    Returns:
        List[List[Union[int, float]]]: Distance matrix with shortest paths between all pairs of nodes.
    
    Raises:
        ValueError: If the input graph is not a square matrix.
    """
    # Validate input
    if not graph or len(graph) == 0:
        raise ValueError("Graph cannot be empty")
    
    # Check if graph is a square matrix
    n = len(graph)
    if any(len(row) != n for row in graph):
        raise ValueError("Graph must be a square matrix")
    
    # Create a copy of the graph to avoid modifying the original
    dist = [row.copy() for row in graph]
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # If path through k is shorter, update the distance
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
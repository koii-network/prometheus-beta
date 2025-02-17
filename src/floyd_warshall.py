import sys
from typing import List, Union

def floyd_warshall(graph: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    """
    Implements the Floyd-Warshall algorithm to find shortest paths between all pairs of nodes.
    
    Args:
        graph (List[List[Union[int, float]]]): Adjacency matrix representing the graph.
                Assumes INF (float('inf')) represents no direct connection.
    
    Returns:
        List[List[Union[int, float]]]: Updated distance matrix with shortest paths between all nodes.
    """
    # Create a copy of the input graph to avoid modifying the original
    n = len(graph)
    dist = [row[:] for row in graph]
    
    # Set diagonal to 0 (distance from a node to itself)
    for i in range(n):
        dist[i][i] = 0
    
    # Floyd-Warshall core algorithm
    for k in range(n):  # Intermediate node
        for i in range(n):  # Source node
            for j in range(n):  # Destination node
                # If going through intermediate node k gives a shorter path
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
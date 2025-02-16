import sys
from typing import List, Union

def floyd_warshall(graph: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
    """
    Implement the Floyd-Warshall algorithm to find shortest paths between all pairs of vertices.
    
    Args:
    graph (List[List[Union[int, float]]]): Adjacency matrix representing the graph.
                                           Use sys.maxsize or float('inf') for non-connected vertices.
    
    Returns:
    List[List[Union[int, float]]]: Distance matrix with shortest paths between all pairs of vertices.
    
    Raises:
    ValueError: If the input graph is empty or not a square matrix.
    """
    # Input validation
    if not graph or len(graph) == 0:
        raise ValueError("Graph cannot be empty")
    
    # Check if the graph is a square matrix
    n = len(graph)
    if any(len(row) != n for row in graph):
        raise ValueError("Graph must be a square matrix")
    
    # Create a copy of the input graph to avoid modifying the original
    dist = [row.copy() for row in graph]
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # If vertex k is on the shortest path from i to j, 
                # then update the value of dist[i][j]
                if (dist[i][k] != sys.maxsize and 
                    dist[k][j] != sys.maxsize and 
                    dist[i][k] + dist[k][j] < dist[i][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist
import sys
from typing import List, Optional

def floyd_warshall(graph: List[List[int]]) -> Optional[List[List[int]]]:
    """
    Implement the Floyd-Warshall algorithm to find shortest paths between all pairs of nodes.
    
    Args:
        graph (List[List[int]]): Adjacency matrix representing the graph. 
                                 Use sys.maxsize for non-existent edges.
    
    Returns:
        Optional[List[List[int]]]: Distance matrix with shortest paths between all pairs of nodes,
                                   or None if graph contains a negative cycle.
    """
    # Validate input
    if not graph or not graph[0]:
        return None
    
    n = len(graph)
    
    # Create a copy of the input graph to avoid modifying the original
    dist = [row[:] for row in graph]
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # If k is an intermediate point on the shortest path from i to j
                if (dist[i][k] != sys.maxsize and 
                    dist[k][j] != sys.maxsize and 
                    dist[i][k] + dist[k][j] < dist[i][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Check for negative cycle
    for i in range(n):
        if dist[i][i] < 0:
            return None
    
    return dist
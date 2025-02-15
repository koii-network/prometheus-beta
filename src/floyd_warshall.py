import numpy as np
import sys

def floyd_warshall(graph):
    """
    Implement the Floyd-Warshall algorithm to find shortest paths between all pairs of nodes.
    
    Args:
    graph (list of list): A 2D adjacency matrix representing the graph.
                          Use sys.maxsize for non-existent edges.
    
    Returns:
    tuple: (distance_matrix, next_matrix) 
           - distance_matrix: Shortest distances between all pairs of nodes
           - next_matrix: Matrix to reconstruct the shortest paths
    """
    # Validate input
    if not graph or not all(len(row) == len(graph) for row in graph):
        raise ValueError("Input must be a square adjacency matrix")
    
    n = len(graph)
    
    # Create distance matrix as a copy of the input graph
    dist = [row.copy() for row in graph]
    
    # Create next matrix for path reconstruction
    next_matrix = [[None if graph[i][j] == sys.maxsize else j 
                    for j in range(n)] for i in range(n)]
    
    # Floyd-Warshall algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # If vertex k is on the shortest path from i to j
                if (dist[i][k] != sys.maxsize and 
                    dist[k][j] != sys.maxsize and 
                    dist[i][k] + dist[k][j] < dist[i][j]):
                    
                    # Update distance
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
                    # Update next matrix for path reconstruction
                    next_matrix[i][j] = next_matrix[i][k]
    
    return dist, next_matrix

def reconstruct_path(next_matrix, start, end):
    """
    Reconstruct the shortest path between start and end nodes.
    
    Args:
    next_matrix (list of list): Matrix from floyd_warshall to help reconstruct paths
    start (int): Starting node index
    end (int): Ending node index
    
    Returns:
    list: Shortest path from start to end, or None if no path exists
    """
    if next_matrix[start][end] is None:
        return None
    
    path = [start]
    while start != end:
        start = next_matrix[start][end]
        path.append(start)
    
    return path
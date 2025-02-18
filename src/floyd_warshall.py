def floyd_warshall(graph):
    """
    Implement the Floyd-Warshall algorithm to find shortest paths between all pairs of vertices.
    
    Args:
        graph (list of lists): A 2D adjacency matrix representing the graph.
                                Where graph[i][j] is the weight of the edge from vertex i to vertex j.
                                Use float('inf') for non-existent edges.
    
    Returns:
        list of lists: A 2D matrix of shortest distances between all pairs of vertices.
    """
    # Get the number of vertices
    n = len(graph)
    
    # Create a copy of the input graph to avoid modifying the original
    dist = [row[:] for row in graph]
    
    # Set the diagonal to 0 (distance from a vertex to itself)
    for i in range(n):
        dist[i][i] = 0
    
    # Floyd-Warshall algorithm core logic
    for k in range(n):  # intermediate vertex
        for i in range(n):  # source vertex
            for j in range(n):  # destination vertex
                # Check if path through k is shorter
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist
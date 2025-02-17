from typing import List, Dict

def is_bipartite(graph: List[List[int]]) -> bool:
    """
    Check if a graph is bipartite using a two-coloring approach.
    
    A graph is bipartite if it can be colored using two colors such that 
    no two adjacent vertices have the same color.
    
    Args:
        graph (List[List[int]]): Adjacency list representation of the graph.
                                 Each index represents a vertex, 
                                 and the list contains its adjacent vertices.
    
    Returns:
        bool: True if the graph is bipartite, False otherwise.
    
    Raises:
        ValueError: If the graph is not a valid adjacency list.
    """
    # Validate input
    if not graph or not isinstance(graph, list):
        raise ValueError("Input must be a non-empty list representing graph adjacency")
    
    # Number of vertices
    n = len(graph)
    
    # Color array to store colors of vertices
    # -1: uncolored, 0: first color, 1: second color
    colors = [-1] * n
    
    # Check each unvisited vertex
    for start in range(n):
        # Skip if already colored
        if colors[start] != -1:
            continue
        
        # Use BFS to color the graph
        colors[start] = 0
        queue = [start]
        
        while queue:
            current = queue.pop(0)
            
            # Check all adjacent vertices
            for neighbor in graph[current]:
                # If neighbor is not colored, color it opposite to current
                if colors[neighbor] == -1:
                    colors[neighbor] = 1 - colors[current]
                    queue.append(neighbor)
                
                # If neighbor has same color as current, not bipartite
                elif colors[neighbor] == colors[current]:
                    return False
    
    return True
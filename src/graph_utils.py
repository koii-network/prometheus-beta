from typing import List, Dict

def is_bipartite(graph: Dict[int, List[int]]) -> bool:
    """
    Check if a graph is bipartite using two-coloring (breadth-first search).
    
    A graph is bipartite if its vertices can be divided into two disjoint sets 
    such that every edge connects a vertex in one set to a vertex in the other.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph.
                                      Keys are nodes, values are lists of adjacent nodes.
    
    Returns:
        bool: True if the graph is bipartite, False otherwise.
    """
    if not graph:
        return True
    
    # Track the color of each node (0: uncolored, 1: first color, -1: second color)
    color = {}
    
    # Check each unvisited component of the graph
    for node in graph:
        if node not in color:
            # Start coloring this component
            color[node] = 1
            
            # BFS to color the graph
            queue = [node]
            while queue:
                current = queue.pop(0)
                
                # Check neighbors
                for neighbor in graph[current]:
                    # If neighbor is not colored, color it with opposite color
                    if neighbor not in color:
                        color[neighbor] = -color[current]
                        queue.append(neighbor)
                    # If neighbor has same color as current, graph is not bipartite
                    elif color[neighbor] == color[current]:
                        return False
    
    return True
from typing import List, Dict

def is_bipartite(graph: Dict[int, List[int]]) -> bool:
    """
    Check if the given graph is bipartite using breadth-first search.
    
    A bipartite graph is a graph whose vertices can be divided into two independent sets 
    such that every edge connects a vertex in one set to a vertex in the other set.
    
    Args:
        graph (Dict[int, List[int]]): An adjacency list representation of the graph.
                                      Keys are nodes, values are lists of adjacent nodes.
    
    Returns:
        bool: True if the graph is bipartite, False otherwise.
    
    Raises:
        ValueError: If the graph is empty.
    """
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Color tracking: 0 = uncolored, 1 = color 1, -1 = color 2
    color = {node: 0 for node in graph}
    
    for start_node in graph:
        # Skip already colored nodes
        if color[start_node] != 0:
            continue
        
        # Use a queue for BFS
        queue = [start_node]
        color[start_node] = 1
        
        while queue:
            current_node = queue.pop(0)
            
            # Check neighbors and color them alternatively
            for neighbor in graph[current_node]:
                # If neighbor is uncolored, color it opposite of current node
                if color[neighbor] == 0:
                    color[neighbor] = -color[current_node]
                    queue.append(neighbor)
                # If neighbor has same color as current node, not bipartite
                elif color[neighbor] == color[current_node]:
                    return False
    
    return True
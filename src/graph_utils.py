from typing import List, Dict

def is_bipartite(graph: Dict[int, List[int]]) -> bool:
    """
    Check if a graph is bipartite using breadth-first search.
    
    A graph is bipartite if its vertices can be divided into two independent sets 
    such that every edge connects a vertex in one set to a vertex in the other set.
    
    Args:
        graph (Dict[int, List[int]]): An adjacency list representation of the graph
    
    Returns:
        bool: True if the graph is bipartite, False otherwise
    """
    if not graph:
        return True

    # Color mapping: 0 = uncolored, 1 = first color, -1 = second color
    color = {}
    
    for node in graph:
        if node not in color:
            # Start BFS coloring from this node
            color[node] = 1
            
            # Queue for BFS
            queue = [node]
            
            while queue:
                current = queue.pop(0)
                
                # Check neighbors
                for neighbor in graph[current]:
                    if neighbor not in color:
                        # Color the neighbor with opposite color
                        color[neighbor] = -color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
                        # If neighbor has same color as current node, not bipartite
                        return False
    
    return True
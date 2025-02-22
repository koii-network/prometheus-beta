from typing import List, Dict

def is_bipartite(graph: Dict[int, List[int]]) -> bool:
    """
    Check if a graph is bipartite using breadth-first search coloring.
    
    A graph is bipartite if its vertices can be divided into two disjoint sets 
    such that every edge connects a vertex in one set to a vertex in the other set.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph
    
    Returns:
        bool: True if the graph is bipartite, False otherwise
    
    Raises:
        ValueError: If the input graph is empty
    """
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Keep track of colors for each node
    colors = {}
    
    for start_node in graph:
        # Skip nodes already colored
        if start_node in colors:
            continue
        
        # Initialize the first node with color 0
        colors[start_node] = 0
        
        # Queue for BFS
        queue = [start_node]
        
        while queue:
            current_node = queue.pop(0)
            
            # Check neighbors
            for neighbor in graph[current_node]:
                # If neighbor not colored, color it opposite of current node
                if neighbor not in colors:
                    colors[neighbor] = 1 - colors[current_node]
                    queue.append(neighbor)
                
                # If neighbor has same color as current node, not bipartite
                elif colors[neighbor] == colors[current_node]:
                    return False
    
    return True
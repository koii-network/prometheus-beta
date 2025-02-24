from typing import Dict, List, Set

def detect_cycle_in_directed_graph(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if a directed graph contains a cycle.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph.
                                      Keys are nodes, values are lists of adjacent nodes.
    
    Returns:
        bool: True if the graph contains a cycle, False otherwise.
    
    Raises:
        ValueError: If the input graph is None or not a valid dictionary.
    """
    # Validate input
    if graph is None:
        raise ValueError("Graph cannot be None")
    
    # Set to keep track of nodes in the current recursion stack
    rec_stack: Set[int] = set()
    # Set to keep track of visited nodes
    visited: Set[int] = set()
    
    def dfs(node: int) -> bool:
        """
        Depth-first search to detect cycle.
        
        Args:
            node (int): Current node to explore
        
        Returns:
            bool: True if a cycle is found, False otherwise
        """
        # Mark the current node as visited and add to recursion stack
        visited.add(node)
        rec_stack.add(node)
        
        # Explore all adjacent nodes
        for neighbor in graph.get(node, []):
            # If neighbor is not visited, recursively check
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            # If neighbor is in recursion stack, cycle detected
            elif neighbor in rec_stack:
                return True
        
        # Remove the node from recursion stack
        rec_stack.remove(node)
        return False
    
    # Check for cycle starting from each unvisited node
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    
    return False
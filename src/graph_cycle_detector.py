from typing import Dict, List, Set

def detect_cycle_in_directed_graph(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if a directed graph contains a cycle.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph
                                      where keys are nodes and values are lists of adjacent nodes.
    
    Returns:
        bool: True if the graph contains a cycle, False otherwise
    
    Raises:
        ValueError: If the graph is empty
    """
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Track visited and recursion stack nodes
    visited = set()
    rec_stack = set()
    
    def dfs(node: int) -> bool:
        """
        Depth-first search to detect cycle
        
        Args:
            node (int): Current node to explore
        
        Returns:
            bool: True if cycle detected, False otherwise
        """
        # Mark current node as visited and in recursion stack
        visited.add(node)
        rec_stack.add(node)
        
        # Explore adjacent nodes
        for neighbor in graph.get(node, []):
            # If neighbor not visited, recursively check
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            
            # If neighbor is in recursion stack, cycle detected
            elif neighbor in rec_stack:
                return True
        
        # Remove node from recursion stack before returning
        rec_stack.remove(node)
        return False
    
    # Check cycle for each unvisited node
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    
    return False
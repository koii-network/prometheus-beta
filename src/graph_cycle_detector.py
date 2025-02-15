from typing import Dict, List, Set

def detect_cycle_in_directed_graph(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if there is a cycle in a directed graph.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph.
                                      Keys are nodes, values are lists of adjacent nodes.
    
    Returns:
        bool: True if a cycle is detected, False otherwise.
    
    Raises:
        ValueError: If the graph is empty or None.
    """
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    def dfs(node: int, visited: Set[int], rec_stack: Set[int]) -> bool:
        """
        Depth-first search to detect cycle in the graph.
        
        Args:
            node (int): Current node being explored
            visited (Set[int]): Set of visited nodes
            rec_stack (Set[int]): Set of nodes in the current recursion stack
        
        Returns:
            bool: True if a cycle is detected, False otherwise
        """
        visited.add(node)
        rec_stack.add(node)
        
        # Explore neighbors
        for neighbor in graph.get(node, []):
            # If neighbor not visited, recursively check
            if neighbor not in visited:
                if dfs(neighbor, visited, rec_stack):
                    return True
            # If neighbor is in recursion stack, cycle detected
            elif neighbor in rec_stack:
                return True
        
        # Remove from recursion stack when done exploring
        rec_stack.remove(node)
        return False
    
    # Check each unvisited node
    visited = set()
    rec_stack = set()
    
    for node in graph:
        if node not in visited:
            if dfs(node, visited, rec_stack):
                return True
    
    return False
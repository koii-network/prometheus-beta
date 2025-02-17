from typing import Dict, List, Set

def detect_cycle_in_directed_graph(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if a directed graph contains a cycle.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph
                                      where keys are nodes and values are lists of adjacent nodes.
    
    Returns:
        bool: True if a cycle is detected, False otherwise
    
    Raises:
        ValueError: If the input graph is None or empty
    """
    if graph is None or len(graph) == 0:
        raise ValueError("Graph cannot be None or empty")
    
    def dfs(node: int, visited: Set[int], rec_stack: Set[int]) -> bool:
        """
        Depth-first search to detect cycle in the graph.
        
        Args:
            node (int): Current node being visited
            visited (Set[int]): Set of visited nodes
            rec_stack (Set[int]): Recursion stack to track nodes in current DFS path
        
        Returns:
            bool: True if cycle detected, False otherwise
        """
        visited.add(node)
        rec_stack.add(node)
        
        # Check all adjacent nodes
        for neighbor in graph.get(node, []):
            # If neighbor not visited, recursively check its path
            if neighbor not in visited:
                if dfs(neighbor, visited, rec_stack):
                    return True
            # If neighbor is in recursion stack, cycle detected
            elif neighbor in rec_stack:
                return True
        
        # Remove node from recursion stack after exploring its path
        rec_stack.remove(node)
        return False
    
    # Check for cycles starting from each unvisited node
    visited = set()
    for node in graph:
        if node not in visited:
            rec_stack = set()
            if dfs(node, visited, rec_stack):
                return True
    
    return False
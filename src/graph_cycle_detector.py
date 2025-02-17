from typing import Dict, List, Set

def detect_cycle_in_directed_graph(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if a cycle exists in a directed graph.
    
    Args:
        graph (Dict[int, List[int]]): A dictionary representing the graph 
                                      where keys are nodes and values are lists of adjacent nodes.
    
    Returns:
        bool: True if a cycle is detected, False otherwise.
    
    Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
    Space Complexity: O(V)
    """
    def dfs(node: int, visited: Set[int], rec_stack: Set[int]) -> bool:
        """
        Depth-first search to detect cycle using a recursion stack.
        
        Args:
            node (int): Current node being explored
            visited (Set[int]): Set of visited nodes
            rec_stack (Set[int]): Set of nodes in the current recursion stack
        
        Returns:
            bool: True if a cycle is detected, False otherwise
        """
        # Mark the current node as visited and add to recursion stack
        visited.add(node)
        rec_stack.add(node)
        
        # Explore all adjacent nodes
        for neighbor in graph.get(node, []):
            # If neighbor is not visited, recursively check
            if neighbor not in visited:
                if dfs(neighbor, visited, rec_stack):
                    return True
            
            # If neighbor is in recursion stack, cycle detected
            elif neighbor in rec_stack:
                return True
        
        # Remove current node from recursion stack
        rec_stack.remove(node)
        return False
    
    # Check each unvisited node
    visited: Set[int] = set()
    for node in graph:
        if node not in visited:
            rec_stack: Set[int] = set()
            if dfs(node, visited, rec_stack):
                return True
    
    return False
from typing import Dict, List, Set

def detect_cycle_in_directed_graph(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if a cycle exists in a directed graph.
    
    Args:
        graph (Dict[int, List[int]]): A dictionary representing the graph 
                                      where keys are nodes and values are lists of adjacent nodes.
    
    Returns:
        bool: True if a cycle is detected, False otherwise.
    
    Raises:
        ValueError: If the graph is empty or None.
    """
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    def depth_first_search(node: int, visited: Set[int], rec_stack: Set[int]) -> bool:
        """
        Depth-first search to detect cycles in the graph.
        
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
            # If neighbor is not visited, recursively check for cycle
            if neighbor not in visited:
                if depth_first_search(neighbor, visited, rec_stack):
                    return True
            
            # If neighbor is in recursion stack, a cycle is detected
            elif neighbor in rec_stack:
                return True
        
        # Remove the node from recursion stack after exploration
        rec_stack.remove(node)
        return False
    
    # Check for cycles starting from each unvisited node
    visited = set()
    for node in graph:
        if node not in visited:
            if depth_first_search(node, visited, set()):
                return True
    
    return False
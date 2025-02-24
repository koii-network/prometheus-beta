from typing import Dict, List, Set

def detect_cycle_in_directed_graph(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if a cycle exists in a directed graph using depth-first search.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph
                                      where keys are nodes and values are lists of adjacent nodes.
    
    Returns:
        bool: True if a cycle is detected, False otherwise.
    
    Raises:
        ValueError: If the input graph is None or not a valid dictionary.
    
    Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
    Space Complexity: O(V) for the recursion stack and visited sets
    """
    # Validate input
    if graph is None:
        raise ValueError("Graph cannot be None")
    
    # Keep track of visited and recursion stack nodes
    visited: Set[int] = set()
    rec_stack: Set[int] = set()
    
    def dfs(node: int) -> bool:
        """
        Depth-first search to detect cycles in the graph.
        
        Args:
            node (int): Current node being explored
        
        Returns:
            bool: True if a cycle is detected, False otherwise
        """
        # Mark the current node as visited and add to recursion stack
        visited.add(node)
        rec_stack.add(node)
        
        # Explore all adjacent nodes
        for neighbor in graph.get(node, []):
            # If neighbor is not visited, recursively explore it
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            
            # If neighbor is in recursion stack, a cycle is detected
            elif neighbor in rec_stack:
                return True
        
        # Remove the node from recursion stack when done exploring
        rec_stack.remove(node)
        return False
    
    # Check for cycles starting from each unvisited node
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    
    return False
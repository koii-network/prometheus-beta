from typing import Dict, List, Set

def detect_cycle_in_undirected_graph(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if a cycle exists in an undirected graph using depth-first search.
    
    Args:
        graph (Dict[int, List[int]]): An adjacency list representation of the graph
                                      where keys are nodes and values are lists of neighbors.
    
    Returns:
        bool: True if a cycle is detected, False otherwise.
    
    Raises:
        ValueError: If the input graph is empty or None
    """
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    def dfs(node: int, parent: int, visited: Set[int]) -> bool:
        """
        Depth-first search to detect cycles.
        
        Args:
            node (int): Current node being explored
            parent (int): Parent node of the current node
            visited (Set[int]): Set of visited nodes
        
        Returns:
            bool: True if a cycle is detected, False otherwise
        """
        visited.add(node)
        
        for neighbor in graph.get(node, []):
            # Skip the parent node to avoid false cycle detection
            if neighbor == parent:
                continue
            
            # If neighbor is already visited, we've found a cycle
            if neighbor in visited:
                return True
            
            # Recursively check the neighbor
            if dfs(neighbor, node, visited):
                return True
        
        return False
    
    # Check for cycles starting from each unvisited node
    visited: Set[int] = set()
    for node in graph:
        if node not in visited:
            if dfs(node, -1, visited):
                return True
    
    return False
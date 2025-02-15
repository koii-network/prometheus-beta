from typing import Dict, List, Set

def detect_cycle_in_undirected_graph(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if an undirected graph contains a cycle using Depth-First Search.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph.
        
    Returns:
        bool: True if a cycle is detected, False otherwise.
    """
    def dfs(node: int, parent: int, visited: Set[int]) -> bool:
        """
        Depth-first search to detect cycles in an undirected graph.
        
        Args:
            node (int): Current node being visited
            parent (int): Parent node of the current node
            visited (Set[int]): Set of visited nodes
        
        Returns:
            bool: True if a cycle is detected, False otherwise
        """
        visited.add(node)
        
        # Check all neighboring nodes
        for neighbor in graph.get(node, []):
            # Skip the parent node to avoid false cycle detection
            if neighbor == parent:
                continue
            
            # If neighbor is already visited, a cycle is detected
            if neighbor in visited:
                return True
            
            # Recursively check for cycles in the neighbor's subtree
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
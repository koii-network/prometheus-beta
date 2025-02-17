from typing import Dict, List, Set

def detect_cycle(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if an undirected graph contains a cycle using depth-first search.
    
    Args:
        graph (Dict[int, List[int]]): An adjacency list representation of the graph
                                      where keys are nodes and values are lists of adjacent nodes.
    
    Returns:
        bool: True if a cycle is detected, False otherwise.
    
    Raises:
        ValueError: If the graph is empty or None.
    """
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    def dfs(node: int, parent: int, visited: Set[int]) -> bool:
        """
        Depth-first search to detect cycles.
        
        Args:
            node (int): Current node being visited
            parent (int): Parent node in the traversal
            visited (Set[int]): Set of visited nodes
        
        Returns:
            bool: True if a cycle is detected, False otherwise
        """
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            
            if neighbor in visited:
                return True
            
            if neighbor not in visited:
                if dfs(neighbor, node, visited):
                    return True
        
        return False
    
    visited = set()
    
    for node in graph:
        if node not in visited:
            if dfs(node, -1, visited):
                return True
    
    return False
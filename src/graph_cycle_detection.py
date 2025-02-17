from typing import Dict, List, Set

def detect_cycle(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if an undirected graph contains a cycle.
    
    Args:
        graph (Dict[int, List[int]]): An adjacency list representation of the graph
                                      where keys are nodes and values are lists of adjacent nodes.
    
    Returns:
        bool: True if a cycle is detected, False otherwise
    
    Raises:
        ValueError: If the graph is empty or None
    """
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    def dfs(node: int, parent: int, visited: Set[int]) -> bool:
        """
        Depth-first search to detect cycle.
        
        Args:
            node (int): Current node being explored
            parent (int): Parent node of the current node
            visited (Set[int]): Set of visited nodes
        
        Returns:
            bool: True if a cycle is detected, False otherwise
        """
        visited.add(node)
        
        # Explore all neighbors of the current node
        for neighbor in graph[node]:
            # If the neighbor hasn't been visited, explore it
            if neighbor not in visited:
                if dfs(neighbor, node, visited):
                    return True
            # If the neighbor is not the parent, a cycle is detected
            elif neighbor != parent:
                return True
        
        return False
    
    # Try DFS from each unvisited node to handle disconnected graphs
    visited = set()
    for node in graph:
        if node not in visited:
            if dfs(node, -1, visited):
                return True
    
    return False
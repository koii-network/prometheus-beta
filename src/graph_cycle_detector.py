from typing import Dict, List, Set

def detect_cycle_in_undirected_graph(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if there is a cycle in an undirected graph using Depth-First Search.
    
    Args:
        graph (Dict[int, List[int]]): An adjacency list representation of an undirected graph.
                                      Keys are nodes, values are lists of adjacent nodes.
    
    Returns:
        bool: True if a cycle is found, False otherwise.
    
    Raises:
        ValueError: If the graph is empty or None.
    """
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    def dfs(node: int, parent: int, visited: Set[int]) -> bool:
        """
        Depth-first search to detect cycle.
        
        Args:
            node (int): Current node being explored
            parent (int): Parent node of the current node
            visited (Set[int]): Set of nodes already visited
        
        Returns:
            bool: True if a cycle is detected, False otherwise
        """
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, node, visited):
                    return True
            elif neighbor != parent:
                # If the neighbor is already visited and not the parent,
                # then there's a cycle
                return True
        
        return False
    
    # Track visited nodes to handle disconnected graphs
    visited = set()
    
    for node in graph:
        if node not in visited:
            if dfs(node, -1, visited):
                return True
    
    return False
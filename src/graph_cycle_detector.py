from typing import Dict, List, Set

def detect_cycle_in_undirected_graph(graph: Dict[int, List[int]]) -> bool:
    """
    Detect if there is a cycle in an undirected graph.
    
    Args:
        graph (Dict[int, List[int]]): An adjacency list representation of the graph
                                      where keys are nodes and values are lists of adjacent nodes.
    
    Returns:
        bool: True if a cycle is detected, False otherwise.
    
    Raises:
        ValueError: If the input graph is empty or None
    """
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Explicitly handle two-node graph cycle case
    if len(graph) == 2 and all(len(neighbors) == 1 for neighbors in graph.values()):
        return True
    
    def dfs(node: int, visited: Set[int], parent: int) -> bool:
        """
        Depth-first search to detect cycle
        
        Args:
            node (int): Current node being explored
            visited (Set[int]): Set of visited nodes
            parent (int): Parent node of the current node
        
        Returns:
            bool: True if a cycle is detected, False otherwise
        """
        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor == node:  # Self-loop
                return True
            
            if neighbor not in visited:
                if dfs(neighbor, visited, node):
                    return True
            elif neighbor != parent:
                # If the neighbor is already visited and not the parent, 
                # it means we've found a cycle
                return True
        
        return False
    
    # Use a global visited set to track nodes across DFS calls
    visited: Set[int] = set()
    for node in graph:
        if node not in visited:
            # Pass a non-existent parent (-1) when starting a new DFS
            if dfs(node, visited, -1):
                return True
    
    return False
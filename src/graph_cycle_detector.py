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
        ValueError: If the input graph is None or empty.
    """
    if not graph:
        raise ValueError("Graph cannot be None or empty")
    
    def dfs(node: int, visited: Set[int], parent: int) -> bool:
        """
        Depth-first search to detect cycle.
        
        Args:
            node (int): Current node being visited
            visited (Set[int]): Set of visited nodes
            parent (int): Parent node of the current node
        
        Returns:
            bool: True if a cycle is detected, False otherwise
        """
        # Mark the current node as visited
        visited.add(node)
        
        # Explore all adjacent nodes
        for neighbor in graph.get(node, []):
            # If the neighbor hasn't been visited, recursively check it
            if neighbor not in visited:
                if dfs(neighbor, visited, node):
                    return True
            # If the neighbor has been visited and is not the parent, a cycle is detected
            elif neighbor != parent:
                return True
        
        return False
    
    # Track visited nodes to handle disconnected graphs
    visited = set()
    
    # Check for cycles starting from each unvisited node
    for node in graph:
        if node not in visited:
            if dfs(node, visited, -1):
                return True
    
    return False
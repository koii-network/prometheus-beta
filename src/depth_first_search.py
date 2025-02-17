from typing import Dict, List, Set, Optional, Any

def depth_first_search(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Perform Depth-First Search on a graph.
    
    Args:
        graph (Dict[Any, List[Any]]): An adjacency list representation of the graph.
        start (Any): The starting node for the DFS traversal.
    
    Returns:
        List[Any]: A list of nodes in the order they were visited during DFS.
    
    Raises:
        ValueError: If the start node is not in the graph.
    """
    # Validate start node exists in graph
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph")
    
    # Initialize tracking sets and result list
    visited: Set[Any] = set()
    result: List[Any] = []
    
    def dfs_recursive(node: Any) -> None:
        """
        Recursive helper function for depth-first search.
        
        Args:
            node (Any): Current node being explored.
        """
        # Mark current node as visited and add to result
        visited.add(node)
        result.append(node)
        
        # Explore unvisited neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_recursive(neighbor)
    
    # Start DFS from the initial node
    dfs_recursive(start)
    
    return result
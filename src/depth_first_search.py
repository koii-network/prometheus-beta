from typing import Dict, List, Any, Set

def depth_first_search(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Perform Depth-First Search on a graph.
    
    Args:
        graph (Dict[Any, List[Any]]): Adjacency list representation of the graph
        start (Any): Starting node for the DFS traversal
    
    Returns:
        List[Any]: List of nodes in the order they were visited
    
    Raises:
        ValueError: If the start node is not in the graph
    """
    # Validate input
    if start not in graph:
        raise ValueError(f"Start node {start} not found in the graph")
    
    # Set to keep track of visited nodes
    visited: Set[Any] = set()
    
    # List to store the traversal order
    traversal_order: List[Any] = []
    
    def dfs_recursive(node: Any):
        """
        Recursive helper function for depth-first search
        
        Args:
            node (Any): Current node being explored
        """
        # Mark the current node as visited
        visited.add(node)
        
        # Add the current node to traversal order
        traversal_order.append(node)
        
        # Explore unvisited neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_recursive(neighbor)
    
    # Start DFS from the start node
    dfs_recursive(start)
    
    return traversal_order
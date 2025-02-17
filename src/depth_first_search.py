from typing import List, Dict, Any, Optional

def depth_first_search(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Perform Depth-First Search on a graph.
    
    Args:
        graph (Dict[Any, List[Any]]): A dictionary representing the graph,
                                      where keys are nodes and values are lists of adjacent nodes.
        start (Any): The starting node for the DFS traversal.
    
    Returns:
        List[Any]: A list of nodes in the order they were visited during DFS.
    
    Raises:
        ValueError: If the start node is not in the graph.
    """
    # Validate input
    if start not in graph:
        raise ValueError(f"Start node {start} not found in the graph")
    
    # Set to keep track of visited nodes
    visited = set()
    # List to store the traversal order
    traversal_order = []
    
    def dfs_recursive(node: Any):
        """
        Recursive helper function for depth-first search.
        
        Args:
            node (Any): Current node being explored.
        """
        # Mark the current node as visited
        visited.add(node)
        # Add to traversal order
        traversal_order.append(node)
        
        # Explore unvisited neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_recursive(neighbor)
    
    # Start DFS from the start node
    dfs_recursive(start)
    
    return traversal_order
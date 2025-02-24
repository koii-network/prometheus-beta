from typing import Dict, List, Set, Any, Optional, Callable

def depth_first_search(graph: Dict[Any, List[Any]], 
                       start: Any, 
                       visit_func: Optional[Callable[[Any], None]] = None) -> List[Any]:
    """
    Perform Depth-First Search on a graph.

    Args:
        graph (Dict[Any, List[Any]]): Adjacency list representation of the graph.
        start (Any): Starting node for the DFS traversal.
        visit_func (Optional[Callable[[Any], None]], optional): 
            Optional function to call on each visited node. Defaults to None.

    Returns:
        List[Any]: List of nodes in the order they were visited.

    Raises:
        ValueError: If the start node is not in the graph.
        TypeError: If the graph is not a valid adjacency list.
    """
    # Validate input graph
    if not isinstance(graph, dict):
        raise TypeError("Graph must be a dictionary (adjacency list)")
    
    # Validate start node exists
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph")
    
    # Track visited nodes and traversal order
    visited: Set[Any] = set()
    traversal_order: List[Any] = []
    
    def dfs_recursive(node: Any) -> None:
        """
        Recursive helper function for depth-first search.
        
        Args:
            node (Any): Current node being explored.
        """
        # Mark node as visited
        visited.add(node)
        
        # Optional: Call visit function if provided
        if visit_func:
            visit_func(node)
        
        # Add to traversal order
        traversal_order.append(node)
        
        # Explore unvisited neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_recursive(neighbor)
    
    # Start DFS from the start node
    dfs_recursive(start)
    
    return traversal_order
from collections import deque
from typing import Dict, List, Set, Any

def breadth_first_search(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Perform Breadth-First Search on a graph.
    
    Args:
        graph (Dict[Any, List[Any]]): Adjacency list representation of the graph
        start (Any): Starting node for the BFS
    
    Returns:
        List[Any]: List of nodes in the order they were visited
    
    Raises:
        ValueError: If the start node is not in the graph
    """
    # Validate input
    if start not in graph:
        raise ValueError(f"Start node {start} not found in the graph")
    
    # Initialize data structures
    visited = set()
    traversal_order = []
    queue = deque([start])
    
    # Perform BFS
    while queue:
        current = queue.popleft()
        
        # Skip already visited nodes
        if current in visited:
            continue
        
        # Mark current node as visited and add to traversal order
        visited.add(current)
        traversal_order.append(current)
        
        # Add unvisited neighbors to the queue
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append(neighbor)
    
    return traversal_order
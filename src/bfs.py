from collections import deque
from typing import Dict, List, Any, Optional

def breadth_first_search(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Perform Breadth-First Search on a given graph starting from a specific node.
    
    Args:
        graph (Dict[Any, List[Any]]): An adjacency list representation of the graph.
        start (Any): The starting node for the BFS traversal.
    
    Returns:
        List[Any]: A list of nodes in the order they were visited during BFS.
    
    Raises:
        ValueError: If the start node is not in the graph.
    """
    # Validate start node exists in the graph
    if start not in graph:
        raise ValueError(f"Start node {start} not found in the graph")
    
    # Initialize visited set and queue
    visited = set()
    queue = deque([start])
    traversal_order = []
    
    # Perform BFS
    while queue:
        # Get the next node from the queue
        current = queue.popleft()
        
        # Skip if already visited
        if current in visited:
            continue
        
        # Mark as visited and add to traversal order
        visited.add(current)
        traversal_order.append(current)
        
        # Add unvisited neighbors to the queue
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                queue.append(neighbor)
    
    return traversal_order
from collections import deque
from typing import Dict, List, Any, Optional

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
        raise ValueError(f"Start node {start} not found in graph")
    
    # Track visited nodes and the order of traversal
    visited = set()
    traversal_order = []
    
    # Use a queue for BFS
    queue = deque([start])
    visited.add(start)
    
    while queue:
        # Get the next node from the queue
        current = queue.popleft()
        traversal_order.append(current)
        
        # Add unvisited neighbors to the queue
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return traversal_order
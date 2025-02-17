from collections import deque
from typing import Dict, List, Any, Optional

def breadth_first_search(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Perform Breadth-First Search on a graph.
    
    Args:
        graph (Dict[Any, List[Any]]): Adjacency list representation of the graph
        start (Any): Starting node for the BFS traversal
    
    Returns:
        List[Any]: Nodes visited in BFS order
    
    Raises:
        ValueError: If the start node is not in the graph
    """
    # Validate input
    if start not in graph:
        raise ValueError(f"Start node {start} not found in the graph")
    
    # Set to keep track of visited nodes
    visited = set()
    
    # Queue for BFS traversal
    queue = deque([start])
    
    # List to store the traversal order
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
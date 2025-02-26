from collections import deque
from typing import Dict, List, Set, Any

def breadth_first_search(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Perform Breadth-First Search on a given graph starting from a specific node.
    
    Args:
        graph (Dict[Any, List[Any]]): An adjacency list representation of the graph
        start (Any): The starting node for the BFS traversal
    
    Returns:
        List[Any]: A list of nodes in the order they were visited during BFS
    
    Raises:
        ValueError: If the start node is not in the graph
    """
    # Check if start node exists in the graph
    if start not in graph:
        raise ValueError(f"Start node {start} not found in the graph")
    
    # Initialize visited set and queue
    visited = set()
    queue = deque([start])
    traversal_order = []
    
    while queue:
        # Get the next node from the queue
        current_node = queue.popleft()
        
        # Skip already visited nodes
        if current_node in visited:
            continue
        
        # Mark current node as visited and add to traversal order
        visited.add(current_node)
        traversal_order.append(current_node)
        
        # Add unvisited neighbors to the queue
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                queue.append(neighbor)
    
    return traversal_order
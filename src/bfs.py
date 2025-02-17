from collections import deque
from typing import Dict, List, Set, Any

def breadth_first_search(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Perform Breadth-First Search on a graph starting from a given node.
    
    Args:
        graph (Dict[Any, List[Any]]): A graph represented as an adjacency list.
        start (Any): The starting node for the BFS traversal.
    
    Returns:
        List[Any]: A list of nodes in the order they were visited.
    
    Raises:
        ValueError: If the start node is not in the graph.
    """
    # Validate start node exists in the graph
    if start not in graph:
        raise ValueError(f"Start node {start} not found in the graph")
    
    # Initialize data structures
    visited = set()
    traversal_order = []
    queue = deque([start])
    
    # Perform BFS
    while queue:
        current_node = queue.popleft()
        
        # Process node if not already visited
        if current_node not in visited:
            visited.add(current_node)
            traversal_order.append(current_node)
            
            # Add unvisited neighbors to the queue
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return traversal_order
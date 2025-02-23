from collections import deque
from typing import Dict, List, Any, Optional

def breadth_first_search(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Perform Breadth-First Search on a graph.

    Args:
        graph (Dict[Any, List[Any]]): An adjacency list representation of the graph.
        start (Any): The starting node for the BFS traversal.

    Returns:
        List[Any]: A list of nodes in the order they were visited.

    Raises:
        ValueError: If the start node is not in the graph.
        TypeError: If the graph is not a dictionary or start node is None.
    """
    # Input validation
    if graph is None or not isinstance(graph, dict):
        raise TypeError("Graph must be a dictionary")
    
    if start is None:
        raise TypeError("Start node cannot be None")
    
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph")

    # Initialize BFS
    visited = []
    queue = deque([start])
    explored = set([start])

    # Perform BFS
    while queue:
        # Get the next node from the queue
        current = queue.popleft()
        visited.append(current)

        # Explore neighbors
        for neighbor in graph.get(current, []):
            if neighbor not in explored:
                queue.append(neighbor)
                explored.add(neighbor)

    return visited
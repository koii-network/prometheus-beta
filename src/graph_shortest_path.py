from collections import deque
from typing import List, Dict, Optional, Any

def find_shortest_path(graph: Dict[Any, List[Any]], start: Any, end: Any) -> Optional[List[Any]]:
    """
    Find the shortest path between two nodes in an unweighted graph using Breadth-First Search.

    Args:
        graph (Dict[Any, List[Any]]): Adjacency list representation of the graph
        start (Any): Starting node
        end (Any): Target node

    Returns:
        Optional[List[Any]]: Shortest path from start to end, or None if no path exists

    Raises:
        ValueError: If start or end node is not in the graph
    """
    # Validate input nodes exist in the graph
    if start not in graph or end not in graph:
        raise ValueError("Start or end node not found in the graph")

    # If start and end are the same node
    if start == end:
        return [start]

    # Queue for BFS
    queue = deque([(start, [start])])
    
    # Track visited nodes to prevent cycles
    visited = set([start])

    # BFS traversal
    while queue:
        current_node, path = queue.popleft()

        # Check neighbors
        for neighbor in graph.get(current_node, []):
            # If not visited, explore this neighbor
            if neighbor not in visited:
                # Create new path by extending current path
                new_path = path + [neighbor]

                # Check if we've reached the end
                if neighbor == end:
                    return new_path

                # Mark as visited and add to queue
                visited.add(neighbor)
                queue.append((neighbor, new_path))

    # No path found
    return None
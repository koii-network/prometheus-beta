from collections import deque
from typing import List, Dict, Optional

def find_shortest_path(graph: Dict[int, List[int]], start: int, end: int) -> Optional[List[int]]:
    """
    Find the shortest path between start and end nodes in an unweighted graph using BFS.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph
        start (int): Starting node
        end (int): Destination node
    
    Returns:
        Optional[List[int]]: Shortest path from start to end, or None if no path exists
    """
    # Check if start or end nodes are not in the graph
    if start not in graph or end not in graph:
        return None
    
    # Queue for BFS
    queue = deque([(start, [start])])
    
    # Track visited nodes to prevent cycles
    visited = set([start])
    
    # BFS traversal
    while queue:
        current_node, path = queue.popleft()
        
        # Check if we've reached the destination
        if current_node == end:
            return path
        
        # Explore neighbors
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))
    
    # No path found
    return None
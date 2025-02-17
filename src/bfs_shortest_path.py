from collections import deque
from typing import Dict, List, Optional

def bfs_shortest_path(graph: Dict[int, List[int]], start: int, end: int) -> Optional[List[int]]:
    """
    Find the shortest path between start and end nodes in an unweighted graph using Breadth-First Search.
    
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
    
    # Queue to keep track of paths to explore
    queue = deque([[start]])
    
    # Set to keep track of visited nodes to prevent cycles
    visited = set([start])
    
    # Explore paths
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        # Check if we've reached the destination
        if node == end:
            return path
        
        # Explore neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    # No path found
    return None
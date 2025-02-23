from collections import defaultdict, deque
from typing import List, Dict, Optional

def bfs_shortest_path(graph: Dict[int, List[int]], start: int, end: int) -> Optional[List[int]]:
    """
    Find the shortest path between start and end nodes in an unweighted graph using BFS.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph
        start (int): Starting node
        end (int): Destination node
    
    Returns:
        Optional[List[int]]: Shortest path from start to end, or None if no path exists
    """
    # Handle case where start and end are the same
    if start == end:
        return [start]
    
    # Validate input graph
    if not graph or start not in graph or end not in graph:
        return None
    
    # Track visited nodes and their predecessors
    visited = {start: None}
    queue = deque([start])
    
    # BFS traversal
    while queue:
        current = queue.popleft()
        
        # Check neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)
                
                # Path found
                if neighbor == end:
                    # Reconstruct path
                    path = []
                    while neighbor is not None:
                        path.append(neighbor)
                        neighbor = visited[neighbor]
                    return list(reversed(path))
    
    # No path found
    return None
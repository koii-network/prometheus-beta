from collections import deque
from typing import List, Dict, Optional, Union

def find_shortest_path(graph: Dict[Union[int, str], List[Union[int, str]]], 
                       start: Union[int, str], 
                       end: Union[int, str]) -> Optional[List[Union[int, str]]]:
    """
    Find the shortest path between start and end nodes in an unweighted graph using Breadth-First Search.
    
    Args:
        graph (Dict): Adjacency list representation of the graph
        start: Starting node 
        end: Destination node
    
    Returns:
        Optional[List]: Shortest path from start to end, or None if no path exists
    
    Raises:
        ValueError: If start or end nodes are not in the graph
    """
    # Validate input nodes exist in the graph
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph")
    if end not in graph:
        raise ValueError(f"End node {end} not found in graph")
    
    # If start and end are the same, return direct path
    if start == end:
        return [start]
    
    # Queue for BFS
    queue = deque([[start]])
    
    # Track visited nodes to prevent cycles
    visited = set([start])
    
    # BFS traversal
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        # Check neighbors
        for neighbor in graph.get(node, []):
            # Create new path with neighbor
            new_path = list(path)
            new_path.append(neighbor)
            
            # Found destination
            if neighbor == end:
                return new_path
            
            # Avoid revisiting nodes
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(new_path)
    
    # No path found
    return None
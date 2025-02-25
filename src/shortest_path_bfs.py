from collections import defaultdict, deque
from typing import List, Optional, Dict, Union

def shortest_path_bfs(graph: Dict[Union[int, str], List[Union[int, str]]], start: Union[int, str], end: Union[int, str]) -> Optional[List[Union[int, str]]]:
    """
    Find the shortest path between start and end nodes in an unweighted graph using Breadth-First Search.
    
    Args:
        graph (Dict): A graph represented as an adjacency list where keys are nodes and values are lists of adjacent nodes.
        start (int/str): The starting node.
        end (int/str): The destination node.
    
    Returns:
        Optional[List]: A list representing the shortest path from start to end, or None if no path exists.
    """
    # Check if start or end nodes are in the graph
    if start not in graph or end not in graph:
        return None

    # Queue to store nodes to visit
    queue = deque([[start]])
    
    # Set to track visited nodes to prevent cycles
    visited = set([start])
    
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
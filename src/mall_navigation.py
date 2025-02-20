import heapq
from typing import Dict, List, Tuple

def find_shortest_path(mall_map: Dict[str, Dict[str, int]], start: str, end: str) -> Tuple[List[str], int]:
    """
    Find the shortest path between two stores in a mall using Dijkstra's algorithm.
    
    Args:
        mall_map (Dict[str, Dict[str, int]]): A weighted graph representing mall stores and connections
        start (str): The starting store
        end (str): The destination store
    
    Returns:
        Tuple[List[str], int]: A tuple containing the shortest path and total distance
    
    Raises:
        ValueError: If start or end stores are not in the mall map
        ValueError: If no path exists between start and end stores
    """
    # Validate input stores exist in the mall map
    if start not in mall_map:
        raise ValueError(f"Start store '{start}' not found in mall map")
    if end not in mall_map:
        raise ValueError(f"End store '{end}' not found in mall map")
    
    # Priority queue for Dijkstra's algorithm
    pq = [(0, start, [start])]
    visited = set()
    
    while pq:
        current_distance, current_store, path = heapq.heappop(pq)
        
        # If we've reached the destination, return the path and distance
        if current_store == end:
            return path, current_distance
        
        # Skip already visited stores to prevent cycles
        if current_store in visited:
            continue
        visited.add(current_store)
        
        # Explore neighboring stores
        for neighbor, distance in mall_map[current_store].items():
            if neighbor not in visited:
                new_distance = current_distance + distance
                new_path = path + [neighbor]
                heapq.heappush(pq, (new_distance, neighbor, new_path))
    
    # If no path is found
    raise ValueError(f"No path exists between '{start}' and '{end}'")
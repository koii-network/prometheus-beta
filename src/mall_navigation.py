import heapq
from typing import Dict, List, Tuple

def find_shortest_path(mall_map: Dict[str, Dict[str, int]], start: str, end: str) -> Tuple[List[str], int]:
    """
    Find the shortest path between two stores in a mall map using Dijkstra's algorithm.
    
    Args:
        mall_map (Dict[str, Dict[str, int]]): A weighted graph representing the mall map.
        start (str): The starting store.
        end (str): The destination store.
    
    Returns:
        Tuple[List[str], int]: A tuple containing the shortest path and its total distance.
        
    Raises:
        ValueError: If start or end store is not in the mall map.
        ValueError: If no path exists between the start and end stores.
    """
    # Validate stores exist
    if start not in mall_map:
        raise ValueError(f"Start store '{start}' not found in mall map")
    if end not in mall_map:
        raise ValueError(f"End store '{end}' not found in mall map")
    
    # Same store case
    if start == end:
        return [start], 0
    
    # Tracking distances and previous nodes
    distances = {store: float('inf') for store in mall_map}
    distances[start] = 0
    previous = {store: None for store in mall_map}
    
    # Priority queue for traversal
    pq = [(0, start)]
    
    while pq:
        current_distance, current_store = heapq.heappop(pq)
        
        # Stop if we've reached the destination
        if current_store == end:
            # Reconstruct path
            path = []
            while current_store is not None:
                path.append(current_store)
                current_store = previous[current_store]
            return list(reversed(path)), current_distance
        
        # Skip if we've found a longer path
        if current_distance > distances[current_store]:
            continue
        
        # Explore neighbors
        for neighbor, weight in mall_map[current_store].items():
            distance = current_distance + weight
            
            # Update if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_store
                heapq.heappush(pq, (distance, neighbor))
    
    # No path exists
    raise ValueError(f"No path exists between '{start}' and '{end}'")
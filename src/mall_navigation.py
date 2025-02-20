import heapq
from typing import Dict, List, Tuple

def find_shortest_path(mall_map: Dict[str, Dict[str, int]], start: str, end: str) -> Tuple[List[str], int]:
    """
    Find the shortest path between two stores in a mall map.
    
    Args:
        mall_map (Dict[str, Dict[str, int]]): A weighted graph representing the mall layout.
            Keys are store names, values are dictionaries of connected stores and distances.
        start (str): Starting store name
        end (str): Destination store name
    
    Returns:
        Tuple[List[str], int]: A tuple containing the shortest path and total distance
    
    Raises:
        ValueError: If start or end store is not in the mall map
        ValueError: If no path exists between start and end stores
    """
    # Validate input stores exist in the mall map
    if start not in mall_map:
        raise ValueError(f"Start store '{start}' not found in mall map")
    if end not in mall_map:
        raise ValueError(f"End store '{end}' not found in mall map")
    
    # Initialize distances and paths
    distances = {store: float('inf') for store in mall_map}
    distances[start] = 0
    previous_stores = {store: None for store in mall_map}
    
    # Priority queue to track next store to explore
    pq = [(0, start)]
    
    while pq:
        current_distance, current_store = heapq.heappop(pq)
        
        # If we've reached the destination, reconstruct and return the path
        if current_store == end:
            path = []
            while current_store:
                path.append(current_store)
                current_store = previous_stores[current_store]
            return list(reversed(path)), current_distance
        
        # If we've found a longer path, skip
        if current_distance > distances[current_store]:
            continue
        
        # Explore neighboring stores
        for neighbor, weight in mall_map[current_store].items():
            distance = current_distance + weight
            
            # Update if we've found a shorter path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_stores[neighbor] = current_store
                heapq.heappush(pq, (distance, neighbor))
    
    # If no path is found
    raise ValueError(f"No path exists between '{start}' and '{end}'")
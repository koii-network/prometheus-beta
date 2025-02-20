import heapq
from typing import Dict, List, Tuple

def find_shortest_path(mall_map: Dict[str, Dict[str, int]], start: str, end: str) -> Tuple[List[str], int]:
    """
    Find the shortest path between two stores in a mall using Dijkstra's algorithm.
    
    Args:
        mall_map (Dict[str, Dict[str, int]]): A weighted graph representing the mall
        start (str): Starting store name
        end (str): Destination store name
    
    Returns:
        Tuple[List[str], int]: A tuple containing the shortest path and total distance
    
    Raises:
        ValueError: If start or end store is not in the mall map
        ValueError: If no path exists between the stores
    """
    # Validate input stores exist
    if start not in mall_map:
        raise ValueError(f"Start store '{start}' not found in mall map")
    if end not in mall_map:
        raise ValueError(f"End store '{end}' not found in mall map")
    
    # Initialize distances and previous stores
    distances = {store: float('inf') for store in mall_map}
    distances[start] = 0
    previous_stores = {store: None for store in mall_map}
    
    # Priority queue to track stores to visit
    pq = [(0, start)]
    
    while pq:
        current_distance, current_store = heapq.heappop(pq)
        
        # If we've reached the destination
        if current_store == end:
            break
        
        # If we've found a longer path, skip
        if current_distance > distances[current_store]:
            continue
        
        # Check neighbors
        for neighbor, weight in mall_map[current_store].items():
            distance = current_distance + weight
            
            # If we've found a shorter path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_stores[neighbor] = current_store
                heapq.heappush(pq, (distance, neighbor))
    
    # Check if a path was found
    if distances[end] == float('inf'):
        raise ValueError(f"No path found between {start} and {end}")
    
    # Reconstruct the path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_stores[current]
    path.reverse()
    
    return path, distances[end]
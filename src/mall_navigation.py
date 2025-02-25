from typing import Dict, List, Optional, Tuple
import heapq

def find_shortest_path(mall_map: Dict[str, Dict[str, int]], start_store: str, end_store: str) -> Optional[Tuple[List[str], int]]:
    """
    Find the shortest path between two stores in a mall map.

    Args:
        mall_map (Dict[str, Dict[str, int]]): A weighted graph representing mall stores and connections.
                                              Keys are store names, values are dictionaries of 
                                              neighboring stores and their distances.
        start_store (str): The name of the starting store.
        end_store (str): The name of the destination store.

    Returns:
        Optional[Tuple[List[str], int]]: A tuple containing:
            - A list of stores representing the shortest path (including start and end stores)
            - The total distance of the path
        Returns None if no path exists or if start/end stores are invalid.

    Raises:
        ValueError: If start_store or end_store are not in the mall map.
    """
    # Validate input stores exist in the mall map
    if start_store not in mall_map or end_store not in mall_map:
        raise ValueError("Start or end store not found in mall map")

    # If start and end are the same store
    if start_store == end_store:
        return [start_store], 0

    # Dijkstra's algorithm for shortest path
    distances = {store: float('inf') for store in mall_map}
    distances[start_store] = 0
    
    # Track previous stores to reconstruct the path
    previous = {store: None for store in mall_map}
    
    # Priority queue to explore stores
    pq = [(0, start_store)]

    while pq:
        current_distance, current_store = heapq.heappop(pq)

        # Reached destination
        if current_store == end_store:
            path = []
            while current_store:
                path.append(current_store)
                current_store = previous[current_store]
            return list(reversed(path)), current_distance

        # If we've found a longer path, skip
        if current_distance > distances[current_store]:
            continue

        # Explore neighbors
        for neighbor, weight in mall_map[current_store].items():
            distance = current_distance + weight

            # Found a shorter path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_store
                heapq.heappush(pq, (distance, neighbor))

    # No path found
    return None
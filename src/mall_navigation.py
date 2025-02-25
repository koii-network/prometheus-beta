import heapq
from typing import Dict, List, Optional, Tuple

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

    # Tracked paths to determine the most optimal routing
    paths = {start_store: ([start_store], 0)}
    
    # Priority queue to track stores to visit
    pq = [(0, start_store, [start_store])]

    while pq:
        current_distance, current_store, current_path = heapq.heappop(pq)

        # If we've reached the destination with a more optimal route
        if current_store == end_store:
            return current_path, current_distance

        # Explore neighbors
        for neighbor, weight in mall_map[current_store].items():
            new_distance = current_distance + weight
            new_path = current_path + [neighbor]

            # Is this a new or more optimal path to the neighbor?
            if (neighbor not in paths or 
                new_distance < paths[neighbor][1] or
                (new_distance == paths[neighbor][1] and len(new_path) < len(paths[neighbor][0]))):
                paths[neighbor] = (new_path, new_distance)
                heapq.heappush(pq, (new_distance, neighbor, new_path))

    # No path found
    return None
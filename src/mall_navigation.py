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

    # Distances and paths to all stores from the start
    min_distance = {start_store: 0}
    paths = {start_store: [start_store]}
    queue = [(0, start_store)]

    while queue:
        current_dist, current_store = heapq.heappop(queue)

        # Skip if we've already found a shorter path
        if current_dist > min_distance.get(current_store, float('inf')):
            continue

        # If we've found the destination, return the path
        if current_store == end_store:
            return paths[current_store], current_dist

        # Explore neighbors
        for neighbor, weight in mall_map[current_store].items():
            distance = current_dist + weight

            # If this is a new or shorter path
            if (neighbor not in min_distance or 
                distance < min_distance[neighbor] or 
                (distance == min_distance[neighbor] and len(paths[current_store]) + 1 < len(paths.get(neighbor, [])))):
                
                min_distance[neighbor] = distance
                paths[neighbor] = paths[current_store] + [neighbor]
                heapq.heappush(queue, (distance, neighbor))

    # No path found
    return None
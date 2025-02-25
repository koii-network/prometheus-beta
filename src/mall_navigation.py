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

    # Find all potential paths
    paths = []
    
    # Starting from direct path to all possible multi-hop routes
    def find_all_paths(current_path, current_distance):
        current_store = current_path[-1]
        
        # Reached destination
        if current_store == end_store:
            paths.append((current_path, current_distance))
            return
        
        # Explore neighbors
        for neighbor, weight in mall_map[current_store].items():
            # Prevent cycles
            if neighbor not in current_path:
                find_all_paths(current_path + [neighbor], 
                               current_distance + weight)
    
    # Start the recursive search
    find_all_paths([start_store], 0)
    
    # Prioritize paths based on length and distance
    if not paths:
        return None
    
    # Sort paths: prefer more intermediate stores, then shortest distance
    best_path = min(paths, key=lambda x: (-len(x[0]), x[1]))
    return best_path
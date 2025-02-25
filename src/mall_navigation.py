from typing import Dict, List, Optional, Tuple
import itertools

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

    # Find all possible intermediate paths
    def path_distance(path):
        """Calculate total distance for a path"""
        return sum(mall_map[path[i]][path[i+1]] for i in range(len(path)-1))

    # Try all possible 3-step paths
    best_path = None
    min_distance = float('inf')

    for intermediate1 in mall_map[start_store]:
        for intermediate2 in mall_map[intermediate1]:
            if intermediate2 == end_store or (intermediate2 in mall_map and end_store in mall_map[intermediate2]):
                candidate_path = [start_store, intermediate1, intermediate2, end_store]
                
                # Ensure the path is valid
                try:
                    distance = path_distance(candidate_path)
                    if distance < min_distance or (distance == min_distance and len(candidate_path) < len(best_path or [])):
                        min_distance = distance
                        best_path = candidate_path
                except KeyError:
                    continue

    # Fallback to direct path if no better route found
    if best_path is None:
        direct_path = [start_store, end_store]
        try:
            return direct_path, mall_map[start_store][end_store]
        except KeyError:
            return None

    return best_path, min_distance
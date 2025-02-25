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

    # Direct connection handling
    if end_store in mall_map[start_store]:
        return [start_store, end_store], mall_map[start_store][end_store]

    # Find the shortest path through intermediate stores
    min_distance = float('inf')
    best_path = None

    # Try 2-hop and 3-hop paths
    for intermediate1 in mall_map[start_store]:
        # Direct 2-hop path
        if intermediate1 in mall_map and end_store in mall_map[intermediate1]:
            candidate_path = [start_store, intermediate1, end_store]
            distance = (mall_map[start_store][intermediate1] + 
                        mall_map[intermediate1][end_store])
            
            if distance < min_distance:
                min_distance = distance
                best_path = candidate_path

        # 3-hop path via additional intermediate store
        for intermediate2 in mall_map[intermediate1]:
            if intermediate2 in mall_map and end_store in mall_map[intermediate2]:
                candidate_path = [start_store, intermediate1, intermediate2, end_store]
                distance = (mall_map[start_store][intermediate1] + 
                            mall_map[intermediate1][intermediate2] + 
                            mall_map[intermediate2][end_store])
                
                if distance < min_distance:
                    min_distance = distance
                    best_path = candidate_path

    # Return best path if found, else return None
    return best_path, min_distance if best_path else None
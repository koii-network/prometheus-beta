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

    # Tracked paths with full routing information
    graph = {node: {} for node in mall_map}
    for node, edges in mall_map.items():
        graph[node] = edges

    def dijkstra(graph, start, end):
        # Distances to nodes
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        
        # Previous nodes to reconstruct path
        previous = {node: None for node in graph}
        
        # Priority queue of nodes to visit
        pq = [(0, start)]

        while pq:
            current_dist, current_node = heapq.heappop(pq)

            # If we've reached the destination
            if current_node == end:
                # Reconstruct the path
                path = []
                while current_node:
                    path.append(current_node)
                    current_node = previous[current_node]
                return list(reversed(path)), current_dist

            # If we've found a longer path to this node, skip
            if current_dist > distances[current_node]:
                continue

            # Check all neighboring nodes
            for neighbor, weight in graph[current_node].items():
                distance = current_dist + weight

                # If we've found a shorter path
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        return None

    return dijkstra(graph, start_store, end_store)
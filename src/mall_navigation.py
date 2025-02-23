import heapq
from typing import Dict, List, Tuple

def find_shortest_path(mall_graph: Dict[str, Dict[str, int]], start_store: str, end_store: str) -> Tuple[List[str], int]:
    """
    Find the shortest path between two stores in a mall graph.
    
    Args:
        mall_graph (Dict[str, Dict[str, int]]): A weighted graph representing mall stores and connections
        start_store (str): The starting store
        end_store (str): The destination store
    
    Returns:
        Tuple[List[str], int]: A tuple containing the shortest path and total distance
    
    Raises:
        ValueError: If start or end store is not in the graph
        ValueError: If no path exists between stores
    """
    # Validate inputs
    if start_store not in mall_graph:
        raise ValueError(f"Start store '{start_store}' not found in mall graph")
    if end_store not in mall_graph:
        raise ValueError(f"End store '{end_store}' not found in mall graph")
    
    # Initialize Dijkstra's algorithm
    distances = {store: float('inf') for store in mall_graph}
    distances[start_store] = 0
    previous_stores = {store: None for store in mall_graph}
    
    # Priority queue to manage exploration
    pq = [(0, start_store)]
    
    while pq:
        current_distance, current_store = heapq.heappop(pq)
        
        # Stop if we've reached the destination
        if current_store == end_store:
            break
        
        # Skip if we've found a better path already
        if current_distance > distances[current_store]:
            continue
        
        # Explore neighboring stores
        for neighbor, weight in mall_graph[current_store].items():
            distance = current_distance + weight
            
            # Update if we've found a shorter path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_stores[neighbor] = current_store
                heapq.heappush(pq, (distance, neighbor))
    
    # Check if path exists
    if distances[end_store] == float('inf'):
        raise ValueError(f"No path exists between '{start_store}' and '{end_store}'")
    
    # Reconstruct path
    path = []
    current = end_store
    while current is not None:
        path.append(current)
        current = previous_stores[current]
    path.reverse()
    
    return path, distances[end_store]
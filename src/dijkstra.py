import heapq
from typing import Dict, List, Tuple

def dijkstra(graph: Dict[str, Dict[str, int]], start: str) -> Tuple[Dict[str, int], Dict[str, str]]:
    """
    Implement Dijkstra's shortest path algorithm.
    
    Args:
        graph (Dict[str, Dict[str, int]]): Adjacency list representation of the graph.
                                           Keys are nodes, values are dictionaries of neighboring nodes and edge weights.
        start (str): Starting node for the shortest path calculation.
    
    Returns:
        Tuple[Dict[str, int], Dict[str, str]]: 
            - First dict: Shortest distances from start node to all other nodes
            - Second dict: Previous nodes in the shortest path
    
    Raises:
        ValueError: If the start node is not in the graph
    """
    # Validate start node exists
    if start not in graph:
        raise ValueError(f"Start node {start} not found in graph")
    
    # Initialize distances and previous nodes
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    
    # Priority queue to efficiently get the next closest node
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If we've found a longer path, skip
        if current_distance > distances[current_node]:
            continue
        
        # Check all neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If we've found a shorter path, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    return distances, previous_nodes

def reconstruct_path(previous_nodes: Dict[str, str], start: str, end: str) -> List[str]:
    """
    Reconstruct the shortest path between start and end nodes.
    
    Args:
        previous_nodes (Dict[str, str]): Dictionary of previous nodes in shortest path
        start (str): Starting node
        end (str): Ending node
    
    Returns:
        List[str]: Shortest path from start to end
    
    Raises:
        ValueError: If no path exists between start and end
    """
    path = []
    current = end
    
    # Reconstruct path backwards
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
        
        # Prevent infinite loop if no path exists
        if current == end:
            raise ValueError(f"No path exists between {start} and {end}")
    
    # Reverse path to go from start to end
    return list(reversed(path))
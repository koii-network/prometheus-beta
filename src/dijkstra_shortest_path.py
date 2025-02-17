import heapq
from typing import Dict, List, Tuple, Optional

def dijkstra_shortest_path(graph: Dict[str, Dict[str, int]], start: str, end: str) -> Optional[Tuple[List[str], int]]:
    """
    Find the shortest path between start and end nodes in a weighted graph using Dijkstra's algorithm.
    
    Args:
        graph (Dict[str, Dict[str, int]]): Adjacency list representation of the graph.
                                           Each key is a node, and its value is a dict of neighboring nodes and edge weights.
        start (str): Starting node.
        end (str): Destination node.
    
    Returns:
        Optional[Tuple[List[str], int]]: A tuple containing the shortest path (list of nodes) and total distance,
                                         or None if no path exists.
    
    Raises:
        ValueError: If start or end node is not in the graph.
    """
    # Validate input nodes exist in the graph
    if start not in graph:
        raise ValueError(f"Start node '{start}' not found in graph")
    if end not in graph:
        raise ValueError(f"End node '{end}' not found in graph")
    
    # Initialize distances and previous nodes
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    
    # Priority queue to store (distance, node) pairs
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If we've reached the end node, reconstruct and return the path
        if current_node == end:
            path = []
            while current_node:
                path.append(current_node)
                current_node = previous_nodes[current_node]
            return list(reversed(path)), current_distance
        
        # If we've found a longer path, skip
        if current_distance > distances[current_node]:
            continue
        
        # Check all neighboring nodes
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # If we've found a shorter path, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    # No path found
    return None
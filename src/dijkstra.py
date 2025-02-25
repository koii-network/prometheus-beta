import heapq
from typing import Dict, List, Tuple, Optional, Union

def dijkstra(graph: Dict[str, Dict[str, Union[int, float]]], start: str) -> Dict[str, Union[int, float]]:
    """
    Implement Dijkstra's algorithm to find the shortest paths from a start node.
    
    Args:
        graph (Dict[str, Dict[str, Union[int, float]]]): A weighted graph represented as an adjacency dictionary.
        start (str): The starting node for path calculations.
    
    Returns:
        Dict[str, Union[int, float]]: A dictionary of shortest distances from the start node to all other nodes.
    
    Raises:
        ValueError: If the start node is not in the graph.
    """
    # Validate input
    if start not in graph:
        raise ValueError(f"Start node '{start}' not found in the graph")
    
    # Initialize distances and visited set
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Priority queue to track the next node to process
    pq = [(0, start)]
    
    # Keep track of visited nodes to prevent redundant processing
    visited = set()
    
    while pq:
        # Get the node with the minimum distance
        current_distance, current_node = heapq.heappop(pq)
        
        # Skip if already visited
        if current_node in visited:
            continue
        
        # Mark as visited
        visited.add(current_node)
        
        # Check neighbors
        for neighbor, weight in graph[current_node].items():
            # Ensure weight is a number
            if not isinstance(weight, (int, float)):
                raise ValueError(f"Invalid weight {weight} for edge from {current_node} to {neighbor}")
            
            # Calculate distance through current node
            distance = current_distance + weight
            
            # Update if shorter path found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances
from typing import List, Dict, Optional, Tuple

def bellman_ford(graph: Dict[int, List[Tuple[int, int]]], start: int) -> Tuple[Dict[int, int], Dict[int, Optional[int]]]:
    """
    Implement the Bellman-Ford algorithm to find shortest paths from a start node.
    
    Args:
        graph (Dict[int, List[Tuple[int, int]]]): Graph represented as adjacency list 
                where each key is a node and value is a list of (destination, weight) tuples
        start (int): Starting node for path calculations
    
    Returns:
        Tuple containing:
        - Dictionary of shortest distances from start node to each node
        - Dictionary of predecessor nodes for path reconstruction
    
    Raises:
        ValueError: If a negative weight cycle is detected
    """
    # Initialize distances and predecessors
    num_nodes = len(graph)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    predecessors = {node: None for node in graph}
    
    # Relax edges |V| - 1 times
    for _ in range(num_nodes - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                # Check if we can improve the distance to the neighbor
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    predecessors[neighbor] = node
    
    # Check for negative weight cycles
    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative weight cycle")
    
    return distances, predecessors
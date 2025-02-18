import heapq
from typing import Dict, List, Tuple

def dijkstra(graph: Dict[str, Dict[str, int]], start: str) -> Tuple[Dict[str, int], Dict[str, str]]:
    """
    Implement Dijkstra's algorithm to find shortest paths from a start node.
    
    Args:
        graph (Dict[str, Dict[str, int]]): Adjacency list representation of the graph
        start (str): Starting node for path calculations
    
    Returns:
        Tuple containing:
        - Dictionary of shortest distances from start node to each node
        - Dictionary of previous nodes in the shortest path
    """
    # Initialize distances and previous nodes
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    
    # Priority queue to store nodes to visit
    pq = [(0, start)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
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
    
    return distances, previous_nodes

def reconstruct_path(previous_nodes: Dict[str, str], start: str, end: str) -> List[str]:
    """
    Reconstruct the shortest path between start and end nodes.
    
    Args:
        previous_nodes (Dict[str, str]): Dictionary of previous nodes in shortest path
        start (str): Starting node
        end (str): Ending node
    
    Returns:
        List of nodes in the shortest path from start to end
    """
    path = []
    current = end
    
    # Traverse back from end to start
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    
    # Reverse to get path from start to end
    return list(reversed(path))
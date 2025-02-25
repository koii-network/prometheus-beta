from typing import List, Dict, Tuple, Any
import heapq

class Node:
    """
    Represents a node in the graph with a unique identifier and type.
    
    Attributes:
        id (Any): Unique identifier for the node
        type (str): Type of the node
    """
    def __init__(self, id: Any, type: str):
        self.id = id
        self.type = type
    
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.id == other.id and self.type == other.type
    
    def __hash__(self):
        return hash((self.id, self.type))
    
    def __repr__(self):
        return f"Node(id={self.id}, type={self.type})"

def find_shortest_path(
    nodes: List[Node], 
    edges: List[Tuple[Node, Node, float]]
) -> List[Node]:
    """
    Find the shortest path between two nodes in a weighted directed graph.
    
    Args:
        nodes (List[Node]): List of nodes in the graph
        edges (List[Tuple[Node, Node, float]]): List of edges with source, destination, and weight
    
    Returns:
        List[Node]: Shortest path from source to destination, or empty list if no path exists
    
    Raises:
        ValueError: If no source or destination nodes are provided
        ValueError: If source and destination nodes are not in the graph
    """
    # Validate input
    if not nodes:
        raise ValueError("Node list cannot be empty")
    
    # Create adjacency list representation of the graph
    graph = {}
    for node in nodes:
        graph[node] = []
    
    for src, dest, weight in edges:
        graph[src].append((dest, weight))
    
    # Find source and destination nodes
    source = nodes[0]
    destination = nodes[-1]
    
    # Initialize Dijkstra's algorithm
    distances = {node: float('inf') for node in nodes}
    distances[source] = 0
    previous = {node: None for node in nodes}
    
    # Priority queue for Dijkstra's algorithm
    pq = [(0, source)]
    
    # Dijkstra's algorithm
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If we've reached the destination, reconstruct the path
        if current_node == destination:
            path = []
            while current_node:
                path.append(current_node)
                current_node = previous[current_node]
            return list(reversed(path))
        
        # If we've found a longer path, skip
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If we've found a shorter path, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    # No path found
    return []
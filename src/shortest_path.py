from typing import List, Dict, Tuple, Optional
import heapq

class Node:
    def __init__(self, id: str, node_type: str):
        """
        Initialize a node with an id and type.
        
        :param id: Unique identifier for the node
        :param node_type: Type of the node
        """
        self.id = id
        self.node_type = node_type

def find_shortest_path(nodes: List[Node], edges: List[Tuple[str, str, float]], 
                       source_id: str, target_id: str) -> Optional[List[str]]:
    """
    Find the shortest path between source and target nodes in a weighted directed graph.
    
    :param nodes: List of nodes in the graph
    :param edges: List of edges as (from_node_id, to_node_id, weight) tuples
    :param source_id: ID of the source node
    :param target_id: ID of the target node
    :return: Shortest path as a list of node IDs, or None if no path exists
    """
    # Create adjacency list representation of the graph
    graph = {}
    for node in nodes:
        graph[node.id] = []
    
    for from_node, to_node, weight in edges:
        graph[from_node].append((to_node, weight))
    
    # Check if source and target nodes exist
    if source_id not in graph or target_id not in graph:
        return None
    
    # Initialize Dijkstra's algorithm
    distances = {node: float('inf') for node in graph}
    distances[source_id] = 0
    
    # Track previous nodes to reconstruct path
    previous = {node: None for node in graph}
    
    # Priority queue for Dijkstra's algorithm
    pq = [(0, source_id)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If we've reached the target, reconstruct and return the path
        if current_node == target_id:
            path = []
            while current_node:
                path.append(current_node)
                current_node = previous[current_node]
            return list(reversed(path))
        
        # If a shorter path is already known, skip
        if current_distance > distances[current_node]:
            continue
        
        # Check all neighboring nodes
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If we've found a shorter path, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    # No path found
    return None
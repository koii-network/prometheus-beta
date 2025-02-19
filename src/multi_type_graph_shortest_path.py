from typing import List, Dict, Tuple, Any
import heapq

class Node:
    def __init__(self, id: str, node_type: str):
        self.id = id
        self.node_type = node_type
    
    def __eq__(self, other):
        return self.id == other.id and self.node_type == other.node_type
    
    def __hash__(self):
        return hash((self.id, self.node_type))

def find_shortest_path(
    nodes: List[Node], 
    edges: List[Tuple[Node, Node, float]]
) -> List[Node]:
    """
    Find the shortest path between source and target nodes in a multi-type graph.
    
    Args:
        nodes (List[Node]): List of nodes in the graph
        edges (List[Tuple[Node, Node, float]]): List of weighted edges
    
    Returns:
        List[Node]: Shortest path from source to target, or empty list if no path exists
    
    Raises:
        ValueError: If nodes list is empty or source/target not in graph
    """
    # Validate input
    if not nodes:
        raise ValueError("Nodes list cannot be empty")
    
    # Create adjacency list representation
    graph = {}
    for node in nodes:
        graph[node] = []
    
    for start, end, weight in edges:
        graph[start].append((end, weight))
    
    # Determine source and target (first and last nodes)
    source = nodes[0]
    target = nodes[-1]
    
    # Dijkstra's algorithm
    distances = {node: float('inf') for node in nodes}
    distances[source] = 0
    
    previous = {node: None for node in nodes}
    
    # Priority queue to track nodes to visit
    pq = [(0, source)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If we've reached the target, reconstruct and return path
        if current_node == target:
            path = []
            while current_node:
                path.append(current_node)
                current_node = previous[current_node]
            return list(reversed(path))
        
        # If we've found a longer path, skip
        if current_distance > distances[current_node]:
            continue
        
        # Check neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # Update if shorter path found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    # No path found
    return []
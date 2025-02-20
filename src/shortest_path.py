from typing import List, Dict, Tuple, Any
import heapq

class Node:
    def __init__(self, name: str, node_type: str):
        self.name = name
        self.type = node_type

    def __eq__(self, other):
        return self.name == other.name and self.type == other.type

    def __hash__(self):
        return hash((self.name, self.type))

def find_shortest_path(nodes: List[Node], edges: List[Tuple[Node, Node, float]]) -> List[Node]:
    """
    Find the shortest path between source and target nodes in a weighted directed graph.
    
    Args:
        nodes (List[Node]): List of nodes in the graph
        edges (List[Tuple[Node, Node, float]]): List of edges with source, destination, and weight
    
    Returns:
        List[Node]: Shortest path from source to target, or empty list if no path exists
    
    Raises:
        ValueError: If source or target nodes are not in the graph
    """
    # Create adjacency list representation of the graph
    graph = {}
    for node in nodes:
        graph[node] = []
    
    for src, dest, weight in edges:
        graph[src].append((dest, weight))
    
    # Find source (first node) and target (last node)
    if not nodes:
        return []
    
    source = nodes[0]
    target = nodes[-1]

    # Dijkstra's algorithm
    distances = {node: float('inf') for node in nodes}
    distances[source] = 0
    
    previous = {node: None for node in nodes}
    
    pq = [(0, source)]
    visited = set()

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        if current_node == target:
            break
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    # Reconstruct path
    path = []
    current = target
    while current is not None:
        path.append(current)
        current = previous[current]
    
    return list(reversed(path)) if path[0] == source else []
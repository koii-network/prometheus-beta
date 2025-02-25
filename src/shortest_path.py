from typing import List, Tuple, Dict, Any
import heapq

class Node:
    def __init__(self, id: str, node_type: str):
        self.id = id
        self.node_type = node_type
    
    def __eq__(self, other):
        return self.id == other.id and self.node_type == other.node_type
    
    def __hash__(self):
        return hash((self.id, self.node_type))

def find_shortest_path(nodes: List[Node], edges: List[Tuple[Node, Node, float]]) -> List[Node]:
    """
    Find the shortest path between two nodes in a weighted directed graph.
    
    Args:
        nodes (List[Node]): List of nodes in the graph
        edges (List[Tuple[Node, Node, float]]): List of weighted edges 
                                                (from_node, to_node, weight)
    
    Returns:
        List[Node]: The shortest path between the first and last node in the nodes list
    
    Raises:
        ValueError: If no path exists between source and target nodes
    """
    # Create adjacency list representation of the graph
    graph = {}
    for node in nodes:
        graph[node] = []
    
    for from_node, to_node, weight in edges:
        graph[from_node].append((to_node, weight))
    
    # Verify at least two nodes exist
    if len(nodes) < 2:
        raise ValueError("At least two nodes are required to find a path")
    
    source = nodes[0]
    target = nodes[-1]
    
    # Dijkstra's algorithm with path tracking
    distances = {node: float('inf') for node in nodes}
    distances[source] = 0
    
    previous = {node: None for node in nodes}
    
    # Priority queue to store (distance, node)
    pq = [(0, source)]
    
    while pq:
        current_distance, current_node = heapq.heappop(pq)
        
        # If we've reached the target, reconstruct and return the path
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
            
            # If we've found a shorter path, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    # No path found
    raise ValueError(f"No path exists between {source.id} and {target.id}")
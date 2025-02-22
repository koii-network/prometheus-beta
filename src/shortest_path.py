from typing import List, Dict, Tuple, Optional
import heapq

class Node:
    def __init__(self, id: str, node_type: str):
        """
        Represents a node in the graph with an ID and type.
        
        :param id: Unique identifier for the node
        :param node_type: Type of the node
        """
        self.id = id
        self.node_type = node_type
    
    def __eq__(self, other):
        return self.id == other.id and self.node_type == other.node_type
    
    def __hash__(self):
        return hash((self.id, self.node_type))

def find_shortest_path(
    nodes: List[Node], 
    edges: List[Tuple[Node, Node, float]]
) -> Optional[List[Node]]:
    """
    Find the shortest path between two nodes in a weighted directed graph.
    
    :param nodes: List of nodes in the graph
    :param edges: List of edges as (source_node, target_node, weight) tuples
    :return: Shortest path as a list of nodes, or None if no path exists
    """
    # Create adjacency list representation of the graph
    graph = {}
    for node in nodes:
        graph[node] = []
    
    for source, target, weight in edges:
        graph[source].append((target, weight))
    
    # Find source and target nodes (first and last in the list)
    if len(nodes) < 2:
        return None
    
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
        
        # Check all neighboring nodes
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # Update if we've found a shorter path
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))
    
    # No path found
    return None
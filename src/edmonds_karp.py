from collections import deque
from typing import List, Dict

def edmonds_karp(graph: Dict[int, Dict[int, int]], source: int, sink: int) -> int:
    """
    Implement the Edmonds-Karp algorithm for maximum flow.
    
    Args:
        graph (Dict[int, Dict[int, int]]): Adjacency list representation of the graph.
                                           Keys are nodes, values are dictionaries of 
                                           adjacent nodes and their capacities.
        source (int): Source node
        sink (int): Sink node
    
    Returns:
        int: Maximum flow from source to sink
    """
    # Create a residual graph that can be modified
    def create_residual_graph(graph):
        residual = {}
        for node in graph:
            residual[node] = graph[node].copy()
        return residual
    
    # Breadth-first search to find augmenting path
    def bfs(graph, source, sink, parent):
        # Reset parent tracking
        for node in parent:
            parent[node] = None
        
        # Track visited nodes
        visited = set()
        
        # Queue for BFS
        queue = deque([source])
        visited.add(source)
        
        while queue:
            current = queue.popleft()
            
            # Check all adjacent nodes
            for neighbor, capacity in graph[current].items():
                # Only traverse if not visited and capacity > 0
                if neighbor not in visited and capacity > 0:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    parent[neighbor] = current
                    
                    # Found path to sink
                    if neighbor == sink:
                        return True
        
        return False
    
    # Validate input
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not in graph")
    
    # Initialize max flow
    max_flow = 0
    
    # Create residual graph and parent tracking
    residual = create_residual_graph(graph)
    
    # Track parent nodes for path finding
    parent = {node: None for node in graph}
    
    # Find augmenting paths
    while bfs(residual, source, sink, parent):
        # Find minimum flow along the path
        path_flow = float('inf')
        current = sink
        
        # Trace back to find minimum capacity
        while current != source:
            prev = parent[current]
            path_flow = min(path_flow, residual[prev][current])
            current = prev
        
        # Augment flow
        max_flow += path_flow
        
        # Update residual graph
        current = sink
        while current != source:
            prev = parent[current]
            residual[prev][current] -= path_flow
            
            # Add reverse edge if it doesn't exist
            if prev not in residual[current]:
                residual[current][prev] = 0
            residual[current][prev] += path_flow
            
            current = prev
    
    return max_flow
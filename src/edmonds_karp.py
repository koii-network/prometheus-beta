from typing import List, Dict
from collections import deque

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
    
    Raises:
        ValueError: If source or sink are not in the graph
    """
    # Validate input
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not in graph")
    
    # Create a residual graph to track remaining capacities
    residual_graph = {}
    for node in graph:
        residual_graph[node] = graph[node].copy()
    
    # Initialize max flow
    max_flow = 0
    
    # Find augmenting paths using BFS
    while True:
        # Track parent nodes for path reconstruction
        parent = {node: None for node in graph}
        
        # Use BFS to find augmenting path
        queue = deque([source])
        
        while queue:
            current = queue.popleft()
            
            # Check all neighbors
            for neighbor, capacity in residual_graph[current].items():
                if capacity > 0 and parent[neighbor] is None and neighbor != source:
                    parent[neighbor] = current
                    
                    # If we've reached the sink, we found an augmenting path
                    if neighbor == sink:
                        break
                    
                    queue.append(neighbor)
        
        # If no path to sink found, we're done
        if parent[sink] is None:
            break
        
        # Find the minimum flow in the path
        path_flow = float('inf')
        current = sink
        while current != source:
            prev = parent[current]
            path_flow = min(path_flow, residual_graph[prev][current])
            current = prev
        
        # Update residual capacities and max flow
        current = sink
        while current != source:
            prev = parent[current]
            residual_graph[prev][current] -= path_flow
            
            # Add reverse edge if it doesn't exist
            if prev not in residual_graph[current]:
                residual_graph[current][prev] = 0
            residual_graph[current][prev] += path_flow
            
            current = prev
        
        # Add path flow to max flow
        max_flow += path_flow
    
    return max_flow
from typing import List, Dict, Optional
from collections import deque

def edmonds_karp(graph: Dict[int, Dict[int, int]], source: int, sink: int) -> int:
    """
    Implement the Edmonds-Karp algorithm to find the maximum flow in a network.
    
    Args:
        graph (Dict[int, Dict[int, int]]): Adjacency list representation of the graph.
                                           Keys are nodes, values are dictionaries of 
                                           adjacent nodes and their edge capacities.
        source (int): The source node
        sink (int): The sink node
    
    Returns:
        int: Maximum flow from source to sink
    
    Raises:
        ValueError: If source or sink nodes are not in the graph
        TypeError: If graph is not a valid format
    """
    # Input validation
    if not isinstance(graph, dict):
        raise TypeError("Graph must be a dictionary")
    
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not found in graph")
    
    # Initialize residual graph
    residual_graph = {}
    for node in graph:
        residual_graph[node] = graph[node].copy()
        for adjacent_node in graph[node]:
            if adjacent_node not in residual_graph:
                residual_graph[adjacent_node] = {}
            if node not in residual_graph[adjacent_node]:
                residual_graph[adjacent_node][node] = 0
    
    # Maximum flow
    max_flow = 0
    
    # Find augmenting paths using BFS
    while True:
        # Perform BFS to find an augmenting path
        parent = {}
        visited = set()
        queue = deque([source])
        visited.add(source)
        
        # BFS to find path
        while queue:
            current = queue.popleft()
            
            # Check adjacent nodes
            for next_node, capacity in residual_graph[current].items():
                if next_node not in visited and capacity > 0:
                    parent[next_node] = current
                    visited.add(next_node)
                    queue.append(next_node)
                    
                    # Path found to sink
                    if next_node == sink:
                        break
            
            # Exit BFS if sink found
            if sink in visited:
                break
        
        # No augmenting path exists
        if sink not in visited:
            break
        
        # Find minimum flow along the path
        path_flow = float('inf')
        current = sink
        while current != source:
            prev = parent[current]
            path_flow = min(path_flow, residual_graph[prev][current])
            current = prev
        
        # Update residual graph
        current = sink
        while current != source:
            prev = parent[current]
            residual_graph[prev][current] -= path_flow
            residual_graph[current][prev] += path_flow
            current = prev
        
        # Add path flow to max flow
        max_flow += path_flow
    
    return max_flow
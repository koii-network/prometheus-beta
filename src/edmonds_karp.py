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
    
    # Initialize residual graph with complete node coverage
    # Find all unique nodes 
    all_nodes = set(graph.keys())
    for node_edges in graph.values():
        all_nodes.update(node_edges.keys())
    
    # Initialize residual graph
    residual_graph = {}
    for node in all_nodes:
        residual_graph[node] = {}
    
    # Populate graph with direct edges and zero-capacity reverse edges
    for node, edges in graph.items():
        for dest, capacity in edges.items():
            # Forward edge
            residual_graph[node][dest] = capacity
            
            # Ensure reverse edge exists
            if dest not in residual_graph:
                residual_graph[dest] = {}
            if node not in residual_graph[dest]:
                residual_graph[dest][node] = 0
    
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
            # Forward edge
            residual_graph[prev][current] -= path_flow
            # Reverse edge
            residual_graph[current][prev] += path_flow
            current = prev
        
        # Add path flow to max flow
        max_flow += path_flow
    
    return max_flow
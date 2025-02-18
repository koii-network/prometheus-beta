from collections import deque
from typing import List, Dict

def edmonds_karp(graph: Dict[int, Dict[int, int]], source: int, sink: int) -> int:
    """
    Implement the Edmonds-Karp algorithm to find maximum flow in a network.
    
    Args:
        graph (Dict[int, Dict[int, int]]): Adjacency list representation of the graph.
                                           Each key is a node, and its value is a dict 
                                           of adjacent nodes and their edge capacities.
        source (int): Source node
        sink (int): Sink node
    
    Returns:
        int: Maximum flow from source to sink
    
    Raises:
        ValueError: If source or sink nodes are not in the graph
    """
    # Validate input
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not in graph")
    
    # Create a residual graph
    residual_graph = {node: graph[node].copy() for node in graph}
    for node in graph:
        for adjacent_node in graph[node]:
            if node not in residual_graph.get(adjacent_node, {}):
                if adjacent_node not in residual_graph:
                    residual_graph[adjacent_node] = {}
                residual_graph[adjacent_node][node] = 0
    
    # Initialize max flow
    max_flow = 0
    
    # Find augmenting paths using BFS
    while True:
        # Perform BFS to find an augmenting path
        parent = {}
        visited = set()
        queue = deque([source])
        visited.add(source)
        
        while queue:
            current = queue.popleft()
            
            # Check all adjacent nodes
            for next_node, capacity in residual_graph[current].items():
                if next_node not in visited and capacity > 0:
                    parent[next_node] = current
                    visited.add(next_node)
                    queue.append(next_node)
                    
                    # Found path to sink
                    if next_node == sink:
                        break
            
            # Exit outer loop if sink is found
            if sink in visited:
                break
        
        # No augmenting path found, terminate
        if sink not in visited:
            break
        
        # Find minimum flow along the path
        path_flow = float('inf')
        current = sink
        while current != source:
            prev = parent[current]
            path_flow = min(path_flow, residual_graph[prev][current])
            current = prev
        
        # Update residual graph and max flow
        current = sink
        while current != source:
            prev = parent[current]
            residual_graph[prev][current] -= path_flow
            residual_graph[current][prev] += path_flow
            current = prev
        
        # Add path flow to max flow
        max_flow += path_flow
    
    return max_flow
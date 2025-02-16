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
        ValueError: If source or sink nodes are not in the graph
    """
    # Validate input
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not in graph")
    
    # Create a residual graph
    def build_residual_graph(graph):
        residual = {}
        for node in graph:
            residual[node] = graph[node].copy()
            for adjacent_node in graph[node]:
                if adjacent_node not in residual:
                    residual[adjacent_node] = {}
                if node not in residual[adjacent_node]:
                    residual[adjacent_node][node] = 0
        return residual
    
    residual_graph = build_residual_graph(graph)
    max_flow = 0
    
    # Find augmenting paths using BFS
    def bfs_find_path(graph, source, sink):
        # Track visited nodes and paths
        visited = set()
        parent = {}
        queue = deque([source])
        visited.add(source)
        
        while queue:
            current = queue.popleft()
            
            # Check adjacent nodes
            for neighbor, capacity in graph[current].items():
                if neighbor not in visited and capacity > 0:
                    parent[neighbor] = current
                    
                    if neighbor == sink:
                        # Path found
                        return parent
                    
                    queue.append(neighbor)
                    visited.add(neighbor)
        
        # No path found
        return None
    
    # Find augmenting paths and update flow
    while True:
        path = bfs_find_path(residual_graph, source, sink)
        
        # No more augmenting paths
        if path is None:
            break
        
        # Find minimum residual capacity along the path
        path_flow = float('inf')
        current = sink
        while current != source:
            parent = path[current]
            path_flow = min(path_flow, residual_graph[parent][current])
            current = parent
        
        # Update residual graph
        current = sink
        while current != source:
            parent = path[current]
            residual_graph[parent][current] -= path_flow
            residual_graph[current][parent] += path_flow
            current = parent
        
        # Add to total max flow
        max_flow += path_flow
    
    return max_flow
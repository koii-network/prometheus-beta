from typing import List, Dict
from collections import deque

def edmonds_karp(graph: Dict[int, Dict[int, int]], source: int, sink: int) -> int:
    """
    Implement the Edmonds-Karp algorithm to find maximum flow in a network.
    
    Args:
        graph (Dict[int, Dict[int, int]]): Adjacency list representation of the graph 
            where graph[u][v] represents the capacity from node u to node v.
        source (int): The source node.
        sink (int): The sink node.
    
    Returns:
        int: The maximum flow from source to sink.
    
    Raises:
        ValueError: If source or sink nodes are not in the graph.
    """
    # Validate input
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not in graph")
    
    # Create a residual graph to track remaining capacities
    residual_graph = {u: graph[u].copy() for u in graph}
    
    # Function to find augmenting path using BFS
    def bfs_find_path() -> List[int]:
        # Track visited nodes and parent nodes
        visited = set()
        parent = {}
        queue = deque([source])
        visited.add(source)
        
        while queue:
            current = queue.popleft()
            
            # Check neighbors
            for neighbor, capacity in residual_graph[current].items():
                if neighbor not in visited and capacity > 0:
                    parent[neighbor] = current
                    
                    # If we've reached the sink, reconstruct and return the path
                    if neighbor == sink:
                        path = []
                        while neighbor != source:
                            path.append(neighbor)
                            neighbor = parent[neighbor]
                        path.append(source)
                        return list(reversed(path))
                    
                    # Mark as visited and add to queue
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        # No augmenting path found
        return []
    
    # Initialize max flow
    max_flow = 0
    
    # Find augmenting paths and update flow
    while True:
        # Find an augmenting path
        path = bfs_find_path()
        
        # If no augmenting path exists, we're done
        if not path:
            break
        
        # Find the minimum residual capacity along the path
        path_flow = float('inf')
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            path_flow = min(path_flow, residual_graph[u][v])
        
        # Update residual capacities
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            
            # Reduce forward edge capacity
            residual_graph[u][v] -= path_flow
            
            # Add backward edge capacity for flow reversal
            if v not in residual_graph or u not in residual_graph[v]:
                if v not in residual_graph:
                    residual_graph[v] = {}
                residual_graph[v][u] = 0
            residual_graph[v][u] += path_flow
        
        # Increase max flow
        max_flow += path_flow
    
    return max_flow
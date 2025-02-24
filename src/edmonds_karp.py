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
    
    Raises:
        ValueError: If source or sink nodes are not in the graph
    """
    # Validate input
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not in graph")
    
    # Create a residual graph
    residual_graph = {node: graph[node].copy() for node in graph}
    for node in graph:
        for adj_node in graph[node]:
            if node not in residual_graph.get(adj_node, {}):
                if adj_node not in residual_graph:
                    residual_graph[adj_node] = {}
                residual_graph[adj_node][node] = 0
    
    max_flow = 0
    
    def bfs_find_path(graph: Dict[int, Dict[int, int]], source: int, sink: int) -> List[int]:
        """Find an augmenting path using BFS."""
        visited = set()
        parent = {}
        queue = deque([source])
        visited.add(source)
        
        while queue:
            current = queue.popleft()
            
            # Check all adjacent nodes
            for neighbor, capacity in graph[current].items():
                if neighbor not in visited and capacity > 0:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    parent[neighbor] = current
                    
                    if neighbor == sink:
                        # Reconstruct path
                        path = []
                        while neighbor != source:
                            path.append(neighbor)
                            neighbor = parent[neighbor]
                        path.append(source)
                        return list(reversed(path))
        
        return []  # No path found
    
    # Main Edmonds-Karp algorithm
    while True:
        # Find augmenting path
        path = bfs_find_path(residual_graph, source, sink)
        
        # If no path exists, we're done
        if not path:
            break
        
        # Find minimum residual capacity along the path
        path_flow = float('inf')
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            path_flow = min(path_flow, residual_graph[u][v])
        
        # Update residual capacities
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            
            # Reduce forward edge capacity
            residual_graph[u][v] -= path_flow
            
            # Add backward edge capacity
            residual_graph[v][u] += path_flow
        
        # Add to total max flow
        max_flow += path_flow
    
    return max_flow
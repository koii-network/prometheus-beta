from typing import List, Dict

def ford_fulkerson(graph: Dict[str, Dict[str, int]], source: str, sink: str) -> int:
    """
    Implement the Ford-Fulkerson algorithm to find maximum flow in a network.
    
    Args:
        graph (Dict[str, Dict[str, int]]): Adjacency list representation of the graph
        source (str): Source node 
        sink (str): Sink node
    
    Returns:
        int: Maximum flow from source to sink
    
    Raises:
        ValueError: If source or sink nodes are not in the graph
    """
    # Validate input
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not found in the graph")
    
    # Create a residual graph (deep copy of original graph)
    residual_graph = {node: graph[node].copy() for node in graph}
    
    # Initialize max flow
    max_flow = 0
    
    # Find augmenting paths using BFS
    while True:
        # Find an augmenting path using breadth-first search
        path, path_flow = bfs_find_path(residual_graph, source, sink)
        
        # If no path is found, we've reached max flow
        if not path:
            break
        
        # Update residual graph and max flow
        max_flow += path_flow
        
        # Reduce residual capacities of the edges along the path
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            
            # Reduce forward edge capacity
            residual_graph[u][v] -= path_flow
            
            # Add/update backward edge
            if v not in residual_graph:
                residual_graph[v] = {}
            if u not in residual_graph[v]:
                residual_graph[v][u] = 0
            residual_graph[v][u] += path_flow
    
    return max_flow

def bfs_find_path(graph: Dict[str, Dict[str, int]], source: str, sink: str) -> tuple:
    """
    Find an augmenting path using Breadth-First Search.
    
    Args:
        graph (Dict[str, Dict[str, int]]): Residual graph
        source (str): Source node
        sink (str): Sink node
    
    Returns:
        tuple: (path, path_flow) - path from source to sink, and minimum flow along the path
    """
    # Track visited nodes and their parents
    visited = {source}
    parent = {}
    
    # Queue for BFS
    queue = [source]
    
    # Find augmenting path
    while queue:
        u = queue.pop(0)
        
        # Check adjacent nodes
        for v, capacity in graph[u].items():
            if v not in visited and capacity > 0:
                queue.append(v)
                visited.add(v)
                parent[v] = u
                
                # If sink is reached, reconstruct path
                if v == sink:
                    # Reconstruct path
                    path = []
                    current = sink
                    while current != source:
                        path.insert(0, current)
                        current = parent[current]
                    path.insert(0, source)
                    
                    # Find minimum flow along the path
                    path_flow = min(graph[path[i]][path[i+1]] for i in range(len(path)-1))
                    
                    return path, path_flow
    
    # No augmenting path found
    return [], 0
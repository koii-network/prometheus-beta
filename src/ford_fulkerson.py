from typing import List, Dict

def ford_fulkerson(graph: Dict[str, Dict[str, int]], source: str, sink: str) -> int:
    """
    Implement the Ford-Fulkerson algorithm to find maximum flow in a network.
    
    Args:
        graph (Dict[str, Dict[str, int]]): A graph represented as an adjacency list 
                                           with node names as keys and their adjacent 
                                           nodes and capacities as nested dictionary.
        source (str): The source node name.
        sink (str): The sink node name.
    
    Returns:
        int: The maximum flow from source to sink.
    
    Raises:
        ValueError: If source or sink nodes are not in the graph.
    """
    # Validate input
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not found in the graph")
    
    # Create a residual graph
    residual_graph = {node: graph[node].copy() for node in graph}
    for node in graph:
        for neighbor in graph:
            if neighbor not in residual_graph[node]:
                residual_graph[node][neighbor] = 0
    
    def bfs_path(graph, source, sink):
        """Find an augmenting path using Breadth-First Search."""
        visited = {node: False for node in graph}
        parent = {node: None for node in graph}
        queue = [source]
        visited[source] = True
        
        while queue:
            current = queue.pop(0)
            
            for neighbor, capacity in graph[current].items():
                if not visited[neighbor] and capacity > 0:
                    queue.append(neighbor)
                    visited[neighbor] = True
                    parent[neighbor] = current
                    
                    if neighbor == sink:
                        return parent
        
        return None
    
    max_flow = 0
    
    # Find augmenting paths and update flow
    while True:
        path = bfs_path(residual_graph, source, sink)
        
        if path is None:
            break
        
        # Find the minimum residual capacity along the path
        path_flow = float('inf')
        current = sink
        while current != source:
            parent = path[current]
            path_flow = min(path_flow, residual_graph[parent][current])
            current = parent
        
        # Update residual capacities
        current = sink
        while current != source:
            parent = path[current]
            residual_graph[parent][current] -= path_flow
            residual_graph[current][parent] += path_flow
            current = parent
        
        max_flow += path_flow
    
    return max_flow
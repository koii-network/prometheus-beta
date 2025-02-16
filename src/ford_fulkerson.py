from typing import List, Dict

def ford_fulkerson(graph: Dict[int, Dict[int, int]], source: int, sink: int) -> int:
    """
    Implement the Ford-Fulkerson algorithm to find maximum flow in a network.
    
    Args:
        graph (Dict[int, Dict[int, int]]): Adjacency list representation of the graph 
                                           where keys are nodes and values are dicts 
                                           of neighboring nodes with their capacities.
        source (int): Source node from which flow originates
        sink (int): Sink node where flow terminates
    
    Returns:
        int: Maximum flow from source to sink
    
    Raises:
        ValueError: If source or sink are not in the graph
    """
    # Validate input
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not found in graph")
    
    # Create a residual graph (deep copy of the original graph)
    residual_graph = {node: dict(neighbors) for node, neighbors in graph.items()}
    
    # Function to find an augmenting path using BFS
    def bfs_find_path(graph: Dict[int, Dict[int, int]], source: int, sink: int) -> List[int]:
        # Track visited nodes and parent nodes for path reconstruction
        visited = set()
        parent = {}
        queue = [source]
        visited.add(source)
        
        while queue:
            current = queue.pop(0)
            
            # Check all neighbors of current node
            for neighbor, capacity in graph.get(current, {}).items():
                if neighbor not in visited and capacity > 0:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    parent[neighbor] = current
                    
                    # Path found to sink
                    if neighbor == sink:
                        # Reconstruct path
                        path = []
                        while neighbor in parent:
                            path.insert(0, neighbor)
                            neighbor = parent[neighbor]
                        path.insert(0, source)
                        return path
        
        # No path found
        return []
    
    # Track maximum flow
    max_flow = 0
    
    # Find augmenting paths
    while True:
        # Find an augmenting path
        path = bfs_find_path(residual_graph, source, sink)
        
        # No more paths exist
        if not path:
            break
        
        # Find minimum flow in the path
        path_flow = float('inf')
        for i in range(len(path) - 1):
            start, end = path[i], path[i+1]
            path_flow = min(path_flow, residual_graph[start][end])
        
        # Update residual graph and max flow
        max_flow += path_flow
        
        # Update capacities in residual graph
        for i in range(len(path) - 1):
            start, end = path[i], path[i+1]
            residual_graph[start][end] -= path_flow
            
            # Add reverse edge if it doesn't exist
            if end not in residual_graph or start not in residual_graph[end]:
                if end not in residual_graph:
                    residual_graph[end] = {}
                residual_graph[end][start] = 0
            
            residual_graph[end][start] += path_flow
    
    return max_flow
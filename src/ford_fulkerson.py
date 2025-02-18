from typing import List, Dict

def ford_fulkerson(graph: Dict[str, Dict[str, int]], source: str, sink: str) -> int:
    """
    Implement the Ford-Fulkerson algorithm to find the maximum flow in a network.
    
    Args:
        graph (Dict[str, Dict[str, int]]): Adjacency list representation of the graph 
                                           where keys are nodes and values are dictionaries 
                                           of adjacent nodes and their capacities.
        source (str): The source node.
        sink (str): The sink node.
    
    Returns:
        int: The maximum flow from source to sink.
    
    Raises:
        ValueError: If source or sink nodes are not in the graph.
    """
    # Validate input
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not in graph")
    
    # Create a residual graph (deep copy of original graph)
    residual_graph = {node: graph[node].copy() for node in graph}
    
    # Function to find an augmenting path using depth-first search
    def find_path(current, path, visited):
        # Mark current node as visited
        visited.add(current)
        
        # If we've reached the sink, return the path
        if current == sink:
            return path
        
        # Explore all adjacent nodes
        for neighbor, capacity in residual_graph[current].items():
            if neighbor not in visited and capacity > 0:
                # Try to find a path through this neighbor
                new_path = path + [neighbor]
                result = find_path(neighbor, new_path, visited)
                if result:
                    return result
        
        return None
    
    # Initialize max flow
    max_flow = 0
    
    # Find augmenting paths
    while True:
        # Find an augmenting path
        visited = set()
        path = find_path(source, [source], visited)
        
        # If no path found, we're done
        if not path:
            break
        
        # Find the minimum residual capacity along the path
        path_flow = float('inf')
        for i in range(len(path) - 1):
            current = path[i]
            next_node = path[i+1]
            path_flow = min(path_flow, residual_graph[current][next_node])
        
        # Update residual capacities
        for i in range(len(path) - 1):
            current = path[i]
            next_node = path[i+1]
            
            # Reduce forward edge capacity
            residual_graph[current][next_node] -= path_flow
            
            # Add backward edge if it doesn't exist
            if current not in residual_graph[next_node]:
                residual_graph[next_node][current] = 0
            
            # Increase backward edge capacity
            residual_graph[next_node][current] += path_flow
        
        # Add path flow to max flow
        max_flow += path_flow
    
    return max_flow
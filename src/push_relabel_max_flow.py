from typing import List, Dict, Tuple

def push_relabel_max_flow(graph: Dict[int, Dict[int, int]], source: int, sink: int) -> int:
    """
    Implement the Push-Relabel algorithm for maximum flow.
    
    Args:
    graph (Dict[int, Dict[int, int]]): Adjacency list representation of the graph 
                                       where graph[u][v] is the capacity from u to v
    source (int): Source node
    sink (int): Sink node
    
    Returns:
    int: Maximum flow from source to sink
    """
    # Get all nodes
    nodes = set(graph.keys())
    for u in graph:
        nodes.update(graph[u].keys())
    
    # Initialize preflow data structures
    excess = {node: 0 for node in nodes}
    height = {node: 0 for node in nodes}
    flow = {u: {v: 0 for v in graph.get(u, {})} for u in nodes}
    
    # Initialize height of source
    height[source] = len(nodes)
    
    # Initial push from source
    for v in graph.get(source, {}):
        push_amount = graph[source][v]
        flow[source][v] = push_amount
        flow[v][source] = -push_amount
        excess[v] += push_amount
        excess[source] -= push_amount
    
    # Helper function to push flow
    def push(u: int, v: int) -> bool:
        """
        Push excess flow from u to v if possible
        Returns True if push was successful, False otherwise
        """
        delta = min(excess[u], 
                    graph.get(u, {}).get(v, 0) - flow.get(u, {}).get(v, 0))
        
        if delta <= 0 or height[u] <= height[v]:
            return False
        
        # Update flow
        flow[u][v] = flow.get(u, {}).get(v, 0) + delta
        flow[v][u] = flow.get(v, {}).get(u, 0) - delta
        
        # Update excess
        excess[u] -= delta
        excess[v] += delta
        
        return True
    
    # Helper function to relabel a node
    def relabel(u: int) -> None:
        """
        Relabel a node to enable pushing more flow
        """
        # Find minimum height of adjacent nodes with residual capacity
        min_height = float('inf')
        for v in graph.get(u, {}):
            if graph[u].get(v, 0) > flow.get(u, {}).get(v, 0):
                min_height = min(min_height, height[v])
        
        # Update height if needed
        if min_height < float('inf'):
            height[u] = min_height + 1
    
    # Main push-relabel loop
    while True:
        # Find an overflowing node (excluding source and sink)
        overflowing_nodes = [
            u for u in nodes 
            if u not in [source, sink] and excess[u] > 0
        ]
        
        if not overflowing_nodes:
            break
        
        for u in overflowing_nodes:
            pushed = False
            for v in graph.get(u, {}):
                if push(u, v):
                    pushed = True
                    break
            
            # If no push was possible, relabel the node
            if not pushed:
                relabel(u)
    
    # Return total flow to sink
    return sum(flow.get(u, {}).get(sink, 0) for u in nodes)
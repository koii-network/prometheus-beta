import heapq
from typing import Dict, List, Tuple, Optional

def johnsons_algorithm(graph: Dict[int, List[Tuple[int, int]]]) -> Optional[Dict[int, Dict[int, int]]]:
    """
    Implement Johnson's algorithm for finding all-pairs shortest paths in a weighted graph.
    
    Args:
        graph (Dict[int, List[Tuple[int, int]]]): A graph represented as an adjacency list 
                                                  where each key is a node and value is a list 
                                                  of (destination, weight) tuples.
    
    Returns:
        Optional[Dict[int, Dict[int, int]]]: A dictionary of shortest path distances between 
                                             all pairs of nodes, or None if a negative cycle exists.
    
    Raises:
        ValueError: If the graph is empty
    """
    # Check for empty graph
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Add a new node connected to all other nodes with zero-weight edges
    nodes = list(graph.keys())
    super_source = max(nodes) + 1
    graph[super_source] = [(node, 0) for node in nodes]
    
    # Step 1: Bellman-Ford to reweight edges
    def bellman_ford(start_node: int) -> Optional[Dict[int, int]]:
        """
        Bellman-Ford algorithm to compute shortest paths from a start node.
        
        Args:
            start_node (int): The source node for path computation
        
        Returns:
            Optional[Dict[int, int]]: Shortest path distances or None if negative cycle exists
        """
        # Initialize distances
        dist = {node: float('inf') for node in graph}
        dist[start_node] = 0
        
        # Relax edges |V| - 1 times
        for _ in range(len(graph) - 1):
            for u in graph:
                for v, w in graph[u]:
                    if dist[u] != float('inf') and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
        
        # Check for negative cycles
        for u in graph:
            for v, w in graph[u]:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    return None  # Negative cycle detected
        
        return dist
    
    # Compute h(u) using Bellman-Ford from super source
    h = bellman_ford(super_source)
    
    # If negative cycle detected, return None
    if h is None:
        return None
    
    # Remove the super source node
    del graph[super_source]
    
    # Reweight edges
    reweighted_graph = {}
    for u in graph:
        reweighted_graph[u] = []
        for v, w in graph[u]:
            # Reweight: w' = w + h(u) - h(v)
            reweighted_edge_weight = w + h[u] - h[v]
            reweighted_graph[u].append((v, reweighted_edge_weight))
    
    # Dijkstra for each node
    shortest_paths = {}
    for start_node in graph:
        # Use Dijkstra's algorithm with reweighted graph
        dist = {node: float('inf') for node in graph}
        dist[start_node] = 0
        pq = [(0, start_node)]
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            # Skip if we've found a shorter path
            if current_dist > dist[u]:
                continue
            
            for v, w in reweighted_graph[u]:
                distance = current_dist + w
                if distance < dist[v]:
                    dist[v] = distance
                    heapq.heappush(pq, (distance, v))
        
        # Adjust distances back to original weights
        shortest_paths[start_node] = {
            v: dist[v] - h[start_node] + h[v] if dist[v] != float('inf') else float('inf')
            for v in graph
        }
    
    return shortest_paths
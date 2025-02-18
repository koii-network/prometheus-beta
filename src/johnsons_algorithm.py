import heapq
from typing import List, Dict, Tuple, Optional

def johnsons_algorithm(graph: Dict[int, List[Tuple[int, int]]]) -> Optional[Dict[int, Dict[int, int]]]:
    """
    Implement Johnson's algorithm for finding shortest paths between all pairs of vertices in a graph.
    
    Args:
        graph (Dict[int, List[Tuple[int, int]]]): Adjacency list representation of the graph.
                                                  Keys are source vertices, values are lists of (destination, weight) tuples.
    
    Returns:
        Optional[Dict[int, Dict[int, int]]]: Dictionary of shortest paths between all pairs of vertices,
                                             or None if a negative cycle is detected.
    """
    # Special case for empty graph
    if not graph:
        return {}
    
    # Step 1: Add a new vertex connected to all other vertices with zero-weight edges
    n = len(graph)
    modified_graph = graph.copy()
    modified_graph[n] = [(v, 0) for v in graph.keys()]
    
    # Step 2: Run Bellman-Ford from the new vertex to detect and handle negative cycles
    def bellman_ford(start_vertex: int) -> Optional[Dict[int, int]]:
        # Initialize distances
        distances = {v: float('inf') for v in modified_graph.keys()}
        distances[start_vertex] = 0
        
        # Relax edges |V| - 1 times
        for _ in range(len(modified_graph) - 1):
            for u in modified_graph:
                for v, weight in modified_graph[u]:
                    if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                        distances[v] = distances[u] + weight
        
        # Check for negative cycle
        for u in modified_graph:
            for v, weight in modified_graph[u]:
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    return None  # Negative cycle detected
        
        return distances
    
    # Compute h (reweighting function)
    h = bellman_ford(n)
    if h is None:
        return None  # Negative cycle detected
    
    # Remove the temporary vertex
    del modified_graph[n]
    del h[n]
    
    # Step 3: Reweight the graph
    reweighted_graph = {}
    for u in graph:
        reweighted_graph[u] = []
        for v, weight in graph[u]:
            # Reweight edge: w'(u,v) = w(u,v) + h(u) - h(v)
            new_weight = weight + h[u] - h[v]
            reweighted_graph[u].append((v, new_weight))
    
    # Step 4: Compute shortest paths using Dijkstra's algorithm
    def dijkstra(start: int) -> Dict[int, int]:
        distances = {v: float('inf') for v in graph}
        distances[start] = 0
        pq = [(0, start)]
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            # If we've found a longer path to u, skip
            if current_dist > distances[u]:
                continue
            
            for v, weight in reweighted_graph.get(u, []):
                distance = current_dist + weight
                
                # If we've found a shorter path to v
                if distance < distances[v]:
                    distances[v] = distance
                    heapq.heappush(pq, (distance, v))
        
        return distances
    
    # Compute shortest paths for all vertices
    all_shortest_paths = {}
    for u in graph:
        # Run Dijkstra's from each vertex
        shortest_paths = dijkstra(u)
        
        # Create the paths dictionary without the source vertex itself and infinities
        paths = {
            v: shortest_paths[v] - h[u] + h[v] 
            for v in graph 
            if v != u and shortest_paths[v] != float('inf')
        }
        
        all_shortest_paths[u] = paths
    
    return all_shortest_paths
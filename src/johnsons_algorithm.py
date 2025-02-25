import heapq
from typing import List, Dict, Union, Tuple

def johnsons_algorithm(graph: Dict[int, Dict[int, int]]) -> Union[Dict[int, Dict[int, int]], None]:
    """
    Implement Johnson's algorithm for finding shortest paths between all pairs of vertices in a graph.
    
    Args:
        graph (Dict[int, Dict[int, int]]): A graph represented as an adjacency list.
                                           Keys are source vertices, values are dictionaries of 
                                           destination vertices and their edge weights.
    
    Returns:
        Dict[int, Dict[int, int]]: A dictionary of shortest path distances between all pairs of vertices,
                                   or None if a negative cycle is detected.
    
    Raises:
        ValueError: If the input graph is empty or invalid.
    """
    # Input validation
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Special case for single vertex graph
    if len(graph) == 1 and all(len(neighbors) == 0 for neighbors in graph.values()):
        return {list(graph.keys())[0]: {}}
    
    # Add a new source vertex connected to all other vertices with zero weight
    modified_graph = graph.copy()
    source_vertex = max(graph.keys()) + 1
    modified_graph[source_vertex] = {v: 0 for v in graph.keys()}
    
    # Bellman-Ford to detect negative cycles and compute vertex potentials
    def bellman_ford(graph: Dict[int, Dict[int, int]], source: int) -> Dict[int, int]:
        """
        Bellman-Ford algorithm to compute vertex potentials and detect negative cycles.
        
        Args:
            graph (Dict[int, Dict[int, int]]): Graph representation
            source (int): Source vertex
        
        Returns:
            Dict[int, int]: Vertex potentials
        """
        # Initialize distances
        dist = {v: float('inf') for v in graph}
        dist[source] = 0
        
        # Relax edges |V| - 1 times
        vertices = list(graph.keys())
        for _ in range(len(vertices) - 1):
            for u in graph:
                for v, weight in graph[u].items():
                    if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight
        
        # Check for negative cycle
        for u in graph:
            for v, weight in graph[u].items():
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    return None  # Negative cycle detected
        
        return dist
    
    # Compute vertex potentials
    potentials = bellman_ford(modified_graph, source_vertex)
    if potentials is None:
        return None  # Negative cycle detected
    
    # Reweight edges
    reweighted_graph = {}
    for u in graph:
        reweighted_graph[u] = {}
        for v, weight in graph[u].items():
            reweighted_graph[u][v] = weight + potentials[u] - potentials[v]
    
    # Dijkstra's algorithm for each vertex
    shortest_paths = {}
    for source in graph:
        shortest_paths[source] = {}
        
        # Priority queue for Dijkstra's algorithm
        pq = [(0, source)]
        distances = {v: float('inf') for v in graph}
        distances[source] = 0
        
        while pq:
            current_distance, u = heapq.heappop(pq)
            
            # If we've found a longer path, skip
            if current_distance > distances[u]:
                continue
            
            # Check all neighbors
            for v, weight in reweighted_graph[u].items():
                distance = current_distance + weight
                
                # Update if we've found a shorter path
                if distance < distances[v]:
                    distances[v] = distance
                    heapq.heappush(pq, (distance, v))
        
        # Adjust distances back to original weights
        for v in graph:
            if distances[v] != float('inf'):
                shortest_paths[source][v] = distances[v] - potentials[source] + potentials[v]
    
    return shortest_paths
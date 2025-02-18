import heapq
import math
from typing import Dict, List, Tuple, Optional

def johnson_shortest_paths(graph: Dict[int, List[Tuple[int, int]]]) -> Optional[Dict[int, Dict[int, float]]]:
    """
    Implements Johnson's algorithm to find shortest paths between all pairs of vertices.
    
    Args:
    graph (Dict[int, List[Tuple[int, int]]]): A graph represented as an adjacency list
        where each key is a vertex, and the value is a list of (destination, weight) tuples.
    
    Returns:
    Optional[Dict[int, Dict[int, float]]]: A dictionary of shortest path distances 
        between all pairs of vertices, or None if a negative cycle is detected.
    """
    # Add a new vertex connected to all other vertices with zero-weight edges
    vertices = list(graph.keys())
    new_vertex = max(vertices) + 1 if vertices else 0
    graph[new_vertex] = [(v, 0) for v in vertices]
    
    # Bellman-Ford to reweight edges and detect negative cycles
    distances = bellman_ford(graph, new_vertex)
    if distances is None:
        return None
    
    # Remove the temporary vertex
    del graph[new_vertex]
    
    # Reweight edges
    reweighted_graph = {}
    for u in graph:
        reweighted_graph[u] = []
        for (v, w) in graph[u]:
            new_weight = w + distances[u] - distances[v]
            reweighted_graph[u].append((v, new_weight))
    
    # Dijkstra for each vertex
    shortest_paths = {}
    for source in graph:
        shortest_paths[source] = dijkstra(reweighted_graph, source, distances)
    
    return shortest_paths

def bellman_ford(graph: Dict[int, List[Tuple[int, int]]], source: int) -> Optional[Dict[int, float]]:
    """
    Bellman-Ford algorithm to find shortest paths from a source vertex and detect negative cycles.
    
    Args:
    graph (Dict[int, List[Tuple[int, int]]]): Graph represented as an adjacency list.
    source (int): Source vertex.
    
    Returns:
    Optional[Dict[int, float]]: Distances from source, or None if negative cycle exists.
    """
    vertices = list(graph.keys())
    distances = {v: math.inf for v in vertices}
    distances[source] = 0
    
    # Relax edges |V| - 1 times
    for _ in range(len(vertices) - 1):
        for u in graph:
            for v, w in graph[u]:
                if distances[u] != math.inf and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w
    
    # Check for negative cycles
    for u in graph:
        for v, w in graph[u]:
            if distances[u] != math.inf and distances[u] + w < distances[v]:
                return None
    
    return distances

def dijkstra(graph: Dict[int, List[Tuple[int, int]]], source: int, 
              reweight_distances: Dict[int, float]) -> Dict[int, float]:
    """
    Dijkstra's algorithm with edge reweighting.
    
    Args:
    graph (Dict[int, List[Tuple[int, int]]]): Reweighted graph.
    source (int): Source vertex.
    reweight_distances (Dict[int, float]): Reweighting distances from Bellman-Ford.
    
    Returns:
    Dict[int, float]: Shortest path distances from source vertex.
    """
    distances = {v: math.inf for v in graph}
    distances[source] = 0
    pq = [(0, source)]
    
    while pq:
        current_distance, u = heapq.heappop(pq)
        
        # If we've found a longer path, skip
        if current_distance > distances[u]:
            continue
        
        for v, w in graph[u]:
            # Adjust the distance calculation
            distance = current_distance + w
            
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(pq, (distance, v))
    
    # Adjust distances back to original weights
    for v in distances:
        if distances[v] != math.inf:
            distances[v] += reweight_distances[v] - reweight_distances[source]
    
    return distances
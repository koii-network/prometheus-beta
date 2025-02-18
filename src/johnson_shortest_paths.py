import heapq
from typing import List, Dict, Optional, Tuple

def johnson_shortest_paths(graph: Dict[int, List[Tuple[int, int]]]) -> Optional[Dict[int, Dict[int, float]]]:
    """
    Implement Johnson's algorithm for finding shortest paths between all pairs of vertices.
    
    Args:
        graph (Dict[int, List[Tuple[int, int]]]): A graph represented as an adjacency list 
                where each key is a vertex and the value is a list of (destination, weight) tuples.
    
    Returns:
        Optional[Dict[int, Dict[int, float]]]: A dictionary of shortest path distances between all pairs of vertices,
        or None if a negative cycle is detected.
    
    Raises:
        ValueError: If the graph is empty.
    """
    # Input validation
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Add a new vertex connected to all other vertices with zero-weight edges
    vertices = list(graph.keys())
    max_vertex = max(vertices)
    new_vertex = max_vertex + 1
    graph[new_vertex] = [(v, 0) for v in vertices]
    
    # Step 1: Bellman-Ford to compute vertex potentials
    # If Bellman-Ford fails (negative cycle detected), return None
    potentials = bellman_ford(graph, new_vertex)
    if potentials is None:
        return None
    
    # Remove the temporary vertex
    del graph[new_vertex]
    
    # Step 2: Reweight the graph using vertex potentials
    reweighted_graph = {}
    for u in graph:
        reweighted_graph[u] = []
        for v, weight in graph[u]:
            new_weight = weight + potentials[u] - potentials[v]
            reweighted_graph[u].append((v, new_weight))
    
    # Step 3: Run Dijkstra from each vertex
    shortest_paths = {}
    for source in graph:
        shortest_paths[source] = dijkstra(reweighted_graph, source, potentials)
    
    return shortest_paths

def bellman_ford(graph: Dict[int, List[Tuple[int, int]]], source: int) -> Optional[Dict[int, float]]:
    """
    Bellman-Ford algorithm to detect negative cycles and compute vertex potentials.
    
    Args:
        graph (Dict[int, List[Tuple[int, int]]]): Graph represented as an adjacency list.
        source (int): Source vertex for computing potentials.
    
    Returns:
        Optional[Dict[int, float]]: Dictionary of vertex potentials, or None if a negative cycle exists.
    """
    vertices = list(graph.keys())
    potentials = {v: float('inf') for v in vertices}
    potentials[source] = 0
    
    # Relax edges |V| - 1 times
    for _ in range(len(vertices) - 1):
        for u in graph:
            for v, weight in graph[u]:
                if potentials[u] != float('inf') and potentials[u] + weight < potentials[v]:
                    potentials[v] = potentials[u] + weight
    
    # Check for negative cycle
    for u in graph:
        for v, weight in graph[u]:
            if potentials[u] != float('inf') and potentials[u] + weight < potentials[v]:
                return None
    
    return potentials

def dijkstra(graph: Dict[int, List[Tuple[int, int]]], source: int, 
              potentials: Optional[Dict[int, float]] = None) -> Dict[int, float]:
    """
    Dijkstra's algorithm to compute shortest paths from a source vertex.
    
    Args:
        graph (Dict[int, List[Tuple[int, int]]]): Reweighted graph as adjacency list.
        source (int): Source vertex.
        potentials (Optional[Dict[int, float]]): Vertex potentials for correcting distances.
    
    Returns:
        Dict[int, float]: Dictionary of shortest path distances from source to each vertex.
    """
    # If no potentials provided, initialize to zeros
    if potentials is None:
        potentials = {v: 0 for v in graph}
    
    # Initialize distances and priority queue
    distances = {v: float('inf') for v in graph}
    distances[source] = 0
    pq = [(0, source)]
    
    while pq:
        current_distance, u = heapq.heappop(pq)
        
        # If we've found a longer path, skip
        if current_distance > distances[u]:
            continue
        
        # Check all neighboring vertices
        for v, weight in graph[u]:
            # Calculate distance with reweighting correction
            distance = current_distance + weight
            
            # Update if a shorter path is found
            if distance < distances[v]:
                distances[v] = distance
                heapq.heappush(pq, (distance, v))
    
    # Correct distances back to original graph
    for v in distances:
        distances[v] += potentials[v] - potentials[source]
    
    return distances
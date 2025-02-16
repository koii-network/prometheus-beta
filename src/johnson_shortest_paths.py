import heapq
from typing import List, Dict, Optional, Tuple

def johnson_shortest_paths(graph: Dict[int, List[Tuple[int, int]]]) -> Dict[int, Dict[int, float]]:
    """
    Implement Johnson's algorithm to find shortest paths between all pairs of vertices.
    
    Args:
        graph (Dict[int, List[Tuple[int, int]]]): Adjacency list representation of the graph. 
                Each key is a vertex, and the value is a list of (destination, weight) tuples.
    
    Returns:
        Dict[int, Dict[int, float]]: A dictionary of shortest paths between all pairs of vertices.
    
    Raises:
        ValueError: If a negative cycle is detected in the graph.
    """
    # Step 1: Add a new source vertex
    def add_source_vertex(graph: Dict[int, List[Tuple[int, int]]]) -> Dict[int, List[Tuple[int, int]]]:
        new_graph = graph.copy()
        source = max(graph.keys()) + 1
        new_graph[source] = [(v, 0) for v in graph.keys()]
        return new_graph, source

    # Step 2: Bellman-Ford to compute vertex potentials
    def bellman_ford(graph: Dict[int, List[Tuple[int, int]]], source: int) -> Dict[int, float]:
        vertices = list(graph.keys())
        dist = {v: float('inf') for v in vertices}
        dist[source] = 0

        # Relax edges |V| - 1 times
        for _ in range(len(vertices) - 1):
            for u in vertices:
                for v, w in graph.get(u, []):
                    if dist[u] != float('inf') and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

        # Check for negative cycle
        for u in vertices:
            for v, w in graph.get(u, []):
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    raise ValueError("Graph contains a negative cycle")

        return dist

    # Step 3: Reweight the graph
    def reweight_graph(graph: Dict[int, List[Tuple[int, int]]], potentials: Dict[int, float]) -> Dict[int, List[Tuple[int, int]]]:
        reweighted = {}
        for u in graph:
            reweighted[u] = []
            for v, w in graph[u]:
                new_weight = w + potentials[u] - potentials[v]
                reweighted[u].append((v, new_weight))
        return reweighted

    # Step 4: Dijkstra for each vertex
    def dijkstra(graph: Dict[int, List[Tuple[int, int]]], source: int) -> Dict[int, float]:
        dist = {v: float('inf') for v in graph}
        dist[source] = 0
        pq = [(0, source)]

        while pq:
            current_dist, u = heapq.heappop(pq)

            # Skip if we've found a shorter path
            if current_dist > dist[u]:
                continue

            for v, w in graph.get(u, []):
                distance = current_dist + w
                if distance < dist[v]:
                    dist[v] = distance
                    heapq.heappush(pq, (distance, v))

        return dist

    # Main Johnson's algorithm implementation
    if not graph:
        return {}

    # Step 1: Add a source vertex
    augmented_graph, source = add_source_vertex(graph)

    # Step 2: Run Bellman-Ford to detect negative cycles and compute potentials
    vertex_potentials = bellman_ford(augmented_graph, source)

    # Remove the source vertex from the potentials
    vertex_potentials.pop(source)

    # Step 3: Reweight the graph
    reweighted_graph = reweight_graph(graph, vertex_potentials)

    # Step 4: Run Dijkstra for each vertex
    shortest_paths = {}
    for u in graph:
        dijkstra_dist = dijkstra(reweighted_graph, u)
        
        # Adjust distances back to original weights
        shortest_paths[u] = {
            v: (dist + vertex_potentials[v] - vertex_potentials[u]) 
            if dist != float('inf') else float('inf')
            for v, dist in dijkstra_dist.items()
        }

    return shortest_paths
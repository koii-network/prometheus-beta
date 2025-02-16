import heapq
from typing import List, Tuple, Dict

def prims_algorithm(graph: Dict[int, List[Tuple[int, int]]]) -> List[Tuple[int, int, int]]:
    """
    Implement Prim's algorithm to find the Minimum Spanning Tree (MST) of a weighted, undirected graph.
    
    Args:
    graph (Dict[int, List[Tuple[int, int]]]): Adjacency list representation of the graph
        where each key is a vertex, and the value is a list of (neighbor, weight) tuples.
    
    Returns:
    List[Tuple[int, int, int]]: List of edges in the Minimum Spanning Tree, 
        each represented as (source, destination, weight)
    
    Raises:
    ValueError: If the graph is empty or disconnected
    """
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Start with an arbitrary vertex (the first vertex in the graph)
    start_vertex = list(graph.keys())[0]
    
    # Set to keep track of vertices in the MST
    mst_vertices = set([start_vertex])
    
    # Priority queue to store edges
    edges_heap = []
    
    # Result list to store MST edges
    mst_edges = []
    
    # Add all edges from the start vertex to the heap
    for neighbor, weight in graph[start_vertex]:
        heapq.heappush(edges_heap, (weight, start_vertex, neighbor))
    
    # Continue until all vertices are included or no more edges can be added
    while edges_heap:
        weight, source, destination = heapq.heappop(edges_heap)
        
        # Skip if destination is already in MST
        if destination in mst_vertices:
            continue
        
        # Add destination to MST vertices
        mst_vertices.add(destination)
        
        # Add the edge to MST
        mst_edges.append((source, destination, weight))
        
        # Add edges from the new vertex
        for next_neighbor, next_weight in graph[destination]:
            if next_neighbor not in mst_vertices:
                heapq.heappush(edges_heap, (next_weight, destination, next_neighbor))
    
    # Check if the MST includes all vertices
    if len(mst_vertices) != len(graph):
        raise ValueError("Graph is not connected")
    
    return mst_edges
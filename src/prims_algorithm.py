import heapq
from typing import Dict, List, Tuple

def prims_algorithm(graph: Dict[str, Dict[str, int]]) -> List[Tuple[str, str, int]]:
    """
    Implement Prim's algorithm to find the minimum spanning tree of a graph.
    
    Args:
        graph (Dict[str, Dict[str, int]]): A graph represented as an adjacency list 
                                           where keys are vertices and values are 
                                           dictionaries of neighboring vertices and 
                                           their edge weights.
    
    Returns:
        List[Tuple[str, str, int]]: A list of edges in the minimum spanning tree, 
                                    where each edge is represented as 
                                    (source, destination, weight).
    
    Raises:
        ValueError: If the graph is empty or disconnected.
    """
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Choose an arbitrary starting vertex
    start_vertex = list(graph.keys())[0]
    
    # Set to keep track of vertices in the minimum spanning tree
    mst_vertices = set([start_vertex])
    
    # Minimum heap to select the minimum weight edge
    edges_heap = []
    
    # Result list to store the minimum spanning tree edges
    mst_edges = []
    
    # Add initial edges from the start vertex
    for neighbor, weight in graph[start_vertex].items():
        heapq.heappush(edges_heap, (weight, start_vertex, neighbor))
    
    while edges_heap:
        weight, source, destination = heapq.heappop(edges_heap)
        
        # Skip if destination is already in MST
        if destination in mst_vertices:
            continue
        
        # Add the edge to MST
        mst_vertices.add(destination)
        mst_edges.append((source, destination, weight))
        
        # Add new edges from the newly added vertex
        for next_neighbor, next_weight in graph[destination].items():
            if next_neighbor not in mst_vertices:
                heapq.heappush(edges_heap, (next_weight, destination, next_neighbor))
    
    # Check if the graph is fully connected
    if len(mst_vertices) != len(graph):
        raise ValueError("Graph is not connected")
    
    return mst_edges
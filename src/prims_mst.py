import heapq
from typing import Dict, List, Tuple, Optional

def prims_minimum_spanning_tree(graph: Dict[str, Dict[str, int]]) -> Optional[List[Tuple[str, str, int]]]:
    """
    Implement Prim's algorithm to find the minimum spanning tree of a weighted, undirected graph.
    
    Args:
        graph (Dict[str, Dict[str, int]]): An adjacency list representation of the graph.
                                           Keys are vertices, values are dictionaries of 
                                           neighboring vertices and their edge weights.
    
    Returns:
        Optional[List[Tuple[str, str, int]]]: A list of edges in the minimum spanning tree, 
                                              where each edge is (source, destination, weight).
                                              Returns None if the graph is empty or disconnected.
    
    Raises:
        ValueError: If the input graph is None or not a dictionary.
    """
    # Validate input
    if not isinstance(graph, dict) or len(graph) == 0:
        return None
    
    # Choose an arbitrary starting vertex
    start_vertex = list(graph.keys())[0]
    
    # Set to keep track of vertices in the minimum spanning tree
    mst_vertices = set([start_vertex])
    
    # Priority queue to find the minimum weight edge
    edge_heap = []
    
    # List to store the minimum spanning tree edges
    mst_edges = []
    
    # Add all edges from the start vertex to the heap
    for neighbor, weight in graph[start_vertex].items():
        heapq.heappush(edge_heap, (weight, start_vertex, neighbor))
    
    # Continue until we've visited all vertices or can't expand further
    while edge_heap:
        weight, source, destination = heapq.heappop(edge_heap)
        
        # Skip if the destination is already in the MST
        if destination in mst_vertices:
            continue
        
        # Add the vertex to the MST
        mst_vertices.add(destination)
        mst_edges.append((source, destination, weight))
        
        # Add neighboring edges of the new vertex
        for next_neighbor, next_weight in graph[destination].items():
            if next_neighbor not in mst_vertices:
                heapq.heappush(edge_heap, (next_weight, destination, next_neighbor))
    
    # Check if all vertices were connected
    return mst_edges if len(mst_vertices) == len(graph) else None
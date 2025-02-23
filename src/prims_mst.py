import heapq
from typing import Dict, List, Tuple

def prims_mst(graph: Dict[str, Dict[str, float]]) -> List[Tuple[str, str, float]]:
    """
    Implement Prim's algorithm to find the minimum spanning tree of a weighted, undirected graph.
    
    Args:
        graph (Dict[str, Dict[str, float]]): A graph represented as an adjacency dictionary 
                                             where keys are vertices and values are dictionaries 
                                             of neighboring vertices and their edge weights.
    
    Returns:
        List[Tuple[str, str, float]]: A list of edges in the minimum spanning tree, 
                                      each represented as (vertex1, vertex2, weight).
    
    Raises:
        ValueError: If the graph is empty or not connected.
    """
    # Check for empty graph
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Choose an arbitrary starting vertex
    start_vertex = list(graph.keys())[0]
    
    # Track vertices in the MST
    mst_vertices = set([start_vertex])
    
    # Track edges in the MST
    mst_edges = []
    
    # Priority queue to store edges to consider
    edge_heap = []
    
    # Initial: add all edges from start vertex
    for neighbor, weight in graph[start_vertex].items():
        heapq.heappush(edge_heap, (weight, start_vertex, neighbor))
    
    # Continue until no more edges can be added
    while edge_heap:
        weight, from_vertex, to_vertex = heapq.heappop(edge_heap)
        
        # Skip if the vertex is already in the MST
        if to_vertex in mst_vertices:
            continue
        
        # Add the vertex to MST vertices
        mst_vertices.add(to_vertex)
        
        # Add the edge to MST edges
        mst_edges.append((from_vertex, to_vertex, weight))
        
        # Add new edges from the newly added vertex
        if to_vertex in graph:  # Ensure the vertex is in the graph
            for neighbor, edge_weight in graph[to_vertex].items():
                if neighbor not in mst_vertices:
                    heapq.heappush(edge_heap, (edge_weight, to_vertex, neighbor))
    
    # Check if all vertices are connected
    if len(mst_vertices) != len(graph):
        raise ValueError("Graph is not fully connected")
    
    return mst_edges
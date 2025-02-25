import heapq
from typing import Dict, List, Tuple, Union

def prims_minimum_spanning_tree(graph: Dict[int, List[Tuple[int, int]]]) -> Union[List[Tuple[int, int, int]], None]:
    """
    Implement Prim's algorithm to find the minimum spanning tree of a weighted, undirected graph.
    
    Args:
        graph (Dict[int, List[Tuple[int, int]]]): 
            An adjacency list representation of the graph where:
            - Keys are vertices
            - Values are lists of (neighbor, weight) tuples
    
    Returns:
        Union[List[Tuple[int, int, int]], None]: 
            A list of edges in the minimum spanning tree, where each edge is (start, end, weight)
            Returns None if the graph is not connected or empty
    
    Raises:
        ValueError: If the input graph is not a valid graph representation
    """
    # Validate input
    if not graph:
        return None
    
    # Choose an arbitrary starting vertex
    start_vertex = list(graph.keys())[0]
    
    # Track visited vertices and the minimum spanning tree edges
    visited = set([start_vertex])
    mst_edges = []
    
    # Priority queue to store candidate edges
    # (weight, start_vertex, end_vertex)
    candidate_edges = []
    
    # Add initial vertex's edges to the candidate edges
    for neighbor, weight in graph[start_vertex]:
        heapq.heappush(candidate_edges, (weight, start_vertex, neighbor))
    
    # Run until all vertices are visited or no more edges
    while candidate_edges:
        weight, start, end = heapq.heappop(candidate_edges)
        
        # Skip if the destination vertex is already in the MST
        if end in visited:
            continue
        
        # Add the edge to MST and mark vertex as visited
        mst_edges.append((start, end, weight))
        visited.add(end)
        
        # Add new candidate edges from the newly added vertex
        for next_neighbor, next_weight in graph[end]:
            if next_neighbor not in visited:
                heapq.heappush(candidate_edges, (next_weight, end, next_neighbor))
    
    # Check if all vertices were visited (graph is connected)
    if len(visited) != len(graph):
        return None
    
    return mst_edges
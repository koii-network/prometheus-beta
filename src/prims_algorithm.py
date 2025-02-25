import heapq
from typing import Dict, List, Tuple, Union

def prims_minimum_spanning_tree(graph: Dict[str, Dict[str, float]]) -> Union[List[Tuple[str, str, float]], None]:
    """
    Implement Prim's algorithm to find the minimum spanning tree of a weighted, undirected graph.
    
    Args:
        graph (Dict[str, Dict[str, float]]): A graph represented as an adjacency dictionary 
                                             where keys are vertices and values are dictionaries 
                                             of neighboring vertices with their edge weights.
    
    Returns:
        Union[List[Tuple[str, str, float]], None]: A list of edges in the minimum spanning tree, 
                                                   where each edge is a tuple (vertex1, vertex2, weight).
                                                   Returns None if the graph is empty or disconnected.
    
    Raises:
        ValueError: If the input graph is not a valid graph representation.
    """
    # Validate input graph
    if not graph or not isinstance(graph, dict):
        raise ValueError("Input must be a non-empty dictionary representing a graph")
    
    # If graph is empty, return None
    if len(graph) == 0:
        return None
    
    # Select an arbitrary starting vertex
    start_vertex = list(graph.keys())[0]
    
    # Set to keep track of visited vertices
    visited = set([start_vertex])
    
    # Minimum spanning tree edges
    mst_edges = []
    
    # Priority queue to select minimum weight edge
    pq = []
    
    # Add all edges from the starting vertex to the priority queue
    for neighbor, weight in graph[start_vertex].items():
        heapq.heappush(pq, (weight, tuple(sorted((start_vertex, neighbor))), start_vertex, neighbor))
    
    # Continue until all vertices are visited or no more edges can be added
    while pq and len(visited) < len(graph):
        weight, sorted_endpoints, from_vertex, to_vertex = heapq.heappop(pq)
        
        # Skip if the destination vertex is already visited
        if to_vertex in visited:
            continue
        
        # Add the edge to the minimum spanning tree
        mst_edges.append((*sorted_endpoints, weight))
        visited.add(to_vertex)
        
        # Add new edges from the newly visited vertex
        for neighbor, edge_weight in graph[to_vertex].items():
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, tuple(sorted((to_vertex, neighbor))), to_vertex, neighbor))
    
    # Check if all vertices are connected
    if len(visited) < len(graph):
        return None
    
    return mst_edges
import heapq
from typing import Dict, List, Tuple

def prims_algorithm(graph: Dict[str, Dict[str, int]]) -> List[Tuple[str, str, int]]:
    """
    Implement Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph.
    
    Args:
        graph (Dict[str, Dict[str, int]]): A graph represented as an adjacency list 
                                           where keys are vertices and values are 
                                           dictionaries of neighboring vertices and 
                                           their edge weights.
    
    Returns:
        List[Tuple[str, str, int]]: A list of edges in the Minimum Spanning Tree, 
                                    where each edge is represented as (source, destination, weight)
    
    Raises:
        ValueError: If the graph is empty or not connected
    """
    # Check if graph is empty
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Choose an arbitrary starting vertex
    start_vertex = list(graph.keys())[0]
    
    # Initialize data structures
    mst = []  # Minimum Spanning Tree edges
    visited = set([start_vertex])  # Set of visited vertices
    edges_heap = []  # Priority queue to store edges
    
    # Add all edges from the start vertex to the heap
    for neighbor, weight in graph[start_vertex].items():
        heapq.heappush(edges_heap, (weight, start_vertex, neighbor))
    
    # Continue until all vertices are visited
    while edges_heap:
        weight, source, destination = heapq.heappop(edges_heap)
        
        # Skip if destination is already visited
        if destination in visited:
            continue
        
        # Add the edge to MST and mark destination as visited
        mst.append((source, destination, weight))
        visited.add(destination)
        
        # Add edges from the new vertex to the heap
        for next_neighbor, next_weight in graph[destination].items():
            if next_neighbor not in visited:
                heapq.heappush(edges_heap, (next_weight, destination, next_neighbor))
    
    # Check if the graph is connected
    if len(visited) != len(graph):
        raise ValueError("Graph is not connected")
    
    return mst
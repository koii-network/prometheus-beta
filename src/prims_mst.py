import heapq
from typing import Dict, List, Tuple, Union

def prims_mst(graph: Dict[str, Dict[str, float]]) -> Union[List[Tuple[str, str, float]], None]:
    """
    Implement Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph.
    
    Args:
        graph (Dict[str, Dict[str, float]]): A weighted, undirected graph represented 
                                             as an adjacency dictionary where each key 
                                             is a node, and the value is a dictionary 
                                             of neighboring nodes and their edge weights.
    
    Returns:
        Union[List[Tuple[str, str, float]], None]: A list of edges in the MST, 
                                                   where each edge is represented as 
                                                   (source, destination, weight). 
                                                   Returns None if the graph is empty 
                                                   or disconnected.
    
    Raises:
        TypeError: If the input is not a dictionary
        ValueError: If the graph structure is invalid
    
    Example:
        >>> graph = {
        ...     'A': {'B': 4, 'C': 2},
        ...     'B': {'A': 4, 'C': 1, 'D': 5},
        ...     'C': {'A': 2, 'B': 1, 'D': 8},
        ...     'D': {'B': 5, 'C': 8}
        ... }
        >>> prims_mst(graph)
        [('A', 'C', 2), ('C', 'B', 1), ('B', 'D', 5)]
    """
    # Validate input type
    if not isinstance(graph, dict):
        raise TypeError("Input must be a dictionary representing a graph")
    
    # Handle empty graph
    if not graph:
        return None
    
    # Choose an arbitrary start node (first node in the graph)
    start_node = next(iter(graph), None)
    if start_node is None:
        return None
    
    # Initialize data structures
    mst = []  # List to store the MST edges
    visited = set([start_node])  # Set of visited nodes
    edges = []  # Priority queue of edges to consider
    
    # Add all edges from the start node to the priority queue
    for neighbor, weight in graph[start_node].items():
        heapq.heappush(edges, (weight, start_node, neighbor))
    
    # Continue until all reachable nodes are visited
    while edges:
        # Get the minimum weight edge
        weight, src, dest = heapq.heappop(edges)
        
        # Skip if destination is already visited
        if dest in visited:
            continue
        
        # Add the edge to MST and mark destination as visited
        mst.append((src, dest, weight))
        visited.add(dest)
        
        # Add new edges from the newly visited node
        for next_neighbor, next_weight in graph[dest].items():
            if next_neighbor not in visited:
                heapq.heappush(edges, (next_weight, dest, next_neighbor))
    
    # Check if all nodes were visited (graph is connected)
    return mst if len(visited) == len(graph) else None
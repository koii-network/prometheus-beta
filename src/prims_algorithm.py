import heapq
from typing import List, Tuple, Dict

def prims_algorithm(graph: Dict[int, List[Tuple[int, int]]]) -> List[Tuple[int, int, int]]:
    """
    Implement Prim's algorithm to find the Minimum Spanning Tree (MST) of a graph.
    
    Args:
        graph (Dict[int, List[Tuple[int, int]]]): Adjacency list representation of the graph. 
                Each key is a vertex, and the value is a list of (destination, weight) tuples.
    
    Returns:
        List[Tuple[int, int, int]]: List of edges in the Minimum Spanning Tree, 
                                    each represented as (source, destination, weight)
    
    Raises:
        ValueError: If the graph is empty or not connected
    """
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Start with an arbitrary node (the first node in the graph)
    start_node = list(graph.keys())[0]
    
    # Track visited nodes and the MST edges
    visited = set()
    mst_edges = []
    
    # Priority queue to select the minimum weight edge
    pq = [(0, start_node, None)]  # (weight, current_node, parent_node)
    
    while pq:
        weight, current_node, parent_node = heapq.heappop(pq)
        
        # Skip if node already visited
        if current_node in visited:
            continue
        
        # Mark node as visited
        visited.add(current_node)
        
        # Add edge to MST if not the starting node
        if parent_node is not None:
            mst_edges.append((parent_node, current_node, weight))
        
        # Explore neighbors
        for neighbor, edge_weight in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, neighbor, current_node))
    
    # Check if all nodes are visited (graph is connected)
    if len(visited) != len(graph):
        raise ValueError("Graph is not connected")
    
    return mst_edges
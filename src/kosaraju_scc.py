from typing import List, Dict, Set

def kosaraju_strongly_connected_components(graph: Dict[int, List[int]]) -> List[List[int]]:
    """
    Find strongly connected components in a directed graph using Kosaraju's Algorithm.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph.
                                      Keys are vertices, values are lists of adjacent vertices.
    
    Returns:
        List[List[int]]: List of strongly connected components, where each component 
                         is a list of vertices.
    
    Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
    Space Complexity: O(V)
    """
    def dfs_first_pass(node: int, visited: Set[int], stack: List[int]):
        """First DFS pass to fill the stack."""
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_first_pass(neighbor, visited, stack)
        stack.append(node)

    def dfs_second_pass(node: int, visited: Set[int], component: List[int], reversed_graph: Dict[int, List[int]]):
        """Second DFS pass to identify strongly connected components."""
        visited.add(node)
        component.append(node)
        for neighbor in reversed_graph.get(node, []):
            if neighbor not in visited:
                dfs_second_pass(neighbor, visited, component, reversed_graph)

    # First create a reversed graph
    reversed_graph = {}
    for vertex, neighbors in graph.items():
        for neighbor in neighbors:
            reversed_graph.setdefault(neighbor, []).append(vertex)
        # Ensure all vertices are in the reversed graph, even if they have no outgoing edges
        reversed_graph.setdefault(vertex, [])

    # First pass: Fill stack by order of finishing times
    visited_first = set()
    stack = []
    for vertex in graph:
        if vertex not in visited_first:
            dfs_first_pass(vertex, visited_first, stack)

    # Second pass: Find SCCs using the reversed graph
    visited_second = set()
    strongly_connected_components = []

    while stack:
        node = stack.pop()
        if node not in visited_second:
            component = []
            dfs_second_pass(node, visited_second, component, reversed_graph)
            strongly_connected_components.append(component)

    return strongly_connected_components
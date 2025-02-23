from typing import List, Dict, Set

def kosaraju_scc(graph: Dict[int, List[int]]) -> List[List[int]]:
    """
    Find strongly connected components in a directed graph using Kosaraju's Algorithm.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph.
                                      Keys are nodes, values are lists of adjacent nodes.
    
    Returns:
        List[List[int]]: List of strongly connected components, where each component 
                         is a list of nodes that are mutually reachable.
    
    Raises:
        ValueError: If the input graph is None or empty.
    """
    # Validate input
    if graph is None or len(graph) == 0:
        raise ValueError("Graph cannot be None or empty")
    
    # Step 1: First DFS to get finishing times
    def first_dfs(node: int, visited: Set[int], stack: List[int]) -> None:
        """Perform first DFS and fill the stack."""
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                first_dfs(neighbor, visited, stack)
        stack.append(node)
    
    # Step 2: Transpose the graph
    def transpose_graph(original_graph: Dict[int, List[int]]) -> Dict[int, List[int]]:
        """Create the transposed graph with reversed edges."""
        transposed = {node: [] for node in original_graph}
        for node, neighbors in original_graph.items():
            for neighbor in neighbors:
                transposed.setdefault(neighbor, []).append(node)
        return transposed
    
    # Step 3: Second DFS to find SCCs
    def second_dfs(node: int, visited: Set[int], 
                   transposed_graph: Dict[int, List[int]], 
                   current_scc: List[int]) -> None:
        """Perform second DFS to find strongly connected components."""
        visited.add(node)
        current_scc.append(node)
        for neighbor in transposed_graph.get(node, []):
            if neighbor not in visited:
                second_dfs(neighbor, visited, transposed_graph, current_scc)
    
    # Main algorithm implementation
    # Nodes tracking
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors)
    
    # First pass: get nodes in order of finishing times
    visited_first = set()
    stack = []
    for node in all_nodes:
        if node not in visited_first:
            first_dfs(node, visited_first, stack)
    
    # Transpose the graph
    transposed_graph = transpose_graph(graph)
    
    # Second pass: find strongly connected components
    visited_second = set()
    strongly_connected_components = []
    
    while stack:
        node = stack.pop()
        if node not in visited_second:
            current_scc = []
            second_dfs(node, visited_second, transposed_graph, current_scc)
            strongly_connected_components.append(current_scc)
    
    return strongly_connected_components
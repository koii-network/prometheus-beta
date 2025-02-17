from typing import List, Dict

def kosaraju_strongly_connected_components(graph: Dict[int, List[int]]) -> List[List[int]]:
    """
    Find strongly connected components in a directed graph using Kosaraju's Algorithm.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph.
        
    Returns:
        List[List[int]]: List of strongly connected components.
    
    Raises:
        ValueError: If the graph is empty.
    """
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    def dfs_first_pass(node: int):
        """First DFS to compute finishing times."""
        visited[node] = True
        for neighbor in graph.get(node, []):
            if not visited.get(neighbor, False):
                dfs_first_pass(neighbor)
        stack.append(node)
    
    def dfs_second_pass(node: int, component: List[int]):
        """Second DFS to find strongly connected components."""
        visited[node] = True
        component.append(node)
        for neighbor in reversed_graph.get(node, []):
            if not visited.get(neighbor, False):
                dfs_second_pass(neighbor, component)
    
    # Create list of nodes
    nodes = list(graph.keys())
    
    # First pass: DFS and fill stack
    visited = {}
    stack = []
    for node in nodes:
        if not visited.get(node, False):
            dfs_first_pass(node)
    
    # Create reversed graph
    reversed_graph = {}
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            reversed_graph.setdefault(neighbor, []).append(node)
    
    # Second pass: Find SCCs
    visited = {}
    strongly_connected_components = []
    
    while stack:
        node = stack.pop()
        if not visited.get(node, False):
            component = []
            dfs_second_pass(node, component)
            strongly_connected_components.append(component)
    
    return strongly_connected_components
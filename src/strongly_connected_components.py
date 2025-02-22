from typing import List, Dict
from collections import defaultdict

def kosaraju_scc(graph: Dict[int, List[int]]) -> List[List[int]]:
    """
    Find strongly connected components in a directed graph using Kosaraju's Algorithm.
    
    :param graph: A dictionary representing the graph where keys are nodes and values are adjacency lists
    :return: A list of strongly connected components, where each component is a list of nodes
    """
    def dfs_first_pass(node):
        """First DFS pass to generate finishing times."""
        visited[node] = True
        for neighbor in graph.get(node, []):
            if not visited.get(neighbor, False):
                dfs_first_pass(neighbor)
        stack.append(node)
    
    def dfs_second_pass(node, component):
        """Second DFS pass to find strongly connected components."""
        visited[node] = True
        component.append(node)
        for neighbor in reversed_graph.get(node, []):
            if not visited.get(neighbor, False):
                dfs_second_pass(neighbor, component)
    
    # Input validation
    if not graph:
        return []
    
    # First pass: DFS and fill stack
    visited = {}
    stack = []
    for node in graph:
        if not visited.get(node, False):
            dfs_first_pass(node)
    
    # Create reversed graph
    reversed_graph = defaultdict(list)
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            reversed_graph[neighbor].append(node)
    
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
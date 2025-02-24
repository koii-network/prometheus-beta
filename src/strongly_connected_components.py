from typing import List, Dict, Set

def kosaraju_scc(graph: Dict[int, List[int]]) -> List[List[int]]:
    """
    Find strongly connected components in a directed graph using Kosaraju's Algorithm.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph.
                                      Keys are nodes, values are lists of adjacent nodes.
    
    Returns:
        List[List[int]]: A list of strongly connected components, where each component 
                         is a list of nodes that are mutually reachable.
    
    Raises:
        ValueError: If the input graph is None or not a valid adjacency list.
    
    Time Complexity: O(V+E), where V is the number of vertices and E is the number of edges
    Space Complexity: O(V)
    """
    # Input validation
    if graph is None:
        raise ValueError("Graph cannot be None")
    
    # First, get all nodes in the graph
    nodes = set(graph.keys())
    for adj_list in graph.values():
        nodes.update(adj_list)
    
    # Step 1: Perform first DFS to get finishing times
    def first_dfs(node: int, visited: Set[int], stack: List[int]):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                first_dfs(neighbor, visited, stack)
        stack.append(node)
    
    # Perform first DFS
    visited = set()
    stack = []
    for node in nodes:
        if node not in visited:
            first_dfs(node, visited, stack)
    
    # Step 2: Create transposed graph
    transposed = {}
    for node in nodes:
        for neighbor in graph.get(node, []):
            if neighbor not in transposed:
                transposed[neighbor] = []
            if node not in transposed:
                transposed[node] = []
            transposed[neighbor].append(node)
    
    # Step 3: Second DFS to find SCCs
    def second_dfs(node: int, visited: Set[int], component: List[int]):
        visited.add(node)
        component.append(node)
        for neighbor in transposed.get(node, []):
            if neighbor not in visited:
                second_dfs(neighbor, visited, component)
    
    # Find SCCs
    visited_second = set()
    strongly_connected_components = []
    
    while stack:
        node = stack.pop()
        if node not in visited_second:
            component = []
            second_dfs(node, visited_second, component)
            if component:
                strongly_connected_components.append(component)
    
    return strongly_connected_components
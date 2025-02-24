from typing import List, Dict, Set

def kosaraju_scc(graph: Dict[int, List[int]]) -> List[List[int]]:
    """
    Find strongly connected components in a directed graph using Kosaraju's Algorithm.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph.
                                      Keys are vertices, values are lists of adjacent vertices.
    
    Returns:
        List[List[int]]: List of strongly connected components, where each component 
                         is a list of vertices.
    
    Raises:
        ValueError: If the input graph is empty or None.
    """
    # Validate input
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # Step 1: First DFS to create finish times order
    def first_dfs(graph: Dict[int, List[int]]) -> List[int]:
        visited = set()
        stack = []
        
        def dfs(node: int):
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)
            stack.append(node)
        
        # Run DFS on all unvisited nodes
        for node in graph:
            if node not in visited:
                dfs(node)
        
        return stack
    
    # Step 2: Transpose the graph (reverse all edges)
    def transpose_graph(graph: Dict[int, List[int]]) -> Dict[int, List[int]]:
        transposed = {node: [] for node in graph}
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                transposed[neighbor].append(node)
        return transposed
    
    # Step 3: Second DFS to find SCCs
    def second_dfs(graph: Dict[int, List[int]], nodes: List[int]) -> List[List[int]]:
        visited = set()
        strongly_connected_components = []
        
        def dfs(node: int, component: List[int]):
            visited.add(node)
            component.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor, component)
        
        # Run DFS in order of finish times
        for node in reversed(nodes):
            if node not in visited:
                component = []
                dfs(node, component)
                if component:
                    strongly_connected_components.append(component)
        
        return strongly_connected_components
    
    # Main Kosaraju Algorithm
    finish_times = first_dfs(graph)
    transposed_graph = transpose_graph(graph)
    
    return second_dfs(transposed_graph, finish_times)
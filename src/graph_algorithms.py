from typing import List, Dict, Set

def kosaraju_scc(graph: Dict[int, List[int]]) -> List[List[int]]:
    """
    Find strongly connected components in a directed graph using Kosaraju's algorithm.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph.
                                      Keys are vertices, values are lists of adjacent vertices.
    
    Returns:
        List[List[int]]: A list of strongly connected components, where each component 
                         is a list of vertices.
    
    Raises:
        ValueError: If the input graph is empty.
    """
    if not graph:
        raise ValueError("Graph cannot be empty")
    
    # First DFS to get finishing times (topological sort)
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
    
    # Reverse the graph
    def reverse_graph(graph: Dict[int, List[int]]) -> Dict[int, List[int]]:
        reversed_graph = {}
        for node, neighbors in graph.items():
            # Ensure all nodes are in the reversed graph
            if node not in reversed_graph:
                reversed_graph[node] = []
            
            for neighbor in neighbors:
                if neighbor not in reversed_graph:
                    reversed_graph[neighbor] = []
                reversed_graph[neighbor].append(node)
        
        return reversed_graph
    
    # Second DFS to find SCCs
    def second_dfs(reversed_graph: Dict[int, List[int]], node: int, visited: Set[int]) -> List[int]:
        component = []
        visited.add(node)
        component.append(node)
        
        for neighbor in reversed_graph.get(node, []):
            if neighbor not in visited:
                component.extend(second_dfs(reversed_graph, neighbor, visited))
        
        return component
    
    # Main Kosaraju algorithm steps
    # 1. First DFS and create stack of vertices by finishing times
    finishing_stack = first_dfs(graph)
    
    # 2. Reverse the graph
    reversed_graph = reverse_graph(graph)
    
    # 3. Second DFS on reversed graph
    visited = set()
    strongly_connected_components = []
    
    # Traverse nodes in order of decreasing finishing times
    while finishing_stack:
        node = finishing_stack.pop()
        if node not in visited:
            component = second_dfs(reversed_graph, node, visited)
            strongly_connected_components.append(component)
    
    return strongly_connected_components
from typing import Dict, List, Any, Set

def depth_first_search(graph: Dict[Any, List[Any]], start: Any) -> List[Any]:
    """
    Perform Depth-First Search on a graph.
    
    :param graph: A dictionary representing an adjacency list graph
    :param start: The starting node for the DFS
    :return: A list of nodes in the order they were visited
    
    Example:
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    depth_first_search(graph, 'A')  # Possible output: ['A', 'B', 'D', 'E', 'F', 'C']
    """
    # Handle empty graph or start node not in graph
    if not graph or start not in graph:
        return []
    
    # Set to keep track of visited nodes to prevent cycles
    visited: Set[Any] = set()
    
    # List to store the order of nodes visited
    traversal_order: List[Any] = []
    
    def dfs_recursive(node: Any):
        """
        Recursive helper function for depth-first search
        """
        # Mark the current node as visited
        visited.add(node)
        
        # Add the current node to traversal order
        traversal_order.append(node)
        
        # Explore unvisited neighbors
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_recursive(neighbor)
    
    # Start DFS from the start node
    dfs_recursive(start)
    
    return traversal_order
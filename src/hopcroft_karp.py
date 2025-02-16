from typing import Dict, List, Set, Union

def hopcroft_karp_matching(graph: Dict[int, Union[List[int], int]]) -> Dict[int, int]:
    """
    Implement the Hopcroft-Karp algorithm for maximum matching in a bipartite graph.
    
    Args:
        graph (Dict[int, Union[List[int], int]]): A bipartite graph represented as an adjacency list.
                                                  Keys are nodes from the first set, 
                                                  Values are lists of adjacent nodes or a single node
    
    Returns:
        Dict[int, int]: A maximum matching where keys are nodes from the first set 
                        and values are their matched nodes from the second set.
    
    Raises:
        ValueError: If the input graph is not a valid bipartite graph dictionary.
    """
    # Validate and convert input graph
    if not isinstance(graph, dict):
        raise ValueError("Input must be a dictionary representing a bipartite graph")
    
    # Normalize graph to ensure all values are lists
    normalized_graph = {}
    for key, value in graph.items():
        if isinstance(value, int):
            normalized_graph[key] = [value]
        elif isinstance(value, list):
            normalized_graph[key] = value
        else:
            raise ValueError(f"Invalid graph structure for key {key}")
    
    # Find all nodes in the second set
    second_set = set()
    for adjacent_nodes in normalized_graph.values():
        second_set.update(adjacent_nodes)
    
    # Initialize matching and tracking variables
    matching = {}  # Matched nodes
    dist = {}      # Distance for BFS
    NIL = 0        # Sentinel value for unmatched nodes
    
    def bfs() -> bool:
        """Breadth-first search to find augmenting paths."""
        queue = []
        
        # Initialize distances for each node
        for u in normalized_graph:
            if matching.get(u, NIL) == NIL:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        
        dist[NIL] = float('inf')
        
        while queue:
            u = queue.pop(0)
            if dist[u] < dist[NIL]:
                for v in normalized_graph[u]:
                    # Check if the matched node (if exists) can be reassigned
                    w = next((key for key, val in matching.items() if val == v), NIL)
                    if dist[w] == float('inf'):
                        dist[w] = dist[u] + 1
                        queue.append(w)
        
        return dist[NIL] != float('inf')
    
    def dfs(u: int) -> bool:
        """Depth-first search to find augmenting paths."""
        if u != NIL:
            for v in normalized_graph[u]:
                # Check the matched node (if exists)
                w = next((key for key, val in matching.items() if val == v), NIL)
                
                # If no match exists or can be rematched
                if dist[w] == dist[u] + 1:
                    if dfs(w):
                        matching[u] = v
                        matching[v] = u
                        return True
            
            # Mark this node as not part of an augmenting path
            dist[u] = float('inf')
            return False
        
        return True
    
    # Main matching algorithm
    while bfs():
        for u in normalized_graph:
            if matching.get(u, NIL) == NIL:
                dfs(u)
    
    # Return only matches for nodes in the original graph
    return {k: v for k, v in matching.items() if k in normalized_graph}
from typing import Dict, List, Set, Optional

def hopcroft_karp_maximum_matching(graph: Dict[int, List[int]]) -> Dict[int, Optional[int]]:
    """
    Implement the Hopcroft-Karp algorithm for maximum matching in a bipartite graph.
    
    Args:
        graph (Dict[int, List[int]]): A bipartite graph represented as an adjacency list 
                                      where keys are nodes and values are lists of adjacent nodes.
    
    Returns:
        Dict[int, Optional[int]]: A maximum matching where keys are nodes and values 
                                  are their matched partners (or None if unmatched).
    
    Raises:
        ValueError: If the input graph is not a valid dictionary.
    """
    # Validate input
    if not isinstance(graph, dict):
        raise ValueError("Input must be a dictionary representing a graph")
    
    # Initialize matching and tracking data structures
    matching: Dict[int, Optional[int]] = {}
    dist: Dict[int, int] = {}
    
    def bfs() -> bool:
        """Breadth-first search to find augmenting paths."""
        queue = []
        
        # Check nodes in the left set
        for u in graph:
            if matching.get(u) is None:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        
        dist[None] = float('inf')
        
        while queue:
            u = queue.pop(0)
            
            if dist[u] < dist[None]:
                for v in graph.get(u, []):
                    # If the matched node is not yet processed
                    if dist.get(matching.get(v), float('inf')) == float('inf'):
                        dist[matching.get(v)] = dist[u] + 1
                        queue.append(matching.get(v))
        
        return dist[None] != float('inf')
    
    def dfs(u: Optional[int]) -> bool:
        """Depth-first search to find augmenting paths."""
        if u is None:
            return True
        
        for v in graph.get(u, []):
            # Check if this is a valid augmenting path
            if dist.get(matching.get(v), float('inf')) == dist[u] + 1:
                if dfs(matching.get(v)):
                    matching[u] = v
                    matching[v] = u
                    return True
        
        dist[u] = float('inf')
        return False
    
    # Find maximum matching
    while bfs():
        for u in graph:
            if matching.get(u) is None:
                dfs(u)
    
    return matching
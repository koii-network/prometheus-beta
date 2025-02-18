from typing import Dict, List, Set

def hopcroft_karp_matching(graph: Dict[int, List[int]]) -> Dict[int, int]:
    """
    Implement the Hopcroft-Karp algorithm for maximum matching in a bipartite graph.
    
    Args:
        graph (Dict[int, List[int]]): A bipartite graph represented as an adjacency list.
                                      Keys are vertices from the left partition,
                                      Values are lists of connected vertices in the right partition.
    
    Returns:
        Dict[int, int]: A maximum matching where keys are vertices from the left partition
                        and values are their matched vertices in the right partition.
    """
    # Initialize matching and graph properties
    matching: Dict[int, int] = {}  # Matching dictionary
    dist: Dict[int, int] = {}  # Distance for BFS
    
    def bfs() -> bool:
        """
        Breadth-first search to find augmenting paths.
        
        Returns:
            bool: True if an augmenting path exists, False otherwise.
        """
        queue = []
        
        # Check unmatched vertices in the left partition
        for u in graph.keys():
            if u not in matching:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = float('inf')
        
        dist[None] = float('inf')
        
        while queue:
            u = queue.pop(0)
            if dist[u] < dist[None]:
                for v in graph[u]:
                    # Check if v is not matched or can be unmatched
                    if dist.get(matching.get(v), float('inf')) == float('inf'):
                        dist[matching.get(v)] = dist[u] + 1
                        queue.append(matching.get(v))
        
        return dist[None] != float('inf')
    
    def dfs(u: int) -> bool:
        """
        Depth-first search to find and augment matching paths.
        
        Args:
            u (int): Current vertex in the left partition.
        
        Returns:
            bool: True if an augmenting path is found, False otherwise.
        """
        if u is not None:
            for v in graph[u]:
                # Check if this is a promising path in the BFS level graph
                if dist.get(matching.get(v), float('inf')) == dist[u] + 1:
                    if dfs(matching.get(v)):
                        matching[v] = u
                        matching[u] = v
                        return True
            
            # Mark this vertex as not part of any augmenting path
            dist[u] = float('inf')
            return False
        
        return True
    
    # Find maximum matching
    while bfs():
        for u in graph.keys():
            if u not in matching:
                dfs(u)
    
    return matching
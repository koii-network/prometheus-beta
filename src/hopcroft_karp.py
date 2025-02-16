from typing import Dict, List, Set, Optional

def hopcroft_karp_matching(graph: Dict[int, List[int]]) -> Dict[int, Optional[int]]:
    """
    Implement the Hopcroft-Karp algorithm for maximum matching in a bipartite graph.
    
    Args:
        graph (Dict[int, List[int]]): A bipartite graph represented as an adjacency list 
                                      where keys are vertices from the first set 
                                      and values are lists of connected vertices from the second set.
    
    Returns:
        Dict[int, Optional[int]]: A maximum matching where keys are vertices from the first set 
                                  and values are their matched vertices (or None if unmatched).
    
    Time Complexity: O(E * sqrt(V)), where E is the number of edges and V is the number of vertices.
    Space Complexity: O(V)
    """
    # Separate vertices into two sets (U and V)
    U = set(graph.keys())
    V = set(v for vertices in graph.values() for v in vertices)
    
    # Initialize matching
    match_u = {u: None for u in U}
    match_v = {v: None for v in V}
    
    def bfs() -> bool:
        """
        Perform BFS to find augmenting paths.
        
        Returns:
            bool: True if an augmenting path exists, False otherwise.
        """
        # Initialize level and queue for BFS
        level = {u: float('inf') for u in U}
        queue = []
        
        # Find unmatched vertices in U and add to queue
        for u in U:
            if match_u[u] is None:
                level[u] = 0
                queue.append(u)
        
        max_level = float('inf')
        
        # BFS traversal
        while queue:
            u = queue.pop(0)
            
            if level[u] > max_level:
                break
            
            for v in graph.get(u, []):
                # If the vertex in V is not matched
                if match_v[v] is None:
                    max_level = level[u] + 1
                
                # If the matched vertex of v has not been visited
                elif level[match_v[v]] == float('inf'):
                    level[match_v[v]] = level[u] + 1
                    queue.append(match_v[v])
        
        return max_level != float('inf')
    
    def dfs(u: int) -> bool:
        """
        Perform DFS to find augmenting paths for unmatched vertices.
        
        Args:
            u (int): Current vertex from set U.
        
        Returns:
            bool: True if an augmenting path is found, False otherwise.
        """
        if u is not None:
            for v in graph.get(u, []):
                # Check if the vertex in V is unmatched or has an augmenting path
                if level[match_v[v]] == level[u] + 1:
                    if match_v[v] is None or dfs(match_v[v]):
                        match_u[u] = v
                        match_v[v] = u
                        return True
            
            # Mark as visited and no augmenting path
            level[u] = float('inf')
            return False
        
        return True
    
    # Iterate to find maximum matching
    max_matching = 0
    while bfs():
        for u in U:
            if match_u[u] is None and dfs(u):
                max_matching += 1
    
    return match_u

def print_matching(matching: Dict[int, Optional[int]]) -> None:
    """
    Print the matching in a readable format.
    
    Args:
        matching (Dict[int, Optional[int]]): The matched vertices.
    """
    print("Maximum Matching:")
    for u, v in matching.items():
        if v is not None:
            print(f"{u} -> {v}")
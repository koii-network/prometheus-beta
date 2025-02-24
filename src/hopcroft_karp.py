from typing import Dict, List, Set

def hopcroft_karp_maximum_matching(graph: Dict[int, List[int]]) -> Dict[int, int]:
    """
    Implement the Hopcroft-Karp algorithm for maximum matching in a bipartite graph.
    
    Args:
        graph (Dict[int, List[int]]): A bipartite graph represented as an adjacency list.
                                      Keys are vertices from one set, values are lists of 
                                      connected vertices from the other set.
    
    Returns:
        Dict[int, int]: A maximum matching, where keys are vertices from the first set 
                        and values are their matched vertices from the second set.
    
    Raises:
        ValueError: If the graph is not a valid bipartite graph input.
    """
    # Validate input
    if not isinstance(graph, dict):
        raise ValueError("Graph must be a dictionary")
    
    # Find all vertices in the left and right sets
    left_vertices = set(graph.keys())
    right_vertices = set(v for vertices in graph.values() for v in vertices)
    
    # Initialize matching
    matching: Dict[int, int] = {}
    
    def bfs() -> Dict[int, int]:
        """Breadth-first search to find augmenting paths."""
        queue = []
        levels = {}
        
        # Initial level assignment
        for u in left_vertices:
            if u not in matching:
                levels[u] = 0
                queue.append(u)
            else:
                levels[u] = float('inf')
        
        max_level = float('inf')
        
        while queue:
            u = queue.pop(0)
            
            if levels[u] > max_level:
                break
            
            for v in graph.get(u, []):
                # If v is not matched
                if v not in matching or levels[matching[v]] == float('inf'):
                    if v not in matching:
                        max_level = levels[u]
                    
                    if matching.get(v) is None:
                        # Found augmenting path, update matching
                        path_u = u
                        path_v = v
                        while path_u is not None:
                            temp = matching.get(path_u)
                            matching[path_u] = path_v
                            matching[path_v] = path_u
                            path_u = temp
                            path_v = path_u
                        return matching
                    else:
                        # Continue BFS
                        w = matching[v]
                        levels[w] = levels[u] + 1
                        queue.append(w)
        
        return matching
    
    # Repeatedly find augmenting paths
    while True:
        old_matching_size = len(matching) // 2
        bfs()
        
        # If no new matches were found, we're done
        if len(matching) // 2 == old_matching_size:
            break
    
    return {k: v for k, v in matching.items() if k in left_vertices}
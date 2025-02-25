from typing import Dict, List, Optional, Set

class HopcroftKarp:
    """
    Implementation of the Hopcroft-Karp algorithm for maximum matching in a bipartite graph.
    
    The algorithm finds the maximum matching in a bipartite graph efficiently,
    with a time complexity of O(E * sqrt(V)), where E is the number of edges 
    and V is the number of vertices.
    """
    
    def __init__(self):
        """
        Initialize the Hopcroft-Karp algorithm data structures.
        """
        self.graph: Dict[int, List[int]] = {}
        self.matching: Dict[int, Optional[int]] = {}
        self.dist: Dict[int, int] = {}
        
    def add_edge(self, u: int, v: int):
        """
        Add an edge between vertices u and v in the bipartite graph.
        
        Args:
            u (int): Vertex from the first set
            v (int): Vertex from the second set
        """
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    
    def bfs(self, left_vertices: Set[int]) -> bool:
        """
        Breadth-first search to find augmenting paths.
        
        Args:
            left_vertices (Set[int]): Set of vertices from the left partition
        
        Returns:
            bool: True if an augmenting path is found, False otherwise
        """
        queue = []
        
        # Initialize distances for unmatched vertices in the left set
        for u in left_vertices:
            if self.matching.get(u) is None:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')
        
        # Set distance of null vertex to infinity
        self.dist[None] = float('inf')
        
        # BFS to find shortest augmenting paths
        while queue:
            u = queue.pop(0)
            
            if self.dist[u] < self.dist[None]:
                for v in self.graph.get(u, []):
                    # Find the matched vertex for v (if exists)
                    matched_with = next((x for x in self.matching if self.matching[x] == v), None)
                    
                    if self.dist.get(matched_with, float('inf')) == float('inf'):
                        self.dist[matched_with] = self.dist[u] + 1
                        queue.append(matched_with)
        
        # Return True if null vertex distance is not infinity
        return self.dist[None] != float('inf')
    
    def dfs(self, u: Optional[int]) -> bool:
        """
        Depth-first search to find augmenting paths.
        
        Args:
            u (Optional[int]): Current vertex to explore
        
        Returns:
            bool: True if an augmenting path is found
        """
        if u is not None:
            for v in self.graph.get(u, []):
                # Check if this is a valid path through the layers
                matched_with = next((x for x in self.matching if self.matching[x] == v), None)
                
                if (matched_with is None or 
                    (self.dist[matched_with] == self.dist[u] + 1 and 
                     self.dfs(matched_with))):
                    # Augment the matching
                    self.matching[u] = v
                    return True
            
            # No augmenting path found
            self.dist[u] = float('inf')
            return False
        
        return True
    
    def maximum_matching(self, left_vertices: Optional[Set[int]] = None) -> Dict[int, int]:
        """
        Find the maximum matching in the bipartite graph.
        
        Args:
            left_vertices (Optional[Set[int]], optional): Set of vertices in the left partition. 
                                                         Defaults to None (automatically inferred).
        
        Returns:
            Dict[int, int]: A dictionary representing the maximum matching
        """
        # If left vertices not provided, infer from the graph
        if left_vertices is None:
            left_vertices = set(self.graph.keys())
        
        # Reset matching
        self.matching.clear()
        
        # Find maximum matching
        while self.bfs(left_vertices):
            for u in left_vertices:
                if self.matching.get(u) is None:
                    self.dfs(u)
        
        # Return only the matched pairs
        return {u: v for u, v in self.matching.items() if v is not None}
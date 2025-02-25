from typing import Dict, List, Set, Optional

class HopcroftKarp:
    """
    Implementation of the Hopcroft-Karp algorithm for maximum matching in bipartite graphs.
    
    The algorithm finds the maximum matching in a bipartite graph efficiently 
    with a time complexity of O(E * sqrt(V)).
    
    Attributes:
        graph (Dict[int, List[int]]): Adjacency list representation of the bipartite graph
        matching (Dict[int, Optional[int]]): Stores the matched vertices
    """
    
    def __init__(self, graph: Dict[int, List[int]]):
        """
        Initialize the Hopcroft-Karp algorithm with a bipartite graph.
        
        Args:
            graph (Dict[int, List[int]]): A dictionary representing the bipartite graph 
                                          where keys are left set vertices and values 
                                          are lists of connected right set vertices.
        
        Raises:
            ValueError: If the input graph is not a valid dictionary
        """
        if not isinstance(graph, dict):
            raise ValueError("Graph must be a dictionary")
        
        self.graph = graph
        self.matching = {}
        self.dist = {}
    
    def bfs(self, left_vertices: Set[int]) -> bool:
        """
        Breadth-first search to find augmenting paths.
        
        Args:
            left_vertices (Set[int]): Set of vertices from the left partition
        
        Returns:
            bool: True if an augmenting path exists, False otherwise
        """
        queue = []
        
        # Initialize distances
        for v in left_vertices:
            if self.matching.get(v) is None:
                self.dist[v] = 0
                queue.append(v)
            else:
                self.dist[v] = float('inf')
        
        self.dist[None] = float('inf')
        
        while queue:
            v = queue.pop(0)
            
            if self.dist[v] < self.dist[None]:
                for u in self.graph.get(v, []):
                    # Find if u is already matched
                    matched_vertex = next((k for k, val in self.matching.items() if val == u), None)
                    
                    if matched_vertex is None:
                        # Unmatched edge found
                        self.dist[None] = self.dist[v] + 1
                    elif self.dist.get(matched_vertex, float('inf')) == float('inf'):
                        # Explore matched vertex's path
                        self.dist[matched_vertex] = self.dist[v] + 1
                        queue.append(matched_vertex)
        
        return self.dist[None] != float('inf')
    
    def dfs(self, v: Optional[int]) -> bool:
        """
        Depth-first search to find and extend augmenting paths.
        
        Args:
            v (Optional[int]): Current vertex to explore
        
        Returns:
            bool: True if an augmenting path is found, False otherwise
        """
        if v is not None:
            for u in self.graph.get(v, []):
                matched_vertex = next((k for k, val in self.matching.items() if val == u), None)
                
                if matched_vertex is None:
                    # Found an unmatched vertex
                    self.matching[v] = u
                    return True
                
                if self.dist.get(matched_vertex, float('inf')) == self.dist[v] + 1:
                    if self.dfs(matched_vertex):
                        self.matching[v] = u
                        return True
            
            self.dist[v] = float('inf')
            return False
        
        return True
    
    def maximum_matching(self) -> Dict[int, int]:
        """
        Compute the maximum matching in the bipartite graph.
        
        Returns:
            Dict[int, int]: A dictionary representing the maximum matching,
                            where keys are left set vertices and values are 
                            matched right set vertices.
        """
        # Reset matching and distance
        self.matching.clear()
        self.dist.clear()
        
        # Get all left vertices
        left_vertices = set(self.graph.keys())
        
        # Continue until no more augmenting paths can be found
        while self.bfs(left_vertices):
            for v in left_vertices:
                if self.matching.get(v) is None:
                    self.dfs(v)
        
        return self.matching
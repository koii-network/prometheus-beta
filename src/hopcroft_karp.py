from typing import Dict, List, Set, Optional


class HopcroftKarp:
    """
    Implementation of the Hopcroft-Karp algorithm for maximum matching in a bipartite graph.
    
    The algorithm finds the maximum matching in a bipartite graph in O(E sqrt(V)) time.
    
    Attributes:
        graph (Dict[int, List[int]]): Adjacency list representation of the bipartite graph
        left_vertices (Set[int]): Set of vertices in the left partition
        right_vertices (Set[int]): Set of vertices in the right partition
    """
    
    def __init__(self, graph: Dict[int, List[int]], left_vertices: Set[int], right_vertices: Set[int]):
        """
        Initialize the Hopcroft-Karp algorithm.
        
        Args:
            graph (Dict[int, List[int]]): Adjacency list of the bipartite graph
            left_vertices (Set[int]): Vertices in the left partition
            right_vertices (Set[int]): Vertices in the right partition
        
        Raises:
            ValueError: If graph is invalid or partitions are incorrect
        """
        self._validate_graph(graph, left_vertices, right_vertices)
        
        self.graph = graph
        self.left_vertices = left_vertices
        self.right_vertices = right_vertices
        
        # Matching from left to right
        self.pair_left = {}
        # Matching from right to left
        self.pair_right = {}
        
        # Distance for BFS
        self.dist = {}
        
    def _validate_graph(self, graph: Dict[int, List[int]], left_vertices: Set[int], right_vertices: Set[int]):
        """
        Validate the input graph and partitions.
        
        Args:
            graph (Dict[int, List[int]]): Adjacency list of the bipartite graph
            left_vertices (Set[int]): Vertices in the left partition
            right_vertices (Set[int]): Vertices in the right partition
        
        Raises:
            ValueError: If graph is invalid
        """
        # Check for empty sets
        if not left_vertices or not right_vertices:
            raise ValueError("Both left and right vertex sets must be non-empty")
        
        # Check for vertex disjointness
        if left_vertices & right_vertices:
            raise ValueError("Left and right vertex sets must be disjoint")
        
        # All vertices in graph must be in left or right partition
        all_vertices = set(graph.keys()).union(
            vertex for neighbors in graph.values() for vertex in neighbors
        )
        partitioned_vertices = left_vertices.union(right_vertices)
        
        if not all_vertices.issubset(partitioned_vertices):
            raise ValueError("All graph vertices must be in either left or right partition")
        
        # Verify all graph edges are between partitions
        for vertex, neighbors in graph.items():
            if vertex in left_vertices:
                if any(neighbor not in right_vertices for neighbor in neighbors):
                    raise ValueError(f"Invalid edge: {vertex} can only connect to right vertices")
            elif vertex in right_vertices:
                if any(neighbor not in left_vertices for neighbor in neighbors):
                    raise ValueError(f"Invalid edge: {vertex} can only connect to left vertices")
    
    def _bfs(self) -> bool:
        """
        Breadth-first search to find augmenting paths.
        
        Returns:
            bool: True if an augmenting path is found, False otherwise
        """
        queue = []
        
        # Initialize distances for unmatched left vertices
        for u in self.left_vertices:
            if u not in self.pair_left:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float('inf')
        
        # Default distance for unvisited vertices
        self.dist[None] = float('inf')
        
        # BFS to find shortest path
        while queue:
            u = queue.pop(0)
            
            if self.dist[u] < self.dist[None]:
                for v in self.graph.get(u, []):
                    # Check if the right vertex is unmatched or we can improve the path
                    w = self.pair_right.get(v)
                    
                    if self.dist[w] == float('inf'):
                        self.dist[w] = self.dist[u] + 1
                        queue.append(w)
        
        # Return True if we found an augmenting path
        return self.dist[None] != float('inf')
    
    def _dfs(self, u: Optional[int]) -> bool:
        """
        Depth-first search to find augmenting paths.
        
        Args:
            u (Optional[int]): Current vertex
        
        Returns:
            bool: True if an augmenting path is found, False otherwise
        """
        if u is not None:
            for v in self.graph.get(u, []):
                w = self.pair_right.get(v)
                
                # Found an augmenting path
                if self.dist[w] == self.dist[u] + 1:
                    if self._dfs(w):
                        self.pair_right[v] = u
                        self.pair_left[u] = v
                        return True
            
            # No augmenting path found
            self.dist[u] = float('inf')
            return False
        
        return True
    
    def maximum_matching(self) -> Dict[int, int]:
        """
        Find the maximum matching in the bipartite graph.
        
        Returns:
            Dict[int, int]: A dictionary representing the maximum matching
        """
        # Reset matching
        self.pair_left.clear()
        self.pair_right.clear()
        
        # Find maximum matching
        while self._bfs():
            for u in self.left_vertices:
                if u not in self.pair_left:
                    self._dfs(u)
        
        return self.pair_left
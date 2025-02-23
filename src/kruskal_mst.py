from typing import List, Tuple, Optional

class DisjointSet:
    """
    Disjoint Set (Union-Find) data structure to support Kruskal's algorithm.
    
    This class helps efficiently manage graph connectivity by:
    1. Finding the root/representative of a set
    2. Merging sets with path compression and union by rank
    """
    def __init__(self, vertices: int):
        """
        Initialize the Disjoint Set with given number of vertices.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices
    
    def find(self, item: int) -> int:
        """
        Find the root/representative of a set with path compression.
        
        :param item: Vertex to find the root for
        :return: Root/representative of the set
        """
        # Path compression: make every node point directly to the root
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x: int, y: int) -> bool:
        """
        Merge two sets using union by rank.
        
        :param x: First vertex
        :param y: Second vertex
        :return: True if sets were merged, False if already in same set
        """
        # Find roots of both sets
        root_x = self.find(x)
        root_y = self.find(y)
        
        # If already in same set, return False
        if root_x == root_y:
            return False
        
        # Union by rank: attach smaller rank tree under root of higher rank tree
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # If ranks are same, make one as root and increment its rank
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True

def kruskal_mst(num_vertices: int, edges: List[Tuple[int, int, int]]) -> Optional[List[Tuple[int, int, int]]]:
    """
    Find the Minimum Spanning Tree using Kruskal's algorithm.
    
    :param num_vertices: Number of vertices in the graph
    :param edges: List of edges with format (from, to, weight)
    :return: List of edges in the MST, or None if no MST exists
    
    Time Complexity: O(E log E), where E is the number of edges
    Space Complexity: O(V + E), where V is the number of vertices
    """
    # Validate input
    if not edges or num_vertices < 2:
        return None
    
    # Sort edges by weight in ascending order
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    # Initialize Disjoint Set
    disjoint_set = DisjointSet(num_vertices)
    
    # List to store edges in the Minimum Spanning Tree
    mst_edges = []
    
    # Iterate through sorted edges
    for edge in sorted_edges:
        u, v, weight = edge
        
        # If adding this edge doesn't create a cycle, add it to MST
        if disjoint_set.union(u, v):
            mst_edges.append(edge)
        
        # Stop when we have V-1 edges (complete MST)
        if len(mst_edges) == num_vertices - 1:
            break
    
    # Check if MST connects all vertices
    if len(mst_edges) != num_vertices - 1:
        return None
    
    return mst_edges
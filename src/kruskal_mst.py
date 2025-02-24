from typing import List, Tuple

class DisjointSet:
    """
    A data structure to perform Union-Find operations efficiently.
    
    This class helps in detecting cycles and connecting components 
    during Kruskal's algorithm implementation.
    """
    def __init__(self, vertices: int):
        """
        Initialize the DisjointSet with each vertex in its own set.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices
    
    def find(self, item: int) -> int:
        """
        Find the root/representative of a set with path compression.
        
        :param item: Vertex to find the root for
        :return: Root of the set containing the vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x: int, y: int) -> bool:
        """
        Merge two sets by rank to keep the tree balanced.
        
        :param x: First vertex
        :param y: Second vertex
        :return: True if union was successful (no cycle), False otherwise
        """
        xroot = self.find(x)
        yroot = self.find(y)
        
        # If vertices are already in the same set, it would create a cycle
        if xroot == yroot:
            return False
        
        # Union by rank
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
        
        return True

def kruskal_mst(vertices: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Find the Minimum Spanning Tree using Kruskal's Algorithm.
    
    :param vertices: Number of vertices in the graph
    :param edges: List of edges in the format (source, destination, weight)
    :return: List of edges in the minimum spanning tree
    
    Time Complexity: O(E log E) where E is the number of edges
    Space Complexity: O(V) where V is the number of vertices
    
    Raises:
    - ValueError: If the input is invalid
    """
    # Input validation
    if vertices < 0:
        raise ValueError("Number of vertices must be non-negative")
    
    if not edges:
        return []
    
    # Sort edges by weight in ascending order
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    # Initialize Disjoint Set
    disjoint_set = DisjointSet(vertices)
    
    # Store the Minimum Spanning Tree
    mst = []
    
    # Process sorted edges
    for edge in sorted_edges:
        src, dest, weight = edge
        
        # Check if adding this edge creates a cycle
        if disjoint_set.union(src, dest):
            mst.append(edge)
        
        # Stop when MST has vertices-1 edges
        if len(mst) == vertices - 1:
            break
    
    return mst
class DisjointSet:
    def __init__(self, vertices):
        """
        Initialize a Disjoint Set data structure for Kruskal's algorithm.
        
        Args:
            vertices (int): Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, item):
        """
        Find the root of an item with path compression.
        
        Args:
            item (int): Vertex to find the root for
        
        Returns:
            int: Root of the vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        """
        Union of two sets by rank.
        
        Args:
            x (int): First vertex
            y (int): Second vertex
        
        Returns:
            bool: True if union was successful, False if already in same set
        """
        xroot = self.find(x)
        yroot = self.find(y)

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

def kruskal_mst(num_vertices, edges):
    """
    Implement Kruskal's algorithm to find Minimum Spanning Tree.
    
    Args:
        num_vertices (int): Number of vertices in the graph
        edges (list): List of edges, where each edge is (weight, u, v)
    
    Returns:
        list: Edges in the Minimum Spanning Tree
    """
    # Input validation
    if num_vertices <= 0:
        raise ValueError("Number of vertices must be positive")
    
    if not edges:
        return []
    
    # Sort edges by weight in ascending order
    sorted_edges = sorted(edges)
    
    # Initialize Disjoint Set
    disjoint_set = DisjointSet(num_vertices)
    
    # MST will store the resultant minimum spanning tree
    mst = []
    
    for weight, u, v in sorted_edges:
        # If including this edge doesn't cause a cycle, add it to MST
        if disjoint_set.union(u, v):
            mst.append((weight, u, v))
        
        # Stop when MST has num_vertices - 1 edges
        if len(mst) == num_vertices - 1:
            break
    
    return mst
class DisjointSet:
    def __init__(self, vertices):
        """
        Initialize a Disjoint Set data structure.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices
    
    def find(self, item):
        """
        Find the root/representative of a set.
        Uses path compression for optimization.
        
        :param item: Vertex to find the root for
        :return: Root/representative of the set
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x, y):
        """
        Union two sets by rank.
        
        :param x: First vertex
        :param y: Second vertex
        :return: Boolean indicating if union was successful
        """
        xroot = self.find(x)
        yroot = self.find(y)
        
        # If vertices are already in the same set
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
    
    :param num_vertices: Number of vertices in the graph
    :param edges: List of edges, where each edge is (weight, u, v)
    :return: List of edges in the Minimum Spanning Tree
    """
    # Validate input
    if not edges or num_vertices <= 0:
        return []
    
    # Sort edges by weight in ascending order
    sorted_edges = sorted(edges)
    
    # Initialize Disjoint Set
    disjoint_set = DisjointSet(num_vertices)
    
    # List to store MST edges
    mst_edges = []
    
    # Process edges
    for weight, u, v in sorted_edges:
        # Check if including this edge creates a cycle
        if disjoint_set.union(u, v):
            mst_edges.append((weight, u, v))
        
        # Stop when MST is complete (num_vertices - 1 edges)
        if len(mst_edges) == num_vertices - 1:
            break
    
    return mst_edges
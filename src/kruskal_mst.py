class DisjointSet:
    """
    Disjoint Set (Union-Find) data structure to support Kruskal's algorithm.
    """
    def __init__(self, vertices):
        """
        Initialize disjoint set with each vertex in its own set.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices
    
    def find(self, item):
        """
        Find the root of the set that an item belongs to with path compression.
        
        :param item: Vertex to find the root for
        :return: Root of the set containing the item
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x, y):
        """
        Union of two sets by rank.
        
        :param x: First vertex
        :param y: Second vertex
        :return: True if union was successful (sets were different), False otherwise
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        return True

def kruskal_mst(num_vertices, edges):
    """
    Implement Kruskal's algorithm to find the Minimum Spanning Tree.
    
    :param num_vertices: Number of vertices in the graph
    :param edges: List of edges, where each edge is a tuple (weight, u, v)
    :return: List of edges in the minimum spanning tree
    """
    # Validate input
    if not edges:
        return []
    
    if num_vertices <= 0:
        raise ValueError("Number of vertices must be positive")
    
    # Sort edges by weight in ascending order
    sorted_edges = sorted(edges)
    
    # Initialize disjoint set
    disjoint_set = DisjointSet(num_vertices)
    
    # Store the minimum spanning tree edges
    mst_edges = []
    
    # Process each edge
    for weight, u, v in sorted_edges:
        # If adding this edge doesn't create a cycle, add it to MST
        if disjoint_set.union(u, v):
            mst_edges.append((weight, u, v))
        
        # Stop if we have num_vertices - 1 edges (complete MST)
        if len(mst_edges) == num_vertices - 1:
            break
    
    return mst_edges
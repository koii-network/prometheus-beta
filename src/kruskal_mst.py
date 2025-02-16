class DisjointSet:
    def __init__(self, vertices):
        """
        Initialize a disjoint set data structure for Kruskal's algorithm.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices
    
    def find(self, item):
        """
        Find the root of an item with path compression.
        
        :param item: Vertex to find the root for
        :return: Root of the vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x, y):
        """
        Union of two sets by rank.
        
        :param x: First vertex
        :param y: Second vertex
        :return: True if union was successful, False if already in same set
        """
        x_root = self.find(x)
        y_root = self.find(y)
        
        if x_root == y_root:
            return False
        
        # Union by rank
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1
        
        return True

def kruskal_mst(num_vertices, edges):
    """
    Implement Kruskal's algorithm to find the Minimum Spanning Tree.
    
    :param num_vertices: Number of vertices in the graph
    :param edges: List of edges, where each edge is (weight, vertex1, vertex2)
    :return: List of edges in the Minimum Spanning Tree
    """
    # Validate inputs
    if num_vertices < 0:
        raise ValueError("Number of vertices must be non-negative")
    
    if not edges:
        return []
    
    # Sort edges by weight
    sorted_edges = sorted(edges)
    
    # Initialize Disjoint Set
    disjoint_set = DisjointSet(num_vertices)
    
    # Minimum Spanning Tree
    mst = []
    
    # Process edges
    for weight, u, v in sorted_edges:
        # If including this edge doesn't create a cycle, add it to MST
        if disjoint_set.union(u, v):
            mst.append((weight, u, v))
        
        # Stop if MST is complete (num_vertices - 1 edges)
        if len(mst) == num_vertices - 1:
            break
    
    return mst
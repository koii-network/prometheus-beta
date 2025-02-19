class UnionFind:
    """
    UnionFind data structure for Kruskal's algorithm to detect cycles in a graph.
    """
    def __init__(self, vertices):
        """
        Initialize the UnionFind data structure.
        
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
        Union two sets by rank.
        
        :param x: First vertex
        :param y: Second vertex
        :return: Boolean indicating if union was successful (no cycle)
        """
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True

def kruskal_mst(graph):
    """
    Implement Kruskal's algorithm to find Minimum Spanning Tree.
    
    :param graph: List of edges, where each edge is (weight, u, v)
    :return: List of edges in the Minimum Spanning Tree
    """
    # Validate input
    if not graph:
        return []
    
    # Sort edges by weight in ascending order
    sorted_edges = sorted(graph, key=lambda x: x[0])
    
    # Find the number of vertices
    vertices = max(max(edge[1], edge[2]) for edge in graph) + 1
    
    # Initialize UnionFind data structure
    uf = UnionFind(vertices)
    
    # Minimum Spanning Tree
    mst = []
    
    # Go through sorted edges
    for weight, u, v in sorted_edges:
        # If adding this edge doesn't create a cycle
        if uf.union(u, v):
            mst.append((weight, u, v))
    
    return mst
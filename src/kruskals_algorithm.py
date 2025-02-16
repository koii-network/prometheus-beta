class DisjointSet:
    def __init__(self, vertices):
        """
        Initialize a Disjoint Set data structure for Kruskal's algorithm.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, item):
        """
        Find the root/representative of a set with path compression.
        
        :param item: Vertex to find the root for
        :return: Root of the set
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        """
        Union two sets by rank.
        
        :param x: First vertex
        :param y: Second vertex
        :return: True if union was successful, False if already in same set
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

    # Sort edges by weight
    graph.sort()

    # Number of vertices
    vertices = max(max(u, v) for _, u, v in graph) + 1
    
    # Initialize Disjoint Set
    disjoint_set = DisjointSet(vertices)
    
    # Minimum Spanning Tree
    mst = []
    
    # Process edges
    for weight, u, v in graph:
        # If including this edge doesn't form a cycle
        if disjoint_set.union(u, v):
            mst.append((weight, u, v))
    
    return mst
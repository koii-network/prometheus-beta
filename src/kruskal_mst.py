class DisjointSet:
    """
    Disjoint Set data structure for Kruskal's Algorithm.
    Supports union and find operations with path compression.
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
        Find the root of a set with path compression.
        
        :param item: Vertex to find the root for
        :return: Root of the set containing the vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        """
        Union of two sets by rank.
        
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

def kruskal_mst(graph):
    """
    Find the Minimum Spanning Tree using Kruskal's Algorithm.
    
    :param graph: List of edges, where each edge is a tuple (weight, u, v)
    :return: List of edges in the Minimum Spanning Tree
    :raises ValueError: If graph is empty or None
    """
    # Input validation
    if not graph:
        raise ValueError("Graph cannot be empty")

    # Sort edges by weight in ascending order
    graph.sort()

    # Number of vertices (assuming 0-indexed)
    vertices = max(max(u, v) for _, u, v in graph) + 1

    # Initialize disjoint set
    disjoint_set = DisjointSet(vertices)
    mst = []

    # Process each edge
    for weight, u, v in graph:
        # If adding this edge doesn't create a cycle
        if disjoint_set.union(u, v):
            mst.append((weight, u, v))

    return mst
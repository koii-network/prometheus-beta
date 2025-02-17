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
        Find the root of an item with path compression.
        
        :param item: The vertex to find the root for
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

def kruskal_mst(graph):
    """
    Find Minimum Spanning Tree using Kruskal's Algorithm.
    
    :param graph: List of edges, each edge is a tuple (weight, vertex1, vertex2)
    :return: List of edges in the Minimum Spanning Tree
    """
    # Input validation
    if not graph:
        return []

    # Sort edges by weight
    graph.sort()

    # Find the number of vertices
    vertices = max(max(edge[1], edge[2]) for edge in graph) + 1

    # Initialize Disjoint Set
    disjoint_set = DisjointSet(vertices)
    mst = []

    # Process each edge
    for weight, u, v in graph:
        # If including this edge doesn't create a cycle, add it to MST
        if disjoint_set.union(u, v):
            mst.append((weight, u, v))

    return mst
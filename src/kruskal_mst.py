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
        
        :param item: Vertex to find the root for
        :return: Root of the set containing the vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x, y):
        """
        Union two sets by rank.
        
        :param x: First vertex
        :param y: Second vertex
        :return: True if union is successful, False if already in same set
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
    Find the Minimum Spanning Tree using Kruskal's Algorithm.
    
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
    
    # Initialize Disjoint Set
    ds = DisjointSet(vertices)
    
    # Store the Minimum Spanning Tree edges
    mst = []
    
    for edge in sorted_edges:
        weight, u, v = edge
        
        # If including this edge doesn't create a cycle, add it to MST
        if ds.union(u, v):
            mst.append(edge)
        
        # Stop when MST has exactly (vertices - 1) edges to ensure minimum number of edges
        if len(mst) == vertices - 1:
            break
    
    return mst
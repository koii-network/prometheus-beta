class DisjointSet:
    def __init__(self, vertices):
        """
        Initialize Disjoint Set data structure with given number of vertices.
        
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
        """
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return

        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

def boruvka_mst(graph):
    """
    Implement Boruvka's algorithm to find Minimum Spanning Tree.
    
    :param graph: List of edges, where each edge is (u, v, weight)
    :return: List of edges in the Minimum Spanning Tree
    """
    # Validate input
    if not graph:
        return []

    # Find the maximum vertex to determine the number of vertices
    vertices = max(max(u, v) for u, v, _ in graph) + 1
    
    # Sort edges by weight
    graph.sort(key=lambda x: x[2])
    
    # Initialize Disjoint Set
    disjoint_set = DisjointSet(vertices)
    
    # Minimum Spanning Tree edges
    mst = []
    
    # Track the number of components
    components = vertices
    
    while components > 1:
        # Track cheapest edge for each component
        cheapest_edges = [None] * vertices
        
        # Find the cheapest edge for each component
        for u, v, weight in graph:
            set_u = disjoint_set.find(u)
            set_v = disjoint_set.find(v)
            
            if set_u != set_v:
                # If no cheapest edge for component u
                if cheapest_edges[set_u] is None or cheapest_edges[set_u][2] > weight:
                    cheapest_edges[set_u] = (u, v, weight)
                
                # If no cheapest edge for component v
                if cheapest_edges[set_v] is None or cheapest_edges[set_v][2] > weight:
                    cheapest_edges[set_v] = (u, v, weight)
        
        # Add cheapest edges to MST
        for edge in cheapest_edges:
            if edge is not None:
                u, v, weight = edge
                set_u = disjoint_set.find(u)
                set_v = disjoint_set.find(v)
                
                if set_u != set_v:
                    disjoint_set.union(u, v)
                    mst.append(edge)
                    components -= 1
        
        # If no edges are added in the last iteration, break
        if not mst:
            break
    
    return mst
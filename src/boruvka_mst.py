class DisjointSet:
    def __init__(self, vertices):
        """
        Initialize a disjoint set data structure.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, item):
        """
        Find the root of a set with path compression.
        
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
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True

def boruvka_mst(num_vertices, edges):
    """
    Implement Boruvka's algorithm to find the Minimum Spanning Tree (MST).
    
    :param num_vertices: Number of vertices in the graph
    :param edges: List of edges, where each edge is a tuple (weight, vertex1, vertex2)
    :return: List of edges in the minimum spanning tree
    """
    # Input validation
    if num_vertices <= 0:
        raise ValueError("Number of vertices must be positive")
    
    if not edges:
        return []

    # Sort edges by weight
    edges.sort()

    # Initialize disjoint set
    disjoint_set = DisjointSet(num_vertices)
    
    # Minimum Spanning Tree
    mst = []
    
    # Tracking components
    components = num_vertices

    while components > 1:
        # Cheapest edge for each component
        cheapest_edges = [None] * num_vertices

        # Find cheapest edge connecting each component
        for weight, u, v in edges:
            set_u = disjoint_set.find(u)
            set_v = disjoint_set.find(v)

            if set_u != set_v:
                # Update cheapest edge for the component if needed
                if cheapest_edges[set_u] is None or weight < cheapest_edges[set_u][0]:
                    cheapest_edges[set_u] = (weight, u, v)
                
                if cheapest_edges[set_v] is None or weight < cheapest_edges[set_v][0]:
                    cheapest_edges[set_v] = (weight, u, v)

        # Add cheapest edges to MST
        for cheapest_edge in cheapest_edges:
            if cheapest_edge is not None:
                weight, u, v = cheapest_edge
                
                # If vertices are in different sets, add to MST
                if disjoint_set.union(u, v):
                    mst.append(cheapest_edge)
                    components -= 1

    return mst
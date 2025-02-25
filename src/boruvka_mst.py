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
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return False

        # Union by rank
        if self.rank[xroot] < self.rank[yroot]:
            xroot, yroot = yroot, xroot

        self.parent[yroot] = xroot
        if self.rank[xroot] == self.rank[yroot]:
            self.rank[xroot] += 1

        return True

def boruvka_mst(num_vertices, edges):
    """
    Implement Boruvka's algorithm to find Minimum Spanning Tree.
    
    :param num_vertices: Number of vertices in the graph
    :param edges: List of edges, where each edge is (weight, u, v)
    :return: List of edges in the Minimum Spanning Tree
    """
    # Input validation
    if num_vertices <= 0:
        raise ValueError("Number of vertices must be positive")
    
    if not edges:
        return []

    # Sort edges by weight
    edges.sort()

    # Initialize Disjoint Set
    ds = DisjointSet(num_vertices)

    # Minimum Spanning Tree result
    mst_edges = []

    # Track the number of sets
    num_sets = num_vertices

    # Boruvka's algorithm
    while num_sets > 1:
        # Keep track of the cheapest edge for each component
        cheapest_edges = [None] * num_vertices

        # Find cheapest edge for each component
        for weight, u, v in edges:
            component_u = ds.find(u)
            component_v = ds.find(v)

            # Skip if vertices are in the same set
            if component_u == component_v:
                continue

            # Update cheapest edge for each component
            if cheapest_edges[component_u] is None or weight < cheapest_edges[component_u][0]:
                cheapest_edges[component_u] = (weight, u, v)
            
            if cheapest_edges[component_v] is None or weight < cheapest_edges[component_v][0]:
                cheapest_edges[component_v] = (weight, u, v)

        # Add the cheapest edges to the MST if they don't create a cycle
        for edge in cheapest_edges:
            if edge is not None:
                weight, u, v = edge
                if ds.union(u, v):
                    mst_edges.append((weight, u, v))
                    num_sets -= 1

    return mst_edges
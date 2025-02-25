class DisjointSet:
    """
    Disjoint Set (Union-Find) data structure to help implement Kruskal's algorithm.
    
    This class provides efficient methods for tracking connected components 
    and detecting cycles in a graph.
    """
    def __init__(self, vertices):
        """
        Initialize the Disjoint Set data structure.
        
        Args:
            vertices (int): Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices
    
    def find(self, item):
        """
        Find the root of a vertex with path compression.
        
        Args:
            item (int): Vertex to find the root for
        
        Returns:
            int: Root of the vertex
        """
        if self.parent[item] != item:
            # Path compression
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x, y):
        """
        Union two sets by rank.
        
        Args:
            x (int): First vertex
            y (int): Second vertex
        
        Returns:
            bool: True if union was successful (no cycle), False otherwise
        """
        # Find roots of x and y
        root_x = self.find(x)
        root_y = self.find(y)
        
        # If roots are same, it creates a cycle
        if root_x == root_y:
            return False
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        
        self.parent[root_y] = root_x
        
        # Update rank if needed
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        
        return True

def kruskal_mst(graph):
    """
    Implement Kruskal's algorithm to find Minimum Spanning Tree.
    
    Args:
        graph (list of tuple): List of edges in the format 
                                [(weight, u, v), ...]
    
    Returns:
        list of tuple: Edges in the Minimum Spanning Tree
    
    Raises:
        ValueError: If graph is None or empty
        TypeError: If graph is not in the correct format
    """
    # Input validation
    if graph is None:
        raise ValueError("Graph cannot be None")
    
    if not graph:
        return []
    
    # Validate graph structure
    try:
        # Sort edges by weight
        sorted_edges = sorted(graph)
    except TypeError:
        raise TypeError("Graph must be a list of (weight, u, v) tuples")
    
    # Find the number of vertices
    vertices = max(max(u, v) for _, u, v in graph) + 1
    
    # Initialize Disjoint Set
    disjoint_set = DisjointSet(vertices)
    
    # Store MST edges
    mst = []
    
    # Process sorted edges
    for weight, u, v in sorted_edges:
        # Try to add edge to MST if it doesn't create a cycle
        if disjoint_set.union(u, v):
            mst.append((weight, u, v))
    
    return mst
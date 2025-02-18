import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set():
    """Test DisjointSet data structure functionality."""
    ds = DisjointSet(5)
    
    # Initially, each vertex is in its own set
    assert ds.find(0) != ds.find(1)
    
    # Union some sets
    ds.union(0, 1)
    ds.union(2, 3)
    
    # Check that vertices are now in the same set
    assert ds.find(0) == ds.find(1)
    assert ds.find(2) == ds.find(3)
    
    # Ensure different sets remain different
    assert ds.find(0) != ds.find(2)

def test_kruskal_mst_simple_graph():
    """Test Kruskal's algorithm on a simple graph."""
    # Graph with 4 vertices and 5 edges
    num_vertices = 4
    edges = [
        (1, 0, 1),   # weight 1, connecting vertex 0 and 1
        (4, 0, 2),   # weight 4, connecting vertex 0 and 2
        (2, 1, 2),   # weight 2, connecting vertex 1 and 2
        (3, 1, 3),   # weight 3, connecting vertex 1 and 3
        (5, 2, 3)    # weight 5, connecting vertex 2 and 3
    ]
    
    mst = kruskal_mst(num_vertices, edges)
    
    # Expected MST should have num_vertices - 1 edges
    assert len(mst) == num_vertices - 1
    
    # Total weight should be minimal
    assert sum(edge[0] for edge in mst) == 6  # 1 + 2 + 3

def test_kruskal_mst_empty_graph():
    """Test Kruskal's algorithm with empty edge list."""
    assert kruskal_mst(0, []) == []
    assert kruskal_mst(3, []) == []

def test_kruskal_mst_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError):
        kruskal_mst(-1, [(1, 0, 1)])
    
    with pytest.raises(ValueError):
        kruskal_mst(0, [(1, 0, 1)])

def test_kruskal_mst_disconnected_graph():
    """Test Kruskal's algorithm on a disconnected graph."""
    num_vertices = 5
    edges = [
        (1, 0, 1),   # weight 1, connecting vertex 0 and 1
        (2, 2, 3),   # weight 2, connecting vertex 2 and 3
        (3, 4, 4)    # weight 3, connecting vertex 4 and isolated vertex
    ]
    
    mst = kruskal_mst(num_vertices, edges)
    
    # Ensure the MST includes the existing connected components
    assert len(mst) == 3  # 3 edges across different components
    
    # Verify the total weight of MST
    assert sum(edge[0] for edge in mst) == 6  # 1 + 2 + 3
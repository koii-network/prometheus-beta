import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set():
    """Test the DisjointSet data structure."""
    ds = DisjointSet(5)
    
    # Initially, each vertex is in its own set
    assert ds.find(0) != ds.find(1)
    
    # Perform unions
    ds.union(0, 1)
    ds.union(2, 3)
    
    # Check if vertices are now in the same set
    assert ds.find(0) == ds.find(1)
    assert ds.find(2) == ds.find(3)
    assert ds.find(0) != ds.find(2)

def test_kruskal_empty_graph():
    """Test Kruskal's algorithm with an empty graph."""
    assert kruskal_mst(0, []) == []
    assert kruskal_mst(5, []) == []

def test_kruskal_single_vertex():
    """Test Kruskal's algorithm with a single vertex."""
    assert kruskal_mst(1, []) == []

def test_kruskal_simple_graph():
    """Test Kruskal's algorithm with a simple connected graph."""
    # Graph with 4 vertices and 5 edges
    edges = [
        (1, 0, 1),   # weight 1, from vertex 0 to vertex 1
        (4, 0, 2),   # weight 4, from vertex 0 to vertex 2
        (2, 1, 2),   # weight 2, from vertex 1 to vertex 2
        (3, 1, 3),   # weight 3, from vertex 1 to vertex 3
        (5, 2, 3)    # weight 5, from vertex 2 to vertex 3
    ]
    
    mst = kruskal_mst(4, edges)
    
    # Expected MST total weight should be 6
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == 6
    
    # MST should have num_vertices - 1 edges
    assert len(mst) == 3

def test_kruskal_disconnected_graph():
    """Test Kruskal's algorithm with a disconnected graph."""
    edges = [
        (1, 0, 1),   # weight 1, from vertex 0 to vertex 1
        (5, 2, 3)    # weight 5, from vertex 2 to vertex 3
    ]
    
    # This should return an empty MST as the graph is not fully connected
    mst = kruskal_mst(4, edges)
    assert mst == []

def test_kruskal_multiple_mst_possibilities():
    """Test Kruskal's algorithm with multiple possible MSTs."""
    edges = [
        (1, 0, 1),   # weight 1, from vertex 0 to vertex 1
        (1, 0, 2),   # weight 1, from vertex 0 to vertex 2
        (2, 1, 2),   # weight 2, from vertex 1 to vertex 2
        (3, 1, 3),   # weight 3, from vertex 1 to vertex 3
        (3, 2, 3)    # weight 3, from vertex 2 to vertex 3
    ]
    
    mst = kruskal_mst(4, edges)
    
    # Expected MST total weight should be 4
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == 4
    
    # MST should have num_vertices - 1 edges
    assert len(mst) == 3
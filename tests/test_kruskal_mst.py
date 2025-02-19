import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set_basic():
    """Test basic functionality of DisjointSet"""
    ds = DisjointSet(5)
    
    # Initially, each vertex is in its own set
    assert ds.find(0) != ds.find(1)
    
    # Union should merge sets
    ds.union(0, 1)
    assert ds.find(0) == ds.find(1)
    
    # Second union should not change the set
    assert ds.union(0, 1) is False

def test_kruskal_mst_simple_graph():
    """Test Kruskal's algorithm on a simple graph"""
    # Graph with 4 vertices and 5 edges
    edges = [
        (1, 0, 1),   # weight, vertex1, vertex2
        (4, 0, 2),
        (2, 1, 2),
        (3, 1, 3),
        (5, 2, 3)
    ]
    
    mst = kruskal_mst(4, edges)
    
    # MST should have num_vertices - 1 edges
    assert len(mst) == 3
    
    # Total weight of MST should be minimal
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == 6  # 1 + 2 + 3

def test_kruskal_mst_empty_graph():
    """Test Kruskal's algorithm with no edges"""
    mst = kruskal_mst(3, [])
    assert mst == []

def test_kruskal_mst_negative_vertices():
    """Test handling of invalid number of vertices"""
    with pytest.raises(ValueError):
        kruskal_mst(-1, [(1, 0, 1)])

def test_kruskal_mst_connected_graph():
    """Test Kruskal's algorithm on a more complex connected graph"""
    edges = [
        (2, 0, 1),
        (3, 1, 2),
        (3, 0, 3),
        (4, 1, 3),
        (5, 2, 3),
        (1, 1, 4),
        (6, 3, 4)
    ]
    
    mst = kruskal_mst(5, edges)
    
    # MST should have num_vertices - 1 edges
    assert len(mst) == 4
    
    # Total weight of MST should be minimal
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == 7  # This depends on specific graph structure

def test_kruskal_mst_edge_cases():
    """Test various edge cases"""
    # Single vertex
    assert kruskal_mst(1, []) == []
    
    # Two vertices, one edge
    assert kruskal_mst(2, [(5, 0, 1)]) == [(5, 0, 1)]
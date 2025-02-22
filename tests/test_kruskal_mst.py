import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set_find():
    """Test the find method of DisjointSet"""
    ds = DisjointSet(5)
    assert ds.find(0) == 0
    assert ds.find(4) == 4

def test_disjoint_set_union():
    """Test the union method of DisjointSet"""
    ds = DisjointSet(5)
    assert ds.union(0, 1) == True  # First union should succeed
    assert ds.union(0, 1) == False  # Subsequent union of same set should fail
    
    # Check that they are now in the same set
    assert ds.find(0) == ds.find(1)

def test_kruskal_mst_simple_graph():
    """Test Kruskal's algorithm on a simple graph"""
    # Graph edges: (weight, vertex1, vertex2)
    graph = [
        (4, 0, 1),
        (8, 0, 7),
        (11, 1, 7),
        (8, 1, 2),
        (7, 7, 8),
        (1, 7, 6),
        (2, 8, 6),
        (6, 2, 8),
        (2, 2, 3),
        (7, 2, 5),
        (4, 3, 5),
        (9, 3, 4),
        (14, 5, 4),
        (10, 6, 5)
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected edges in the MST (sorted by weight)
    expected_mst_edges = [
        (1, 7, 6),
        (2, 2, 3),
        (2, 8, 6),
        (4, 0, 1),
        (4, 3, 5),
        (7, 2, 5)
    ]
    
    # Check the number of edges in MST
    assert len(mst) == 6
    
    # Check that MST edges match expected edges
    assert sorted(mst) == sorted(expected_mst_edges)

def test_kruskal_mst_empty_graph():
    """Test Kruskal's algorithm with an empty graph"""
    assert kruskal_mst([]) == []

def test_kruskal_mst_single_vertex():
    """Test Kruskal's algorithm with a single vertex"""
    graph = [(1, 0, 0)]
    assert kruskal_mst(graph) == []

def test_kruskal_mst_disconnected_graph():
    """Test Kruskal's algorithm with a disconnected graph"""
    graph = [
        (1, 0, 1),  # Component 1
        (5, 2, 3),  # Component 2
        (10, 4, 5)  # Component 3
    ]
    
    mst = kruskal_mst(graph)
    
    # Each component should have at least one edge
    assert len(mst) == 2
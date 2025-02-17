import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set():
    """Test DisjointSet data structure"""
    ds = DisjointSet(5)
    
    # Initially, each vertex is in its own set
    assert ds.find(0) != ds.find(1)
    
    # Union some sets
    ds.union(0, 1)
    ds.union(2, 3)
    
    # Now these should be in the same set
    assert ds.find(0) == ds.find(1)
    assert ds.find(2) == ds.find(3)
    
    # These should still be in different sets
    assert ds.find(0) != ds.find(2)

def test_kruskal_mst_basic():
    """Test Kruskal's algorithm with a simple graph"""
    graph = [
        (4, 0, 1),   # edge with weight 4 between vertices 0 and 1
        (2, 1, 2),   # edge with weight 2 between vertices 1 and 2
        (3, 2, 0),   # edge with weight 3 between vertices 2 and 0
        (5, 1, 3),   # edge with weight 5 between vertices 1 and 3
        (1, 3, 0)    # edge with weight 1 between vertices 3 and 0
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected MST should have vertices-1 edges (3 edges for 4 vertices)
    assert len(mst) == 3
    
    # Verify total MST weight
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == 6  # 1 + 2 + 3

def test_kruskal_mst_empty_graph():
    """Test Kruskal's algorithm with an empty graph"""
    graph = []
    mst = kruskal_mst(graph)
    assert mst == []

def test_kruskal_mst_single_vertex():
    """Test Kruskal's algorithm with a single vertex"""
    graph = []
    mst = kruskal_mst(graph)
    assert mst == []

def test_kruskal_mst_disconnected_graph():
    """Test Kruskal's algorithm with a disconnected graph"""
    graph = [
        (1, 0, 1),   # Cluster 1
        (2, 2, 3),   # Cluster 2
        (10, 0, 3)   # Expensive cross-cluster edge
    ]
    
    mst = kruskal_mst(graph)
    
    # Should have min-spanning edges from each cluster
    assert len(mst) == 2
    assert sorted([(edge[0], sorted(edge[1:])) for edge in mst]) == [
        (1, [0, 1]),
        (2, [2, 3])
    ]
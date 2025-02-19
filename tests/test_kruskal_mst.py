import pytest
from ..src.kruskal_mst import kruskal_mst, UnionFind

def test_kruskal_mst_basic():
    """
    Test a simple graph with known MST.
    Graph:
    0 -- 1 (weight 4)
    0 -- 7 (weight 8)
    1 -- 7 (weight 11)
    1 -- 2 (weight 8)
    7 -- 8 (weight 7)
    7 -- 6 (weight 1)
    2 -- 8 (weight 2)
    2 -- 5 (weight 4)
    2 -- 3 (weight 7)
    8 -- 6 (weight 6)
    6 -- 5 (weight 2)
    3 -- 5 (weight 14)
    3 -- 4 (weight 9)
    5 -- 4 (weight 10)
    """
    graph = [
        (4, 0, 1), (8, 0, 7), (11, 1, 7), (8, 1, 2),
        (7, 7, 8), (1, 7, 6), (2, 8, 2), (4, 2, 5),
        (7, 2, 3), (6, 8, 6), (2, 6, 5), (14, 3, 5),
        (9, 3, 4), (10, 5, 4)
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected total weight of MST
    expected_total_weight = 37
    
    # Check the total weight of the MST
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == expected_total_weight
    
    # Check the number of edges in MST (should be vertices - 1)
    assert len(mst) == 8  # For 9 vertices (0-8)

def test_kruskal_mst_empty_graph():
    """
    Test MST with an empty graph.
    """
    graph = []
    mst = kruskal_mst(graph)
    assert mst == []

def test_kruskal_mst_single_vertex():
    """
    Test MST with a single vertex graph.
    """
    graph = [(1, 0, 0)]
    mst = kruskal_mst(graph)
    assert mst == []

def test_unionfind_basic():
    """
    Test UnionFind data structure.
    """
    uf = UnionFind(5)
    
    # Initially, each vertex is in its own set
    assert uf.find(0) != uf.find(1)
    
    # Union some vertices
    uf.union(0, 1)
    uf.union(2, 3)
    
    # Check that they are now in the same set
    assert uf.find(0) == uf.find(1)
    assert uf.find(2) == uf.find(3)
    
    # Check they are not in the same set as other vertices
    assert uf.find(0) != uf.find(2)

def test_unionfind_cycle_detection():
    """
    Test UnionFind cycle detection.
    """
    uf = UnionFind(5)
    
    # First union should succeed
    assert uf.union(0, 1) == True
    
    # Second union of same vertices should fail (cycle detected)
    assert uf.union(0, 1) == False
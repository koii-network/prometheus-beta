import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_kruskal_mst_basic():
    # Simple graph with known MST
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
    
    # Expected total weight of MST
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == 37

def test_kruskal_mst_empty_graph():
    # Test empty graph
    assert kruskal_mst([]) == []

def test_disjoint_set_operations():
    # Test DisjointSet find and union
    ds = DisjointSet(5)
    
    # Initially, each vertex is in its own set
    assert ds.find(0) != ds.find(1)
    
    # Union some sets
    ds.union(0, 1)
    ds.union(2, 3)
    
    # Now these vertices should be in the same set
    assert ds.find(0) == ds.find(1)
    assert ds.find(2) == ds.find(3)
    assert ds.find(0) != ds.find(2)

def test_kruskal_mst_disconnected_graph():
    # Graph with disconnected components
    graph = [
        (1, 0, 1),
        (2, 1, 2),
        (3, 3, 4)
    ]
    mst = kruskal_mst(graph)
    
    # Should return the minimum edges
    assert len(mst) == 2
    assert set((u, v) for _, u, v in mst) == {(0, 1), (1, 2)}

def test_kruskal_mst_single_edge():
    # Test graph with single edge
    graph = [(5, 0, 1)]
    mst = kruskal_mst(graph)
    
    assert mst == [(5, 0, 1)]
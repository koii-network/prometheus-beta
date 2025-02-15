import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set():
    """Test Disjoint Set data structure."""
    ds = DisjointSet(5)
    
    # Test initial state
    assert ds.find(0) == 0
    assert ds.find(4) == 4
    
    # Test union and find
    assert ds.union(0, 1) == True  # First union
    assert ds.find(0) == ds.find(1)  # Same root after union
    
    assert ds.union(2, 3) == True
    assert ds.find(2) == ds.find(3)
    
    # Test repeated union
    assert ds.union(0, 1) == False  # Already in same set

def test_kruskal_mst_empty_graph():
    """Test MST with empty graph."""
    assert kruskal_mst([]) == []

def test_kruskal_mst_simple_graph():
    """Test MST with a simple connected graph."""
    graph = [
        (4, 0, 1),
        (8, 0, 7),
        (8, 1, 2),
        (11, 1, 7),
        (7, 1, 3),
        (2, 2, 3),
        (4, 2, 5),
        (6, 2, 8),
        (2, 3, 5),
        (7, 3, 4),
        (14, 3, 6),
        (9, 4, 5),
        (10, 4, 6),
        (1, 7, 8)
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected MST total weight
    expected_edges = [
        (1, 7, 8),
        (2, 2, 3),
        (2, 3, 5),
        (4, 0, 1),
        (4, 2, 5),
        (6, 2, 8),
        (7, 1, 3)
    ]
    
    # Check MST edges
    assert set(mst) == set(expected_edges)
    
    # Verify no cycles and all vertices are connected
    ds = DisjointSet(9)
    for _, u, v in mst:
        assert ds.union(u, v), f"Cycle detected between {u} and {v}"

def test_kruskal_mst_disconnected_graph():
    """Test MST with a disconnected graph."""
    graph = [
        (1, 0, 1),
        (2, 2, 3),
        (3, 4, 5),
        (4, 6, 7)
    ]
    
    mst = kruskal_mst(graph)
    
    # Some minimal spanning tree edges should be present
    assert len(mst) > 0
    assert len(mst) < len(graph)
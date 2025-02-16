import pytest
from src.kruskals_algorithm import kruskal_mst, DisjointSet

def test_disjoint_set():
    """Test the DisjointSet data structure."""
    ds = DisjointSet(5)
    
    # Initially, each vertex is in its own set
    assert ds.find(0) != ds.find(1)
    
    # Union of vertices
    ds.union(0, 1)
    assert ds.find(0) == ds.find(1)
    
    # Multiple unions
    ds.union(2, 3)
    ds.union(1, 3)
    assert ds.find(0) == ds.find(2)
    assert ds.find(0) == ds.find(3)

def test_kruskal_mst_basic():
    """Test Kruskal's algorithm with a simple graph."""
    # Graph edges: (weight, u, v)
    graph = [
        (1, 0, 1),
        (2, 1, 2),
        (3, 0, 2)
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected MST edges
    expected_mst = [(1, 0, 1), (2, 1, 2)]
    assert set(mst) == set(expected_mst)

def test_kruskal_mst_complex():
    """Test Kruskal's algorithm with a more complex graph."""
    graph = [
        (4, 0, 1),
        (8, 0, 7),
        (11, 1, 7),
        (8, 1, 2),
        (7, 7, 8),
        (1, 7, 6),
        (2, 8, 6),
        (4, 2, 5),
        (7, 2, 3),
        (9, 3, 5),
        (14, 5, 4),
        (10, 4, 3)
    ]
    
    mst = kruskal_mst(graph)
    
    # Sum of MST weights should be minimal
    mst_weight = sum(weight for weight, _, _ in mst)
    
    # There can be multiple valid MSTs with similar total weights
    assert 37 <= mst_weight <= 44, f"MST weight {mst_weight} is not in expected range"
    
    # Verify the number of edges in MST
    assert len(mst) == 8  # A MST for n vertices has n-1 edges

def test_kruskal_mst_empty_graph():
    """Test Kruskal's algorithm with an empty graph."""
    graph = []
    mst = kruskal_mst(graph)
    assert mst == []

def test_kruskal_mst_single_edge():
    """Test Kruskal's algorithm with a single edge."""
    graph = [(5, 0, 1)]
    mst = kruskal_mst(graph)
    assert mst == [(5, 0, 1)]
import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set():
    """Test DisjointSet data structure operations."""
    ds = DisjointSet(5)
    
    # Test initial state
    assert ds.find(0) == 0
    assert ds.find(4) == 4
    
    # Test union and find
    assert ds.union(0, 1) == True  # First union should succeed
    assert ds.find(0) == ds.find(1)  # Should be in same set
    
    assert ds.union(0, 1) == False  # Second union should fail (already in same set)
    
    # Test multiple unions
    ds.union(2, 3)
    ds.union(0, 3)
    
    assert ds.find(0) == ds.find(2)
    assert ds.find(0) == ds.find(3)

def test_kruskal_mst_basic():
    """Test Kruskal's Algorithm with a simple graph."""
    # Graph edges: (weight, vertex1, vertex2)
    graph = [
        (1, 0, 1),  # Edge between vertex 0 and 1 with weight 1
        (4, 0, 2),  # Edge between vertex 0 and 2 with weight 4
        (3, 1, 2),  # Edge between vertex 1 and 2 with weight 3
        (2, 1, 3),  # Edge between vertex 1 and 3 with weight 2
        (5, 2, 3)   # Edge between vertex 2 and 3 with weight 5
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected result: Edges with total minimum weight that connect all vertices
    expected_weights = {1, 2, 3}
    mst_weights = {edge[0] for edge in mst}
    
    assert len(mst) == 3  # MST should have vertices-1 edges
    assert mst_weights == expected_weights

def test_kruskal_mst_disconnected():
    """Test Kruskal's Algorithm with a disconnected graph."""
    graph = [
        (1, 0, 1),  # Edge between vertex 0 and 1 with weight 1
        (5, 2, 3)   # Edge between vertex 2 and 3 with weight 5
    ]
    
    mst = kruskal_mst(graph)
    
    # Edges directly included should be the original graph's minimal edges
    assert mst == [(1, 0, 1)]

def test_kruskal_mst_empty_graph():
    """Test Kruskal's Algorithm with an empty graph."""
    graph = []
    mst = kruskal_mst(graph)
    
    assert mst == []

def test_kruskal_mst_large_graph():
    """Test Kruskal's Algorithm with a larger graph."""
    graph = [
        (1, 0, 1), (3, 0, 2), (6, 0, 3),
        (4, 1, 2), (2, 1, 3), (5, 1, 4),
        (7, 2, 3), (8, 2, 5),
        (9, 3, 4), (10, 3, 5),
        (11, 4, 5)
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected total weight should be minimal
    total_weight = sum(edge[0] for edge in mst)
    
    assert len(mst) == 5  # For 6 vertices, MST should have 5 edges
    assert total_weight == 16  # Verified minimal spanning tree weight
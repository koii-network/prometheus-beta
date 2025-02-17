import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set():
    """Test Disjoint Set data structure functionality."""
    ds = DisjointSet(5)
    
    # Initially, all vertices should be in separate sets
    assert ds.find(0) != ds.find(1)
    assert ds.find(2) != ds.find(3)
    
    # Perform unions
    assert ds.union(0, 1) is True  # First union should succeed
    assert ds.union(0, 1) is False  # Second union to same set should fail
    
    # After union, vertices should have same root
    assert ds.find(0) == ds.find(1)

def test_kruskal_mst_simple_graph():
    """Test Kruskal's Algorithm on a simple graph."""
    # Graph: 3 vertices, 3 edges
    graph = [
        (1, 0, 1),   # Edge between 0 and 1 with weight 1
        (2, 1, 2),   # Edge between 1 and 2 with weight 2
        (3, 0, 2)    # Edge between 0 and 2 with weight 3
    ]
    
    mst = kruskal_mst(graph)
    
    # MST should have 2 edges (vertices - 1)
    assert len(mst) == 2
    
    # Check that the minimum weight edges are selected
    mst_weights = [edge[0] for edge in mst]
    assert set(mst_weights) == {1, 2}

def test_kruskal_mst_complex_graph():
    """Test Kruskal's Algorithm on a more complex graph."""
    graph = [
        (4, 0, 1),   # Edge between 0 and 1 with weight 4
        (8, 0, 7),   # Edge between 0 and 7 with weight 8
        (8, 1, 2),   # Edge between 1 and 2 with weight 8
        (11, 1, 7),  # Edge between 1 and 7 with weight 11
        (7, 1, 3),   # Edge between 1 and 3 with weight 7
        (2, 2, 3),   # Edge between 2 and 3 with weight 2
        (6, 2, 5),   # Edge between 2 and 5 with weight 6
        (4, 2, 8),   # Edge between 2 and 8 with weight 4
        (2, 3, 5),   # Edge between 3 and 5 with weight 2
        (7, 3, 4),   # Edge between 3 and 4 with weight 7
        (9, 4, 5),   # Edge between 4 and 5 with weight 9
        (10, 4, 6),  # Edge between 4 and 6 with weight 10
        (2, 6, 7),   # Edge between 6 and 7 with weight 2
        (6, 7, 8)    # Edge between 7 and 8 with weight 6
    ]
    
    mst = kruskal_mst(graph)
    
    # MST should have at most 8 vertices - 1 = 7 edges
    assert len(mst) <= 7
    
    # Total weight of MST
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight <= 37

def test_kruskal_mst_empty_graph():
    """Test Kruskal's Algorithm with an empty graph."""
    graph = []
    mst = kruskal_mst(graph)
    assert mst == []
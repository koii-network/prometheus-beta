import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set():
    """Test Disjoint Set data structure functionality."""
    ds = DisjointSet(5)
    
    # Initial state: each vertex is in its own set
    for i in range(5):
        assert ds.find(i) == i
    
    # Union of sets
    ds.union(0, 1)
    ds.union(2, 3)
    
    # Check roots after union
    assert ds.find(0) == ds.find(1)
    assert ds.find(2) == ds.find(3)
    assert ds.find(0) != ds.find(2)

def test_kruskal_empty_graph():
    """Test Kruskal's algorithm with an empty graph."""
    assert kruskal_mst(0, []) == []
    assert kruskal_mst(1, []) == []

def test_kruskal_invalid_input():
    """Test Kruskal's algorithm with invalid inputs."""
    with pytest.raises(ValueError):
        kruskal_mst(-1, [])

def test_kruskal_simple_graph():
    """Test Kruskal's algorithm with a simple graph."""
    # Simple graph with 4 vertices
    edges = [
        (1, 0, 1),  # weight 1, connecting vertices 0 and 1
        (4, 1, 2),  # weight 4, connecting vertices 1 and 2
        (2, 0, 2),  # weight 2, connecting vertices 0 and 2
        (3, 1, 3),  # weight 3, connecting vertices 1 and 3
        (5, 2, 3),  # weight 5, connecting vertices 2 and 3
    ]
    
    mst = kruskal_mst(4, edges)
    
    # Expect 3 edges in MST for 4 vertices
    assert len(mst) == 3
    
    # Check total weight of MST
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == 6  # 1 + 2 + 3

def test_kruskal_disconnected_graph():
    """Test Kruskal's algorithm with a disconnected graph."""
    edges = [
        (1, 0, 1),   # weight 1, connecting vertices 0 and 1
        (5, 2, 3),   # weight 5, connecting vertices 2 and 3
        (10, 4, 5)   # weight 10, connecting vertices 4 and 5
    ]
    
    mst = kruskal_mst(6, edges)
    
    # Expect 2 edges in partial MST
    assert len(mst) == 2
    
    # Ensure the minimum weight edges are selected
    assert sorted(mst) == [(1, 0, 1), (5, 2, 3)]

def test_kruskal_complete_graph():
    """Test Kruskal's algorithm with a complete graph."""
    edges = [
        (1, 0, 1), (2, 0, 2), (3, 0, 3),
        (2, 1, 2), (4, 1, 3),
        (5, 2, 3)
    ]
    
    mst = kruskal_mst(4, edges)
    
    # Always expect 3 edges in MST for a 4-vertex graph
    assert len(mst) == 3
    
    # Check that the total weight is minimized
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == 6  # Minimum total weight
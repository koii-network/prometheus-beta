import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set():
    """Test DisjointSet data structure."""
    ds = DisjointSet(5)
    
    # Initially, each vertex is in its own set
    assert ds.find(0) != ds.find(1)
    
    # Union some sets
    ds.union(0, 1)
    ds.union(2, 3)
    
    # Check they are now in the same set
    assert ds.find(0) == ds.find(1)
    assert ds.find(2) == ds.find(3)
    assert ds.find(0) != ds.find(2)

def test_kruskal_basic():
    """Test Kruskal's algorithm on a simple graph."""
    num_vertices = 4
    edges = [
        (1, 0, 1),  # weight, vertex1, vertex2
        (3, 1, 2),
        (4, 2, 3),
        (2, 0, 2),
        (5, 1, 3)
    ]
    
    mst = kruskal_mst(num_vertices, edges)
    
    # Expected total weight and number of edges
    assert len(mst) == 3  # For 4 vertices, MST has 3 edges
    
    # Calculate total MST weight
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == 6  # 1 + 2 + 3

def test_kruskal_empty_graph():
    """Test Kruskal's algorithm on an empty graph."""
    assert kruskal_mst(0, []) == []

def test_kruskal_single_vertex():
    """Test Kruskal's algorithm on a single vertex graph."""
    assert kruskal_mst(1, []) == []

def test_kruskal_invalid_input():
    """Test invalid input for number of vertices."""
    with pytest.raises(ValueError):
        kruskal_mst(-1, [])

def test_kruskal_disconnected_graph():
    """Test Kruskal's algorithm on a disconnected graph."""
    num_vertices = 5
    edges = [
        (1, 0, 1),
        (2, 2, 3),
        (3, 3, 4)
    ]
    
    mst = kruskal_mst(num_vertices, edges)
    
    # Should return whatever edges can form a spanning tree
    assert len(mst) > 0
    assert len(mst) <= num_vertices - 1
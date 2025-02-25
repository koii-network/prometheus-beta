import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set_basic():
    """Test basic Disjoint Set operations."""
    ds = DisjointSet(5)
    
    # Initially, each element should be in its own set
    assert ds.find(0) != ds.find(1)
    
    # Union should allow merging sets
    assert ds.union(0, 1) == True
    assert ds.find(0) == ds.find(1)
    
    # Repeated union should return False
    assert ds.union(0, 1) == False

def test_kruskal_mst_simple_graph():
    """Test Kruskal's algorithm on a simple graph."""
    # Simple graph with 3 vertices
    graph = [
        (1, 0, 1),  # weight 1, edge between 0 and 1
        (2, 1, 2),  # weight 2, edge between 1 and 2
        (3, 0, 2)   # weight 3, edge between 0 and 2
    ]
    
    mst = kruskal_mst(graph)
    
    # Should return 2 edges (minimum spanning tree)
    assert len(mst) == 2
    
    # Total weight should be 3
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == 3

def test_kruskal_mst_disconnected_graph():
    """Test Kruskal's algorithm on a disconnected graph."""
    graph = [
        (1, 0, 1),  # weight 1, edge between 0 and 1
        (5, 2, 3),  # weight 5, edge between 2 and 3
        (3, 4, 5)   # weight 3, edge between 4 and 5
    ]
    
    mst = kruskal_mst(graph)
    
    # Should return 2 disconnected edges
    assert len(mst) == 2

def test_kruskal_mst_empty_graph():
    """Test Kruskal's algorithm with empty graph."""
    graph = []
    mst = kruskal_mst(graph)
    assert len(mst) == 0

def test_kruskal_mst_none_input():
    """Test Kruskal's algorithm with None input."""
    with pytest.raises(ValueError):
        kruskal_mst(None)

def test_kruskal_mst_invalid_input():
    """Test Kruskal's algorithm with invalid input."""
    with pytest.raises(TypeError):
        kruskal_mst([1, 2, 3])  # Invalid input format

def test_kruskal_mst_complex_graph():
    """Test Kruskal's algorithm on a more complex graph."""
    graph = [
        (1, 0, 1),
        (2, 1, 2),
        (3, 0, 2),
        (4, 1, 3),
        (5, 2, 3),
        (6, 0, 3)
    ]
    
    mst = kruskal_mst(graph)
    
    # Should return 3 edges (for 4 vertices)
    assert len(mst) == 3
    
    # Verify total weight is minimal
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == 6
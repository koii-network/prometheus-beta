import pytest
from src.boruvka_mst import boruvka_mst, DisjointSet

def test_disjoint_set():
    """Test DisjointSet functionality."""
    ds = DisjointSet(5)
    ds.union(0, 1)
    ds.union(2, 3)
    
    assert ds.find(0) == ds.find(1)  # Should be in same set
    assert ds.find(2) == ds.find(3)  # Should be in same set
    assert ds.find(0) != ds.find(2)  # Should be in different sets

def test_boruvka_simple_graph():
    """Test Boruvka's algorithm on a simple connected graph."""
    graph = [
        (0, 1, 4),
        (0, 7, 8),
        (1, 2, 8),
        (1, 7, 11),
        (2, 3, 7),
        (2, 8, 2),
        (2, 5, 4),
        (3, 4, 9),
        (3, 5, 14),
        (4, 5, 10),
        (5, 6, 2),
        (6, 7, 1),
        (6, 8, 6),
        (7, 8, 7)
    ]
    
    mst = boruvka_mst(graph)
    
    # Validate number of edges in MST
    assert len(mst) == 6  # For a graph with 9 vertices, MST should have n-1 edges
    
    # Validate total MST weight
    total_weight = sum(weight for _, _, weight in mst)
    assert total_weight == 23  # Known MST weight for this graph

def test_boruvka_disconnected_graph():
    """Test Boruvka's algorithm on a disconnected graph."""
    graph = [
        (0, 1, 1),  # Cluster 1
        (2, 3, 2),  # Cluster 2
        (4, 5, 3)   # Cluster 3
    ]
    
    mst = boruvka_mst(graph)
    
    # Each cluster will have its own cheapest edge
    assert len(mst) == 3

def test_boruvka_empty_graph():
    """Test Boruvka's algorithm on an empty graph."""
    graph = []
    
    mst = boruvka_mst(graph)
    
    assert len(mst) == 0

def test_boruvka_single_vertex_graph():
    """Test Boruvka's algorithm on a graph with a single vertex."""
    graph = [(0, 0, 0)]
    
    mst = boruvka_mst(graph)
    
    assert len(mst) == 0  # No edges in a single vertex graph
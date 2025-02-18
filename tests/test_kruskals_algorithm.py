import pytest
from src.kruskals_algorithm import kruskal_mst, DisjointSet

def test_disjoint_set():
    """Test DisjointSet data structure"""
    ds = DisjointSet(5)
    
    # Check initial states
    assert ds.find(0) == 0
    assert ds.find(1) == 1
    
    # Test union and find
    assert ds.union(0, 1) == True  # Should successfully union
    assert ds.find(0) == ds.find(1)  # Should be in same set
    
    assert ds.union(0, 1) == False  # Already in same set
    
    # Ensure different sets remain separate
    assert ds.find(2) != ds.find(0)

def test_kruskal_mst_simple_graph():
    """Test Kruskal's algorithm on a simple graph"""
    # Graph with 4 vertices and 5 edges
    graph = [
        (1, 0, 1),   # weight, vertex1, vertex2
        (4, 0, 2),
        (3, 1, 2),
        (2, 1, 3),
        (5, 2, 3)
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected MST should have n-1 edges (for n vertices)
    assert len(mst) == 3
    
    # Total weight of MST
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == 6  # 1 (0-1) + 2 (1-3) + 3 (1-2)

def test_kruskal_mst_empty_graph():
    """Test Kruskal's algorithm with empty graph"""
    assert kruskal_mst([]) == []

def test_kruskal_mst_single_vertex():
    """Test Kruskal's algorithm with a single vertex"""
    graph = [(1, 0, 0)]
    assert kruskal_mst(graph) == []

def test_kruskal_mst_disconnected_graph():
    """Test Kruskal's algorithm with a disconnected graph"""
    graph = [
        (1, 0, 1),
        (5, 2, 3),
        (4, 4, 5)
    ]
    
    mst = kruskal_mst(graph)
    
    # Should connect only the connected components
    assert len(mst) == 2
    
    # Validate no cycles
    vertices = set()
    for _, u, v in mst:
        assert u not in vertices or v not in vertices
        vertices.update([u, v])

def test_kruskal_mst_complex_graph():
    """Test Kruskal's algorithm on a more complex graph"""
    graph = [
        (2, 0, 1),
        (3, 1, 2),
        (3, 0, 3),
        (4, 1, 3),
        (5, 1, 4),
        (6, 2, 4),
        (7, 3, 4)
    ]
    
    mst = kruskal_mst(graph)
    
    # Should have n-1 edges (5 vertices)
    assert len(mst) == 4
    
    # Validate total weight is minimal
    total_weight = sum(edge[0] for edge in mst)
    assert total_weight == 14  # 2 + 3 + 3 + 6
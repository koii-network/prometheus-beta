import pytest
from src.kruskal_mst import kruskal_mst

def test_basic_mst():
    """
    Test a simple graph with a clear Minimum Spanning Tree
    """
    num_vertices = 4
    edges = [
        (0, 1, 10),   # edge between vertex 0 and 1 with weight 10
        (0, 2, 6),    # edge between vertex 0 and 2 with weight 6
        (0, 3, 5),    # edge between vertex 0 and 3 with weight 5
        (1, 3, 15),   # edge between vertex 1 and 3 with weight 15
        (2, 3, 4)     # edge between vertex 2 and 3 with weight 4
    ]
    
    # Expected MST should have these edges
    expected_mst = {(0, 3, 5), (0, 2, 6), (2, 3, 4)}
    
    result = kruskal_mst(num_vertices, edges)
    assert result is not None
    assert set(result) == expected_mst
    assert len(result) == num_vertices - 1

def test_disconnected_graph():
    """
    Test a graph that cannot form a complete MST
    """
    num_vertices = 5
    # Edges do not connect all vertices
    edges = [
        (0, 1, 10),
        (2, 3, 5)
    ]
    
    result = kruskal_mst(num_vertices, edges)
    assert result is None

def test_empty_graph():
    """
    Test graph with no edges
    """
    num_vertices = 3
    edges = []
    
    result = kruskal_mst(num_vertices, edges)
    assert result is None

def test_single_vertex_graph():
    """
    Test graph with single vertex
    """
    num_vertices = 1
    edges = []
    
    result = kruskal_mst(num_vertices, edges)
    assert result is None

def test_cyclic_graph():
    """
    Test a graph with multiple possible MSTs
    """
    num_vertices = 4
    edges = [
        (0, 1, 1),
        (1, 2, 1),
        (2, 3, 1),
        (3, 0, 1),
        (0, 2, 2)
    ]
    
    result = kruskal_mst(num_vertices, edges)
    assert result is not None
    
    # Verify MST has V-1 edges
    assert len(result) == num_vertices - 1
    
    # Verify total weight
    total_weight = sum(edge[2] for edge in result)
    assert total_weight <= 3  # Should be minimal

def test_large_weighted_graph():
    """
    Test a larger weighted graph
    """
    num_vertices = 7
    edges = [
        (0, 1, 7),
        (0, 3, 5),
        (1, 2, 8),
        (1, 3, 9),
        (1, 4, 7),
        (2, 4, 5),
        (3, 4, 15),
        (3, 5, 6),
        (4, 5, 8),
        (4, 6, 9),
        (5, 6, 11)
    ]
    
    result = kruskal_mst(num_vertices, edges)
    assert result is not None
    assert len(result) == num_vertices - 1

def test_all_same_weight_edges():
    """
    Test graph with all edges having the same weight
    """
    num_vertices = 4
    edges = [
        (0, 1, 1),
        (0, 2, 1),
        (0, 3, 1),
        (1, 2, 1),
        (1, 3, 1),
        (2, 3, 1)
    ]
    
    result = kruskal_mst(num_vertices, edges)
    assert result is not None
    assert len(result) == num_vertices - 1
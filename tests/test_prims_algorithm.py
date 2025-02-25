import pytest
from src.prims_algorithm import prims_minimum_spanning_tree

def test_basic_graph():
    """Test a simple connected graph"""
    graph = {
        0: [(1, 4), (7, 8)],
        1: [(0, 4), (2, 8), (7, 11)],
        2: [(1, 8), (3, 7), (5, 4), (8, 2)],
        3: [(2, 7), (4, 9), (5, 14)],
        4: [(3, 9), (5, 10)],
        5: [(2, 4), (3, 14), (4, 10), (6, 2)],
        6: [(5, 2), (7, 1), (8, 6)],
        7: [(0, 8), (1, 11), (6, 1), (8, 7)],
        8: [(2, 2), (6, 6), (7, 7)]
    }
    
    mst = prims_minimum_spanning_tree(graph)
    
    # Validate MST properties
    assert mst is not None
    assert len(mst) == len(graph) - 1  # MST should have V-1 edges
    
    # Validate total weight (test value is from a known solution)
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 37

def test_disconnected_graph():
    """Test a disconnected graph"""
    graph = {
        0: [(1, 1)],
        1: [(0, 1)],
        2: [(3, 1)],
        3: [(2, 1)]
    }
    
    mst = prims_minimum_spanning_tree(graph)
    assert mst is None

def test_single_vertex_graph():
    """Test a graph with only one vertex"""
    graph = {0: []}
    
    mst = prims_minimum_spanning_tree(graph)
    assert mst == []

def test_empty_graph():
    """Test an empty graph"""
    graph = {}
    
    mst = prims_minimum_spanning_tree(graph)
    assert mst is None

def test_complete_graph():
    """Test a complete graph with multiple edges"""
    graph = {
        0: [(1, 1), (2, 2)],
        1: [(0, 1), (2, 3)],
        2: [(0, 2), (1, 3)]
    }
    
    mst = prims_minimum_spanning_tree(graph)
    
    assert mst is not None
    assert len(mst) == len(graph) - 1
    
    # Verify the expected minimum edges
    expected_edges = {(0, 1, 1), (0, 2, 2)}
    assert set((a, b, w) for a, b, w in mst) == expected_edges

def test_graph_with_negative_edges():
    """Test a graph with negative edge weights"""
    graph = {
        0: [(1, -1), (2, 2)],
        1: [(0, -1), (2, 3)],
        2: [(0, 2), (1, 3)]
    }
    
    mst = prims_minimum_spanning_tree(graph)
    
    assert mst is not None
    assert len(mst) == len(graph) - 1
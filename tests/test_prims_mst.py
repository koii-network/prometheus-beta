import pytest
from src.prims_mst import prims_minimum_spanning_tree

def test_basic_graph():
    """Test a simple connected graph"""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2},
        'E': {'C': 10, 'D': 2}
    }
    
    mst = prims_minimum_spanning_tree(graph)
    assert mst is not None
    
    # Check total number of edges
    assert len(mst) == len(graph) - 1
    
    # Verify the edges (using a set of tuples for unordered comparison)
    expected_edges = {
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('D', 'E', 2),
        ('B', 'D', 5)
    }
    assert set(mst) == expected_edges

def test_single_vertex_graph():
    """Test a graph with only one vertex"""
    graph = {'A': {}}
    
    mst = prims_minimum_spanning_tree(graph)
    assert mst == []

def test_empty_graph():
    """Test an empty graph"""
    graph = {}
    
    mst = prims_minimum_spanning_tree(graph)
    assert mst is None

def test_none_input():
    """Test input that is None"""
    graph = None
    
    mst = prims_minimum_spanning_tree(graph)
    assert mst is None

def test_disconnected_graph():
    """Test a disconnected graph"""
    graph = {
        'A': {'B': 1},
        'B': {'A': 1},
        'C': {'D': 2},
        'D': {'C': 2}
    }
    
    mst = prims_minimum_spanning_tree(graph)
    assert mst is None

def test_fully_connected_graph():
    """Test a fully connected graph"""
    graph = {
        'A': {'B': 1, 'C': 2, 'D': 3},
        'B': {'A': 1, 'C': 1, 'D': 2},
        'C': {'A': 2, 'B': 1, 'D': 1},
        'D': {'A': 3, 'B': 2, 'C': 1}
    }
    
    mst = prims_minimum_spanning_tree(graph)
    assert mst is not None
    assert len(mst) == len(graph) - 1

def test_weighted_edges():
    """Test graph with varying edge weights"""
    graph = {
        'A': {'B': 1, 'C': 5},
        'B': {'A': 1, 'C': 2, 'D': 3},
        'C': {'A': 5, 'B': 2, 'D': 4},
        'D': {'B': 3, 'C': 4}
    }
    
    mst = prims_minimum_spanning_tree(graph)
    assert mst is not None
    
    # Verify minimum total weight
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 6  # 1 (A-B) + 2 (B-C) + 3 (B-D)
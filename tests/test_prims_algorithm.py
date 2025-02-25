import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from prims_algorithm import prims_minimum_spanning_tree

def test_simple_graph():
    """Test a simple connected graph"""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2},
        'E': {'C': 10, 'D': 2}
    }
    
    mst = prims_minimum_spanning_tree(graph)
    
    # Expected edges in the MST (order might vary)
    expected_edges = {
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('D', 'E', 2),
        ('B', 'D', 5)
    }
    
    assert len(mst) == 4
    assert set(mst) == expected_edges

def test_empty_graph():
    """Test behavior with an empty graph"""
    with pytest.raises(ValueError):
        prims_minimum_spanning_tree({})

def test_single_vertex_graph():
    """Test a graph with a single vertex"""
    graph = {'A': {}}
    
    mst = prims_minimum_spanning_tree(graph)
    
    assert mst == []

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

def test_graph_with_multiple_minimum_spanning_trees():
    """Test a graph where multiple minimum spanning trees are possible"""
    graph = {
        'A': {'B': 1, 'C': 1},
        'B': {'A': 1, 'C': 1},
        'C': {'A': 1, 'B': 1}
    }
    
    mst = prims_minimum_spanning_tree(graph)
    
    assert len(mst) == 2
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 2

def test_invalid_graph_input():
    """Test invalid graph input"""
    with pytest.raises(ValueError):
        prims_minimum_spanning_tree(None)
    
    with pytest.raises(ValueError):
        prims_minimum_spanning_tree([])
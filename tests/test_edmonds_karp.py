import pytest
from src.edmonds_karp import edmonds_karp

def test_simple_graph():
    """Test a simple graph with a known maximum flow."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    
    assert edmonds_karp(graph, 0, 5) == 10

def test_disconnected_graph():
    """Test a graph where no flow is possible."""
    graph = {
        0: {1: 5},
        1: {0: 0},
        2: {3: 10},
        3: {2: 0}
    }
    
    assert edmonds_karp(graph, 0, 3) == 0

def test_single_edge_graph():
    """Test a graph with a single edge."""
    graph = {
        0: {1: 5},
        1: {}
    }
    
    assert edmonds_karp(graph, 0, 1) == 5

def test_multiple_paths_graph():
    """Test a graph with multiple possible paths."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    
    assert edmonds_karp(graph, 0, 5) == 10

def test_invalid_source_sink():
    """Test that an error is raised for invalid source or sink."""
    graph = {
        0: {1: 5},
        1: {}
    }
    
    with pytest.raises(ValueError):
        edmonds_karp(graph, 2, 1)
    
    with pytest.raises(ValueError):
        edmonds_karp(graph, 0, 2)

def test_large_graph():
    """Test a larger graph with multiple nodes and paths."""
    graph = {
        0: {1: 16, 2: 13},
        1: {2: 10, 3: 12},
        2: {1: 4, 3: 9, 4: 14},
        3: {4: 7, 5: 20},
        4: {5: 4},
        5: {}
    }
    
    assert edmonds_karp(graph, 0, 5) == 23
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
    
    # Maximum flow from source 0 to sink 5
    max_flow = edmonds_karp(graph, 0, 5)
    assert max_flow == 19

def test_no_path_graph():
    """Test a graph with no path between source and sink."""
    graph = {
        0: {1: 10},
        1: {2: 5},
        2: {},
        3: {}
    }
    
    max_flow = edmonds_karp(graph, 0, 3)
    assert max_flow == 0

def test_single_edge_graph():
    """Test a graph with a single edge."""
    graph = {
        0: {1: 5},
        1: {}
    }
    
    max_flow = edmonds_karp(graph, 0, 1)
    assert max_flow == 5

def test_disconnected_source_sink():
    """Test a graph where source and sink are not connected."""
    graph = {
        0: {},
        1: {2: 10},
        2: {}
    }
    
    max_flow = edmonds_karp(graph, 0, 2)
    assert max_flow == 0

def test_invalid_graph_input():
    """Test handling of invalid graph input."""
    with pytest.raises(TypeError):
        edmonds_karp([], 0, 1)

def test_invalid_source_sink():
    """Test handling of invalid source or sink nodes."""
    graph = {
        0: {1: 10},
        1: {}
    }
    
    with pytest.raises(ValueError):
        edmonds_karp(graph, 2, 1)
    
    with pytest.raises(ValueError):
        edmonds_karp(graph, 0, 2)

def test_complex_graph():
    """Test a more complex graph with multiple paths."""
    graph = {
        0: {1: 3, 2: 3, 3: 2},
        1: {2: 4, 4: 4},
        2: {3: 1, 4: 2},
        3: {5: 2},
        4: {5: 3},
        5: {}
    }
    
    max_flow = edmonds_karp(graph, 0, 5)
    assert max_flow == 4
import pytest
from src.edmonds_karp import edmonds_karp

def test_basic_max_flow():
    """Test a simple graph with known max flow."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    assert edmonds_karp(graph, 0, 5) == 19

def test_disconnected_graph():
    """Test graph where no path exists from source to sink."""
    graph = {
        0: {},
        1: {},
        2: {}
    }
    assert edmonds_karp(graph, 0, 2) == 0

def test_single_path_graph():
    """Test a graph with a single path."""
    graph = {
        0: {1: 5},
        1: {2: 5},
        2: {}
    }
    assert edmonds_karp(graph, 0, 2) == 5

def test_complex_graph():
    """Test a more complex flow network."""
    graph = {
        0: {1: 3, 2: 3},
        1: {2: 4, 3: 1, 4: 2},
        2: {4: 2},
        3: {5: 2},
        4: {3: 1, 5: 3},
        5: {}
    }
    assert edmonds_karp(graph, 0, 5) == 4

def test_invalid_source_sink():
    """Test that invalid source or sink raises ValueError."""
    graph = {
        0: {1: 10},
        1: {}
    }
    
    with pytest.raises(ValueError):
        edmonds_karp(graph, 2, 1)
    
    with pytest.raises(ValueError):
        edmonds_karp(graph, 0, 2)
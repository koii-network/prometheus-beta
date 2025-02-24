import pytest
from src.edmonds_karp import edmonds_karp

def test_simple_graph():
    """Test a simple graph with a clear maximum flow."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    assert edmonds_karp(graph, 0, 5) == 19

def test_single_path_graph():
    """Test a graph with only one path."""
    graph = {
        0: {1: 5},
        1: {2: 5},
        2: {}
    }
    assert edmonds_karp(graph, 0, 2) == 5

def test_no_path_graph():
    """Test a graph with no path between source and sink."""
    graph = {
        0: {},
        1: {},
        2: {}
    }
    assert edmonds_karp(graph, 0, 2) == 0

def test_complex_graph():
    """Test a more complex graph with multiple paths."""
    graph = {
        0: {1: 3, 2: 3},
        1: {2: 4, 3: 1, 4: 2},
        2: {4: 2},
        3: {5: 2},
        4: {3: 1, 5: 3},
        5: {}
    }
    assert edmonds_karp(graph, 0, 5) == 4

def test_invalid_source():
    """Test raising ValueError for invalid source."""
    graph = {1: {2: 5}, 2: {}}
    with pytest.raises(ValueError):
        edmonds_karp(graph, 0, 2)

def test_invalid_sink():
    """Test raising ValueError for invalid sink."""
    graph = {0: {1: 5}, 1: {}}
    with pytest.raises(ValueError):
        edmonds_karp(graph, 0, 2)

def test_symmetric_graph():
    """Test a symmetric graph."""
    graph = {
        0: {1: 10, 2: 10},
        1: {0: 0, 2: 2, 3: 4, 4: 8},
        2: {0: 0, 1: 0, 4: 9},
        3: {1: 0, 5: 10},
        4: {1: 0, 2: 0, 3: 6, 5: 10},
        5: {3: 0, 4: 0}
    }
    assert edmonds_karp(graph, 0, 5) == 19
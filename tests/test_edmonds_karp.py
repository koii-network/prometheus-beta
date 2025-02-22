import pytest
from src.edmonds_karp import edmonds_karp

def test_simple_graph():
    # Simple graph with maximum flow of 4
    graph = {
        0: {1: 3, 2: 3},
        1: {2: 2, 3: 3},
        2: {3: 2},
        3: {}
    }
    assert edmonds_karp(graph, 0, 3) == 4

def test_complex_graph():
    # More complex graph
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    assert edmonds_karp(graph, 0, 5) == 19

def test_no_path():
    # Graph with no path from source to sink
    graph = {
        0: {},
        1: {},
        2: {}
    }
    assert edmonds_karp(graph, 0, 2) == 0

def test_single_path():
    # Graph with a single path
    graph = {
        0: {1: 5},
        1: {}
    }
    assert edmonds_karp(graph, 0, 1) == 5

def test_invalid_nodes():
    # Test invalid source or sink nodes
    graph = {
        0: {1: 5},
        1: {}
    }
    with pytest.raises(ValueError):
        edmonds_karp(graph, 2, 1)
    with pytest.raises(ValueError):
        edmonds_karp(graph, 0, 2)

def test_symmetric_graph():
    # Symmetric graph with equal paths
    graph = {
        0: {1: 5, 2: 5},
        1: {2: 3, 3: 5},
        2: {3: 3},
        3: {}
    }
    assert edmonds_karp(graph, 0, 3) == 8
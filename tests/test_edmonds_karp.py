import pytest
from src.edmonds_karp import edmonds_karp

def test_simple_graph():
    # Simple graph with one path
    graph = {
        0: {1: 10},
        1: {0: 0}
    }
    assert edmonds_karp(graph, 0, 1) == 10

def test_multiple_path_graph():
    # Graph with multiple possible paths
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 0: 0},
        2: {3: 8, 0: 0, 1: 0},
        3: {0: 0, 1: 0, 2: 0}
    }
    assert edmonds_karp(graph, 0, 3) == 12

def test_complex_network():
    # More complex network
    graph = {
        0: {1: 3, 2: 3},
        1: {2: 4, 3: 1, 0: 0},
        2: {3: 2, 0: 0, 1: 0},
        3: {0: 0, 1: 0, 2: 0}
    }
    assert edmonds_karp(graph, 0, 3) == 4

def test_no_path_graph():
    # Graph with no path between source and sink
    graph = {
        0: {1: 0},
        1: {0: 0}
    }
    assert edmonds_karp(graph, 0, 1) == 0

def test_invalid_nodes():
    # Test for nodes not in graph
    graph = {
        0: {1: 10},
        1: {0: 0}
    }
    with pytest.raises(ValueError):
        edmonds_karp(graph, 2, 1)
    with pytest.raises(ValueError):
        edmonds_karp(graph, 0, 2)
import pytest
from src.edmonds_karp import edmonds_karp

def test_basic_max_flow():
    # Simple graph with known max flow
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    assert edmonds_karp(graph, 0, 5) == 19

def test_single_path_flow():
    # Simple linear graph
    graph = {
        0: {1: 5},
        1: {2: 5},
        2: {}
    }
    assert edmonds_karp(graph, 0, 2) == 5

def test_multiple_paths():
    # Graph with multiple possible paths
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
    # Graph with no path between source and sink
    graph = {
        0: {},
        1: {},
        2: {}
    }
    assert edmonds_karp(graph, 0, 2) == 0

def test_invalid_source_or_sink():
    # Graph with invalid source or sink
    graph = {
        0: {1: 10},
        1: {}
    }
    with pytest.raises(ValueError):
        edmonds_karp(graph, 2, 1)
    with pytest.raises(ValueError):
        edmonds_karp(graph, 0, 2)

def test_complex_flow():
    # More complex graph with multiple paths and capacities
    graph = {
        0: {1: 7, 2: 6},
        1: {2: 5, 3: 3},
        2: {3: 8, 4: 5},
        3: {4: 6, 5: 4},
        4: {5: 7},
        5: {}
    }
    assert edmonds_karp(graph, 0, 5) == 10
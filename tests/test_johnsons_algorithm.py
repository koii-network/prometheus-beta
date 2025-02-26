import pytest
from src.johnsons_algorithm import johnsons_algorithm

def test_simple_graph():
    # Simple graph with positive weights
    graph = {
        0: [(1, 5), (2, 2)],
        1: [(2, 1), (3, 3)],
        2: [(3, 6)],
        3: []
    }
    
    result = johnsons_algorithm(graph)
    
    # Expected shortest paths
    expected = {
        0: {1: 5, 2: 2, 3: 8},
        1: {2: 1, 3: 3},
        2: {3: 6},
        3: {}
    }
    
    assert result == expected

def test_graph_with_negative_edges():
    # Graph with some negative edges (but no negative cycles)
    graph = {
        0: [(1, -1), (2, 4)],
        1: [(2, 3), (3, 2)],
        2: [(3, 5)],
        3: []
    }
    
    result = johnsons_algorithm(graph)
    
    # Expected shortest paths
    expected = {
        0: {1: -1, 2: 2, 3: 1},
        1: {2: 3, 3: 2},
        2: {3: 5},
        3: {}
    }
    
    assert result == expected

def test_disconnected_graph():
    # Graph with some disconnected vertices
    graph = {
        0: [(1, 1)],
        1: [],
        2: [(3, 5)],
        3: []
    }
    
    result = johnsons_algorithm(graph)
    
    # Expected shortest paths
    expected = {
        0: {1: 1},
        1: {},
        2: {3: 5},
        3: {}
    }
    
    assert result == expected

def test_negative_cycle():
    # Graph with a negative cycle
    graph = {
        0: [(1, 1)],
        1: [(2, -3)],
        2: [(0, -2)]
    }
    
    result = johnsons_algorithm(graph)
    
    # Should return None for negative cycle
    assert result is None

def test_single_vertex_graph():
    # Single vertex graph
    graph = {0: []}
    
    result = johnsons_algorithm(graph)
    
    # Expected result is an empty dict of paths for the single vertex
    expected = {0: {}}
    
    assert result == expected

def test_empty_graph():
    # Empty graph
    graph = {}
    
    result = johnsons_algorithm(graph)
    
    # Expected result is an empty dict
    expected = {}
    
    assert result == expected
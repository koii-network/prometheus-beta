import pytest
from src.ford_fulkerson import ford_fulkerson

def test_basic_flow():
    # Simple graph with a clear maximum flow
    graph = {
        'S': {'A': 10, 'B': 10},
        'A': {'T': 10, 'B': 2},
        'B': {'T': 10},
        'T': {}
    }
    assert ford_fulkerson(graph, 'S', 'T') == 20

def test_complex_flow():
    # More complex graph with multiple paths
    graph = {
        'S': {'A': 3, 'B': 2, 'C': 5},
        'A': {'B': 1, 'C': 3, 'D': 4},
        'B': {'D': 2},
        'C': {'T': 4},
        'D': {'T': 3},
        'T': {}
    }
    assert ford_fulkerson(graph, 'S', 'T') == 7

def test_no_flow():
    # Graph with no path from source to sink
    graph = {
        'S': {},
        'A': {'B': 1},
        'B': {},
        'T': {}
    }
    assert ford_fulkerson(graph, 'S', 'T') == 0

def test_single_path_flow():
    # Simple linear path
    graph = {
        'S': {'A': 5},
        'A': {'B': 5},
        'B': {'T': 5},
        'T': {}
    }
    assert ford_fulkerson(graph, 'S', 'T') == 5

def test_invalid_nodes():
    # Test with invalid source or sink
    graph = {
        'S': {'A': 5},
        'A': {'T': 5}
    }
    
    with pytest.raises(ValueError):
        ford_fulkerson(graph, 'X', 'T')
    
    with pytest.raises(ValueError):
        ford_fulkerson(graph, 'S', 'X')

def test_large_capacity_flow():
    # Test with very large capacities
    graph = {
        'S': {'A': 1000, 'B': 2000},
        'A': {'T': 800, 'B': 500},
        'B': {'T': 1500},
        'T': {}
    }
    assert ford_fulkerson(graph, 'S', 'T') == 2500
import pytest
from src.ford_fulkerson import ford_fulkerson

def test_simple_network():
    # Simple network with one path
    graph = {
        0: {1: 10},
        1: {2: 10},
        2: {}
    }
    assert ford_fulkerson(graph, 0, 2) == 10

def test_complex_network():
    # More complex network with multiple paths
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 4, 3: 8},
        2: {3: 9},
        3: {}
    }
    assert ford_fulkerson(graph, 0, 3) == 19

def test_no_flow_network():
    # Network with no possible flow
    graph = {
        0: {},
        1: {}
    }
    assert ford_fulkerson(graph, 0, 1) == 0

def test_zero_capacity_network():
    # Network with zero capacities
    graph = {
        0: {1: 0},
        1: {}
    }
    assert ford_fulkerson(graph, 0, 1) == 0

def test_invalid_source_or_sink():
    # Test invalid source or sink
    graph = {
        0: {1: 10},
        1: {}
    }
    with pytest.raises(ValueError):
        ford_fulkerson(graph, 2, 1)
    with pytest.raises(ValueError):
        ford_fulkerson(graph, 0, 2)

def test_large_network():
    # Larger network to test more complex scenarios
    graph = {
        0: {1: 16, 2: 13},
        1: {2: 10, 3: 12},
        2: {1: 4, 3: 9, 4: 14},
        3: {4: 7, 5: 20},
        4: {5: 4},
        5: {}
    }
    assert ford_fulkerson(graph, 0, 5) == 23
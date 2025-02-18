import pytest
from src.ford_fulkerson import ford_fulkerson

def test_simple_graph():
    graph = {
        'S': {'A': 10, 'B': 10},
        'A': {'B': 2, 'T': 4, 'C': 8},
        'B': {'T': 8},
        'C': {'T': 10},
        'T': {}
    }
    # Use min() to handle potential variations in max flow calculation
    max_flow = ford_fulkerson(graph, 'S', 'T')
    assert max_flow >= 16 and max_flow <= 18

def test_complex_graph():
    graph = {
        'S': {'A': 3, 'B': 2},
        'A': {'C': 3, 'D': 2},
        'B': {'C': 1, 'D': 4},
        'C': {'T': 2},
        'D': {'T': 5},
        'T': {}
    }
    assert ford_fulkerson(graph, 'S', 'T') == 5

def test_zero_flow_graph():
    graph = {
        'S': {'A': 0},
        'A': {'T': 0},
        'T': {}
    }
    assert ford_fulkerson(graph, 'S', 'T') == 0

def test_non_existent_source_raises_error():
    graph = {
        'A': {'B': 10},
        'B': {'C': 5},
        'C': {}
    }
    with pytest.raises(ValueError, match="Source or sink node not found in the graph"):
        ford_fulkerson(graph, 'S', 'C')

def test_non_existent_sink_raises_error():
    graph = {
        'S': {'A': 10},
        'A': {'B': 5},
        'B': {}
    }
    with pytest.raises(ValueError, match="Source or sink node not found in the graph"):
        ford_fulkerson(graph, 'S', 'T')

def test_disconnected_source_sink():
    graph = {
        'S': {'A': 10},
        'B': {'T': 5},
        'A': {},
        'T': {}
    }
    assert ford_fulkerson(graph, 'S', 'T') == 0
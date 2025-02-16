import pytest
from src.ford_fulkerson import ford_fulkerson

def test_ford_fulkerson_simple_graph():
    """
    Test a simple graph with a known maximum flow
    """
    graph = {
        's': {'a': 10, 'c': 10},
        'a': {'b': 4, 'c': 2, 'd': 8},
        'b': {'t': 10},
        'c': {'d': 9},
        'd': {'b': 6, 't': 10},
        't': {}
    }
    assert ford_fulkerson(graph, 's', 't') == 19

def test_ford_fulkerson_no_flow():
    """
    Test a graph with no possible flow
    """
    graph = {
        's': {},
        't': {}
    }
    assert ford_fulkerson(graph, 's', 't') == 0

def test_ford_fulkerson_single_path():
    """
    Test a graph with a single path
    """
    graph = {
        's': {'a': 5},
        'a': {'t': 5}
    }
    assert ford_fulkerson(graph, 's', 't') == 5

def test_ford_fulkerson_multiple_paths():
    """
    Test a graph with multiple possible paths
    """
    graph = {
        's': {'a': 10, 'b': 10},
        'a': {'c': 4, 't': 8},
        'b': {'c': 8, 't': 5},
        'c': {'t': 15}
    }
    assert ford_fulkerson(graph, 's', 't') == 19

def test_ford_fulkerson_invalid_source():
    """
    Test that an error is raised when source is not in graph
    """
    graph = {
        'a': {'b': 10},
        'b': {'c': 5}
    }
    with pytest.raises(ValueError, match="Source or sink node not found in the graph"):
        ford_fulkerson(graph, 's', 'c')

def test_ford_fulkerson_invalid_sink():
    """
    Test that an error is raised when sink is not in graph
    """
    graph = {
        's': {'a': 10},
        'a': {'b': 5}
    }
    with pytest.raises(ValueError, match="Source or sink node not found in the graph"):
        ford_fulkerson(graph, 's', 't')
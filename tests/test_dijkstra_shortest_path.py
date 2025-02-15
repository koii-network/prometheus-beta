import pytest
from src.dijkstra_shortest_path import dijkstra_shortest_path

def test_basic_shortest_path():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    path, cost = dijkstra_shortest_path(graph, 'A', 'D')
    assert path == ['A', 'C', 'B', 'D']
    assert cost == 4

def test_direct_path():
    graph = {
        'A': {'B': 5},
        'B': {}
    }
    path, cost = dijkstra_shortest_path(graph, 'A', 'B')
    assert path == ['A', 'B']
    assert cost == 5

def test_no_path():
    graph = {
        'A': {},
        'B': {'C': 3},
        'C': {}
    }
    assert dijkstra_shortest_path(graph, 'A', 'C') is None

def test_single_node():
    graph = {
        'A': {}
    }
    assert dijkstra_shortest_path(graph, 'A', 'A') == (['A'], 0)

def test_invalid_node():
    graph = {
        'A': {'B': 5},
        'B': {}
    }
    with pytest.raises(ValueError):
        dijkstra_shortest_path(graph, 'A', 'C')
    with pytest.raises(ValueError):
        dijkstra_shortest_path(graph, 'C', 'B')

def test_complex_graph():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3, 'E': 1},
        'C': {'B': 1, 'D': 5},
        'D': {'E': 2},
        'E': {}
    }
    path, cost = dijkstra_shortest_path(graph, 'A', 'E')
    assert path == ['A', 'C', 'B', 'E']
    assert cost == 4
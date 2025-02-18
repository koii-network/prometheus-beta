import pytest
from src.dijkstra_shortest_path import dijkstra, reconstruct_path

def test_dijkstra_basic_graph():
    # Simple graph for testing
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }

    distances, previous_nodes = dijkstra(graph, 'A')

    # Expected distances
    assert distances == {
        'A': 0,
        'B': 3,  # A -> C -> B
        'C': 2,  # A -> C
        'D': 6   # A -> C -> B -> D
    }

def test_dijkstra_multiple_paths():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'D': 3},
        'C': {'D': 1},
        'D': {}
    }

    distances, previous_nodes = dijkstra(graph, 'A')

    assert distances['D'] == 4  # A -> B -> C -> D

def test_reconstruct_path():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }

    distances, previous_nodes = dijkstra(graph, 'A')
    path = reconstruct_path(previous_nodes, 'A', 'D')
    assert path == ['A', 'C', 'B', 'D']

def test_invalid_graph():
    with pytest.raises(ValueError):
        dijkstra({}, 'A')

    with pytest.raises(ValueError):
        dijkstra({'A': {}}, 'B')

def test_single_node_graph():
    graph = {'A': {}}
    
    distances, previous_nodes = dijkstra(graph, 'A')
    assert distances == {'A': 0}
    assert previous_nodes == {'A': None}

def test_disconnected_nodes():
    graph = {
        'A': {'B': 1},
        'C': {'D': 2}
    }

    distances, previous_nodes = dijkstra(graph, 'A')
    assert distances['C'] == float('inf')
    assert previous_nodes['C'] is None
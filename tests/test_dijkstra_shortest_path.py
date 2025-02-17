import pytest
from src.dijkstra_shortest_path import dijkstra_shortest_path

def test_basic_shortest_path():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    
    # Path from A to D
    result = dijkstra_shortest_path(graph, 'A', 'D')
    assert result is not None
    path, distance = result
    assert path == ['A', 'C', 'B', 'D']
    assert distance == 4  # 2 (A to C) + 1 (C to B) + 3 (B to D)

def test_same_start_and_end():
    graph = {
        'A': {'B': 4},
        'B': {}
    }
    
    # Path from A to A
    result = dijkstra_shortest_path(graph, 'A', 'A')
    assert result is not None
    path, distance = result
    assert path == ['A']
    assert distance == 0

def test_no_path_exists():
    graph = {
        'A': {'B': 4},
        'B': {},
        'C': {}
    }
    
    # No path from A to C
    result = dijkstra_shortest_path(graph, 'A', 'C')
    assert result is None

def test_multiple_paths():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'D': 3},
        'C': {'D': 2},
        'D': {}
    }
    
    # Path from A to D
    result = dijkstra_shortest_path(graph, 'A', 'D')
    assert result is not None
    path, distance = result
    assert path == ['A', 'C', 'D']
    assert distance == 6  # 4 (A to C) + 2 (C to D)

def test_invalid_graph():
    with pytest.raises(KeyError):
        dijkstra_shortest_path({}, 'A', 'B')

def test_invalid_start_node():
    graph = {
        'A': {'B': 4},
        'B': {}
    }
    with pytest.raises(KeyError):
        dijkstra_shortest_path(graph, 'C', 'B')
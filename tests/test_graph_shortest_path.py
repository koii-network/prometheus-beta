import pytest
from src.graph_shortest_path import find_shortest_path

def test_simple_path():
    graph = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3, 5],
        5: [4]
    }
    path = find_shortest_path(graph, 1, 5)
    assert path == [1, 2, 4, 5]

def test_same_start_end():
    graph = {
        1: [2, 3],
        2: [1],
        3: [1]
    }
    path = find_shortest_path(graph, 1, 1)
    assert path == [1]

def test_no_path():
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3]
    }
    path = find_shortest_path(graph, 1, 4)
    assert path is None

def test_invalid_nodes():
    graph = {
        1: [2],
        2: [1]
    }
    with pytest.raises(ValueError, match="Start or end node not in graph"):
        find_shortest_path(graph, 1, 3)
    
    with pytest.raises(ValueError, match="Start or end node not in graph"):
        find_shortest_path(graph, 3, 1)

def test_multiple_shortest_paths():
    graph = {
        1: [2, 3],
        2: [4],
        3: [4],
        4: [5],
        5: []
    }
    path = find_shortest_path(graph, 1, 5)
    assert 3 <= len(path) <= 4  # Acceptable path length
    assert path[0] == 1 and path[-1] == 5

def test_disconnected_graph():
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3],
        5: []
    }
    path = find_shortest_path(graph, 1, 5)
    assert path is None
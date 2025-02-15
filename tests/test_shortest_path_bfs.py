import pytest
from src.shortest_path_bfs import find_shortest_path

def test_basic_shortest_path():
    # Simple graph with a direct path
    graph = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3]
    }
    assert find_shortest_path(graph, 1, 4) == [1, 2, 4] or find_shortest_path(graph, 1, 4) == [1, 3, 4]

def test_multiple_paths():
    # Graph with multiple possible paths
    graph = {
        1: [2, 3],
        2: [4],
        3: [4],
        4: []
    }
    assert find_shortest_path(graph, 1, 4) == [1, 2, 4] or find_shortest_path(graph, 1, 4) == [1, 3, 4]

def test_no_path():
    # Graph with no path between nodes
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3]
    }
    assert find_shortest_path(graph, 1, 4) is None

def test_start_node_not_in_graph():
    graph = {
        2: [3],
        3: [2]
    }
    assert find_shortest_path(graph, 1, 3) is None

def test_end_node_not_in_graph():
    graph = {
        1: [2],
        2: [1]
    }
    assert find_shortest_path(graph, 1, 3) is None

def test_same_start_and_end():
    graph = {
        1: [2],
        2: [1]
    }
    assert find_shortest_path(graph, 1, 1) == [1]
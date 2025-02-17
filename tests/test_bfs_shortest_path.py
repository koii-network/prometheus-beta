import pytest
from src.bfs_shortest_path import bfs_shortest_path

def test_basic_path():
    graph = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3, 5],
        5: [4]
    }
    assert bfs_shortest_path(graph, 1, 5) == [1, 2, 4, 5]

def test_same_start_and_end():
    graph = {
        1: [2, 3],
        2: [1],
        3: [1]
    }
    assert bfs_shortest_path(graph, 1, 1) == [1]

def test_no_path():
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3]
    }
    assert bfs_shortest_path(graph, 1, 4) is None

def test_node_not_in_graph():
    graph = {
        1: [2],
        2: [1]
    }
    assert bfs_shortest_path(graph, 1, 3) is None
    assert bfs_shortest_path(graph, 3, 1) is None

def test_complex_path():
    graph = {
        1: [2, 3],
        2: [1, 4, 5],
        3: [1, 6],
        4: [2],
        5: [2, 6],
        6: [3, 5]
    }
    result = bfs_shortest_path(graph, 1, 6)
    assert result == [1, 3, 6] or result == [1, 2, 5, 6]
import pytest
from src.graph_utils import bfs_shortest_path

def test_bfs_shortest_path_direct_connection():
    graph = {
        1: [2],
        2: [1, 3],
        3: [2]
    }
    assert bfs_shortest_path(graph, 1, 3) == [1, 2, 3]

def test_bfs_shortest_path_multiple_hops():
    graph = {
        1: [2, 3],
        2: [4],
        3: [4],
        4: [1, 2, 3]
    }
    # Multiple possible shortest paths
    assert bfs_shortest_path(graph, 1, 4) in [[1, 2, 4], [1, 3, 4]]

def test_bfs_shortest_path_same_node():
    graph = {
        1: [2, 3],
        2: [3],
        3: [1]
    }
    assert bfs_shortest_path(graph, 1, 1) == [1]

def test_bfs_shortest_path_no_path():
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3]
    }
    assert bfs_shortest_path(graph, 1, 4) is None

def test_bfs_shortest_path_invalid_input():
    graph = {
        1: [2],
        2: [1]
    }
    assert bfs_shortest_path(graph, 3, 1) is None
    assert bfs_shortest_path({}, 1, 2) is None
    assert bfs_shortest_path(graph, 1, 3) is None
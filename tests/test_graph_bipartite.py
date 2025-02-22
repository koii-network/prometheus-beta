import pytest
from src.graph_bipartite import is_bipartite

def test_simple_bipartite_graph():
    graph = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }
    assert is_bipartite(graph) == True

def test_simple_non_bipartite_graph():
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }
    assert is_bipartite(graph) == False

def test_disconnected_bipartite_graph():
    graph = {
        0: [1],
        1: [0],
        2: [3],
        3: [2]
    }
    assert is_bipartite(graph) == True

def test_disconnected_non_bipartite_graph():
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1],
        3: [4],
        4: [5],
        5: [3]
    }
    assert is_bipartite(graph) == False

def test_single_node_graph():
    graph = {0: []}
    assert is_bipartite(graph) == True

def test_empty_graph_raises_error():
    with pytest.raises(ValueError):
        is_bipartite({})

def test_large_graph():
    graph = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5, 6],
        3: [1, 7],
        4: [1, 7],
        5: [2, 8],
        6: [2, 8],
        7: [3, 4],
        8: [5, 6]
    }
    assert is_bipartite(graph) == True
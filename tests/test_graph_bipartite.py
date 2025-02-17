import pytest
from src.graph_bipartite import is_bipartite

def test_bipartite_graph():
    # Simple bipartite graph
    graph1 = {
        1: [2, 4],
        2: [1, 3],
        3: [2, 4],
        4: [1, 3]
    }
    assert is_bipartite(graph1) == True

def test_non_bipartite_graph():
    # Graph with an odd-length cycle (not bipartite)
    graph2 = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2]
    }
    assert is_bipartite(graph2) == False

def test_disconnected_bipartite_graph():
    # Disconnected but still bipartite graph
    graph3 = {
        1: [2],
        2: [1],
        3: [4],
        4: [3]
    }
    assert is_bipartite(graph3) == True

def test_single_node_graph():
    # Single node graph is bipartite
    graph4 = {1: []}
    assert is_bipartite(graph4) == True

def test_empty_graph_raises_error():
    # Empty graph should raise ValueError
    with pytest.raises(ValueError):
        is_bipartite({})

def test_complex_bipartite_graph():
    # More complex bipartite graph
    graph5 = {
        1: [3, 5],
        2: [4, 6],
        3: [1, 7],
        4: [2, 8],
        5: [1, 7],
        6: [2, 8],
        7: [3, 5],
        8: [4, 6]
    }
    assert is_bipartite(graph5) == True

def test_complex_non_bipartite_graph():
    # Complex non-bipartite graph with multiple edges
    graph6 = {
        1: [2, 3],
        2: [1, 3, 4],
        3: [1, 2, 4],
        4: [2, 3]
    }
    assert is_bipartite(graph6) == False
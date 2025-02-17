import pytest
from src.bipartite_graph_check import is_bipartite

def test_bipartite_simple_graph():
    """Test a simple bipartite graph"""
    graph = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }
    assert is_bipartite(graph) == True

def test_non_bipartite_graph():
    """Test a graph that is not bipartite"""
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1]
    }
    assert is_bipartite(graph) == False

def test_disconnected_bipartite_graph():
    """Test a disconnected bipartite graph"""
    graph = {
        0: [1],
        1: [0],
        2: [3],
        3: [2]
    }
    assert is_bipartite(graph) == True

def test_empty_graph_raises_error():
    """Test that empty graph raises a ValueError"""
    with pytest.raises(ValueError):
        is_bipartite({})

def test_single_node_graph():
    """Test a graph with a single node"""
    graph = {0: []}
    assert is_bipartite(graph) == True

def test_complex_bipartite_graph():
    """Test a more complex bipartite graph"""
    graph = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3, 4],
        3: [0, 2],
        4: [2]
    }
    assert is_bipartite(graph) == True
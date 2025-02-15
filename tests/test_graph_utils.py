import pytest
from src.graph_utils import is_bipartite

def test_empty_graph():
    """Test that an empty graph is considered bipartite."""
    assert is_bipartite({}) == True

def test_simple_bipartite_graph():
    """Test a simple bipartite graph."""
    graph = {
        1: [2, 4],
        2: [1, 3],
        3: [2, 4],
        4: [1, 3]
    }
    assert is_bipartite(graph) == True

def test_non_bipartite_graph():
    """Test a graph that is not bipartite (contains an odd-length cycle)."""
    graph = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2]
    }
    assert is_bipartite(graph) == False

def test_disconnected_bipartite_graph():
    """Test a disconnected graph that is bipartite."""
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3],
        5: []
    }
    assert is_bipartite(graph) == True

def test_disconnected_non_bipartite_graph():
    """Test a disconnected graph that is not bipartite."""
    graph = {
        1: [2, 3],
        2: [1, 3],
        3: [1, 2],
        4: [5],
        5: [4]
    }
    assert is_bipartite(graph) == False

def test_complex_bipartite_graph():
    """Test a more complex bipartite graph."""
    graph = {
        1: [3, 5],
        2: [4, 6],
        3: [1, 7],
        4: [2, 8],
        5: [1, 7],
        6: [2, 8],
        7: [3, 5],
        8: [4, 6]
    }
    assert is_bipartite(graph) == True

def test_single_node_graph():
    """Test a graph with a single node."""
    graph = {1: []}
    assert is_bipartite(graph) == True
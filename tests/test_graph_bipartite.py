import pytest
from src.graph_bipartite import is_bipartite

def test_bipartite_graph():
    """Test a simple bipartite graph"""
    graph = [
        [1, 3],    # Vertex 0 connects to 1 and 3
        [0, 2],    # Vertex 1 connects to 0 and 2
        [1, 3],    # Vertex 2 connects to 1 and 3
        [0, 2]     # Vertex 3 connects to 0 and 2
    ]
    assert is_bipartite(graph) == True

def test_non_bipartite_graph():
    """Test a graph that is not bipartite"""
    graph = [
        [1, 2, 3],  # Vertex 0 connects to 1, 2, 3
        [0, 2],     # Vertex 1 connects to 0 and 2
        [0, 1, 3],  # Vertex 2 connects to 0, 1, 3
        [0, 2]      # Vertex 3 connects to 0 and 2
    ]
    assert is_bipartite(graph) == False

def test_single_vertex_graph():
    """Test a graph with a single vertex"""
    graph = [[]]
    assert is_bipartite(graph) == True

def test_disconnected_bipartite_graph():
    """Test a disconnected but bipartite graph"""
    graph = [
        [1],        # First component
        [0],
        [3],        # Second component
        [2]
    ]
    assert is_bipartite(graph) == True

def test_empty_graph_raises_error():
    """Test that empty graph raises ValueError"""
    with pytest.raises(ValueError):
        is_bipartite([])

def test_invalid_graph_input():
    """Test that invalid input raises ValueError"""
    with pytest.raises(ValueError):
        is_bipartite(None)

def test_complete_graph_three_vertices():
    """Test a complete graph with 3 vertices (not bipartite)"""
    graph = [
        [1, 2],
        [0, 2],
        [0, 1]
    ]
    assert is_bipartite(graph) == False
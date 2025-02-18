import pytest
from src.prims_algorithm import prims_algorithm

def test_prims_algorithm_simple_graph():
    """
    Test Prim's algorithm on a simple connected graph
    """
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2},
        'E': {'C': 10, 'D': 2}
    }
    
    mst = prims_algorithm(graph)
    
    # Check the MST edges (order might vary)
    expected_edges = {
        ('A', 'C', 2),
        ('C', 'B', 1),
        ('D', 'E', 2),
        ('B', 'D', 5)
    }
    
    assert len(mst) == 4  # MST should have n-1 edges for n vertices
    assert set(mst) == expected_edges

def test_prims_algorithm_empty_graph():
    """
    Test that an empty graph raises a ValueError
    """
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        prims_algorithm({})

def test_prims_algorithm_disconnected_graph():
    """
    Test that a disconnected graph raises a ValueError
    """
    graph = {
        'A': {'B': 1},
        'C': {'D': 2}
    }
    
    with pytest.raises(ValueError, match="Graph is not connected"):
        prims_algorithm(graph)

def test_prims_algorithm_single_vertex():
    """
    Test a graph with a single vertex
    """
    graph = {
        'A': {}
    }
    
    mst = prims_algorithm(graph)
    assert len(mst) == 0  # No edges in a single vertex graph

def test_prims_algorithm_all_same_weights():
    """
    Test a graph where all edges have the same weight
    """
    graph = {
        'A': {'B': 1, 'C': 1},
        'B': {'A': 1, 'C': 1},
        'C': {'A': 1, 'B': 1}
    }
    
    mst = prims_algorithm(graph)
    
    # The MST should have n-1 edges with minimal total weight
    assert len(mst) == 2
    assert all(edge[2] == 1 for edge in mst)
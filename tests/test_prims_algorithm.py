import pytest
from src.prims_algorithm import prims_algorithm

def test_simple_graph():
    """Test a simple connected graph"""
    graph = {
        0: [(1, 2), (2, 3)],
        1: [(0, 2), (2, 1), (3, 4)],
        2: [(0, 3), (1, 1), (3, 5)],
        3: [(1, 4), (2, 5)]
    }
    
    mst = prims_algorithm(graph)
    
    # Sort the MST edges for consistent comparison
    mst_sorted = sorted(mst, key=lambda x: x[2])
    
    # Expected MST should have len(graph) - 1 edges and total minimal weight
    assert len(mst) == len(graph) - 1
    
    # Verify the minimal spanning tree weights
    expected_mst_edges = [
        (1, 2, 1),   # min weight edge
        (0, 1, 2),   # next min weight edge
        (1, 3, 4)    # final edge 
    ]
    
    assert mst_sorted == expected_mst_edges

def test_empty_graph():
    """Test that an empty graph raises a ValueError"""
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        prims_algorithm({})

def test_disconnected_graph():
    """Test that a disconnected graph raises a ValueError"""
    graph = {
        0: [(1, 2)],
        1: [(0, 2)],
        2: [(3, 3)],
        3: [(2, 3)]
    }
    
    with pytest.raises(ValueError, match="Graph is not connected"):
        prims_algorithm(graph)

def test_single_vertex_graph():
    """Test a graph with a single vertex"""
    graph = {0: []}
    
    mst = prims_algorithm(graph)
    
    assert len(mst) == 0

def test_fully_connected_graph():
    """Test a fully connected graph"""
    graph = {
        0: [(1, 4), (2, 2), (3, 3)],
        1: [(0, 4), (2, 1), (3, 5)],
        2: [(0, 2), (1, 1), (3, 6)],
        3: [(0, 3), (1, 5), (2, 6)]
    }
    
    mst = prims_algorithm(graph)
    
    # Verify MST has correct number of edges
    assert len(mst) == len(graph) - 1
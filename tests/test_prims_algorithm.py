import pytest
from src.prims_algorithm import prims_mst

def test_basic_graph():
    """Test a simple connected graph"""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2},
        'E': {'C': 10, 'D': 2}
    }
    
    mst = prims_mst(graph)
    
    # Check the number of edges in MST (should be n-1 for n vertices)
    assert len(mst) == len(graph) - 1
    
    # Check total weight of MST (there's only one minimum spanning tree for this graph)
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 10

def test_empty_graph():
    """Test that an empty graph raises a ValueError"""
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        prims_mst({})

def test_disconnected_graph():
    """Test that a disconnected graph raises a ValueError"""
    graph = {
        'A': {'B': 1},
        'C': {'D': 2}
    }
    
    with pytest.raises(ValueError, match="Graph is not fully connected"):
        prims_mst(graph)

def test_single_vertex_graph():
    """Test a graph with only one vertex"""
    graph = {
        'A': {}
    }
    
    mst = prims_mst(graph)
    assert len(mst) == 0

def test_fully_connected_graph():
    """Test a fully connected graph"""
    graph = {
        'A': {'B': 5, 'C': 2, 'D': 4},
        'B': {'A': 5, 'C': 1, 'D': 3},
        'C': {'A': 2, 'B': 1, 'D': 6},
        'D': {'A': 4, 'B': 3, 'C': 6}
    }
    
    mst = prims_mst(graph)
    
    # Check the number of edges in MST
    assert len(mst) == len(graph) - 1
    
    # Verify the total minimum weight
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 7
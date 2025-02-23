import pytest
from src.prims_mst import prims_mst

def test_simple_graph():
    """Test a simple connected graph"""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
        'E': {'C': 10, 'D': 2, 'F': 3},
        'F': {'D': 6, 'E': 3}
    }
    
    mst = prims_mst(graph)
    
    # Check total number of edges
    assert len(mst) == len(graph) - 1
    
    # Check total weight (a simple validation)
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 13  # known MST weight for this graph

def test_disconnected_graph():
    """Test that an error is raised for a disconnected graph"""
    graph = {
        'A': {},
        'B': {},
        'C': {}
    }
    
    with pytest.raises(ValueError, match="Graph is not fully connected"):
        prims_mst(graph)

def test_disconnected_graph_with_components():
    """Test that an error is raised for a graph with unconnected components"""
    graph = {
        'A': {'B': 1},
        'B': {'A': 1},
        'C': {'D': 2},
        'D': {'C': 2}
    }
    
    with pytest.raises(ValueError, match="Graph is not fully connected"):
        prims_mst(graph)

def test_empty_graph():
    """Test that an error is raised for an empty graph"""
    graph = {}
    
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        prims_mst(graph)

def test_single_vertex_graph():
    """Test a graph with only a single vertex"""
    graph = {
        'A': {}
    }
    
    mst = prims_mst(graph)
    assert len(mst) == 0
    
def test_single_vertex_with_self_loop():
    """Test a graph with a single vertex and a self-loop"""
    graph = {
        'A': {'A': 1}
    }
    
    with pytest.raises(ValueError, match="Graph is not fully connected"):
        prims_mst(graph)

def test_graph_with_multiple_mst_options():
    """Test a graph where multiple minimum spanning trees are possible"""
    graph = {
        'A': {'B': 1, 'C': 1},
        'B': {'A': 1, 'C': 1},
        'C': {'A': 1, 'B': 1}
    }
    
    mst = prims_mst(graph)
    
    # Validate MST properties
    assert len(mst) == 2  # tree will have 2 edges
    assert len(set(vertex for edge in mst for vertex in edge[:2])) == 3
    
    # Verify total weight
    total_weight = sum(edge[2] for edge in mst)
    assert total_weight == 2  # known minimal total weight
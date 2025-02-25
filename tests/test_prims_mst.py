import pytest
from src.prims_mst import prims_mst

def test_basic_mst():
    """Test a simple connected graph with a known MST."""
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8},
        'D': {'B': 5, 'C': 8}
    }
    
    result = prims_mst(graph)
    
    # Verify the correct edges are in the MST
    expected_edges = {
        ('A', 'C', 2),
        ('C', 'B', 1),
        ('B', 'D', 5)
    }
    
    assert len(result) == 3
    assert set(result) == expected_edges

def test_empty_graph():
    """Test empty graph returns None."""
    assert prims_mst({}) is None

def test_single_node_graph():
    """Test graph with a single node."""
    graph = {'A': {}}
    assert prims_mst(graph) == []

def test_disconnected_graph():
    """Test that an algorithm returns None for disconnected graphs."""
    graph = {
        'A': {'B': 1},
        'B': {'A': 1},
        'C': {'D': 2},
        'D': {'C': 2}
    }
    assert prims_mst(graph) is None

def test_graph_with_duplicate_edges():
    """Test graph with multiple paths between nodes."""
    graph = {
        'A': {'B': 1, 'C': 3},
        'B': {'A': 1, 'C': 2, 'D': 4},
        'C': {'A': 3, 'B': 2, 'D': 5},
        'D': {'B': 4, 'C': 5}
    }
    
    result = prims_mst(graph)
    
    # Verify the correct minimal spanning tree
    expected_edges = {
        ('A', 'B', 1),
        ('B', 'C', 2),
        ('B', 'D', 4)
    }
    
    assert len(result) == 3
    assert set(result) == expected_edges

def test_fully_connected_graph():
    """Test a fully connected graph."""
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 3},
        'C': {'A': 4, 'B': 2, 'D': 5},
        'D': {'B': 3, 'C': 5}
    }
    
    result = prims_mst(graph)
    
    # Verify three edges forming the minimum spanning tree
    assert len(result) == 3
    total_weight = sum(edge[2] for edge in result)
    assert total_weight == 6

def test_type_error():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        prims_mst(None)
    
    with pytest.raises(TypeError):
        prims_mst(42)
    
    with pytest.raises(TypeError):
        prims_mst("not a graph")
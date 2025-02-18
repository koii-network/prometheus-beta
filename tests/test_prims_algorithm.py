import pytest
from src.prims_algorithm import prims_minimum_spanning_tree

def test_prims_algorithm_simple_graph():
    # Simple connected graph
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2},
        'E': {'C': 10, 'D': 2}
    }
    
    mst = prims_minimum_spanning_tree(graph)
    
    # Expected MST edges (may have different order due to algorithm)
    expected_edges = {
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('D', 'E', 2),
        ('B', 'D', 5)
    }
    
    assert len(mst) == 4  # MST should have n-1 edges for n vertices
    assert set(mst) == expected_edges

def test_prims_algorithm_error_handling():
    # Test empty graph
    with pytest.raises(ValueError, match="Graph cannot be empty"):
        prims_minimum_spanning_tree({})
    
    # Test disconnected graph
    disconnected_graph = {
        'A': {'B': 1},
        'C': {'D': 2}
    }
    with pytest.raises(ValueError, match="Graph is not connected"):
        prims_minimum_spanning_tree(disconnected_graph)

def test_prims_algorithm_single_vertex():
    # Single vertex graph
    graph = {
        'A': {}
    }
    
    mst = prims_minimum_spanning_tree(graph)
    assert len(mst) == 0  # No edges in a single vertex graph

def test_prims_algorithm_fully_connected_graph():
    # Fully connected graph
    graph = {
        'A': {'B': 5, 'C': 2, 'D': 4},
        'B': {'A': 5, 'C': 1, 'D': 3},
        'C': {'A': 2, 'B': 1, 'D': 6},
        'D': {'A': 4, 'B': 3, 'C': 6}
    }
    
    mst = prims_minimum_spanning_tree(graph)
    
    # Verify total weight and number of edges
    total_mst_weight = sum(edge[2] for edge in mst)
    assert len(mst) == 3  # n-1 edges for n vertices
    assert total_mst_weight == 6  # Minimum total weight
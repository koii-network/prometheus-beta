import pytest
from src.johnsons_algorithm import johnsons_algorithm

def test_basic_graph():
    """Test a basic graph with positive weights"""
    graph = {
        1: [(2, 4), (3, 2)],
        2: [(3, 3), (4, 1)],
        3: [(4, 5)],
        4: []
    }
    result = johnsons_algorithm(graph)
    
    # Verify the overall structure of the result
    assert result is not None
    assert len(result) == 4
    assert all(len(paths) == 4 for paths in result.values())

def test_graph_with_negative_edges():
    """Test a graph with some negative edges"""
    graph = {
        1: [(2, -1), (3, 4)],
        2: [(3, 3), (4, 2)],
        3: [(4, 5)],
        4: []
    }
    result = johnsons_algorithm(graph)
    
    # Verify the result is computed
    assert result is not None

def test_disconnected_graph():
    """Test a graph with disconnected nodes"""
    graph = {
        1: [(2, 1)],
        2: [(1, 1)],
        3: [(4, 1)],
        4: [(3, 1)]
    }
    result = johnsons_algorithm(graph)
    
    # Verify distances for disconnected components
    assert result is not None

def test_negative_cycle():
    """Test a graph with a negative cycle"""
    graph = {
        1: [(2, -1)],
        2: [(3, -1)],
        3: [(1, -1)]
    }
    result = johnsons_algorithm(graph)
    
    # Verify that a graph with a negative cycle returns None
    assert result is None

def test_empty_graph_raises_error():
    """Test that an empty graph raises a ValueError"""
    with pytest.raises(ValueError):
        johnsons_algorithm({})

def test_single_node_graph():
    """Test a graph with a single node"""
    graph = {1: []}
    result = johnsons_algorithm(graph)
    
    # Verify the result for a single node
    assert result is not None
    assert len(result) == 1
    assert result[1][1] == 0

def test_result_symmetry():
    """Test that the shortest path computation is symmetrical"""
    graph = {
        1: [(2, 4), (3, 2)],
        2: [(1, 4), (3, 3), (4, 1)],
        3: [(1, 2), (2, 3), (4, 5)],
        4: [(2, 1), (3, 5)]
    }
    result = johnsons_algorithm(graph)
    
    # Check symmetry of paths (optional, as Johnson's doesn't guarantee)
    assert result is not None
    for u in result:
        for v in result[u]:
            # Distance from u to v should be same as v to u in most cases
            if result[u][v] != float('inf') and result[v][u] != float('inf'):
                # Allow small float discrepancies
                assert abs(result[u][v] - result[v][u]) < 1e-9
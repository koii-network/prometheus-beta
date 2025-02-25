import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from johnsons_algorithm import johnsons_algorithm

def test_basic_graph():
    """Test a basic graph with multiple vertices and positive weights."""
    graph = {
        0: {1: 5, 2: 2},
        1: {2: 1, 3: 3},
        2: {3: 6, 4: 4},
        3: {4: 2},
        4: {}
    }
    
    result = johnsons_algorithm(graph)
    
    # Verify basic properties
    assert result is not None
    assert len(result) == len(graph)
    
    # Spot check some expected paths
    assert result[0][4] == 6  # 0 -> 2 -> 4 path
    assert result[1][4] == 5  # 1 -> 2 -> 4 path

def test_disconnected_graph():
    """Test a graph with disconnected vertices."""
    graph = {
        0: {1: 1},
        1: {0: 1},
        2: {3: 1},
        3: {2: 1},
        4: {}
    }
    
    result = johnsons_algorithm(graph)
    
    assert result is not None
    assert len(result) == len(graph)
    assert result[0].get(4) is None  # No path between disconnected vertices

def test_complete_graph():
    """Test a fully connected graph."""
    graph = {
        0: {1: 1, 2: 4, 3: 3},
        1: {0: 1, 2: 2, 3: 5},
        2: {0: 4, 1: 2, 3: 1},
        3: {0: 3, 1: 5, 2: 1}
    }
    
    result = johnsons_algorithm(graph)
    
    assert result is not None
    assert len(result) == len(graph)
    
    # Verify symmetry and consistency
    for u in graph:
        for v in graph:
            if u != v:
                assert result[u][v] is not None

def test_single_vertex_graph():
    """Test a graph with a single vertex."""
    graph = {0: {}}
    
    result = johnsons_algorithm(graph)
    
    assert result is not None
    assert len(result) == 1
    assert len(result[0]) == 0

def test_error_handling():
    """Test error handling for invalid input."""
    with pytest.raises(ValueError):
        johnsons_algorithm({})

def test_negative_edges_graph():
    """Test a graph with negative (but non-negative cycle) edges."""
    graph = {
        0: {1: -1, 2: 4},
        1: {2: 3, 3: 2},
        2: {3: 5},
        3: {}
    }
    
    result = johnsons_algorithm(graph)
    
    assert result is not None

def test_negative_cycle_graph():
    """Test a graph with a negative cycle."""
    graph = {
        0: {1: 1},
        1: {2: -3},
        2: {0: -2}
    }
    
    result = johnsons_algorithm(graph)
    
    assert result is None  # Johnson's should detect and return None
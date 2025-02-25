import pytest
import sys
import os

# Ensure the src directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from bellman_ford import bellman_ford

def test_basic_graph():
    """Test a simple graph with positive edge weights"""
    graph = [
        (0, 1, 4),   # Vertex 0 to 1, weight 4
        (0, 2, 3),   # Vertex 0 to 2, weight 3
        (1, 2, 1),   # Vertex 1 to 2, weight 1
        (1, 3, 2),   # Vertex 1 to 3, weight 2
        (2, 3, 5)    # Vertex 2 to 3, weight 5
    ]
    
    result = bellman_ford(graph, 0, 4)
    assert result is not None
    
    # Check specific distances
    assert result[0] == 0    # Distance to start vertex is 0
    assert result[1] == 4    # 0 -> 1
    assert result[2] == 3    # 0 -> 2
    assert result[3] == 6    # 0 -> 1 -> 3

def test_graph_with_negative_edges():
    """Test a graph with some negative edge weights"""
    graph = [
        (0, 1, -1),  # Vertex 0 to 1, weight -1
        (0, 2, 4),   # Vertex 0 to 2, weight 4
        (1, 2, 3),   # Vertex 1 to 2, weight 3
        (1, 3, 2),   # Vertex 1 to 3, weight 2
        (3, 2, 5)    # Vertex 3 to 2, weight 5
    ]
    
    result = bellman_ford(graph, 0, 4)
    assert result is not None
    
    # Check specific distances
    assert result[0] == 0    # Distance to start vertex is 0
    assert result[1] == -1   # 0 -> 1
    assert result[2] == 2    # 0 -> 1 -> 2
    assert result[3] == 1    # 0 -> 1 -> 3

def test_negative_cycle_detection():
    """Test that the algorithm detects negative cycles"""
    graph = [
        (0, 1, 1),   # Vertex 0 to 1, weight 1
        (1, 2, -3),  # Vertex 1 to 2, weight -3
        (2, 0, -2)   # Vertex 2 back to 0, weight -2
    ]
    
    result = bellman_ford(graph, 0, 3)
    assert result is None  # Negative cycle should return None

def test_disconnected_vertex():
    """Test a graph with a vertex that cannot be reached"""
    graph = [
        (0, 1, 4),   # Vertex 0 to 1, weight 4
        (1, 2, 3)    # Vertex 1 to 2, weight 3
    ]
    
    result = bellman_ford(graph, 0, 4)
    assert result is not None
    assert result[3] == float('inf')  # Unreachable vertex

def test_invalid_start_vertex():
    """Test handling of invalid start vertex"""
    graph = [
        (0, 1, 4),
        (1, 2, 3)
    ]
    
    with pytest.raises(ValueError):
        bellman_ford(graph, 4, 3)  # Start vertex out of range
    
    with pytest.raises(ValueError):
        bellman_ford(graph, -1, 3)  # Negative start vertex

def test_empty_graph():
    """Test an empty graph"""
    graph = []
    
    with pytest.raises(ValueError):
        bellman_ford(graph, 0, 0)
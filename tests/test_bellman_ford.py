import pytest
from src.bellman_ford import bellman_ford

def test_simple_graph():
    # Simple graph without negative cycles
    graph = [
        (0, 1, 5),   # Edge from vertex 0 to vertex 1, weight 5
        (0, 2, 2),   # Edge from vertex 0 to vertex 2, weight 2
        (1, 2, -3),  # Edge from vertex 1 to vertex 2, weight -3
        (2, 3, 1),   # Edge from vertex 2 to vertex 3, weight 1
        (3, 1, 4)    # Edge from vertex 3 to vertex 1, weight 4
    ]
    
    # Expected shortest path distances from vertex 0
    result = bellman_ford(graph, 0, 4)
    assert result is not None
    
    # Verify specific distances
    assert result[0] == 0     # Distance to start vertex is 0
    assert result[1] == 1     # Distance to vertex 1 should be 1
    assert result[2] == -1    # Distance to vertex 2 should be -1
    assert result[3] == 0     # Distance to vertex 3 should be 0

def test_negative_cycle():
    # Graph with a negative cycle
    graph = [
        (0, 1, 1),
        (1, 2, -3),
        (2, 0, -2)  # Creates a negative cycle
    ]
    
    # Should return None when a negative cycle exists
    result = bellman_ford(graph, 0, 3)
    assert result is None

def test_disconnected_graph():
    # Graph with an unreachable vertex
    graph = [
        (0, 1, 5),
        (0, 2, 2)
    ]
    
    result = bellman_ford(graph, 0, 4)
    assert result is not None
    
    # Verify unreachable vertices remain at infinity
    assert result[3] == float('inf')

def test_single_vertex():
    # Graph with just one vertex
    graph = []
    
    result = bellman_ford(graph, 0, 1)
    assert result is not None
    assert result[0] == 0  # Distance to start vertex is always 0
    assert len(result) == 1

def test_invalid_arguments():
    # Test with invalid number of vertices
    with pytest.raises(KeyError):
        bellman_ford([(0, 1, 5)], 0, 0)
    
    # Test with start vertex out of range
    with pytest.raises(KeyError):
        bellman_ford([(0, 1, 5)], 2, 2)
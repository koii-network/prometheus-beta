import pytest
from src.bellman_ford import bellman_ford

def test_basic_shortest_path():
    # Simple graph with known shortest paths
    graph = [
        (0, 1, 4),   # edge from 0 to 1 with weight 4
        (0, 2, 3),   # edge from 0 to 2 with weight 3
        (1, 2, 1),   # edge from 1 to 2 with weight 1
        (1, 3, 2),   # edge from 1 to 3 with weight 2
        (2, 3, 5)    # edge from 2 to 3 with weight 5
    ]
    distances = bellman_ford(graph, 0, 4)
    
    assert distances is not None
    assert distances[0] == 0     # source to itself is 0
    assert distances[1] == 4     # 0 -> 1 
    assert distances[2] == 3     # 0 -> 2
    assert distances[3] == 6     # 0 -> 1 -> 3

def test_negative_weights():
    # Graph with negative weights (but no negative cycle)
    graph = [
        (0, 1, -1),
        (0, 2, 4),
        (1, 2, 3),
        (1, 3, 2),
        (3, 2, 5)
    ]
    distances = bellman_ford(graph, 0, 4)
    
    assert distances is not None
    assert distances[0] == 0
    assert distances[1] == -1
    assert distances[2] == 2
    assert distances[3] == 1

def test_negative_cycle_detection():
    # Graph with a negative cycle
    graph = [
        (0, 1, 1),
        (1, 2, -3),
        (2, 0, -2)  # Creates a negative cycle
    ]
    
    # Should return None due to negative cycle
    distances = bellman_ford(graph, 0, 3)
    assert distances is None

def test_disconnected_graph():
    # Graph with a vertex unreachable from source
    graph = [
        (0, 1, 4),
        (1, 2, 3)
        # Vertex 3 is disconnected
    ]
    
    distances = bellman_ford(graph, 0, 4)
    
    assert distances is not None
    assert distances[0] == 0
    assert distances[1] == 4
    assert distances[2] == 7
    assert distances[3] == float('inf')

def test_single_vertex():
    # Graph with just one vertex
    graph = []
    
    distances = bellman_ford(graph, 0, 1)
    
    assert distances is not None
    assert distances[0] == 0

def test_invalid_inputs():
    # Test that function handles different graph sizes correctly
    with pytest.raises(Exception):
        bellman_ford([], 0, 0)  # No vertices
    
    with pytest.raises(Exception):
        bellman_ford([], 5, 1)  # Source out of range
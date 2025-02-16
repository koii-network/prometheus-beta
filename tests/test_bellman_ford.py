import pytest
from src.bellman_ford import bellman_ford

def test_bellman_ford_basic_graph():
    # Simple graph with positive weights
    graph = {
        0: [(1, 4), (2, 3)],
        1: [(2, 1), (3, 2)],
        2: [(3, 5)],
        3: []
    }
    
    distances, predecessors = bellman_ford(graph, 0)
    
    # Expected shortest distances from node 0
    expected_distances = {0: 0, 1: 4, 2: 3, 3: 6}
    
    assert distances == expected_distances
    assert predecessors[1] == 0  # Path to 1 goes through 0
    assert predecessors[2] == 0  # Path to 2 goes through 0
    assert predecessors[3] == 1  # Path to 3 goes through 1

def test_bellman_ford_single_node():
    # Graph with a single node
    graph = {0: []}
    
    distances, predecessors = bellman_ford(graph, 0)
    
    assert distances == {0: 0}
    assert predecessors == {0: None}

def test_bellman_ford_negative_weights():
    # Graph with negative weights (but no negative cycles)
    graph = {
        0: [(1, -1), (2, 4)],
        1: [(2, 3), (3, 2)],
        2: [(3, 5)],
        3: []
    }
    
    distances, predecessors = bellman_ford(graph, 0)
    
    # Expected shortest distances from node 0
    expected_distances = {0: 0, 1: -1, 2: 2, 3: 1}
    
    assert distances == expected_distances

def test_bellman_ford_negative_cycle():
    # Graph with a negative weight cycle
    graph = {
        0: [(1, 1)],
        1: [(2, -3)],
        2: [(0, -2)]
    }
    
    with pytest.raises(ValueError, match="Graph contains a negative weight cycle"):
        bellman_ford(graph, 0)
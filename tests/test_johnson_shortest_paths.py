import pytest
import math
from src.johnson_shortest_paths import johnson_shortest_paths, bellman_ford, dijkstra

def test_johnson_basic_graph():
    # Basic graph with positive weights
    graph = {
        0: [(1, 5), (2, 3)],
        1: [(2, 2), (3, 4)],
        2: [(3, 1)],
        3: []
    }
    
    result = johnson_shortest_paths(graph)
    assert result is not None
    
    # Check specific path distances
    assert result[0][1] == 5  # 0 -> 1
    assert result[0][2] == 3  # 0 -> 2
    assert result[0][3] == 4  # 0 -> 3
    assert result[1][3] == 4  # 1 -> 3
    assert result[2][3] == 1  # 2 -> 3

def test_johnson_negative_weights():
    # Graph with negative weights (but no negative cycles)
    graph = {
        0: [(1, -1), (2, 4)],
        1: [(2, 3), (3, 2)],
        2: [(3, 5)],
        3: []
    }
    
    result = johnson_shortest_paths(graph)
    assert result is not None
    
    # Check specific path distances
    assert result[0][1] == -1  # 0 -> 1
    assert result[0][2] == 2   # 0 -> 2
    assert result[0][3] == 1   # 0 -> 3

def test_johnson_negative_cycle():
    # Graph with a negative cycle
    graph = {
        0: [(1, 1)],
        1: [(2, -3)],
        2: [(0, -2)]
    }
    
    result = johnson_shortest_paths(graph)
    assert result is None

def test_johnson_single_vertex():
    # Single vertex graph
    graph = {0: []}
    
    result = johnson_shortest_paths(graph)
    assert result is not None
    assert len(result) == 1
    assert result[0][0] == 0

def test_bellman_ford_basic():
    graph = {
        0: [(1, 5), (2, 3)],
        1: [(2, 2), (3, 4)],
        2: [(3, 1)],
        3: []
    }
    
    result = bellman_ford(graph, 0)
    assert result is not None
    assert result[0] == 0
    assert result[1] == 5
    assert result[2] == 3
    assert result[3] == 4

def test_bellman_ford_negative_cycle():
    graph = {
        0: [(1, 1)],
        1: [(2, -3)],
        2: [(0, -2)]
    }
    
    result = bellman_ford(graph, 0)
    assert result is None
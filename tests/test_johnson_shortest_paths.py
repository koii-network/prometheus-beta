import pytest
from src.johnson_shortest_paths import johnson_shortest_paths, bellman_ford, dijkstra

def test_johnson_shortest_paths_simple_graph():
    # Simple graph with positive weights
    graph = {
        1: [(2, 4), (3, 2)],
        2: [(3, 3), (4, 1)],
        3: [(4, 5)],
        4: []
    }
    
    result = johnson_shortest_paths(graph)
    
    # Check that result is not None
    assert result is not None
    
    # Verify specific path lengths
    assert result[1][4] == 5  # 1 -> 2 -> 4 path
    assert result[1][3] == 2  # 1 -> 3 direct path
    assert result[2][4] == 1  # 2 -> 4 direct path

def test_johnson_shortest_paths_negative_weights():
    # Graph with some negative weights
    graph = {
        1: [(2, -1), (3, 4)],
        2: [(3, 3), (4, 2)],
        3: [(4, 5)],
        4: []
    }
    
    result = johnson_shortest_paths(graph)
    
    # Check that result is not None
    assert result is not None
    
    # Verify specific path lengths
    assert result[1][4] == 1  # Shortest path might go through vertices to avoid higher total cost

def test_johnson_shortest_paths_negative_cycle():
    # Graph with a negative cycle
    graph = {
        1: [(2, -1)],
        2: [(3, -1)],
        3: [(1, -1)]
    }
    
    result = johnson_shortest_paths(graph)
    
    # Verify negative cycle detection
    assert result is None

def test_johnson_shortest_paths_empty_graph():
    # Empty graph should raise ValueError
    with pytest.raises(ValueError):
        johnson_shortest_paths({})

def test_bellman_ford_basic():
    # Basic graph for Bellman-Ford testing
    graph = {
        1: [(2, 4), (3, 2)],
        2: [(3, 3), (4, 1)],
        3: [(4, 5)],
        4: []
    }
    
    potentials = bellman_ford(graph, 1)
    
    # Check potentials are computed (not None)
    assert potentials is not None
    assert isinstance(potentials, dict)
    assert len(potentials) == 4

def test_dijkstra_basic():
    # Basic graph for Dijkstra testing
    graph = {
        1: [(2, 4), (3, 2)],
        2: [(3, 3), (4, 1)],
        3: [(4, 5)],
        4: []
    }
    
    distances = dijkstra(graph, 1)
    
    # Check distances are computed correctly
    assert distances[1] == 0
    assert distances[4] == 5  # 1 -> 2 -> 4 path
import pytest
from src.johnson_shortest_paths import johnson_shortest_paths

def test_johnson_shortest_paths_basic():
    # Simple graph with positive weights
    graph = {
        0: [(1, 5), (2, 2)],
        1: [(2, 1), (3, 3)],
        2: [(3, 6)],
        3: []
    }
    
    result = johnson_shortest_paths(graph)
    
    # Check specific path lengths
    assert result[0][1] == 5  # Path from 0 to 1
    assert result[0][2] == 2  # Path from 0 to 2
    assert result[0][3] == 8  # Path from 0 to 3 (0 -> 2 -> 1 -> 3)

def test_johnson_shortest_paths_disconnected():
    # Graph with some disconnected vertices
    graph = {
        0: [(1, 5)],
        1: [(2, 3)],
        2: [],
        3: []
    }
    
    result = johnson_shortest_paths(graph)
    
    # Verify path lengths and disconnected vertices
    assert result[0][1] == 5
    assert result[0][2] == float('inf')
    assert result[0][3] == float('inf')

def test_johnson_shortest_paths_negative_weights():
    # Graph with negative weights (but no negative cycles)
    graph = {
        0: [(1, -1), (2, 4)],
        1: [(2, 3), (3, 2)],
        2: [(3, 5)],
        3: []
    }
    
    result = johnson_shortest_paths(graph)
    
    # Check specific path lengths with negative weights
    assert result[0][1] == -1
    assert result[0][2] == 2
    assert result[0][3] == 1

def test_johnson_shortest_paths_empty_graph():
    # Empty graph
    graph = {}
    
    result = johnson_shortest_paths(graph)
    
    # Should return an empty dictionary
    assert result == {}

def test_johnson_shortest_paths_negative_cycle():
    # Graph with a negative cycle should raise ValueError
    graph = {
        0: [(1, 1)],
        1: [(2, -3)],
        2: [(0, -2)]
    }
    
    with pytest.raises(ValueError, match="Graph contains a negative cycle"):
        johnson_shortest_paths(graph)

def test_johnson_shortest_paths_single_vertex():
    # Graph with a single vertex
    graph = {0: []}
    
    result = johnson_shortest_paths(graph)
    
    # Should have a result for the single vertex
    assert len(result) == 1
    assert len(result[0]) == 1
    assert result[0][0] == 0

def test_johnson_shortest_paths_complex_graph():
    # More complex graph with multiple paths
    graph = {
        0: [(1, 3), (2, 6)],
        1: [(2, 1), (3, 4)],
        2: [(3, 2), (4, 2)],
        3: [(4, 5)],
        4: []
    }
    
    result = johnson_shortest_paths(graph)
    
    # Verify some specific path lengths
    assert result[0][1] == 3
    assert result[0][2] == 4  # 0 -> 1 -> 2
    assert result[0][3] == 7  # 0 -> 1 -> 3 or 0 -> 2 -> 3
    assert result[0][4] == 6  # 0 -> 2 -> 4
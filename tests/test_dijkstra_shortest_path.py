import pytest
from src.dijkstra_shortest_path import dijkstra_shortest_path

def test_basic_shortest_path():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    
    # Test finding shortest path from A to D
    result = dijkstra_shortest_path(graph, 'A', 'D')
    assert result is not None
    path, distance = result
    assert path == ['A', 'C', 'B', 'D']
    assert distance == 4  # 2 (A to C) + 1 (C to B) + 3 (B to D)

def test_same_start_and_end():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    
    # Test when start and end are the same
    result = dijkstra_shortest_path(graph, 'A', 'A')
    assert result is not None
    path, distance = result
    assert path == ['A']
    assert distance == 0

def test_no_path_exists():
    graph = {
        'A': {'B': 4},
        'B': {},
        'C': {'D': 3},
        'D': {}
    }
    
    # Test when no path exists between nodes
    result = dijkstra_shortest_path(graph, 'A', 'C')
    assert result is None

def test_nonexistent_nodes():
    graph = {
        'A': {'B': 4},
        'B': {}
    }
    
    # Test with nodes not in the graph
    result = dijkstra_shortest_path(graph, 'A', 'X')
    assert result is None
    
    result = dijkstra_shortest_path(graph, 'X', 'B')
    assert result is None

def test_complex_path():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'C': 2, 'D': 5},
        'C': {'D': 1},
        'D': {}
    }
    
    # Test finding the most optimal path
    result = dijkstra_shortest_path(graph, 'A', 'D')
    assert result is not None
    path, distance = result
    assert path == ['A', 'B', 'C', 'D']
    assert distance == 4  # 1 (A to B) + 2 (B to C) + 1 (C to D)
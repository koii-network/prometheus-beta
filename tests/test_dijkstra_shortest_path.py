import pytest
from src.dijkstra_shortest_path import dijkstra_shortest_path

def test_basic_shortest_path():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    
    # Test basic path finding
    result = dijkstra_shortest_path(graph, 'A', 'D')
    assert result is not None
    path, distance = result
    assert path == ['A', 'C', 'B', 'D']
    assert distance == 4

def test_direct_path():
    graph = {
        'A': {'B': 5},
        'B': {}
    }
    
    # Test direct path
    result = dijkstra_shortest_path(graph, 'A', 'B')
    assert result is not None
    path, distance = result
    assert path == ['A', 'B']
    assert distance == 5

def test_no_path():
    graph = {
        'A': {},
        'B': {}
    }
    
    # Test no path exists
    result = dijkstra_shortest_path(graph, 'A', 'B')
    assert result is None

def test_same_start_end():
    graph = {
        'A': {'B': 5},
        'B': {}
    }
    
    # Test when start and end are the same
    result = dijkstra_shortest_path(graph, 'A', 'A')
    assert result is not None
    path, distance = result
    assert path == ['A']
    assert distance == 0

def test_invalid_node():
    graph = {
        'A': {'B': 5},
        'B': {}
    }
    
    # Test invalid start or end node
    with pytest.raises(ValueError):
        dijkstra_shortest_path(graph, 'C', 'A')
    
    with pytest.raises(ValueError):
        dijkstra_shortest_path(graph, 'A', 'C')
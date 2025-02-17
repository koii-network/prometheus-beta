import pytest
from src.dijkstra_shortest_path import dijkstra_shortest_path

def test_basic_shortest_path():
    # Simple graph with a clear shortest path
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    
    path, distance = dijkstra_shortest_path(graph, 'A', 'D')
    assert path == ['A', 'C', 'B', 'D']
    assert distance == 4

def test_direct_path():
    # Graph with a direct path
    graph = {
        'A': {'B': 5},
        'B': {}
    }
    
    path, distance = dijkstra_shortest_path(graph, 'A', 'B')
    assert path == ['A', 'B']
    assert distance == 5

def test_no_path():
    # Graph with no path between nodes
    graph = {
        'A': {},
        'B': {}
    }
    
    assert dijkstra_shortest_path(graph, 'A', 'B') is None

def test_complex_path():
    # More complex graph with multiple possible routes
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3, 'E': 1},
        'C': {'B': 1, 'D': 5},
        'D': {'E': 2},
        'E': {}
    }
    
    path, distance = dijkstra_shortest_path(graph, 'A', 'E')
    assert path == ['A', 'C', 'B', 'E']
    assert distance == 4

def test_invalid_start_node():
    # Test with non-existent start node
    graph = {
        'A': {'B': 5},
        'B': {}
    }
    
    with pytest.raises(ValueError, match="Start node 'C' not found in graph"):
        dijkstra_shortest_path(graph, 'C', 'B')

def test_invalid_end_node():
    # Test with non-existent end node
    graph = {
        'A': {'B': 5},
        'B': {}
    }
    
    with pytest.raises(ValueError, match="End node 'C' not found in graph"):
        dijkstra_shortest_path(graph, 'A', 'C')
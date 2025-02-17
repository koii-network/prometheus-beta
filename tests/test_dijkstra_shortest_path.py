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

def test_no_path_exists():
    # Graph with no path between start and end
    graph = {
        'A': {'B': 4},
        'B': {'A': 4},
        'C': {'D': 5},
        'D': {'C': 5}
    }
    
    result = dijkstra_shortest_path(graph, 'A', 'C')
    assert result is None

def test_start_equals_end():
    # Graph where start and end are the same node
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'C': 1},
        'C': {}
    }
    
    path, distance = dijkstra_shortest_path(graph, 'A', 'A')
    assert path == ['A']
    assert distance == 0

def test_invalid_nodes():
    # Graph with non-existent start or end nodes
    graph = {
        'A': {'B': 4},
        'B': {'A': 4}
    }
    
    # Test with non-existent start node
    result1 = dijkstra_shortest_path(graph, 'C', 'A')
    assert result1 is None
    
    # Test with non-existent end node
    result2 = dijkstra_shortest_path(graph, 'A', 'C')
    assert result2 is None

def test_complex_graph():
    # More complex graph with multiple possible paths
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
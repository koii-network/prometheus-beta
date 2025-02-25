import pytest
from src.dijkstra import dijkstra, reconstruct_path

def test_dijkstra_basic_graph():
    # Simple graph with known shortest paths
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    
    # Test distances
    distances, previous = dijkstra(graph, 'A')
    assert distances == {
        'A': 0,
        'B': 3,  # A -> C -> B
        'C': 2,  # A -> C
        'D': 6   # A -> C -> B -> D
    }

def test_dijkstra_no_path_graph():
    graph = {
        'A': {},
        'B': {},
        'C': {}
    }
    
    # Test with no connections
    distances, previous = dijkstra(graph, 'A')
    assert distances == {
        'A': 0,
        'B': float('inf'),
        'C': float('inf')
    }

def test_dijkstra_invalid_start_node():
    graph = {
        'A': {'B': 1},
        'B': {}
    }
    
    with pytest.raises(ValueError, match="Start node X not found in graph"):
        dijkstra(graph, 'X')

def test_reconstruct_path():
    previous_nodes = {
        'A': None,
        'B': 'A',
        'C': 'A',
        'D': 'B'
    }
    
    path = reconstruct_path(previous_nodes, 'A', 'D')
    assert path == ['A', 'B', 'D']

def test_reconstruct_path_no_path():
    previous_nodes = {
        'A': None,
        'B': 'A',
        'C': 'B'
    }
    
    with pytest.raises(ValueError, match="No path exists between A and C"):
        reconstruct_path(previous_nodes, 'A', 'C')

def test_dijkstra_complex_graph():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3, 'E': 1},
        'C': {'B': 1, 'D': 5, 'E': 6},
        'D': {'E': 2},
        'E': {}
    }
    
    distances, previous = dijkstra(graph, 'A')
    assert distances['E'] == 4  # Shortest path: A -> B -> E
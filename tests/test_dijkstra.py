import pytest
from src.dijkstra import dijkstra, reconstruct_path

def test_dijkstra_basic_graph():
    # Simple graph
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
    
    # Test path reconstruction
    path_to_d = reconstruct_path(previous, 'A', 'D')
    assert path_to_d == ['A', 'C', 'B', 'D']

def test_dijkstra_disconnected_node():
    # Graph with a disconnected node
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2},
        'C': {'A': 4, 'B': 2},
        'D': {}  # Completely disconnected
    }
    
    distances, previous = dijkstra(graph, 'A')
    
    assert distances['D'] == float('inf')
    assert previous['D'] is None

def test_dijkstra_single_node():
    # Single node graph
    graph = {
        'A': {}
    }
    
    distances, previous = dijkstra(graph, 'A')
    
    assert distances['A'] == 0
    assert previous['A'] is None

def test_reconstruct_path_same_node():
    # Reconstruction when start and end are the same
    previous = {'A': None, 'B': 'A', 'C': 'B'}
    path = reconstruct_path(previous, 'A', 'A')
    assert path == ['A']

def test_dijkstra_error_handling():
    # Ensure it handles invalid inputs
    with pytest.raises(KeyError):
        graph = {'A': {'B': 1}}
        dijkstra(graph, 'C')  # Start node not in graph
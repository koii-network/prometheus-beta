import pytest
from src.dijkstra import dijkstra, reconstruct_path

def test_dijkstra_simple_graph():
    # Simple graph with known shortest paths
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    
    # Test distances from node A
    distances, previous = dijkstra(graph, 'A')
    
    # Expected distances
    expected_distances = {
        'A': 0,
        'B': 3,  # A -> C -> B
        'C': 2,  # A -> C
        'D': 6   # A -> C -> B -> D
    }
    
    assert distances == expected_distances

def test_dijkstra_path_reconstruction():
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    
    # Calculate shortest paths from A
    distances, previous = dijkstra(graph, 'A')
    
    # Reconstruct path from A to D
    path = reconstruct_path(previous, 'A', 'D')
    
    # Expected path should be A -> C -> B -> D
    assert path == ['A', 'C', 'B', 'D']

def test_dijkstra_single_node_graph():
    graph = {
        'A': {}
    }
    
    # Test with single node graph
    distances, previous = dijkstra(graph, 'A')
    assert distances == {'A': 0}
    assert previous == {'A': None}

def test_dijkstra_disconnected_node():
    graph = {
        'A': {'B': 4},
        'B': {'A': 4},
        'C': {}  # Disconnected node
    }
    
    # Calculate shortest paths from A
    distances, previous = dijkstra(graph, 'A')
    
    # Verify distances
    assert distances['A'] == 0
    assert distances['B'] == 4
    assert distances['C'] == float('inf')

def test_dijkstra_negative_input():
    with pytest.raises(TypeError):
        dijkstra(None, 'A')
    
    with pytest.raises(KeyError):
        dijkstra({'A': {}}, 'B')  # Start node not in graph
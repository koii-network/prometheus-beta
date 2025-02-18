import pytest
from src.dijkstra_shortest_path import dijkstra_shortest_path, reconstruct_path

def test_dijkstra_basic_graph():
    # Simple graph with known shortest paths
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3},
        'C': {'B': 1, 'D': 5},
        'D': {}
    }
    
    # Test from start node A
    distances, previous = dijkstra_shortest_path(graph, 'A')
    
    # Expected distances
    assert distances == {
        'A': 0,
        'B': 3,  # A -> C -> B
        'C': 2,  # A -> C
        'D': 6   # A -> C -> B -> D
    }

def test_dijkstra_single_node_graph():
    # Graph with only one node
    graph = {'A': {}}
    
    distances, previous = dijkstra_shortest_path(graph, 'A')
    
    assert distances == {'A': 0}
    assert previous == {'A': None}

def test_dijkstra_disconnected_node():
    # Graph with a disconnected node
    graph = {
        'A': {'B': 1},
        'B': {'A': 1},
        'C': {}
    }
    
    distances, previous = dijkstra_shortest_path(graph, 'A')
    
    assert distances['C'] == float('inf')

def test_dijkstra_invalid_start_node():
    # Graph without the start node
    graph = {
        'A': {'B': 1},
        'B': {'A': 1}
    }
    
    with pytest.raises(ValueError, match="Start node X not found in graph"):
        dijkstra_shortest_path(graph, 'X')

def test_reconstruct_path():
    # Previous nodes from a sample Dijkstra run
    previous_nodes = {
        'A': None,
        'B': 'A',
        'C': 'A',
        'D': 'B'
    }
    
    # Test path reconstruction
    path = reconstruct_path(previous_nodes, 'A', 'D')
    assert path == ['A', 'B', 'D']

def test_reconstruct_path_same_start_end():
    # Path with start and end being the same node
    previous_nodes = {
        'A': None
    }
    
    path = reconstruct_path(previous_nodes, 'A', 'A')
    assert path == ['A']

def test_reconstruct_path_no_path():
    # No path between nodes
    previous_nodes = {
        'A': None,
        'B': None,
        'C': 'B'
    }
    
    with pytest.raises(ValueError, match="No path exists between A and C"):
        reconstruct_path(previous_nodes, 'A', 'C')
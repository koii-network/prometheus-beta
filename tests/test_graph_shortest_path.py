import pytest
from src.graph_shortest_path import find_shortest_path

def test_basic_path():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    # Direct connection
    assert find_shortest_path(graph, 'A', 'B') == ['A', 'B']
    
    # Path with multiple hops
    assert find_shortest_path(graph, 'A', 'F') == ['A', 'C', 'F']

def test_same_node():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    
    # Same start and end node should return single-node path
    assert find_shortest_path(graph, 'A', 'A') == ['A']

def test_no_path():
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    
    # No path between disconnected nodes
    assert find_shortest_path(graph, 'A', 'C') is None

def test_invalid_nodes():
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    
    # Raise error for non-existent start node
    with pytest.raises(ValueError, match="Start node X not found in graph"):
        find_shortest_path(graph, 'X', 'A')
    
    # Raise error for non-existent end node
    with pytest.raises(ValueError, match="End node Y not found in graph"):
        find_shortest_path(graph, 'A', 'Y')

def test_complex_path():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B', 'G'],
        'E': ['B', 'F'],
        'F': ['C', 'E', 'G'],
        'G': ['D', 'F']
    }
    
    # Longer path with multiple routing options
    path = find_shortest_path(graph, 'A', 'G')
    assert path in [
        ['A', 'B', 'D', 'G'],
        ['A', 'C', 'F', 'G']
    ]
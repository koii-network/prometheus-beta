import pytest
from src.graph_shortest_path import find_shortest_path

def test_basic_shortest_path():
    """Test finding a simple shortest path in a graph"""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    path = find_shortest_path(graph, 'A', 'F')
    assert path == ['A', 'C', 'F'] or path == ['A', 'B', 'E', 'F']

def test_same_start_end_node():
    """Test when start and end nodes are the same"""
    graph = {
        'A': ['B', 'C'],
        'B': ['A'],
        'C': ['A']
    }
    path = find_shortest_path(graph, 'A', 'A')
    assert path == ['A']

def test_no_path_exists():
    """Test when no path exists between nodes"""
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    path = find_shortest_path(graph, 'A', 'C')
    assert path is None

def test_node_not_in_graph():
    """Test raising ValueError when nodes are not in graph"""
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    with pytest.raises(ValueError, match="Start or end node not found in the graph"):
        find_shortest_path(graph, 'A', 'X')
    
    with pytest.raises(ValueError, match="Start or end node not found in the graph"):
        find_shortest_path(graph, 'X', 'B')

def test_complex_graph_path():
    """Test finding path in a more complex graph"""
    graph = {
        1: [2, 3],
        2: [1, 4, 5],
        3: [1, 6],
        4: [2],
        5: [2, 6],
        6: [3, 5]
    }
    path = find_shortest_path(graph, 1, 6)
    assert path == [1, 3, 6] or path == [1, 2, 5, 6]

def test_disconnected_nodes():
    """Test scenario with completely disconnected nodes"""
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    path = find_shortest_path(graph, 'A', 'C')
    assert path is None
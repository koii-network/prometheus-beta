import pytest
from src.graph_shortest_path import bfs_shortest_path

def test_basic_path():
    """Test finding a basic path in a simple graph"""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    path = bfs_shortest_path(graph, 'A', 'F')
    assert path in [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

def test_same_start_end():
    """Test when start and end nodes are the same"""
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    path = bfs_shortest_path(graph, 'A', 'A')
    assert path == ['A']

def test_no_path():
    """Test when no path exists between nodes"""
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    path = bfs_shortest_path(graph, 'A', 'C')
    assert path is None

def test_start_node_not_in_graph():
    """Test error when start node is not in graph"""
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    with pytest.raises(ValueError, match="Start node X not in graph"):
        bfs_shortest_path(graph, 'X', 'A')

def test_end_node_not_in_graph():
    """Test error when end node is not in graph"""
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    with pytest.raises(ValueError, match="End node X not in graph"):
        bfs_shortest_path(graph, 'A', 'X')

def test_numeric_graph():
    """Test graph with numeric nodes"""
    graph = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 5],
        4: [2],
        5: [3]
    }
    path = bfs_shortest_path(graph, 1, 4)
    assert path == [1, 2, 4]

def test_long_path():
    """Test finding a path in a larger graph"""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B', 'F'],
        'E': ['C', 'G'],
        'F': ['D', 'G'],
        'G': ['E', 'F']
    }
    path = bfs_shortest_path(graph, 'A', 'G')
    # Multiple valid shortest paths possible
    assert path in [
        ['A', 'C', 'E', 'G'], 
        ['A', 'B', 'D', 'F', 'G']
    ]
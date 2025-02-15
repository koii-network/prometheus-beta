import pytest
from src.bfs import breadth_first_search

def test_bfs_basic_graph():
    """Test BFS on a simple graph."""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B', 'C', 'D', 'E', 'F']

def test_bfs_single_node_graph():
    """Test BFS on a graph with a single node."""
    graph = {'X': []}
    result = breadth_first_search(graph, 'X')
    assert result == ['X']

def test_bfs_disconnected_graph():
    """Test BFS on a disconnected graph starting from a node."""
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B']

def test_bfs_invalid_start_node():
    """Test BFS with a start node not in the graph."""
    graph = {'A': ['B'], 'B': ['A']}
    with pytest.raises(ValueError, match="Start node Z not found in the graph"):
        breadth_first_search(graph, 'Z')

def test_bfs_empty_graph():
    """Test BFS on an empty graph."""
    graph = {}
    with pytest.raises(ValueError, match="Start node X not found in the graph"):
        breadth_first_search(graph, 'X')
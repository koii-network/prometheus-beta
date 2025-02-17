import pytest
from src.depth_first_search import depth_first_search

def test_simple_graph():
    """Test DFS on a simple graph."""
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    result = depth_first_search(graph, 'A')
    assert result == ['A', 'B', 'D', 'C', 'E', 'F']

def test_linear_graph():
    """Test DFS on a linear graph."""
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['D'],
        'D': []
    }
    
    result = depth_first_search(graph, 'A')
    assert result == ['A', 'B', 'C', 'D']

def test_disconnected_graph():
    """Test DFS starting from a node in a disconnected graph."""
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C'],
        'E': []
    }
    
    result = depth_first_search(graph, 'A')
    assert result == ['A', 'B']

def test_node_not_in_graph():
    """Test that a ValueError is raised when start node is not in graph."""
    graph = {
        'A': ['B'],
        'B': ['C'],
        'C': []
    }
    
    with pytest.raises(ValueError, match="Start node X not found in graph"):
        depth_first_search(graph, 'X')

def test_empty_graph():
    """Test DFS on an empty graph raises a ValueError."""
    graph = {}
    
    with pytest.raises(ValueError, match="Start node A not found in graph"):
        depth_first_search(graph, 'A')

def test_graph_with_cycles():
    """Test DFS on a graph with cycles."""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['C']
    }
    
    result = depth_first_search(graph, 'A')
    assert result == ['A', 'B', 'D', 'C', 'E']
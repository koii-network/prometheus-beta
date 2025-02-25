import pytest
from src.depth_first_search import depth_first_search

def test_dfs_basic_graph():
    """
    Test DFS on a simple graph with multiple connections.
    """
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    result = depth_first_search(graph, 'A')
    assert result == ['A', 'B', 'D', 'E', 'F', 'C']

def test_dfs_single_node_graph():
    """
    Test DFS on a graph with only one node.
    """
    graph = {
        'X': []
    }
    
    result = depth_first_search(graph, 'X')
    assert result == ['X']

def test_dfs_disconnected_graph():
    """
    Test DFS on a graph with disconnected components.
    """
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    
    result = depth_first_search(graph, 'A')
    assert result == ['A', 'B']

def test_dfs_error_on_missing_start_node():
    """
    Test that a ValueError is raised when the start node is not in the graph.
    """
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    
    with pytest.raises(ValueError, match="Start node Z not found in the graph"):
        depth_first_search(graph, 'Z')

def test_dfs_cyclic_graph():
    """
    Test DFS on a graph with cycles.
    """
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E'],
        'D': ['B'],
        'E': ['C']
    }
    
    result = depth_first_search(graph, 'A')
    assert len(result) == len(set(result))  # All nodes visited only once
    assert set(result) == set(graph.keys())
    assert result[0] == 'A'  # Starts from the given start node
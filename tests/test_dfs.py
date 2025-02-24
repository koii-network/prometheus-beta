import pytest
from src.dfs import depth_first_search

def test_dfs_basic_graph():
    """
    Test DFS on a basic graph with multiple nodes.
    """
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    # DFS starting from 'A'
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
    Test DFS on a disconnected graph.
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
    Test that an error is raised when the start node is not in the graph.
    """
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    
    with pytest.raises(ValueError, match="Start node Z not found in graph"):
        depth_first_search(graph, 'Z')

def test_dfs_complex_graph():
    """
    Test DFS on a more complex graph structure.
    """
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6],
        4: [],
        5: [6],
        6: []
    }
    
    result = depth_first_search(graph, 1)
    assert result == [1, 2, 4, 5, 6, 3]
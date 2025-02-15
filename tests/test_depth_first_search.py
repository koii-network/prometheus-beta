import pytest
from src.depth_first_search import depth_first_search

def test_basic_graph_dfs():
    """
    Test DFS on a basic graph
    """
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    # Validate DFS starting from 'A'
    result = depth_first_search(graph, 'A')
    assert result == ['A', 'B', 'D', 'E', 'F', 'C']

def test_single_node_graph():
    """
    Test DFS on a graph with a single node
    """
    graph = {'X': []}
    
    result = depth_first_search(graph, 'X')
    assert result == ['X']

def test_disconnected_graph():
    """
    Test DFS on a graph with disconnected components
    """
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    
    result = depth_first_search(graph, 'A')
    assert result == ['A', 'B']

def test_error_on_nonexistent_start_node():
    """
    Test that a ValueError is raised when start node is not in graph
    """
    graph = {'A': ['B'], 'B': []}
    
    with pytest.raises(ValueError, match="Start node Z not found in the graph"):
        depth_first_search(graph, 'Z')

def test_empty_graph():
    """
    Test behavior with an empty graph
    """
    graph = {}
    
    with pytest.raises(ValueError, match="Start node X not found in the graph"):
        depth_first_search(graph, 'X')
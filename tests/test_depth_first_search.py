import pytest
from src.depth_first_search import depth_first_search

def test_dfs_basic_graph():
    """
    Test DFS on a basic graph
    """
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    result = depth_first_search(graph, 'A')
    
    # Verify the first node is the start node
    assert result[0] == 'A'
    
    # Verify all nodes are visited
    assert set(result) == set(graph.keys())

def test_dfs_empty_graph():
    """
    Test DFS on an empty graph
    """
    graph = {}
    
    result = depth_first_search(graph, 'A')
    
    assert result == []

def test_dfs_start_node_not_in_graph():
    """
    Test DFS when start node is not in the graph
    """
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    
    result = depth_first_search(graph, 'C')
    
    assert result == []

def test_dfs_single_node_graph():
    """
    Test DFS on a graph with a single node
    """
    graph = {
        'A': []
    }
    
    result = depth_first_search(graph, 'A')
    
    assert result == ['A']

def test_dfs_disconnected_graph():
    """
    Test DFS on a disconnected graph
    """
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    
    result = depth_first_search(graph, 'A')
    
    # Verify A and B are visited
    assert set(result) == {'A', 'B'}
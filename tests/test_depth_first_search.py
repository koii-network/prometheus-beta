import pytest
from src.depth_first_search import depth_first_search

def test_basic_graph_dfs():
    """
    Test DFS on a basic graph with multiple nodes and connections.
    """
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    # Test starting from different nodes
    assert depth_first_search(graph, 'A') == ['A', 'B', 'D', 'E', 'F', 'C']
    assert depth_first_search(graph, 'B') == ['B', 'D', 'E', 'F']

def test_single_node_graph():
    """
    Test DFS on a graph with only one node.
    """
    graph = {'X': []}
    assert depth_first_search(graph, 'X') == ['X']

def test_disconnected_graph():
    """
    Test DFS on a disconnected graph.
    """
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C'],
        'E': []
    }
    
    # Verify the traversal starts from the specified node
    assert depth_first_search(graph, 'A') == ['A', 'B']
    assert depth_first_search(graph, 'C') == ['C', 'D']
    assert depth_first_search(graph, 'E') == ['E']

def test_error_handling():
    """
    Test error handling when the start node is not in the graph.
    """
    graph = {'A': ['B'], 'B': ['C']}
    
    with pytest.raises(ValueError, match="Start node X not found in the graph"):
        depth_first_search(graph, 'X')

def test_cyclic_graph():
    """
    Test DFS on a graph with cycles.
    """
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C']
    }
    
    # Ensure each node is visited only once
    result = depth_first_search(graph, 'A')
    assert len(result) == len(set(result))
    assert set(result) == set(['A', 'B', 'C', 'D'])
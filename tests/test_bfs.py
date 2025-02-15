import pytest
from src.bfs import breadth_first_search

def test_bfs_basic_graph():
    """Test BFS on a simple graph"""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    # Check that the traversal starts from the correct node
    result = breadth_first_search(graph, 'A')
    assert result[0] == 'A', "BFS should start from the start node"
    
    # Verify that all nodes are visited
    assert set(result) == set(graph.keys()), "BFS should visit all nodes"

def test_bfs_single_node_graph():
    """Test BFS on a graph with a single node"""
    graph = {'X': []}
    
    result = breadth_first_search(graph, 'X')
    assert result == ['X'], "BFS should work with a single node graph"

def test_bfs_disconnected_graph():
    """Test BFS on a graph where the start node has no connections"""
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': [],
        'D': []
    }
    
    result = breadth_first_search(graph, 'C')
    assert result == ['C'], "BFS should work with disconnected nodes"

def test_bfs_invalid_start_node():
    """Test that an error is raised when the start node is not in the graph"""
    graph = {'A': ['B'], 'B': ['A']}
    
    with pytest.raises(ValueError, match="Start node Z not found in graph"):
        breadth_first_search(graph, 'Z')

def test_bfs_node_traversal_order():
    """Test the order of node traversal"""
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }
    
    result = breadth_first_search(graph, 'A')
    
    # Verify the order of traversal
    assert result[0] == 'A'
    assert set(result[1:3]) == {'B', 'C'}
    assert set(result[3:]) == {'D', 'E', 'F'}
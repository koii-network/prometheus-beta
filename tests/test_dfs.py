import pytest
from src.dfs import depth_first_search

def test_basic_dfs():
    """Test basic DFS traversal on a simple graph."""
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

def test_dfs_with_visit_func():
    """Test DFS with a visit function."""
    visited_nodes = []
    def visit_tracker(node):
        visited_nodes.append(node)
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': []
    }
    
    depth_first_search(graph, 'A', visit_func=visit_tracker)
    assert visited_nodes == ['A', 'B', 'D', 'C', 'E']

def test_dfs_single_node():
    """Test DFS on a graph with a single node."""
    graph = {
        'A': []
    }
    
    result = depth_first_search(graph, 'A')
    assert result == ['A']

def test_dfs_invalid_start_node():
    """Test DFS with a start node not in the graph."""
    graph = {
        'A': ['B'],
        'B': []
    }
    
    with pytest.raises(ValueError, match="Start node X not found in graph"):
        depth_first_search(graph, 'X')

def test_dfs_invalid_graph():
    """Test DFS with an invalid graph input."""
    with pytest.raises(TypeError, match="Graph must be a dictionary"):
        depth_first_search([1, 2, 3], 1)

def test_dfs_cyclic_graph():
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
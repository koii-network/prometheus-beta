import pytest
from src.bfs import breadth_first_search

def test_basic_bfs():
    # Simple graph with known BFS traversal order
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    # Test starting from different nodes
    assert breadth_first_search(graph, 'A') == ['A', 'B', 'C', 'D', 'E', 'F']
    assert breadth_first_search(graph, 'B') == ['B', 'A', 'D', 'E', 'C', 'F']

def test_single_node_graph():
    # Graph with only one node
    graph = {'X': []}
    assert breadth_first_search(graph, 'X') == ['X']

def test_disconnected_graph():
    # Graph with disconnected components
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    
    result_a = breadth_first_search(graph, 'A')
    result_c = breadth_first_search(graph, 'C')
    
    assert result_a == ['A', 'B']
    assert result_c == ['C', 'D']

def test_error_handling():
    # Test invalid inputs
    with pytest.raises(TypeError, match="Graph must be a dictionary"):
        breadth_first_search(None, 'A')
    
    with pytest.raises(TypeError, match="Start node cannot be None"):
        breadth_first_search({}, None)
    
    with pytest.raises(ValueError, match="Start node X not found in graph"):
        breadth_first_search({'A': ['B']}, 'X')

def test_empty_graph():
    # Empty graph
    with pytest.raises(ValueError):
        breadth_first_search({}, 'A')

def test_nodes_with_no_neighbors():
    # Graph with some nodes having no neighbors
    graph = {
        'A': ['B', 'C'],
        'B': [],
        'C': ['A'],
        'D': []
    }
    
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B', 'C']
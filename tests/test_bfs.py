import pytest
from src.bfs import breadth_first_search

def test_bfs_basic_graph():
    # Basic graph with integer nodes
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6],
        4: [],
        5: [7],
        6: [],
        7: []
    }
    
    # Test from node 1
    result = breadth_first_search(graph, 1)
    assert result == [1, 2, 3, 4, 5, 6, 7]

def test_bfs_single_node_graph():
    # Graph with only one node
    graph = {
        'A': []
    }
    
    result = breadth_first_search(graph, 'A')
    assert result == ['A']

def test_bfs_disconnected_graph():
    # Graph with disconnected nodes
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [3],
        5: []
    }
    
    # Test starting from different nodes
    result1 = breadth_first_search(graph, 1)
    assert result1 == [1, 2]
    
    result2 = breadth_first_search(graph, 3)
    assert result2 == [3, 4]

def test_bfs_error_handling():
    # Graph for error testing
    graph = {
        1: [2, 3],
        2: [4],
        3: []
    }
    
    # Test error when start node is not in graph
    with pytest.raises(ValueError, match="Start node 10 not found in the graph"):
        breadth_first_search(graph, 10)

def test_bfs_complex_graph():
    # More complex graph with mixed types
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['G'],
        'F': [],
        'G': []
    }
    
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B', 'C', 'D', 'E', 'F', 'G']
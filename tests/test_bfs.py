import pytest
from src.bfs import breadth_first_search

def test_bfs_basic_graph():
    # Simple graph with known expected traversal
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    # BFS from node 'A'
    result = breadth_first_search(graph, 'A')
    expected = ['A', 'B', 'C', 'D', 'E', 'F']
    assert result == expected

def test_bfs_single_node_graph():
    # Graph with only one node
    graph = {'X': []}
    result = breadth_first_search(graph, 'X')
    assert result == ['X']

def test_bfs_disconnected_graph():
    # Graph with disconnected components
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B']

def test_bfs_invalid_start_node():
    # Graph with invalid start node
    graph = {'A': ['B'], 'B': ['A']}
    with pytest.raises(ValueError, match="Start node Z not found in graph"):
        breadth_first_search(graph, 'Z')

def test_bfs_complex_graph():
    # More complex graph structure
    graph = {
        1: [2, 3],
        2: [4, 5],
        3: [6],
        4: [],
        5: [6],
        6: []
    }
    
    result = breadth_first_search(graph, 1)
    expected = [1, 2, 3, 4, 5, 6]
    assert result == expected
import pytest
from src.bfs import breadth_first_search

def test_bfs_basic_graph():
    # Basic graph example
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    # Test BFS starting from 'A'
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B', 'C', 'D', 'E', 'F']

def test_bfs_single_node_graph():
    # Graph with a single node
    graph = {
        'X': []
    }
    
    # Test BFS on single node graph
    result = breadth_first_search(graph, 'X')
    assert result == ['X']

def test_bfs_disconnected_graph():
    # Disconnected graph
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    
    # Test BFS starting from 'A'
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B']

def test_bfs_non_existent_start_node():
    # Graph with no start node
    graph = {
        'A': ['B'],
        'B': ['A']
    }
    
    # Test that ValueError is raised for non-existent start node
    with pytest.raises(ValueError, match="Start node Z not found in the graph"):
        breadth_first_search(graph, 'Z')

def test_bfs_complex_graph():
    # More complex graph
    graph = {
        1: [2, 3],
        2: [1, 4, 5],
        3: [1, 6],
        4: [2],
        5: [2, 6],
        6: [3, 5]
    }
    
    # Test BFS starting from node 1
    result = breadth_first_search(graph, 1)
    assert result == [1, 2, 3, 4, 5, 6]
import pytest
from src.bfs import breadth_first_search

def test_bfs_simple_graph():
    # Simple graph with known traversal order
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B', 'C', 'D', 'E', 'F']

def test_bfs_single_node_graph():
    # Graph with only one node
    graph = {'X': []}
    result = breadth_first_search(graph, 'X')
    assert result == ['X']

def test_bfs_disconnected_graph():
    # Graph with disconnected components
    graph = {
        '1': ['2', '3'],
        '2': ['1'],
        '3': ['1'],
        '4': ['5'],
        '5': ['4']
    }
    result = breadth_first_search(graph, '1')
    assert result == ['1', '2', '3']

def test_bfs_invalid_start_node():
    # Test invalid start node
    graph = {'A': ['B'], 'B': ['A']}
    with pytest.raises(ValueError, match="Start node C not found in the graph"):
        breadth_first_search(graph, 'C')

def test_bfs_with_cycles():
    # Graph with cycles
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C']
    }
    result = breadth_first_search(graph, 'A')
    assert result == ['A', 'B', 'C', 'D']